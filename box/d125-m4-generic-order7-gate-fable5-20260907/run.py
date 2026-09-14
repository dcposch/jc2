#!/usr/bin/env python3
import sys; sys.dont_write_bytecode=True
import subprocess, hashlib, json, resource, time
from pathlib import Path
HERE=Path(__file__).resolve().parent; G=HERE/'gate_controls.py'
def caps(): resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,)*2)
modes=['','--mutate-omit-moving-derivative','--mutate-double-factor','--mutate-drop-gamma6-R1','--mutate-even-kernel','--mutate-point-relation','--mutate-h-zero']
recs=[]; t0=time.time(); wit={}
for opt in (False,True):
    for m in modes:
        cmd=[sys.executable,'-B']+(['-O'] if opt else [])+[str(G)]+([m] if m else [])
        r=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps)
        recs.append({'optimized':opt,'mutation':m or None,'rc':r.returncode,'stderr':r.stderr.decode().strip()[:200],'stdout_sha256':hashlib.sha256(r.stdout).hexdigest()})
        if not m: wit[opt]=r.stdout
        if (r.returncode!=0)!=bool(m): print('UNEXPECTED',m,opt,r.stderr.decode()); sys.exit(2)
if wit[False]!=wit[True]: print('normal/-O differ'); sys.exit(3)
(HERE/'witness.json').write_bytes(wit[False])
json.dump({'status':'PASS','runs':recs,'wall_s':round(time.time()-t0,3),'caps':'30wall25CPU512MiB'},open(HERE/'replay.json','w'),indent=1,sort_keys=True)
print(json.dumps({'status':'PASS','runs':len(recs),'witness_sha256':hashlib.sha256(wit[False]).hexdigest(),'wall_s':round(time.time()-t0,3)}))
