#!/usr/bin/env python3
"""Bound normal/-O runner with five expected-failure corruption modes."""
import argparse
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time


def need(condition, message):
    if not condition:
        raise RuntimeError(message)


parser = argparse.ArgumentParser()
parser.add_argument('--inputs', required=True)
parser.add_argument('--output', required=True)
args = parser.parse_args()
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
signal.alarm(30)
started = time.monotonic()
checker = Path(__file__).with_name('gate_check.py').resolve()
runs = []
for optimized in (False, True):
    for inject in ('none', 'cofactor', 'buchberger', 'protocol', 'source', 'authority'):
        command = [sys.executable, '-B'] + (['-O'] if optimized else []) + [
            str(checker), '--inputs', str(Path(args.inputs).resolve()), '--inject', inject]
        completed = subprocess.run(command, capture_output=True, text=True,
              env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'},
              timeout=max(1, 29-(time.monotonic()-started)))
        expected = 0 if inject == 'none' else 1
        need(completed.returncode == expected,
             'unexpected rc for '+inject+' optimized='+str(optimized))
        if inject != 'none':
            needles = {'cofactor': 'not one', 'buchberger': 'Buchberger',
                       'protocol': 'index/short', 'source': 'literal ring/suffix',
                       'authority': 'separation'}
            need(needles[inject] in completed.stderr,
                 'wrong corruption failure for '+inject)
        runs.append({'optimized': optimized, 'inject': inject,
                     'returncode': completed.returncode,
                     'stdout': completed.stdout, 'stderr': completed.stderr})
report = {'status': 'PASS', 'runs': runs, 'wall_seconds': time.monotonic()-started,
          'child_user_seconds': resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime,
          'child_system_seconds': resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime,
          'child_maxrss_kib': resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss}
encoded = (json.dumps(report, sort_keys=True)+'\n').encode()
with Path(args.output).open('xb') as output:
    output.write(encoded)
    output.flush()
    os.fsync(output.fileno())
print(json.dumps({'status': report['status'], 'runs': len(runs),
                  'wall_seconds': report['wall_seconds'],
                  'child_maxrss_kib': report['child_maxrss_kib']}, sort_keys=True))
