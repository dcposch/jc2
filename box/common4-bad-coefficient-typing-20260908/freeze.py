"""Mechanical charged snapshots and metadata preflight only. No source imports."""
import datetime,hashlib,json,os,pathlib,shutil,subprocess
R=pathlib.Path('/home/ubuntu/jc2');B=R/'box/common4-bad-coefficient-typing-20260908'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
 with (B/name).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
sources=[
 ('scope.md','box/common4-bad-coefficient-typing-20260908/scope.md',None),
 ('receiver-composition.md','xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md','7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413'),
 ('common-centering-interface.md','xmodel/d125-common-to-unequal-interface-discriminator-astra-20260908.md','4af46f416d1b489a4792a0af017b028327c1b4d0b8778242d76d5e7590c54219'),
 ('lift-contract.md','xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md','433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad'),
 ('baseline.py','box/d125-small-source-exporter-prep-20260906/baseline.py','ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'),
 ('exporter.py','box/d125-small-source-exporter-prep-20260906/exporter.py','9fd003e420f3ee069f1ed1c06a365e5b4500d361bc3951f2f8f17ef733ab3703'),
 ('common4-header.json','box/d125-small-source-construction-pilot-20260906/evidence/common_4-rational/header.json',None),
 ('common4-manifest.json','box/d125-small-source-construction-pilot-20260906/evidence/common_4-rational/client-common_4-rational.manifest.json',None)]
for _,src,pin in sources:
 if pin and sha(R/src)!=pin:raise SystemExit('SOURCE DRIFT '+src)
(B/'inputs').mkdir()
entries=[]
for name,src,pin in sources:
 out=B/'inputs'/name
 with out.open('xb') as dst,(R/src).open('rb') as inp:shutil.copyfileobj(inp,dst)
 if sha(out)!=sha(R/src):raise SystemExit('COPY DRIFT')
 entries.append(dict(original=src,original_sha256=sha(R/src),snapshot=str(out.relative_to(R)),snapshot_sha256=sha(out),bytes=out.stat().st_size))
aud=(R/'AUDIT.md').read_text();parts=[]
for letter in ['l','m','n','s']:
 marker='### 17('+letter*13+')'
 start=aud.index(marker);end=aud.find('\n### ',start+len(marker))
 if end<0:raise SystemExit('AUDIT SECTION BOUNDARY')
 parts.append(aud[start:end].rstrip()+'\n')
out=B/'inputs/accepted-audit-context.md'
with out.open('x') as f:f.write('# Dated accepted source context — not a whole-ledger charge\n\n'+'\n'.join(parts))
entries.append(dict(original='AUDIT.md',original_sha256=sha(R/'AUDIT.md'),sections=['17('+x*13+')' for x in ['l','m','n','s']],snapshot=str(out.relative_to(R)),snapshot_sha256=sha(out),bytes=out.stat().st_size))
src='history/APPROACHES-before-20260908T0304-cleanup.md';lines=(R/src).read_text().splitlines(keepends=True)
out=B/'inputs/history-context.md'
with out.open('x') as f:f.write('# Historical context only: source lines229–270\n\n'+''.join(lines[228:270]))
entries.append(dict(original=src,original_sha256=sha(R/src),lines=[229,270],snapshot=str(out.relative_to(R)),snapshot_sha256=sha(out),bytes=out.stat().st_size))
other=['xmodel/d125-minimal-receiver-client-preflight-astra-20260906.md','xmodel/d125-small-source-exporter-prep-astra-20260906.md','xmodel/d125-small-source-construction-pilot-astra-20260906.md','ops/lane.sh','ops/adapters/sol.sh']
provenance=[dict(path=p,bytes=(R/p).stat().st_size,sha256=sha(R/p)) for p in other]
save('PINS.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PREP_ONLY',entries=entries,provenance_only=provenance))
p=subprocess.run(['sed','-n','s/^charged_input=//p',str(B/'sol.prompt.md')],capture_output=True,text=True,timeout=10)
got=p.stdout.splitlines();want=[e['snapshot'] for e in entries];txt=(B/'sol.prompt.md').read_text()
if p.returncode or got!=want or len(set(pathlib.Path(x).name for x in got))!=10:raise SystemExit('PARSER FAIL')
if txt.count('{{LANE_INPUTS}}')!=1 or txt.count('xmodel/common4-bad-coefficient-typing-sol56-20260908.md')!=1:raise SystemExit('PROMPT FAIL')
if any(x.startswith('charge_basis=') for x in txt.splitlines()):raise SystemExit('PRICE FAIL')
if not os.access(R/'ops/adapters/sol.sh',os.X_OK) or (R/'ops/adapters/sol56.sh').exists():raise SystemExit('ADAPTER EXPECTATION DRIFT')
for e in entries:
 if sha(R/e['snapshot'])!=e['snapshot_sha256'] or sha(R/e['original'])!=e['original_sha256']:raise SystemExit('PIN DRIFT')
final='xmodel/common4-bad-coefficient-typing-prep-astra-20260908.md';token='1b5f758df3c34fcf046495d17abd675bafc335e3ef8956c0e846c8af7e80eed2'
records=[]
for phase in ['close','finalize','verify']:
 argv=['python3','-I','-B','ops/artifact_finalize.py',phase,'--final',final]
 if phase!='verify':argv+=['--token',token]
 r=subprocess.run(argv,cwd=R,capture_output=True,text=True,timeout=30)
 records.append(dict(argv=argv,rc=r.returncode,stdout=r.stdout,stderr=r.stderr))
 if r.returncode:raise SystemExit(records[-1])
save('verification.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PASS_METADATA_ONLY',parser_argv=p.args,parser_stdout=p.stdout,inputs=len(got),adapter='sol',math_runs=0,launches=0,transaction=records))
files=sorted(x for x in B.rglob('*') if x.is_file())+[R/final,R/(final+'.artifact.json')]
out=[dict(path=str(x.relative_to(R)),bytes=x.stat().st_size,sha256=sha(x)) for x in files]
save('custody.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='TERMINAL_PREP',writers='idle after freeze',children='terminal',entries=out))
for x in files+[B/'custody.json']:x.chmod(0o444)
print(json.dumps(dict(status='VERIFIED_IDLE',report_sha256=sha(R/final),transaction_sha256=sha(R/(final+'.artifact.json')),custody_sha256=sha(B/'custody.json'),pins_sha256=sha(B/'PINS.json'),prompt_sha256=sha(B/'sol.prompt.md'),inputs=len(got))))
