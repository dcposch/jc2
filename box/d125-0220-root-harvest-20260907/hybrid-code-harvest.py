"""Root terminal code-prep pins and two tiny modes, not production metadata."""
import ast,hashlib,json,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
BOX=ROOT/'box/d125-hybrid-affine-code-prep-20260907'
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
need(sha(BOX/'custody.json')=='7e7fba3a68af30c16b023391e98ea4e801c2f7c183c9e3f31fa5062385ba3385','custody pin')
c=json.loads((BOX/'custody.json').read_bytes());q=json.loads((BOX/'pins.json').read_bytes())
pins={str((BOX/p).relative_to(ROOT)):h for p,h in c['owned_evidence'].items()}
pins.update(q['inputs']);pins['xmodel/d125-hybrid-affine-code-prep-astra-20260907.md']='18f983a99c0496f4928fc4cb04bee33c1b80d8c7cbd3eeda57bf4ac01bb4e3c0'
def verify():
    for p,h in pins.items():need(sha(ROOT/p)==h,'pin '+p)
verify()
for name in ('construct.py','replay.py','baseline.py','test_tiny.py'):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((BOX/name).read_bytes()))),'Assert '+name)
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
start=time.monotonic();runs=[]
for flags in ([],['-O']):
    p=subprocess.run([sys.executable,'-B',*flags,str(BOX/'test_tiny.py')],capture_output=True,timeout=30,preexec_fn=caps)
    need(p.returncode==0 and b'Ran 20 tests' in p.stderr and b'\nOK\n' in p.stderr,'tiny methods')
    runs.append(dict(flags=flags,returncode=p.returncode,stdout=p.stdout.decode(),stderr=p.stderr.decode()))
verify();result=dict(status='PASS_TINY_ONLY',pins=pins,runs=runs,wall_seconds=time.monotonic()-start,production_metadata=False,source_rows=0)
dest=OUT/'hybrid-code-harvest.json'
with dest.open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=result['status'],pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(dest))))
