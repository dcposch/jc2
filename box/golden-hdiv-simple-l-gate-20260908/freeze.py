"""Exclusive mechanical snapshots, literal parser preflight and transaction."""
import datetime,hashlib,json,pathlib,shutil,subprocess
R=pathlib.Path('/home/ubuntu/jc2');B=R/'box/golden-hdiv-simple-l-gate-20260908'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
 with (B/name).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
sources=[
 ('scope.md','box/golden-hdiv-simple-l-gate-20260908/scope.md',None),
 ('cross-proof.md','xmodel/ideation-20260908T2220Z-cross-astra.md','eee98b84da9adaf3f069eb3a3325769dcb725f36d5cf34a649ed47fa8ce8886b'),
 ('cross-transaction.json','xmodel/ideation-20260908T2220Z-cross-astra.md.artifact.json','542d8f457a98ba58029cf4ffd1dc40f4b59e54981532cb8cfeab52e82ba803e3'),
 ('cross-custody.json','box/ideation-20260908T2220Z-cross-astra/custody.json',None),
 ('cross-input-pins.json','box/ideation-20260908T2220Z-cross-astra/input-pins.json','db18358b1789dada91171636e7c29437225b63287e1b1d76f31f099c16806676'),
 ('source-proof.md','xmodel/golden-two-regime-initial-discriminator-astra-20260908.md','14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6'),
 ('audit-15m.md','box/ideation-20260908T2220Z-poststate/snapshots/audit-15m-only.md','b02ae267bb8cfef6956d6e0cec0b6188196b222d3d9d78e3d1582f4a5cc1a440'),
 ('prior-gate.md','xmodel/golden-nonh-composition-gate-fable5-20260908.md','ddd2077da0d63d53aea062373f82ce7bdb21d9df1fcf4180127789e98409b9e2'),
 ('prior-gate.run.v2','xmodel/golden-nonh-composition-gate-fable5-20260908.run.v2','7971057038e18affa811263af93b02311cbfc8c3ccbf7a0bf7bbe3089e08e4d9')]
for _,src,pin in sources:
 if pin and sha(R/src)!=pin:raise SystemExit('SOURCE DRIFT '+src)
cust=json.loads((R/'box/ideation-20260908T2220Z-cross-astra/custody.json').read_text())
for e in cust['entries']:
 if sha(R/e['path'])!=e['sha256']:raise SystemExit('CROSS CUSTODY DRIFT '+e['path'])
(B/'inputs').mkdir()
entries=[]
for name,src,pin in sources:
 out=B/'inputs'/name
 with out.open('xb') as dst,(R/src).open('rb') as inp:shutil.copyfileobj(inp,dst)
 h=sha(out)
 if h!=sha(R/src):raise SystemExit('COPY DRIFT')
 entries.append(dict(original=src,original_sha256=h,snapshot=str(out.relative_to(R)),snapshot_sha256=h,bytes=out.stat().st_size))
save('PINS.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PREP_ONLY',entries=entries))
p=subprocess.run(['sed','-n','s/^charged_input=//p',str(B/'fable.prompt.md')],capture_output=True,text=True,timeout=10)
got=p.stdout.splitlines();want=[e['snapshot'] for e in entries]
txt=(B/'fable.prompt.md').read_text()
if p.returncode or got!=want or len(set(pathlib.Path(x).name for x in got))!=9:raise SystemExit('PARSER FAIL')
if txt.count('{{LANE_INPUTS}}')!=1 or txt.count('xmodel/golden-hdiv-simple-l-gate-fable5-20260908.md')!=1:raise SystemExit('PROMPT FAIL')
if any(line.startswith('charge_basis=') for line in txt.splitlines()):raise SystemExit('PRICE FAIL')
for e in entries:
 if sha(R/e['original'])!=e['original_sha256'] or sha(R/e['snapshot'])!=e['snapshot_sha256']:raise SystemExit('PIN DRIFT')
final='xmodel/golden-hdiv-simple-l-gate-prep-astra-20260908.md'
token='352ae12d4a8efb442326daabaa0a747b979f4795560bef87ffdd3f1e1eef2ff0'
records=[]
for phase in ['close','finalize','verify']:
 argv=['python3','-I','-B','ops/artifact_finalize.py',phase,'--final',final]
 if phase!='verify':argv+=['--token',token]
 r=subprocess.run(argv,cwd=R,capture_output=True,text=True,timeout=30)
 records.append(dict(argv=argv,rc=r.returncode,stdout=r.stdout,stderr=r.stderr))
 if r.returncode:raise SystemExit(records[-1])
save('verification.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PASS_METADATA_ONLY',parser_argv=p.args,parser_stdout=p.stdout,inputs=len(got),math_runs=0,launches=0,transaction=records))
files=sorted(x for x in B.rglob('*') if x.is_file())+[R/final,R/(final+'.artifact.json')]
out=[dict(path=str(x.relative_to(R)),bytes=x.stat().st_size,sha256=sha(x)) for x in files]
save('custody.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='TERMINAL_PREP',writers='idle after freeze',children='terminal',entries=out))
for x in files+[B/'custody.json']:x.chmod(0o444)
print(json.dumps(dict(status='VERIFIED_IDLE',report_sha256=sha(R/final),transaction_sha256=sha(R/(final+'.artifact.json')),custody_sha256=sha(B/'custody.json'),pins_sha256=sha(B/'PINS.json'),prompt_sha256=sha(B/'fable.prompt.md'),inputs=len(got))))
