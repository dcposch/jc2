import sys
sys.dont_write_bytecode=True
import os,json,hashlib,subprocess,datetime,resource,urllib.request
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2'); P=Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
inputs=['COORDINATION.md','APPROACHES.md','ladder/REDUCTION.md','AUDIT.md','xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md','xmodel/d125-client-interface-astra-20260906.md','xmodel/row2515-order-gate-sol56-20260903.md','xmodel/topface-license-sol56-20260903.md','xmodel/twopoint-batch-gpt55-20260903.md','box/census-coverage-20260905/core-ggv-layout.txt','box/census-coverage-20260905/moh-layout.txt']
rows=[]
for name in inputs:
 b=(R/name).read_bytes(); rows.append({'path':name,'sha256':sha(b),'bytes':len(b)})
with (P/'input-pins.json').open('x') as f:json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'inputs':rows},f,indent=2)
for name,source in [('ggv-v3.txt','box/census-coverage-20260905/core-ggv-layout.txt'),('moh.txt','box/census-coverage-20260905/moh-layout.txt')]:
 with (P/name).open('xb') as f:f.write((R/source).read_bytes())
c=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/source-multiplicity-admissibility-astra-20260909.md'),'--basis','0d39df3c9fd69c939a8420c54d03228b9077777d','--owner','/root/nonemptiness_certificate'],capture_output=True,check=True,timeout=25)
fd=os.open(P/'capability.json',os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
with os.fdopen(fd,'wb') as f:f.write(c.stdout)
print(json.dumps({'partial':json.loads(c.stdout)['partial_path'],'input_count':len(rows)}))
