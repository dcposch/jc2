#!/usr/bin/env python3
"""Print a terminal custody record; does not write or alter charged artifacts."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json

box=Path(__file__).resolve().parent
repo=box.parents[1]
def item(path):
    raw=path.read_bytes()
    return {'path':str(path.relative_to(repo)),'bytes':len(raw),'sha256':sha256(raw).hexdigest()}
telemetry=json.loads((box/'controls.telemetry.json').read_text())
assert telemetry['status']=='NORMAL_EXIT'
assert telemetry['child_exit_code']==0
assert telemetry['termination']['group_live_before_reap']==[]
result=json.loads((box/'controls.stdout').read_text())
assert result['status']=='D108_PUBLISHED_CASE_SMALL_CONTROLS_PASS'
assert len(result['genuine_mutations_rejected'])==6
assert (box/'controls.stderr').stat().st_size==0
report=repo/'xmodel/d108-published-case-interface-astra-20260906.md'
assert item(report)['sha256']=='528d745faac9de5a7e80a57e534c1f36377eb99b8576c1cfa72894fa3b110a1e'
inputs=[
 'box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json',
 'xmodel/d108-source-frontier-interface-astra-20260906.md',
 'xmodel/d108-source-frontier-gate-fable5-20260906.md',
 'box/ideation-20260906T1210Z/ggvh-2204.14178v1.pdf',
 'box/ideation-20260906T1210Z/ggvh-2204.14178v1.txt',
 'refs/guccione_valqui2017_ja471_shape_counterexamples.pdf',
 'box/census-coverage-20260905/core-ggv-layout.txt','jc72108/CROSSCHECK.md']
record={
 'schema':'D108_PUBLISHED_CASE_INTERFACE_CUSTODY/v1',
 'utc':datetime.now(timezone.utc).isoformat(),
 'owner':'/root/nonemptiness_certificate','recipient':'/root',
 'status':'TERMINAL_PRODUCER_CHECKED_STATEMENT_INTERFACE_DISCHARGED',
 'evidence_tier':'Exact small chain arithmetic plus EXTERNAL-THEOREM applicability; external exclusions not freshly replayed',
 'all_writers_done':True,'active_jobs':[],
 'AWS_action':'NONE','CAS_engine_used':False,'solver_launched':False,
 'source_expansion':'Only fixed source face and degree-28 root control; no full source expansion',
 'controls':{'status':result['status'],'six_genuine_mutations_rejected':True,'telemetry':telemetry},
 'statement_interface':'Keller specialization of the literal D108 source implies the exact published (8,28),(11/4,7),(3,2) case; no global-minimality antecedent.',
 'composition':'Conditional on published Prop4.3 plus retained faithful external exclusions, this literal physical-Keller source family is excluded.',
 'separate_debt':'Cor7.4 lower target-direction positivity interval not independently replayed; no coefficientwise cut map or new unit certificate.',
 'whole_proofs_read_unread':'Exact inventory in report section7; not all papers/dependencies read.',
 'reports':[item(report),item(report.with_name(report.name+'.artifact.json'))],
 'inputs':[item(repo/p) for p in inputs],
 'files':[item(p) for p in sorted(box.iterdir()) if p.is_file() and p.name!='custody.json'],
 'primary_urls':{
   'ggvh-algorithms-1708.07936v1.pdf':'https://arxiv.org/pdf/1708.07936v1',
   'ggv-lower-1605.09430v2.pdf':'https://arxiv.org/pdf/1605.09430v2',
   'ggvh-roots-1708.09367v2.pdf':'https://arxiv.org/pdf/1708.09367v2',
   'ggvh-roots-published2019.pdf':'https://revistas.pucp.edu.pe/index.php/promathematica/article/download/21094/20844',
   'helali-readme-snapshot.md':'https://raw.githubusercontent.com/bilLkarkariy/jc2-72-108-exact-certificates/main/README.md'},
 'source_bytes_preserved':True,'earlier_artifacts_unchanged':True,'no_shared_ledger_edit':True,
 'no_live_peer_report_read':True,
 'no_live_edit_promise':'This packet is immutable after custody publication; root may grant a fresh read-only independent gate.'}
print(json.dumps(record,sort_keys=True,indent=2))
