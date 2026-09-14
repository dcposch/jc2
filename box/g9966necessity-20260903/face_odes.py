#!/usr/bin/env python3
"""The three face-ODE identities of sec 4.3."""
import sympy as sp
pi, a, c, t, z, rho = sp.symbols('pi a c t z rho')
print("Xu display (8.2), delta = 2:")
q = pi*(pi+3*a)**2*(pi-2*a); p = pi**2*(pi+3*a)
A, B = q*t**-1, p*t**-2
J = sp.simplify(sp.diff(A,t)*sp.diff(B,pi) - sp.diff(A,pi)*sp.diff(B,t))
print("   d(q t^-1, p t^-2)/d(t,pi) =", sp.factor(J))
print("   minus Xu's printed 5 pi^4 (pi+3a)^2 t^-4 :",
      sp.simplify(J - 5*pi**4*(pi+3*a)**2*t**-4), "; and 5 p^2 equals it:",
      sp.simplify(5*p**2 - 5*pi**4*(pi+3*a)**2) == 0)
print("\ndesign (2.5), the degree-40 T3 leader at delta = 2:")
p2 = z**2*(z+3*rho); R = z**25*(z+3*rho)**14*(z-2*rho)
quo, rem = sp.div(sp.Poly(sp.expand(2*p2*sp.diff(R,z) - 25*sp.diff(p2,z)*R), z),
                  sp.Poly(p2**14, z))
print("   deg R = %d ; 2 p R' - 25 p' R = (%s) p^14 with remainder %s"
      % (sp.degree(sp.Poly(R, z)), quo.as_expr(), sp.simplify(rem.as_expr())))
print("\nXu delta = 5/2 :  q1' + 2 p^3 = 0,  p = pi(pi^2-c)")
p5 = pi*(pi**2-c)
q1 = pi**10 - sp.Rational(15,4)*c*pi**8 + 5*c**2*pi**6 - sp.Rational(5,2)*c**3*pi**4
print("   d/dpi[(-1/5) q1] + 2 p^3 =", sp.expand(sp.diff(-q1/5, pi) + 2*p5**3))
B = p5*t**sp.Rational(-1,2); Aq = -q1/5
print("   d((-1/5)q1, p t^-1/2)/d(t,pi) + p^4 t^-3/2 =",
      sp.simplify(sp.diff(Aq,t)*sp.diff(B,pi) - sp.diff(Aq,pi)*sp.diff(B,t)
                  + p5**4*t**sp.Rational(-3,2)))
print("   deg q1 = %d = 3 u_s + 1 ; deg(p^10 q1) = %d = 13 u_s + 1"
      % (sp.degree(sp.Poly(q1, pi)), sp.degree(sp.Poly(sp.expand(p5**10*q1), pi))))
