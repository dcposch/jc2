"""Root custody/AST replay of the terminal moving-face normalization desk."""
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
S = ROOT / 'box/d125-parity-unit-normalization-20260907'
def need(ok, why):
    if not ok:
        raise ValueError(why)
def sha(data):
    return hashlib.sha256(data).hexdigest()
need(sha((S/'custody.json').read_bytes()) == '494d7d9dcea21488162f0b4bd0e6a860439ff1413d6572230df08cb79294005f', 'custody pin')
c = json.loads((S/'custody.json').read_bytes())
pins = {**c['owned'], **c['inputs']}
def verify():
    for name, row in pins.items():
        data = (ROOT/name).read_bytes()
        need(sha(data) == row['sha256'] and len(data) == row['bytes'], 'pin '+name)
verify()
for path in (S/'check.py', ROOT/'box/d125-minimal-receiver-client-preflight-20260906/client.py', Path(__file__)):
    need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(path.read_bytes()))), 'Assert gate')
def cap():
    resource.setrlimit(resource.RLIMIT_CPU, (25,25))
    resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
rows = []
start = time.monotonic()
for flags in ([], ['-O']):
    for mutation in ('', '--mutate-face', '--mutate-c-power', '--mutate-omit-guard'):
        argv = [sys.executable, '-I', '-B', *flags, str(S/'check.py')] + ([mutation] if mutation else [])
        p = subprocess.run(argv, capture_output=True, timeout=30, preexec_fn=cap)
        need(p.returncode == (1 if mutation else 0), 'exit '+mutation)
        if mutation:
            message = b'omitted invertibility' if mutation == '--mutate-omit-guard' else b'changed face or c exponent'
            need(message in p.stderr and not p.stdout, 'mutation reason')
        else:
            need(not p.stderr and sha(p.stdout) == 'a04393cf75fbc22d2ff4fb4480fa27600921fba57de42cd5b2556f80cff7e39c', 'witness')
        rows.append({'flags': flags, 'mutation': mutation, 'returncode': p.returncode,
                     'stdout_sha256': sha(p.stdout), 'stderr_sha256': sha(p.stderr)})
verify()
record = {'status':'PASS', 'pins':pins, 'runs':rows, 'wall_seconds':time.monotonic()-start,
          'assert_nodes':0, 'scope':'producer desk normalization controls; not different-model gate or full row construction'}
with (OUT/'unit-normalization.json').open('x') as f:
    json.dump(record, f, indent=2, sort_keys=True)
    f.write('\n')
print(json.dumps({'status':'PASS', 'pins':len(pins), 'runs':len(rows), 'wall_seconds':record['wall_seconds'],
                  'receipt_sha256':sha((OUT/'unit-normalization.json').read_bytes())}))
