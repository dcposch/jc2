import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
root=Path('/home/ubuntu/jc2')
box=Path(__file__).resolve().parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def need(ok,message):
    if not ok:raise ValueError(message)
pins={
 'xmodel/golden-two-regime-initial-discriminator-astra-20260908.md':'14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6',
 'xmodel/golden-two-regime-initial-discriminator-astra-20260908.md.artifact.json':'a80659d8c6b38fd4800b7eb70b650af57a0065e0c67b077f2878c1c24377c8af',
 'box/golden-two-regime-initial-discriminator-20260908/custody.json':'fcc12304ee659dc5b83eb8f5e323a8c38a7cf3616e6a4b2f4b53cd1ca438568d'}
for item in json.loads((root/'box/golden-two-regime-initial-discriminator-20260908/custody.json').read_text())['entries']:
    pins[item['path']]=item['sha256']
pins[str((box/'check.py').relative_to(root))]=digest(box/'check.py')
pins[str(Path(__file__).relative_to(root))]=digest(Path(__file__))
for path,h in pins.items():need(digest(root/path)==h,'input drift '+path)
errors={'positive':'','wrong-quintic-factor':'Y10 coefficient cancellation fixes quintic factor','wrong-face-sign':'source c=-5lambda cubed*t/9','wrong-target-factor':'Morse target denominator t squared*a','drop-resonant-target':'resonant initial bracket equals source target order36'}
runs=[];start=time.monotonic()
for opt in (False,True):
    for mode,error in errors.items():
        argv=['/usr/bin/prlimit','--cpu=25:25','--as=536870912:536870912','--','/usr/bin/python3','-I','-B']+(['-O'] if opt else [])+[str(box/'check.py'),mode]
        r=subprocess.run(argv,capture_output=True,timeout=30)
        need(r.returncode==(0 if mode=='positive' else 1),'returncode '+mode)
        stderr=r.stderr.decode()
        need((not stderr) if not error else stderr.rstrip().endswith('ValueError: '+error),'error '+mode)
        if mode=='positive':need(json.loads(r.stdout)['status']=='PASS','positive')
        runs.append({'argv':argv,'rc':r.returncode,'stdout':r.stdout.decode(),'stderr':stderr,'stdout_sha256':hashlib.sha256(r.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(r.stderr).hexdigest()})
for path,h in pins.items():need(digest(root/path)==h,'post drift '+path)
report={'status':'PASS','utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'pins':pins,'runs':runs,'scope':'three algebraic coefficient/sign mutations plus one false resonance-order inference, not full source verification'}
with (box/'replay.json').open('x') as f:json.dump(report,f,indent=2,sort_keys=True)
print(json.dumps({'status':'PASS','runs':len(runs),'pins':len(pins),'seconds':report['elapsed_seconds'],'checker_sha256':digest(box/'check.py'),'replay_sha256':digest(box/'replay.json')}))
