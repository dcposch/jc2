#!/usr/bin/env python3
"""Graded Laurent-bridge coefficients phi_k for the K=16 ray.

n=12t+4, m=8t+4, e=n/4=3t+1, q=m/4=2t+1, r=e/q.
Phi := Q*eta^m = (Q/h^q) * (P/h^e)^{-q/e}.  Top graded: Ubar=A/h^{t+1}, eta-weight
4t+1.  Ubar^k sits at eta-exponent k(4t+1) == k (mod 4), so the 4-tuple conditions
restricted to the graded part are [U^1]=[U^2]=[U^3]=0, [U^4] free, and
[U^5] != 0 -- exponent 5(4t+1)=20t+5=M_2+m, exactly the tuple index.
"""
import sympy as sp

t, x, y, r = sp.symbols('t x y r')
N = 7

def mul(a, b):
    return [sp.expand(sum(a[i]*b[k-i] for i in range(k+1))) for k in range(N)]

def pw(a, s):
    """a^s, a[0]=1, via k c_k = sum_{j=1..k} (s j - (k-j)) a_j c_{k-j}."""
    c = [sp.Integer(1)] + [None]*(N-1)
    for k in range(1, N):
        acc = sum((s*j - (k-j))*a[j]*c[k-j] for j in range(1, k+1))
        c[k] = sp.cancel(sp.expand(acc)/k)
    return c

F = [sp.Integer(1), x, y] + [sp.Integer(0)]*(N-3)
Fr = pw(F, r)
g1, g2, g3 = (sp.factor(v) for v in Fr[1:4])
print("== E1-E3 solved coefficients (F^r truncation) ==")
print("  g1 =", g1); print("  g2 =", g2); print("  g3 =", g3)

def binom(s, k):
    out = sp.Integer(1)
    for i in range(k):
        out *= (s - i)
    return sp.cancel(out/sp.factorial(k))
for nm, gg, ref in (("g1", Fr[1], r*x), ("g2", Fr[2], r*y + binom(r,2)*x**2),
                    ("g3", Fr[3], 2*binom(r,2)*x*y + binom(r,3)*x**3)):
    print(f"  charged {nm} matches:", sp.expand(sp.cancel(gg - ref)) == 0)

e, q = 3*t+1, 2*t+1
sub = {r: sp.Rational(1,1)*e/q}
E4 = sp.cancel(sp.expand(((e-3*q)*x*Fr[3] + (2*e-2*q)*y*Fr[2]).subs(sub)))
Hhat = 12*q**2*y**2 - 12*q*(t+1)*x**2*y + (t+1)*(3*t+2)*x**4
print("\n== E4 vs charged (H) ==")
print("  E4/Hhat =", sp.factor(sp.cancel(E4/Hhat)))
print("  c=-y*g3 =", sp.factor(sp.cancel((-y*Fr[3]).subs(sub))))

G = [sp.Integer(1), Fr[1], Fr[2], Fr[3]] + [sp.Integer(0)]*(N-4)
Phi = mul(F, pw(G, -1/r))
print("\n== Phi graded coefficients (generic r) ==")
for k in range(6):
    print(f"  phi_{k} =", sp.factor(sp.cancel(Phi[k])))

print("\n== x=1 slice, ray value r=(3t+1)/(2t+1) ==")
H1 = sp.expand(Hhat.subs(x, 1))
p4 = sp.cancel(sp.together(Phi[4].subs(sub).subs(x, 1)))
p5 = sp.cancel(sp.together(Phi[5].subs(sub).subs(x, 1)))
n5, d5 = sp.fraction(p5)
n5 = sp.expand(n5)
print("  H_t(y) =", sp.factor(H1))
print("  phi_4  =", sp.factor(p4))
print("  phi_5  =", sp.factor(p5))
quo, rem = sp.div(sp.Poly(n5, y), sp.Poly(H1, y))
print("  num(phi_5) = (", sp.factor(quo.as_expr()), ")*H_t + (", sp.factor(sp.expand(rem.as_expr())), ")")
print("  phi_5 == 0 in A_t ?", sp.expand(rem.as_expr()) == 0)
print("  Res_y(H_t,num phi_5) =", sp.factor(sp.resultant(H1, n5, y)))
print("  denom(phi_5) =", sp.factor(d5))
