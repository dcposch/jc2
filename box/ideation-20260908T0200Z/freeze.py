import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json,datetime,subprocess,re,os
R=Path('/home/ubuntu/jc2'); B=Path(__file__).resolve().parent; S=B/'snapshots'
S.mkdir(exist_ok=False)
names=['APPROACHES.md','AUDIT.md','PROGRESS.md','COORDINATION.md','FALLACY-v2.md',
'ladder/REDUCTION.md','history/APPROACHES-before-20260906-cleanup.md',
'xmodel/ideation-20260907T2200Z-synthesis.md','xmodel/websweep-20260907T0735Z-astra.md',
'xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md',
'xmodel/d125-cone-first-contact-source-astra-20260908.md',
'xmodel/d125-cone-global-initial-consumer-astra-20260908.md',
'xmodel/d125-cone-source-composition-gate-fable5-20260908.md',
'box/d125-0220-root-harvest-20260907/0126-cone-source-harvest.json',
'box/d125-0220-root-harvest-20260907/0119-cone-consumer-harvest.json',
'box/d125-0220-root-harvest-20260907/0156-cone-gate-harvest.json',
'xmodel/d125-nonodd-cone-discriminator-astra-20260908.md',
'box/d125-0220-root-harvest-20260907/0159-nonodd-harvest.json',
'xmodel/d125-golden-divisibility-control-astra-20260908.md',
'box/d125-0220-root-harvest-20260907/0149-golden-harvest.json',
'xmodel/d125-common-to-unequal-interface-discriminator-astra-20260908.md',
'box/d125-0220-root-harvest-20260907/0200-common-interface-harvest.json']
if len({Path(n).name for n in names})!=len(names):raise RuntimeError('basename collision')
inputs=[]
def put(path,data):
    with path.open('xb') as f:f.write(data)
    os.chmod(path,0o444)
def pin(source,path,data,scope='whole'):
    inputs.append({'source':source,'snapshot':str(path.relative_to(R)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'scope':scope})
for n in names:
    data=(R/n).read_bytes(); dest=S/Path(n).name;put(dest,data);pin(n,dest,data)
notes=(R/'notes.md').read_bytes(); lines=notes.splitlines(keepends=True)
starts=[i for i,x in enumerate(lines) if x.startswith(b'## ') and b'LIVE STATE' in x]
last=starts[-1]; data=b''.join(lines[last:])
if not data.startswith(b'## 2026-09-08 02:02 UTC LIVE STATE'):raise RuntimeError('latest LIVE changed')
put(S/'LATEST-LIVE.md',data);pin('notes.md',S/'LATEST-LIVE.md',data,'exact latest block; whole-source-sha256='+hashlib.sha256(notes).hexdigest())
audit=(S/'AUDIT.md').read_bytes(); lines=audit.splitlines(keepends=True)
starts=[i for i,x in enumerate(lines) if x.startswith(b'### ') and b'2026-09-08 01:59 UTC' in x]
if len(starts)!=1:raise RuntimeError('15h section')
i=starts[0];end=next((j for j in range(i+1,len(lines)) if lines[j].startswith(b'### ')),len(lines))
data=b''.join(lines[i:end]);put(S/'AUDIT-15h.md',data);pin('AUDIT.md',S/'AUDIT-15h.md',data,'exact section lines '+str(i+1)+'..'+str(end))
historical=(S/'APPROACHES-before-20260906-cleanup.md').read_text()
ids=sorted(set(map(int,re.findall(r'^\|\s*(\d+)\s*\|',historical,re.M))))
if ids!=list(range(1,47)):raise RuntimeError(('historical ID coverage',ids))
packet=(B/'packet.md').read_bytes();os.chmod(B/'packet.md',0o444);pin('owned packet',B/'packet.md',packet)
manifest={'frozen_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'frozen_basis':'0d39df3c9fd69c939a8420c54d03228b9077777d','round':'20260908T0200Z','root_blind_prerequisite':'NOT INSPECTED; root must seal first; NO invitation authorized by prep','historical_ids':ids,'inputs':inputs}
put(B/'MANIFEST.json',(json.dumps(manifest,indent=2,sort_keys=True)+'\n').encode())
charged=[str((B/'packet.md').relative_to(R)),str((B/'MANIFEST.json').relative_to(R))]+[x['snapshot'] for x in inputs if x['source']!='owned packet']
common='''# Blind full-spectrum critical scan — 20260908T0200Z

PRE-LAUNCH REQUIREMENT: root must separately confirm its own coordinator report is sealed and pinned BEFORE issuing this invitation. This preparation does not claim that condition has happened. Root alone launches.

Read {{LANE_INPUTS}} and the WHOLE packet.md; the packet is the binding identical contract/tool boundary for coordinator, Astra, Fable and Sol. Read all46 historical IDs, current whole APP, latest LIVE, current PROGRESS/REDUCTION, exact15h, prior2200 synthesis and broad sweep. Full AUDIT is named-history lookup. Read the focused reports at their exact ACCEPTED/PROVISIONAL/root-checked tiers. No live nonodd review or peer/root blind bytes. No theorem promotion in this round.

Report target: xmodel/ideation-20260908T0200Z-LANE.md. Blind target02:45UTC September8, <=35minutes from actual invitation, <=2800words excluding compact46-row vector. Cross03:05, synthesis03:25 targets. Produce every contract item; at most3 cards TOTAL. No extra agents, remote operations, fullsource/high powers/CAS. Same targeted-primary permission and tiny local caps as packet. No new external evidence is assumed; no broad clock reset.

External completion: final unique standalone <!-- BODY-END --> only when finished, nothing after; NO authored seal. Local/root publication uses artifact transaction. Omit charge_basis; make no new exit-price claim. Source pins are current frozen state, not a commit-priced theorem.

'''
decl='\n'.join('charged_input='+p for p in charged)+'\n'
for lane in ('coordinator','astra','fable5','sol56'):
    p=B/(lane+'.prompt.md');put(p,(common.replace('LANE.md',lane+'.md')+decl).encode())
    # EXACT extraction command used by ops/lane.sh, not an indexed-key surrogate.
    parsed=subprocess.run(['sed','-n','s/^charged_input=//p',str(p)],check=True,stdout=subprocess.PIPE).stdout.decode().splitlines()
    if parsed!=charged:raise RuntimeError('literal lane parser mismatch')
if len({Path(x).name for x in charged})!=len(charged):raise RuntimeError('charged basename collision')
for x in inputs:
    if hashlib.sha256((R/x['snapshot']).read_bytes()).hexdigest()!=x['sha256']:raise RuntimeError('pin changed')
preflight={'status':'PASS','charged_per_lane':len(charged),'identical_charged_vectors':True,'historical_ids':ids,'parser':"sed -n 's/^charged_input=//p' (ops/lane.sh line258)",'root_blind_read':False,'invitations_launched':False,'manifest_sha256':hashlib.sha256((B/'MANIFEST.json').read_bytes()).hexdigest(),'packet_sha256':hashlib.sha256(packet).hexdigest()}
put(B/'preflight.json',(json.dumps(preflight,indent=2,sort_keys=True)+'\n').encode());print(json.dumps(preflight))
