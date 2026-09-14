#!/usr/bin/env python3
"""Independent frozen-input checks; never invokes Singular or a production path."""
import ast
import hashlib
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

INPUTS = Path('/tmp/jc2-lane.wWImXu/inputs')
sys.path.insert(0, str(INPUTS))
import engine as N
import driver as D
import exact as E
import hybrid as H

PINS = {
    'ERRATUM.md': 'bd312311284fc9617533f349f90306940b4bd105272434ef3627b00b4822a3c1',
    'HARVEST.md': '84746860d736e7bf5fcfd1ad565a68be1aa49b3e85d1059065c95a08a0d898e4',
    'REGISTRATION.md': '364a5d8c57a967d6dc3467db13eb0b19ba6c7924a573dc5b3ea67da7eb6f1ee5',
    'd125-hybrid81-caller-repair-gate-sol56-20260907.md': '46a6304811af423042f29d9a8f4c3022189d648286e7770d02ae59d478615fac',
    'd125-hybrid81-engine-prep-astra-20260907.md': '481ba6521e86e7a5786e71b9f8e1ac266c483d56bfe9eba164bd59f468812fbf',
    'driver.py': 'ce599a26a0ed051eddd71125f492bb0b19c4ef86cdf97a6bc887f5cf47cade5a',
    'engine.py': 'a87debfce5ca01817c03c2b180fd514d8e45269b1173c6f4a562255883188ae5',
    'exact.py': '7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9',
    'hybrid.py': 'c9755a7172eaa7f1393860931d55c38a0b9d79b5b170eadbf14baff0203c35a3',
    'test_engine.py': '6bbd6499957e05ad02d180b9e2d61d80bbfe2666a68582f857f7d8569781818f',
    'tiny-engine-fixture.jsonl': 'd00df83bafddcd3436dad44034bdb1680d306f6d67f8bfa83d4b32de19961bbf',
}
VARIABLES = ['x', 'y', 'k', 'z']
ROWS = ['0', 'x/2', '0', 'x/2', '1-x', '0', 'k*z-1']
COFACTORS = ['0', '1', '0', '1', '1', '0', '0']


def sha(data):
    return hashlib.sha256(data).hexdigest()


def result(rows=ROWS, cofactors=COFACTORS, source=N.FIXTURE_SHA,
           basis=('1',), i_size=None):
    if i_size is None:
        i_size = sum(row != '0' for row in rows)
    lines = ['JC2CERT 1 '+source+' '+E.ring_id(VARIABLES),
             'I_SIZE '+str(i_size), 'I_BEGIN '+str(len(rows))]
    lines += ['I '+str(i+1)+' '+row for i, row in enumerate(rows)]
    lines += ['I_END', 'G_BEGIN '+str(len(basis))]
    lines += ['G '+str(i+1)+' '+row for i, row in enumerate(basis)]
    lines += ['G_END']
    if cofactors is not None:
        lines += ['T_BEGIN '+str(len(cofactors))]
        lines += ['T '+str(i+1)+' '+row for i, row in enumerate(cofactors)]
        lines += ['T_END', 'CHECK 1', 'END UNIT']
    else:
        lines += ['END NONUNIT']
    return ('\n'.join(lines)+'\n').encode('ascii')


class ReachedPastParentCheck(Exception):
    pass


