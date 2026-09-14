#!/usr/bin/python3
"""Exclusive immutable snapshots and prompt assembly; no proof replay or launch."""
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path
import resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
rows=[
 ('xmodel/d125-cone-global-initial-consumer-astra-20260908.md','consumer-report.md','139bbda05a16913adfc3c1748217a8cc421f6c4d48075e612fa9d63afcfa3249'),
 ('xmodel/d125-cone-global-initial-consumer-astra-20260908.md.artifact.json','consumer-transaction.json','8eab17a3860c3e4ea3d6a546184552f7da9b70075db306e60a8c5fe9c53e04c7'),
 ('box/d125-cone-global-initial-consumer-20260908/check.py','consumer-check.py','45305b1f27ada877995bfc4a33eee80a4560b8834786a98f7bb29c3e427913dd'),
 ('box/d125-cone-global-initial-consumer-20260908/witness.json','consumer-witness.json','fa1fe3df479a3edd95ac7c2035e231bf0d9485f1e40c0a2b40c1bcfe62047166'),
 ('box/d125-cone-global-initial-consumer-20260908/replay.json','consumer-replay.json','a612050652308f06f996fe5dc835d794d2fb08c7878a245e7daea764b80cf5be'),
 ('box/d125-cone-global-initial-consumer-20260908/custody.json','consumer-custody.json','741635912eb28fb15dc854986e490fe853304db30870b0c9d25eb560018cdcd1'),
 ('box/d125-0220-root-harvest-20260907/0119-cone-consumer-harvest.json','root-consumer-receipt.json','1abd22b275f9c5e65895380840dd69f7af276da5bc1535ca4963a9f268e86e8f'),
 ('xmodel/d125-parity-unit-normalization-astra-20260907.md','accepted14c-source.md','19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc'),
 ('xmodel/d125-symmetry-discriminator-astra-20260907.md','accepted-symmetry-support.md','9bed554644b1bd3c881ba4e289ea0950601ed6141677a45152577442fd477b12'),
 ('xmodel/d125-pure-high-alpha-discriminator-astra-20260907.md','accepted15f-interface.md','3eaf5610aede5885efa1c9aba95dc2016269952f5c0983675abfacc79b9c9bed'),
 ('xmodel/d125-reducible-cone-initial-discriminator-astra-20260908.md','cone-counter-report.md','6b92e38c1d337889c8c9ee4c749aa29d9d972365434e9f1096956771dc6aeccb'),
 ('box/d125-reducible-cone-initial-discriminator-20260908/check.py','cone-counter-check.py','00832fc16c6bc73ba8cf4fe5dafa21bc282690604ec587db89027fce1b1471f8'),
 ('box/d125-reducible-cone-initial-discriminator-20260908/witness.json','cone-counter-witness.json','120d8d7f28dcc144c92f373f93fb9fec4f5ebaf06762aff4d226e76ae6bdc488'),
]
release_path=HERE/'SOURCE-RELEASE.json'
release=None
if release_path.exists():
    release=json.loads(release_path.read_bytes())
    if release.get('root_explicit_release') is not True or release.get('status')!='TERMINAL_RELEASED':
        raise ValueError('source is not explicitly terminal/released')
    rows.extend(tuple(x) for x in release['rows'])
if len({r[1] for r in rows})!=len(rows): raise ValueError('duplicate basename')
snap=HERE/'inputs'
snap.mkdir()
entries=[]
for source,name,expected in rows:
    data=(ROOT/source).read_bytes()
    digest=hashlib.sha256(data).hexdigest()
    if digest!=expected: raise ValueError('source drift: '+source)
    target=snap/name
    with target.open('xb') as f: f.write(data)
    target.chmod(0o444)
    if target.read_bytes()!=data: raise ValueError('snapshot mismatch')
    entries.append({'source':source,'snapshot':str(target.relative_to(ROOT)),'basename':name,
                    'bytes':len(data),'source_sha256':digest,'snapshot_sha256':digest})
source_status=('TERMINAL SOURCE RELEASED: the source snapshots listed in PINS are now charged.\n'
               'They are frozen producer claims requiring this independent gate, not promoted conclusions.'
               if release else
               'SOURCE NOT RELEASED: no source-first-contact report/code/evidence is charged.\n'
               'The direct source composition remains an EMPTY GAP. Targets2/3 and the\n'
               'source-dependent part of6 must remain GAP; review the conditional consumer\n'
               'separately. Do not discover or read a live source report to fill this gap.')
poststate=('Frozen post-state for this gate only.\n\n'
           'Root states accepted14c, symmetry support and15f have the scoped acceptance\n'
           'used here. Historical headers remain byte-identical; optional claims are not\n'
           'promoted by copying them. Root consumer receipt records whole-proof/code and\n'
           'ten normal/-O checks; this is not the independent Fable judgment.\n\n'+source_status+'\n\n'
           +(release['root_poststate']+'\n\n' if release else '')+
           'Root alone launches and promotes. No moving-lift premise is charged.\n')
post=snap/'frozen-scope-poststate.md'
data=poststate.encode()
with post.open('xb') as f: f.write(data)
post.chmod(0o444)
digest=hashlib.sha256(data).hexdigest()
entries.append({'source':'root task/release messages, explicitly frozen here','snapshot':str(post.relative_to(ROOT)),
                'basename':post.name,'bytes':len(data),'source_sha256':None,'snapshot_sha256':digest})
packet={'status':'PREP_ONLY','frozen_basis':'0d39df3c9fd69c939a8420c54d03228b9077777d',
        'lane_inputs_token':'{{LANE_INPUTS}}','entries':entries,'charged_snapshot_count':len(entries),
        'source_status':'TERMINAL_RELEASED' if release else 'NOT_RELEASED_GAP',
        'unique_basenames':True,'root_launch_authority':True,'no_launch':True,'no_math_replay':True,
        'review_minutes':25,'reviewer_report':'xmodel/d125-cone-source-composition-gate-fable5-20260908.md'}
pins=HERE/'PINS.json'
with pins.open('x') as f: json.dump(packet,f,sort_keys=True,indent=2); f.write('\n')
pins.chmod(0o444)
charged='charged_input='+str(pins.relative_to(ROOT))+'\n'+'\n'.join('charged_input='+e['snapshot'] for e in entries)
prompt=(HERE/'prompt-template.txt').read_text().replace('@CHARGED_INPUTS@',charged).replace('@SOURCE_STATUS@',source_status)
if '{{LANE_INPUTS}}' not in prompt or '@SOURCE_' in prompt or '@CHARGED_' in prompt:
    raise ValueError('unresolved template')
if any(line.startswith('charge_basis=') for line in prompt.splitlines()): raise ValueError('invalid exit-price declaration')
out=HERE/'prompt.txt'
with out.open('x') as f: f.write(prompt)
out.chmod(0o444)
print(json.dumps({'status':'PREPARED','snapshots':len(entries),'source_status':packet['source_status'],
                  'PINS_sha256':hashlib.sha256(pins.read_bytes()).hexdigest(),
                  'prompt_sha256':hashlib.sha256(out.read_bytes()).hexdigest()},sort_keys=True))
