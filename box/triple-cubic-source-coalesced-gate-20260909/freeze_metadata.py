"""Exclusive mechanical snapshots and metadata checks/publication only."""
import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path('/home/ubuntu/jc2')
OWN = ROOT / 'box/triple-cubic-source-coalesced-gate-20260909'
FINAL = 'xmodel/triple-cubic-source-coalesced-gate-prep-astra-20260909.md'
TOKEN = '0a88bbd298afde3113af3b0886dbc9aec1ec12cb1dea6e9ed28ec691d2956170'
PROD = ROOT / 'box/triple-cubic-source-coalesced-20260909/custody.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def put(name, value):
    with (OWN / name).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def main():
    custody = json.loads(PROD.read_text())
    original = custody['entries'] + custody['inputs']
    pins = {r['path']: r['sha256'] for r in original}
    for row in original:
        p = ROOT / row['path']
        if sha(p) != row['sha256'] or p.stat().st_size != row['bytes']:
            raise SystemExit('producer custody drift: ' + row['path'])
    sources = [
        ('xmodel/triple-cubic-source-coalesced-astra-20260909.md', 'cubic-source-proof.md'),
        ('xmodel/triple-cubic-source-coalesced-astra-20260909.md.artifact.json', 'cubic-source-transaction.json'),
        ('box/triple-cubic-source-coalesced-20260909/custody.json', 'cubic-source-custody.json'),
        ('box/triple-cubic-source-coalesced-20260909/input-pins.json', 'cubic-source-input-pins.json'),
        ('xmodel/positive-face-actual-receiver-discriminator-astra-20260906.md', 'moh-actual-source.md'),
        ('xmodel/positive-face-actual-receiver-gate-fable5-20260906.md', 'moh-actual-source-gate.md')]
    (OWN / 'inputs').mkdir()
    rows = []
    for original_name, basename in sources:
        source = ROOT / original_name
        destination = OWN / 'inputs' / basename
        if destination.exists() or destination.is_symlink():
            raise SystemExit('snapshot target exists')
        before = sha(source)
        shutil.copyfile(source, destination)
        destination.chmod(0o444)
        if sha(source) != before or sha(destination) != before:
            raise SystemExit('copy drift')
        rows.append({'original': original_name, 'snapshot': str(destination.relative_to(ROOT)),
                     'original_sha256': before, 'snapshot_sha256': sha(destination),
                     'bytes': destination.stat().st_size})
    scope = OWN / 'scope.md'
    rows.append({'original': str(scope.relative_to(ROOT)), 'snapshot': str(scope.relative_to(ROOT)),
                 'original_sha256': sha(scope), 'snapshot_sha256': sha(scope),
                 'bytes': scope.stat().st_size})
    put('PINS.json', {'status': 'FROZEN_PREP_ONLY', 'entries': rows,
                      'producer_owned_source_checks': original})
    prompt = OWN / 'fable.prompt.md'
    extraction = subprocess.run(['sed', '-n', 's/^charged_input=//p', str(prompt)],
                                capture_output=True, text=True, check=True, timeout=10)
    charged = extraction.stdout.splitlines()
    expected = [r['snapshot'] for r in rows]
    if charged != expected or len(set(Path(p).name for p in charged)) != 7:
        raise SystemExit('literal parser/input vector mismatch')
    body = prompt.read_text()
    if '{{LANE_INPUTS}}' not in body or 'xmodel/triple-cubic-source-coalesced-gate-fable5-20260909.md' not in body:
        raise SystemExit('placeholder/output mismatch')
    if any(line.startswith('charge_basis=') for line in body.splitlines()):
        raise SystemExit('unlicensed price declaration')
    put('preflight.json', {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                           'status': 'PASS_PREP_ONLY', 'actual_sed_inputs': charged,
                           'prompt_sha256': sha(prompt), 'launch': False,
                           'deadline': 'UNSET_UNTIL_ROOT_INVITATION', 'math_subprocesses': 0})
    results = []
    for op in ('close', 'finalize', 'verify'):
        argv = ['python3', '-I', '-B', 'ops/artifact_finalize.py', op, '--final', FINAL]
        if op != 'verify':
            argv += ['--token', TOKEN]
        result = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=30)
        results.append({'argv': argv, 'returncode': result.returncode,
                        'stdout': result.stdout, 'stderr': result.stderr})
        if result.returncode:
            put('publication-failure.json', results)
            raise SystemExit('publication failed')
    for row in rows:
        if sha(ROOT / row['original']) != row['original_sha256'] or sha(ROOT / row['snapshot']) != row['snapshot_sha256']:
            raise SystemExit('final input drift')
    utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    put('publication.json', {'terminal_utc': utc, 'outcomes': results, 'post_pins': 'UNCHANGED'})
    owned = [OWN / 'freeze_metadata.py', prompt, scope, OWN / 'PINS.json', OWN / 'preflight.json',
             OWN / 'publication.json', ROOT / FINAL, ROOT / (FINAL + '.artifact.json')]
    owned += [OWN / 'inputs' / name for _, name in sources]
    put('custody.json', {'terminal_utc': utc, 'writers': 'IDLE', 'children': [],
                        'launch': False, 'mathematical_subprocesses': 0,
                        'entries': [{'path': str(p.relative_to(ROOT)), 'sha256': sha(p),
                                     'bytes': p.stat().st_size} for p in owned]})
    for p in owned + [OWN / 'custody.json']:
        p.chmod(0o444)
    print(json.dumps({'terminal_utc': utc, 'report_sha256': sha(ROOT / FINAL),
                      'transaction_sha256': sha(ROOT / (FINAL + '.artifact.json')),
                      'prompt_sha256': sha(prompt), 'PINS_sha256': sha(OWN / 'PINS.json'),
                      'custody_sha256': sha(OWN / 'custody.json'),
                      'preflight_sha256': sha(OWN / 'preflight.json'),
                      'owned_entries': len(owned), 'charged_inputs': len(charged), 'writers': 'IDLE'}))

if __name__ == '__main__':
    main()
