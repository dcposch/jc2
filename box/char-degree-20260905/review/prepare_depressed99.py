#!/usr/bin/env python3
"""Exact polynomial coordinate change; retain all five target scalars."""
import argparse,hashlib,json,sys,time
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent;N=HERE.parent
sys.path.insert(0,str(N/'g9966'/'source'));import engine as E

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,required=True)
 ap.add_argument('--out',type=Path,required=True);a0=ap.parse_args();a0.out.mkdir(parents=True,exist_ok=True)
 started=time.monotonic();args=json.loads(a0.input.read_text());assert args['k']==33 and args['target']==55
 cp=Path(args['source_coordinate_input']['path']);data=json.loads(cp.read_text())
 assert hashlib.sha256(cp.read_bytes()).hexdigest()==args['source_coordinate_input']['sha256']
 assert data['branch']=='delta52' and data['stage']==8 and data['residual_rows']==[]
 maps={n:{(r,q):s.sympify(v) for r,q,v in tab} for n,tab in data['maps'].items()}
 a,b,c,d,e=s.symbols('target_a target_b target_c target_d target_e')
 A=a/3+b*b/18;B=a*b/12+b**3/54-c/2;aa=a+b*b/4
 constants=[('C3',(33,0),s.Symbol('C3c_33_0')),('B2',(65,0),s.Symbol('B2c_65_0')),('A3',(98,0),s.Symbol('A3c_98_0'))]
 for n,pos,var in constants:
  assert maps[n][pos]==var
  assert [(m,site) for m,tab in maps.items() for site,expr in tab.items() if var in expr.free_symbols]==[(n,pos)]
 Cvars=set().union(*(v.free_symbols for v in maps['A3'].values()))
 assert all(str(v).startswith('A3c_') for v in Cvars)
 for value in maps['A3'].values():
  poly=s.Poly(value,*sorted(Cvars,key=str),domain=s.QQ)
  assert poly.total_degree()==1 and poly.coeff_monomial(1)==0
 renamed={v:s.Symbol('old__'+str(v)) for v in Cvars};oldvars=set(renamed.values())
 shift={(r+33,q):b*v/4 for (r,q),v in maps['B2'].items()}
 shift[(98,0)]=s.expand(shift.get((98,0),0)-B-b*A/4)
 rows=[]
 for pos in sorted(set(maps['A3'])|set(shift)):
  base=maps['A3'].get(pos,s.S.Zero)
  rows.append((f'A3_basis_transport_{pos[0]}_{pos[1]}',base.subs(renamed,simultaneous=True)-base-shift.get(pos,0)))
 residue,solved,pivots,zero=E.qstar_reduce(rows,oldvars);solved=E.resolve_map(solved)
 assert not residue and set(solved)==oldvars
 assert all(s.sympify(p.coefficient).is_Rational and p.coefficient!=0 for p in pivots)
 assert all(E.substitute_map(expr,solved)==0 for _,expr in rows)
 forward={v:solved[renamed[v]] for v in Cvars}
 forward.update({s.Symbol('C3c_33_0'):s.Symbol('C3c_33_0')+b/6,
  s.Symbol('B2c_65_0'):s.Symbol('B2c_65_0')-A,
  d:d-b*c/2+aa*aa/3,e:e-c*c/4+aa*d/3+aa**3/27})
 forward={v:s.expand(expr) for v,expr in forward.items() if s.expand(expr-v)!=0}
 inverse={s.Symbol('C3c_33_0'):s.Symbol('C3c_33_0')-b/6,
  s.Symbol('B2c_65_0'):s.Symbol('B2c_65_0')+A,
  d:d+b*c/2-aa*aa/3,e:e+c*c/4-aa*(d+b*c/2)/3+2*aa**3/27}
 # A3 free coordinates have unit own-position images. Read those actual sites;
 # matching the variable suffix would not establish their ring map.
 pivot_positions={}
 for var in Cvars:
  sites=[pos for pos,value in maps['A3'].items() if value==var]
  assert len(sites)==1,(var,sites);pos=sites[0];pivot_positions[str(var)]=pos
  inverse[var]=var-b*maps['B2'].get((pos[0]-33,pos[1]),0)/4+(B if pos==(98,0) else 0)
 inverse={v:s.expand(expr) for v,expr in inverse.items() if s.expand(expr-v)!=0}
 subst=lambda expr,mp:s.expand(s.sympify(expr).subs(mp,simultaneous=True))
 full=set(s.symbols(' '.join(args['names'])))
 assert all(expr.free_symbols<=full for mp in [forward,inverse] for expr in mp.values())
 for var in full:
  assert subst(forward.get(var,var),inverse)==var,('forward_inverse',var)
  assert subst(inverse.get(var,var),forward)==var,('inverse_forward',var)
 image_sites=0
 for name,tab in maps.items():
  for pos,value in tab.items():
   expected=value
   if name=='C3' and pos==(33,0):expected+=b/6
   elif name=='B2' and pos==(65,0):expected-=A
   elif name=='A3':expected+=shift.get(pos,0)
   assert subst(value,forward)==s.expand(expected),(name,pos)
   assert subst(subst(value,forward),inverse)==value
   image_sites+=1
 assert set(shift)<=set(maps['A3'])
 # The same represented spaces, now in new coordinates, are precisely H,v,V.
 assert all(r>30 for r,q in maps['B2']) and all(r>62 for r,q in maps['A3'])
 rawd=d-b*c/2+aa*aa/3;rawe=e-c*c/4+aa*d/3+aa**3/27
 assert s.expand(rawd+b*c/2-aa*aa/3-d)==0
 assert s.expand(rawe+c*c/4-aa*(rawd+b*c/2)/3+2*aa**3/27-e)==0
 record={'status':'PASS','field':'Q','type':'POLYNOMIAL_RING_ISOMORPHISM_NOT_GAUGE',
  'branch':data['branch'],'stage':data['stage'],'input':str(a0.input),
  'input_sha256':hashlib.sha256(a0.input.read_bytes()).hexdigest(),
  'source_coordinates':str(cp),'source_coordinates_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),
  'source_engine_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
  'generator_order_old':args['names'],'generator_order_new':args['names'],
  'unlisted_generator_images':'identity','old_generator_images_in_new_ring':{str(v):str(x) for v,x in forward.items()},
  'new_generator_images_in_old_ring':{str(v):str(x) for v,x in inverse.items()},
  'all_generator_roundtrips_both_directions':True,'all_source_images_forward_and_inverse_checked':image_sites,
  'constant_coordinates_each_have_one_actual_occurrence':True,
  'A3_basis_Qstar_pivots':[{'row':p.label,'variable':str(p.variable),'leader':str(p.coefficient)} for p in pivots],
  'A3_basis_raw_rows':[(label,str(expr)) for label,expr in rows],
  'A3_basis_map':{str(v):str(x) for v,x in solved.items()},'A3_basis_residuals':[],
  'A3_actual_unit_position_map':pivot_positions,
  'finite_residuals_before':[],'finite_residuals_after':[],
  'strong_front_preserved':{'D_cut_inclusive':30,'C_cut_inclusive':62,'bD_first_band':64},
  'raw_target_d_in_new_ring':str(s.expand(rawd)),'raw_target_e_in_new_ring':str(s.expand(rawe)),
  'all_five_target_coefficients_retained':True,'a_b_c_retained_as_unused_coordinates':True,
  'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  'elapsed_seconds':round(time.monotonic()-started,3)}
 proof=a0.out/'coordinate-isomorphism.json';proof.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
 args['depressed_coordinates']=True
 args['depressed_coordinate_receipt']={'path':str(proof),'sha256':hashlib.sha256(proof.read_bytes()).hexdigest()}
 args['coordinate_semantics']='h_expr,D_expr,C_expr now denote H,v,V; target_d,target_e now denote p,q; all original generators recover by the explicit inverse ring map'
 output=a0.out/'depressed.input.json';output.write_text(json.dumps(args,indent=2,sort_keys=True)+'\n')
 print('DEPRESSED99_PASS',len(pivots),len(forward),image_sites,'seconds',round(time.monotonic()-started,3),flush=True)

if __name__=='__main__':main()
