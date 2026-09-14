"""Terminal, tiny gate replays; no source expansions or frozen-output writes."""
import ast
import hashlib
import json
import re
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/ubuntu/jc2')
OUT = ROOT / 'box/d125-0220-root-harvest-20260907/2225-resumption-gates.json'
pins = {}
runs = []
def need(ok, message):
    if not ok:
        raise ValueError(message)
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def pin(path, expected):
    path = ROOT / path
    need(sha(path) == expected, 'pin mismatch: ' + str(path))
    pins[str(path.relative_to(ROOT))] = expected
def receipt(tag, expected):
    path = Path('xmodel') / (tag + '.run.v2')
    pin(path, expected)
    d = dict(line.split('=', 1) for line in (ROOT / path).read_text().splitlines() if '=' in line)
    for k, v in {'final_status':'DONE', 'exit_code':'0', 'seal_boundary':'CLEAN', 'report_state':'BODY_SEALED', 'charge_basis_status':'ABSENT'}.items():
        need(d.get(k) == v, 'receipt ' + k)
    pin(d['report'], d['report_sha256'])
    for i in range(1, int(d['charged_inputs']) + 1):
        key = 'charged_input_' + str(i)
        pin(d[key], d[key + '_sha256'])
    return ROOT / d['report']
def table(report, prefix):
    for line in report.read_text().splitlines():
        match = re.fullmatch(r'\|\s*`?([^|`]+?)`?\s*\|\s*`?([0-9a-f]{64})`?\s*\|', line)
        if match:
            filename = match[1].replace(' (byte copy)', '').replace(' (rc 0)', '').replace(' (empty)', '')
            candidate = ROOT / prefix / filename
            if candidate.is_file():
                pin(candidate, match[2])
def execute(checker, mode, optimized, expected_rc, expected_stdout, expected_error):
    path = ROOT / checker
    need(not any(isinstance(node, ast.Assert) for node in ast.walk(ast.parse(path.read_text()))), 'assert gate: ' + checker)
    argv = ['/usr/bin/prlimit', '--cpu=25:25', '--as=536870912:536870912', '--', '/usr/bin/python3', '-I', '-B']
    argv += ['-O'] if optimized else []
    argv += [str(path)] + ([mode] if mode else [])
    start = time.monotonic()
    result = subprocess.run(argv, cwd=path.parent, capture_output=True, timeout=30)
    digest = hashlib.sha256(result.stdout).hexdigest()
    error = result.stderr.decode()
    need(result.returncode == expected_rc, 'return code: ' + checker + ' ' + mode)
    need(digest == expected_stdout, 'stdout: ' + checker + ' ' + mode)
    need(error.strip().endswith(expected_error.strip()), 'error: ' + checker + ' ' + mode)
    if not expected_error:
        need(not error, 'unexpected stderr')
    runs.append({'checker':checker, 'mode':mode, 'optimized':optimized, 'returncode':result.returncode, 'stdout_sha256':digest, 'stderr':error, 'seconds':time.monotonic()-start})
    return result.stdout

need(not OUT.exists(), 'fresh receipt required')
start = time.monotonic()
uniform = 'uniform-cone-jacobian-degree-gate-fable5-20260908'
golden = 'd125-golden-eight-parameter-gate-fable5-20260908'
ur = receipt(uniform, 'd409f11443bc6a66bf0e599780a306127d6ec240e566820b4ace89ae5300490e')
gr = receipt(golden, 'cd5e00657a40ad43c302ea6c4fc1a5b364581620d3a9eec7bf65af9caeae86f9')
table(ur, Path('box') / uniform)
table(gr, Path('box') / golden)
j12 = 'box/d125-golden-j12-attachment-gate-20260908'
custody = j12 + '/custody.json'
pin(custody, '1dca4bc7dac2b3bd27fa3113287acf36b17a8e5c7657bc5d26c33f7d48612dae')
for item in json.loads((ROOT / custody).read_text())['entries']:
    pin(item['path'], item['sha256'])
for item in json.loads((ROOT / ('box/' + uniform + '/replay-fable5.json')).read_text())['runs']:
    execute('box/' + uniform + '/scratch/uniform-check.py', item['argv'][-1], '-O' in item['argv'], item['rc'], item['stdout_sha256'], item['stderr_last'])
for item in json.loads((ROOT / ('box/' + golden + '/replay.json')).read_text())['runs']:
    execute('box/' + golden + '/control.py', item['mode'], item['optimized'], item['rc'], item['stdout_sha256'], item['stderr_tail'])
for item in json.loads((ROOT / (j12 + '/replay.json')).read_text())['runs']:
    execute(j12 + '/check.py', item['mode'], item['optimized'], item['returncode'], item['stdout_sha256'], item['stderr'])
for optimized in (False, True):
    raw = execute('box/' + uniform + '/attack.py', '', optimized, 0, '3656cf8d19badb99bd09e4a51406b038ec1ca440231c5b5c1577790abaec670b', '')
    data = json.loads(raw)
    need(data['A_vandermonde_22']['injective'], 'Vandermonde attack')
    need(not data['C']['some_c_makes_commute'], 'Euler attack')
    need(not data['B']['e=p^0']['nonzero'] and data['B']['e=p^1']['nonzero'] and data['B']['e=p^2']['nonzero'], 'positive p degree attack')
    need(not data['B']['e=Zp']['equals_PZ_times_eprime'], 'Z-carrying attack')
for path, digest in pins.items():
    need(sha(ROOT / path) == digest, 'post-replay drift: ' + path)
pin(Path(__file__), sha(Path(__file__)))
report = {'status':'PASS', 'utc':datetime.now(timezone.utc).isoformat(), 'elapsed_seconds':time.monotonic()-start, 'pins':pins, 'runs':runs, 'scope':'36 tiny normal/optimized outcomes, full prose reviewed separately; no actual source powers, no mathematical inference from finite illustrations'}
with OUT.open('x') as output:
    json.dump(report, output, indent=2, sort_keys=True)
print(json.dumps({'status':'PASS', 'pins':len(pins), 'runs':len(runs), 'elapsed_seconds':report['elapsed_seconds'], 'receipt':str(OUT.relative_to(ROOT)), 'sha256':sha(OUT)}))
