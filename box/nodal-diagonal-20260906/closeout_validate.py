#!/usr/bin/env python3
"""Validate retained receipts and seal; does not claim an ideal certificate."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
REPORT = ROOT / 'xmodel/nodal-diagonal-astra-20260906.md'

def digest(path):
    return sha256(path.read_bytes()).hexdigest()

def read(name):
    return json.loads((HERE / name).read_text())

def bind(data, key, name):
    assert data[key] == digest(HERE / name), (key, name)

body = REPORT.read_bytes()
assert 12000 <= len(body) <= 25000
assert body.count(b'<!-- BODY-END -->') == 1
assert body.endswith(b'<!-- BODY-END -->\n')
assert b'PENDING' not in body
for row in (HERE / 'inputs.sha256').read_text().splitlines():
    expected, path = row.split(maxsplit=1)
    assert digest(Path(path.strip())) == expected

controls = read('exact_controls.json')
bind(controls, 'driver_sha256', 'exact_controls.py')
assert all(controls[k] for k in ['diagonal_identity', 'first_strip_identity',
                               'second_strip_division_exact', 'target_inverse_identity'])
assert controls['3']['all_rows_exact_Q'] and controls['4']['all_rows_exact_Q']
assert [controls['3']['rank_Q'], controls['4']['rank_Q']] == [17, 22]
assert [controls['3']['e_over_C'], controls['4']['e_over_C']] == [1, -1]
bits = [int(x) for x in re.findall(r'_unit_bit=(\d)',
        (HERE / 'localization_controls.log').read_text())]
assert bits == [0, 1, 0, 1, 0, 1]

source_rows = {}
for client in ['99_delta2', '99_delta52', '108']:
    data = read('source-' + client + '.json')
    assert data['status'] == 'COMPLETE_CIRCUIT_NO_IDEAL_DECISION'
    bind(data, 'driver_sha256', 'source_stream.py')
    bind(data, 'recurrence_driver_sha256', 'recurrence_stream.py')
    source_rows[client] = data['rows']
assert list(source_rows.values()) == [52893, 53672, 75111]

source_controls = read('source_controls.json')
bind(source_controls, 'driver_sha256', 'source_controls.py')
for row in source_controls['controls']:
    assert all(value is True for key, value in row.items() if key != 'client')

prefixes = []
for name, depth in [('expanded_q_attempt', 27), ('flint_q_attempt', 48),
                    ('fast_q_attempt', 58)]:
    data = read(name + '.json')
    bind(data, 'driver_sha256', name + '.py')
    assert data['unit_candidate'] is None
    assert data['remaining_residual_count'] == 0
    assert int(data['blocks'][-1]['name'].rsplit('_', 1)[1]) == depth
    prefixes.append({'driver': name, 'completed_prefix': depth,
                     'cpu_seconds': data['cpu_seconds'],
                     'max_rss_KiB': data['max_rss_KiB']})

assert not any(p.is_dir() for p in HERE.iterdir())
retained_bytes = len(body) + sum(p.stat().st_size for p in HERE.iterdir())
assert retained_bytes < 2_000_000
now = datetime.now(timezone.utc)
start = datetime.fromisoformat('2026-09-06T00:28:59+00:00')
assert (now - start).total_seconds() < 200 * 60
result = {
    'status': 'SEALED_EXACT_Q_OPEN_NO_BRANCH_PROMOTION',
    'clients': {k: 'EXACT_Q_OPEN' for k in source_rows},
    'source_rows': source_rows,
    'localization_control_unit_bits': bits,
    'input_hashes_passed': 7,
    'report_bytes': len(body), 'report_sha256': digest(REPORT),
    'closed_utc': now.isoformat(),
    'elapsed_minutes': (now - start).total_seconds() / 60,
    'expansion_attempts': prefixes,
    'aggregate_CPU_accounting_upper_seconds': 3460,
    'CPU_accounting_basis': {'boundary_agent_upper': 1250,
                            'three_expansion_caps': 1800,
                            'root_construction_and_repeats_upper': 310,
                            'remaining_controls_and_allowance': 100},
    'retained_bytes_before_this_receipt_and_manifest': retained_bytes,
    'driver_sha256': digest(Path(__file__)),
}
(HERE / 'closeout.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
