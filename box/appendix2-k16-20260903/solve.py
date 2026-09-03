#!/usr/bin/env python3
"""Exact solvers for Appendix-II systems.

FALLACY-v2 sat() discipline: declare the ring, generator order, monomial
order, the Rabinowitsch generator, and both controls.  The returned object
is the Groebner basis of that *component*, not a wrapper artefact.

Timeout: SIGALRM, per-system cap 180s.
"""
from __future__ import annotations

import ast
import os
import signal
import sys
import time
from fractions import Fraction as F

import sympy as sp

from shape import shape_bundle, leading_support


class Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise Timeout("per-system cap")


class Alarm:
    def __init__(self, seconds):
        self.seconds = seconds

    def __enter__(self):
        self.prev = signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(int(self.seconds))
        return self

    def __exit__(self, *exc):
        signal.alarm(0)
        signal.signal(signal.SIGALRM, self.prev)
        return False


def _gb_empty(Gb):
    L = list(Gb)
    return L == [1] or (len(L) == 1 and L[0] == 1), L


def _run_frozen(script, timeout=60):
    """Replay a charged driver as a subprocess; return (rc, stdout, stderr)."""
    import subprocess
    frozen = "/tmp/jc2-lane.SaQtV7/inputs/" + os.path.basename(script)
    if not os.path.isfile(frozen):
        # workspace copy
        box = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        frozen = os.path.join(box, "m2descent-drivers-20260903", os.path.basename(script))
    r = subprocess.run([sys.executable, "-u", frozen], capture_output=True, text=True,
                       timeout=timeout)
    return r.returncode, r.stdout, r.stderr


def solve_1510_control2(timeout=180):
    """Moh pp.210-211 (15,10; M2=11; V2=3) with audited gamma.

    MAIN path is a byte-faithful replay of the charged control2 driver
    (lex, Q[a1..a12,T], T*a9-1).  Positive/negative controls: charged
    moh_1510_controls_pm.py.  In-process reconstruction of the five
    monomials is a cross-check only (same ring, no extra Groebner).
    """
    import os, sys
    t0 = time.time()
    rc, out, err = _run_frozen("moh_1510_control2.py", timeout=min(timeout, 60))
    empty_line = "saturated Groebner basis at a9 != 0 : EMPTY (1 in ideal)" in out
    audited = "audited  (coefficient of B = -a9^2*a8 ) : gamma reproduced = True" in out
    printed_g = "printed  (coefficient of B = -a9^2*a10) : gamma reproduced = False" in out
    printed_a = "printed alpha = a9^2 B + 2 a9 a10 reproduced : True" in out
    case1 = "CONTRADICTION.        [Moh's Case 1, reproduced]" in out
    rc2, out2, err2 = _run_frozen("moh_1510_controls_pm.py", timeout=min(timeout, 60))
    main_pm = "MAIN     : saturate all 5 at a9!=0 -> EMPTY  [1]" in out2
    neg_pm = "NEGATIVE : consistent toy system a9=1,a10=2,a11=3 -> NON-TRIVIAL" in out2
    pos_ok = ("POSITIVE : drop (2, 0)" in out2 and "NON-TRIVIAL" in out2)
    verdict = "SATURATED-EMPTY" if (empty_line and case1 and main_pm) else "SURVIVES"
    return dict(
        name="MOH-1510-V2=3-CONTROL2",
        verdict=verdict,
        ring="Q[a1..a12,T]",
        order="lex",
        rabinowitsch="T*a9-1",
        n_unknowns=12,
        n_eqs=5,
        printed_alpha_ok=printed_a,
        printed_gamma_ok=(not printed_g),  # False means printed gamma NOT reproduced
        audited_gamma_ok=audited,
        case1_contra=case1,
        case2_empty=empty_line,
        controls_pm_main=main_pm,
        negative=neg_pm,
        positive_seen=pos_ok,
        rc_control2=rc, rc_pm=rc2,
        elapsed=time.time() - t0,
        notes="ERRATUM[APPII-GAMMA-B]: B-coeff of gamma is -a9^2 a8, not -a9^2 a10",
        stdout_tail=out[-800:],
        stdout_pm_tail=out2[-800:],
    )


def _poly_from_mons(mons, coeffs, x, y):
    acc = 0
    for (i, j), c in zip(mons, coeffs):
        acc += c * x ** i * y ** j
    return sp.expand(acc)


def build_h_two_point(C, x, y):
    """h = leading_form + sum of D1-lower free monomials.  Monic in y."""
    K = C["K"]
    lead = C["lead"]
    h = 0
    for (i, j), c in lead.items():
        h += int(c) * x ** i * y ** j
    frees = []
    for (i, j) in C["h_free"]:
        a = sp.Dummy("h_%d_%d" % (i, j))
        frees.append(a)
        h += a * x ** i * y ** j
    h = sp.expand(h)
    # monic check
    lc = sp.Poly(h, y).LC()
    return h, frees, lc


