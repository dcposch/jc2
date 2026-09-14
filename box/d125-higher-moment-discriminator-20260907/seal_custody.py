#!/usr/bin/env python3
"""Exclusive custody receipt after bounded writers and report publication finish."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

base=Path(__file__).resolve().parent
root=base.parent.parent
report=root/'xmodel/d125-higher-moment-discriminator-astra-20260907.md'
files=sorted(p for p in base.iterdir() if p.is_file() and p.name!='custody.json')
files += [report,Path(str(report)+'.artifact.json')]
records=[]
for p in files:
    data=p.read_bytes()
    records.append({'path':str(p.relative_to(root)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
packet={'schema':'jc2.bounded-desk-custody/v1','owner':'nonemptiness_certificate',
        'terminal_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'status':'TERMINAL_NO_GAIN','all_writers_idle_after_this_exclusive_write':True,
        'workers':[],'no_live_edits_promised':True,'files':records,
        'charged_replay':'v2-replay.json',
        'preliminary_evidence':'Unprefixed replay/output files are superseded and retained; only v2 matches the final strengthened checker.',
        'claims':'Literal-chart exactness criterion and moment necessity; all-moment countermodels and failed Mathieu interface. No fixed-face point or exclusion, solve, full source power expansion, or JC2 claim.'}
data=(json.dumps(packet,indent=2,sort_keys=True)+'\n').encode()
with (base/'custody.json').open('xb') as f:
    f.write(data)
print(json.dumps({'status':'TERMINAL','files':len(records),'custody_sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)},sort_keys=True))
