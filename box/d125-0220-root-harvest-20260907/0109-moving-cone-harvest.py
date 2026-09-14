"""Terminal tiny moving-lift/cone replay, with no full-source construction."""
import ast, concurrent.futures, datetime, hashlib, json, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2'); start=time.monotonic()
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
boxes=[('d125-moving-lift-forced-degeneration-20260908','bc87d7bba7f9baf400aeef5ce9ecda776fbd98cb00dd8d33021108ebac369ebb'),('d125-reducible-cone-initial-discriminator-20260908','0bdc872addd88e41a83ced1463bd2c93f4adf16b37a21e2cce848c4230cf0cb1')]
pins={}; cases=[]
for tag,digest in boxes:
    b=ROOT/'box'/tag; custody=b/'custody.json'; pins[str(custody)]=digest
    need(sha(custody)==digest,'custody drift')
    for e in json.loads(custody.read_bytes())['entries']: pins[str(ROOT/e['path'])]=e['sha256']
    checker=b/'check.py'
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(checker.read_text()))),'Assert gate')
    for row in json.loads((b/'replay.json').read_bytes())['runs']:
        if 'argv' in row:
            cases.append((row['argv'],row['rc'],hashlib.sha256(row['stdout'].encode()).hexdigest(),row['stderr']))
        else:
            argv=['/usr/bin/python3','-I','-B']+(['-O'] if row['optimized'] else [])+[str(checker),row['mode']]
            cases.append((argv,row['returncode'],row['stdout_sha256'],row['stderr']))
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
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS','pins':pins,'runs':runs,'seconds':time.monotonic()-start,'scope':'Both whole proofs and checkers read after terminal transaction/current pins. Moving family source interface is unreviewed; cone global-tuple lemma and branch-selection countercontrol are not a source exclusion. Only tiny monomials/quintic/first-order cubic controls; no actual high R powers/full A15B25 or CAS.','corrections':['Root original seed omitted -v^-1; the corrected lift in the report is the accepted source lift.', 'Replay metadata rss_bytes is an address-space limit, not a sampled RSS claim.', 'The cone scalar-initial field is a recorded formal identity, not an executed full R_s cube.']}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f: json.dump(out,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
