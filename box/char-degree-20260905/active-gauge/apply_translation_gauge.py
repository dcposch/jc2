#!/usr/bin/env python3
"""Audited global residual diagonal-translation slice, after source derivation.

No chart coefficient is guessed: apply the ring map jet0 -> 0 to every
coefficient image and residual, retaining all other free coordinates.
"""
import argparse,hashlib,json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[3]
PROOFS=[
 'box/g9966-corrected-20260905/translation-proof.md',
 'box/g9966-corrected-20260905/minor_gauge-final-audit.md',
 'box/g9966-corrected-20260905/translation-controls.json',
 'box/g9966-corrected-20260905/minor_gauge-transport-controls.json',
]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True)
 ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
 data=json.loads(a.input.read_text());assert 'jet0' in data['full_free_coordinates']
 before=list(data['full_free_coordinates']);j=sp.Symbol('jet0')
 def image(v):return sp.expand(sp.sympify(v).subs(j,0))
 changes=[]
 for name,rows in data['maps'].items():
  new=[]
  for r,q,v in rows:
   v0=image(v)
   if str(v0)!=v:changes.append([name,r,q,v,str(v0)])
   if v0!=0:new.append([r,q,str(v0)])
  data['maps'][name]=new
 data['residual_rows']=[[label,str(v0)] for label,v in data['residual_rows'] if (v0:=image(v))!=0]
 data['full_free_coordinates']=[name for name in before if name!='jet0']
 assert set(before)-set(data['full_free_coordinates'])=={'jet0'}
 assert all(j not in sp.sympify(v).free_symbols for rows in data['maps'].values() for _,_,v in rows)
 assert all(j not in sp.sympify(v).free_symbols for _,v in data['residual_rows'])
 proof_files=[{'path':p,'sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in PROOFS]
 for p in PROOFS[2:]:assert json.loads((ROOT/p).read_text())['status']=='PASS'
 data['source_gauge']={
  'type':'PROVED_GLOBAL_ORBIT_SLICE',
  'parent_input':str(a.input),'parent_input_sha256':hashlib.sha256(a.input.read_bytes()).hexdigest(),
  'ring_map':{'jet0':'0'},'all_other_free_generator_images':'identity',
  'group_spend':'Residual diagonal source translation only; major ordinary centre already fixed',
  'source_action':'Q_q(x,y)=Q(x+q,y+q)',
  'slice_isomorphism':'p -> (T_jet0(p),jet0); inverse (p0,j) -> T_(-j)(p0)',
  'minor_action':{'jet0':'jet0-q','u':'u','minor_a2' if data['branch']=='delta2' else 'v':('minor_a2' if data['branch']=='delta2' else 'v')+'-q*u','rho_or_c':'unchanged'},
  'characteristic_extension':'All five target scalars and leader are unchanged by source translation; full Q composition commutes; total degree bound and homogeneous top face are preserved. Thus the full augmented characteristic ideal is invariant.',
  'front_extension':'Diagonal translation increases t order and preserves z degree, so the already proved front cuts are preserved.',
  'retained_free_coordinates':data['full_free_coordinates'],
  'removed_coordinates':['jet0'],'dimension_adjustment_for_free_centre':1,
  'source_proofs':proof_files,'map_changes':changes,
  'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 }
 a.output.parent.mkdir(parents=True,exist_ok=True)
 a.output.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
 print(data['branch'],data['stage'],'GAUGE',len(before),'->',len(data['full_free_coordinates']),'map changes',len(changes))

if __name__=='__main__':main()
