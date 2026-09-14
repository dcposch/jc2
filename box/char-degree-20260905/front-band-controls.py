#!/usr/bin/env python3
"""Read-only frozen-map checks and exact leading-band division controls."""
import hashlib, importlib.util, json, sys
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
OUT={}
cases=[('9966','box/g9966-corrected-20260905/engine.py',33,3,4,189,285,27),
       ('10872','box/d108-rekill-20260905/work/rekill_engine.py',36,4,5,276,416,30)]
z,tau=sp.symbols('z tau')
for tag,rel,k,wt,wz,dfloor,cfloor,cutoff in cases:
 path=ROOT/rel
 spec=importlib.util.spec_from_file_location('front_audit_'+tag,path)
 E=importlib.util.module_from_spec(spec);sys.modules[spec.name]=E;spec.loader.exec_module(E)
 if tag=='9966':
  blocks,free,meta=E.outer_state(0);specs=E.S['outer_specs']
  specfloors={b:v[1] for b,v in specs.items()}
 else:
  blocks,free,meta=E.outer_state(E.SRC,0)
  specfloors={b:v['W0'] for b,v in meta['specs'].items()}
 all_eq=[]
 for b,pol in blocks.items():
  all_eq.extend([(b,r,q,str(v)) for (r,q),v in pol.items()
                if wt*r+wz*q==specfloors[b] and v!=0])
 assert all_eq==[]
 qcap=k-1
 def allowed(r,floor):
  return [q for q in range(qcap+1) if wt*r+wz*q>=floor]
 dmin=next(r for r in range(2*k) if allowed(r,dfloor))
 cmin=next(r for r in range(3*k) if allowed(r,cfloor))
 mappedmins={b:min(r for (r,q),v in blocks[b].items() if v!=0) for b in ['A3','B2']}
 H0=z**(24 if k==33 else 28)*(1+z)**(9 if k==33 else 8)
 degmax=2*qcap-k
 table=[]
 for r in range(dmin,cutoff+1):
  table.append({'r':r,'D_allowed_q':allowed(r,dfloor),
     'C_index':2*r+1,'C_allowed_q':allowed(2*r+1,cfloor),
     'quotient_degree_bound':degmax,'bD_start':r+k,
     'bD_strictly_later':r+k>2*r+1})
 assert all(row['bD_strictly_later'] for row in table)
 if k==33:
  form=tau*z**27*(1+z)**5
  quo,rem=sp.div(sp.expand(form**2),sp.expand(H0),z)
  assert rem==0 and sp.expand(quo-tau**2*z**30*(1+z))==0
  corner=blocks['B2'].get((27,27),sp.Integer(0))
  assert corner==0
  neg={'omitting_corner_would_allow_front':str(form),
       'corner_coefficient':str(sp.expand(form).coeff(z,27)),
       'exact_quotient':str(quo),'exact_remainder':str(rem),
       'quotient_fits_C55_floor':all(wt*55+wz*q>=cfloor for (q,),v in sp.Poly(quo,z).terms())}
 else:
  form=tau*z**31*(1+z)**4
  quo,rem=sp.div(sp.expand(form**2),sp.expand(H0),z)
  assert rem==0 and sp.expand(quo-tau**2*z**34)==0
  neg={'r31_must_not_be_blanket_zero':str(form),'exact_quotient':str(quo),
       'exact_remainder':str(rem),'C63_nonzero_image':str(blocks['A3'].get((63,34),0)),
       'source_floor_of_C63_z34':wt*63+wz*34,
       'fits_source_floor':wt*63+wz*34>=cfloor}
 OUT[tag]={'engine':rel,'engine_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
   'source_qcap':qcap,'D_floor':dfloor,'C_floor':cfloor,
   'D_ambient_min_r':dmin,'C_ambient_min_r':cmin,
   'source_stage0_mapped_min_r':mappedmins,'all_D2_equality_images_zero':True,
   'front_rows':table,'proved_D_cutoff':cutoff,
   'proved_C_cutoff':2*(cutoff+1),'quotient_front_after_cutoff':2*(cutoff+1)+1,
   'negative_control':neg}
outpath=HERE/'front-band-controls.json'
outpath.write_text(json.dumps(OUT,indent=2)+'\n')
print(outpath)
