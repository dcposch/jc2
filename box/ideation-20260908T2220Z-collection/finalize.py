import sys
sys.dont_write_bytecode=True
import json,subprocess,hashlib,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
ROOT=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def must(c,m):
 if not c:raise RuntimeError(m)
c=json.loads((P/'collection.json').read_bytes());a=c['local']['astra']['replay_metadata']['charged_inputs']
must(len(a)==19,'Astra recorded input count');actual={e['path']:e['sha256'] for e in a};must(actual==c['inputs'],'Astra recorded input vector mismatch')
for path,h in c['inputs'].items():must(sha(ROOT/path)==h,'final charged drift '+path)
for lane,r in c['external'].items():
 must(sha(ROOT/r['path'])==r['sha256'],'final receipt drift '+lane);must(sha(ROOT/r['fields']['report'])==r['fields']['report_sha256'],'final report drift '+lane)
with (P/'local-input-vector.json').open('xb') as f:f.write(json.dumps({'status':'PASS','count':19,'vector_equal':True,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2).encode())
cap=json.loads((P/'capability.json').read_bytes());results=[]
for op in ('close','finalize','verify'):
 cmd=['/usr/bin/python3','-I','-B',str(ROOT/'ops/artifact_finalize.py'),op,'--final',cap['final_path']]
 if op!='verify':cmd+=['--token',cap['token']]
 r=subprocess.run(cmd,capture_output=True,timeout=25);must(r.returncode==0,op+': '+r.stderr.decode()+r.stdout.decode());results.append({'operation':op,'result':json.loads(r.stdout)})
with (P/'publication.json').open('xb') as f:f.write(json.dumps(results,indent=2).encode())
paths=[x for x in P.rglob('*') if x.is_file()]+[Path(cap['final_path']),Path(cap['final_path']+'.artifact.json')]
owned=[{'path':str(x.relative_to(ROOT)),'bytes':x.stat().st_size,'sha256':sha(x)} for x in sorted(paths)]
cust={'owner':'/root/nonemptiness_certificate','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'TERMINAL_METADATA_COLLECTION','writers':'ALL IDLE after this exclusive custody write; no further writes promised','peer_bodies_read':False,'entries':owned,'charged_inputs':c['inputs'],'parent_reports':{k:v['fields']['report_sha256'] for k,v in c['external'].items()},'deadline_unchanged':c['deadline']}
with (P/'custody.json').open('xb') as f:f.write(json.dumps(cust,indent=2).encode())
for e in owned:must(sha(ROOT/e['path'])==e['sha256'],'owned drift')
print(json.dumps({'status':'TERMINAL','report_sha256':sha(Path(cap['final_path'])),'transaction_sha256':sha(Path(cap['final_path']+'.artifact.json')),'custody_sha256':sha(P/'custody.json'),'entries':len(owned),'collection_sha256':sha(P/'collection.json')},indent=2))
