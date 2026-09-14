#!/usr/bin/python3
import sys
sys.dont_write_bytecode=True
import hashlib
import json
from pathlib import Path

ROOT=Path('/home/ubuntu/jc2')
HERE=Path(__file__).resolve().parent
REPORT=ROOT/'xmodel/d125-reducible-cone-initial-discriminator-astra-20260908.md'
inputs={
 'xmodel/d125-pure-critical-remainder-astra-20260907.md':'7d7993d2bca7cd84bd2c7c7f40b7567c1f5be9b69c119c18c98f6d2b97ca7c74',
 'xmodel/d125-pure-high-alpha-discriminator-astra-20260907.md':'3eaf5610aede5885efa1c9aba95dc2016269952f5c0983675abfacc79b9c9bed',
}
paths=[ROOT/p for p in inputs]+[HERE/p for p in ('check.py','replay.py','witness.json','replay.json','custody.py')]+[REPORT,Path(str(REPORT)+'.artifact.json')]
entries=[]
for p in paths:
    data=p.read_bytes()
    rel=str(p.relative_to(ROOT))
    digest=hashlib.sha256(data).hexdigest()
    if rel in inputs and digest!=inputs[rel]: raise ValueError(('input drift',rel))
    entries.append({'path':rel,'bytes':len(data),'sha256':digest,'role':'input' if rel in inputs else 'owned'})
receipt={'status':'TERMINAL','owner':'/root/nonemptiness_certificate','writers':'ALL IDLE','jobs':[],
         'scope':'Local cone tuple lemma and branch-selection countercontrol; no source arc or degeneration premise',
         'no_live_edit':True,'entries':entries,'whole_proofs_read':list(inputs),'new_external_theorems':[]}
data=(json.dumps(receipt,sort_keys=True,indent=2)+'\n').encode()
with (HERE/'custody.json').open('xb') as f: f.write(data)
print(json.dumps({'entries':len(entries),'custody_sha256':hashlib.sha256(data).hexdigest(),
                  'report_sha256':next(e['sha256'] for e in entries if e['path']==str(REPORT.relative_to(ROOT)))},sort_keys=True))
