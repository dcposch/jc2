"""Root two terminal gates: scope-adapted math and path-restored exact-argv delta."""
import sys
sys.dont_write_bytecode=True
import ast,hashlib,json,resource,shutil,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');HERE=Path(__file__).resolve().parent;OUT=Path(__file__).with_suffix('.json')
def need(c,s):
    if not c:raise RuntimeError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512*2**20,512*2**20))
pins={};receipts={};start=time.monotonic();runs=[]
for tag in ('d125-pure-uniform-gate-fable5-20260907','d125-hybrid81-parent-gate-fable5-20260907'):
    r=dict(x.split('=',1) for x in (ROOT/'xmodel'/(tag+'.run.v2')).read_text().splitlines() if '=' in x)
    need(r['final_status']=='DONE' and r['exit_code']=='0' and r['seal_boundary']=='CLEAN' and r['report_state']=='BODY_SEALED' and r['charge_basis_status']=='ABSENT','terminal '+tag)
    receipts[tag]=r;pins[r['report']]=r['report_sha256']
    for i in range(1,int(r['charged_inputs'])+1):
        k='charged_input_'+str(i);need(r[k+'_post']=='UNCHANGED','post declared input');pins[r[k]]=r[k+'_sha256']
P=ROOT/'box/d125-pure-uniform-gate-fable5-20260907';G=ROOT/'box/d125-hybrid81-parent-gate-fable5-20260907'
for box,name in ((P,'owned-pins.sha256'),(G,'BOX-HASHES.txt')):
    for line in (box/name).read_text().splitlines():
        h,n=line.split(None,1);pins[str((box/n.strip()).relative_to(ROOT))]=h
for p,h in pins.items():need(sha(ROOT/p)==h,'prepin '+p)
pr=receipts['d125-hybrid81-parent-gate-fable5-20260907'];snap=HERE/'2142-parent-inputs';snap.mkdir()
for i in range(1,int(pr['charged_inputs'])+1):
    k='charged_input_'+str(i);d=snap/pr[k+'_basename'];need(not d.exists(),'copy collision');shutil.copyfile(ROOT/pr[k],d);need(sha(d)==pr[k+'_sha256'],'copy pin')
ps=(P/'controls.py').read_text()
old='Rp=add(pw(p,5),scale(pw(p,3),-3)); R3p=pw(Rp,3); R5p=pw(Rp,5)'
new='Rp=add(pw(p,5),scale(pw(p,3),-3)); R3p=projected_power(Rp,3,{3,13,15}); R5p=projected_power(Rp,5,{15})'
need(ps.count(old)==1,'scalar projection location')
prefix='''from itertools import product
def projected_power(a,n,slots):
    out={}
    for terms in product(tuple(a.items()),repeat=n):
        if sum(e[P] for e,c in terms) not in slots:continue
        key=tuple(sum(e[i] for e,c in terms) for i in range(NV));value=1
        for e,c in terms:value*=c
        out[key]=out.get(key,0)+value
    return {e:c for e,c in out.items() if c}
'''
ps=prefix+ps.replace(old,new)
old='R0=rpoly(2); R1=rpoly(1); Rs=add(R0,mul(s,R1))';new='R0=g; R1=p; Rs=add(R0,mul(s,R1))'
need(ps.count(old)==1,'bounded moving control location');ps=ps.replace(old,new)
gs=(G/'fable_controls.py').read_text();old="INPUTS = Path('/tmp/jc2-lane.Fwngeq/inputs')";need(gs.count(old)==1,'path restore');gs=gs.replace(old,'INPUTS = Path('+repr(str(snap))+')')
for src in (ps,gs):need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(src))),'adapted Assert gate')
def run(src,path,opt,mode,fragment,witness):
    body='import sys;sys.dont_write_bytecode=True;__file__='+repr(str(path))+';sys.argv=[__file__,'+repr(mode)+'];exec(compile('+repr(src)+',__file__,"exec"))'
    r=subprocess.run([sys.executable,'-I','-B']+opt+['-c',body],capture_output=True,timeout=30,preexec_fn=caps,cwd=ROOT)
    need((r.returncode!=0)==bool(fragment),'exit '+str(path)+' '+mode)
    if fragment:need(fragment.encode() in r.stderr,'wrong failure '+mode)
    digest=hashlib.sha256(r.stdout).hexdigest()
    if witness:need(digest==witness,'witness '+str(path))
    runs.append(dict(checker=str(path.relative_to(ROOT)),optimized=bool(opt),mode=mode,returncode=r.returncode,stdout_sha256=digest,stderr=r.stderr.decode()))
modes=[('',None),('--mutate-W-drop-L','universal collision'),('--mutate-sixth-coefficient','universal collision'),('--mutate-fourth-coefficient','universal collision'),('--mutate-drop-D','universal collision'),('--mutate-unit-object','U*Uinv=1'),('--mutate-unit-scalar','U*Uinv=1'),('--mutate-omit-alphaG','exact moving identity'),('--mutate-omit-deltaF','exact moving identity'),('--mutate-freeze-R','exact moving identity'),('--mutate-omit-FG','exact moving identity')]
for opt in ([],['-O']):
    for mode,fragment in modes:run(ps,P/'controls.py',opt,mode,fragment,None if fragment else '8d876a06d4518a353770973d5a4996f31a9da3ecf74610eb30aaae6ff78a88f6')
    run(gs,G/'fable_controls.py',opt,'',None,'3ca24febc1abeaf926585e0cb89b86fee4e4b81d9a2cfc811a8b4a458978b543' if opt else '2bda9bdd6c3ac8504ad0a6836057fd17bad635fa83b773b1784a4045d465a59a')
for p,h in pins.items():need(sha(ROOT/p)==h,'postpin '+p)
for i in range(1,int(pr['charged_inputs'])+1):
    k='charged_input_'+str(i);need(sha(snap/pr[k+'_basename'])==pr[k+'_sha256'],'post snapshot')
out=dict(status='PASS_SCOPED',pins=pins,runs=runs,seconds=time.monotonic()-start,math_adaptations=['only requested pure-p coefficient projections, not complete powers','formal moving R=g+s*p instead of random quadratic R'],correction='Fable prose scalar countercontrol needs x=3*s^3*sqrt(1-s^2/3+s^5/3); code correctly starts square root at3',parent_adaptation='Only deleted frozen path replaced by12 byte-identical copies',scope='Universal six-jet/cubic collision, unit parity/conditional Pell; NO uniform source theorem. Parent argv delta only; NO engine/source authority.')
with OUT.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),runs=len(runs),seconds=out['seconds'],receipt_sha256=sha(OUT))))
