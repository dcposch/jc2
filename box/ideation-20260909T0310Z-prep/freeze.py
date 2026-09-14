import sys
sys.dont_write_bytecode=True
import json, hashlib, datetime, subprocess, os, resource, re
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(25,25));resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
R=Path('/home/ubuntu/jc2');B=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def need(c,m):
 if not c:raise RuntimeError(m)
def since(src,marker):
 lines=(R/src).read_bytes().splitlines(keepends=True); starts=[i for i,x in enumerate(lines) if x.startswith(marker)]
 need(bool(starts),'marker missing '+src);return(starts[-1]+1,len(lines))
notes=(R/'notes.md').read_bytes().splitlines(keepends=True)
idx=[i for i,x in enumerate(notes) if re.match(rb'^#{2,3} .*LIVE STATE',x)]
need(bool(idx),'LIVE missing');need(b'03:0' in notes[idx[-1]],'WAIT: root fresh03:09 LIVE not frozen yet')
specs=[
('COORDINATION.md','coordination.md',None),('APPROACHES.md','approaches.md',None),('PROGRESS.md','progress.md',None),
('notes.md','latest-live.md',(idx[-1]+1,len(notes))),('AUDIT.md','audit-guide.md',(1,40)),
('AUDIT.md','accepted-15q-through-15v.md',since('AUDIT.md',b'### 17(qqqqqqqqqqqqqqq)')),
('history/APPROACHES-before-20260906-cleanup.md','master46-history.md',(257,309)),
('ladder/REDUCTION.md','reduction.md',None),
('xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md','binding-bd-gal.md',None),
('xmodel/ideation-20260909T0040Z-synthesis.md','last-0040-synthesis.md',None),
('xmodel/ideation-20260909T0040Z-synthesis.md.artifact.json','last-0040-transaction.json',None),
('xmodel/websweep-20260908T2212Z-astra.md','last-broad-sweep.md',None),
('xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md','minimal-receiver.md',None),
('xmodel/positive-face-actual-receiver-discriminator-astra-20260906.md','actual-moh-source.md',None),
('xmodel/positive-face-actual-receiver-gate-fable5-20260906.md','actual-moh-source-gate.md',None),
('xmodel/d125-client-interface-astra-20260906.md','remaining-m90-source-interface.md',None),
('xmodel/late-contact-triple-endpoint-astra-20260909.md','accepted-15s-proof.md',None),
('xmodel/late-contact-triple-endpoint-gate-fable5-20260909.md','accepted-15s-gate.md',None),
('xmodel/triple-cubic-source-coalesced-astra-20260909.md','accepted-15t-proof.md',None),
('xmodel/triple-cubic-source-coalesced-gate-fable5-20260909.md','accepted-15t-gate.md',None),
('xmodel/triple-source-contact-cover-astra-20260909.md','accepted-15u-contact-cover.md',None),
('xmodel/triple-three-simple-separated-coordinator-20260909.md','accepted-15u-three-simple.md',None),
('xmodel/triple-cover-three-simple-gate-fable5-20260909.md','accepted-15u-gate.md',None),
('xmodel/triple-one-plus-double-separated-astra-20260909.md','accepted-15v-proof.md',None),
('xmodel/triple-one-plus-double-gate-fable5-20260909.md','accepted-15v-gate.md',None),
('xmodel/late-contact-keller-descent-astra-20260909.md','provisional-allD-descent.md',None),
('xmodel/late-contact-direct-obstruction-coordinator-20260909.md','provisional-allD-direct.md',None),
('xmodel/late-contact-descent-admissibility-astra-20260909.md','root-checked-allD-admissibility.md',None)]
required={
'binding-bd-gal.md':'f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8',
'last-0040-synthesis.md':'e97b254a0615cd583ac657cdf2a2ab0e11096f3f7a3d2c5ed6d56e690c8d1d3b',
'last-broad-sweep.md':'364431f6267629e2f45e49785b18bf6393f4a9b4f2b59b4d3ee47047a70440dc',
'minimal-receiver.md':'7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413',
'actual-moh-source.md':'07e53340002c48b29a97d567ceb9eb867a292e9cbdd932ce7f508e0694875c46',
'actual-moh-source-gate.md':'eade8ec8b9b9162bf3a6a9e60408094185b63b633e6343cce11b7e233e904284',
'remaining-m90-source-interface.md':'0c5270a432a6336c17c4693034e36cb496f139c3267843e3ac06628ec8c4b255',
'accepted-15s-proof.md':'b541308788da31f52e9f7985c7767e206231e8f3251ff53c1b2bd9c96b64f097',
'accepted-15s-gate.md':'c9a399a87dc91d78bfc4f811249996ea3e217eda075be679cf27b41af5795c26',
'accepted-15t-proof.md':'1620f9ef6b2edc598d35cab274cdfcc24d71353d18132d3a35ffb59fd2c46099',
'accepted-15t-gate.md':'cc5f4ca64fef11197c84e6d19b6bc8b5c3d526adac05cb66b28d94573144525b',
'accepted-15u-contact-cover.md':'f3ab28a6b26345cfd4ce2bd74cf77a335acdf7865c650a4662964a2e738edc08',
'accepted-15u-three-simple.md':'0ec157b262e8658e493b98ff0776bce4603cb8aa1b731fc93f38e58372637d83',
'accepted-15u-gate.md':'0d1d2e7ce9393f4fe316cf62521a7d5c963db7876117be83f4221e6c81e6da4f',
'accepted-15v-proof.md':'7709b0da88c6fa42fcbea38b9209573855edb1d6167c2cb77c1f8e374a5d1368',
'accepted-15v-gate.md':'fb281624a480b34c8950e45035a141f43ae1af137fbdc3d86f1ce541899336dd',
'provisional-allD-descent.md':'857b2e2fa93cc14acb24fa590a2ffa76961a0d136113908f12b213e126889672',
'provisional-allD-direct.md':'2dcff1644acdc77a4665916d71dd4865b6f8f35d0965fb43ece6dd3c671393fa',
'root-checked-allD-admissibility.md':'aae419fdf0051b915a44f5fd517ce06b7d9bfcd55efbd16985710e04e63dc67a'}
# Check all supplied pins BEFORE snapshot/body consumers. No mathematical execution.
for src,dst,span in specs:
 if dst in required:need(sha(R/src)==required[dst],'released source drift '+src)
