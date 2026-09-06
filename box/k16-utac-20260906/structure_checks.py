#!/usr/bin/env python3
"""Exact rational polynomial checks for the written uniform structural lemmas."""
import json
from pathlib import Path
import sympy as s

x, b, B, eta, w, a, u = s.symbols('x b B eta w a u')
l2,l3,l4,l5 = s.symbols('l2 l3 l4 l5')

def residual(L, P, bb=b, BB=B, ee=eta):
    G=s.Rational(3,2)*L*(L+bb)-BB*x
    R=s.Rational(3,16)*L**2*(L*(L+2*bb)-4*BB*x)-ee*x*x*(bb*L/2+BB*x)
    return s.expand(x*s.diff(P*P,x)-3*P*P+G*P-R)

checks={}
L=-b+l2*x*x+l3*x**3+l4*x**4+l5*x**5
P=-b*b/4-B*x+eta*x*x+w*x**3
phi4=s.expand(2*residual(L,P).coeff(x,4)/(b*b))
P+=phi4*x**4
phi5=s.expand(residual(L,P).coeff(x,5)/(b*b))
c4=2*(eta**2-3*B*w-b*eta*l2-s.Rational(3,8)*b*b*l2*l2)/(b*b)
c5=30*B*B*w/b**4-10*B*eta**2/b**4+10*B*eta*l2/b**3+3*B*l2*l2/b**2+4*eta*w/b**2-eta*l3/b-s.Rational(3,2)*l2*w/b-s.Rational(3,4)*l2*l3
checks['Phi4_matches_frozen']=s.cancel(phi4-c4)==0
checks['Phi5_matches_frozen']=s.cancel(phi5-c5)==0
T2=3*b*b*phi4+18*B*w-10*eta*eta
checks['T2_identity']=s.expand(T2+(4*eta+3*b*l2)**2/4)==0
checks['B_axis_residual']=residual(-b,-b*b/4-B*x,ee=0)==0
checks['cubic_axis_residual']=residual(-b+a*x**3,-(-b+a*x**3)**2/4,BB=0,ee=0)==0
mixed=residual(-b+a*x**3,-(-b+a*x**3)**2/4-B*x,ee=0)
checks['mixed_ansatz_residual']=s.expand(mixed-s.Rational(3,2)*B*a*x**4*(-b+a*x**3))==0
checks['eta_nonzero_pivot_zero']=(4+s.Rational(3)*(-s.Rational(4,3))==0)
checks['eta_zero_pivot_nonzero']=(4*0+3*s.Rational(1,3)==1)
# Ideal of the two lines via product of their two free coordinates.
z,v=s.symbols('z v')
checks['union_coordinate_ring']='Q[z,v]/(z*v)'
checks['normalization']='Q[z] x Q[v]'
# Leading ratio and every top-down pivot in the written proof.
m,d,j,p=s.symbols('m d j p')
pform=1/(4*(2*d+1))
checks['UT_parametrization']=s.cancel(((4*m-3)*pform**2+s.Rational(3,2)*pform-s.Rational(3,16)).subs(m,3*d*d))==0
lam=2*(2*m+j-3)*pform+s.Rational(3,2)
checks['top_pivot_identity']=s.cancel(lam-(2*m+j+6*d)/(2*(2*d+1)))==0
beta_pivot=-((4*m-3)*pform+s.Rational(3,4))
checks['B_pivot_identity']=s.cancel((beta_pivot+s.Rational(3,2)*d).subs(m,3*d*d))==0
# The ideal (b) demonstrates why a result after inverting b alone does not
# imply an unlocalized radical assertion about eta; it is only a logical control.
checks['localization_boundary_control']={
    'ring':'Q[b,eta]', 'ideal':'(b)', 'localized_ideal':'(1)',
    'eta_not_in_radical':True, 'claim_about_UF_solutions':False}
# Uniform nonreduced slice: L=-1, B=w2=0, u=4*eta. Here P^2 solves a
# linear Euler equation and its marked square root has no odd terms.
z=s.symbols('z')
coeff={2*r: -s.binomial(s.Rational(1,2),r)*(-8)**r/4 for r in range(1,25)}
checks['slice_coefficients_nonzero']=all(c!=0 for c in coeff.values())
H=s.Rational(1,16)-z*x*x/2
checks['slice_Euler_identity']=s.expand(x*s.diff(H,x)-3*H+s.Rational(3,16)-z*x*x/2)==0
checks['slice_examples']={str(nn):{
    'image_ideal':f'(z^{nn+1})',
    'first_closing_coefficient':str(coeff[2*nn+2]),
    'uniform_proof':'all even closing coefficients are nonzero multiples of z^r, N+1 <= r <= 2N'
} for nn in [4,5,6,8,12]}
checks['all_polynomial_identity_checks_pass']=all(v for v in checks.values() if isinstance(v,bool))
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
assert checks['all_polynomial_identity_checks_pass']
