#!/usr/bin/env python3
"""Exclusive small metadata export; exact mathematical numbers never pass through JS."""
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
 'xmodel/d125-pure-low-alpha-discriminator-astra-20260907.md':'e5416761dc0447a8fef0c83d228d731fdbc524cb6a12d04c34b2e78f4608d657',
 'xmodel/ideation-20260907T2200Z-cross-astra.md':'0fdc5f6cdd700869b445d89070d6ccc6e43bd383af793e97f1dfaa93467cfc32',
 'box/d125-zero-k-deformation-discriminator-20260907/check.py':'25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66'}
owned=['xmodel/d125-pure-critical-remainder-astra-20260907.md','xmodel/d125-pure-critical-remainder-astra-20260907.md.artifact.json']+[str(p.relative_to(ROOT)) for p in sorted(HERE.iterdir()) if p.is_file()]
entries=[]
for path in list(inputs)+owned:
    data=(ROOT/path).read_bytes(); digest=hashlib.sha256(data).hexdigest()
    if path in inputs and digest!=inputs[path]: raise RuntimeError('input drift: '+path)
    entries.append({'path':path,'sha256':digest,'bytes':len(data),'role':'input' if path in inputs else 'owned'})
packet={'owner':'/root/nonemptiness_certificate','task':'d125-pure-critical-remainder-20260907','status':'TERMINAL_PROVISIONAL_THEOREM','writers':'ALL_IDLE','publication':'begin-close-finalize-verify completed','mathematical_scope':'finite a<j excluded for genuine pure-center arcs in accepted14v setup; no claim for a>=j or degeneration existence','controls':'14 final normal/-O capped runs; earlier pre-cosmetic run retained, not final evidence','remote_activity':'NONE','live_peer_access':'NONE','no_live_edit_promise':True,'entries':entries}
with (HERE/'custody.json').open('x') as stream: json.dump(packet,stream,sort_keys=True,indent=2); stream.write('\n')
for e in entries:
    if hashlib.sha256((ROOT/e['path']).read_bytes()).hexdigest()!=e['sha256']: raise RuntimeError('post-export drift')
print(json.dumps({'status':'VERIFIED','entries':len(entries),'custody_sha256':hashlib.sha256((HERE/'custody.json').read_bytes()).hexdigest(),'check_sha256':hashlib.sha256((HERE/'check.py').read_bytes()).hexdigest(),'final_replay_sha256':hashlib.sha256((HERE/'final-replay.json').read_bytes()).hexdigest()}))
