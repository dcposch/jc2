from fractions import Fraction as Q
from math import gcd, lcm
import json
import sympy as s
n=99
M={1:-66,2:77,3:97}
d={1:99,2:33,3:11,4:1}
V={2:8,3:8,4:1}
delta={}
for i in [1,2,3]:
    num=Q(n-M[i]); den=Q(n-M[3]-1)
    for j in range(i+1,4):
        num*=V[j]*(n-M[j])-d[j]
        den*=V[j]*(n-M[j-1])-d[j]
    delta[i]=1-num/den
L={i:lcm(*(delta[j].denominator for j in range(i+1,4))) for i in [1,2]}
A={i:(L[i]*delta[i]).denominator for i in [1,2]}
assert delta=={1:Q(4,9),2:Q(1,3),3:Q(-1)}
assert L=={1:3,2:1} and A=={1:3,2:3}
lo=[(r,q) for r in range(1,12) for q in range(12-r)]
counts={k:len([rq for rq in lo if (3*rq[0]+4*rq[1]<32 if k=='below' else 3*rq[0]+4*rq[1]==32 if k=='equal' else 3*rq[0]+4*rq[1]>32)]) for k in ['below','equal','above']}
assert counts=={'below':43,'equal':2,'above':21}
p,a,b,beta,U=s.symbols('pi a b beta U')
P=p**8+a*p**5+b*p**2
Q2=(p**3-beta)**8
coeff21=s.expand(Q2-P**3).coeff(p,21)
assert coeff21==-3*a-8*beta
# At the C2 floor ord_t C2>=-2/3, t^22 C2 has s-weight>=64.
# Because deg_y C2<=10, degree_pi of its s-weight64 face <=10.
# Thus C2face*P has pi-degree<=18, C3face has pi-degree<=10.
payload={
 'delta_y':{str(k):str(v) for k,v in delta.items()},
 'L':L,'A':A,'D2_g_root_count':n//d[3]*V[3],
 'D1_g_root_count':n//d[2]*V[2],
 'D2_z_radius':str(1+delta[2]),'D1_z_radius':str(1+delta[1]),
 'h3_order_t':str(8*delta[2]+3*delta[3]),
 'K3_s_weight':str(3*(11+8*delta[2]+3*delta[3])),
 'h3_ambient_counts':counts,'h3_equality_slots':[list(rq) for rq in lo if 3*rq[0]+4*rq[1]==32],
 'K2_face':str(Q2),'K2_pi21':str(s.expand(Q2).coeff(p,21)),
 'K3_face_general':str(P),'K3cube_pi21':str(s.expand(P**3).coeff(p,21)),
 'face_constraint_pi21':str(coeff21), 'forced_a':str(-s.Rational(8,3)*beta),
 'C2_face_sites':[[r,q] for r in range(1,23) for q in range(11) if r+q<=22 and 3*r+4*q==64],
 'C3_face_sites':[[r,q] for r in range(1,34) for q in range(11) if r+q<=33 and 3*r+4*q==96],
 'strict33_compatible_with_source_C2floor_and_beta_nonzero':False
}
print(json.dumps(payload,indent=2))
