"""Exclusive byte-copy and prompt rendering for a collected blind round."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, os
R=Path('/home/ubuntu/jc2'); P=R/'box/ideation-20260907T2200Z'; B=P/'cross-review-prep'
C=P/'collection-20260907T222755Z-astra.json'
def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def pin(p):
    d=p.read_bytes(); return {'bytes':len(d),'sha256':hashlib.sha256(d).hexdigest()}
def emit(name,data):
    with (B/name).open('xb') as f:f.write(data)
    os.chmod(B/name,0o444)
def js(x):return (json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
need(pin(C)['sha256']=='1695f100ecb0c7b05e367eb0afadf92838c9f2b8beae911ec0d697b9f572ace2','collection drift')
collection=json.loads(C.read_bytes())
original={}
for lane,data in collection['lanes'].items():
    for p in data['current_pins']:
        path=R/p['path']; need(pin(path)['sha256']==p['sha256'],'collected pin drift')
        original[str(path)]=p['sha256']
sources={
 'blind-astra.md':R/'xmodel/ideation-20260907T2200Z-astra.md',
 'blind-fable5.md':R/'xmodel/ideation-20260907T2200Z-fable5.md',
 'blind-sol56.md':R/'xmodel/ideation-20260907T2200Z-sol56.md',
 'blind-coordinator.md':R/'xmodel/ideation-20260907T2200Z-coordinator.md',
 'original-packet.md':P/'packet.md',
 'frozen-approaches.md':P/'snapshots/APPROACHES.md',
 'frozen-coordination.md':P/'snapshots/COORDINATION.md',
 'frozen-reduction.md':P/'snapshots/REDUCTION.md',
 'frozen-fallacy-v2.md':P/'snapshots/FALLACY-v2.md',
 'frozen-pure-discriminator.md':P/'snapshots/d125-pure-uniform-discriminator-astra-20260907.md',
 'frozen-pure-gate.md':P/'snapshots/d125-pure-uniform-gate-fable5-20260907.md',
 'frozen-exceptional-gate.md':P/'snapshots/d125-exceptional-pure-gate-fable5-20260907.md',
 'frozen-arc-interface.md':P/'snapshots/d125-arc-closure-interface-astra-20260907.md',
 'collection-before-body.json':C,
}
need(pin(sources['blind-coordinator.md'])['sha256']==
     'c35e775e8295f5e5f6a0e5fa630820f81da95545c0940320136c0afd39827033','root drift')
inputs={}
for name,path in sources.items():
    if name not in ('blind-coordinator.md','collection-before-body.json'):
        need(str(path) in original,'source not collected')
    data=path.read_bytes(); emit(name,data)
    need(pin(B/name)==pin(path),'copy mismatch')
    inputs[name]=dict(pin(path),original_path=str(path.relative_to(R)))
for name in ('deduplicated-packet.md','post-snapshot-root-facts.md'):
    inputs[name]=pin(B/name)
emit('cross-input-pins.json',js({'schema':'jc2.cross-inputs/v1','files':inputs}))
names=list(inputs)+['cross-input-pins.json']
need(len(names)==len(set(names)),'duplicate basename')
charges='\n'.join('charged_input='+str((B/n).relative_to(R)) for n in names)
template=(B/'cross.prompt.template.md').read_text()
need('{{LANE_INPUTS}}' in template,'template missing')
prompts={}
for lane in ('astra','fable5','sol56'):
    prompt=template.replace('@@LANE@@',lane).replace('@@CHARGED_INPUT_LINES@@',charges)
    need('@@' not in prompt,'render failure')
    target='xmodel/ideation-20260907T2200Z-cross-'+lane+'.md'
    need(prompt.count(target)==1,'destination ambiguity')
    name='cross-'+lane+'.prompt.md';emit(name,prompt.encode());prompts[lane]=pin(B/name)
owned=names+list('cross-'+x+'.prompt.md' for x in prompts)+['cross.prompt.template.md','freeze-cross.py']
emit('cross-custody.json',js({'schema':'jc2.cross-prep-custody/v1',
 'utc':datetime.now(timezone.utc).isoformat(),
 'collection_before_body':pin(C),'files':{n:pin(B/n) for n in owned},
 'launches':0,'remaining_children':0,'status':'PREP_ONLY_FROZEN'}))
print(json.dumps({'status':'FROZEN_NO_LAUNCH','charged_count':len(names),
 'prompts':prompts,'custody':pin(B/'cross-custody.json'),
 'input_pins':pin(B/'cross-input-pins.json')},sort_keys=True))