class GateChecks(unittest.TestCase):
    def test_all_frozen_pins_and_declared_sizes(self):
        for name, expected in PINS.items():
            data = (INPUTS/name).read_bytes()
            self.assertEqual(sha(data), expected, name)
        self.assertEqual(len((INPUTS/'engine.py').read_text().splitlines()), 73)
        self.assertEqual(len((INPUTS/'test_engine.py').read_text().splitlines()), 55)
        self.assertEqual(len((INPUTS/'tiny-engine-fixture.jsonl').read_bytes()), 1698)

    def test_exact_tiny_script_and_alarm_bytes(self):
        data = (INPUTS/'tiny-engine-fixture.jsonl').read_bytes()
        variables, rows, labels, prefix = H.read_hybrid(data, production=False)
        self.assertEqual(variables, VARIABLES)
        self.assertEqual([H.ordinary(row, variables) for row in rows],
                         ['0', '(1/2)*x', '0', '(1/2)*x', '1+-1*x', '0', '-1+1*k*z'])
        self.assertEqual(labels, ['R/0', 'R/1', 'R/2', 'R/3', 'R/4', 'R/5', 'UNIT/kz'])
        script = N.hybrid_script(data)
        self.assertEqual(script, prefix+D.footer(variables, N.FIXTURE_SHA, control=True))
        self.assertEqual((len(script.encode('ascii')), sha(script.encode('ascii'))),
                         (1072, '59295067207d4f17eb2acdbd4eac9d4755d16c94bfc36884e2f14d2731b9ad11'))
        self.assertEqual(script.count('// '), 7)
        self.assertEqual(script.count('matrix T=lift(I,ideal(1));'), 1)
        for forbidden in ('slimgb', 'std(', 'dim(', 'system(', 'write(', 'LIB '):
            self.assertNotIn(forbidden, script)
        alarm = N.alarm_script().encode('ascii')
        self.assertEqual((len(alarm), sha(alarm)),
                         (102, '446daa14cdedeb55ec9d0753ff48582b9ad3945bf889d471f56059911ea1f4b7'))

    def test_positive_full_slot_replay(self):
        data = (INPUTS/'tiny-engine-fixture.jsonl').read_bytes()
        verdict = N.check_hybrid(data, result(), b'')
        self.assertEqual(verdict, {
            'status': 'TINY_HYBRID_ENGINE_REPLAY_PASS',
            'verdict': 'EXACT_Q_UNIT_COFACTOR_CERTIFICATE',
            'rows': 7, 'engine_columns': 7, 'cofactor_rows': 7,
            'mapping': [0, 1, 0, 1, 4, 0, 6]})

    def test_changed_stream_objects_reject(self):
        data = (INPUTS/'tiny-engine-fixture.jsonl').read_bytes()
        good = result()
        changed = [
            (good.replace(b'T 5 1', b'T 5 2'), b''),
            (good.replace(b'I_SIZE 4', b'I_SIZE 3'), b''),
            (good, b' \n'),
            (good+b'EXTRA\n', b''),
            (result(rows=ROWS[:-1], cofactors=COFACTORS[:-1]), b''),
            (result(rows=ROWS[:2]+ROWS[3:], cofactors=COFACTORS[:2]+COFACTORS[3:]), b''),
            (result(rows=[ROWS[0], ROWS[1], ROWS[2], ROWS[4], ROWS[3], ROWS[5], ROWS[6]]), b''),
            (result(basis=('0',)), b''),
        ]
        for stdout, stderr in changed:
            with self.subTest(stdout=sha(stdout), stderr=stderr):
                with self.assertRaises(ValueError):
                    N.check_hybrid(data, stdout, stderr)

    def test_wrong_fixture_object_rejects(self):
        data = (INPUTS/'tiny-engine-fixture.jsonl').read_bytes()
        changed = data.replace(b'"1","2"', b'"1","3"', 1)
        self.assertNotEqual(sha(changed), N.FIXTURE_SHA)
        with self.assertRaises(ValueError):
            N.hybrid_script(changed)
        with self.assertRaises(ValueError):
            N.check_hybrid(changed, result(), b'')

    def test_exact_engineering_binding(self):
        binding = {'operation': 'hybrid', 'helper_sha256': 'a'*64,
                   'fixture_sha256': N.FIXTURE_SHA, 'root_green_sha256': 'b'*64}
        authority = {'mode': 'engineering_control', 'engineering': binding}
        N.control_binding(authority, 'hybrid', 'a'*64, 'b'*64)
        bad = [
            ({**authority, 'mode': 'solver'}, 'hybrid', 'a'*64, 'b'*64),
            ({**authority, 'engineering': {**binding, 'operation': 'alarm'}}, 'hybrid', 'a'*64, 'b'*64),
            ({**authority, 'engineering': {**binding, 'extra': True}}, 'hybrid', 'a'*64, 'b'*64),
            (authority, 'decision', 'a'*64, 'b'*64),
            (authority, 'hybrid', 'c'*64, 'b'*64),
            (authority, 'hybrid', 'a'*64, 'not-a-digest'),
        ]
        for args in bad:
            with self.subTest(args=args[1:]):
                with self.assertRaises(ValueError):
                    N.control_binding(*args)

    def test_invalid_operation_stops_before_context_or_write(self):
        with patch.object(D, 'context', side_effect=AssertionError('context reached')), \
             patch.object(D, 'write_new', side_effect=AssertionError('write reached')):
            with self.assertRaises(ValueError):
                N.payload('decision', 'NO_AUTHORITY')

    def _parent_probe(self, argv):
        fake_root = INPUTS
        fake_eng = fake_root/'engineering'
        authority_path = fake_eng/'hybrid.authority.json'
        helper_sha, green_sha = 'a'*64, 'b'*64
        authority = {'mode': 'engineering_control', 'engineering': {
            'operation': 'hybrid', 'helper_sha256': helper_sha,
            'fixture_sha256': N.FIXTURE_SHA, 'root_green_sha256': green_sha}}

        def fake_file_sha(path):
            name = Path(path).name
            if name in N.PINS:
                return N.PINS[name]
            if name == 'engine.py':
                return helper_sha
            if name == 'ROOT-GREEN.md':
                return green_sha
            raise AssertionError('unexpected hash path '+str(path))

        real_read_bytes = Path.read_bytes
        def fake_read_bytes(path):
            if str(path) == '/proc/8765/cmdline':
                return b'\0'.join(argv)+b'\0'
            return real_read_bytes(path)

        old_cwd = Path.cwd()
        os.chdir(fake_root)
        try:
            with patch.object(N, 'ROOT', fake_root), patch.object(N, 'ENG', fake_eng), \
                 patch.object(D, 'context', return_value=(authority, 'c'*64, 1.0)), \
                 patch.object(D, 'file_sha', side_effect=fake_file_sha), \
                 patch.object(N.os, 'getpid', return_value=4321), \
                 patch.object(N.os, 'getpgrp', return_value=4321), \
                 patch.object(N.os, 'getppid', return_value=8765), \
                 patch.object(Path, 'read_bytes', fake_read_bytes), \
                 patch.object(D, 'arm_deadline', side_effect=ReachedPastParentCheck) as armed:
                try:
                    N.payload('hybrid', authority_path)
                finally:
                    reached = armed.called
        finally:
            os.chdir(old_cwd)
        return reached

    def test_counterexample_parent_path_token_is_not_exact_argv(self):
        runner = str(INPUTS/'run_capped.py').encode()
        bogus = [b'/usr/bin/python3', runner, b'--wall-seconds', b'999',
                 b'--stdout-file', b'/tmp/wrong', b'--', b'/bin/false']
        with self.assertRaises(ReachedPastParentCheck):
            self._parent_probe(bogus)

    def test_parent_without_path_token_rejects(self):
        missing = [b'/usr/bin/python3', b'/tmp/not-the-runner.py', b'--wall-seconds', b'10']
        with self.assertRaises(ValueError):
            self._parent_probe(missing)

    def test_static_no_new_lifecycle_and_deadline_order(self):
        source = (INPUTS/'engine.py').read_text()
        tree = ast.parse(source)
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        for forbidden in ('D.SOURCE', 'production=True', 'subprocess', 'fork(', 'setsid(', 'Popen', 'setitimer('):
            self.assertNotIn(forbidden, source)
        self.assertEqual(source.count("D.context(authority_path,'control')"), 1)
        self.assertEqual(source.count('D.arm_deadline('), 1)
        self.assertLess(source.index("D.context(authority_path,'control')"), source.index('D.arm_deadline('))
        self.assertLess(source.index('D.arm_deadline('), source.index("D.limits('control')"))
        self.assertLess(source.index("D.limits('control')"), source.index("operation+'.identity.json'"))
        self.assertLess(source.index("operation+'.identity.json'"), source.index("'tiny-engine-fixture.jsonl'"))
        self.assertLess(source.index("'tiny-engine-fixture.jsonl'"), source.index('os.execve('))


if __name__ == '__main__':
    unittest.main(verbosity=2)
