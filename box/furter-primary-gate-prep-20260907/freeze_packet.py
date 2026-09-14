#!/usr/bin/env python3
"""One-shot metadata-only custody check and exclusive packet receipts."""
import hashlib
import json
import pathlib
import subprocess
from datetime import datetime, timezone

ROOT = pathlib.Path('/home/ubuntu/jc2')
HERE = ROOT / 'box/furter-primary-gate-prep-20260907'
SWEEP = ROOT / 'box/websweep-20260907T0735Z'

def pin(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def require(ok, message):
    if not ok:
        raise ValueError(message)

def emit(name, obj):
    data = (json.dumps(obj, indent=2, sort_keys=True) + '\n').encode()
    with (HERE / name).open('xb') as handle:
        handle.write(data)

require(pin(SWEEP / 'custody.json')['sha256'] ==
        'c0d46225197b1136474c5f989d46310acaf9e40c9c51a50c54c7f417f9e01454',
        'sweep custody drift')
old = json.loads((SWEEP / 'custody.json').read_bytes())
require(len(old['files']) == 194, 'sweep count drift')
for name, expected in old['files'].items():
    require(pin(SWEEP / name) == expected, 'sweep drift: ' + name)

transactions = {}
for name in ('websweep-20260907T0735Z-astra',
             'd125-parity-unit-normalization-astra-20260907'):
    result = subprocess.run([
        '/usr/bin/python3', '-B', str(ROOT / 'ops/artifact_finalize.py'),
        'verify', '--final', str(ROOT / ('xmodel/' + name + '.md'))],
        check=True, capture_output=True, timeout=10)
    require(result.stderr == b'', 'transaction stderr')
    transactions[name] = json.loads(result.stdout)
    require(transactions[name]['status'] == 'VERIFIED', 'transaction state')

sources = {
 'producer-rigidity.typ': SWEEP / 'sources/furter-proof.typ',
 'producer-proof.pdf': SWEEP / 'sources/furter-proof.pdf',
 'producer-refs.yml': SWEEP / 'sources/furter-refs.yml',
 'producer-readme.md': SWEEP / 'sources/furter-readme.md',
 'furter-original-author.pdf': SWEEP / 'sources/furter-primary-author.pdf',
 'furter-original-author.txt': SWEEP / 'sources/furter-primary-author.txt',
 'campaign-approaches-0731.md': SWEEP / 'charged/APPROACHES.md',
 'campaign-torsor.md': SWEEP / 'charged/d125-torsor-geometry-discriminator-astra-20260907.md',
 'campaign-moving-face-14c.md': ROOT / 'xmodel/d125-parity-unit-normalization-astra-20260907.md',
}
inputs = {}
for name, source in sources.items():
    item = pin(HERE / name)
    require(item == pin(source), 'copy drift: ' + name)
    inputs[name] = dict(item, original_path=str(source))
inputs['scope-and-provenance.md'] = pin(HERE / 'scope-and-provenance.md')
emit('input-pins.json', {'schema': 'jc2.furter-primary-input-pins/v1',
                       'files': inputs})
prompt = (HERE / 'review.prompt.md').read_text()
require('{{LANE_INPUTS}}' in prompt, 'missing literal staging template')
charged = [line.split('=', 1)[1] for line in prompt.splitlines()
           if line.startswith('charged_input=')]
require(len(charged) == 11, 'wrong charged count')
names = [pathlib.Path(path).name for path in charged]
require(len(set(names)) == len(names), 'basename collision')
require(set(names) == set(inputs) | {'input-pins.json'}, 'charged set drift')
for path in charged:
    require((ROOT / path).parent == HERE and (ROOT / path).is_file(),
            'invalid charged path')
receipt = {'utc': datetime.now(timezone.utc).isoformat(),
           'prior_sweep_pins_checked': 194, 'prior_sweep_pins_match': True,
           'prior_custody': pin(SWEEP / 'custody.json'),
           'transactions': transactions, 'unique_charged_basenames': names,
           'copied_sources_match': True, 'external_calls': 0,
           'review_launched': False, 'arithmetic_tests': 0}
emit('verification.json', receipt)
owned = sorted(list(inputs) + ['input-pins.json', 'review.prompt.md',
                              'freeze_packet.py', 'verification.json'])
emit('custody.json', {'schema': 'jc2.furter-primary-gate-prep/v1',
                     'files': {name: pin(HERE / name) for name in owned},
                     'status': 'PREP_ONLY_NO_LAUNCH',
                     'remaining_child_processes': 0})
print(json.dumps({'status': 'PASS', 'prior_pins': 194,
                  'charged_files': len(charged),
                  'prompt': pin(HERE / 'review.prompt.md'),
                  'input_pins': pin(HERE / 'input-pins.json'),
                  'custody': pin(HERE / 'custody.json')}, sort_keys=True))
