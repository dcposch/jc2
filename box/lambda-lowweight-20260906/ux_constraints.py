#!/usr/bin/env python3
"""Linear alpha1 constraints forced by actual T2 degree/scalar attainment.
Also computes lambda modulo this coordinate ideal by an exact monomial map.
"""
import json,pathlib,gzip,hashlib,re
O=pathlib.Path(__file__).resolve().parent;rows=[]
for d in json.loads((O/'run_cases.json').read_text()):
 aa=[v for v in d['variables'] if v.startswith('A1_')];K,W=d['K'],d['W'];assert W!=K
 if W>K:
  z=[v for v in aa if v!='A1_0_0'];rule='all alpha1 coordinates except A1_0_0 vanish'
 else:
  z=[v for v in aa if K-int(v.split('_')[2])<W or (K-int(v.split('_')[2])==W and int(v.split('_')[1])>0)]
  rule='alpha1 y-deficit < W vanishes; positive-x alpha1 coordinates at y-deficit W vanish'
 raw=gzip.decompress(pathlib.Path(d['lambda_path']).read_bytes());assert hashlib.sha256(raw).hexdigest()==d['lambda_sha256']
 terms=re.findall(r'[+-]?[^+-]+',raw.decode().strip());Z=set(z);kept=[];counts={}
 for term in terms:
  found=Z.intersection(re.findall(r'\b[A-Za-z][A-Za-z0-9_]*\b',term))
  if found:
   v=min(found,key=z.index);counts[v]=counts.get(v,0)+1
  else:kept.append(term)
 assert kept;reduced=''.join(kept).lstrip('+')+'\n';rd=reduced.encode();lp=O/(d['id']+'.lambda-UX.txt.gz');lp.write_bytes(gzip.compress(rd,mtime=0))
 rows.append(dict(id=d['id'],class_id=d.get('class_id'),K=K,W=W,D2=d['D2'],rule=rule,zero_variables=z,zero_variable_bidegrees={v:[int(v.split('_')[1]),K-int(v.split('_')[2])] for v in z},number_of_linear_constraints=len(z),original_lambda_path=d['lambda_path'],original_lambda_sha256=d['lambda_sha256'],original_lambda_terms=len(terms),reduced_lambda_path=str(lp.relative_to(O.parents[1])),reduced_lambda_sha256=hashlib.sha256(rd).hexdigest(),reduced_lambda_compressed_sha256=hashlib.sha256(lp.read_bytes()).hexdigest(),reduced_lambda_terms=len(kept),removed_terms=len(terms)-len(kept),removed_term_cofactor_partition_counts=counts,exact_identity='lambda-lambda_UX=sum(z*D_z), assigning each removed monomial to its first UX coordinate and dividing by that coordinate',ideal_necessity='Every listed coordinate lies in the characteristic upper/scalar-leader ideal U by successive monic -q pivots; no radical-only inference.'))
result=dict(schema='jc2.lambda.linear-upper/v1',status='PASS',coefficient_field='Q',proof_note='box/lambda-lowweight-20260906/UX-note.md',cases=rows)
p=O/'UX.json';t=p.with_suffix('.json.tmp');t.write_text(json.dumps(result,indent=2)+'\n');t.replace(p)
print(json.dumps([(r['id'],r['number_of_linear_constraints'],r['original_lambda_terms'],r['reduced_lambda_terms']) for r in rows]))
