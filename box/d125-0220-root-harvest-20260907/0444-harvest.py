"""Root integration of three terminal packets; no production arithmetic."""
import ast,hashlib,json,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pins={}
for tag,h,n in [
 ('d125-ramified-twojet-gate-fable5-20260907','82ad1c16832a37f87c2c8e245fc0edd983bada9861479a153c20986d6042d974',12),
 ('d125-parity-hybrid-cost-gate-fable5-20260907','bff1b2073c3fb878458de346fa1b3c87ab378ce5b7a5320e3a634b7b7da0950c',13)]:
    r=dict(x.split('=',1) for x in (ROOT/'xmodel'/f'{tag}.run.v2').read_text().splitlines() if '=' in x)
    need(tuple(r[k] for k in ('final_status','exit_code','report_state','seal_boundary','charge_basis_status'))==('DONE','0','BODY_SEALED','CLEAN','ABSENT'),'receipt '+tag)
    need(int(r['charged_inputs'])==n and r['report_sha256']==h,'census/report '+tag)
    for i in range(1,n+1):
        need(r[f'charged_input_{i}_post']=='UNCHANGED','post input')
        pins[r[f'charged_input_{i}']]=r[f'charged_input_{i}_sha256']
    pins[r['report']]=h
GEN=ROOT/'box/d125-generic-ramification-discriminator-20260907'
need(sha(GEN/'custody.json')=='53c56fba1b1d6fa630f5a49fa877f1ac8b0b99f50203f9a6226f4644fd0f2ba8','generic custody')
c=json.loads((GEN/'custody.json').read_bytes())
need(c['status']=='TERMINAL' and c['all_writers_finished'],'generic terminal')
for section in ('owned','inputs'):
    for p,m in c[section].items():pins[p]=m['sha256']
pins['xmodel/d125-generic-ramification-discriminator-astra-20260907.md']='a7b37d6e5c1ce4f72bd3a4c2efa748f17d0ac11d141160b49da1754cc9e5e293'
def verify():
    for p,h in pins.items():need(sha(ROOT/p)==h,'pin '+p)
RBOX=ROOT/'box/d125-ramified-twojet-gate-fable5-20260907'
HBOX=ROOT/'box/d125-parity-hybrid-cost-gate-fable5-20260907'
pins[str((RBOX/'gate_controls.py').relative_to(ROOT))]='973c1242acfca43c281b20adfeb0396f50ead82b3fa1adeff92f144e651bd297'
pins[str((HBOX/'gate_controls.py').relative_to(ROOT))]='9f7e007491bfbc4c14b485cc9c50a2a811dbc8c4dab1d5e78e21354989a5706f'
verify()
if '--pins-only' in sys.argv:
    print(json.dumps(dict(status='PINS_PASS_ONLY',pins=len(pins))));sys.exit(0)
for p in (RBOX/'gate_controls.py',HBOX/'gate_controls.py',GEN/'check.py',ROOT/'box/d125-zero-k-deformation-discriminator-20260907/check.py'):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(p.read_bytes()))),'Assert '+str(p))
# Frozen files remain unchanged. The m2 reviewer exceeded its requested R=g
# toy scope and additionally lifted degree-eight R*Rt. Replace precisely those
# diagnostics in memory; proof uses multiplicativity of the two ordinary lifts.
rsource=(RBOX/'gate_controls.py').read_text()
replacements=[('Rtoy=add(g,power(p,2),mul(g,p));','Rtoy=g;'),
 ('all(e[1]>=0 for e in subst(mul(R,Rt),phig,phip))','all(e[1]>=0 for e in subst(Rt,phig,phip))')]
for old,new in replacements:
    need(rsource.count(old)==1,'named m2 diagnostic target');rsource=rsource.replace(old,new)
hsource=(HBOX/'gate_controls.py').read_text()
old='/tmp/jc2-lane.pPWk5L/inputs/client.py';new=str(ROOT/'box/d125-minimal-receiver-client-preflight-20260906/client.py')
need(hsource.count(old)==1,'exact deleted-private alias');hsource=hsource.replace(old,new)
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
def launch(source,path,flags,mode):
    wrapper='import sys;sys.dont_write_bytecode=True;sys.argv='+repr([str(path)]+([mode] if mode else []))+';exec(compile('+repr(source)+','+repr(str(path))+',"exec"),{"__name__":"__main__","__file__":'+repr(str(path))+'})'
    return subprocess.run([sys.executable,'-B',*flags,'-c',wrapper],capture_output=True,timeout=30,preexec_fn=caps)
start=time.monotonic();runs=[]
configs=[('ramified_scope_repaired',rsource,RBOX/'gate_controls.py',[
 ('',None),('--mutate-cubic-factor','FAIL order-3 identity, cubic 5/27'),
 ('--mutate-omit-negative-row','FAIL phi(D) valuation >= -1 (phi(TD) ordinary)'),
 ('--mutate-independent-tangent','FAIL [p]U1=-c(t+3), [gp^2]U1=c(t+3), d-free'),
 ('--mutate-truncated-saturation','FAIL nilpotent k cannot be canceled')]),
 ('hybrid_metadata_alias',hsource,HBOX/'gate_controls.py',[
 ('',None),('pivot','FIRST_FAILING_GATE sheared slot free but not a pivot'),
 ('face','FIRST_FAILING_GATE B pivots free, off both faces'),
 ('inverse','FIRST_FAILING_GATE literal inverse equals own adjugate'),
 ('mapdegree','FIRST_FAILING_GATE J degree <= 3'),('guard','FIRST_FAILING_GATE guard cofactor r=3')]),
 ('mixed_order_toy',(GEN/'check.py').read_text(),GEN/'check.py',[
 ('',None),('--mutate-drop-mixed-orders','mixed orders are required through order six'),
 ('--mutate-full-arc-claim','finite toy is not a full commuting arc'),
 ('--mutate-guarded-s4-survivor','zero x cannot satisfy saturated k=s4 leading row')])]
for label,source,path,modes in configs:
    for flags in ([],['-O']):
        for mode,error in modes:
            p=launch(source,path,flags,mode)
            need(p.returncode==(1 if error else 0),'exit '+label+' '+mode)
            if error:
                output=(p.stdout+p.stderr).decode();need(error in output,'actual first gate '+label+' '+mode)
            elif label=='ramified_scope_repaired':need(hashlib.sha256(p.stdout).hexdigest()=='3ede3e4e59d2803684a8fdaa73e01839bd5d6fd87a79b81a871ec575a8304d4a','m2 witness')
            elif label=='mixed_order_toy':need(hashlib.sha256(p.stdout).hexdigest()=='24a90700ac30b9af4823891a246287abd9c7826485a7795c3d1dcacda3168de1','mixed witness')
            else:
                v=json.loads(p.stdout);need((v['status'],v['variables'],v['J_universe'],v['optimized'])==('GATE_CONTROLS_PASS',81,1362,bool(flags)),'hybrid witness')
            runs.append(dict(label=label,flags=flags,mode=mode,returncode=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode(),failure_stdout=p.stdout.decode() if error else None))
verify()
result=dict(status='PASS',pins=pins,runs=runs,wall_seconds=time.monotonic()-start,
    m2_scope_replacements=replacements,m2_adapted_code_sha256=hashlib.sha256(rsource.encode()).hexdigest(),
    hybrid_pinned_alias=[old,new],scope='tiny metadata, degree-five generators, R=g toy, degree-three/five independent mixed toy; no actual full pair/source',bytecode_disabled=True)
dest=OUT/'0444-harvest.json'
with dest.open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status='PASS',pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(dest))))
