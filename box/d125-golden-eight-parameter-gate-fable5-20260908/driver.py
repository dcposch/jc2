import sys
sys.dont_write_bytecode=True
import subprocess,hashlib,json,time,os
d=os.path.dirname(os.path.abspath(__file__))
modes=('normal','wrong-t','drop-M-square','wrong-59','zero-gp-target','wrong-U-shift','wrong-c')
runs=[];t0=time.time()
for opt in (False,True):
    for m in modes:
        cmd=['/usr/bin/python3','-I','-B']+(['-O'] if opt else [])+[os.path.join(d,'control.py'),m]
        r=subprocess.run(cmd,capture_output=True,timeout=30)
        runs.append({'mode':m,'optimized':opt,'rc':r.returncode,'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_tail':r.stderr.decode()[-120:].strip()})
ok=all((r['rc']==0)==(r['mode']=='normal') for r in runs)
json.dump({'status':'PASS' if ok else 'FAIL','elapsed_seconds':round(time.time()-t0,3),'runs':runs},open(os.path.join(d,'replay.json'),'w'),indent=1,sort_keys=True)
print(json.dumps({'status':'PASS' if ok else 'FAIL','n':len(runs),'elapsed':round(time.time()-t0,3)}))
for r in runs:print(r['mode'],r['optimized'],r['rc'],r['stdout_sha256'][:12],r['stderr_tail'][-80:])
