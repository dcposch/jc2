#!/usr/bin/env python3
"""Replay A2^{(r)} and A1 at one legal t per r=1..5 by the fixed-t engine.

t = 3r+3 (the CHAIN-STEP bound).  Extracts band t+3r+1 monomial x^3 and
band 2t-1 monomial b3^2.  Reports N(Du) and whether it vanishes.
This is a HYP(r) unit test at one t, not a closed form in t.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sq_engine as S  # noqa: E402
from sq_engine import E, b3, c1, c2, c3, c4, d, ex, red, spine, x  # noqa: E402


def N_of(co, tv):
    e = sp.together(co)
    n, den = sp.fraction(e)
    P = sp.Poly(sp.expand(n), d)
    A, B = P.nth(1), P.nth(0)
    return sp.expand(B**2 - A**2 * (tv + 1) / 3), sp.expand(den)


def is_high_num(k, tv):
    return ex(k) >= 2 * tv


def run_one(RV, TV):
    T0 = time.time()
    S.set_r(RV)
    S.set_t(TV)
    from sq_engine import E as EE, red as redd, spine as spn, ex as exx

    O = spn(has_b1=(RV == 1))
    Phi = O["Phi"]
    high = {k: v for k, v in Phi.items() if exx(k) >= 2 * TV}
    order = [(EE(3, 1, 1), c1), (EE(3, 0, 0), c2), (EE(2, 2, 1), c3), (EE(2, 1, 0), c4)]
    SOL = {}
    for key, var in order:
        row = redd(high[key].subs(SOL))
        P = sp.Poly(row, var)
        if P.degree() != 1:
            print("t=%d r=%d pivot %s deg=%s FAIL" % (TV, RV, var, P.degree()), flush=True)
            return
        lead, rem = redd(P.nth(1)), redd(P.nth(0))
        SOL[var] = redd(-rem / lead)
    bad = [exx(k) for k in high if redd(high[k].subs(SOL)) != 0]
    print(
        "t=%d r=%d high_residual=%s elapsed_high=%.1f"
        % (TV, RV, bad or "all0", time.time() - T0),
        flush=True,
    )
    if RV != 1:
        print("  b1_condition", redd(O["extra"]["b1_condition"].subs(SOL)), flush=True)
    targets = {
        "A1_b3^2": (2 * TV - 1, (0, 2)),
        "A2_x^3": (TV + 3 * RV + 1, (3, 0)),
        "A5_b3^3": (TV - 2, (0, 3)),
    }
    for name, (band, mon) in targets.items():
        # find the Phi key with this numeric exponent
        hit = None
        for k, v in Phi.items():
            if exx(k) == band and not (exx(k) >= 2 * TV):
                hit = redd(v.subs(SOL))
                break
        if hit is None:
            print("  %s band %d NOT_TERMINAL_OR_MISSING" % (name, band), flush=True)
            continue
        if hit == 0:
            print("  %s band %d ZERO_ROW" % (name, band), flush=True)
            continue
        P = sp.Poly(hit, x, b3)
        terms = {m: redd(c) for m, c in P.terms()}
        co = terms.get(mon)
        extra = [m for m in terms if m != mon]
        if co is None:
            print("  %s band %d missing mon %s present=%s" % (name, band, mon, list(terms)), flush=True)
            continue
        Nn, den = N_of(co, TV)
        print(
            "  %s band=%d extra_mons=%s Nnum=%s den=%s vanishes=%s (%.1fs)"
            % (name, band, extra, Nn, den, Nn == 0, time.time() - T0),
            flush=True,
        )


def main():
    pairs = [(1, 6), (2, 9), (3, 12), (4, 15), (5, 18)]
    if len(sys.argv) > 1:
        pairs = [(int(sys.argv[i]), int(sys.argv[i + 1])) for i in range(1, len(sys.argv), 2)]
    for RV, TV in pairs:
        run_one(RV, TV)


if __name__ == "__main__":
    main()
