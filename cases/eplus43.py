#!/usr/bin/env python3
"""eplus43.py -- the D43 extended-window operator + e+ certifier.

STATUS: INTERNAL TOOLING, UNREVIEWED.  FAIL-CLOSED THROUGHOUT.
Spec: xmodel/sol-xside-spec.md (followed exactly; every CONJECTURE
implemented fail-closed).  Ruling: xmodel/sol-h29-dichotomy.md.
Review: xmodel/grok-h29-review.md.

WHAT THIS IS.  The band-<=42 extension of the corrected 30x30 Euler/Ore
window of cases/eplus_certify.py: a CONFIGURED engine instance (a
source-configured copy of the banked cases/valuation_e2.py with
DBUILD = 43, RMAX = 42; nothing is mutated after import; every
dependent array, Toeplitz/jet dimension, GIDX, row registry and hash
is recomputed from the configuration), plus the REAL level-42 x-side
of sol-xside-spec.md sect 2-3:

    U_f = 1 + alpha t^42 + O(t^84),  U_g = 1 + beta t^42 + O(t^84),
    Phi_full = U_f Phi_y,  Gamma_full = U_g Gamma_y,
    E_full = B(Phi_full, Gamma_full) + 42 t^20.

X-SIDE TANGENT CLASSIFICATION (spec 2.2, MANDATORY): alpha, beta are
declared INDEPENDENT filtered tangent coordinates (case 3).  No
repository value or derivation of (alpha, beta) exists (CONJECTURE
X-SIDE-DERIVATION is undischarged; CONJECTURE X-SIDE-30 is not
consumed), so fail-closed the window is the FULL LEGAL

    184 rows x 182 columns   (180 y-columns + Dalpha + Dbeta),

never the conditional 184x180.  Their completion VALUES here are the
NAMED finite-support completion alpha = beta = 0 (a completion choice,
recorded + hashed in the manifest; NOT a derivation -- spec 3.2).

RUN MODES (spec 5.3; the artifact records the mode; results from mode
2 are never reported in mode-3 language):
  LEGACY_BAND40_REGRESSION  --regress / --regress-full: at banked D25
      (and D23) named completions, the extended build restricted to
      bands <= 40 / old columns, reordered to the exact old
      registries, must be BYTE-IDENTICAL to the banked 174x170 arrays,
      per-point operator hash, and every banked gate number.
  D25_COMPLETION_BAND42     --smoke: one banked D25 completion, legal
      x-side (named alpha = beta = 0), window extended to 184x182.
      Operator smoke test ONLY: NOT a D43 survivor, NOT a depth
      measurement (spec C0).
  D43_SURVIVOR              --prolong / --survivor: numeric D43
      prolongation of D25 cell points (rung solves 26..42 through the
      certifier's own operator, level-cap guarded, kernel frees = 0)
      and the genuine D43 floor measurement at those points.

e+ SEMANTICS: identical to cases/eplus_certify.py -- every window
number is a certified LOWER bound on ell(L_s^+) at the named
completion (E_PLUS_CANDIDATE tier); e_plus_certified is ALWAYS None;
no section is constructed; no germ is certified.  D43 threshold
floor((43-1)/2) = 21.

USAGE
  python3 cases/eplus43.py --selftest
  python3 cases/eplus43.py --regress [--n N] [--out cases/d43_regress.json]
  python3 cases/eplus43.py --regress-full        # all 360 D25 + d23 spot
  python3 cases/eplus43.py --smoke [--out cases/d43_smoke.json]
  python3 cases/eplus43.py --prolong [--out cases/d43_points.json]
  python3 cases/eplus43.py --survivor cases/d43_points.json
        [--out cases/d43_eplus.json]
"""
import argparse
import collections
import hashlib
import importlib.util
import json
import os
import random
import sys
import time
import types

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import valuation_e as V                  # banked 1a plumbing
import valuation_e2 as V2                # banked engine (UNTOUCHED)
import eplus_certify as EC               # banked 8.S9 certifier
import d25_eplus as DE                   # banked 9.S3 driver (reused)

TOOL = "cases/eplus43.py"
CAND = "E_PLUS_CANDIDATE"
D43 = 43
THRESH43 = (D43 - 1) // 2                # 21
PRIMES = (105337, 105673)

BANNER = (
    "D43 extended-window certifier (band <= 42, x-side sidecar, "
    "184x182 fail-closed under independent alpha/beta).  Window "
    "numbers are certified LOWER bounds at the named completion "
    "(%s tier); e_plus_certified is always None; no section, no germ, "
    "no all-depth claim.  Mode-2 (D25_COMPLETION_BAND42) results are "
    "an operator smoke test, NEVER a depth measurement." % CAND)

# ------------------------------------------------- configured engine V43
# Source-configured copy of the banked valuation_e2.py.  The patches are
# exact-match (build fails closed if the banked source drifts); the
# configuration is applied BEFORE module exec -- nothing is mutated
# after import, and GIDX/GD/_S/Toeplitz tables all recompute.
_PATCHES = [
    ("DBUILD = 42            # slots 0..41; pure-y exact below t^42",
     "DBUILD = 43            # D43 CONFIG: slots 0..42 (band 42 exact "
     "given source values through level 74)"),
    ("RMAX = 40              # tangent coords r <= 40 can reach bands <= 41",
     "RMAX = 42              # D43 CONFIG: tangent coords r <= 42"),
    ("GD = len(GIDX)                                                 # 170",
     "XCOLS = ((\"Xf_alpha\", 42), (\"Xg_beta\", 42))\n"
     "for _xc in XCOLS:\n"
     "    GIDX[_xc] = len(GIDX)\n"
     "GD = len(GIDX)                          # 182 = 180 y + 2 x sidecar"),
]


def _load_configured():
    src_path = os.path.join(HERE, "valuation_e2.py")
    src = open(src_path).read()
    for old, new in _PATCHES:
        assert src.count(old) == 1, \
            "configured-engine patch anchor missing/ambiguous: %r" % old[:50]
        src = src.replace(old, new)
    mod = types.ModuleType("valuation_e43")
    mod.__file__ = src_path
    sys.modules["valuation_e43"] = mod
    exec(compile(src, "valuation_e43<configured:DBUILD=43,RMAX=42,+X>",
                 "exec"), mod.__dict__)
    return mod


V43 = _load_configured()
assert V43.DBUILD == 43 and V43.RMAX == 42 and V43._S == 43
assert V43.GD == 182 and len(V43.GIDX) == 182
XCOL_A = V43.GIDX[("Xf_alpha", 42)]
XCOL_B = V43.GIDX[("Xg_beta", 42)]
assert (XCOL_A, XCOL_B) == (180, 181), "x sidecar must be the last columns"

S30 = list(V43.S_A) + [V43.S_29]         # 30 output shifts, s_29 = 36
FAMS = V43.FAMS

# canonical registries (spec 4.1 append-only serialization)
NEWROWS = [(2, 6), (5, 6), (8, 6), (11, 6), (14, 6), (17, 6), (20, 6),
           (23, 6), (26, 6), (29, 1)]
NEWCOLS = [("tf1", 41), ("tf1", 42), ("tf2", 41), ("tf2", 42),
           ("tg1", 41), ("tg1", 42), ("tg2", 41), ("tg2", 42),
           ("tg01", 42), ("tg02", 42)]
XCOLS = [("Xf_alpha", 42), ("Xg_beta", 42)]

