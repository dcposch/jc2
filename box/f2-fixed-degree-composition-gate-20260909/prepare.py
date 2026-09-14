import sys
sys.dont_write_bytecode=True
import os,json,hashlib,subprocess,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent;I=P/'inputs';I.mkdir(exist_ok=False)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(c,m):
 if not c:raise RuntimeError(m)
data=[
('xmodel/f2-fixed-degree-standardization-gate-astra-20260909.md','astra-source-audit.md','3935d7633e472dcbb0a7d14c5e2386d693e338001f21a82f04c02d4bc468a205','WHOLE new proof'),
('xmodel/f2-fixed-degree-composition-coordinator-20260909.md','coordinator-joint-proof.md','aeeddd6a501d59529120a49377ecf42aa22314d880c4304f65cc6dd56091d318','WHOLE new proof'),
('xmodel/d125-published-chain-discriminator-astra-20260906.md','accepted-f2-chain-proof.md','9b439af269c23e349615d3e404e0732c9c7f491a9342d5500e061aab91ad4e88','WHOLE necessary source interface; historical computational descriptions are not replay authority'),
('xmodel/d125-published-chain-gate-fable5-20260906.md','accepted-f2-chain-review.md','5be50d001d285481233c8de415b2f4d22411a22cb930a0c1db287c0579b3cd7b','WHOLE accepted interface and exact import perimeter; no old controls consumed or rerun'),
('xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md','accepted-minimal-map-proof.md','7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413','WHOLE polynomial cone/map/top/scalar interface'),
('xmodel/d125-minimal-receiver-gate-fable5-20260906.md','accepted-minimal-map-review.md','cd69c23885de119e4bd910992dad5ef695e7b12013168ec1c401546d8aa6ed8d','WHOLE accepted map interface; no old controls consumed or rerun'),
('xmodel/d125-weightfree-client-interface-astra-20260909.md','accepted-wf-client-interface.md','dcb3a30a48c5977005083a3ad7bbc5935e1f2f74ade6c3569a4b45751c213276','WHOLE conditional map; its then-unreviewed WF status is superseded only by frozen15q'),
('box/f2-fixed-degree-standardization-gate-20260909/makar-limanov-serdica-2025.txt','primary-ml-whole.txt','b9cf07f455c48d1e90d826e2be1ba6efcc65daafb4c70a2de436012777a669e6f','PLACEHOLDER'),
]
# Correct explicit ML pin; no numeric serialization or mathematical work occurs.
data[-1]=(data[-1][0],data[-1][1],'b9cf07f455c48d1e90d826e2be1ba6efcc48e67e1b1dff4ceacc017875d87215','Required printed302-305 full normalization proof plus preceding independence lemma; later reductions optional and not premises')
old=R/'box/f2-fixed-degree-standardization-gate-20260909'
for rel,name in [
('xmodel/f2-fixed-degree-standardization-gate-astra-20260909.md.artifact.json','astra-source-transaction.json'),
('xmodel/f2-fixed-degree-composition-coordinator-20260909.md.artifact.json','coordinator-joint-transaction.json'),
('box/f2-fixed-degree-standardization-gate-20260909/custody.json','astra-source-custody.json'),
('box/f2-fixed-degree-standardization-gate-20260909/input-pins.json','astra-source-input-pins.json'),
('box/f2-fixed-degree-standardization-gate-20260909/publication.json','astra-source-publication.json'),
('box/f2-fixed-degree-standardization-gate-20260909/source-record.md','primary-read-scope.md'),
('box/f2-fixed-degree-standardization-gate-20260909/chau-0408077v1.txt','primary-chau-whole.txt')]:
 data.append((rel,name,sha(R/rel),'METADATA ONLY' if name.endswith('.json') else ('WHOLE read-scope metadata' if name.endswith('.md') else 'Required Division Lemma and Section3 proof; remainder optional primary reference')))
entries=[]
for rel,name,pin,scope in data:
 src=R/rel;require(sha(src)==pin,'pin drift '+rel);raw=src.read_bytes();dst=I/name
 with dst.open('xb') as f:f.write(raw)
 dst.chmod(0o444);entries.append({'source':rel,'source_sha256':pin,'snapshot':str(dst.relative_to(R)),'sha256':sha(dst),'bytes':len(raw),'read_scope':scope,'extraction':'WHOLE'})
extracts=[
('box/f2-fixed-degree-standardization-gate-20260909/ggv-1401.1784v3.txt','primary-ggv-exact-statements.txt',[(695,747),(1431,1461),(2259,2292)],'WHOLE selected Def4.3/Prop4.1/Prop5.20/Cor7.9 statements and proofs; minimality surroundings retained'),
('box/f2-fixed-degree-standardization-gate-20260909/gghv-1708.07936v1.txt','primary-gghv-exact-chain-tables.txt',[(205,338),(613,817),(910,1050),(1120,1258),(1362,1464)],'WHOLE selected valid-edge/complete-chain/admissibility/family statements and proofs, Section5 tables; published enumeration imported, not rerun')]
for rel,name,ranges,scope in extracts:
 src=R/rel;raw=src.read_bytes();lines=raw.splitlines(keepends=True)
 out=b''
 for lo,hi in ranges:
  out+=('\n===== EXACT PRIMARY TEXT LINES %d-%d =====\n'%(lo,hi)).encode()+b''.join(lines[lo-1:hi])
 dst=I/name
 with dst.open('xb') as f:f.write(out)
 dst.chmod(0o444);entries.append({'source':rel,'source_sha256':hashlib.sha256(raw).hexdigest(),'snapshot':str(dst.relative_to(R)),'sha256':sha(dst),'bytes':len(out),'read_scope':scope,'extraction':ranges})
src=R/'AUDIT.md';raw=src.read_bytes();start=raw.index(b'### 17(qqqqqqqqqqqqqqq)');end=raw.index(b'### 17(rrrrrrrrrrrrrrr)',start);out=raw[start:end];dst=I/'accepted-audit15q-only.md'
with dst.open('xb') as f:f.write(out)
dst.chmod(0o444);entries.append({'source':'AUDIT.md','source_sha256':hashlib.sha256(raw).hexdigest(),'source_bytes':len(raw),'snapshot':str(dst.relative_to(R)),'sha256':sha(dst),'bytes':len(out),'read_scope':'WHOLE exact accepted theorem, corrections and scope; NO original WF review or its prohibited code charged','extraction':{'start_byte':start,'end_byte_exclusive':end,'heading':'17(qqqqqqqqqqqqqqq)'}})
verifications=[]
for rel in ['xmodel/f2-fixed-degree-standardization-gate-astra-20260909.md','xmodel/f2-fixed-degree-composition-coordinator-20260909.md']:
 r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'verify','--final',str(R/rel)],capture_output=True,timeout=10,check=True);verifications.append(json.loads(r.stdout))
with (P/'PINS.json').open('x') as f:json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'frozen_basis':'0d39df3c9fd69c939a8420c54d03228b9077777d','status':'PREP_ONLY_NOT_LAUNCHED','entries':entries,'transactions':verifications,'mathematical_subprocesses':0},f,indent=2)
r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/f2-fixed-degree-composition-gate-prep-astra-20260909.md'),'--basis','0d39df3c9fd69c939a8420c54d03228b9077777d','--owner','/root/nonemptiness_certificate'],capture_output=True,timeout=10,check=True)
fd=os.open(P/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
print(json.dumps({'partial':json.loads(r.stdout)['partial_path'],'snapshots':len(entries),'snapshot_bytes':sum(e['bytes'] for e in entries),'pins_sha256':sha(P/'PINS.json')}))
