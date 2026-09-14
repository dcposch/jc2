"""Root replay of terminal independent low-row gate, never --record."""
import ast, hashlib, json, resource, subprocess, sys, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=Path(__file__).resolve().parent
TAG='d125-low-jet-saturation-gate-fable5-20260907'
BOX=ROOT/'box'/TAG
def need(ok,msg):
    if not ok: raise ValueError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
r=dict(x.split('=',1) for x in (ROOT/'xmodel'/f'{TAG}.run.v2').read_text().splitlines() if '=' in x)
need((r['final_status'],r['exit_code'],r['report_state'],r['seal_boundary'],r['charge_basis_status'])==('DONE','0','BODY_SEALED','CLEAN','ABSENT'),'receipt')
pins={}
for i in range(1,12):
    need(r[f'charged_input_{i}_post']=='UNCHANGED','post input')
    pins[r[f'charged_input_{i}']]=r[f'charged_input_{i}_sha256']
need(r['report_sha256']=='65bb46ee40c9dc7c873de732a333f000206c2efa4016be06e1f89b880effa583','report receipt')
pins[r['report']]=r['report_sha256']
pins[str((BOX/'gate_controls.py').relative_to(ROOT))]='2ce673dd76d6519d50a3a5a619676eee97ef9cee18a3870036144973bb30525e'
for p in (BOX/'witness.json',BOX/'witness-O.json',BOX/'replay.json',BOX/'input_pins.txt'):
    pins[str(p.relative_to(ROOT))]=sha(p)
def verify():
    for p,h in pins.items(): need(sha(ROOT/p)==h,'pin '+p)
verify()
need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((BOX/'gate_controls.py').read_bytes()))),'Assert')
def caps():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(512<<20,)*2)
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
start=time.monotonic();runs=[]
for flags in ([],['-O']):
    for mode,error in [('',None),('--mutate-wrong-sign',b'FAIL cert-k4-h2\n'),('--mutate-omit-A1B3',b'FAIL A1B3-terms\n'),('--mutate-false-unguarded-equivalence',b'FAIL false-unguarded-equivalence\n')]:
        p=subprocess.run([sys.executable,'-B',*flags,str(BOX/'gate_controls.py')]+([mode] if mode else []),capture_output=True,timeout=30,preexec_fn=caps)
        need(p.returncode==(1 if error else 0),'exit '+mode)
        if error: need(p.stderr==error,'exact first failing gate')
        else: need(sha(BOX/'witness.json')==hashlib.sha256(p.stdout).hexdigest()=='cc2f5336f63fe9dd9cf631bdaac17987d48ac393cd5db0d0e4cd7f19ff0e319e','positive bytes')
        runs.append(dict(flags=flags,mode=mode,returncode=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
verify()
result=dict(status='PASS',pins=pins,runs=runs,wall_seconds=time.monotonic()-start,
    scope='low Jacobian rows, truncated boundary coefficients, two degree-five inertness monomials; no full pair/source')
dest=OUT/'low-gate-harvest.json'
with dest.open('x') as f:json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status='PASS',pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(dest))))
