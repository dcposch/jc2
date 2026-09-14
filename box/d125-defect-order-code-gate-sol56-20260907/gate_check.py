#!/usr/bin/env python3
"""Independent tiny strict-delta checks; no CAS and no production source reads."""
import argparse
import ast
import copy
import json
from pathlib import Path
import sys


class GateFailure(RuntimeError):
    pass


def need(condition, reason):
    if not condition:
        raise GateFailure(reason)


def expect_value(label, fragment, action, outcomes):
    try:
        action()
    except ValueError as exc:
        need(fragment in str(exc), label+': wrong exception: '+str(exc))
        outcomes.append(label)
        return
    raise GateFailure(label+': missing live ValueError')


def source_fixture(E, variables, expressions):
    records = [{'type': 'header', 'field': 'Q',
                'order': 'global degree reverse lexicographic, displayed variable order',
                'expected_rows': len(expressions), 'expected_variables': len(variables)}]
    records += [{'type': 'variable', 'id': i, 'name': name}
                for i, name in enumerate(variables)]
    for i, expression in enumerate(expressions):
        terms = []
        for monomial, coefficient in sorted(E.polynomial(expression, variables).items()):
            terms.append([[[str(coefficient.numerator), str(coefficient.denominator)],
                           ['0', '1']], list(monomial)])
        records.append({'type': 'row', 'label': 'R/'+str(i), 'terms': terms})
    prefix = b''.join(E.canonical(record) for record in records)
    footer = {'type': 'footer', 'complete': True, 'prefix_sha256': E.digest(prefix),
              'prefix_records': len(records), 'counts': {'rows': len(expressions)}}
    data = prefix+E.canonical(footer)
    pieces = ['// R/'+str(i)+'\n'+expression for i, expression in enumerate(expressions)]
    literal = ('ring R=0,('+','.join(variables)+'),dp;\nideal I=\n'+
               ',\n'.join(pieces)+E.ENDING).encode('ascii')
    return data, literal


def result_fixture(E, variables, source_hash, order, engine, basis, cofactors=None):
    nonzero = sum(bool(E.polynomial(row, variables)) for row in engine)
    lines = ['JC2CERT 1 '+source_hash+' '+E.ring_id(variables, order),
             'I_SIZE '+str(nonzero), 'I_BEGIN '+str(len(engine))]
    lines += ['I '+str(i)+' '+row for i, row in enumerate(engine, 1)]
    lines += ['I_END', 'G_BEGIN '+str(len(basis))]
    lines += ['G '+str(i)+' '+row for i, row in enumerate(basis, 1)]
    lines.append('G_END')
    if cofactors is not None:
        lines.append('T_BEGIN '+str(len(cofactors)))
        lines += ['T '+str(i)+' '+row for i, row in enumerate(cofactors, 1)]
        lines += ['T_END', 'CHECK 1', 'END UNIT']
    else:
        lines.append('END NONUNIT')
    return ('\n'.join(lines)+'\n').encode('ascii')


