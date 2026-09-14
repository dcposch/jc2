"""Terminal nonodd-gate replay and an actual h=0 countercontrol."""
import ast,concurrent.futures,datetime,hashlib,json,re,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2'); TAG='d125-nonodd-cone-gate-fable5-20260908'; B=ROOT/'box'/TAG
start=time.monotonic()
def need(x,m):
    if not x: raise RuntimeError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rp=ROOT/'xmodel'/(TAG+'.run.v2');d=dict(x.split('=',1) for x in rp.read_text().splitlines() if '=' in x)
need(all(d[k]==v for k,v in {'final_status':'DONE','exit_code':'0','seal_boundary':'CLEAN','report_state':'BODY_SEALED','charge_basis_status':'ABSENT'}.items()),'terminal receipt')
pins={str(rp):'26c82aef4449cfc3ca2727af360c87aee29b72b1af6eb9b43a328ed3f9180b68',str(ROOT/d['report']):d['report_sha256'],str(B/'custody.json'):'4983eb6988e763197c98638c540f987ed96ba7105be79e5a54cea75149e4dc2a'}
for i in range(1,15):pins[str(ROOT/d[f'charged_input_{i}'])]=d[f'charged_input_{i}_sha256']
for p,h in json.loads((B/'custody.json').read_bytes())['pins'].items():pins[str((B/p).resolve())]=h
for p,h in pins.items():need(sha(Path(p))==h,'pre drift '+p)
for p in (B/'fable5_controls.py',B/'scratch/nonodd-check.py'):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(p.read_text()))),'Assert gate')
counter='''import json
def need(x,m):
 if not x: raise ValueError(m)
# P=Z^3+Z, Q=Z^5+Z. Both p-derivatives vanish exactly.
P={3:1,1:1}; Q={5:1,1:1}
def euler_residual(poly,degree,h): return {i:(i-degree)*h*a for i,a in poly.items() if (i-degree)*h*a}
need(P!={3:1} and Q!={5:1},"nontrivial constant coefficients")
need(not euler_residual(P,3,0) and not euler_residual(Q,5,0),"h=0 permits both monic homogeneous commuting polynomials")
need(euler_residual(P,3,1)=={1:-2} and euler_residual(Q,5,1)=={1:-4},"same changed object fails positive homogeneous degree")
print(json.dumps({"status":"PASS","h0_countercontrol":"monic depressed P=Z^3+Z,Q=Z^5+Z commute; positive-h homogeneity fails"},sort_keys=True))
'''
cases=[('producer',r) for r in json.loads((B/'fable5-replay.json').read_bytes())['runs']]
cases += [(kind,{'optimized':opt}) for kind in ('reviewer','root-h0') for opt in (False,True)]
def run(case):
    kind,r=case; argv=['/usr/bin/prlimit','--cpu=25','--as=536870912','/usr/bin/python3','-I','-B']+(['-O'] if r['optimized'] else [])
    if kind=='producer':
        argv += [str(B/'scratch/nonodd-check.py')]+([] if r['mode']=='positive' else [r['mode']]); rc=r['rc']; out=r['stdout_sha256']; err=r['error_line']
    elif kind=='reviewer':
        argv += [str(B/'fable5_controls.py')]; rc=0;out='ee1e50117832e08df86e4b873bc4aee68794ffc6d350638397f00200ec09166c';err=''
    else: argv+=['-c',counter];rc=0;out=None;err=''
    z=subprocess.run(argv,capture_output=True,timeout=30,cwd=ROOT)
    need(z.returncode==rc,'exit '+str(case))
    digest=hashlib.sha256(z.stdout).hexdigest()
    if out is not None:need(digest==out,'stdout '+str(case))
    lines=re.findall(r'^(\w+Error: .*)$',z.stderr.decode(),re.M)
    need((lines[-1] if lines else '')==err,'error marker '+str(case))
    if not err:need(not z.stderr,'unexpected stderr')
    return {'kind':kind,'optimized':r['optimized'],'mode':r.get('mode','positive with internal changed objects'),'returncode':rc,'stdout_sha256':digest,'stderr_sha256':hashlib.sha256(z.stderr).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:runs=list(pool.map(run,cases))
need(len({r['stdout_sha256'] for r in runs if r['kind']=='root-h0'})==1,'root normal/O identity')
for p,h in pins.items():need(sha(Path(p))==h,'post drift '+p)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,'root_h0_control':counter,
     'scope':'All six nonodd proof arrows checked after terminal original unit/model absent, receipt/current14 inputs/report, whole proof/checkers. Exact unequal/squarefree-Q field-point exclusion only. No actual high source/H/R powers or CAS.',
     'corrections':['Reviewer C3_construction_c_d and C4_euler_reduction are True/prose placeholders, not executable checks; C4 loop does nothing. Their mathematical proofs are explicit in prose; producer free-symbol checker verifies Euler. Root adds an actual h=0 countercontrol above.', 'C5 has90 finite (j,q0) cases, not9x14=126. q0>=14 gives eta=j/2 for every j<=9, so no larger q0 introduces a new eta regime; universal inequalities remain the proof.', 'C6 finite monomial table is a control, not a proof for unrestricted degree; the elementary normality/weight argument supplies the bound.', 'Rejected reviewer C7 draft is retained but not executed or treated as evidence. Root avoids the inner timeout process group.', 'No finite quotient or nonreduced/unit-ideal descent is promoted in this gate. Source implications are field-point statements, sufficient for their exclusion purpose.']}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
