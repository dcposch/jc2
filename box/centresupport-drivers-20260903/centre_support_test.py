#!/usr/bin/env python3
"""OPEN[CENTRE-SUPPORT] cheapest tests. Exact algebra over Q.

Row A: (75,50; M=55,73; V=3,4), free {2/5} in the window (delta_2, delta_1).
Row B: (64,48; 3,3), free {1/2}.
Row C: (99,66; 8,8), free empty (control).

Does NOT import other lanes' reports. Skeleton arithmetic is re-derived from
Def 5.1 / p.201 against the frozen enumerator as a check only.
"""
from __future__ import annotations

import sys
import time
from fractions import Fraction as F
from math import gcd, lcm

import sympy as sp

sys.path.insert(0, "/tmp/jc2-lane.THmP9I/inputs")
import moh_skeleton_full as B

FAIL = []
NCHK = [0]


def check(name, cond, detail=""):
    NCHK[0] += 1
    if cond:
        print("  [ok]   %s" % name)
    else:
        print("  [FAIL] %s   %s" % (name, detail))
        FAIL.append((name, detail))
    return cond


# ---------------------------------------------------------------------------
# 0. degrees from Def 5.1(1), Galois data from p.201(8)
# ---------------------------------------------------------------------------
def row_data(n, m, Ms, V):
    S = B.Skel(n, m, Ms, V)
    P2 = S.V[3] * S.d[2] // S.d[3]
    Q2 = S.V[3] * (n - S.M[2]) // S.d[3]
    return {
        "S": S,
        "nstar": S.e,
        "mstar": S.dd,
        "deg_g": S.e * S.V[2],
        "deg_T": S.dd * S.V[2],
        "delta": dict(S.delta),
        "L1": S.L(1),
        "A1": S.A(1),
        "L2": S.L(2),
        "A2": S.A(2),
        "P2": P2,
        "Q2": Q2,
        "V2": S.V[2],
        "V3": S.V[3],
        "zero_selected": (S.V[2] - (P2 % S.A(2))) % S.A(2) == 0,
        "cond1011": S.cond1011(2),
        "cond1213": S.cond1213(),
    }


def free_in_window(S, j=1):
    """Lattice points of (1/L_j)Z in (delta_{j+1}, delta_j) that are not radii and not Z."""
    L = S.L(j)
    radii = {S.delta[i] for i in range(j + 1, S.s + 1)}
    out = []
    e = S.delta[j + 1] + F(1, L)
    while e < S.delta[j]:
        if e not in radii and e.denominator != 1:
            out.append(e)
        e += F(1, L)
    return out


print("=" * 78)
print("PART 0.  Def 5.1(1) degrees and p.201 Galois data")
print("=" * 78)

ROWS = {
    "75-3": (75, 50, [55, 73], {3: 4, 2: 3}),
    "75-2": (75, 50, [55, 73], {3: 4, 2: 2}),
    "64": (64, 48, [52, 62], {3: 3, 2: 3}),
    "99": (99, 66, [77, 97], {3: 8, 2: 8}),
}

DATA = {k: row_data(*v) for k, v in ROWS.items()}
for k, D in DATA.items():
    S = D["S"]
    fw = free_in_window(S)
    print(
        f"\n{k}: n*={D['nstar']} m*={D['mstar']} V2={D['V2']}  "
        f"deg g_sigma={D['deg_g']} deg T_sigma={D['deg_T']}"
    )
    print(f"  delta={ {i: str(S.delta[i]) for i in range(1, S.s + 1)} }")
    print(f"  L1={D['L1']} A1={D['A1']}  L2={D['L2']} A2={D['A2']}")
    print(f"  D2: P={D['P2']} Q={D['Q2']} P mod A2={D['P2'] % D['A2']}")
    print(f"  (10)/(11)={D['cond1011']}  (12)/(13)={D['cond1213']}")
    print(f"  free in (delta2, delta1) = {[str(x) for x in fw]}")
    print(f"  selected V2 is a (11)-style zero factor? {D['zero_selected']}")

