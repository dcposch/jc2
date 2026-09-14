"""Bounded root replay of two small, sealed desk controls."""
import ast
import hashlib
import json
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

ROOT = Path('/home/ubuntu/jc2')
HERE = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
signal.alarm(30)
cases = [
 ('composition', ROOT/'box/d125-b-a-hermite-composition-gate-fable5-20260907/control.py',
  '5a68cf56d2d626c2df005e7b373431b1389d23c9160315ec6a3e8d14c6e55223', ['gdeg', 'inverse', 'lift']),
 ('lambda', ROOT/'box/d125-zero-lambda-obstruction-20260907/check.py',
  'f0c9acb295d0ff8c1c2dcf8818c705174a04eb3e6d0386c93f2d7675c3c5f425', ['--mutate-map', '--mutate-drop-negative'])]
results = []
start = time.monotonic()
for name, script, pin, mutations in cases:
    if hashlib.sha256(script.read_bytes()).hexdigest() != pin:
        raise RuntimeError('code pin')
    if any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(script.read_text()))):
        raise RuntimeError('removable assertion')
    for mode in ([], ['-O']):
        for mutation in [None]+mutations:
            argv = [sys.executable, '-B', *mode, str(script)]+([] if mutation is None else [mutation])
            run = subprocess.run(argv, capture_output=True, text=True, timeout=5)
            item = {'case': name, 'mode': mode, 'mutation': mutation, 'returncode': run.returncode,
                    'stdout': run.stdout, 'stderr': run.stderr, 'code_sha256': pin}
            results.append(item)
            if run.returncode != (0 if mutation is None else 1):
                raise RuntimeError('unexpected control result '+str(item))
    if hashlib.sha256(script.read_bytes()).hexdigest() != pin:
        raise RuntimeError('post code pin')
with (HERE/'results.json').open('x') as f:
    json.dump({'status': 'PASS', 'seconds': time.monotonic()-start, 'results': results}, f, sort_keys=True)
print('PASS', len(results), 'runs, both modes, all real mutations rejected')
