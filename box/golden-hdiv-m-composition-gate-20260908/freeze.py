"""Exclusive metadata-only review packet and transactional preparation report."""
import datetime,hashlib,json,pathlib,shutil,subprocess
R=pathlib.Path('/home/ubuntu/jc2');B=R/'box/golden-hdiv-m-composition-gate-20260908'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
 with (B/name).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
sources=[
 ('scope.md','box/golden-hdiv-m-composition-gate-20260908/scope.md',None),
 ('coalesced-proof.md','xmodel/golden-hdiv-coalesced-m-source-astra-20260908.md','fd04a5fd0bbbbbe89e10a50310d931bbf72d442512422912b1dd62cdcaa38654'),
 ('coalesced-transaction.json','xmodel/golden-hdiv-coalesced-m-source-astra-20260908.md.artifact.json','2f36b75b2ea2857b2264df0e992019300bad76a50461a498c8b937a42eedd9fa'),
 ('coalesced-custody.json','box/golden-hdiv-coalesced-m-source-20260908/custody.json','63afa4581f3e9834e607a9932e569b0311ac5ff9323321c24925c9b970da2091'),
 ('coalesced-input-pins.json','box/golden-hdiv-coalesced-m-source-20260908/input-pins.json','180b2b64e2bea86b2f1890927297229716c65bc596efef24a3eaadc97d837cea'),
 ('separated-proof.md','xmodel/golden-hdiv-separated-m-source-coordinator-20260908.md','e8ae9f1ab4c319f12af4514ad9cb70f3b3b48541e0bf82d9acd55cd81e67ca87'),
 ('separated-transaction.json','xmodel/golden-hdiv-separated-m-source-coordinator-20260908.md.artifact.json','bed766fae3fdaeff28d6ca82bab381267fa7ed5fc7c5686d06958e0193c12174'),
 ('source-framework.md','xmodel/golden-two-regime-initial-discriminator-astra-20260908.md','14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6'),
 ('source-transaction.json','xmodel/golden-two-regime-initial-discriminator-astra-20260908.md.artifact.json','a80659d8c6b38fd4800b7eb70b650af57a0065e0c67b077f2878c1c24377c8af'),
 ('audit-15m.md','box/ideation-20260908T2220Z-poststate/snapshots/audit-15m-only.md','b02ae267bb8cfef6956d6e0cec0b6188196b222d3d9d78e3d1582f4a5cc1a440')]
for _,src,pin in sources:
 if pin and sha(R/src)!=pin:raise SystemExit('SOURCE DRIFT '+src)
c=json.loads((R/'box/golden-hdiv-coalesced-m-source-20260908/custody.json').read_text())
for e in c['entries']+c['charged_inputs']:
 if sha(R/e['path'])!=e['sha256']:raise SystemExit('PRODUCER CUSTODY DRIFT '+e['path'])
records=[]
for path in [sources[1][1],sources[5][1],sources[7][1]]:
 argv=['python3','-I','-B','ops/artifact_finalize.py','verify','--final',path]
 p=subprocess.run(argv,cwd=R,capture_output=True,text=True,timeout=30)
 records.append(dict(argv=argv,rc=p.returncode,stdout=p.stdout,stderr=p.stderr))
 if p.returncode:raise SystemExit(records[-1])
(B/'inputs').mkdir();entries=[]
for name,src,pin in sources:
 out=B/'inputs'/name
 with out.open('xb') as dst,(R/src).open('rb') as inp:shutil.copyfileobj(inp,dst)
 if sha(out)!=sha(R/src):raise SystemExit('COPY DRIFT')
 entries.append(dict(original=src,original_sha256=sha(R/src),snapshot=str(out.relative_to(R)),snapshot_sha256=sha(out),bytes=out.stat().st_size))
save('PINS.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PREP_ONLY',entries=entries))
p=subprocess.run(['sed','-n','s/^charged_input=//p',str(B/'fable.prompt.md')],capture_output=True,text=True,timeout=10)
got=p.stdout.splitlines();want=[e['snapshot'] for e in entries];txt=(B/'fable.prompt.md').read_text()
if p.returncode or got!=want or len(set(pathlib.Path(x).name for x in got))!=10:raise SystemExit('PARSER FAIL')
if txt.count('{{LANE_INPUTS}}')!=1 or txt.count('xmodel/golden-hdiv-m-composition-gate-fable5-20260908.md')!=1:raise SystemExit('PROMPT FAIL')
if any(x.startswith('charge_basis=') for x in txt.splitlines()):raise SystemExit('PRICE FAIL')
for e in entries:
 if sha(R/e['snapshot'])!=e['snapshot_sha256'] or sha(R/e['original'])!=e['original_sha256']:raise SystemExit('PIN DRIFT')
final='xmodel/golden-hdiv-m-composition-gate-prep-astra-20260908.md';token='cf4032815ed4773d0dbb44374bcecf3ce0432cdd9e04418c7b400d3044631504'
for phase in ['close','finalize','verify']:
 argv=['python3','-I','-B','ops/artifact_finalize.py',phase,'--final',final]
 if phase!='verify':argv+=['--token',token]
 r=subprocess.run(argv,cwd=R,capture_output=True,text=True,timeout=30)
 records.append(dict(argv=argv,rc=r.returncode,stdout=r.stdout,stderr=r.stderr))
 if r.returncode:raise SystemExit(records[-1])
save('verification.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PASS_METADATA_ONLY',parser_argv=p.args,parser_stdout=p.stdout,inputs=len(got),math_runs=0,launches=0,transactions=records))
files=sorted(x for x in B.rglob('*') if x.is_file())+[R/final,R/(final+'.artifact.json')]
out=[dict(path=str(x.relative_to(R)),bytes=x.stat().st_size,sha256=sha(x)) for x in files]
save('custody.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='TERMINAL_PREP',writers='idle after freeze',children='terminal',entries=out))
for x in files+[B/'custody.json']:x.chmod(0o444)
print(json.dumps(dict(status='VERIFIED_IDLE',report_sha256=sha(R/final),transaction_sha256=sha(R/(final+'.artifact.json')),custody_sha256=sha(B/'custody.json'),pins_sha256=sha(B/'PINS.json'),prompt_sha256=sha(B/'fable.prompt.md'),inputs=len(got))))
