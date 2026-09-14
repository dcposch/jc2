#!/usr/bin/env python3
"""Independent exact-Q audit of root driver's identities and monic division."""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import sympy as s

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'g9966/source'
sys.path.insert(0,str(SOURCE))
import engine as E

H,A,B,C,D,a,b,c,d,e=s.symbols('H A B C D a b c d e')
F=H**3+A*H+B
G=H**2+C*H+D
original=G**3-F**2+a*G**2+b*F*G+c*F+d*G+e
after=s.expand(original.subs({b:-3*C,A:(3*D+a)/2},simultaneous=True))
L3=-2*B+C**3-3*C*D/2+C*a/2+c
L2=-3*B*C-3*C**2*D/2-C**2*a/2+3*D**2/4+D*a/2-a**2/4+d
L1=-3*B*C**2-3*B*D-B*a-3*C*D**2/2+C*D*a/2+C*d+3*D*c/2+a*c/2
L0=-B**2-3*B*C*D+B*c+D**3+D**2*a+D*d+e
assert s.expand(after-(L3*H**3+L2*H**2+L1*H+L0))==0
assert s.Poly(s.expand(original),H).nth(5)==3*C+b
assert s.expand(s.Poly(s.expand(original),H).nth(4).subs(b,-3*C))==3*D-2*A+a

checks=[]
for stage in range(8):
    outer,free,meta=E.outer_state(stage)
    ta,tb=s.symbols('ta tb')
    pre={v:s.Integer(0) for v in free if str(v).startswith('B1c_')}
    pre[s.Symbol('B1c_32_0')]=-tb/3
    for v in free:
        if str(v).startswith('A2c_'):
            pre[v]=s.Rational(3,2)*s.Symbol(str(v).replace('A2c_','B2c_'))
    pre[s.Symbol('A2c_65_0')]+=ta/2
    changed={name:{p:E.substitute_map(v,pre) for p,v in poly.items()} for name,poly in outer.items()}
    assert all(s.expand(changed['A2'].get(p,0)-s.Rational(3,2)*changed['B2'].get(p,0)
                        -(ta/2 if p==(65,0) else 0))==0 for p in set(changed['A2'])|set(changed['B2']))
    assert all(s.expand(v-(-tb/3 if p==(32,0) else 0))==0 for p,v in changed['B1'].items())
    actual=set().union(*(v.free_symbols for poly in changed.values() for v in poly.values()))
    declared=(free-set(pre))|{ta,tb}
    assert actual<=declared,actual-declared
    checks.append({'stage':stage,'remaining_declared_outer':len(declared),
                   'premap_count':len(pre),'unbound_symbols':0,
                   'A2_B2_identity':True,'B1_constant_identity':True})

# Prove the proposed H-adic alternative with a symbolic monic H of degree 3,
# coefficient polynomials of maximum allowed degree, and all target scalars.
# The H-power identity is formal, so the degree-three check is a dense
# control of the independent implementation, not the logical proof itself.
y,x=s.symbols('y x')
hp=y**3+(x+1)*y**2+(x*x-2)*y+x+3
bp=(x+2)*y*y+(x*x-1)*y+2
dp=(2*x-1)*y*y+(x+4)*y+x*x
actual_L=[s.Poly(s.expand(v.subs({B:bp,D:dp})),y) for v in (L3,L2,L1,L0)]
hpoly=s.Poly(hp,y)
u2,v2=s.div(actual_L[1],hpoly)
u1,v1=s.div(actual_L[2],hpoly)
u0,v0=s.div(actual_L[3],hpoly)
u00,v00=s.div(u0,hpoly)
R3=actual_L[0]+u2;R2=v2+u1+u00;R1=v1+v00;R0=v0
assert all(p.degree()<3 for p in (R3,R2,R1,R0))
direct=s.expand(sum(p.as_expr()*hp**power for p,power in zip(actual_L,(3,2,1,0))))
adic=s.expand(sum(p.as_expr()*hp**power for p,power in zip((R3,R2,R1,R0),(3,2,1,0))))
assert s.expand(direct-adic)==0

# The leading coefficient extraction after reducing R3,R2 and the high part
# of R1 is the scalar coefficient of y^(d-h) in R1, without subtracting an
# incorrect zero target.
leader=s.Symbol('lambda')
control=s.expand((leader*y**2+x*y+7)*hp+(x*x*y*y+1))
assert s.degree(control,y)==5 and control.coeff(y,5)==leader

record={'field':'Q','premap_coefficient_identity':True,'L3_L2_L1_L0_identity':True,
        'outer_maps_all_finite_offsets':checks,
        'physical_map':'(r,q) -> x^(D-r-q)*(y-x)^q',
        'H_adic_control':{'dense_symbolic_degree':3,'divisor_leader':'1',
                           'division_identity':True,'remainder_y_degree_less_than_H':True,
                           'lambda_target_control':True,
                           'general_33_rule':'R3=R2=0; deg_y R1<=22; [y^22]R1 scalar unit'},
        'driver_sha256':hashlib.sha256((HERE.parent/'g9966/run_characteristic.py').read_bytes()).hexdigest(),
        'self_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'g9966_driver_control.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True))
