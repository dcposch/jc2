"""Tiny stdlib controls. No production source, CAS, remote calls or runner jobs."""
from fractions import Fraction as F
import unittest
from unittest.mock import patch
import exact as E
import driver as D

V = ['x', 'y']


def p(text, variables=V):
    return E.polynomial(text, variables)


def toy_source(texts):
    header = {'type': 'header', 'field': 'Q', 'order': 'global degree reverse lexicographic, displayed variable order',
              'expected_rows': len(texts), 'expected_variables': 2}
    records = [header]+[{'type': 'variable', 'id': i, 'name': name} for i, name in enumerate(V)]
    for i, text in enumerate(texts):
        terms = [[[[str(c.numerator), str(c.denominator)], ['0', '1']], list(m)]
                 for m, c in sorted(p(text).items())]
        records.append({'type': 'row', 'label': 'R/'+str(i), 'terms': terms})
    return source_records(records, texts)


def source_records(records, texts):
    prefix = b''.join(E.canonical(r) for r in records)
    footer = {'type': 'footer', 'complete': True, 'prefix_sha256': E.digest(prefix),
              'prefix_records': len(records), 'counts': {'rows': len(texts)}}
    singular = 'ring R=0,(x,y),dp;\nideal I=\n'+',\n'.join('// R/'+str(i)+'\n'+t
                    for i, t in enumerate(texts))+E.ENDING
    return prefix+E.canonical(footer), singular.encode()


def result(engine, basis, cofactors=None, variables=V, source='a'*64):
    lines = ['JC2CERT 1 '+source+' '+E.ring_id(variables),
             'I_SIZE '+str(sum(bool(p(t, variables)) for t in engine))]
    for name, values in [('I', engine), ('G', basis)]+([] if cofactors is None else [('T', cofactors)]):
        lines.append(name+'_BEGIN '+str(len(values)))
        lines.extend(name+' '+str(i+1)+' '+v for i, v in enumerate(values))
        lines.append(name+'_END')
    lines.extend(['END NONUNIT'] if cofactors is None else ['CHECK 1', 'END UNIT'])
    return ('\n'.join(lines)+'\n').encode()


