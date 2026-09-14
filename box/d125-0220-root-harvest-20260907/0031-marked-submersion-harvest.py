"""Root terminal small submersion controls; not a new promotion."""
import ast,datetime,hashlib,json,subprocess,time
from pathlib import Path
R=Path('/home/ubuntu/jc2'); B=R/'box/d125-marked-component-submersion-discriminator-20260908'
start=time.monotonic()
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
need(sha(B/'custody.json')=='4b0cd5f0b4d50492e22eee653cf794e1e4579e24f3af20cf359f3e5c733028f4','custody drift')
pins={e['path']:e['sha256'] for e in json.loads((B/'custody.json').read_bytes())['entries']}
for p,h in pins.items():need(sha(R/p)==h,'input drift '+p)
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((B/'check.py').read_text()))),'Assert node')
runs=[]
for row in json.loads((B/'replay.json').read_bytes())['runs']:
    cmd=['/usr/bin/prlimit','--cpu=25','--as=536870912','/usr/bin/python3','-I','-B']+(['-O'] if row['optimized'] else [])+[str(B/'check.py'),row['mode']]
    p=subprocess.run(cmd,capture_output=True,timeout=30,cwd=R)
    need(p.returncode==row['returncode'],'returncode')
    need(hashlib.sha256(p.stdout).hexdigest()==row['stdout_sha256'],'stdout')
    need(p.stderr.decode()==row['stderr'],'stderr')
    runs.append({'argv':cmd,'returncode':p.returncode,'stdout_sha256':row['stdout_sha256'],'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()})
for p,h in pins.items():need(sha(R/p)==h,'post drift '+p)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,'scope':'Root whole elementary proof/code and exact tiny controls; embedding-only obstruction refuted by vN. Degree_u(M)<=1 exclusion does not cover actual degree14; not independently promoted.','correction':'The final y!=empty dictionary check only tests nonzeroness, not nonextension across y=0; the explicit v=y^-1 formula establishes that caveat in prose.'}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
