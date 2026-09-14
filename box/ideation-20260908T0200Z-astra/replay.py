import sys
sys.dont_write_bytecode=True
from pathlib import Path
import subprocess,json,hashlib,time
B=Path(__file__).resolve().parent; rows=[];start=time.monotonic()
for opt in (False,True):
    for mode in ('normal','change-ribbon','thicken-ribbon','change-golden-pivot'):
        c=['/usr/bin/python3','-I','-B']+(['-O'] if opt else [])+[str(B/'check.py'),mode]
        p=subprocess.run(c,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
        if (p.returncode==0)!=(mode=='normal'):raise RuntimeError((c,p.returncode,p.stderr))
        if mode=='normal' and not opt:
            with (B/'witness.json').open('xb') as f:f.write(p.stdout)
        rows.append({'mode':mode,'optimized':opt,'returncode':p.returncode,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr':p.stderr.decode()})
out={'status':'PASS','elapsed_seconds':round(time.monotonic()-start,6),'runs':rows}
with (B/'replay.json').open('xb') as f:f.write((json.dumps(out,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps({'status':'PASS','runs':len(rows),'elapsed_seconds':out['elapsed_seconds']}))
