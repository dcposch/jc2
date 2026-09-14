#!/usr/bin/env python3
"""Bounded byte-preserving exclusive export; only small receipt to terminal."""
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent

def caps():
    resource.setrlimit(resource.RLIMIT_CPU, (25,25))
    resource.setrlimit(resource.RLIMIT_AS, (512*1024*1024,512*1024*1024))

records = []
for optimized in (False, True):
    for mutation in ('', '--mutate-parity', '--mutate-lambda-weight'):
        command = [sys.executable] + (['-O'] if optimized else []) + [str(HERE/'check.py')] + ([mutation] if mutation else [])
        start = time.monotonic()
        result = subprocess.run(command, capture_output=True, timeout=30, preexec_fn=caps)
        expected = 1 if mutation else 0
        if (result.returncode != 0) != bool(expected):
            raise RuntimeError('unexpected control exit: '+result.stderr.decode())
        if mutation:
            expected_message = b'forbidden parity/character slot' if mutation == '--mutate-parity' else b'lift row covariance'
            if expected_message not in result.stderr:
                raise RuntimeError('mutation failed for an unrelated reason')
        else:
            with (HERE/('witness-O.json' if optimized else 'witness.json')).open('xb') as handle:
                handle.write(result.stdout)
        records.append({'optimized': optimized, 'mutation': mutation or None,
                        'returncode': result.returncode, 'wall_seconds': round(time.monotonic()-start, 6),
                        'stdout_sha256': hashlib.sha256(result.stdout).hexdigest(),
                        'stderr_sha256': hashlib.sha256(result.stderr).hexdigest()})
if (HERE/'witness.json').read_bytes() != (HERE/'witness-O.json').read_bytes():
    raise RuntimeError('normal/-O witness mismatch')
receipt = {'status': 'PASS', 'runs': records, 'all_writers_finished': True,
           'arithmetic_caps': {'each_wall_seconds':30,'each_CPU_seconds':25,'each_AS_MiB':512},
           'no_assert_nodes': True, 'raw_stdout_export': 'bytes -> exclusive file, no JS numeric roundtrip'}
with (HERE/'replay.json').open('x') as handle:
    json.dump(receipt, handle, sort_keys=True, indent=2)
    handle.write('\n')
print(json.dumps({'status':'PASS','runs':len(records),'witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest(),
                  'witness_bytes':(HERE/'witness.json').stat().st_size}))
