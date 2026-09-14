"""Root replay of terminal degree-three golden controls, not source equations."""
import ast, concurrent.futures, datetime, hashlib, json, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2')
B=ROOT/'box/d125-golden-divisibility-control-20260908'
start=time.monotonic()
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
cp=B/'custody.json'
pins={str(cp):'2da3a29b98017a17cb900ac440738237d0f421dd684aa91526769779128f30eb'}
need(sha(cp)==pins[str(cp)],'custody drift')
for e in json.loads(cp.read_bytes())['entries']: pins[str(ROOT/e['path'])]=e['sha256']
for p,h in pins.items(): need(sha(Path(p))==h,'pre drift '+p)
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((B/'check.py').read_text()))),'Assert gate')
def run(row):
    argv=['/usr/bin/python3','-I','-B']+(['-O'] if row['optimized'] else [])+[str(B/'check.py'),row['mode']]
    z=subprocess.run(['/usr/bin/prlimit','--cpu=25','--as=536870912']+argv,capture_output=True,timeout=30,cwd=ROOT)
    need(z.returncode==row['returncode'],'exit '+str(argv))
    need(hashlib.sha256(z.stdout).hexdigest()==row['stdout_sha256'],'stdout '+str(argv))
    need(z.stderr.decode()==row['stderr'],'stderr '+str(argv))
    return {'argv':argv,'returncode':z.returncode,'stdout_sha256':hashlib.sha256(z.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(z.stderr).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    runs=list(pool.map(run,json.loads((B/'replay.json').read_bytes())['runs']))
for p,h in pins.items(): need(sha(Path(p))==h,'post drift '+p)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,
     'scope':'Terminal author idle; transaction and current pins checked before whole report/checker/replay. Exact degree-three classification and repeated-root reduced-branch countercontrol only. No source H|F^2 premise supplied; not a full-source point or exclusion. Both conjugates retained.',
     'corrections':['Producer rss_bytes denotes the address-space cap, not sampled RSS. Factor exponents, not an expanded F^2 or H^2, certify the displayed divisibility.']}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f: json.dump(out,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