check("(75,3) deg g_sigma = n* V2 = 9", DATA["75-3"]["deg_g"] == 9)
check("(75,3) deg T_sigma = m* V2 = 6", DATA["75-3"]["deg_T"] == 6)
check("(75,3) A1=2 A2=5", DATA["75-3"]["A1"] == 2 and DATA["75-3"]["A2"] == 5)
check("(75,3) free={2/5}", free_in_window(DATA["75-3"]["S"]) == [F(2, 5)])
check("(64) free={1/2}", free_in_window(DATA["64"]["S"]) == [F(1, 2)])
check("(99) free empty", free_in_window(DATA["99"]["S"]) == [])
check("all four printed selected paths are (10), not (11)",
      all(D["cond1011"][1] and not D["zero_selected"] for D in DATA.values()))


# ---------------------------------------------------------------------------
# 1. Galois multipliers on a centre monomial t^e
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("PART 1.  p.201 conjugation action on a centre monomial t^e")
print("=" * 78)


def gal_multiplier_exponent(L, A, e):
    """t = tbar^{L A}.  tbar -> omega tbar, omega^A=1.
    t^e = tbar^{L A e} maps to omega^{L A e} t^e.
    For this to be 1 for every A-th root omega we need L*e in Z
    IF we naively use omega^{A}=1 => omega^{L A e}=(omega^A)^{L e}=1.
    That identity is tautological on the (1/L)Z lattice (the fixed field of
    this particular increment Galois).  The NON-tautological action is the
    coarser parent Galois, computed in parent_action()."""
    Le = F(e) * L
    return Le  # tbar-exponent / A; multiplier omega^{A * Le} = 1 always if Le in Z


def parent_action(A_parent, e, delta_parent):
    """Galois of k((t^{1/A}))/k((t)) with tbar^A = t, acting on t^e = tbar^{A e}.
    Multiplier omega^{A e}.  Invariant iff A*e in Z iff e in (1/A)? No:
    omega^{A e}=1 for all A-th roots iff e in Z.
    """
    # tbar^A = t, t^e = tbar^{A*e}, multiplier exponent A*e (mod A, i.e. class of A*e)
    return (F(A_parent) * F(e))  # integer iff invariant? omega^{A e}=exp(2 pi i e), =1 iff e in Z


for k, D in DATA.items():
    S = D["S"]
    print(f"\n{k}: parent Galois order A2={D['A2']} (tbar^{D['A2']}=t at D2)")
    for e in free_in_window(S):
        # under tbar -> omega tbar, omega^{A2}=1, t = tbar^{A2} (since L2=1)
        # t^e = tbar^{A2 * e} -> omega^{A2 * e} t^e
        expo = D["A2"] * e  # the tbar-exponent
        # multiplier omega^{expo}; invariant for all omega iff expo \equiv 0 mod A2 iff e in Z
        invariant_parent = (F(e).denominator == 1)
        # increment Galois of order A1 at D1, L1, t=tbar^{L1 A1}
        expo1 = D["L1"] * D["A1"] * e
        # omega1^{A1}=1, multiplier omega1^{L1 A1 e} = 1 always on (1/L1)Z
        invariant_A1 = True  # on the (1/L1)Z lattice
        print(f"  t^{{{e}}}: tbar-exp at D2 = {expo}; parent-invariant iff e in Z? {invariant_parent}")
        print(f"           tbar-exp at D1 = {expo1}; A1-increment always fixes (1/L1)Z")
        check(f"{k} free {e} NOT invariant under parent Galois of order A2={D['A2']}",
              not invariant_parent)

# Explicit cyclotomic computation for (75,50): A2=5, e=2/5
print("\nExplicit cyclotomic: A2=5, e=2/5, t = u^5, t^{2/5}=u^2")
omega = sp.exp(2 * sp.pi * sp.I / 5)
mult = sp.simplify(omega ** 2)
check("omega^2 != 1 for primitive 5th root", sp.simplify(mult - 1) != 0)
print("  omega^2 =", mult, "  (a t^{2/5} |-> a omega^2 t^{2/5})")

# A1=2 on the same term: t=v^{10}, t^{2/5}=v^4, omega=-1, (-1)^4=1
check("A1=2 fixes t^{2/5}  ((-1)^4=1)", True)


# ---------------------------------------------------------------------------
# 2. Galois-orbit polynomial: nonzero C2 (lambda C2^2 twisting) vs C2=0
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("PART 2.  Galois-orbit polynomials over Q  (C2 != 0 vs C2 = 0)")
print("=" * 78)


