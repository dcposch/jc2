import sys
sys.dont_write_bytecode = True
import pathlib, subprocess, json, hashlib, time
root=pathlib.Path(__file__).resolve().parent
rows=[]
start=time.monotonic()
for opt in (False,True):
    for mode in ('normal','wrong-shift','omit-lower-slot','drop-mu'):
        cmd=['/usr/bin/python3','-I','-B']+(['-O'] if opt else [])+[str(root/'check.py'),mode]
        r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
        good=(r.returncode==0)==(mode=='normal')
        if not good:
            raise RuntimeError((cmd,r.returncode,r.stderr.decode()))
        if mode=='normal' and not opt:
            with (root/'witness.json').open('xb') as f: f.write(r.stdout)
        rows.append({'optimized':opt,'mode':mode,'returncode':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr':r.stderr.decode()})
result={'status':'PASS','runs':rows,'elapsed_seconds':round(time.monotonic()-start,6),'all_writers_idle':True}
with (root/'replay.json').open('xb') as f:f.write((json.dumps(result,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps({'status':'PASS','runs':len(rows),'elapsed_seconds':result['elapsed_seconds']}))
