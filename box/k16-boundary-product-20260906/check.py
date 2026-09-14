#!/usr/bin/env python3
"""Small exact identities for the K16 marked rational-pole and norm lemmas.

No ideal solver, finite-degree search, files generated, or numerical evidence.
Run: python3 box/k16-boundary-product-20260906/check.py
"""
import sympy as S

x, z, w, wp, a, B, eta = S.symbols("x z w wp a B eta")
r, s, h, p, c = S.symbols("r s h p c", nonzero=True)


def residual(X, W, Wp, A, b, e):
    U = X**3 * A**2
    return (2*X*W*Wp-W**2+(S.Rational(3, 2)*U-b)*W
            -S.Rational(3, 16)*U**2+S.Rational(3, 4)*b*U+b*e*X)


def zero(expr, label):
    assert S.cancel(expr) == 0, (label, S.factor(expr))
    print("PASS", label)


sc = S.expand(residual(x, s*w, s*r*wp, h*a, s*B, s*r*eta)
              -s**2*residual(r*x, w, wp, a, B, eta))
zero(S.rem(sc, h**2-s*r**3, h), "scaling modulo h^2=s*r^3")

# A genuine whole-equation rational solution, not a finite-degree search.
Ap = c/x
Wp = p*c**2*x-B
ep = (p+S.Rational(3, 4))*c**2
rp = S.cancel(residual(x, Wp, S.diff(Wp, x), Ap, B, ep))
zero(rp-c**4*x**2*(p**2+S.Rational(3, 2)*p-S.Rational(3, 16)),
     "rational negative-control residual")
zero(ep-S.diff(Wp, x)-S.Rational(3, 4)*c**2,
     "negative control misses exactly the marked linear jet")

# At the only possible origin pole of A, its residue is killed by B != 0.
w2, a0 = S.symbols("w2 a0")
jet = S.series(residual(x, -B+eta*x+w2*x**2, eta+2*w2*x,
                       c/x+a0, B, eta), x, 0, 2).removeO()
zero(S.expand(jet).coeff(x, 1)+S.Rational(3, 4)*B*c**2,
     "origin simple-pole coefficient")

# Quadratic cover. Z denotes x*A, and its pulled-back value is independent
# for the two identities below; no particular A or degree is sampled.
t, Z = S.symbols("t Z")
f = 3*t*(t-1)
D = S.Rational(3, 4)*Z**2
Q = (t-1)*D-1
Qs = -t*D-1
R = S.Rational(3, 16)*x*Z**4-S.Rational(3, 4)*Z**2-1
zero(Q*Qs+R.subs(x, f), "quadratic norm")
tau = x*Z**2/4
zero(3*tau*(tau-1)-x-x*R, "inverse map f(U/4)=x modulo R")
zero(f*Z**2/4-t-t*Q, "inverse map U(f)/4=t modulo Q")

J = 2*wp-(w+1)/x+S.Rational(3, 2)*x**2*a**2
Ra = R.subs(Z, x*a)
zero(residual(x, w, wp, a, 1, 1)-x*(w*J-Ra),
     "entire boundary equals x*(W*J-R)")

# The branch value is never a multiple zero of R, if it is a zero at all.
Zp = S.symbols("Zp")
Rprime = S.diff(R, x)+S.diff(R, Z)*Zp
zero(S.rem(S.together(R.subs(x, -S.Rational(3, 4))), Z**2+S.Rational(8, 3), Z),
     "retained ramification value R(-3/4)=0")
zero(S.rem(S.together(Rprime.subs(x, -S.Rational(3, 4)))-S.Rational(4, 3),
           Z**2+S.Rational(8, 3), Z),
     "ramification zero has derivative 4/3")

# Verify the cleared differential norm filter with independent values/jets.
M, Ms, Mt, Mts, N, Ns, aa = S.symbols("M Ms Mt Mts N Ns aa", nonzero=True)
dm = Mt*Ms-M*Mts
Wf = -M*Ms/aa
Jf = aa*N*Ns
Wp_f = -dm/(3*aa*(2*t-1))
link = Jf-2*Wp_f+(Wf+1)/f-2*D
filter_rhs = (-2*t*(t-1)*dm+(2*t-1)*(M*Ms-aa)
              +6*aa*t*(t-1)*(2*t-1)*D)
filter_lhs = 3*aa**2*t*(t-1)*(2*t-1)*N*Ns
zero(3*aa*t*(t-1)*(2*t-1)*link-filter_lhs+filter_rhs,
     "cleared differential norm filter")

print("ALL_EXACT_IDENTITY_CHECKS_PASS")
