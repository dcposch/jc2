"""Mechanical immutable post-cutoff snapshots and metadata only; no lane/math calls."""
import datetime,hashlib,json,pathlib,re,shutil
R=pathlib.Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260908T2220Z-poststate'; S=B/'snapshots'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(v,m):
 if not v:raise SystemExit(m)
receipt=R/'xmodel/golden-nonh-composition-gate-fable5-20260908.run.v2'
require(sha(receipt)=='7971057038e18affa811263af93b02311cbfc8c3ccbf7a0bf7bbe3089e08e4d9','receipt drift')
kv=dict(line.split('=',1) for line in receipt.read_text().splitlines() if '=' in line)
for k,v in [('final_status','DONE'),('exit_code','0'),('seal_boundary','CLEAN'),('report_state','BODY_SEALED'),('charge_basis_status','ABSENT'),('charged_inputs','10')]:require(kv[k]==v,'receipt '+k)
charged=[]
for i in range(1,11):
 p=R/kv['charged_input_'+str(i)];h=kv['charged_input_'+str(i)+'_sha256']
 require(sha(p)==h and kv['charged_input_'+str(i)+'_post']=='UNCHANGED','input drift')
 charged.append(dict(path=str(p.relative_to(R)),sha256=h))
S.mkdir(exist_ok=False)
spec=[('xmodel/golden-resonant-source-consumer-coordinator-20260908.md','consumer-full.md','1770c414adacb5f8a60438ed3379b3e39969c50e247cee2e5e898acc689f3c8f'),('xmodel/golden-nonh-composition-gate-fable5-20260908.md','nonh-gate-full.md','ddd2077da0d63d53aea062373f82ce7bdb21d9df1fcf4180127789e98409b9e2'),(str(receipt.relative_to(R)),'nonh-gate.run.v2','7971057038e18affa811263af93b02311cbfc8c3ccbf7a0bf7bbe3089e08e4d9'),('box/d125-0220-root-harvest-20260907/2300-nonh-sweep-harvest.json','root-2300-replay.json','f9613955aa159c71a930be449426d0bf38238913b9c9074a599f0b833e93f903'),('xmodel/websweep-20260908T2212Z-astra.md','completed-sweep-full.md','364431f6267629e2f45e49785b18bf6393f4a9b4f2b59b4d3ee47047a70440dc'),('xmodel/websweep-20260908T2212Z-astra.md.artifact.json','completed-sweep-transaction.json','ce452b6238ea96d7ce4b367a117dbfa7290ec272e61718af9cba0b30d94be0ad')]
entries=[]
for src,dest,h in spec:
 p=R/src;require(sha(p)==h,'source drift '+src);q=S/dest;shutil.copyfile(p,q)
 entries.append(dict(original=src,original_sha256=h,snapshot=str(q.relative_to(R)),snapshot_sha256=sha(q),bytes=q.stat().st_size))
audit=R/'AUDIT.md';raw=audit.read_text();marker='### 17(mmmmmmmmmmmmmmm) —';a=raw.index(marker);e=raw.find('\n### ',a+len(marker));section=raw[a:] if e<0 else raw[a:e]
require('23:00 UTC' in section and 'nonodd golden non-H-divisible branch excluded' in section,'wrong audit scope')
q=S/'audit-15m-only.md';q.write_text(section)
entries.append(dict(original='AUDIT.md',original_sha256=sha(audit),section='17(mmmmmmmmmmmmmmm)',snapshot=str(q.relative_to(R)),snapshot_sha256=sha(q),bytes=q.stat().st_size))
for name in ['delta.md']:
 p=B/name;entries.append(dict(original=str(p.relative_to(R)),original_sha256=sha(p),snapshot=str(p.relative_to(R)),snapshot_sha256=sha(p),bytes=p.stat().st_size))
old=R/'box/ideation-20260908T2220Z/snapshots/provisional-golden-proof.md'
require(sha(old)=='14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6','old source drift')
references=[dict(original='xmodel/golden-two-regime-initial-discriminator-astra-20260908.md',original_sha256=sha(old),existing_snapshot=str(old.relative_to(R)),snapshot_sha256=sha(old),reason='already charged to every original blind; do not duplicate')]
provenance=[('xmodel/golden-resonant-source-consumer-coordinator-20260908.md.artifact.json','aec7cfe1801ec0b6b45855f2ab263289d2a6e1f9852f781905f07b400725a3c0'),('box/websweep-20260908T2212Z/custody.json','f1851987d1c174c9bc3515b19b6897d45d485a1541eb8e6b48949c74fd6fa31d')]
for p,h in provenance:require(sha(R/p)==h,'provenance drift '+p)
index=dict(schema='JC2-POST-CUTOFF/v1',freeze_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),original_blind_cutoff='2026-09-08T22:26:47.147953+00:00',state='POST_CUTOFF_ONLY_NO_LAUNCH',entries=entries,reuse=references,provenance_only=[dict(path=p,sha256=h) for p,h in provenance],gate_current_inputs=charged,gate_report_sha256=kv['report_sha256'],parent_machine_observation_utc='2026-09-08T22:54:45Z',own_machine_check=False,math_replays=0,blind_body_or_receipt_reads=False)
with (B/'PINS.json').open('x') as f:json.dump(index,f,indent=2);f.write('\n')
for x in entries:require(sha(R/x['snapshot'])==x['snapshot_sha256'],'snapshot drift')
names=[pathlib.Path(x['snapshot']).name for x in entries]+[old.name]
require(len(names)==len(set(names)),'duplicate basename')
print(json.dumps(dict(status='FROZEN',freeze_utc=index['freeze_utc'],new_content_files=len(entries),reused_source_files=len(references),new_content_bytes=sum(x['bytes'] for x in entries),pins_sha256=sha(B/'PINS.json'))))
