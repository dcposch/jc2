"""Root terminal direct-source interface controls, no full-source expansion."""
import ast, concurrent.futures, datetime, hashlib, json, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2'); B=ROOT/'box/d125-cone-first-contact-source-20260908'
start=time.monotonic()
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
cp=B/'custody.json'; pins={str(cp):'19ee02e51ec209adc6dfb3981b63e722be9fd6d238fd1fe38f2e461bb1875606'}
need(sha(cp)==pins[str(cp)],'custody drift')
for e in json.loads(cp.read_bytes())['entries']: pins[str(ROOT/e['path'])]=e['sha256']
for p,h in pins.items(): need(sha(Path(p))==h,'pre drift '+p)
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((B/'check.py').read_text()))),'Assert gate')
def run(row):
    p=subprocess.run(['/usr/bin/prlimit','--cpu=25','--as=536870912']+row['argv'],capture_output=True,timeout=30,cwd=ROOT)
    need(p.returncode==row['rc'],'exit '+str(row['argv']))
    need(p.stdout.decode()==row['stdout'],'stdout '+str(row['argv']))
    need(p.stderr.decode()==row['stderr'],'stderr '+str(row['argv']))
    return {'argv':row['argv'],'rc':p.returncode,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: runs=list(pool.map(run,json.loads((B/'replay.json').read_bytes())['runs']))
for p,h in pins.items(): need(sha(Path(p))==h,'post drift '+p)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,'scope':'Whole direct-source proof and final checker read after terminal transaction/current pins. Only formal wedge/shear and scalar/factor controls, no actual H^2/H^3/H^5/source/CAS. Root checked literal matching to conditional consumer: R_s odd, F/G coefficient degree bounds13/23 from positive even s-order and total combined degree15/25, normal C from deg_g<=2, scalar alpha10/delta20. Composite source exclusion remains unreviewed.','corrections':['Initial double-beta checker is retained failed development evidence, not a valid replay mode.', 'Tiny omitted-weight control does not itself multiply the high square; the elementary factorization in prose proves H|P^2.']}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f: json.dump(out,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
