"""FIRST review harness (Fable 5.1): replay the 13 producer tests with SOURCE overridden
to the frozen inputs directory, then run in-memory mutation controls against latebind.bind.
Stdlib only; writes nothing; executes no input document; imports only the charged
latebind.py (through the charged test_latebind.py) and this file.
Usage: python3 -I -S -B review_controls.py /tmp/jc2-lane.a27KVq/inputs"""
import copy
import hashlib
import importlib.util
import json
import re
import sys
import unittest
from pathlib import Path

PINS = {
    'TASK.md': 'f276baaa99a89a46c32e279d0bb98a449ef3cc63c567f7afde818d9c9f9cbdf9',
    'latebind.py': 'ff2beb48b68b55dc5035709a9114bc7202dd38cef488d20b8163d0c55e2366fe',
    'test_latebind.py': '85d5390babe473deed13e9a88c40ea82193c6306284a4224cdb021f65ca5ec06',
    'CONTRACT.md': '33e7308f21b60beb884977829fba0afeefd5ce6cac5183435677779a18de2d12',
    'caprun-latebinder-code-astra-20260911.md': '68e416319cfb0e52900fd0ff0444644aa0d17a8e1d5488106876197f49b4e309',
    'ROOT-REGISTRATION.preholder.json': '31c942b17ed290f13b0bcd87457ec3a2b68f760fc4cf99443fee0e8386eceb74',
    'ROOT-REGISTRATION.json': '4d0d8475ed7d4aac1e42b70b1c7b4ee0198270ead0c3bb46adb78d7a91153ba3',
    'AUTHORITIES.preholder.json': '58d35c476c3dc7c4f6fe36adf73b79e5e0d8843e6ddd388c27a745b747a40d2e',
    'ROOT-EXECUTION-CARD.preholder.md': '1d9f837a23bb94b9609c7ac572909afbb0a4a96e44cb3c84b4875a9b310d02be',
    'ROOT-EXECUTION-CARD.md': 'a92cf2680c8d6aff6044f5376fb1dcfeed87a29c527d55c953d940e39a99f281',
    'final-install.preholder.sh': '6d414284920782a75a951fa3e59a8c23a391470a5efea28003b968bb1052fc62',
    'final-install.sh': 'abff072f218cbecaa6f47278891a62b36463a70e34ae4be546e44a5f3c3cd208',
    'FINAL-INSTALL-INPUTS.sha256': 'd90196456531bdf917098c84a84a88861384c220dcff6882a5305bacd48e8943'}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def wire(o):
    return (json.dumps(o, ensure_ascii=True, separators=(',', ':')) + '\n').encode('ascii')


def leafdiff(a, b, path=''):
    out = []
    if type(a) is dict and type(b) is dict and set(a) == set(b):
        for k in a:
            out += leafdiff(a[k], b[k], path + '/' + k)
    elif type(a) is list and type(b) is list and len(a) == len(b):
        for i, (x, y) in enumerate(zip(a, b)):
            out += leafdiff(x, y, path + '/' + str(i))
    elif a != b or type(a) is not type(b):
        out.append(path)
    return out


