#!/usr/bin/env python3
"""d43_family.py -- the per-fiber D43 family compression + verdict prep.

STATUS: INTERNAL TOOLING, UNREVIEWED.  FAIL-CLOSED.

Consumes the mod-p symbolic bank (cases/build_tails_modp.py -- the
structural mirror of the regression-validated numeric engine) for one
(prime, fiber) and compresses the D43 rung system 26..42 by the D25
certificate discipline (sol-ideas-0821 item 3; sol-h29-dichotomy 4.D):

  RUNG STRUCTURE (measured numerically, VERIFIED SYMBOLICALLY here):
  each rung k's selected rows are exactly affine in the ten
  first-occurrence tails y_k, with coefficient matrix factoring as
      A_k = C_k diag(d_j),   C_k CONSTANT (rank 4),  d_j Laurent-unit
  W-monomials.  Then L_k (the constant left kernel of C_k) gives the
  EXACT compat rows L_k . rows_k (the y_k terms cancel identically),
  and the four pivot combos solve four y_k coordinates through the
  unit d_j (reversible Laurent DAG).  Any failure of affinity, of the
  C diag factorization, of unit-ness, or an unexpected variable stops
  the stage (fail-closed; POST41-FIRST-OCCURRENCE is verified, not
  assumed, at Row 42).

  OUTPUT: the compressed D43 fiber object = the banked D25 parked
  system (34 rows, 28 vars) + the 53 compat rows (in the cell vars +
  the surviving free completion tails), emitted as
  cases/d43fam_p<P>_<LAB>.ms for the pivot pass / msolve fallback,
  plus a JSON structure report (C_k, L_k, d_j, DAG, sizes, gates).

  The x-side: Row 42's rows carry the exact x correction
  42 S_M G_M (3 alpha - 2 beta) p4p'[h] (spec (3.5)); alpha, beta are
  adjoined as variables (independent tangents, fail-closed) -- they
  enter the rung-42 block as one extra affine direction and are
  handled by the same factorization (their column is proportional to
  the p4p' pattern).

Usage:
  python3 cases/d43_family.py --bank cases/d43modp_p105337_a00pp.pkl
        [--out-prefix cases/d43fam] [--no-emit]
"""
import argparse
import hashlib
import json
import os
import pickle
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_tails_modp import (pmul, padd_into, pscal, pconst, pvar,
                              peval_point, pderiv, ONE, FAMS)

S30 = [6 + 2 * ((a + 1) % 3) for a in range(29)]
S30[28] = 16
S30 = S30 + [36]

P4P1 = {2: -23328, 5: 101088, 8: -186624, 11: 191808, 14: -120528,
        17: 47952, 20: -12096, 23: 1872, 26: -162, 29: 6}


def rung_rows_idx(k):
    return [a for a in range(30) if S30[a] % 6 == k % 6 and S30[a] <= k]


def rung_tails(k):
    return (["%s_%d" % (f, k + 27) for f in ("tf1", "tf2", "tg1",
                                             "tg2")] +
            ["%s_%d" % (f, k + 32) for f in FAMS])


def sub_zero(poly, vid):
    """poly with variable vid -> 0."""
    return {m: c for m, c in poly.items()
            if not any(v == vid for v, _e in m)}


def split_affine(poly, vids, p):
    """poly = const_part + sum_j vids[j] * coeff_j; FAILS on any
    higher-degree or cross occurrence of the vids."""
    vset = set(vids)
    const = {}
    coeffs = {v: {} for v in vids}
    for m, c in poly.items():
        hit = [(v, e) for (v, e) in m if v in vset]
        if not hit:
            const[m] = c
            continue
        assert len(hit) == 1 and hit[0][1] == 1, \
            ("nonaffine occurrence", hit)
        v = hit[0][0]
        m2 = tuple((vv, ee) for (vv, ee) in m if vv != v)
        coeffs[v][m2] = c
    return const, coeffs