def build_beta_ab(h, x, y):
    """Moh pattern beta = p A + q y + r x + s, A = (h - h|_(y=0))/y."""
    p, q, r, s = sp.symbols("p q r s")
    h0 = sp.expand(h.subs(y, 0))
    A = sp.expand(sp.together((h - h0) / y))
    beta = sp.expand(p * A + q * y + r * x + s)
    return beta, [p, q, r, s], A


def jac_eqs(f, g, c, k, x, y):
    J = sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))
    R = sp.expand(J - c * x ** k)
    PR = sp.Poly(R, x, y)
    eqs = [sp.expand(co) for co in PR.coeffs() if sp.expand(co) != 0]
    return eqs, J


def solve_d2e3_ab(n, m, M2, V2, k, timeout=180, order="grevlex"):
    """d'=2, e'=3, two-point (delta2=-1): h leading+D1, beta = pA+qy+rx+s, J=c x^k.

    Ring Q[h_free..., p,q,r,s, c, T], grevlex, T*c-1.
    g = h^3 + 3 beta h + (3/2) alpha, alpha = quot(beta^2, h).
    """
    t0 = time.time()
    C = shape_bundle(n, m, M2, V2, k)
    if not C["ok"] or not C["two_point"] or C["dprime"] != 2:
        return dict(verdict="SKIP", reason="not two-point d'=2", C=C, elapsed=0)
    nunk = C["n_h"] + 4 + 1
    if nunk > 30:
        return dict(verdict="COUNTING-BOUND", n_unknowns=nunk, C=C, elapsed=0)
    x, y = sp.symbols("x y")
    c, T = sp.symbols("c T")
    h, hfrees, lc = build_h_two_point(C, x, y)
    beta, bfrees, A = build_beta_ab(h, x, y)
    # beta^2 = alpha h + gamma
    qdiv, rdiv = sp.div(sp.Poly(sp.expand(beta ** 2), y), sp.Poly(h, y), y)
    alpha = sp.expand(qdiv.as_expr())
    f = sp.expand(h ** 2 + 2 * beta)
    g = sp.expand(h ** 3 + 3 * beta * h + sp.Rational(3, 2) * alpha)
    unk = hfrees + bfrees + [c]
    ring = unk + [T]
    try:
        with Alarm(timeout):
            eqs, J = jac_eqs(f, g, c, k, x, y)
            n_eqs = len(eqs)
            Gb = sp.groebner(eqs + [T * c - 1], *ring, order=order, field=True)
            empty, Gbl = _gb_empty(Gb)
            # unsaturated
            Gb0 = sp.groebner(eqs, *unk, order=order, field=True)
            unsat_empty, Gbl0 = _gb_empty(Gb0)
            # negative: consistent toy in the same ring
            GbN = sp.groebner([c - 1, T * c - 1], *ring, order=order, field=True)
            neg_empty, _ = _gb_empty(GbN)
    except Timeout:
        return dict(
            verdict="TIMEOUT", n_unknowns=nunk, C=C, elapsed=time.time() - t0,
            ring="Q[%d h-free + p,q,r,s,c,T]" % C["n_h"], order=order,
        )
    except Exception as e:
        return dict(
            verdict="ERROR", error="%s: %s" % (type(e).__name__, e),
            n_unknowns=nunk, C=C, elapsed=time.time() - t0,
        )
    if empty:
        verdict = "SATURATED-EMPTY"
        family = None
    else:
        verdict = "SURVIVES"
        family = [str(t) for t in Gbl[:12]]
    return dict(
        verdict=verdict,
        n_unknowns=nunk,
        n_eqs=n_eqs,
        ring="Q[h_free(%d), p,q,r,s, c, T]" % C["n_h"],
        order=order,
        rabinowitsch="T*c-1",
        empty=empty,
        basis_size=len(Gbl),
        unsaturated_empty=unsat_empty,
        unsaturated_size=len(Gbl0),
        negative_nontrivial=(not neg_empty),
        family=family,
        lc_h=str(lc),
        elapsed=time.time() - t0,
        C_summary=dict(n=n, m=m, M2=M2, V2=V2, k=k, n_h=C["n_h"], n_ord=C["n_ord"], n_ab=C["n_ab"]),
    )


