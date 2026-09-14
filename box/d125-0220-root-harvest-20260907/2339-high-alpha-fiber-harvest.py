"""Terminal small-control replay and exact primary/source custody, no full source."""
import datetime,hashlib,json,resource,subprocess,time
from pathlib import Path
R=Path('/home/ubuntu/jc2'); B=R/'box/d125-pure-high-alpha-discriminator-20260907'
start=time.monotonic()
def need(c,m):
    if not c: raise RuntimeError(m)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
pins={}
for rel,want in [('box/d125-pure-high-alpha-discriminator-20260907/custody.json','64ac1f6170cb652d0fed422adff76fb37f90b6f2c2df42f55963372cafcb9ea1'),('box/d125-marked-fiber-global-discriminator-20260907/custody.json','9787c2251c86d95d5c5b7f16f5d210a311b47313ca1827fafecd5d2d2f33f474')]:
    need(sha(R/rel)==want,'custody drift')
    pins[rel]=want
    for e in json.loads((R/rel).read_bytes())['entries']: pins[e['path']]=e['sha256']
for n,h in pins.items():need(sha(R/n)==h,'input drift '+n)
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
runs=[]
for ref in json.loads((B/'replay.json').read_bytes())['runs']:
    argv=['/usr/bin/python3','-I','-B']+(['-O'] if ref['optimized'] else [])+[str(B/'check.py')]+([ref['mutation']] if ref['mutation'] else [])
    p=subprocess.run(argv,capture_output=True,timeout=30,preexec_fn=caps)
    need(p.returncode==ref['returncode'],'returncode')
    need(hashlib.sha256(p.stdout).hexdigest()==ref['stdout_sha256'],'stdout')
    need(hashlib.sha256(p.stderr).hexdigest()==ref['stderr_sha256'],'stderr')
    runs.append({**ref,'root_replayed':True})
for n,h in pins.items():need(sha(R/n)==h,'post drift '+n)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,'scope':'High-alpha producer small controls/root whole-proof hand check; marked fiber custody only, whole primary interface reading separate. Neither is different-model promotion.','correction':'Checker parity toy is an observation, not a meaningful necessity countercontrol; the 3/5 lemma also holds without parity after a scalar shift.'}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
