"""Root receipt-first custody and tiny actual-output/code-gate replay only."""
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
ENG = ROOT/'box/d125-defect-order-engineering-20260907'
SOL = ROOT/'box/d125-defect-order-code-gate-sol56-20260907'
CODE = ROOT/'box/d125-defect-order-code-prep-20260907'
def need(ok, why):
    if not ok:
        raise ValueError(why)
def sha(data):
    return hashlib.sha256(data).hexdigest()
pins = {}
snapshots = {}
for tag in ('d125-defect-order-code-gate-sol56-20260907',
            'd125-compatible-order-delta-gate-fable5-20260907'):
    r = dict(line.split('=', 1) for line in (ROOT/'xmodel'/f'{tag}.run.v2').read_text().splitlines())
    need(all(r[k] == v for k, v in {'final_status':'DONE', 'exit_code':'0',
         'report_state':'BODY_SEALED', 'seal_boundary':'CLEAN', 'charge_basis_status':'ABSENT'}.items()), 'receipt '+tag)
    for i in range(1, int(r['charged_inputs'])+1):
        name = r[f'charged_input_{i}']
        pins[name] = r[f'charged_input_{i}_sha256']
        need(r[f'charged_input_{i}_post'] == 'UNCHANGED', 'post input '+name)
        p = Path(r['lane_inputs_dir'])/r[f'charged_input_{i}_basename']
        snapshots[name] = 'REMOVED; current and terminal-post pins checked'
        if p.exists():
            need(sha(p.read_bytes()) == pins[name], 'snapshot '+name)
            snapshots[name] = 'MATCH'
    for key in ('prompt','adapter','launcher','sandbox_profile','charge_basis_validator',
                'seal_tool','fallacy','model_prompt'):
        need(r[key+'_sha256'] == r['post_'+key+'_sha256'], 'runtime drift '+key)
    pins[r['report']] = r['report_sha256']
for name, digest in {
    'xmodel/d125-defect-order-engineering-astra-20260907.md':'4e765fc31900e73124335f4ca9069149085ea1580e1e63174af503c9346c25cb',
    'box/d125-defect-order-engineering-20260907/remote-custody.json':'f9a1b62d4ef67855c126d963a967693901f72e5ea499c1da95c7b464f051002b',
    'box/d125-defect-order-engineering-20260907/root_replay.py':'f388d9ec0bb2ebd3209c0eea03c78aa722c14cdec952a4aa5cd2586417e1faec',
    'box/d125-defect-order-engineering-20260907/engineering.py':'4600cddd7d5cb69cd9f1c1fb658bacaf936596c9a9a09c3efb34069f0f52bade',
    'box/d125-defect-order-engineering-20260907/REGISTRATION.md':'4a2566914d1ea0a372387e0306988b3dd6ea22c154764ee72691a77a26f0b8f8',
}.items():
    pins[name] = digest
def verify():
    for name, digest in pins.items():
        need(sha((ROOT/name).read_bytes()) == digest, 'pin '+name)
verify()
custody = json.loads((ENG/'remote-custody.json').read_bytes())
for name, row in custody['files'].items():
    path = ENG/'evidence'/name
    need(len(path.read_bytes()) == row['bytes'], 'byte count '+name)
    pins[str(path.relative_to(ROOT))] = row['sha256']
for path in (SOL/'gate_check.py', SOL/'run_controls.py', ENG/'root_replay.py',
             ENG/'engineering.py', CODE/'exact.py', CODE/'driver.py', CODE/'defect_order.py',
             Path(__file__)):
    need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(path.read_bytes()))), 'Assert '+str(path))
    pins[str(path.relative_to(ROOT))] = sha(path.read_bytes())
for path in (SOL/'normal.json', SOL/'optimized.json', SOL/'run.json'):
    pins[str(path.relative_to(ROOT))] = sha(path.read_bytes())
verify()
def cap():
    resource.setrlimit(resource.RLIMIT_CPU, (25,25))
    resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
    resource.setrlimit(resource.RLIMIT_FSIZE, (64*1024**2,)*2)
    resource.setrlimit(resource.RLIMIT_CORE, (0,0))
runs = []
start = time.monotonic()
for flags in ([], ['-O']):
    for label, script, args in (
        ('sol', SOL/'gate_check.py', ['--inputs', str(CODE)]),
        ('engineering', ENG/'root_replay.py', []),
    ):
        argv = [sys.executable, '-I', '-B', *flags, str(script), *args]
        p = subprocess.run(argv, capture_output=True, timeout=30, preexec_fn=cap)
        need(p.returncode == 0 and p.stderr == b'', label+' failed '+p.stderr.decode(errors='replace'))
        result = json.loads(p.stdout)
        if label == 'sol':
            need(result['status'] == 'PASS' and result['checks'] == 39, 'Sol checks')
        else:
            need(result['status'] == 'LOCAL_ACTUAL_EVIDENCE_REPLAY_PASS' and result['files_verified'] == 49, 'actual checks')
        runs.append({'label':label, 'flags':flags, 'argv':argv, 'result':result,
                     'stdout_sha256':sha(p.stdout), 'stderr_sha256':sha(p.stderr)})
verify()
record = {'status':'PASS', 'pins':pins, 'snapshots':snapshots, 'runs':runs,
          'wall_seconds':time.monotonic()-start, 'assert_nodes':0,
          'scope':'Sol delta and engineering tiny controls only; Fable receipt/pins only, not yet root replayed; no CAS/full source'}
with (OUT/'harvest.json').open('x') as f:
    json.dump(record, f, sort_keys=True, indent=2)
    f.write('\n')
print(json.dumps({'status':'PASS', 'pins':len(pins), 'runs':len(runs),
                  'wall_seconds':record['wall_seconds'], 'receipt_sha256':sha((OUT/'harvest.json').read_bytes())}))
