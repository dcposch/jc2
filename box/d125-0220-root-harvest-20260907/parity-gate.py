"""Replay terminal Fable parity gate with explicit relocated immutable inputs."""
import ast
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import subprocess
import sys
import time
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
TAG = 'd125-symmetry-delta-gate-fable5-20260907'
S = ROOT/'box'/TAG
def need(ok, why):
    if not ok:
        raise ValueError(why)
def sha(data):
    return hashlib.sha256(data).hexdigest()
receipt = dict(line.split('=',1) for line in (ROOT/'xmodel'/f'{TAG}.run.v2').read_text().splitlines() if '=' in line)
for key,value in {'final_status':'DONE','exit_code':'0','seal_boundary':'CLEAN','report_state':'BODY_SEALED','charge_basis_status':'ABSENT'}.items():
    need(receipt[key] == value, 'terminal receipt '+key)
pins = {receipt['report']:receipt['report_sha256']}
aliases = {}
for i in range(1,int(receipt['charged_inputs'])+1):
    k = f'charged_input_{i}'
    need(receipt[k+'_post'] == 'UNCHANGED', 'post drift')
    pins[receipt[k]] = receipt[k+'_sha256']
    aliases[receipt[k+'_basename']] = ROOT/receipt[k]
pins.update({str((S/name).relative_to(ROOT)): digest for name,digest in {
    'delta_check.py':'da93d650b8a4cd4b434a6cd0b2959057fe244c627b8d5ae6656f3f8185494588',
    'delta-witness.json':'f124fa364c2c31dcc3c61a06fa014adc52a6953c04bb67a2afe0b9039760ea25',
    'delta-witness-O.json':'f124fa364c2c31dcc3c61a06fa014adc52a6953c04bb67a2afe0b9039760ea25',
    'delta-replay.json':'0364430caf77a18a8dd1ef6dd9746cd66d65c772735ef6ade1979e0d4f7b1813'}.items()})
def verify():
    for name,digest in pins.items():
        need(sha((ROOT/name).read_bytes()) == digest, 'pin '+name)
verify()
for path in (S/'delta_check.py',Path(__file__)):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(path.read_bytes()))), 'Assert gate')
class RelocatedInputs:
    def __truediv__(self, name):
        return aliases[name]
if len(sys.argv)>1 and sys.argv[1]=='--child':
    spec=importlib.util.spec_from_file_location('fable_parity_delta',S/'delta_check.py')
    m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m.FROZEN=RelocatedInputs()
    mutation=sys.argv[2] if len(sys.argv)>2 else ''
    print(json.dumps(m.main(mutation),sort_keys=True,indent=1,default=str))
    verify()
    raise SystemExit(0)
def cap():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,)*2)
start=time.monotonic(); runs=[]
for flags in ([],['-O']):
    for mutation in ('','--mutate-lambda-weight','--mutate-source-action','--mutate-shear-sign'):
        p=subprocess.run([sys.executable,'-I','-B',*flags,str(Path(__file__).resolve()),'--child',mutation],capture_output=True,timeout=30,preexec_fn=cap)
        need(p.returncode==(1 if mutation else 0),'expected exit')
        if mutation:
            message=b'shear kernel-slot action' if mutation=='--mutate-shear-sign' else b'source action covariance'
            need(message in p.stderr and not p.stdout,'mutation reason')
        else:
            need(not p.stderr and sha(p.stdout)=='f124fa364c2c31dcc3c61a06fa014adc52a6953c04bb67a2afe0b9039760ea25','positive witness')
        runs.append({'flags':flags,'mutation':mutation,'returncode':p.returncode,'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr)})
verify()
result={'status':'PASS','pins':pins,'runs':runs,'wall_seconds':time.monotonic()-start,
        'private_snapshot_exists':Path(receipt['lane_inputs_dir']).exists(),'relocated_input_paths':{k:str(v) for k,v in aliases.items()},
        'assert_nodes':0,'scope':'independent parity fixed-locus/composition delta; small exact numeric controls, not full symbolic rows'}
with (OUT/'parity-gate.json').open('x') as f:
    json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),'wall_seconds':result['wall_seconds'],
                  'receipt_sha256':sha((OUT/'parity-gate.json').read_bytes())}))