class ExactTests(unittest.TestCase):
    def test_rational_explicit_parser(self):
        self.assertEqual(p('-(x-y)^2+(1/2)*x^2'), p('-x^2/2+2*x*y-y^2'))
        self.assertEqual(p('x^0'), E.ONE)
        self.assertEqual(p('0*(x+y)'), {})
        self.assertEqual(p('x/(2/3)'), p('3*x/2'))

    def test_bad_syntax(self):
        for text in ['x/y', 'x^-1', '2x', 'rho', 'x;quit', '__import__(x)', '1/0',
                     'x^2^3', 'x^10001', '(x', 'x)', 'x$y', '1//2']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                p(text)

    def test_order(self):
        ordered = [p(t) for t in ['x^2', 'x*y', 'y^2', 'x', 'y', '1']]
        keys = [E.key(next(iter(q)), 2) for q in ordered]
        self.assertEqual(keys, sorted(keys, reverse=True))
        self.assertGreater(E.key((1, 1), 3), E.key((0, 2), 3))

    def test_unit_zero_duplicate_maps(self):
        rows = [p(t) for t in ['0', 'x', '0', 'x', '1-x', '0']]
        engine = [p('x'), p('1-x')]
        verdict, mapping, lifted = E.unit_certificate(rows, engine, [E.ONE, E.ONE])
        self.assertEqual(mapping, [1, 4]); self.assertEqual(len(lifted), 6)
        self.assertIn('UNIT_COFACTOR', verdict)
        full = [p(t) for t in ['0', '1/2', '0', '1/2', '1', '0']]
        self.assertIn('UNIT', E.unit_certificate(rows, rows, full)[0])

    def test_changed_cofactor(self):
        with self.assertRaisesRegex(ValueError, 'not one'):
            E.unit_certificate([p('x'), p('1-x')], [p('x'), p('1-x')], [p('2'), p('1')])

    def test_missing_engine_equation(self):
        with self.assertRaisesRegex(ValueError, 'absent'):
            E.engine_map([p('x'), p('y')], [p('x')])
        with self.assertRaisesRegex(ValueError, 'not original'):
            E.engine_map([p('x')], [p('2*x')])

    def test_dimension_and_duplicate_cofactor_errors(self):
        with self.assertRaises(ValueError):
            E.unit_certificate([p('x')], [p('x')], [])
        with self.assertRaises(ValueError):
            E.unit_certificate([p('x'), p('1-x')], [p('x'), p('x'), p('1-x')],
                               [E.ONE, E.ONE, E.ONE])

    def test_proper_and_strict_superideal(self):
        rows = [p(t) for t in ['0', 'x^2', '0', 'x*y', '0']]
        self.assertIn('PROPER', E.proper_certificate(rows, [p('x^2'), p('x*y')], 2))
        self.assertIn('PROPER', E.proper_certificate(rows, [p('x')], 2))
        self.assertIn('PROPER', E.proper_certificate([{}], [], 2))

    def test_false_proper_buchberger(self):
        bad = [p('x^2'), p('x*y-1')]
        self.assertEqual(E.normal_form(E.ONE, bad, 2), E.ONE)
        self.assertTrue(all(not E.normal_form(q, bad, 2) for q in bad))
        with self.assertRaisesRegex(ValueError, 'Buchberger'):
            E.proper_certificate(bad, bad, 2)

    def test_missing_original_and_unit_proper(self):
        with self.assertRaisesRegex(ValueError, 'original equation missing'):
            E.proper_certificate([p('x'), p('y')], [p('x')], 2)
        with self.assertRaisesRegex(ValueError, 'unit basis'):
            E.proper_certificate([p('x')], [E.ONE], 2)

    def test_full_protocol(self):
        data = result(['0', 'x', '0', 'x', '1-x', '0'], ['1'], ['0', '1/2', '0', '1/2', '1', '0'])
        engine, basis, h = E.parse_result(data, b'', V, 'a'*64)
        self.assertEqual(basis, [E.ONE]); self.assertIn('UNIT', E.unit_certificate(engine, engine, h)[0])
        engine, basis, h = E.parse_result(result(['x^2'], ['x']), b'', V, 'a'*64)
        self.assertIsNone(h); E.proper_certificate(engine, basis, 2)

    def test_protocol_mutations(self):
        data = result(['x', '1-x'], ['1'], ['1', '1'])
        changes = [data.replace(b'I 2 ', b'I 1 '), data.replace(b'T_BEGIN 2', b'T_BEGIN 1'),
                   data.replace(b'CHECK 1', b'CHECK 0'), data.replace(b'END UNIT\n', b''),
                   data+b'EXTRA\n', data.replace(b'I_END\n', b''),
                   data.replace(b'G 1 1', b'G 1 unknown'), data.replace(b'I_SIZE 2', b'I_SIZE 9')]
        for changed in changes:
            with self.subTest(changed=changed[-80:]), self.assertRaises(ValueError):
                E.parse_result(changed, b'', V, 'a'*64)
        for variables, source, stderr in [(['y', 'x'], 'a'*64, b''), (V, 'b'*64, b''), (V, 'a'*64, b'error')]:
            with self.assertRaises(ValueError):
                E.parse_result(data, stderr, variables, source)

    def test_literal_roundtrip_and_real_mutations(self):
        data, sing = toy_source(['0', 'x^2/2-y', '0', 'x^2/2-y', '1-x', '0'])
        variables, rows, labels, prefix = E.read_source(data, sing)
        self.assertEqual(len(rows), 6); self.assertEqual(variables, V)
        self.assertEqual((prefix+E.ENDING[2:]).encode(), sing)
        for changed in [sing.replace(b'x^2/2-y', b'x^2/3-y', 1),
                        sing.replace(b'// R/0\n0', b'// R/0\n1'),
                        sing.replace(b',dp;', b',lp;'), sing.replace(b'// R/0\n0,\n', b''),
                        sing.replace(b'// R/0', b'// R/99'), sing+b'quit;\n']:
            with self.assertRaises(ValueError): E.read_source(data, changed)
        records = [E.strict_json(line) for line in data.splitlines()][:-1]
        records[-2]['terms'][0][0][1] = ['1', '1']
        changed, _ = source_records(records, ['0', 'x^2/2-y', '0', 'x^2/2-y', '1-x', '0'])
        with self.assertRaisesRegex(ValueError, 'golden'): E.read_source(changed, sing)
        with self.assertRaisesRegex(ValueError, 'pin drift'): E.read_source(changed, sing, production=True)

    def test_resynchronized_omission(self):
        data, sing = toy_source(['x', 'y'])
        records = [E.strict_json(line) for line in data.splitlines()][:-1]
        records.pop(); records[0]['expected_rows'] = 1
        changed, _ = source_records(records, ['x'])
        with self.assertRaisesRegex(ValueError, 'row count'): E.read_source(changed, sing)

    def test_authority_isolation_and_drift(self):
        observed = {'system': 'Linux', 'vendor': 'Amazon EC2', 'instance': D.INSTANCE,
                    'cwd': D.CWD, 'boot': 'test-boot', 'now': 100.0}
        expected = {'test': 'pin'}
        a = {'schema': 'jc2.d125-exact-solver-authority/v1', 'root_green': True,
             'mode': 'engineering_control', 'job_id': 'test', 'pins': expected, 'caps': D.CAPS,
             'instance_id': D.INSTANCE, 'cwd': D.CWD, 'boot_id': 'test-boot',
             'started_utc': '1970-01-01T00:01:30Z', 'deadline_utc': '1970-01-01T00:03:00Z'}
        self.assertEqual(D.authority_check(a, 'control', observed, expected), 10)
        with self.assertRaises(ValueError): D.authority_check(a, 'decision', observed, expected)
        solver = {**a, 'mode': 'solver', 'full_stream_gate_accepted': True,
                  **{k: 'c'*64 for k in ['full_stream_gate_sha256', 'engine_index_control_sha256',
                            'output_limit_control_sha256', 'descendant_control_sha256']}}
        self.assertEqual(D.authority_check(solver, 'decision', observed, expected), 80)
        for field, value in [('root_green', False), ('mode', 'engineering_control'), ('full_stream_gate_accepted', False),
                             ('engine_index_control_sha256', ''), ('pins', {}), ('boot_id', 'other'), ('caps', {})]:
            with self.subTest(field=field), self.assertRaises(ValueError):
                D.authority_check({**solver, field: value}, 'decision', observed, expected)
        for field, value in [('system', 'Darwin'), ('vendor', 'other'), ('instance', 'i-12345678'),
                             ('cwd', '/home/ubuntu'), ('now', 181)]:
            with self.subTest(field=field), self.assertRaises(ValueError):
                D.authority_check(solver, 'decision', {**observed, field: value}, expected)

    def test_serializer_and_limit_calls(self):
        control = D.control_input()
        self.assertNotIn('slimgb', control); self.assertNotIn('std(', control)
        self.assertIn('ideal I=0,x,0,x,1-x,0;', control)
        self.assertIn('short=0', control); self.assertIn('ncols(matrix(I))', control)
        production = D.footer(V, 'a'*64)
        self.assertEqual(production.count('slimgb(I)'), 1)
        self.assertLess(production.index('G_END'), production.index('lift(I'))
        for forbidden in ['system(', 'write(', 'link ', 'LIB ', 'dim(', 'msolve']:
            self.assertNotIn(forbidden, production)
        with patch.object(D.resource, 'setrlimit') as mock:
            D.limits('decision')
        self.assertEqual(mock.call_count, 3)
        self.assertEqual(mock.call_args_list[1].args, (D.resource.RLIMIT_FSIZE, (64*1024**2,)*2))
        self.assertEqual(mock.call_args_list[2].args, (D.resource.RLIMIT_CORE, (0, 0)))

    def test_pending_engine_control_replay_on_synthetic_stream(self):
        prefix = 'ring R=0,(x),dp;\nideal I='+','.join(D.CONTROL_TEXT)+';\n'
        data = result(['0', 'x', '0', 'x', '1-x'], ['1'], ['0', '1/2', '0', '1/2', '1'],
                      variables=['x'], source=E.digest(prefix.encode()))
        replay = D.check_control(data, b'')
        self.assertEqual(replay['original_rows'], 6)
        self.assertEqual(replay['engine_columns'], 5)
        with self.assertRaises(ValueError):
            D.check_control(data.replace(b'T 4 1/2', b'T 4 3/2'), b'')


if __name__ == '__main__':
    unittest.main()
