#!/usr/bin/env python3
"""Read-only curation of completed checkpoint records, never an ideal verdict.

Run after the final artifact pull. Alternative continuation JSONs may be given
with --jacobian; their original hashes and chart/gauge scope are preserved.
"""
import argparse,csv,hashlib,json
from pathlib import Path
N=Path(__file__).resolve().parent
ap=argparse.ArgumentParser()
ap.add_argument('--jacobian',type=Path,action='append')
args=ap.parse_args()
rows=[];inputs=[]
def read(path):
    raw=path.read_bytes();q=json.loads(raw)
    inputs.append({'path':str(path),'sha256':hashlib.sha256(raw).hexdigest()})
    return q
def add(branch,lane,phase,power,record,path,gauge):
    dimension=record.get('dimension')
    assert isinstance(dimension,int),(path,phase,dimension)
    point=record.get('rational_point',{})
    rows.append({'branch':branch,'lane':lane,'phase':phase,'power':power,
        'dimension':dimension,'jet0_gauge':gauge,
        'residual_rows':record.get('residual_count',''),
        'rational_point_status':point.get('status',''),
        'record_source':str(path)})
for branch in ('delta2','delta52'):
    p=N/'results'/f'full-{branch}.json'
    q=read(p)
    for r in q['records']:
        if r['stage']<=8:
            add(branch,'finite-source',str(r['stage']),r['stage'],r,p,'free')
    p=N/'results-source-full'/f'source-full-{branch}_minor_block.json'
    q=read(p)
    for r in q['trace']:
        add(branch,'complete-minor',r['kind'],r['local_power'],r,p,'jet0=0; audited isomorphism')
paths=args.jacobian or [N/'results-fullJ-flint'/f'fullJ-flint-{b}.json' for b in ('delta2','delta52')]
endpoints=[]
def ancestor_path(meta):
    name=Path(meta['state']).name
    expected=meta['state_sha256']
    candidates=[p for p in N.rglob(name) if p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==expected]
    assert candidates,('missing exact ancestor',name,expected)
    return sorted(candidates)[0]
def continuation(p,seen):
    p=p.resolve();q=read(p)
    assert q['field']=='Q'
    if q.get('resumed_from'):
        continuation(ancestor_path(q['resumed_from']),seen)
    for r in q['records']:
        key=(q['branch'],r['phase'])
        assert key not in seen,('duplicate continuation phase',key)
        seen.add(key)
        power=r['phase'].removeprefix('Jacobian_t') if r['phase'].startswith('Jacobian_t') else ''
        add(q['branch'],'nonzero-D1-and-J',r['phase'],power,r,p,'jet0=0; audited isomorphism')
    return q
for p in paths:
    p=p.resolve();seen=set();q=continuation(p,seen)
    powers=sorted(int(phase.removeprefix('Jacobian_t')) for branch,phase in seen if phase.startswith('Jacobian_t'))
    if powers:
        assert powers==list(range(powers[0],q['last_completed_t']+1)),('Jacobian continuation gap',powers)
    endpoints.append({'branch':q['branch'],'path':str(p),'final':q['final'],
        'last_completed_t':q['last_completed_t'],'stop_reason':q.get('stop_reason'),
        'last_completed_record':q['records'][-1] if q['records'] else None,
        'recursive_continuation_powers':powers,
        'inherited_weak_J_prefix':q.get('weak_J_bands_already_proved'),
        'scope':'This summary reports a maintained prefix; final promotion requires the independent phase/source/gauge audit.'})
out=N/'stage-trace.csv'
with out.open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
result={'type':'CURATED COMPLETED RECORDS, NOT AN INDEPENDENT VERDICT','inputs':inputs,
    'stage_trace_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
    'record_count':len(rows),'endpoints':endpoints}
(N/'stage-trace-summary.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps({'record_count':len(rows),'endpoints':[{k:v for k,v in x.items() if k in ('branch','last_completed_t','final','stop_reason')} for x in endpoints]},indent=2))
