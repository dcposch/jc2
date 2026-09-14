import sys
sys.dont_write_bytecode=True
import os,json,hashlib,subprocess,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2'); P=Path(__file__).resolve().parent
expected={
'xmodel/d125-weightfree-reference-source-astra-20260909.md':'cbc0330b001faeb8692e45c3be3fdcd3c0727b5734e648143642234da5d63696',
'xmodel/positive-face-actual-receiver-discriminator-astra-20260906.md':'07e53340002c48b29a97d567ceb9eb867a292e9cbdd932ce7f508e0694875c46',
'xmodel/positive-face-actual-receiver-gate-fable5-20260906.md':'eade8ec8b9b9162bf3a6a9e60408094185b63b633e6343cce11b7e233e904284',
'xmodel/source-multiplicity-admissibility-astra-20260909.md':'909ba868b027834a31c6eda37546f17694478cad93d35233d047f1321c0875c0'}
entries=[]
for name,pin in expected.items():
 b=(R/name).read_bytes(); got=hashlib.sha256(b).hexdigest()
 if got!=pin: raise RuntimeError('input drift '+name)
 entries.append({'path':name,'sha256':got,'bytes':len(b),'read_scope':'whole file including seal; gate through BODY-END'})
with (P/'input-pins.json').open('x') as f:json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'entries':entries},f,indent=2)
r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/late-contact-triple-endpoint-astra-20260909.md'),'--basis','0d39df3c9fd69c939a8420c54d03228b9077777d','--owner','/root/nonemptiness_certificate'],capture_output=True,check=True,timeout=25)
fd=os.open(P/'capability.json',os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
print(json.dumps({'partial':json.loads(r.stdout)['partial_path'],'inputs':len(entries)}))
