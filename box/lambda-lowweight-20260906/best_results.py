#!/usr/bin/env python3
"""Canonical best receipt index, without replacing historical computation records."""
import collections,hashlib,json
from pathlib import Path
import receiver_alias
HERE=Path(__file__).resolve().parent
def kind(r):
    s=r['case']
    return 'charge0' if '.charge0' in s else 'Keller+UX' if '.UX' in s else 'Keller' if '.keller' in s else 'baseline'
def score(r):
    status=r.get('source_status',r['status'])
    return (int(status=='UNIT_CANDIDATE_NEEDS_COFACTORS'),
            int(r.get('completed_homogeneous_weight') is not None),
            int(bool(r.get('run_complete'))),int(bool(r.get('input_ready'))),
            int(bool(r.get('frontier_ready'))),
            int(r['receipt'].endswith('.packed511.N'+str(r['N'])+'.json')),
            r.get('finished_utc',''))
def main():
    receiver_alias.alias();groups=collections.defaultdict(list)
    for p in sorted(HERE.glob('*.N*.json')):
        r=json.loads(p.read_text())
        if 'N' not in r or 'cutoff' not in r:continue
        if '.parallel7g' in r['case']:continue
        r['receipt']=p.name
        groups[(r['case'].split('.')[0],r['N'],kind(r))].append(r)
    selected=[]
    for (cid,N,variant),rows in sorted(groups.items()):
        r=max(rows,key=score)
        entry={k:r.get(k) for k in ('status','source_status','source_receipt','input_ready','std_done','completed_homogeneous_weight','wall_seconds','peak_rss_bytes','basis_size','nf_is_zero','nf_is_query','driver_sha256','original_rows_sha256','UX_row_cache_receipt')}
        entry.update(case=cid,N=N,variant=variant,W=r['W'],requested_cutoff=r['cutoff'],receipt=r['receipt'],
                     receipt_sha256=hashlib.sha256((HERE/r['receipt']).read_bytes()).hexdigest(),
                     all_historical_receipts=[a['receipt'] for a in rows])
        selected.append(entry)
    output={'scope':'Best evidence per case/N/variant; OPEN requested cutoffs are not completed weights.',
            'driver_sha256':hashlib.sha256((HERE/'run_truncated.py').read_bytes()).hexdigest(),
            'records':selected,'record_count':len(selected)}
    (HERE/'best-results.json').write_text(json.dumps(output,indent=2)+'\n')
    lines=['# Canonical result receipts','',
           '| Case | N | Variant | B requested | Completed B | Status | Input ready | Receipt |',
           '|---|---:|---|---:|---:|---|---|---|']
    for r in selected:
        lines.append('| '+' | '.join(map(str,[r['case'],r['N'],r['variant'],r['requested_cutoff'],r['completed_homogeneous_weight'],r['status']+(' / '+r['source_status'] if r['source_status'] else ''),r['input_ready'],r['receipt']]))+' |')
    (HERE/'best-results.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps({'record_count':len(selected),'counts':dict(collections.Counter((r['variant']+':'+(r['source_status'] or r['status'])) for r in selected))}))
if __name__=='__main__':main()
