#!/usr/bin/env python3
"""Independent tiny controls only; no CAS, solver, worker, or production stream."""
import ast
import copy
from fractions import Fraction as F
import json
from pathlib import Path
import sys
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'copy'))
import exact as E
import hybrid as H
import driver as D

V = ['x', 'y', 'k', 'z']
TEXTS = ['0', 'x/2', '0', 'x/2', '1-x', '0', 'k*z-1']
EXPECTED_PINS = {
    'exact.py': '7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9',
    'hybrid.py': 'c9755a7172eaa7f1393860931d55c38a0b9d79b5b170eadbf14baff0203c35a3',
    'driver.py': 'faf7a1e08fa7fafac09160b57587eb325ef4542da30a7defbf5165bc329569d9',
}


def need(condition, reason):
    if not condition:
        raise RuntimeError(reason)


def wire(poly):
    return [[[[str(c.numerator), str(c.denominator)], ['0', '1']], list(m)]
            for m, c in sorted(poly.items())]


def pack(records):
    records = copy.deepcopy(records)
    prefix = b''.join(E.canonical(r) for r in records[:-1])
    records[-1]['prefix_sha256'] = E.digest(prefix)
    return prefix + E.canonical(records[-1])


def fixture(texts=TEXTS, variables=V):
    records = [
        {'type': 'header', 'schema': 'jc2.hybrid-affine/v1', 'field': 'Q',
         'order': 'dp', 'target': H.TARGET, 'source_sha256': H.ORIGINAL_SHA,
         'variables': variables, 'original_variables': variables},
        {'type': 'coefficient_map', 'member': 'A', 'source_entry': {'name': 'TOY'},
         'terms': wire(E.polynomial(variables[0], variables))},
        {'type': 'graph', 'member': 'A', 'degree': 1, 'pivots': [[0, 1]],
         'inverse': [[['1', '1']]]},
    ]
    rows = [E.polynomial(text, variables) for text in texts]
    for index, row in enumerate(rows):
        records.append({
            'type': 'row',
            'original_index': index if index < len(rows) - 1 else None,
            'label': 'R/' + str(index) if index < len(rows) - 1 else 'UNIT/kz',
            'terms': wire(row),
            'old_from_new_ell_power': 0,
            'guard_power': 1 if index == len(rows) - 1 else 0,
            'guard_cofactor': wire(E.ONE if index == len(rows) - 1 else {}),
        })
    records.append({
        'type': 'footer', 'complete': True, 'rows': len(rows),
        'original_rows': len(rows) - 1, 'terms': sum(map(len, rows)),
        'zero_original_rows': sum(not row for row in rows[:-1]),
        'coefficient_map_terms': 1,
    })
    return pack(records)


def records(data):
    return [E.strict_json(line) for line in data.splitlines()]


def certificate(data, engine, basis, cofactors=None, variables=V):
    lines = ['JC2CERT 1 ' + E.digest(data) + ' ' + E.ring_id(variables),
             'I_SIZE ' + str(sum(bool(E.polynomial(t, variables)) for t in engine))]
    blocks = [('I', engine), ('G', basis)]
    if cofactors is not None:
        blocks.append(('T', cofactors))
    for name, values in blocks:
        lines.append(name + '_BEGIN ' + str(len(values)))
        lines.extend(name + ' ' + str(i + 1) + ' ' + value
                     for i, value in enumerate(values))
        lines.append(name + '_END')
    if cofactors is None:
        lines.append('END NONUNIT')
    else:
        lines.extend(['CHECK 1', 'END UNIT'])
    return ('\n'.join(lines) + '\n').encode('ascii')


def expect_value_error(results, name, function, fragment=None):
    try:
        function()
    except ValueError as exc:
        message = str(exc)
        need(fragment is None or fragment in message,
             name + ': wrong rejection: ' + message)
        results[name] = {'status': 'PASS', 'gate': message}
        return
    raise RuntimeError(name + ': mutation was accepted')


