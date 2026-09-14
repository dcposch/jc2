"""Read-only bounded replay; emit a NEW receipt on stdout, never alter inputs."""
from pathlib import Path
import ast
import hashlib
import json
import re
import subprocess
import time
from datetime import datetime, timezone

BASE = Path('/home/ubuntu/jc2')
REPORT = BASE / 'xmodel/golden-hdiv-simple-l-gate-fable5-20260908.md'
RECEIPT = BASE / 'xmodel/golden-hdiv-simple-l-gate-fable5-20260908.run.v2'
BOX = BASE / 'box/golden-hdiv-simple-l-gate-fable5-20260908'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

start = time.monotonic()
pins = {REPORT: 'f72285134924774c1e13928383ee50a886551aab0ce8dcee3b5730c4907d0f2e',
        RECEIPT: '966ecd8eceed9c7a3e99827d8b8bbf43318d2b853e92497a0baed2799572bc06'}
table = re.findall(r'^- `([^`]+)` `([0-9a-f]{64})`$', REPORT.read_text(), re.M)
require(len(table) == 19, 'expected code plus eighteen retained output pins')
for name, expected in table:
    require('/' not in name, 'unexpected artifact name')
    pins[BOX / name] = expected
metadata = dict(line.split('=', 1) for line in RECEIPT.read_text().splitlines() if '=' in line)
for i in range(1, 10):
    key = f'charged_input_{i}'
    pins[BASE / metadata[key]] = metadata[key + '_sha256']
for path, expected in pins.items():
    require(sha(path) == expected, f'pre-drift: {path}')
control = BOX / 'control.py'
require(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(control.read_text()))), 'assert in control')
results = []
expected_checks = {
    'positive': ['CHECK1 PASS', 'CHECK2 PASS', 'CHECK3 PASS'],
    'wrong-root': ['CHECK1 FAIL', 'CHECK2 PASS', 'CHECK3 PASS'],
    'nonmonic': ['CHECK1 PASS', 'CHECK2 FAIL(expected in nonmonic mode)', 'CHECK3 PASS'],
}
for mode, checks in expected_checks.items():
    for optimized in (False, True):
        suffix = mode + ('_O' if optimized else '')
        argv = ['prlimit', '--cpu=25', '--as=536870912', 'python3', '-I', '-B']
        if optimized:
            argv.append('-O')
        argv += [str(control), mode]
        t = time.monotonic()
        run = subprocess.run(argv, cwd=BOX, capture_output=True, timeout=30)
        stored_rc = (BOX / f'out_{suffix}.rc').read_text().strip()
        require(stored_rc == f'rc={run.returncode}', 'return code mismatch')
        require(run.stdout == (BOX / f'out_{suffix}.stdout').read_bytes(), 'stdout mismatch')
        require(run.stderr == (BOX / f'out_{suffix}.stderr').read_bytes(), 'stderr mismatch')
        text = run.stdout.decode()
        require([line for line in text.splitlines() if line.startswith('CHECK')] == checks, 'changed-object predicate mismatch')
        require(run.returncode == 0 and not run.stderr, 'unexpected runtime outcome')
        if mode == 'nonmonic':
            require('Euler P: False Euler Q: True' in text, 'nonmonic control is not homogeneous: preserve correction')
        results.append({'argv': argv, 'mode': mode, 'optimized': optimized,
                        'elapsed_seconds': round(time.monotonic() - t, 6),
                        'rc': run.returncode, 'stdout': text, 'stderr': run.stderr.decode(),
                        'checks': checks})
for path, expected in pins.items():
    require(sha(path) == expected, f'post-drift: {path}')
print(json.dumps({'utc': datetime.now(timezone.utc).isoformat(), 'status': 'PASS',
                  'pins': [{'path': str(p.relative_to(BASE)), 'sha256': v} for p, v in pins.items()],
                  'pin_count': len(pins), 'results': results,
                  'seconds': round(time.monotonic() - start, 6),
                  'scope': 'Six finite illustration replays, full output matching and explicit changed-object predicates; prose supplies the proof. Nonmonic P is mixed-degree, not Euler degree4. No source high powers or inner timeout.'}, indent=2))
