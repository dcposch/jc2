"""Root bounded replay of terminal m4 packet; no full A/B expansion."""
import hashlib,json,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
BOX=ROOT/'box/d125-m4-residue-discriminator-20260907'
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
need(sha(BOX/'custody.json')=='2a7b25ddd02308a7b51c461f4a6fc2da44bfa23dd63156a0bb361da410dc9a14','custody drift')
c=json.loads((BOX/'custody.json').read_bytes());need(c['status']=='TERMINAL' and c['all_writers_finished'] and not c['jobs'] and not c['workers'],'not terminal')
pins={p:v['sha256'] for group in ('inputs','owned') for p,v in c[group].items()}
pins['xmodel/d125-m4-residue-discriminator-astra-20260907.md']=c['report']['sha256']
pins['xmodel/d125-m4-residue-discriminator-astra-20260907.md.artifact.json']=c['transaction']['sha256']
def verify():
    for p,h in pins.items():need(sha(ROOT/p)==h,'pin '+p)
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
verify();runs=[];start=time.monotonic()
for name,modes,witness in [
 ('check.py',[('',None),('--mutate-C-basis','complete C ordinary basis'),('--mutate-C-low-row','C_v is a real low constraint'),('--mutate-linear-C-kernel','actual linear C kernel factor'),('--mutate-keep-kernel-despite-e4','e4 kills gamma4')],'witness.json'),
 ('check_jet.py',[('',None),('--mutate-q-negative',('literal D support','actual q negative row')),('--mutate-U4-low','actual U4 low jet'),('--mutate-B6-cross','full six-jet cross coefficient'),('--mutate-b4','actual saturated x square')],'jet-final-witness.json')]:
    for opt in (False,True):
        for mode,failure in modes:
            command=[sys.executable,'-B']+(['-O'] if opt else [])+[str(BOX/name)]+([mode] if mode else [])
            r=subprocess.run(command,capture_output=True,timeout=30,preexec_fn=caps)
            need(r.returncode==0 if failure is None else r.returncode!=0,'exit '+name+mode+': '+r.stderr.decode()[-400:])
            if failure is None:need(hashlib.sha256(r.stdout).hexdigest()==sha(BOX/witness),'witness mismatch')
            else:need(any(x.encode() in r.stderr for x in (failure if isinstance(failure,tuple) else (failure,))),'wrong mutation failure')
            runs.append(dict(script=name,optimized=opt,mutation=mode or None,rc=r.returncode,stdout_sha256=hashlib.sha256(r.stdout).hexdigest(),stderr_tail=r.stderr.decode()[-300:]))
verify();result=dict(status='PASS',pins=len(pins),runs=runs,wall_seconds=time.monotonic()-start,helper_sha256=sha(Path(__file__)),scope='producer literal small factors/linear spaces and R=g formal controls only, no full source expansion')
with (OUT/'m4-harvest.json').open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status='PASS',pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(OUT/'m4-harvest.json'))))
