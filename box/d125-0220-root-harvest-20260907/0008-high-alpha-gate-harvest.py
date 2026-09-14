"""Terminal high-alpha review: pinned small controls only, no source expansion."""
import ast, datetime, hashlib, json, subprocess, time
from pathlib import Path
ROOT = Path('/home/ubuntu/jc2')
TAG = 'd125-pure-high-alpha-gate-fable5-20260907'
B = ROOT / 'box' / TAG
start = time.monotonic()
def need(ok, message):
    if not ok:
        raise RuntimeError(message)
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
receipt = ROOT / 'xmodel' / (TAG + '.run.v2')
d = dict(line.split('=', 1) for line in receipt.read_text().splitlines() if '=' in line)
need(all(d[k] == v for k, v in {'final_status':'DONE', 'exit_code':'0', 'seal_boundary':'CLEAN', 'report_state':'BODY_SEALED', 'charge_basis_status':'ABSENT'}.items()), 'terminal receipt')
pins = {str(receipt): 'daea763bdabeacf09bab30fad6e04581d39184fd83598ebfc605d8f2489bcf2b', str(ROOT / d['report']): d['report_sha256']}
for i in range(1, 13):
    pins[str(ROOT / d[f'charged_input_{i}'])] = d[f'charged_input_{i}_sha256']
pins[str(B / 'custody.json')] = sha(B / 'custody.json')
for e in json.loads((B / 'custody.json').read_bytes())['entries']:
    pins[str(ROOT / e['path'])] = e['sha256']
P = ROOT / 'box/d125-pure-high-alpha-discriminator-20260907'
for e in json.loads((P / 'custody.json').read_bytes())['entries']:
    pins[str(ROOT / e['path'])] = e['sha256']
for p, h in pins.items():
    need(sha(Path(p)) == h, 'input drift ' + p)
scripts = [B / 'fable5_independent_checks.py', P / 'check.py', ROOT / 'box/d125-zero-k-deformation-discriminator-20260907/check.py']
for script in scripts:
    need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(script.read_text()))), 'Assert node ' + str(script))
runs = []
def run(argv, expected_rc, expected_stdout, marker=None, expected_stderr=None):
    command = ['/usr/bin/prlimit', '--cpu=25', '--as=536870912', '/usr/bin/python3', '-I', '-B'] + argv
    p = subprocess.run(command, capture_output=True, timeout=30, cwd=ROOT)
    need(p.returncode == expected_rc, 'return code ' + str(argv))
    need(hashlib.sha256(p.stdout).hexdigest() == expected_stdout, 'stdout ' + str(argv))
    if expected_stderr is not None:
        need(hashlib.sha256(p.stderr).hexdigest() == expected_stderr, 'stderr ' + str(argv))
    elif marker:
        need(marker.encode() in p.stderr, 'failure marker')
    else:
        need(not p.stderr, 'unexpected stderr')
    runs.append({'argv':command, 'returncode':p.returncode, 'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(), 'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()})
for opt in [[], ['-O']]:
    run(opt + [str(scripts[0])], 0, '6133d908810864c95a538e553b3bd420099abf060ca2641f7327d5af1560db39')
for ref in json.loads((P / 'replay.json').read_bytes())['runs']:
    argv = (['-O'] if ref['optimized'] else []) + [str(P / 'check.py')] + ([ref['mutation']] if ref['mutation'] else [])
    run(argv, ref['returncode'], ref['stdout_sha256'], expected_stderr=ref['stderr_sha256'])
for p, h in pins.items():
    need(sha(Path(p)) == h, 'post drift ' + p)
out = {'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'pins':pins, 'runs':runs, 'seconds':time.monotonic()-start, 'scope':'Root whole proof and reviewer code read; finite degree-five factors and formal 3/5 calculations only; no high powers of actual R or A15/B25/full source.', 'corrections':['The producer parity-necessity toy is not a meaningful countercontrol; scalar shifting removes d0 without parity.', 'Reviewer has 26 printed checks, including two literal need(True) prose markers, not 26 independent computed identities.', 'The valuation grid uses a finite sentinel for infinity; universal infinity reasoning and top bracket rows are prose proofs.', 'Producer local_pole_orders are recorded constants; reviewer computes a truncated local series and proves the orders in prose.']}
dest = Path(__file__).with_suffix('.json')
with dest.open('x') as f:
    json.dump(out, f, indent=2, sort_keys=True)
    f.write('\n')
print(json.dumps({'status':'PASS', 'pins':len(pins), 'runs':len(runs), 'seconds':out['seconds'], 'receipt_sha256':sha(dest)}))
