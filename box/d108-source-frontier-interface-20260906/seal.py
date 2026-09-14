#!/usr/bin/env python3
"""Terminal custody of bounded D108 desk interface; no arithmetic."""
import hashlib
import json
from pathlib import Path
root=Path(__file__).resolve().parent
repo=root.parents[1]
def item(p):
    raw=p.read_bytes();return {'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
jobs=[]
for name in ('source','controls','edge','replay','replay2','critical'):
    t=json.loads((root/(name+'.telemetry.json')).read_text())
    assert t['status']=='NORMAL_EXIT' and t['termination']['group_live_before_reap']==[]
    assert t['child_exit_code']==(1 if name=='replay' else 0)
    jobs.append({'name':name,'exit_code':t['child_exit_code'],'pgid':t['pgid'],'utc_end':t['utc_end'],
      'wall_seconds':t['wall_elapsed_seconds'],'caps':t['caps'],
      'typed_result':'HARNESS_TUPLE_LIST_MISMATCH_CORRECTED_BY_REPLAY2' if name=='replay' else 'PASS'})
paths=[
 'box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json',
 'box/t2t3-direct-20260906/build_direct.py','box/t2t3-chain-20260906/acyclic-graph-d108-free-mean.json',
 'xmodel/full-ideal-counterexample-gate-fable5-20260906.md','xmodel/t2t3-chain-sol56-20260906.md',
 'xmodel/t2t3-direct-sol56-20260906.md','box/ideation-20260906T1210Z/ggvh-2204.14178v1.pdf',
 'box/ideation-20260906T1210Z/ggvh-2204.14178v1.txt','refs/guccione_valqui2017_ja471_shape_counterexamples.pdf',
 'box/census-coverage-20260905/core-ggv-layout.txt','jc72108/SECTION4-AUTOMATION.md','jc72108/CROSSCHECK.md']
result={'schema':'D108_SOURCE_INTERFACE_CUSTODY/v1','owner':'/root/nonemptiness_certificate','recipient':'/root',
 'status':'TERMINAL_PRODUCER_CHECKED_EXACT_PARTIAL_MAP_PLUS_SCOPED_RANK_PORT',
 'cutoff':'post1210round; not inserted into that sealed round',
 'first_history_checksum_UTC':'2026-09-06T12:27:14Z',
 'first_history_checksums':{'APPROACHES.md':'46147a6af9775156efd5a22f3175f36546c9a7a943cc0a561cfdf4664cf2626d',
  'AUDIT.md':'0bcbd9a45262fbaaf75d8f882c859ec2463253520112a238e650575508c0b151',
  'ladder/REDUCTION.md':'7f901db6c8e6fbc80c85581a331c247d5c219e23bf286136f77fbc0182ebbe1b'},
 'all_writers_done':True,'active_jobs':[],'AWS_action':'NONE','full_source_expansion':False,'solver_launched':False,
 'no_live_blind_report_read':True,'no_shared_ledger_edit':True,'source_bytes_preserved':True,
 'map_gap':'Uninstantiated exhaustive lower-edge/root-cut and successor-tail support transport; standard-pair and fixed starting-edge conditions themselves were checked.',
 'rank_scope':'192dim actual C space: full rank191 at every base field point; abstract W190 unit minor; no concrete D108 pivot matrix emitted',
 'root_suggested_delta':'critical_jet.json; not claimed independent ideation',
 'jobs':jobs,'inputs':[item(repo/p) for p in paths],
 'files':[item(p) for p in sorted(root.iterdir()) if p.is_file() and p.name!='custody.json'],
 'no_live_edit_promise':'All charged task outputs immutable after this seal. Root may authorize fresh read-only review; no worker custody change.'}
out=root/'custody.json';assert not out.exists();out.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(item(out),sort_keys=True))
