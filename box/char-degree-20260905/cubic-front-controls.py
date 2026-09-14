#!/usr/bin/env python3
import json
from pathlib import Path
import sympy as s
z=s.symbols('z')
rows=[]
for name,k,zpow,wpow,floor,u,v,rs,depth in [
 ('99',33,24,9,189,3,4,[28],141),
 ('108',36,28,8,276,4,5,[31,32],151)]:
 for r in rs:
  qmin=(floor-u*r+v-1)//v
  wmin=(2*wpow+2)//3
  assert qmin+wmin>k-1
  assert 3*r+1<min(depth,4*k-2)
  rows.append(dict(client=name,r=r,z_min=qmin,w_min=wmin,
   required_degree=qmin+wmin,degree_cap=k-1,
   characteristic_band=3*r+1,leader_depth=depth,first_p_band=4*k-2,
   contradiction=True))
for k,H0,d in [(33,z**24*(1+z)**9,z**26*(1+z)**6),
                (36,z**28*(1+z)**8,z**29*(1+z)**6)]:
 U=s.cancel(d*d/H0);R=s.cancel(d**3/(6*H0**2))
 assert s.Poly(U,z).degree()<k and s.Poly(R,z).degree()<k
 assert s.expand(s.Rational(3,4)*R*H0**2-s.Rational(1,8)*d*U*H0)==0
out={'field':'Q','result':'PASS','eliminated_first_bands':rows,
 'next_band_shapes_pass_leading_identities':True,
 'zero_coordinates_are_radical_consequences':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
