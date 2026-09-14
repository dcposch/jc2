#!/usr/bin/env python3
"""Terminal custody; no discovery outside this box and named input files."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
REPORT=ROOT/'xmodel/d125-low-jet-saturation-discriminator-astra-20260907.md'
PINS={
 'xmodel/d125-parity-unit-normalization-astra-20260907.md':'19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc',
 'xmodel/d125-minimal-receiver-client-preflight-astra-20260906.md':'e0debc7da22b8864ba43f0d29928e2104f2d8f161421ad26f29d8017f7b95e80',
 'xmodel/d125-lift-hermite-gate-fable5-20260906.md':'7e2594d53150bf4346f4e4cc6e7f6ff05a021b045b640128de763cc653a8a8ca',
 'xmodel/d125-b-reconstruction-gate-fable5-20260906.md':'3f154e7816deb5de39e727f99cafac3328592c703af246614d4f1e9fe2ccf1ea',
 'xmodel/d125-zero-k-boundary-classification-astra-20260907.md':'129947ee5a370991864a52936d1936179ec9c38efdf0fd80de989e8ed57237a2'
}
def pin(path):
    raw=path.read_bytes()
    return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
inputs={}
for name,expected in PINS.items():
    item=pin(ROOT/name)
    if item['sha256']!=expected: raise RuntimeError('input drift: '+name)
    inputs[name]=item
owned={str(p.relative_to(ROOT)):pin(p) for p in sorted(HERE.iterdir()) if p.is_file() and p.name!='custody.json'}
data={'schema':'jc2.bounded-desk-custody/v1','status':'TERMINAL','utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
      'owner':'nonemptiness_certificate','all_writers_finished':True,'workers':[],'jobs':[],
      'main_low_row_result_independent_of_provisional_classification':True,
      'optional_DVR_interface_conditional_on_classification':True,
      'no_live_classification_gate_or_peer_read':True,'no_AWS_SSH_CAS_full_source_solver_shared_edit':True,
      'owned':owned,'inputs':inputs,'report':pin(REPORT),'transaction':pin(Path(str(REPORT)+'.artifact.json')),
      'no_live_edit_promise':'All owned artifacts immutable from publication; no continuing writer.'}
with (HERE/'custody.json').open('x') as f:
    json.dump(data,f,sort_keys=True,indent=2); f.write('\n')
print(json.dumps({'status':'TERMINAL','owned_files':len(owned),'input_files':len(inputs),
                  'report_sha256':data['report']['sha256'],'custody_sha256':pin(HERE/'custody.json')['sha256']}))
