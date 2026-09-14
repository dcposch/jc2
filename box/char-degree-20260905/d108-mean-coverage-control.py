#!/usr/bin/env python3
import hashlib,json,sys
from pathlib import Path
import sympy as s
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'d108'))
import rekill_engine_snapshot as E
mu,c,t,z,pi=s.symbols('mu c tt zz pi')
K=z**7*(1+z)**2+2*mu*t**4*z**4*(1+z)+(mu**2-c)*t**8*z
h3={(int(mt[0]),int(mt[1])):co for mt,co in s.Poly(K,t,z).terms()}
assert all(4*r+5*q>=35 and r+q<=9 for (r,q) in h3)
assert s.expand(K.subs(t,0)-z**7*(1+z)**2)==0
jet0,jet1,jet2=E.symbols_jet()
local=E.minor_local_rows(h3,8,True)
local0={(r,q):s.expand(co.subs({jet0:0,jet1:0,jet2:0})) for (r,q),co in local.items()}
assert all(co==0 for (r,q),co in local0.items() if r<8)
face=s.expand(sum(co*pi**q for (r,q),co in local0.items() if r==8))
assert s.expand(face+((pi-mu)**2-c))==0
assert face.coeff(pi,1)==2*mu
x,y=s.symbols('x y')
hphysical=(y-x)*((y*(y-x)**3+mu)**2-c)
assert s.expand(t**9*hphysical.subs({x:1/t,y:(1+z)/t})-K)==0
h2,hfree,hmeta=E.build_major_h2(E.SRC,h3,36,True)
assert hmeta['h2_D1_residual']==[]
out={'field':'Q','result':'PASS','engine_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest(),
 'physical_h3':str(hphysical),'normalized_h3':str(K),'all_source_h3_D2_floor_positions_valid':True,
 'strict_minor_jets':[0,0,0],'minor_face':str(face),'even_face_linear_residual':str(face.coeff(pi,1)),
 'major_h2_D1_residual':hmeta['h2_D1_residual'],'major_h2_D1_pivots':hmeta['h2_D1_pivots'],
 'coverage_conclusion':'source h3 support and compatible major h2 rows do not force at-level mean zero',
 'not_a_realized_Keller_pair':True,'not_a_full_necessary_chart_survivor':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