for old in ['box/late-contact-descent-admissibility-20260909/custody.json','box/late-contact-keller-descent-20260909/custody.json']:
 cu=json.loads((R/old).read_bytes())
 for e in cu['entries']+cu['inputs']:need(sha(R/e['path'])==e['sha256'],'custody drift '+e['path'])
S=B/'snapshots';S.mkdir(exist_ok=False);M=B/'metadata';M.mkdir(exist_ok=False);entries=[];provenance=[]
for src,dst,span in specs:
 p=R/src; data=p.read_bytes(); before=sha(p);out=data if span is None else b''.join(data.splitlines(keepends=True)[span[0]-1:span[1]])
 q=S/dst
 with q.open('xb') as f:f.write(out)
 need(sha(p)==before,'source changed during copy');q.chmod(0o444)
 entries.append({'source':src,'source_sha256':before,'lines':span,'path':str(q.relative_to(R)),'sha256':sha(q),'bytes':len(out)})
 if src.startswith('xmodel/') and (R/(src+'.artifact.json')).is_file():
  z=R/(src+'.artifact.json'); zz=M/(dst+'.transaction.json')
  with zz.open('xb') as f:f.write(z.read_bytes())
  zz.chmod(0o444);provenance.append({'source':str(z.relative_to(R)),'path':str(zz.relative_to(R)),'sha256':sha(zz),'bytes':zz.stat().st_size})
for name in ['packet.md','contract.md','root-release.md']:
 p=B/name;entries.append({'source':str(p.relative_to(R)),'source_sha256':sha(p),'lines':None,'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
manifest={'schema':'JC2-BLIND-PACKET/v1','freeze_utc':now,'basis':'0d39df3c9fd69c939a8420c54d03228b9077777d','stage':'PREP_ONLY_EQUAL_PACKET_READY_NOT_INVITED','invitation_utc':None,'blind_deadline_utc':None,'launch_authorized':False,'root_blind_required_first':True,'core_models':['coordinator','astra','fable5','sol56'],'omitted_noninterruptible_worker':'late-contact-keller-direct-gate-fable5-20260909 (not an ideator)','last_completed_full':'2026-09-09T01:57:40Z','next_full_backstop':'2026-09-09T13:57:40Z','last_broad_cutoff':'2026-09-08T22:24:26.958594Z','mathematical_subprocesses_allowed':0,'entries':entries,'provenance_only':provenance}
with (B/'MANIFEST.json').open('x') as f:json.dump(manifest,f,indent=2)
paths=[e['path'] for e in entries]+[str((B/'MANIFEST.json').relative_to(R))]
common='\n'.join('charged_input='+p for p in paths)+'\n\nRead every common frozen input in {{LANE_INPUTS}} WHOLE and follow contract.md. Same state/contract/tool boundary for all seats. ZERO mathematical subprocesses. No peer/live body access. No start or deadline is authorized until root explicit invitation; root must seal its SAME-PACKET blind first. Append BODY-END only after substantive completion; omit charge_basis.\n'
for seat in ['coordinator','astra','fable5','sol56']:
 with (B/(seat+'.prompt.md')).open('x') as f:f.write(common+'Write exactly xmodel/ideation-20260909T0310Z-'+seat+'.md.\n')
for p in [B/'MANIFEST.json',B/'packet.md',B/'contract.md',B/'root-release.md']+[B/(x+'.prompt.md') for x in ['coordinator','astra','fable5','sol56']]:p.chmod(0o444)
pins={str(p.relative_to(R)):sha(p) for p in sorted(B.rglob('*')) if p.is_file()}
with (B/'PINS.json').open('x') as f:json.dump(pins,f,indent=2)
r=subprocess.run(['/usr/bin/python3','-I','-B',str(R/'ops/artifact_finalize.py'),'begin','--final',str(R/'xmodel/ideation-20260909T0310Z-prep-astra.md'),'--basis',manifest['basis'],'--owner','/root/nonemptiness_certificate'],capture_output=True,timeout=25,check=True)
fd=os.open(B/'capability.json',os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
with os.fdopen(fd,'wb') as f:f.write(r.stdout)
print(json.dumps({'partial':json.loads(r.stdout)['partial_path'],'freeze_utc':now,'charged':len(paths),'snapshot_count':len(specs),'content_bytes':sum(x['bytes'] for x in entries),'manifest_sha256':sha(B/'MANIFEST.json'),'pins_sha256':sha(B/'PINS.json'),'launch':False}))
