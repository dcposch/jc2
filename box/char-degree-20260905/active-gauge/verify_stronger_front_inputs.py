#!/usr/bin/env python3
"""Replay stronger-front rational graphs and all original coefficient images."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;records=[]
def substitute(v,mapping):
 return s.expand(s.sympify(v).subs(mapping,simultaneous=True))
for branch in ['delta2','delta52']:
 for version in ['quartic','strongest']:
  path=HERE/'inputs'/f'{branch}_stage8.{version}.json';data=json.loads(path.read_text())
  meta=data['stronger_characteristic_front'];parent=Path(meta['parent_input'])
  assert hashlib.sha256(parent.read_bytes()).hexdigest()==meta['parent_input_sha256']
  old=json.loads(parent.read_text());mapping={s.Symbol(k):s.sympify(v) for k,v in meta['map'].items()}
  assert all(s.sympify(p['leader']).is_Rational and s.sympify(p['leader'])!=0 for p in meta['Qstar_pivots'])
  assert set(map(str,mapping))==set(old['full_free_coordinates'])-set(data['full_free_coordinates'])
  assert set(data['full_free_coordinates'])<=set(old['full_free_coordinates'])
  assert not any(set(mapping)&value.free_symbols for value in mapping.values())
  assert all(substitute(v,mapping)==0 for _,v in meta['raw_rows'])
  assert not meta['residual_rows'] and not data['residual_rows'] and not old['residual_rows']
  sites=0
  for name,rows in old['maps'].items():
   before={(r,q):s.sympify(v) for r,q,v in rows};after={(r,q):s.sympify(v) for r,q,v in data['maps'][name]}
   for key in before.keys()|after.keys():
    assert substitute(before.get(key,0),mapping)==after.get(key,0)
    sites+=1
  full=set(s.symbols(' '.join(data['full_free_coordinates'])))
  assert all(s.sympify(v).free_symbols<=full for rows in data['maps'].values() for _,_,v in rows)
  assert all(r>meta['D_cut_inclusive'] for r,q,v in data['maps']['B2'])
  assert all(r>meta['C_cut_inclusive'] for r,q,v in data['maps']['A3'])
  records.append({'branch':branch,'version':version,'field':'Q','stage':8,
    'D_cut_inclusive':meta['D_cut_inclusive'],'C_cut_inclusive':meta['C_cut_inclusive'],
    'rational_pivots':len(mapping),'all_raw_rows_zero_after_map':True,
    'coefficient_sites_replayed':sites,'full_free_coordinates':len(full),
    'all_coordinate_images_in_declared_full_ring':True,
    'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
record={'status':'PASS','records':records,'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True))
