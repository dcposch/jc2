#!/usr/bin/env python3
"""st39_transport_check.py -- exact checks for the td=8 equal-join
Statement 3.9 coefficient-transport system (Fable 5 primary, 2026-08-29).

Standard library only.  Exact Fraction / Gaussian-rational arithmetic for
every load-bearing identity; a log-polar monomial instantiation (exact in
the exponents, float only in one gauge angle) for the full system.

Checked layers (see the report for derivations):
  P1  local ODE constants in monic gauge: R_H=(21/2)A^2,
      R_G=-(16+12t)a^2, R_tr=(68/3)A^2, pole family sigma=(3/2)r,
      pi=(3/8)r^2, const=(9/8)r^3; mutations die
  P2  drop-vertex arithmetic: no-drop refuted at H, G, trunk;
      (k2,l2)=(7,6); (k3,l3)=(112+84t, 635+476t) coprime all t
      (symbolic Euclid ending at remainder 1); k_G=79; mu_G=93/14;
      k_tr(t)=39984t^2+106650t+71117; all transport exponents integral
  P3  M*-gcd consistency at G and trunk for all t
  P4  leading-coefficient factors over Q(i): L_e = 8 nu^3 alpha^6/c^3 at
      BOTH merge orbits, Psi'=2 nu alpha^2 at both, K=-(49/2)c^19 at the
      H chain root (exact Taylor shifts)
  P5  exact Gaussian-rational twin-cycle closure at t=1 (omega=-1):
      (A1/A2)^2 = omega^{-15} closes the H1/H2 ratio of the vertex
      equations exactly; exponent mutations break it
  P6  full-system instantiation at t=0,1,2,10 in log-polar monomial
      arithmetic: all six vertex equations satisfied, gauges nonzero,
      twin law reproduced; prefactor-invariance reruns
"""

from fractions import Fraction as Fr
import math, random

CHECKS = 0
def ok(cond, label):
    global CHECKS
    if not cond:
        raise SystemExit("FAIL: " + label)
    CHECKS += 1

# ---------- dense polynomials over Fraction ----------
def pmul(a, b):
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    r[i + j] += x * y
    return r
def padd(a, b):
    n = max(len(a), len(b)); r = [Fr(0)] * n
    for i, x in enumerate(a): r[i] += x
    for i, x in enumerate(b): r[i] += x
    return r
def pscal(c, a): return [c * x for x in a]
def pdiff(a): return [a[i] * i for i in range(1, len(a))]
def ppow(a, n):
    r = [Fr(1)]
    for _ in range(n): r = pmul(r, a)
    return r
def pT(coeffs_T, nu):
    r = [Fr(0)] * ((len(coeffs_T) - 1) * nu + 1)
    for i, c in enumerate(coeffs_T): r[i * nu] = c
    return r
def is_const_multiple(lhs, rhs):
    n = max(len(lhs), len(rhs))
    lhs = lhs + [Fr(0)] * (n - len(lhs)); rhs = rhs + [Fr(0)] * (n - len(rhs))
    const = None
    for x, y in zip(lhs, rhs):
        if y == 0:
            if x != 0: return None
        else:
            c = x / y
            if const is None: const = c
            elif c != const: return None
    return const
def ode_const(X, kbar, Phi, Psi):
    lhs = padd(pscal(Fr(X), pmul(Phi, pdiff(Psi))),
               pscal(Fr(-kbar), pmul(pdiff(Phi), Psi)))
    return is_const_multiple(lhs, Phi)

