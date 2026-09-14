"""Verify the claimed master identity for Astra's (F3) polynomial Abel equation.

CLAIM (Opus, this round).  With  r=b^2/4,  Phi = x*W - r,  K = x^2*C - y*b,
M = K + y*b = x^2*C,  B = -W(0),  eta = W'(0),  the equation (F3)

  2*(x*W-r)*W' = W^2 + (B-2A+D)*W + A*(A-D)/3 - B*(A-D)
                 - b*eta*K/(2y) - B*eta*x + (2*r*A - 4*r*(B+W))/x
  A = 3x^3C^2/(4y^2),  D = 3bxC/(2y)

is EQUIVALENT (after multiplying by x^2) to the single factorization identity

  Phi * Lam  =  Gee                                            (F3')
  Lam := 2*x*Phi' - 3*Phi + 3*K*M/(2*y^2) - B*x
  Gee := 3*K^3*(K+2*b*y)/(16*y^4) - 3*B*x*K^2/(4*y^2)
         - b*eta*x^2*K/(2*y) - B*eta*x^3

Test: generic symbolic W (deg 2t+1) and C (deg t-1), B and eta FREE symbols
(so the check is an identity of rational functions, independent of (F1)).
Then re-impose B = -W(0), eta = W'(0) and check again.
"""
import sympy as sp

x, y, b, B, eta = sp.symbols('x y b B eta')

def check(t, impose_normalization):
    w = sp.symbols('w0:%d' % (2*t+2))      # W = sum w_i x^i , deg 2t+1
    c = sp.symbols('c0:%d' % (t-1))        # C monic of degree t-1
    W = sum(w[i]*x**i for i in range(2*t+2))
    C = sum(c[i]*x**i for i in range(t-1)) + x**(t-1)
    Bv, etav = B, eta
    if impose_normalization:
        Bv = -W.subs(x, 0)
        etav = sp.diff(W, x).subs(x, 0)
    r = b**2/4
    A = 3*x**3*C**2/(4*y**2)
    D = 3*b*x*C/(2*y)
    K = x**2*C - y*b
    M = K + y*b
    lhs = 2*(x*W - r)*sp.diff(W, x)
    rhs = (W**2 + (Bv - 2*A + D)*W + A*(A-D)/3 - Bv*(A-D)
           - b*etav*K/(2*y) - Bv*etav*x
           + (2*r*A - 4*r*(Bv + W))/x)
    E = sp.together(sp.expand(x**2*(lhs - rhs)))
    Phi = x*W - r
    Lam = 2*x*sp.diff(Phi, x) - 3*Phi + 3*K*M/(2*y**2) - Bv*x
    Gee = (3*K**3*(K + 2*b*y)/(16*y**4) - 3*Bv*x*K**2/(4*y**2)
           - b*etav*x**2*K/(2*y) - Bv*etav*x**3)
    F = sp.expand(Phi*Lam - Gee)
    diff = sp.simplify(sp.expand(sp.together(E - F)))
    return diff

for t in (2, 3, 4):
    for imp in (False, True):
        d = check(t, imp)
        print("t=%d impose_norm=%-5s  E - (Phi*Lam - Gee) = %s" % (t, imp, d))