class Ctx:
    def __init__(self, M, raw):
        self.M, self.raw = M, raw
        self.bundle = {n: raw[n] for n in M.NAMES}
        final = json.loads(raw['ROOT-REGISTRATION.json'])
        self.final = final
        self.obs = {k: final[k] for k in ('instance_id', 'hostname', 'boot_id', 'pid_namespace', 'cgroup_path')}
        self.obs.update(schema='caprun-late-observation/v1', context='HISTORICAL_TEST',
                        holder_pid=32389, start_ticks=73194, invocation_id='ac02f213754c46888489c54d5cb3e60a',
                        outer_device=31, outer_inode=6012,
                        leaves=[dict(name=n, **final['closed_child_guard']['leaves'][n]) for n in M.PHASES],
                        coordinator_receipt_sha256='780d953e46feecfbe070fd859c4f9b46b104dcfb1f97f6ceaf7f35c6a5a35968',
                        native_manifest_sha256=final['pins'][final['native_manifest']],
                        native_list_sha256='f5a855a617f317080e23724f2590cfb74aa674986285b89752816bbd991658c0')

    def call(self, obs=None, bundle=None, dec=None):
        o = wire(self.obs if obs is None else obs)
        b = self.bundle if bundle is None else bundle
        pins = {n: sha(b[n]) for n in self.M.NAMES}
        d = dict(schema='ROOT_METADATA_BINDING_ONLY_NOT_RELEASE', context='HISTORICAL_TEST',
                 prepared_pins=dict(pins), observation_sha256=sha(o), enabled=True,
                 exclusive_no_concurrent_writer=True, root_no_migration=True, freeze_token=self.M.FREEZE)
        if dec:
            d.update(dec)
        return self.M.bind(b, pins, o, wire(d))

    def obs_with(self, fn):
        x = copy.deepcopy(self.obs)
        fn(x)
        return x

    def bundle_text(self, name, fn):
        b = dict(self.bundle)
        b[name] = fn(b[name].decode('utf-8')).encode('utf-8')
        return b

    def bundle_json(self, name, fn):
        b = dict(self.bundle)
        obj = json.loads(b[name])
        fn(obj)
        b[name] = (json.dumps(obj, indent=2) + '\n').encode('ascii')
        return b


ROWS = []


def expect(name, want, fn):
    """want: REJECT (must raise) / ACCEPT / EXTERNAL (accepted by the helper; caller duty)."""
    try:
        fn()
        got = 'ACCEPT'
    except ValueError as e:
        got = 'REJECT ValueError: ' + str(e)[:60]
    except Exception as e:  # any other exception type is still fail-closed but noted
        got = 'REJECT ' + type(e).__name__
    ok = got.startswith('REJECT') if want == 'REJECT' else got == 'ACCEPT'
    ROWS.append((name, want, got, ok))
    print(('PASS' if ok else 'FAIL'), name, '| want', want, '| got', got)
    return ok


