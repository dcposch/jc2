#!/usr/bin/env python3
"""Root terminal receipt/pin and bounded independent desk-control harvest."""
import ast
import hashlib
import json
from pathlib import Path
import resource
import subprocess
import sys
import time
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
TAG = 'd125-defect-order-gate-fable5-20260907'
G = ROOT/'box'/TAG
M = ROOT/'box/d125-higher-moment-discriminator-20260907'
def sha(data):
    return hashlib.sha256(data).hexdigest()
def need(ok, why):
    if not ok:
        raise ValueError(why)
receipt = dict(line.split('=',1) for line in (ROOT/'xmodel'/f'{TAG}.run.v2').read_text().splitlines())
need(receipt['final_status']=='DONE' and receipt['exit_code']=='0' and
     receipt['report_state']=='BODY_SEALED' and receipt['seal_boundary']=='CLEAN' and
     receipt['charge_basis_status']=='ABSENT', 'terminal receipt')
pins = {}
snapshot_checks = {}
for i in range(1,8):
    name = receipt[f'charged_input_{i}']
    pins[name] = receipt[f'charged_input_{i}_sha256']
    need(receipt[f'charged_input_{i}_post']=='UNCHANGED','post input')
    snapshot = Path(receipt['lane_inputs_dir'])/receipt[f'charged_input_{i}_basename']
    if snapshot.exists():
        need(sha(snapshot.read_bytes())==pins[name], 'snapshot '+name)
        snapshot_checks[name] = 'MATCH'
    else:
        snapshot_checks[name] = 'TEMP_SNAPSHOT_REMOVED; current pin and terminal post receipt checked'
for key in ('prompt','adapter','launcher','sandbox_profile','charge_basis_validator','seal_tool','fallacy','model_prompt'):
    need(receipt[key+'_sha256']==receipt['post_'+key+'_sha256'], 'tool/prompt drift '+key)
pins[receipt['report']] = receipt['report_sha256']
pins[str((G/'gate_own.py').relative_to(ROOT))] = '827d543cb9ab63cc24f1bcf04200d389b89d068256dad923cde468311bf2f3ba'
need(sha((M/'custody.json').read_bytes())=='30be624e34b9af0726bf6ff2c2a17d43af868bbca3e4c711de4e3bd19ea47318','moment custody')
for filename in ('custody.json','v2-inputs.json'):
    for row in json.loads((M/filename).read_bytes())['files']:
        pins[row['path']] = row['sha256']
def verify():
    for name,digest in pins.items():
        need(sha((ROOT/name).read_bytes())==digest, 'pin '+name)
verify()
for path in (G/'gate_own.py', M/'check.py'):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(path.read_bytes()))),'Assert gate')
wit = json.loads((ROOT/'box/d125-defect-order-discriminator-20260907/witnesses.json').read_bytes())
dp = {'field':'Q','order':'dp','variables':wit['order']['variables']}
dp_sha = sha((json.dumps(dp,sort_keys=True,separators=(',',':'))+'\n').encode())
need(dp_sha=='ccd93ccf39b0109a36dc89d54f1fd281bcef17b1dc5fab3c65f2988027333d73','dp descriptor digest, not ring-line digest')
def cap():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,)*2)
start = time.monotonic()
runs = []
for flags in ([],['-O']):
    for mutation in ('','w2','w3','envelope','tiebreak'):
        label = ('optimized' if flags else 'normal')+'-'+(mutation or 'positive')
        output = OUT/('fable-order-'+label+'.json')
        need(not output.exists(),'fresh output')
        argv = [sys.executable,*flags,str(G/'gate_own.py'),
                '--baseline',str(ROOT/'box/d125-small-source-exporter-prep-20260906/baseline.py'),
                '--witnesses',str(ROOT/'box/d125-defect-order-discriminator-20260907/witnesses.json'),
                '--out',str(output)]
        if mutation:
            argv += ['--mutate',mutation]
        p = subprocess.run(argv,capture_output=True,timeout=30,preexec_fn=cap)
        need(p.returncode==(1 if mutation else 0),'Fable exit '+label)
        if mutation:
            need(b'ValueError: REJECT:' in p.stderr and not output.exists(),'actual rejected object '+label)
        else:
            need(sha(output.read_bytes())=='4eaaf7032801e3a588499d9713183002dd2e3eb1f099c39cb6dcef77d72bc4b9','Fable witness exact')
        runs.append({'label':'order-'+label,'rc':p.returncode,'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr)})
    for mode in ('normal','mutate-index','mutate-denominator'):
        p = subprocess.run([sys.executable,*flags,str(M/'check.py'),mode],capture_output=True,timeout=30,preexec_fn=cap)
        need(p.returncode==(0 if mode=='normal' else 1),'moment exit')
        if mode=='normal':
            need(json.loads(p.stdout)['checks']==322 and p.stderr==b'','moment controls')
        else:
            need(b'ValueError:' in p.stderr,'moment mutation failure')
        runs.append({'label':'moment-'+repr(flags)+'-'+mode,'rc':p.returncode,'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr)})
verify()
record = {'status':'PASS','pins':pins,'runs':runs,'wall_seconds':time.monotonic()-start,
          'snapshot_checks':snapshot_checks,
          'preliminary_harness_failure':'Required expired temporary snapshot; failed before any arithmetic. Repaired to record absence and verify current and terminal post pins.',
          'dp_descriptor_sha256':dp_sha,'assert_nodes':0,
          'scope':'Fable order gate plus producer moment controls; no full source/CAS'}
with (OUT/'gate-harvest.json').open('x') as f:
    json.dump(record,f,indent=2,sort_keys=True)
    f.write('\n')
print(json.dumps({'status':'PASS','pins':len(pins),'runs':len(runs),
                  'wall_seconds':record['wall_seconds'],'receipt_sha256':sha((OUT/'gate-harvest.json').read_bytes())}))
