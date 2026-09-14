"""Root terminal-only replay; no full source expansions or immutable edits."""
import sys
sys.dont_write_bytecode=True
import ast,hashlib,json,resource,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2')
P=ROOT/'box/d125-pure-uniform-discriminator-20260907'
OUT=ROOT/'box/d125-0220-root-harvest-20260907/0747-pure-harvest.json'
def need(c,s):
    if not c:raise RuntimeError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*2**20,512*2**20))
start=time.monotonic(); c=json.loads((P/'custody.json').read_text())
need(c['status']=='TERMINAL' and c['all_writers_finished'] and not c['live_jobs'],'terminal custody')
pins={x['path']:x['sha256'] for x in c['inputs']+c['owned']}
pins[str((P/'custody.json').relative_to(ROOT))]='fdaa7ccf901ff8027fd9dc6dc8a73c7ac3f2a375da1853f21fb699eb4855a383'
for p,h in pins.items():need(sha(ROOT/p)==h,'prepin '+p)
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((P/'check.py').read_text()))),'Assert gate')
modes=[('',None),('--mutate-remove-intermediate','actual formal collision'),('--mutate-sixth-factor','actual formal collision'),('--mutate-omit-alphaG','actual moving identity'),('--mutate-unit-object','actual nonconstant affine unit')]
runs=[]
for opt in ([],['-O']):
    for mode,fragment in modes:
        p=subprocess.run([sys.executable,'-B']+opt+[str(P/'check.py')]+([mode] if mode else []),capture_output=True,timeout=30,preexec_fn=caps,cwd=ROOT)
        need((p.returncode!=0)==bool(fragment),'exit '+mode)
        if fragment:need(fragment.encode() in p.stderr,'wrong mutation '+mode)
        h=hashlib.sha256(p.stdout).hexdigest()
        if not fragment:need(h=='face35182eb0e5570693e705289e57bd1a1a20a721808cfebe52850251ed00ad','witness')
        runs.append(dict(optimized=bool(opt),mode=mode,returncode=p.returncode,stdout_sha256=h,stderr=p.stderr.decode()))
for p,h in pins.items():need(sha(ROOT/p)==h,'postpin '+p)
out=dict(status='PASS_SCOPED',pins=pins,runs=runs,seconds=time.monotonic()-start,scope='Actual degree<=5 generators and formal/circuit identities only. Uniform pure exclusion remains GAP; claims provisional pending different-model review.')
with OUT.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),runs=len(runs),seconds=out['seconds'],receipt_sha256=sha(OUT))))
