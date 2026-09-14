#!/usr/bin/env python3
"""Exact local reduced-pattern differential identity controls; not global realization."""
import json
from pathlib import Path
import sympy as s
x=s.Symbol('pi');z6=x**6;z5=x**5;z7=x**7;z4=x**4
R=s.Rational
a=(3+s.sqrt(-3))/2;b=(3-s.sqrt(-3))/2
A=(7+s.sqrt(-35))/6;B=(A-7)/5
cases=[
 ('180_top',10,25,x**4*(z6-1),x*(z6-1)*(z6**3-R(3,2)*z6**2+R(3,8)*z6+R(1,16)),R(45,8)),
 ('180_small_23',5,4,x**2*(x-1)**3,x*(x-1)*(x**2-R(7,5)*x+R(7,25)),R(21,25)),
 ('180_large_112',20,16,(z5-a)*(z5-b)*(z5-1)**2,x*(z5-a)*(z5-b)*(z5-1),-60),
 ('180_large_13',20,16,(z5-A)*(z5-1)**3,x*(z5-A)*(z5-1)*(z5+B),20*B*A),
 ('192_top',10,15,x**3*(z7-1),x*(z7-1)*(z7-R(1,2)),-R(35,2)),
 ('192_small_13',4,3,x*(x-1)**3,x*(x-1)*(x-R(5,4)),R(5,4)),
 ('192_large_cube',12,9,(z4-1)**3,x*(z4-1)*(z4-R(5,4)),15),
]
out=[]
for name,P,Q,p,q,C in cases:
    p=s.Poly(s.expand(p),x,extension=True);q=s.Poly(s.expand(q),x,extension=True)
    residual=s.simplify(s.expand(P*p.as_expr()*s.diff(q.as_expr(),x)-Q*q.as_expr()*s.diff(p.as_expr(),x)-C*p.as_expr()))
    identity=(residual==0)
    sqfree=s.degree(s.gcd(q,q.diff()))==0
    includes=s.rem(q,p.sqf_part()).is_zero
    assert identity and sqfree and includes and s.simplify(C)!=0
    out.append({'name':name,'P':P,'Q':Q,'C':str(s.simplify(C)),'identity':identity,'q_squarefree':sqfree,'q_contains_p_roots':includes,'gcd_multiplicities':s.polys.polytools.sqf_list(p)[1][0][1] if len(s.polys.polytools.sqf_list(p)[1])==1 else 1})
print(json.dumps(out,indent=2))
Path('box/exact-contact-gate-20260906/closure-controls.json').write_text(json.dumps(out,indent=2)+'\n')
# Final-disc controls. The scalar multiples 60 and48 recover n,m weights.
f46=x*(x**3-1);g46=x**6-R(3,2)*x**3+R(3,8)
f69=x**6+x**4+R(5,8)*x*x+R(3,32)
g69=x*(x**8+R(3,2)*x**6+R(21,16)*x**4+R(35,64)*x*x+R(63,512))
b912=(6+s.sqrt(6))/18;c912=R(4,3);d912=R(2,9)+R(4,3)*b912;e912=-R(4,81)+R(4,9)*b912
f912=x*(z4*z4+z4+b912);g912=z4**3+c912*z4*z4+d912*z4+e912
final=[]
for name,n,m,f,g,C,A in [
 ('final_f4_g6',3,2,f46,g46,-R(9,8),3),
 ('final_f6_g9',3,2,f69,g69,-R(189,8192),2),
 ('final_f9_g12',4,3,f912,g912,4*b912*e912,4)]:
    residual=s.simplify(s.expand(n*g*s.diff(f,x)-m*f*s.diff(g,x)-C))
    assert residual==0 and s.simplify(C)!=0
    fp=s.Poly(f,x,extension=True);gp=s.Poly(g,x,extension=True)
    assert s.degree(s.gcd(fp,fp.diff()))==0 and s.degree(s.gcd(gp,gp.diff()))==0 and s.degree(s.gcd(fp,gp))==0
    assert all(k[0]%A in [fp.degree()%A] for k,v in fp.terms())
    assert all(k[0]%A in [gp.degree()%A] for k,v in gp.terms())
    final.append({'name':name,'C':str(s.simplify(C)),'identity':True,'squarefree_and_coprime':True,'Galois_A':A,'Galois_law':True})
Path('box/exact-contact-gate-20260906/closure-controls.json').write_text(json.dumps({'upper':out,'final':final},indent=2)+'\n')
print(json.dumps(final,indent=2))
