#!/usr/bin/env python3
"""Bounded root replay of two terminal desk packets; no CAS/full rows."""
import ast
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
G = 'box/d125-torsor-geometry-discriminator-20260907/'
D = 'box/d125-defect-order-discriminator-20260907/'
pins = {
    G+'custody.json': '85a329895b923e22e657c731b792e9395fc2c25cefaba56f39c32611e0853986',
    D+'check.py': '5fb9827d147e693b3de49e1d4c9125880c6e459318e1c32a92f78f712a97531d',
    D+'witnesses.json': '6e8c0102089ca6d046f4e1834ce30917a1dff6b2ad7d8ab29de95e7fc7eb83a1',
    D+'replay.json': '984ba0abc7b7d686c844cb31988598d85883bda492cea01d8da69b2139c87c6c',
    'box/d125-small-source-exporter-prep-20260906/baseline.py': 'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
    'xmodel/d125-minimal-receiver-b-reconstruction-astra-20260906.md': 'cd2792c8ec4fdbd286fe7925f36739337ea621eb69d5ea8df90a7cd5804c82bf',
    'xmodel/d125-b-reconstruction-gate-fable5-20260906.md': '3f154e7816deb5de39e727f99cafac3328592c703af246614d4f1e9fe2ccf1ea',
    'box/d125-small-exact-solver-strict-repair-20260907/exact.py': '7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9',
    'box/d125-small-exact-solver-strict-repair-20260907/driver.py': '7f081576ea72005c2509ef2d575aa63b9fd53416987f3535ed520fd79fdc130d',
}
def sha(data):
    return hashlib.sha256(data).hexdigest()
def need(ok, msg):
    if not ok:
        raise ValueError(msg)
need(sha((ROOT/(G+'custody.json')).read_bytes()) == pins[G+'custody.json'], 'custody pin')
for inventory in ('custody.json', 'inputs.json'):
    for row in json.loads((ROOT/(G+inventory)).read_bytes())['files']:
        if row['path'] in pins:
            need(pins[row['path']] == row['sha256'], 'conflicting pin')
        pins[row['path']] = row['sha256']
def verify():
    for name, digest in pins.items():
        need(sha((ROOT/name).read_bytes()) == digest, 'pin '+name)
verify()
scans = {}
for name in (G+'check.py', D+'check.py', 'box/d125-small-source-exporter-prep-20260906/baseline.py'):
    scans[name] = sum(isinstance(node, ast.Assert) for node in ast.walk(ast.parse((ROOT/name).read_bytes())))
    need(scans[name] == 0, 'optimized assertion '+name)
def cap():
    resource.setrlimit(resource.RLIMIT_AS, (512*1024*1024,)*2)
    resource.setrlimit(resource.RLIMIT_CPU, (25,25))
start = time.monotonic()
runs = []
for directory, mutations in ((G, ([], ['mutate-transition'], ['mutate-differential-sign'])),
                             (D, ([], ['--mutate','w2'], ['--mutate','w3'], ['--mutate','nonprimitive']))):
    for opt in ([], ['-O']):
        for args in mutations:
            cmd = [sys.executable, *opt, str(ROOT/(directory+'check.py')), *args]
            run = subprocess.run(cmd, capture_output=True, timeout=30, preexec_fn=cap)
            need(run.returncode == (1 if args else 0), 'unexpected return code '+repr(cmd))
            if not args:
                need(run.stderr == b'', 'nonempty positive stderr')
                if directory == D:
                    need(run.stdout == (ROOT/(D+'witnesses.json')).read_bytes(), 'witness byte mismatch')
            else:
                need(b'ValueError:' in run.stderr, 'wrong mutation failure')
            runs.append({'path': directory+'check.py', 'mode': opt, 'args': args,
                         'rc': run.returncode, 'stdout_sha256': sha(run.stdout),
                         'stderr_sha256': sha(run.stderr)})
verify()
result = {'status': 'PASS', 'pins': pins, 'assert_nodes': scans, 'runs': runs,
          'wall_seconds': time.monotonic()-start,
          'scope': 'Two terminal desk controls only; no independent model promotion or full source arithmetic'}
with (OUT/'replay.json').open('x') as stream:
    json.dump(result, stream, indent=2, sort_keys=True)
    stream.write('\n')
print(json.dumps({'status': 'PASS', 'pins': len(pins), 'runs': len(runs),
                  'wall_seconds': result['wall_seconds'], 'receipt_sha256': sha((OUT/'replay.json').read_bytes())}))
