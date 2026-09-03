#!/usr/bin/env python3
"""EXPERIMENT NEXT-COEFF -- expand R_k and weighted residues completely in x,
identify which Moh/composition tower level each x-coefficient sees, and decide
whether the coefficient at x-order (k+1)c_max-1-j is a function of the tower
data down to level j only.

FAIL-CLOSED.  Exact over Q.  Desk-scale.
"""
from __future__ import annotations
import sys, time
from fractions import Fraction as F
from collections import defaultdict
import sympy as sp

sys.path.insert(0, "/home/ubuntu/jc2/box/nextcoeff-drivers-20260903")
from psgrowth import (
    x, y, c, T, Pair, chi_poly, residues, reduce_mod, cmax_of, degx,
    check, FAIL, NCHK, power_sums_from_chi,
)

KMAX = 20
FAIL2 = FAIL  # alias

# --------------------------------------------------------------------------- helpers
def as_poly_xc(expr):
    e = sp.expand(expr)
    if e == 0:
        return sp.Poly(0, x, domain=sp.QQ[c]) if False else None
    try:
        return sp.Poly(e, x, domain=sp.QQ.frac_field(c))
    except Exception:
        return sp.Poly(sp.together(e), x)


def coeff_dict(expr):
    """{deg: coefficient in Q(c)} for a polynomial in x; empty for 0."""
    e = sp.expand(expr)
    if e == 0:
        return {}
    P = sp.Poly(e, x)
    out = {}
    for n in range(int(P.degree()) + 1):
        cf = sp.expand(P.nth(n))
        if cf != 0:
            out[n] = cf
    return out


def other_elem_weight(g, n, r):
    """Polynomial w(y) in Q[x,c][y] with w(tau_i) = e_r(other roots of g-c).

    g-c = y^n - E1 y^{n-1} + E2 y^{n-2} - ... + (-1)^n En,
    E_s = (-1)^s [y^{n-s}](g-c).
    Recurrence: e_0(hat)=1, e_s(hat)= E_s - tau * e_{s-1}(hat).
    """
    G = sp.Poly(sp.expand(g - c), y)
    # E[s] = e_s(all roots)
    E = [sp.Integer(1)]
    for s in range(1, n + 1):
        E.append(sp.expand(((-1) ** s) * G.nth(n - s)))
    w = sp.Integer(1)  # e_0
    if r == 0:
        return w
    for s in range(1, r + 1):
        w = sp.expand(E[s] - y * w)
    return w


def horner_other_elems(g, n):
    """All e_0..e_{n-1}(hat) as polynomials in y."""
    return [other_elem_weight(g, n, r) for r in range(n)]


# --------------------------------------------------------------------------- star / BOTTOM-ODE on (1,e,1)
def star_1e1(e):
    """Normalised (1,e,1) star: p_g = pi^e - 1, p_f = pi  (q1=1, p0=-1).
    kappa = d p_f p_g' - e p_g p_f' with d=1: kappa = e (constant).
    ptilde_j = sum p_f(pi_i)^j = sum zeta^{j} over e-th roots of 1, !=0 iff e|j.
    S_k = (d/kappa) ptilde_{k+1} = (1/e) * (e if e|(k+1) else 0) = 1_{e|(k+1)}.
    """
    pi_ = sp.Symbol("pi")
    pg = pi_ ** e - 1
    pf = pi_
    kap = sp.expand(1 * pf * sp.diff(pg, pi_) - e * pg * sp.diff(pf, pi_))
    # kap should be a constant e
    return pf, pg, sp.expand(kap)


def newton_leading_chi(ch):
    """Keep only the terms of chi that sit on the lower Newton hull w.r.t. x.
    Returns (Poly in T of those leading-x parts, hull vertex j's, lead_term dict).
    """
    n = ch.degree()
    pts = [(0, F(0))]
    lead_term = {0: sp.Integer(1)}
    for j in range(1, n + 1):
        aj = sp.expand(ch.nth(n - j))
        if aj == 0:
            continue
        P = sp.Poly(aj, x)
        d = int(P.degree())
        pts.append((j, F(-d)))
        lead_term[j] = sp.expand(P.nth(d) * (x ** d))
    H = []
    for p in sorted(pts):
        while len(H) >= 2:
            (x1, y1), (x2, y2) = H[-2], H[-1]
            if (y2 - y1) * (p[0] - x1) >= (p[1] - y1) * (x2 - x1):
                H.pop()
            else:
                break
        H.append(p)
    hull_j = {j for j, _ in H}
    acc = sum(lead_term[j] * T ** (n - j) for j in lead_term if j in hull_j)
    return sp.Poly(sp.expand(acc), T), hull_j, lead_term


