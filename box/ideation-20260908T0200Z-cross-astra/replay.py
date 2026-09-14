import sys
sys.dont_write_bytecode=True
from pathlib import Path
import subprocess,json,hashlib,time
B=Path(__file__).resolve().parent;start=time.monotonic();rows=[]
for opt in (False,True):
    for m in ('normal','change-cubic-face','change-quadratic-face','change-D','change-target'):
        args=['/usr/bin/python3','-I','-B']+(['-O'] if opt else [])+[str(B/'check.py'),m]
        p=subprocess.run(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
        if (p.returncode==0)!=(m=='normal'):raise RuntimeError((args,p.returncode,p.stderr))
        if m=='normal' and not opt:
            with (B/'witness.json').open('xb') as f:f.write(p.stdout)
        rows.append({'mode':m,'optimized':opt,'returncode':p.returncode,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr':p.stderr.decode()})
out={'status':'PASS','elapsed_seconds':round(time.monotonic()-start,6),'runs':rows}
with (B/'replay.json').open('xb') as f:f.write((json.dumps(out,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps({'status':'PASS','runs':len(rows),'elapsed_seconds':out['elapsed_seconds']}))
