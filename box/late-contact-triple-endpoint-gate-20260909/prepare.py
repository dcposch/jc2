import sys
sys.dont_write_bytecode=True
import os,json,hashlib,subprocess,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(c,m):
 if not c:raise RuntimeError(m)
old=R/'box/late-contact-triple-endpoint-20260909'
require(sha(old/'custody.json')=='6cacbdeda4895267d6639e88f0bdaf4efd2004f0547b446a126e01bdb35a8872','custody drift')
cust=json.loads((old/'custody.json').read_bytes())
for e in cust['entries']+cust['inputs']:require(sha(R/e['path'])==e['sha256'],'old pin drift '+e['path'])
v=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'verify','--final',str(R/'xmodel/late-contact-triple-endpoint-astra-20260909.md')],capture_output=True,timeout=25,check=True)
data=[
('xmodel/late-contact-triple-endpoint-astra-20260909.md','late-triple-proof.md'),
('xmodel/d125-weightfree-reference-source-astra-20260909.md','two-pattern-framework.md'),
('xmodel/positive-face-actual-receiver-discriminator-astra-20260906.md','actual-moh-source.md'),
('xmodel/positive-face-actual-receiver-gate-fable5-20260906.md','actual-moh-source-gate.md'),
('xmodel/source-multiplicity-admissibility-astra-20260909.md','multiplicity-admissibility.md'),
('xmodel/late-contact-triple-endpoint-astra-20260909.md.artifact.json','late-triple-transaction.json'),
('box/late-contact-triple-endpoint-20260909/custody.json','late-triple-custody.json'),
('box/late-contact-triple-endpoint-20260909/input-pins.json','late-triple-input-pins.json'),
('box/late-contact-triple-endpoint-20260909/publication.json','late-triple-publication.json')]
(P/'inputs').mkdir(exist_ok=False);rows=[]
for source,name in data:
 src=R/source;dst=P/'inputs'/name;b=src.read_bytes()
 with dst.open('xb') as f:f.write(b)
 require(sha(dst)==sha(src),'copy drift');dst.chmod(0o444)
 rows.append({'source':source,'snapshot':str(dst.relative_to(R)),'sha256':sha(dst),'bytes':len(b),'read_scope':'whole proof/report, metadata files are provenance only'})
with (P/'PINS.json').open('x') as f:json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PREP_ONLY_NO_LAUNCH','frozen_basis':'0d39df3c9fd69c939a8420c54d03228b9077777d','entries':rows,'producer_transaction_verification':json.loads(v.stdout),'source_status':'late triple theorem unreviewed; two-pattern framework never a triple premise'},f,indent=2)
(P/'PINS.json').chmod(0o444)
r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/late-contact-triple-endpoint-gate-prep-astra-20260909.md'),'--basis','0d39df3c9fd69c939a8420c54d03228b9077777d','--owner','/root/nonemptiness_certificate'],capture_output=True,timeout=25,check=True)
fd=os.open(P/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
print(json.dumps({'partial':json.loads(r.stdout)['partial_path'],'snapshots':len(rows),'pins_sha256':sha(P/'PINS.json')}))