def controls(M, raw):
    c = Ctx(M, raw)
    reg0, auth0 = json.loads(raw['ROOT-REGISTRATION.preholder.json']), json.loads(raw['AUTHORITIES.preholder.json'])
    out = c.call()
    assert out == c.call(), 'nondeterministic'
    print('PASS C01 deterministic; 14 outputs:', sorted(out))
    reg1 = json.loads(out['ROOT-REGISTRATION.json'])
    d = leafdiff(reg0, reg1)
    cats = {'flags': [p for p in d if p in ('/enabled', '/exclusive_no_concurrent_writer', '/closed_child_guard/root_no_migration')],
            'outer': [p for p in d if p.startswith('/closed_child_guard/outer_')],
            'leaves': [p for p in d if p.startswith('/closed_child_guard/leaves/')],
            'argv': [p for p in d if p.startswith('/commands/')]}
    other = set(d) - set(sum(cats.values(), []))
    print('C02 registration diff', {k: len(v) for k, v in cats.items()}, 'total', len(d), 'unclassified', sorted(other))
    assert (len(cats['flags']), len(cats['outer']), len(cats['leaves']), len(cats['argv']), len(d), other) == (3, 2, 18, 44, 67, set())
    auth1 = {l: json.loads(out['authority/' + l + '.json']) for l in M.PHASES}
    da = leafdiff(auth0, auth1)
    print('C02 authority diff', da)
    assert sorted(da) == ['/dummy/closed_scope/device', '/dummy/closed_scope/inode', '/valid/closed_scope/device', '/valid/closed_scope/inode']
    for l in M.PHASES:
        cmd = reg1['commands'][l]
        assert cmd[cmd.index('--closed-child-device') + 1] == str(reg1['closed_child_guard']['leaves'][l]['device'])
        assert cmd[cmd.index('--closed-child-inode') + 1] == str(reg1['closed_child_guard']['leaves'][l]['inode'])
        assert cmd[cmd.index('--closed-outer-device') + 1] == '31' and cmd[cmd.index('--closed-outer-inode') + 1] == '6012'
        flag = '--policy-sha256' if l in ('valid', 'dummy') else '--authorization-sha256'
        slot = cmd[cmd.index(flag) + 1]
        assert slot == ('0' * 64 if l == 'refuse-hash' else sha(out['authority/' + l + '.json'])), l
        assert out['authority/' + l + '.json'] == (json.dumps(auth1[l], sort_keys=True, separators=(',', ':'), ensure_ascii=True) + '\n').encode()
    print('PASS C03 nine argv slots bound to own leaf pair, outer pair, own canonical digest; refuse-hash zero; refuse-hash object digest', sha(out['authority/refuse-hash.json'])[:16], '(nonzero)')
    r_sha, c_sha = sha(out['ROOT-REGISTRATION.json']), sha(out['ROOT-EXECUTION-CARD.md'])
    man = out['FINAL-INSTALL-INPUTS.sha256'].decode()
    m_sha = sha(out['FINAL-INSTALL-INPUTS.sha256'])
    card, inst = out['ROOT-EXECUTION-CARD.md'].decode(), out['final-install.sh'].decode()
    assert man == r_sha + '  ROOT-REGISTRATION.json\n' + c_sha + '  ROOT-EXECUTION-CARD.md\n' + c.obs['native_list_sha256'] + '  native.sha256\n'
    assert 'final-install' not in man and sha(out['final-install.sh']) not in man
    assert card.count(r_sha) == 1 and c_sha not in card and m_sha not in card
    assert inst.count(r_sha) == 2 and inst.count(c_sha) == 1 and inst.count(m_sha) == 1 and sha(out['final-install.sh']) not in inst
    for l in M.PHASES:
        a = out['authority/' + l + '.json'].decode()
        assert r_sha not in a and c_sha not in a and m_sha not in a
    s = json.loads(out['SUMMARY.json'])
    assert set(s['outputs']) == set(out) - {'SUMMARY.json'} and sha(out['SUMMARY.json']) not in out['SUMMARY.json'].decode()
    assert all(s['outputs'][n]['sha256'] == sha(out[n]) for n in s['outputs'])
    assert s['status'] == 'CANDIDATE_NOT_INSTALLED_NOT_RELEASED' and s['installation_or_release_authorized'] is False
    assert len(s['text_changes']['card']) == 8 and len(s['text_changes']['installer']) == 7 and len(s['argv_changes']) == 44
    inv = {reg1['pins'][reg1['native_manifest']], reg1['pins'][reg1['source_native_manifest']]}
    assert c.obs['native_list_sha256'] not in inv and len(inv) == 2
    print('PASS C04 acyclic policy->registration->card->manifest->installer; manifest excludes installer; summary excludes self; three native digests distinct in data')
    tok = re.compile(r'JC2_[A-Z0-9_]+_PLACEHOLDER')
    holders = sorted(n for n, v in out.items() if tok.search(v.decode('utf-8')))
    assert holders == ['SUMMARY.json'], holders  # the summary's change log names the replaced tokens
    print('PASS C05 no residual placeholder token in the 13 candidate documents (SUMMARY.json change log names the old tokens)')
    ob = c.obs_with(lambda x: x.update(context='ROOT_ATTESTED_CANDIDATE'))
    o2 = c.call(obs=ob, dec={'context': 'ROOT_ATTESTED_CANDIDATE'})
    same = [n for n in out if out[n] == o2[n]]
    print('C06 outputs byte-identical across HISTORICAL_TEST vs ROOT_ATTESTED_CANDIDATE:', len(same), 'of 14; differing:', sorted(set(out) - set(same)))
    assert sorted(set(out) - set(same)) == ['SUMMARY.json'] and json.loads(o2['SUMMARY.json'])['context'] == 'ROOT_ATTESTED_CANDIDATE'
    src = raw['latebind.py'].decode()
    print('C07 latebind.py source: 64-hex literals', len(re.findall(r'[0-9a-f]{64}', src)), '; instance/boot/date literals',
          any(t in src for t in ('i-0', '55c4b95a', '2026-', 'ip-172')), '; imports', sorted(re.findall(r'^import (\w+)', src, re.M)))
    assert len(re.findall(r'[0-9a-f]{64}', src)) == 0 and sorted(re.findall(r'^import (\w+)', src, re.M)) == ['copy', 'hashlib', 'json', 're']
    assert not any(t in src for t in ('open(', 'subprocess', 'os.', 'sys.', 'socket', 'pathlib', 'exec(', 'eval('))
    basepins = {n: sha(c.bundle[n]) for n in M.NAMES}
    expect('M01 observation extra key', 'REJECT', lambda: c.call(c.obs_with(lambda x: x.update(extra=1))))
    expect('M02 holder_pid 2**31', 'REJECT', lambda: c.call(c.obs_with(lambda x: x.update(holder_pid=2 ** 31))))
    expect('M03 holder_pid 0', 'REJECT', lambda: c.call(c.obs_with(lambda x: x.update(holder_pid=0))))
    expect('M04 start_ticks string', 'REJECT', lambda: c.call(c.obs_with(lambda x: x.update(start_ticks='73194'))))
    expect('M05 invocation uppercase', 'REJECT', lambda: c.call(c.obs_with(lambda x: x.update(invocation_id=x['invocation_id'].upper()))))
    expect('M06 leaf device 2**64', 'REJECT', lambda: c.call(c.obs_with(lambda x: x['leaves'][0].update(device=2 ** 64))))
    expect('M07 leaves as dict', 'REJECT', lambda: c.call(c.obs_with(lambda x: x.update(leaves={l['name']: l for l in x['leaves']}))))
    expect('M08 ten leaves (dup name)', 'REJECT', lambda: c.call(c.obs_with(lambda x: x['leaves'].append(dict(x['leaves'][0], inode=9999)))))
    expect('M09 two leaves same (device,inode)', 'REJECT', lambda: c.call(c.obs_with(lambda x: x['leaves'][2].update(inode=x['leaves'][1]['inode']))))
    expect('M10 leaf shares outer inode on other device', 'ACCEPT', lambda: c.call(c.obs_with(lambda x: x['leaves'][2].update(device=32, inode=6012))))
    expect('M11 cgroup_path mismatch', 'REJECT', lambda: c.call(c.obs_with(lambda x: x.update(cgroup_path=x['cgroup_path'] + 'x'))))
    expect('M12 native_manifest_sha256 = source inventory digest', 'REJECT', lambda: c.call(c.obs_with(lambda x: x.update(native_manifest_sha256=c.final['pins'][c.final['source_native_manifest']]))))
    expect('M13 native_list_sha256 = full inventory digest (role swap, not enforced)', 'EXTERNAL', lambda: c.call(c.obs_with(lambda x: x.update(native_list_sha256=x['native_manifest_sha256']))))
    expect('M14 receipt sha uppercase', 'REJECT', lambda: c.call(c.obs_with(lambda x: x.update(coordinator_receipt_sha256=x['coordinator_receipt_sha256'].upper()))))
    expect('M15 decision extra key', 'REJECT', lambda: c.call(dec={'note': 'x'}))
    expect('M16 decision prepared_pins extra entry', 'REJECT', lambda: c.call(dec={'prepared_pins': dict(basepins, extra='0' * 64)}))
    expect('M17 decision context mismatch', 'REJECT', lambda: c.call(dec={'context': 'ROOT_ATTESTED_CANDIDATE'}))
    expect('M18 decision exclusive flag "true" string', 'REJECT', lambda: c.call(dec={'exclusive_no_concurrent_writer': 'true'}))
    expect('M19 decision schema RELEASE', 'REJECT', lambda: c.call(dec={'schema': 'ROOT_RELEASE'}))
    expect('M20 preholder enabled=true', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[0], lambda r: r.update(enabled=True))))
    expect('M21 preholder enabled=0 (int)', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[0], lambda r: r.update(enabled=0))))
    expect('M22 registration extra top key', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[0], lambda r: r.update(extra=1))))
    expect('M23 refuse-hash template digest nonzero', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[0], lambda r: r['commands']['refuse-hash'].__setitem__(-3, 'JC2_REFUSE_HASH_AUTH_SHA_PLACEHOLDER'))))
    expect('M24 aggregate_cpu_start_usec "1"', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[0], lambda r: r.update(aggregate_cpu_start_usec='1'))))
    expect('M25 dormant produce profile changed', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[0], lambda r: r['profiles'].__setitem__('produce', [900, 600, 8589934592]))))
    expect('M26 valid argv wall-seconds 900', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[0], lambda r: r['commands']['valid'].__setitem__(r['commands']['valid'].index('--wall-seconds') + 1, '900'))))
    expect('M27 tenth phase added', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[0], lambda r: (r['allowed_phases'].append('produce'), r['commands'].__setitem__('produce', r['commands']['valid'])))))
    expect('M28 registration self pin', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[0], lambda r: r['pins'].__setitem__(r['outer_argv'][-1], '1' * 64))))
    expect('M29 source_limits cpu 601', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[0], lambda r: r['source_limits'].update(cpu_seconds='601'))))
    expect('M30 base path other prefix', 'REJECT', lambda: c.call(bundle=c.bundle_text(M.NAMES[0], lambda t: t.replace('/opt/jc2-closedchild-preflight9-20260911b', '/opt/jc2-other-20260911b'))))
    expect('M31 authorities valid.closed_scope.device preset', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[1], lambda a: a['valid']['closed_scope'].update(device=31))))
    expect('M32 authorities refuse-status REGISTERED', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[1], lambda a: a['refuse-status'].update(status='REGISTERED'))))
    expect('M33 authorities valid science_outcome POSITIVE', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[1], lambda a: a['valid'].update(science_outcome='POSITIVE'))))
    expect('M34 authorities refuse-caps limits restored to 600', 'REJECT', lambda: c.call(bundle=c.bundle_json(M.NAMES[1], lambda a: a['refuse-caps']['limits'].update(cpu_seconds='600'))))
    expect('M35 authority key order permuted (canonical sort absorbs)', 'ACCEPT', lambda: c.call(bundle=c.bundle_json(M.NAMES[1], lambda a: a.update({'dummy': a.pop('dummy'), 'valid': a.pop('valid')}))))
    expect('M36 card DISABLED heading twice', 'REJECT', lambda: c.call(bundle=c.bundle_text(M.NAMES[2], lambda t: t + '# ROOT closed-child nine-phase execution card — DISABLED\n')))
    expect('M37 card unformed sentence removed', 'REJECT', lambda: c.call(bundle=c.bundle_text(M.NAMES[2], lambda t: t.replace('Final registration and holder topology remain unformed in this preholder card.', 'x'))))
    expect('M38 card worker line altered', 'REJECT', lambda: c.call(bundle=c.bundle_text(M.NAMES[2], lambda t: t.replace('hostname ip-172-30-0-21,', 'hostname ip-10-0-0-1,'))))
    expect('M39 card lowercase placeholder evades TOKEN', 'EXTERNAL', lambda: c.call(bundle=c.bundle_text(M.NAMES[2], lambda t: t + 'JC2_x_PLACEHOLDER\n')))
    expect('M40 installer registration placeholder once', 'REJECT', lambda: c.call(bundle=c.bundle_text(M.NAMES[3], lambda t: t.replace("test \"$(sha256sum \"$jc2_final\" | cut -d ' ' -f 1)\" = 'JC2_FINAL_REGISTRATION_SHA_PLACEHOLDER'\n", ''))))
    expect('M41 installer freeze placeholder removed', 'REJECT', lambda: c.call(bundle=c.bundle_text(M.NAMES[3], lambda t: t.replace("test 'JC2_FINAL_INSTALL_RELEASE_PLACEHOLDER' = ROOT_FREEZE_EXACT_PREFLIGHT9_REGISTRATION_ONLY\n", ''))))
    expect('M42 installer jc2_base other batch', 'REJECT', lambda: c.call(bundle=c.bundle_text(M.NAMES[3], lambda t: t.replace('jc2_base=/opt/jc2-closedchild-preflight9-20260911b\n', 'jc2_base=/opt/jc2-closedchild-preflight9-20260912c\n'))))
    expect('M43 installer deadline literal 2099 (not checked)', 'EXTERNAL', lambda: c.call(bundle=c.bundle_text(M.NAMES[3], lambda t: t.replace('2026-09-11T12:27:45', '2099-01-01T00:00:00'))))
    expect('M44 installer jc2_unit other unit (not checked)', 'EXTERNAL', lambda: c.call(bundle=c.bundle_text(M.NAMES[3], lambda t: t.replace('jc2_unit=jc2-closedchild-preflight9-20260911b.service', 'jc2_unit=other.service'))))
    expect('M45 installer arbitrary appended command (not checked)', 'EXTERNAL', lambda: c.call(bundle=c.bundle_text(M.NAMES[3], lambda t: t + 'echo not-validated-by-helper\n')))
    expect('M46 card EBS volume id altered (not checked)', 'EXTERNAL', lambda: c.call(bundle=c.bundle_text(M.NAMES[2], lambda t: t.replace('vol-097211997797395f2', 'vol-000000000000000000'))))
    expect('M47 bundle CR byte', 'REJECT', lambda: c.call(bundle=c.bundle_text(M.NAMES[2], lambda t: t + '\r\n')))
    expect('M48 prepared pin uppercase hex', 'REJECT', lambda: M.bind(c.bundle, {n: sha(c.bundle[n]).upper() for n in M.NAMES}, wire(c.obs), b'{}\n'))
    expect('M49 deep nesting 3000', 'REJECT', lambda: M.load(b'[' * 3000 + b']' * 3000))
    expect('M50 integer 21 digits', 'REJECT', lambda: M.load(b'{"x":123456789012345678901}'))
    expect('M51 leading zero rejected by parser', 'REJECT', lambda: M.load(b'{"x":01}'))
    expect('M52 depth 17 dict', 'REJECT', lambda: M.load(b'{"a":' * 17 + b'1' + b'}' * 17))
    return all(r[3] for r in ROWS)


