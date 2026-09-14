#!/usr/bin/env python3
"""Exclusive current-pin custody export for a conditional desk composition."""
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path
import resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
inputs={
 'xmodel/d125-parity-unit-normalization-astra-20260907.md':'19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc',
 'xmodel/d125-zero-k-boundary-classification-astra-20260907.md':'129947ee5a370991864a52936d1936179ec9c38efdf0fd80de989e8ed57237a2',
 'xmodel/d125-low-jet-saturation-discriminator-astra-20260907.md':'57d85da3010d6a2a432cdb79b543054b14d415cec249481275f0d8e6f2dbbe6a',
 'xmodel/d125-exceptional-pure-discriminator-astra-20260907.md':'9b3538b8d7d65477f5fb273ce8abb4b9556c8529dc374dc9affb4266f2793fb8',
 'xmodel/d125-uniform-ramification-discriminator-astra-20260907.md':'94fa51948a1d97894b754c141b8d15593be2abf9473a941c7c568ddb272e6c3b',
 'xmodel/d125-exceptional-center-discriminator-astra-20260907.md':'3c9aee528612bd75fb2f77200565a874b9f16baf1a142302df4392c5e94c46d7',
 'xmodel/d125-exceptional-tuned-discriminator-astra-20260907.md':'d0937ebe91b14e61cec7d47b671f9bdebc18c321ff035bb20449e75a1214e03f',
 'xmodel/d125-arc-closure-interface-astra-20260907.md':'6f9e63a8162af7c6d212363b62c368f9029b282fa8acbb65bcdc5d9cf81b72d3',
 'xmodel/d125-arc-closure-gate-fable5-20260907.md':'d266fb9c68421fb4717373d89435d69cbe4e36cd65a24611801bc8353f018c92',
 'xmodel/d125-pure-critical-remainder-astra-20260907.md':'7d7993d2bca7cd84bd2c7c7f40b7567c1f5be9b69c119c18c98f6d2b97ca7c74',
 'xmodel/d125-pure-critical-remainder-gate-fable5-20260907.md':'6f6fef2133d33482b0f45f2db86d78712976a3f984c848d68e4c388615227be8',
 'xmodel/d125-pure-high-alpha-discriminator-astra-20260907.md':'3eaf5610aede5885efa1c9aba95dc2016269952f5c0983675abfacc79b9c9bed',
 'box/d125-arc-closure-interface-20260907/stacks-0CM1.html':'b819193679a3772dd4e9024d1955957d5fb837ad77c7a0046b2255814f28c1bc',
 'box/d125-arc-closure-interface-20260907/stacks-0C0S.html':'d9968d0ab1375d148b4d9ce9798ee7464852085dcc1ffe56ea4ed51b60adc1eb'}
owned=[ROOT/'xmodel/d125-finite-boundary-composition-astra-20260908.md',ROOT/'xmodel/d125-finite-boundary-composition-astra-20260908.md.artifact.json']+[p for p in sorted(HERE.iterdir()) if p.is_file()]
entries=[]
for path,expected in inputs.items():
    data=(ROOT/path).read_bytes(); digest=hashlib.sha256(data).hexdigest()
    if digest!=expected: raise RuntimeError('input drift: '+path)
    role='PROVISIONAL_CONDITIONAL_PREMISE' if 'pure-high-alpha-discriminator' in path else 'accepted_input_or_primary'
    entries.append({'path':path,'sha256':digest,'bytes':len(data),'role':role})
for path in owned:
    data=path.read_bytes(); entries.append({'path':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'role':'owned'})
packet={'owner':'/root/nonemptiness_certificate','task':'d125-finite-boundary-composition-20260908','status':'TERMINAL_CONDITIONAL_COMPOSITION_NOT_PROMOTED','writers':'ALL_IDLE','publication':'begin-close-finalize-verify completed','conditional_premise':'frozen high-alpha producer only; its live gate NOT read','strongest_scope':'J+(k)=S and exact saturated/open ring isomorphism, optional finite vertical CRT split; NOT J=S','read_scope':'whole named reports; whole USED Stacks32.15.1 and10.160.10 statements/proofs in retained HTML, not every unrelated section/comment','controls':'12 normal/-O tiny ring/parameter controls; no source proof replay','remote_activity':'NONE','live_peer_access':'NONE','no_live_edit_promise':True,'entries':entries}
with (HERE/'custody.json').open('x') as stream: json.dump(packet,stream,sort_keys=True,indent=2); stream.write('\n')
for row in entries:
    if hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()!=row['sha256']: raise RuntimeError('post-export drift')
print(json.dumps({'status':'VERIFIED','entries':len(entries),'custody_sha256':hashlib.sha256((HERE/'custody.json').read_bytes()).hexdigest(),'check_sha256':hashlib.sha256((HERE/'check.py').read_bytes()).hexdigest(),'replay_sha256':hashlib.sha256((HERE/'replay.json').read_bytes()).hexdigest()}))
