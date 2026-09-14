#!/usr/bin/python3
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path

ROOT=Path('/home/ubuntu/jc2')
HERE=Path(__file__).resolve().parent
REPORT=ROOT/'xmodel/d125-prescribed-cofactor-submersion-control-astra-20260908.md'
inputs={
 'xmodel/d125-parity-unit-normalization-astra-20260907.md':'19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc',
 'xmodel/d125-marked-fiber-global-discriminator-astra-20260907.md':'e8bd150980cc9ec855d9cfe73ea7b3116a4a06c774f34154c8bac50b12209e16',
 'xmodel/d125-marked-component-submersion-discriminator-astra-20260908.md':'3c127d20c133acf5bcd9af43eec4a3e7d9a403a19d30ab1e827ed8f760b051f5',
}
names=['check.py','replay.py','witness-v2.json','replay-v2.json','custody.py','witness.json','replay.json']
paths=[ROOT/p for p in inputs]+[HERE/p for p in names]+[REPORT,Path(str(REPORT)+'.artifact.json')]
entries=[]
for p in paths:
    data=p.read_bytes()
    rel=str(p.relative_to(ROOT))
    digest=hashlib.sha256(data).hexdigest()
    if rel in inputs and digest!=inputs[rel]:
        raise ValueError(('input drift',rel))
    role='input' if rel in inputs else ('development' if p.name in ('witness.json','replay.json') else 'owned final')
    entries.append({'path':rel,'bytes':len(data),'sha256':digest,'role':role})
receipt={'status':'TERMINAL','owner':'/root/nonemptiness_certificate','writers':'ALL IDLE','jobs':[],
         'scope':'Exact cofactor-compatible polynomial submersion, not Keller/full-source point',
         'no_live_edit':True,'entries':entries,
         'premises':'accepted14c and exact marked restriction only; earlier low-degree theorem is history, not mathematical premise',
         'external_theorems':'none','final_replay':'replay-v2.json'}
data=(json.dumps(receipt,sort_keys=True,indent=2)+'\n').encode()
with (HERE/'custody.json').open('xb') as f:
    f.write(data)
print(json.dumps({'entries':len(entries),'custody_sha256':hashlib.sha256(data).hexdigest(),
                  'report_sha256':next(e['sha256'] for e in entries if e['path']==str(REPORT.relative_to(ROOT)))},sort_keys=True))
