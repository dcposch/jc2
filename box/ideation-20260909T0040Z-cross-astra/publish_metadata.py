"""Metadata/publication only. No mathematical imports or calculations."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path('/home/ubuntu/jc2')
OWN = ROOT / 'box/ideation-20260909T0040Z-cross-astra'
FINAL = 'xmodel/ideation-20260909T0040Z-cross-astra.md'
TOKEN = 'a0e4ecd23fe670070b4fa914bd6e63308f8191e47bfc231f059f88dc7053d1a9'
PROMPT = 'box/ideation-20260909T0040Z/cross-astra.prompt.md'
CPINS = 'box/ideation-20260909T0040Z/cross-PINS.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def put(name, value):
    with (OWN / name).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def main():
    pins = json.loads((ROOT / CPINS).read_text())['pins']
    charged = [line.split('=', 1)[1] for line in (ROOT / PROMPT).read_text().splitlines()
               if line.startswith('charged_input=')]
    if len(charged) != 10 or len(set(charged)) != 10:
        raise SystemExit('wrong input vector')
    entries = []
    for name in charged + [PROMPT]:
        path = ROOT / name
        digest = sha(path)
        if digest != pins[name]:
            raise SystemExit('input drift: ' + name)
        entries.append({'path': name, 'sha256': digest, 'bytes': path.stat().st_size})
    entries.append({'path': CPINS, 'sha256': sha(ROOT / CPINS),
                    'bytes': (ROOT / CPINS).stat().st_size})
    put('input-pins.json', {'read_scope': 'ten charged bodies WHOLE; metadata only otherwise',
                            'entries': entries})
    outcomes = []
    for op in ('close', 'finalize', 'verify'):
        argv = ['python3', '-I', '-B', 'ops/artifact_finalize.py', op, '--final', FINAL]
        if op != 'verify':
            argv += ['--token', TOKEN]
        result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=30)
        outcomes.append({'argv': argv, 'returncode': result.returncode,
                         'stdout': result.stdout, 'stderr': result.stderr})
        if result.returncode:
            put('publication-failure.json', outcomes)
            raise SystemExit('publication failed')
    for entry in entries:
        if sha(ROOT / entry['path']) != entry['sha256']:
            raise SystemExit('post-publication input drift')
    utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    put('publication.json', {'terminal_utc': utc, 'outcomes': outcomes,
                             'post_input_pins': 'UNCHANGED', 'math_subprocesses': 0})
    owned = [OWN / 'publish_metadata.py', OWN / 'input-pins.json', OWN / 'publication.json',
             ROOT / FINAL, ROOT / (FINAL + '.artifact.json')]
    put('custody.json', {'terminal_utc': utc, 'writers': 'IDLE', 'children': [],
                        'entries': [{'path': str(p.relative_to(ROOT)), 'sha256': sha(p),
                                     'bytes': p.stat().st_size} for p in owned]})
    print(json.dumps({'terminal_utc': utc, 'report_sha256': sha(ROOT / FINAL),
                      'transaction_sha256': sha(ROOT / (FINAL + '.artifact.json')),
                      'custody_sha256': sha(OWN / 'custody.json'),
                      'input_pins_sha256': sha(OWN / 'input-pins.json'),
                      'publication_sha256': sha(OWN / 'publication.json'),
                      'writers': 'IDLE'}))

if __name__ == '__main__':
    main()
