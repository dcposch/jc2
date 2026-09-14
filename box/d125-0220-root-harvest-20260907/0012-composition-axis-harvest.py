"""Two terminal small controls, no full-source calculations."""
import ast, concurrent.futures, datetime, hashlib, json, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2')
start=time.monotonic()
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
packs=[('d125-finite-boundary-composition-20260908','8536d268362822ad1bea3e316802b56062d1a7f29a712442821b3462ed252512'),('d125-axis-bezout-unit-discriminator-20260908','644f86fa83439f66ad426b6ba322f88b0c9df5c86ed0e9d58756bc5bf25b3d2e')]
pins={}; cases=[]
for tag,h in packs:
    b=ROOT/'box'/tag
    pins[str(b/'custody.json')]=h
    need(sha(b/'custody.json')==h,'custody drift')
    for e in json.loads((b/'custody.json').read_bytes())['entries']:
        pins[str(ROOT/e['path'])]=e['sha256']
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((b/'check.py').read_text()))),'Assert node')
    for row in json.loads((b/'replay.json').read_bytes())['runs']:
        if 'argv' in row: argv=row['argv']
        else: argv=['/usr/bin/python3','-I','-B']+(['-O'] if row['optimized'] else [])+[str(b/'check.py')]+([row['mutation']] if row['mutation'] else [])
        cases.append((tag,argv,row))
for p,h in pins.items(): need(sha(Path(p))==h,'input drift '+p)
def run(case):
    tag,argv,row=case
    cmd=['/usr/bin/prlimit','--cpu=25','--as=536870912']+argv
    p=subprocess.run(cmd,capture_output=True,timeout=30,cwd=ROOT)
    need(p.returncode==row['returncode'],'exit '+str(cmd))
    need(hashlib.sha256(p.stdout).hexdigest()==row['stdout_sha256'],'stdout '+str(cmd))
    need(hashlib.sha256(p.stderr).hexdigest()==row['stderr_sha256'],'stderr '+str(cmd))
    return {'tag':tag,'argv':cmd,'returncode':p.returncode,'stdout_sha256':row['stdout_sha256'],'stderr_sha256':row['stderr_sha256']}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: runs=list(pool.map(run,cases))
for p,h in pins.items(): need(sha(Path(p))==h,'post drift '+p)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,'scope':'Root whole proof/code and bounded toy/projection controls; composition PROVISIONAL pending independent gate, axis redundant producer/root-checked only, not new promotion.'}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f: json.dump(out,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
