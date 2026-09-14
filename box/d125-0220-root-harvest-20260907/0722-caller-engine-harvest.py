"""Root terminal replay of the caller delta and new tiny engineering preparation."""
import sys
sys.dont_write_bytecode=True
import ast,hashlib,json,resource,subprocess,time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2');B=ROOT/'box/d125-hybrid81-engine-review-prep-20260907';N=ROOT/'box/d125-hybrid81-engine-prep-20260907'
OUT=ROOT/'box/d125-0220-root-harvest-20260907/0722-caller-engine-harvest.json'
def need(c,s):
    if not c:raise RuntimeError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512*2**20,512*2**20))
pins=json.loads((B/'replay-results.json').read_text())['pins']
bp=json.loads((B/'PINS.json').read_text())
for p,v in bp['owned'].items():pins[str((B/p).relative_to(ROOT))]=v['sha256']
for p,v in bp['charged_inputs'].items():pins[p]=v['sha256']
pins[str((B/'PINS.json').relative_to(ROOT))]='266758af5308b13f848578722bb5f87f4101813771c8ef514342f56c2b9b718e'
pins[str((N/'custody.json').relative_to(ROOT))]='d4d57ce782a4c4873a03fa97f8467f94468943700c6c0f2a6fd802fcedec017c'
for p,h in json.loads((N/'custody.json').read_text())['files'].items():pins[str((N/p).relative_to(ROOT))]=h
for p,h in pins.items():need(sha(ROOT/p)==h,'prepin '+p)
for p in [N/'engine.py',N/'test_engine.py',B/'replay_gate.py',B.parent/'d125-hybrid81-caller-repair-gate-sol56-20260907/gate_checks.py']:
    need(not any(isinstance(x,ast.Assert) for x in ast.walk(ast.parse(p.read_text()))),'Assert '+str(p))
tree=ast.parse((N/'engine.py').read_text());f=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='alarm_script')
need(len(ast.literal_eval(f.body[0].value).encode('ascii'))==102,'alarm prose correction')
start=time.monotonic();runs=[]
for opt in ([],['-O']):
    for name,cwd,args in [('caller',B,[str(B/'replay_gate.py')]),('helper',N,['-m','unittest','-v','test_engine'])]:
        p=subprocess.run([sys.executable,'-B']+opt+args,cwd=cwd,capture_output=True,timeout=30,preexec_fn=caps)
        need(p.returncode==0,'replay '+name+' '+p.stderr.decode())
        d=json.loads(p.stdout) if name=='caller' else None
        if d:
            need(d['status']=='PASS' and d['outcome_count']==33 and not p.stderr,'caller outcomes')
            for probe in d['probes']:
                need(not Path('/proc',str(probe['events'][0]['pid'])).exists(),'probe PID still exists')
        else:need(b'Ran 6 tests' in p.stderr and p.stderr.rstrip().endswith(b'OK'),'helper census')
        runs.append(dict(name=name,optimized=bool(opt),returncode=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode(),details=d))
for p,h in pins.items():need(sha(ROOT/p)==h,'postpin '+p)
out=dict(status='PASS_SCOPED',pins=pins,runs=runs,seconds=time.monotonic()-start,caller_scope='two named repairs, generic Linux/Python only',helper_scope='PREPARATION, six tiny tests only; different-model helper review and actual engine still required',corrections=['RUNS digest in sealed Sol prose/PINS has62hex; actual64hex explicitly charged','patch EOF two blank context lines omitted; exact source diff matches','helper alarm program102bytes, sealed producer prose107 is corrected by frozen sidecar'])
with OUT.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),runs=len(runs),seconds=out['seconds'],receipt_sha256=sha(OUT))))
