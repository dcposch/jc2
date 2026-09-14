"""Root/Astra's scoped independent behavior oracle; normal mode, no CAS."""
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import tempfile

resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2,) * 2)
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
root = Path(__file__).resolve().parents[2]
gate = root / 'ops/frontier_gate.py'
source = gate.read_text()
before = hashlib.sha256(gate.read_bytes()).hexdigest()
cases = [
    (['--total-degrees', '99', '66'], 3, 'NOT_CLOSED_BY_THIS_GATE', 'EXCLUDED_BY_EXTERNAL_LT108'),
    (['--total-degrees', '108', '72'], 0, 'NOT_CLOSED_BY_THIS_GATE', 'INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND'),
    (['--total-degrees', '108', '108'], 0, 'NOT_CLOSED_BY_THIS_GATE', 'INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND'),
    (['--total-degrees', '108', '107'], 3, 'REFUSE_CLASSICALLY_CLOSED', 'INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND'),
    (['--total-cap', '107'], 3, 'NOT_CLOSED_BY_THIS_GATE', 'EXCLUDED_BY_EXTERNAL_LT108'),
    (['--total-cap', '108'], 0, 'NOT_CLOSED_BY_THIS_GATE', 'INCONCLUSIVE_BY_EXTERNAL_MAX_BOUND'),
    (['--partial-y-degrees', '99', '66', '--total-unbounded'], 0, 'NOT_CLOSED_BY_THIS_GATE', 'OUT_OF_SCOPE_ACTUAL_TOTAL_UNBOUNDED'),
    (['--total-degrees', '99', '66', '--purpose', 'method-control'], 0, 'NOT_CLOSED_BY_THIS_GATE', 'EXCLUDED_BY_EXTERNAL_LT108'),
]

def failures(path):
    bad = []
    for argv, rc, legacy, conclusion in cases:
        p = subprocess.run([sys.executable, '-B', str(path), *argv, '--tag', 'root-hostile-control'], capture_output=True, text=True, timeout=5)
        d = json.loads(p.stdout)
        expected_overall = ('METHOD_CONTROL_ONLY' if 'method-control' in argv else 'REFUSE_CLASSICALLY_CLOSED') if conclusion.startswith('EXCLUDED') or legacy == 'REFUSE_CLASSICALLY_CLOSED' else 'NOT_CLOSED_BY_THIS_GATE'
        if (p.returncode, d['verdict'], d['conclusion'], d['overall_verdict']) != (rc, legacy, conclusion, expected_overall):
            bad.append(argv)
    return bad

if failures(gate):
    raise RuntimeError('production behavior disagrees with independent oracle')
mutations = {
    'ignore_external': ('overall_closed = gcd_closed or external_closed', 'overall_closed = gcd_closed'),
    'ignore_gcd': ('overall_closed = gcd_closed or external_closed', 'overall_closed = external_closed'),
    'wrong_pair_bound': ('actual_max_degree = max(deg_p, deg_q)', 'actual_max_degree = min(deg_p, deg_q)'),
    'wrong_endpoint': ('return actual_max_degree < EXTERNAL_MIN_ACTUAL_MAX_DEGREE', 'return actual_max_degree <= EXTERNAL_MIN_ACTUAL_MAX_DEGREE'),
}
detected = {}
with tempfile.TemporaryDirectory(prefix='jc2-root-frontier-') as scratch:
    for name, (old, new) in mutations.items():
        if source.count(old) != 1:
            raise RuntimeError('mutation target is not unique: ' + name)
        path = Path(scratch) / (name + '.py')
        path.write_text(source.replace(old, new, 1))
        bad = failures(path)
        if not bad:
            raise RuntimeError('mutation survived: ' + name)
        detected[name] = bad
after = hashlib.sha256(gate.read_bytes()).hexdigest()
if before != after:
    raise RuntimeError('production implementation changed during review')
print(json.dumps({'status': 'PASS_NORMAL_ONLY', 'gate_sha256': before, 'positive_cases': len(cases), 'rejected_source_mutations': detected}, sort_keys=True))
