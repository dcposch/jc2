"""FIRST review harness (Fable 5.1): supplied-input candidate caller.

Relocated in-process replay of the supplied tests plus independent controls.
Every candidate stays as bytes in memory; nothing is applied, written or run.
Invocation: python3 -I -S -B review_controls.py /tmp/jc2-lane.kgQvAj/inputs
The supplied test_real_standalone_cli is NOT invoked here (it would infer
original sibling helper paths); ROOT replayed that standalone run itself.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import re
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

INPUTS = Path(sys.argv[1]).resolve()
PINS = {
    'TASK.md': '34bfd0953a0f08cd2e2ea16284da01fe23d26e424ce7d44afde3d39304a6e937',
    'latebind.py': 'ff2beb48b68b55dc5035709a9114bc7202dd38cef488d20b8163d0c55e2366fe',
    'caprun-latebinder-first-fable5-20260911.md': '3201abe5cae352f9e12ec6c842c6efe7ac463394b515cf2279d8266717296661',
    'stage_patch.py': 'f7c61db67a9982a99f1febaed6dae0b6e3595199ffccad70647b66556b907066',
    'EXERCISE.json': 'e37735ceeee1d60ee97ce492e196c312a8b9ee5d887f8abc9809af71924ce5b5',
    'caprun-candidate-stage-first-fable5-20260911.md': 'd96d979c950bf51faea0ad430af4f2eed1366d8f7b3e952e27d048ca2dff2273',
    'ROOT-REGISTRATION.preholder.json': '31c942b17ed290f13b0bcd87457ec3a2b68f760fc4cf99443fee0e8386eceb74',
    'ROOT-REGISTRATION.json': '4d0d8475ed7d4aac1e42b70b1c7b4ee0198270ead0c3bb46adb78d7a91153ba3',
    'AUTHORITIES.preholder.json': '58d35c476c3dc7c4f6fe36adf73b79e5e0d8843e6ddd388c27a745b747a40d2e',
    'ROOT-EXECUTION-CARD.preholder.md': '1d9f837a23bb94b9609c7ac572909afbb0a4a96e44cb3c84b4875a9b310d02be',
    'ROOT-EXECUTION-CARD.md': 'a92cf2680c8d6aff6044f5376fb1dcfeed87a29c527d55c953d940e39a99f281',
    'final-install.preholder.sh': '6d414284920782a75a951fa3e59a8c23a391470a5efea28003b968bb1052fc62',
    'final-install.sh': 'abff072f218cbecaa6f47278891a62b36463a70e34ae4be546e44a5f3c3cd208',
    'FINAL-INSTALL-INPUTS.sha256': 'd90196456531bdf917098c84a84a88861384c220dcff6882a5305bacd48e8943',
    'caller.py': '73596b115c73db9aac6751c08d26b2a90cbddccfaa1d6a8615ada65a8076df90',
    'test_caller.py': 'e5c6a438016c5b0129f13b2f0cf2ae5a1cdf450750429c8c5a5450c590b4cc35',
    'CONTRACT.md': 'f57c247414746a6f4576b45a84f8f17c52052be4414f69e951e3be093b82e9cd',
    'PINS.json': 'e465ca6c062a8de1822eedd3f29ed5cb7bc2490b8d09fccaa89e79890048970d',
    'fixture-pins.json': 'd4d68584e3b60bb166155a20fcedc5bb67a1526235726ca0b2c53fda8d96853a',
    'fixture-observation.json': '6b4ab0834f67b69fa4f6af8d7246ec4d1de5f26a3b2731a2f4cf637280430126',
    'fixture-decision.json': '7f9ff04852b1d2c6a59815aff6ca28968204abb42ece7e5c5d444d489186e53e',
    'caprun-candidate-caller-astra-20260911.md': '2a673cbd51a163c476f5b0a14faa4683a51851477a9780a0f76c5fbd05ca26da',
    'caprun-candidate-caller-astra-20260911.md.artifact.json': '511b7c06ab00dc1609039589415b231d0934f912332c3116badf443d6337bfc2',
}
H8 = ('ROOT-REGISTRATION.preholder.json', 'ROOT-REGISTRATION.json', 'AUTHORITIES.preholder.json',
      'ROOT-EXECUTION-CARD.preholder.md', 'ROOT-EXECUTION-CARD.md', 'final-install.preholder.sh',
      'final-install.sh', 'FINAL-INSTALL-INPUTS.sha256')
STATUS = 'CANDIDATE_NOT_INSTALLED_NOT_RELEASED'
REFUSAL = 'REFUSED: candidate input or dependency\n'
RESULTS = []


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def expect(tag, ok, note=''):
    RESULTS.append((tag, bool(ok)))
    print(tag, 'ok' if ok else 'FAIL', note)


def pinned(stage):
    for name, digest in PINS.items():
        expect(stage + ' ' + name, sha((INPUTS / name).read_bytes()) == digest)


pinned('PREPIN')

# ---- static reading of the frozen sources ------------------------------------
src = (INPUTS / 'caller.py').read_bytes().decode('utf-8')
tsrc = (INPUTS / 'test_caller.py').read_bytes().decode('utf-8')
imports = [l for l in src.split('\n') if l.startswith(('import ', 'from '))]
expect('S01 caller imports exactly hashlib/importlib.util/json/pathlib.Path/sys',
       imports == ['import hashlib', 'import importlib.util', 'import json', 'from pathlib import Path', 'import sys'])
BAD = ('subprocess', 'import os', 'os.', 'socket', 'shutil', 'eval(', 'exec(', 'write_bytes', 'write_text',
       'mkdir', 'unlink', 'rename', 'chmod', "'w'", "'a'", "'wb'", 'system(', 'popen', 'fork', 'ctypes',
       'signal', 'tempfile', 'glob', 'apply', 'install', 'urllib', 'http')
expect('S02 no execution/write/network tokens in caller', not any(t in src for t in BAD),
       str([t for t in BAD if t in src]))
expect('S03 single file open, read-binary, bounded', src.count('open(') == 1 and "open(path, 'rb')" in src
       and 'stream.read(MAX_READ + 1)' in src and "raise ValueError('input size')" in src)
expect('S04 only stdout packet and stderr refusal writes', src.count('.write(') == 2
       and 'sys.stdout.write(wire)' in src and "sys.stderr.write('REFUSED: candidate input or dependency\\n')" in src)
expect('S05 main guard is the only CLI tail', src.endswith("\n\nif __name__ == '__main__':\n    raise SystemExit(main())\n")
       and src.count('__main__') == 1)
hexes = re.findall(r'[0-9a-f]{64}', src)
expect('S06 the only 64-hex literals are the two charged helper pins',
       sorted(hexes) == sorted([PINS['latebind.py'], PINS['stage_patch.py']]))
expect('S07 both helper hashes precede either import (code order)',
       src.index('hexdigest() != DEPENDENCY_SHA256[name]') < src.index('spec_from_file_location')
       and src.count('for name, path in DEPENDENCY_PATHS.items():') == 2)
expect('S08 prefix is only unpacked and handed to make_patch', src.count('prefix') == 2
       and 'stage.make_patch(candidates, prefix)' in src)
expect('S09 no historical identity literal in caller', re.search(r'i-0[0-9a-f]{8,}|ip-172|20260911b|XXo03Rv3|32389', src) is None)
expect('S10 packet is serialized ASCII with allow_nan=False, one LF, bounded before stdout',
       "json.dumps(answer, ensure_ascii=True, allow_nan=False, separators=(',', ':')) + '\\n'" in src
       and src.index('len(wire) > MAX_PACKET') < src.index('sys.stdout.write(wire)'))
expect('S11 supplied test subprocess target is only the adjacent caller under -I -S -B',
       tsrc.count('subprocess.run(') == 1 and "subprocess.run([sys.executable, '-I', '-S', '-B', str(CALLER_PATH)" in tsrc)
expect('S12 supplied tests never write files', not any(t in tsrc for t in ('write_bytes', 'write_text', "'w'", 'mkdir', 'open(')))

# ---- load supplied tests from the flat snapshot, location-only rebinding -----
spec = importlib.util.spec_from_file_location('supplied_tests', INPUTS / 'test_caller.py')
tests = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tests)
tests.HISTORY = INPUTS
tests.FIXTURES = INPUTS
tests.EXERCISE_PATH = INPUTS / 'EXERCISE.json'
C = tests.C
C.DEPENDENCY_PATHS = {'latebind': INPUTS / 'latebind.py', 'stage_patch': INPUTS / 'stage_patch.py'}
expect('L01 caller module loaded from the snapshot', Path(C.__file__).resolve() == INPUTS / 'caller.py')
expect('L02 DEPENDENCY_SHA256 literal unchanged and equal to charged pins',
       C.DEPENDENCY_SHA256 == {'latebind': PINS['latebind.py'], 'stage_patch': PINS['stage_patch.py']})
expect('L03 supplied HISTORY_PINS equal the eight charged pins; exercise pin literal present',
       tests.HISTORY_PINS == {n: PINS[n] for n in H8} and PINS['EXERCISE.json'] in tsrc)
expect('L04 FORBIDDEN is exactly VT FF FS GS RS NEL LS PS',
       C.FORBIDDEN == '\v\f\x1c\x1d\x1e\x85  ' and len(C.FORBIDDEN) == 8)
expect('L05 bounds literal', C.MAX_READ == 131072 and C.MAX_PACKET == 8388608)

FIVE = ['test_main_ascii_stream', 'test_missing_argument_and_file', 'test_pins_context_decision_and_json',
        'test_wrong_dependency_hash_precedes_import', 'test_eight_separators_after_valid_updated_commitments']
res = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(unittest.TestSuite(tests.Controls(n) for n in FIVE))
expect('R01 five supplied methods pass in RELOCATED IN-PROCESS replay (not a standalone run)',
       res.wasSuccessful() and res.testsRun == 5, 'run=%d fail=%d err=%d' % (res.testsRun, len(res.failures), len(res.errors)))
for f in res.failures + res.errors:
    print('   ', f[0], f[1].strip().splitlines()[-1])
print('R02 test_real_standalone_cli deliberately not invoked (ROOT replayed the real standalone CLI)')

# ---- independent main(argv) controls through builtins.open substitution ------
FIX = {n: (INPUTS / n).read_bytes() for n in ('fixture-pins.json', 'fixture-observation.json', 'fixture-decision.json')}
HIST = {n: (INPUTS / n).read_bytes() for n in H8}
EXERCISE = json.loads((INPUTS / 'EXERCISE.json').read_bytes())
PREFIX = EXERCISE['directory']
P = lambda n: str(INPUTS / n)
ARGS = [str(INPUTS), P('fixture-pins.json'), P('fixture-observation.json'), P('fixture-decision.json'), PREFIX, 'HISTORICAL_TEST']
REAL_OPEN = open
OPENS = []


def wire(value):
    return (json.dumps(value, ensure_ascii=True, separators=(',', ':')) + '\n').encode('ascii')


def run_main(args, files=None):
    files = files or {}

    def fake_open(path, mode='r', *a, **k):
        OPENS.append((str(path), mode))
        v = files.get(str(path))
        if isinstance(v, BaseException):
            raise v
        if v is not None:
            return io.BytesIO(v)
        return REAL_OPEN(path, mode, *a, **k)
    buf, err = io.BytesIO(), io.StringIO()
    out = io.TextIOWrapper(buf, encoding='ascii', write_through=True)
    with patch('builtins.open', side_effect=fake_open), contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        status = C.main(args)
    out.flush()
    return status, buf.getvalue(), err.getvalue()


def refused(tag, args=None, files=None):
    s, o, e = run_main(ARGS if args is None else args, files)
    expect(tag, (s, o, e) == (2, b'', REFUSAL), 'status=%s stdout=%dB' % (s, len(o)))


def readback(out):
    obj = json.loads(out.decode('ascii'))
    lines = obj['patch'].split('\n')
    assert (lines[0], lines[-2], lines[-1]) == ('*** Begin Patch', '*** End Patch', '')
    files, cur = {}, None
    for line in lines[1:-2]:
        if line.startswith('*** Add File: '):
            cur = line[14:]
            assert cur not in files
            files[cur] = bytearray()
        else:
            assert line.startswith('+') and cur is not None
            files[cur] += (line[1:] + '\n').encode('utf-8')
    return obj, {k: bytes(v) for k, v in files.items()}


s, out, err = run_main(ARGS)
expect('P01 historical main(argv): exit 0, empty stderr', s == 0 and err == '')
expect('P02 one ASCII line with a single trailing LF', out.isascii() and out.endswith(b'\n') and out.count(b'\n') == 1)
obj, files = readback(out)
expect('P03 five packet keys, candidate-only status, HISTORICAL_TEST, 78889 bytes',
       set(obj) == {'patch', 'expected_sha256', 'status', 'context', 'candidate_bytes'} and obj['status'] == STATUS
       and obj['context'] == 'HISTORICAL_TEST' and obj['candidate_bytes'] == 78889)
expect('P04 fourteen expected hashes equal the frozen EXERCISE map',
       len(obj['expected_sha256']) == 14 and obj['expected_sha256'] == EXERCISE['expected_sha256'])
expect('P05 LF readback reproduces all fourteen hashes and 78889 bytes', len(files) == 14
       and {k: sha(v) for k, v in files.items()} == obj['expected_sha256'] and sum(map(len, files.values())) == 78889)
expect('P06 four historical finals byte-identical', all(files[PREFIX + '/' + n] == HIST[n] for n in
       ('ROOT-REGISTRATION.json', 'ROOT-EXECUTION-CARD.md', 'final-install.sh', 'FINAL-INSTALL-INPUTS.sha256')))
summary = json.loads(files[PREFIX + '/SUMMARY.json'])
expect('P07 SUMMARY context, no-release flag, thirteen commitments pair with reconstructed bytes',
       summary['context'] == 'HISTORICAL_TEST' and summary['installation_or_release_authorized'] is False
       and len(summary['outputs']) == 13 and all(summary['outputs'][n] == {'sha256': sha(files[PREFIX + '/' + n]),
       'bytes': len(files[PREFIX + '/' + n])} for n in summary['outputs']))
expect('P08 em dash escaped in packet, raw in reconstructed card', b'\\u2014' in out and b'\xe2\x80\x94' not in out
       and b'\xe2\x80\x94' in files[PREFIX + '/ROOT-EXECUTION-CARD.md'])
expect('P09 deterministic packet', run_main(ARGS)[1] == out, 'stdout sha256 ' + sha(out))
expect('P10 every open is read-binary under the snapshot; no original path touched',
       all(m == 'rb' and p.startswith(str(INPUTS) + '/') for p, m in OPENS) and len(OPENS) > 0, '%d opens' % len(OPENS))


class Broken(io.TextIOBase):
    def write(self, s):
        raise OSError('output device')


try:
    with contextlib.redirect_stdout(Broken()), contextlib.redirect_stderr(io.StringIO()):
        C.main(ARGS)
    device = 'returned'
except OSError:
    device = 'raised'
expect('P11 output-device failure propagates: neither exit 0 nor REFUSED', device == 'raised')

obs2 = json.loads(FIX['fixture-observation.json']); obs2['context'] = 'ROOT_ATTESTED_CANDIDATE'; obs2_raw = wire(obs2)
dec2 = json.loads(FIX['fixture-decision.json']); dec2['context'] = 'ROOT_ATTESTED_CANDIDATE'; dec2['observation_sha256'] = sha(obs2_raw)
s, o, e = run_main(ARGS[:5] + ['ROOT_ATTESTED_CANDIDATE'], {P('fixture-observation.json'): obs2_raw, P('fixture-decision.json'): wire(dec2)})
obj2, files2 = readback(o)
expect('P12 ROOT_ATTESTED_CANDIDATE is transport acceptance only: 13 documents identical, SUMMARY differs, still candidate-only',
       s == 0 and obj2['context'] == 'ROOT_ATTESTED_CANDIDATE' and obj2['status'] == STATUS
       and all(files2[k] == files[k] for k in files if not k.endswith('/SUMMARY.json'))
       and files2[PREFIX + '/SUMMARY.json'] != files[PREFIX + '/SUMMARY.json']
       and json.loads(files2[PREFIX + '/SUMMARY.json'])['installation_or_release_authorized'] is False)
pad = FIX['fixture-pins.json'] + b' ' * (131072 - len(FIX['fixture-pins.json']))
s, o, e = run_main(ARGS, {P('fixture-pins.json'): pad})
expect('P13 pins at exactly 131072 bytes accepted', s == 0 and o == out)

# ---- negatives: every one must refuse with empty stdout and the exact stderr --
refused('N01 five arguments', ARGS[:5])
refused('N02 seven arguments', ARGS + ['x'])
refused('N03 lowercase context', ARGS[:5] + ['historical_test'])
refused('N04 empty context', ARGS[:5] + [''])
refused('N05 missing pins file (helpers present)', files={P('fixture-pins.json'): FileNotFoundError()})
refused('N06 missing bundle file (helpers present)', files={P('AUTHORITIES.preholder.json'): FileNotFoundError()})
refused('N07 pins at 131073 bytes (valid JSON) end-to-end size refusal', files={P('fixture-pins.json'): pad + b' '})
big = HIST['ROOT-EXECUTION-CARD.preholder.md']
refused('N08 bundle card at 131073 bytes', files={P('ROOT-EXECUTION-CARD.preholder.md'): big + b' ' * (131073 - len(big))})
refused('N09 bundle card hash mismatch (one LF appended)', files={P('ROOT-EXECUTION-CARD.preholder.md'): big + b'\n'})
d = json.loads(FIX['fixture-decision.json']); d['context'] = 'ROOT_ATTESTED_CANDIDATE'
refused('N10 decision context mismatch', files={P('fixture-decision.json'): wire(d)})
o2 = json.loads(FIX['fixture-observation.json']); o2['context'] = 'ROOT_ATTESTED_CANDIDATE'
refused('N11 observation context mismatch', files={P('fixture-observation.json'): wire(o2)})
d = json.loads(FIX['fixture-decision.json']); d['observation_sha256'] = '0' * 64
refused('N12 decision observation hash stale', files={P('fixture-decision.json'): wire(d)})
d = json.loads(FIX['fixture-decision.json']); d['enabled'] = False
refused('N13 decision enabled false', files={P('fixture-decision.json'): wire(d)})
d = json.loads(FIX['fixture-decision.json']); d['freeze_token'] = d['freeze_token'] + 'X'
refused('N14 decision freeze token altered', files={P('fixture-decision.json'): wire(d)})
d = json.loads(FIX['fixture-decision.json']); d['prepared_pins']['final-install.preholder.sh'] = '1' * 64
refused('N15 decision pins differ from supplied pins', files={P('fixture-decision.json'): wire(d)})
pins = json.loads(FIX['fixture-pins.json'])
q = dict(pins); q['final-install.preholder.sh'] = 'f' + q['final-install.preholder.sh'][1:]
refused('N16 pins one digest altered', files={P('fixture-pins.json'): wire(q)})
q = dict(pins); q['extra'] = '0' * 64
refused('N17 pins extra key', files={P('fixture-pins.json'): wire(q)})
q = dict(pins); q['final-install.preholder.sh'] = q['final-install.preholder.sh'].upper()
refused('N18 pins uppercase digest', files={P('fixture-pins.json'): wire(q)})
for tag, raw in (('N19 pins top-level list', b'[]\n'), ('N20 pins float', b'{"x":1.0}\n'), ('N21 pins duplicate key', b'{"x":1,"x":2}\n'),
                 ('N22 pins NaN', b'{"x":NaN}\n'), ('N23 pins trailing garbage', FIX['fixture-pins.json'] + b'}'),
                 ('N24 pins CR byte', FIX['fixture-pins.json'].replace(b'}', b'\r}')), ('N25 pins invalid UTF-8', b'{"\xff":1}\n'),
                 ('N26 pins empty', b''), ('N27 observation top-level string', b'"x"\n')):
    refused(tag, files={P('fixture-observation.json' if 'observation' in tag else 'fixture-pins.json'): raw})
o2 = json.loads(FIX['fixture-observation.json']); o2['hostname'] = o2['hostname'] + ' '
d = json.loads(FIX['fixture-decision.json']); d['observation_sha256'] = sha(wire(o2))
refused('N28 separator inside observation metadata cannot reach candidates (parent equality check)',
        files={P('fixture-observation.json'): wire(o2), P('fixture-decision.json'): wire(d)})
refused('N29 prefix relative', ARGS[:4] + ['box/caprun-stage-exercise-20260911.abcdef', 'HISTORICAL_TEST'])
refused('N30 prefix trailing newline', ARGS[:4] + [PREFIX + '\n', 'HISTORICAL_TEST'])
refused('N31 prefix outside namespace', ARGS[:4] + ['/tmp/caprun-stage-exercise-20260911.abcdef', 'HISTORICAL_TEST'])
for tag, files in (('N32 latebind bytes tampered', {P('latebind.py'): b'tampered\n'}),
                   ('N33 stage_patch bytes tampered', {P('stage_patch.py'): b'tampered\n'}),
                   ('N34 both helpers tampered', {P('latebind.py'): b'a\n', P('stage_patch.py'): b'b\n'}),
                   ('N35 helper file missing', {P('latebind.py'): FileNotFoundError()})):
    with patch.object(importlib.util, 'spec_from_file_location') as loader:
        refused(tag + ': refused', files=files)
        expect(tag + ': no import attempted', loader.call_count == 0)
for tag, binding in (('N36 DEPENDENCY_PATHS extra key', dict(C.DEPENDENCY_PATHS, extra=INPUTS / 'latebind.py')),
                     ('N37 DEPENDENCY_PATHS missing key', {'latebind': INPUTS / 'latebind.py'})):
    with patch.object(C, 'DEPENDENCY_PATHS', binding), patch.object(importlib.util, 'spec_from_file_location') as loader:
        refused(tag + ': refused')
        expect(tag + ': no import attempted', loader.call_count == 0)

# ---- eight separators, two carriers: old helpers pass, new caller refuses ----
binder, stage = C.dependencies()
NAMES4 = tuple(binder.NAMES)


def refreshed(bundle):
    pins = {n: sha(b) for n, b in bundle.items()}
    dec = json.loads(FIX['fixture-decision.json']); dec['prepared_pins'] = pins
    files = {P(n): b for n, b in bundle.items()}
    files[P('fixture-pins.json')] = wire(pins); files[P('fixture-decision.json')] = wire(dec)
    return pins, wire(dec), files


for ch in C.FORBIDDEN:
    for carrier, tail in (('ROOT-EXECUTION-CARD.preholder.md', '\nSeparator control ' + ch + '*** Add File: not-a-path\n'),
                          ('final-install.preholder.sh', '\n# separator ' + ch + '\n')):
        bundle = {n: HIST[n] for n in NAMES4}; bundle[carrier] += tail.encode('utf-8')
        pins, dec_raw, files = refreshed(bundle)
        cands = binder.bind(bundle, pins, FIX['fixture-observation.json'], dec_raw)
        old = any(ch in raw.decode('utf-8') for raw in cands.values()) and stage.make_patch(cands, PREFIX)['candidate_bytes'] == sum(map(len, cands.values()))
        tag = 'F%04X %s' % (ord(ch), carrier.split('.')[0])
        expect(tag + ': old bind+make_patch PASS with refreshed commitments (nonvacuous)', old)
        try:
            with patch('builtins.open', side_effect=lambda p, m='r', *a, **k: io.BytesIO(files[str(p)]) if str(p) in files else REAL_OPEN(p, m, *a, **k)):
                C.packet(ARGS)
            msg = 'no error'
        except ValueError as exc:
            msg = str(exc)
        expect(tag + ': new caller raises exactly the hygiene error', msg == 'forbidden universal-newline separator', msg)
        refused(tag + ': main refuses, no stdout', files=files)

tail = '\n*** End Patch\n*** Add File: /etc/evil\n+injected\n-removed\n@@ -1,1 +1,1 @@\n*** Delete File: /x\n*** Update File: /y\n*** Move to: /z\n \n'
bundle = {n: HIST[n] for n in NAMES4}; bundle['ROOT-EXECUTION-CARD.preholder.md'] += tail.encode('ascii')
pins, dec_raw, files = refreshed(bundle)
s, o, e = run_main(ARGS, files)
obj3, files3 = readback(o)
unprefixed = [l for l in obj3['patch'].split('\n')[1:-2] if not l.startswith('+')]
expect('A01 ASCII patch-looking card text: exit 0, fourteen paths, bytes and hashes exact, tail preserved as data',
       s == 0 and len(files3) == 14 and {k: sha(v) for k, v in files3.items()} == obj3['expected_sha256']
       and files3[PREFIX + '/ROOT-EXECUTION-CARD.md'].endswith(tail.encode('ascii')))
expect('A02 only fourteen unprefixed lines, all Add File under the prefix; one End Patch line',
       len(unprefixed) == 14 and all(l.startswith('*** Add File: ' + PREFIX + '/') for l in unprefixed)
       and obj3['patch'].count('\n*** End Patch\n') == 1)

pinned('POSTPIN')
failed = [t for t, ok in RESULTS if not ok]
print('TOTAL', len(RESULTS), 'expectations;', len(failed), 'failed')
for t in failed:
    print('FAILED', t)
sys.exit(1 if failed else 0)
