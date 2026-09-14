"""Terminal gate replay; replace unnecessary face powers by scalar projections."""
import ast, concurrent.futures, csv, datetime, hashlib, io, json, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2'); TAG='d125-finite-boundary-composition-gate-fable5-20260908'
B=ROOT/'box'/TAG; start=time.monotonic()
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
rp=ROOT/'xmodel'/(TAG+'.run.v2')
d=dict(line.split('=',1) for line in rp.read_text().splitlines() if '=' in line)
need(all(d[k]==v for k,v in {'final_status':'DONE','exit_code':'0','seal_boundary':'CLEAN','report_state':'BODY_SEALED','charge_basis_status':'ABSENT'}.items()),'terminal receipt')
pins={str(rp):'ec3169c8169aa7ab56719a865289e969096cc352885beccc08d20626024256c6',str(ROOT/d['report']):d['report_sha256'],str(B/'custody.json'):sha(B/'custody.json')}
for i in range(1,28):pins[str(ROOT/d[f'charged_input_{i}'])]=d[f'charged_input_{i}_sha256']
for e in json.loads((B/'custody.json').read_bytes())['owned']:pins[str(ROOT/e['path'])]=e['sha256']
for p,h in pins.items():need(sha(Path(p))==h,'pin drift '+p)
controls=B/'fable5_composition_controls.py'; scratch=B/'scratch/check.py'
for p in [controls,scratch]:need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(p.read_text()))),'Assert node')
source=controls.read_text()
old1="    c5=pw(Rp,5,n1).get((15,),F(0)); c3=pw(Rp,3,n1).get((15,),F(0)); c1=Rp.get((15,),F(0))"
new1="    from math import comb\n    def pc(n,target):\n        return sum(F(comb(n,r)*(-3)**(n-r)) for r in range(n+1) if 3*n+2*r==target)\n    c5,c3,c1=pc(5,15),pc(3,15),pc(1,15)"
old2="    n2=2; pp=var(0,n2); gg=var(1,n2); A15=mul(pw(pp,6,n2),pw(add(pw(pp,3,n2),pw(gg,3,n2)),3,n2))\n    need(A15.get((15,0))==F(1),'[p^15]A=1 so the entire shear is available')"
new2="    top_p15=sum(F(comb(3,r)) for r in range(4) if 6+3*r==15 and 3*(3-r)==0)\n    need(top_p15==F(1),'[p^15]A=1 so the entire shear is available')"
for old in [old1,old2]:need(source.count(old)==1,'exact projection replacement site')
replacements=[(old1,new1),(old2,new2)]
patched=source
for old,new in replacements:patched=patched.replace(old,new)
need('pw(Rp,5' not in patched and 'A15=mul' not in patched,'high face powers removed')
loader='from pathlib import Path\np='+repr(str(controls))+'\ns=Path(p).read_text()\n'
for old,new in replacements:loader+='s=s.replace('+repr(old)+','+repr(new)+')\n'
loader+="exec(compile(s,p,'exec'),{'__file__':p,'__name__':'__main__'})\n"
cases=[]
for kind,rel in [('producer','replay/replay-individual.tsv'),('reviewer','controls/runs.tsv')]:
    for row in csv.DictReader(io.StringIO((B/rel).read_text()),delimiter='\t'):cases.append((kind,row))
def run(case):
    kind,row=case
    argv=['/usr/bin/prlimit','--cpu=25','--as=536870912','/usr/bin/python3','-I','-B']+(['-O'] if row['optimized']=='-O' else [])
    argv+=(['-c',loader] if kind=='reviewer' else [str(scratch)])
    if row['mutation']!='positive':argv.append(row['mutation'])
    p=subprocess.run(argv,capture_output=True,timeout=30,cwd=ROOT)
    need(p.returncode==int(row['rc']),'exit '+str(case))
    need(hashlib.sha256(p.stdout).hexdigest()==row['stdout_sha256'],'stdout '+str(case))
    need(row['marker'].encode() in p.stderr if row['marker'] else not p.stderr,'failure marker '+str(case))
    return {'kind':kind,'optimized':row['optimized'],'mutation':row['mutation'],'returncode':p.returncode,'stdout_sha256':row['stdout_sha256'],'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:runs=list(pool.map(run,cases))
for p,h in pins.items():need(sha(Path(p))==h,'post drift '+p)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,'replacements':replacements,'loaded_reviewer_sha256':hashlib.sha256(patched.encode()).hexdigest(),'scope':'Root whole report/code and exact primary theorem/proof scope checked;24 bounded normal/O controls. Frozen code unchanged; unnecessary specialized R powers/top face expanded only in reviewer are replaced in root memory by scalar coefficient counts.','corrections':['The producer report remains historically conditional, discharged by separate accepted15f; it is not erroneous frozen wording.', 'Reviewer finite integer check r=-2..2 is not a proof that sqrt(2) is irrational; monic rational-root/integer-square argument supplies that fact.', 'Control A division by its constructed I is not itself an intersection proof; the general saturation argument and principal gcd argument are prose.', 'A discarded incorrect inverse-series trial is overwritten by the correct tau1^n recursion, then both compositions verified.', 'Receipt27 includes input manifest; report26 means other evidence inputs. Actual launcher start00:18:57, model confirmed00:19:06, end00:29:23.']}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
