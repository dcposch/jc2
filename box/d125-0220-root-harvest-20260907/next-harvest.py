"""Root capped replays of three terminal packets, never full construction."""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
ZERO=ROOT/'box/d125-zero-k-deformation-discriminator-20260907'
READY=ROOT/'box/d125-parity-pilot-readiness-20260907'
GATE=ROOT/'box/d125-parity-compression-code-gate-sol56-20260907'
def need(ok,why):
    if not ok: raise ValueError(why)
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def receipt():
    return dict(line.split('=',1) for line in (ROOT/'xmodel/d125-parity-compression-code-gate-sol56-20260907.run.v2').read_text().splitlines() if '=' in line)
def aliases():
    r=receipt()
    return {r[f'charged_input_{i}_basename']:ROOT/r[f'charged_input_{i}'] for i in range(1,14)}
if len(sys.argv)>1 and sys.argv[1]=='control':
    spec=importlib.util.spec_from_file_location('root_sol_control',GATE/'control.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    class Alias:
        def __truediv__(self,name): return aliases()[name]
    m.LANE=Alias()
    m.main(sys.argv[2])
    raise SystemExit(0)

need(sha(ZERO/'custody.json')=='e92749c203e8d4bb5d2b21b6c7f9b16b69166a8debc4a5bf127392dbb045f3d6','zero custody')
need(sha(READY/'pins.json')=='51c5baf0891fc6d9d3e8bac333feb5a9d1de68f860c54e3d360df354573b5686','readiness pins')
need(sha(GATE/'control.py')=='019296660fd6e91431908197811b52c42e8984cf74fb121518eca3bc92af0547','independent control')
pins=json.loads((READY/'pins.json').read_bytes())['pins']
z=json.loads((ZERO/'custody.json').read_bytes())
for section in ('inputs','owned'):
    pins.update({k:v['sha256'] for k,v in z[section].items()})
r=receipt()
need(r['final_status']=='DONE' and r['exit_code']=='0' and r['seal_boundary']=='CLEAN' and r['report_state']=='BODY_SEALED','terminal code gate')
for i in range(1,14):
    need(r[f'charged_input_{i}_post']=='UNCHANGED','lane post pin')
    pins[r[f'charged_input_{i}']]=r[f'charged_input_{i}_sha256']
pins[r['report']]=r['report_sha256']
pins[str((GATE/'control.py').relative_to(ROOT))]='019296660fd6e91431908197811b52c42e8984cf74fb121518eca3bc92af0547'
def verify():
    for p,h in pins.items(): need(sha(ROOT/p)==h,'pin drift '+p)
verify()
for p in pins:
    if p.endswith('.py') and ('zero-k-deformation' in p or 'parity-pilot-readiness' in p or 'code-gate-sol56' in p):
        need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((ROOT/p).read_bytes()))),'Assert '+p)
def cap():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
    resource.setrlimit(resource.RLIMIT_CORE,(0,0))
start=time.monotonic();runs=[]
def run(flags,path,args=(),expected=0,message=None):
    p=subprocess.run([sys.executable,'-B',*flags,str(path),*args],cwd=path.parent,capture_output=True,timeout=30,preexec_fn=cap)
    need(p.returncode==expected if expected==0 else p.returncode!=0,'unexpected exit '+str(path))
    if message: need(message in p.stderr,'wrong test/mutation reason')
    runs.append(dict(path=str(path.relative_to(ROOT)),flags=flags,args=list(args),rc=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
    return p
for flags in ([],['-O']):
    for mode,message in [('',None),('--mutate-R',b'changed R breaks ordinary lift'),('--mutate-second-factor',b'second-order coefficient factor'),('--mutate-omit-faces',b'omitted moving faces accepted dependent jet')]:
        p=run(flags,ZERO/'check.py',[mode] if mode else [],1 if mode else 0,message)
        if not mode: need(hashlib.sha256(p.stdout).hexdigest()=='fac3910177f640869e69517e266126ce08f54f0950061e4b50a5eada53f336ee','boundary witness')
    for folder,name,count in [('d125-parity-compression-code-prep-20260907','test_construct.py',13),('d125-parity-compression-pilot-prep-20260907','test_once.py',6),('d125-parity-pilot-readiness-20260907','test_host_control.py',6)]:
        p=run(flags,ROOT/'box'/folder/name,['-v'],message=f'Ran {count} tests'.encode())
        need(p.stderr.endswith(b'\nOK\n'),'unittest status')
    target=OUT/('sol-control-root-O.json' if flags else 'sol-control-root.json')
    run(flags,Path(__file__),['control',str(target)])
    data=json.loads(target.read_bytes())
    need(data['status']=='PASS_TINY_INDEPENDENT_NO_PRODUCTION' and data['counts']['original_rows']==803 and len(data['mutations_rejected'])==10,'independent census/control')
verify()
result=dict(status='PASS',pins=pins,runs=runs,wall_seconds=time.monotonic()-start,scope='boundary tiny controls; code gate tiny independent replay; mock host readiness only. No AWS or production.')
with (OUT/'next-harvest.json').open('x') as f:
    json.dump(result,f,indent=2,sort_keys=True);f.write('\n')
print(json.dumps(dict(status='PASS',pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(OUT/'next-harvest.json'))))