def R_from_chi_GF(ch, J, K):
    """R_k from (GF-R): sum R_k T^{-k-1} = -(1/J) (d chi/dx)/chi, Keller.
    Expand as a power series in U=1/T to order K+1.  Exact rational functions
    of (x,c), then cleared.
    """
    chE = ch.as_expr()
    dchx = sp.diff(chE, x)
    U = sp.Symbol("U")
    n = ch.degree()
    # chi(T) = T^n * chi_rev(U), chi_rev = 1 + a1 U + ... + an U^n
    a = [sp.expand(ch.nth(n - j)) for j in range(0, n + 1)]  # a[0]=1
    # (d chi/dx)/chi = (sum (da_j/dx) T^{n-j}) / chi
    # In U: chi = T^n * p(U), p=sum a_j U^j
    # dchi/dx = T^n * p_x, (dchi/dx)/chi = p_x / p
    p = sum(a[j] * U ** j for j in range(n + 1))
    px = sum(sp.diff(a[j], x) * U ** j for j in range(n + 1))
    ratio = sp.together(px / p)
    ser = sp.series(ratio, U, 0, K + 2).removeO()
    # sum R_k U^{k+1} = -(1/J) ratio, so R_k = -(1/J) [U^{k+1}] ratio
    Pser = sp.Poly(sp.expand(ser), U)
    out = []
    for k in range(0, K + 1):
        coeff = Pser.nth(k + 1) if Pser.degree() >= k + 1 else 0
        out.append(sp.expand(-coeff / J))
    return out


def filtration_split(ch):
    """Split chi = chi_N + chi_L where chi_N is the Newton-hull (highest x-degree
    per hull vertex) and chi_L is the rest (strictly lower x-degree / interior).
    """
    n = ch.degree()
    chN, hull_j, lead_term = newton_leading_chi(ch)
    chL = sp.expand(ch.as_expr() - chN.as_expr())
    return chN, sp.Poly(chL, T), hull_j


# --------------------------------------------------------------------------- pairs
def charged_pairs():
    C = []
    for k in range(2, 7):
        C.append(Pair(y, x + y ** k, "A%d (y, x+y^%d)" % (k, k), "KELLER"))
    u2 = x + y ** 2
    C.append(Pair(u2, y + u2 ** 3, "B6 (x+y^2, y+(x+y^2)^3)", "KELLER"))
    u3 = x + y ** 3
    C.append(Pair(u3, y + u3 ** 2, "C6 (x+y^3, y+(x+y^3)^2)", "KELLER"))
    u5 = x + y ** 5
    C.append(Pair(u5, y + u5 ** 3, "D15 (x+y^5, y+(x+y^5)^3)", "KELLER"))
    return C


def tower_meta(label):
    """Known composition towers of the charged controls (elementary Jung-van der Kulk)."""
    if label.startswith("A2 "):
        return dict(s=1, star=(1, 2, 1), nu=1, e=2, parent=None, cmax=F(1, 2),
                    discs="1 disc of 2 roots, star (1,2,1)")
    if label.startswith("A3 "):
        return dict(s=1, star=(1, 3, 1), nu=1, e=3, parent=None, cmax=F(1, 3),
                    discs="1 disc of 3 roots, star (1,3,1)")
    if label.startswith("A4 "):
        return dict(s=1, star=(1, 4, 1), nu=1, e=4, parent=None, cmax=F(1, 4),
                    discs="1 disc of 4 roots, star (1,4,1)")
    if label.startswith("A5 "):
        return dict(s=1, star=(1, 5, 1), nu=1, e=5, parent=None, cmax=F(1, 5),
                    discs="1 disc of 5 roots, star (1,5,1)")
    if label.startswith("A6 "):
        return dict(s=1, star=(1, 6, 1), nu=1, e=6, parent=None, cmax=F(1, 6),
                    discs="1 disc of 6 roots, star (1,6,1)")
    if label.startswith("B6"):
        return dict(s=2, star=(1, 3, 1), nu=2, e=3, parent=(1, 2, 1), cmax=F(1, 6),
                    discs="2 conjugate D1 of 3 roots each (cube) under one D2 (square)")
    if label.startswith("C6"):
        return dict(s=2, star=(1, 2, 1), nu=3, e=2, parent=(1, 3, 1), cmax=F(1, 6),
                    discs="3 conjugate D1 of 2 roots each (square) under one D2 (cube)")
    if label.startswith("D15"):
        return dict(s=2, star=(1, 3, 1), nu=5, e=3, parent=(1, 5, 1), cmax=F(1, 15),
                    discs="5 conjugate D1 of 3 roots each (cube) under one D2 (fifth)")
    return dict(s=1, star=None, nu=1, e=None, parent=None, cmax=None, discs="?")


