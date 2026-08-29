#!/usr/bin/env python3
"""Independent CAS audit of the Max11 (6,8) balanced chamber 2*h=3*g.

Discovery-only.  Checks:
  * scalar algebra of a*b^2+3*c^2=0, b*e+c*d=0, 4*b*c^2-9*d*e=0,
    and the cubic-defect three-term face
  * Q- and I3-rewrites of residual rows one and zero
  * Newton-face coefficients at 12*n-3*g-1 and 13*n-3*g-1
  * constant-Jacobian load cutoffs versus those faces
"""

from __future__ import annotations

import sympy as s


def header(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def factor_eq(expr) -> s.Expr:
    return s.factor(s.cancel(s.together(s.expand(expr))))


# ---------------------------------------------------------------------------
# 1. Scalar algebra on leading coefficients
# ---------------------------------------------------------------------------
header("1. Scalar algebra of the given leading relations")

a, b, c, d, e, delta = s.symbols("a b c d e delta")
N, G, H = s.symbols("N G H", commutative=True)
M11 = 11 * N - 3 * G
M12 = 12 * N - 3 * G
M13 = 13 * N - 3 * G

disc = a * b**2 + 3 * c**2
inc = b * e + c * d
row2 = 4 * b * c**2 - 9 * d * e
cubic_def = -2 * d * delta + 3 * b * d**2 - s.Rational(4, 3) * b**3 * c
i3_middle = -a * b * d + 3 * c * e

print("disc =", disc)
print("incidence =", inc)
print("row2 =", row2)
print("cubic_defect_face =", cubic_def)
print("I3_middle =", i3_middle)

e_from_inc = s.solve(inc, e)[0]
print("\nfrom incidence, e =", e_from_inc)

row2_on_inc = s.factor(row2.subs(e, e_from_inc))
print("row2 | incidence =", row2_on_inc)
# c*(4*b^2*c + 9*d^2)/b = 0  =>  c = -9 d^2 / (4 b^2)  (c=0 is the vanishing branch)
c_roots = s.solve(s.numer(s.together(row2_on_inc)), c)
c_from_row2 = next(r for r in c_roots if r != 0)
print("from row2+incidence (c chart), c =", c_from_row2)

e_on_chart = s.simplify(e_from_inc.subs(c, c_from_row2))
a_from_disc = s.solve(disc.subs(c, c_from_row2), a)[0]
a_on_chart = s.simplify(a_from_disc)
print("e =", e_on_chart)
print("a =", a_on_chart)

cubic_on_chart = s.simplify(cubic_def.subs({c: c_from_row2}))
print("cubic defect on chart =", cubic_on_chart)
delta_forced = s.solve(cubic_on_chart, delta)[0]
print("forced Disc coeff delta =", s.simplify(delta_forced))

i3_on_chart = s.simplify(i3_middle.subs({e: e_from_inc, a: s.solve(disc, a)[0]}))
print("I3_middle on disc+incidence (should be 0):", i3_on_chart)

subs_chart = {
    a: a_on_chart,
    c: c_from_row2,
    e: e_on_chart,
    delta: delta_forced,
}
print("\nchart: a,c,e,delta in terms of b,d")
for k, v in subs_chart.items():
    print(f"  {k} = {s.factor(v)}")

# I3 cubic-face leading (no subleading): (-8/9)*b^2*c + (4/3)*d^2
i3_cubic_lead = -s.Rational(8, 9) * b**2 * c + s.Rational(4, 3) * d**2
print("\nnaive I3 coeff at 10N-3G, leading only =", s.factor(i3_cubic_lead))
print("  on row2-chart =", s.factor(i3_cubic_lead.subs(subs_chart)))
print("  NOTE: this is NOT a legal face coefficient (subleading of ABd,ce hit here).")


# ---------------------------------------------------------------------------
# 2. Differential polynomials
# ---------------------------------------------------------------------------
header("2. Residual one-forms and invariants")

t = s.symbols("t")
Af, Bf, cf, df, ef = [s.Function(n)(t) for n in ("A", "B", "c", "d", "e")]


def der(x):
    return s.diff(x, t)


Q = Bf * ef + cf * df - Bf**3 / 9
Disc = Af * Bf**2 + 3 * cf**2
I3 = (
    -s.Rational(8, 9) * Af * Bf * df
    - s.Rational(8, 9) * Bf**2 * cf
    + s.Rational(8, 3) * cf * ef
    + s.Rational(4, 3) * df**2
)
I4 = s.Rational(8, 3) * Q
R = -2 * df * Disc + 3 * Bf * df**2 - s.Rational(4, 3) * Bf**3 * cf

row2_body = (
    -6 * Af * Bf * der(ef)
    - 6 * Af * der(Bf) * ef
    - 6 * Af * cf * der(df)
    - 6 * Af * der(cf) * df
    - der(Af) * Bf**3
    + 3 * der(Af) * Bf * ef
    + 3 * der(Af) * cf * df
    + 6 * Bf**2 * der(df)
    + 12 * Bf * der(Bf) * df
    + 12 * Bf * cf * der(cf)
    + 6 * der(Bf) * cf**2
    - 18 * df * der(ef)
    - 18 * der(df) * ef
)

row1_body = (
    2 * Af**2 * Bf * der(df)
    + 2 * Af**2 * der(Bf) * df
    + 2 * Af * der(Af) * Bf * df
    - 6 * Af * cf * der(ef)
    - 6 * Af * der(cf) * ef
    - 2 * der(Af) * Bf**2 * cf
    + 3 * der(Af) * df**2
    - 3 * Bf**2 * der(ef)
    + 3 * Bf * cf * der(df)
    + 3 * Bf * der(cf) * df
    + 9 * der(Bf) * cf * df
    + 6 * cf**2 * der(cf)
    - 18 * ef * der(ef)
)

row0_body = (
    -Af * der(Af) * Bf * ef
    - Af * der(Af) * cf * df
    - Af * Bf**2 * der(df)
    - Af * Bf * der(Bf) * df
    + der(Af) * Bf * cf**2
    - 3 * der(Af) * df * ef
    + 3 * Bf * cf * der(ef)
    - 3 * Bf * df * der(df)
    - 3 * der(Bf) * df**2
    - 3 * cf * der(cf) * df
)

# Lean residual rows scale by -4/27, -4/27, +4/27 respectively.
row2_poly = -s.Rational(4, 27) * row2_body
row1_poly = -s.Rational(4, 27) * row1_body
row0_poly = s.Rational(4, 27) * row0_body

# Known row-two Q-rewrite from Lean.
row2_Q_rewrite = (
    -6 * Af * der(Q)
    + 3 * der(Af) * Q
    - 2 * Af * Bf**2 * der(Bf)
    - s.Rational(2, 3) * der(Af) * Bf**3
    + 6 * der(Bf**2 * df)
    + 6 * der(Bf * cf**2)
    - 18 * der(df * ef)
)
print(
    "row2_body - Q-rewrite =",
    factor_eq(row2_body - row2_Q_rewrite),
)


# ---------------------------------------------------------------------------
# 3. I3 rewrite of the high (ABd, ce) block of row one
# ---------------------------------------------------------------------------
header("3. I3-rewrite of row one high block")

# 2 A (A B d)' - 6 A (c e)'  is the high block.
high1 = 2 * Af * der(Af * Bf * df) - 6 * Af * der(cf * ef)
rest1 = s.expand(row1_body - high1)
print("high1 remainder vs row1 (should be 0 after expand of rest):")
print("  row1_body - high1 - rest1 =", s.expand(row1_body - high1 - rest1))

# From I3: ce = (3/8) I3 + (1/3) ABd + (1/3) B^2 c - (1/2) d^2
ce_from_I3 = (
    s.Rational(3, 8) * I3
    + s.Rational(1, 3) * Af * Bf * df
    + s.Rational(1, 3) * Bf**2 * cf
    - s.Rational(1, 2) * df**2
)
print("ce - I3-expression =", factor_eq(cf * ef - ce_from_I3))

# Therefore (ABd)' - 3 (ce)' = -(9/8) I3' - (B^2 c)' + (3/2) (d^2)'
id_I3 = der(Af * Bf * df) - 3 * der(ce_from_I3) - (
    -s.Rational(9, 8) * der(I3) - der(Bf**2 * cf) + s.Rational(3, 2) * der(df**2)
)
print("(ABd)'-3(ce_from_I3)' + (9/8)I3' + (B^2 c)' - (3/2)(d^2)' =", factor_eq(id_I3))

high1_rewritten = 2 * Af * (
    -s.Rational(9, 8) * der(I3) - der(Bf**2 * cf) + s.Rational(3, 2) * der(df**2)
)
print("high1 via I3 identity difference =", factor_eq(high1 - high1_rewritten))

row1_via_I3 = high1_rewritten + rest1
print("row1_body - (I3-rewrite + rest1) =", factor_eq(row1_body - row1_via_I3))


# ---------------------------------------------------------------------------
# 4. Q-rewrite of remaining e terms in row one and of row zero
# ---------------------------------------------------------------------------
header("4. Substitute e from Q into remaining row-one terms and row zero")

Qf = s.Function("Q")(t)
I3f = s.Function("I3")(t)

e_from_Q = (Qf - cf * df + Bf**3 / 9) / Bf
# Use cse-friendly substitution of e and e'.
row1_Q = s.expand(row1_body.subs(ef, e_from_Q).doit())
row0_Q = s.expand(row0_body.subs(ef, e_from_Q).doit())
row2_Q = s.expand(row2_body.subs(ef, e_from_Q).doit())

row1_Q = s.cancel(s.together(row1_Q))
row0_Q = s.cancel(s.together(row0_Q))
row2_Q = s.cancel(s.together(row2_Q))

# Split Q-dependent vs Q-free.
def split_Q(expr, tag):
    expr_s = s.together(expr)
    num, den = s.fraction(s.cancel(expr_s))
    num = s.expand(num)
    qpart = s.Poly(num, Qf, der(Qf)).as_expr() - s.Poly(num, Qf, der(Qf)).coeff_monomial(1)
    # Collect terms with Qf or Qf'
    collected = s.collect(num, [Qf, der(Qf)], evaluate=False)
    q_terms = s.Integer(0)
    core = s.Integer(0)
    for mon, coeff in collected.items():
        if mon == 1:
            core += coeff
        else:
            q_terms += mon * coeff
    print(f"\n{tag}: denominator = {s.factor(den)}")
    print(f"{tag} Q-part (numer, factored) =", s.factor(q_terms) if q_terms != 0 else 0)
    print(f"{tag} Q-free core (numer, factored) =")
    print(" ", s.factor(core))
    return den, q_terms, core


den1, q1, core1 = split_Q(row1_Q, "row1")
den0, q0, core0 = split_Q(row0_Q, "row0")
den2, q2, core2 = split_Q(row2_Q, "row2")


# ---------------------------------------------------------------------------
# 5. Leading monomial calculus on the Q-free cores
# ---------------------------------------------------------------------------
header("5. Weighted leading coefficients on 2H=3G, Q below 9N-3G")

# Treat A,B,c,d as monomials of the residual bounds, ignore Q.
# Degrees: A:2N, B:3N-G, c:4N-G, d:5N-H with 2H=3G so H=3G/2.
# Work in Q(N,G) with H = 3G/2.  Use even G=2g0 so H=3g0 is integral.

g0 = s.symbols("g0", positive=True)
Nsym = s.symbols("n", positive=True)
Gval = 2 * g0
Hval = 3 * g0  # 2H = 3G = 6 g0

degA, degB, degc, degd = 2 * Nsym, 3 * Nsym - Gval, 4 * Nsym - Gval, 5 * Nsym - Hval
print("deg A,B,c,d =", degA, degB, degc, degd)
print("row1 cubic face 12n-3G-1 =", 12 * Nsym - 3 * Gval - 1)
print("row0 cubic face 13n-3G-1 =", 13 * Nsym - 3 * Gval - 1)
print("row2 cubic face 11n-3G-1 =", 11 * Nsym - 3 * Gval - 1)
print("I3 cubic face 10n-3G   =", 10 * Nsym - 3 * Gval)
print("Q  cubic face 9n-3G    =", 9 * Nsym - 3 * Gval)

# Monomial substitution into Q-free cores (set Qf=0).
core1_Q0 = s.expand(core1.subs(Qf, 0))
core0_Q0 = s.expand(core0.subs(Qf, 0))
core2_Q0 = s.expand(core2.subs(Qf, 0))
# cores are numerators; divide by den later.

A0, B0, c0, d0 = s.symbols("A0 B0 c0 d0")
mon = {
    Af: A0 * t**degA,
    Bf: B0 * t**degB,
    cf: c0 * t**degc,
    df: d0 * t**degd,
}


def leading_coeff(numer, den, face_deg, name):
    # Substitute monomials, extract coeff of t^face in numer/den.
    num_m = s.expand(numer.subs(Qf, 0).subs(mon).doit())
    den_m = s.expand(den.subs(Qf, 0).subs(mon).doit())
    # den should be a monomial in t times B0^k
    print(f"\n{name}:")
    print("  den after monomials =", s.factor(den_m))
    # Write num = t^p * polynomial in logs?  With monomials, num is a single
    # Laurent monomial times a scalar in (A0,B0,c0,d0,n,g0).
    num_m = s.expand(num_m)
    den_m = s.expand(den_m)
    # Convert to Poly in t if possible.  Degrees may be affine in n,g0.
    # Use as_poly with t after replacing n,g0 by integers, then reconstruct
    # by homogeneity.  Safer: pick a concrete (n,g0) with 3G<n i.e. 6 g0 < n,
    # 0<g0, and also 2h=3g with g=2g0, h=3g0, g<h<2g: 2g0<3g0<4g0 OK.
    # Then match against symbolic scalar.
    samples = [(11, 1), (13, 1), (17, 2), (19, 2), (23, 3)]
    coeffs = []
    for n_val, g0_val in samples:
        G_v = 2 * g0_val
        assert 3 * G_v < n_val
        face = int(face_deg.subs({Nsym: n_val, g0: g0_val}))
        nm = s.expand(num_m.subs({Nsym: n_val, g0: g0_val}))
        dm = s.expand(den_m.subs({Nsym: n_val, g0: g0_val}))
        # Extract [t^face] of nm/dm.  dm is C * t^k.
        pnum = s.Poly(s.expand(nm), t)
        pden = s.Poly(s.expand(dm), t)
        k = pden.degree()
        # nm/dm coeff of t^face is num_coeff(face+k) / leading_den
        cnum = pnum.coeff_monomial(t ** (face + k)) if face + k >= 0 else 0
        cden = pden.LC()
        val = s.together(cnum / cden)
        coeffs.append((n_val, g0_val, s.factor(val)))
        print(f"  sample n={n_val}, g0={g0_val}, face={face}: {s.factor(val)}")
    return coeffs


c_row1 = leading_coeff(core1, den1, 12 * Nsym - 3 * Gval - 1, "row1 inner at 12n-3G-1")
c_row0 = leading_coeff(core0, den0, 13 * Nsym - 3 * Gval - 1, "row0 inner at 13n-3G-1")
c_row2 = leading_coeff(core2, den2, 11 * Nsym - 3 * Gval - 1, "row2 inner at 11n-3G-1")


# Fit the sample scalars as polynomials in N,G,A0,B0,c0,d0.
def fit_scalar(samples, namescalar):
    # samples: (n, g0, expr in A0,B0,c0,d0)
    # Guess: k * (12n-3G) * A0 * B0^p * (alpha B0^2 c0 + beta d0^2) etc.
    n0, g00, e0 = samples[0]
    print(f"\nfit {namescalar} first sample ratio checks:")
    for n1, g01, e1 in samples[1:]:
        # Compare e1/e0 as rational in A0,... should be 1 if same, or (M(n1)/M(n0))
        if e0 == 0 and e1 == 0:
            print("  both zero")
            continue
        ratio = s.factor(s.together(e1 / e0))
        print(f"  ({n1},{g01})/({n0},{g00}) = {ratio}")
    return e0


print("\n--- ratio tests ---")
fit_scalar(c_row1, "row1")
fit_scalar(c_row0, "row0")
fit_scalar(c_row2, "row2")


# ---------------------------------------------------------------------------
# 6. Closed-form inner coefficients from monomial calculus
# ---------------------------------------------------------------------------
header("6. Closed form of Q-free cores at the cubic faces")

# Reconstruct by dividing out the universal (degree) prefactor.
# Row1 inner face index 12n-3G-1, product degree 12n-3G.
# Expected structure from I3-rewrite:
#   2 A ( -(B^2 c)' + (3/2) (d^2)' ) + rest_Qfree
# Rest still has A' B^2 c, c^3, A' d^2, and Q-free e remnants replaced by B^2/9.

def monomial_coeff_symbolic():
    # Direct Newton: for P = X1...Xk with deg sum D, (P)' coeff at D-1 is D * product tops.
    # We evaluate the Q=0 rational e = B^2/9 - c d/B as a sum of two monomials
    # of DIFFERENT degrees: B^2 at 6n-2G and -cd/B at 6n-G-H = 6n-5G/2.
    # On 2H=3G, 6n-5G/2 > 6n-2G, so e_top = -c d / B  (middle incidence),
    # and B^2/9 is the first subleading of e, at gap G/2.
    #
    # For the cubic face 12n-3G, B^2/9 of e DOES contribute, because
    # A * c * (B^2)' is at 2n+(4n-G)+(6n-2G-1)=12n-3G-1.  Yes!
    # So the monomial-only model with e = e_top t^{6n-H} MISSES this.
    # The Q-substitution with actual polynomial B automatically includes B^2/9.
    #
    # Using e = B^2/9 - c d / B with monomials B,c,d:
    e_mon = B0**2 / 9 * t ** (2 * degB) - (c0 * d0 / B0) * t ** (degc + degd - degB)
    A_m = A0 * t**degA
    B_m = B0 * t**degB
    c_m = c0 * t**degc
    d_m = d0 * t**degd
    # Build row1_body with these explicit monomials (two-term e).
    # Use symbols for derivatives of powers: d/dt t^k = k t^{k-1}.
    # We'll sample as before.
    return e_mon


print("e two-term degrees:")
print("  B^2 term degree =", 2 * degB)
print("  -cd/B term degree =", degc + degd - degB)
print("  difference (should be G/2 = g0) =", s.simplify((degc + degd - degB) - 2 * degB))

# Direct evaluation of full row1_body on two-term e, monomials A,B,c,d.
def eval_row_on_two_term(row_body, face_deg, name, scale):
    A_m = A0 * t**degA
    B_m = B0 * t**degB
    c_m = c0 * t**degc
    d_m = d0 * t**degd
    e_m = B0**2 / 9 * t ** (2 * degB) - (c0 * d0 / B0) * t ** (degc + degd - degB)
    subs_fun = {Af: A_m, Bf: B_m, cf: c_m, df: d_m, ef: e_m}
    samples = [(11, 1), (13, 1), (17, 2), (19, 2), (23, 3)]
    print(f"\n{name} two-term-e monomial samples (after scale):")
    vals = []
    for n_val, g0_val in samples:
        face = int(face_deg.subs({Nsym: n_val, g0: g0_val}))
        expr = row_body.subs(subs_fun).doit()
        expr = s.expand(expr.subs({Nsym: n_val, g0: g0_val}))
        # expr is a Laurent polynomial in t
        expr = s.expand(expr)
        p = s.Poly(s.numer(s.together(expr)), t)
        q = s.Poly(s.denom(s.together(expr)), t)
        k = q.degree()
        cnum = p.coeff_monomial(t ** (face + k))
        val = s.together(scale * cnum / q.LC())
        valf = s.factor(val)
        vals.append((n_val, g0_val, valf))
        print(f"  n={n_val} g0={g0_val} face={face}: {valf}")
    return vals


# Use inner bodies; scale later by -4/27 or 4/27.
v1 = eval_row_on_two_term(row1_body, 12 * Nsym - 3 * Gval - 1, "row1_body", 1)
v0 = eval_row_on_two_term(row0_body, 13 * Nsym - 3 * Gval - 1, "row0_body", 1)
v2 = eval_row_on_two_term(row2_body, 11 * Nsym - 3 * Gval - 1, "row2_body", 1)


def interpolate_prefactor(samples, M_expr_at):
    """samples (n,g0,val).  Guess val = prefactor(n,g0)*homogeneous(A0,B0,c0,d0)."""
    n0, g00, e0 = samples[0]
    print("  sample0 factored =", e0)
    # Strip A0,B0,c0,d0 by dividing by e0 at (A0,B0,c0,d0)=(1,1,1,1) vs generic
    unit = e0.subs({A0: 1, B0: 1, c0: 1, d0: 1})
    form = s.factor(e0)
    print("  unit(A=B=c=d=1) =", unit)
    return form


print("\ninterpolated row1_body face:")
print(" ", interpolate_prefactor(v1, 12 * Nsym - 3 * Gval))
print("interpolated row0_body face:")
print(" ", interpolate_prefactor(v0, 13 * Nsym - 3 * Gval))
print("interpolated row2_body face:")
print(" ", interpolate_prefactor(v2, 11 * Nsym - 3 * Gval))


# ---------------------------------------------------------------------------
# 7. Impose disc + row2 chart on the cubic-face scalars
# ---------------------------------------------------------------------------
header("7. Evaluate cubic-face scalars on the balanced chart")

# From samples, identify the polynomial form by dividing out numbers.
# We'll take sample (n,g0)=(11,1): G=2, H=3, 3G=6<11, faces:
# row1: 12*11-6-1=125; row0: 13*11-6-1=136; row2: 11*11-6-1=114

def on_chart(val):
    # A0,c0,d0,B0 with a = A0 etc, using chart in b,d
    return s.factor(val.subs({A0: a_on_chart, c0: c_from_row2, B0: b, d0: d}))


print("row1_body sample (11,1) on chart:", on_chart(v1[0][2]))
print("row0_body sample (11,1) on chart:", on_chart(v0[0][2]))
print("row2_body sample (11,1) on chart:", on_chart(v2[0][2]))
print("row1_body sample (17,2) on chart:", on_chart(v1[2][2]))
print("row0_body sample (17,2) on chart:", on_chart(v0[2][2]))
print("row2_body sample (17,2) on chart:", on_chart(v2[2][2]))

# Also impose disc only (not row2) to see the factor 4 b c^2 - 9 d e
a_from_disc_only = s.solve(disc, a)[0]
e_from_inc_only = e_from_inc
print("\non disc+incidence only (keep c,d,b):")
sub_di = {A0: a_from_disc_only, B0: b, c0: c, d0: d}
# e is already two-term, so incidence is built in for the top of e.
# Disc: A0 = -3 c0^2 / B0^2
print("  A0 from disc =", a_from_disc_only)
for name, samples in (("row1", v1), ("row0", v0), ("row2", v2)):
    val = samples[0][2].subs({A0: -3 * c0**2 / B0**2})
    print(f"  {name} (11,1) on disc =", s.factor(s.together(val)))
    valb = samples[2][2].subs({A0: -3 * c0**2 / B0**2})
    print(f"  {name} (17,2) on disc =", s.factor(s.together(valb)))


# ---------------------------------------------------------------------------
# 8. Homogeneous surface reduction (Q=0 and I3=0), ratio chart
# ---------------------------------------------------------------------------
header("8. Homogeneous Q=0, I3=0 pullback (middle_surface style)")

# Exact load-free invariants.
e_hom = Bf**2 / 9 - cf * df / Bf
# I3=0 solved for A (from the python discovery file)
A_hom = (
    -s.Rational(2, 3) * Bf * cf / df
    - 3 * cf**2 / Bf**2
    + s.Rational(3, 2) * df / Bf
)
print("A_hom =", A_hom)
print("I3 on (A_hom, e_hom) =", factor_eq(I3.subs({Af: A_hom, ef: e_hom}).doit()))
print("Q on e_hom =", factor_eq(Q.subs(ef, e_hom)))

row1_hom = factor_eq(row1_body.subs({Af: A_hom, ef: e_hom}).doit())
row0_hom = factor_eq(row0_body.subs({Af: A_hom, ef: e_hom}).doit())
row2_hom = factor_eq(row2_body.subs({Af: A_hom, ef: e_hom}).doit())
print("\nrow2_hom =", row2_hom)
print("row1_hom =", row1_hom)
print("row0_hom =", row0_hom)

# Ratio coordinates c = B r, d = B u
rf = s.Function("r")(t)
uf = s.Function("u")(t)
ratio_subs = {
    cf: Bf * rf,
    df: Bf * uf,
}
row2_r = factor_eq(row2_hom.subs(ratio_subs).doit())
row1_r = factor_eq(row1_hom.subs(ratio_subs).doit())
row0_r = factor_eq(row0_hom.subs(ratio_subs).doit())
print("\nratio row2 =", row2_r)
print("ratio row1 =", row1_r)
print("ratio row0 =", row0_r)

Bp, rp, up = s.symbols("Bp rp up")
dsubs = {der(Bf): Bp, der(rf): rp, der(uf): up}
linear = [s.cancel(x.subs(dsubs)) for x in (row2_r, row1_r, row0_r)]
M = s.Matrix([[s.diff(x, v) for v in (Bp, rp, up)] for x in linear])
print("\ndet(row2,row1,row0 / B',r',u') =")
print(s.factor(s.cancel(M.det())))

# On balanced leading-term ratio: r_top = c/b, u_top = d/b, with
# c = -9 d^2/(4 b^2) so r = -9 u^2 / 4   because r = c/b, u=d/b,
# c/b = -9 d^2/(4 b^3) = -9 u^2 /(4 b)  -- NOT homogeneous in ratio!
# Wait: c has weight 4, B weight 3, r = c/B has weight 1.
# d has weight 5, u=d/B weight 2.
# c = -9 d^2 / (4 b^2): weights 4 vs 10-6=4.  In ratios:
# r B = -9 (u B)^2 / (4 B^2) => r = -9 u^2 / 4
# Yes r = -9 u^2 / 4, independent of B.  Good.

print("\nbalanced chart in ratios: r = -9 u^2 / 4")
# Leading monomial B,r,u with degrees:
# B: 3n-g, r: (4n-g)-(3n-g)=n, u: (5n-h)-(3n-g)=2n-h+g
# On 2h=3g: u degree = 2n - 3g/2 + g = 2n - g/2
# r degree = n
# For Newton of the reduced ODE, plug monomials.


# ---------------------------------------------------------------------------
# 9. Load cutoff table
# ---------------------------------------------------------------------------
header("9. Constant-Jacobian load degree table vs cubic faces")

# Degree bounds after D = A B/3 + d:
# A<=2n, B<=3n-g, c<=4n-g, d<=5n-h, e<=6n-h, D<=5n-g
# Load generators from cubicLoad{S,T,U,V}.

n, g, h = s.symbols("n g h", positive=True, integer=True)

print("deg Ul dominated by l A^3 = 6n")
print("deg Tl dominated by l AB, l D = 5n-g")
print("deg Vl dominated by l A^2 B, l A D = 7n-g")
print("deg Sl dominated by l A^2 = 4n")
print("D <= 5n-g, C0 <= 4n, E <= 6n")

print("row1 load terms: Ul D', Tl E', C0 Vl', D Ul'")
print("row0 load terms: Ul E', D Vl'")

# Explicit dominant terms:
print("\nDominant load terms:")
print("  Ul~l A^3 (6n) * D' (5n-g-1) = 11n-g-1")
print("  Tl~l D (5n-g) * E' (6n-1) = 11n-g-1")
print("  C0 (4n) * Vl'~l A^2 B (7n-g-1) = 11n-g-1")
print("  D (5n-g) * Ul'~l A^3 (6n-1) = 11n-g-1")
print("  Ul~l A^3 (6n) * E' (6n-1) = 12n-1   << row0 load naive")
print("  D (5n-g) * Vl'~l A^2 B (7n-g-1) = 12n-2g-1")

print("\nGaps in chamber 3g<n, g<h<2g, 2h=3g:")
print("  (12n-3g-1) - (11n-g-1) = n-2g > g > 0  => row1 cubic face is load-free")
print("  (12n-g-h-1)-(11n-g-1) = n-h > n-2g > 0 => row1 high face is load-free")
print("  row0 naive load 12n-1 vs cubic face 13n-3g-1: (13n-3g-1)-(12n-1)= n-3g+0 >0")
print("    since 3g<n, n-3g>=1, so 12n-1 < 13n-3g-1.  row0 cubic face is load-free")
print("  row0 naive load 12n-1 vs high face 13n-g-h-1=13n-5g/2-1:")
print("    (13n-5g/2-1)-(12n-1)= n-5g/2.  Need n>5g/2, true because n>3g>5g/2.")
print("    so row0 HIGH face is also load-free under 3g<n.")

# I3 / I4 load cutoffs already in Lean: I4 load < 9n-3g, I3 load < 10n-3g.

print("\nI4 load < 9n-3g  (Lean cubicFace cutoff): Q itself < 9n-3g")
print("I3 load < 10n-3g (Lean cubicFace cutoff): residual I3 < 10n-3g")
print("Disc polynomial after a*b^2+3*c^2=0: < 8n-2g")
print("Cubic defect R < 13n-4g (Lean)")
print("On 2h=3g, Disc participating index 8n-4g+h = 8n-5g/2")
print("  drop from 8n-2g is g/2; R face forces Disc_(8n-5g/2)=3*b*d")


# ---------------------------------------------------------------------------
# 10. Identify exact row1 scalar by reconstructing from samples + disc
# ---------------------------------------------------------------------------
header("10. Exact cubic-face scalars (inner bodies)")

# From disc-only samples, factor in B0,c0,d0.
print("row1 (11,1) raw =", v1[0][2])
print("row1 (11,1) disc =", s.factor(s.together(v1[0][2].subs(A0, -3 * c0**2 / B0**2))))
print("row2 (11,1) raw =", v2[0][2])
print("row2 (11,1) disc =", s.factor(s.together(v2[0][2].subs(A0, -3 * c0**2 / B0**2))))
print("row0 (11,1) raw =", v0[0][2])
print("row0 (11,1) disc =", s.factor(s.together(v0[0][2].subs(A0, -3 * c0**2 / B0**2))))

# Closed form guesses from Newton:
# Row2 inner on disc, Q-rewrite: -8/3 * M11 * a * b^3 + -18 * M11 * d * e_top
# with e_top = -c d / b, a = -3 c^2 / b^2:
# = M11 * [ -8/3 (-3 c^2/b^2) b^3 - 18 d (-c d/b) ]
# = M11 * [ 8 c^2 b + 18 c d^2 / b ]
# = M11 * (2 c / b) * (4 b^2 c + 9 d^2)
# Then residual row2 = -4/27 * inner, and Lean says
# (-8/27)*M11*(4 b c^2 - 9 d e) which with e=-cd/b is
# (-8/27)*M11*(4 b c^2 + 9 c d^2 / b) = (-8/27)*M11*(c/b)*(4 b^2 c + 9 d^2)
# inner would be (-4/27)^{-1} times that = (8/3)*M11*(c/b)*(4 b^2 c+9 d^2)
# mismatch check against samples.

print("\nPredicted row2_body on disc+two-term e:")
M11s = 11 * Nsym - 3 * Gval
e_top_pred = -c0 * d0 / B0
pred2 = (
    -s.Rational(8, 3) * M11s * (-3 * c0**2 / B0**2) * B0**3
    + -18 * M11s * d0 * e_top_pred
)
pred2 = s.factor(s.together(pred2))
print(" ", pred2)
print(" sample (11,1) pred =", s.factor(pred2.subs({Nsym: 11, g0: 1})))
print(" sample (11,1) got  =", s.factor(s.together(v2[0][2].subs(A0, -3 * c0**2 / B0**2))))

# Row0 inner predicted:
# (2n) A0 * ( -A0 B0^3 /9 + B0 c0^2 - 3 d0 e_top )
M13s = 13 * Nsym - 3 * Gval
pred0 = (2 * Nsym) * A0 * (
    -A0 * B0**3 / 9 + B0 * c0**2 - 3 * d0 * e_top_pred
)
print("\nPredicted row0_body (Q-rewrite, leading A,B,c,d,e_top):")
print(" ", s.factor(s.together(pred0)))
print(" sample (11,1) pred =", s.factor(pred0.subs({Nsym: 11, g0: 1, A0: -3 * c0**2 / B0**2})))
print(" sample (11,1) got  =", s.factor(s.together(v0[0][2].subs(A0, -3 * c0**2 / B0**2))))
print(" sample (11,1) pred raw A =", s.factor(pred0.subs({Nsym: 11, g0: 1})))
print(" sample (11,1) got raw    =", v0[0][2])

# Row1 prediction from I3-rewrite + remaining core.
# high1_rewritten with I3=0: 2 A ( -(B^2 c)' + 3/2 (d^2)' )
# coeff: 2 A0 * ( -(10n-3G) B0^2 c0 + (3/2)(10n-2H) d0^2 ) = 2 A0 (10n-3G) (-B0^2 c0 + 3/2 d0^2)
# rest1 at this face: -2 A' B^2 c + 3 A' d^2 + 6 (c^2 c') + Q-free e terms
# A' B^2 c coeff: -2 * (2n) A0 * B0^2 c0
# 3 A' d^2: 3 * (2n) A0 * d0^2
# 6 c^2 c': 6 * (4n-G) c0^3
# e terms: -3 B^2 e' + 3 B (cd)' + 9 B' cd -18 e e'
# with two-term e.

M10 = 10 * Nsym - 3 * Gval
pred1_I3high = 2 * A0 * M10 * (-(B0**2) * c0 + s.Rational(3, 2) * d0**2)
pred1_Aprime = -2 * (2 * Nsym) * A0 * B0**2 * c0 + 3 * (2 * Nsym) * A0 * d0**2
pred1_c3 = 6 * (4 * Nsym - Gval) * c0**3
print("\nPartial row1 predictions (missing Q-free e block):")
print("  I3-high =", s.factor(pred1_I3high))
print("  A' block =", s.factor(pred1_Aprime))
print("  c^3 =", s.factor(pred1_c3))
partial = pred1_I3high + pred1_Aprime + pred1_c3
print("  sum =", s.factor(s.together(partial)))
print("  sample (11,1) partial =", s.factor(partial.subs({Nsym: 11, g0: 1})))
print("  sample (11,1) got     =", v1[0][2])
print("  difference at (11,1)  =", s.factor(s.together(
    v1[0][2] - partial.subs({Nsym: 11, g0: 1})
)))


# ---------------------------------------------------------------------------
# 11. Linear algebra identity search for row1 Q-free core
# ---------------------------------------------------------------------------
header("11. Match row1 cubic-face inner against a,b,c,d monomials")

# Generic linear combination of face monomials at 12n-3G-1:
# A' B^2 c, A (B^2 c)', A' d^2, A (d^2)', (c^3)', (B^4)', A B^3 B' types,
# B^2 (B^2)', c (B^3)', etc. from e = B^2/9 - cd/B.
#
# Use the sample values as a linear form:
# alpha1 * (2n) A0 B0^2 c0 + alpha2 * (10n-3G) A0 B0^2 c0
# + beta1 * (2n) A0 d0^2 + beta2 * (10n-3G) A0 d0^2
# + gamma * (4n-G) c0^3
# + delta * (6n-2G) B0^4   (from B^2 * (B^2)' type)
# + eps * (3n-G) A0 B0^3 something wait A is 2n, B^4 is 12n-4G, not 12n-3G.
# B^4 degree 12n-4G, too low by G.
# A B^3: 2n+9n-3G=11n-3G, too low by n.
# So the only monomials of product degree 12n-3G from A,B,c,d with
# deg A=2n, B=3n-G, c=4n-G, d=5n-3G/2:
#   A * B^2 * c : 2n + 6n-2G + 4n-G = 12n-3G
#   A * d^2     : 2n + 10n-3G = 12n-3G
#   c^3         : 12n-3G
#   B * c * d   : 3n-G+4n-G+5n-3G/2 = 12n-7G/2  too low by G/2
#   B^2 * e_top : e_top at 6n-3G/2, B^2 at 6n-2G: 12n-7G/2 too low
#   e_top^2     : 12n-3G  YES  (e_top = -c d/B, degree 6n-3G/2, square 12n-3G)
#   B^2 * (B^2/9) : 6n-2G + 6n-2G = 12n-4G too low
#   e_top * (B^2/9): (6n-3G/2)+(6n-2G)=12n-7G/2 too low
#
# So monomials at the face: A B^2 c, A d^2, c^3, e_top^2 = c^2 d^2 / B^2
# and mixed derivative distributions.

# Fit:
# row1_body coeff = p*(2n)*A0*B0^2*c0 + q*(10n-3G)*A0*B0^2*c0
#                 + r*(2n)*A0*d0^2 + s*(10n-3G)*A0*d0^2
#                 + u*(4n-G)*c0^3
#                 + v*(12n-3G)* (c0^2 d0^2 / B0^2)
#                 + w*(2n)*A0*(c0^2 d0^2 / B0^2)/A0 wait no
# e e' contributes (12n-3G) e_top^2.

samples_for_fit = v1
# Use (11,1) and (17,2) as two degree points, plus monomial independence.

def eval_form(n_val, g0_val, coeffs):
    p, q, r, s_, u, v = coeffs
    Nv, Gv = n_val, 2 * g0_val
    return (
        p * (2 * Nv) * A0 * B0**2 * c0
        + q * (10 * Nv - 3 * Gv) * A0 * B0**2 * c0
        + r * (2 * Nv) * A0 * d0**2
        + s_ * (10 * Nv - 3 * Gv) * A0 * d0**2
        + u * (4 * Nv - Gv) * c0**3
        + v * (12 * Nv - 3 * Gv) * (c0**2 * d0**2 / B0**2)
    )

# Solve using polynomial identity at two samples by comparing coefficients
# of A0 B0^2 c0, A0 d0^2, c0^3, c0^2 d0^2 / B0^2.
mons = [
    A0 * B0**2 * c0,
    A0 * d0**2,
    c0**3,
    c0**2 * d0**2 / B0**2,
]


def coeff_vec(expr):
    expr = s.together(s.expand(expr))
    # multiply by B0^2 to clear
    cleared = s.expand(s.together(expr * B0**2))
    # cleared is polynomial in A0,B0,c0,d0
    return [
        s.expand(s.together(expr)).subs({A0: 1, B0: 1, c0: 1, d0: 0})  # dummy
    ]


# Direct: expand v1[0][2] * B0**2 and match monomials.
def monomials_of(expr):
    cleared = s.expand(s.together(expr * B0**2))
    p = s.Poly(cleared, A0, B0, c0, d0)
    return p


print("\nCleared row1 (11,1) monomials:")
P11 = monomials_of(v1[0][2])
print(P11.as_expr())
print("Cleared row1 (17,2) monomials:")
P17 = monomials_of(v1[2][2])
print(P17.as_expr())

# So row1_body * B0^2 is a polynomial.  Divide back.
print("\nrow1 (11,1) as rational =", s.factor(s.together(v1[0][2])))
print("row1 (17,2) as rational =", s.factor(s.together(v1[2][2])))
print("row1 (13,1) as rational =", s.factor(s.together(v1[1][2])))
print("row1 (23,3) as rational =", s.factor(s.together(v1[4][2])))

print("\nrow0 (11,1) as rational =", s.factor(s.together(v0[0][2])))
print("row0 (17,2) as rational =", s.factor(s.together(v0[2][2])))
print("row2 (11,1) as rational =", s.factor(s.together(v2[0][2])))
print("row2 (17,2) as rational =", s.factor(s.together(v2[2][2])))


# ---------------------------------------------------------------------------
# 12. Final chart evaluation including residual scale -4/27, +4/27
# ---------------------------------------------------------------------------
header("12. Residual-row cubic-face coefficients on the balanced chart")

scale2 = -s.Rational(4, 27)
scale1 = -s.Rational(4, 27)
scale0 = s.Rational(4, 27)

print("residual row2 (11,1) on disc+row2-chart:",
      s.factor(scale2 * on_chart(v2[0][2])))
print("residual row1 (11,1) on disc+row2-chart:",
      s.factor(scale1 * on_chart(v1[0][2])))
print("residual row0 (11,1) on disc+row2-chart:",
      s.factor(scale0 * on_chart(v0[0][2])))
print("residual row2 (17,2) on chart:", s.factor(scale2 * on_chart(v2[2][2])))
print("residual row1 (17,2) on chart:", s.factor(scale1 * on_chart(v1[2][2])))
print("residual row0 (17,2) on chart:", s.factor(scale0 * on_chart(v0[2][2])))

# Nonvanishing of prefactors: 11n-3g, 12n-3g, 13n-3g, n, a, b, c, d
print("\nPrefactor nonvanishing in 3G<n, char 0:")
print("  11n-3G >= 11n-n =10n >0")
print("  12n-3G >0, 13n-3G>0, n>0")
print("  a,b,c,d,e nonzero on the selected middle face")

header("13. Contradiction summary")
print("On disc + incidence + row2, with c = -9 d^2/(4 b^2):")
print("  residual row2 cubic face = 0")
print("  residual row0 cubic face = 0")
print("  residual row1 cubic face = (27/2) (14 n - 3 g) d^6 / b^6")
print("  nonzero in char 0 for b,d != 0 and 3 g < n")
print("Cubic defect is not required: it only forces Disc_(8n-4g+h) = 3 b d.")
print("\nDONE")
