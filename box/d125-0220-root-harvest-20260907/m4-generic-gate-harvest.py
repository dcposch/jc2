"""Root terminal generic-m4 review replay; no full source arithmetic."""
import hashlib,json,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
TAG='d125-m4-generic-order7-gate-fable5-20260907';BOX=ROOT/'box'/TAG
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r=dict(x.split('=',1) for x in (ROOT/'xmodel'/f'{TAG}.run.v2').read_text().splitlines() if '=' in x)
need(tuple(r[k] for k in ('final_status','exit_code','report_state','seal_boundary','charge_basis_status'))==('DONE','0','BODY_SEALED_AFTER_DIVERT','DIVERTED','ABSENT'),'receipt')
need(int(r['charged_inputs'])==9,'input census')
pins={r['report']:'facf4906db69369c33b4ecfb548db13a973af9a999ba8663a9fd77a724102aa4',r['raw_report']:r['raw_report_sha256'],r['overflow']:r['overflow_sha256']}
for i in range(1,10):
    need(r[f'charged_input_{i}_post']=='UNCHANGED','post input');pins[r[f'charged_input_{i}']]=r[f'charged_input_{i}_sha256']
code=BOX/'gate_controls.py';pins[str(code.relative_to(ROOT))]='67aa3c2b5ac710838c8803dce16b8957aa65173d7cfe1130b4d5cd26d5af4ccf'
def verify():
    for p,h in pins.items():need(sha(ROOT/p)==h,'pin '+p)
verify()
# Reviewer's no-odd-weight2 test is vacuous (already assumes total degree2
# and odd parity). Supply the actual full bounded A support check, and the
# elementary universal identity w-(i+j)=4i-8j, so their parities agree.
slots=[(i,j) for i in range(14) for j in range(14-i) if (i+j)%2]
need(all((5*i-7*j)-(i+j)==4*i-8*j and (5*i-7*j)%2==1 and 5*i-7*j!=2 for i,j in slots),'actual odd weight parity')
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
start=time.monotonic();runs=[]
for opt in (False,True):
    for mode,failure in [('',None),('--mutate-omit-moving-derivative','order-seven moving-reference bracket identity'),('--mutate-double-factor','order-seven moving-reference bracket identity'),('--mutate-drop-gamma6-R1','order-seven moving-reference bracket identity'),('--mutate-even-kernel','odd kernel with pole<=2'),('--mutate-point-relation','point (0,a) lies on T=0'),('--mutate-h-zero','e_1..e_5=0 force gamma_1..gamma_5=0')]:
        p=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(code)]+([mode] if mode else []),capture_output=True,timeout=30,preexec_fn=caps)
        need(p.returncode==0 if failure is None else p.returncode!=0,'exit '+mode+': '+p.stderr.decode()[-400:])
        if failure is None:need(hashlib.sha256(p.stdout).hexdigest()=='52f39f9d1c6993c9a686eb6d37e71c59a7eff3bfb7fe21ff28e1b4944d318c4f','positive witness')
        else:need(failure.encode() in p.stderr,'wrong first failure')
        runs.append(dict(optimized=opt,mutation=mode or None,rc=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
verify();result=dict(status='PASS_GENERIC_M4_GATE',pins=len(pins),runs=runs,wall_seconds=time.monotonic()-start,helper_sha256=sha(Path(__file__)),corrections=['Select a=0 using e1 before invoking the first-tangent form','Vacuous reviewer parity check supplemented by actual support and universal parity identity','DIVERTED overflow read: seal only, no additional mathematical claim'],scope='generic finite k=s4 and explicitly saturated seven-jets only; no allm/exception/infinity/guarded emptiness')
with (OUT/'m4-generic-gate-harvest.json').open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=result['status'],pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(OUT/'m4-generic-gate-harvest.json'))))
