#!/usr/bin/env python3
"""Controls for the independent (99,66) engine."""
import sys, json, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from fractions import Fraction as Fr
import sympy as sp
import indep_engine as E
from ring import *

OUT = {}
x, y = sp.symbols('x y')

def K_of(poly, D):
    """K = t^D poly(t^-1, w/t) = sum poly_ij t^{D-i-j} w^j ; t-series of w-polys."""
    p = sp.Poly(sp.expand(poly), x, y)
    S = {}
    for (i, j), c in zip(p.monoms(), p.coeffs()):
        a = D - i - j
        assert a >= 0, (i, j, D)
        S.setdefault(a, {}).setdefault(j, Fr(0))
        S[a][j] += Fr(int(c))
    N = D + 1
    return [{j: const(v) for j, v in S.get(a, {}).items() if v} for a in range(N)]

def KJ_generic(KF, KG, n, m):
    """n KF KG_w - t KF_t KG_w - m KF_w KG + t KF_w KG_t  (w-monomial basis)."""
    N = min(len(KF), len(KG))
    KF = KF[:N]; KG = KG[:N]
    Fw = [pdiff(p) for p in KF]; Gw = [pdiff(p) for p in KG]
    Ft = E.dt(KF); Gt = E.dt(KG)
    T1 = E.tmul(KF, Gw, N); T2 = E.tmul(Ft, Gw, N)
    T3 = E.tmul(Fw, KG, N); T4 = E.tmul(Fw, Gt, N)
    return [padd(padd(psmul(T1[a], n), psmul(T2[a], -1)),
                 padd(psmul(T3[a], -m), T4[a])) for a in range(N)]

# ---------- C1: tame automorphism, degrees 6 and 36, single point at infinity ----------
Fa = x + y**6
Ga = y + (x + y**6)**6
n, m = 6, 36
jac = sp.expand(sp.diff(Fa, x) * sp.diff(Ga, y) - sp.diff(Fa, y) * sp.diff(Ga, x))
OUT['C1_direct_jacobian'] = str(sp.simplify(jac))
D = n + m                      # need t-series long enough to reach t^{n+m-2}
KF = K_of(Fa, n) + [pzero()] * (D + 1 - (n + 1))
KG = K_of(Ga, m) + [pzero()] * (D + 1 - (m + 1))
KJ = KJ_generic(KF, KG, n, m)
bad = []
for a, P in enumerate(KJ):
    for j, c in P.items():
        v = as_const(c)
        want = Fr(1) if (a == n + m - 2 and j == 0) else Fr(0)
        if v != want: bad.append((a, j, str(v), str(want)))
OUT['C1_top_forms'] = {'in_F': str(sp.Poly(Fa, x, y).homogeneous_order() or 'inhom'),
                       'in_F_lead': str(sp.LT(sp.Poly(Fa, x, y))),
                       'in_G_lead': str(sp.LT(sp.Poly(Ga, x, y)))}
OUT['C1_KJ_equals_t40_w0'] = (not bad)
OUT['C1_violations'] = bad[:5]
OUT['C1_bands_checked'] = sum(len(P) for P in KJ)

# ---------- C1b: perturbation must break C1 (discriminating power) ----------
KJp = KJ_generic(KF, KG, n - 1, m)      # wrong homogeneity weight
badp = [(a, j) for a, P in enumerate(KJp) for j, c in P.items()
        if as_const(c) != (Fr(1) if (a == n + m - 2 and j == 0) else Fr(0))]
OUT['C1b_perturbed_engine_fails'] = bool(badp)
OUT['C1b_n_violations'] = len(badp)

# ---------- C2: zero-point control on the (99,66) chart ----------
# all free chart coordinates 0 => F = P^9, G = P^6 => J(F,G) == 0 identically.
K3 = E.build_K3(E.NT)
K3z = [{q: const(as_const(c) or 0) for q, c in P.items() if not vars_of(c)} for P in K3]
K2z, _, _, _ = E.build_K2(K3z)
K2z = [{q: c for q, c in P.items() if not vars_of(c)} for P in K2z]
B1z = [pzero() for _ in range(E.NT)]
KFz, KGz = E.build_KFKG(K2z, B1z)
KJz = E.build_KJ(KFz, KGz)                     # direct (unfactored) formula
nz = [(a, j) for a, P in enumerate(KJz) for j, c in E.to_w(P).items() if c]
OUT['C2_zero_point_KJ_identically_zero'] = (not nz)
OUT['C2_nonzero_slots'] = nz[:5]
OUT['C2_KF_top_is_P9'] = (E.to_w(KFz[0]) == E.to_w(
    pmul(ppow({0: const(1), 1: const(1)}, 27), {72: const(1)})))
print(json.dumps(OUT, indent=1))
json.dump(OUT, open('box/g9966indep-20260903/controls.json', 'w'), indent=1)
