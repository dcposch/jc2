import sys
sys.dont_write_bytecode=True
import os,json,hashlib,subprocess,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(c,m):
 if not c:raise RuntimeError(m)
old=R/'box/triple-one-plus-double-separated-20260909'
require(sha(old/'custody.json')=='87f91c7f870354b2234249ca7e02ae8c66d0feb8026c512ac0f1d80daf3e5389','custody drift')
cust=json.loads((old/'custody.json').read_bytes())
for e in cust['entries']+cust['inputs']:require(sha(R/e['path'])==e['sha256'],'producer pin drift')
v=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'verify','--final',str(R/'xmodel/triple-one-plus-double-separated-astra-20260909.md')],capture_output=True,timeout=25,check=True)
data=[
('xmodel/triple-one-plus-double-separated-astra-20260909.md','one-plus-double-proof.md','7709b0da88c6fa42fcbea38b9209573855edb1d6167c2cb77c1f8e374a5d1368'),
('xmodel/triple-cubic-source-coalesced-astra-20260909.md','accepted-cubic-producer.md','1620f9ef6b2edc598d35cab274cdfcc24d71353d18132d3a35ffb59fd2c46099'),
('xmodel/triple-cubic-source-coalesced-gate-fable5-20260909.md','accepted-cubic-gate.md','cc5f4ca64fef11197c84e6d19b6bc8b5c3d526adac05cb66b28d94573144525b'),
('xmodel/late-contact-triple-endpoint-astra-20260909.md','accepted-late-contact-producer.md','b541308788da31f52e9f7985c7767e206231e8f3251ff53c1b2bd9c96b64f097'),
('xmodel/late-contact-triple-endpoint-gate-fable5-20260909.md','accepted-late-contact-gate.md','c9a399a87dc91d78bfc4f811249996ea3e217eda075be679cf27b41af5795c26'),
('xmodel/triple-source-contact-cover-astra-20260909.md','conditional-contact-table.md','f3ab28a6b26345cfd4ce2bd74cf77a335acdf7865c650a4662964a2e738edc08'),
('xmodel/triple-one-plus-double-separated-astra-20260909.md.artifact.json','one-plus-double-transaction.json','a86d3157fb1a2a781615507349635660448a2eda460340c1b81062b800eab7dc'),
('box/triple-one-plus-double-separated-20260909/custody.json','one-plus-double-custody.json','87f91c7f870354b2234249ca7e02ae8c66d0feb8026c512ac0f1d80daf3e5389'),
('box/triple-one-plus-double-separated-20260909/input-pins.json','one-plus-double-input-pins.json','e6060a849955f53b611979d8ecd1d0ef541b2d8f6aa461b5224ad6c3875bee5c'),
('box/triple-one-plus-double-separated-20260909/publication.json','one-plus-double-publication.json','39a4de295fafbbb5b80d3c590d77f7333960ad998c879f5c9dfb674342194033')]
(P/'inputs').mkdir(exist_ok=False);rows=[]
for src,name,h in data:
 source=R/src;require(sha(source)==h,'source drift '+src);dst=P/'inputs'/name;b=source.read_bytes()
 with dst.open('xb') as f:f.write(b)
 require(sha(dst)==h,'snapshot drift');dst.chmod(0o444)
 rows.append({'source':src,'snapshot':str(dst.relative_to(R)),'sha256':h,'bytes':len(b),'tier':'CONDITIONAL_TABLE_ONLY_NOT_ACCEPTED' if name=='conditional-contact-table.md' else 'producer proof pending review' if name=='one-plus-double-proof.md' else 'accepted exact statement or metadata as labelled'})
with (P/'PINS.json').open('x') as f:json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PREP_ONLY_NOT_LAUNCHED','frozen_basis':'0d39df3c9fd69c939a8420c54d03228b9077777d','entries':rows,'transaction_verification':json.loads(v.stdout),'whole_source_composition':'NOT CHARGED AS PROVED'},f,indent=2)
(P/'PINS.json').chmod(0o444)
r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/triple-one-plus-double-gate-prep-astra-20260909.md'),'--basis','0d39df3c9fd69c939a8420c54d03228b9077777d','--owner','/root/nonemptiness_certificate'],capture_output=True,timeout=25,check=True)
fd=os.open(P/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
print(json.dumps({'partial':json.loads(r.stdout)['partial_path'],'snapshots':len(rows),'pins_sha256':sha(P/'PINS.json')}))
