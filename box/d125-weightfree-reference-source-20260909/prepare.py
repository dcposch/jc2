import sys
sys.dont_write_bytecode=True
import json,hashlib,subprocess,os,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
INPUTS={
'xmodel/golden-two-regime-initial-discriminator-astra-20260908.md':'14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6',
'box/ideation-20260908T2220Z-poststate/snapshots/audit-15m-only.md':'b02ae267bb8cfef6956d6e0cec0b6188196b222d3d9d78e3d1582f4a5cc1a440',
'xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md':'7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for name,expected in INPUTS.items():
 p=R/name
 if sha(p)!=expected:raise RuntimeError('input drift '+name)
 rows.append({'path':name,'sha256':expected,'bytes':p.stat().st_size})
with (P/'input-pins.json').open('xb') as f:f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'entries':rows},indent=2).encode())
cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/d125-weightfree-reference-source-astra-20260909.md'),'--basis','0d39df3c9fd69c939a8420c54d03228b9077777d','--owner','/root/nonemptiness_certificate']
r=subprocess.run(cmd,capture_output=True,timeout=25,check=True);fd=os.open(P/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
c=json.loads(r.stdout);print(json.dumps({'status':'PASS','pins':len(rows),'partial':c['partial_path']}))
