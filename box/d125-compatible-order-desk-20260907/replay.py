#!/usr/bin/env python3
import ast
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time
base = Path(__file__).resolve().parent
code = base/'check.py'
def cap():
    resource.setrlimit(resource.RLIMIT_CPU, (25,25))
    resource.setrlimit(resource.RLIMIT_AS, (512*1024*1024,)*2)
start = time.monotonic()
before = hashlib.sha256(code.read_bytes()).hexdigest()
if any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(code.read_bytes()))):
    raise ValueError('Assert gate')
runs = []
for flags in ([], ['-O']):
    for mode in ('normal','no-w4','reverse-w5'):
        p = subprocess.run([sys.executable,*flags,str(code),mode],capture_output=True,timeout=30,preexec_fn=cap)
        if p.returncode != (0 if mode=='normal' else 1):
            raise ValueError((flags,mode,p.returncode,p.stderr))
        if mode=='normal':
            if flags:
                if p.stdout != (base/'witness.json').read_bytes():
                    raise ValueError('mode drift')
            else:
                with (base/'witness.json').open('xb') as f:
                    f.write(p.stdout)
        elif b'ValueError:' not in p.stderr:
            raise ValueError('wrong failure')
        runs.append({'flags':flags,'mode':mode,'rc':p.returncode,
                     'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),
                     'stderr':p.stderr.decode() if p.returncode else ''})
if hashlib.sha256(code.read_bytes()).hexdigest()!=before:
    raise ValueError('code drift')
record = {'status':'PASS', 'code_sha256':before,'assert_nodes':0,'runs':runs,
          'wall_seconds':time.monotonic()-start}
with (base/'replay.json').open('x') as f:
    json.dump(record,f,indent=2,sort_keys=True)
    f.write('\n')
print(json.dumps({'status':'PASS','wall_seconds':record['wall_seconds'],'runs':len(runs),
                  'code_sha256':before,'witness_sha256':hashlib.sha256((base/'witness.json').read_bytes()).hexdigest(),
                  'replay_sha256':hashlib.sha256((base/'replay.json').read_bytes()).hexdigest(),
                  'order_sha256':json.loads((base/'witness.json').read_bytes())['order_sha256']}))
