"""Bounded tiny controls and source custody; no CAS or original-source arithmetic."""
import ast, datetime, hashlib, json, pathlib, subprocess, time
R=pathlib.Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260909T0040Z-astra'; P=R/'box/ideation-20260909T0040Z'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((B/'check_maps.py').read_text()))): raise SystemExit('assert')
m=json.loads((P/'MANIFEST.json').read_text()); inputs=[]
for e in m['entries']:
 p=R/e['path']
 if sha(p)!=e['sha256']: raise SystemExit('frozen input drift')
 inputs.append(dict(path=e['path'],sha256=sha(p),bytes=p.stat().st_size,read_scope='WHOLE; matched protocol/map/previous-synthesis reading from same-agent preparation also retained'))
for name in ['MANIFEST.json','astra.invitation.prompt.md']:
 p=P/name; inputs.append(dict(path=str(p.relative_to(R)),sha256=sha(p),bytes=p.stat().st_size,read_scope='WHOLE'))
for path in ['xmodel/positive-face-actual-receiver-discriminator-astra-20260906.md','xmodel/positive-face-actual-receiver-gate-fable5-20260906.md']:
 p=R/path; inputs.append(dict(path=path,sha256=sha(p),bytes=p.stat().st_size,read_scope='WHOLE terminal accepted history, no checker replay'))
for path,lo,hi,name in [('AUDIT.md',18465,18472,'audit13k.md'),('ladder/REDUCTION.md',1,165,'ladder-read-excerpt.md')]:
 p=R/path; data=b''.join(p.read_bytes().splitlines(keepends=True)[lo-1:hi]); q=B/name
 with q.open('xb') as f: f.write(data)
 inputs.append(dict(path=path,sha256=sha(p),read_scope=[lo,hi],snapshot=str(q.relative_to(R)),snapshot_sha256=sha(q)))
with (B/'input-pins.json').open('x') as f: json.dump(dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),entries=inputs),f,indent=2); f.write('\n')
start=time.monotonic(); rows=[]
for opt in [[],['-O']]:
 for mutation in ['none','bad-slope','wrong-map-sign','wrong-swap']:
  argv=['prlimit','--as=536870912','--cpu=25','--','python3','-I','-B']+opt+[str(B/'check_maps.py'),mutation]
  r=subprocess.run(argv,cwd=R,capture_output=True,text=True,timeout=30)
  decoded=json.loads(r.stdout)
  if r.returncode!=(0 if mutation=='none' else 2) or r.stderr or decoded['passed']!=(mutation=='none'): raise SystemExit('control outcome '+mutation)
  rows.append(dict(argv=argv,rc=r.returncode,stdout=r.stdout,stderr=r.stderr))
with (B/'replay.json').open('x') as f: json.dump(dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),seconds=time.monotonic()-start,no_assert=True,check_sha256=sha(B/'check_maps.py'),runs=rows),f,indent=2); f.write('\n')
print(json.dumps(dict(status='PASS',modes=len(rows),seconds=time.monotonic()-start,inputs=len(inputs),replay_sha256=sha(B/'replay.json'),input_pins_sha256=sha(B/'input-pins.json'))))
