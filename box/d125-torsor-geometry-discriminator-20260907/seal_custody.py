#!/usr/bin/env python3
"""Exclusive final inventory after all owned arithmetic/publication writers exit."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

base = Path(__file__).resolve().parent
root = base.parent.parent
report = root/'xmodel/d125-torsor-geometry-discriminator-astra-20260907.md'
files = sorted(p for p in base.iterdir() if p.is_file() and p.name != 'custody.json')
files += [report, Path(str(report)+'.artifact.json')]
records = []
for p in files:
    data = p.read_bytes()
    records.append({'path': str(p.relative_to(root)), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
packet = {'schema':'jc2.bounded-desk-custody/v1', 'owner':'nonemptiness_certificate',
          'terminal_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),
          'status':'TERMINAL_NO_HIT', 'all_writers_idle_after_this_exclusive_write':True,
          'workers':[], 'no_live_edits_promised':True, 'files':records,
          'lifecycle_note':'Initial finalize command had a mistyped token and failed closed; corrected token finalized and verified unchanged closed bytes.',
          'claims':'Exact torsor/marked-map and quasi-finite interfaces only; no source point, solver, properness, or new JC2 theorem.'}
data = (json.dumps(packet, indent=2, sort_keys=True)+'\n').encode()
with (base/'custody.json').open('xb') as f:
    f.write(data)
print(json.dumps({'status':'TERMINAL', 'files':len(records), 'custody_sha256':hashlib.sha256(data).hexdigest(), 'bytes':len(data)}, sort_keys=True))
