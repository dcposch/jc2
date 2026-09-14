"""Tiny final producer controls only, no record mode or frozen writes."""
from pathlib import Path
import hashlib,json,subprocess,time
R=Path('/home/ubuntu/jc2');B=R/'box/d125-pure-low-alpha-discriminator-20260907';start=time.monotonic()
def need(c,m):
 if not c:raise RuntimeError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((B/'custody.json').read_bytes());pins={p['path']:p['sha256'] for p in c['inputs']+c['owned']}
for n,s in pins.items():need(sha(R/n)==s,'pin drift '+n)
rows=[]
modes=[('',None),('--mutate-delta-sign','universal pre-3j mixed identity'),('--mutate-intermediate','universal pre-3j mixed identity'),('--mutate-omit-alphaG','actual scalar-kernel jet identity'),('--mutate-drop-scalar-cubic','actual retained scalar cubic coefficient'),('--mutate-constant-C','nonconstant even leading transverse coefficient')]
for flags in ([],['-O']):
 for mode,msg in modes:
  cmd=['/usr/bin/python3','-I','-B']+flags+[str(B/'check.py')]+([mode] if mode else [])
  p=subprocess.run(cmd,capture_output=True,timeout=5)
  need((p.returncode!=0)==bool(mode),'wrong return')
  if mode:need(msg.encode() in p.stderr,'wrong rejection')
  else:need(not p.stderr and p.stdout==(B/'final-witness.json').read_bytes(),'positive witness drift')
  rows.append({'argv':cmd,'returncode':p.returncode,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()})
for n,s in pins.items():need(sha(R/n)==s,'post drift '+n)
out=Path(__file__).with_suffix('.json');r={'scope':'PRODUCER_CONTROLS_ONLY_NOT_PROMOTION','pins':pins,'runs':rows,'seconds':time.monotonic()-start}
with out.open('x') as f:json.dump(r,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(rows),'seconds':r['seconds'],'receipt_sha256':sha(out)}))
