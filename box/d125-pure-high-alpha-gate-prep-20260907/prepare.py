#!/usr/bin/env python3
"""Read-only input verification and exclusive byte snapshots; NO mathematical replay."""
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path
import resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
rows=[
 ('xmodel/d125-pure-high-alpha-discriminator-astra-20260907.md','ha-producer.md','3eaf5610aede5885efa1c9aba95dc2016269952f5c0983675abfacc79b9c9bed'),
 ('xmodel/d125-pure-high-alpha-discriminator-astra-20260907.md.artifact.json','ha-producer.artifact.json','b4fd01c9c2e1e51f526649d77d66cafe172952dd87e1c0dc982818315034ff38'),
 ('box/d125-pure-high-alpha-discriminator-20260907/check.py','ha-checker.py','d4b9f1aa715d8bcb47475a1dd90f3115d7d111b0f9612a430cde713774d31c68'),
 ('box/d125-zero-k-deformation-discriminator-20260907/check.py','ha-factor-helper.py','25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66'),
 ('box/d125-pure-high-alpha-discriminator-20260907/witness.json','ha-witness.json','85b3e0ea5469e2867296af390bd3d4fd03bd7619e1ae22b0f88a08c7ee938c25'),
 ('box/d125-pure-high-alpha-discriminator-20260907/witness-O.json','ha-witness-optimized.json','85b3e0ea5469e2867296af390bd3d4fd03bd7619e1ae22b0f88a08c7ee938c25'),
 ('box/d125-pure-high-alpha-discriminator-20260907/replay.json','ha-replay.json','7a6bad86a0703b2f2e7a802b39314cd00131f522181300d8da2f3e13af2d5e9c'),
 ('box/d125-pure-high-alpha-discriminator-20260907/custody.json','ha-producer-custody.json','64ac1f6170cb652d0fed422adff76fb37f90b6f2c2df42f55963372cafcb9ea1'),
 ('xmodel/d125-parity-unit-normalization-astra-20260907.md','accepted14c-source.md','19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc'),
 ('xmodel/d125-zero-k-boundary-classification-astra-20260907.md','accepted14f-boundary.md','129947ee5a370991864a52936d1936179ec9c38efdf0fd80de989e8ed57237a2'),
 ('xmodel/d125-low-jet-saturation-discriminator-astra-20260907.md','accepted14g-low-rows.md','57d85da3010d6a2a432cdb79b543054b14d415cec249481275f0d8e6f2dbbe6a'),
 ('xmodel/d125-exceptional-pure-discriminator-astra-20260907.md','accepted14v-first-contact.md','9b3538b8d7d65477f5fb273ce8abb4b9556c8529dc374dc9affb4266f2793fb8')]
if len({r[1] for r in rows})!=len(rows): raise RuntimeError('duplicate basename')
snap=HERE/'inputs'; snap.mkdir()
entries=[]
for source,name,expected in rows:
    data=(ROOT/source).read_bytes(); digest=hashlib.sha256(data).hexdigest()
    if digest!=expected: raise RuntimeError('source drift: '+source)
    target=snap/name
    with target.open('xb') as stream: stream.write(data)
    target.chmod(0o444)
    copied=target.read_bytes()
    if copied!=data: raise RuntimeError('snapshot mismatch')
    entries.append({'source':source,'snapshot':str(target.relative_to(ROOT)),'basename':name,'bytes':len(data),'source_sha256':digest,'snapshot_sha256':hashlib.sha256(copied).hexdigest()})
packet={'status':'PREP_ONLY','charge_basis':'0d39df3c9fd69c939a8420c54d03228b9077777d','charged_count':len(entries),'unique_basenames':True,'entries':entries,'no_replay':True,'no_launch':True,'root_launch_authority':True,'omitted_nonpremises':['14y','15b','pending low-alpha critical-remainder theorem','all ongoing review bodies'],'reviewer_report':'xmodel/d125-pure-high-alpha-gate-fable5-20260907.md'}
with (HERE/'PINS.json').open('x') as stream: json.dump(packet,stream,sort_keys=True,indent=2); stream.write('\n')
(HERE/'PINS.json').chmod(0o444)
print(json.dumps({'status':'PREPARED','snapshots':len(entries),'PINS_sha256':hashlib.sha256((HERE/'PINS.json').read_bytes()).hexdigest()}))
