"""Terminal source-composition gate replay with scalar-only dilation controls."""
import ast, concurrent.futures, datetime, hashlib, json, re, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2'); TAG='d125-cone-source-composition-gate-fable5-20260908'
B=ROOT/'box'/TAG; start=time.monotonic()
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
rp=ROOT/'xmodel'/(TAG+'.run.v2')
d=dict(line.split('=',1) for line in rp.read_text().splitlines() if '=' in line)
need(all(d[k]==v for k,v in {'final_status':'DONE','exit_code':'0','seal_boundary':'CLEAN','report_state':'BODY_SEALED','charge_basis_status':'ABSENT'}.items()),'terminal receipt')
pins={str(rp):'e3d1f5b8c87e819ec1d6291b8a4000d1d75e79c05d0d6938b00e6a2974bc4d60',str(ROOT/d['report']):d['report_sha256'],str(B/'custody.json'):'c1a1884bf101bc9c78d9600bbf7c0739ef9567db59b5bf1760eb710e2aeb2902'}
for i in range(1,23): pins[str(ROOT/d[f'charged_input_{i}'])]=d[f'charged_input_{i}_sha256']
for e in json.loads((B/'custody.json').read_bytes())['owned']: pins[str(ROOT/e['path'])]=e['sha256']
for p,h in pins.items(): need(sha(Path(p))==h,'pre drift '+p)
controls=B/'fable5_controls.py'
for p in [controls]+[B/x for x in ('consumer-check.py','cone-counter-check.py','source-first-contact-check.py')]:
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(p.read_text()))),'Assert gate')
source=controls.read_text()
begin=source.index('for trial in range(3):\n'); end=source.index('out["C1_dilation_law"]',begin)
old=source[begin:end]
new='''for ag,ap,bg,bp in ((9,6,15,9),(2,1,1,0),(0,15,1,24)):
    coefficient=ag*bp-ap*bg
    need(coefficient!=0, "scalar monomial bracket nonzero")
    degree=ag+ap+bg+bp-2
    exponent=(15-ag-ap)+(25-bg-bp)
    need(exponent==38-degree, "dilation law")
    need(exponent-1!=38-degree, "changed-exponent control must fail")
'''
patched=source[:begin]+new+source[end:]
loader='from pathlib import Path\np='+repr(str(controls))+'\ns=Path(p).read_text()\ns=s.replace('+repr(old)+','+repr(new)+')\nexec(compile(s,p,"exec"),{"__file__":p,"__name__":"__main__"})\n'
cases=[('charged',row) for row in json.loads((B/'fable5-replay.json').read_bytes())['runs']]
cases += [('reviewer',{'optimized':opt}) for opt in (False,True)]
def run(case):
    kind,row=case
    argv=['/usr/bin/prlimit','--cpu=25','--as=536870912','/usr/bin/python3','-I','-B']+(['-O'] if row['optimized'] else [])
    if kind=='charged':
        argv += [str(B/row['script'])]+([] if row['mode']=='(no-arg positive)' else [row['mode']])
        expected_rc=row['returncode']; expected_out=row['stdout_sha256']; expected_error=row['stderr_error_line']
    else:
        argv += ['-c',loader]; expected_rc=0; expected_out='87cf7c581307d12a35422b7f2049868db1672610c106259919db9d483a619c84'; expected_error=''
    z=subprocess.run(argv,capture_output=True,timeout=30,cwd=ROOT)
    need(z.returncode==expected_rc,'exit '+str(case))
    need(hashlib.sha256(z.stdout).hexdigest()==expected_out,'stdout '+str(case))
    errors=re.findall(r'^(\w+Error: .*)$',z.stderr.decode(),re.M)
    need((errors[-1] if errors else '')==expected_error,'error marker '+str(case))
    if not expected_error: need(not z.stderr,'unexpected stderr')
    return {'kind':kind,'optimized':row['optimized'],'script':row.get('script','fable5_controls.py in-memory scalar C1'),'mode':row.get('mode','positive with internal changed objects'),'returncode':z.returncode,'stdout_sha256':expected_out,'stderr_sha256':hashlib.sha256(z.stderr).hexdigest()}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: runs=list(pool.map(run,cases))
for p,h in pins.items(): need(sha(Path(p))==h,'post drift '+p)
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pins':pins,'runs':runs,'seconds':time.monotonic()-start,'replacement':{'old':old,'new':new},'loaded_reviewer_sha256':hashlib.sha256(patched.encode()).hexdigest(),
     'scope':'Root verified terminal unit/original model absent before receipt and22 current charged pins/report; whole gate and all checker code read. Exact odd-source exclusion composition, no broader coverage. No actual high source/H/R powers or CAS in root replay.',
     'corrections':['Reviewer T_s weight<=-9 is too strong when R1 is nonzero: w(R1)=-7; only w(T_s)<=1 is needed and holds.', 'ord alpha is10 only when alpha!=0, otherwise infinity; the actual bound is>=10. All zero-scalar cases retained.', 'C1 constructs unrelated sparse degree15/25 toy pairs despite the broad no-A15/B25 header. Root replaces these unnecessary expansions in memory with scalar monomial-chain-rule checks; frozen bytes unchanged and stdout identical.', 'C1/C7 random finite evaluations are illustrations, not universal identity proofs. Whole prose rederivation and the charged free-symbol checker supply the universal identities. C8 is explicitly finite illustration.', 'Reviewer timeout wrapper used an unrecorded inner group for tiny runs; root uses subprocess wall timeout with direct prlimit children, no inner timeout group.', 'The evidence establishes an existential unit ideal, not a computed Nullstellensatz identity. Unguarded k=0, nonodd, golden and common cases are not excluded here.']}
dest=Path(__file__).with_suffix('.json')
with dest.open('x') as f: json.dump(out,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'seconds':out['seconds'],'receipt_sha256':sha(dest)}))