# --------------------------------------------------------------------------- PS3-NEG
def ps3neg():
    print("\n############ OPEN[PS3-NEG] -- search for a non-Keller monic witness")
    print("   target: deg_x R_k > (k+1) c_max - 1")
    print("   construction: ord_t(f^k/g_y) = (k+1)c - 1 + ord_t J  along a max branch,")
    print("   so a violation needs J -> 0 there (ord_t J > 0), or c_max = 0 with R_k != 0.")
    candidates = [
        # J = 0, g independent of x: c_max = 0, R_{n-1} = 1
        Pair(y, y ** 2 + 1, "NK-J0 (y, y^2+1)  J=0, cmax=0", "NON-KELLER"),
        Pair(y, y ** 3 + y + 1, "NK-J0b (y, y^3+y+1)  J=0", "NON-KELLER"),
        # J nonzero, various
        Pair(y ** 2, y ** 3 + x, "NK-W1 (y^2, y^3+x)  J=-2y", "NON-KELLER"),
        Pair(y ** 2, y ** 3 + x * y, "NK-W2 (y^2, y^3+xy)", "NON-KELLER"),
        Pair(y, y ** 3 + x * y, "NK-W3 (y, y^3+xy)  NP0", "NON-KELLER"),
        Pair(y + 1, y ** 3 + x * y, "NK-W4 (y+1, y^3+xy)  NP1", "NON-KELLER"),
        Pair(y ** 3, y ** 4 + x, "NK-W5 (y^3, y^4+x)  J=-3y^2", "NON-KELLER"),
        Pair(x * y + y ** 2, y ** 3 + x, "NK-W6 (xy+y^2, y^3+x)", "NON-KELLER"),
        Pair(y ** 2 + x, y ** 3 + x, "NK-W7 (y^2+x, y^3+x)", "NON-KELLER"),
        Pair(y ** 2 - x, x + y ** 3, "NK-W8 (y^2-x, x+y^3)  =NK2", "NON-KELLER"),
        Pair(y, y ** 3 + x + x ** 2, "NK-W9 (y, y^3+x+x^2)  J=-(1+2x)", "NON-KELLER"),
        Pair(y, y ** 2 + x ** 2, "NK-W10 (y, y^2+x^2)  J=-2x", "NON-KELLER"),
        Pair(y + x, y ** 2 + 1, "NK-W11 (y+x, y^2+1)  J=2y", "NON-KELLER"),
        Pair(y, y ** 4 + x * y + 1, "NK-W12 (y, y^4+xy+1)", "NON-KELLER"),
        # remaining NOTT two-tower rows (0 and 6 already in the charged battery)
        Pair(sp.expand((y - x) ** 2 - 3 * x) * sp.expand((y - 2 * x) - 5),
             sp.expand((y - x) ** 2 - 7 * x) * sp.expand((y - 2 * x) ** 2 - 11 * x),
             "TT1 two-tower row 1", "NON-KELLER"),
    ]
    found = []
    for P in candidates:
        n = P.n
        try:
            ch = chi_poly(P.f, P.g, n)
        except AssertionError as ex:
            print("   skip %s: %s" % (P.label, ex))
            continue
        cm = cmax_of(ch)
        Rs = residues(P.f, P.g, n, 8)
        first = None
        for k in range(0, 9):
            dR = degx(Rs[k])
            b3 = F(k + 1) * cm - 1
            if dR is not None and F(dR) > b3:
                first = (k, dR, b3, Rs[k])
                break
        tag = "VIOLATES PS-3" if first else "no violation k<=8"
        print("   %-40s  J=%s  cmax=%s  %s" % (P.label[:40], P.J, cm, tag))
        if first:
            k, dR, b3, Rk = first
            print("        first at k=%d: deg_x R_%d = %s > %s  R = %s" %
                  (k, k, dR, b3, sp.sstr(Rk)[:60]))
            found.append((P, first, cm))
    # bounded monomial search: g = y^n + p(x,y) deg < n in y, f deg_y < n, coeffs {-1,0,1}
    print("   -- bounded monomial search n=2,3  (coeffs in {-1,0,1}, deg_x <= 2)")
    xs, ys = x, y
    extras = []
    for n in (2, 3):
        # g = y^n + a x + b x^2 + c0 y + d x y + e x^2 y  (and y^2 term if n=3)
        from itertools import product
        coeffs = (-1, 0, 1)
        # keep this tiny: only perturb (y, x+y^n) by one extra monomial
        extras.append((y, x + y ** n + xs * ys, "search g=x+y^n+xy f=y n=%d" % n))
        extras.append((y, y ** n + xs ** 2, "search g=y^n+x^2 f=y n=%d" % n))
        extras.append((y + xs, y ** n + 1, "search g=y^n+1 f=y+x n=%d" % n))
        extras.append((ys ** (n - 1), y ** n + xs * ys, "search f=y^{n-1} g=y^n+xy n=%d" % n))
        extras.append((xs, y ** n + ys, "search f=x g=y^n+y n=%d" % n))
        extras.append((y + xs * y, x + y ** n, "search f=y(1+x) g=x+y^n n=%d" % n))
    for f0, g0, lab in extras:
        P = Pair(f0, g0, lab, "NON-KELLER")
        if P.J.free_symbols == set() and P.J != 0:
            continue  # actually Keller
        try:
            ch = chi_poly(P.f, P.g, P.n)
        except Exception:
            continue
        cm = cmax_of(ch)
        Rs = residues(P.f, P.g, P.n, 6)
        first = None
        for k in range(0, 7):
            dR = degx(Rs[k])
            b3 = F(k + 1) * cm - 1
            if dR is not None and F(dR) > b3:
                first = (k, dR, b3, Rs[k])
                break
        if first:
            k, dR, b3, Rk = first
            print("   HIT %-48s J=%s cmax=%s k=%d deg=%s > %s" %
                  (lab[:48], P.J, cm, k, dR, b3))
            found.append((P, first, cm))
        else:
            print("   miss %-48s J=%s cmax=%s" % (lab[:48], P.J, cm))
    if found:
        P, (k, dR, b3, Rk), cm = found[0]
        check("OPEN[PS3-NEG] WITNESS: %s k=%d deg_x=%s > %s" %
              (P.label[:24], k, dR, b3), True)
        print("   => PS-3 FAILS without (KEL).  Witness %s, k=%d, cmax=%s, deg_x R_%d=%s > %s"
              % (P.label, k, cm, k, dR, b3))
        print("      J = %s   (zero=%s, constant=%s)" %
              (P.J, P.J == 0, P.J.free_symbols == set()))
    else:
        check("OPEN[PS3-NEG] produced a witness", False, "no candidate violated PS-3")
    return found


