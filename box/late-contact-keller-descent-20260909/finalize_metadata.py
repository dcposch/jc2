"""Pinning and publication only; no mathematical subprocess or source arithmetic."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path('/home/ubuntu/jc2')
OWN = ROOT / 'box/late-contact-keller-descent-20260909'
FINAL = 'xmodel/late-contact-keller-descent-astra-20260909.md'
TOKEN = '9b5f3d21690f595562d0826426e90c1aa722d6618844854a4d9158e14a0826f9'
PINS = {
    'xmodel/late-contact-triple-endpoint-astra-20260909.md':
        'b541308788da31f52e9f7985c7767e206231e8f3251ff53c1b2bd9c96b64f097',
    'xmodel/late-contact-triple-endpoint-gate-fable5-20260909.md':
        'c9a399a87dc91d78bfc4f811249996ea3e217eda075be679cf27b41af5795c26'}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def put(name, value):
    with (OWN / name).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def check_inputs():
    for name, digest in PINS.items():
        if sha(ROOT / name) != digest:
            raise SystemExit('input drift: ' + name)

def main():
    check_inputs()
    rows = [{'path': name, 'sha256': digest, 'bytes': (ROOT / name).stat().st_size,
             'read_scope': 'WHOLE; finite general lemma accepted, triple endpoint not a premise'}
            for name, digest in PINS.items()]
    put('input-pins.json', {'entries': rows, 'mathematical_subprocesses': 0})
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
    check_inputs()
    utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    put('publication.json', {'terminal_utc': utc, 'outcomes': outcomes, 'post_inputs': 'UNCHANGED'})
    owned = [OWN / 'finalize_metadata.py', OWN / 'input-pins.json', OWN / 'publication.json',
             ROOT / FINAL, ROOT / (FINAL + '.artifact.json')]
    put('custody.json', {'terminal_utc': utc, 'status': 'PROVISIONAL_COORDINATE_OBSTRUCTION_AND_CONDITIONAL_DESCENT',
                        'writers': 'IDLE', 'children': [], 'mathematical_subprocesses': 0,
                        'entries': [{'path': str(p.relative_to(ROOT)), 'sha256': sha(p),
                                     'bytes': p.stat().st_size} for p in owned], 'inputs': rows})
    for path in owned + [OWN / 'custody.json']:
        path.chmod(0o444)
    print(json.dumps({'terminal_utc': utc, 'report_sha256': sha(ROOT / FINAL),
                      'transaction_sha256': sha(ROOT / (FINAL + '.artifact.json')),
                      'custody_sha256': sha(OWN / 'custody.json'),
                      'input_pins_sha256': sha(OWN / 'input-pins.json'),
                      'publication_sha256': sha(OWN / 'publication.json'),
                      'owned_entries': len(owned), 'writers': 'IDLE'}))

if __name__ == '__main__':
    main()
