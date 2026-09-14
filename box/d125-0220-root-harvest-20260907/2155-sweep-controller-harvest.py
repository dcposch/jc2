"""Bounded custody verification and tiny mock replay; no source arithmetic."""
from pathlib import Path
import hashlib,json,subprocess,time
ROOT=Path('/home/ubuntu/jc2');OUT=Path(__file__).parent/'2155-sweep-controller-harvest.json'
def need(c,m):
 if not c:raise RuntimeError(m)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
start=time.monotonic();pins={};counts={}
for name,cpin in [('websweep-20260907T0735Z','c0d46225197b1136474c5f989d46310acaf9e40c9c51a50c54c7f417f9e01454'),('d125-hybrid81-controller-prep-20260907','534d227ae3bd1e3b4ab4696373afd89b095716b97e4da15ccc4c59e362f2f9ac')]:
 base=ROOT/'box'/name;cp=base/'custody.json';need(sha(cp)==cpin,'custody drift');pins[str(cp.relative_to(ROOT))]=cpin
 c=json.loads(cp.read_bytes());counts[name]=len(c['files'])
 for n,v in c['files'].items():
  p=base/n;need(p.resolve().is_relative_to(base.resolve()),'path escape')
  need(p.stat().st_size==v['bytes'] and sha(p)==v['sha256'],'file drift '+str(p));pins[str(p.relative_to(ROOT))]=v['sha256']
rows=[]
for flags in ([],['-O']):
 cmd=['/usr/bin/python3','-I','-B']+flags+[str(ROOT/'box/d125-hybrid81-controller-prep-20260907/test_controller.py')]
 p=subprocess.run(cmd,capture_output=True,timeout=5);need(p.returncode==0 and not p.stderr,'mock test failure')
 rows.append({'argv':cmd,'rc':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()})
for n,s in pins.items():need(sha(ROOT/n)==s,'post drift '+n)
r={'scope':'CUSTODY_AND_MOCK_ONLY','counts':counts,'pins':pins,'runs':rows,'elapsed_seconds':time.monotonic()-start,'cutoff':'2026-09-07T07:56:45Z','social_holes_since':'2026-09-03T10:17:00Z','authority_issued':False,'remote_access':False}
with OUT.open('x') as f:json.dump(r,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'status':'PASS','counts':counts,'pins':len(pins),'runs':len(rows),'elapsed_seconds':r['elapsed_seconds'],'receipt_sha256':sha(OUT)}))