def main():
    inputs = Path(sys.argv[1])
    raw = {n: (inputs / n).read_bytes() for n in PINS}
    bad = [n for n in PINS if sha(raw[n]) != PINS[n]]
    print('PREPIN', 'OK 13/13' if not bad else 'MISMATCH ' + str(bad))
    if bad:
        return 2
    spec = importlib.util.spec_from_file_location('producer_tests', inputs / 'test_latebind.py')
    T = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(T)
    T.SOURCE = inputs  # override BEFORE collection; the inferred default path is never read
    print('SOURCE override ->', T.SOURCE, '| latebind loaded from', T.M.__spec__.origin)
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(T.Controls)
    res = unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)
    print('REPLAY', res.testsRun, 'run,', len(res.failures), 'failures,', len(res.errors), 'errors')
    ok = controls(T.M, raw)
    print('CONTROLS', sum(r[3] for r in ROWS), '/', len(ROWS), 'as expected; EXTERNAL rows (accepted, caller duty):', [r[0][:3] for r in ROWS if r[1] == 'EXTERNAL'])
    post = [n for n in PINS if sha((inputs / n).read_bytes()) != PINS[n]]
    print('POSTPIN', 'OK 13/13' if not post else 'MISMATCH ' + str(post))
    return 0 if (ok and res.wasSuccessful() and res.testsRun == 13 and not post) else 1


if __name__ == '__main__':
    sys.exit(main())
