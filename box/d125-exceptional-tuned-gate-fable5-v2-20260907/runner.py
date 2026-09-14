#!/usr/bin/env python3
import sys; sys.dont_write_bytecode=True
import subprocess, hashlib, json, resource, time
from pathlib import Path
HERE=Path(__file__).resolve().parent
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
modes=[('',None),('--mutate-wrong-quadratic',b'C1-identity'),('--mutate-omit-cross',b'C1-identity'),('--mutate-zero-cross',b'C1-nonzero-cross'),
       ('--mutate-omit-reference-betaF',b'C2-reference-G'),('--mutate-low-p3',b'C3-low-rows-kill-c-d')]
recs=[]; t0=time.time(); ok=True
for opt in (False,True):
    for mode,msg in modes:
        cmd=[sys.executable,'-B']+(['-O'] if opt else [])+[str(HERE/'gate_controls.py')]+([mode] if mode else [])
        out=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps)
        exp=(out.returncode!=0)==bool(mode) and (msg is None or msg in out.stderr)
        ok=ok and exp
        if not mode: (HERE/('witness-O.json' if opt else 'witness.json')).write_bytes(out.stdout)
        recs.append({'optimized':opt,'mutation':mode or None,'returncode':out.returncode,'expected':exp,
                     'first_fail':out.stderr.decode().strip()[:120] or None,'stdout_sha256':hashlib.sha256(out.stdout).hexdigest()})
same=(HERE/'witness.json').read_bytes()==(HERE/'witness-O.json').read_bytes()
rep={'status':'PASS' if ok and same else 'FAIL','runs':recs,'witness_bytes_identical':same,'wall_s':round(time.time()-t0,2),
     'caps':'30 wall / 25 CPU s / 512 MiB each','witness_sha256':hashlib.sha256((HERE/'witness.json').read_bytes()).hexdigest()}
(HERE/'replay.json').write_text(json.dumps(rep,indent=1,sort_keys=True)+'\n')
print(json.dumps({k:rep[k] for k in ('status','witness_bytes_identical','wall_s','witness_sha256')}))
for r in recs: print(r['optimized'],r['mutation'],r['returncode'],r['expected'],r['first_fail'])
