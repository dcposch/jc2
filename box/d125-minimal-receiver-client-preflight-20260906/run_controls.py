#!/usr/bin/env python3
"""Bounded terminal receipt for exact toy controls; no production arithmetic."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

box = Path(__file__).resolve().parent
rows = []
for optimized, mutation in [(True, None), (False, 'target'), (True, 'target'),
                            (False, 'face'), (True, 'face')]:
    name = ('O' if optimized else 'normal')+'-'+(mutation or 'pass')
    command = [sys.executable]+(['-O'] if optimized else [])+[
        str(box/'test_client.py'), '--output', str(box/('test-'+name+'-final.json'))]
    if mutation:
        command += ['--mutate', mutation]
    started = time.monotonic()
    run = subprocess.run(command, capture_output=True, text=True, timeout=30)
    expected_rc = 1 if mutation else 0
    if run.returncode != expected_rc:
        raise RuntimeError((name, run.returncode, run.stdout, run.stderr))
    rows.append({'name': name, 'argv': command, 'returncode': run.returncode,
                 'expected_returncode': expected_rc, 'stdout': run.stdout,
                 'stderr': run.stderr, 'seconds': time.monotonic()-started,
                 'terminal': True})
pins = {}
for name in ('client.py', 'test_client.py', 'run_controls.py',
             'test-normal-final.json', 'test-O-pass-final.json'):
    pins[name] = hashlib.sha256((box/name).read_bytes()).hexdigest()
with (box/'control-receipts-final.json').open('x') as out:
    json.dump({'runs': rows, 'sha256': pins, 'all_writers_terminal': True,
               'initial_pretest_corrections': [
                   'Added missing F.__rsub__ after TypeError; no evidence output existed.',
                   'Preserved actual fixed-zero face mutation for external face switch; earlier preliminary face switch rejected a scalar gauge mutation. Final runs use the actual face change.'],
               'earlier_evidence_retained': ['test-normal.json', 'test-O-pass.json', 'control-receipts.json']},
              out, sort_keys=True, indent=2)
    out.write('\n')
print(json.dumps({'status': 'PASS', 'terminal_subprocesses': len(rows), 'sha256': pins}))
