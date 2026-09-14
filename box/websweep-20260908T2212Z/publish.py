import sys
sys.dont_write_bytecode=True
import json,hashlib,datetime,subprocess,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
ROOT=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
c=json.loads((P/'transaction-capability.json').read_bytes()); rows=[]
for op in ('close','finalize','verify'):
 cmd=['/usr/bin/python3','-I','-B',str(ROOT/'ops/artifact_finalize.py'),op,'--final',c['final_path']]
 if op!='verify':cmd+=['--token',c['token']]
 r=subprocess.run(cmd,capture_output=True,timeout=25)
 if r.returncode:raise RuntimeError(op+': '+r.stderr.decode()+r.stdout.decode())
 rows.append({'operation':op,'result':json.loads(r.stdout)})
with (P/'publication.json').open('xb') as f:f.write(json.dumps(rows,indent=2).encode())
files=[f for f in P.rglob('*') if f.is_file()]+[Path(c['final_path']),Path(c['final_path']+'.artifact.json')]
entries=[]
for f in sorted(files):entries.append({'path':str(f),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
inputs=json.loads((P/'charged-pins.json').read_bytes())
for x in inputs:
 f=ROOT/x['source'];x['current_sha256']=hashlib.sha256(f.read_bytes()).hexdigest();x['current_matches_frozen']=x['current_sha256']==x['sha256']
cust={'owner':'/root/nonemptiness_certificate','completed':datetime.datetime.now(datetime.timezone.utc).isoformat(),'writer_status':'ALL WRITERS DONE; no network/arithmetic jobs remain; no further writes promised','status':'TERMINAL / PARTIAL-COVERAGE / NO ACTION','entries':entries,'campaign_inputs':inputs,'caps':'each tiny validation <=30wall/25CPU/512MiB; no CAS/AWS/source expansion','private_metadata':'transaction-capability.json is a local lifecycle capability, not a reader input','prior_empty_lease':'preserved, superseded before any report content was written'}
with (P/'custody.json').open('xb') as f:f.write(json.dumps(cust,indent=2).encode())
for e in entries:
 f=Path(e['path'])
 if hashlib.sha256(f.read_bytes()).hexdigest()!=e['sha256']:raise RuntimeError('post-custody drift '+str(f))
print(json.dumps({'status':'TERMINAL','entries':len(entries),'report_sha256':hashlib.sha256(Path(c['final_path']).read_bytes()).hexdigest(),'custody_sha256':hashlib.sha256((P/'custody.json').read_bytes()).hexdigest(),'publication_sha256':hashlib.sha256((P/'publication.json').read_bytes()).hexdigest(),'input_drift':[x['source'] for x in inputs if not x['current_matches_frozen']]},indent=2))