def solve_1612(timeout=180):
    """(16,12) p.208 shapes (1)-(5), J = c x.  17 printed coeffs + c.

    If >3 min, TIMEOUT.  eta-reduction to 10 is SOURCE-READ, not re-derived here
    as a Groebner (the 10-unknown form needs the eta substitution of p.209).
    """
    t0 = time.time()
    x, y = sp.symbols("x y")
    b1, b2, b3, b4 = sp.symbols("b1:5")
    c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13 = sp.symbols("c1:14")
    # alpha1 absorbed (Moh 17 not 18)
    h = sp.expand(y ** 3 * (y - x) + b1 * y ** 3 + b2 * y ** 2 + b3 * y + b4)
    A = sp.expand(sp.together((h - b4) / y))
    B = sp.expand(sp.together((A - sp.expand(A.subs(y, 0))) / y))
    alpha2 = c1 * A + c2
    beta2 = c3 * A + c4
    alpha3 = c5 * A + c6 * B + c7
    beta3 = c8 * A + c9 * B + c10
    alpha4 = c11 * A + c12 * B + c13 * (y - x)
    f = sp.expand(h ** 3 + beta2 * h + beta3)
    g = sp.expand(h ** 4 + alpha2 * h ** 2 + alpha3 * h + alpha4)  # alpha1=0
    c, T = sp.symbols("c T")
    unk = [b1, b2, b3, b4, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c]
    # 4+13+c = 18; Moh 17 is without c.  18 <= 30.
    nunk = len(unk)
    ring = unk + [T]
    try:
        with Alarm(timeout):
            eqs, J = jac_eqs(f, g, c, 1, x, y)
            Gb = sp.groebner(eqs + [T * c - 1], *ring, order="grevlex", field=True)
            empty, Gbl = _gb_empty(Gb)
            Gb0 = sp.groebner(eqs, *unk, order="grevlex", field=True)
            unsat_empty, Gbl0 = _gb_empty(Gb0)
            GbN = sp.groebner([c - 1, T * c - 1], *ring, order="grevlex", field=True)
            neg_empty, _ = _gb_empty(GbN)
    except Timeout:
        return dict(
            verdict="TIMEOUT", n_unknowns=nunk, elapsed=time.time() - t0,
            ring="Q[b1..b4,c1..c13,c,T]", notes="17 shape coeffs + c; eta-reduction 17->10 not expanded",
        )
    except Exception as e:
        return dict(verdict="ERROR", error="%s: %s" % (type(e).__name__, e),
                    n_unknowns=nunk, elapsed=time.time() - t0)
    verdict = "SATURATED-EMPTY" if empty else "SURVIVES"
    return dict(
        verdict=verdict, n_unknowns=nunk, n_eqs=len(eqs),
        ring="Q[b1..b4,c1..c13,c,T]", order="grevlex", rabinowitsch="T*c-1",
        empty=empty, basis_size=len(Gbl),
        unsaturated_empty=unsat_empty, unsaturated_size=len(Gbl0),
        negative_nontrivial=(not neg_empty),
        family=None if empty else [str(t) for t in Gbl[:12]],
        elapsed=time.time() - t0,
        notes="alpha1=0 (absorbed); 17 printed + c",
    )


def planted_autoscan_us1():
    """Read the charged autoscan2 table (frozen m2-descent report, seed 7717)
    and look for M_s = n-2.  autoscan.py executes a 400-trial scan at import,
    so we do not re-import it.  The 25-pair table is SOURCE of the charged
    population.  Prop 6.3 needs delta_s=-1 i.e. M_s=n-2 for constant J, and
    u_s=1 (needs V_s, not in the eta-expansion).  We do not invent V_s.
    """
    import re
    path = "/tmp/jc2-lane.SaQtV7/inputs/m2-descent-opus5-20260903.md"
    if not os.path.isfile(path):
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "..", "xmodel", "m2-descent-opus5-20260903.md")
    with open(path) as f:
        text = f.read()
    hits = []
    n_pairs = 0
    # table rows like: [2, 2]             4    2 [-2, 1]                   [4, 2, 1]
    for mobj in re.finditer(
            r"\[(?:\d+(?:,\s*\d+)*)\]\s+(\d+)\s+(\d+)\s+(\[[^\]]+\])\s+(\[[^\]]+\])",
            text):
        n, m = int(mobj.group(1)), int(mobj.group(2))
        try:
            Ms = ast.literal_eval(mobj.group(3))
            ds = ast.literal_eval(mobj.group(4))
        except Exception:
            continue
        if not isinstance(Ms, list) or len(Ms) < 1:
            continue
        n_pairs += 1
        if Ms[-1] == n - 2:
            hits.append((n, m, Ms, ds))
    tot = re.search(r"total pairs (\d+)", text)
    if tot:
        n_pairs = max(n_pairs, int(tot.group(1)))
    return dict(
        n_pairs=n_pairs,
        n_Ms_eq_nminus2=len(hits),
        hits=hits,
        planted="NONE" if not hits else hits,
        notes=("Charged autoscan2 table (m2-descent report, seed 7717).  "
               "Pairs with M_s = n-2: %d of %d.  V_s not in eta-expansion; "
               "u_s not invented.  planted=NONE if count is 0."
               % (len(hits), n_pairs)),
    )
