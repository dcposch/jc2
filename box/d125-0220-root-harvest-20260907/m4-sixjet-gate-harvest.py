"""Root finite-sixjet gate harvest with one explicit no-face-expansion repair."""
import hashlib,json,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
TAG='d125-m4-sixjet-gate-fable5-v2-20260907';BOX=ROOT/'box'/TAG
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r=dict(x.split('=',1) for x in (ROOT/'xmodel'/f'{TAG}.run.v2').read_text().splitlines() if '=' in x)
need(tuple(r[k] for k in ('final_status','exit_code','report_state','seal_boundary','charge_basis_status'))==('DONE','0','BODY_SEALED_AFTER_DIVERT','DIVERTED','ABSENT'),'receipt')
need(int(r['charged_inputs'])==7,'input census')
pins={r['report']:'3ec2125b485277787035f5d922287fed07a6af019e7cd4af4c0c675f370e7bb3',r['raw_report']:r['raw_report_sha256'],r['overflow']:r['overflow_sha256']}
for i in range(1,8):
    need(r[f'charged_input_{i}_post']=='UNCHANGED','post input');pins[r[f'charged_input_{i}']]=r[f'charged_input_{i}_sha256']
code=BOX/'gate_controls.py';pins[str(code.relative_to(ROOT))]='58d4906856333eb5ddc5d33933bd808ad1e064b41c9a95405615171abe15cef7'
def verify():
    for p,h in pins.items():need(sha(ROOT/p)==h,'pin '+p)
verify()
source=code.read_text()
old="    H=add(M(0,5),M(3,2)); H3=pw(H,3); H5=pw(H,5)\n    gate('H^3/H^5 outer-face zero count 6/10', 10-len(H3)==6 and 16-len(H5)==10)"
new="    # Root scope repair: binomial face has r+1 distinct nonzero slots in characteristic zero; no H^3/H^5 expansion.\n    gate('H^3/H^5 outer-face zero count 6/10', 10-len(range(4))==6 and 16-len(range(6))==10)"
need(source.count(old)==1,'unique face repair');source=f'__file__={str(code)!r}\n'+source.replace(old,new)
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
start=time.monotonic();runs=[]
for opt in (False,True):
    for mode,failure in [('',None),('--mutate-q','phi(q) complete negative part = v^-1'),('--mutate-U4','U4 low jet == g^2 p exactly'),('--mutate-CU','displayed B table == (1+eps)^(5/3) through s^6'),('--mutate-b4','([gp]C)^2=b^4=3')]:
        p=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+['-c',source]+([mode] if mode else []),capture_output=True,timeout=30,preexec_fn=caps)
        need(p.returncode==0 if failure is None else p.returncode!=0,'exit '+mode+': '+p.stderr.decode()[-400:])
        if failure is None:need(hashlib.sha256(p.stdout).hexdigest()=='dc29df2cd4756f0fb9d8e71df24d91ae85e7aacf39201286c997bc1d428bdc68','positive witness')
        else:need(failure.encode() in p.stderr,'wrong first failure')
        runs.append(dict(optimized=opt,mutation=mode or None,rc=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
verify();result=dict(status='PASS_SCOPED_FINITE_SIXJET',pins=len(pins),runs=runs,wall_seconds=time.monotonic()-start,adapted_code_sha256=hashlib.sha256(source.encode()).hexdigest(),helper_sha256=sha(Path(__file__)),corrections=['Unmodified frozen checker NOT executed: literal H3/H5 expansion replaced by binomial slot count','Reviewer O(s8) equality must read O(s7); only coefficients through6 checked','DIVERTED overflow is the read seal/artifact listing only, no extra mathematical claim','General residue necessity and linear-space census not promoted by this gate'])
with (OUT/'m4-sixjet-gate-harvest.json').open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=result['status'],pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(OUT/'m4-sixjet-gate-harvest.json'))))
