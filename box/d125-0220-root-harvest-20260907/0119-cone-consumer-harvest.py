"""Root terminal consumer controls only; no source-applicability claim."""
import ast, concurrent.futures, datetime, hashlib, json, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2'); B=ROOT/'box/d125-cone-global-initial-consumer-20260908'
start=time.monotonic()
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
cp=B/'custody.json'; pins={str(cp):'741635912eb28fb15dc854986e490fe853304db30870b0c9d25eb560018cdcd1'}
need(sha(cp)==pins[str(cp)],'custody drift')
for e in json.loads(cp.read_bytes())['entries']: pins[str(ROOT/e['path'])]=e['sha256']
for p,h in pins.items(): need(sha(Path(p))==h,'pre drift '+p)
checker=B/'check.py'
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(checker.read_text()))),'Assert gate')
def run(row):
    argv=['/usr/bin/prlimit','--cpu=25','--as=536870912','/usr/bin/python3','-I','-B']+(['-O'] if row['optimized'] else [])+[str(checker),row['mode']]
    p=subprocess.run(argv,capture_output=True,timeout=30,cwd=ROOT)
    need(p.returncode==row['returncode'],'exit '+row['mode'])
    need(hashlib.sha256(p.stdout).hexdigest()==row['stdout_sha256'],'stdout '+row['mode'])
    need(p.stderr.decode()==row['stderr'],'stderr '+row['mode'])
    return {'argv':argv,'rc':p.returncode,'stdout_sha256':row['stdout_sha256'],'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: runs=list(pool.map(run,json.loads((B/'replay.json').read_bytes())['runs']))
for p,h in pins.items(): need(sha(Path(p))==h,'post drift '+p)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,'scope':'Whole conditional proof/checker read after terminal transaction/current pins. Only formal 3/5 identities and finite valuation/product controls; source applicability remains separate. q=infinity illustration uses a finite surrogate for a lower bound, not universal proof.'}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f: json.dump(out,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
