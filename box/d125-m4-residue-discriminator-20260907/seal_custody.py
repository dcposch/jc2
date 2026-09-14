#!/usr/bin/env python3
import sys
sys.dont_write_bytecode=True
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
REPORT=ROOT/'xmodel/d125-m4-residue-discriminator-astra-20260907.md'
PINS={
 'xmodel/d125-parity-unit-normalization-astra-20260907.md':'19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc',
 'xmodel/d125-low-jet-saturation-discriminator-astra-20260907.md':'57d85da3010d6a2a432cdb79b543054b14d415cec249481275f0d8e6f2dbbe6a',
 'xmodel/d125-zero-k-boundary-classification-astra-20260907.md':'129947ee5a370991864a52936d1936179ec9c38efdf0fd80de989e8ed57237a2',
 'xmodel/d125-ramified-twojet-discriminator-astra-20260907.md':'1440132691e51058b51927ba40234d0441d787a167321aba0af2bd53e8b698d4',
 'xmodel/d125-generic-ramification-discriminator-astra-20260907.md':'a7b37d6e5c1ce4f72bd3a4c2efa748f17d0ac11d141160b49da1754cc9e5e293',
 'box/d125-zero-k-deformation-discriminator-20260907/check.py':'25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66'
}
def pin(p):
    raw=p.read_bytes(); return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
inputs={}
for name,expected in PINS.items():
    z=pin(ROOT/name)
    if z['sha256']!=expected: raise RuntimeError('input drift: '+name)
    inputs[name]=z
owned={str(p.relative_to(ROOT)):pin(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='custody.json'}
data={'schema':'jc2.bounded-desk-custody/v1','status':'TERMINAL','owner':'nonemptiness_certificate',
      'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'all_writers_finished':True,
      'workers':[],'jobs':[],'inputs':inputs,'owned':owned,'report':pin(REPORT),
      'transaction':pin(Path(str(REPORT)+'.artifact.json')),'no_live_gate_or_peer_read':True,
      'no_AWS_SSH_CAS_full_A15_B25_expansion_solver_shared_edits':True,'bytecode_disabled':True,
      'charged_jet_control':'jet-final-replay.json; initial jet-replay.json retained as superseded control strength',
      'no_live_edit_promise':'All owned files immutable at publication; no continuing writer.'}
with (HERE/'custody.json').open('x') as f: json.dump(data,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'TERMINAL','input_files':len(inputs),'owned_files':len(owned),
                  'report_sha256':data['report']['sha256'],'custody_sha256':pin(HERE/'custody.json')['sha256']}))
