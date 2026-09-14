#!/usr/bin/env python3
"""Refresh final custody while retaining previously passed static audit checks."""
import datetime, hashlib, json, subprocess
from pathlib import Path
BASE=Path('/home/ubuntu/jc2/box/char-degree-20260905/resume-r2')
remote=r'''
import datetime,hashlib,json
from pathlib import Path
BASE=Path('/home/ubuntu/jc2/box/char-degree-20260905')
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  while b:=f.read(1024*1024):h.update(b)
 return h.hexdigest()
out=[]
for stage in range(9):
 for branch in ('delta2','delta52'):
  d=BASE/'g9966/circuit-runs'/f'{branch}_stage{stage}'
  ep=d/'execution.json';mp=d/'augmented.circuit.json';sp=d/'augmented.sing';op=d/'augmented.circuit.out'
  ex=json.loads(ep.read_text());meta=json.loads(mp.read_text())
  assert sha(sp)==meta['script_sha256']
  assert sha(Path(meta['input']))==meta['input_sha256']
  assert sha(BASE/'d108/coefficient_circuit_backend_v2.py')==meta['driver_sha256']
  out.append({'branch':branch,'stage':stage,'execution':ex,'metadata':{k:v for k,v in meta.items() if k!='ring_generator_order'},'execution_sha256':sha(ep),'metadata_sha256':sha(mp),'output':op.read_text(),'output_sha256':sha(op)})
rp=BASE/'resume-r2/resource-observations.json'
print(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':out,'resources':json.loads(rp.read_text()),'resources_sha256':sha(rp)}))
'''
proc=subprocess.run(['ssh','-i',str(Path.home()/'.ssh/jc2-fleet'),'ubuntu@172.30.0.40','python3','-'],input=remote,text=True,capture_output=True,timeout=60)
assert proc.returncode==0,proc.stderr
fresh=json.loads(proc.stdout)
path=BASE/'audit-99.json';old=json.loads(path.read_text());by={(r['branch'],r['stage']):r for r in old['records']}
for row in fresh['records']:
 o=by[(row['branch'],row['stage'])];meta=row['metadata'];ex=row['execution']
 assert o['script_sha256']==meta['script_sha256'] and o['input_sha256']==meta['input_sha256']
 assert o['backend_sha256']==meta['driver_sha256']
 o.update(status=ex['status'],metadata_sha256=row['metadata_sha256'],execution_sha256=row['execution_sha256'],
   driver_rc=ex.get('returncode'),cas_rc=meta.get('cas',{}).get('returncode'),total_wall_seconds=ex.get('elapsed_seconds'),
   backend_phases=meta['phases'],output=row['output'],output_sha256=row['output_sha256'],
   in_run_controls=meta.get('cas',{}).get('controls',[]),
   acceptance='COMPUTE-BOUND: no END_GB/END_RESULT, no unit or properness read' if 'END_RESULT' not in row['output'] else 'REQUIRES_PARENT_REVIEW')
 observed=[r for r in fresh['resources']['records'] if o['script'] in r['args']]
 if observed:
  o.update(rss_observations=observed,rss_kib=max(r['max_observed_VmHWM_kib'] for r in observed),
   rss_note='Observed process VmHWM through last parent-monitor sample, a lower bound on eventual peak, not an exact final peak.')
old.update(receipt_refresh_utc=fresh['utc'],resource_observations_updated_utc=fresh['resources']['updated_utc'],
  resource_observations_sha256=fresh['resources_sha256'],
  refresh_note='Static checks retained only after recomputing unchanged script, input and backend hash relationships.')
path.write_text(json.dumps(old,indent=2,sort_keys=True)+'\n')
print(json.dumps({'utc':fresh['utc'],'states':[(r['branch'],r['stage'],r['status'],r.get('total_wall_seconds'),r['rss_kib']) for r in old['records']]},indent=2))
