#!/usr/bin/env python3
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
NAMES=[
 'xmodel/d125-parity-unit-normalization-astra-20260907.md',
 'xmodel/d125-zero-k-boundary-classification-astra-20260907.md',
 'xmodel/d125-low-jet-saturation-discriminator-astra-20260907.md',
 'xmodel/d125-ramified-twojet-discriminator-astra-20260907.md',
 'xmodel/d125-generic-ramification-discriminator-astra-20260907.md',
 'xmodel/d125-m4-order7-discriminator-astra-20260907.md',
 'box/d125-zero-k-deformation-discriminator-20260907/check.py',
 'box/char-degree-20260905/arzhantsev-petravchuk-closed-polynomials.pdf']
EXPECTED=[
 '19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc',
 '129947ee5a370991864a52936d1936179ec9c38efdf0fd80de989e8ed57237a2',
 '57d85da3010d6a2a432cdb79b543054b14d415cec249481275f0d8e6f2dbbe6a',
 '1440132691e51058b51927ba40234d0441d787a167321aba0af2bd53e8b698d4',
 'a7b37d6e5c1ce4f72bd3a4c2efa748f17d0ac11d141160b49da1754cc9e5e293',
 '6ee3ee52a9d353cde821528b498505c4930f17e1224cd1eefd6db78421f82df7',
 '25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66',
 '70429c3820eede008640a0d462d67ddb1f32c1f6e37f6b35f3589a0be2081e28']
def pin(p):
    data=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
inputs=[]
for name,want in zip(NAMES,EXPECTED):
    row=pin(ROOT/name)
    if row['sha256']!=want: raise RuntimeError('input drift: '+name)
    inputs.append(row)
owned=[pin(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='custody.json']
report=ROOT/'xmodel/d125-uniform-ramification-discriminator-astra-20260907.md'
owned.extend([pin(report),pin(Path(str(report)+'.artifact.json'))])
receipt={'status':'TERMINAL','owner':'/root/nonemptiness_certificate','custody_transfer':'ROOT read-only review',
         'inputs':inputs,'owned':owned,'all_writers_finished':True,'live_jobs':[],
         'new_claim':'PROVISIONAL uniform finite generic-center arc obstruction',
         'not_claimed':['guarded source emptiness','existence of degeneration','exceptional or infinity exclusion','JC2'],
         'no_live_read':True,'no_new_cache_writes':True,'no_more_mutations':True,
         'operational_note':'Initial custody-only run used .manifest.json rather than .artifact.json and failed before any custody write; corrected before this terminal export. Frozen report/check/witness unchanged.'}
with (HERE/'custody.json').open('x') as f: json.dump(receipt,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'TERMINAL','input_pins':len(inputs),'owned_pins':len(owned),'custody':pin(HERE/'custody.json')}))