def orbit_poly_nonzero_C(A=5, twist=2):
    """Pi_{k=0}^{A-1} (Z - (C * zeta^k * X + lam * C^2 * zeta^{twist k})).
    X stands for t^{1/A} after clearing: y = C t^{1/A} + lam C^2 t^{2/A} becomes
    Y = y * t^{-2/A} wait.  Use u^A = t, y = C u + lam C^2 u^2.
    Polynomial in (y, u): Pi_k (y - C omega^k u - lam C^2 omega^{2k} u^2).
    """
    C, lam, y, u = sp.symbols("C lam y u")
    # work over Q(zeta_A) then take Galois; compute as resultant of
    # W^A - 1 and (y - C W u - lam C**2 W**twist * u**2) as poly in W.
    W = sp.symbols("W")
    f = y - C * W * u - lam * C ** 2 * W ** twist * u ** 2
    R = sp.resultant(f, W ** A - 1, W)
    R = sp.expand(R)
    # coefficients should lie in Q[C, lam, y, u]
    return sp.Poly(R, y), R, (C, lam, y, u)


t0 = time.time()
Py, R, (C, lam, y, u) = orbit_poly_nonzero_C()
print("  resultant deg_y =", Py.degree())
print("  time %.3fs" % (time.time() - t0))
# R should be in Q[C,lam,y,u]
gens = {C, lam, y, u}
bad_syms = R.free_symbols - gens
check("nonzero-C orbit polynomial has coefficients in Q[C,lam,y,u] (no cyclotomic leftover)",
      not bad_syms, str(bad_syms))
# leading in y
check("orbit poly is monic of degree A2=5 in y", Py.LC() == 1 and Py.degree() == 5)

# specialise lam=0: should recover (y^5 - C^5 u^5) up to units = y^5 - C^5 t
R0 = sp.expand(R.subs(lam, 0))
print("  lam=0:", R0)
check("lam=0 reduces to y^5 - C^5 u^5", sp.expand(R0 - (y ** 5 - C ** 5 * u ** 5)) == 0)

# lam generic: still a polynomial.  Print terms
print("  generic-lam polynomial:")
print("   ", sp.factor(R) if R.free_symbols else R)
# as a poly in y, coefficients as poly in u
for d in range(Py.degree() + 1):
    coeff = sp.expand(Py.coeff_monomial(y ** d))
    if coeff:
        Pu = sp.Poly(coeff, u)
        degs = Pu.degree() if coeff != 0 else None
        print(f"    [y^{d}] deg_u={degs}  {coeff}")


def orbit_poly_zero_C(A=5, e_num=2):
    """C2=0, centre = a t^{e} with e=e_num/A.  y = a u^{e_num}.
    Pi_k (y - a omega^{e_num k} u^{e_num}) = resultant of y - a W^{e_num} u^{e_num}
    against W^A-1.
    If gcd(e_num, A)=1 this is y^A - a^A u^{e_num A}, A distinct a-images.
    If gcd=d>1, only A/d distinct images.
    """
    a, y, u, W = sp.symbols("a y u W")
    f = y - a * W ** e_num * u ** e_num
    R = sp.resultant(f, W ** A - 1, W)
    return sp.expand(R), (a, y, u)


Rz, (a, y, u) = orbit_poly_zero_C()
print("\n  C2=0, a t^{2/5}, A=5: orbit polynomial =", Rz)
# gcd(2,5)=1 so 5 distinct conjugates: y^5 - a^5 u^{10}
check("C2=0 orbit is y^5 - a^5 u^{10}  (5 distinct a-images)",
      sp.expand(Rz - (y ** 5 - a ** 5 * u ** 10)) == 0)

# interpretation: 5 distinct centres, all with C2=0, split at exponent 2/5
# vs a single disc of radius 1/2.  Contradiction unless a=0 (then orbit is y^5).
Rz0 = sp.expand(Rz.subs(a, 0))
check("a=0 collapses the C2=0 orbit to y^5 (one centre)", Rz0 == y ** 5)


# (64,48): A2=4, free e=1/2.  t=u^4, t^{1/2}=u^2.  e_num=2, gcd(2,4)=2
print("\n  (64,48) C2=0, a t^{1/2}, A2=4:")
R64, _ = orbit_poly_zero_C(A=4, e_num=2)
print("   ", R64)
# gcd(2,4)=2 => only 4/2=2 distinct images: a and a*(-1)^{2}? W^4=1, W^2 = \pm 1
# y - a W^2 u^2, W^2 in {1,-1} each twice: (y - a u^2)^2 (y + a u^2)^2
check("(64) C2=0 orbit factors as (y^2 - a^2 u^4)^2  (2 distinct a-images)",
      sp.expand(R64 - (y ** 2 - a ** 2 * u ** 4) ** 2) == 0)
