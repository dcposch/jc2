"""Read-only terminal collection; no reconstruction, CAS or source-row replay."""
from pathlib import Path
from collections import Counter
import hashlib,json,os,platform,subprocess,time
W=Path('/home/ubuntu/d125-hybrid-affine-pilot-20260907')
SOURCE=Path('/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational.jsonl')
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024**2),b''):h.update(b)
    return h.hexdigest()
def strict(b):
    def pairs(xs):
        d={}
        for k,v in xs:need(k not in d,'duplicate key');d[k]=v
        return d
    return json.loads(b,object_pairs_hook=pairs)
boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip()
need(platform.system()=='Linux' and Path('/sys/class/dmi/id/sys_vendor').read_text().strip()=='Amazon EC2' and Path('/sys/class/dmi/id/board_asset_tag').read_text().strip()=='i-0da0cebfc97c9fd54' and boot=='bef732b9-38e5-4a9a-8f93-77203426d2b8','host/boot')
t=strict((W/'pilot.telemetry.json').read_bytes())
need(t['status']=='NORMAL_EXIT' and t['child_returncode']==0 and t['runner_exit_code']==0 and t['error'] is None,'terminal telemetry')
receipt=strict((W/'production.receipt.json').read_bytes());launch=strict((W/'production.launch.json').read_bytes())
ids={launch[k]['pid'] for k in ('controller','runner','payload')};groups={launch[k]['pgid'] for k in ('controller','runner','payload')}
members=[]
for p in Path('/proc').iterdir():
    if not p.name.isdigit():continue
    try:s=(p/'stat').read_text().rsplit(') ',1)[1].split()
    except (FileNotFoundError,ProcessLookupError):continue
    if int(s[2]) in groups:members.append(int(p.name))
need(not members and all(not Path('/proc',str(i)).exists() for i in ids),'live owned identities')
files={}
for name in ('pilot.telemetry.json','production.receipt.json','production.launch.json','production.claim.json','pilot.stdout','pilot.stderr','replay-result.json','authority.json','ROOT-GREEN.md','REGISTRATION.md','engineering/rss.authority.json','engineering/ROOT-GREEN.md'):
    b=(W/name).read_bytes();need(len(b)<1024**2,'compact file size')
    files[name]=dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),text=b.decode())
stages=[strict(line) for line in (W/'pilot.stderr').read_bytes().splitlines()]
need(all(r.get('type')=='stage' and 'error' not in r for r in stages),'nonstage stderr/traceback')
replay=strict((W/'replay-result.json').read_bytes())
need(replay['status']=='ALL_803_ORIGINAL_ROWS_COVER_TRANSPORTED' and strict((W/'pilot.stdout').read_bytes())==replay,'replay result/status')
h=hashlib.sha256();counts=Counter();row_groups={};header=footer=None;row_count=terms=zeros=maps=0;guard_degrees={};max_degree=0
with (W/'construction.jsonl').open('rb') as f:
    for line in f:
        r=strict(line);need(json.dumps(r,sort_keys=True,separators=(',',':')).encode()+b'\n'==line,'noncanonical stream')
        need(footer is None,'record after footer');kind=r['type'];counts[kind]+=1
        if kind=='footer':
            need(r['prefix_sha256']==h.hexdigest(),'prefix hash');footer=r;continue
        h.update(line)
        if kind=='header':header=r
        if kind=='coefficient_map':maps+=len(r['terms'])
        if kind=='row':
            need(r['original_index']==(row_count if row_count<803 else None),'row index');row_count+=1
            label=r['label'];group=label.split('/')[0];g=row_groups.setdefault(group,dict(rows=0,nonzero=0,terms=0,max_degree=0))
            degree=max((len(m) for c,m in r['terms']),default=0)
            g['rows']+=1;g['nonzero']+=bool(r['terms']);g['terms']+=len(r['terms']);g['max_degree']=max(g['max_degree'],degree)
            terms+=len(r['terms']);zeros+=row_count<=803 and not r['terms'];max_degree=max(max_degree,degree)
            if group in ('GUARD','UNIT') and r['terms']:guard_degrees[label]=degree
need(counts['header']==counts['footer']==1 and row_count==804 and footer['complete'] is True,'completion')
need((footer['rows'],footer['terms'],footer['zero_original_rows'],footer['coefficient_map_terms'])==(row_count,terms,zeros,maps),'footer counts')
need(len(header['variables'])==81 and len(header['original_variables'])==269,'variable counts')
need(all(replay[k]==footer[k] for k in ('rows','original_rows','terms','zero_original_rows')),'replay/footer discrepancy')
for name in ('construction.jsonl','replay-result.json','pilot.stdout','pilot.stderr'):
    need(sha(W/name)==receipt['files'][name]['sha256'] and (W/name).stat().st_size==receipt['files'][name]['bytes'],'receipt file drift')
pins={n:sha(W/n) for n in ('construct.py','replay.py','baseline.py','run_capped.py')}
need(all(pins[n]==v for n,v in receipt['post_pins'].items()),'payload drift')
source_sha=sha(SOURCE);need(source_sha==receipt['source_post_sha256']==header['source_sha256'],'source drift')
summary=dict(header=header,footer=footer,record_counts=dict(counts),row_groups=row_groups,guard_degrees=guard_degrees,max_row_degree=max_degree,canonical_prefix_verified=True,stage_counts=dict(Counter(r['stage'] for r in stages)),all_stderr_json_stages=True)
print(json.dumps(dict(status='PRODUCTION_TERMINAL_CUSTODY',utc=time.time(),hostname=platform.node(),boot=boot,instance='i-0da0cebfc97c9fd54',owner='coordinator-factored-jacobian-20260906',cwd=str(W),ids_absent=sorted(ids),groups_absent=sorted(groups),files=files,construction=dict(path=str(W/'construction.jsonl'),bytes=(W/'construction.jsonl').stat().st_size,sha256=sha(W/'construction.jsonl')),source=dict(path=str(SOURCE),bytes=SOURCE.stat().st_size,sha256=source_sha),payload_pins=pins,summary=summary,memory=subprocess.check_output(['free','-m'],text=True),disk=subprocess.check_output(['df','-Pk',str(W)],text=True),mount=subprocess.check_output(['findmnt','-n','-o','SOURCE,FSTYPE,TARGET','/'],text=True),ebs_serial=subprocess.check_output(['lsblk','-dn','-o','SERIAL','/dev/nvme0n1'],text=True).strip(),source_rows_replayed_again=False),sort_keys=True))
