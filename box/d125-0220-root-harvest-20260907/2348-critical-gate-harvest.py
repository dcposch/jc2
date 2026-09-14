"""Four bounded independent reviewer controls, fixed inputs and exact stdout."""
import ast,concurrent.futures,datetime,hashlib,json,subprocess,time
from pathlib import Path
R=Path('/home/ubuntu/jc2'); tag='d125-pure-critical-remainder-gate-fable5-20260907'
B=R/'box'/tag; C=B/'controls'; start=time.monotonic()
def need(c,m):
    if not c:raise RuntimeError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
d=dict(s.split('=',1) for s in (R/'xmodel'/f'{tag}.run.v2').read_text().splitlines() if '=' in s)
need(all(d[k]==v for k,v in {'final_status':'DONE','exit_code':'0','seal_boundary':'CLEAN','report_state':'BODY_SEALED','charge_basis_status':'ABSENT'}.items()),'terminal receipt')
need(sha(B/'custody.json')=='c061de59531535fced060fa6dc6948eac82b29a747ba52da239b7500a71f62bd','custody')
byname={Path(d[f'charged_input_{i}']).name:R/d[f'charged_input_{i}'] for i in range(1,15)}
pins={}
for row in json.loads((B/'custody.json').read_bytes())['entries']:
    p=byname[Path(row['path']).name] if row['role']=='input' else Path(row['path'])
    pins[str(p)]=row['sha256']
for p,h in pins.items():need(sha(Path(p))==h,'pin drift '+p)
for p in C.glob('*_control.py'):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(p.read_text()))),'Assert node')
cases=[]
for line in (C/'runs.tsv').read_text().splitlines():
    name,*fields=line.split('\t'); rec=dict(x.split('=',1) for x in fields)
    base=next(s for s in ['chain_rule_control','valuation_control','recursion_point_control','weight_lemma_control'] if name.startswith(s))
    cases.append((name,base,rec))
def run(case):
    name,base,ref=case; before=time.monotonic()
    argv=['/usr/bin/prlimit','--cpu=25','--as=536870912','/usr/bin/python3','-I','-B']+(['-O'] if ref['opt']=='-O' else [])+[str(C/(base+'.py'))]+([] if ref['mode']=='positive' else [ref['mode']])
    p=subprocess.run(argv,capture_output=True,timeout=30)
    need(p.returncode==int(ref['rc']),'returncode '+name)
    need(p.stdout==(C/'out'/(name+'.stdout')).read_bytes(),'exact stdout '+name)
    need(not ref['msg'] or ref['msg'].encode() in p.stderr,'failure marker '+name)
    need(ref['msg'] or not p.stderr,'unexpected stderr '+name)
    return {'name':name,'argv':argv,'returncode':p.returncode,'seconds':time.monotonic()-before,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:runs=list(pool.map(run,cases))
for p,h in pins.items():need(sha(Path(p))==h,'post drift '+p)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,'scope':'Reviewer finite coefficient-space controls and degree-five factors/formal moving toy only; no actual A15/B25 or high R powers/full source.','corrections':['Arrow4 exact order a+v belongs to the isolated first summand, not necessarily the entire left side; the displayed bound follows by isolation.','Arrow5 middle equality to D(-5*kappa^3/(27p)) has a sign typo; the resulting primitive const-5*kappa^3/(27p) is correct.','ControlC represents infinity by finite sentinel10^9 in a bounded box; the universal infinity cases are proved in prose.']}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
