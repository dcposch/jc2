"""Root terminal pins and bounded replay, no source arithmetic."""
import ast,hashlib,json,resource,shutil,subprocess,sys,tempfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pins={}
for tag,h,n in [
 ('d125-hybrid-affine-code-gate-sol56-20260907','83bd439aa52af686514dcdd6aa4fa400d099abccc8c5d5b5967b208777e47fb4',11),
 ('d125-mixed-order-countercontrol-gate-fable5-20260907','ad1a4ddb11b9f0041042ce81e4e24a3242cc51af46b74b0a8eb5bfef962396a9',9)]:
    r=dict(x.split('=',1) for x in (ROOT/'xmodel'/f'{tag}.run.v2').read_text().splitlines() if '=' in x)
    need(tuple(r[k] for k in ('final_status','exit_code','report_state','seal_boundary','charge_basis_status'))==('DONE','0','BODY_SEALED','CLEAN','ABSENT'),'receipt '+tag)
    need(int(r['charged_inputs'])==n and r['report_sha256']==h,'census/report '+tag)
    for i in range(1,n+1):
        need(r[f'charged_input_{i}_post']=='UNCHANGED','post input')
        pins[r[f'charged_input_{i}']]=r[f'charged_input_{i}_sha256']
    pins[r['report']]=h
READY=ROOT/'box/d125-hybrid-pilot-readiness-20260907'
need(sha(READY/'custody.json')=='f99183f4da520aa045d9f35f439867f769611aaf2d9a1909cb912b77a096a288','readiness custody')
need(sha(READY/'pins.json')=='eb6e3dd282e78f8a4cc99ffc11c3d63867e4dc3dd22982ee2b2350d9b824f718','readiness pins')
pins['xmodel/d125-hybrid-pilot-readiness-astra-20260907.md']='904dc6cd2c9342f7e6091258f1abc8e3ade5e64033b64d490b0e452123039d06'
def verify():
    for p,h in pins.items():need(sha(ROOT/p)==h,'pin '+p)
manifest=json.loads((READY/'pins.json').read_bytes())
for p,h in manifest['owned'].items():pins[str((READY/p).relative_to(ROOT))]=h
pins.update(manifest['frozen_inputs'])
SOL=ROOT/'box/d125-hybrid-affine-code-gate-sol56-20260907/gate_controls.py'
FAB=ROOT/'box/d125-mixed-order-countercontrol-gate-fable5-20260907/gate_controls.py'
pins[str(SOL.relative_to(ROOT))]='b8a5d4c842bc885ee24ac1812f2142cfd2f9d659a3324f3e09da040406624c5c'
pins[str(FAB.relative_to(ROOT))]='aecf4c7686323dc810289feded2261724d344906a574687f9886a08ef6b10bbb'
verify()
records=[];started=time.monotonic()
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
def run(label,optimized,source=None,path=None,mode='',failure=None):
    command=[sys.executable,'-B']+(['-O'] if optimized else [])
    if source is not None:
        command+=['-c',source]
    else:command+=[str(path)]
    if mode:command.append(mode)
    t=time.monotonic();r=subprocess.run(command,capture_output=True,timeout=30,preexec_fn=caps)
    need(r.returncode==0 if failure is None else r.returncode!=0,'exit '+label+': '+r.stderr.decode()[-1000:])
    if failure is not None:need(failure.encode() in r.stderr,'wrong first failure '+label)
    records.append(dict(label=label,optimized=optimized,mutation=mode or None,returncode=r.returncode,wall_seconds=time.monotonic()-t,stdout=r.stdout.decode(),stderr=r.stderr.decode(),adapted_code_sha256=hashlib.sha256(source.encode()).hexdigest() if source is not None else None))
def replace_once(source,old,new):
    need(source.count(old)==1,'replacement not unique: '+old[:70]);return source.replace(old,new)

# Restore the reviewer's removed private snapshot in a new disposable directory.
# Only byte copies of the seven already pinned inputs; no source construction.
with tempfile.TemporaryDirectory(prefix='jc2-root-hybrid-gate-') as td:
    frozen=Path(td)/'inputs';frozen.mkdir();own=Path(td)/'outputs';own.mkdir()
    for name in ('construct.py','replay.py','baseline.py','test_tiny.py','REPLAY-CONTRACT.md','pins.json'):
        shutil.copyfile(ROOT/'box/d125-hybrid-affine-code-prep-20260907'/name,frozen/name)
    shutil.copyfile(ROOT/'xmodel/d125-hybrid-affine-code-prep-astra-20260907.md',frozen/'d125-hybrid-affine-code-prep-astra-20260907.md')
    source=replace_once(SOL.read_text(),"FROZEN = Path('/tmp/jc2-lane.5eg5Cq/inputs')",f'FROZEN = Path({str(frozen)!r})')
    source=replace_once(source,"OWN = Path('/home/ubuntu/jc2/box/d125-hybrid-affine-code-gate-sol56-20260907')",f'OWN = Path({str(own)!r})')
    for optimized in (False,True):run('sol-code-gate-private-path-restoration',optimized,source=source)