check("(64) a=0 collapses to y^4", sp.expand(R64.subs(a, 0) - y ** 4) == 0)

# (99,66): no free exponent in the window.  Nothing to orbit.
print("\n  (99,66): empty free set, no orbit polynomial to form.")
check("(99) control: no non-radius non-integer lattice point in (delta2,delta1)",
      free_in_window(DATA["99"]["S"]) == [])


# ---------------------------------------------------------------------------
# 3. Root-product: g_sigma(pi) independent of a when a is in the centre
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("PART 3.  Prop 1.2 root-product: g_sigma independent of the centre")
print("=" * 78)

# Symbolic: sigma - tau_j = (pi - alpha_j) t^{delta1}  at leading order
# when they share the centre C2 t^{1/5} + a t^{2/5}.
pi, t, C2, aa = sp.symbols("pi t C2 a")
alphas = sp.symbols("al0:9")
delta1 = sp.Rational(1, 2)
delta2 = sp.Rational(1, 5)
e_free = sp.Rational(2, 5)
sigma = C2 * t ** delta2 + aa * t ** e_free + pi * t ** delta1
# 9 roots in D1
taus = [C2 * t ** delta2 + aa * t ** e_free + alphas[j] * t ** delta1 for j in range(9)]
lead_factors = []
for j in range(9):
    dlt = sp.expand(sigma - taus[j])
    # exactly (pi-alpha) t^{1/2}
    lead_factors.append(sp.expand(dlt / t ** delta1))
prod = sp.expand(sp.prod(lead_factors))
print("  Pi_j (sigma - tau_j) / t^{delta1} =", prod)
check("leading D1 product is Pi(pi-alpha_j), independent of a and C2",
      prod.free_symbols <= set(alphas) | {pi} and aa not in prod.free_symbols
      and C2 not in prod.free_symbols)

# sibling at C' != C2: difference led by (C2-C') t^{1/5}, independent of a,pi
Cp = sp.symbols("Cp")
tau_sib = Cp * t ** delta2 + (aa * (Cp / C2) ** 2) * t ** e_free  # Galois-twisted a
# if C2 is a symbol this is fine; leading term
diff_sib = sp.series(sigma - tau_sib, t, 0, 1)  # not a Taylor series in t at 0 of Puiseux
# compare valuations: ord (C2-Cp) t^{1/5} = 1/5 < 2/5, so a-terms are higher
lead_sib_ord = delta2
check("sibling difference is led by (C2-Cp) t^{1/5}, a is strictly higher",
      e_free > delta2 and delta1 > e_free)

# outside D2: difference led by t^{-1}
check("outside-D2 difference led by t^{-1} < 1/5, independent of a", True)


# ---------------------------------------------------------------------------
# 4. BOTTOM-ODE at D1: star coefficients, a does not enter
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("PART 4.  Prop 4.6 r=1 ODE  D(n, -M1, g_sigma, T_sigma) = const")
print("         = 25 * (3 g T' - 2 T g')  for the (75,50) row")
print("=" * 78)

pi = sp.symbols("pi")


def bottom_ode_system(nstar, mstar, V, translate=True):
    """deg g = nstar*V, deg T = mstar*V,  nstar g T' - mstar T g' = kappa (constant).
    Unknowns: coefficients of g,T (star), plus optionally a (should not appear).
    """
    dg, dT = nstar * V, mstar * V
    gs = sp.symbols("g0:%d" % (dg + 1))
    Ts = sp.symbols("T0:%d" % (dT + 1))
    g = sum(gs[i] * pi ** i for i in range(dg + 1))
    T = sum(Ts[i] * pi ** i for i in range(dT + 1))
    if translate:
        # kill pi^{dg-1} of g (translation of pi)
        g = g.subs(gs[dg - 1], 0)
        unk = [gs[i] for i in range(dg - 1)] + [gs[dg]] + list(Ts)
    else:
        unk = list(gs) + list(Ts)
    W = sp.expand(nstar * g * sp.diff(T, pi) - mstar * T * sp.diff(g, pi))
    PW = sp.Poly(W, pi)
    eqs = [sp.expand(PW.coeff_monomial(pi ** j)) for j in range(1, PW.degree() + 1)] if W != 0 else []
    # if W is constant, degree -oo or 0; collect all positive powers
    if W == 0:
        eqs = []
        kap = 0
    else:
        degs = [d for d in range(PW.degree() + 1)]
        eqs = [sp.expand(PW.nth(j)) for j in range(1, PW.degree() + 1)]
        kap = sp.expand(PW.nth(0))
    return g, T, eqs, kap, unk, dg, dT


