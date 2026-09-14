#!/usr/bin/env python3
"""Hash completed owned outputs and emit final task custody; no arithmetic."""
import hashlib
import json
from pathlib import Path

root=Path(__file__).resolve().parent
repo=root.parents[1]
def item(path):
    raw=path.read_bytes()
    return {'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

for name in ('run','replay'):
    t=json.loads((root/(name+'.telemetry.json')).read_text())
    assert t['status']=='NORMAL_EXIT' and t['child_exit_code']==0
    assert t['termination']['group_live_before_reap']==[]
files=[item(p) for p in sorted(root.iterdir()) if p.is_file() and p.name!='custody.json']
dependencies=[item(repo/p) for p in (
 'box/char-degree-20260905/active-gauge/inputs/delta2_stage8.strongest.json',
 'box/factored-jacobian-pilot-20260906/complete_export.json',
 'box/factored-jacobian-pilot-20260906/complete_export.rows.tsv',
 'box/linear-c-discriminator-20260906/filtered_basis_summary.json',
 'box/linear-c-discriminator-20260906/reconstruction_summary.json',
 'box/linear-c-transverse-rank-20260906/line_support_check.json')]
packet={'schema':'JC2_OWNED_TASK_CUSTODY/v1','task':'linear-c-wfiltration-pilot-20260906',
 'status':'TERMINAL_METHOD_SOURCE_VALIDATION_ONLY_PROVISIONAL',
 'owner':'/root/nonemptiness_certificate','recipient':'/root',
 'basis_commit':'0d39df3c9fd69c939a8420c54d03228b9077777d',
 'scope':'one tiny exact rational generation and read-only semantic replay; no source expansion or solver',
 'host':'math-hq','worker_used':False,'worker_172_30_0_56_action':'NONE; ROOT retains prior custody',
 'all_arithmetic_writers_done':True,'active_jobs':[],
 'jobs':[{'name':n,'status':'NORMAL_EXIT','pgid':json.loads((root/(n+'.telemetry.json')).read_text())['pgid']} for n in ('run','replay')],
 'caps_per_job':{'wall_seconds':60,'cpu_seconds':60,'aggregate_RSS_bytes':209715200},
 'post_cutoff_notice':'Parent reported AUDIT17 frontier HOLD after GGHV arXiv2204.14178v1 Theorem2.1; applicability gate pending. No new 99-frontier descendant authorized.',
 'source_bytes_preserved':True,'original_pilot_artifacts_preserved':True,'no_live_report_read':True,
 'no_live_edit_promise':'All listed task outputs immutable after seal; reviewer may read or replay read-only. No worker writer exists.',
 'files':files,'dependencies':dependencies}
target=root/'custody.json'
assert not target.exists()
target.write_text(json.dumps(packet,sort_keys=True,indent=2)+'\n')
print(json.dumps(item(target),sort_keys=True))
