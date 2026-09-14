"""Read-only final machine/group/output custody; never opens a source input."""
import hashlib,json,os,subprocess,time
from pathlib import Path
W=Path('/home/ubuntu/d125-parity-compression-pilot-20260907');E=W/'engineering'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
batch=json.loads((E/'batch-pre.json').read_bytes())
ids=[batch['controller']['pid']];groups=[batch['controller']['pgid']]
for label in ('authorize','rss'):
    launch=json.loads((E/(label+'.launch.json')).read_bytes())
    t=json.loads((E/(label+'.telemetry.json')).read_bytes())
    ids += [launch['runner_identity']['pid'],t['pid']]
    groups += [launch['runner_identity']['pgid'],t['pgid']]
ids.append(json.loads((E/'rss-descendant.identity.json').read_bytes())['pid'])
members=[]
for p in Path('/proc').iterdir():
    if not p.name.isdigit():continue
    try:s=(p/'stat').read_text().rsplit(') ',1)[1].split()
    except (FileNotFoundError,ProcessLookupError):continue
    if int(s[2]) in groups or int(p.name) in ids:members.append(dict(pid=int(p.name),pgid=int(s[2]),state=s[0]))
files=[p for p in E.iterdir() if p.is_file()]+[W/'REGISTRATION.md']
out=dict(utc=time.time(),boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
         expected_ids=ids,expected_groups=sorted(set(groups)),remaining=members,
         files={str(p.relative_to(W)):dict(bytes=p.stat().st_size,sha256=sha(p)) for p in sorted(files)},
         deployed_code={name:sha(W/name) for name in ['construct.py','replay.py','baseline.py','qpoly.py','run_once.py','run_capped.py']},
         source_access=False,production_outputs_absent=all(not(W/n).exists() for n in ['authority.json','construction.jsonl','replay-result.json']),
         disk=subprocess.check_output(['df','-Pk',str(W)],text=True),
         memory=subprocess.check_output(['free','-m'],text=True))
if members or out['boot']!='1a830d1e-1fa2-47f3-98bc-8c26c8cb8453':raise ValueError('final custody mismatch')
print(json.dumps(out,sort_keys=True))
