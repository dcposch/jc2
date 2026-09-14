"""Metadata/text-contract checks only. Never scans the banked report corpus."""
import datetime
import hashlib
import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path('/home/ubuntu/jc2')
OWN = ROOT / 'box/ideation-20260909T0310Z-astra'
PARTIAL = ROOT / 'xmodel/.ideation-20260909T0310Z-astra.md.partial-378549782e2ba28f4be33a1a0f3fb112'

def pin(path):
    content = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(content).hexdigest(), 'bytes': len(content)}

def main():
    original = json.loads((OWN / 'input-pins.json').read_text())
    checked = []
    for entry in original['entries']:
        actual = pin(ROOT / entry['path'])
        if actual != entry:
            raise SystemExit('charged input drift: ' + entry['path'])
        checked.append(actual)
    primary = json.loads((OWN / 'primary-perimeter.json').read_text())
    primary_actual = pin(ROOT / primary['path'])
    if any(primary_actual[key] != primary[key] for key in ('path', 'sha256', 'bytes')):
        raise SystemExit('primary supplement drift')
    text = PARTIAL.read_text()
    rows = re.findall(r'^\|(\d+)\|(unchanged|raise|lower|reopen)\|', text, re.M)
    if [int(number) for number, _ in rows] != list(range(1, 47)):
        raise SystemExit('full46 vector missing, duplicate or unordered')
    if len(re.findall(r'^## [34]\. Card[12] ', text, re.M)) != 2:
        raise SystemExit('two-card contract drift')
    marker = '<!-- BODY-END -->\n'
    if text.count(marker) != 1 or not text.endswith(marker):
        raise SystemExit('body framing incomplete')
    spec = importlib.util.spec_from_file_location('own_open_metadata', ROOT / 'ops/open_collision.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    questions = module.extract_raised_opens(text)
    if questions:
        raise SystemExit('unexpected raised OPEN; no corpus scan authorized')
    collision_block = module.render_collisions(questions, ())
    if collision_block.rstrip() not in text:
        raise SystemExit('rendered empty collision block absent')
    record = {
        'checked_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'status': 'METADATA_PASS_NOT_MATHEMATICAL_VERIFICATION',
        'charged': checked, 'charged_whole_reads_declared': 32,
        'supplement': primary_actual, 'partial': pin(PARTIAL),
        'avenue_rows': rows, 'cards': 2, 'own_raised_open_count': 0,
        'corpus_scanned': False, 'peer_or_live_gate_reads': False,
        'mathematical_subprocesses': 0, 'body_framing': 'COMPLETE'
    }
    with (OWN / 'submission-check.json').open('x') as output:
        json.dump(record, output, indent=2)
    print(json.dumps({key: record[key] for key in ('checked_utc', 'status', 'cards', 'own_raised_open_count', 'corpus_scanned', 'mathematical_subprocesses')}))

if __name__ == '__main__':
    main()