def run(inputs):
    inputs = inputs.resolve()
    need(inputs.is_dir(), 'frozen input directory missing')
    sys.path.insert(0, str(inputs))
    import defect_order as O
    import exact as E
    import driver as D

    outcomes = []
    here = Path(__file__).resolve().parent
    for path in (inputs/'exact.py', inputs/'driver.py', inputs/'defect_order.py',
                 inputs/'test_order.py', here/'gate_check.py', here/'run_controls.py'):
        tree = ast.parse(path.read_text(encoding='utf-8'))
        need(not any(isinstance(node, ast.Assert) for node in ast.walk(tree)),
             'Assert statement: '+str(path))
    outcomes.append('ast_no_assert')

    exact_tree = ast.parse((inputs/'exact.py').read_text(encoding='utf-8'))
    functions = {node.name: node for node in exact_tree.body if isinstance(node, ast.FunctionDef)}
    key_calls = [node for node in ast.walk(exact_tree) if isinstance(node, ast.Call)
                 and isinstance(node.func, ast.Name) and node.func.id == 'key']
    need(len(key_calls) == 4 and all(len(node.args) == 3 and
         isinstance(node.args[2], ast.Name) and node.args[2].id == 'weights'
         for node in key_calls), 'not every leading-term key receives weights')
    nf_calls = [node for node in ast.walk(functions['proper_certificate'])
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == 'normal_form']
    need(len(nf_calls) == 3 and all(len(node.args) == 4 and
         isinstance(node.args[3], ast.Name) and node.args[3].id == 'weights'
         for node in nf_calls), 'not every certificate NF receives weights')
    driver_tree = ast.parse((inputs/'driver.py').read_text(encoding='utf-8'))
    proper_calls = [node for node in ast.walk(driver_tree) if isinstance(node, ast.Call)
                    and isinstance(node.func, ast.Attribute)
                    and node.func.attr == 'proper_certificate']
    need(len(proper_calls) == 1 and len(proper_calls[0].args) == 4,
         'production properness call lacks explicit weights')
    outcomes.append('static_all_weight_paths')

    variables = ['x', 'y', 'z']
    weights = [[3, 1, 4], [1, 0, 1], [1, 0, 1]]
    order = O.descriptor(variables, weights)
    graph = [E.polynomial(text, variables) for text in ('x-y^2', 'z-y^3')]
    leads = [max(row, key=lambda monomial: E.key(monomial, 3, weights)) for row in graph]
    need(leads == [(0,), (2,)], 'weighted graph leaders')
    seen_key, seen_nf = [], []
    original_key, original_nf = E.key, E.normal_form
    def tracked_key(monomial, nvars, supplied=()):
        seen_key.append(copy.deepcopy(supplied))
        return original_key(monomial, nvars, supplied)
    def tracked_nf(polynomial, basis, nvars, supplied=()):
        seen_nf.append(copy.deepcopy(supplied))
        return original_nf(polynomial, basis, nvars, supplied)
    E.key, E.normal_form = tracked_key, tracked_nf
    try:
        verdict = E.proper_certificate(graph, graph, 3, weights)
    finally:
        E.key, E.normal_form = original_key, original_nf
    need('PROPER' in verdict and len(seen_nf) == 4 and seen_key and
         all(item == weights for item in seen_nf+seen_key),
         'dynamic weight propagation through Buchberger/NF')
    expect_value('graph_dp_reject', 'Buchberger',
                 lambda: E.proper_certificate(graph, graph, 3), outcomes)
    changed_graph_weights = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
    expect_value('graph_changed_vector_reject', 'Buchberger',
                 lambda: E.proper_certificate(graph, graph, 3, changed_graph_weights), outcomes)
    outcomes.append('weighted_graph_accept')

    names = ['x', 'y', 'z', 't', 'u']
    levels = O.descriptor(names, [[2, 1, 2, 2, 2], [1, 0, 0, 1, 0],
                                  [1, 0, 0, 0, 0]])
    for label, high, low in [('W1', 'x', 'y'), ('W2', 'x', 'z'),
                             ('W3', 'x', 't'), ('degree', 'y^2', 'z'),
                             ('dp', 'z', 'u')]:
        hm = next(iter(E.polynomial(high, names)))
        lm = next(iter(E.polynomial(low, names)))
        need(E.key(hm, 5, levels['weight_rows']) > E.key(lm, 5, levels['weight_rows']),
             label+' comparator')
        outcomes.append('level_'+label)

    need(E.ring_id(variables, order) == E.digest(E.canonical(order)), 'order digest')
    tiny = O.descriptor(['a', 'b'], [[1, 1], [0, 1], [0, 0]])
    need(O.ring_declaration(tiny) == 'ring R=0,(a,b),(a(1,1),a(0,1),a(0,0),dp);\n',
         'tiny descriptor serialization')
    expect_value('nine_variable_descriptor_reject', 'pinned production',
                 lambda: O.descriptor(['v'+str(i) for i in range(9)],
                                      [[1]*9, [0]*9, [0]*9]), outcomes)
    expect_value('fake_production_descriptor_reject', 'pinned production',
                 lambda: O.descriptor(['v'+str(i) for i in range(269)],
                                      [[1]*269, [0]*269, [0]*269]), outcomes)
    expect_value('fake_fixed_names_reject', 'identity/order drift',
                 lambda: O.fixed(['v'+str(i) for i in range(269)]), outcomes)

    data, literal = source_fixture(E, ['x', 'y'], ['0', 'x^2-y', '0', '1-x', '0'])
    source_vars, source_rows, labels, original = E.read_source(data, literal)
    need(source_vars == ['x', 'y'] and len(source_rows) == 5 and len(labels) == 5,
         'tiny source parse')
    expected_original = literal.decode('ascii')[:-len(E.ENDING)]+';\n'
    need(original == expected_original and original.startswith('ring R=0,(x,y),dp;\n'),
         'read_source did not preserve original dp prefix')
    source_order = O.descriptor(source_vars, [[3, 1], [1, 0], [1, 0]])
    executed = O.adapt_prefix(original, source_vars, source_order)
    O.check_prefix(original, executed, source_vars, source_order)
    need(original.partition('\n')[2] == executed.partition('\n')[2], 'non-ring suffix changed')
    for label, damaged in (
            ('prefix_vector', executed.replace('a(3,1)', 'a(3,2)', 1)),
            ('prefix_row', executed.replace('x^2-y', 'x^2+y', 1)),
            ('prefix_omitted_row', executed.replace('// R/2\n0,\n', '', 1)),
            ('prefix_append', executed+'quit;\n')):
        expect_value(label+'_reject', 'suffix drift',
                     lambda damaged=damaged: O.check_prefix(original, damaged, source_vars, source_order),
                     outcomes)
    expect_value('non_dp_original_reject', 'dp source prefix',
                 lambda: O.adapt_prefix(original.replace(',dp;', ',lp;', 1),
                                        source_vars, source_order), outcomes)
    outcomes.append('source_and_first_line_adapter')

    unit_names = ['x', 'y']
    unit_order = O.descriptor(unit_names, [[3, 1], [1, 0], [1, 0]])
    engine_text = ['0', 'x', '0', 'x', '1-x', '0']
    raw = result_fixture(E, unit_names, 'a'*64, unit_order, engine_text, ['1'],
                         ['0', '0', '0', '1', '1', '0'])
    engine, basis, cofactors = E.parse_result(raw, b'', unit_names, 'a'*64, unit_order)
    source = [E.polynomial(text, unit_names) for text in engine_text]
    unit_verdict, mapping, lifted = E.unit_certificate(source, engine, cofactors)
    need('UNIT' in unit_verdict and mapping == [0, 1, 0, 1, 4, 0] and len(lifted) == 6,
         'zero/duplicate full-row mapping')
    expect_value('stderr_whitespace_reject', 'nonempty stderr',
                 lambda: E.parse_result(raw, b' \n\t', unit_names, 'a'*64, unit_order), outcomes)
    expect_value('isize_reject', 'nonzero count',
                 lambda: E.parse_result(raw.replace(b'I_SIZE 3', b'I_SIZE 0', 1), b'',
                                        unit_names, 'a'*64, unit_order), outcomes)
    expect_value('dp_header_reject', 'header mismatch',
                 lambda: E.parse_result(raw, b'', unit_names, 'a'*64), outcomes)
    changed_order = copy.deepcopy(unit_order)
    changed_order['weight_rows'][2][0] += 1
    expect_value('vector_header_reject', 'header mismatch',
                 lambda: E.parse_result(raw, b'', unit_names, 'a'*64, changed_order), outcomes)
    expect_value('source_header_reject', 'header mismatch',
                 lambda: E.parse_result(raw, b'', unit_names, 'b'*64, unit_order), outcomes)
    damaged_raw = raw.replace(b'T 4 1', b'T 4 2', 1)
    damaged_engine, unused_basis, damaged_cofactors = E.parse_result(
        damaged_raw, b'', unit_names, 'a'*64, unit_order)
    expect_value('cofactor_reject', 'not one',
                 lambda: E.unit_certificate(source, damaged_engine, damaged_cofactors), outcomes)
    x, y = E.polynomial('x', unit_names), E.polynomial('y', unit_names)
    expect_value('unit_omitted_original_reject', 'absent from engine',
                 lambda: E.engine_map([x, y], [x]), outcomes)
    expect_value('unit_changed_engine_reject', 'not original',
                 lambda: E.engine_map([x, y], [E.polynomial('x+y', unit_names)]), outcomes)
    outcomes.append('strict_stream_and_full_unit_rows')

    false_basis = [E.polynomial('x*y-1', unit_names), E.polynomial('x^2', unit_names)]
    need(E.normal_form(E.ONE, false_basis, 2, unit_order['weight_rows']) == E.ONE and
         all(not E.normal_form(row, false_basis, 2, unit_order['weight_rows'])
             for row in false_basis), 'false-proper premise fixture')
    expect_value('falseproper_buchberger_reject', 'Buchberger',
                 lambda: E.proper_certificate(false_basis, false_basis, 2,
                                              unit_order['weight_rows']), outcomes)
    expect_value('proper_omitted_original_reject', 'original equation missing',
                 lambda: E.proper_certificate([x, y], [x], 2, unit_order['weight_rows']), outcomes)

    observed = {'system': 'Linux', 'vendor': 'Amazon EC2', 'instance': D.INSTANCE,
                'cwd': D.CWD, 'boot': 'fixture-boot', 'now': 100.0}
    expected_pins = {'fixture': 'new-job-pin'}
    authority = {'schema': D.AUTHORITY_SCHEMA, 'root_green': True,
                 'execution_order_sha256': O.ORDER_SHA, 'mode': 'solver',
                 'job_id': 'fresh-defect-order-job', 'pins': expected_pins, 'caps': D.CAPS,
                 'instance_id': D.INSTANCE, 'cwd': D.CWD, 'boot_id': 'fixture-boot',
                 'started_utc': '1970-01-01T00:01:30Z',
                 'deadline_utc': '1970-01-01T00:03:00Z',
                 'full_stream_gate_accepted': True, 'order_gate_accepted': True}
    for field in ('full_stream_gate_sha256', 'engine_index_control_sha256',
                  'output_limit_control_sha256', 'descendant_control_sha256',
                  'order_gate_sha256', 'order_engine_control_sha256'):
        authority[field] = 'c'*64
    need(D.authority_check(authority, 'decision', observed, expected_pins) == 80,
         'valid solver authority fixture')
    authority_cases = (
        ('blank_job', {**authority, 'job_id': ' '}),
        ('old_schema', {**authority, 'schema': 'jc2.d125-exact-solver-authority/v1'}),
        ('old_cwd', {**authority, 'cwd': '/home/ubuntu/d125-small-exact-solver-20260907'}),
        ('old_job_pins', {**authority, 'pins': {'fixture': 'old-job-pin'}}),
        ('control_mode', {**authority, 'mode': 'engineering_control'}),
        ('wrong_order', {**authority, 'execution_order_sha256': 'd'*64}),
        ('missing_order_gate', {**authority, 'order_gate_accepted': False}),
        ('missing_engine_control', {**authority, 'order_engine_control_sha256': ''}),
    )
    for label, candidate in authority_cases:
        expect_value('authority_'+label+'_reject', '',
                     lambda candidate=candidate: D.authority_check(
                         candidate, 'decision', observed, expected_pins), outcomes)
    outcomes.append('new_job_cwd_authority_separation')

    return {'status': 'PASS', 'checks': len(outcomes), 'outcomes': outcomes,
            'inputs': str(inputs)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(run(args.inputs), sort_keys=True))


if __name__ == '__main__':
    main()