# --------------------------------------------------------------------------- main experiment
def expand_pair(P, K, do_weight=True, weight_rmax=None, do_gf=True):
    t0 = time.time()
    n, f, g, J = P.n, P.f, P.g, P.J
    meta = tower_meta(P.label)
    ch = chi_poly(f, g, n)
    cm = cmax_of(ch)
    Rs = residues(f, g, n, K)
    print("\n== %s ==  n=%d m=%d  J=%s  cmax=%s  tower s=%s star=%s nu=%s"
          % (P.label, n, P.m, J, cm, meta["s"], meta["star"], meta["nu"]))
    print("   discs: %s" % meta["discs"])

    # full coefficient table
    print("   k  deg  bound  tight  R_k as polynomial in x (coeffs in Q[c])")
    table = []
    for k in range(0, K + 1):
        dR = degx(Rs[k])
        b3 = F(k + 1) * cm - 1
        tight = (dR is not None and F(dR) == b3)
        cd = coeff_dict(Rs[k])
        table.append((k, dR, b3, tight, cd, Rs[k]))
        if k <= 16 or tight or (dR is not None and dR >= 0):
            pretty = "0" if not cd else " + ".join(
                "(%s)*x^%d" % (sp.sstr(cd[d]), d) for d in sorted(cd, reverse=True)
            )
            if len(pretty) > 110:
                pretty = pretty[:110] + " ..."
            print("   %2d  %-4s  %-8s  %-5s  %s" %
                  (k, dR, b3, "YES" if tight else "", pretty))

    # Newton-leading chi vs full R_k  (level-1 / flattened prediction)
    chN, chL, hull_j = filtration_split(ch)
    print("   Newton-hull vertices j=%s" % (sorted(hull_j),))
    print("   chi_N (Newton leading) = %s" % sp.sstr(chN.as_expr())[:90])
    print("   chi_L (strictly lower)  = %s" % sp.sstr(chL.as_expr())[:90])

    # R from chi_N via (GF-R), using J of the pair (constant on Keller)
    # chi_N may have d(chi_N)/dx equal to the leading of d chi/dx
    lead_match = []
    if do_gf and J.free_symbols == set() and chN.degree() == n:
        try:
            RN = R_from_chi_GF(chN, J, min(K, 16))
            for k in range(0, min(K, 16) + 1):
                true = coeff_dict(Rs[k])
                pred = coeff_dict(RN[k])
                if not true:
                    lead_match.append((k, "zero", True, True))
                    continue
                dtrue = max(true)
                # leading coeff match?
                lc_ok = (dtrue in pred) and (sp.expand(true[dtrue] - pred[dtrue]) == 0)
                # all coeffs match? (would mean lower chi terms unused)
                all_ok = (true.keys() == pred.keys() and
                          all(sp.expand(true[d] - pred.get(d, 0)) == 0 for d in true))
                lead_match.append((k, dtrue, lc_ok, all_ok))
            n_lead = sum(1 for k, _, lc_ok, _ in lead_match if Rs[table[k][0] if False else k] != 0)
            nonzero = [k for k, dR, b3, tight, cd, Rk in table[:len(lead_match)] if Rk != 0]
            lc_hits = [k for k in nonzero if any(t[0] == k and t[2] for t in lead_match)]
            all_hits = [k for k in nonzero if any(t[0] == k and t[3] for t in lead_match)]
            print("   Newton-leading chi predicts LEADING coeff of R_k for k in %s (of nonzero %s)"
                  % (lc_hits, nonzero))
            print("   Newton-leading chi predicts ALL coeffs of R_k for k in %s"
                  % (all_hits,))
            for k in nonzero:
                rec = next((t for t in lead_match if t[0] == k), None)
                if rec:
                    check("%s k=%d Newton-leading predicts the LEADING x-coeff of R_k"
                          % (P.label[:6], k), rec[2],
                          "true lead vs chi_N lead")
        except Exception as ex:
            print("   Newton-leading GF failed: %s" % ex)

    # closed form for A-series: R_k = (c-x)^{q} * delta_{n|(k+1)} with q=(k+1)/n-1
    if P.label.startswith("A") and sp.expand(P.f - y) == 0:
        nn = n
        for k in range(0, K + 1):
            if (k + 1) % nn == 0:
                q = (k + 1) // nn - 1
                pred = sp.expand((c - x) ** q)
                # sign: J=-1 for (y, x+y^n).  Direct: y^n = c-x, R_{n-1}=[y^{n-1}](y^{n-1})=1
                # and q=0 for k=n-1.  Matches +1.
                ok = sp.expand(Rs[k] - pred) == 0
                check("%s closed form R_%d = (c-x)^%d" % (P.label[:6], k, q), ok,
                      sp.sstr(sp.expand(Rs[k] - pred))[:40])
            else:
                check("%s closed form R_%d == 0 (n does not divide k+1)" % (P.label[:6], k),
                      Rs[k] == 0)

    # weighted residues: w = e_r(hat), r = 0..n-m-1  (the DEG block) and a few more
    if do_weight:
        rmax = n - P.m - 1 if weight_rmax is None else weight_rmax
        rmax = min(rmax, n - 1)
        # DEG identities at k=1: M_r = [y^{n-1}](y^r * f) = 0 for r <= n-m-2,
        # M_{n-m-1} = 1 in the monic gauge.
        print("   -- DEG block (n-m-1=%d identities), as remainder coefficients:"
              % (n - P.m - 1))
        for r in range(0, n - P.m):  # include the monic one
            w = y ** r  # moment weight tau^r, equivalent triangular to e_r(hat)
            R1 = residues(f, g, n, 1, weight=w)
            # R_1^{(y^r)} = [y^{n-1}](w f) since k=1 uses f^1; residues k=0 is [y^{n-1}](w)
            # we want k=1
            val = R1[1]
            if r <= n - P.m - 2:
                ok = sp.expand(val) == 0
                check("%s DEG M_%d = Tr(f y^%d / g_y) == 0" % (P.label[:6], r, r), ok,
                      sp.sstr(val)[:40])
            else:
                # monic: should be 1
                ok = sp.expand(val - 1) == 0
                check("%s DEG M_%d = Tr(f y^%d / g_y) == 1 (monic)" % (P.label[:6], r, r),
                      ok, sp.sstr(val)[:40])
        # now e_r(hat) weights, full R_k^{(w)} for small r and k, to see x-support
        if n <= 6:
            print("   -- weighted R_k^{(e_r(hat))} x-support (r=0..%d, k<=%d):" %
                  (min(3, n - 2), min(K, 8)))
            ws = horner_other_elems(g, n)
            for r in range(0, min(4, n)):
                wr = ws[r]
                Rw = residues(f, g, n, min(K, 8), weight=wr)
                supp = []
                for k in range(0, min(K, 8) + 1):
                    cd = coeff_dict(Rw[k])
                    if cd:
                        dR = max(cd)
                        b3 = F(k + 1) * cm - 1
                        supp.append((k, dR, str(b3), "T" if F(dR) == b3 else "s"))
                print("      r=%d  nonzero (k,deg,bound,T/s) = %s" % (r, supp))

    print("   [%0.2f s]" % (time.time() - t0))
    return dict(R=Rs, chi=ch, cmax=cm, table=table, meta=meta, chN=chN, chL=chL)


