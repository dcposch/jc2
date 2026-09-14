#!/usr/bin/env python3
"""k0-row law, derived + verified, and its transfer to Moh's (16,12) chart.

DERIVATION (u=y, v=y-x; J_{x,y}=J_{u,v} since d(u,v)/d(x,y)=1):
  F_top = u^a v^b,  a=e*A, b=e*B
  B1c_{r,Q} term of B1*h^(f-1) = (u-v)^c u^d v^g,  c=K-1-r-Q, d=A(f-1), g=Q+B(f-1)
  J = (u-v)^(c-1) u^(a+d-1) v^(b+g-1) [ -c(a+b) u - beta x ],  beta = -(ac+ag-bd)
  ac+ag-bd = e*A*(K-1-r)          <-- Q cancels identically
  lowest y-power k0 = a+d-1 = A(e+f-1)-1, coefficient (-1)^(b+g-1) * e*A*(K-1-r)
So the k0 row of the t^p band (r=p-1) is  +- e*A*(K-p) * sum_Q (-1)^Q B1c_{p-1,Q}.
"""
import sympy as sp
from itertools import product

def k0_closed(A, B, e, f, p, Q):
    K = A + B; r = p - 1
    N = e*B + Q + B*(f-1) - 1
    return (-1)**N * e*A*(K-1-r)

def k0_direct(A, B, e, f, p, Q):
    """independent expansion in (u,v) -> coefficient of x^(D-k0) y^k0"""
    x, u = sp.symbols("x u")
    K = A+B; r = p-1; n, m = e*K, f*K
    c = K-1-r-Q; d = A*(f-1); g = Q + B*(f-1); a = e*A; b = e*B
    if c < 0: return None
    v = u - x
    F = u**a * v**b
    G = x**c * u**d * v**g
    J = sp.expand(sp.diff(F,x)*sp.diff(G,u) + sp.diff(F,u)*(-sp.diff(G,x))
                  - (sp.diff(F,u)*sp.diff(G,x) - sp.diff(F,x)*sp.diff(G,u)))  # placeholder
    # J_{x,y} = F_u G_v - F_v G_u ; in (x,u) coords with v=u-x: d/dv = -d/dx, d/du|_v = d/du+d/dx
    Fu = sp.diff(F,u)+sp.diff(F,x); Fv = -sp.diff(F,x)
    Gu = sp.diff(G,u)+sp.diff(G,x); Gv = -sp.diff(G,x)
    J = sp.expand(Fu*Gv - Fv*Gu)
    D = n+m-2-p; k0 = A*(e+f-1)-1
    return sp.Poly(J, x, u).coeff_monomial(x**(D-k0)*u**k0)

print("=== control: (99,66)  A=9 B=24 e=3 f=2  K=33  k0=%d ===" % (9*(3+2-1)-1))
A,B,e,f = 9,24,3,2
for p in (1,2,3,4,5,6,7,8):
    cl = {abs(k0_closed(A,B,e,f,p,Q)) for Q in range(0, A+B-p+1)}
    print("  p=%d  closed-form |c_J(k0)| = %s   e*A*(K-p) = %d" % (p, cl, e*A*(A+B-p)))
print("  spot-check by direct expansion (p=4, Q=22): %s   (pivot ledger: -783)" %
      k0_direct(A,B,e,f,4,22))
print("  spot-check by direct expansion (p=8, Q=19): %s   (gate ladder:  +675)" %
      k0_direct(A,B,e,f,8,19))

print("\n=== transfer: Moh p.208 (16,12)  h_top = y^3(y-x)  A=3 B=1 e=4 f=3  K=4 ===")
A,B,e,f = 3,1,4,3
K=A+B; n,m=e*K,f*K; k0 = A*(e+f-1)-1
print("  n=%d m=%d K=%d  k0=A(e+f-1)-1=%d  total deg n+m-2=%d" % (n,m,K,k0,n+m-2))
for p in range(1, K+2):
    if p-1 > K-1: break
    cl = sorted({k0_closed(A,B,e,f,p,Q) for Q in range(0, K-p+1)}, key=abs)
    dr = [k0_direct(A,B,e,f,p,Q) for Q in range(0, K-p+1)]
    print("  p=%d  D=%2d  closed |c_J(k0)|=%s   direct over Q=%s   e*A*(K-p)=%d"
          % (p, n+m-2-p, sorted({abs(z) for z in cl}), dr, e*A*(K-p)))
print("\n  ladder c(p,k) = e*A*(K-p) - n*(k-k0):")
for p in range(1, K+1):
    row=[]
    k=k0
    while e*A*(K-p) - n*(k-k0) > 0:
        row.append((k, e*A*(K-p)-n*(k-k0))); k+=1
    print("   p=%d : %s" % (p, row if row else "EMPTY (ladder exhausted)"))