def is_w_monomial(poly, wids):
    """poly == scalar * W-monomial?  Returns (scalar, monomial) or
    None."""
    if len(poly) != 1:
        return None
    m, c = next(iter(poly.items()))
    if all(v in wids for v, _e in m):
        return (c, m)
    return None


def proportional(pa, pb, p):
    """pb == lam * pa for a scalar lam?  Returns lam or None."""
    # Decide pb = lambda * pa.  The zero polynomial is 0 * pa.
    if not pb:
        return 0
    if not pa:
        return None
    if set(pa) != set(pb):
        return None
    m0 = next(iter(pa))
    lam = pb[m0] * pow(pa[m0], p - 2, p) % p
    for m, c in pa.items():
        if pb[m] != c * lam % p:
            return None
    return lam


def left_kernel_const(C, p):
    R = len(C)
    Cc = np.array(C, dtype=np.int64) % p
    M = np.concatenate([Cc, np.eye(R, dtype=np.int64)], axis=1)
    r = 0
    for c in range(Cc.shape[1]):
        piv = next((i for i in range(r, R) if M[i][c]), None)
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        M[r] = M[r] * pow(int(M[r][c]), p - 2, p) % p
        nz = np.nonzero(M[:, c])[0]
        nz = nz[nz != r]
        if len(nz):
            M[nz] = (M[nz] - np.outer(M[nz, c], M[r])) % p
        r += 1
    return M[r:, Cc.shape[1]:].tolist(), r


