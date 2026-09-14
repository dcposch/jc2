"""FIRST harness: in-memory replay + attack controls for stage_patch/historical_exercise.
Usage: python3 -I -S -B review_controls.py <inputs_dir>
Reads only the frozen inputs; writes nothing; every candidate stays bytes in memory."""
import contextlib
import hashlib
import importlib.util
import io
import json
import random
import re
import sys
import unittest
from collections import OrderedDict
from pathlib import Path

CHARGED = {
 'TASK.md': '6ac8e9ea645a2cb42c91ba0fe389d60d3db6c277b201c3557c2b231be8656067',
 'stage_patch.py': 'f7c61db67a9982a99f1febaed6dae0b6e3595199ffccad70647b66556b907066',
 'historical_exercise.py': 'fbec59b7317689fd71124bc5702ebdd0cd5ddb4ec8854592bb8a0f0447d66ff8',
 'test_stage_patch.py': 'e8e59687fb87adf42f8656c265e8a525741c21239d4479ce0b3da8f855a8e54a',
 'CONTRACT.md': 'e21c3efe2a061dfbd25328c9d0f519b6fe693938317e127ecabb351514dc9da5',
 'RECIPE.js': '88e7bc408852d226b119cc6dd26f9e91d0be16897e414b669e9c690142bab579',
 'EXERCISE.json': 'e37735ceeee1d60ee97ce492e196c312a8b9ee5d887f8abc9809af71924ce5b5',
 'tests.stdout': '69449fd5c02eb9f604d9b9f71532de9ecaf0e513e1e584c058da7db7bd9124d2',
 'latebind.py': 'ff2beb48b68b55dc5035709a9114bc7202dd38cef488d20b8163d0c55e2366fe',
 'test_latebind.py': '85d5390babe473deed13e9a88c40ea82193c6306284a4224cdb021f65ca5ec06',
 'caprun-latebinder-first-fable5-20260911.md': '3201abe5cae352f9e12ec6c842c6efe7ac463394b515cf2279d8266717296661',
 'ROOT-REGISTRATION.preholder.json': '31c942b17ed290f13b0bcd87457ec3a2b68f760fc4cf99443fee0e8386eceb74',
 'ROOT-REGISTRATION.json': '4d0d8475ed7d4aac1e42b70b1c7b4ee0198270ead0c3bb46adb78d7a91153ba3',
 'AUTHORITIES.preholder.json': '58d35c476c3dc7c4f6fe36adf73b79e5e0d8843e6ddd388c27a745b747a40d2e',
 'ROOT-EXECUTION-CARD.preholder.md': '1d9f837a23bb94b9609c7ac572909afbb0a4a96e44cb3c84b4875a9b310d02be',
 'ROOT-EXECUTION-CARD.md': 'a92cf2680c8d6aff6044f5376fb1dcfeed87a29c527d55c953d940e39a99f281',
 'final-install.preholder.sh': '6d414284920782a75a951fa3e59a8c23a391470a5efea28003b968bb1052fc62',
 'final-install.sh': 'abff072f218cbecaa6f47278891a62b36463a70e34ae4be546e44a5f3c3cd208',
 'FINAL-INSTALL-INPUTS.sha256': 'd90196456531bdf917098c84a84a88861384c220dcff6882a5305bacd48e8943',
 'PINS.json': '0363a58346b318be4767cf7938d77ff199a135d86f9d916e459f8db0b8b6a95a',
 'caprun-candidate-stage-root-20260911.md': '498787894944fe77717687e1483979851993f93fb30a1e652e7fca3f5f9e143f',
 'caprun-candidate-stage-root-20260911.md.artifact.json': '4f8a2a2990ff7dafa018132a3be01493887896c5cbebc97c87b0c9b10f220d60'}

INPUTS = Path(sys.argv[1]).resolve()
RESULTS = []


def rec(tag, ok, note=''):
    RESULTS.append((tag, ok))
    print(('PASS ' if ok else 'FAIL ') + tag + ((' ' + note) if note else ''))


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def pins(label):
    bad = [n for n, d in CHARGED.items() if sha((INPUTS / n).read_bytes()) != d]
    rec(label, not bad and len(list(INPUTS.iterdir())) == 22, 'bad=' + repr(bad))


def raises(fn, *a, exc=(ValueError,)):
    try:
        fn(*a)
    except exc:
        return True
    except Exception:
        return False
    return False


