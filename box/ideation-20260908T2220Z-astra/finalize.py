"""Metadata-only blind report publication; no math replay or lane invocation."""
import datetime,hashlib,json,pathlib,re,subprocess
R=pathlib.Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260908T2220Z-astra'; P=R/'box/ideation-20260908T2220Z'
final='xmodel/ideation-20260908T2220Z-astra.md'; token='61392c7e1cbc5c6aa77311fdf2eaf697ea603229b28fa8f23db53fea50ac7d65'
partial=R/'xmodel/.ideation-20260908T2220Z-astra.md.partial-e2e75a39d09358823a03db0e11c34a1e'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(argv):
 p=subprocess.run(argv,cwd=R,capture_output=True,text=True,timeout=30)
 return dict(argv=argv,rc=p.returncode,stdout=p.stdout,stderr=p.stderr)
m=json.loads((P/'MANIFEST.json').read_text())
for e in m['entries']:
 if sha(R/e['path'])!=e['sha256']: raise SystemExit('charged drift '+e['path'])
body=partial.read_text(); ids=re.findall(r'^\|(\d+)\|[^\n]*\|unchanged\|',body,re.M)
if [int(x) for x in ids]!=list(range(1,47)): raise SystemExit('full46 dispositions missing')
if body.count('<!-- BODY-END -->')!=1 or not body.endswith('<!-- BODY-END -->\n'): raise SystemExit('body framing')
rows=[]
for phase in ['close','finalize','verify']:
 argv=['python3','-I','-B','ops/artifact_finalize.py',phase,'--final',final]
 if phase!='verify': argv+=['--token',token]
 r=run(argv); rows.append(r)
 if r['rc']: raise SystemExit(r)
now=datetime.datetime.now(datetime.timezone.utc)
record=dict(utc=now.isoformat(),original_target=m['blind_target_utc'],timeliness='ON_TIME' if now<=datetime.datetime.fromisoformat(m['blind_target_utc']) else 'LATE',all46=True,math_replays=0,peer_reads=False,charged_inputs=m['entries']+[dict(path=str((P/'MANIFEST.json').relative_to(R)),sha256=sha(P/'MANIFEST.json'))],transaction=rows)
with (B/'replay-and-input-pins.json').open('x') as f:json.dump(record,f,indent=2);f.write('\n')
files=[B/'finalize.py',B/'replay-and-input-pins.json',R/final,R/(final+'.artifact.json')]
entries=[dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=sha(p)) for p in files]
c=dict(utc=now.isoformat(),status='TERMINAL_BLIND_SUBMISSION',timeliness=record['timeliness'],writers='idle after freeze',children='terminal',entries=entries)
with (B/'custody.json').open('x') as f:json.dump(c,f,indent=2);f.write('\n')
for p in files+[B/'custody.json']:p.chmod(0o444)
print(json.dumps(dict(status='VERIFIED_IDLE',timeliness=record['timeliness'],report_sha256=sha(R/final),transaction_sha256=sha(R/(final+'.artifact.json')),custody_sha256=sha(B/'custody.json'),utc=now.isoformat())))
