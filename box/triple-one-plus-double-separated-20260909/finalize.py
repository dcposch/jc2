import sys
sys.dont_write_bytecode=True
import json,subprocess,hashlib,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(c,m):
 if not c:raise RuntimeError(m)
pins=json.loads((P/'input-pins.json').read_bytes())
for e in pins['entries']:require(sha(R/e['path'])==e['sha256'],'input drift')
cap=json.loads((P/'capability.json').read_bytes());out=[]
require(Path(cap['partial_path']).read_bytes().endswith(b'<!-- BODY-END -->\n'),'body incomplete')
for op in ('close','finalize','verify'):
 cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),op,'--final',cap['final_path']]
 if op!='verify':cmd+=['--token',cap['token']]
 r=subprocess.run(cmd,capture_output=True,timeout=25);require(r.returncode==0,op+': '+r.stdout.decode()+r.stderr.decode());out.append({'operation':op,'result':json.loads(r.stdout)})
with (P/'publication.json').open('x') as f:json.dump(out,f,indent=2)
paths=[p for p in P.iterdir() if p.is_file() and p.name!='capability.json']+[Path(cap['final_path']),Path(cap['final_path']+'.artifact.json')]
entries=[{'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(paths)]
cust={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'owner':'/root/nonemptiness_certificate','status':'TERMINAL_PROVISIONAL_CONDITIONAL_ONE_PLUS_DOUBLE_PROOF','writers':'ALL IDLE after this exclusive metadata write','entries':entries,'inputs':pins['entries'],'mathematical_subprocesses':0,'controls':'manual factored/hypothesis controls only','full_source_or_high_powers_materialized':False,'contact_cover_status':'hypothesized, not promoted by this report','aws_ssh_web_agents':False}
with (P/'custody.json').open('x') as f:json.dump(cust,f,indent=2)
for e in entries:require(sha(R/e['path'])==e['sha256'],'owned drift')
for e in pins['entries']:require(sha(R/e['path'])==e['sha256'],'post input drift')
print(json.dumps({'utc':cust['utc'],'report_sha256':sha(Path(cap['final_path'])),'transaction_sha256':sha(Path(cap['final_path']+'.artifact.json')),'custody_sha256':sha(P/'custody.json'),'input_pins_sha256':sha(P/'input-pins.json'),'publication_sha256':sha(P/'publication.json'),'inputs':len(pins['entries']),'owned':len(entries),'writers':'IDLE'},indent=2))