pins('PREPIN 22/22')
# Static source checks before any import (sources already read WHOLE by the reviewer).
sp = (INPUTS / 'stage_patch.py').read_text('utf-8')
he = (INPUTS / 'historical_exercise.py').read_text('utf-8')
imp = re.findall(r'^(?:import|from) (\S+)', sp, re.M)
rec('C01 stage_patch imports exactly hashlib/json/re', imp == ['hashlib', 'json', 're'], repr(imp))
rec('C02 stage_patch has no I/O/exec tokens', not re.search(r'open\(|subprocess|\bos\b|\bsys\b|exec\(|eval\(|socket|write', sp))
imp2 = re.findall(r'^(?:import|from) (\S+)', he, re.M)
rec('C03 historical_exercise imports stdlib only', imp2 == ['hashlib', 'importlib.util', 'json', 'pathlib', 'sys'], repr(imp2))
rec('C04 historical_exercise reads only 2 pinned files, prints, never applies', he.count('read_bytes') == 1 and 'apply' not in he.replace('apply_patch', '') and 'print(json.dumps' in he and not re.search(r'subprocess|open\(|write|os\.', he))

# Location-only overrides: E.OLD and loaded fixture SOURCE -> frozen inputs; no original path is touched.
tests = module('review_test_stage_patch', INPUTS / 'test_stage_patch.py')
tests.E.OLD = INPUTS
_orig = tests.E.module


def wrapped(name, path):
    mod = _orig(name, path)
    if name == 'stage_historical_fixture':
        mod.SOURCE = INPUTS
    return mod


tests.E.module = wrapped
M, E, PREFIX = tests.M, tests.E, tests.PREFIX

# Replay the nine producer methods in-process.
suite = unittest.TestLoader().loadTestsFromModule(tests)
stream = io.StringIO()
res = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
names = sorted(l.split(' ')[0] for l in stream.getvalue().splitlines() if l.startswith('test_'))
rec('R01 producer suite 9/9 ok', res.testsRun == 9 and not res.failures and not res.errors and len(set(names)) == 9, 'run=%d fail=%d err=%d' % (res.testsRun, len(res.failures), len(res.errors)))
print('  methods: ' + ' '.join(names))

# Reconstruct the 14 candidates and all hashes against EXERCISE.json.
cands = E.historical_candidates()
ex = json.loads((INPUTS / 'EXERCISE.json').read_text('utf-8'))
exdir = ex['directory']
mine = {exdir + '/' + n: sha(r) for n, r in cands.items()}
rec('H01 14 reconstructed hashes == EXERCISE.expected_sha256', mine == ex['expected_sha256'] and len(mine) == 14)
rec('H02 candidate_bytes == 78889', sum(map(len, cands.values())) == ex['candidate_bytes'] == 78889)
rec('H03 SUMMARY hash 2d78477f...', sha(cands['SUMMARY.json']) == '2d78477f0df15efb820933c14f12e143d1d34ade77ce932b44b96cbeeb18ca46')
rec('H04 4 main docs == charged input hashes', all(sha(cands[n]) == CHARGED[n] for n in ('ROOT-REGISTRATION.json', 'ROOT-EXECUTION-CARD.md', 'FINAL-INSTALL-INPUTS.sha256', 'final-install.sh')))
rec('H05 summary context HISTORICAL_TEST, no release', json.loads(cands['SUMMARY.json'])['context'] == 'HISTORICAL_TEST' and json.loads(cands['SUMMARY.json'])['installation_or_release_authorized'] is False)
# Replay historical_exercise.main() in memory with the exercise directory string (never accessed).
sys.argv = ['historical_exercise.py', exdir]
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    E.main()
packet = json.loads(buf.getvalue())
rec('H06 main() JSON packet == EXERCISE map/status/context/bytes', packet['expected_sha256'] == ex['expected_sha256'] and packet['status'] == ex['status'] and packet['context'] == ex['context'] and packet['candidate_bytes'] == ex['candidate_bytes'] and set(packet) == {'patch', 'expected_sha256', 'status', 'context', 'candidate_bytes'})
rec('H07 main() rejects argv count', raises(lambda: E.main()) if not sys.argv.append('x') else False)
sys.argv = ['historical_exercise.py', exdir]


def parse_nl(patch):
    """Independent '\\n'-only add-file parser; returns path -> bytes."""
    lines = patch.split('\n')
    assert lines[0] == '*** Begin Patch' and lines[-2] == '*** End Patch' and lines[-1] == ''
    files, cur = {}, None
    for line in lines[1:-2]:
        if line.startswith('*** Add File: '):
            cur = line[14:]
            assert cur not in files
            files[cur] = []
        else:
            assert cur is not None and line.startswith('+'), line
            files[cur].append(line[1:])
    return {p: ('\n'.join(ls) + '\n').encode('utf-8') for p, ls in files.items()}


