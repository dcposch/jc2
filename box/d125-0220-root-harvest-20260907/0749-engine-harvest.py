"""Restore immutable flat inputs and replay terminal Sol gate unchanged except path."""
import sys
sys.dont_write_bytecode=True
import ast,hashlib,json,resource,shutil,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2'); HERE=Path(__file__).resolve().parent
TAG='d125-hybrid81-engine-gate-sol56-v2-20260907'
G=ROOT/'box'/TAG; SNAP=HERE/'engine-gate-inputs'; OUT=HERE/'0749-engine-harvest.json'
def need(c,s):
    if not c:raise RuntimeError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512*2**20,512*2**20))
start=time.monotonic()
r=dict(x.split('=',1) for x in (ROOT/'xmodel'/(TAG+'.run.v2')).read_text().splitlines() if '=' in x)
need(r['final_status']=='DONE' and r['exit_code']=='0' and r['seal_boundary']=='CLEAN' and r['report_state']=='BODY_SEALED' and r['charge_basis_status']=='ABSENT','terminal receipt')
pins={r['report']:r['report_sha256']}
for i in range(1,int(r['charged_inputs'])+1):
    k='charged_input_'+str(i);need(r[k+'_post']=='UNCHANGED','postpin');pins[r[k]]=r[k+'_sha256']
for name,h in [('gate_checks.py','2db05fe18541a749190e0536f6b4caa06ad8d1571a01a5120b63d0de6a49a90b'),('PINS.json','7d3b96d016be81b45ef34a78e992e29b094cd37fad285c270dd3b2b2aa49c150'),('RUNS.json','286ccb1c9cd8f802d3980d45f6c5b15e934cd2338e0634847406c28add691c2c')]:pins[str((G/name).relative_to(ROOT))]=h
for p,h in pins.items():need(sha(ROOT/p)==h,'prepin '+p)
SNAP.mkdir()
for i in range(1,int(r['charged_inputs'])+1):
    k='charged_input_'+str(i); dest=SNAP/r[k+'_basename'];need(not dest.exists(),'snapshot collision');shutil.copyfile(ROOT/r[k],dest)
    need(sha(dest)==r[k+'_sha256'],'copy pin')
source=(G/'gate_checks.py').read_text()
old="INPUTS = Path('/tmp/jc2-lane.wWImXu/inputs')"
need(source.count(old)==1,'path restore unique')
source=source.replace(old,'INPUTS = Path('+repr(str(SNAP))+')')
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(source))),'Assert gate')
runs=[]
for opt in ([],['-O']):
    body='import sys;sys.dont_write_bytecode=True;__file__='+repr(str(G/'gate_checks.py'))+';exec(compile('+repr(source)+',__file__,"exec"))'
    p=subprocess.run([sys.executable,'-I','-B']+opt+['-c',body],capture_output=True,timeout=30,preexec_fn=caps,cwd=ROOT)
    need(p.returncode==0 and b'Ran 10 tests' in p.stderr and p.stderr.rstrip().endswith(b'OK'),'gate replay')
    runs.append(dict(optimized=bool(opt),returncode=p.returncode,stdout=p.stdout.decode(),stderr=p.stderr.decode()))
for p,h in pins.items():need(sha(ROOT/p)==h,'postpin '+p)
for i in range(1,int(r['charged_inputs'])+1):
    k='charged_input_'+str(i);need(sha(SNAP/r[k+'_basename'])==r[k+'_sha256'],'post copy pin')
out=dict(status='PASS_SCOPED_REVIEW_REPLAY',pins=pins,runs=runs,seconds=time.monotonic()-start,adaptation='Only INPUTS path restored to11 byte-identical retained copies; no frozen edits',result='Parent pathname membership is NOT exact parent argv; tiny verifier otherwise confirmed. No actual engine or source execution.')
with OUT.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),runs=len(runs),seconds=out['seconds'],receipt_sha256=sha(OUT))))
