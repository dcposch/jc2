"""Finalize only this owned preparation and collect read-only checks. No lane calls."""
import datetime,hashlib,json,pathlib,subprocess
R=pathlib.Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260908T2220Z'
final='xmodel/ideation-20260908T2220Z-prep-astra.md'
token='a55f176d5f8e015c81aa166c0431cee5daa2f11dd49e98e384b6d88c5fa8eb46'
def run(argv):
 p=subprocess.run(argv,cwd=R,capture_output=True,text=True,timeout=30)
 return dict(argv=argv,rc=p.returncode,stdout=p.stdout,stderr=p.stderr)
checks=[]
for args,want in [([],0),(['--invitation-ready'],1)]:
 r=run(['python3','-I','-B',str(B/'preflight.py')]+args); checks.append(r)
 if r['rc']!=want: raise SystemExit('unexpected preflight outcome')
if 'root blind absent' not in checks[1]['stderr']: raise SystemExit('wrong invitation refusal')
receipts=[]
for phase in ['close','finalize','verify']:
 argv=['python3','-I','-B','ops/artifact_finalize.py',phase,'--final',final]
 if phase!='verify': argv+=['--token',token]
 r=run(argv); receipts.append(r)
 if r['rc']: raise SystemExit(r)
receipt=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),checks=checks,transaction=receipts,launch_performed=False)
with (B/'preflight-and-transaction.json').open('x') as f: json.dump(receipt,f,indent=2);f.write('\n')
def entry(p):
 return dict(path=str(p.relative_to(R)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
files=sorted(p for p in B.rglob('*') if p.is_file())+[R/final,R/(final+'.artifact.json')]
custody=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),state='TERMINAL_PREP_ONLY',launch_performed=False,all_children='terminal',writers='idle after custody freeze',entries=[entry(p) for p in files])
with (B/'custody.json').open('x') as f: json.dump(custody,f,indent=2);f.write('\n')
for p in files+[B/'custody.json']: p.chmod(0o444)
for e in custody['entries']:
 if entry(R/e['path'])!=e: raise SystemExit('custody drift')
print(json.dumps(dict(status='VERIFIED_IDLE',entries=len(files),report=entry(R/final),transaction=entry(R/(final+'.artifact.json')),custody=entry(B/'custody.json'))))
