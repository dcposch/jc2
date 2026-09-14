from pathlib import Path
import json,datetime
root=Path('/home/ubuntu/jc2/box/graded-moh-20260905');r=root/'resume-r2'
status=json.loads((root/'runs/r2_77_full_n2_Q/status.json').read_text())
assert status['state']=='FINISHED'
assert status['returncode']==124,'A non-timeout needs exact mathematical review before finalization'
audit=json.loads((r/'execution-custody.json').read_text());assert audit['all_finished'] and audit['all_declared_hashes_match']
own=json.loads((r/'owned-instances-final.json').read_text());assert {d['ID'] for d in own}=={'i-05bbedf0197e8eee3','i-02aaa996f54d2c004'};assert all(d['State']=='terminated' for d in own)
now=datetime.datetime.now(datetime.timezone.utc);elapsed=(now-datetime.datetime(2026,9,5,14,19,30,tzinfo=datetime.timezone.utc)).total_seconds()
f=(r/'report-foundation.md').read_text();c=(r/'report-compute.md').read_text()
c=c.replace('[FULL77_N2_FINAL]',f'The further full77 test retains all150 original rows, uses the reversed pivot order with positive weights w, and targets c² at(4,78) through weight78. It timed out rc124 after{status["elapsed_seconds"]:.2f}s under128GiB, without a completed basis or rational identity; original c² membership remains OPEN.')
c=c.replace('[TERMINATION_FINAL]',f'Both owned workers were terminated with `bash ops/fleet/fleet.sh term <ID>` after harvesting: `.67` first, then `.86`. The final EC2 record `resume-r2/owned-instances-final.json` confirms TERMINATED for both exact IDs. All{audit["execution_count"]} status-recorded invocations are finished and all their declared input/output hashes match. Operational cutoff: {now.strftime("%H:%M:%SZ")} ({int(elapsed//60)}m{int(elapsed%60):02d}s in round2), within150min.')
assert not any(x in c for x in ['[FULL77_N2_FINAL]','[TERMINATION_FINAL]','[FULL_SOLVER_TABLE]','[FINAL_CUSTODY_TERMINATION]'])
(r/'report-compute.md').write_text(c)
body=f+c+'\n<!-- BODY-END -->\n'
assert 15000<=len(body.encode())<=29650,len(body.encode())
p=Path('/home/ubuntu/jc2/xmodel/graded-moh-astra-r2-20260905.md');p.write_text(body)
(r/'resume-state.md').write_text(f'Round2 completed{now.isoformat()}. Report{p}. Four exactQ N1 nonmembership certificates; no class kill or original c² certificate. Both owned workers confirmedterminated in owned-instances-final.json. All{audit["execution_count"]} status-recordedinvocations finished; all declared executionhashesmatch. Seal and finalcustody checks follow; do not rerun solvers.\n')
print(json.dumps(dict(report=str(p),body_bytes=len(body.encode()),cutoff=now.isoformat(),elapsed_seconds=elapsed)))
