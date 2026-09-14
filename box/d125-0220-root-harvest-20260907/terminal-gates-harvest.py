"""Root terminal pins and tiny controls only; no worker or full row arithmetic."""
import ast, hashlib, importlib.util, json, resource, subprocess, sys, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
TAG = 'd125-zero-k-classification-gate-fable5-20260907'
GATE = ROOT / 'box' / TAG / 'gate_controls.py'
LOW = ROOT / 'box/d125-low-jet-saturation-discriminator-20260907'
ATTEMPT = ROOT / 'box/d125-parity-construction-attempt-20260907'
def need(ok, msg):
    if not ok: raise ValueError(msg)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def receipt():
    return dict(line.split('=', 1) for line in (ROOT/'xmodel'/f'{TAG}.run.v2').read_text().splitlines() if '=' in line)
def caps():
    resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
    resource.setrlimit(resource.RLIMIT_AS, (512 << 20,)*2)
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
if len(sys.argv) > 1 and sys.argv[1] == '--gate-child':
    caps()
    r = receipt()
    aliases = {r[f'charged_input_{i}_basename']: ROOT/r[f'charged_input_{i}'] for i in range(1, 14)}
    class FrozenAliases:
        def __truediv__(self, name): return aliases[name]
    spec = importlib.util.spec_from_file_location('frozen_gate', GATE)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    mod.FROZEN = FrozenAliases()
    mode = sys.argv[2]
    if mode == '--root-factor-only':
        # The frozen shared mutation stops at C3 before reaching C5. Bypass
        # exactly that scalar diagnostic for this separately labelled C5 test.
        original_need = mod.need
        def factor_need(ok, msg):
            if msg == 'same-field scalar r=g5/f3^2 normalizes both tops': return
            original_need(ok, msg)
        mod.need = factor_need
        mode = '--mutate-wrong-factor'
    print(json.dumps(mod.run(mode), sort_keys=True, indent=1))
    sys.exit(0)
r = receipt()
need(r['final_status']=='DONE' and r['exit_code']=='0' and r['report_state']=='BODY_SEALED' and r['seal_boundary']=='CLEAN' and r['charge_basis_status']=='ABSENT', 'terminal lane receipt')
pins = {}
def pin(path, value):
    need(path not in pins or pins[path] == value, 'inconsistent pin '+path)
    pins[path] = value
for i in range(1,14):
    need(r[f'charged_input_{i}_post']=='UNCHANGED', 'changed review input')
    pin(r[f'charged_input_{i}'], r[f'charged_input_{i}_sha256'])
pin(r['report'], '68e04e8ce62585b824d73749b956f51ea58a46661375e4c810d747680be5370f')
need(r['report_sha256']==pins[r['report']], 'report receipt pin')
for p in (GATE, GATE.parent/'witness.json', GATE.parent/'witness-O.json', GATE.parent/'replay.json', ROOT/'xmodel'/f'{TAG}.run.v2'):
    pin(str(p.relative_to(ROOT)), sha(p))
need(sha(ATTEMPT/'pins.json')=='033456f54a8a79d48d52a59b7557317e1ba574e29eb584890b49793dec96eb40', 'attempt pins index')
for p,h in json.loads((ATTEMPT/'pins.json').read_bytes())['pins'].items(): pin(p,h)
pin('xmodel/d125-parity-construction-attempt-astra-20260907.md', 'd4f0ccc486fcc2f69f1901d4050cc1756de7f39ba2ccd28ed96cc39bb6dca284')
need(sha(LOW/'custody.json')=='8e936a614cf610ef1ebd1082d8fb89e3a5db56c112c673fed642d3f4e839070a', 'low custody')
c = json.loads((LOW/'custody.json').read_bytes())
for section in ('owned','inputs'):
    for p,item in c[section].items(): pin(p,item['sha256'])
pin('xmodel/d125-low-jet-saturation-discriminator-astra-20260907.md', c['report']['sha256'])
def verify():
    for p,h in pins.items(): need(sha(ROOT/p)==h, 'pin '+p)
verify()
for p in (GATE, LOW/'check.py', ATTEMPT/'verify_custody.py', Path(__file__)):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(p.read_bytes()))), 'Assert '+str(p))
start = time.monotonic(); runs=[]
def run(label, args, error=None, expected_hash=None):
    p = subprocess.run(args,capture_output=True,timeout=30,preexec_fn=caps)
    need((p.returncode != 0)==bool(error), 'unexpected exit '+label)
    if error: need(error in p.stderr, 'wrong mutation reason '+label)
    if expected_hash: need(hashlib.sha256(p.stdout).hexdigest()==expected_hash, 'witness '+label)
    runs.append(dict(label=label,argv=args,returncode=p.returncode,stdout_sha256=hashlib.sha256(p.stdout).hexdigest(),stderr=p.stderr.decode()))
for flags in ([],['-O']):
    for mode, error in [('',None),('--mutate-source-face',b'exactly three lower generator slots'),('--mutate-missing-negative-row',b'omitted negative row'),('--mutate-wrong-factor',b'same-field scalar'),('--root-factor-only',b'pure order two [R,E], factor -1/3')]:
        run('classification '+str(flags)+' '+mode,[sys.executable,'-B',*flags,str(Path(__file__).resolve()),'--gate-child',mode],error,
            None if error else '1461b907f837402cbeb2cf0bca3c1b99e669fd5fd4213e0affa73aa3279d5b2d')
    for mode,error in [('',None),('--mutate-omit-A1B3',b'missing A1-B3 contributions'),('--mutate-certificate-sign',b'k4 h2 certificate'),('--mutate-raw-equivalence',b'unguarded equivalence is false')]:
        run('low rows '+str(flags)+' '+mode,[sys.executable,'-B',*flags,str(LOW/'check.py')]+([mode] if mode else []),error,
            None if error else '37fc6434e2020d4580bf7401f0ed1eefde80778d6165e2cb406bbd045a1c92ca')
run('construction terminal custody NORMAL ONLY',[sys.executable,'-B',str(ATTEMPT/'verify_custody.py')])
verify()
result=dict(status='PASS',pins=pins,runs=runs,wall_seconds=time.monotonic()-start,
            scope='terminal custody, degree-five and R=g review controls, degree-three low rows only; no old forbidden checker execution',
            correction='Frozen wrong-factor mutation stops at C3. Root separately bypasses only C3 scalar diagnostic to test actual C5 pure-order-two factor.')
dest=OUT/'terminal-gates-harvest.json'
with dest.open('x') as f: json.dump(result,f,sort_keys=True,indent=2);f.write('\n')
print(json.dumps(dict(status='PASS',pins=len(pins),runs=len(runs),wall_seconds=result['wall_seconds'],receipt_sha256=sha(dest))))
