"""Root terminal nonodd interface controls; no actual high source powers."""
import ast, concurrent.futures, datetime, hashlib, json, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2'); B=ROOT/'box/d125-nonodd-cone-discriminator-20260908'
start=time.monotonic()
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
cp=B/'custody.json'; pins={str(cp):'53e6d8bc7ca9006be56a8f19bd123039eb6d0f176a426be902899d0b911d8837'}
need(sha(cp)==pins[str(cp)],'custody drift')
for e in json.loads(cp.read_bytes())['entries']: pins[str(ROOT/e['path'])]=e['sha256']
for p,h in pins.items(): need(sha(Path(p))==h,'pre drift '+p)
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((B/'check.py').read_text()))),'Assert gate')
def run(row):
    z=subprocess.run(['/usr/bin/prlimit','--cpu=25','--as=536870912']+row['argv'],capture_output=True,timeout=30,cwd=ROOT)
    need(z.returncode==row['rc'],'exit '+str(row['argv']))
    need(z.stdout.decode()==row['stdout'],'stdout '+str(row['argv']))
    need(z.stderr.decode()==row['stderr'],'stderr '+str(row['argv']))
    return {'argv':row['argv'],'returncode':z.returncode,'stdout_sha256':hashlib.sha256(z.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(z.stderr).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    runs=list(pool.map(run,json.loads((B/'replay.json').read_bytes())['runs']))
for p,h in pins.items(): need(sha(Path(p))==h,'post drift '+p)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,
     'scope':'Whole nonodd proof/checker read after author IDLE, transaction and all current pins. Free-symbol wedge and Euler controls only. Root checked all five scalar kernels and source combined grading; all-degree/golden/common cases not included. Different-model extension review still required.',
     'corrections':['The frozen provisional centralizer-parent header is historical; its exact lemma is now independently reviewed in15h. This does not promote the new nonodd argument.', 'Coefficient ordinary degree G<=23 follows ordG>=2j>=2 even without parity. No arbitrary lower-degree bound is imposed.']}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f: json.dump(out,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
