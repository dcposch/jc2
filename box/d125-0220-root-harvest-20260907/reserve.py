"""Tiny root replay of the terminal independent five-row desk gate."""
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
G = ROOT/'box/d125-compatible-order-delta-gate-fable5-20260907'
def need(ok, why):
    if not ok:
        raise ValueError(why)
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
pins = {
 'xmodel/d125-compatible-order-delta-gate-fable5-20260907.md':'31650da9234577fa7a6f12004ce31efb0aea0fcc920b4fb6cc818d0c0ff5d327',
 'box/d125-compatible-order-delta-gate-fable5-20260907/gate_own.py':'60525071f7ab2df38b2a3f3197503bcad843c2fcd4151f08352fa46e7f04fa79',
 'box/d125-compatible-order-desk-20260907/witness.json':'86804185bbaba641f2a3305dd379aa06e2f85a5f833233c79a10b575c0be67f6',
 'box/d125-small-source-exporter-prep-20260906/baseline.py':'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'}
def verify():
    for name, sha in pins.items():
        need(digest(ROOT/name) == sha, 'pin '+name)
verify()
for path in (G/'gate_own.py', ROOT/'box/d125-small-source-exporter-prep-20260906/baseline.py', Path(__file__)):
    need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(path.read_bytes()))), 'Assert gate')
def cap():
    resource.setrlimit(resource.RLIMIT_CPU, (25,25))
    resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
runs = []
start = time.monotonic()
for flags in ([], ['-O']):
    for mode in ('normal','no-w4','reverse-w5','bad-matrix','w1-zero-lambda'):
        argv = [sys.executable, '-I', '-B', *flags, str(G/'gate_own.py'),
                '--baseline', str(ROOT/'box/d125-small-source-exporter-prep-20260906/baseline.py'),
                '--witness', str(ROOT/'box/d125-compatible-order-desk-20260907/witness.json'), '--mode', mode]
        p = subprocess.run(argv, capture_output=True, timeout=30, preexec_fn=cap)
        need(p.returncode == (0 if mode == 'normal' else 1), 'exit '+mode)
        if mode == 'normal':
            need(p.stderr == b'' and hashlib.sha256(p.stdout).hexdigest() ==
                 'b460190fb43860eeb7f3e0466d8e6bd601acab1b0ce2426330c95516d07f64ca', 'positive bytes')
        else:
            need(b'RuntimeError: FAIL:' in p.stderr and p.stdout == b'', 'mutation rejection')
        runs.append({'mode':mode, 'flags':flags, 'returncode':p.returncode,
                     'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),
                     'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()})
verify()
record = {'status':'PASS','pins':pins,'runs':runs,'wall_seconds':time.monotonic()-start,
          'assert_nodes':0,'scope':'desk leading-ideal delta only; no five-row engine/code/solver claim'}
with (OUT/'reserve.json').open('x') as f:
    json.dump(record, f, indent=2, sort_keys=True)
    f.write('\n')
print(json.dumps({'status':'PASS','runs':len(runs),'wall_seconds':record['wall_seconds'],
                  'receipt_sha256':digest(OUT/'reserve.json')}))
