"""Metadata and exclusive mechanical snapshots only; never mathematical code."""
import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path('/home/ubuntu/jc2')
OWN = ROOT / 'box/triple-cover-three-simple-gate-20260909'
FINAL = 'xmodel/triple-cover-three-simple-gate-prep-astra-20260909.md'
TOKEN = '81278ba7f59d68887eddc141dd8aeb9c1cdbf7aba7ffbd1c1a83f61d4f7cfba7'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def put(name, value):
    with (OWN / name).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')

def main():
    c1path = ROOT / 'box/triple-three-simple-separated-20260909/custody.json'
    c2path = ROOT / 'box/triple-source-contact-cover-20260909/custody.json'
    if sha(c1path) != '1fc65eef2477c5b0b8c27418010ed3b6989e6b17271c60d6ef53602fcfee1717' or sha(c2path) != '60eb523cce013f595ccc7f70b67fe5c5e6ea4b4e0a19bd726c03e4d085ff2050':
        raise SystemExit('custody drift')
    c1, c2 = json.loads(c1path.read_text()), json.loads(c2path.read_text())
    scientific = c1['entries'] + c2['entries'] + c2['inputs']
    scientific += json.loads((ROOT / 'box/triple-three-simple-separated-20260909/input-pins.json').read_text())['entries']
    for r in scientific:
        p = ROOT / r['path']
        if sha(p) != r['sha256'] or p.stat().st_size != r['bytes']:
            raise SystemExit('source drift: ' + r['path'])
    wf_gate = ROOT / 'xmodel/d125-weightfree-composition-gate-fable5-20260909.md'
    if sha(wf_gate) != '1337b099163ab59ae862e7fc83fcfa6491444ebb745400e5ed2b35e3512760ac':
        raise SystemExit('old gate drift')
    cubic_gate = ROOT / 'xmodel/triple-cubic-source-coalesced-gate-fable5-20260909.md'
    if sha(cubic_gate) != 'cc5f4ca64fef11197c84e6d19b6bc8b5c3d526adac05cb66b28d94573144525b':
        raise SystemExit('accepted cubic gate drift')
    sources = [
        ('xmodel/triple-source-contact-cover-astra-20260909.md', 'contact-cover-proof.md'),
        ('xmodel/triple-source-contact-cover-astra-20260909.md.artifact.json', 'contact-cover-transaction.json'),
        ('box/triple-source-contact-cover-20260909/custody.json', 'contact-cover-custody.json'),
        ('xmodel/triple-three-simple-separated-coordinator-20260909.md', 'three-simple-proof.md'),
        ('xmodel/triple-three-simple-separated-coordinator-20260909.md.artifact.json', 'three-simple-transaction.json'),
        ('box/triple-three-simple-separated-20260909/custody.json', 'three-simple-custody.json'),
        ('xmodel/late-contact-triple-endpoint-astra-20260909.md', 'canonical-lateT-proof.md'),
        ('xmodel/late-contact-triple-endpoint-gate-fable5-20260909.md', 'canonical-lateT-gate.md'),
        ('xmodel/d125-weightfree-local-consumer-coordinator-20260909.md', 'generic-double-local-proof.md'),
        ('xmodel/d125-weightfree-composition-gate-fable5-20260909.md', 'generic-double-local-gate.md'),
        ('xmodel/triple-cubic-source-coalesced-astra-20260909.md', 'conditional-cubic-chart-proof.md'),
        ('xmodel/triple-cubic-source-coalesced-gate-fable5-20260909.md', 'accepted-cubic-chart-gate.md')]
    (OWN / 'inputs').mkdir()
    rows = []
    for name, basename in sources:
        source, target = ROOT / name, OWN / 'inputs' / basename
        if target.exists() or target.is_symlink():
            raise SystemExit('existing snapshot')
        digest = sha(source)
        shutil.copyfile(source, target)
        target.chmod(0o444)
        if sha(source) != digest or sha(target) != digest:
            raise SystemExit('copy drift')
        rows.append({'original': name, 'snapshot': str(target.relative_to(ROOT)),
                     'original_sha256': digest, 'snapshot_sha256': digest, 'bytes': target.stat().st_size})
    scope = OWN / 'scope.md'
    rows.append({'original': str(scope.relative_to(ROOT)), 'snapshot': str(scope.relative_to(ROOT)),
                 'original_sha256': sha(scope), 'snapshot_sha256': sha(scope), 'bytes': scope.stat().st_size})
    put('PINS.json', {'status': 'FROZEN_PREP_ONLY', 'entries': rows,
                      'original_custody_perimeter': scientific})
    prompt = OWN / 'fable.prompt.md'
    result = subprocess.run(['sed', '-n', 's/^charged_input=//p', str(prompt)],
                            capture_output=True, text=True, check=True, timeout=10)
    charged = result.stdout.splitlines()
    if charged != [r['snapshot'] for r in rows] or len(set(Path(p).name for p in charged)) != 13:
        raise SystemExit('literal parser mismatch')
    body = prompt.read_text()
    if '{{LANE_INPUTS}}' not in body or 'xmodel/triple-cover-three-simple-gate-fable5-20260909.md' not in body:
        raise SystemExit('placeholder/output mismatch')
    if any(line.startswith('charge_basis=') for line in body.splitlines()):
        raise SystemExit('price declaration')
    put('preflight.json', {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                           'status': 'PASS_PREP_ONLY', 'actual_sed_inputs': charged,
                           'prompt_sha256': sha(prompt), 'deadline': 'UNSET_UNTIL_INVITATION',
                           'launch': False, 'math_subprocesses': 0})
    outcomes = []
    for op in ('close', 'finalize', 'verify'):
        argv = ['python3', '-I', '-B', 'ops/artifact_finalize.py', op, '--final', FINAL]
        if op != 'verify':
            argv += ['--token', TOKEN]
        r = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True, timeout=30)
        outcomes.append({'argv': argv, 'returncode': r.returncode, 'stdout': r.stdout, 'stderr': r.stderr})
        if r.returncode:
            put('publication-failure.json', outcomes)
            raise SystemExit('publication failed')
    for row in rows:
        if sha(ROOT / row['original']) != row['original_sha256'] or sha(ROOT / row['snapshot']) != row['snapshot_sha256']:
            raise SystemExit('post input drift')
    utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    put('publication.json', {'terminal_utc': utc, 'outcomes': outcomes, 'post_pins': 'UNCHANGED'})
    owned = [OWN / 'freeze_metadata.py', prompt, scope, OWN / 'PINS.json', OWN / 'preflight.json',
             OWN / 'publication.json', ROOT / FINAL, ROOT / (FINAL + '.artifact.json')]
    owned += [OWN / 'inputs' / name for _, name in sources]
    put('custody.json', {'terminal_utc': utc, 'writers': 'IDLE', 'children': [], 'launch': False,
                        'mathematical_subprocesses': 0,
                        'entries': [{'path': str(p.relative_to(ROOT)), 'sha256': sha(p),
                                     'bytes': p.stat().st_size} for p in owned]})
    for p in owned + [OWN / 'custody.json']:
        p.chmod(0o444)
    print(json.dumps({'terminal_utc': utc, 'report_sha256': sha(ROOT / FINAL),
                      'transaction_sha256': sha(ROOT / (FINAL + '.artifact.json')),
                      'prompt_sha256': sha(prompt), 'PINS_sha256': sha(OWN / 'PINS.json'),
                      'custody_sha256': sha(OWN / 'custody.json'), 'preflight_sha256': sha(OWN / 'preflight.json'),
                      'owned_entries': len(owned), 'charged_inputs': len(charged), 'writers': 'IDLE'}))

if __name__ == '__main__':
    main()
