import sys
sys.dont_write_bytecode=True
import os,json,hashlib,subprocess,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
expected={
'xmodel/late-contact-triple-endpoint-astra-20260909.md':'b541308788da31f52e9f7985c7767e206231e8f3251ff53c1b2bd9c96b64f097',
'xmodel/late-contact-triple-endpoint-gate-fable5-20260909.md':'c9a399a87dc91d78bfc4f811249996ea3e217eda075be679cf27b41af5795c26',
'xmodel/triple-source-contact-cover-astra-20260909.md':'f3ab28a6b26345cfd4ce2bd74cf77a335acdf7865c650a4662964a2e738edc08',
'xmodel/triple-cubic-source-coalesced-astra-20260909.md':'1620f9ef6b2edc598d35cab274cdfcc24d71353d18132d3a35ffb59fd2c46099'}
rows=[]
for name,pin in expected.items():
 b=(R/name).read_bytes();h=hashlib.sha256(b).hexdigest()
 if h!=pin:raise RuntimeError('input drift '+name)
 rows.append({'path':name,'sha256':h,'bytes':len(b),'scope':'late producer/gate accepted; contact table and cubic coordinate interface explicitly hypothesized here'})
with (P/'input-pins.json').open('x') as f:json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'entries':rows},f,indent=2)
r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/triple-one-plus-double-separated-astra-20260909.md'),'--basis','0d39df3c9fd69c939a8420c54d03228b9077777d','--owner','/root/nonemptiness_certificate'],capture_output=True,timeout=25,check=True)
fd=os.open(P/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
print(json.dumps({'partial':json.loads(r.stdout)['partial_path'],'inputs':len(rows)}))
