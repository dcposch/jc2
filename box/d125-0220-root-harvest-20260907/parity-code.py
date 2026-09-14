"""Root pin and tiny normal/optimized replay; never production construction."""
import ast
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
S=ROOT/'box/d125-parity-compression-code-prep-20260907'
def need(ok, why):
    if not ok: raise ValueError(why)
def sha(data): return hashlib.sha256(data).hexdigest()
need(sha((S/'pins.json').read_bytes())=='f655e3c4791e0a3cc333234889fb9167ef21d1dee58a76f3a132b74de0d42860','pin manifest')
need(sha((S/'custody.json').read_bytes())=='bb6f9ac6f9d15a81a4c66719dae19b80380782a359e7998b18ecf8d2f01bb51e','custody')
pins=json.loads((S/'pins.json').read_bytes())['pins']
def verify():
    for name,pin in pins.items(): need(sha((ROOT/name).read_bytes())==pin,'pin '+name)
verify()
for name in ('construct.py','replay.py','test_construct.py','qpoly.py','baseline.py','run_tests.py'):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((S/name).read_bytes()))),'Assert '+name)
def cap():
    resource.setrlimit(resource.RLIMIT_CPU,(12,12))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
start=time.monotonic(); runs=[]
for flags in ([],['-O']):
    p=subprocess.run([sys.executable,'-B',*flags,str(S/'test_construct.py'),'-v'],cwd=S,capture_output=True,
                     timeout=max(0.1,30-(time.monotonic()-start)),preexec_fn=cap)
    need(p.returncode==0 and b'Ran 13 tests' in p.stderr and p.stderr.endswith(b'\nOK\n'),'tiny tests')
    runs.append({'flags':flags,'returncode':p.returncode,'stdout':p.stdout.decode(),'stderr':p.stderr.decode()})
verify()
result={'status':'PASS','pins':pins,'runs':runs,'wall_seconds':time.monotonic()-start,'assert_nodes':0,
        'scope':'13 tiny methods each mode, actual mutations; no production metadata, reconstruction or original full stream'}
with (OUT/'parity-code.json').open('x') as f:
    json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':2,'methods_each':13,'wall_seconds':result['wall_seconds'],
                  'receipt_sha256':sha((OUT/'parity-code.json').read_bytes())}))
