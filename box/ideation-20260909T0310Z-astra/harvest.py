"""Terminal local publication custody. Metadata only; no mathematical verifier."""
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path('/home/ubuntu/jc2')
OWN = ROOT / 'box/ideation-20260909T0310Z-astra'
REPORT = ROOT / 'xmodel/ideation-20260909T0310Z-astra.md'

def pin(path):
    raw = path.read_bytes()
    return {'path': str(path.relative_to(ROOT)), 'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw)}

def main():
    frozen = json.loads((OWN / 'input-pins.json').read_text())
    current = [pin(ROOT / entry['path']) for entry in frozen['entries']]
    if current != frozen['entries']:
        raise SystemExit('terminal frozen-input drift')
    result = subprocess.run(
        [sys.executable, '-I', '-B', str(ROOT / 'ops/artifact_finalize.py'), 'verify', '--final', str(REPORT)],
        capture_output=True, text=True, timeout=30, check=True)
    if result.stderr:
        raise SystemExit('unexpected transaction verifier stderr')
    verified = json.loads(result.stdout)
    if verified['status'] != 'VERIFIED' or verified['full_sha256'] != '47e1475aeb83b53446e2e8f5df3fae7136941d68715b654d537ddd7e30b36d1a':
        raise SystemExit('unexpected final publication')
    publication = {
        'terminal_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'actual_start_utc': frozen['actual_start_utc'], 'deadline_utc': frozen['deadline_utc'],
        'artifact_verify': verified, 'current_charged': current,
        'mathematical_subprocesses': 0, 'new_primary_sources': 1,
        'peer_or_live_gate_reads': False, 'all_charged_bodies_read_whole': True,
        'own_open_count': 0, 'corpus_scan': False,
        'publication_event': 'An initial close invocation transcribed one token nibble incorrectly and failed INVALID before closing; the matching own lease capability was then used. No frozen body or input was changed, no lease override occurred.',
        'writer_status_on_exit': 'IDLE', 'own_children_awaited_terminal': True
    }
    with (OWN / 'publication.json').open('x') as out:
        json.dump(publication, out, indent=2)
    paths = [OWN / name for name in (
        'pin_packet.py', 'input-pins.json', 'ggv-1401.1784v3.pdf',
        'primary-perimeter.json', 'check_submission.py', 'submission-check.json',
        'harvest.py', 'publication.json')]
    paths.extend([REPORT, pathlib.Path(verified['manifest_path'])])
    custody = {
        'schema': 'jc2.owned-blind-custody/v1',
        'terminal_utc': publication['terminal_utc'],
        'owner': '/root/model_productivity', 'basis': verified['basis'],
        'entries': [pin(path) for path in paths],
        'charged_manifest': frozen['entries'][-1],
        'frozen_inputs_unchanged': True, 'writer_status_on_exit': 'IDLE',
        'remote_writes': False, 'mathematical_subprocesses': 0
    }
    with (OWN / 'custody.json').open('x') as out:
        json.dump(custody, out, indent=2)
    print(json.dumps({'terminal_utc': publication['terminal_utc'], 'report': pin(REPORT),
                      'transaction': pin(pathlib.Path(verified['manifest_path'])),
                      'custody': pin(OWN / 'custody.json'), 'input_pins': pin(OWN / 'input-pins.json'),
                      'publication': pin(OWN / 'publication.json'),
                      'owned_entries': len(custody['entries']), 'current_charged': len(current),
                      'status': 'FINAL_VERIFIED_WRITERS_IDLE_ON_EXIT'}))

if __name__ == '__main__':
    main()
