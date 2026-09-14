#!/usr/bin/env python3
"""Completion-only custody, accepted-certificate, and owned-process audit."""
import hashlib,json,os,re,subprocess
from datetime import datetime,timezone
from pathlib import Path

root=Path(__file__).resolve().parent
workspace=root.parent.parent
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):h.update(block)
    return h.hexdigest()
def read(name):return json.loads((root/name).read_text())
def hashes_match(values):
    for name,digest in values.items():
        p=root/name
        assert p.is_file(),name
        assert sha(p)==digest,name

manifest=subprocess.run(['sha256sum','-c',str(root/'input-manifest.sha256')],text=True,capture_output=True,check=True)
assert manifest.stdout.count(': OK')==10
(root/'input-verification-final.log').write_text(manifest.stdout)
t2=read('audit_t2.json')
assert {r['d'] for r in t2}=={-1,1}
for r in t2:
    assert all(r[k] for k in ('U_unit','X_unit','main_unit','boundary_unit','cone_nonunit','rows_deleted_nonunit'))
for t in (3,4):
    r=read(f't{t}_transport_circuit.json')
    assert r['verification']=='ALL_EXACT_ASSERTIONS_PASS'
    hashes_match(r['input_sha256'])
    assert sha(root/f't{t}_transport.sing')==r['transport_script_sha256']
    assert sha(root/f't{t}_transport.log')==r['log_sha256']
    if t==3:assert r['expanded_main_verified']
r=read('t5_rank_independent_result.json')
assert r['verdict']=='INDEPENDENT_T5_RANK_MODEL_AND_DETERMINANT_PASS'
assert r['determinant_mod_p']==29155 and r['basis_size']==1792
assert r['raw_denominators_prime_units'] and r['scaled_selected_coefficients_integral_in_e']
hashes_match(r['hashes'])
q=read('t5_rank_chart_circuit.json')
assert q['verdict']=='EXACT_T5_MAIN_AND_BOUNDARY_UNIT_BY_REPLAYED_RANK_AND_DETERMINANT_CIRCUITS'
hashes_match(q['hashes'])
assert all(32009%d for d in range(2,180))
assert read('linear_t5_replay_status.json')['jobs_remaining']==0

accepted_logs=['audit_t2.log','controls_t3_emit.log','controls_t4_emit.log','controls_t5_emit.log',
 't3_emit_charts.log','t4_emit_charts.log','t5_emit_charts.log','t3_cone.log','t4_cone.log',
 't3_transport.log','t4_transport.log','t5_rank_chart_maps.log','linear_t4_replay.log',
 'boundary_structure_t3.log','decoupled_controls.log']
for name in accepted_logs:
    text=(root/name).read_text()
    assert not re.search(r'(^\s*\? |^FAIL |Traceback)',text,re.M),name

# Only this lane's processes are relevant. Other campaign work is untouched.
ps=subprocess.run(['ps','-eo','pid=,ppid=,comm=,args='],capture_output=True,text=True,check=True).stdout
live=[]
for line in ps.splitlines():
    parts=line.split(None,3)
    if len(parts)!=4:continue
    pid,ppid,comm,args=parts
    if int(pid)==os.getpid():continue
    if comm in ('Singular','msolve','python3','python') and 'k16xempty-20260905' in args:live.append(line)
assert not live,live
remote={}
for host in ('172.30.0.7','172.30.0.18'):
    cmd=['ssh','-i',str(Path.home()/'.ssh/jc2-fleet'),'-o','BatchMode=yes','-o','ConnectTimeout=10',f'ubuntu@{host}','ps -eo pid=,ppid=,comm=,args=']
    out=subprocess.run(cmd,capture_output=True,text=True,check=True).stdout
    jobs=[]
    for line in out.splitlines():
        parts=line.split(None,3)
        if len(parts)==4 and parts[2] in ('Singular','msolve','python3') and any(x in parts[3] for x in ('k16xempty-20260905','t4_lift.sing','t5_cone.sing')):jobs.append(line)
    assert not jobs,(host,jobs)
    remote[host]={'owned_cas_jobs':jobs}

accepted=['audit_t2.json','t3_transport_circuit.json','t4_transport_circuit.json',
 'linear_t4_certificate.sing','linear_t5_rank_certificate.json','t5_rank_independent_result.json',
 't5_rank_chart_circuit.json','report-review.md','source-links.json']+accepted_logs
record={name:{'sha256':sha(root/name),'bytes':(root/name).stat().st_size} for name in accepted}
(root/'accepted-artifacts.json').write_text(json.dumps(record,indent=2)+'\n')
review=(root/'report-review.md').read_text()
assert 'mathematically sound' in review
report=(workspace/'xmodel/k16-xempty-astra-20260905.md').read_text()
assert 'Assume B*eta is nonzero throughout this subsection.' in report
assert 'which the open condition xL nonzero removes' in report
assert not any(x in report for x in ('placeholder','FINITE_RESULT_TABLE','RANK_AUDIT_RESULT'))
assert 20000<=len(report.encode())<40000
result={'all_lane_jobs_finished':True,'accepted_artifacts_pass':True,
 'completed_utc':datetime.now(timezone.utc).isoformat(),'local_owned_cas_jobs':live,'remote':remote,
 'finite_verdict':'X_main and X_boundary UNIT in characteristic zero at t=2,3,4,5 on every field factor',
 'uniform_verdict':'OPEN; no all-t promotion','optional_t5_expanded_replay':'INCONCLUSIVE_TIMEOUT, reaped',
 'accepted_manifest_sha256':sha(root/'accepted-artifacts.json')}
(root/'final-audit.json').write_text(json.dumps(result,indent=2)+'\n')
files=[p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='artifacts.sha256']
lines=[f'{sha(p)}  {p.relative_to(root)}' for p in sorted(files)]
(root/'artifacts.sha256').write_text('\n'.join(lines)+'\n')
print(json.dumps(result,indent=2))
