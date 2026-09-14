"""Terminal custody; scoped independent single-coefficient replay, no full source."""
from pathlib import Path
import hashlib,json,subprocess,datetime,time
R=Path('/home/ubuntu/jc2'); start=time.monotonic();pins={}
def need(c,m):
    if not c:raise RuntimeError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
tag='d125-nonnegative-grading-gate-fable5-20260907';B=R/'box'/tag
d=dict(s.split('=',1) for s in (R/'xmodel'/f'{tag}.run.v2').read_text().splitlines() if '=' in s)
need(all(d[k]==v for k,v in {'final_status':'DONE','exit_code':'0','seal_boundary':'CLEAN','report_state':'BODY_SEALED','charge_basis_status':'ABSENT'}.items()),'receipt')
for i in range(1,11):
    need(d[f'charged_input_{i}_post']=='UNCHANGED','post')
    pins[d[f'charged_input_{i}']]=d[f'charged_input_{i}_sha256']
pins[d['report']]=d['report_sha256']
for row in json.loads((B/'custody.json').read_bytes())['owned']:pins[row['path']]=row['sha256']
T=R/'box/furter-transition-typing-20260907';c=json.loads((T/'input-pins.json').read_bytes())
pins.update(c['files']);pins.update(c['derived_outputs'])
for n,h in pins.items():need(sha(R/n)==h,'pin drift '+n)
src=(B/'reconstruct.py').read_text()
old='def cdir(i,j): return lift_full(i,j).get((0,-3),0)'
new="""def cdir(i,j):
    # Root single scalar-coefficient projection; no high-power image.
    memo={}
    def count(n,e):
        if n==0:return int(e==0)
        if abs(e)>n:return 0
        if (n,e) not in memo:memo[n,e]=count(n-1,e-1)+count(n-1,e+1)
        return memo[n,e]
    return (-1)**j*count(j,i-3)"""
need(src.count(old)==1,'exact scope replacement')
src=src.replace(old,new)
for name in ('witness.json','check.py'):
    oldpath='/tmp/jc2-lane.YwoVCk/inputs/'+name
    need(src.count(oldpath)==1,'exact path replacement')
    src=src.replace(oldpath,str(R/'box/d125-nonnegative-grading-discriminator-20260907'/name))
runs=[]
for opt in ([],['-O']):
    p=subprocess.run(['/usr/bin/python3','-I','-B']+opt+['-c',src],capture_output=True,timeout=5)
    need(p.returncode==0 and not p.stderr,'independent replay')
    h=hashlib.sha256(p.stdout).hexdigest()
    need(h=='835e1764b92bf0b900bf98fb178d8dccf6c02efe049bd92310c470f83f5e5d0d','exact independent witness')
    runs.append({'optimized':bool(opt),'returncode':p.returncode,'stdout_sha256':h,'witness':json.loads(p.stdout)})
for n,h in pins.items():need(sha(R/n)==h,'post drift '+n)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,
     'scope':'One-row grading proof only; transition source-only NOT PROMOTED.',
     'adaptation':'Replace cdir full high-degree monomial images with scalar +/-1 coefficient counting; remaining full images have j<=5. Two frozen-input paths restored. Frozen bytes unchanged.',
     'corrections':['Include i>=0 in polygon halfplanes','fixed total face has10 odd lattice slots; with inner(2,1), fixed odd11. Reviewer prose says9 on total face incorrectly; independent witness is correct','No abstract quotient-grading no-go follows','Mutation stderr hashes are path-dependent']}
P=Path(__file__).with_suffix('.json')
with P.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(P)}))
