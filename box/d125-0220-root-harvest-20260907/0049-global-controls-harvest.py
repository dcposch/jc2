"""Root terminal replay of two tiny global discriminators; no source expansion."""
import ast, concurrent.futures, datetime, hashlib, json, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2')
start=time.monotonic()
def need(ok, msg):
    if not ok: raise RuntimeError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
boxes=[('d125-prescribed-cofactor-submersion-control-20260908','67c88aecaf31e41607b19db9a512ea6946155b42aab8e02ae7ded7bb58632889'),('k16-square-discriminant-ramification-discriminator-20260908','8be8774fce66bae559154806f8f4ab34fba71cf73fcf00bed6763c12b9c8a6f8')]
pins={}; cases=[]
for tag, digest in boxes:
    b=ROOT/'box'/tag; custody=b/'custody.json'; pins[str(custody)]=digest
    need(sha(custody)==digest,'custody drift')
    for e in json.loads(custody.read_bytes())['entries']: pins[str(ROOT/e['path'])]=e['sha256']
    checker=b/'check.py'
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(checker.read_text()))),'Assert gate')
    if tag.startswith('d125'):
        for row in json.loads((b/'replay-v2.json').read_bytes())['runs']:
            args=['/usr/bin/python3','-I','-B']+(['-O'] if row['optimized'] else [])+[str(checker),row['mode']]
            cases.append((args,row['returncode'],row['stdout_sha256'],row['stderr']))
    else:
        for row in json.loads((b/'replay.json').read_bytes())['runs']:
            cases.append((row['argv'],row['rc'],hashlib.sha256(row['stdout'].encode()).hexdigest(),row['stderr']))
for p,h in pins.items(): need(sha(Path(p))==h,'pre drift '+p)
def run(case):
    argv,rc,outsha,err=case
    p=subprocess.run(['/usr/bin/prlimit','--cpu=25','--as=536870912']+argv,capture_output=True,timeout=30,cwd=ROOT)
    need(p.returncode==rc,'return code '+str(argv))
    need(hashlib.sha256(p.stdout).hexdigest()==outsha,'stdout '+str(argv))
    need(p.stderr.decode()==err,'stderr '+str(argv))
    return {'argv':argv,'rc':rc,'stdout_sha256':outsha,'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: runs=list(pool.map(run,cases))
for p,h in pins.items(): need(sha(Path(p))==h,'post drift '+p)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','pins':pins,'runs':runs,'seconds':time.monotonic()-start,'scope':'Whole proofs and checkers read after terminal transaction/current pins. Exact physical degree15 toy only, not actual degree75/125 source. Universal submersion and split-cover proofs are prose; code checks a=1 and formal identities. No new promoted theorem or CAS.'}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f: json.dump(out,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
