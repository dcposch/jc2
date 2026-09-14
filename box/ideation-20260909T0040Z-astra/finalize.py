"""Close the one blind report and freeze custody; never inspect peer reports."""
import datetime, hashlib, json, pathlib, re, subprocess
R=pathlib.Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260909T0040Z-astra'
report=R/'xmodel/ideation-20260909T0040Z-astra.md'
partial=R/'xmodel/.ideation-20260909T0040Z-astra.md.partial-2b4597f9d4bb2822f49accff6d045df3'
token='498211a171fa86b42330318853b919dbb86ae30c78955ea6402dfb74bf7767e9'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
body=partial.read_text()
rows=re.findall(r'^\|(\d+)\|(unchanged|raise|lower|reopen)\|',body,re.M)
if [int(n) for n,_ in rows]!=list(range(1,47)): raise SystemExit('missing/duplicate avenue')
if body.count('<!-- BODY-END -->')!=1 or not body.endswith('<!-- BODY-END -->\n'): raise SystemExit('incomplete body')
if len(re.findall(r'^## Card\d',body,re.M))>3: raise SystemExit('too many cards')
inputs=json.loads((B/'input-pins.json').read_text())
post=[]
for e in inputs['entries']:
 path=e.get('snapshot',e['path']); expected=e.get('snapshot_sha256',e['sha256']); p=R/path
 if sha(p)!=expected: raise SystemExit('input drift '+path)
 post.append(dict(path=path,sha256=sha(p),unchanged=True))
replay=json.loads((B/'replay.json').read_text())
if sha(B/'check_maps.py')!=replay['check_sha256']: raise SystemExit('checker drift')
publication=[]
for phase in ['close','finalize','verify']:
 argv=['python3','-I','-B',str(R/'ops/artifact_finalize.py'),phase,'--final',str(report)]
 if phase!='verify': argv+=['--token',token]
 p=subprocess.run(argv,cwd=R,capture_output=True,text=True,check=True)
 publication.append(dict(argv=argv,rc=p.returncode,stdout=p.stdout,stderr=p.stderr))
now=datetime.datetime.now(datetime.timezone.utc)
with (B/'publication.json').open('x') as f: json.dump(dict(utc=now.isoformat(),common_deadline_utc='2026-09-09T01:22:00+00:00',on_time=now<datetime.datetime(2026,9,9,1,22,tzinfo=datetime.timezone.utc),full46=True,dispositions=rows,post_inputs=post,publication=publication),f,indent=2); f.write('\n')
owned=[p for p in sorted(B.rglob('*')) if p.is_file()]+[report,pathlib.Path(str(report)+'.artifact.json')]
entries=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)) for p in owned]
with (B/'custody.json').open('x') as f: json.dump(dict(utc=now.isoformat(),owner='/root/model_productivity',status='TERMINAL_BLIND_COMPLETE',writers='IDLE after final custody write',entries=entries),f,indent=2); f.write('\n')
for p in owned+[B/'custody.json']: p.chmod(0o444)
print(json.dumps(dict(terminal_utc=now.isoformat(),report_sha256=sha(report),transaction_sha256=sha(pathlib.Path(str(report)+'.artifact.json')),custody_sha256=sha(B/'custody.json'),input_pins_sha256=sha(B/'input-pins.json'),publication_sha256=sha(B/'publication.json'),owned_pins=len(entries),writers='IDLE')))
