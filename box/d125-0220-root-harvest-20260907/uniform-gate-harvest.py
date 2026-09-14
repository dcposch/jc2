"""Root terminal gate pins and untouched bounded normal/optimized controls."""
import sys
sys.dont_write_bytecode=True
import ast,hashlib,json,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');B=ROOT/'box/d125-uniform-ramification-gate-fable5-20260907'
def need(x,s):
    if not x:raise ValueError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r={}
for line in (ROOT/'xmodel/d125-uniform-ramification-gate-fable5-20260907.run.v2').read_text().splitlines():
    if '=' in line:k,v=line.split('=',1);r[k]=v
need(r['final_status']=='DONE' and r['exit_code']=='0' and r['report_state']=='BODY_SEALED' and r['seal_boundary']=='CLEAN_SEALED' and r['charge_basis_status']=='ABSENT','terminal receipt')
pins={r['report']:'acb88e00ddbddc3f10d7489a3683e9fd02f0629d34d45e3b5b6d3d3ba5ccec6e',
 str((B/'gate_controls.py').relative_to(ROOT)):'57b2f1a5e153b0ef3e3fa1c4a9b0828c2f2e5190b2611cb976e8a383834e3560',
 str((B/'witness.json').relative_to(ROOT)):'6928878463a6e77756f9b123379059d9804afab32a8646c1c9560f83db24af9a',
 str((B/'replay.json').relative_to(ROOT)):'8ec3ac6306ffead47aac3198fe1a0c7c92d3b67ffac951538ee2e2df3507b3f5'}
for i in range(1,int(r['charged_inputs'])+1):
    key='charged_input_'+str(i);need(r[key+'_post']=='UNCHANGED','post input');pins[r[key]]=r[key+'_sha256']
for p,h in pins.items():need(sha(ROOT/p)==h,'prepin '+p)
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((B/'gate_controls.py').read_text()))),'Assert gate')
runs=[];t=time.monotonic()
modes=[('',None),('--mutate-moving-denominator','negative-R part'),('--mutate-double-factor','mixed C^2D coefficient'),('--mutate-omit-low-lift','lift kernel is exactly'),('--mutate-origin-bound','localized kernel exponents exactly')]
for opt in ([],['-O']):
    for mode,msg in modes:
        p=subprocess.run([sys.executable,'-B']+opt+[str(B/'gate_controls.py')]+([mode] if mode else []),capture_output=True,cwd=ROOT,timeout=30)
        need((p.returncode!=0)==bool(msg),'exit mode '+mode)
        if msg:need(msg.encode() in p.stderr,'wrong mutation gate')
        else:need(hashlib.sha256(p.stdout).hexdigest()==pins[str((B/'witness.json').relative_to(ROOT))],'witness drift')
        runs.append(dict(optimized=bool(opt),mutation=mode or None,rc=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
for p,h in pins.items():need(sha(ROOT/p)==h,'postpin '+p)
dest=ROOT/'box/d125-0220-root-harvest-20260907/uniform-gate-harvest.json'
out=dict(status='PASS_UNIFORM_GENERIC_ARC_GATE',pins=len(pins),runs=runs,wall_seconds=time.monotonic()-t,corrections=['Review N0=M1-(M0/R0)S only for a=1; general coefficientwise W/N proof is charged','Finite grid kernel control is supplemented by exact two-row elimination, b=c and a=-b'],scope='finite char0 field coefficient arcs k=s^m,h!=0 only; not degeneration existence, exceptional/infinity or guarded emptiness')
with dest.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),wall_seconds=out['wall_seconds'],receipt_sha256=sha(dest))))
