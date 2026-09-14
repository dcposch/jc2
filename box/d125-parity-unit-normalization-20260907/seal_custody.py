#!/usr/bin/env python3
"""Exclusive terminal custody; explicitly named accepted inputs only."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
REPORT=ROOT/'xmodel/d125-parity-unit-normalization-astra-20260907.md'
PINS={
 'xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md':'433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad',
 'xmodel/d125-small-polynomial-lift-gate-fable5-20260906.md':'4295593a57a65e4d31630aecdef0b54e9d6078935e07cfb5e64acfd83fae4122',
 'xmodel/d125-zero-lambda-obstruction-astra-20260907.md':'a878a87bdeae772cc66d19ea817d43184882c649769c61d5babb47292d339d3a',
 'xmodel/d125-zero-lambda-gate-fable5-20260907.md':'33cb032a5d7f52cb12bd9122032ff5336499c3e67b9e650aa2c3c211935dd607',
 'xmodel/d125-minimal-receiver-client-preflight-astra-20260906.md':'e0debc7da22b8864ba43f0d29928e2104f2d8f161421ad26f29d8017f7b95e80',
 'box/d125-minimal-receiver-client-preflight-20260906/client.py':'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53'
}
def pin(path):
    data=path.read_bytes()
    return {'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
inputs={}
for name,expected in PINS.items():
    item=pin(ROOT/name)
    if item['sha256']!=expected: raise RuntimeError('input drift: '+name)
    inputs[name]=item
owned={str(p.relative_to(ROOT)):pin(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='custody.json'}
data={'schema':'jc2.bounded-desk-custody/v1','status':'TERMINAL','utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
      'owner':'nonemptiness_certificate','all_writers_finished':True,'jobs':[],'workers':[],
      'no_pending_22_coordinate_theorem_dependency':True,'no_live_peer_reads':True,
      'whole_proofs_read':list(PINS)[:5],'source_code_read':list(PINS)[5:],
      'owned':owned,'inputs':inputs,'report':pin(REPORT),'transaction':pin(Path(str(REPORT)+'.artifact.json')),
      'no_live_edit_promise':'All owned files immutable on this publication; no continuing writer.'}
with (HERE/'custody.json').open('x') as f:
    json.dump(data,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'TERMINAL','owned_files':len(owned),'input_files':len(inputs),'report_sha256':data['report']['sha256'],
                  'custody_sha256':pin(HERE/'custody.json')['sha256']}))
