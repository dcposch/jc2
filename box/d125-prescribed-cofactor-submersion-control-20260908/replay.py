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
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))

if any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((HERE/'check.py').read_text()))):
    raise ValueError('assert forbidden')
rows=[]
witness=None
start=time.monotonic()
for opt in (False,True):
    for mode in ('normal','changed-L-sign','changed-derivative-sign','omit-a'):
        argv=['/usr/bin/python3','-I','-B']+(['-O'] if opt else [])+[str(HERE/'check.py'),mode]
        p=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30,preexec_fn=caps)
        expected=0 if mode=='normal' else 1
        if p.returncode!=expected:
            raise ValueError((opt,mode,p.returncode,p.stderr.decode()))
        if mode=='normal':
            if witness is not None and witness!=p.stdout:
                raise ValueError('optimized witness mismatch')
            witness=p.stdout
        rows.append({'optimized':opt,'mode':mode,'returncode':p.returncode,
                     'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr':p.stderr.decode()})
with (HERE/'witness-v2.json').open('xb') as f:
    f.write(witness)
receipt={'status':'PASS','runs':rows,'elapsed_seconds':round(time.monotonic()-start,6),
         'caps':{'wall_seconds':30,'cpu_seconds':25,'rss_bytes':536870912},'zero_assert':True}
with (HERE/'replay-v2.json').open('x') as f:
    json.dump(receipt,f,sort_keys=True,indent=2)
    f.write('\n')
print(json.dumps({'status':'PASS','runs':len(rows),'elapsed_seconds':receipt['elapsed_seconds'],
                  'witness_sha256':hashlib.sha256(witness).hexdigest()},sort_keys=True))