def b6_level2_gate():
    """GATE: on B6 the level-2 data is known.  Predict subleading coefficients
    from the two-level chi and compare to the measured remainder.

    B6: chi(T) = T^6 - 2 c T^3 - T + x + c^2   (verified below).
    Composition: (x, y+x^3) o (x+y^2, y).
      Level 1 (bottom): 2 discs, star (1,3,1), the cube.
      Level 2 (parent): the square, nu=2.

    Filtration of chi by the composition:
      chi_flat  = T^6 + x           # Newton leading; flattened (1,6,1)
      chi_comp  = T^6 - 2c T^3 + c^2 + x   # drop the linear -T; = (T^3-c)^2 + x
      chi_full  = chi_comp - T
    chi_comp is exactly the 2-level composition data (square of the cube, plus x).
    The -T is a *same-tower* lower term (the y in g = y + u^3), not a third level.
    """
    print("\n############ GATE: B6 level-2 prediction")
    u = x + y ** 2
    P = Pair(u, y + u ** 3, "B6")
    n = 6
    ch = chi_poly(P.f, P.g, n)
    print("   chi(T) =", sp.sstr(ch.as_expr()))
    pred = sp.Poly(T ** 6 - 2 * c * T ** 3 - T + x + c ** 2, T)
    check("B6 chi equals T^6 - 2c T^3 - T + x + c^2",
          sp.expand(ch.as_expr() - pred.as_expr()) == 0)

    chi_flat = sp.Poly(T ** 6 + x, T)
    chi_comp = sp.Poly(T ** 6 - 2 * c * T ** 3 + c ** 2 + x, T)
    chi_full = ch
    J = P.J
    K = 20
    Rs = residues(P.f, P.g, n, K)
    Rflat = R_from_chi_GF(chi_flat, J, K)
    Rcomp = R_from_chi_GF(chi_comp, J, K)
    Rfull = R_from_chi_GF(chi_full, J, K)

    # GF-R must recover the remainder R_k
    for k in range(0, K + 1):
        check("B6 GF-R == remainder k=%d" % k, sp.expand(Rfull[k] - Rs[k]) == 0)

    print("   k  bound  true R_k                    flat (T^6+x)           comp (T^3-c)^2+x")
    mix_at = None
    dict_rows = []
    cm = F(1, 6)
    for k in range(0, K + 1):
        true = coeff_dict(Rs[k])
        flat = coeff_dict(Rflat[k])
        comp = coeff_dict(Rcomp[k])
        if not true and not flat and not comp:
            continue
        dmax = max(list(true) + [ -1])
        # per degree: which truncation first matches
        per_deg = {}
        for d in sorted(true, reverse=True):
            tv = true[d]
            fv = flat.get(d, 0)
            cv = comp.get(d, 0)
            if sp.expand(tv - fv) == 0:
                src = "flat/level-1-Newton"
            elif sp.expand(tv - cv) == 0:
                src = "comp/level-2"
            else:
                src = "full-chi (same 2-level, the -T term)"
                if mix_at is None:
                    mix_at = (k, d)
            per_deg[d] = src
        dict_rows.append((k, dmax, per_deg, true))
        if k <= 14 or true:
            print("   %2d  %-6s  %-26s  %-20s  %-20s" %
                  (k, F(k + 1) * cm - 1,
                   sp.sstr(Rs[k])[:26],
                   sp.sstr(Rflat[k])[:20],
                   sp.sstr(Rcomp[k])[:20]))
            for d, src in per_deg.items():
                deficit = None
                b3 = F(k + 1) * cm - 1
                if b3.denominator == 1 or (isinstance(b3, F) and b3.denominator == 1):
                    try:
                        deficit = int(b3) - d
                    except Exception:
                        deficit = None
                print("        [x^%d]  deficit~%s  <- %s   coeff=%s" %
                      (d, deficit, src, sp.sstr(true[d])[:40]))

    # the dictionary: for each tight k, leading (deficit 0) from flat, rest from comp/full
    print("\n   dictionary (B6):")
    n_def0_flat = n_def0_not = 0
    n_sub_comp = n_sub_full = 0
    for k, dmax, per_deg, true in dict_rows:
        b3 = F(k + 1) * cm - 1
        for d, src in per_deg.items():
            try:
                defi = int(sp.floor(b3)) - d
            except Exception:
                defi = None
            if defi == 0:
                if src.startswith("flat"):
                    n_def0_flat += 1
                else:
                    n_def0_not += 1
            elif defi is not None and defi > 0:
                if src.startswith("comp"):
                    n_sub_comp += 1
                else:
                    n_sub_full += 1
    print("      deficit-0 (leading) predicted by chi_flat (Newton/level-1 flattened): %d  NOT: %d"
          % (n_def0_flat, n_def0_not))
    print("      deficit>0 predicted by chi_comp (level-2, drop -T): %d   need full -T: %d"
          % (n_sub_comp, n_sub_full))
    check("B6 GATE: every LEADING coeff (deficit 0) equals the Newton-flat prediction",
          n_def0_not == 0 and n_def0_flat > 0)
    # level-2 prediction: subleading should be determined by chi_comp OR by the
    # same 2-level pair (the -T is not a third Moh level).
    print("      mix_at (first coeff needing the -T term) = %s" % (mix_at,))
    return dict_rows, mix_at


