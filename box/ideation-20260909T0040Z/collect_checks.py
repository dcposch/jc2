"""Tiny read-only preflight controls and exclusive metadata receipt."""
import ast, datetime, hashlib, json, pathlib, subprocess, time
R=pathlib.Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260909T0040Z'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse((B/'preflight.py').read_text()))): raise SystemExit('assert gate')
runs=[]; start=time.monotonic()
for opt in [[],['-O']]:
 for args,fragment in [([],None),(['--invitation-ready'],'explicit fresh invitation deadline missing'),(['--invitation-ready','--deadline-utc','2000-01-01T00:00:00Z'],'deadline not future'),(['--invitation-ready','--deadline-utc','DISABLED'],'invalid deadline')]:
  argv=['python3','-I','-B']+opt+[str(B/'preflight.py')]+args
  p=subprocess.run(argv,cwd=R,capture_output=True,text=True,timeout=10)
  ok=(p.returncode==0 and json.loads(p.stdout)['status']=='PASS') if fragment is None else (p.returncode!=0 and fragment in p.stderr)
  if not ok: raise SystemExit('unexpected control outcome '+repr(argv))
  runs.append(dict(argv=argv,rc=p.returncode,stdout=p.stdout,stderr=p.stderr,expected=fragment or 'PASS'))
m=json.loads((B/'MANIFEST.json').read_text()); comparisons=[]
for e in m['entries']+m['provenance_only']:
 p=R/e['path']; source=R/e['source']; data=source.read_bytes(); span=e.get('lines')
 fragment=data if span is None else b''.join(data.splitlines(keepends=True)[span[0]-1:span[1]])
 if sha(p)!=e['sha256'] or p.read_bytes()!=fragment: raise SystemExit('snapshot mismatch '+e['path'])
 comparisons.append(dict(path=e['path'],source=e['source'],snapshot_sha256=sha(p),source_sha256_current=sha(source),source_sha256_at_freeze=e['source_sha256'],exact_snapshot_fragment_matches=True))
receipt=dict(status='PASS_PREP_ONLY',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),seconds=time.monotonic()-start,preflight_sha256=sha(B/'preflight.py'),no_assert=True,runs=runs,source_comparisons=comparisons,mathematical_execution=False,launch_performed=False)
with (B/'checks.json').open('x') as f: json.dump(receipt,f,indent=2); f.write('\n')
print(json.dumps(dict(status=receipt['status'],runs=len(runs),source_matches=len(comparisons),seconds=receipt['seconds'],checks_sha256=sha(B/'checks.json'))))
