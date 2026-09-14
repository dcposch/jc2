"""One-shot mechanical snapshot and equal prompt rendering; no launch operations."""
import datetime, hashlib, json, pathlib, shutil
R=pathlib.Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260908T2220Z'
S=B/'snapshots'; S.mkdir(exist_ok=False)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
specs=[('COORDINATION.md','coordination.md',None),('APPROACHES.md','approaches.md',None),('notes.md','live-2219.md',(21861,21875)),('AUDIT.md','audit-guide.md',(1,40)),('AUDIT.md','audit-15h-through-15l.md',(18850,18892)),('history/APPROACHES-before-20260906-cleanup.md','master46-history.md',(257,309)),('xmodel/ideation-20260908T0200Z-synthesis.md','previous-0200-synthesis.md',None),('xmodel/websweep-20260907T0735Z-astra.md','last-broad-sweep.md',None),('xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md','minimal-receiver.md',None),('xmodel/uniform-cone-jacobian-degree-astra-20260908.md','accepted-uniform-proof.md',None),('xmodel/golden-two-regime-initial-discriminator-astra-20260908.md','provisional-golden-proof.md',None),('xmodel/golden-two-regime-initial-discriminator-astra-20260908.md.artifact.json','golden-transaction.json',None)]
for f in ['custody.json','check.py','replay.json','input-pins.json']:
 specs.append(('box/golden-two-regime-initial-discriminator-20260908/'+f,'golden-'+f,None))
entries=[]
for src,dst,lines in specs:
 p=R/src; q=S/dst
 if lines:
  data=p.read_bytes().splitlines(keepends=True); q.write_bytes(b''.join(data[lines[0]-1:lines[1]]))
 else: shutil.copyfile(p,q)
 entries.append(dict(source=src,source_sha256=sha(p),lines=lines,path=str(q.relative_to(R)),sha256=sha(q),bytes=q.stat().st_size))
required={'provisional-golden-proof.md':'14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6','golden-custody.json':'fcc12304ee659dc5b83eb8f5e323a8c38a7cf3616e6a4b2f4b53cd1ca438568d','minimal-receiver.md':'7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413'}
for name,h in required.items():
 if sha(S/name)!=h: raise SystemExit('REFUSE drift: '+name)
for f in ['packet.md','contract.md']:
 p=B/f; entries.append(dict(source=str(p.relative_to(R)),source_sha256=sha(p),lines=None,path=str(p.relative_to(R)),sha256=sha(p),bytes=p.stat().st_size))
now=datetime.datetime.now(datetime.timezone.utc)
m=dict(schema='JC2-BLIND-PACKET/v1',freeze_utc=now.isoformat(),basis='0d39df3c9fd69c939a8420c54d03228b9077777d',blind_target_utc=(now+datetime.timedelta(minutes=30)).isoformat(),cross_minutes=15,synthesis_minutes=15,entries=entries)
with (B/'MANIFEST.json').open('x') as f: json.dump(m,f,indent=2); f.write('\n')
paths=[e['path'] for e in entries]+[str((B/'MANIFEST.json').relative_to(R))]
for seat in ['coordinator','astra','fable5','sol56']:
 tag='ideation-20260908T2220Z-'+seat
 prompt='\n'.join('charged_input='+p for p in paths)+'\n\nRead the common frozen packet in {{LANE_INPUTS}} and follow its EQUAL contract in full.\nWrite exactly xmodel/'+tag+'.md.\nNo launch/compute authority. Root blind must be sealed before invitations; all peer reports remain unread during your blind work.\nAppend standalone <!-- BODY-END --> only at completion. Omit charge_basis.\n'
 with (B/(seat+'.prompt.md')).open('x') as f: f.write(prompt)
pins={str(p.relative_to(R)):sha(p) for p in sorted(B.rglob('*')) if p.is_file()}
with (B/'PINS.json').open('x') as f: json.dump(pins,f,indent=2); f.write('\n')
print(json.dumps(dict(freeze_utc=m['freeze_utc'],charged_inputs=len(paths),snapshot_bytes=sum(e['bytes'] for e in entries),manifest_sha256=sha(B/'MANIFEST.json'))))
