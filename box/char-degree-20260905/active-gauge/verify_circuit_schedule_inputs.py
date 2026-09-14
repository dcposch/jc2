#!/usr/bin/env python3
"""Independent replay of all18 gauge maps, rational graphs, and API images."""
from pathlib import Path
import argparse,hashlib,json,sys
import sympy as s
HERE=Path(__file__).resolve().parent
from active_ring_backend import from_g9966_input

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--directory',type=Path,required=True);a=ap.parse_args()
 prepared=json.loads((a.directory/'preparation.json').read_text());records=[];jet=s.Symbol('jet0')
 assert {(r['branch'],r['stage']) for r in prepared['records']}=={(b,j) for b in ['delta2','delta52'] for j in range(9)}
 for rec in prepared['records']:
  branch,stage=rec['branch'],rec['stage'];tag=f'{branch}_stage{stage}'
  path=Path(rec['coordinate_path']);data=json.loads(path.read_text());meta=data['stronger_characteristic_front']
  gaugepath=Path(meta['parent_input']);gauge=json.loads(gaugepath.read_text())
  originalpath=Path(gauge['source_gauge']['parent_input']);original=json.loads(originalpath.read_text())
  assert data['branch']==gauge['branch']==original['branch']==branch
  assert data['stage']==gauge['stage']==original['stage']==stage
  assert hashlib.sha256(path.read_bytes()).hexdigest()==rec['coordinate_sha256']
  assert hashlib.sha256(gaugepath.read_bytes()).hexdigest()==meta['parent_input_sha256']
  assert hashlib.sha256(originalpath.read_bytes()).hexdigest()==gauge['source_gauge']['parent_input_sha256']
  assert set(original['full_free_coordinates'])-set(gauge['full_free_coordinates'])=={'jet0'}
  assert set(gauge['full_free_coordinates'])<=set(original['full_free_coordinates'])
  mapping={s.Symbol(k):s.sympify(v) for k,v in meta['map'].items()}
  assert all(s.sympify(p['leader']).is_Rational and s.sympify(p['leader'])!=0 for p in meta['Qstar_pivots'])
  assert set(map(str,mapping))==set(gauge['full_free_coordinates'])-set(data['full_free_coordinates'])
  assert set(data['full_free_coordinates'])<=set(gauge['full_free_coordinates'])
  assert not any(set(mapping)&v.free_symbols for v in mapping.values())
  def graph(v):return s.expand(s.sympify(v).subs(mapping,simultaneous=True))
  assert all(graph(v)==0 for _,v in meta['raw_rows'])
  assert not meta['residual_rows'] and not data['residual_rows'] and not gauge['residual_rows'] and not original['residual_rows']
  sites=0
  for name,rows in original['maps'].items():
   origin={(r,q):s.sympify(v) for r,q,v in rows}
   middle={(r,q):s.sympify(v) for r,q,v in gauge['maps'][name]}
   final={(r,q):s.sympify(v) for r,q,v in data['maps'][name]}
   for key in origin.keys()|middle.keys()|final.keys():
    assert s.expand(origin.get(key,s.S.Zero).subs(jet,0)-middle.get(key,0))==0
    assert s.expand(graph(middle.get(key,0))-final.get(key,0))==0
    sites+=1
  full=set(s.symbols(' '.join(data['full_free_coordinates'])))
  assert all(s.sympify(v).free_symbols<=full for rows in data['maps'].values() for _,_,v in rows)
  expectedcut=(29,60) if stage==0 else (30,62)
  assert (meta['D_cut_inclusive'],meta['C_cut_inclusive'])==expectedcut
  assert all(r>expectedcut[0] for r,q,v in data['maps']['B2'])
  assert all(r>expectedcut[1] for r,q,v in data['maps']['A3'])
  argsfile=Path(rec['input_path']);args=json.loads(argsfile.read_text());rebuilt=from_g9966_input(path)
  assert {k:v for k,v in args.items() if k!='source_coordinate_input'}==json.loads(json.dumps(rebuilt))
  assert hashlib.sha256(argsfile.read_bytes()).hexdigest()==rec['input_sha256']
  assert args['source_coordinate_input']['sha256']==rec['coordinate_sha256']
  assert len(args['names'])==len(set(args['names'])) and 'jet0' not in args['names']
  assert {'target_'+q for q in 'abcde'}|{'leader55','Z55'}<=set(args['names'])
  records.append(dict(rec,all_gauge_and_graph_images_replayed=True,coefficient_sites_checked=sites,
      all_raw_rows_checked=True,all_five_targets_and_source_coordinates_retained=True))
  print('VERIFIED',tag,sites,flush=True)
 result={'status':'PASS','field':'Q','records':records,
   'preparation_sha256':hashlib.sha256((a.directory/'preparation.json').read_bytes()).hexdigest(),
   'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
 (a.directory/'verification.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')

if __name__=='__main__':main()
