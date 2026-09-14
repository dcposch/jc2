"""Declared tiny delta controls; no CAS, remote access or full-source arithmetic."""
import ast
import copy
import hashlib
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import defect_order as O
import exact as E
import driver as D
import test_exact as T

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
META = ROOT/'box/d125-defect-order-discriminator-20260907/witnesses.json'
META_SHA = '6e8c0102089ca6d046f4e1834ce30917a1dff6b2ad7d8ab29de95e7fc7eb83a1'
V = ['x', 'y', 'z']
ORDER = O.descriptor(V, [[3, 1, 4], [1, 0, 1], [1, 0, 1]])


def graph():
    return [E.polynomial(t, V) for t in ['x-y^2', 'z-y^3']]


class OrderTests(unittest.TestCase):
    def test_ast_no_assert_and_unchanged_arithmetic_source_parser(self):
        for name in ('exact.py', 'driver.py', 'defect_order.py', 'test_order.py',
                     'test_exact.py', 'run_tests.py'):
            tree = ast.parse((HERE/name).read_text())
            self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(tree)), name)
        old = (ROOT/'box/d125-small-exact-solver-strict-repair-20260907/exact.py').read_text()
        new = (HERE/'exact.py').read_text()
        def functions(source):
            return {node.name: ast.get_source_segment(source, node)
                    for node in ast.parse(source).body if isinstance(node, (ast.FunctionDef, ast.ClassDef))}
        old_functions, new_functions = functions(old), functions(new)
        for name in ('read_source', 'Parser', 'polynomial', 'add', 'mul', 'quotient',
                     'engine_map', 'unit_certificate'):
            self.assertEqual(old_functions[name], new_functions[name], name)

    def test_exact_production_metadata_pin(self):
        data = META.read_bytes()
        self.assertEqual(hashlib.sha256(data).hexdigest(), META_SHA)
        fixture = json.loads(data)
        order = O.fixed(fixture['order']['variables'])
        self.assertEqual(order, fixture['order'])
        self.assertEqual(E.ring_id(order['variables'], order), O.ORDER_SHA)
        self.assertEqual(O.ring_declaration(order), fixture['ring_declaration'])
        self.assertEqual(E.ring_id(order['variables']), O.DP_NAMES_SHA)
        changed = copy.deepcopy(order)
        changed['weight_rows'][1][71] += 1
        with self.assertRaisesRegex(ValueError, 'pinned production'):
            O.validate(changed)
        with self.assertRaises(ValueError):
            O.fixed(list(reversed(order['variables'])))

    def test_descriptor_drift_and_type_controls(self):
        changes = [('field', 'Fp'), ('tie_break', 'lp'), ('comparison', 'reverse'),
                   ('schema', 'other'), ('extra', True)]
        for key, value in changes:
            with self.subTest(key=key), self.assertRaises(ValueError):
                O.validate({**ORDER, key: value})
        for weights in ([[0, 1, 4], [1, 0, 1], [1, 0, 1]],
                        [[3, 1, 4], [1, 0], [1, 0, 1]],
                        [[3.0, 1, 4], [1, 0, 1], [1, 0, 1]],
                        [[True, 1, 4], [1, 0, 1], [1, 0, 1]]):
            with self.assertRaises(ValueError):
                O.descriptor(V, weights)

    def test_weighted_graph_vs_dp(self):
        basis = graph()
        self.assertEqual([max(g, key=lambda m: E.key(m, 3, ORDER['weight_rows']))
                          for g in basis], [(0,), (2,)])
        with patch.object(E, 'normal_form', wraps=E.normal_form) as nf:
            verdict = E.proper_certificate(basis, basis, 3, ORDER['weight_rows'])
        self.assertIn('PROPER', verdict)
        self.assertGreaterEqual(nf.call_count, 4)
        self.assertTrue(all(call.args[3] == ORDER['weight_rows'] for call in nf.call_args_list))
        with self.assertRaisesRegex(ValueError, 'Buchberger'):
            E.proper_certificate(basis, basis, 3)
        changed = copy.deepcopy(ORDER)
        changed['weight_rows'] = [[1, 1, 1], [0, 0, 0], [0, 0, 0]]
        with self.assertRaisesRegex(ValueError, 'Buchberger'):
            E.proper_certificate(basis, basis, 3, changed['weight_rows'])

    def test_all_order_comparison_levels(self):
        names = ['x', 'y', 'z', 't', 'u']
        order = O.descriptor(names, [[2, 1, 2, 2, 2], [1, 0, 0, 1, 0], [1, 0, 0, 0, 0]])
        for high, low in [('x', 'y'), ('x', 'z'), ('x', 't'), ('y^2', 'z'), ('z', 'u')]:
            hm = next(iter(E.polynomial(high, names)))
            lm = next(iter(E.polynomial(low, names)))
            self.assertGreater(E.key(hm, 5, order['weight_rows']), E.key(lm, 5, order['weight_rows']))

    def test_protocol_cannot_fall_back_to_dp(self):
        raw = T.result(['x-y^2', 'z-y^3'], ['x-y^2', 'z-y^3'], variables=V)
        weighted = raw.replace(E.ring_id(V).encode(), E.ring_id(V, ORDER).encode(), 1)
        engine, basis, cofactors = E.parse_result(weighted, b'', V, 'a'*64, ORDER)
        self.assertIsNone(cofactors)
        self.assertIn('PROPER', E.proper_certificate(engine, basis, 3, ORDER['weight_rows']))
        for stream, order in [(weighted, None), (raw, ORDER)]:
            with self.assertRaisesRegex(ValueError, 'header mismatch'):
                E.parse_result(stream, b'', V, 'a'*64, order)
        changed = copy.deepcopy(ORDER); changed['weight_rows'][2][0] += 1
        with self.assertRaisesRegex(ValueError, 'header mismatch'):
            E.parse_result(weighted, b'', V, 'a'*64, changed)

    def test_ring_line_only_and_real_suffix_omissions(self):
        data, literal = T.toy_source(['0', 'x^2-y', '0', '1-x', '0'])
        variables, rows, labels, original = E.read_source(data, literal)
        order = O.descriptor(variables, [[3, 1], [1, 0], [1, 0]])
        executed = O.adapt_prefix(original, variables, order)
        O.check_prefix(original, executed, variables, order)
        self.assertEqual(original.partition('\n')[2], executed.partition('\n')[2])
        for changed in [executed.replace('// R/0\n0,\n', ''),
                        executed.replace('x^2-y', 'x^2+y'),
                        executed.replace('// R/0\n0', '// R/0\n1'),
                        executed.replace('ideal I=', 'ideal J='),
                        executed+'quit;\n']:
            with self.assertRaisesRegex(ValueError, 'suffix drift'):
                O.check_prefix(original, changed, variables, order)
        with self.assertRaisesRegex(ValueError, 'dp source prefix'):
            O.adapt_prefix(original.replace(',dp;', ',lp;'), variables, order)
        with self.assertRaises(ValueError):
            E.read_source(data, literal.replace(b'// R/0\n0,\n', b''))

    def test_footer_only_order_header_delta(self):
        old = D.footer(V, 'a'*64)
        weighted = D.footer(V, 'a'*64, order=ORDER)
        self.assertEqual(weighted, old.replace(E.ring_id(V), E.ring_id(V, ORDER), 1))
        self.assertEqual(weighted.count('slimgb(I)'), 1)
        self.assertNotIn('slimgb', D.control_input())

    def test_weighted_unit_maps_and_strict_parser_retained(self):
        names = ['x', 'y']
        order = O.descriptor(names, [[3, 1], [1, 0], [1, 0]])
        rows = ['0', 'x', '0', 'x', '1-x', '0']
        raw = T.result(rows, ['1'], ['0', '0', '0', '1', '1', '0'])
        raw = raw.replace(E.ring_id(names).encode(), E.ring_id(names, order).encode(), 1)
        engine, basis, cofactors = E.parse_result(raw, b'', names, 'a'*64, order)
        source = [E.polynomial(t, names) for t in rows]
        verdict, mapping, lifted = E.unit_certificate(source, engine, cofactors)
        self.assertIn('UNIT', verdict)
        self.assertEqual(mapping, [0, 1, 0, 1, 4, 0])
        self.assertEqual(len(lifted), 6)
        for stderr in (b' ', b'\n', b'\t'):
            with self.assertRaisesRegex(ValueError, 'nonempty stderr'):
                E.parse_result(raw, stderr, names, 'a'*64, order)
        with self.assertRaisesRegex(ValueError, 'nonzero count'):
            E.parse_result(raw.replace(b'I_SIZE 3', b'I_SIZE 0'), b'', names, 'a'*64, order)
        damaged = raw.replace(b'T 4 1', b'T 4 2')
        engine, basis, cofactors = E.parse_result(damaged, b'', names, 'a'*64, order)
        with self.assertRaisesRegex(ValueError, 'not one'):
            E.unit_certificate(source, engine, cofactors)

    def test_weighted_falseproper_and_missing_original(self):
        names = ['x', 'y']; weights = [[3, 1], [1, 0], [1, 0]]
        p = lambda t: E.polynomial(t, names)
        bad = [p('x*y-1'), p('x^2')]
        self.assertEqual(E.normal_form(E.ONE, bad, 2, weights), E.ONE)
        self.assertTrue(all(not E.normal_form(row, bad, 2, weights) for row in bad))
        with self.assertRaisesRegex(ValueError, 'Buchberger'):
            E.proper_certificate(bad, bad, 2, weights)
        with self.assertRaisesRegex(ValueError, 'original equation missing'):
            E.proper_certificate([p('x'), p('y')], [p('x')], 2, weights)

    def test_new_authority_old_job_and_order_gate_rejected(self):
        observed = {'system': 'Linux', 'vendor': 'Amazon EC2', 'instance': D.INSTANCE,
                    'cwd': D.CWD, 'boot': 'fixture', 'now': 100.0}
        authority = {'schema': D.AUTHORITY_SCHEMA, 'root_green': True,
                     'execution_order_sha256': O.ORDER_SHA, 'mode': 'solver', 'job_id': 'fixture',
                     'pins': {}, 'caps': D.CAPS, 'instance_id': D.INSTANCE,
                     'cwd': D.CWD, 'boot_id': 'fixture', 'started_utc': '1970-01-01T00:01:30Z',
                     'deadline_utc': '1970-01-01T00:03:00Z', 'full_stream_gate_accepted': True,
                     'order_gate_accepted': True}
        for name in ('full_stream_gate_sha256', 'engine_index_control_sha256',
                     'output_limit_control_sha256', 'descendant_control_sha256',
                     'order_gate_sha256', 'order_engine_control_sha256'):
            authority[name] = 'a'*64
        self.assertEqual(D.authority_check(authority, 'decision', observed, {}), 80)
        for key, value in [('schema', 'jc2.d125-exact-solver-authority/v1'),
                           ('execution_order_sha256', 'a'*64), ('order_gate_accepted', False),
                           ('order_gate_sha256', ''), ('order_engine_control_sha256', ''),
                           ('mode', 'engineering_control'), ('root_green', False)]:
            with self.subTest(key=key), self.assertRaises(ValueError):
                D.authority_check({**authority, key: value}, 'decision', observed, {})
        with self.assertRaises(ValueError):
            D.authority_check(authority, 'decision',
                             {**observed, 'cwd': '/home/ubuntu/d125-small-exact-solver-20260907'}, {})


if __name__ == '__main__':
    unittest.main()
