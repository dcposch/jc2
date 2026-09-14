#!/usr/bin/env python3
"""Exact monic-quotient controls including both separated conjugate components."""
import argparse,hashlib,importlib.util,json
from pathlib import Path
import sympy as sp
ap=argparse.ArgumentParser();ap.add_argument('--helper',type=Path,required=True);ap.add_argument('--raw-helper',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
def module(path):
 spec=importlib.util.spec_from_file_location(path.stem,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
nfmod=module(args.helper);rawmod=module(args.raw_helper)
d,e,a,b=sp.symbols('delta epsilon a b');q=d*d+d*e*e-2*e**4
quotient={'d':str(d),'e':str(e),'a':'-1','b':'-2','polynomial':str(q)}
S={'h3_degree':2,'inner_power':3,'k2_degree':6,'n':18,'m':12,'outer_power_F':3,'outer_power_G':2}
h={(0,1):sp.Integer(1),(1,0):d+sp.Rational(2,3)*e,(2,0):a+d**3}
c2={(1,1):b+e*e,(2,0):d*d};c3={(2,1):d**3-a*e**4}
outer={name:{(1,0):sp.Rational(i+1,7)+d,(2,1):e+i*a,(3,0):d**(i+2)+b} for i,name in enumerate(['A2','A3','B1','B2'])}
raw,_=rawmod.jacobian_bands(h,c2,c3,outer,8,S,first_band=0)
got,meta=nfmod.jacobian_bands(h,c2,c3,outer,8,S,first_band=0,quotient=quotient)
checks=[]
for t in range(9):
 for k in set(raw[t])|set(got[t]):
  original=raw[t].get(k,sp.Integer(0));image=got[t].get(k,sp.Integer(0))
  expected=sp.Poly(original,d).rem(sp.Poly(q,d)).as_expr()
  assert sp.expand(image-expected)==0
  assert sp.Poly(image,d).degree()<=1
  assert sp.Poly(original-image,d).rem(sp.Poly(q,d)).is_zero
  for root in (e*e,-2*e*e):assert sp.expand((original-image).subs(d,root))==0
 checks.append({'t':t,'coefficient_slots':len(set(raw[t])|set(got[t]))})
# A linear remainder may vanish on one component and fail on the other.
# It must be retained as one polynomial, never split into its two coefficients.
linear=d-e*e
assert linear.subs({d:1,e:1})==0 and linear.subs({d:-2,e:1})==-3
assert sp.groebner([q,linear],d,e).polys[0].as_expr()!=1
negative=[]
for bad in (sp.sqrt(2),1/d,sp.sin(d)):
 try:nfmod.jacobian_band({(0,1):bad},c2,c3,outer,2,S,quotient=quotient)
 except (AssertionError,TypeError):negative.append(str(bad))
 else:raise AssertionError('invalid coefficient accepted '+str(bad))
result={'status':'PASS','independent_monic_polynomial_remainder_match':True,'both_components_preserved':True,
        'linear_remainder_not_split':str(linear),'checks':checks,'negative_controls':negative,'backend_metadata':meta,
        'helper_sha256':hashlib.sha256(args.helper.read_bytes()).hexdigest(),'oracle':'SymPy monic division in delta; exact evaluation at both delta=epsilon² and delta=-2epsilon²'}
args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print('MONIC QUOTIENT CONTROL PASS',flush=True)
