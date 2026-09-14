#!/usr/bin/env python3
"""(i) weighted tangent cone of Q_P at (0,-b): Q_P(x,-b+ell) = (3/8) b^2 ell^2 + b eta x^2 ell + kappa x^4 + (wt>4),
       wt(x)=1, wt(ell)=2, kappa = (b^2/2) P_4 + 3 B w2 - eta^2;  its ell-discriminant is b^2 x^4 Lpivot^2/16.
   (ii) P = -L^2/4 (so B=0, eta = b l_2/2 forced by the jets): (UF) <=> L^2 (x L' - 3(L+b)) = -2 eta b x^2, hence
        deg forces N=3, l_2=0, eta=0: the exceptional t=2 family and nothing else."""
import sympy as sp, json
x,b,B,eta,w2,ell,P4 = sp.symbols('x b B eta w2 ell P4')
l2,l3 = sp.symbols('l2 l3')
out={}
# (i)
Lv=sp.Symbol('Lv')
P = -b**2/4 - B*x + eta*x**2 + w2*x**3 + P4*x**4
Q = sp.expand(sp.Rational(3,16)*Lv**2*(Lv*(Lv+2*b)-4*B*x) - eta*x**2*(b*Lv/2+B*x) - (sp.Rational(3,2)*Lv*(Lv+b)-B*x)*P - (x*sp.diff(P**2,x)-3*P**2))
Qe = sp.expand(Q.subs(Lv,-b+ell))
# keep weighted degree <= 4 terms (wt x=1, wt ell=2)
poly = sp.Poly(Qe, x, ell)
low = sum(c*x**i*ell**j for (i,j),c in poly.terms() if i+2*j<=4)
kappa = sp.expand(b**2*P4/2 + 3*B*w2 - eta**2)
target = sp.Rational(3,8)*b**2*ell**2 + b*eta*x**2*ell + kappa*x**4
out['tangent_cone_wt4_matches'] = bool(sp.simplify(sp.expand(low-target))==0)
out['tangent_cone_lower_wt_terms_vanish'] = bool(all(c==0 for (i,j),c in poly.terms() if i+2*j<4))
# discriminant in ell of the weighted form, with kappa from row 4: kappa = -b eta l2 - (3/8) b^2 l2^2
kap_row4 = -b*eta*l2 - sp.Rational(3,8)*b**2*l2**2
disc = sp.factor(sp.expand((b*eta*x**2)**2 - 4*sp.Rational(3,8)*b**2*kap_row4*x**4))
out['tangent_cone_discriminant'] = str(disc)
out['disc_equals_b2x4Lpivot2/16'] = bool(sp.simplify(disc - b**2*x**4*(4*eta+3*b*l2)**2/16)==0)
# (ii)
Lf = sp.Function('L')(x)
Pf = -Lf**2/4
etaf = sp.Symbol('eta_f')   # keep eta free; B = 0 forced by P_1 = 0
UF = sp.expand(x*sp.diff(Pf**2,x) - 3*Pf**2 + sp.Rational(3,2)*Lf*(Lf+b)*Pf - (sp.Rational(3,16)*Lf**2*(Lf*(Lf+2*b)) - etaf*x**2*(b*Lf/2)))
red = sp.factor(sp.expand(UF*4/Lf))
out['P=-L^2/4, B=0: 4*(UF)/L ='] = str(red)
out['equals L^2(xL\'-3L-3b)+2 eta b x^2'] = bool(sp.simplify(sp.expand(UF*4/Lf) - (Lf**2*(x*sp.diff(Lf,x)-3*Lf-3*b) + 2*etaf*b*x**2))==0)
# with L polynomial of degree N: top coefficient of L^2(xL'-3(L+b)) is (N-3) l_N^3 x^{3N}; for N=3 the identity forces l_2=0
N=3; lN=sp.Symbol('lN')
Lp = -b + l2*x**2 + lN*x**3
expr = sp.expand(Lp**2*(x*sp.diff(Lp,x)-3*Lp-3*b) + 2*(b*l2/2)*b*x**2)
out['N=3 residual coefficients'] = str(sp.Poly(expr,x).all_coeffs())
json.dump(out, open('tacnode_checks.json','w'), indent=1)
for k,v in out.items(): print(k,'=',v)
