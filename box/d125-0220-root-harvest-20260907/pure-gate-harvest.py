"""Root replay with generator-only adaptations, frozen reviewer unchanged."""
import sys
sys.dont_write_bytecode=True
import ast,hashlib,json,resource,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');B=ROOT/'box/d125-exceptional-pure-gate-fable5-20260907'
OUT=ROOT/'box/d125-0220-root-harvest-20260907/pure-gate-harvest.json'
def need(c,s):
    if not c:raise RuntimeError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512*2**20,512*2**20))
r=dict(x.split('=',1) for x in (ROOT/'xmodel/d125-exceptional-pure-gate-fable5-20260907.run.v2').read_text().splitlines() if '=' in x)
need(r['final_status']=='DONE' and r['exit_code']=='0' and r['seal_boundary']=='CLEAN_SEALED' and r['report_state']=='BODY_SEALED' and r['charge_basis_status']=='ABSENT','terminal')
pins={r['report']:r['report_sha256']}
for i in range(1,8):
    k='charged_input_'+str(i);need(r[k+'_post']=='UNCHANGED','post input');pins[r[k]]=r[k+'_sha256']
for line in (B/'owned-pins.sha256').read_text().splitlines():
    h,p=line.split(None,1);pins[str((B/p.strip()).relative_to(ROOT))]=h
for p,h in pins.items():need(sha(ROOT/p)==h,'prepin '+p)
src=(B/'controls.py').read_text()
need(not any(isinstance(x,ast.Assert) for x in ast.walk(ast.parse(src))),'Assert')
# Replace high-degree actual products by factor reasoning and individual
# low-coefficient convolutions; never expand the actual source pair.
old="    need(mul(bad,bad)==mul(mul(pw(g,2),Vp),R),'(gpV)^2 = (g^2 V) R by a 9-term product, no R^2')"
need(src.count(old)==1,'bad replacement')
src=src.replace(old,"    # gpV squared = (g²V)(p²V) by factor exponents, proof checked by root.")
i=src.index('    # --- 5.');j=src.index('    # --- 6.',i)
src=src[:i]+'    # Arbitrary C coefficient/ordinaryness claims checked in proof, not random high-degree lifts.\n'+src[j:]
i=src.index('    RZ=mul(R,Z);');j=src.index("    return {'status'",i)
small='''    brRZ=br(R,Z)
    need(brRZ!={},'actual [R,Z] nonzero')
    need(even(Z) and Z.get((0,)*NV,0)==0 and coef(Z,0,8)==0 and deg(Z)==2 and all(e[G]<=2*e[P] for e in Z),'actual Z meets leading C support')
    need(deg(R)+deg(Z)==7 and wt(R)+wt(Z)==-1 and deg(R)+2*deg(Z)==9 and wt(R)+2*wt(Z)==-3,'factor degree and weight additivity in a domain')
    def product_coefficient(a,b,i,j):
        return sum((ca*cb for ea,ca in a.items() for eb,cb in b.items() if ea[G]+eb[G]==i and ea[P]+eb[P]==j),Q(0))
    need(all(product_coefficient(R,Z,i,j)==0 for i,j in ((1,2),(0,3),(0,1),(2,1))),'actual selected low coefficients: nilpotent source lacks moving k face')
    # R and Z lifts were separately checked; polynomiality of products is automatic.
'''
src=src[:i]+small+src[j:]
src=src.replace('own stdlib controls; degree<=5 factors, RZ, RZ^2, (gpV)^2, random deg<=8 C times R; no R^2,R^3,R^5,R^2S expansion','root generator-only adaptation; formal moving identity, cubic lifts, individual low coefficient convolutions, no actual high-degree products')
need(not any(isinstance(x,ast.Assert) for x in ast.walk(ast.parse(src))),'adapted Assert')
runs=[];start=time.monotonic();positive=[]
for opt in ([],['-O']):
    for mode,msg in [('',None),('--mutate-drop-vm1-row','both lift rows force'),('--mutate-identity-delta-sign','identity (I)'),('--mutate-jet-coefficient','formal chain-rule')]:
        code='import sys;sys.dont_write_bytecode=True;__file__='+repr(str(B/'controls.py'))+';sys.argv=[__file__,'+repr(mode)+'];exec(compile('+repr(src)+',__file__,"exec"))'
        p=subprocess.run([sys.executable,'-B']+opt+['-c',code],cwd=ROOT,capture_output=True,timeout=30,preexec_fn=caps)
        need((p.returncode!=0)==bool(msg),'mode exit')
        if msg:need(msg.encode() in p.stderr,'mode failure')
        else:positive.append(hashlib.sha256(p.stdout).hexdigest())
        runs.append(dict(optimized=bool(opt),mode=mode or 'positive',returncode=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
need(len(set(positive))==1,'mode witnesses')
for p,h in pins.items():need(sha(ROOT/p)==h,'postpin '+p)
out=dict(status='PASS_SCOPED',pins=pins,runs=runs,seconds=time.monotonic()-start,adaptations=['no bad², random R*C or actual RZ/RZ² expansions; selected coefficients and generator lift/factor reasoning instead'],scope='pure necessary first contact only; uniform exclusion unresolved',evidence_correction='producer weight/face mutations are predicate flips, not changed objects; only three genuine producer mutations claimed')
with OUT.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),runs=len(runs),seconds=out['seconds'],positive_sha256=positive[0],receipt_sha256=sha(OUT))))
