import sys
sys.dont_write_bytecode=True
from pathlib import Path
import subprocess,json,time,hashlib
B=Path(__file__).resolve().parent;rows=[];start=time.monotonic()
for opt in (False,True):
    for m in ('normal','change-alpha-cross','add-even-kernel','change-G1'):
        a=['/usr/bin/python3','-I','-B']+(['-O'] if opt else [])+[str(B/'check.py'),m]
        p=subprocess.run(a,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=30)
        if (p.returncode==0)!=(m=='normal'):raise RuntimeError((a,p.returncode,p.stderr))
        if m=='normal' and not opt:
            with (B/'witness.json').open('xb') as f:f.write(p.stdout)
        rows.append({'mode':m,'optimized':opt,'returncode':p.returncode,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr':p.stderr.decode()})
o={'status':'PASS','elapsed_seconds':round(time.monotonic()-start,6),'runs':rows}
with (B/'replay.json').open('xb') as f:f.write((json.dumps(o,indent=2,sort_keys=True)+'\n').encode())
print(json.dumps({'status':'PASS','runs':len(rows),'elapsed_seconds':o['elapsed_seconds']}))
