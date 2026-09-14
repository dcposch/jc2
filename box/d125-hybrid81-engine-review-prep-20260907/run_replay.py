"""Bounded terminal gate replay and current-pin harvest; no engine work."""
import hashlib,json,subprocess,sys,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
receipt=ROOT/'xmodel/d125-hybrid81-caller-repair-gate-sol56-20260907.run.v2'
fields=dict(line.split('=',1) for line in receipt.read_text().splitlines() if '=' in line)
if fields['final_status']!='DONE' or fields['exit_code']!='0': raise RuntimeError('not terminal')
pins={}
for i in range(1,11):
    key='charged_input_'+str(i);p=ROOT/fields[key]
    if fields[key+'_post']!='UNCHANGED' or digest(p)!=fields[key+'_sha256']: raise RuntimeError('charged pin')
    if digest(HERE/'inputs'/p.name)!=digest(p): raise RuntimeError('replay copy pin')
    pins[str(p.relative_to(ROOT))]=digest(p)
# RUNS actual pin: report/PINS omit one "cd" (62 hex digits); retained as a
# named transcription defect, not silently treated as a matching reported pin.
for name,expected in [('PINS.json','a0f457d3569d16393e2a410083f368901f67b9ea181654b8834bf997aae2067b'),('RUNS.json','0a42d8b7a459cdcdcd78b744fc9708b1fa5b32ab6d0e62d26201fc90bcbeebfc'),('gate_checks.py','6006db6bea500abc12182b33db07dd9e1ba6767f4f0bb6a8645ddb9c8799c816')]:
    p=HERE.parent/'d125-hybrid81-caller-repair-gate-sol56-20260907'/name
    if digest(p)!=expected: raise RuntimeError('reviewer artifact pin')
    pins[str(p.relative_to(ROOT))]=expected
report=ROOT/fields['report']
if digest(report)!=fields['report_sha256']: raise RuntimeError('report pin')
pins[str(report.relative_to(ROOT))]=digest(report)
pins[str(receipt.relative_to(ROOT))]=digest(receipt)
results=[]
for mode in ('normal','optimized'):
    argv=['timeout','--signal=KILL','30s','prlimit','--as=536870912','--cpu=25','--',sys.executable,'-B']
    if mode=='optimized': argv+=['-O']
    argv+=[str(HERE/'replay_gate.py')]
    started=time.monotonic();r=subprocess.run(argv,cwd=HERE,capture_output=True,timeout=32)
    for suffix,data in [('stdout',r.stdout),('stderr',r.stderr)]:
        with (HERE/(mode+'.'+suffix)).open('xb') as f:f.write(data)
    if r.returncode!=0 or r.stderr: raise RuntimeError('replay failed '+mode+': '+r.stderr.decode())
    parsed=json.loads(r.stdout)
    if parsed['status']!='PASS' or parsed['outcome_count']!=33: raise RuntimeError('replay census')
    results.append({'mode':mode,'argv':argv,'returncode':r.returncode,'wall_seconds':time.monotonic()-started,'metrics':parsed['metrics'],'outcomes':33})
for p,h in pins.items():
    if digest(ROOT/p)!=h:raise RuntimeError('post-replay drift')
with (HERE/'replay-results.json').open('xb') as f:f.write(json.dumps({'status':'PASS','pins':pins,'runs':results,'engine_executed':False},indent=2,sort_keys=True).encode()+b'\n')
print(json.dumps({'status':'PASS','runs':results},sort_keys=True))