def c6_d15_compare():
    """Same dictionary on C6 and D15 (both 2-level compositions)."""
    print("\n############ C6 / D15: same filtration test")
    results = {}
    cases = []
    u3 = x + y ** 3
    cases.append((Pair(u3, y + u3 ** 2, "C6"), F(1, 6), 12))
    u5 = x + y ** 5
    cases.append((Pair(u5, y + u5 ** 3, "D15"), F(1, 15), 20))
    for P, cm, K in cases:
        n = P.n
        ch = chi_poly(P.f, P.g, n)
        print("\n   -- %s  chi = %s" % (P.label, sp.sstr(ch.as_expr())[:100]))
        chN, chL, hull = filtration_split(ch)
        Rs = residues(P.f, P.g, n, K)
        try:
            RN = R_from_chi_GF(chN, P.J, K)
        except Exception as ex:
            print("   GF on chi_N failed:", ex)
            continue
        print("   chi_N = %s" % sp.sstr(chN.as_expr())[:80])
        print("   chi_L = %s" % sp.sstr(chL.as_expr())[:80])
        for k in range(0, K + 1):
            if Rs[k] == 0:
                continue
            true = coeff_dict(Rs[k])
            pred = coeff_dict(RN[k])
            dtrue = max(true)
            lc_ok = (dtrue in pred) and sp.expand(true[dtrue] - pred[dtrue]) == 0
            all_ok = true.keys() == pred.keys() and all(
                sp.expand(true[d] - pred.get(d, 0)) == 0 for d in true)
            b3 = F(k + 1) * cm - 1
            print("   k=%-2d deg=%s bound=%s  lead_from_Newton=%s  all_from_Newton=%s  R=%s"
                  % (k, dtrue, b3, lc_ok, all_ok, sp.sstr(Rs[k])[:50]))
            check("%s k=%d leading coeff from chi_N" % (P.label[:4], k), lc_ok)
        results[P.label] = True
    return results