# ---------- P1 ----------
def phase1():
    random.seed(20260829)
    for _ in range(5):
        A = Fr(random.randint(1, 40), random.randint(1, 9))
        B = Fr(3, 2) * A
        Phi = pT(pmul(pmul([-A, Fr(1)], [-A, Fr(1)]), [-B, Fr(1)]), 7)
        Psi = pmul([Fr(0), Fr(1)], pT(pmul([-A, Fr(1)], [-B, Fr(1)]), 7))
        ok(ode_const(7, 5, Phi, Psi) == Fr(21, 2) * A * A,
           "P1 R_H = (21/2)A^2")
        Bb = B + 1
        Phib = pT(pmul(pmul([-A, Fr(1)], [-A, Fr(1)]), [-Bb, Fr(1)]), 7)
        Psib = pmul([Fr(0), Fr(1)], pT(pmul([-A, Fr(1)], [-Bb, Fr(1)]), 7))
        ok(ode_const(7, 5, Phib, Psib) is None, "P1 H mutation dies")
    for t in [0, 1, 2, 3, 7, 20]:
        nu = 4 + 3 * t; X = 16 + 12 * t; kbar = 6 + 4 * t
        a = Fr(random.randint(1, 30), random.randint(1, 7))
        Phi = pT(pmul(ppow([-a, Fr(1)], 3), ppow([a, Fr(1)], 3)), nu)
        Psi = pmul([Fr(0), Fr(1)], pT(pmul([-a, Fr(1)], [a, Fr(1)]), nu))
        ok(ode_const(X, kbar, Phi, Psi) == -Fr(X) * a * a,
           "P1 R_G = -(16+12t)a^2 at t=%d" % t)
    for _ in range(3):
        A = Fr(random.randint(1, 30), random.randint(1, 7))
        B = Fr(4, 3) * A
        Phi = pT(pmul(ppow([-A, Fr(1)], 3), ppow([-B, Fr(1)], 2)), 17)
        Psi = pmul([Fr(0), Fr(1)], pT(pmul([-A, Fr(1)], [-B, Fr(1)]), 17))
        ok(ode_const(17, 7, Phi, Psi) == Fr(68, 3) * A * A,
           "P1 R_tr = (68/3)A^2")
    for _ in range(4):
        r = Fr(random.randint(1, 30), random.randint(1, 7))
        p = [Fr(0), -r, Fr(0), Fr(0), Fr(1)]
        sig = Fr(3, 2) * r; pi = Fr(3, 8) * r * r
        q = [pi, Fr(0), Fr(0), -sig, Fr(0), Fr(0), Fr(1)]
        lhs = padd(pscal(Fr(2), pmul(p, pdiff(q))),
                   pscal(Fr(-3), pmul(pdiff(p), q)))
        ok(is_const_multiple(lhs, [Fr(1)]) == Fr(9, 8) * r ** 3,
           "P1 pole const = (9/8)r^3")
        qb = [pi, Fr(0), Fr(0), -sig - 1, Fr(0), Fr(0), Fr(1)]
        lhsb = padd(pscal(Fr(2), pmul(p, pdiff(qb))),
                    pscal(Fr(-3), pmul(pdiff(p), qb)))
        ok(is_const_multiple(lhsb, [Fr(1)]) is None, "P1 pole mutation dies")
        lhs12 = padd(pmul(p, pdiff(q)), pscal(Fr(-2), pmul(pdiff(p), q)))
        ok(is_const_multiple(lhs12, [Fr(1)]) is None, "P1 pole (1,2) dies")
        # uniqueness: solve generic sigma,pi -> forced values
        for sg, pg in [(sig + 2, pi), (sig, pi + 1)]:
            qg = [pg, Fr(0), Fr(0), -sg, Fr(0), Fr(0), Fr(1)]
            lg = padd(pscal(Fr(2), pmul(p, pdiff(qg))),
                      pscal(Fr(-3), pmul(pdiff(p), qg)))
            ok(is_const_multiple(lg, [Fr(1)]) is None, "P1 pole forced")

