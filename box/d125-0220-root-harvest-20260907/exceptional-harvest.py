"""Terminal exceptional report and bounded current-code controls only."""
import sys
sys.dont_write_bytecode=True
import hashlib,json,resource,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');B=ROOT/'box/d125-exceptional-center-discriminator-20260907'
def need(x,s):
    if not x:raise ValueError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
need(sha(B/'custody.json')=='2661993221783a58c45e936a6ec6707e4e6c423a354234836008a5fbe8ec7480','custody pin')
c=json.loads((B/'custody.json').read_bytes());need(c['status']=='TERMINAL' and c['all_writers_finished'] and not c['live_jobs'],'terminal scope')
pins={r['path']:r['sha256'] for r in c['inputs']+c['owned']}
for p,h in pins.items():need(sha(ROOT/p)==h,'prepin '+p)
r=subprocess.run([sys.executable,'-B','ops/artifact_finalize.py','verify','--final','xmodel/d125-exceptional-center-discriminator-astra-20260907.md'],cwd=ROOT,capture_output=True,timeout=10);need(r.returncode==0,'transaction')
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
t=time.monotonic();runs=[]
for opt in ([],['-O']):
    for mode,msg in [('',None),('--mutate-delta-sign','exact scalar remainder'),('--mutate-omit-lift-row','both actual U lift rows'),('--mutate-omit-low-A','actual alpha-unit low-A'),('--mutate-omit-low-B','actual gamma-unit low-B'),('--mutate-tangent','actual full first-order bracket')]:
        p=subprocess.run([sys.executable,'-B']+opt+[str(B/'check.py')]+([mode] if mode else []),capture_output=True,cwd=ROOT,timeout=30,preexec_fn=caps)
        need((p.returncode!=0)==bool(msg),'exit '+mode)
        if msg:need(msg.encode() in p.stderr,'wrong first gate')
        else:need(hashlib.sha256(p.stdout).hexdigest()=='ccf4b97501b337ef02bd1d6d5733dc47f004b513af90a312819779297e395145','witness')
        runs.append(dict(optimized=bool(opt),mutation=mode or None,rc=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
for p,h in pins.items():need(sha(ROOT/p)==h,'postpin '+p)
dest=ROOT/'box/d125-0220-root-harvest-20260907/exceptional-harvest.json'
out=dict(status='PASS_EXCEPTIONAL_DESK_PROVISIONAL',pins=len(pins),runs=runs,wall_seconds=time.monotonic()-t,scope='finite h=0 arcs require delta=0; no tuned-stratum exclusion/degeneration/guarded point')
with dest.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),wall_seconds=out['wall_seconds'],receipt_sha256=sha(dest))))
