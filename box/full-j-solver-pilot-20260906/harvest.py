#!/usr/bin/env python3
"""Terminal-only strict harvest and compact custody; never reads foreign live jobs."""
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import subprocess
import tarfile
import time

root=Path('/home/ubuntu/full-j-solver-pilot-20260906')
source=Path('/home/ubuntu/factored-jacobian-pilot-20260906')
if socket.gethostname()!='ip-172-30-0-56' or Path.cwd()!=root:raise SystemExit('wrong worker/root')
def sha(path):
    d=hashlib.sha256()
    with Path(path).open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):d.update(chunk)
    return d.hexdigest()
def save(name,obj):
    with (root/name).open('x') as f:json.dump(obj,f,sort_keys=True,indent=2);f.write('\n')
jobs={}
for mode in ['singular','msolve']:
    telemetry=json.loads((root/(mode+'.telemetry.json')).read_text())
    if not telemetry.get('utc_end') or telemetry['child_returncode'] is None:raise SystemExit('nonterminal engine')
    jobs[mode]={'telemetry':telemetry,'launch':json.loads((root/(mode+'.launch.json')).read_text())}
ps=subprocess.check_output(['ps','-eo','pid=,pgid=,state='],text=True)
pgids={j['telemetry']['pgid'] for j in jobs.values()}
live=[line for line in ps.splitlines() if int(line.split()[1]) in pgids and not line.split()[2].startswith('Z')]
if live:raise SystemExit('registered group still live')

text=(root/'singular.stdout').read_text(errors='replace')
lines=text.splitlines()
markers=['ALL_ROWS_PARSED','BEGIN_SLIMGB','END_SLIMGB','BEGIN_RESULT','END_RESULT']
counts={s:sum(line.strip()==s for line in lines) for s in markers}
errors=[line for line in lines if re.match(r'^\s*\?',line)]
values={}
for key in ['GENERATORS','VARIABLES','REDUCE_ONE','BASIS_SIZE','DIMENSION','INPUT_REMAINDER_SIZE']:
    found=[line.strip().split('=',1)[1] for line in lines if line.strip().startswith(key+'=')]
    values[key]=found[0] if len(found)==1 else None
complete=(jobs['singular']['telemetry']['status']=='NORMAL_EXIT' and jobs['singular']['telemetry']['child_returncode']==0
          and all(counts[s]==1 for s in markers) and not errors and values['GENERATORS']=='1629' and values['VARIABLES']=='600'
          and values['INPUT_REMAINDER_SIZE']=='0' and (root/'singular/basis.sing').is_file())
verdict='INCOMPLETE_NO_UNIT_OR_PROPERNESS_RESULT'
if complete and values['REDUCE_ONE']=='0':verdict='ENGINE_EXACT_Q_UNIT_COMPLETE_FAMILY_ONLY'
elif complete and values['REDUCE_ONE']=='1':verdict='ENGINE_EXACT_Q_REDUCED_NONUNIT_REQUIRES_INDEPENDENT_CONFIRMATION'
jobs['singular'].update({'markers':counts,'values':values,'errors':errors,'complete_result':complete,'verdict':verdict})
mb=root/'msolve/basis.ms'
jobs['msolve'].update({'basis_exists':mb.exists(),'basis_bytes':mb.stat().st_size if mb.exists() else None,
    'complete_result':False,'verdict':'SIGNAL11_NO_MATHEMATICAL_RESULT' if jobs['msolve']['telemetry']['child_signal']==11 else 'NO_PROMOTED_RESULT'})

old=json.loads((source/'custody.json').read_text())
original=[]
for record in old['artifacts']:
    actual=sha(record['path'])
    if actual!=record['sha256']:raise SystemExit('original artifact changed: '+record['path'])
    original.append({'path':record['path'],'sha256':actual,'bytes':Path(record['path']).stat().st_size})
