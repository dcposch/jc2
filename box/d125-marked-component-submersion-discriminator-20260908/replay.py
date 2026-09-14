#!/usr/bin/python3
import sys
sys.dont_write_bytecode=True
import ast
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import time

HERE=Path(__file__).resolve().parent
def limit():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))

tree=ast.parse((HERE/'check.py').read_text())
if any(isinstance(n,ast.Assert) for n in ast.walk(tree)):
    raise ValueError('assert forbidden')
rows=[]
reference=None
start=time.monotonic()
for optimized in (False,True):
    for mode in ('normal','bad-M','bad-Q-sign','bad-critical'):
        cmd=['/usr/bin/python3','-I','-B']+(['-O'] if optimized else [])+[str(HERE/'check.py'),mode]
        result=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30,preexec_fn=limit)
        expected=0 if mode=='normal' else 1
        if result.returncode!=expected:
            raise ValueError((mode,optimized,result.returncode,result.stderr.decode()))
        if mode=='normal':
            if reference is not None and reference!=result.stdout:
                raise ValueError('normal/-O bytes differ')
            reference=result.stdout
        rows.append({'optimized':optimized,'mode':mode,'returncode':result.returncode,
                     'stdout_sha256':hashlib.sha256(result.stdout).hexdigest(),
                     'stderr':result.stderr.decode() if mode!='normal' else ''})
with (HERE/'witness.json').open('xb') as f:
    f.write(reference)
receipt={'status':'PASS','runs':rows,'elapsed_seconds':round(time.monotonic()-start,6),
         'caps':{'wall_seconds':30,'cpu_seconds':25,'rss_bytes':536870912},'zero_assert':True}
with (HERE/'replay.json').open('x') as f:
    json.dump(receipt,f,sort_keys=True,indent=2)
    f.write('\n')
print(json.dumps({'status':'PASS','runs':len(rows),'elapsed_seconds':receipt['elapsed_seconds'],
                  'witness_sha256':hashlib.sha256(reference).hexdigest()},sort_keys=True))
