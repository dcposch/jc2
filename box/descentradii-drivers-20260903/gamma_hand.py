#!/usr/bin/env python3
"""DESCENT-RADII (A): re-derive gamma by hand.

Moh p.211: h = A y + a8 = B y^2 + (a6 x + a7) y + a8
           beta = a9 A + a10 y + a11 x + a12
Claim (PROVED-HERE): A^2 ≡ (a6 x + a7) A - a8 B  (mod h)
                      A y ≡ -a8                 (mod h)
whence the B-coefficient of gamma is -a9^2 a8, not -a9^2 a10.
"""
import sympy as sp

x, y = sp.symbols('x y')
a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12 = A_ = sp.symbols('a1:13')

B = (y**2 - x**2 + a1*y + a2*x + a3)*y + (a4*x + a5)
A = sp.expand(B*y + (a6*x + a7))
h = sp.expand(A*y + a8)
beta = sp.expand(a9*A + a10*y + a11*x + a12)

print("== identities mod h ==")
# A y + a8 = h ≡ 0  =>  A y ≡ -a8
q, r = sp.div(sp.Poly(sp.expand(A*y + a8), y), sp.Poly(h, y), y)
print("  A y + a8 == h  (exact, not just mod):", sp.expand(A*y + a8 - h) == 0)
print("  hence A y ≡ -a8 (mod h): remainder of A*y + a8 is", sp.expand(r.as_expr()))

# A = B y + (a6 x + a7), so A^2 = A * (B y + (a6x+a7))
# = B (A y) + (a6x+a7) A ≡ B (-a8) + (a6x+a7) A  (mod h)
idA2 = sp.expand(A**2 - ((a6*x + a7)*A - a8*B))
q2, r2 = sp.div(sp.Poly(idA2, y), sp.Poly(h, y), y)
print("  A^2 - ((a6x+a7)A - a8 B) remainder mod h:", sp.expand(r2.as_expr()))
print("  A^2 ≡ (a6x+a7)A - a8 B (mod h):", sp.expand(r2.as_expr()) == 0)

print("\n== beta^2 mod h ==")
# beta = a9 A + L, L = a10 y + a11 x + a12
L = a10*y + a11*x + a12
# beta^2 = a9^2 A^2 + 2 a9 A L + L^2
# ≡ a9^2 ((a6x+a7)A - a8 B) + 2 a9 A L + L^2
# L = a10 y + M, M = a11 x + a12
# 2 a9 A L = 2 a9 A a10 y + 2 a9 A M = 2 a9 a10 (A y) + 2 a9 M A
#           ≡ -2 a9 a10 a8 + 2 a9 M A
# so beta^2 ≡ [a9^2 (a6x+a7) + 2 a9 M] A  - a9^2 a8 B  + L^2 - 2 a8 a9 a10
M = a11*x + a12
bracket = (a9**2*a6 + 2*a9*a11)*x + (a9**2*a7 + 2*a9*a12)
hand_gamma = sp.expand(bracket*A - a9**2*a8*B + L**2 - 2*a8*a9*a10)
hand_alpha = sp.expand(a9**2*B + 2*a9*a10)

q, r = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
alpha, gamma = sp.expand(q.as_expr()), sp.expand(r.as_expr())
print("  printed alpha = a9^2 B + 2 a9 a10  reproduced:", sp.expand(alpha - hand_alpha) == 0)
print("  audited  gamma (B-coeff = -a9^2 a8) reproduced:", sp.expand(gamma - hand_gamma) == 0)
printed_gamma = sp.expand(bracket*A - a9**2*a10*B + L**2 - 2*a8*a9*a10)
print("  printed  gamma (B-coeff = -a9^2 a10) reproduced:", sp.expand(gamma - printed_gamma) == 0)
print("  ERRATUM[APPII-GAMMA-B] confirmed:",
      sp.expand(gamma - hand_gamma) == 0 and sp.expand(gamma - printed_gamma) != 0)
