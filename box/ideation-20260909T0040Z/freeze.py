"""One-shot exact snapshots and equal prompts; no launch or mathematical execution."""
import datetime, hashlib, json, pathlib, shutil
R=pathlib.Path('/home/ubuntu/jc2'); B=R/'box/ideation-20260909T0040Z'
S=B/'snapshots'; S.mkdir(exist_ok=False); M=B/'metadata'; M.mkdir(exist_ok=False)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def lines_after(path,prefix):
 data=(R/path).read_bytes().splitlines(keepends=True)
 starts=[i for i,line in enumerate(data) if line.decode().startswith(prefix)]
 if not starts: raise SystemExit('missing source marker '+prefix)
 return (starts[-1]+1,len(data))
live=(R/'notes.md').read_bytes().splitlines(keepends=True)
starts=[i for i,line in enumerate(live) if line.startswith(b'## ') and b'LIVE STATE' in line]
if not starts: raise SystemExit('missing LIVE')
specs=[('COORDINATION.md','coordination.md',None),('APPROACHES.md','approaches.md',None),('notes.md','latest-live.md',(starts[-1]+1,len(live))),('AUDIT.md','audit-guide.md',(1,40)),('AUDIT.md','audit-15m-through-15p.md',lines_after('AUDIT.md','### 17(mmmmmmmmmmmmmmm)')),('history/APPROACHES-before-20260906-cleanup.md','master46-history.md',(257,309)),('xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md','binding-row26-bd-gal.md',None),('xmodel/ideation-20260908T2220Z-synthesis.md','previous-2220-synthesis.md',None),('xmodel/websweep-20260908T2212Z-astra.md','latest-broad-sweep.md',None),('xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md','minimal-receiver.md',None),('xmodel/golden-two-regime-initial-discriminator-astra-20260908.md','accepted-golden-framework.md',None),('xmodel/golden-hdiv-m-composition-gate-fable5-20260908.md','accepted-m-gate.md',None),('xmodel/d125-weightfree-reference-source-astra-20260909.md','unreviewed-weightfree-framework.md',None),('xmodel/d125-weightfree-client-interface-astra-20260909.md','unreviewed-conditional-client-map.md',None)]
required={'binding-row26-bd-gal.md':'f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8','minimal-receiver.md':'7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413','accepted-golden-framework.md':'14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6','accepted-m-gate.md':'50045412e9b0d9cf3e640844e768e359bd7dd466e862316e9b4e9380d40c68cf','unreviewed-weightfree-framework.md':'cbc0330b001faeb8692e45c3be3fdcd3c0727b5734e648143642234da5d63696','unreviewed-conditional-client-map.md':'dcb3a30a48c5977005083a3ad7bbc5935e1f2f74ade6c3569a4b45751c213276','latest-broad-sweep.md':'364431f6267629e2f45e49785b18bf6393f4a9b4f2b59b4d3ee47047a70440dc'}
entries=[]
for src,dst,span in specs:
 p=R/src; data=p.read_bytes(); before=hashlib.sha256(data).hexdigest()
 if dst in required and before!=required[dst]: raise SystemExit('REFUSE source pin '+src)
 q=S/dst
 with q.open('xb') as f: f.write(data if span is None else b''.join(data.splitlines(keepends=True)[span[0]-1:span[1]]))
 if sha(p)!=before: raise SystemExit('source changed during copy '+src)
 entries.append(dict(source=src,source_sha256=before,lines=span,path=str(q.relative_to(R)),sha256=sha(q),bytes=q.stat().st_size))
provenance=[]
for src,dst in [('xmodel/d125-weightfree-reference-source-astra-20260909.md.artifact.json','wf-framework-transaction.json'),('box/d125-weightfree-reference-source-20260909/custody.json','wf-framework-custody.json'),('box/d125-weightfree-reference-source-20260909/input-pins.json','wf-framework-input-pins.json'),('xmodel/d125-weightfree-client-interface-astra-20260909.md.artifact.json','conditional-interface-transaction.json'),('box/d125-weightfree-client-interface-astra-20260909/custody.json','conditional-interface-custody.json'),('xmodel/golden-hdiv-m-composition-gate-fable5-20260908.run.v2','m-gate-run.v2'),('box/d125-0220-root-harvest-20260907/0019-m-gate-harvest.json','m-root-replay.json')]:
 p=R/src; q=M/dst; shutil.copyfile(p,q)
 if sha(p)!=sha(q): raise SystemExit('provenance drift '+src)
 provenance.append(dict(source=src,source_sha256=sha(p),path=str(q.relative_to(R)),sha256=sha(q),bytes=q.stat().st_size))
for f in ['packet.md','contract.md']:
 p=B/f; entries.append(dict(source=str(p.relative_to(R)),source_sha256=sha(p),lines=None,path=str(p.relative_to(R)),sha256=sha(p),bytes=p.stat().st_size))
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
m=dict(schema='JC2-BLIND-PACKET/v1',freeze_utc=now,basis='0d39df3c9fd69c939a8420c54d03228b9077777d',blind_target_utc=None,invitation_utc=None,deadline_policy='Explicit root invitation chooses common future UTC deadline AFTER root blind seal; never retroactive.',launch_authorized=False,cross_minutes=15,synthesis_minutes=15,entries=entries,provenance_only=provenance)
with (B/'MANIFEST.json').open('x') as f: json.dump(m,f,indent=2); f.write('\n')
paths=[e['path'] for e in entries]+[str((B/'MANIFEST.json').relative_to(R))]
for seat in ['coordinator','astra','fable5','sol56']:
 prompt='\n'.join('charged_input='+p for p in paths)+'\n\nRead every common frozen input in {{LANE_INPUTS}} and follow the EQUAL full46 contract.\nWrite exactly xmodel/ideation-20260909T0040Z-'+seat+'.md.\nNo peer invitation exists from this file alone: root must seal its same-input blind FIRST and later supply an explicit common future deadline at actual invitation. Do not reset any assigned target.\nNo launch/compute authority; no peer or live report reads. Append standalone <!-- BODY-END --> only at substantive completion. Omit charge_basis.\n'
 with (B/(seat+'.prompt.md')).open('x') as f: f.write(prompt)
pins={str(p.relative_to(R)):sha(p) for p in sorted(B.rglob('*')) if p.is_file()}
with (B/'PINS.json').open('x') as f: json.dump(pins,f,indent=2); f.write('\n')
print(json.dumps(dict(freeze_utc=now,charged_inputs=len(paths),charged_content_bytes=sum(e['bytes'] for e in entries),manifest_sha256=sha(B/'MANIFEST.json'),invitation_authorized=False)))