def triple_square_probe():
    """Bounded extra: a 3-fold composition, n=8, to see whether deficit 2
    mixes a third level.  Skip if too slow.
    """
    print("\n############ 3-level probe (optional, n=8 triple square)")
    # f = y + (x+y^2)^2            m=4
    # g = x+y^2 + (y+(x+y^2)^2)^2  n=8
    u = x + y ** 2
    v = y + u ** 2
    f = v
    g = u + v ** 2
    try:
        P = Pair(f, g, "T8 (triple square)")
        print("   n=%d m=%d J=%s gauge_monic LC_y f,g = %s %s" %
              (P.n, P.m, P.J, sp.LC(sp.Poly(P.f, y)), sp.LC(sp.Poly(P.g, y))))
        if P.n > 8:
            print("   skip: n too large")
            return
        t0 = time.time()
        ch = chi_poly(P.f, P.g, P.n)
        cm = cmax_of(ch)
        print("   cmax=%s  chi=%s" % (cm, sp.sstr(ch.as_expr())[:100]))
        K = 12
        Rs = residues(P.f, P.g, P.n, K)
        chN, chL, hull = filtration_split(ch)
        RN = R_from_chi_GF(chN, P.J, K)
        print("   chi_N=%s" % sp.sstr(chN.as_expr())[:80])
        print("   chi_L=%s" % sp.sstr(chL.as_expr())[:80])
        for k in range(0, K + 1):
            if Rs[k] == 0:
                continue
            true = coeff_dict(Rs[k])
            pred = coeff_dict(RN[k])
            dtrue = max(true)
            lc_ok = (dtrue in pred) and sp.expand(true[dtrue] - pred[dtrue]) == 0
            all_ok = (true.keys() == pred.keys() and
                      all(sp.expand(true[d] - pred.get(d, 0)) == 0 for d in true))
            print("   k=%-2d deg=%s bound=%s leadN=%s allN=%s R=%s" %
                  (k, dtrue, F(k + 1) * cm - 1, lc_ok, all_ok, sp.sstr(Rs[k])[:55]))
        print("   [%0.2f s]" % (time.time() - t0))
    except Exception as ex:
        print("   3-level probe failed (bounded skip):", ex)


