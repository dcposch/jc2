"""Frozen conditional interface sources, metadata only; no math execution."""
import datetime,hashlib,json,pathlib,shutil,subprocess
R=pathlib.Path('/home/ubuntu/jc2');B=R/'box/d125-weightfree-client-interface-astra-20260909'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,obj):
 with (B/name).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
sources=[
 ('candidate.md','box/d125-weightfree-client-interface-astra-20260909/candidate.md',None),
 ('receiver-composition.md','xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md','7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413'),
 ('sufficient-lift.md','xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md','433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad'),
 ('published-chain-gate.md','xmodel/d125-published-chain-gate-fable5-20260906.md','5be50d001d285481233c8de415b2f4d22411a22cb930a0c1db287c0579b3cd7b'),
 ('published-chain-producer.md','xmodel/d125-published-chain-discriminator-astra-20260906.md','9b439af269c23e349615d3e404e0732c9c7f491a9342d5500e061aab91ad4e88'),
 ('common4-typing-gate.md','xmodel/common4-bad-coefficient-typing-gate-astra-20260909.md',None)]
for _,src,pin in sources:
 if pin and sha(R/src)!=pin:raise SystemExit('SOURCE DRIFT '+src)
(B/'inputs').mkdir();entries=[]
for name,src,pin in sources:
 out=B/'inputs'/name
 with out.open('xb') as dst,(R/src).open('rb') as inp:shutil.copyfileobj(inp,dst)
 if sha(out)!=sha(R/src):raise SystemExit('COPY DRIFT')
 entries.append(dict(original=src,original_sha256=sha(R/src),snapshot=str(out.relative_to(R)),snapshot_sha256=sha(out),bytes=out.stat().st_size,read_scope='whole'))
def excerpt(src,name,parts,description):
 out=B/'inputs'/name
 with out.open('x') as f:f.write(description+'\n\n'+'\n'.join(parts))
 entries.append(dict(original=src,original_sha256=sha(R/src),snapshot=str(out.relative_to(R)),snapshot_sha256=sha(out),bytes=out.stat().st_size,read_scope=description))
aud=(R/'AUDIT.md').read_text();sections=[];markers=[]
for letter,n in [('j',13),('l',13),('m',13),('n',13),('s',13),('i',15),('j',15),('m',15),('n',15),('o',15)]:
 marker='### 17('+letter*n+')';start=aud.index(marker);end=aud.find('\n### ',start+len(marker))
 if end<0:end=len(aud)
 sections.append(aud[start:end].rstrip()+'\n');markers.append(marker)
excerpt('AUDIT.md','audit-context.md',sections,'# Scoped accepted history: '+', '.join(markers))
app=(R/'APPROACHES.md').read_text();start=app.index('### D125: current source coverage');end=app.index('\n### Computation:',start)
excerpt('APPROACHES.md','approaches-d125.md',[app[start:end]],'# Current D125 section only; no whole avenue charge')
lines=(R/'PROGRESS.md').read_text().splitlines(keepends=True)
excerpt('PROGRESS.md','progress-sep9.md',[''.join(lines[:20])],'# September9 digest through first dated entry')
notes=(R/'notes.md').read_text();start=notes.index('## 2026-09-09 00:04 UTC LIVE STATE');end=notes.find('\n## ',start+4)
if end<0:end=len(notes)
excerpt('notes.md','live-0004.md',[notes[start:end]],'# Named newest LIVE read: 2026-09-09 00:04 UTC (not live peer output)')
provenance=[]
for path,scope in [('ladder/REDUCTION.md','scoped literal searches; no matched weight-free source'),('xmodel/d125-common-to-unequal-interface-discriminator-astra-20260908.md','whole in preceding completed typing task; current canonical comparison'),('xmodel/d125-minimal-receiver-client-preflight-astra-20260906.md','whole in preceding completed typing task; exact counts'),('xmodel/d125-small-source-exporter-prep-astra-20260906.md','whole in preceding completed typing task; exact full-source counts')]:
 provenance.append(dict(path=path,sha256=sha(R/path),bytes=(R/path).stat().st_size,read_scope=scope))
save('PINS.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='CONDITIONAL_CLIENT_TYPING_WF_UNREVIEWED',task_start='2026-09-09T00:17:43Z',deadline='2026-09-09T00:29:43Z',entries=entries,provenance_only=provenance,math_runs=0))
for e in entries:
 if sha(R/e['snapshot'])!=e['snapshot_sha256'] or sha(R/e['original'])!=e['original_sha256']:raise SystemExit('PIN DRIFT')
final='xmodel/d125-weightfree-client-interface-astra-20260909.md';token='a10b0355cfd0612918bd5ffbd37f8bd3ecf86510ceaf1796e1b6547e0f0f4697';records=[]
for phase in ['close','finalize','verify']:
 argv=['python3','-I','-B','ops/artifact_finalize.py',phase,'--final',final]
 if phase!='verify':argv+=['--token',token]
 r=subprocess.run(argv,cwd=R,capture_output=True,text=True,timeout=30)
 records.append(dict(argv=argv,rc=r.returncode,stdout=r.stdout,stderr=r.stderr))
 if r.returncode:raise SystemExit(records[-1])
save('verification.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PASS_METADATA_ONLY',mathematical_runs=0,launches=0,transaction=records))
files=sorted(x for x in B.rglob('*') if x.is_file())+[R/final,R/(final+'.artifact.json')]
out=[dict(path=str(x.relative_to(R)),bytes=x.stat().st_size,sha256=sha(x)) for x in files]
save('custody.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='TERMINAL_CONDITIONAL_INTERFACE',writers='idle after freeze',children='terminal',entries=out))
for x in files+[B/'custody.json']:x.chmod(0o444)
print(json.dumps(dict(status='VERIFIED_IDLE',report_sha256=sha(R/final),transaction_sha256=sha(R/(final+'.artifact.json')),custody_sha256=sha(B/'custody.json'),pins_sha256=sha(B/'PINS.json'),source_entries=len(entries))))