if len(original)!=54:raise SystemExit('unexpected original artifact census')
allocation=subprocess.check_output([str(root/'allocation_control')],text=True)
(root/'allocation.control.stdout').write_text(allocation)
gate=subprocess.check_output(['python3',str(root/'frontier_gate.py'),'--total-degrees','99','66','--purpose','frontier','--tag','full-j-solver-pilot-astra-20260906'],text=True)
(root/'frontier.json').write_text(gate)
save('results.json',{'schema':'JC2_FULL_J_SOLVER_RESULT/v1','jobs':jobs,'registered_groups_live':live,
    'all_row_modular_audit':json.loads((root/'modular.audit.json').read_text()),
    'allocation_overflow':{'original_count':2484540704,'required_count':6779508000,'original_bytes':9938162816,'required_bytes':27118032000,
        'static_defect_confirmed':True,'crash_stack_not_obtained':True,'full_retry_launched':False},
    'source_family':'actual total99/66 delta2 gauged stage8','properness_claim':False,'counterexample_claim':False})

artifacts=[]
for path in sorted(root.iterdir()):
    if path.is_file() and path.name not in ['custody.json','compact.tar.gz']:
        artifacts.append({'path':str(path),'bytes':path.stat().st_size,'sha256':sha(path)})
for name in ['singular/basis.sing','msolve/basis.ms','msolve-source/src/msolve/iofiles.c','msolve-source/src/msolve/msolve-data.h',
             'msolve-source/src/neogb/io.c','msolve-source/src/neogb/data.h','msolve-source/.libs/msolve',
             'msolve-source/src/msolve/.libs/libmsolve.so.3.0.7','msolve-source/src/neogb/.libs/libneogb.so.3.0.7']:
    path=root/name
    if path.is_file():artifacts.append({'path':str(path),'bytes':path.stat().st_size,'sha256':sha(path)})
save('custody.json',{'schema':'JC2_FULL_J_SOLVER_CUSTODY/v1','status':'TERMINAL_ROOT_CUSTODY','utc_end':time.time(),
    'worker':{'instance_id':'i-0da0cebfc97c9fd54','private_ip':'172.30.0.56','hostname':socket.gethostname(),'type':'r7i.8xlarge',
              'retained':True,'owner':'/root','termination_authorized':False},
    'scratch':str(root),'all_task_writers_done_after_this_harvest':True,'registered_process_groups_empty':True,
    'source_originals_all54_unchanged':original,'jobs':jobs,'artifacts':artifacts,
    'source_custody_sha256':sha(source/'custody.json'),
    'independent_gate_sha256':'c01996800fbb4084a640770f1edd21092fe2b23ae1e3b50281477767e5488535',
    'package_changes':json.loads((root/'apt.custody.json').read_text()),
    'scope':{'variables':600,'rows':1629,'terms':11299180,'field_exact':'Q','order':'global dp','modular_prime':1073741827,
             'all_rows_retained':True,'variables_removed':[],'gauge_J0_equals1':False,'properness_claim':False}})

# Host receives only selected small artifacts; all dense streams stay worker-side.
chosen=[]
for path in sorted(root.iterdir()):
    if path.is_file() and path.stat().st_size<=1024*1024 and not path.name.startswith('complete.') and path.name!='compact.tar.gz':
        chosen.append(path)
for name in ['msolve-source/src/msolve/iofiles.c','msolve-source/src/msolve/msolve-data.h','msolve-source/src/neogb/io.c','msolve-source/src/neogb/data.h']:
    chosen.append(root/name)
total=sum(p.stat().st_size for p in chosen)
if total>8*1024*1024:raise SystemExit('compact host budget exceeded')
with tarfile.open(root/'compact.tar.gz','w:gz') as tf:
    for path in chosen:tf.add(path,arcname=str(path.relative_to(root)),recursive=False)
print(json.dumps({'results':str(root/'results.json'),'custody_sha256':sha(root/'custody.json'),
    'compact_bytes':(root/'compact.tar.gz').stat().st_size,'uncompressed_host_bytes':total,'jobs':{k:v['verdict'] for k,v in jobs.items()}},sort_keys=True))
