"""Bounded root replay of terminal arc-interface gate and pure-center producer."""
import sys
sys.dont_write_bytecode=True
import ast, hashlib, json, resource, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2')
OUT=ROOT/'box/d125-0220-root-harvest-20260907/0712-math-harvest.json'
def need(c,s):
    if not c: raise RuntimeError(s)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*2**20,512*2**20))
pins={}; runs=[]; start=time.monotonic()
tag='d125-arc-closure-gate-fable5-20260907'
r=dict(x.split('=',1) for x in (ROOT/'xmodel'/ (tag+'.run.v2')).read_text().splitlines() if '=' in x)
need(r['final_status']=='DONE' and r['exit_code']=='0' and r['seal_boundary']=='CLEAN_SEALED' and r['report_state']=='BODY_SEALED' and r['charge_basis_status']=='ABSENT','terminal arc receipt')
pins[r['report']]=r['report_sha256']
for i in range(1,int(r['charged_inputs'])+1):
    k='charged_input_'+str(i);need(r[k+'_post']=='UNCHANGED','post input');pins[r[k]]=r[k+'_sha256']
E=ROOT/'box'/tag
for line in (E/'own_artifacts.sha256').read_text().splitlines():
    h,name=line.split(None,1);pins[str((E/name.strip()).relative_to(ROOT))]=h
P=ROOT/'box/d125-exceptional-pure-discriminator-20260907'
pc=json.loads((P/'custody.json').read_text())
need(pc['status']=='TERMINAL' and pc['all_writers_finished'],'pure terminal')
for x in pc['inputs']+pc['owned']:pins[x['path']]=x['sha256']
pins[str((P/'custody.json').relative_to(ROOT))]='c062672b5d4d167c12201c3e62fb37523369a2d968758710e1419d712b0160c4'
for p,h in pins.items():need(sha(ROOT/p)==h,'prepin '+p)
for p in (E/'gate_controls.py',P/'check.py',ROOT/'box/d125-zero-k-deformation-discriminator-20260907/check.py'):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(p.read_text()))),'Assert gate')
# Frozen reviewer builds entire pure-p powers. Root instead enumerates ONLY
# requested scalar coefficients. This adaptation does not change frozen bytes.
src=(E/'gate_controls.py').read_text()
old='R3=pw(Rp,3);R5=pw(Rp,5)'
new='R3=projected_power(Rp,3,{3,13,15});R5=projected_power(Rp,5,{3,15})'
need(src.count(old)==1,'projection replacement count')
prefix='''from itertools import product
def projected_power(a,n,slots):
    out={}
    for terms in product(tuple(a.items()),repeat=n):
        if sum(k[0] for k,v in terms) not in slots: continue
        key=tuple(sum(k[i] for k,v in terms) for i in range(5))
        value=1
        for k,v in terms:value*=v
        out[key]=out.get(key,0)+value
    return {k:v for k,v in out.items() if v}
'''
src=prefix+src.replace(old,new)
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(src))),'adapted Assert')
def run(args,label,fragment=None,witness=None):
    p=subprocess.run([sys.executable,'-B']+args,cwd=ROOT,capture_output=True,timeout=30,preexec_fn=caps)
    need((p.returncode!=0)==bool(fragment),'exit '+label)
    if fragment:need(fragment.encode() in p.stderr,'wrong failure '+label)
    h=hashlib.sha256(p.stdout).hexdigest()
    if witness:need(h==witness,'witness '+label)
    runs.append(dict(label=label,returncode=p.returncode,stdout_sha256=h,stderr=p.stderr.decode()))
for opt in ([],['-O']):
    for mode,msg in [('',None),('--omit-243','D = 81'),('--gamma-sign','w=B_p3'),('--claim-global-h','boundary equation h'),('--drop-tp3','[p^13]')]:
        body='import sys; sys.dont_write_bytecode=True; __file__='+repr(str(E/'gate_controls.py'))+'; sys.argv=[__file__,'+repr(mode)+']; exec(compile('+repr(src)+',__file__,"exec"))'
        run(opt+['-c',body],'arc '+str(opt)+' '+mode,msg,None if msg else '53cfb36403777c877f4de70a05c67d0e6fae71027df93cee6e54816e1afc423f')
    for mode,msg in [('',None),('--mutate-omit-weight','weight hypothesis cannot'),('--mutate-omit-mixed-linear','moving-reference mixed correction'),('--mutate-freeze-moving-R','complete moving-R polynomial'),('--mutate-jet-coefficient','actual formal twojet'),('--mutate-omit-k-face','nilpotent candidate does not')]:
        run(opt+[str(P/'check.py')]+([mode] if mode else []),'pure '+str(opt)+' '+mode,msg,None if msg else 'f617242b28e40ba1110b0be45d9ec650c1ea484b33ecdb934df3c78391d8eb81')
for p,h in pins.items():need(sha(ROOT/p)==h,'postpin '+p)
out=dict(status='PASS_SCOPED',pins=pins,runs=runs,seconds=time.monotonic()-start,arc_adaptation='in-memory scalar coefficient projections only; frozen reviewer untouched',arc_scope='H,D in radical(J+(k)), not radical(J)',pure_scope='necessary first-contact restrictions only, pending different-model review')
with OUT.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),runs=len(runs),seconds=out['seconds'],receipt_sha256=sha(OUT))))
