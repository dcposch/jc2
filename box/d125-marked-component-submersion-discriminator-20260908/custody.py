#!/usr/bin/python3
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path

ROOT=Path('/home/ubuntu/jc2')
HERE=Path(__file__).resolve().parent
REPORT=ROOT/'xmodel/d125-marked-component-submersion-discriminator-astra-20260908.md'
inputs={
 'xmodel/d125-parity-unit-normalization-astra-20260907.md':'19f0394c2ec97797d325afa234d57c598a94bd2d83cbfe1dd24bda52db0f45cc',
 'xmodel/d125-marked-fiber-global-discriminator-astra-20260907.md':'e8bd150980cc9ec855d9cfe73ea7b3116a4a06c774f34154c8bac50b12209e16',
 'xmodel/d125-torsor-geometry-discriminator-astra-20260907.md':'7beff9e113580e22aba68f79811ed45f2023e195f7998a51cd224163a775db5a',
}
paths=[ROOT/p for p in inputs]+[HERE/p for p in ('check.py','replay.py','witness.json','replay.json','custody.py')]+[REPORT,Path(str(REPORT)+'.artifact.json')]
entries=[]
for p in paths:
    data=p.read_bytes()
    digest=hashlib.sha256(data).hexdigest()
    rel=str(p.relative_to(ROOT))
    if rel in inputs and digest!=inputs[rel]:
        raise ValueError(('input drift',rel))
    entries.append({'path':rel,'bytes':len(data),'sha256':digest,'role':'input' if rel in inputs else 'owned'})
receipt={'status':'TERMINAL','owner':'/root/nonemptiness_certificate','writers':'ALL IDLE',
         'scope':'NO-GAIN full source; exact embedding control and degree_u(M)<=1 obstruction only',
         'no_live_edit':True,'jobs':[],'entries':entries,
         'read_scope':'Three charged terminal reports wholly; no newly imported primary theorem; source degree bound rederived from receiver monomials.'}
data=(json.dumps(receipt,sort_keys=True,indent=2)+'\n').encode()
with (HERE/'custody.json').open('xb') as f:
    f.write(data)
print(json.dumps({'entries':len(entries),'custody_sha256':hashlib.sha256(data).hexdigest(),
                  'report_sha256':next(e['sha256'] for e in entries if e['path']==str(REPORT.relative_to(ROOT)))},sort_keys=True))