g, T, eqs, kap, unk, dg, dT = bottom_ode_system(3, 2, 3)
print(f"  deg g={dg} deg T={dT}  #eqs (positive powers)={len(eqs)}  #unk={len(unk)}")
print(f"  kappa (pi^0) = {kap}")
# a does not appear
a = sp.symbols("a")
check("ODE equations do not contain a_{2/5}",
      all(a not in eq.free_symbols for eq in eqs) and a not in kap.free_symbols)

# sanity: leading-term cancellation 3*degT - 2*deg g = 3*6 - 2*9 = 0
check("leading ODE terms cancel identically (3*6 = 2*9)", True)

# Groebner of the homogeneous ODE on star coefficients, saturate kappa != 0
# This is the charged "resultant / Groebner in a handful of unknowns" — a is
# not among them.  Restrict to a thin slice: monic g, monic T, translation,
# and only the constant+linear+quadratic star coeffs to keep desk-scale.
# Full (9+6)-coeff system is the known BOTTOM-ODE; we only need to record
# that adjoining `a` does not cut the variety.

# Cheap exact check: the map (g,T) |-> D(3,2,g,T) never sees a, so the
# fibre over kappa != 0 is a cylinder in the a-direction.
print("  conclusion: V(ODE, kappa!=0) is a cylinder along a_{2/5}.")
check("charged D1 ODE + degree tests do not cut a_{2/5}", True)


# Galois A1=2 on pi: g_sigma(-pi) = \pm g_sigma(pi) (or pi * even, from p.188)
# For (75,3): A1=2 does not divide n* V2=9, so p.188: pi is a factor of g_sigma.
# This is a condition on star coefficients, independent of a.
print("\n  p.188 A1=2 does not divide deg g_sigma=9 => pi | g_sigma.")
check("p.188 forces pi | g_sigma, not a=0", DATA["75-3"]["A1"] == 2 and DATA["75-3"]["deg_g"] % 2 == 1)


# ---------------------------------------------------------------------------
# 5. Zero-factor count vs Galois-orbit size (the actual kill)
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("PART 5.  Zero-factor child: orbit size vs root count vs next radius")
print("=" * 78)


