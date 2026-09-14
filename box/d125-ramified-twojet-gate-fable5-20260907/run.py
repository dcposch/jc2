#!/usr/bin/env python3
import subprocess,sys,hashlib,json,resource,ast,time
from pathlib import Path
HERE=Path(__file__).resolve().parent; S=HERE/'gate_controls.py'
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,)*2)
assert_nodes=sum(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(S.read_text())))
modes=[('',None),('--mutate-cubic-factor',b'order-3 identity'),('--mutate-omit-negative-row',b'phi(D) valuation'),
       ('--mutate-independent-tangent',b'[p]U1=-c(t+3)'),('--mutate-truncated-saturation',b'nilpotent k cannot be canceled')]
recs=[]; wit={}
t0=time.time()
for opt in (False,True):
    for m,msg in modes:
        cmd=[sys.executable,'-B']+(['-O'] if opt else [])+[str(S)]+([m] if m else [])
        r=subprocess.run(cmd,capture_output=True,timeout=30,preexec_fn=caps,env={'PYTHONDONTWRITEBYTECODE':'1'})
        ok=(r.returncode!=0)==bool(m) and (msg is None or msg in r.stderr)
        recs.append({'optimized':opt,'mutation':m or None,'rc':r.returncode,'first_fail':r.stderr.decode().strip(),'expected_ok':ok,
                     'stdout_sha256':hashlib.sha256(r.stdout).hexdigest()})
        if not m: wit[opt]=r.stdout
out={'status':'PASS' if all(x['expected_ok'] for x in recs) and wit[False]==wit[True] and assert_nodes==0 else 'FAIL',
     'assert_nodes':assert_nodes,'runs':recs,'witness_sha256':hashlib.sha256(wit[False]).hexdigest(),'wall_s':round(time.time()-t0,2),
     'caps':'30 wall / 25 CPU s / 512 MiB','controls_sha256':hashlib.sha256(S.read_bytes()).hexdigest()}
(HERE/'witness.json').write_bytes(wit[False]); (HERE/'replay.json').write_text(json.dumps(out,indent=1)+'\n')
print(json.dumps({k:out[k] for k in ('status','assert_nodes','witness_sha256','wall_s','controls_sha256')}))
for x in recs: print(x['optimized'],x['mutation'],x['rc'],x['expected_ok'],x['first_fail'][:60])
