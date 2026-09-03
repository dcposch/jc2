#!/usr/bin/env python3
"""Attack C: Moh p.150/p.152 numeric screens on the descended K=16 ray, symbolic in t.

p.150: d_1=n, d_{j+1}=gcd(n,M_1,...,M_j), M_j=min{i: f_i!=0, d_j not| i},
       n_j=d_j/d_{j+1}, q_1=M_1, q_j=M_j-M_{j-1}, lam_j=sum_{i<=j} q_i d_i,
       mu_j=lam_j/d_j, th_j=mu_j-M_j.
p.152 Prop 2.2: with E=ord_eta(sum f_j(x)eta^j - sum f_j(0)eta^j) (=n-1 under the
       Jacobian condition, Lemma 2.1), and M_r<=E: deg_y T_r(f,g) = -mu_r,
       and T_r monic in y when M_r<E.
"""
import sympy as sp
t = sp.symbols('t', positive=True, integer=True)
n, m, M1, M2, V2 = 12*t+4, 8*t+4, -(8*t+4), 12*t+1, 3
d1, d2, d3 = n, sp.Integer(4), sp.Integer(1)
print("gcd chain: d1=n=%s, d2=gcd(n,m)=4, d3=gcd(4,M2)=gcd(4,12t+1)=1" % d1)
print("  n_1=d1/d2 =", sp.simplify(d1/d2), "   n_2=d2/d3 =", d2/d3)
q1, q2 = M1, sp.expand(M2 - M1)
lam1 = sp.expand(q1*d1); lam2 = sp.expand(lam1 + q2*d2)
mu1, mu2 = sp.expand(lam1/d1), sp.expand(lam2/d2)
th1, th2 = sp.expand(mu1-M1), sp.expand(mu2-M2)
E = n-1
for nm, v in (("q_1",q1),("q_2",q2),("lam_1",lam1),("lam_2",lam2),
              ("mu_1",mu1),("mu_2",mu2),("th_1",th1),("th_2",th2),("E=n-1",E)):
    print(f"  {nm:7s} = {sp.factor(v)}")
print("\nProp 2.2 screens (need integrality and M_r<=E):")
print("  M_1<=E:", sp.simplify(E-M1), ">0 for t>=1 -> True")
print("  M_2<=E:", sp.simplify(E-M2), "= 2 > 0 -> True (M_2<E, so T_2 monic in y)")
print("  deg_y T_1 = -mu_1 =", sp.factor(-mu1), " integral, >0 for t>=1")
print("  deg_y T_2 = -mu_2 =", sp.factor(-mu2), " integral, >0 for t>=1")
print("  n_1=d1/d2 =", sp.factor(sp.simplify(d1/d2)), "integral;  n_2 = 4 integral")
print("  => no integrality/positivity screen from p.150/p.152 bites on the ray.")
# Moh Def 5.1(3) / Prop 5.3 window (charged): V_3 d_2/d_3 >= V_2 > d_2/(n-M_2)
print("\nDef 5.1 window:  V_3*d_2/d_3 = 4 >= V_2 = 3 > d_2/(n-M_2) = 4/3 :",
      sp.simplify(4 - 3) >= 0 and sp.Rational(4,3) < 3)
print("Def 5.1(3) denominator n-M_2-1 =", sp.simplify(n-M2-1), "(nonzero, uniform)")
# tuple index and the Ubar-power dictionary
print("\nTuple index in the reciprocal parameter:  N = M_2-(n-m) = m-3 =", sp.factor(m-3))
print("eta-order of the tuple anchor:  M_2+m = ", sp.factor(sp.expand(M2+m)),
      " = 5*(4t+1) = 5*wt(x) = wt(c)")
