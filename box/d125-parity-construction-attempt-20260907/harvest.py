"""Terminal receipt/hash/footer custody only; no reconstruction or row replay."""
import datetime,hashlib,json,os,resource,subprocess,time
from pathlib import Path
W=Path('/home/ubuntu/d125-parity-compression-pilot-20260907')
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2));resource.setrlimit(resource.RLIMIT_CPU,(25,25))
def need(ok,msg):
    if not ok:raise ValueError(msg)
def read(p):return json.loads(p.read_bytes())
def fileinfo(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
    return dict(bytes=p.stat().st_size,sha256=h.hexdigest())
terminal=read(W/'pilot-runner.result.json');telemetry=read(W/'pilot.telemetry.json')
launch=read(W/'pilot.launch.json');payload=read(W/'pilot.payload-identity.json')['payload']
ids=[launch['controller']['pid'],launch['runner']['pid'],telemetry['pid']]
groups=[launch['controller']['pgid'],launch['runner']['pgid'],telemetry['pgid']]
members=[]
for p in Path('/proc').iterdir():
    if not p.name.isdigit():continue
    try:s=(p/'stat').read_text().rsplit(') ',1)[1].split()
    except (FileNotFoundError,ProcessLookupError):continue
    if int(p.name) in ids or int(s[2]) in groups:members.append(dict(pid=int(p.name),pgid=int(s[2]),state=s[0]))
need(not members,'task group remains')
need(Path('/proc/sys/kernel/random/boot_id').read_text().strip()==launch['runner']['boot'],'boot changed')
names=['authority.json','REGISTRATION.md','pilot-pre.json','pilot.launch.json','pilot.payload-identity.json',
       'pilot.stdout','pilot.stderr','pilot.telemetry.json','pilot-runner.stdout','pilot-runner.stderr',
       'pilot-runner.result.json','construction.jsonl','replay-result.json']
files={name:fileinfo(W/name) for name in names if (W/name).is_file()}
construction=W/'construction.jsonl';framing=dict(footer=None,complete=False)
if construction.exists() and construction.stat().st_size:
    # Read only a bounded terminal footer and hash its preceding byte stream.
    with construction.open('rb') as f:
        size=construction.stat().st_size;f.seek(max(0,size-65536));tail=f.read()
    final=tail.rstrip(b'\n').rsplit(b'\n',1)[-1]
    if len(final)<32768:
        try:footer=json.loads(final)
        except (ValueError,UnicodeDecodeError):footer=None
        if isinstance(footer,dict) and footer.get('type')=='footer':
            need(tail.endswith(b'\n'),'footer newline missing')
            prefix_bytes=size-len(final)-1;h=hashlib.sha256()
            with construction.open('rb') as f:
                remaining=prefix_bytes
                while remaining:
                    block=f.read(min(1024*1024,remaining));need(bool(block),'short prefix');h.update(block);remaining-=len(block)
            framing=dict(footer=footer,complete=footer.get('complete') is True,
                         prefix_hash_matches=h.hexdigest()==footer.get('prefix_sha256'))
receipt=None
if (W/'replay-result.json').exists() and (W/'replay-result.json').stat().st_size:
    need((W/'replay-result.json').stat().st_size<1024*1024,'unexpected receipt size')
    receipt=read(W/'replay-result.json')
source=Path('/home/ubuntu/d125-small-source-construction-pilot-20260906/unequal-rational/client-unequal-rational.jsonl')
source_info=fileinfo(source)
need(source_info['sha256']=='b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac','source posthash drift')
code={name:fileinfo(W/name) for name in ['construct.py','replay.py','baseline.py','qpoly.py','run_once.py','run_capped.py']}
good=(terminal['runner_rc']==0 and telemetry['status']=='NORMAL_EXIT' and telemetry['child_returncode']==0
      and (W/'pilot.stderr').read_bytes()==b'' and framing['complete'] and framing.get('prefix_hash_matches')
      and receipt is not None and receipt.get('status')=='ALL_ORIGINAL_ROWS_TRANSPORTED' and receipt.get('rows')==803)
out=dict(status='CONSTRUCTED_AND_REPLAYED_NO_IDEAL_DECISION' if good else 'INCONCLUSIVE',
         utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),terminal=terminal,telemetry=telemetry,
         files=files,framing=framing,replay_receipt=receipt,post_code=code,source_posthash=source_info,
         ids=ids,groups=groups,remaining=members,extra_reconstruction_or_replay=False,
         memory=subprocess.check_output(['free','-m'],text=True),disk=subprocess.check_output(['df','-Pk',str(W)],text=True))
print(json.dumps(out,sort_keys=True))
