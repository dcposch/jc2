#!/usr/bin/env python3
"""Tiny fixtures only. Never call real metadata/reconstruct/original_rows."""
import ast
import copy
from fractions import Fraction as F
import json
from pathlib import Path
import tempfile
import time
import unittest
import construct as C
import replay as R


def ops(**changes):
    caps = dict(C.CEILINGS)
    caps.update(changes)
    return C.Arithmetic(caps, time.monotonic()+20)


def trace(original, maps):
    rows, residual = [], 0
    for index, (label, p) in enumerate(original):
        q = C.transport(p, maps, ops())
        rows.append(dict(original_index=index, label=label, terms=C.wire(q),
                         residual_index=residual if q else None))
        residual += bool(q)
    return rows


class Tiny(unittest.TestCase):
    def test_no_assert_nodes(self):
        for name in ('construct.py', 'test_construct.py', 'baseline.py', 'qpoly.py', 'replay.py', 'run_tests.py'):
            nodes = ast.walk(ast.parse(Path(__file__).with_name(name).read_text()))
            self.assertFalse(any(isinstance(n, ast.Assert) for n in nodes))

    def test_no_production_context(self):
        with self.assertRaisesRegex(ValueError, 'authorized context'):
            C.metadata('slice', ops())
        with self.assertRaisesRegex(ValueError, 'authorized context'):
            C.reconstruct('full', ops())

    def test_a_hermite_fixture(self):
        # A=(g+p)^3+z*g+b*p. The single lower odd Hermite graph b=z
        # makes A(v^-1,v^4u-lambda*v-v^-1) polynomial.
        a = {(0, 3): C.const(1), (1, 2): C.const(3), (2, 1): C.const(3),
             (3, 0): C.const(1), (1, 0): {(0,): F(1)}, (0, 1): {}}
        forcing = C.liftrow(a, 0, -1, 1, ops())
        values, inv = C.solve_constants(C.hermite_matrix(1), [forcing], ops())
        self.assertEqual(values, [{(0,): F(1)}])
        self.assertEqual(inv, [[F(-1)]])
        a[0, 1] = values[0]
        for e in (-3, -2, -1):
            self.assertEqual(C.liftrow(a, 0, e, 1, ops()), {})
        a[0, 1] = {}
        self.assertNotEqual(C.liftrow(a, 0, -1, 1, ops()), {})

    def test_hermite_matrix_orientation(self):
        # A genuinely 2x2 Hermite block; independent binomial expansion.
        matrix = C.hermite_matrix(7)
        self.assertEqual(matrix, [[-1, 1], [7, -6]])
        inv = C.inverse(matrix)
        self.assertEqual([[sum(F(matrix[i][k])*inv[k][j] for k in range(2))
                           for j in range(2)] for i in range(2)], [[1, 0], [0, 1]])

    def test_actual_b_d5_kernel_and_orientation(self):
        # One small actual constant block, not all production dimensions.
        columns = [0, 1, 2, 3]
        matrix = C.b_matrix(5, columns)
        kernel = [1, 0, 0, 1]  # H=p^5+g^3*p^2
        self.assertTrue(all(sum(c*v for c, v in zip(row, kernel)) == 0 for row in matrix))
        h3 = {(0, 15): C.const(1), (3, 12): C.const(3),
              (6, 9): C.const(3), (9, 6): C.const(1)}
        for i in columns:
            for r in range(19):
                direct = C.jrow(h3, {(i, 5-i): C.const(1)}, r, 18-r, ops(), False)
                self.assertEqual(direct, C.const(matrix[r][i]))
        bad = copy.deepcopy(matrix)
        bad[2][0] += 1
        self.assertFalse(all(sum(c*v for c, v in zip(row, kernel)) == 0 for row in bad))

    def test_actual_b_pivot_solve(self):
        columns = [3, 2, 1]  # kernel coordinate i=0 held fixed
        matrix = C.b_matrix(5, columns)
        chosen = C.independent_rows(matrix)
        square = [matrix[r] for r in chosen]
        wanted = [{(0,): F(2)}, C.const(3), {(1,): F(-1)}]
        forcing = []
        for row in square:
            p = {}
            for c, q in zip(row, wanted):
                p = C.Q.add(p, q, -F(c))
            forcing.append(p)
        got, _ = C.solve_constants(square, forcing, ops())
        self.assertEqual(got, wanted)
        self.assertNotEqual(C.solve_constants(square, list(reversed(forcing)), ops())[0], wanted)
        m1 = C.b_matrix(1, [0])
        self.assertEqual(C.independent_rows(m1), [2])
        self.assertEqual(m1[2], [9])

    def test_full_lower_shear_inverse(self):
        a = {(0, 3): C.const(1), (0, 1): C.const(2)}
        b = {(0, 5): {(0,): F(1)}, (0, 3): {}, (0, 1): C.const(7)}
        scalar = {(1,): F(1)}
        full = C.shear(a, b, scalar, ops())
        self.assertEqual(C.shear(a, full, C.Q.add({}, scalar, -1), ops()), b)
        bad = copy.deepcopy(full)
        bad[0, 1] = b[0, 1]  # isolated leading shear drops lower coefficient
        self.assertNotEqual(C.shear(a, bad, C.Q.add({}, scalar, -1), ops()), b)
        self.assertEqual(full[0, 1], {(): F(7), (1,): F(2)})

    def test_changed_fixed_face(self):
        entries = [{'point': [0, 3], 'name': 'top', 'fixed': C.B.F(1).wire()},
                   {'point': [1, 2], 'name': 'zero', 'fixed': C.B.F(0).wire()}]
        coeffs = {(0, 3): C.const(1), (1, 2): {}}
        C.check_fixed(entries, coeffs)
        for point in coeffs:
            bad = copy.deepcopy(coeffs)
            bad[point] = C.const(2)
            with self.assertRaisesRegex(ValueError, 'fixed face'):
                C.check_fixed(entries, bad)

    def test_all_rows_transport_zero_duplicate(self):
        original = [('zero', {}), ('graph', {(0,): F(1), (1, 1): F(-1)}),
                    ('residual', {(0,): F(1), (): F(-2)}),
                    ('duplicate', {(0,): F(1), (): F(-2)}), ('tail', {})]
        maps = {0: {(0, 0): F(1)}, 1: {(0,): F(1)}}
        rows = trace(original, maps)
        self.assertEqual(C.verify_transport(original, maps, rows, ops()), 2)
        with self.assertRaisesRegex(ValueError, 'missing original'):
            C.verify_transport(original, maps, rows[:-1], ops())
        for mutation in ('coefficient', 'residual', 'label', 'index'):
            bad = copy.deepcopy(rows)
            if mutation == 'coefficient':
                bad[2]['terms'] = []
            if mutation == 'residual':
                bad[2]['residual_index'] = None
            if mutation == 'label':
                bad[2]['label'] = 'different'
            if mutation == 'index':
                bad[2]['original_index'] = 0
            with self.assertRaises(ValueError):
                C.verify_transport(original, maps, bad, ops())

    def test_target_and_guard(self):
        self.assertEqual(C.jrow({}, {}, 2, 0, ops()), C.const(F(5, 9)))
        self.assertNotEqual(C.jrow({}, {}, 2, 0, ops()), C.const(F(-5, 9)))
        original = [('guard', {(0, 1): F(1), (): F(-1)})]
        maps = {0: C.const(F(-5, 9)), 1: C.const(F(-9, 5))}
        good = trace(original, maps)
        self.assertEqual(C.verify_transport(original, maps, good, ops()), 0)
        maps[1] = C.const(1)
        with self.assertRaisesRegex(ValueError, 'mismatch'):
            C.verify_transport(original, maps, good, ops())

    def test_resource_limits_before_growth(self):
        with self.assertRaisesRegex(ValueError, 'pair cap'):
            ops(multiply_pairs=1).mul({(): F(1), (0,): F(1)}, {(0,): F(1)})
        with self.assertRaisesRegex(ValueError, 'bit cap'):
            ops(coefficient_bits=3).check(C.const(16))
        with self.assertRaisesRegex(ValueError, 'retained term cap'):
            ops(retained_terms=1).keep({(): F(1), (0,): F(1)})

    def test_stream_exclusive_and_pre_wire(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)/'only.jsonl'
            stream = C.Stream(path, 1024)
            stream.polynomial(dict(type='row', label='x'), {(0,): F(1)})
            with self.assertRaisesRegex(ValueError, 'pre-wire'):
                stream.polynomial(dict(type='row'), {(): F(2**5000)})
            stream.close()
            records = [json.loads(x) for x in path.read_bytes().splitlines()]
            self.assertEqual(len(records), 1)
            with self.assertRaises(FileExistsError):
                C.Stream(path, 1024)

    def test_replay_wire_and_footer(self):
        import hashlib
        p = {(0, 0): F(2, 3), (1,): F(-7)}
        self.assertEqual(R.decode_terms(C.wire(p), 2), p)
        for bad in (C.wire(p)*2, C.wire({(2,): F(1)}), C.wire({(0,): F(0)})):
            with self.assertRaises(ValueError):
                R.decode_terms(bad, 2)
        with tempfile.TemporaryDirectory() as temp:
            prefix = C.B.canonical(dict(type='row', label='toy', terms=C.wire(p)))
            footer = dict(type='footer', complete=True, prefix_sha256=hashlib.sha256(prefix).hexdigest())
            data = prefix+C.B.canonical(footer)
            path = Path(temp)/'toy.jsonl'
            with path.open('xb') as stream:
                stream.write(data)
            self.assertEqual(len(list(R.records(path))), 2)
            for index, corrupted in enumerate((prefix, data+b'{}\n', data.replace(b'"complete":true', b'"complete":false'))):
                badpath = Path(temp)/('bad'+str(index)+'.jsonl')
                with badpath.open('xb') as stream:
                    stream.write(corrupted)
                with self.assertRaises(ValueError):
                    list(R.records(badpath))
        with self.assertRaisesRegex(ValueError, 'host-authorized'):
            R.replay_frozen('not-read', 'not-read', ops())


if __name__ == '__main__':
    unittest.main()
