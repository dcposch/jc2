"""Root terminal harvest: two reviews, tuned proof controls, disabled readiness."""
import sys
sys.dont_write_bytecode = True
import ast, hashlib, json, resource, subprocess, time
from pathlib import Path
ROOT=Path('/home/ubuntu/jc2')
OUT=ROOT/'box/d125-0220-root-harvest-20260907/0644-harvest.json'
def need(c,s):
    if not c: raise RuntimeError(s)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
pins={}; runs=[]; started=time.monotonic()
def run(args,label,want=0,fragment=None,witness=None):
    p=subprocess.run([sys.executable,'-B']+args,cwd=ROOT,capture_output=True,timeout=30,preexec_fn=caps)
    need((p.returncode==0)==(want==0),label+' exit '+str(p.returncode))
    if fragment: need(fragment.encode() in p.stderr,label+' wrong failure')
    if witness: need(hashlib.sha256(p.stdout).hexdigest()==witness,label+' witness drift')
    runs.append(dict(label=label,rc=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
    return p
for tag,wanted in [('d125-hybrid81-solver-gate-sol56-20260907','b4198c3689e0d713eca6a1a7dfe95854f88bb48f45217b737adb29e03c4fcc46'),('d125-exceptional-center-gate-fable5-20260907','1cfb57436ff94945ccb642ad96b51f783d15cc2bacfca3e4ee3dfdd4ef2e21d6')]:
    r=dict(line.split('=',1) for line in (ROOT/'xmodel'/ (tag+'.run.v2')).read_text().splitlines() if '=' in line)
    need(r['final_status']=='DONE' and r['exit_code']=='0' and r['report_state']=='BODY_SEALED' and r['charge_basis_status']=='ABSENT','terminal receipt')
    need(r['seal_boundary'] in ('CLEAN','CLEAN_SEALED'),'seal boundary')
    need(r['report_sha256']==wanted,'report receipt binding')
    pins[r['report']]=wanted
    for i in range(1,int(r['charged_inputs'])+1):
        key='charged_input_'+str(i)
        need(r[key+'_post']=='UNCHANGED','post input')
        pins[r[key]]=r[key+'_sha256']
S=ROOT/'box/d125-hybrid81-solver-gate-sol56-20260907'
sp=json.loads((S/'PINS.json').read_text())
for name,h in sp['own_artifacts'].items(): pins[str((S/name).relative_to(ROOT))]=h
for name in ('exact.py','hybrid.py','driver.py','test_exact.py','test_hybrid.py'):
    pins[str((S/'copy'/name).relative_to(ROOT))]=sp['frozen_inputs'][name]
E=ROOT/'box/d125-exceptional-center-gate-fable5-20260907'
for line in (E/'own_artifacts.sha256').read_text().splitlines():
    h,name=line.split(None,1);pins[str((E/name.strip()).relative_to(ROOT))]=h
T=ROOT/'box/d125-exceptional-tuned-discriminator-20260907'
tc=json.loads((T/'custody.json').read_text())
need(tc['status']=='TERMINAL' and tc['all_writers_finished'],'tuned terminal')
for item in tc['inputs']+tc['owned']: pins[item['path']]=item['sha256']
pins[str((T/'custody.json').relative_to(ROOT))]='53f42d167e47477006c09e147e98bb2997b7df09c4226a253822289a725869f3'
R=ROOT/'box/d125-hybrid81-solver-readiness-20260907'
pins['xmodel/d125-hybrid81-solver-readiness-astra-20260907.md']='60844a0842f4484210644e435c14f680634db39ab5cb244604e26e3de8a7aa49'
pins['xmodel/d125-hybrid81-solver-readiness-astra-20260907.md.artifact.json']='0d1c99c68aa84d546d66f52f2a0ab44b82f02b6bc8dfd0ffbb86257dc85ae503'
pins[str((R/'READINESS.md').relative_to(ROOT))]='aca30ac4e95b2eeb7a6bd67d48939284d81d12586bb0744c5ce39c7e601e5549'
pins[str((R/'REUSE.json').relative_to(ROOT))]='78eea04c20c8658c5d00b8dfa29ba3857cb06f1b33731014bec3b6985a7fafba'
for p,h in pins.items():need(sha(ROOT/p)==h,'prepin '+p)
for path in (S/'gate_controls.py',E/'gate_controls.py',T/'check.py',ROOT/'box/d125-zero-k-deformation-discriminator-20260907/check.py'):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(path.read_text()))),'Assert '+str(path))
for report in ('d125-exceptional-tuned-discriminator-astra-20260907','d125-hybrid81-solver-readiness-astra-20260907'):
    run(['ops/artifact_finalize.py','verify','--final','xmodel/'+report+'.md'],'transaction '+report)
emodes=[('',None),('--mutate-delta-sign','G1'),('--mutate-shear-no-gamma','G2'),('--mutate-even-f','G4'),('--mutate-omit-lift-row','G6'),('--mutate-drop-p3','G7'),('--mutate-omit-low-A','G8')]
tmodes=[('',None),('--mutate-quadratic-factor','complete polynomial identity'),('--mutate-omit-cross','complete polynomial identity'),('--mutate-omit-reference-cross','reference removal retains'),('--mutate-omit-p3-reference','both low-A and p3 reference')]
for opt in ([],['-O']):
    for mode,msg in emodes:
        run(opt+[str(E/'gate_controls.py')]+([mode] if mode else []),'exception '+str(opt)+' '+mode,want=bool(msg),fragment=msg,witness=None if msg else '7883cffee63edc3276933f72797fc8714fa53efafa9a80d55332ff0e88b774be')
    for mode,msg in tmodes:
        run(opt+[str(T/'check.py')]+([mode] if mode else []),'tuned '+str(opt)+' '+mode,want=bool(msg),fragment=msg,witness=None if msg else 'dbbcf4b8beb0578d49bc5de6aa426275cdfacbfd613abe5b9e09ffa0f0d56373')
    p=run(opt+[str(S/'gate_controls.py')],'Sol '+str(opt))
    d=json.loads(p.stdout)
    need(d['test_count']==23,'Sol count')
    for name in ('posthash_receipt_bypass_present','deadline_handoff_stale_allowance_present'):
        need(d['tests'][name]['status']=='BUG_CONFIRMED','Sol actual caller finding')
for p,h in pins.items():need(sha(ROOT/p)==h,'postpin '+p)
out=dict(status='PASS_SCOPED_HARVEST',pins=pins,runs=runs,wall_seconds=time.monotonic()-started,
         conclusions=['exceptional delta nonzero finite-arc exclusion confirmed with checker-scope corrections','tuned alpha nonzero finite-arc obstruction provisional','hybrid adapter confirmed, caller two lifecycle bugs confirmed; no dispatch','readiness disabled, no remote state observation'],
         scope='No full source arithmetic, actual CAS, new worker authority, guarded emptiness or JC2 proof')
with OUT.open('x') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status=out['status'],pins=len(pins),runs=len(runs),wall_seconds=out['wall_seconds'],receipt_sha256=sha(OUT))))
