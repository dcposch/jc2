"""Root tiny desk replay, not any source construction."""
import hashlib,json,resource,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=Path(__file__).resolve().parent
BOX=ROOT/'box/d125-parity-hybrid-cost-design-20260907'
def need(ok,msg):
    if not ok:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
need(sha(BOX/'pins.json')=='7f610eacc80504b63221e306265bf053636fed39d249684466933bb71a142e80','pins index')
pins=json.loads((BOX/'pins.json').read_bytes())['files']
pins['xmodel/d125-parity-hybrid-cost-design-astra-20260907.md']='b33d6944976ac934535bcc516bae82c738cd2e957665bfffb2325ec63170aa5a'
def verify():
    for p,h in pins.items():need(sha(ROOT/p)==h,'pin '+p)
verify()
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
start=time.monotonic();runs=[]
recorded=json.loads((BOX/'check-results.json').read_bytes())['runs']
for i,flags in enumerate(([],['-O'])):
    p=subprocess.run([sys.executable,'-B',*flags,str(BOX/'check.py')],capture_output=True,timeout=30,preexec_fn=caps)
    need(p.returncode==0 and not p.stderr,'tiny replay exit')
    result=json.loads(p.stdout);need(result==recorded[i],'recorded result')
    runs.append(dict(flags=flags,result=result,stdout_sha256=hashlib.sha256(p.stdout).hexdigest()))
verify()
dest=OUT/'hybrid-harvest.json'
with dest.open('x') as f:json.dump(dict(status='PASS',pins=pins,runs=runs,wall_seconds=time.monotonic()-start,scope='tiny matrices and monomial spaces; no source rows'),f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status='PASS',pins=len(pins),runs=len(runs),receipt_sha256=sha(dest))))