def rebound_stale_output(changed, old_engine=TEXTS, variables=V):
    return certificate(changed, old_engine, ['1'],
                       ['0', '1', '0', '1', '1', '0', '0'], variables)


def main():
    results = {}
    for name, wanted in EXPECTED_PINS.items():
        got = E.digest((HERE / 'copy' / name).read_bytes())
        need(got == wanted, 'copy pin mismatch: ' + name)
    results['private_copy_pins'] = {'status': 'PASS', 'pins': EXPECTED_PINS}

    base = fixture()
    variables, rows, labels, singular_prefix = H.read_hybrid(base)
    need(variables == V and len(rows) == len(TEXTS) and labels[-1] == 'UNIT/kz',
         'base dimensions/labels')
    pieces = singular_prefix.split('ideal I=\n', 1)[1][:-2].split(',\n')
    for piece, row in zip(pieces, rows):
        need(E.polynomial(piece.split('\n', 1)[1], variables) == row,
             'serializer roundtrip')
    need('+-1*x' in singular_prefix, 'signed ordinary form not exercised')
    results['literal_roundtrip_signed_zero_duplicate'] = {
        'status': 'PASS', 'variables': len(variables), 'rows': len(rows),
        'bytes_without_engine_footer': len(singular_prefix.encode('ascii')),
    }

    good = certificate(base, TEXTS, ['1'], ['0', '1', '0', '1', '1', '0', '0'])
    verdict, mapping, unused_labels = H.checked_certificate(base, good, b'')
    need(verdict == 'EXACT_Q_UNIT_COFACTOR_CERTIFICATE' and
         mapping == [0, 1, 0, 1, 4, 0, 6], 'valid unit/mapping')
    results['unit_full_slot_mapping'] = {'status': 'PASS', 'mapping': mapping}
    expect_value_error(results, 'unit_cofactor',
                       lambda: H.checked_certificate(base,
                           good.replace(b'T 5 1\n', b'T 5 2\n'), b''), 'not one')

    proper_data = fixture(['x^2', 'x*y', 'k*z-1'])
    proper = certificate(proper_data, ['x^2', 'x*y', 'k*z-1'],
                         ['x', 'k*z-1'])
    need(H.checked_certificate(proper_data, proper, b'')[0] ==
         'EXACT_Q_PROPER_SUPERIDEAL_CERTIFICATE', 'valid proper certificate')
    results['proper_superideal'] = {'status': 'PASS'}
    false_data = fixture(['x^2', 'x*y-1', 'k*z-1'])
    false_output = certificate(false_data, ['x^2', 'x*y-1', 'k*z-1'],
                               ['x^2', 'x*y-1', 'k*z-1'])
    expect_value_error(results, 'proper_false_basis',
                       lambda: H.checked_certificate(false_data, false_output, b''),
                       'Buchberger')

    changed = records(base)
    changed[0]['source_sha256'] = 'a' * 64
    expect_value_error(results, 'source_binding', lambda: H.read_hybrid(pack(changed)),
                       'original source binding')
    changed = records(base)
    changed[0]['target'] = 'J-5*k^3*g^2/9'
    expect_value_error(results, 'target_sign_binding', lambda: H.read_hybrid(pack(changed)),
                       'schema/field/order/target')

    changed = records(base)
    changed[7]['terms'] = wire(E.polynomial('1+x', V))
    changed = pack(changed)
    H.read_hybrid(changed)
    expect_value_error(results, 'row_sign_rebound_stale_I',
                       lambda: H.checked_certificate(changed,
                           rebound_stale_output(changed), b''),
                       'engine equation not original')

    changed_records = records(base)
    changed_records[3]['terms'] = wire(E.polynomial('y', V))
    changed_records[-1]['terms'] += 1
    changed_records[-1]['zero_original_rows'] -= 1
    changed = pack(changed_records)
    H.read_hybrid(changed)
    expect_value_error(results, 'changed_zero_resynced_rebound_stale_I',
                       lambda: H.checked_certificate(changed,
                           rebound_stale_output(changed), b''), 'absent')

    changed_records = records(base)
    changed_records.pop(7)
    for index, row_record in enumerate(changed_records[3:-2]):
        row_record['original_index'] = index
        row_record['label'] = 'R/' + str(index)
    changed_records[-1]['rows'] -= 1
    changed_records[-1]['original_rows'] -= 1
    changed_records[-1]['terms'] -= 2
    changed = pack(changed_records)
    H.read_hybrid(changed)
    stale_engine = ['0', 'x/2', '0', 'x/2', '1-x', '0', 'k*z-1']
    stale_cofactors = ['0', '1', '0', '1', '1', '0', '0']
    stale = certificate(changed, stale_engine, ['1'], stale_cofactors)
    expect_value_error(results, 'row_omission_fully_resynced_rebound_stale_I',
                       lambda: H.checked_certificate(changed, stale, b''),
                       'engine equation not original')

    changed_records = records(base)
    changed_records[7]['terms'] = wire(E.polynomial('1-x/2', V))
    changed = pack(changed_records)
    H.read_hybrid(changed)
    expect_value_error(results, 'wrong_canonical_rational_rebound_stale_I',
                       lambda: H.checked_certificate(changed,
                           rebound_stale_output(changed), b''),
                       'engine equation not original')
    changed_records = records(base)
    changed_records[4]['terms'][0][0][0] = ['2', '4']
    expect_value_error(results, 'noncanonical_rational_wire',
                       lambda: H.read_hybrid(pack(changed_records)),
                       'noncanonical rational')
    changed_records = records(base)
    changed_records[4]['terms'][0][0][1] = ['1', '3']
    expect_value_error(results, 'golden_component',
                       lambda: H.read_hybrid(pack(changed_records)),
                       'golden coefficient/splitting forbidden')

    changed_records = records(base)
    changed_records[1]['terms'] = wire(E.polynomial('y', V))
    changed = pack(changed_records)
    H.read_hybrid(changed)
    expect_value_error(results, 'stale_certificate_source_metadata',
                       lambda: H.checked_certificate(changed, good, b''),
                       'header mismatch')

    swapped = records(base)
    swapped[0]['variables'] = ['y', 'x', 'k', 'z']
    swapped = pack(swapped)
    swapped_variables = ['y', 'x', 'k', 'z']
    H.read_hybrid(swapped)
    swapped_stale = certificate(swapped, TEXTS, ['1'],
                                ['0', '1', '0', '1', '1', '0', '0'],
                                swapped_variables)
    expect_value_error(results, 'variable_order_image_rebound_stale_I',
                       lambda: H.checked_certificate(swapped, swapped_stale, b''),
                       'engine equation not original')

    observed = {'system': 'Linux', 'vendor': 'Amazon EC2', 'instance': D.INSTANCE,
                'cwd': D.CWD, 'boot': 'toy-boot', 'now': 100.0}
    pins = {'toy': 'pin'}
    authority = {
        'schema': 'jc2.d125-hybrid81-solver-authority/v1', 'root_green': True,
        'mode': 'engineering_control', 'job_id': 'toy', 'pins': pins,
        'caps': D.CAPS, 'instance_id': D.INSTANCE, 'cwd': D.CWD,
        'boot_id': 'toy-boot', 'started_utc': '1970-01-01T00:01:30Z',
        'deadline_utc': '1970-01-01T00:03:00Z',
    }
    need(D.authority_check(authority, 'control', observed, pins) == 10,
         'control authority pass')
    expect_value_error(results, 'authority_engineering_to_decision',
                       lambda: D.authority_check(authority, 'decision', observed, pins),
                       'authority separation')
    expect_value_error(results, 'authority_engineering_to_verify',
                       lambda: D.authority_check(authority, 'verify', observed, pins),
                       'authority separation')
    solver = dict(authority)
    solver.update({'mode': 'solver', 'full_stream_gate_accepted': True})
    solver.update({name: 'c' * 64 for name in
                   ('full_stream_gate_sha256', 'engine_index_control_sha256',
                    'output_limit_control_sha256', 'descendant_control_sha256')})
    need(D.authority_check(solver, 'decision', observed, pins) == 80 and
         D.authority_check(solver, 'verify', observed, pins) == 80,
         'solver authority pass')
    expect_value_error(results, 'authority_solver_to_control',
                       lambda: D.authority_check(solver, 'control', observed, pins),
                       'authority separation')

    for module in (E, H, D):
        tree = ast.parse(Path(module.__file__).read_text())
        need(not any(isinstance(node, ast.Assert) for node in ast.walk(tree)),
             'Assert gate in ' + module.__name__)
    own_tree = ast.parse(Path(__file__).read_text())
    need(not any(isinstance(node, ast.Assert) for node in ast.walk(own_tree)),
         'Assert gate in own controls')
    results['no_assert_enforcement'] = {'status': 'PASS'}

    footer = D.footer(V, 'a' * 64)
    need(footer.count('slimgb(I)') == 1 and 'lift(I,ideal(1))' in footer and
         'ncols(matrix(I))' in footer and 'ncols(matrix(G))' in footer,
         'footer algorithm drift')
    need('slimgb' not in D.control_input(), 'control invoked solver')
    need(len((singular_prefix + footer).encode('ascii')) <= 2 * 1024**2,
         'toy generated input cap')
    results['footer_and_including_suffix_cap_toy'] = {
        'status': 'PASS',
        'bytes': len((singular_prefix + footer).encode('ascii')),
    }

    driver_text = Path(D.__file__).read_text()
    publish = driver_text.index("write_new(phase+'.result.json'")
    postcheck = driver_text.index("E.need(after == {'jsonl': H.CONSTRUCTION_SHA}")
    need(publish < postcheck, 'posthash publication ordering unexpectedly repaired')
    need("receipt['source_pins_after']" not in driver_text,
         'verify source-pins check unexpectedly present')
    results['posthash_receipt_bypass_present'] = {
        'status': 'BUG_CONFIRMED',
        'gate': 'result published before post-hash acceptance and verify ignores source_pins_after',
    }

    deadline_authority = dict(solver)
    deadline_authority['deadline_utc'] = '1970-01-01T00:07:20Z'
    old_allowance = D.authority_check(deadline_authority, 'decision', observed, pins)
    late_observed = dict(observed)
    late_observed['now'] = 439.0
    fresh_allowance = D.authority_check(deadline_authority, 'decision', late_observed, pins)
    need((old_allowance, fresh_allowance) == (300, 1), 'deadline toy allowances')
    launch_body = driver_text[driver_text.index('def launch('):driver_text.index('def main(')]
    payload_body = driver_text[driver_text.index('def payload('):driver_text.index('def launch(')]
    need("'--wall-seconds', str(duration)" in launch_body and
         'a, authority_sha, duration = context(authority_path, phase)' in payload_body and
         'duration' not in payload_body.split('a, authority_sha, duration = context(authority_path, phase)', 1)[1],
         'deadline handoff unexpectedly repaired')
    results['deadline_handoff_stale_allowance_present'] = {
        'status': 'BUG_CONFIRMED', 'launch_allowance': old_allowance,
        'fresh_payload_allowance': fresh_allowance,
        'gate': 'payload recomputes but does not enforce fresh allowance',
    }

    output = {'schema': 'jc2.sol56.hybrid81-gate-controls/v1',
              'mode': 'optimized' if not __debug__ else 'normal',
              'tests': results, 'test_count': len(results)}
    print(json.dumps(output, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
