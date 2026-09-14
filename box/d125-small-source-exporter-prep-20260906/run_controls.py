#!/usr/bin/env python3
"""Sequential bounded toy subprocess receipts; no remote or production work."""
import json
from pathlib import Path
import subprocess
import sys
import time
import exporter as E

box = Path(__file__).resolve().parent
runs = []
variants = [(True, None)]+[(opt, mutation) for mutation in (
    'missing_low', 'field_split', 'target', 'fixed_zero', 'guard', 'resynced')
    for opt in (False, True)]
for opt, mutation in variants:
    label = ('O' if opt else 'normal')+'-'+(mutation or 'pass')
    argv = [sys.executable]+(['-O'] if opt else [])+[
        str(box/'test_exporter.py'), '--output', str(box/('test-'+label+'-final.json'))]
    if mutation:
        argv += ['--mutation', mutation]
    start = time.monotonic()
    run = subprocess.run(argv, capture_output=True, text=True, timeout=30)
    expected_rc = 1 if mutation else 0
    E.require(run.returncode == expected_rc, 'unexpected control exit '+label)
    E.require(not mutation or 'ValueError: strict full stream replay mismatch at ' in run.stderr,
              'mutation failed for unrelated cause '+label)
    runs.append({'label': label, 'argv': argv, 'rc': run.returncode,
                 'expected_rc': expected_rc, 'stdout': run.stdout, 'stderr': run.stderr,
                 'wall_seconds': time.monotonic()-start, 'terminal': True})
names = ['baseline.py', 'exporter.py', 'test_exporter.py', 'run_controls.py',
         'test-normal-final.json', 'test-O-pass-final.json']
result = {'status': 'PASS', 'all_subprocesses_terminal': True, 'runs': runs,
          'pins': {name: E.sha(box/name) for name in names},
          'production_arithmetic': False, 'remote_or_cas': False}
with (box/'control-receipts-final.json').open('x') as out:
    json.dump(result, out, sort_keys=True, indent=2)
    out.write('\n')
print(json.dumps({'status': 'PASS', 'terminal_subprocesses': len(runs), 'pins': result['pins']}))
