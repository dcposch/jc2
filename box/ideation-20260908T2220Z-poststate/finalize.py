"""Owned artifact transaction and metadata recheck only."""
import datetime,hashlib,json,pathlib,subprocess
R=pathlib.Path('/home/ubuntu/jc2');B=R/'box/ideation-20260908T2220Z-poststate'
final='xmodel/ideation-20260908T2220Z-poststate-prep-astra.md';token='48611217a317413894638ec0a403839820831daaa0aac8c2eb50242c04a7ed55'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
index=json.loads((B/'PINS.json').read_text())
for e in index['entries']:
 if sha(R/e['snapshot'])!=e['snapshot_sha256']:raise SystemExit('snapshot drift')
for e in index['reuse']:
 if sha(R/e['existing_snapshot'])!=e['snapshot_sha256']:raise SystemExit('original source drift')
records=[]
for phase in ['close','finalize','verify']:
 argv=['python3','-I','-B','ops/artifact_finalize.py',phase,'--final',final]
 if phase!='verify':argv+=['--token',token]
 p=subprocess.run(argv,cwd=R,capture_output=True,text=True,timeout=30)
 records.append(dict(argv=argv,rc=p.returncode,stdout=p.stdout,stderr=p.stderr))
 if p.returncode:raise SystemExit(records[-1])
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (B/'metadata-verification.json').open('x') as f:json.dump(dict(utc=now,status='PASS',new_content_files=len(index['entries']),reused_files=len(index['reuse']),math_replays=0,launches=0,transaction=records),f,indent=2);f.write('\n')
files=sorted(p for p in B.rglob('*') if p.is_file())+[R/final,R/(final+'.artifact.json')]
entries=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)) for p in files]
with (B/'custody.json').open('x') as f:json.dump(dict(utc=now,status='TERMINAL_POSTSTATE_PREP',writers='idle after freeze',children='terminal',entries=entries),f,indent=2);f.write('\n')
for p in files+[B/'custody.json']:p.chmod(0o444)
for e in entries:
 if sha(R/e['path'])!=e['sha256']:raise SystemExit('final custody drift')
print(json.dumps(dict(status='VERIFIED_IDLE',utc=now,files=len(entries),report_sha256=sha(R/final),transaction_sha256=sha(R/(final+'.artifact.json')),custody_sha256=sha(B/'custody.json'),delta_sha256=sha(B/'delta.md'),pins_sha256=sha(B/'PINS.json'))))
