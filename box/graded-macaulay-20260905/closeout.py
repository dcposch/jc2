#!/usr/bin/env python3
"""Close custody after all computations finish; seal only checked results."""
from pathlib import Path
import datetime,hashlib,json,os,subprocess,sys
BASE=Path('box/graded-macaulay-20260905');START=datetime.datetime(2026,9,5,15,19,17,tzinfo=datetime.timezone.utc)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,indent=2)+'\n')
expected={77:(4,14),111:(6,14),129:(4,14),136:(6,12)};grids=[]
for n,(b,y) in expected.items():
 p=BASE/f'hilbert/hilbert_{n}_B{b}_Y{y}.json';d=json.loads(p.read_text());assert len(d['components'])==(b+1)*(y+1)
 for c in d['components']:
  assert c['status'] in ('EXACT_Q','EXACT_Q_VIA_HOMOGENEOUS_UNIT_MAP'),c
  assert c['hilbert_Q']==c['columns']-c['rank_Q']
  assert 0<=c['rank_Q']<=min(c['columns'],c['rows'])
 assert sha(d['original_direct_rows_path'])==d['original_direct_rows_sha256']
 grids.append({'fibre':n,'path':str(p),'sha256':sha(p),'components':len(d['components']),'direct_components':sum(c['status']=='EXACT_Q' for c in d['components']),'unit_map_components':sum(c['status']=='EXACT_Q_VIA_HOMOGENEOUS_UNIT_MAP' for c in d['components'])})
active=[]
for p in Path('/proc').iterdir():
 if not p.name.isdigit():continue
 try:args=(p/'cmdline').read_bytes().split(b'\0')
 except (OSError,PermissionError):continue
 targets=[b'box/graded-macaulay-20260905/hilbert/compute_hilbert.py',b'box/graded-macaulay-20260905/counts/reduced-hilbert/compute136.py',b'box/graded-macaulay-20260905/reduced/reduce_counts.py']
 if any(any(a.endswith(t) for t in targets) for a in args):active.append(int(p.name))
assert not active,active
assert subprocess.run(['sha256sum','-c',str(BASE/'inputs.sha256')],capture_output=True,text=True).returncode==0
now=datetime.datetime.now(datetime.timezone.utc);elapsed=(now-START).total_seconds();assert elapsed<=10800
status={'start_utc':START.isoformat(),'closeout_utc':now.isoformat(),'elapsed_seconds':elapsed,'deadline_utc':(START+datetime.timedelta(minutes=180)).isoformat(),'target_N2_N3_status':{str(n):'NOT_ASSEMBLED_INFEASIBLE_EXACT_SIZE' for n in expected},'target_membership':{str(n):{'c2':'OPEN','c3':'OPEN','radical':'OPEN'} for n in expected},'class_kills':0,'groebner_computations':0,'fleet_instances_launched':[],'fleet_instances_owned':[],'termination_obligation':'NONE_NO_WORKER_LAUNCHED_OR_ADOPTED','other_workers_used_or_terminated':[],'active_lane_computation_pids':active,'hilbert_grids':grids,'root_reduction_command':'python3 box/graded-macaulay-20260905/reduced/reduce_counts.py','root_reduction_observed_exit_code':0,'frozen_input_verification':'SIX_OK','source_mutations':[],'allowed_new_outputs':[str(BASE),'xmodel/graded-macaulay-astra-20260905.md']}
write(BASE/'run-status.json',status)
# Subtree manifests are independently checked before the encompassing manifest.
checks=[]
for rel in ['counts/ambient-counts.sha256','counts/reduced-ambient-counts.sha256','counts/independent-reduced-check.sha256','counts/reduced-hilbert/artifacts.sha256','hilbert/SHA256SUMS']:
 p=BASE/rel
 if p.exists():
  r=subprocess.run(['sha256sum','-c',str(p)],capture_output=True,text=True);assert r.returncode==0,(p,r.stdout,r.stderr);checks.append({'path':str(p),'returncode':r.returncode,'checked_files':len(r.stdout.splitlines())})
write(BASE/'manifest-subchecks.json',checks)
# Remove only this script family's ephemeral draft; final report is separate.
(BASE/'report-draft.md').unlink(missing_ok=True)
excluded={'artifacts.sha256','artifacts-check.log','seal-verification.json'}
files=sorted(p for p in BASE.rglob('*') if p.is_file() and '__pycache__' not in p.parts and not (p.parent==BASE and p.name in excluded))
manifest=BASE/'artifacts.sha256';manifest.write_text(''.join(f'{sha(p)}  {p}\n' for p in files))
r=subprocess.run(['sha256sum','-c',str(manifest)],capture_output=True,text=True);(BASE/'artifacts-check.log').write_text(r.stdout+r.stderr);assert r.returncode==0
# The body explicitly reports that custody has passed before it is sealed.
r=subprocess.run([sys.executable,str(BASE/'build_report.py'),'--seal'],capture_output=True,text=True);assert r.returncode==0,(r.stdout,r.stderr)
report=Path('xmodel/graded-macaulay-astra-20260905.md');data=report.read_bytes();mark=b'<!-- BODY-END -->\n';assert data.count(mark)==1
end=data.index(mark)+len(mark);body=data[:end];seal=data[end:];digest=hashlib.sha256(body).hexdigest()
assert str(len(body)).encode() in seal and digest.encode() in seal
assert 12000<=len(data)<=25000,(len(body),len(data))
verify={'report':str(report),'body_bytes':len(body),'file_bytes':len(data),'body_sha256':digest,'body_end_marker_count':1,'file_sha256':sha(report),'artifact_manifest_sha256':sha(manifest),'artifact_files_checked':len(files),'artifact_manifest_check_rc':0,'frozen_inputs_check_rc':0}
write(BASE/'seal-verification.json',verify)
print(json.dumps(verify,indent=2))