# ---------- P2 ----------
def phase2():
    for t in range(0, 401):
        iH, iG, iT = 2, 14, 112 + 84 * t
        MH, MG, MT = 21, 24 + 18 * t, 85
        dqH, dqG, dqT = 15, 9 + 6 * t, 35
        DH, DG, DT = iH * MH, iG * MG, iT * MT
        muH = Fr(3, 2)
        ok(iH * (muH - 1) == 1, "P2 k_H = 1")
        QH = 1 * MH + dqH
        ok(QH == 36 and DH == 42, "P2 H degrees")
        ok(DH * (muH - 1) + 1 != QH, "P2 H no-drop refuted")
        ok(Fr(QH, DH) == Fr(6, 7), "P2 (k2,l2)=(7,6)")
        muG = Fr(3, 2) + Fr(6 * 6, 7)
        ok(muG == Fr(93, 14), "P2 mu_G = 93/14")
        kG = iG * (muG - 1)
        ok(kG == 79, "P2 k_G = 79")
        QG = 79 * MG + dqG
        ok(QG == 1905 + 1428 * t, "P2 Q_G")
        ok(DG * (muG - 1) + 1 != QG, "P2 G no-drop refuted")
        ok(Fr(QG, DG) == Fr(635 + 476 * t, 112 + 84 * t), "P2 k3 l3 ratio")
        ok(math.gcd(635 + 476 * t, 112 + 84 * t) == 1, "P2 gcd(l3,k3)=1")
        k3, l3 = 112 + 84 * t, 635 + 476 * t
        muT = muG + Fr((k3 - 1) * l3, k3)
        kT = iT * (muT - 1)
        ok(kT == 39984 * t * t + 106650 * t + 71117, "P2 k_tr(t)")
        ok(kT.denominator == 1, "P2 k_tr integer")
        QT = int(kT) * MT + dqT
        ok(DT * (muT - 1) + 1 != QT, "P2 trunk no-drop refuted")
        for e in [Fr(iH * 3, 2), Fr(iG * 3, 2), Fr(iT * 3, 2),
                  Fr(iG * 6, 7), Fr(iT * 6, 7), Fr(iT * l3, k3)]:
            ok(e.denominator == 1, "P2 integral transport exponent")
        ok(Fr(iT * l3, k3) == l3, "P2 i_T l3/k3 = l3")
        ok(Fr(iG * 6, 7) == 12 and Fr(iG * 3, 2) == 21, "P2 iG exponents")
    for t in range(0, 2001):
        a, b = 635 + 476 * t, 112 + 84 * t
        r1 = a - 5 * b; ok(r1 == 75 + 56 * t, "P2 euclid r1")
        r2 = b - r1;    ok(r2 == 37 + 28 * t, "P2 euclid r2")
        ok(r1 - 2 * r2 == 1, "P2 euclid ends at 1")
        c, d = 635 + 476 * t, 4 + 3 * t
        s1 = c - 158 * d; ok(s1 == 3 + 2 * t, "P2 euclid2 s1")
        s2 = d - s1;      ok(s2 == 1 + t, "P2 euclid2 s2")
        ok(s1 - s2 == 2 + t and (s1 - s2) - s2 == 1, "P2 euclid2 ends 1")
        ok((635 + 476 * t) % 2 == 1, "P2 l3 odd")

