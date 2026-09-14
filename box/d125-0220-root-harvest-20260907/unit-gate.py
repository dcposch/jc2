"""Root replay of terminal independent normalization gate, two tiny jobs/batch."""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import subprocess
import sys
import time
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
TAG='d125-parity-unit-normalization-gate-fable5-20260907'
S=ROOT/'box'/TAG
def need(ok,why):
    if not ok: raise ValueError(why)
def sha(data): return hashlib.sha256(data).hexdigest()
r=dict(line.split('=',1) for line in (ROOT/'xmodel'/f'{TAG}.run.v2').read_text().splitlines() if '=' in line)
for k,v in {'final_status':'DONE','exit_code':'0','seal_boundary':'CLEAN','report_state':'BODY_SEALED','charge_basis_status':'ABSENT'}.items():
    need(r[k]==v,'terminal '+k)
pins={r['report']:r['report_sha256']}
for i in range(1,8):
    k=f'charged_input_{i}';need(r[k+'_post']=='UNCHANGED','post pin')
    pins[r[k]]=r[k+'_sha256']
for name,digest in {
    'gate_controls.py':'d123d57bd13fa8790fd4154a6c32e4d39db84ec4b2e5eafb65e3a04c74125f50',
    'replay.json':'df885b1a6abadec684bf7145560bc7515e04fc360e71f61feae4394dbc6c13fe',
    'witness.json':'0dc1e2b824aafb88e0736d30351bbc5b33678d68b59050205bb386d31573d63e',
    'witness-O.json':'0dc1e2b824aafb88e0736d30351bbc5b33678d68b59050205bb386d31573d63e'}.items():
    pins[str((S/name).relative_to(ROOT))]=digest
def verify():
    for name,pin in pins.items():need(sha((ROOT/name).read_bytes())==pin,'pin '+name)
verify()
for path in (S/'gate_controls.py',ROOT/'box/d125-minimal-receiver-client-preflight-20260906/client.py',Path(__file__)):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(path.read_bytes()))),'Assert')
if len(sys.argv)>1 and sys.argv[1]=='--child':
    spec=importlib.util.spec_from_file_location('unit_gate',S/'gate_controls.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    m.CLIENT=ROOT/'box/d125-minimal-receiver-client-preflight-20260906/client.py'
    print(json.dumps(m.run(sys.argv[2]),sort_keys=True,indent=1))
    verify();raise SystemExit(0)
def cap():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
start=time.monotonic();runs=[]
messages={'--mutate-unchanged-face':b'moved faces k,5k/3,5k^2/9','--mutate-c-power':b'c target power',
          '--mutate-omit-guard':b'k=0 must fail','--mutate-parity':b'parity violation'}
for mutation in ('',*messages):
    jobs=[]
    try:
        for flags in ([],['-O']):
            p=subprocess.Popen([sys.executable,'-I','-B',*flags,str(Path(__file__).resolve()),'--child',mutation],
                               stdout=subprocess.PIPE,stderr=subprocess.PIPE,preexec_fn=cap)
            jobs.append((flags,p,time.monotonic()))
        for flags,p,began in jobs:
            stdout,stderr=p.communicate(timeout=max(.1,30-(time.monotonic()-began)))
            need(p.returncode==(1 if mutation else 0),'expected exit')
            if mutation:need(messages[mutation] in stderr and not stdout,'mutation reason')
            else:need(not stderr and sha(stdout)=='0dc1e2b824aafb88e0736d30351bbc5b33678d68b59050205bb386d31573d63e','witness')
            runs.append({'flags':flags,'mutation':mutation,'returncode':p.returncode,'stdout_sha256':sha(stdout),
                         'stderr_sha256':sha(stderr),'wall_seconds':time.monotonic()-began})
    finally:
        for flags,p,began in jobs:
            if p.poll() is None:p.kill()
            p.communicate()
verify()
result={'status':'PASS','pins':pins,'runs':runs,'wall_seconds':time.monotonic()-start,'assert_nodes':0,
        'scope':'independent tiny nilpotent moving-face/row transport controls; no full client or nonemptiness'}
with (OUT/'unit-gate.json').open('x') as f:
    json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'wall_seconds':result['wall_seconds'],
                  'receipt_sha256':sha((OUT/'unit-gate.json').read_bytes())}))
