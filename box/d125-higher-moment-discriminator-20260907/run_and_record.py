#!/usr/bin/env python3
"""Capped exact controls and exclusive byte-pinned evidence export."""
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

base=Path(__file__).resolve().parent
root=base.parent.parent
tag=sys.argv[1] if len(sys.argv)>1 else ''
def cap():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
def write(name,data):
    with (base/(tag+name)).open('xb') as f:
        f.write(data)
def record(p):
    data=p.read_bytes()
    return {'path':str(p.relative_to(root)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
start=time.monotonic();runs=[]
for optimized in (False,True):
    for mode in ('normal','mutate-index','mutate-denominator'):
        p=subprocess.run([sys.executable,*(['-O'] if optimized else []),str(base/'check.py'),mode],capture_output=True,timeout=30,preexec_fn=cap)
        if p.returncode!=(0 if mode=='normal' else 1):
            raise RuntimeError((optimized,mode,p.returncode,p.stdout,p.stderr))
        label=('optimized' if optimized else 'normal')+'-'+mode
        write(label+'.stdout',p.stdout);write(label+'.stderr',p.stderr)
        runs.append({'label':label,'exit_code':p.returncode,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()})
inputs=[root/p for p in ('xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md','xmodel/round2-norm-moment-sep-20260824.md','xmodel/r050-parent-residue-pilot-astra-20260906.md','avenues/MATHIEU.md','avenues/MATHIEU-REVIEW.md')]
inputs+=sorted(base.glob('*.pdf'))+sorted(base.glob('*.txt'))
write('inputs.json',(json.dumps({'schema':'jc2.input-pins/v1','files':[record(p) for p in inputs]},indent=2,sort_keys=True)+'\n').encode())
receipt={'status':'PASS','runs':runs,'wall_seconds':time.monotonic()-start,'caps':{'cpu_seconds':25,'wall_seconds':30,'memory_bytes':512*1024*1024},'no_full_client_powers_or_sampling':True,'all_arithmetic_writers_idle':True}
write('replay.json',(json.dumps(receipt,indent=2,sort_keys=True)+'\n').encode())
print(json.dumps({'status':'PASS','runs':len(runs),'inputs':record(base/(tag+'inputs.json')),'replay':record(base/(tag+'replay.json'))},sort_keys=True))
