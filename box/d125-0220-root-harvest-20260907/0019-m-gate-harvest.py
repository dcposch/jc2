"""Read-only tiny M-gate replay; stdout is a new receipt, no input writes."""
from pathlib import Path
import ast, hashlib, json, subprocess, time
from datetime import datetime, timezone
B = Path('/home/ubuntu/jc2')
box = B / 'box/golden-hdiv-m-composition-gate-fable5-20260908'
rp = B / 'xmodel/golden-hdiv-m-composition-gate-fable5-20260908.md'
rcp = B / 'xmodel/golden-hdiv-m-composition-gate-fable5-20260908.run.v2'
def require(ok, what):
    if not ok: raise RuntimeError(what)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
pins = {rp:'50045412e9b0d9cf3e640844e768e359bd7dd466e862316e9b4e9380d40c68cf',
        rcp:'72863f6f94a02ebcc7c0818a68508d69c5551899608897078df41a847c18c579'}
for name,h in [('scalar_control.py','919003eefe8317f81d84f61be10d9a210270201df52a90d5d08620d5968a03af'),
               ('argv.txt','3a7f49a102b8e4b321e1e1d3408b38379d2ae8d2480e37edac90cd5c5a07bbfe'),
               ('run_normal.stdout','3259cb2f122067a78ccf50f7df8566a75f86c698612eb4db6e9668cd79df8bd8'),
               ('run_optimized.stdout','d496ba2a6f059929d71afcc6d1ec971755c7e27e7873a4094bbad6fdbb64f651')]:
    pins[box/name]=h
meta=dict(l.split('=',1) for l in rcp.read_text().splitlines() if '=' in l)
for i in range(1,11):
    k=f'charged_input_{i}'; pins[B/meta[k]]=meta[k+'_sha256']
for p,h in pins.items(): require(sha(p)==h, f'pre-drift {p}')
code=box/'scalar_control.py'
require(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(code.read_text()))), 'assert in code')
start=time.monotonic(); results=[]
for opt in (False,True):
    mode='optimized' if opt else 'normal'
    argv=['prlimit','--cpu=25','--as=536870912','python3','-I','-B']
    if opt: argv.append('-O')
    argv.append(str(code))
    run=subprocess.run(argv,cwd=box,capture_output=True,timeout=30)
    require(run.returncode==0 and not run.stderr, 'runtime')
    require(run.stdout==(box/f'run_{mode}.stdout').read_bytes(), 'retained stdout mismatch')
    txt=run.stdout.decode(); lines=txt.splitlines()
    require(len([x for x in lines if f'[{mode}] PASS ' in x])==26, '26 predicates')
    require(len([x for x in lines if 'PASS REJECT expected:' in x])==4, 'four scope controls')
    require(lines[-1]==f'[{mode}] SUMMARY 26/26 checks as expected', 'summary')
    results.append({'argv':argv,'rc':run.returncode,'stdout':txt,'stderr':run.stderr.decode()})
for p,h in pins.items(): require(sha(p)==h, f'post-drift {p}')
print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
                  'pin_count':len(pins),'pins':[{'path':str(p.relative_to(B)),'sha256':h} for p,h in pins.items()],
                  'seconds':round(time.monotonic()-start,6),'results':results,
                  'scope':'22 finite identities and four scope controls in both modes; two rho-change comparisons and two sign/balance controls. Prose supplies universal proof. No actual H/R high powers or source build.'},indent=2))
