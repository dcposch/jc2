"""One-shot root intake of the terminal non-H gate and source-matched C3 check.
No frozen driver is run and no frozen output is overwritten.
"""
import ast, datetime, hashlib, json, re, subprocess, time
from pathlib import Path

ROOT = Path('/home/ubuntu/jc2')
pins = {}
runs = []
def need(ok, message):
    if not ok:
        raise ValueError(message)
def pin(path, expected):
    p = Path(path)
    if not p.is_absolute(): p = ROOT / p
    got = hashlib.sha256(p.read_bytes()).hexdigest()
    need(got == expected, 'pin ' + str(p))
    pins[str(p)] = got
def own_pin(path):
    p = ROOT / path
    pin(p, hashlib.sha256(p.read_bytes()).hexdigest())
def execute(script, mode, optimized):
    argv = ['/usr/bin/prlimit', '--cpu=25', '--as=536870912', '--',
            '/usr/bin/python3', '-I', '-B'] + (['-O'] if optimized else []) + [str(script)]
    if mode is not None: argv.append(mode)
    t = time.monotonic()
    r = subprocess.run(argv, capture_output=True, timeout=30)
    runs.append({'argv': argv, 'rc': r.returncode, 'stdout': r.stdout.decode(),
                 'stderr': r.stderr.decode(), 'seconds': time.monotonic()-t})
    return r

t0 = time.monotonic()
tag = 'golden-nonh-composition-gate-fable5-20260908'
receipt = ROOT / 'xmodel' / (tag + '.run.v2')
pin(receipt, '7971057038e18affa811263af93b02311cbfc8c3ccbf7a0bf7bbe3089e08e4d9')
d = dict(line.split('=', 1) for line in receipt.read_text().splitlines() if '=' in line)
for key, expected in [('final_status','DONE'), ('exit_code','0'), ('seal_boundary','CLEAN'),
                      ('report_state','BODY_SEALED'), ('charge_basis_status','ABSENT')]:
    need(d.get(key) == expected, key)
for i in range(1, int(d['charged_inputs'])+1):
    key = f'charged_input_{i}'
    need(d[key+'_post'] == 'UNCHANGED', key)
    pin(d[key], d[key+'_sha256'])
pin(d['report'], d['report_sha256'])
for row in json.loads((ROOT/'box/golden-nonh-composition-gate-20260908/PINS.json').read_bytes())['entries']:
    pin(row['source'], row['sha256'])
    pin(row['path'], row['sha256'])
report = (ROOT/d['report']).read_text()
for path, sha in re.findall(r'\| (box/[^ |]+) \| `([0-9a-f]{64})` \|', report):
    pin(path, sha)

sw = ROOT/'box/websweep-20260908T2212Z'
pin(sw/'custody.json', 'f1851987d1c174c9bc3515b19b6897d45d485a1541eb8e6b48949c74fd6fa31d')
for row in json.loads((sw/'custody.json').read_bytes())['entries']:
    pin(row['path'], row['sha256'])
pin('xmodel/websweep-20260908T2212Z-astra.md', '364431f6267629e2f45e49785b18bf6393f4a9b4f2b59b4d3ee47047a70440dc')
pin('xmodel/websweep-20260908T2212Z-astra.md.artifact.json', 'ce452b6238ea96d7ce4b367a117dbfa7290ec272e61718af9cba0b30d94be0ad')

for directory in ['golden-two-regime-initial-discriminator-20260908', 'golden-resonant-source-consumer-20260908']:
    base = ROOT/'box'/directory
    script = base/'check.py'
    need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(script.read_bytes()))), 'assert')
    for row in json.loads((base/'replay.json').read_bytes())['runs']:
        r = execute(script, row['argv'][-1], '-O' in row['argv'])
        need((r.returncode, r.stdout.decode(), r.stderr.decode()) ==
             (row['rc'], row['stdout'], row['stderr']), 'parent replay mismatch')

attack = ROOT/'box'/tag/'attack/attack.py'
need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(attack.read_bytes()))), 'attack assert')
for opt in [False, True]:
    r = execute(attack, None, opt)
    need(r.returncode == 0 and not r.stderr, 'attack run')
    need(r.stdout == (attack.parent/'attack.out').read_bytes(), 'attack stdout')
    a = json.loads(r.stdout)
    need(a['attack1_violation_count'] == 0 and not a['attack1_violations'], 'order attack')
    need(a['attack1_survivors_exactly_resonant_set'] and a['attack1_survivor_count'] == 1739, 'survivors')
    need(a['attack2_resonant_matches_consumer'], 'resonant bracket')
    need(not a['attack2_Y10_coeff_q=5/3'] and bool(a['attack2_Y10_coeff_q=4/3']) and bool(a['attack2_Y10_coeff_q=2']), 'quintic mutation')
    need(a['attack3_slots']['w1_deg<=5'] == [[3,2]] and a['attack3_s12_triples_all_ge2'], 'weight slots')
    for row in a['attack4_rows']:
        need(row['row_g16p10_residual'] == ['0','0'] and row['row_g9p5_residual'] == ['0','0'], 'face rows')
        need(all(row[k] for k in ['c_face_equals_-5t/9','disc_is_3rho','t2_is_rho','rho_nonzero','tm1_nonzero']), 'golden identities')
    for key, row in a.items():
        if key.startswith('attack5_rho='):
            need(all(row[k] for k in ['M(g0)=0','equals_t-1','equals_t(t-1)','w3_coeff/p2_is_rho']), 'critical jet')

script = sw/'check_c3.py'
need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(script.read_bytes()))), 'C3 assert')
for row in json.loads((sw/'replay.json').read_bytes())['runs']:
    r = execute(script, row['mode'], row['optimized'])
    need((r.returncode,r.stdout.decode(),r.stderr.decode()) ==
         (row['returncode'],row['stdout'],row['stderr']), 'C3 mismatch')
for path, sha in list(pins.items()): pin(path, sha)
out = {'status':'PASS', 'completed':datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'elapsed_seconds':time.monotonic()-t0, 'pins':pins, 'runs':runs,
       'limitations':['Order enumeration is finite, not the universal proof.',
       'The independent attack endpoint display uses one float: 91/3 is the exact value; that display is not evidence.',
       'Independent attacks print predicates; root explicitly checked the load-bearing predicates.',
       'Source quadratic control is tautological; drop-resonant-target is a false-inference control.',
       'Sweep coverage is partial; C3 verification does not resolve JC2.']}
output = Path(__file__).with_suffix('.json')
with output.open('xb') as f: f.write(json.dumps(out,indent=2).encode())
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs), 'elapsed_seconds':out['elapsed_seconds'],
                  'output_sha256':hashlib.sha256(output.read_bytes()).hexdigest()}))
