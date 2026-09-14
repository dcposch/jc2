import sys
sys.dont_write_bytecode=True
import json,hashlib,subprocess,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
d=json.loads((P/'root-release.json').read_bytes());rows=[]
for key,name in [('report','local-consumer.md'),('transaction','local-consumer-transaction.json')]:
 src=R/d[key]['path']
 if sha(src)!=d[key]['sha256']:raise RuntimeError('root released input drift '+key)
 rows.append({'source':d[key]['path'],'snapshot':str((P/'inputs'/name).relative_to(R)),'sha256':d[key]['sha256'],'bytes':src.stat().st_size})
r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'verify','--final',str(R/d['report']['path'])],capture_output=True,timeout=25,check=True)
for e in rows:
 with (R/e['snapshot']).open('xb') as f:f.write((R/e['source']).read_bytes())
 if sha(R/e['snapshot'])!=e['sha256']:raise RuntimeError('root snapshot drift')
with (P/'root-freeze.json').open('xb') as f:f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'entries':rows,'transaction_verify':json.loads(r.stdout),'read_boundary':'verified before proof-body access'},indent=2).encode())
print(json.dumps({'status':'ROOT_RELEASE_VERIFIED_FROZEN','entries':len(rows),'report_sha256':d['report']['sha256']}))
