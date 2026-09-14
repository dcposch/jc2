#!/usr/bin/env python3
"""Run stock open_collision with stricter blind metadata exclusions.

No changes to ops/open_collision.py. Receipts are annotations, not promotion.
"""
import collections
import hashlib
import json
from pathlib import Path
import sys
root=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(root/'ops'))
import open_collision
original=open_collision.banked_corpus
protected=('moh100-14rows-opus5-20260905','k16-f3abel-astra-20260905')

def guarded(repo,report):
    paths=original(repo,report)
    kept=[]; skipped=[]; records=[]; counts=collections.Counter()
    for p in paths:
        if p.name.startswith(protected) or p.name.endswith('.prompt.md'):
            skipped.append(str(p.relative_to(repo.resolve())))
            continue
        kept.append(p)
        receipt=p.with_suffix('.run.v2')
        d={}; digest=None
        if receipt.is_file():
            raw=receipt.read_bytes(); digest=hashlib.sha256(raw).hexdigest()
            d=dict(line.split('=',1) for line in raw.decode(errors='replace').splitlines() if '=' in line)
        state=d.get('report_state','LEGACY_OR_UNRECORDED')
        counts[state]+=1
        records.append(dict(path=str(p.relative_to(repo.resolve())),
                            final_status=d.get('final_status'),report_state=state,
                            receipt_sha256=digest))
    assert not any(p.name.startswith(protected) for p in kept)
    assert not any(p.name.startswith('ideation-20260905T0200Z-') and
                   not p.name.endswith('-packet.md') for p in kept)
    out=dict(engine='ops/open_collision.py unmodified',
             extra_guards=['protected lane prefixes regardless of completion','prompt metadata'],
             included=len(kept),excluded_additionally=len(skipped),
             status_counts=dict(counts),skipped=skipped,records=records)
    (Path(__file__).resolve().parent/'collision-corpus.json').write_text(json.dumps(out,indent=2)+'\n')
    return tuple(kept)

open_collision.banked_corpus=guarded
raise SystemExit(open_collision.main())