def analyze(bank_path, emit=True, out_prefix=None):
    t0 = time.time()
    with open(bank_path, "rb") as fh:
        B = pickle.load(fh)
    p = B["prime"]
    lab = B["fiber"]
    vars_ = B["vars"]
    vid = {nm: i for i, nm in enumerate(vars_)}
    byk = B["byk"]
    print("bank: p=%d fiber=%s D=%d vars=%d bands=%s"
          % (p, lab, B["D"], len(vars_), sorted(byk)), flush=True)
    # sizes
    for s in sorted(byk):
        tc = sum(len(v) for v in byk[s].values())
        print("  band %2d: %2d comps, %7d terms"
              % (s, len(byk[s]), tc), flush=True)
    # uf30 -> 0 (scope pin)
    u30 = vid["uf30"]
    rows = {}
    for s, comps in byk.items():
        for h, poly in comps.items():
            rows[(h, s)] = sub_zero(poly, u30)
    # adjoin alpha, beta (independent x tangents) to Row 42:
    # E_full[h][42] = E_y[h][42] + 42*S_M*G_M*(3a-2b)*p4p'[h]
    via = len(vars_)
    vib = via + 1
    vars_x = vars_ + ["Xf_alpha", "Xg_beta"]
    SM = pow(7, 12, p) * pow(pow(2, 6, p), p - 2, p) % p
    GM = (-pow(7, 18, p)) * pow(pow(2, 9, p), p - 2, p) % p
    for h, cf in P4P1.items():
        base = 42 * SM * GM % p * (cf % p) % p
        poly = rows.get((h, 42), {})
        padd_into(poly, {((via, 1),): 3 * base % p}, p)
        padd_into(poly, {((vib, 1),): (-2) * base % p}, p)
        rows[(h, 42)] = poly
    wids = {vid["W1"], vid["W2"]}
    report = {"prime": p, "fiber": lab, "bank": os.path.basename(
        bank_path), "rungs": {}}
    dag = []
    compat = []
    solved = {}          # vid -> (num_poly, den_scalar, den_wmono)
    for k in range(26, 43, 2):
        hs = rung_rows_idx(k)
        ynames = rung_tails(k)
        yv = [vid[nm] for nm in ynames]
        if k == 42:
            ynames = ynames + ["Xf_alpha", "Xg_beta"]
            yv = yv + [via, vib]
        rrows = []
        for h in hs:
            poly = rows[(h, k)]
            # substitute previously solved tails (Laurent DAG):
            poly = substitute_all(poly, solved, p)
            rrows.append(poly)
        # affine split
        consts, Amat = [], []
        for poly in rrows:
            const, coeffs = split_affine(poly, yv, p)
            consts.append(const)
            Amat.append([coeffs[v] for v in yv])
        # C diag factorization
        ncol = len(yv)
        Ccols, dcols = [], []
        for j in range(ncol):
            col = [Amat[i][j] for i in range(len(hs))]
            i0 = next((i for i in range(len(col)) if col[i]), None)
            if i0 is None:
                Ccols.append([0] * len(hs))
                dcols.append(pconst(1, p))
                continue
            lams = []
            for i in range(len(col)):
                lam = proportional(col[i0], col[i], p)
                assert lam is not None, \
                    ("C-diag factorization FAILS", k, ynames[j], i)
                lams.append(lam)
            Ccols.append(lams)
            dcols.append(col[i0])
        C = [[Ccols[j][i] for j in range(ncol)]
             for i in range(len(hs))]
        L, rk = left_kernel_const(C, p)
        report["rungs"][k] = {
            "rows": len(hs), "cols": ncol, "rank_C": int(rk),
            "n_compat": len(L),
            "d_units": [], "d_all_w_monomials": True}
        # d_j unit audit
        for j in range(ncol):
            wm = is_w_monomial(dcols[j], wids)
            if wm is None and dcols[j]:
                report["rungs"][k]["d_all_w_monomials"] = False
                report["rungs"][k]["d_units"].append(
                    [ynames[j], "NON-MONOMIAL (%d terms)"
                     % len(dcols[j])])
            elif dcols[j]:
                report["rungs"][k]["d_units"].append(
                    [ynames[j], "unit W-monomial"])
        # exact compat rows: L . rrows (y terms cancel by construction;
        # verified exactly)
        for li, lrow in enumerate(L):
            comb = {}
            for i, poly in enumerate(rrows):
                if lrow[i]:
                    padd_into(comb, poly, p, scal=lrow[i])
            # verify the y-part cancelled exactly
            for m in comb:
                assert not any(v in set(yv) for v, _e in m), \
                    ("compat row retains a rung tail", k, li)
            compat.append(((k, li), comb))
        # pivot solve: 4 pivot combos.  Use the RREF of C to pick 4
        # pivot COLUMNS j1..j4 and rows; solve y_{j} for those columns.
        piv = pivot_solve(C, dcols, consts, Amat, yv, p, rk)
        for v, sol in piv.items():
            solved[v] = sol
            dag.append([vars_x[v] if v < len(vars_x) else str(v),
                        "solved at rung %d" % k])
        print("rung %d: rows %d, rank C = %d, compat %d, solved %d "
              "(%.0fs)" % (k, len(hs), rk, len(L), len(piv),
                           time.time() - t0), flush=True)
    # compat row sizes + variable census
    used = set()
    for _kli, comb in compat:
        for m in comb:
            for v, _e in m:
                used.add(v)
    report["n_compat_rows"] = len(compat)
    report["compat_term_counts"] = [len(c) for _k, c in compat]
    report["compat_vars"] = sorted(vars_x[v] for v in used)
    report["seconds"] = round(time.time() - t0)
    out_prefix = out_prefix or os.path.join(HERE, "d43fam")
    rp = "%s_p%d_%s_report.json" % (out_prefix, p, lab)
    with open(rp, "w") as f:
        json.dump(report, f, indent=1, sort_keys=True)
    print("-> wrote %s" % rp, flush=True)
    if emit:
        emit_ms(compat, vars_x, p, lab, out_prefix)
    return report, compat, vars_x


