#!/usr/bin/env python3
import hashlib,json,math
from pathlib import Path
P=Path(__file__).resolve().parent
p=P/'roster.supplementary.jsonl';rows=[json.loads(x) for x in p.read_text().splitlines()]
result=[]
for row in rows:
 s=row['source']
 if s['u_s']<2:continue
 M=s['M'];d=[s['n']]
 for m in M:d.append(math.gcd(d[-1],m))
 assert d==s['d']
 q=[M[0]]+[b-a for a,b in zip(M,M[1:])]
 degree=[];lam=0
 for i,v in enumerate(q):
  lam+=d[i]*v;assert lam%d[i]==0;degree.append(-lam//d[i])
 for i in range(1,len(degree)):assert (d[i-1]//d[i])*degree[i-1]-degree[i]==q[i]
 assert M[-1]==s['n']-2 and all(m<s['n']-1 for m in M)
 result.append({'row_id':row['row_id'],'n':s['n'],'m':s['m'],'M':M,'d':d,'effective_characteristic_degrees':degree,
                'recursive_attainment_defects':q[1:],'leaf_count':row['split_window']['leaf_count'],
                'leaves':row['split_window']['leaves'],
                'scope':'parent-realization necessary rows; no child Keller hypothesis or coordinate lift inferred',
                'all_effective_scalar_leaders_necessary':True,'all_parent_total_degrees_necessary':True,
                'child_prefix_only':row['descent']['prefix_only']})
assert len(result)==20 and sum(r['leaf_count'] for r in result)==36
assert all(r['leaf_count']==len(r['leaves']) for r in result)
out={'supplementary_roster_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'parent_rows':20,'typed_ES_leaves_mechanically_counted':36,'prior_report_claim':38,'count_discrepancy':2,'rows':result,
     'verdict':'UNIFORM NECESSITY ON A REALIZED PARENT COEFFICIENT LIFT; NO LEAF KILL OR ATTAINMENT CLAIM',
     'defect_range':[min(q for r in result for q in r['recursive_attainment_defects']),max(q for r in result for q in r['recursive_attainment_defects'])]}
(P/'instrument-manifest.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
