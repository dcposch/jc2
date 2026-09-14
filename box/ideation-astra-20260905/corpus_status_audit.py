#!/usr/bin/env python3
"""Blind-safe receipt metadata sidecar; never opens any corpus report body.

Exploratory instrument, not a replacement for open_collision or a promotion gate.
"""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import sys

p = argparse.ArgumentParser()
p.add_argument('--root', type=Path, default=Path.cwd())
p.add_argument('--report', required=True, type=Path)
p.add_argument('--out', required=True, type=Path)
a = p.parse_args()
root = a.root.resolve()
sys.path.insert(0, str(root / 'ops'))
import open_collision
paths = open_collision.banked_corpus(root, a.report)
counts = collections.Counter()
rows = []
for path in paths:
    receipt = path.with_suffix('.run.v2')
    if receipt.is_file():
        raw = receipt.read_bytes()
        d = dict(line.split('=', 1) for line in raw.decode(errors='replace').splitlines() if '=' in line)
        final = d.get('final_status')
        state = d.get('report_state', 'UNRECORDED')
        digest = hashlib.sha256(raw).hexdigest()
    else:
        final, state, digest = 'LEGACY', 'NO_RECEIPT', None
    counts[f'{final}/{state}'] += 1
    rows.append({'path': str(path.relative_to(root)), 'final_status': final,
                 'report_state': state, 'receipt_sha256': digest})
protected = {'xmodel/moh100-14rows-opus5-20260905.md',
             'xmodel/k16-f3abel-astra-20260905.md'}
leaks = [r['path'] for r in rows if r['path'] in protected or
         (Path(r['path']).name.startswith('ideation-20260905T0200Z-') and
          not Path(r['path']).name.endswith('-packet.md'))]
result = {'instrument': 'INTERNAL-UNREVIEWED / metadata-only',
          'report': str(a.report), 'corpus_files': len(rows),
          'status_counts': dict(sorted(counts.items())),
          'protected_or_blind_leaks': leaks, 'receipts': rows}
a.out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'receipts'}, indent=2))
if leaks:
    raise SystemExit(2)
