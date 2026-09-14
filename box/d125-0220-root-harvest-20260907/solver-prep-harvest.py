"""Verify terminal hybrid solver preparation, then replay only tiny tests."""
import sys
sys.dont_write_bytecode=True
import hashlib,json,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');B=ROOT/'box/d125-hybrid81-solver-prep-20260907'
def need(x,s):
    if not x:raise ValueError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pins={'xmodel/d125-hybrid81-solver-prep-astra-20260907.md':'d99f7696a3916bd021f77c1b9753eab7b2854309ffb8e805b509781909e23338',
 'xmodel/d125-hybrid81-solver-prep-astra-20260907.md.artifact.json':'fe86f681e643a266567f78294f73e3bcf47985bea9cbd2a8397f4a7dd5808193',
 'box/d125-hybrid81-solver-prep-20260907/custody.json':'319fe354fd46e5aef2d17ff8ca0c54782a6ec6f277de6122d2d9df0c64967d87'}
for p,h in pins.items():need(sha(ROOT/p)==h,'outer pin '+p)
c=json.loads((B/'custody.json').read_bytes());need(c['all_writers_terminal_at_handoff'] and not c['remote_access'] and not c['full_client_local'],'terminal scope')
pins.update(c['files'])
for p,h in pins.items():need(sha(ROOT/p)==h,'pre pin '+p)
need((B/'exact.py').read_bytes()==(ROOT/'box/d125-small-exact-solver-strict-repair-20260907/exact.py').read_bytes(),'exact checker changed')
r=subprocess.run([sys.executable,'-B','ops/artifact_finalize.py','verify','--final','xmodel/d125-hybrid81-solver-prep-astra-20260907.md'],cwd=ROOT,capture_output=True,timeout=10);need(r.returncode==0,'transaction')
start=time.monotonic();p=subprocess.run([sys.executable,'-B',str(B/'run_tests.py')],cwd=ROOT,capture_output=True,timeout=35)
need(p.returncode==0,'tiny batch');d=json.loads(p.stdout)
need(len(d['results'])==2 and all(v['returncode']==0 and 'Ran 25 tests' in v['stderr'] for v in d['results']),'actual both-mode tests')
for q,h in pins.items():need(sha(ROOT/q)==h,'post pin '+q)
out=dict(status='PASS_SOLVER_PREP_TINY_ONLY',pins=len(pins),wall_seconds=time.monotonic()-start,transaction=r.stdout.decode(),result=d,full_source=False,worker=False,solver=False)
dest=ROOT/'box/d125-0220-root-harvest-20260907/solver-prep-harvest.json'
with dest.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),wall_seconds=out['wall_seconds'],receipt_sha256=sha(dest))))