base = M.make_patch(cands, PREFIX)
rt = parse_nl(base['patch'])
rec('A01 base round trip: 14 paths, bytes exact, keys == expected map', set(rt) == set(base['expected_sha256']) and all(rt[PREFIX + '/' + n] == r for n, r in cands.items()) and all(sha(rt[p]) == d for p, d in base['expected_sha256'].items()))
rec('A02 deterministic', M.make_patch(cands, PREFIX) == base)
rec('A03 ROOT_ATTESTED_CANDIDATE context accepted (contract positive)', (lambda s: M.make_patch(tests.update_commitment(dict(cands), 'ROOT-EXECUTION-CARD.md', cands['ROOT-EXECUTION-CARD.md']) | {'SUMMARY.json': (json.dumps(s) + '\n').encode()}, PREFIX)['context'])(dict(json.loads(cands['SUMMARY.json']), context='ROOT_ATTESTED_CANDIDATE')) == 'ROOT_ATTESTED_CANDIDATE')


def with_summary(**kw):
    s = json.loads(cands['SUMMARY.json']); s.update(kw)
    return dict(cands, **{'SUMMARY.json': (json.dumps(s) + '\n').encode()})


rec('A04 context HISTORICAL rejected', raises(M.make_patch, with_summary(context='HISTORICAL'), PREFIX))
rec('A05 schema drift rejected', raises(M.make_patch, with_summary(schema='caprun-latebinding-summary/v2'), PREFIX))
s = json.loads(cands['SUMMARY.json']); s['outputs']['SUMMARY.json'] = {'sha256': '0' * 64, 'bytes': 1}
rec('A06 outputs containing SUMMARY.json rejected', raises(M.make_patch, dict(cands, **{'SUMMARY.json': (json.dumps(s) + '\n').encode()}), PREFIX))
s = json.loads(cands['SUMMARY.json']); s['outputs']['final-install.sh']['bytes'] = True
rec('A07 bool bytes commitment rejected', raises(M.make_patch, dict(cands, **{'SUMMARY.json': (json.dumps(s) + '\n').encode()}), PREFIX))
s = json.loads(cands['SUMMARY.json']); s['outputs']['final-install.sh']['sha256'] = s['outputs']['final-install.sh']['sha256'].upper()
rec('A08 uppercase digest commitment rejected', raises(M.make_patch, dict(cands, **{'SUMMARY.json': (json.dumps(s) + '\n').encode()}), PREFIX))
s = json.loads(cands['SUMMARY.json']); s['outputs']['final-install.sh']['extra'] = 1
rec('A09 extra record key rejected', raises(M.make_patch, dict(cands, **{'SUMMARY.json': (json.dumps(s) + '\n').encode()}), PREFIX))
rec('A10 dict subclass rejected', raises(M.make_patch, OrderedDict(cands), PREFIX))
rec('A11 bytearray value rejected', raises(M.make_patch, dict(cands, **{'final-install.sh': bytearray(cands['final-install.sh'])}), PREFIX))
rec('A12 str value rejected', raises(M.make_patch, dict(cands, **{'final-install.sh': cands['final-install.sh'].decode()}), PREFIX))
rec('A13 invalid SUMMARY JSON raises ValueError family', raises(M.make_patch, dict(cands, **{'SUMMARY.json': b'{\n'}), PREFIX))
one = tests.update_commitment(cands, 'ROOT-EXECUTION-CARD.md', b'\n')
rec('A14 single-LF file round-trips', parse_nl(M.make_patch(one, PREFIX)['patch'])[PREFIX + '/ROOT-EXECUTION-CARD.md'] == b'\n')
big = tests.update_commitment(cands, 'ROOT-EXECUTION-CARD.md', b'x' * 131071 + b'\n')
rec('A15 131072-byte file accepted, 131073 rejected', M.make_patch(big, PREFIX)['candidate_bytes'] > 0 and raises(M.make_patch, tests.update_commitment(cands, 'ROOT-EXECUTION-CARD.md', b'x' * 131072 + b'\n'), PREFIX))
agg = cands
for n in ('ROOT-EXECUTION-CARD.md', 'final-install.sh', 'ROOT-REGISTRATION.json', 'FINAL-INSTALL-INPUTS.sha256'):
    agg = tests.update_commitment(agg, n, bytes([65 + len(n) % 20]) * 131071 + b'\n')