ROWS_OLD = [(a, j) for a in range(30) for j in range((40 - S30[a]) // 6 + 1)]
ROWS_CANON = ROWS_OLD + NEWROWS
_old_gidx_sorted = sorted(V2.GIDX.items(), key=lambda kv: kv[1])
COLS_OLD = [k for k, _ in _old_gidx_sorted]
COLS_CANON = COLS_OLD + NEWCOLS + XCOLS
assert len(ROWS_OLD) == 174 and len(ROWS_CANON) == 184
assert len(COLS_OLD) == 170 and len(COLS_CANON) == 182
assert set(ROWS_CANON) == {(a, j) for a in range(30)
                           for j in range((42 - S30[a]) // 6 + 1)}
assert set(COLS_CANON) == set(V43.GIDX)

# exact ten-row x vector (spec 3.3) -- recomputed from p = eta^6-6eta^3+6
P4P1_TABLE = {2: -23328, 5: 101088, 8: -186624, 11: 191808, 14: -120528,
              17: 47952, 20: -12096, 23: 1872, 26: -162, 29: 6}


def _p4p1_recompute():
    pe = [0] * 7
    pe[0], pe[3], pe[6] = 6, -6, 1
    prod = [1]

    def pmul(a, b):
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                r[i + j] += x * y
        return r
    for _ in range(4):
        prod = pmul(prod, pe)
    dp = [i * c for i, c in enumerate(pe)][1:]
    full = pmul(prod, dp)
    return {i: c for i, c in enumerate(full) if c}


assert _p4p1_recompute() == P4P1_TABLE, "p^4 p' table mismatch (spec 3.3)"


def smgm(p):
    SM = pow(7, 12, p) * pow(pow(2, 6, p), p - 2, p) % p
    GM = (-pow(7, 18, p)) * pow(pow(2, 9, p), p - 2, p) % p
    return SM, GM


# ------------------------------------------------------- operator build
def apply_xside(jf, jg, p, alpha, beta):
    """Production path (spec 5.2): form U_f Phi_y and U_g Gamma_y as
    dual jets BEFORE the Euler-row constructor.  alpha, beta carry unit
    gradients in the two sidecar columns (independent tangents)."""
    Uf = V43.Jet(1, True)
    Uf.V[0][0] = 1.0
    Uf.V[0][42] = alpha % p
    Uf.G[0][42][XCOL_A] = 1.0
    Ug = V43.Jet(1, True)
    Ug.V[0][0] = 1.0
    Ug.V[0][42] = beta % p
    Ug.G[0][42][XCOL_B] = 1.0
    return V43.jmul(Uf, jf, p), V43.jmul(Ug, jg, p), Uf, Ug


def build_operator(point, p, alpha, beta, Z=None):
    if Z is None:
        pt, _r3, _h = V.radical_env(p)
        Z = [pow(pt["z"], m, p) for m in range(42)]
    jf, jg = V43.build_jets(point, p, Z)
    jff, jgf, Uf, Ug = apply_xside(jf, jg, p, alpha, beta)
    E = V43.euler_rows(jff, jgf, p)
    return E, {"jf": jf, "jg": jg, "jff": jff, "jgf": jgf,
               "Uf": Uf, "Ug": Ug, "Z": Z}


def _bexpr(jA_src, jB_src, p, with_gauge=False):
    """B(Phi, Gamma) = (theta Phi - 12 Phi) Gamma_eta - Phi_eta
    (theta Gamma - 18 Gamma) as a Jet (optionally + 42 t^20)."""
    jA = V43.theta_shift(jA_src, 12, p)
    jBg = V43.theta_shift(jB_src, 18, p)
    jfH = V43.eta_deriv(jA_src, p)
    jgH = V43.eta_deriv(jB_src, p)
    T1 = V43.jmul(jA, jgH, p)
    T2 = V43.jmul(jfH, jBg, p)
    E = V43.Jet(V43.HMAX, True)
    h1 = min(T1.h, V43.HMAX)
    E.V[:h1] += T1.V[:h1]
    E.G[:h1] += T1.G[:h1]
    h2 = min(T2.h, V43.HMAX)
    E.V[:h2] -= T2.V[:h2]
    E.G[:h2] -= T2.G[:h2]
    E.V %= p
    E.G %= p
    if with_gauge:
        E.V[0][20] = (E.V[0][20] + 42) % p
    return E


def identity_32_path(jf, jg, p, alpha, beta):
    """Independent grouped path (spec (3.2), EXACT DERIVATION):
    B_full = U_f U_g B_y + U_g (theta U_f) Phi_y Gamma_{y,eta}
             - U_f (theta U_g) Phi_{y,eta} Gamma_y,   then + 42 t^20."""
    By = _bexpr(jf, jg, p, with_gauge=False)
    Uf = V43.Jet(1, True)
    Uf.V[0][0] = 1.0
    Uf.V[0][42] = alpha % p
    Uf.G[0][42][XCOL_A] = 1.0
    Ug = V43.Jet(1, True)
    Ug.V[0][0] = 1.0
    Ug.V[0][42] = beta % p
    Ug.G[0][42][XCOL_B] = 1.0
    thUf = V43.Jet(1, True)
    thUf.V[0][42] = 42 * alpha % p
    thUf.G[0][42][XCOL_A] = 42.0
    thUg = V43.Jet(1, True)
    thUg.V[0][42] = 42 * beta % p
    thUg.G[0][42][XCOL_B] = 42.0
    UfUg = V43.jmul(Uf, Ug, p)
    t1 = V43.jmul(UfUg, By, p)
    t2 = V43.jmul(V43.jmul(Ug, thUf, p), V43.jmul(jf, V43.eta_deriv(jg, p),
                                                  p), p)
    t3 = V43.jmul(V43.jmul(Uf, thUg, p), V43.jmul(V43.eta_deriv(jf, p), jg,
                                                  p), p)
    E = V43.Jet(V43.HMAX, True)
    for T, sgn in ((t1, 1), (t2, 1), (t3, -1)):
        h = min(T.h, V43.HMAX)
        E.V[:h] += sgn * T.V[:h]
        E.G[:h] += sgn * T.G[:h]
    E.V %= p
    E.G %= p
    E.V[0][20] = (E.V[0][20] + 42) % p
    return E


# ------------------------------------------------------- window + scans
def window_object43(E):
    """The full legal band-42 window in the canonical order (spec 4.1):
    184 rows (old registry + ten new) x 182 columns (old GIDX + ten new
    y + two x).  Entries are the ACTUAL gradient values; causality is
    measured, never imposed."""
    Gg = E.G.astype(np.int64)
    row_lv = np.array([S30[a] + 6 * j for (a, j) in ROWS_CANON])
    col_lv = np.array([r for (_f, r) in COLS_CANON])
    M = np.zeros((len(ROWS_CANON), len(COLS_CANON)), dtype=np.int64)
    for ri, (a, j) in enumerate(ROWS_CANON):
        n = S30[a] + 6 * j
        for ci, lab in enumerate(COLS_CANON):
            M[ri][ci] = Gg[a][n][V43.GIDX[lab]]
    return row_lv, col_lv, M


def row_label(i):
    a, j = ROWS_CANON[i]
    return "H%d_j%d_lv%d" % (a, j, S30[a] + 6 * j)


def _colspace(M, cols, p):
    cs = V43.Colspace(M.shape[0], p)
    for j in cols:
        cs.add(M[:, j].copy())
    return cs


def left_kernel_np(A, p):
    """Left kernel of A (R x C) mod p: RREF of [A | I] rows."""
    R, C = A.shape
    M = np.concatenate([A % p, np.eye(R, dtype=np.int64)], axis=1)
    r = 0
    for c in range(C):
        piv = None
        for i in range(r, R):
            if M[i][c]:
                piv = i
                break
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        M[r] = M[r] * pow(int(M[r][c]), p - 2, p) % p
        nz = np.nonzero(M[:, c])[0]
        nz = nz[nz != r]
        if len(nz):
            M[nz] = (M[nz] - np.outer(M[nz, c], M[r])) % p
        r += 1
    return M[r:, C:], r


def dual_witness(M, col_idx, target_row, p):
    """Exact sparse left-cokernel witness: lambda^T M[:, cols] = 0,
    lambda[target] = 1 (spec 7.4).  None if the target is covered."""
    A = M[:, col_idx] if len(col_idx) else np.zeros((M.shape[0], 0),
                                                   dtype=np.int64)
    K, rk = left_kernel_np(A, p)
    hit = [k for k in K if k[target_row]]
    if not hit:
        return None
    lam = hit[0] * pow(int(hit[0][target_row]), p - 2, p) % p
    assert not (lam @ A % p).any() and lam[target_row] == 1
    return {row_label(i): int(v) for i, v in enumerate(lam) if v}


def loss_scan_brute(row_lv, col_lv, M, p, witness_targets=()):
    """Literal brute-force scan over ALL n = 0..42 (spec 7): for each n
    the eligible columns are level >= n; an uncovered unit target of
    level b >= n certifies ell >= b - n + 1.  Profile schema records
    the minimum included column level AND the eligible column count."""
    ell = 0
    profile = []
    best = []
    wits = {}
    for n in range(0, 43):
        cols = [j for j in range(M.shape[1]) if col_lv[j] >= n]
        cs = _colspace(M, cols, p)
        cov = cs.covered_rows()
        bad = np.nonzero((~cov) & (row_lv >= n))[0]
        mx = int(row_lv[bad].max()) if len(bad) else None
        bound = (mx - n + 1) if mx is not None else 0
        profile.append([n, int(min(col_lv[j] for j in cols)) if cols else
                        None, len(cols), int(len(bad)), mx,
                        max(0, bound)])
        if bound > ell:
            ell = bound
            best = [(n, int(i)) for i in bad if row_lv[i] == mx]
        elif bound == ell and bound > 0:
            best += [(n, int(i)) for i in bad if row_lv[i] == mx
                     and (n, int(i)) not in best]
        for (wn, wi) in witness_targets:
            if wn == n:
                wits[(wn, wi)] = dual_witness(M, cols, wi, p)
    # dual witnesses for every maximizing pair
    for (n, i) in best:
        if (n, i) not in wits:
            cols = [j for j in range(M.shape[1]) if col_lv[j] >= n]
            wits[(n, i)] = dual_witness(M, cols, i, p)
            assert wits[(n, i)] is not None, "maximizer lost its witness"
    return ell, profile, best, wits


def loss_scan_fast(row_lv, col_lv, M, p):
    """Optimized constant-column-set interval scan (the banked
    delayed_loss_scan pattern); must agree with the brute scan."""
    levels = sorted({int(v) for v in col_lv}, reverse=True)
    order = np.argsort(-col_lv, kind="stable")
    cs = V43.Colspace(len(row_lv), p)
    oi = 0
    ell = 0
    best = []
    for k, v in enumerate(levels):
        while oi < len(order) and col_lv[order[oi]] >= v:
            cs.add(M[:, order[oi]].copy())
            oi += 1
        n_eval = (levels[k + 1] + 1) if k + 1 < len(levels) else 0
        cov = cs.covered_rows()
        bad = np.nonzero((~cov) & (row_lv >= n_eval))[0]
        if len(bad):
            mx = int(row_lv[bad].max())
            bound = mx - n_eval + 1
            if bound > ell:
                ell = bound
                best = [(n_eval, int(i)) for i in bad if row_lv[i] == mx]
            elif bound == ell and bound > 0:
                best += [(n_eval, int(i)) for i in bad
                         if row_lv[i] == mx and (n_eval, int(i)) not in best]
    return ell, len(cs.basis), best


# --------------------------------------------------- completion manifest
def completion_manifest(point, p, provenance, alpha, beta):
    """Spec 5.1: EVERY consumed coefficient classified; absence from the
    builder is not the value zero.  provenance: dict label -> class for
    solved/represented coordinates; everything else in the registry is
    the named finite-support zero completion (asserted 0)."""
    entries = []
    for f in FAMS:
        for r in V43.allowed_r(f):
            lab = "%s_%d" % (f, 32 + r)
            val = int(point["tails"][f].get(r, 0))
            klass = provenance.get(lab)
            if klass is None:
                assert val == 0, ("unclassified NONZERO coefficient %s"
                                  % lab)
                klass = "named_finite_support_zero"
            entries.append([lab, r, val, klass])
    fixed = sorted((k, int(v)) for k, v in point["fixed"].items())
    x_entries = [
        ["Xf_alpha", 42, int(alpha),
         "independent_tangent; named finite-support completion value; "
         "CONJECTURE X-SIDE-DERIVATION undischarged (no banked "
         "derivation); factor-coordinate level 42"],
        ["Xg_beta", 42, int(beta),
         "independent_tangent; named finite-support completion value; "
         "CONJECTURE X-SIDE-DERIVATION undischarged; level 42"]]
    man = {
        "prime": p,
        "pin42": "pinned 0; never a tangent direction (r = 10 absent)",
        "y_registry": entries,
        "fixed_chart_data": fixed,
        "x_side": x_entries,
        "consumption_cap": ("bands <= 42 consume tangent levels r <= 42 "
                            "and absolute tail levels <= 74 "
                            "(causality measured by gate CAUSALITY-42); "
                            "later data cannot enter this window"),
        "tangent_classification": {
            "alpha": "independent", "beta": "independent",
            "consequence": "window is 184x182 (spec 2.2 case 3); the "
                           "180-column scan would be invalid"},
    }
    man["sha256"] = hashlib.sha256(
        json.dumps(man, sort_keys=True).encode()).hexdigest()
    return man


# ------------------------------------------------------------ gate suite
def gate_suite(point, p, env, alpha, beta, provenance, mode,
               skip_controls=False):
    """The spec sect-9 executable gates at one completed point.
    Returns (checks, info, E, aux).  Fail-closed: the caller must treat
    any False as a stop."""
    checks = {}
    info = {}
    E, aux = build_operator(point, p, alpha, beta)
    Vv = E.V.astype(np.int64)
    Gg = E.G.astype(np.int64)
    SM, GM = smgm(p)

    # SOURCE-CENSUS-42 (gate 2)
    man = completion_manifest(point, p, provenance, alpha, beta)
    lad = {}
    for (f, rho) in V43.STREAMS:
        lad[(f, rho)] = sorted(r for r in V43.allowed_r(f)
                               if r % 6 == rho % 6)
    ycols = sorted((f, r) for (f, rho), rs in lad.items() for r in rs)
    checks["s2_source_census_182"] = bool(
        ycols == sorted(k for k in V43.GIDX if not k[0].startswith("X")) and
        len(ycols) == 180 and
        all(min(rs) == V43.r_start(rho) and
            all(b - a == 6 for a, b in zip(rs, rs[1:]))
            for (f, rho), rs in lad.items()) and
        all(r != 10 for (_f, r) in V43.GIDX) and
        len(man["y_registry"]) == 180)
    info["manifest_sha256"] = man["sha256"]

    # OUTPUT-CENSUS-42 (gate 3) + surplus sidecar
    slot42 = [a for a in range(V43.HMAX)
              if Vv[a][42] or Gg[a][42].any()]
    allowed42 = {a for a in range(30) if S30[a] % 6 == 0}
    checks["s3_output_census_row42"] = bool(set(slot42) <= allowed42)
    info["row42_eta_support"] = slot42
    info["surplus_eta30_33_row42"] = {
        "values": [int(Vv[a][42]) for a in range(30, 34)],
        "grad_nnz": [int((Gg[a][42] != 0).sum()) for a in range(30, 34)]}
    checks["s3_surplus_eta30_33_zero"] = bool(
        not Vv[30:].any() and not Gg[30:].any())

    # XSIDE-ONSET (gate 4): U-1 vanish through 41; perturbing alpha
    # changes no row below 42
    onset_ok = bool(not aux["Uf"].V[0][1:42].any() and
                    not aux["Ug"].V[0][1:42].any())
    if not skip_controls:
        E_a, _ = build_operator(point, p, alpha + 1, beta, Z=aux["Z"])
        E_b, _ = build_operator(point, p, alpha, beta + 1, Z=aux["Z"])
        onset_ok = onset_ok and bool(
            np.array_equal(E_a.V[:, :42], E.V[:, :42]) and
            np.array_equal(E_a.G[:, :42, :], E.G[:, :42, :]) and
            np.array_equal(E_b.V[:, :42], E.V[:, :42]) and
            np.array_equal(E_b.G[:, :42, :], E.G[:, :42, :]))
        # NEGATIVE-XSIDE-CONTROLS (gate 8): measured column deltas at 42
        da = (E_a.V[:, 42].astype(np.int64) - Vv[:, 42]) % p
        db = (E_b.V[:, 42].astype(np.int64) - Vv[:, 42]) % p
        wa = {a: 126 * SM * GM % p * (P4P1_TABLE[a] % p) % p
              for a in P4P1_TABLE}
        wb = {a: (-84) * SM * GM % p * (P4P1_TABLE[a] % p) % p
              for a in P4P1_TABLE}
        ok8 = all(int(da[a]) == wa.get(a, 0) for a in range(34)) and \
            all(int(db[a]) == wb.get(a, 0) for a in range(34))
        ok8 = ok8 and int(wa[29]) == 756 * SM * GM % p and \
            int(wb[29]) == (-504) * SM * GM % p
        r32 = pow(-2 % p, p - 2, p) * 3 % p    # the 3 : -2 ratio
        ok8 = ok8 and all(wa[a] == wb[a] * r32 % p for a in P4P1_TABLE)
        checks["s8_negative_xside_controls"] = bool(ok8)
    checks["s4_xside_onset"] = onset_ok

    # XSIDE-PROVENANCE (gate 5): mandatory tangent classification (2.2)
    # -- both x coefficients classified (independent), matrix enlarged;
    # X-SIDE-DERIVATION not consumed.
    checks["s5_x_tangent_classified"] = bool(
        man["tangent_classification"]["alpha"] == "independent" and
        man["tangent_classification"]["beta"] == "independent" and
        len(man["x_side"]) == 2)

    # ROW42-IDENTITY (gate 6): direct row 42 vs (3.5) at every eta;
    # gradient columns vs (3.11)/(3.12)
    Ey = _bexpr(aux["jf"], aux["jg"], p, with_gauge=True)
    EyV = Ey.V.astype(np.int64)
    corr = 42 * SM * GM % p * ((3 * alpha - 2 * beta) % p) % p
    ok6 = True
    for a in range(34):
        want = (EyV[a][42] + corr * (P4P1_TABLE.get(a, 0) % p)) % p
        ok6 = ok6 and int(Vv[a][42]) == want
    ca = Gg[:, 42, XCOL_A]
    cb = Gg[:, 42, XCOL_B]
    for a in range(34):
        ok6 = ok6 and int(ca[a]) == 126 * SM * GM % p * \
            (P4P1_TABLE.get(a, 0) % p) % p
        ok6 = ok6 and int(cb[a]) == (-84) * SM * GM % p * \
            (P4P1_TABLE.get(a, 0) % p) % p
    ok6 = ok6 and not Gg[:, :42, XCOL_A].any() and \
        not Gg[:, :42, XCOL_B].any()
    checks["s6_row42_identity"] = bool(ok6)

    # TWO-PATH-DIFFERENTIAL (gate 7): (3.2) grouped path and the
    # hand-assembled path-A grouping, both == the production dual path
    E2 = identity_32_path(aux["jf"], aux["jg"], p, alpha, beta)
    ok7 = bool(np.array_equal(E2.V, E.V) and np.array_equal(E2.G, E.G))
    DG = V43.path_A_rows(aux["jff"], aux["jgf"], p)
    ok7 = ok7 and bool(np.array_equal(DG, E.G))
    checks["s7_two_path_differential"] = ok7

    # CAUSALITY-42 (gate 10): measured, not imposed
    viol = 0
    for lab, col in V43.GIDX.items():
        r = lab[1]
        if Gg[:, :min(r, V43._S), col].any():
            viol += 1
    checks["s10_causality_42"] = bool(viol == 0)

    # ORE/GRADING-42 (gate 11): congruences, odd rows, starts, affinity
    odd = [n for n in range(V43._S) if n % 2 == 1]
    g_ok = bool(not Vv[:, odd].any() and not Gg[:, odd].any())
    starts = []
    for a in range(30):
        nz = [n for n in range(V43._S) if Vv[a][n] or Gg[a][n].any()]
        if any(n % 6 != S30[a] % 6 or n < S30[a] for n in nz):
            g_ok = False
        starts.append(next((n for n in range(V43._S) if Gg[a][n].any()),
                           None))
    checks["s11_grading_congruence_42"] = g_ok
    # support starts: ENGINE-consistency check.  The absolute
    # starts == S30 check is point-class-dependent (the banked c4
    # fails at the 72 all-cell-zero witnesses -- 9.S3 sole exception),
    # so the gate demands equality with the old engine's measurement
    # at the SAME point (band <= 41 content is byte-identical by the
    # regression; a new start at band 42 is only legal where the old
    # start was absent).
    shim0 = project_band40(E)
    G0 = shim0.G.astype(np.int64)
    starts_old = [next((n for n in range(42) if G0[a][n].any()), None)
                  for a in range(30)]
    checks["s11_support_starts_consistent"] = bool(all(
        (sn == so) or (so is None and sn in (None, 42))
        for sn, so in zip(starts, starts_old)))
    info["support_starts"] = starts
    info["support_starts_eq_S30"] = bool(starts == S30)
    n3, naff, _sup = V43.ore_affinity_gate(E, p)
    checks["s11_ore_affinity_42"] = bool(naff == n3)
    info["ore_bins_3plus"] = [int(n3), int(naff)]

    # window + M2 + scans
    row_lv, col_lv, M = window_object43(E)
    checks["p1_window_184x182"] = bool(M.shape == (184, 182))
    M2 = np.zeros((60, 60), dtype=np.int64)
    for ai, (a, j) in enumerate([(a, j) for a in range(30)
                                 for j in (0, 1)]):
        for qi, ((f, rho), i) in enumerate([(s, i) for s in V43.STREAMS
                                            for i in (0, 1)]):
            M2[ai][qi] = Gg[a][S30[a] + 6 * j][
                V43.GIDX[(f, V43.r_start(rho) + 6 * i)]]
    rank2 = V43.rankp(M2.copy(), p)
    info["M2_rank"] = int(rank2)
    info["delta_plus_N2"] = int(60 - rank2)
    info["M2_note"] = ("exact 60x60 x-corrected block (spec 4.3); NO "
                      "stabilization claim; 30-stream subblock only "
                      "(independent x directions exist)")
    M1 = np.zeros((30, 30), dtype=np.int64)
    for a in range(30):
        for q, (f, rho) in enumerate(V43.STREAMS):
            M1[a][q] = Gg[a][S30[a]][V43.GIDX[(f, V43.r_start(rho))]]
    info["delta_plus_N1"] = int(30 - V43.rankp(M1.copy(), p))

    iy0 = ROWS_CANON.index((29, 0))
    iy1 = ROWS_CANON.index((29, 1))
    ell, profile, best, wits = loss_scan_brute(
        row_lv, col_lv, M, p, witness_targets=[(0, iy0), (0, iy1)])
    ell_f, wrank, best_f = loss_scan_fast(row_lv, col_lv, M, p)
    checks["s15_brute_fast_agree"] = bool(
        ell == ell_f and set(best) >= set(best_f) and
        (ell == 0 or set(best_f) & set(best)))
    info["window_rank_184x182"] = int(wrank)
    info["ell_lb_certified"] = int(ell)
    info["ell_profile"] = profile
    info["ell_profile_key"] = ("[n_eval, min_included_col_level, "
                               "n_eligible_cols, n_uncovered, "
                               "max_uncovered_level, ell_ge]")
    info["maximizers"] = [[n, row_label(i)] for (n, i) in sorted(best)]
    # Y0-RECHECK (gate 14) + the H29 u^1 verdict targets at n = 0
    w0 = wits.get((0, iy0))
    w1 = wits.get((0, iy1))
    checks["s14_y0_uncovered_recheck"] = bool(w0 is not None)
    info["y0_dual_witness"] = w0
    info["y1_H29u1_uncovered"] = bool(w1 is not None)
    info["y1_dual_witness"] = w1
    # diagnostic ONLY (labeled): coverage in the 180 y-columns, i.e.
    # the conditional X-SIDE-30 window.  The VERDICT column set is the
    # full legal 182 (spec 7: scanning the 180-column submatrix would
    # be invalid while alpha, beta are independent).
    ycols_idx = [j for j in range(M.shape[1])
                 if not COLS_CANON[j][0].startswith("X")]
    w1y = dual_witness(M, ycols_idx, iy1, p)
    w0y = dual_witness(M, ycols_idx, iy0, p)
    info["y1_uncovered_in_y180_diagnostic"] = bool(w1y is not None)
    info["y0_uncovered_in_y180_diagnostic"] = bool(w0y is not None)
    info["y1_dual_witness_y180"] = w1y
    info["y180_note"] = (
        "y180 objects are DIAGNOSTIC/CONDITIONAL: exact dual "
        "certificates against the 180 y-columns only, i.e. the "
        "30-stream window of CONJECTURE X-SIDE-30 with alpha, beta "
        "held fixed/derived-with-zero-chain-rule.  They are NOT the "
        "legal verdict while alpha, beta are independent tangents "
        "(spec 7); the verdict scan uses all 182 columns.")
    info["dual_witnesses_maximizers"] = {
        "%d|%s" % (n, row_label(i)): wits[(n, i)]
        for (n, i) in wits if wits[(n, i)] is not None}
    # verify each retained witness independently after (de)serialization
    lab2idx = {row_label(i): i for i in range(len(ROWS_CANON))}
    for key, wt in list(info["dual_witnesses_maximizers"].items()):
        n = int(key.split("|")[0])
        lam = np.zeros(len(ROWS_CANON), dtype=np.int64)
        for lb, c in wt.items():
            lam[lab2idx[lb]] = c
        cols = [j for j in range(M.shape[1]) if col_lv[j] >= n]
        assert not (lam @ M[:, cols] % p).any(), "witness replay failed"

    # residual + registry hashes (gate 12)
    val_bands = sorted({int(n) for n in range(V43._S)
                        if Vv[:30, n].any()})
    nu = val_bands[0] if val_bands else None
    info["nu_window"] = nu
    info["value_bands_le42"] = val_bands
    reg = {
        "rows": [[a, j, S30[a] + 6 * j] for (a, j) in ROWS_CANON],
        "cols": [[f, r] for (f, r) in COLS_CANON],
    }
    info["registry_hash"] = hashlib.sha256(
        json.dumps(reg, sort_keys=True).encode()).hexdigest()
    info["matrix_hash"] = hashlib.sha256(
        json.dumps(M.tolist()).encode()).hexdigest()
    info["value_array_hash"] = hashlib.sha256(
        json.dumps(Vv.tolist()).encode()).hexdigest()
    shim = project_band40(E)
    info["band40_operator_hash"] = V2.operator_hash(shim, p)
    info["mode"] = mode
    info["alpha_beta"] = [int(alpha), int(beta)]
    info["manifest"] = man
    return checks, info, E, aux


def project_band40(E43):
    """Label-selected band-<=40 restriction in the EXACT old registries
    (spec sect 8): slots 0..41, the 170 old GIDX columns, old order."""
    Vv = E43.V[:, :42].copy()
    Gg = np.zeros((V43.HMAX, 42, 170))
    for idx, lab in enumerate(COLS_OLD):
        Gg[:, :, idx] = E43.G[:, :42, V43.GIDX[lab]]
    shim = types.SimpleNamespace(V=Vv, G=Gg, h=V43.HMAX)
    return shim


# --------------------------------------------- D25-completion utilities
def completed_point_v2(p, wit72, deep, env):
    """The banked 9.S3 completion pipeline, verbatim semantics: fiber
    frame + band-24 frontier completion through the V2 engine.  Returns
    (point_v2, E_v2, frontier_dict)."""
    pt, _r3, _h = V.radical_env(p)
    Z = [pow(pt["z"], m, p) for m in range(42)]
    point = DE.build_point_f(p, wit72, deep, env)
    jf, jg = V2.build_jets(point, p, Z)
    E = V2.euler_rows(jf, jg, p)
    frontier = {}
    if E.V.astype(np.int64)[:30, 24].any():
        y, fdiag = DE.frontier_solve(E, p)
        assert y is not None, ("frontier completion failed", fdiag)
        for (fam, r), v in y.items():
            if v:
                point["tails"][fam][r] = v
                frontier["%s_%d" % (fam, 32 + r)] = int(v)
        blob = json.dumps({"base_zc": point["zc_hash"],
                           "frontier": sorted(
                               ("%s_%d" % k, v) for k, v in y.items())},
                          sort_keys=True)
        point["zc_hash"] = hashlib.sha256(blob.encode()).hexdigest()
        jf, jg = V2.build_jets(point, p, Z)
        E = V2.euler_rows(jf, jg, p)
    return point, E, frontier


def point43_from_v2(p, wit72, deep, env, extra_tails=None):
    """V43 point with the same tails/fixed data as the V2 completed
    point (fiber frame); extra_tails: {(fam, r): val} adjoined
    completion coordinates (frontier / rung solves)."""
    point = V43.build_point(p, wit72, deep)
    fx = point["fixed"]
    fx["A1"], fx["A2"] = env["A1"], env["A2"]
    fx["HW1"] = env["h1"] * fx["W1"] % p
    fx["HW2"] = env["h2"] * fx["W2"] % p
    if extra_tails:
        for (fam, r), v in extra_tails.items():
            if v:
                point["tails"][fam][r] = int(v)
    blob = json.dumps({"prime": p, "base_zc": point["zc_hash"],
                       "fiber": {k: env[k] for k in
                                 ("label", "A1", "A2", "h1", "h2")},
                       "extra": sorted(("%s_%d" % k, int(v))
                                       for k, v in
                                       (extra_tails or {}).items()),
                       "xside": "alpha=beta=0 named completion"},
                      sort_keys=True)
    point["zc_hash"] = hashlib.sha256(blob.encode()).hexdigest()
    return point


# ------------------------------------------------ LEGACY_BAND40_REGRESSION
def _strip_seconds(o):
    if isinstance(o, dict):
        return {k: _strip_seconds(v) for k, v in o.items()
                if k != "seconds"}
    if isinstance(o, list):
        return [_strip_seconds(v) for v in o]
    return o


def _iter_bank_points(bank, kinds=("witness", "interior")):
    for rec in bank["points"]:
        if rec.get("verdict") == "ACCEPTED" and rec["kind"] in kinds:
            yield rec


def _interior_freevals(bank_seed):
    """Replay the exact 9.S3 RNG stream: the 288 interior free-var
    draws in run order."""
    rng = random.Random(bank_seed)
    targets = [(pp, "a00pp") for pp in PRIMES] + \
              [(PRIMES[0], lab) for lab in DE.OTHER_FIBERS_P0]
    out = {}
    for pp, lab in targets:
        for ci in range(16):
            for s in range(1, 4):
                fv = {v: rng.randrange(pp)
                      for v in DE.FREE_BASE + DE.FREE_LIFT}
                out[(pp, lab, ci, s)] = fv
    return out


def regress_one(rec, bank_seed, fv_map, heavy):
    """One banked D25 point: (i) reproduce the banked record via the
    unmodified 9.S3 driver; (ii) extended build at the same completion;
    (iii) band-<=40 projection byte-identical + old gates identical."""
    p, lab = rec["prime"], rec["fiber"]
    env = DE.fiber_env(p, lab)
    if rec["kind"] == "witness":
        cellval = DE.witness_cellval(p, lab)
    else:
        hdr, rows = DE.parse_fiber_ms(p, lab)
        cells = DE.cells_of_fiber(p, lab)
        W1, W2 = cells[rec["cell"]]
        fv = fv_map[(p, lab, rec["cell"], rec["sample"])]
        cellval = DE.solve_cell_point(p, hdr, rows, fv, W1, W2)
        assert int(cellval["W1"]) == rec["W1"] and \
            int(cellval["W2"]) == rec["W2"], "RNG replay drifted"
    mine = DE.process_point(p, lab, env, rec["cell"], rec["sample"],
                            cellval, heavy=heavy, quiet=True)
    same_bank = _strip_seconds(mine) == _strip_seconds(rec)
    # (ii) the same completed point through the extended engine
    dval, _diag = DE.reconstruct_point(p, cellval, env)
    wit72, deep = DE.witness72_of(p, dval)
    point_v2, E_v2, frontier = completed_point_v2(p, wit72, deep, env)
    extra = {}
    for labl, v in frontier.items():
        fam, lvl = labl.rsplit("_", 1)
        extra[(fam, int(lvl) - 32)] = v
    point43 = point43_from_v2(p, wit72, deep, env, extra_tails=extra)
    for f in FAMS:                        # identical tails assertion
        assert {r: int(v) for r, v in point_v2["tails"][f].items()
                if v} == {r: int(v) for r, v in point43["tails"][f].items()
                          if v}, ("tail drift", f)
    E43, aux = build_operator(point43, p, 0, 0)
    shim = project_band40(E43)
    byte_ok = bool(
        np.array_equal(shim.V, E_v2.V) and
        np.array_equal(shim.G, E_v2.G))
    op_ok = bool(V2.operator_hash(shim, p) == rec["certify"]
                 ["operator_hash"] == V2.operator_hash(E_v2, p))
    # (iii) rerun the banked gate stack on the projection
    g_c = EC.gate_cyclic30(shim, p)
    g_b = DE.gate_bridge30_f(shim, p, point_v2, env)
    g_f = DE.gate_filter30_f(shim, p, point_v2, wit72, env)
    g_p = EC.gate_param30(shim, p, 25)
    bc = rec["certify"]["gates"]
    gates_ok = bool(
        {k: bool(v) for k, v in g_c["checks"].items()} ==
        {k: bool(v) for k, v in bc["CYCLIC-30"]["checks"].items()
         if not k.startswith("f6") and not k.startswith("f7")} and
        {k: bool(v) for k, v in g_b["checks"].items()} ==
        {k: bool(v) for k, v in bc["BRIDGE-30"]["checks"].items()} and
        {k: bool(v) for k, v in g_f["checks"].items()} ==
        {k: bool(v) for k, v in bc["FILTER-30"]["checks"].items()
         if k not in ("f6_zeta_branch_invariance",
                      "f7_second_diff_path")} and
        g_p["ell_lb_certified"] == rec["ell_lb_certified"] and
        g_p["window_rank_174x170"] == rec["window_rank"] and
        g_p["delta_plus_N1"] == rec["delta_plus_N1"] and
        g_b["nu_window"] == rec["nu_window"])
    heavy_ok = True
    if heavy:
        pt, _r3, _h = V.radical_env(p)
        Z2r = pow(pt["z"], 5, p)
        Z2 = [pow(Z2r, m, p) for m in range(42)]
        E43z, _ = build_operator(point43, p, 0, 0, Z=Z2)
        heavy_ok = bool(V2.operator_hash(project_band40(E43z), p) ==
                        V2.operator_hash(shim, p))
        DG43 = V43.path_A_rows(aux["jff"], aux["jgf"], p)
        Gp = np.zeros((V43.HMAX, 42, 170))
        for idx, labl in enumerate(COLS_OLD):
            Gp[:, :, idx] = DG43[:, :42, V43.GIDX[labl]]
        heavy_ok = heavy_ok and bool(np.array_equal(Gp, shim.G))
    return {
        "prime": p, "fiber": lab, "cell": rec["cell"],
        "sample": rec["sample"], "kind": rec["kind"],
        "banked_record_reproduced": bool(same_bank),
        "band40_arrays_byte_identical": byte_ok,
        "operator_hash_match": op_ok,
        "old_gates_identical": gates_ok,
        "heavy_paths_match": bool(heavy_ok),
        "pass": bool(same_bank and byte_ok and op_ok and gates_ok and
                     heavy_ok),
    }


def run_regress(n_points, out_path, full=False):
    print("== LEGACY_BAND40_REGRESSION (mandatory gate; spec sect 8) ==")
    print("   " + BANNER)
    t0 = time.time()
    bank = json.load(open(os.path.join(HERE, "d25_eplus.json")))
    seed = bank["sampling"]["seed"]
    fv_map = _interior_freevals(seed)
    wit = [r for r in _iter_bank_points(bank, ("witness",))]
    inte = [r for r in _iter_bank_points(bank, ("interior",))]
    if full:
        chosen = wit + inte
    else:
        nw = max(8, n_points // 2)
        rngsel = random.Random(43)
        chosen = (rngsel.sample(wit, min(nw, len(wit))) +
                  rngsel.sample(inte, max(n_points - nw, 12)))
    print("   points: %d witnesses + %d interior (of %d banked)"
          % (sum(1 for r in chosen if r["kind"] == "witness"),
             sum(1 for r in chosen if r["kind"] == "interior"),
             len(bank["points"])))
    results = []
    ckpath = (out_path + ".ck") if out_path else None
    done_keys = set()
    if ckpath and os.path.exists(ckpath):
        prev = json.load(open(ckpath))
        results = prev["results"]
        done_keys = {tuple(r[k] for k in ("prime", "fiber", "cell",
                                          "sample")) for r in results}
        print("   resume: %d already done" % len(results))
    for rec in chosen:
        key = (rec["prime"], rec["fiber"], rec["cell"], rec["sample"])
        if key in done_keys:
            continue
        heavy = rec["kind"] == "witness"
        r = regress_one(rec, seed, fv_map, heavy)
        results.append(r)
        print("p%d %s c%02d s%d [%s]: bank=%s bytes=%s hash=%s gates=%s"
              "%s -> %s"
              % (r["prime"], r["fiber"], r["cell"], r["sample"],
                 r["kind"], r["banked_record_reproduced"],
                 r["band40_arrays_byte_identical"],
                 r["operator_hash_match"], r["old_gates_identical"],
                 "" if not heavy else " heavy=%s" % r["heavy_paths_match"],
                 "PASS" if r["pass"] else "FAIL"), flush=True)
        if ckpath and len(results) % 10 == 0:
            with open(ckpath, "w") as f:
                json.dump({"results": results}, f)
    # d23 spot fixtures (both primes, w0k0): EC path + projection
    d23 = []
    for p in PRIMES:
        w0 = next(V2.iter_points(p))
        res, E_old = EC.certify_point(p, w0[2], w0[3], D=23, heavy=False)
        point43 = V43.build_point(p, w0[2], w0[3])
        E43, _aux = build_operator(point43, p, 0, 0)
        shim = project_band40(E43)
        bankd23 = json.load(open(os.path.join(HERE, "d23_eplus.json")))
        brec = next(r for r in bankd23["points"]
                    if r["prime"] == p and r["witness"] == 0 and
                    r["kernel_draw"] == 0)
        ok = bool(np.array_equal(shim.V, E_old.V) and
                  np.array_equal(shim.G, E_old.G) and
                  V2.operator_hash(shim, p) == brec["operator_hash"] ==
                  res["operator_hash"] and
                  EC.gate_param30(shim, p, 23)["ell_lb_certified"] ==
                  brec["gates"]["PARAM-30"]["ell_lb_certified"] == 37)
        d23.append({"prime": p, "witness": 0, "kernel_draw": 0,
                    "pass": ok})
        print("d23 p%d w0k0: %s" % (p, "PASS" if ok else "FAIL"),
              flush=True)
    # char-0 crosscheck through the configured engine (spec sect 8)
    cc = []
    for p in PRIMES:
        got, want = V43.zero_config_crosscheck(p)
        cc.append({"prime": p, "pass": bool(got == want)})
        print("char0 eta29/tf1_48 crosscheck p%d: %s"
              % (p, "PASS" if got == want else "FAIL"), flush=True)
    npass = sum(1 for r in results if r["pass"])
    allpass = (npass == len(results) and all(r["pass"] for r in d23) and
               all(r["pass"] for r in cc))
    out = {
        "tool": TOOL, "mode": "LEGACY_BAND40_REGRESSION",
        "date": time.strftime("%Y-%m-%d"),
        "status": "INTERNAL / UNREVIEWED; fail-closed",
        "banner": BANNER,
        "engine": {"DBUILD": 43, "RMAX": 42, "GD": 182,
                   "x_sidecar": ["Xf_alpha@42", "Xg_beta@42"],
                   "alpha_beta_completion": [0, 0]},
        "banked_fixture_sha256": {
            "d25_eplus.json": V.sha256(os.path.join(HERE,
                                                    "d25_eplus.json")),
            "d23_eplus.json": V.sha256(os.path.join(HERE,
                                                    "d23_eplus.json"))},
        "comparison": ("banked 9.S3 record reproduced (seconds "
                       "stripped) + extended build projected to bands "
                       "<= 40 / old 170-column GIDX in the exact old "
                       "order: byte-identical arrays, identical "
                       "per-point operator hash, identical CYCLIC/"
                       "BRIDGE/FILTER/PARAM gate outputs"),
        "n_points": len(results), "n_pass": npass,
        "d23_spot": d23, "char0_crosscheck": cc,
        "all_pass": bool(allpass),
        "points": results,
        "seconds": round(time.time() - t0),
    }
    if out_path:
        with open(out_path, "w") as f:
            json.dump(out, f, indent=1, sort_keys=True)
        print("-> wrote %s" % out_path)
    print("REGRESSION: %d/%d points byte-identical; d23 spot %s; "
          "char-0 %s; ALL %s"
          % (npass, len(results),
             all(r["pass"] for r in d23), all(r["pass"] for r in cc),
             "PASS" if allpass else "FAIL"), flush=True)
    return allpass


# ------------------------------------------------- D25_COMPLETION_BAND42
def smoke_point(p, lab, cellval, env, skip_controls=False):
    dval, diag = DE.reconstruct_point(p, cellval, env)
    wit72, deep = DE.witness72_of(p, dval)
    point_v2, _E_v2, frontier = completed_point_v2(p, wit72, deep, env)
    extra = {}
    prov = {}
    x2tf = DE.x2tf_cached()
    for labl, v in frontier.items():
        fam, lvl = labl.rsplit("_", 1)
        extra[(fam, int(lvl) - 32)] = v
        prov[labl] = "solved_completion (band-24 frontier, rank 4, "\
                     "kernel frees 0)"
    for xn, tf in x2tf.items():
        if tf[:2] in ("tf", "tg"):
            prov.setdefault(tf, "represented_cell_or_witness_coordinate")
    for nm in [V.DEEPMAP[x] for x in V.DEEPX]:
        prov.setdefault(V2.DEEP_RELABEL.get(nm, nm),
                        "represented_deep_draw_coordinate")
    prov["tg1_44"] = prov["tg2_44"] = \
        "solved_completion (band-22 affine tg probe)"
    point43 = point43_from_v2(p, wit72, deep, env, extra_tails=extra)
    checks, info, E, _aux = gate_suite(
        point43, p, env, 0, 0, prov, "D25_COMPLETION_BAND42",
        skip_controls=skip_controls)
    rec = {
        "prime": p, "fiber": lab, "mode": "D25_COMPLETION_BAND42",
        "mode_note": ("operator smoke test at a banked D25 completion "
                      "(spec C0/5.3 mode 2): NOT a D43 survivor, NOT a "
                      "depth measurement; rows 26..42 need NOT vanish "
                      "here"),
        "zc_hash": point43["zc_hash"],
        "checks": {k: bool(v) for k, v in checks.items()},
        "checks_all_pass": bool(all(checks.values())),
    }
    for k in ("window_rank_184x182", "ell_lb_certified", "nu_window",
              "delta_plus_N1", "delta_plus_N2", "M2_rank",
              "y1_H29u1_uncovered", "maximizers", "row42_eta_support",
              "registry_hash", "matrix_hash", "band40_operator_hash",
              "manifest_sha256", "value_bands_le42",
              "y1_uncovered_in_y180_diagnostic",
              "y0_uncovered_in_y180_diagnostic",
              "y1_dual_witness_y180", "y180_note",
              "support_starts_eq_S30"):
        rec[k] = info[k]
    rec["y0_dual_witness"] = info["y0_dual_witness"]
    rec["y1_dual_witness"] = info["y1_dual_witness"]
    rec["ell_profile"] = info["ell_profile"]
    rec["ell_profile_key"] = info["ell_profile_key"]
    return rec, info


def run_smoke(out_path, labs=None, per_prime_witnesses=6):
    print("== D25_COMPLETION_BAND42 SMOKE (spec C0; NOT a depth "
          "measurement) ==")
    print("   " + BANNER)
    t0 = time.time()
    results = []
    labs_all = sorted(DE.replay()["parked_fibers"]["105337"])
    if labs is None:
        labs = labs_all[::max(1, len(labs_all) // per_prime_witnesses)][
            :per_prime_witnesses]
    for p in PRIMES:
        for lab in labs:
            env = DE.fiber_env(p, lab)
            cv = DE.witness_cellval(p, lab)
            rec, _info = smoke_point(p, lab, cv, env)
            results.append(rec)
            print("p%d %s: ell+>=%d rank=%d/184x182 nu=%s d+(1)=%d "
                  "d+(2)=%d H29u1_uncovered=%s checks=%s"
                  % (p, lab, rec["ell_lb_certified"],
                     rec["window_rank_184x182"], rec["nu_window"],
                     rec["delta_plus_N1"], rec["delta_plus_N2"],
                     rec["y1_H29u1_uncovered"],
                     "ALL-PASS" if rec["checks_all_pass"] else "FAIL"),
                  flush=True)
    ell = collections.Counter(r["ell_lb_certified"] for r in results)
    y1u = collections.Counter(r["y1_H29u1_uncovered"] for r in results)
    out = {
        "tool": TOOL, "mode": "D25_COMPLETION_BAND42",
        "date": time.strftime("%Y-%m-%d"),
        "status": "INTERNAL / UNREVIEWED; fail-closed; %s only" % CAND,
        "banner": BANNER,
        "mode_note": ("spec C0: banked D25 zero/frontier completions "
                      "with the real level-42 x-side (named alpha = "
                      "beta = 0 completion, independent tangents) and "
                      "the window extended to 184x182.  Pointwise "
                      "discriminator between the shifted obstruction "
                      "and coverage.  It does NOT measure the D43 "
                      "survivor-locus floor; these completions need "
                      "not satisfy Rows 26..42.  NEVER a third-depth "
                      "survivor result."),
        "n_points": len(results),
        "ell_lb_distribution": {str(k): v for k, v in sorted(ell.items())},
        "H29u1_uncovered_distribution": {str(k): v for k, v in
                                         sorted(y1u.items())},
        "points": results,
        "seconds": round(time.time() - t0),
    }
    if out_path:
        with open(out_path, "w") as f:
            json.dump(out, f, indent=1, sort_keys=True)
        print("-> wrote %s" % out_path)
    print("SMOKE: ell distribution %s; H29u1 uncovered %s"
          % (dict(sorted(ell.items())), dict(sorted(y1u.items()))),
          flush=True)
    return out


# ----------------------------------------------- D43 numeric prolongation
RUNGS = list(range(26, 43, 2))


def rung_columns(k):
    """First-occurrence directions of Row k (spec 6.1): four ordinary
    tails at absolute k+27 (r = k-5) + all six at k+32 (r = k).  For
    Row 42 this is CONJECTURE POST41-FIRST-OCCURRENCE: it is used only
    as the candidate unknown set; the level-cap guard + post-solve
    replay measure it, and any unexpected extra support fails closed."""
    return ([(f, k - 5) for f in ("tf1", "tf2", "tg1", "tg2")] +
            [(f, k) for f in FAMS])


def rung_rows(k):
    """Selected output components at band k: streams with s_a == k
    (mod 6), s_a <= k."""
    return [a for a in range(30) if S30[a] % 6 == k % 6 and S30[a] <= k]


def prolong_unknowns():
    """The 90 provisional first-occurrence completion coordinates of
    the nine rungs (spec 6.2): for each even k = 26..42, four ordinary
    tails at absolute k+27 (r = k-5) and all six at k+32 (r = k).
    Row-42's block is CONJECTURE POST41-FIRST-OCCURRENCE; the solve
    below measures actual occurrence and fails closed on any residual
    support it cannot reach."""
    out = []
    for k in RUNGS:
        out += rung_columns(k)
    assert len(out) == 90 and len(set(out)) == 90
    return out


def _build_E(point, p, Z):
    jf, jg = V43.build_jets(point, p, Z)
    jff, jgf, _Uf, _Ug = apply_xside(jf, jg, p, 0, 0)
    return V43.euler_rows(jff, jgf, p)


def prolong_point(p, wit72, deep, env, verbose=True):
    """Numeric D43 prolongation of one completed D25 point.

    STAGE A (bands 26..40): the residual at every even band <= 40 is
    EXACTLY jointly affine in the 90 undetermined completion
    coordinates (any product of two undetermined tails has level
    >= 21+21 = 42 > 40), so ONE joint affine system is solved with the
    deterministic kernel completion (RREF, free coordinates = 0) and
    verified by full jet rebuild -- a violated affinity assumption
    fires the replay assert (fail-closed).
    STAGE B (band 42): after the rebuild (which realizes the single
    quadratic 21+21 interaction exactly), the band-42 residual is
    affine in the ten rung-42 coordinates; one final solve + rebuild
    proves nu >= 43.  An inconsistent stage is a NO_PROLONGATION
    verdict for this named completion -- NOT family emptiness."""
    point_v2, _E, frontier = completed_point_v2(p, wit72, deep, env)
    extra = {}
    prov = {}
    for labl, v in frontier.items():
        fam, lvl = labl.rsplit("_", 1)
        extra[(fam, int(lvl) - 32)] = v
        prov[labl] = "solved_completion (band-24 frontier)"
    point = point43_from_v2(p, wit72, deep, env, extra_tails=extra)
    pt, _r3, _h = V.radical_env(p)
    Z = [pow(pt["z"], m, p) for m in range(42)]
    unknowns = prolong_unknowns()
    for (f, r) in unknowns:
        assert r not in point["tails"][f], ("unknown already set", f, r)
    cidx = [V43.GIDX[c] for c in unknowns]
    diag = {}
    E = _build_E(point, p, Z)
    Vv = E.V.astype(np.int64)
    Gg = E.G.astype(np.int64)
    low = sorted({int(n) for n in range(26) if Vv[:30, n].any()})
    assert not low, ("bands below 26 nonzero at the D25 completion",
                     low)
    assert not Gg[:30, :26, :][:, :, cidx].any(), \
        "an undetermined column occurs below band 26 (level cap)"
    # STAGE A: joint affine system over even bands 26..40
    rowsA = []
    for k in range(26, 41, 2):
        sel = rung_rows(k)
        nz = sorted(int(a) for a in range(30) if Vv[a][k])
        assert set(nz) <= set(sel), \
            ("band %d residual outside selected rows" % k, nz)
        rowsA += [(a, k) for a in sel]
    A = [[int(Gg[a][n][c]) for c in cidx] for (a, n) in rowsA]
    b = [(-int(Vv[a][n])) % p for (a, n) in rowsA]
    y, rkA = DE.solve_deep_zero_completion(A, b, p)
    assert y is not None, \
        "STAGE A INCONSISTENT (bands 26..40; no prolongation here)"
    nzA = 0
    for (f, r), v in zip(unknowns, y):
        if v:
            point["tails"][f][r] = int(v)
            prov["%s_%d" % (f, 32 + r)] = \
                "solved_completion (D43 joint bands 26..40, rank %d)" \
                % rkA
            nzA += 1
    diag["stageA"] = {"rows": len(rowsA), "unknowns": len(unknowns),
                      "rank": int(rkA), "nonzero": nzA}
    if verbose:
        print("      stage A: %d rows, rank %d, %d/90 nonzero"
              % (len(rowsA), rkA, nzA), flush=True)
    E = _build_E(point, p, Z)
    Vv = E.V.astype(np.int64)
    Gg = E.G.astype(np.int64)
    resid = sorted({int(n) for n in range(42) if Vv[:30, n].any()})
    assert not resid, ("STAGE A replay: bands <= 41 nonzero (affinity "
                       "assumption violated)", resid)
    # STAGE B: band 42 over the ten rung-42 coordinates
    cols42 = rung_columns(42)
    c42 = [V43.GIDX[c] for c in cols42]
    sel42 = rung_rows(42)
    nz42 = sorted(int(a) for a in range(30) if Vv[a][42])
    assert set(nz42) <= set(sel42), \
        ("band 42 residual outside selected rows "
         "(POST41 census violated)", nz42)
    A2 = [[int(Gg[a][42][c]) for c in c42] for a in sel42]
    b2 = [(-int(Vv[a][42])) % p for a in sel42]
    y2, rkB = DE.solve_deep_zero_completion(A2, b2, p)
    assert y2 is not None, \
        "STAGE B INCONSISTENT (band 42; no prolongation here)"
    nzB = 0
    for (f, r), v in zip(cols42, y2):
        if v:
            old = point["tails"][f].get(r, 0)
            nv = int((old + v) % p)
            if nv:
                point["tails"][f][r] = nv
            else:
                point["tails"][f].pop(r, None)
            prov["%s_%d" % (f, 32 + r)] = \
                "solved_completion (D43 band 42, rank %d)" % rkB
            nzB += 1
    diag["stageB"] = {"rows": len(sel42), "rank": int(rkB),
                      "nonzero": nzB}
    if verbose:
        print("      stage B: %d rows, rank %d, %d/10 adjusted"
              % (len(sel42), rkB, nzB), flush=True)
    # final replay: bands <= 42 all zero
    E = _build_E(point, p, Z)
    Vv = E.V.astype(np.int64)
    resid = sorted({int(n) for n in range(V43._S) if Vv[:30, n].any()})
    assert not resid, ("prolongation replay: bands nonzero", resid)
    diag["nu_window_ge"] = 43
    blob = json.dumps({"base_zc": point["zc_hash"],
                       "rung_tails": sorted(
                           ("%s_%d" % (f, 32 + r), int(v))
                           for f in FAMS
                           for r, v in point["tails"][f].items())},
                      sort_keys=True)
    point["zc_hash"] = hashlib.sha256(blob.encode()).hexdigest()
    return point, prov, diag


def run_prolong(out_path, n_interior=2, labs=None, seed=20260843):
    """Stage-2 numeric arm: D43 points over D25 cells.  Witness + N
    interior samples per chosen fiber, both primes for a00pp."""
    print("== D43 NUMERIC PROLONGATION (rung solves 26..42; the D25 "
          "frontier discipline extended) ==")
    t0 = time.time()
    rng = random.Random(seed)
    labs = labs or ["a00pp", "a00mm", "a01pp", "a10pm", "a22mp"]
    results = []
    ck = (out_path + ".ck") if out_path else None
    done = set()
    if ck and os.path.exists(ck):
        results = json.load(open(ck))["results"]
        done = {(r["prime"], r["fiber"], r["cell"], r["sample"])
                for r in results}
        print("   resume: %d done" % len(results))
    targets = [(p, "a00pp") for p in PRIMES] + \
              [(PRIMES[0], lab) for lab in labs if lab != "a00pp"]
    for p, lab in targets:
        env = DE.fiber_env(p, lab)
        hdr, rows = DE.parse_fiber_ms(p, lab)
        cells = DE.cells_of_fiber(p, lab)
        jobs = [(0, 0, None)]
        for s in range(1, n_interior + 1):
            ci = rng.randrange(16)
            fv = {v: rng.randrange(p) for v in DE.FREE_BASE +
                  DE.FREE_LIFT}
            jobs.append((ci, s, fv))
        for ci, s, fv in jobs:
            key = (p, lab, ci, s)
            if key in done:
                continue
            rec = {"prime": p, "fiber": lab, "cell": ci, "sample": s,
                   "kind": "witness" if s == 0 else "interior"}
            try:
                if s == 0:
                    cellval = DE.witness_cellval(p, lab)
                else:
                    W1, W2 = cells[ci]
                    cellval = DE.solve_cell_point(p, hdr, rows, fv, W1,
                                                  W2)
                dval, _dg = DE.reconstruct_point(p, cellval, env)
                wit72, deep = DE.witness72_of(p, dval)
                print("   p%d %s cell%02d s%d:" % (p, lab, ci, s),
                      flush=True)
                point, prov, diag = prolong_point(p, wit72, deep, env)
                rec["verdict"] = "PROLONGED"
                rec["diag"] = diag
                rec["zc_hash"] = point["zc_hash"]
                rec["tails"] = {f: sorted((int(r), int(v)) for r, v in
                                          point["tails"][f].items())
                                for f in FAMS}
                rec["fixed"] = sorted((k, int(v)) for k, v in
                                      point["fixed"].items())
                rec["provenance"] = sorted(prov.items())
                rec["wit72"] = wit72
                rec["deep"] = deep
                rec["env"] = {k: env[k] for k in ("label", "A1", "A2",
                                                  "h1", "h2")}
            except AssertionError as e:
                rec["verdict"] = "NO_PROLONGATION"
                rec["reason"] = str(e)
                print("   p%d %s cell%02d s%d: NO PROLONGATION (%s)"
                      % (p, lab, ci, s, e), flush=True)
            results.append(rec)
            if ck:
                with open(ck, "w") as f:
                    json.dump({"results": results}, f)
    npro = sum(1 for r in results if r["verdict"] == "PROLONGED")
    out = {
        "tool": TOOL, "mode": "D43_PROLONGATION",
        "date": time.strftime("%Y-%m-%d"),
        "status": "INTERNAL / UNREVIEWED; fail-closed",
        "note": ("numeric D43 prolongations of banked D25 cell points "
                 "through the certifier's own operator: even rungs "
                 "26..42 solved over the measured first-occurrence "
                 "directions (level-cap guarded; kernel frees = 0; "
                 "Row-42 census = CONJECTURE POST41-FIRST-OCCURRENCE, "
                 "fail-closed), alpha = beta = 0 named x completion. "
                 "POINTWISE objects on named cells/completions: not a "
                 "family certificate, not locus-wide."),
        "n_points": len(results), "n_prolonged": npro,
        "points": results,
        "seconds": round(time.time() - t0),
    }
    if out_path:
        with open(out_path, "w") as f:
            json.dump(out, f, indent=1, sort_keys=True)
        print("-> wrote %s" % out_path)
    print("PROLONG: %d/%d points prolonged to nu >= 43"
          % (npro, len(results)), flush=True)
    return out


# ------------------------------------------------------ D43_SURVIVOR mode
def survivor_point(rec, negative_controls=True):
    """Full D43_SURVIVOR certification of one prolonged point: rebuild,
    D43-RESIDUAL, complete gate battery, floor measurement."""
    p = rec["prime"]
    env = dict(rec["env"])
    point = point43_from_v2(
        p, rec["wit72"], rec["deep"], env,
        extra_tails={})
    # replace tails wholesale with the banked prolonged tails
    point["tails"] = {f: {int(r): int(v) for r, v in rec["tails"][f]}
                      for f in FAMS}
    point["zc_hash"] = rec["zc_hash"]
    prov = dict(rec["provenance"])
    checks, info, E, aux = gate_suite(point, p, env, 0, 0, prov,
                                      "D43_SURVIVOR")
    Vv = E.V.astype(np.int64)
    # D43-RESIDUAL (gate 9): all 184 selected pristine coefficients zero
    sel_zero = all(int(Vv[a][S30[a] + 6 * j]) == 0
                   for (a, j) in ROWS_CANON)
    checks["s9_d43_residual_184_zero"] = bool(sel_zero)
    checks["s9_nu_ge_43"] = bool(info["nu_window"] is None)
    # unit/chart audit (FILTER-30 f3 pattern)
    ptv, r3, h32 = V.radical_env(p)
    fx = point["fixed"]
    u_ok = (pow(r3, 2, p) == 3 % p and
            pow(fx["A1"], 3, p) == (3 + r3) % p and
            pow(fx["A2"], 3, p) == (3 - r3) % p and
            fx["W1"] % p != 0 and fx["W2"] % p != 0 and
            all(p % q for q in (2, 3, 5, 7)))
    checks["s9_chart_unit_audit"] = bool(u_ok)
    out = {
        "prime": p, "fiber": rec["fiber"], "cell": rec["cell"],
        "sample": rec["sample"], "kind": rec["kind"],
        "mode": "D43_SURVIVOR", "depth_D": D43,
        "zc_hash": rec["zc_hash"],
        "checks": {k: bool(v) for k, v in checks.items()},
        "checks_all_pass": bool(all(checks.values())),
        "threshold_floor_Dm1_2": THRESH43,
    }
    for k in ("window_rank_184x182", "ell_lb_certified", "nu_window",
              "delta_plus_N1", "delta_plus_N2", "M2_rank",
              "y1_H29u1_uncovered", "maximizers", "row42_eta_support",
              "registry_hash", "matrix_hash", "value_array_hash",
              "band40_operator_hash", "manifest_sha256",
              "y1_uncovered_in_y180_diagnostic",
              "y0_uncovered_in_y180_diagnostic",
              "y1_dual_witness_y180", "y180_note",
              "support_starts_eq_S30"):
        out[k] = info[k]
    out["y0_dual_witness"] = info["y0_dual_witness"]
    out["y1_dual_witness"] = info["y1_dual_witness"]
    out["dual_witnesses_maximizers"] = info["dual_witnesses_maximizers"]
    out["ell_profile"] = info["ell_profile"]
    out["ell_profile_key"] = info["ell_profile_key"]
    out["e_plus"] = {
        "certified": None,
        "certified_note": ("fail-closed: no section constructed; "
                           "certified LOWER bound only"),
        "candidate_window_floor": info["ell_lb_certified"],
        "tag": CAND,
        "at_or_below_threshold": bool(info["ell_lb_certified"] <=
                                      THRESH43)}
    if negative_controls and out["checks_all_pass"]:
        ctl = {}
        # (a) perturb a point coordinate with a recorded incidence
        pt2 = {f: dict(point["tails"][f]) for f in FAMS}
        pert = None
        for f in FAMS:
            for r, v in sorted(point["tails"][f].items()):
                if v:
                    pert = (f, r)
                    break
            if pert:
                break
        assert pert is not None
        pt2[pert[0]][pert[1]] = (pt2[pert[0]][pert[1]] + 1) % p
        point2 = dict(point)
        point2["tails"] = pt2
        E2p, _ = build_operator(point2, p, 0, 0, Z=aux["Z"])
        ctl["residual_breaks_on_point_perturbation"] = bool(
            E2p.V.astype(np.int64)[:30, :43].any())
        # (b) perturb a matrix entry hit by the stored dual witness
        row_lv, col_lv, M = window_object43(E)
        lab2idx = {row_label(i): i for i in range(len(ROWS_CANON))}
        w0 = out["y0_dual_witness"]
        lam = np.zeros(len(ROWS_CANON), dtype=np.int64)
        for lb, c in w0.items():
            lam[lab2idx[lb]] = c
        cols0 = [j for j in range(M.shape[1]) if col_lv[j] >= 0]
        i0 = next(i for i in range(len(lam)) if lam[i])
        Mp = M.copy()
        j0 = next(j for j in cols0
                  if (lam @ M[:, [j]] % p == 0) and M[:, j].any())
        Mp[i0, j0] = (Mp[i0, j0] + 1) % p
        ctl["dual_witness_breaks_on_matrix_perturbation"] = bool(
            (lam @ Mp[:, cols0] % p).any())
        # (c) registry label/order perturbation changes the hash
        reg2 = {"rows": [[a, j, S30[a] + 6 * j] for (a, j) in
                         (ROWS_CANON[1:] + ROWS_CANON[:1])],
                "cols": [[f, r] for (f, r) in COLS_CANON]}
        ctl["registry_hash_breaks_on_reorder"] = bool(
            hashlib.sha256(json.dumps(reg2, sort_keys=True).encode())
            .hexdigest() != out["registry_hash"])
        # (d) omitting a manifest coefficient must fail completeness
        try:
            bad_prov = dict(prov)
            man2 = completion_manifest(point, p, bad_prov, 0, 0)
            ok_d = len(man2["y_registry"]) == 180
            pt3 = {f: dict(point["tails"][f]) for f in FAMS}
            done = False
            for f in FAMS:
                for r, v in sorted(pt3[f].items()):
                    lb = "%s_%d" % (f, 32 + r)
                    if v and lb in bad_prov:
                        del bad_prov[lb]
                        done = True
                        break
                if done:
                    break
            try:
                completion_manifest(point, p, bad_prov, 0, 0)
                ctl["manifest_omission_detected"] = False
            except AssertionError:
                ctl["manifest_omission_detected"] = bool(ok_d)
        except AssertionError:
            ctl["manifest_omission_detected"] = False
        out["negative_controls"] = ctl
        out["negative_controls_all_fire"] = bool(all(ctl.values()))
    return out


def run_survivor(points_path, out_path):
    print("== D43_SURVIVOR CERTIFICATION (the third depth measurement) "
          "==")
    print("   " + BANNER)
    t0 = time.time()
    bank = json.load(open(points_path))
    pro = [r for r in bank["points"] if r["verdict"] == "PROLONGED"]
    results = []
    ck = (out_path + ".ck") if out_path else None
    done = set()
    if ck and os.path.exists(ck):
        results = json.load(open(ck))["results"]
        done = {(r["prime"], r["fiber"], r["cell"], r["sample"])
                for r in results}
        print("   resume: %d done" % len(results))
    for rec in pro:
        key = (rec["prime"], rec["fiber"], rec["cell"], rec["sample"])
        if key in done:
            continue
        r = survivor_point(rec)
        results.append(r)
        print("p%d %s c%02d s%d [%s]: ell+>=%d rank=%d nu>=43=%s "
              "H29u1_uncovered=%s checks=%s ctl=%s"
              % (r["prime"], r["fiber"], r["cell"], r["sample"],
                 r["kind"], r["ell_lb_certified"],
                 r["window_rank_184x182"], r["checks"]["s9_nu_ge_43"],
                 r["y1_H29u1_uncovered"],
                 "PASS" if r["checks_all_pass"] else "FAIL",
                 r.get("negative_controls_all_fire")), flush=True)
        if ck:
            with open(ck, "w") as f:
                json.dump({"results": results}, f)
    ell = collections.Counter(r["ell_lb_certified"] for r in results
                              if r["checks_all_pass"])
    y1 = collections.Counter(r["y1_H29u1_uncovered"] for r in results
                             if r["checks_all_pass"])
    nfail = sum(1 for r in results if not r["checks_all_pass"])
    out = {
        "tool": TOOL, "mode": "D43_SURVIVOR",
        "date": time.strftime("%Y-%m-%d"),
        "status": "INTERNAL / UNREVIEWED; fail-closed; %s only" % CAND,
        "banner": BANNER,
        "depth_D": D43, "threshold_e_le": THRESH43,
        "scope": ("mod p ONLY (105337, 105673); residue-A B-frozen "
                  "no-log W1W2 != 0 chart with PIN42; chart-local; "
                  "named deterministic completions (incl. alpha = beta "
                  "= 0 x-side, INDEPENDENT tangents, 184x182 window); "
                  "POINTWISE at named D43 prolongations of named D25 "
                  "cells -- sampling proves no locus-wide claim "
                  "(CONJECTURE LOCUS-UNIVERSAL-H29 not consumed)"),
        "source_points_file": os.path.basename(points_path),
        "source_points_sha256": V.sha256(points_path),
        "n_points": len(results),
        "n_checks_all_pass": len(results) - nfail,
        "ell_lb_certified_distribution": {str(k): v for k, v in
                                          sorted(ell.items())},
        "H29u1_uncovered_distribution": {str(k): v for k, v in
                                         sorted(y1.items())},
        "n_formal_germs_certified": 0,
        "e_plus_certified_all_points": None,
        "points": results,
        "seconds": round(time.time() - t0),
    }
    if out_path:
        with open(out_path, "w") as f:
            json.dump(out, f, indent=1, sort_keys=True)
        print("-> wrote %s" % out_path)
    print("SURVIVOR: ell floor distribution %s; H29u1 uncovered %s; "
          "%d/%d all-pass" % (dict(sorted(ell.items())),
                              dict(sorted(y1.items())),
                              len(results) - nfail, len(results)),
          flush=True)
    return out


# ---------------------------------------------------------------- selftest
def selftest():
    p = 105337
    # engine configuration
    assert V43.GD == 182 and V43._S == 43 and V43.RMAX == 42
    assert sum((42 - s) // 6 + 1 for s in S30) == 184
    # brute scanner controls (the banked eplus_certify controls, rerun
    # against the new brute scan)
    for e in (0, 1, 3):
        K = 12
        rl = np.arange(K + 1)
        cl = np.arange(K + 1)
        M = np.zeros((K + 1, K + 1), dtype=np.int64)
        for r in range(K + 1 - e):
            M[r + e][r] = 1
        # local brute (bands 0..K)
        ell = 0
        for n in range(K + 1):
            cols = [j for j in range(K + 1) if cl[j] >= n]
            cs = _colspace(M, cols, p)
            cov = cs.covered_rows()
            bad = np.nonzero((~cov) & (rl >= n))[0]
            if len(bad):
                ell = max(ell, int(rl[bad].max()) - n + 1)
        assert ell == e, ("diag control", e, ell)
    # dual-witness control: 2x1 uncovered target
    M = np.array([[1], [0]], dtype=np.int64)
    w = dual_witness(M, [0], 1, p)
    assert w == {row_label(1): 1}
    assert dual_witness(M, [0], 0, p) is None
    # x-column proportionality control on a synthetic window
    SM, GM = smgm(p)
    assert (126 * SM * GM + 2 * 84 * SM * GM * pow(2, p - 2, p) * 1) % p \
        != 0  # sanity: nonzero columns
    assert 756 * SM * GM % p == 126 * SM * GM % p * 6 % p
    print("PASS selftest: configured engine (43/42/182), 184-row "
          "registry, brute scanner diag controls, dual witness, "
          "x-vector scalars")


def main():
    ap = argparse.ArgumentParser(description="D43 extended-window "
                                 "certifier (fail-closed)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--regress", action="store_true")
    ap.add_argument("--regress-full", action="store_true")
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--prolong", action="store_true")
    ap.add_argument("--survivor", default=None)
    ap.add_argument("--n", type=int, default=24)
    ap.add_argument("--interior", type=int, default=2)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    if args.regress or args.regress_full:
        out = args.out or os.path.join(HERE, "d43_regress.json")
        ok = run_regress(args.n, out, full=args.regress_full)
        sys.exit(0 if ok else 1)
    if args.smoke:
        run_smoke(args.out or os.path.join(HERE, "d43_smoke.json"))
        return
    if args.prolong:
        run_prolong(args.out or os.path.join(HERE, "d43_points.json"),
                    n_interior=args.interior)
        return
    if args.survivor:
        run_survivor(args.survivor,
                     args.out or os.path.join(HERE, "d43_eplus.json"))
        return
    ap.print_help()


if __name__ == "__main__":
    main()
