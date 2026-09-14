"""Terminal telemetry first; compact read-only copy/identity custody only."""
from pathlib import Path
import hashlib,json,os,time
W=Path('/home/ubuntu/d125-hybrid-affine-pilot-20260907');E=W/'engineering'
def need(ok,msg):
    if not ok:raise ValueError(msg)
boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip();need(boot=='bef732b9-38e5-4a9a-8f93-77203426d2b8','boot')
telemetry={label:json.loads((E/(label+'.telemetry.json')).read_bytes()) for label in ('authorize','rss')}
need(telemetry['authorize']['status']=='NORMAL_EXIT' and telemetry['authorize']['child_returncode']==0,'authorize terminal')
need(telemetry['rss']['status']=='RESOURCE_CAP' and telemetry['rss']['resource']=='rss','RSS terminal')
batch=json.loads((E/'batch-result.json').read_bytes());need(batch['status']=='ENGINEERING_ONLY_PASS','batch incomplete')
ids=set();groups=set()
for label,t in telemetry.items():
    launch=json.loads((E/(label+'.launch.json')).read_bytes())
    for ident in (launch['controller'],launch['runner']):ids.add(ident['pid']);groups.add(ident['pgid'])
    ids.add(t['pid']);groups.add(t['pgid'])
desc=json.loads((E/'rss-descendant.identity.json').read_bytes());ids.add(desc['pid']);groups.add(desc['pgid'])
members=[]
for p in Path('/proc').iterdir():
    if not p.name.isdigit():continue
    try:s=(p/'stat').read_text().rsplit(') ',1)[1].split()
    except (FileNotFoundError,ProcessLookupError):continue
    if int(s[2]) in groups:members.append(int(p.name))
need(not members and not any(Path('/proc',str(p)).exists() for p in ids),'engineering identity/group still present')
files={}
for p in sorted(E.iterdir()):
    need(p.is_file(),'unexpected engineering subdir')
    b=p.read_bytes();need(len(b)<1024**2,'compact artifact cap')
    files[str(p.relative_to(W))]=dict(sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),text=b.decode() if p.suffix!='.py' else None)
for name in ('authority.json','ROOT-GREEN.md','REGISTRATION.md'):
    b=(W/name).read_bytes();files[name]=dict(sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),text=b.decode())
pins={n:hashlib.sha256((W/n).read_bytes()).hexdigest() for n in ('construct.py','replay.py','baseline.py','run_capped.py')}
need(not os.path.lexists(W/'construction.jsonl') and not os.path.lexists(W/'replay-result.json'),'production output appeared')
print(json.dumps(dict(status='ENGINEERING_TERMINAL_CUSTODY',utc=time.time(),boot=boot,ids_absent=sorted(ids),groups_absent=sorted(groups),files=files,payload_pins=pins,production_outputs_absent=True,source_access=False),sort_keys=True))