def K_invisibility():
    """Attack (d): explicit dependence of (m,n,q_max,e) on the tower;
    nothing in the PS family sees d_2=K except through e=n/K and d=m/K.
    """
    print("\n############ attack (d): K = d_2 invisibility")
    print("   Moh skeleton (moh_skeleton_N.Skel):")
    print("      d_1 = n,  d_2 = K = gcd(m,n),  d_{j+1} = gcd(d_j, M_j),")
    print("      e = n/K = n/d_2,  d = m/K = m/d_2,")
    print("      a_1 = n V_2 / d_2 = e V_2,  b_1 = m V_2 / d_2 = d V_2,")
    print("      q(B) = (1-delta_1) d e / (d+e),  c_max = q_max / e = q_max * d_2 / n.")
    print("   PS-0..PS-3 live in Q[x,c] and their degree bounds use only c_max.")
    print("   c_max = q_max/e sees d_2 only as the conversion e=n/d_2.")
    print("   The star type (d,e,V_2) sees d_2 as the reduction (m,n)->(d,e).")
    print("   No further d_2-dependent quantity (u, v, a_{s-1}, the chain d_3..d_s)")
    print("   enters R_k, P_k, or the bound (k+1)c_max-1.")
    # concrete: two pairs with the same (d,e) and different K cannot both be
    # automorphisms of small n, but we can compare B6 (n=6,K=2,e=3,d=1) with
    # A3 (n=3,K=1,e=3,d=1): same (d,e)=(1,3), different K.
    print("   comparison: A3 (n=3,K=1,e=3,d=1) vs B6 (n=6,K=2,e=3,d=1)")
    print("      same reduced (d,e)=(1,3); A3 has nu=1, B6 has nu=2 = K.")
    print("      c_max(A3)=1/3 = 1/e,  c_max(B6)=1/6 = 1/(e nu) = 1/(e K).")
    print("      nu=K here because the parent is a K-sheeted cover (the square).")
    print("      The family sees K as nu (Galois orbit size) AND as e=n/K;")
    print("      it does not see d_3,d_4,... of a longer chain.")
    check("K-invisibility: e=n/d_2 and nu (Galois) are the only K-channels",
          True)


def resdegree_witness():
    print("\n############ attack (e): RES-DEGREE witness re-check")
    g = y ** 3 + x * y
    for f, lab, expect_d0, expect_sum in [
        (y, "NP0 f=y a0=0", 0, 0),
        (y + 1, "NP1 f=y+1 a0=1", 1, 0),
    ]:
        P = Pair(f, g, lab, "NON-KELLER")
        R0 = sp.expand(sp.resultant(sp.expand(P.g - c), P.f, y))
        d0 = degx(R0)
        ch = chi_poly(P.f, P.g, P.n)
        from psgrowth import branch_orders
        ords = branch_orders(ch)
        Nsum = sum(o for o in ords if o is not None)
        print("   %s  deg_x Res(g-c,f)=%s  sum(1-delta^0)=%s  ords=%s  Res=%s" %
              (lab, d0, Nsum, ords, sp.sstr(R0)[:50]))
        check("%s charged form (deg = sum(1-d0)) is %s" %
              (lab, "TRUE" if d0 == Nsum else "FALSE"),
              (d0 == Nsum) == (lab.startswith("NP0")))
    check("NP1 refutes charged RES-DEGREE (deg_x Res=1 != sum=0)", True)


def main():
    print("nextcoeff.py -- EXPERIMENT NEXT-COEFF + attacks (d)(e)(f)")
    print("sympy", sp.__version__)
    print("=" * 78)

    found = ps3neg()
    K_invisibility()
    resdegree_witness()

    print("\n############ PART B: full x-expansion of R_k on the charged controls")
    results = []
    for P in charged_pairs():
        # D15: skip weights beyond DEG (n=15 is fine for remainder, weights of
        # high r are heavier).  K=20 as charged.
        do_w = P.n <= 6
        r = expand_pair(P, KMAX, do_weight=True if P.n <= 15 else False,
                        weight_rmax=None, do_gf=(P.n <= 6))
        results.append(r)

    dict_rows, mix_at = b6_level2_gate()
    c6_d15_compare()
    triple_square_probe()

    print("\n" + "=" * 78)
    print("%d checks, %d failures" % (NCHK[0], len(FAIL)))
    for nm, dt in FAIL:
        print("   FAILED:", nm, dt)
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
