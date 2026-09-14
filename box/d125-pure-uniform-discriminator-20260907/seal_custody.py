#!/usr/bin/env python3
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
names={
 'xmodel/d125-exceptional-pure-discriminator-astra-20260907.md':'9b3538b8d7d65477f5fb273ce8abb4b9556c8529dc374dc9affb4266f2793fb8',
 'xmodel/d125-parity-unit-normalization-astra-20260907.md':'19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc',
 'xmodel/d125-zero-k-boundary-classification-astra-20260907.md':'129947ee5a370991864a52936d1936179ec9c38efdf0fd80de989e8ed57237a2',
 'xmodel/d125-low-jet-saturation-discriminator-astra-20260907.md':'57d85da3010d6a2a432cdb79b543054b14d415cec249481275f0d8e6f2dbbe6a',
 'box/d125-zero-k-deformation-discriminator-20260907/check.py':'25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66'}
def pin(p):
    b=p.read_bytes(); return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
inputs=[]
for name,want in names.items():
    row=pin(ROOT/name)
    if row['sha256']!=want: raise RuntimeError('input drift: '+name)
    inputs.append(row)
owned=[pin(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='custody.json']
report=ROOT/'xmodel/d125-pure-uniform-discriminator-astra-20260907.md'
owned.extend([pin(report),pin(Path(str(report)+'.artifact.json'))])
receipt={'status':'TERMINAL','owner':'/root/nonemptiness_certificate','custody_transfer':'ROOT read-only review',
         'inputs':inputs,'owned':owned,'all_writers_finished':True,'live_jobs':[],
         'uniform_exclusion':'NO-GAIN/GAP: no full source to regular scalar Pell residue map established',
         'claims':'PROVISIONAL actual source-compatible cubic collision and conditional affine-unit parity/Pell obstruction',
         'no_live_read':True,'no_new_cache_writes':True,'no_more_mutations':True,
         'primary_scope':'whole Stacks33.9.3 read online; primary-note is not a raw HTML hash claim'}
with (HERE/'custody.json').open('x') as f: json.dump(receipt,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'TERMINAL','input_pins':len(inputs),'owned_pins':len(owned),'custody':pin(HERE/'custody.json')}))