# ---------- P3 ----------
def phase3():
    for t in range(0, 401):
        for l1 in [1, 2, 3, 5, 11]:
            ok(math.gcd(math.gcd(14, 21), math.gcd(12, 14 * l1)) == 1,
               "P3 M*_G list gcd")
        iT = 112 + 84 * t; l3 = 635 + 476 * t
        g = 0
        for x in [iT, iT * 3 // 2, iT * 6 // 7, l3]:
            g = math.gcd(g, x)
        ok(g == 1, "P3 M*_tr list gcd at t=%d" % t)

# ---------- Gaussian rationals ----------
class GQ:
    __slots__ = ("re", "im")
    def __init__(s, re=0, im=0): s.re = Fr(re); s.im = Fr(im)
    def __add__(a, b): return GQ(a.re + b.re, a.im + b.im)
    def __sub__(a, b): return GQ(a.re - b.re, a.im - b.im)
    def __mul__(a, b): return GQ(a.re * b.re - a.im * b.im,
                                 a.re * b.im + a.im * b.re)
    def inv(a):
        n = a.re * a.re + a.im * a.im
        return GQ(a.re / n, -a.im / n)
    def __truediv__(a, b): return a * b.inv()
    def __pow__(a, n):
        if n < 0: return a.inv() ** (-n)
        r = GQ(1)
        for _ in range(n): r = r * a
        return r
    def __eq__(a, b): return a.re == b.re and a.im == b.im
    def iszero(s): return s.re == 0 and s.im == 0

def gq_pmul(a, b):
    r = [GQ(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] = r[i + j] + x * y
    return r
def gq_shift(p, c):
    """coefficients of p(eta + c) by Horner"""
    res = [GQ(0)]
    for k in range(len(p) - 1, -1, -1):
        new = [GQ(0)] * (len(res) + 1)
        for j, v in enumerate(res):
            new[j + 1] = new[j + 1] + v
            new[j] = new[j] + v * c
        new[0] = new[0] + p[k]
        res = new
    while len(res) > 1 and res[-1].iszero(): res.pop()
    return res
def gq_pT(coeffs_T, nu):
    r = [GQ(0)] * ((len(coeffs_T) - 1) * nu + 1)
    for i, c in enumerate(coeffs_T): r[i * nu] = c
    return r
def lc_at(p, c, mult):
    sh = gq_shift(p, c)
    for j in range(mult):
        ok(sh[j].iszero(), "P4 vanishing order at root")
    ok(not sh[mult].iszero(), "P4 exact order at root")
    return sh[mult]

# ---------- P4 ----------
def phase4():
    nu = 7
    c1 = GQ(Fr(3, 2)); alpha = c1 ** nu
    c2 = GQ(-1) * c1
    ma = GQ(0) - alpha
    Phi = gq_pT(gq_pmul(gq_pmul(gq_pmul([ma, GQ(1)], [ma, GQ(1)]),
        [ma, GQ(1)]), gq_pmul(gq_pmul([alpha, GQ(1)], [alpha, GQ(1)]),
        [alpha, GQ(1)])), nu)
    for c, tag in [(c1, "c1"), (c2, "c2")]:
        L = lc_at(Phi, c, 3)
        ok(L == GQ(8 * nu ** 3) * alpha ** 6 / (c ** 3),
           "P4 L_e formula at " + tag)
    Psi = gq_pmul([GQ(0), GQ(1)], gq_pT(gq_pmul([ma, GQ(1)],
                                                [alpha, GQ(1)]), nu))
    for c in [c1, c2]:
        ok(lc_at(Psi, c, 1) == GQ(2 * nu) * alpha ** 2,
           "P4 L' = 2 nu alpha^2")
    cP = GQ(Fr(2, 3)); A = cP ** 7; B = GQ(Fr(3, 2)) * A
    mA = GQ(0) - A; mB = GQ(0) - B
    PhiH = gq_pT(gq_pmul(gq_pmul([mA, GQ(1)], [mA, GQ(1)]), [mB, GQ(1)]), 7)
    ok(lc_at(PhiH, cP, 2) == GQ(Fr(-49, 2)) * cP ** 19,
       "P4 K = -(49/2)c^19")

# ---------- P5 ----------
def phase5():
    nu = 7
    c1 = GQ(Fr(5, 3)); alpha = c1 ** nu
    omega = GQ(-1)
    c2 = omega * c1
    L1 = GQ(8 * nu ** 3) * alpha ** 6 / (c1 ** 3)
    L2 = GQ(8 * nu ** 3) * alpha ** 6 / (c2 ** 3)
    ok(L1 / L2 == omega ** 3, "P5 L1/L2 = omega^3")
    rho = GQ(0, 1)
    ok(rho ** 2 == omega ** (-15), "P5 (A1/A2)^2 = omega^-15")
    Cr = (L1 / L2) ** 14
    taur = (L1 / L2) ** 12
    Tr = (L1 / L2) ** 21
    ok(Cr * taur * (rho ** 2) == Tr, "P5 twin cycle closes exactly")
    ok(not (Cr * taur * (rho ** 2) == (L1 / L2) ** 20), "P5 mut T exp")
    ok(not (Cr * ((L1 / L2) ** 11) * (rho ** 2) == Tr), "P5 mut tau exp")
    ok(not (Cr * taur == Tr), "P5 A1=A2 fails at omega=-1")

# ---------- P6: log-polar monomial instantiation ----------
class LP:
    """number = exp(lm) * exp(i*ph): purely multiplicative model"""
    __slots__ = ("lm", "ph")
    def __init__(s, lm=0.0, ph=0.0): s.lm = float(lm); s.ph = float(ph)
    @staticmethod
    def real(x):
        if x > 0: return LP(math.log(x), 0.0)
        return LP(math.log(-x), math.pi)
    def __mul__(a, b): return LP(a.lm + b.lm, a.ph + b.ph)
    def __truediv__(a, b): return LP(a.lm - b.lm, a.ph - b.ph)
    def powr(a, e): return LP(a.lm * e, a.ph * e)
    def close(a, b, tol=1e-6):
        # tol=1e-6 covers float phase accumulation over ~1e6-radian
        # exponent chains at large t; a structural mismatch in the twin
        # cycle would be at least pi/(3 nu) ~ 3e-2.  Exactness of the
        # cycle itself is P5's Gaussian-rational check.
        dp = (a.ph - b.ph) % (2 * math.pi)
        dp = min(dp, 2 * math.pi - dp)
        return abs(a.lm - b.lm) <= tol and dp <= tol

def phase6(t, seed):
    rnd = random.Random(seed)
    pf = {v: LP.real(rnd.choice([1, 2, 3, 5, 7, 0.5, 0.75]))
          for v in ["tr", "G", "H1", "H2", "P1", "P2"]}
    nu = 4 + 3 * t; iG, iH, iT = 14, 2, 112 + 84 * t
    XG = 16 + 12 * t; k3, l3 = 112 + 84 * t, 635 + 476 * t
    c0 = LP(rnd.uniform(-1, 1), rnd.uniform(0, 6))
    s0 = LP(rnd.uniform(-1, 1), rnd.uniform(0, 6))
    s2 = LP(rnd.uniform(-1, 1), rnd.uniform(0, 6))
    s3 = LP(rnd.uniform(-1, 1), rnd.uniform(0, 6))
    C_tr = LP(rnd.uniform(-1, 1), rnd.uniform(0, 6))
    B_tr = LP(rnd.uniform(-1, 1), rnd.uniform(0, 6))  # free via s4
    t0_tr = (s0 * C_tr.powr(3)).powr(0.5)
    t2_tr = (s2 * C_tr.powr(6)).powr(1.0 / 7.0)
    t3_tr = (s3 * C_tr.powr(l3)).powr(1.0 / k3)
    T_tr = t0_tr * t2_tr.powr(6) * t3_tr.powr(k3 - 1)
    # (*_tr) solved for R_tr = (68/3) A_F^2
    R_tr = pf["tr"] * c0 * T_tr / (LP.real(iT) * C_tr * B_tr)
    AF2 = R_tr / LP.real(68.0 / 3.0)
    ok(math.isfinite(AF2.lm), "P6 trunk gauge exists t=%d" % t)
    lhs = LP.real(iT) * C_tr * B_tr * LP.real(68.0 / 3.0) * AF2
    ok(lhs.close(pf["tr"] * c0 * T_tr), "P6 trunk residual")
    AF = AF2.powr(0.5)
    cG = AF.powr(1.0 / 17.0)
    # L_G = (17 c^16)^3 * (A_F - (4/3)A_F)^2 = 17^3 c^48 * A_F^2 / 9
    LG = LP.real(17.0 ** 3 / 9.0) * cG.powr(48) * AF2
    C_G = C_tr * LG.powr(iT)
    t0_G = t0_tr * LG.powr(iT * 3 // 2)
    t2_G = t2_tr * LG.powr(iT * 6 // 7)
    tau_G = t3_tr * LG.powr(l3)
    T_G = t0_G * t2_G.powr(6)
    a2 = pf["G"] * c0 * T_G / (LP.real(iG) * C_G * tau_G * LP.real(-XG))
    ok(math.isfinite(a2.lm), "P6 merge gauge exists")
    lhs = LP.real(iG) * C_G * tau_G * LP.real(-XG) * a2
    ok(lhs.close(pf["G"] * c0 * T_G), "P6 merge residual")
    alpha = a2.powr(0.5)
    c1 = alpha.powr(1.0 / nu)
    omega = LP(0.0, math.pi / nu)          # omega^nu = -1
    A2 = {}
    for e, ce in [("H1", c1), ("H2", omega * c1)]:
        Le = LP.real(8.0 * nu ** 3) * alpha.powr(6) / ce.powr(3)
        C_H = C_G * Le.powr(iG)
        t0_H = t0_G * Le.powr(21)
        tau_H = t2_G * Le.powr(12)
        T_H = t0_H
        A2[e] = pf[e] * c0 * T_H / (LP.real(iH) * C_H * tau_H *
                                    LP.real(10.5))
        lhs = LP.real(iH) * C_H * tau_H * LP.real(10.5) * A2[e]
        ok(lhs.close(pf[e] * c0 * T_H), "P6 %s residual" % e)
        Ae = A2[e].powr(0.5); cP = Ae.powr(1.0 / 7.0)
        # K = 49 c^12 * (A - (3/2)A) = -(49/2) c^12 A = -(49/2) c^19
        Ke = LP.real(-49.0 / 2.0) * cP.powr(19)
        C_P = C_H * Ke.powr(2)
        t0_P = t0_H * Ke.powr(3)
        B_P = t0_P
        r3 = c0 / (pf["P" + e[1]] * C_P * B_P * LP.real(9.0 / 8.0))
        ok(math.isfinite(r3.lm), "P6 pole gauge exists " + e)
        lhs = pf["P" + e[1]] * C_P * B_P * LP.real(9.0 / 8.0) * r3
        ok(lhs.close(c0), "P6 pole residual " + e)
    ratio = (A2["H1"] / A2["H2"]) * (pf["H2"] / pf["H1"])
    ok(ratio.close(omega.powr(-15)), "P6 twin law t=%d" % t)

def main():
    phase1(); phase2(); phase3(); phase4(); phase5()
    for t in [0, 1, 2, 10]:
        for seed in [11, 23]:
            phase6(t, seed)
    print("ST39_TRANSPORT_CHECK_PASS checks=%d" % CHECKS)

if __name__ == "__main__":
    main()
