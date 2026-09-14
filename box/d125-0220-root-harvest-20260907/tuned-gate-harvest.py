"""Root scoped replay: keep formal R=g, avoid actual R^2 just for its weight."""
import sys
sys.dont_write_bytecode=True
import ast,hashlib,json,resource,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');B=ROOT/'box/d125-exceptional-tuned-gate-fable5-v2-20260907'
def need(c,s):
    if not c:raise RuntimeError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
r=dict(l.split('=',1) for l in (ROOT/'xmodel/d125-exceptional-tuned-gate-fable5-v2-20260907.run.v2').read_text().splitlines() if '=' in l)
need(r['final_status']=='DONE' and r['exit_code']=='0' and r['report_state']=='BODY_SEALED' and r['seal_boundary']=='CLEAN' and r['charge_basis_status']=='ABSENT','terminal receipt')
pins={r['report']:'bfede999311fd933cb08f0b23dac1ec4aa404dd593b2b1f017b6ef1499e2446f'}
for name,h in {'gate_controls.py':'de6a79c31925806d6e00c718a777592f7b60437ecbfc5c2c3c59341959cf45f1','runner.py':'6ba746981a23f7c965ad41836e2363f2947c0cb00f34f853e387238cfc339311','replay.json':'d917b188e54f051ce5f81269fec71f8bbe7139d8fff00c699f9feb7f0dd7337e','witness.json':'45de42f6e5ac04c2a84450db98be669bdb95d77170134bb1721b0e4aa0812fbe'}.items():pins[str((B/name).relative_to(ROOT))]=h
for i in range(1,8):
    k='charged_input_'+str(i);need(r[k+'_post']=='UNCHANGED','postpin state');pins[r[k]]=r[k+'_sha256']
for p,h in pins.items():need(sha(ROOT/p)==h,'prepin '+p)
source=(B/'gate_controls.py').read_text()
changes={"Rs=[('R=g',g),('R=g+p^2',add(g,power(p,2)))]":"Rs=[('R=g',g)]",'max(5*e[0]-7*e[1] for e in power(R5,2))==2':'2*max(5*e[0]-7*e[1] for e in R5)==2'}
for old,new in changes.items():need(source.count(old)==1,'unique adaptation');source=source.replace(old,new)
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(source))),'adapted no Assert')
adapted_sha=hashlib.sha256(source.encode()).hexdigest()
program='import sys\nsys.dont_write_bytecode=True\n__file__='+repr(str(B/'gate_controls.py'))+'\nsys.argv=[__file__]+sys.argv[1:]\nexec(compile('+repr(source)+',__file__,"exec"))'
modes=[('',None),('--mutate-wrong-quadratic','C1-identity'),('--mutate-omit-cross','C1-identity'),('--mutate-zero-cross','C1-nonzero-cross'),('--mutate-omit-reference-betaF','C2-reference-G'),('--mutate-low-p3','C3-low-rows-kill-c-d')]
runs=[];t=time.monotonic();positive=[]
for opt in ([],['-O']):
    for mode,msg in modes:
        p=subprocess.run([sys.executable,'-B']+opt+['-c',program]+([mode] if mode else []),capture_output=True,cwd=ROOT,timeout=30,preexec_fn=caps)
        need((p.returncode!=0)==bool(msg),'expected exit '+mode)
        if msg:need(msg.encode() in p.stderr,'mutation gate')
        else:
            d=json.loads(p.stdout);need(d['status']=='PASS' and d['gate_count']==40 and d['assert_nodes']==0,'positive gates');positive.append(p.stdout)
        runs.append(dict(optimized=bool(opt),mutation=mode or None,rc=p.returncode,stdout=p.stdout.decode(),stderr=p.stderr.decode()))
need(positive[0]==positive[1],'positive equality')
for p,h in pins.items():need(sha(ROOT/p)==h,'postpin '+p)
out=dict(status='PASS_TUNED_FINITE_ARC_GATE',pins=pins,adapted_source_sha256=adapted_sha,adaptations=changes,runs=runs,wall_seconds=time.monotonic()-t,scope='field finite arcs alpha0 nonzero delta0 zero only; no pure center/global degeneration/guarded emptiness')
dest=ROOT/'box/d125-0220-root-harvest-20260907/tuned-gate-harvest.json'
with dest.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),runs=len(runs),wall_seconds=out['wall_seconds'],receipt_sha256=sha(dest),positive_sha256=hashlib.sha256(positive[0]).hexdigest())))