# The Fable checker exceeds its declared generator-only scope. Do not execute
# it unmodified. Preserve its frozen bytes and bound actual products to degree 3;
# all unrestricted bracket identities below use independent R=g,S=p toys.
source=FAB.read_text()
source=replace_once(source,'R,U,V,W=(randpoly(3,rng) for _ in range(4));','R=var(3,0); U,V,W=(randpoly(3,rng) for _ in range(3));')
source=replace_once(source,'def check(mode):', '''def lowmul(a,b):
    # Actual g,p support never exceeds degree three, even in intermediate maps.
    r={}
    for e1,c1 in a.items():
        for e2,c2 in b.items():
            e=tuple(x+y for x,y in zip(e1,e2))
            if e[0]+e[1]>3:continue
            v=r.get(e,Q(0))+c1*c2
            if v:r[e]=v
            else:r.pop(e,None)
    return r
def value(P,hv=Q(3)):
    return sum(c*hv**k for (i,j,k),c in P.items())
def check(mode):''')
source=replace_once(source,'RS2=mul(Ra,power(Sa,2))','RS2=lowmul(Ra,lowmul(Sa,Sa))')
source=source.replace('mul(power(Ra,2),Sa)','lowmul(lowmul(Ra,Ra),Sa)')
start=source.index('    # actual F2 at h=3')
end=source.index("    need(add(mul(h,Sa)",start)
source=source[:start]+'''    # Degree<=3 projections check the low slots. The nonproportionality
    # proof cancels nonzero R*S: F2=d R^2 S would force S proportional
    # to R, impossible because their total degrees are 3 and 5.
    for hv in (Q(3),Q(1),Q(-2)):
        ev=lambda P:add(*[{(i,j,0):c*hv**k} for (i,j,k),c in P.items()]) if P else {}
        Rh=ev(Ra); Sh=ev(Sa)
        F2low=add(scale(lowmul(Rh,lowmul(Sh,Sh)),9),scale(lowmul(lowmul(Rh,Rh),Sh),-9/hv))
        need(coef(F2low,(0,1,0))==0 and coef(F2low,(0,3,0))==0 and coef(F2low,(1,2,0))==0,'F2 low slots')
        need(coef(Rh,(0,1,0))==-hv,'[p]R=-h forces c=0')
        need(stats(Rh)[0]==5 and stats(Sh)[0]==3,'distinct generator degrees for nonproportionality')
        need(add(scale(Sh,hv),scale(Rh,-1))==add(scale(power(p,3),3),scale(H,-1)),'hS-R=3p^3-H')
''' +source[end:]
start=source.index('    JRS=bracket(Ra,Sa);')
end=source.index("    out['status']='PASS'",start)
source=source[:start]+'''    need(bracket(power(Rv,2),Sv)==scale(mul(Rv,bracket(Rv,Sv)),2),'independent-toy chain rule')
    val=value(deriv(Ra,0))*value(deriv(Sa,1))-value(deriv(Ra,1))*value(deriv(Sa,0))
    need(val==14,'[R,S](1,1,t=0)!=14')
    need(value(Sa)==1,'S(1,1)!=1')
    out['JRS_at_1_1_t0']='14';out['root_scope']='actual generators/lifts and degree<=3 projected products; independent R=g,S=p toys'
''' +source[end:]
source=f'__file__={str(FAB)!r}\n'+source
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(source))),'adapted Assert')
for optimized in (False,True):
    for mode,failure in [('',None),('--mutate-drop-mixed-orders','bracket nonzero below order seven'),('--mutate-full-arc-claim','finite toy is not a full commuting arc'),('--mutate-guarded-s4-survivor','x=0 cannot meet')]:
        run('fable-mixed-order-root-scope-adapted',optimized,source=source,mode=mode,failure=failure)
for optimized in (False,True):run('readiness-mocked-host',optimized,path=READY/'test_host_control.py')
verify()
result=dict(status='PASS',pins=len(pins),wall_seconds=time.monotonic()-started,runs=records,limitations=['No full source or 803-row construction/replay','Sol path-only restoration into disposable pinned snapshot','Fable frozen checker NOT run unmodified: root scope adaptation above','Readiness is mocked-host only; GAP-AUTH not resolved by tests'],helper_sha256=sha(Path(__file__)))
with (OUT/'0508-harvest.json').open('x') as f:json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps(dict(status='PASS',pins=len(pins),runs=len(records),wall_seconds=result['wall_seconds'],receipt_sha256=sha(OUT/'0508-harvest.json'))))
