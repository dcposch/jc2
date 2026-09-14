#!/usr/bin/env python3
"""Verify/freeze prepared review metadata; never import or run a mathematical checker."""
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path
import resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
pins=json.loads((HERE/'PINS.json').read_text()); prompt=(HERE/'prompt.txt').read_text()
declared=[x.split('=',1)[1] for x in prompt.splitlines() if x.startswith('charged_input=')]
expected=[x['snapshot'] for x in pins['entries']]
if declared!=expected or len(set(Path(x).name for x in declared))!=12: raise RuntimeError('charge declarations/names mismatch')
if prompt.count('{{LANE_INPUTS}}')!=1 or 'charge_basis='+pins['charge_basis'] not in prompt: raise RuntimeError('literal template/basis missing')
if '<!-- BODY-END -->' not in prompt or 'no authored Seal' in prompt: pass
entries=[]
for row in pins['entries']:
    for key,hashkey in [('source','source_sha256'),('snapshot','snapshot_sha256')]:
        data=(ROOT/row[key]).read_bytes()
        if hashlib.sha256(data).hexdigest()!=row[hashkey]: raise RuntimeError('drift: '+row[key])
    entries.append(row)
owned=[p for p in sorted(HERE.rglob('*')) if p.is_file()]
owned += [ROOT/'xmodel/d125-pure-high-alpha-gate-prep-astra-20260907.md',ROOT/'xmodel/d125-pure-high-alpha-gate-prep-astra-20260907.md.artifact.json']
ownpins=[]
for path in owned:
    data=path.read_bytes(); path.chmod(0o444)
    ownpins.append({'path':str(path.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
packet={'status':'PREP_ONLY_TERMINAL','owner':'/root/nonemptiness_certificate','writers':'ALL_IDLE','launch':'NOT_PERFORMED_ROOT_ONLY','replay':'NOT_PERFORMED','source_snapshot_pairs_verified':len(entries),'source_snapshot_pairs':entries,'owned_files':ownpins,'read_only_packet':True,'no_live_edit_promise':True}
with (HERE/'custody.json').open('x') as stream: json.dump(packet,stream,sort_keys=True,indent=2); stream.write('\n')
(HERE/'custody.json').chmod(0o444)
for row in ownpins:
    if hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()!=row['sha256']: raise RuntimeError('post-freeze drift')
print(json.dumps({'status':'VERIFIED_FROZEN','charged':len(entries),'own_pins':len(ownpins),'custody_sha256':hashlib.sha256((HERE/'custody.json').read_bytes()).hexdigest(),'prompt_sha256':hashlib.sha256((HERE/'prompt.txt').read_bytes()).hexdigest(),'pins_sha256':hashlib.sha256((HERE/'PINS.json').read_bytes()).hexdigest()}))
