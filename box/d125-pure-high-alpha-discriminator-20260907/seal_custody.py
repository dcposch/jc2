#!/usr/bin/env python3
"""Exclusive compact custody export; no mathematical-number JSON roundtrip."""
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path
import resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
inputs={
 'xmodel/d125-parity-unit-normalization-astra-20260907.md':'19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc',
 'xmodel/d125-zero-k-boundary-classification-astra-20260907.md':'129947ee5a370991864a52936d1936179ec9c38efdf0fd80de989e8ed57237a2',
 'xmodel/d125-low-jet-saturation-discriminator-astra-20260907.md':'57d85da3010d6a2a432cdb79b543054b14d415cec249481275f0d8e6f2dbbe6a',
 'xmodel/d125-exceptional-pure-discriminator-astra-20260907.md':'9b3538b8d7d65477f5fb273ce8abb4b9556c8529dc374dc9affb4266f2793fb8',
 'xmodel/d125-pure-uniform-discriminator-astra-20260907.md':'1f71ea56f697fe48169cdd95cfe7e2417a98d37efa2f425a86661dfe5ff8e04d',
 'xmodel/d125-pure-low-alpha-discriminator-astra-20260907.md':'e5416761dc0447a8fef0c83d228d731fdbc524cb6a12d04c34b2e78f4608d657',
 'box/d125-zero-k-deformation-discriminator-20260907/check.py':'25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66'}
owned=['xmodel/d125-pure-high-alpha-discriminator-astra-20260907.md','xmodel/d125-pure-high-alpha-discriminator-astra-20260907.md.artifact.json']+[str(p.relative_to(ROOT)) for p in sorted(HERE.iterdir()) if p.is_file()]
entries=[]
for path in list(inputs)+owned:
    data=(ROOT/path).read_bytes(); digest=hashlib.sha256(data).hexdigest()
    if path in inputs and digest!=inputs[path]: raise RuntimeError('input drift: '+path)
    role='owned'
    if path in inputs: role='history' if 'pure-uniform-discriminator' in path or 'pure-low-alpha-discriminator' in path else 'accepted_input_or_helper'
    entries.append({'path':path,'sha256':digest,'bytes':len(data),'role':role})
packet={'owner':'/root/nonemptiness_certificate','task':'d125-pure-high-alpha-discriminator-20260907','status':'TERMINAL_PROVISIONAL_THEOREM','writers':'ALL_IDLE','publication':'begin-close-finalize-verify completed','independent_parents':'accepted14c/f/g/v; pending low-alpha critical-remainder theorem NOT a premise or charged input','mathematical_scope':'no genuine pure-center finite source arc with ord(alpha)>=j, including alpha=0; no degeneration existence or source emptiness conclusion','controls':'12 normal/-O runs,30wall25CPU512MiB each','remote_activity':'NONE','live_peer_access':'NONE','no_live_edit_promise':True,'entries':entries}
with (HERE/'custody.json').open('x') as stream: json.dump(packet,stream,sort_keys=True,indent=2); stream.write('\n')
for e in entries:
    if hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest()!=e['sha256']: raise RuntimeError('post-export drift')
print(json.dumps({'status':'VERIFIED','entries':len(entries),'custody_sha256':hashlib.sha256((HERE/'custody.json').read_bytes()).hexdigest(),'check_sha256':hashlib.sha256((HERE/'check.py').read_bytes()).hexdigest(),'replay_sha256':hashlib.sha256((HERE/'replay.json').read_bytes()).hexdigest()}))
