"""Bounded historical documentary tests; never write/apply candidate bytes."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
CALLER_PATH = HERE / 'caller.py'
HISTORY = HERE.parent / 'caprun-closed-scope-b-execution-root-20260911'
EXERCISE_PATH = HERE.parent / 'caprun-candidate-stage-root-20260911/EXERCISE.json'
FIXTURES = HERE
# Reviewers may replace only these location bindings and caller.DEPENDENCY_PATHS
# in memory; the historical and helper expected digests remain unchanged.
HISTORY_PINS = {
    'ROOT-REGISTRATION.preholder.json': '31c942b17ed290f13b0bcd87457ec3a2b68f760fc4cf99443fee0e8386eceb74',
    'ROOT-REGISTRATION.json': '4d0d8475ed7d4aac1e42b70b1c7b4ee0198270ead0c3bb46adb78d7a91153ba3',
    'AUTHORITIES.preholder.json': '58d35c476c3dc7c4f6fe36adf73b79e5e0d8843e6ddd388c27a745b747a40d2e',
    'ROOT-EXECUTION-CARD.preholder.md': '1d9f837a23bb94b9609c7ac572909afbb0a4a96e44cb3c84b4875a9b310d02be',
    'ROOT-EXECUTION-CARD.md': 'a92cf2680c8d6aff6044f5376fb1dcfeed87a29c527d55c953d940e39a99f281',
    'final-install.preholder.sh': '6d414284920782a75a951fa3e59a8c23a391470a5efea28003b968bb1052fc62',
    'final-install.sh': 'abff072f218cbecaa6f47278891a62b36463a70e34ae4be546e44a5f3c3cd208',
    'FINAL-INSTALL-INPUTS.sha256': 'd90196456531bdf917098c84a84a88861384c220dcff6882a5305bacd48e8943',
}
spec = importlib.util.spec_from_file_location('supplied_caller', CALLER_PATH)
C = importlib.util.module_from_spec(spec)
spec.loader.exec_module(C)


def wire(value):
    return (json.dumps(value, ensure_ascii=True, separators=(',', ':')) + '\n').encode('ascii')


class Controls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.historical = {n: C.read_bounded(HISTORY / n) for n in HISTORY_PINS}
        for n, raw in cls.historical.items():
            if hashlib.sha256(raw).hexdigest() != HISTORY_PINS[n]:
                raise ValueError('historical pin: ' + n)
        raw = C.read_bounded(EXERCISE_PATH)
        if hashlib.sha256(raw).hexdigest() != 'e37735ceeee1d60ee97ce492e196c312a8b9ee5d887f8abc9809af71924ce5b5':
            raise ValueError('exercise pin')
        cls.exercise = json.loads(raw)
        cls.binder, cls.stage = C.dependencies()

    def setUp(self):
        self.paths = [FIXTURES / n for n in ('fixture-pins.json', 'fixture-observation.json', 'fixture-decision.json')]
        self.args = [str(HISTORY), *(str(p) for p in self.paths), self.exercise['directory'], 'HISTORICAL_TEST']
        self.raw = {str(p): C.read_bounded(p) for p in self.paths}

    def invoke(self, changes=None, args=None):
        original = C.read_bounded
        replacements = {} if changes is None else changes
        def read(path):
            return replacements[str(path)] if str(path) in replacements else original(path)
        out, err = io.StringIO(), io.StringIO()
        with patch.object(C, 'read_bounded', side_effect=read), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            status = C.main(self.args if args is None else args)
        return status, out.getvalue(), err.getvalue()

    def assert_refused(self, changes=None, args=None):
        status, out, err = self.invoke(changes, args)
        self.assertEqual((status, out, err), (2, '', 'REFUSED: candidate input or dependency\n'))

    def verify_packet(self, raw):
        self.assertTrue(raw.isascii())
        obj = json.loads(raw)
        self.assertEqual(set(obj), {'patch', 'expected_sha256', 'status', 'context', 'candidate_bytes'})
        self.assertEqual(obj['status'], 'CANDIDATE_NOT_INSTALLED_NOT_RELEASED')
        self.assertEqual(obj['context'], 'HISTORICAL_TEST')
        self.assertEqual(obj['candidate_bytes'], 78889)
        self.assertEqual(obj['expected_sha256'], self.exercise['expected_sha256'])
        lines = obj['patch'].split('\n')
        self.assertEqual((lines[0], lines[-2], lines[-1]), ('*** Begin Patch', '*** End Patch', ''))
        reconstructed = {}
        current = None
        for line in lines[1:-2]:
            if line.startswith('*** Add File: '):
                current = line[len('*** Add File: '):]
                self.assertNotIn(current, reconstructed)
                reconstructed[current] = bytearray()
            else:
                self.assertTrue(line.startswith('+') and current is not None)
                reconstructed[current].extend((line[1:] + '\n').encode('utf-8'))
        self.assertEqual(len(reconstructed), 14)
        self.assertEqual({p: hashlib.sha256(b).hexdigest() for p, b in reconstructed.items()}, obj['expected_sha256'])
        self.assertEqual(sum(map(len, reconstructed.values())), 78889)
        for n in ('ROOT-REGISTRATION.json', 'ROOT-EXECUTION-CARD.md', 'final-install.sh', 'FINAL-INSTALL-INPUTS.sha256'):
            self.assertEqual(bytes(reconstructed[self.args[4] + '/' + n]), self.historical[n])
        summary = json.loads(reconstructed[self.args[4] + '/SUMMARY.json'])
        self.assertEqual(summary['context'], 'HISTORICAL_TEST')
        self.assertFalse(summary['installation_or_release_authorized'])
        self.assertIn(b'\xe2\x80\x94', reconstructed[self.args[4] + '/ROOT-EXECUTION-CARD.md'])

    def test_real_standalone_cli(self):
        # Only this own short documentary CLI is launched. No shell or file outputs.
        run = subprocess.run([sys.executable, '-I', '-S', '-B', str(CALLER_PATH), *self.args],
                             capture_output=True, timeout=10, check=False)
        self.assertEqual((run.returncode, run.stderr), (0, b''))
        self.verify_packet(run.stdout)

    def test_main_ascii_stream(self):
        buffer = io.BytesIO()
        stream = io.TextIOWrapper(buffer, encoding='ascii')
        with contextlib.redirect_stdout(stream):
            self.assertEqual(C.main(self.args), 0)
        stream.flush()
        self.verify_packet(buffer.getvalue())

    def test_missing_argument_and_file(self):
        self.assert_refused(args=self.args[:-1])
        with patch.object(C, 'read_bounded', side_effect=FileNotFoundError):
            self.assert_refused()

    def test_pins_context_decision_and_json(self):
        pins = json.loads(self.raw[str(self.paths[0])])
        pins[next(iter(pins))] = '0' * 64
        self.assert_refused({str(self.paths[0]): wire(pins)})
        wrong = self.args[:]; wrong[-1] = 'ROOT_ATTESTED_CANDIDATE'
        self.assert_refused(args=wrong)
        decision = json.loads(self.raw[str(self.paths[2])]); decision['enabled'] = False
        self.assert_refused({str(self.paths[2]): wire(decision)})
        for invalid in (b'{"x":1,"x":2}\n', b'{"x":1.0}\n', b'{"x":NaN}\n'):
            with self.subTest(invalid=invalid):
                self.assert_refused({str(self.paths[0]): invalid})

    def test_wrong_dependency_hash_precedes_import(self):
        bad = dict(C.DEPENDENCY_PATHS); bad['stage_patch'] = self.paths[0]
        with patch.object(C, 'DEPENDENCY_PATHS', bad), patch.object(C.importlib.util, 'spec_from_file_location') as loader:
            self.assert_refused()
            loader.assert_not_called()

    def test_eight_separators_after_valid_updated_commitments(self):
        for char in C.FORBIDDEN:
            with self.subTest(codepoint=ord(char)):
                bundle = {n: self.historical[n] for n in self.binder.NAMES}
                name = 'ROOT-EXECUTION-CARD.preholder.md'
                bundle[name] += ('\nHistorical separator control ' + char + '*** Add File: not-a-path\n').encode('utf-8')
                pins = {n: hashlib.sha256(raw).hexdigest() for n, raw in bundle.items()}
                obs = self.raw[str(self.paths[1])]
                decision = json.loads(self.raw[str(self.paths[2])])
                decision['prepared_pins'] = pins
                decision_raw = wire(decision)
                # This must reach the NEW hygiene barrier, not stale hash rejection.
                candidates = self.binder.bind(bundle, pins, obs, decision_raw)
                self.assertTrue(any(char in raw.decode('utf-8') for raw in candidates.values()))
                self.stage.make_patch(candidates, self.args[4])
                changes = {str(HISTORY / n): raw for n, raw in bundle.items()}
                changes.update({str(self.paths[0]): wire(pins), str(self.paths[2]): decision_raw})
                original = C.read_bounded
                def read(path):
                    return changes[str(path)] if str(path) in changes else original(path)
                with patch.object(C, 'read_bounded', side_effect=read):
                    with self.assertRaisesRegex(ValueError, '^forbidden universal-newline separator$'):
                        C.packet(self.args)
                self.assert_refused(changes)


if __name__ == '__main__':
    unittest.main()
