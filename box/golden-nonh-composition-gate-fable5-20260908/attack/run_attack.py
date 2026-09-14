import subprocess, json, hashlib, time
argv=['/usr/bin/prlimit','--cpu=25','--as=536870912','--','/usr/bin/python3','-I','-B','/home/ubuntu/jc2/box/golden-nonh-composition-gate-fable5-20260908/attack/attack.py']
t=time.time(); cp=subprocess.run(argv,capture_output=True,timeout=30); dt=time.time()-t
open('/home/ubuntu/jc2/box/golden-nonh-composition-gate-fable5-20260908/attack/attack.out','wb').write(cp.stdout)
open('/home/ubuntu/jc2/box/golden-nonh-composition-gate-fable5-20260908/attack/attack.err','wb').write(cp.stderr)
print(json.dumps({'argv':argv,'rc':cp.returncode,'seconds':round(dt,3),'stdout_sha256':hashlib.sha256(cp.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(cp.stderr).hexdigest(),'stderr_bytes':len(cp.stderr)}))