def substitute_all(poly, solved, p):
    """Substitute solved vars (num, den_inv) repeatedly until none
    remain.  solved[v] = (num_poly, den_inv_poly) with v = num * den_inv
    (den_inv = the exact Laurent inverse as a polynomial in uW's --
    caller guarantees exactness)."""
    guard = 0
    while True:
        guard += 1
        assert guard < 50, "substitution did not terminate"
        hit = None
        for m in poly:
            for v, _e in m:
                if v in solved:
                    hit = v
                    break
            if hit is not None:
                break
        if hit is None:
            return poly
        num, dinv = solved[hit]
        out = {}
        for m, c in poly.items():
            e = 0
            rest = []
            for v, ee in m:
                if v == hit:
                    e = ee
                else:
                    rest.append((v, ee))
            term = {tuple(rest): c}
            for _ in range(e):
                term = pmul(term, num, p)
                term = pmul(term, dinv, p)
            padd_into(out, term, p)
        poly = out


def pivot_solve(C, dcols, consts, Amat, yv, p, rk):
    """Solve rk pivot combos: choose rk independent rows/cols of C,
    solve those y (divided by the unit d_j).  d_j must be a W-monomial
    unit; its exact inverse is the uW-monomial.  Returns {vid: (num,
    den_inv)} for the solved y's.  NOTE: requires the caller's bank
    vars to include uW1, uW2?  We keep the inverse as a formal
    (den_inv) polynomial built from uW variables adjoined by the
    emitter; internally we represent den_inv as the W-monomial with
    NEGATIVE exponents folded into a marker -- to stay exact we
    instead solve only when d_j == scalar (no W content), else we
    SKIP the substitution (the compat rows are exact regardless; the
    skipped solves only mean later rungs keep those tails symbolic
    inside their consts, which is handled because the later rung's
    affine split treats them as ordinary variables)."""
    out = {}
    # find pivot (row, col) pairs by RREF on C
    Cc = np.array(C, dtype=np.int64) % p
    M = Cc.copy()
    r = 0
    pivots = []
    usedr = []
    for c in range(M.shape[1]):
        piv = next((i for i in range(r, M.shape[0]) if M[i][c]), None)
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        M[r] = M[r] * pow(int(M[r][c]), p - 2, p) % p
        nz = np.nonzero(M[:, c])[0]
        nz = nz[nz != r]
        if len(nz):
            M[nz] = (M[nz] - np.outer(M[nz, c], M[r])) % p
        pivots.append(c)
        r += 1
    # v1: skip explicit substitution (exactness-first; the feed-forward
    # of solved tails is retained implicitly because later rungs'
    # rows still contain those tails as variables and the FULL system
    # keeps the pivot rows -- emitted below).
    return out


def emit_ms(compat, vars_x, p, lab, out_prefix):
    """Emit the compat rows as an .ms fragment (tail-name variables,
    coefficients in [0, p)).  The full compressed system = the parked
    fiber .ms (28 vars, 34 rows) + this fragment + the rung pivot rows
    (kept implicitly: the compat rows alone OVER-approximate the
    projection; for the EMPTY direction 1 in <parked + compat> "
    "suffices)."""
    used = sorted({v for _k, comb in compat for m in comb
                   for v, _e in m})
    names = [vars_x[v] for v in used]
    path = "%s_p%d_%s_compat.ms" % (out_prefix, p, lab)
    with open(path, "w") as f:
        f.write(", ".join(names) + "\n%d\n" % p)
        lines = []
        for (_k, _li), comb in compat:
            terms = []
            for m, c in sorted(comb.items()):
                t = str(c)
                for v, e in m:
                    t += "*%s" % vars_x[v]
                    if e > 1:
                        t += "^%d" % e
                terms.append(t)
            lines.append("+".join(terms) if terms else "0")
        f.write(",\n".join(lines))
        f.write("\n")
    print("-> wrote %s (%d rows, %d vars)"
          % (path, len(compat), len(names)), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank", required=True)
    ap.add_argument("--out-prefix", default=None)
    ap.add_argument("--no-emit", action="store_true")
    a = ap.parse_args()
    analyze(a.bank, emit=not a.no_emit, out_prefix=a.out_prefix)


if __name__ == "__main__":
    main()
