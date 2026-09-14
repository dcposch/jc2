"""Bounded pure-data controls. Reads8 pinned historical texts; writes no files."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('tested_latebind', HERE / 'latebind.py')
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)
SOURCE = HERE.parent / 'caprun-closed-scope-b-execution-root-20260911'
PINS = {
    'ROOT-REGISTRATION.preholder.json': '31c942b17ed290f13b0bcd87457ec3a2b68f760fc4cf99443fee0e8386eceb74',
    'ROOT-REGISTRATION.json': '4d0d8475ed7d4aac1e42b70b1c7b4ee0198270ead0c3bb46adb78d7a91153ba3',
    'AUTHORITIES.preholder.json': '58d35c476c3dc7c4f6fe36adf73b79e5e0d8843e6ddd388c27a745b747a40d2e',
    'ROOT-EXECUTION-CARD.preholder.md': '1d9f837a23bb94b9609c7ac572909afbb0a4a96e44cb3c84b4875a9b310d02be',
    'ROOT-EXECUTION-CARD.md': 'a92cf2680c8d6aff6044f5376fb1dcfeed87a29c527d55c953d940e39a99f281',
    'final-install.preholder.sh': '6d414284920782a75a951fa3e59a8c23a391470a5efea28003b968bb1052fc62',
    'final-install.sh': 'abff072f218cbecaa6f47278891a62b36463a70e34ae4be546e44a5f3c3cd208',
    'FINAL-INSTALL-INPUTS.sha256': 'd90196456531bdf917098c84a84a88861384c220dcff6882a5305bacd48e8943'}


def wire(obj):
    return (json.dumps(obj, ensure_ascii=True, separators=(',', ':'))+'\n').encode('ascii')


class Controls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.raw = {n: (SOURCE/n).read_bytes() for n in PINS}
        for n, raw in cls.raw.items():
            if hashlib.sha256(raw).hexdigest() != PINS[n]:
                raise ValueError('historical pin: '+n)

    def setUp(self):
        self.bundle = {n: self.raw[n] for n in M.NAMES}
        self.pins = {n: PINS[n] for n in M.NAMES}
        final = json.loads(self.raw['ROOT-REGISTRATION.json'])
        self.obs = {k: final[k] for k in
                    ('instance_id', 'hostname', 'boot_id', 'pid_namespace', 'cgroup_path')}
        self.obs.update(schema='caprun-late-observation/v1', context='HISTORICAL_TEST',
            holder_pid=32389, start_ticks=73194, invocation_id='ac02f213754c46888489c54d5cb3e60a',
            outer_device=31, outer_inode=6012,
            leaves=[dict(name=n, **final['closed_child_guard']['leaves'][n]) for n in M.PHASES],
            coordinator_receipt_sha256='780d953e46feecfbe070fd859c4f9b46b104dcfb1f97f6ceaf7f35c6a5a35968',
            native_manifest_sha256=final['pins'][final['native_manifest']],
            native_list_sha256='f5a855a617f317080e23724f2590cfb74aa674986285b89752816bbd991658c0')

    def call(self, obs=None, decision_change=None):
        raw = wire(self.obs if obs is None else obs)
        decision = dict(schema='ROOT_METADATA_BINDING_ONLY_NOT_RELEASE', context='HISTORICAL_TEST',
            prepared_pins=self.pins, observation_sha256=hashlib.sha256(raw).hexdigest(),
            enabled=True, exclusive_no_concurrent_writer=True, root_no_migration=True,
            freeze_token=M.FREEZE)
        if decision_change:
            decision.update(decision_change)
        return M.bind(self.bundle, self.pins, raw, wire(decision))

    def change_bundle(self, name, raw):
        self.bundle[name] = raw
        self.pins[name] = hashlib.sha256(raw).hexdigest()

    def test_historical_exact_and_nonprobe_hashes(self):
        out = self.call()
        self.assertEqual(len(out), 14)
        for n in ('ROOT-REGISTRATION.json', 'ROOT-EXECUTION-CARD.md',
                  'final-install.sh', 'FINAL-INSTALL-INPUTS.sha256'):
            self.assertEqual(out[n], self.raw[n], n)
        old = json.loads(self.raw['AUTHORITIES.preholder.json'])
        final = json.loads(out['ROOT-REGISTRATION.json'])
        for label in M.PHASES:
            if label not in ('valid', 'dummy'):
                expected = (json.dumps(old[label], sort_keys=True, separators=(',', ':'),
                                       ensure_ascii=True)+'\n').encode('ascii')
                self.assertEqual(out['authority/'+label+'.json'], expected)
            if label == 'refuse-hash':
                self.assertEqual(final['commands'][label][-3], '0'*64)
        summary = json.loads(out['SUMMARY.json'])
        self.assertEqual(summary['status'], M.STATUS)
        self.assertFalse(summary['installation_or_release_authorized'])

    def test_missing_duplicate_wrong_leaf(self):
        variants = []
        x = copy.deepcopy(self.obs); x['leaves'].pop(); variants.append(x)
        x = copy.deepcopy(self.obs); x['leaves'][1] = x['leaves'][0].copy(); variants.append(x)
        x = copy.deepcopy(self.obs); x['leaves'][0]['device'] = '31'; variants.append(x)
        x = copy.deepcopy(self.obs); x['leaves'][0]['path'] += '/wrong'; variants.append(x)
        x = copy.deepcopy(self.obs); x['leaves'][0]['inode'] = x['outer_inode']; variants.append(x)
        for x in variants:
            with self.subTest(x=x['leaves'][0]):
                with self.assertRaises(ValueError): self.call(x)

    def test_bool_not_integer(self):
        for field in ('holder_pid', 'start_ticks', 'outer_device', 'outer_inode'):
            x = copy.deepcopy(self.obs); x[field] = True
            with self.subTest(field=field):
                with self.assertRaises(ValueError): self.call(x)
        x = copy.deepcopy(self.obs); x['leaves'][0]['inode'] = True
        with self.assertRaises(ValueError): self.call(x)

    def test_decisions_fail_closed(self):
        for bad in ({'enabled': False}, {'enabled': 1}, {'root_no_migration': False},
                    {'freeze_token': 'RELEASE'}, {'observation_sha256': '0'*64},
                    {'context': 'LIVE'}):
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError): self.call(decision_change=bad)

    def test_hash_drift(self):
        self.bundle[M.NAMES[0]] += b' '
        with self.assertRaises(ValueError): self.call()

    def test_order_path_placeholder_and_cap(self):
        for case in ('order', 'path', 'placeholder', 'cap'):
            self.setUp()
            r = json.loads(self.bundle[M.NAMES[0]])
            if case == 'order': r['allowed_phases'].reverse()
            elif case == 'path': r['commands']['valid'][6] += '/wrong'
            elif case == 'placeholder': r['hostname'] = 'JC2_EXTRA_PLACEHOLDER'
            else: r['limits']['cpu_seconds'] = '2101'
            self.change_bundle(M.NAMES[0], wire(r))
            with self.subTest(case=case):
                with self.assertRaises(ValueError): self.call()

    def test_duplicate_json_and_numbers(self):
        for bad in (b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":1.0}'):
            with self.assertRaises(ValueError): M.load(bad)

    def test_no_mutation_and_preservation(self):
        before = copy.deepcopy((self.bundle, self.pins, self.obs))
        out = self.call()
        self.assertEqual((self.bundle, self.pins, self.obs), before)
        old, new = json.loads(self.bundle[M.NAMES[0]]), json.loads(out['ROOT-REGISTRATION.json'])
        for field in ('source_limits', 'limits', 'source_files', 'source_pins', 'place',
                      'admission_deadline_utc', 'mathematical_deadline_utc', 'profiles'):
            self.assertEqual(old[field], new[field])

    def test_each_device_is_independent(self):
        self.obs['leaves'][5]['device'] = 32
        out = self.call()
        reg = json.loads(out['ROOT-REGISTRATION.json'])
        self.assertEqual(reg['closed_child_guard']['leaves']['valid']['device'], 32)
        self.assertEqual(reg['closed_child_guard']['leaves']['dummy']['device'], 31)
        self.assertEqual(json.loads(out['authority/valid.json'])['closed_scope']['device'], 32)

    def test_wrong_identity_or_native_role(self):
        for key, value in (('boot_id', 'wrong'), ('native_manifest_sha256', self.obs['native_list_sha256'])):
            x = copy.deepcopy(self.obs); x[key] = value
            with self.assertRaises(ValueError): self.call(x)

    def test_size_bound(self):
        self.bundle[M.NAMES[2]] = b'x'*(M.MAX_INPUT+1)
        self.pins[M.NAMES[2]] = hashlib.sha256(self.bundle[M.NAMES[2]]).hexdigest()
        with self.assertRaises(ValueError): self.call()

    def test_future_prepared_bindings_are_preserved(self):
        old = json.loads(self.bundle[M.NAMES[0]])
        replacements = {
            'jc2-closedchild-preflight9-20260911b': 'jc2-closedchild-preflight9-20260912c',
            old['instance_id']: 'i-0123456789abcdef0',
            old['hostname']: 'ip-192-0-2-10',
            old['boot_id']: '12345678-1234-1234-1234-123456789abc',
            old['pid_namespace']: 'pid:[4026555555]',
            '2026-09-11': '2026-09-12'}
        for name, raw in list(self.bundle.items()):
            changed = raw.decode('utf-8')
            for before, after in replacements.items():
                changed = changed.replace(before, after)
            self.change_bundle(name, changed.encode('utf-8'))
        prepared = json.loads(self.bundle[M.NAMES[0]])
        for field in ('instance_id', 'hostname', 'boot_id', 'pid_namespace', 'cgroup_path'):
            self.obs[field] = prepared[field]
        for leaf in self.obs['leaves']:
            leaf['path'] = prepared['cgroup_path']+'/'+leaf['name']
        out = self.call()
        final = json.loads(out['ROOT-REGISTRATION.json'])
        for field in ('instance_id', 'hostname', 'boot_id', 'pid_namespace',
                      'admission_deadline_utc', 'mathematical_deadline_utc',
                      'task_deadline_utc', 'worker_deadline_utc', 'pins', 'source_pins'):
            self.assertEqual(final[field], prepared[field])
        self.assertNotEqual(final['instance_id'], old['instance_id'])
        self.assertNotEqual(final['admission_deadline_utc'], old['admission_deadline_utc'])
        for raw in out.values():
            self.assertNotIn(b'jc2-closedchild-preflight9-20260911b', raw)

    def test_text_placeholder_count(self):
        name = M.NAMES[2]
        for suffix in (b'JC2_EXTRA_PLACEHOLDER\n', b'JC2_CAPTURED_HOLDER_PID_PLACEHOLDER\n'):
            self.setUp()
            self.change_bundle(name, self.bundle[name]+suffix)
            with self.assertRaises(ValueError): self.call()


if __name__ == '__main__':
    unittest.main(verbosity=2)
