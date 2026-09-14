#!/usr/bin/env python3
"""Exclusive small terminal receipt; named inputs only, no numeric reserialization."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
REPORT=ROOT/'xmodel/d125-ramified-twojet-discriminator-astra-20260907.md'
PINS={
 'xmodel/d125-parity-unit-normalization-astra-20260907.md':'19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc',
 'xmodel/d125-zero-k-deformation-discriminator-astra-20260907.md':'99d251478969b569c5523349b71a58534fc1fc95c7125e2fcc7e706dda963f2c',
 'xmodel/d125-zero-k-boundary-classification-astra-20260907.md':'129947ee5a370991864a52936d1936179ec9c38efdf0fd80de989e8ed57237a2',
 'xmodel/d125-low-jet-saturation-discriminator-astra-20260907.md':'57d85da3010d6a2a432cdb79b543054b14d415cec249481275f0d8e6f2dbbe6a',
 'box/d125-zero-k-deformation-discriminator-20260907/check.py':'25be0862730df8b66076eb59a2d1d0909fbcf563ea73ce16924affdc7c70ad66',
 'box/char-degree-20260905/arzhantsev-petravchuk-closed-polynomials.pdf':'70429c3820eede008640a0d462d67ddb1f32c1f6e37f6b35f3589a0be2081e28'
}
def pin(p):
    raw=p.read_bytes(); return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
inputs={}
for name,expected in PINS.items():
    item=pin(ROOT/name)
    if item['sha256']!=expected: raise RuntimeError('input drift: '+name)
    inputs[name]=item
owned={str(p.relative_to(ROOT)):pin(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='custody.json'}
data={'schema':'jc2.bounded-desk-custody/v1','status':'TERMINAL','owner':'nonemptiness_certificate',
      'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'all_writers_finished':True,
      'workers':[],'jobs':[],'inputs':inputs,'owned':owned,'report':pin(REPORT),
      'transaction':pin(Path(str(REPORT)+'.artifact.json')),
      'low_row_composition_provisional_at_cutoff':True,'no_live_peer_or_gate_read':True,
      'no_AWS_SSH_CAS_full_pair_full_source_solver_shared_edits':True,
      'no_live_edit_promise':'All owned files immutable at terminal publication; no ongoing writer.'}
with (HERE/'custody.json').open('x') as f:
    json.dump(data,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'TERMINAL','input_files':len(inputs),'owned_files':len(owned),
                  'report_sha256':data['report']['sha256'],'custody_sha256':pin(HERE/'custody.json')['sha256']}))
