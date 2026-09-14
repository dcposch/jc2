#!/usr/bin/env python3
"""Pin only this owned box, its transaction, and explicitly named terminal inputs."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REPORT = ROOT/'xmodel/d125-symmetry-discriminator-astra-20260907.md'
EXPECTED = {
 'xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md':'7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413',
 'xmodel/d125-minimal-receiver-client-preflight-astra-20260906.md':'e0debc7da22b8864ba43f0d29928e2104f2d8f161421ad26f29d8017f7b95e80',
 'xmodel/d125-small-receiver-polynomial-lift-contract-astra-20260906.md':'433cc2fe9f11ce1b2e1f1fc57aab24def921afb1f93154a2d631ddee0b88cdad',
 'xmodel/d125-lift-hermite-pivots-astra-20260906.md':'b6a81fc0c925d63f13f72d4b8ee1203adcecb8a6f4dc349f8c2a62d5805cf126',
 'xmodel/d125-lift-hermite-gate-fable5-20260906.md':'7e2594d53150bf4346f4e4cc6e7f6ff05a021b045b640128de763cc653a8a8ca',
 'box/d125-minimal-receiver-client-preflight-20260906/client.py':'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53',
 'xmodel/d125-minimal-receiver-b-reconstruction-astra-20260906.md':'cd2792c8ec4fdbd286fe7925f36739337ea621eb69d5ea8df90a7cd5804c82bf',
 'xmodel/d125-b-reconstruction-gate-fable5-20260906.md':'3f154e7816deb5de39e727f99cafac3328592c703af246614d4f1e9fe2ccf1ea',
 'xmodel/d125-b-witness-exact-export-repair-astra-20260906.md':'e456830948ce1f48dbdba3ddfba47e6a8c2b58ffa67b6cf183fe4b08cb98f0df',
 'box/d125-b-witness-exact-export-repair-20260906/exact-witnesses-v2.json':'07b4ce881b4f90f9a41a3f8cb01fcd3a120ff64a4f04969e60126dbdb6e7f246',
 'xmodel/d125-b-a-hermite-composition-astra-20260907.md':'769ffb37443260edbe68585c2a7e9d775123a674b987f9108c23ca84dbb8fe9c',
 'xmodel/d125-b-a-hermite-composition-gate-fable5-20260907.md':'601cbe68958556ca736ade77b5b849d1326835f2328a2b951d2413609ebdbe59',
}

def entry(path):
    raw = path.read_bytes()
    return {'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

inputs = {}
for relative, expected in EXPECTED.items():
    value = entry(ROOT/relative)
    if value['sha256'] != expected:
        raise RuntimeError('input hash mismatch: '+relative)
    inputs[relative] = value
owned = {str(path.relative_to(ROOT)):entry(path) for path in sorted(HERE.iterdir())
         if path.is_file() and path.name != 'custody.json'}
receipt = {'schema':'jc2.bounded-desk-custody/v1','status':'TERMINAL',
           'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
           'owner':'nonemptiness_certificate','all_arithmetic_export_writers_finished':True,
           'jobs':[],'workers':[],'no_AWS_SSH_CAS_solver_live_peer_or_shared_edits':True,
           'owned':owned,'terminal_inputs':inputs,
           'report':entry(REPORT),'transaction':entry(Path(str(REPORT)+'.artifact.json')),
           'no_live_edit_promise':'All owned files immutable on this publication; no continuing writer.'}
with (HERE/'custody.json').open('x') as f:
    json.dump(receipt,f,sort_keys=True,indent=2)
    f.write('\n')
print(json.dumps({'status':'TERMINAL','owned_files':len(owned),'input_files':len(inputs),
                  'report_sha256':receipt['report']['sha256'],'custody_sha256':entry(HERE/'custody.json')['sha256']}))
