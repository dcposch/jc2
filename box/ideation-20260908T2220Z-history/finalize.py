"""Metadata-only history custody and report publication; no mathematical replay."""
import datetime,hashlib,json,pathlib,subprocess
R=pathlib.Path('/home/ubuntu/jc2');B=R/'box/ideation-20260908T2220Z-history'
final='xmodel/ideation-20260908T2220Z-history-astra.md'
token='6a6fe9ceda374585fef1796df7af5fbec5d3f3b3ab7e489a0f756715efd2168a'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(name,obj):
 with (B/name).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
scopes={
 'APPROACHES.md':'scoped searches; lines180-235',
 'AUDIT.md':'scoped searches; lines1232-1267 and1310-1378',
 'PROGRESS.md':'scoped searches; lines1-112',
 'notes.md':'newest LIVE lines21877-21910',
 'ladder/REDUCTION.md':'named block/Euler/common4 term search only',
 'history/APPROACHES-before-20260906-cleanup.md':'historical master46 row26',
 'box/ideation-20260908T2220Z/snapshots/master46-history.md':'historical master46 row26',
 'xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md':'whole',
 'xmodel/block-descent-d2-galois-obstruction-producer-sol56-20260830.md':'whole',
 'xmodel/block-descent-d2-galois-obstruction-hostile-review-opus5-20260830.md':'summary and sections0-3.1 only',
 'xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md':'whole',
 'xmodel/ideation-20260908T2220Z-sol56.md':'whole terminal blind',
 'xmodel/ideation-20260908T2220Z-coordinator.md':'scoped search and lines50-135',
 'xmodel/ideation-20260908T2220Z-astra.md':'own terminal blind',
 'xmodel/d125-common-to-unequal-interface-discriminator-astra-20260908.md':'whole',
 'xmodel/d125-golden-divisibility-control-astra-20260908.md':'whole',
 'xmodel/uniform-cone-jacobian-degree-astra-20260908.md':'already whole-read producer; current scoped Euler/lower-B history comparison'}
expected={
 'xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md':'ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778',
 'xmodel/block-descent-d2-galois-obstruction-producer-sol56-20260830.md':'766a843a25eaf560840f15afa8971dd39246fc8b15290491d18e7f4a4c6bb7f7',
 'xmodel/block-descent-d2-galois-obstruction-hostile-review-opus5-20260830.md':'e324c104d06ad9e987cfe304ee001e52a58d91eaba941b80c78555a058056df9',
 'xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md':'f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8',
 'xmodel/d125-golden-divisibility-control-astra-20260908.md':'54a499bb55d401e88716dde5762ca39341817adaa7ea1f41faf5865570ac4b0e'}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
entries=[]
for path,scope in scopes.items():
 p=R/path;h=sha(p)
 if path in expected and h!=expected[path]:raise SystemExit('SOURCE DRIFT '+path)
 entries.append(dict(path=path,bytes=p.stat().st_size,sha256=h,read_scope=scope))
write('history-pins.json',dict(utc=now,entries=entries,math_replays=0,live_peer_reads=0))
ex=[]
for path,lo,hi in [('AUDIT.md',1236,1257),('AUDIT.md',1333,1365),('notes.md',21877,21910)]:
 lines=(R/path).read_text().splitlines(keepends=True)
 ex.append(dict(path=path,start_line=lo,end_line=hi,text=''.join(lines[lo-1:hi])))
write('canonical-excerpts.json',dict(utc=now,excerpts=ex))
records=[]
for phase in ['close','finalize','verify']:
 argv=['python3','-I','-B','ops/artifact_finalize.py',phase,'--final',final]
 if phase!='verify':argv+=['--token',token]
 p=subprocess.run(argv,cwd=R,capture_output=True,text=True,timeout=30)
 records.append(dict(argv=argv,rc=p.returncode,stdout=p.stdout,stderr=p.stderr))
 if p.returncode:raise SystemExit(records[-1])
write('metadata-verification.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PASS',transaction=records,math_replays=0))
files=sorted(p for p in B.iterdir() if p.is_file())+[R/final,R/(final+'.artifact.json')]
out=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)) for p in files]
write('custody.json',dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='TERMINAL_HISTORY_ONLY',writers='idle after freeze',children='terminal',entries=out))
for p in files+[B/'custody.json']:p.chmod(0o444)
for e in out:
 if sha(R/e['path'])!=e['sha256']:raise SystemExit('CUSTODY DRIFT')
print(json.dumps(dict(status='VERIFIED_IDLE',report_sha256=sha(R/final),transaction_sha256=sha(R/(final+'.artifact.json')),custody_sha256=sha(B/'custody.json'),pins_sha256=sha(B/'history-pins.json'),entries=len(entries))))
