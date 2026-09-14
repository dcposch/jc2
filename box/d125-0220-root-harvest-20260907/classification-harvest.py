"""Root replay of sealed degree-five classification controls only."""
import ast,hashlib,json,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
BOX=ROOT/'box/d125-zero-k-boundary-classification-20260907'
def need(ok,why):
    if not ok: raise ValueError(why)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
need(sha(BOX/'custody.json')=='bc37d9e5a52e0830364beaa2fb1bd493b404407c42bc41d11cbe50b37443f290','custody')
c=json.loads((BOX/'custody.json').read_bytes())
pins={p:v['sha256'] for s in ('owned','inputs') for p,v in c[s].items()}
def verify():
    for p,h in pins.items():need(sha(ROOT/p)==h,'pin '+p)
verify()
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((BOX/'check.py').read_bytes()))),'Assert')
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
start=time.monotonic();runs=[]
for flags in ([],['-O']):
    for mode,message in [('',None),('--mutate-support',b'forbidden lower support slot'),('--mutate-drop-row',b'omitted negative row'),('--mutate-normalization',b'same-field leading normalization')]:
        p=subprocess.run([sys.executable,'-B',*flags,str(BOX/'check.py')]+([mode] if mode else []),capture_output=True,timeout=30,preexec_fn=caps)
        need((p.returncode!=0)==bool(mode),'exit')
        if mode:need(message in p.stderr,'mutation reason')
        else:need(hashlib.sha256(p.stdout).hexdigest()=='fc345a150a1946c502cd0ad0f7dd5d5a34ecb16e5ef5bf317bb4a864eb4c0a7a','witness')
        runs.append(dict(flags=flags,mode=mode,rc=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
verify()
result=dict(status='PASS',pins=pins,runs=runs,wall_seconds=time.monotonic()-start,scope='degree-five classification and small general-jet identity only; no full pair')
with (OUT/'classification-harvest.json').open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status='PASS',pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(OUT/'classification-harvest.json'))))
