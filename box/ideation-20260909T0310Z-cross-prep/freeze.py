import sys
sys.dont_write_bytecode=True
import os,json,hashlib,subprocess,datetime,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');P=Path(__file__).resolve().parent;I=P/'inputs';I.mkdir(exist_ok=False);O=R/'box/ideation-20260909T0310Z-prep'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def require(c,m):
 if not c:raise RuntimeError(m)
rows=[]
def copy(src,name,pin,scope='WHOLE'):
 require(sha(src)==pin,'input drift '+str(src));raw=src.read_bytes();dst=I/name
 with dst.open('xb') as f:f.write(raw)
 dst.chmod(0o444);rows.append({'source':str(src.relative_to(R)),'source_sha256':pin,'snapshot':str(dst.relative_to(R)),'sha256':sha(dst),'bytes':len(raw),'read_scope':scope})
for seat,pin in [('coordinator','64d3b5a24b382a7833479e4c7c41b3b28c73d67964bc73a8e7c7fc2552393d47'),('astra','47e1475aeb83b53446e2e8f5df3fae7136941d68715b654d537ddd7e30b36d1a'),('fable5','ecd7305aa30862716a78452bd284284211f15873b12587493df7fc96e5ee5866383'),('sol','ce12b6406f95178372fce98ca2f9719b30a9d028c096c395f76a9e7609e33e60')]:
 if seat=='fable5':pin='ecd7305aa30862716a78452bd284211f15873b12587493df7fc96e5ee5866383'
 copy(R/f'xmodel/ideation-20260909T0310Z-{seat}.md',f'blind-{seat}.md',pin)
manifest=json.loads((O/'ROOT-FINAL-MANIFEST.json').read_bytes());byname={Path(e['path']).name:e for e in manifest['entries']}
for name in ['coordination.md','approaches.md','master46-history.md','reduction-interfaces.md','root-checked-allD-admissibility.md','remaining-m90-source-interface.md','last-0040-synthesis.md','binding-bd-gal.md']:
 e=byname[name];copy(R/e['path'],'frozen-'+name,e['sha256'])
copy(O/'ROOT-FINAL-MANIFEST.json','original-0310-manifest.json',sha(O/'ROOT-FINAL-MANIFEST.json'),'METADATA ONLY: actual31 entries plus manifest32 files')
for rel,name,pin in [
('xmodel/late-contact-keller-direct-gate-fable5-20260909.md','accepted-15w-review.md','41a72b886ed2f00815849078e915207b8fc8d215e8bf715aa3c7103df2d8db1e'),
('xmodel/f2-fixed-degree-composition-coordinator-20260909.md','provisional-fixed-degree-composition.md','aeeddd6a501d59529120a49377ecf42aa22314d880c4304f65cc6dd56091d318'),
('xmodel/f2-fixed-degree-standardization-gate-astra-20260909.md','provisional-primary-source-audit.md','3935d7633e472dcbb0a7d14c5e2386d693e338001f21a82f04c02d4bc468a205')]:copy(R/rel,name,pin)
src=R/'AUDIT.md';raw=src.read_bytes();start=raw.index(b'### 17(wwwwwwwwwwwwwww)');nxt=raw.find(b'\n### ',start+1);end=len(raw) if nxt<0 else nxt;dst=I/'accepted-audit15w-only.md'
with dst.open('xb') as f:f.write(raw[start:end])
rows.append({'source':'AUDIT.md','source_sha256':hashlib.sha256(raw).hexdigest(),'snapshot':str(dst.relative_to(R)),'sha256':sha(dst),'bytes':dst.stat().st_size,'read_scope':'WHOLE exact named15w paragraph','extraction':{'start':start,'end':end}})
src=R/'box/f2-fixed-degree-standardization-gate-20260909/ggv-1401.1784v3.txt';raw=src.read_bytes();lines=raw.splitlines(keepends=True);out=b''
for lo,hi in [(168,182),(360,394)]:out+=('\n===== EXACT PRIMARY LINES %d-%d =====\n'%(lo,hi)).encode()+b''.join(lines[lo-1:hi])
dst=I/'primary-balanced-top-exclusion.txt'
with dst.open('xb') as f:f.write(out)
rows.append({'source':str(src.relative_to(R)),'source_sha256':hashlib.sha256(raw).hexdigest(),'snapshot':str(dst.relative_to(R)),'sha256':sha(dst),'bytes':len(out),'read_scope':'WHOLE endpoint definitions, Remark2.5 and Theorem2.6 proof','extraction':[[168,182],[360,394]],'primary_url':'https://arxiv.org/pdf/1401.1784v3'})
for name in ['contract.md','poststate.md']:copy(P/name,'common-'+name,sha(P/name))
with (P/'PINS.json').open('x') as f:json.dump({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'frozen_basis':'0d39df3c9fd69c939a8420c54d03228b9077777d','stage':'CROSS_PREP_ONLY_NO_INVITATIONS','entries':rows,'original_manifest_entries':len(manifest['entries']),'original_with_self':1+len(manifest['entries']),'blind_bodies_read_by_preparer':False,'mathematical_subprocesses':0},f,indent=2)
vector=[str((P/'PINS.json').relative_to(R))]+[e['snapshot'] for e in rows]
for seat in ['astra','fable5','sol']:
 text='# 0310 equal cross invitation template — PREP ONLY\n'+'tag=ideation-20260909T0310Z-cross-'+seat+'\nreport=xmodel/ideation-20260909T0310Z-cross-'+seat+'.md\nfrozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d\n'+''.join('charged_input='+p+'\n' for p in vector)+'\nRead and follow common-contract.md and common-poststate.md WHOLE under {{LANE_INPUTS}}. All listed files are the identical frozen cross vector, not mutable paths. Root alone invites; prospective common deadline2026-09-09 04:40 UTC. No mathematical subprocesses of any size. This template is not an invitation.\n'
 with (P/(seat+'.prompt.md')).open('x') as f:f.write(text)
r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/ideation-20260909T0310Z-cross-prep-astra.md'),'--basis','0d39df3c9fd69c939a8420c54d03228b9077777d','--owner','/root/nonemptiness_certificate'],capture_output=True,timeout=10,check=True)
fd=os.open(P/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
print(json.dumps({'partial':json.loads(r.stdout)['partial_path'],'snapshots':len(rows),'bytes':sum(e['bytes'] for e in rows),'charged':len(vector),'pins_sha256':sha(P/'PINS.json'),'original_entries':len(manifest['entries'])}))
