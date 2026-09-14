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
rows=[]; witness=None; start=time.monotonic()
for opt in (False,True):
    for mode in ('normal','wrong-middle','freeze-conjugate','wrong-motion-sign','wrong-c-normalization'):
        argv=['/usr/bin/python3','-I','-B']+(['-O'] if opt else [])+[str(HERE/'check.py'),mode]
        z=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30,preexec_fn=caps)
        if z.returncode!=(0 if mode=='normal' else 1): raise ValueError((mode,opt,z.returncode,z.stderr.decode()))
        if mode=='normal':
            if witness is not None and witness!=z.stdout: raise ValueError('optimized mismatch')
            witness=z.stdout
        rows.append({'mode':mode,'optimized':opt,'returncode':z.returncode,
                     'stdout_sha256':hashlib.sha256(z.stdout).hexdigest(),'stderr':z.stderr.decode()})
with (HERE/'witness.json').open('xb') as f: f.write(witness)
receipt={'status':'PASS','runs':rows,'elapsed_seconds':round(time.monotonic()-start,6),
         'caps':{'wall_seconds':30,'cpu_seconds':25,'rss_bytes':536870912},'zero_assert':True}
with (HERE/'replay.json').open('x') as f: json.dump(receipt,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'PASS','runs':len(rows),'elapsed_seconds':receipt['elapsed_seconds'],
                  'witness_sha256':hashlib.sha256(witness).hexdigest()},sort_keys=True))