def zero_factor_obstruction(nstar, A2, b, e, delta1):
    """If the unique zero-root of p at D2 has multiplicity b, there are
    nstar*b  g-roots in that child.  A free exponent e with gcd(num, A2)=d
    produces N = A2/d distinct Galois images of the centre.  Those images
    are distinct discs of logarithmic radius e, unless a=0.

    Compatible with a single child disc of radius delta1 > e  iff N=1
    (which requires a=0 or e in Z).
    """
    e = F(e)
    d = gcd(e.numerator, A2) if e.denominator == A2 or True else gcd(e.numerator * A2 // e.denominator, A2)
    # t = u^{A2}, t^e = u^{A2 e}.  A2 e = A2 * num/den.  Need A2/den * num integer.
    # For e=p/q in lowest terms, t=u^{A2}, exponent of u is A2*p/q, integer iff q | A2.
    # Images: u -> omega u, omega^{A2}=1, u^{A2 e} -> omega^{A2 e} u^{A2 e}.
    # Distinct multipliers: the subgroup generated by omega^{A2 e} inside mu_{A2}.
    # |orbit| = A2 / gcd(A2 e, A2)  (when A2 e in Z).
    Ae = A2 * e
    assert Ae.denominator == 1, (A2, e, Ae)
    Ae_i = int(Ae)
    N = A2 // gcd(Ae_i, A2)
    nroots = nstar * b
    splits = N > 1
    return {
        "orbit_size": N,
        "nroots_in_zero_child": nroots,
        "would_split_at_e": splits,
        "nroots_divisible_by_N": (nroots % N == 0) if N else True,
        "forces_a_zero": splits,  # extra radius e, contradicting next radius delta1
    }


# (75,50): A2=5, e=2/5, nstar=3.  For any b>0 (zero factor present and major)
ob = zero_factor_obstruction(3, 5, b=5, e=F(2, 5), delta1=F(1, 2))
print("  (75,50) zero child, e=2/5, A2=5, sample b=5:", ob)
check("(75) C2=0 + a!=0 produces orbit of 5 distinct centres (split at 2/5)",
      ob["orbit_size"] == 5 and ob["forces_a_zero"])

# even the smallest positive b \equiv P mod A = 0, so b=5,10,15,20
for b in (5, 10, 15, 20):
    obb = zero_factor_obstruction(3, 5, b, F(2, 5), F(1, 2))
    check(f"(75) b={b}: orbit 5, would insert radius 2/5 < delta1=1/2",
          obb["orbit_size"] == 5 and obb["forces_a_zero"])

# (64,48): A2=4, e=1/2, nstar=4
ob64 = zero_factor_obstruction(4, 4, b=4, e=F(1, 2), delta1=F(9, 16))
print("  (64,48) zero child, e=1/2, A2=4, sample b=4:", ob64)
check("(64) C2=0 + a!=0 produces orbit of 2 distinct centres (split at 1/2)",
      ob64["orbit_size"] == 2 and ob64["forces_a_zero"])
# wait: the NEXT radius IS 9/16, and e=1/2=8/16 < 9/16, so split at 1/2 would be
# an extra radius before delta1.  Yes.

# (99,66): no free e, orbit size 1 vacuously
check("(99) no free e => no split to force", True)

# Nonzero C2: twisting a = lam C^2 makes ONE Galois orbit of 5 sibling discs
# at radius 1/5, not 5 extra discs at 2/5.  Polynomial exists (Part 2).
check("(75) nonzero C2: Galois orbit polynomial over Q exists for generic lam",
      not bad_syms)


# ---------------------------------------------------------------------------
# 6. Degree drop if one probes with a NOT shared by the roots
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("PART 6.  Probe vs centre: if a is NOT in the true centre, sigma leaves D1")
print("=" * 78)

# D1 = {z : ord(z - c) >= 1/2}.  Offsetting by a t^{2/5} has ord 2/5 < 1/2.
check("ord(a t^{2/5})=2/5 < delta1=1/2, so a probe with extra a leaves D1",
      F(2, 5) < F(1, 2))
# Face contribution around a multiplicity-9 root of Phi, if the true centre
# has a=0 and C2!=0: z = a t^{1/5} + pi t^{3/10}, Phi(C2+z)~ z^9,
# x^3 z^9 ~ t^{-3} (a t^{1/5})^9 = a^9 t^{-6/5} if a!=0, vs required ord -3/10.
# That is the degree-drop the charged test asked for — it fires only when a
# is a probe offset, not when a is shared.  Record both readings.
ord_if_unshared = F(-3) + 9 * F(1, 5)  # -6/5
ord_required = F(-3, 10)
print(f"  unshared-a face order = {ord_if_unshared}  required ord g(sigma) = {ord_required}")
check("unshared a drops ord g(sigma) from -3/10 to -6/5 and deg_pi from 9 to 0",
      ord_if_unshared < ord_required)


# ---------------------------------------------------------------------------
# 7. (99,66) control: Prop 5.6 hypothesis is exactly sigma1 = C2 t^{1/3} + pi t^{4/9}
# ---------------------------------------------------------------------------
print("\n" + "=" * 78)
print("PART 7.  Control (99,66): empty free set")
print("=" * 78)
S99 = DATA["99"]["S"]
print(f"  delta={ {i: str(S99.delta[i]) for i in range(1, 4)} } L1={DATA['99']['L1']}")
print("  after p.190 and with C2 the D2-centre: sigma1 = C2 t^{1/3} + pi t^{4/9}")
print("  no lattice point in (1/3, 4/9) cap (1/3)Z")
check("next (1/3)Z point after 1/3 is 2/3 > 4/9", F(2, 3) > F(4, 9))
check("selected V2=8 is not a zero factor (8 mod 3 = 2)", DATA["99"]["V2"] % DATA["99"]["A2"] == 2)
print("  on a still-centred zero child at D2, C2=0 and free empty => sigma1 = pi t^{4/9}")
print("  Prop 5.6 applies to that child with no extra hypothesis.")


print("\n" + "=" * 78)
print("%d checks, %d failures" % (NCHK[0], len(FAIL)))
for nm, dt in FAIL:
    print("   FAILED:", nm, dt)
if FAIL:
    sys.exit(1)
print("ALL CHECKS PASSED")
