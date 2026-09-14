#!/usr/bin/env python3
"""Exclusive custody for this bounded report and explicitly pinned inputs."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
REPORT=ROOT/'xmodel/d125-zero-k-deformation-discriminator-astra-20260907.md'
PINS={
 'xmodel/d125-parity-unit-normalization-astra-20260907.md':'19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc',
 'xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md':'433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad',
 'xmodel/d125-minimal-receiver-client-preflight-astra-20260906.md':'e0debc7da22b8864ba43f0d29928e2104f2d8f161421ad26f29d8017f7b95e80',
 'box/char-degree-20260905/arzhantsev-petravchuk-closed-polynomials.pdf':'70429c3820eede008640a0d462d67ddb1f32c1f6e37f6b35f3589a0be2081e28',
 'box/char-degree-20260905/arzhantsev-petravchuk-closed-polynomials.txt':'ce2749ccfe09dc24442466fe6d163821532e437ff1a0cb7d04422b134c25286c'
}
def pin(path):
    raw=path.read_bytes()
    return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
inputs={}
for relative,expected in PINS.items():
    value=pin(ROOT/relative)
    if value['sha256']!=expected: raise RuntimeError('input drift: '+relative)
    inputs[relative]=value
owned={str(p.relative_to(ROOT)):pin(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='custody.json'}
data={'schema':'jc2.bounded-desk-custody/v1','status':'TERMINAL','utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
      'owner':'nonemptiness_certificate','all_writers_finished':True,'workers':[],'jobs':[],
      'no_full_A15_B25_pair_or_803_row_expansion':True,'no_AWS_SSH_CAS_solver_live_peer_or_shared_edits':True,
      'owned':owned,'inputs':inputs,'report':pin(REPORT),'transaction':pin(Path(str(REPORT)+'.artifact.json')),
      'no_live_edit_promise':'Owned files immutable from this publication; no continuing writer.'}
with (HERE/'custody.json').open('x') as f:
    json.dump(data,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'TERMINAL','owned_files':len(owned),'input_files':len(inputs),
                  'report_sha256':data['report']['sha256'],'custody_sha256':pin(HERE/'custody.json')['sha256']}))
