#!/usr/bin/env python3
"""Two tiny local modes, combined wall<=30 and CPU<=25; AS512MiB each."""
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent


def cap():
    resource.setrlimit(resource.RLIMIT_CPU, (12, 12))
    resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


started = time.monotonic()
runs = []
for optimized in (False, True):
    command = [sys.executable]+(['-O'] if optimized else [])+[str(HERE/'test_construct.py'), '-v']
    result = subprocess.run(command, cwd=HERE, capture_output=True,
                            timeout=max(0.1, 30-(time.monotonic()-started)), preexec_fn=cap)
    runs.append(dict(command=command, rc=result.returncode,
                     stdout=result.stdout.decode(), stderr=result.stderr.decode()))
    if result.returncode:
        break
record = dict(scope='tiny only; no production metadata/row expansion/CAS/AWS',
              elapsed_seconds=time.monotonic()-started, runs=runs,
              pins={p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in sorted(HERE.glob('*.py'))})
target = sys.argv[1] if len(sys.argv) == 2 else 'test-results.json'
if Path(target).name != target or not target.endswith('.json'):
    raise ValueError('one fresh local evidence basename required')
with (HERE/target).open('x') as stream:
    json.dump(record, stream, sort_keys=True, indent=2)
    stream.write('\n')
print(json.dumps(record, sort_keys=True))
sys.exit(0 if len(runs) == 2 and all(r['rc'] == 0 for r in runs) else 1)