rec('A16 aggregate 524288 bound is non-vacuous (4x131072 + rest rejected)', raises(M.make_patch, agg, PREFIX))
good_pref = ['/home/ubuntu/jc2/box/caprun-stage-exercise-20260911.abcdef', '/home/ubuntu/jc2/box/caprun-stage-exercise-20260911.' + 'A' * 24, '/home/ubuntu/jc2/box/caprun-stage-exercise-99999999.XXo03Rv3']
bad_pref = ['/home/ubuntu/jc2/box/caprun-stage-exercise-20260911.abcde', '/home/ubuntu/jc2/box/caprun-stage-exercise-20260911.' + 'A' * 25, PREFIX + '\n', PREFIX + ' ', '/home/ubuntu/jc2/box/caprun-stage-exercise-20260911.a_b', '/home/ubuntu/jc2/box/caprun-stage-exercise-2026091.abcdef', 'home/ubuntu/jc2/box/caprun-stage-exercise-20260911.abcdef', '/home/ubuntu/jc2/box/caprun-stage-exercise-20260911.abc/../def', PREFIX.encode(), None]
rec('A17 prefix regex: 3 accepted incl. non-date 99999999, 10 rejected', all(M.make_patch(cands, p)['expected_sha256'] for p in good_pref) and all(raises(M.make_patch, cands, p) for p in bad_pref))
# Patch-looking content beyond the producer: every directive keyword as a full content line, all 14 files.
directives = b'*** Begin Patch\n*** End Patch\n*** Add File: /outside/a\n*** Delete File: /outside/b\n*** Update File: /outside/c\n*** Move to: /outside/d\n@@ -1,1 +1,1 @@\n*** End of File\n-deleted\n+added\n \n'
evil = cands
for n in M.NAMES[:-1]:
    evil = tests.update_commitment(evil, n, cands[n] + directives)
ev = M.make_patch(evil, PREFIX)
evrt = parse_nl(ev['patch'])
rec('A18 directive lines in all 13 files stay data; exactly 14 paths; bytes exact', set(evrt) == set(ev['expected_sha256']) and len(evrt) == 14 and all(evrt[PREFIX + '/' + n] == evil[n] for n in M.NAMES) and ev['patch'].count('\n*** Add File: ') == 14 and ev['patch'].count('\n*** End Patch\n') == 1 and not re.search(r'\n\*\*\* (Delete|Update|Move)', ev['patch']))
# Universal-newline delimitation: bytes that Python splitlines() treats as line ends but stage_patch does not.
seps = ['\x0b', '\x0c', '\x1c', '\x1d', '\x1e', '\x85', ' ', ' ']
accepted, extra_paths = [], []
for sep in seps:
    c = tests.update_commitment(cands, 'ROOT-EXECUTION-CARD.md', cands['ROOT-EXECUTION-CARD.md'] + ('x' + sep + '*** Add File: /outside/evil\n').encode('utf-8'))
    try:
        r = M.make_patch(c, PREFIX)
    except ValueError:
        continue
    accepted.append(sep)
    nl = [l for l in r['patch'].split('\n') if l.startswith('*** Add File: ')]
    un = [l for l in r['patch'].splitlines() if l.startswith('*** Add File: ')]
    extra_paths.append((len(nl), len(un)))
rec('D01 DELIMIT: 8 universal-newline separators accepted; LF-only parser sees 14 paths, splitlines-parser sees 15', len(accepted) == 8 and all(t == (14, 15) for t in extra_paths), repr([hex(ord(s)) for s in accepted]))
# Round-trip fuzz over UTF-8 content with leading +/-/@@/*** lines.
rng = random.Random(20260911)
alpha = ['+', '-', '*** ', '@@ ', ' ', 'a', 'z', '0', '—', 'é', '中', '\n', '\n\n', '\t', '\\', '"', '{', '}']
okc = 0
for i in range(150):
    body = ''.join(rng.choice(alpha) for _ in range(rng.randint(1, 400))).rstrip('\n') + '\n'
    raw = body.encode('utf-8')
    c = tests.update_commitment(cands, 'authority/valid.json', raw) if i % 2 else tests.update_commitment(cands, 'ROOT-EXECUTION-CARD.md', raw)
    r = M.make_patch(c, PREFIX)
    p = parse_nl(r['patch'])
    okc += all(p[PREFIX + '/' + n] == c[n] for n in M.NAMES) and len(p) == 14
rec('A19 150 random UTF-8 candidates round-trip exactly', okc == 150, 'ok=%d' % okc)
rec('A20 inputs unchanged after all controls', E.historical_candidates() == cands)
pins('POSTPIN 22/22')
fails = [t for t, ok in RESULTS if not ok]
print('CONTROLS %d/%d passed; FAIL=%s' % (len(RESULTS) - len(fails), len(RESULTS), fails))
