import sys
sys.dont_write_bytecode=True
import json,hashlib,subprocess,os,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent
DATA=[
('xmodel/d125-weightfree-reference-source-astra-20260909.md','framework.md','cbc0330b001faeb8692e45c3be3fdcd3c0727b5734e648143642234da5d63696'),
('xmodel/d125-weightfree-reference-source-astra-20260909.md.artifact.json','framework-transaction.json','80de225fb7e13eb0520b968ad137ff9528ccd0403aa96f5c03f2fdafb384254f'),
('xmodel/d125-weightfree-client-interface-astra-20260909.md','client-interface.md','dcb3a30a48c5977005083a3ad7bbc5935e1f2f74ade6c3569a4b45751c213276'),
('xmodel/d125-weightfree-client-interface-astra-20260909.md.artifact.json','client-transaction.json','2b22ef07b5c1941136ee0a2080a302e23e0120768dc9b40d654dd076359dfea1'),
('xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md','minimal-receiver.md','7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413'),
('xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md','sufficient-lift.md','433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad'),
('xmodel/d125-published-chain-gate-fable5-20260906.md','published-chain-gate.md','5be50d001d285481233c8de415b2f4d22411a22cb930a0c1db287c0579b3cd7b')]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[];(P/'inputs').mkdir(exist_ok=False)
for src,name,h in DATA:
 source=R/src
 if sha(source)!=h:raise RuntimeError('source drift '+src)
 target=P/'inputs'/name
 with target.open('xb') as f:f.write(source.read_bytes())
 if sha(target)!=h:raise RuntimeError('snapshot drift')
 rows.append({'source':src,'snapshot':str(target.relative_to(R)),'sha256':h,'bytes':target.stat().st_size})
checks=[]
for final in ('xmodel/d125-weightfree-reference-source-astra-20260909.md','xmodel/d125-weightfree-client-interface-astra-20260909.md'):
 r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'verify','--final',str(R/final)],capture_output=True,timeout=25,check=True);checks.append(json.loads(r.stdout))
with (P/'known-inputs.json').open('xb') as f:f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PENDING_ROOT_LOCAL_CONSUMER_NO_LAUNCH','entries':rows,'transactions':checks},indent=2).encode())
cmd=['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/d125-weightfree-composition-gate-prep-astra-20260909.md'),'--basis','0d39df3c9fd69c939a8420c54d03228b9077777d','--owner','/root/nonemptiness_certificate']
r=subprocess.run(cmd,capture_output=True,timeout=25,check=True);fd=os.open(P/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
c=json.loads(r.stdout);print(json.dumps({'status':'PENDING_ROOT_INPUT','frozen_inputs':len(rows),'partial':c['partial_path']}))
