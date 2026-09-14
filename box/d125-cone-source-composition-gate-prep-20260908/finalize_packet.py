#!/usr/bin/python3
"""Verify final prep bytes and publish exclusive custody; no launch/replay."""
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path

ROOT=Path('/home/ubuntu/jc2')
HERE=Path(__file__).resolve().parent
REPORT=ROOT/'xmodel/d125-cone-source-composition-gate-prep-astra-20260908.md'
pins=json.loads((HERE/'PINS.json').read_bytes())
prompt=(HERE/'prompt.txt').read_text()
expected=[str((HERE/'PINS.json').relative_to(ROOT))]+[e['snapshot'] for e in pins['entries']]
actual=[line.split('=',1)[1] for line in prompt.splitlines() if line.startswith('charged_input=')]
if actual!=expected: raise ValueError('charged input vector mismatch')
if len({Path(p).name for p in actual})!=len(actual): raise ValueError('duplicate charged basename')
if '{{LANE_INPUTS}}' not in prompt or pins['lane_inputs_token']!='{{LANE_INPUTS}}':
    raise ValueError('missing literal lane token')
if 'charge_basis' in pins or any(x.startswith('charge_basis=') for x in prompt.splitlines()):
    raise ValueError('exit-price declaration forbidden')
for entry in pins['entries']:
    snap=(ROOT/entry['snapshot']).read_bytes()
    if hashlib.sha256(snap).hexdigest()!=entry['snapshot_sha256']:
        raise ValueError('snapshot drift')
    if entry['source_sha256'] is not None:
        source=(ROOT/entry['source']).read_bytes()
        if source!=snap or hashlib.sha256(source).hexdigest()!=entry['source_sha256']:
            raise ValueError('source drift')
files=[HERE/p for p in ('prompt-template.txt','prepare.py','PINS.json','prompt.txt','finalize_packet.py')]
if (HERE/'SOURCE-RELEASE.json').exists(): files.append(HERE/'SOURCE-RELEASE.json')
files += [ROOT/e['snapshot'] for e in pins['entries']]
files += [REPORT,Path(str(REPORT)+'.artifact.json')]
owned=[]
for p in files:
    data=p.read_bytes()
    owned.append({'path':str(p.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
receipt={'status':'TERMINAL_PREP_ONLY','owner':'/root/nonemptiness_certificate',
         'writers':'ALL IDLE','jobs':[],'no_launch':True,'no_math_replay':True,
         'source_status':pins['source_status'],'charged_count_including_PINS':len(actual),
         'root_only_launch_authority':True,'no_live_edit':True,'owned':owned,
         'source_pins':pins['entries']}
data=(json.dumps(receipt,sort_keys=True,indent=2)+'\n').encode()
with (HERE/'custody.json').open('xb') as f: f.write(data)
print(json.dumps({'status':'VERIFIED_PREP_ONLY','charged':len(actual),'owned':len(owned),
                  'source_status':pins['source_status'],
                  'custody_sha256':hashlib.sha256(data).hexdigest(),
                  'report_sha256':hashlib.sha256(REPORT.read_bytes()).hexdigest()},sort_keys=True))
