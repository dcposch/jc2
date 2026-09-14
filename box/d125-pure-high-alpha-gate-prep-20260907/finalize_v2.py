#!/usr/bin/env python3
"""Scope-only supersession; no mathematical replay or launch."""
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path
import resource
resource.setrlimit(resource.RLIMIT_CPU,(25,25)); resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))
HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[1]
pins=json.loads((HERE/'PINS.json').read_text()); prompt=(HERE/'prompt-v2.txt').read_text()
declared=[line.split('=',1)[1] for line in prompt.splitlines() if line.startswith('charged_input=')]
if declared!=[x['snapshot'] for x in pins['entries']] or len({Path(p).name for p in declared})!=12: raise RuntimeError('charge mismatch')
if prompt.count('{{LANE_INPUTS}}')!=1 or 'charge_basis='+pins['charge_basis'] not in prompt: raise RuntimeError('template mismatch')
if '<!-- BODY-END -->' not in prompt or 'no authored Seal section' not in prompt: raise RuntimeError('output protocol missing')
for entry in pins['entries']:
    for key,hkey in [('source','source_sha256'),('snapshot','snapshot_sha256')]:
        if hashlib.sha256((ROOT/entry[key]).read_bytes()).hexdigest()!=entry[hkey]: raise RuntimeError('input drift')
paths=[p for p in sorted(HERE.rglob('*')) if p.is_file()]
paths += [ROOT/'xmodel/d125-pure-high-alpha-gate-prep-astra-20260907.md',ROOT/'xmodel/d125-pure-high-alpha-gate-prep-astra-20260907.md.artifact.json']
owned=[]
for path in paths:
    data=path.read_bytes(); path.chmod(0o444)
    owned.append({'path':str(path.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
packet={'status':'PREP_ONLY_TERMINAL_V2','owner':'/root/nonemptiness_certificate','active_prompt':'box/d125-pure-high-alpha-gate-prep-20260907/prompt-v2.txt','scope_correction':'SCOPE-CORRECTION.md','superseded_prompt_preserved':'prompt.txt','original_custody_preserved':'custody.json','charged_snapshots_unchanged':12,'writers':'ALL_IDLE','launch':'NOT_PERFORMED_ROOT_ONLY','replay':'NOT_PERFORMED','owned_files':owned,'read_only_packet':True,'no_live_edit_promise':True}
with (HERE/'custody-v2.json').open('x') as stream: json.dump(packet,stream,sort_keys=True,indent=2); stream.write('\n')
(HERE/'custody-v2.json').chmod(0o444)
for row in owned:
    if hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest()!=row['sha256']: raise RuntimeError('post-freeze drift')
print(json.dumps({'status':'VERIFIED_FROZEN_V2','own_pins':len(owned),'prompt_v2_sha256':hashlib.sha256((HERE/'prompt-v2.txt').read_bytes()).hexdigest(),'custody_v2_sha256':hashlib.sha256((HERE/'custody-v2.json').read_bytes()).hexdigest(),'scope_correction_sha256':hashlib.sha256((HERE/'SCOPE-CORRECTION.md').read_bytes()).hexdigest()}))
