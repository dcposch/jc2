#!/usr/bin/python3
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path

ROOT=Path('/home/ubuntu/jc2')
HERE=Path(__file__).resolve().parent
REPORT=ROOT/'xmodel/d125-golden-divisibility-control-astra-20260908.md'
source='xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md'
expected='7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413'
paths=[ROOT/source]+[HERE/p for p in ('check.py','replay.py','witness.json','replay.json','custody.py')]+[REPORT,Path(str(REPORT)+'.artifact.json')]
entries=[]
for p in paths:
    data=p.read_bytes(); rel=str(p.relative_to(ROOT)); digest=hashlib.sha256(data).hexdigest()
    if rel==source and digest!=expected: raise ValueError('input drift')
    entries.append({'path':rel,'bytes':len(data),'sha256':digest,'role':'accepted literal input' if rel==source else 'owned'})
receipt={'status':'TERMINAL','owner':'/root/nonemptiness_certificate','writers':'ALL IDLE','jobs':[],
         'scope':'Golden degree3 divisibility classification and transport countercontrol only',
         'no_live_edit':True,'entries':entries,'whole_proof_read':source,
         'both_conjugates_retained':True,'source_H_divides_F_squared_assumed_or_proved':False,
         'new_external_theorems':[]}
data=(json.dumps(receipt,sort_keys=True,indent=2)+'\n').encode()
with (HERE/'custody.json').open('xb') as f: f.write(data)
print(json.dumps({'entries':len(entries),'custody_sha256':hashlib.sha256(data).hexdigest(),
                  'report_sha256':next(e['sha256'] for e in entries if e['path']==str(REPORT.relative_to(ROOT)))},sort_keys=True))
