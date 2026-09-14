"""Build the reduced (F3') chart.

(F3')   Phi*Lam = Gee,  Lam = 2x Phi' - 3 Phi + 3 K M /(2y^2) - B x
Equivalently   x*(Phi^2)' - 3*Phi^2 = Gee + Phi*(B x - 3 K M/(2 y^2)).
The operator x d/dx - 3 is diagonal with eigenvalue (n-3); so for n != 3 the
coefficient equation SOLVES for phi_n (coefficient of phi_n is (n-3)*2*phi_0
= -(n-3)*b^2/2, a unit off b=0).  n = 0,1,2,3 are vacuous identities.
=> free data (b, B, eta, phi_3, c_0..c_{t-2}) = t+3 unknowns,
   phi_4..phi_{2t+2} determined, and the residual system is
   phi_n = 0  for n = 2t+3 .. 4t+4    (2t+2 equations).
"""
import sys, sympy as sp

t = int(sys.argv[1])
q = 2*t+1
x = sp.Symbol('x')
d = sp.Symbol('d')
DMIN = d**2 - sp.Rational(t+1, 3)

def red(e):
    e = sp.expand(e)
    return sp.expand(sp.rem(sp.Poly(e, d), sp.Poly(DMIN, d)).as_expr()) if e.has(d) else e

y = (d + t + 1)/(2*q)
b, B, eta, f3 = sp.symbols('b B eta f3')
c = sp.symbols('c0:%d' % max(t-1, 1))
C = sum(c[i]*x**i for i in range(t-1)) + x**(t-1)
K = sp.expand(x**2*C - y*b)
M = sp.expand(x**2*C)
KM = sp.expand(K*M)
Gee = sp.expand(3*K**3*(K+2*b*y)/(16*y**4) - 3*B*x*K**2/(4*y**2)
                - b*eta*x**2*K/(2*y) - B*eta*x**3)

N = 4*t+4
def cf(p, n):
    return p.coeff(x, n)
gc  = [red(sp.together(sp.simplify(cf(Gee, n)))) for n in range(N+1)]
kmc = [red(sp.expand(cf(KM, n))) for n in range(N+1)]
c32 = red(sp.together(3/(2*y**2)))

phi = {0: -b**2/4, 1: -B, 2: eta, 3: f3}
for n in range(4, N+1):
    # (n-3)*sum_{i} phi_i phi_{n-i} = gc[n] + B*phi_{n-1} - c32*sum_j kmc[j] phi_{n-j}
    known = sum(phi[i]*phi[n-i] for i in range(1, n))          # excludes 2*phi_0*phi_n
    rhs = gc[n] + B*phi.get(n-1, 0) - c32*sum(kmc[j]*phi[n-j] for j in range(2, n+1) if (n-j) in phi)
    val = sp.cancel(sp.together((rhs/(n-3) - known)/(2*phi[0])))
    phi[n] = red(sp.expand(sp.numer(val)))/sp.expand(sp.denom(val)) if False else sp.cancel(val)
    if n <= 6:
        print("  phi_%d computed, ops=%d" % (n, sp.count_ops(phi[n])))

eqs = []
for n in range(2*t+3, N+1):
    e = sp.numer(sp.together(phi[n]))
    e = red(sp.expand(e))
    e = sp.factor_terms(e)
    eqs.append(e)
print("t=%d : unknowns = b,B,eta,f3,%s  (%d)   equations n=%d..%d (%d)"
      % (t, ','.join(map(str, c[:t-1])), t+3, 2*t+3, N, len(eqs)))
for i, e in enumerate(eqs):
    print("  eq[%d] (n=%d): ops=%d deg_b=%s" % (i, 2*t+3+i, sp.count_ops(e),
          sp.degree(sp.Poly(e, b)) if e != 0 else '-'))
sp.pprint(sp.factor(eqs[-1]))
