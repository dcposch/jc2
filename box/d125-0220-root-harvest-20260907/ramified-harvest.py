"""Root tiny replay of sealed m=2 arc desk, bytecode writes disabled."""
import ast,hashlib,json,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
BOX=ROOT/'box/d125-ramified-twojet-discriminator-20260907'
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
need(sha(BOX/'custody.json')=='07fda43a6f001bfdace4943089a4cfef8c7a2044623e894de1352b86e73ed42e','custody')
c=json.loads((BOX/'custody.json').read_bytes())
pins={p:x['sha256'] for section in ('owned','inputs') for p,x in c[section].items()}
pins['xmodel/d125-ramified-twojet-discriminator-astra-20260907.md']='1440132691e51058b51927ba40234d0441d787a167321aba0af2bd53e8b698d4'
def verify():
    for p,h in pins.items():need(sha(ROOT/p)==h,'pin '+p)
verify()
for p in (BOX/'check.py',ROOT/'box/d125-zero-k-deformation-discriminator-20260907/check.py'):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(p.read_bytes()))),'Assert '+str(p))
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
start=time.monotonic();runs=[]
for flags in ([],['-O']):
    for mode,error in [('',None),('--mutate-cubic-factor',b'third-order cubic coefficient'),('--mutate-omit-negative-row',b'omitted v^-2 row admits a pole'),('--mutate-independent-tangent',b'tangent p/gp2 compatibility'),('--mutate-truncated-saturation',b'nilpotent k cannot be canceled')]:
        p=subprocess.run([sys.executable,'-B',*flags,str(BOX/'check.py')]+([mode] if mode else []),capture_output=True,timeout=30,preexec_fn=caps)
        need((p.returncode!=0)==bool(mode),'exit '+mode)
        if error:need(error in p.stderr,'mutation reason')
        else:need(hashlib.sha256(p.stdout).hexdigest()=='37387ae526322c18c614502d78794a9b6be983b4afecf90ee3a58ffbb41618ec','witness')
        runs.append(dict(flags=flags,mode=mode,returncode=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
verify()
result=dict(status='PASS',pins=pins,runs=runs,wall_seconds=time.monotonic()-start,scope='degree-five lifts/degree-four kernel/R=g brackets only; no full source',bytecode_writes_disabled=True)
dest=OUT/'ramified-harvest.json'
with dest.open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status='PASS',pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(dest))))
