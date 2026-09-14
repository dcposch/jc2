"""Root pin/AST/tiny replay of the sealed symmetry desk packet."""
import ast
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
S = ROOT/'box/d125-symmetry-discriminator-20260907'
def need(ok, why):
    if not ok:
        raise ValueError(why)
def sha(data):
    return hashlib.sha256(data).hexdigest()
need(sha((S/'custody.json').read_bytes()) == '28ad166d1907e58ef85800348518932ae6a454e94d970142ba862b5dcaa141fe', 'custody pin')
custody = json.loads((S/'custody.json').read_bytes())
pins = {**custody['owned'], **custody['terminal_inputs']}
def verify():
    for name, row in pins.items():
        data = (ROOT/name).read_bytes()
        need(sha(data) == row['sha256'] and len(data) == row['bytes'], 'pin '+name)
verify()
for path in (S/'check.py', S/'composition_check.py',
             ROOT/'box/d125-minimal-receiver-client-preflight-20260906/client.py', Path(__file__)):
    need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(path.read_bytes()))), 'Assert gate')
def cap():
    resource.setrlimit(resource.RLIMIT_CPU, (25,25))
    resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
runs = []
start = time.monotonic()
for flags in ([], ['-O']):
    for filename, mutations, expected in (
        ('check.py', ('','--mutate-parity','--mutate-lambda-weight'),
         '9c3708294dc3c0df25cb256598436db5736a9737a2504dada04d0777171c2e4a'),
        ('composition_check.py', ('','--mutate-kernel-character','--mutate-gauge-inverse'),
         '2692591d3fc163efa7e27583d5a28c7805571942bbcf50eb3c0b2972429e8a1b')):
        for mutation in mutations:
            argv = [sys.executable, '-I', '-B', *flags, str(S/filename)] + ([mutation] if mutation else [])
            p = subprocess.run(argv, capture_output=True, timeout=30, preexec_fn=cap)
            need(p.returncode == (1 if mutation else 0), 'exit '+filename+mutation)
            if mutation:
                need(b'ValueError:' in p.stderr and p.stdout == b'', 'mutation reject')
            else:
                need(p.stderr == b'' and sha(p.stdout) == expected, 'witness')
            runs.append({'script':filename,'flags':flags,'mutation':mutation,'returncode':p.returncode,
                         'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr)})
verify()
record = {'status':'PASS','pins':pins,'runs':runs,'wall_seconds':time.monotonic()-start,
          'assert_nodes':0,'scope':'producer symmetry desk controls; not different-model review or full source construction'}
with (OUT/'symmetry.json').open('x') as f:
    json.dump(record, f, indent=2, sort_keys=True)
    f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'wall_seconds':record['wall_seconds'],
                  'receipt_sha256':sha((OUT/'symmetry.json').read_bytes())}))
