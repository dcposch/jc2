import sys
sys.dont_write_bytecode=True
import hashlib,json,resource,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');P=ROOT/'box/d125-hybrid81-parent-repair-20260907';OUT=Path(__file__).with_suffix('.json')
def need(c,s):
    if not c:raise RuntimeError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512*2**20,512*2**20))
c=json.loads((P/'custody.json').read_text());need(c['status']=='TERMINAL' and c['all_writers_finished'] and not c['active_jobs'],'terminal')
pins={x['path']:x['sha256'] for x in c['inputs']+c['owned']};pins[str((P/'custody.json').relative_to(ROOT))]='de220779c1768efb376b5c51bdb6caf6afd62a96cda3d0f7e2acd767a04078d3'
for p,h in pins.items():need(sha(ROOT/p)==h,'prepin '+p)
runs=[];start=time.monotonic()
for opt in ([],['-O']):
    r=subprocess.run([sys.executable,'-I','-B']+opt+[str(P/'check.py')],capture_output=True,timeout=30,preexec_fn=caps,cwd=ROOT)
    need(r.returncode==0 and r.stderr==b'' and json.loads(r.stdout)['payload_cases']==94,'actual payload mocks')
    need(hashlib.sha256(r.stdout).hexdigest()=='9097ba47ce0ac17eba9e4a5a318210df029238394791aba94389005b5e92b470','witness')
    runs.append(dict(optimized=bool(opt),returncode=r.returncode,stdout_sha256=hashlib.sha256(r.stdout).hexdigest(),stderr_sha256=hashlib.sha256(r.stderr).hexdigest()))
for p,h in pins.items():need(sha(ROOT/p)==h,'postpin '+p)
out=dict(status='PASS_SCOPED',pins=pins,runs=runs,seconds=time.monotonic()-start,scope='Exact argv predicate delta, actual payload mocked before deadline/writes. No engine/authority; independent gate pending.')
with OUT.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),cases_per_mode=94,seconds=out['seconds'],receipt_sha256=sha(OUT))))
