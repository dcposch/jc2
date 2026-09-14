#!/usr/bin/env python3
"""Exact independent covariance and lifted-remainder identity controls."""
from pathlib import Path
import hashlib,json
import sympy as s
x,y,q=s.symbols('x y q');a,b,c,d,e=s.symbols('a b c d e')
F=y**3+2*x*y+x**2+3*y+5;G=y**2+x*y+7*x+11
def translate(f):return s.expand(f.subs({x:x+q,y:y+q},simultaneous=True))
def target(f,g):return g**3-f**2+a*g**2+b*f*g+c*f+d*g+e
T=s.expand(target(F,G));Tq=s.expand(target(translate(F),translate(G)))
assert s.expand(Tq-translate(T))==0
degree=s.Poly(T,x,y).total_degree()
def top(f,D):return s.Add(*(coeff*x**i*y**j for (i,j),coeff in s.Poly(f,x,y).terms() if i+j==D))
assert top(Tq,degree)==top(T,degree)
assert s.expand(translate(T).subs(q,-q).subs({x:x+q,y:y+q},simultaneous=True)-T)==0
H,v,U,R,p,qq=s.symbols('H v U R p qq')
V=s.Rational(3,8)*U
depressed=-2*V*H**3+(s.Rational(3,4)*v**2+p)*H**2-3*v*V*H+v**3-V**2+p*v+qq
lifted=(s.Rational(3,4)*R+p)*H**2-s.Rational(1,8)*v*U*H+v*R-s.Rational(9,64)*U**2+p*v+qq
certificate=s.expand(depressed-lifted)
assert s.expand(certificate-(v**2-U*H-R)*(s.Rational(3,4)*H**2+v))==0
record={'status':'PASS','field':'Q','all_five_target_coefficients_symbolically_retained':True,
 'diagonal_translation_target_covariance':True,'homogeneous_target_top_invariant':True,
 'translation_inverse':True,'lifted_remainder_identity':str(s.factor(certificate)),
 'lifted_identity_requires_graph_relation':'v^2-U*H-R=0',
 'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,sort_keys=True))
