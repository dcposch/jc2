#!/usr/bin/env python3
"""d43_famcheck.py -- fidelity gate: symbolic compat rows == numeric.

STATUS: INTERNAL TOOLING, UNREVIEWED.  FAIL-CLOSED.

For each rung k and each constant left-kernel row L of the fiber's
C_k (as computed by d43_family2), the symbolic compat row must
EVALUATE, at completed cell points with RANDOMIZED rung/deep tails,
to the same value as L . (numeric band-k selected row values) from
the byte-identically-regressed numeric engine (cases/eplus43.py).
Points on V(I23) only (the compat rows are NF-reduced mod I23); the
randomized tails exercise the affine rung structure and feed-forward.

Usage (box01):
  python3 d43_famcheck.py --ckdir d43red --prime P --fiber LAB
        [--points 2] [--seed 7]
"""
import argparse
import json
import os
import random
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import d25_reduce as DR
import d43_family2 as F2
import eplus43 as X
import d25_eplus as DE
import valuation_e as V

V43 = X.V43
GBVARS = DR.GBVARS


def eval_compat(comb, base_vals, deep_vals, p):
    tot = 0
    for (pk, deep), c in comb.items():
        t = c
        e22 = DR.unpack(pk)
        for i, e in enumerate(e22):
            if e:
                t = t * pow(base_vals[GBVARS[i]], e, p) % p
        for nm in deep:
            t = t * deep_vals[nm] % p
        tot = (tot + t) % p
    return tot


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckdir", required=True)
    ap.add_argument("--prime", type=int, required=True)
    ap.add_argument("--fiber", default="a00pp")
    ap.add_argument("--points", type=int, default=2)
    ap.add_argument("--seed", type=int, default=7)
    a = ap.parse_args()
    p = a.prime
    lab = a.fiber
    t0 = time.time()
    # recompute the compat rows (structure verified inside analyze;
    # emission skipped)
    report, compat = F2.analyze(a.ckdir, p, lab, parked_ms=None,
                                out_prefix="/tmp/d43famchk",
                                run_gb=False)
    env = DE.fiber_env(p, lab)
    hdr, rows = DE.parse_fiber_ms(p, lab)
    cells = DE.cells_of_fiber(p, lab)
    rng = random.Random(a.seed)
    pt, _r3, _h = V.radical_env(p)
    Z = [pow(pt["z"], m, p) for m in range(42)]
    nchk = 0
    for pi in range(a.points):
        fv = {v: rng.randrange(p) for v in DE.FREE_BASE + DE.FREE_LIFT}
        cv = DE.solve_cell_point(p, hdr, rows, fv,
                                 *cells[rng.randrange(16)])
        dval, _dg = DE.reconstruct_point(p, cv, env)
        wit72, deep = DE.witness72_of(p, dval)
        _pv, _E, fr = X.completed_point_v2(p, wit72, deep, env)
        extra = {}
        for labl, vv in fr.items():
            fam, lvl = labl.rsplit("_", 1)
            extra[(fam, int(lvl) - 32)] = vv
        point = X.point43_from_v2(p, wit72, deep, env,
                                  extra_tails=extra)
        # randomize every rung tail (exercise the affine structure)
        for (f, r) in X.prolong_unknowns():
            point["tails"][f][r] = rng.randrange(p)
        alpha = rng.randrange(p)
        beta = rng.randrange(p)
        jf, jg = V43.build_jets(point, p, Z)
        jff, jgf, _u, _u2 = X.apply_xside(jf, jg, p, alpha, beta)
        E = V43.euler_rows(jff, jgf, p)
        Vv = E.V.astype(np.int64)
        # variable values for the symbolic side
        base_vals = {}
        for nm in GBVARS:
            tl = F2.X2T.get(nm, nm)
            if nm in ("W1", "W2"):
                base_vals[nm] = point["fixed"][nm] % p
            elif nm in ("uW1", "uW2"):
                base_vals[nm] = pow(point["fixed"][nm[1:]], p - 2, p)
            elif tl.startswith(("uf", "vf")):
                base_vals[nm] = point["fixed"].get(tl, 0) % p
            else:
                fam, lvl = tl.rsplit("_", 1)
                base_vals[nm] = point["tails"][fam].get(
                    int(lvl) - 32, 0) % p
        deep_vals = {"Xf_alpha": alpha, "Xg_beta": beta}

        def dval_of(nm):
            tl = F2.X2T.get(nm, nm)
            if tl == "uf24":
                return point["fixed"].get("uf24", 0) % p
            if tl == "uf30":
                return 0
            fam, lvl = tl.rsplit("_", 1)
            return point["tails"][fam].get(int(lvl) - 32, 0) % p
        # THE GATE: compat row value == L . (numeric selected band
        # values) from the regressed engine, at the SAME point.
        for (k, li), lrow, comb in compat:
            need = {nm for (_pk, deep) in comb for nm in deep}
            for nm in need:
                if nm not in deep_vals:
                    deep_vals[nm] = dval_of(nm)
            got = eval_compat(comb, base_vals, deep_vals, p)
            hs = F2.rung_rows_idx(k)
            want = 0
            for i, h in enumerate(hs):
                if lrow[i]:
                    want = (want + lrow[i] * int(Vv[h][k])) % p
            assert got == want, ("famcheck MISMATCH", k, li, got, want)
            nchk += 1
        print("point %d: %d compat rows evaluated (%.0fs)"
              % (pi, len(compat), time.time() - t0), flush=True)
    print("PASS famcheck scaffolding: %d evaluations (direct L-vs-"
          "numeric equality is asserted inside analyze via exact "
          "y-cancellation + the C-diag factorization)" % nchk,
          flush=True)


if __name__ == "__main__":
    main()
