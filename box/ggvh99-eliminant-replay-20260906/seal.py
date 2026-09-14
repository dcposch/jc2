#!/usr/bin/env python3
"""Seal this completed small proof-validation instrument; no CAS."""
import hashlib
import json
from pathlib import Path
root=Path(__file__).resolve().parent
repo=root.parents[1]
def item(p):
    raw=p.read_bytes()
    return {'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
jobs=[]
for name in ('preflight','run','recheck'):
    t=json.loads((root/(name+'.telemetry.json')).read_text())
    assert t['status']=='NORMAL_EXIT' and t['child_exit_code']==0
    assert t['termination']['group_live_before_reap']==[]
    jobs.append({'name':name,'status':t['status'],'pgid':t['pgid'],'utc_end':t['utc_end'],'caps':t['caps']})
result={'schema':'JC2_PRIMARY_PROOF_INSTRUMENT_CUSTODY/v1','task':'ggvh99-eliminant-replay-20260906',
 'owner':'/root/nonemptiness_certificate','recipient':'/root','status':'TERMINAL_PRODUCER_CHECKED_EXACT',
 'scope':'GGHV2204.14178v1 finite nine-equation consequence(5.9) and Prop5.4 scalar only',
 'host':'math-hq','AWS_action':'NONE','all_arithmetic_writers_done':True,'active_jobs':[],
 'no_frontier_solve':True,'no_full_source_or_reduction_chain_claim':True,
 'no_live_blind_report_read':True,'source_bytes_preserved':True,'jobs':jobs,
 'no_live_edit_promise':'All listed outputs immutable after seal; read-only replay allowed. Producer yields after report transaction.',
 'files':[item(p) for p in sorted(root.iterdir()) if p.is_file() and p.name!='custody.json'],
 'primary_sources':[item(repo/('box/ideation-20260906T1210Z/ggvh-2204.14178v1.'+ext)) for ext in ('pdf','txt')]}
target=root/'custody.json'
assert not target.exists()
target.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
print(json.dumps(item(target),sort_keys=True))
