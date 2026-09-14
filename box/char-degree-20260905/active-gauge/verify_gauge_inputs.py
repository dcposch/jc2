#!/usr/bin/env python3
"""Independently replay every gauge image and retained coordinate."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;records=[];j=s.Symbol('jet0')
for branch in ['delta2','delta52']:
 p=HERE/'inputs'/f'{branch}_stage8.json';d=json.loads(p.read_text())
 parent=Path(d['source_gauge']['parent_input']);before=json.loads(parent.read_text())
 assert hashlib.sha256(parent.read_bytes()).hexdigest()==d['source_gauge']['parent_input_sha256']
 assert set(before['full_free_coordinates'])-set(d['full_free_coordinates'])=={'jet0'}
 assert set(d['full_free_coordinates'])<=set(before['full_free_coordinates'])
 tested=0
 for name,rows in before['maps'].items():
  old={(r,q):s.sympify(v) for r,q,v in rows};new={(r,q):s.sympify(v) for r,q,v in d['maps'][name]}
  for key in old.keys()|new.keys():
   assert s.expand(old.get(key,s.S.Zero).subs(j,0)-new.get(key,s.S.Zero))==0
   tested+=1
 expected=[(label,s.expand(s.sympify(v).subs(j,0))) for label,v in before['residual_rows']]
 expected=[(label,v) for label,v in expected if v!=0]
 assert len(expected)==len(d['residual_rows'])
 for (l,v),(l2,v2) in zip(expected,d['residual_rows']):assert l==l2 and s.expand(v-s.sympify(v2))==0
 protected={'target_'+x for x in 'abcde'}|{'leader55','Z55','Hc_11_0','u',('minor_a2' if branch=='delta2' else 'v'),('rho' if branch=='delta2' else 'c')}
 assert protected<=set(d['full_free_coordinates']),protected-set(d['full_free_coordinates'])
 hfirst={r for r,q,v in d['maps']['h3'] if r>0}
 assert min(hfirst)>=2
 records.append({'branch':branch,'stage':8,'image_sites_checked':tested,'all_residuals_checked':True,
                 'only_jet0_removed':True,'all_protected_coordinates_retained':True,
                 'h3_first_positive_t_order':min(hfirst),
                 'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
result={'status':'PASS','field':'Q','records':records,
        'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print(json.dumps(result,indent=2,sort_keys=True))
