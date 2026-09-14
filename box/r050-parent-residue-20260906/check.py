#!/usr/bin/env python3
"""Small exact checks for the R050 physical-place residue pilot; stdout only."""
import json
import sympy as S

y, w, x, u, v, z, s, a, kappa, eps, T = S.symbols(
    "y w x u v z s a kappa eps T"
)
d = 1 - a
q = y * w**4 - 1
r = y * w**4 - a
F = r**2 * (y**4 * w**2 * q**8 - kappa*y*w**2*q + eps*y*w**3*q)
fp = S.Poly(S.expand(F), y, w)
assert fp.total_degree() == 56
assert sum(c*y**i*w**j for (i, j), c in fp.terms() if i+j == 56) == y**14*w**42

# Exact pullback at the zero root of the final major face.
Y, W = 1 + u**5 + u**7*v, 1 + u**2*v
Q = S.cancel((Y*W**4 - 1)/u**2)
assert S.Poly(Q, u, v).total_degree() >= 0
H = (d+u**2*Q)**2 * (
    u**2*Y**4*W**2*Q**8 - kappa*Y*W**2*Q + eps*u*Y*W**3*Q
)
H0 = S.expand(H.subs(u, 0))
H1 = S.expand(S.diff(H, u).subs(u, 0))
assert S.factor(H0 + 4*kappa*d**2*v) == 0
assert S.factor(H1 - 4*eps*d**2*v) == 0
A0 = S.diff(H0, v)
v0 = S.cancel(T/A0)
residue = S.factor(4*S.diff(H1, v).subs(v, v0)/A0**2)
assert S.factor(residue - eps/(kappa**2*d**2)) == 0

# Face extraction, using normalized factors so no large Laurent expansion occurs.
face_d2 = z**2*(z**4-1)**8*(z**4-a)**2
# x=s^-28, y=s^-28+s^7+s^19*z: q=s^12*Qs, r=d+s^12*Qs.
Ys, Ws = 1+s**35+s**47*z, 1+s**12*z
Qs = S.cancel((Ys*Ws**4-1)/s**12)
Fscaled = (d+s**12*Qs)**2 * (
    Ys**4*Ws**2*Qs**8-kappa*Ys*Ws**2*Qs+eps*s**7*Ys*Ws**3*Qs
)
face_d1 = S.factor(Fscaled.subs(s, 0))
assert S.expand(face_d1-d**2*((4*z)**8-4*kappa*z)) == 0
assert S.diff(face_d1, eps) == 0
assert S.diff(face_d2, eps) == 0
assert S.expand(S.diff(face_d1, z).subs(z, 0)+4*kappa*d**2) == 0

# General floor: i+(19/7)j >= -2/7, N=i+3j.
allowed = {
    N: [j for j in range(57) if S.Rational(N-3*j)+S.Rational(19,7)*j >= -S.Rational(2,7)]
    for N in (-1, 0, 1)
}
assert allowed == {-1: [], 0: [0, 1], 1: [0, 1, 2, 3, 4]}

# Algebraic redundancy on the FULL constant-Jacobian chart.
A, B, bminus = S.symbols("A B bminus")
h = S.symbols("h0:5")
g = S.symbols("g0:4")
H1gen = sum(h[i]*v**i for i in range(5))
G0 = sum(g[i]*v**i for i in range(4))
Hgen, Ggen = A*v+B+u*H1gen, bminus/u+G0+u*v
Juv = S.expand(S.diff(Hgen,u)*S.diff(Ggen,v)-S.diff(Hgen,v)*S.diff(Ggen,u))
assert S.expand(Juv).coeff(u, -2) == A*bminus
assert S.expand(S.expand(Juv).coeff(u,-1)-bminus*S.diff(H1gen,v)) == 0

# Positive automorphism control; omega_f=dx and dg=-omega_f.
fauto, gauto = y+x**2, -x
Jauto = S.diff(fauto,x)*S.diff(gauto,y)-S.diff(fauto,y)*S.diff(gauto,x)
assert Jauto == 1

# Mandatory negative control h=x+x^2*y: no affine critical point, fibrewise exact.
hbad = x+x**2*y
hx, hy = S.diff(hbad,x), S.diff(hbad,y)
assert S.expand((1-2*x*y)*hx+4*y**2*hy) == 1
assert S.diff(-1/x,x) == 1/x**2
assert S.residue(1/x**2,x,0) == 0
assert S.residue((1/x**2).subs(x,1/z)*(-1/z**2),z,0) == 0
assert S.simplify(hbad.subs(y,(T-x)/x**2)) == T
assert hx.subs(x,0) == 1
assert S.simplify(hx.subs(y,-1/x)) == -1

# Sol's displayed twisted example has an off-by-one exponent. Repair it.
gamma, pi = S.symbols("gamma pi")
twisted = []
for ell in range(1, 6):
    Qr = gamma*pi
    Pcorrect = gamma**ell/S.Integer(ell)
    Pprinted = gamma**(ell+1)/S.Integer(ell+1)
    Jcorrect = S.diff(Pcorrect,gamma)*S.diff(Qr,pi)
    Jprinted = S.diff(Pprinted,gamma)*S.diff(Qr,pi)
    assert Jcorrect == gamma**ell
    assert Jprinted == gamma**(ell+1)
    assert S.diff(Pcorrect,gamma) == gamma**ell/gamma
    twisted.append(ell)
assert S.residue(1/gamma,gamma,0) == 1
assert S.residue((1/gamma).subs(gamma,1/z)*(-1/z**2),z,0) == -1

print(json.dumps({
    "status": "PASS_EXACT_SYMBOLIC",
    "family_degree": fp.total_degree(),
    "expanded_terms_in_y_w": len(fp.terms()),
    "D2_face": str(face_d2), "D1_face": str(face_d1),
    "H0": str(S.factor(H0)), "H1": str(S.factor(H1)),
    "v0_generic_T": str(v0), "physical_place_e": 4,
    "residue": str(residue), "generic_H1_degree_bound": 4,
    "full_jacobian_residue_row": "[u^-1] J_uv = bminus*H1'(v)",
    "positive_automorphism": "PASS",
    "negative_fibre_exactness": "PASS",
    "twisted_exponent_repair_checked_ell": twisted,
    "scope": "Top/D2/D1 face control, NOT full R050 source realization or Keller pair"
}, indent=2, sort_keys=True))
