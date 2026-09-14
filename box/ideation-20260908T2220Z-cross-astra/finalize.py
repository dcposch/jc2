import sys
sys.dont_write_bytecode=True
import json,subprocess,hashlib,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def must(c,m):
 if not c:raise RuntimeError(m)
pins=json.loads((P/'input-pins.json').read_bytes())
for e in pins['entries']:must(sha(R/e['path'])==e['sha256'],'input drift '+e['path'])
cap=json.loads((P/'capability.json').read_bytes());results=[]
body=Path(cap['partial_path']).read_text();words=len(body.split())
must(body.endswith('<!-- BODY-END -->\n'),'body boundary')
for op in ('close','finalize','verify'):
 cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),op,'--final',cap['final_path']]
 if op!='verify':cmd+=['--token',cap['token']]
 r=subprocess.run(cmd,capture_output=True,timeout=25);must(r.returncode==0,op+': '+r.stderr.decode()+r.stdout.decode());results.append({'operation':op,'result':json.loads(r.stdout)})
with (P/'publication.json').open('xb') as f:f.write(json.dumps(results,indent=2).encode())
paths=[x for x in P.iterdir() if x.is_file()]+[Path(cap['final_path']),Path(cap['final_path']+'.artifact.json')]
owned=[{'path':str(x.relative_to(R)),'bytes':x.stat().st_size,'sha256':sha(x)} for x in sorted(paths)]
now=datetime.datetime.now(datetime.timezone.utc);deadline=datetime.datetime(2026,9,8,23,19,34,tzinfo=datetime.timezone.utc)
cust={'owner':'/root/nonemptiness_certificate','utc':now.isoformat(),'status':'TERMINAL_CROSS_UNREVIEWED','writers':'ALL IDLE after this exclusive custody write; no further writes promised','entries':owned,'charged_inputs':pins['entries'],'original_deadline':deadline.isoformat(),'late_seconds_at_custody':max(0,(now-deadline).total_seconds()),'body_whitespace_word_count':words,'mathematical_subprocesses':0,'new_agents':0}
with (P/'custody.json').open('xb') as f:f.write(json.dumps(cust,indent=2).encode())
for e in owned:must(sha(R/e['path'])==e['sha256'],'owned drift')
print(json.dumps({'status':'TERMINAL','report_sha256':sha(Path(cap['final_path'])),'transaction_sha256':sha(Path(cap['final_path']+'.artifact.json')),'custody_sha256':sha(P/'custody.json'),'entries':len(owned),'words':words,'late_seconds':cust['late_seconds_at_custody']},indent=2))
