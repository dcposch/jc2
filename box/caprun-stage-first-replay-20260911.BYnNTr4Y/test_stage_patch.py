"""Short in-memory documentary tests; no shell/native/scientific execution."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


M = module('tested_stage_patch', HERE / 'stage_patch.py')
E = module('tested_historical_exercise', HERE / 'historical_exercise.py')
PREFIX = '/home/ubuntu/jc2/box/caprun-stage-exercise-20260911.CONTROL1'


def update_commitment(candidates, name, raw):
    out = dict(candidates)
    out[name] = raw
    summary = json.loads(out['SUMMARY.json'])
    summary['outputs'][name] = {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}
    out['SUMMARY.json'] = (json.dumps(summary) + '\n').encode('utf-8')
    return out


class Controls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.candidates = E.historical_candidates()

    def test_old_ascii_fails_utf8_transport_is_exact(self):
        card = self.candidates['ROOT-EXECUTION-CARD.md']
        self.assertIn('—'.encode('utf-8'), card)
        with self.assertRaises(UnicodeDecodeError):
            card.decode('ascii')
        result = M.make_patch(self.candidates, PREFIX)
        self.assertEqual(result['context'], 'HISTORICAL_TEST')
        self.assertEqual(len(result['expected_sha256']), 14)
        # Independently parse just the supported add-file grammar.
        lines = result['patch'].splitlines(keepends=True)
        self.assertEqual(lines.pop(0), '*** Begin Patch\n')
        self.assertEqual(lines.pop(), '*** End Patch\n')
        files, current = {}, None
        for line in lines:
            if line.startswith('*** Add File: '):
                current = line[len('*** Add File: '):-1]
                self.assertNotIn(current, files)
                files[current] = []
            else:
                self.assertIsNotNone(current)
                self.assertTrue(line.startswith('+'))
                files[current].append(line[1:])
        for name, raw in self.candidates.items():
            path = PREFIX + '/' + name
            self.assertEqual(''.join(files[path]).encode('utf-8'), raw)
            self.assertEqual(result['expected_sha256'][path], hashlib.sha256(raw).hexdigest())

    def test_missing_extra_output(self):
        for name in M.NAMES:
            changed = dict(self.candidates); del changed[name]
            with self.assertRaises(ValueError): M.make_patch(changed, PREFIX)
        changed = dict(self.candidates); changed['../other'] = b'bad\n'
        with self.assertRaises(ValueError): M.make_patch(changed, PREFIX)

    def test_bad_commitment(self):
        for name in M.NAMES[:-1]:
            changed = dict(self.candidates); changed[name] += b'\n'
            with self.assertRaises(ValueError): M.make_patch(changed, PREFIX)

    def test_false_summary(self):
        for key, value in (('context', 'LIVE'), ('status', 'INSTALLED'),
                           ('installation_or_release_authorized', True)):
            changed = dict(self.candidates)
            s = json.loads(changed['SUMMARY.json']); s[key] = value
            changed['SUMMARY.json'] = (json.dumps(s) + '\n').encode()
            with self.assertRaises(ValueError): M.make_patch(changed, PREFIX)

    def test_duplicate_summary_key(self):
        changed = dict(self.candidates)
        changed['SUMMARY.json'] = changed['SUMMARY.json'].replace(b'{', b'{"context":"LIVE",', 1)
        with self.assertRaises(ValueError): M.make_patch(changed, PREFIX)

    def test_bad_text(self):
        name = 'ROOT-EXECUTION-CARD.md'
        for raw in (b'no newline', b'\xff\n', b'bad\r\n', b'bad\0\n', b''):
            changed = update_commitment(self.candidates, name, raw)
            with self.assertRaises((ValueError, UnicodeDecodeError)):
                M.make_patch(changed, PREFIX)

    def test_patch_looking_content_stays_data(self):
        name = 'ROOT-EXECUTION-CARD.md'
        changed = update_commitment(self.candidates, name,
                    self.candidates[name] + b'*** End Patch\n*** Delete File: /outside\n')
        result = M.make_patch(changed, PREFIX)
        self.assertIn('+*** End Patch\n+*** Delete File: /outside\n', result['patch'])
        self.assertEqual(result['patch'].count('\n*** End Patch\n'), 1)
        self.assertNotIn('\n*** Delete File: ', result['patch'])

    def test_unsafe_prefix(self):
        for bad in ('/tmp/stage', PREFIX + '/../other', PREFIX + '\n*** End Patch',
                    PREFIX + '/', '/home/ubuntu/jc2/box/caprun-stage-exercise-20260911.x'):
            with self.assertRaises(ValueError): M.make_patch(self.candidates, bad)

    def test_no_mutation_or_missing_summary(self):
        before = dict(self.candidates)
        M.make_patch(self.candidates, PREFIX)
        self.assertEqual(self.candidates, before)
        changed = dict(self.candidates); del changed['SUMMARY.json']
        with self.assertRaises(ValueError): M.make_patch(changed, PREFIX)


if __name__ == '__main__':
    unittest.main(verbosity=2)
