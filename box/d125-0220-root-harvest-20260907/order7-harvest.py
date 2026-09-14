"""Root receipt-first bounded replay of terminal order-seven packet."""
import hashlib,json,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
BOX=ROOT/'box/d125-m4-order7-discriminator-20260907'
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
need(sha(BOX/'custody.json')=='f33ecc3cf2337160de878a63222fa1410aeaa1a5938f6b2886dcad3f721f12f0','custody drift')
c=json.loads((BOX/'custody.json').read_bytes());need(c['status']=='TERMINAL' and c['all_writers_finished'] and not c['jobs'] and not c['workers'],'not terminal')
pins={p:v['sha256'] for group in ('inputs','owned') for p,v in c[group].items()}
pins['xmodel/d125-m4-order7-discriminator-astra-20260907.md']=c['report']['sha256']
pins['xmodel/d125-m4-order7-discriminator-astra-20260907.md.artifact.json']=c['transaction']['sha256']
def verify():
    for p,h in pins.items():need(sha(ROOT/p)==h,'pin '+p)
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
verify();runs=[];start=time.monotonic()
for opt in (False,True):
    for mode,failure in [('',None),('--mutate-omit-moving-derivative','actual moving-reference order-seven identity'),('--mutate-double-factor','actual moving-reference order-seven identity'),('--mutate-even-kernel','even double-pole kernel is forbidden'),('--mutate-point-relation','point must lie on literal T=0')]:
        r=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(BOX/'check.py')]+([mode] if mode else []),capture_output=True,timeout=30,preexec_fn=caps)
        need(r.returncode==0 if failure is None else r.returncode!=0,'exit '+mode+': '+r.stderr.decode()[-400:])
        if failure is None:need(hashlib.sha256(r.stdout).hexdigest()==sha(BOX/'witness.json'),'witness mismatch')
        else:need(failure.encode() in r.stderr,'wrong first failure')
        runs.append(dict(optimized=opt,mutation=mode or None,rc=r.returncode,stdout_sha256=hashlib.sha256(r.stdout).hexdigest(),stderr_tail=r.stderr.decode()[-300:]))
verify();result=dict(status='PASS',pins=len(pins),runs=runs,wall_seconds=time.monotonic()-start,helper_sha256=sha(Path(__file__)),scope='small formal moving-reference identities and finite unit certificate; not whole source or general theorem verification')
with (OUT/'order7-harvest.json').open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status='PASS',pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(OUT/'order7-harvest.json'))))
