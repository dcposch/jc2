import sys
sys.dont_write_bytecode=True
import json,hashlib,subprocess,os,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def must(c,m):
 if not c:raise RuntimeError(m)
rp=R/'xmodel/common4-bad-coefficient-typing-sol56-20260908.run.v2'
must(sha(rp)=='88011bd4c732bde47abe6c6524a8f8cfe66830656ea344b96cad693f9f2dedce','receipt pin')
d=dict(line.split('=',1) for line in rp.read_text().splitlines() if '=' in line)
for k,v in {'final_status':'DONE','exit_code':'0','seal_boundary':'CLEAN','report_state':'BODY_SEALED','charge_basis_status':'ABSENT','charged_inputs':'10'}.items():must(d[k]==v,k)
rows=[]
for i in range(1,11):
 name=d[f'charged_input_{i}'];h=d[f'charged_input_{i}_sha256'];must(d[f'charged_input_{i}_post']=='UNCHANGED','post pin');must(sha(R/name)==h,'input drift '+name);rows.append({'path':name,'sha256':h,'bytes':(R/name).stat().st_size})
must(d['report_sha256']=='5bd69bddb0c63cd9ba1e1c1ef44943e03fe63d5c536a7c8fe93af3595b26a9a9','declared report pin');must(sha(R/d['report'])==d['report_sha256'],'report drift')
rows.extend([{'path':str(rp.relative_to(R)),'sha256':sha(rp),'bytes':rp.stat().st_size},{'path':d['report'],'sha256':d['report_sha256'],'bytes':(R/d['report']).stat().st_size}])
with (P/'input-pins.json').open('xb') as f:f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'terminal_receipt_verified_before_body':True,'entries':rows},indent=2).encode())
cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/common4-bad-coefficient-typing-gate-astra-20260909.md'),'--basis','0d39df3c9fd69c939a8420c54d03228b9077777d','--owner','/root/nonemptiness_certificate']
r=subprocess.run(cmd,capture_output=True,timeout=25,check=True);fd=os.open(P/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
c=json.loads(r.stdout);print(json.dumps({'status':'PASS','pins':len(rows),'partial':c['partial_path']}))
