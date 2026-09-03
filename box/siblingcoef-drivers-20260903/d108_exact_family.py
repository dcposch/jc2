#!/usr/bin/env python3
"""Exact Qbar one-parameter family for the D=108 cyclic bottom ODE.

The discrete coefficient field is K=Q[a]/(MINPOLY).  The displayed member is
normalised by F,G monic and coeff(z^6,F)=1.  Root dilation supplies the free
parameter s: F_s(z)=s^-7 F(sz), G_s(z)=s^-10 G(sz).
"""

import sympy as sp


a, z, x, s = sp.symbols("a z x s")
MINPOLY = (
    287548593020928*a**5 - 688401965085696*a**4
    + 640652914818432*a**3 - 292066554895024*a**2
    + 65563255857792*a - 5817852446211
)
assert sp.Poly(MINPOLY, a, domain=sp.QQ).is_irreducible


def reduce_k(expr):
    """Normal form in K, including rational functions whose denominator is a unit."""
    numerator, denominator = sp.together(expr).as_numer_denom()
    modulus = sp.Poly(MINPOLY, a, domain=sp.QQ)
    inverse = sp.invert(sp.Poly(denominator, a, domain=sp.QQ), modulus)
    return sp.factor(sp.rem(sp.Poly(numerator, a, domain=sp.QQ) * inverse,
                            modulus).as_expr())


fc = [None] * 8
fc[0] = (
    2473699609838592*a**4 - 4880250718447104*a**3
    + 3484831588909616*a**2 - 1079655594514872*a
    + 123291106405875
) / sp.Integer(15858472891479552)
fc[1] = (
    5513086784810050560*a**4 - 11023906566235965696*a**3
    + 7949047218967327952*a**2 - 2481117197487437928*a
    + 284986511308009521
) / sp.Integer(401747979917481984)
fc[2] = 7 * (
    1898608366334131200*a**4 - 3803361970401319680*a**3
    + 2745126606514279984*a**2 - 857130636468363480*a
    + 98443252126745919
) / sp.Integer(66957996652913664)
fc[3] = 7 * (
    1472867824488238080*a**4 - 2950502889599315712*a**3
    + 2129064709044490224*a**2 - 664388468462807608*a
    + 76242600010205835
) / sp.Integer(11159666108818944)
fc[4] = (
    3771978574908902400*a**4 - 7556165936778735360*a**3
    + 5450946367591254384*a**2 - 1699030592727011128*a
    + 194711288931974931
) / sp.Integer(2789916527204736)
fc[5], fc[6], fc[7] = a, sp.Integer(1), sp.Integer(1)
fc = list(map(reduce_k, fc))

# The coefficient of z^k in
#   W = 3*z*G*F' - (G+2*z*G')*F
# is sum_{i+j=k}(3*i-2*j-1) f_i g_j.  Equations k=16,...,7
# are triangular and determine g_9,...,g_0.
gc = [None] * 11
gc[10] = sp.Integer(1)
for k in range(16, 6, -1):
    j = k - 7
    coefficient = 20 - 2*j
    rest = sum(
        (3*i - 2*jj - 1) * fc[i] * gc[jj]
        for i in range(8) for jj in range(11)
        if i + jj == k and jj != j and gc[jj] is not None
    )
    gc[j] = reduce_k(-rest / coefficient)

F = sum(fc[i] * z**i for i in range(8))
G = sum(gc[j] * z**j for j in range(11))
W = 3*z*G*sp.diff(F, z) - (G + 2*z*sp.diff(G, z))*F
assert all(reduce_k(sp.Poly(W, z).nth(k)) == 0 for k in range(1, 17))
kappa = reduce_k(sp.Poly(W, z).nth(0))

# Positive saturation control, and the negative control obtained by forcing
# the saturand to zero: gcd 1 says K has no point with kappa=0.
modulus = sp.Poly(MINPOLY, a, domain=sp.QQ)
for label, value in (("F(0)", fc[0]), ("G(0)", gc[0]), ("kappa", kappa)):
    numerator = sp.together(value).as_numer_denom()[0]
    assert sp.gcd(sp.Poly(numerator, a, domain=sp.QQ), modulus).degree() == 0
    print(label, "NONZERO in K")

Fbar = sp.expand(sum(fc[7-i] * x**i for i in range(8)))
Gbar = sp.expand(sum(gc[10-i] * x**i for i in range(11)))
difference = sp.Poly(sp.expand(Fbar**3 - Gbar**2), x)
assert all(reduce_k(difference.nth(i)) == 0 for i in range(17))
assert reduce_k(difference.nth(17)) != 0

print("MINPOLY =", MINPOLY)
print("F =", F)
print("G =", G)
print("W = kappa != 0; reversed difference has exact order 17: PASS")
print("family: F_s(z)=s^-7 F(s*z), G_s(z)=s^-10 G(s*z), s != 0")
