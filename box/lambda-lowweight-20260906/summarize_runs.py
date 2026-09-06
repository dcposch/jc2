#!/usr/bin/env python3
"""Produce compact receipts from the individual bounded-run JSON records."""
import collections, json
from pathlib import Path

HERE=Path(__file__).resolve().parent
records=[]; pending=[]
for path in sorted(HERE.glob('*.N*.json')):
    try: row=json.loads(path.read_text())
    except json.JSONDecodeError:
        pending.append(path.name)
        continue
    if 'N' not in row or 'cutoff' not in row: continue
    row['receipt']=path.name
    records.append(row)
summary={
    'record_count':len(records),
    'pending_or_invalid_receipts':pending,
    'status_counts':dict(collections.Counter(r.get('status','UNKNOWN') for r in records)),
    'total_process_wall_seconds':round(sum(r.get('wall_seconds') or 0 for r in records),3),
    'maximum_recorded_peak_rss_bytes':max((r.get('peak_rss_bytes') or 0 for r in records),default=0),
    'records':records,
}
(HERE/'run-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Run receipt index','',
       'Completed weights below are target-specific homogeneous certificate bounds. '
       'A requested cutoff on a timed-out run is not a completed degree. '
       'The charge0 variant is an exact target component, not the full weighted basis.','',
       '| Case / variant | N | Requested B | Status | Input ready | std done | GB size | Seconds | Peak MiB |',
       '|---|---:|---:|---|---|---|---:|---:|---:|']
for r in records:
    lines.append('| '+' | '.join(map(str,[r['case'],r['N'],r['cutoff'],r.get('status'),r.get('input_ready'),r.get('std_done'),r.get('basis_size','—'),r.get('wall_seconds'),round((r.get('peak_rss_bytes') or 0)/2**20,1)]))+' |')
(HERE/'run-summary.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='records'}))
