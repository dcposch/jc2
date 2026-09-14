#!/usr/bin/env python3
"""Bounded tiny replays and byte-pinned inputs; no numeric JS roundtrip."""
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

base = Path(__file__).resolve().parent
root = base.parent.parent
def cap():
    resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
    resource.setrlimit(resource.RLIMIT_AS, (512*1024*1024, 512*1024*1024))
def write(name, data):
    with (base/name).open('xb') as f:
        f.write(data)
def record(path):
    data = path.read_bytes()
    return {'path': str(path.relative_to(root)), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
start = time.monotonic()
runs = []
for opt in ([], ['-O']):
    for mode in ('normal', 'mutate-transition', 'mutate-differential-sign'):
        p = subprocess.run([sys.executable, *opt, str(base/'check.py'), mode], capture_output=True, timeout=30, preexec_fn=cap)
        expected = 0 if mode == 'normal' else 1
        if p.returncode != expected:
            raise RuntimeError((opt, mode, p.returncode, p.stdout, p.stderr))
        label = ('optimized' if opt else 'normal') + '-' + mode
        write(label+'.stdout', p.stdout)
        write(label+'.stderr', p.stderr)
        runs.append({'label': label, 'returncode': p.returncode, 'stdout_sha256': hashlib.sha256(p.stdout).hexdigest(), 'stderr_sha256': hashlib.sha256(p.stderr).hexdigest()})
inputs = [root/p for p in (
    'xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md',
    'xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md',
    'xmodel/d125-lambda-translation-discriminator-astra-20260907.md',
    'xmodel/bd-a2-firstleg-log-kodaira-coordinator-integration-sol56-20260830.md')]
inputs += sorted(base.glob('*.pdf')) + sorted(base.glob('*.txt')) + sorted(base.glob('*.html'))
write('inputs.json', (json.dumps({'schema': 'jc2.input-pins/v1', 'files': [record(p) for p in inputs]}, indent=2, sort_keys=True)+'\n').encode())
receipt = {'status': 'PASS', 'wall_seconds': time.monotonic()-start, 'runs': runs, 'caps': {'per_process_cpu_seconds':25, 'per_process_wall_seconds':30, 'per_process_memory_bytes':512*1024*1024}, 'all_arithmetic_writers_idle': True}
write('replay.json', (json.dumps(receipt, indent=2, sort_keys=True)+'\n').encode())
print(json.dumps({'status': 'PASS', 'runs': len(runs), 'replay': record(base/'replay.json'), 'inputs': record(base/'inputs.json')}, sort_keys=True))
