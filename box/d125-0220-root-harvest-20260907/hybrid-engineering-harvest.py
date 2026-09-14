"""Root compact engineering acceptance; no AWS or mathematical source read."""
import ast,hashlib,json,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
B=ROOT/'box/d125-hybrid-affine-first-attempt-20260907'
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pins={'ENGINEERING-CHECKPOINT.md':'b79d81e67c64ef2779030b5322e8fcb1260db82f11efae5968eee4949551efae',
 'engineering-custody.json':'52d4dc9584f74494b25440974a5399eb30072b6daa254d3c213aaa550cbb0fa7',
 'REGISTRATION.md':'1ef0444a0778d13c2bf79fe1df51a82643478532716dd94434a04a412e0f12e6',
 'readiness.json':'492ab1e6daaf1cc07a239929f4703c078b3f0041ff990673fcc80303adb97652',
 'readiness.py':'9055ab2a00fad92396e88baaf9c21bddea0e953e68e07da2d3eb488481430c40',
 'deploy.py':'aefb9cbad5cde8cad2cc631c607744e97fea20eb443ad7f5cfe09b8915c284d0',
 'engineering_batch.py':'25ef56f4092c4f30b4bedf58a715e559a9e87fd95de8d57026477a3f80cedfe5',
 'harvest_engineering.py':'841fee0c7d40509234bc3e3b738397b94ed916ce3d8a4d65120f69627715d587',
 'verify_engineering.py':'8921e68106a2a5ff146a2626bf7dbe3ebe0d051d33c30c5228440a4bc1b5ccff'}
def verify():
    for p,h in pins.items():need(sha(B/p)==h,'pin '+p)
verify();custody=json.loads((B/'engineering-custody.json').read_bytes())
need(custody['status']=='ENGINEERING_TERMINAL_CUSTODY' and custody['boot']=='bef732b9-38e5-4a9a-8f93-77203426d2b8','custody scope')
for name,pin in custody['payload_pins'].items():
    p=ROOT/'box/d125-hybrid-affine-code-prep-20260907'/name if name!='run_capped.py' else ROOT/'box/full-j-solver-pilot-20260906/evidence/run_capped.py'
    need(sha(p)==pin,'payload '+name)
for name in ('verify_engineering.py','deploy.py','engineering_batch.py','harvest_engineering.py'):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((B/name).read_text()))),'Assert '+name)
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
start=time.monotonic();runs=[]
for opt in (False,True):
    r=subprocess.run([sys.executable,'-B']+(['-O'] if opt else [])+[str(B/'verify_engineering.py')],capture_output=True,timeout=30,preexec_fn=caps)
    need(r.returncode==0 and not r.stderr,'metadata replay failed '+r.stderr.decode())
    result=json.loads(r.stdout);need(result['checked_files']==22 and result['status']=='ENGINEERING_COMPACT_REPLAY_PASS','replay scope')
    runs.append(dict(optimized=opt,returncode=r.returncode,stdout=r.stdout.decode()))
verify();result=dict(status='ROOT_ENGINEERING_ACCEPTED',runs=runs,wall_seconds=time.monotonic()-start,root_pins=len(pins)+4,compact_artifacts=22,cooperative_dispatch_only=True,production_invoked=False,helper_sha256=sha(Path(__file__)))
with (OUT/'hybrid-engineering-harvest.json').open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(**result,receipt_sha256=sha(OUT/'hybrid-engineering-harvest.json'))))
