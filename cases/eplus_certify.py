#!/usr/bin/env python3
"""eplus_certify.py -- the e+ CERTIFIER: application-gate implementation of
the PROMOTED filtered differential Newton lemma (xmodel/sol-newton-lemma.md,
Theorem 3.1 + Cor 3.2 + Theorem 6.1; hostile review CONFIRMED in
xmodel/grok-newton-review.md; AUDIT.md 2026-08-19 tail entry).

STATUS: INTERNAL TOOLING, UNREVIEWED.  FAIL-CLOSED THROUGHOUT.

WHAT IS PROMOTED (and therefore consumed here as a theorem): over any
field incl. char p, a residual of global t-order D lifts to a formal
solution whenever D >= 2e+1, where e is the loss of an EXACT CAUSAL RIGHT
SECTION of the corrected 30x30 Euler/Ore linearization L_s^+
(sol-newton-lemma.md (2.1)-(2.3), Theorem 3.1, Corollary 3.2).

WHAT IS NOT PROMOTED (the four application gates of the review, each
implemented below as an EXECUTABLE CHECK; where full discharge needs an
unproved lemma the result is labeled E_PLUS_CANDIDATE pending that lemma;
nothing here fabricates a section or an all-depth statement):

  CYCLIC-30  the full all-depth equation (incl. t^42+ x-side) has exactly
             the 30 output streams (9.1).  Executable part: the band-41
             regression of the corrected 30-output grading (eta^30..33
             identically zero, odd bands zero, congruences n == s_a mod 6
             with n >= s_a for a = 0..29 incl. H_29 at s_29 = 36, exact
             support starts, 30-ladder input partition).  PENDING: the
             all-depth identity -- a band-41 regression does NOT prove it
             (the H_29 discovery is the standing warning).
  BRIDGE-30  universal levelwise pristine/emitted identities (5.9).
             Executable part: direct pristine-row replay AT THE POINT --
             the residual computed from raw coefficients per (1.11), the
             86-row banked-pipeline cross-match (76 raw D21 + 10 pristine
             Row_22 derivative rows, exact), the certified band-22 deep
             Schur rank 4.  PENDING: the universal identities on the whole
             Newton ball (identities only after evaluation at s are
             explicitly insufficient, sol-newton-lemma.md section 5).
  PARAM-30   an exact all-depth causal right section of L_s^+ with the
             advertised loss, every char-p resonance closed.  Executable
             part: the corrected SQUARE 30x30 window object (174 output x
             170 input coordinates, bands <= 40, exact for the named zero
             completion), the causal delayed-loss scan with the literal
             n >= 0 convention of (2.1) -- in-window coverage failures are
             CERTIFIED lower bounds on ell+ (causality: inputs with r > 40
             cannot reach bands <= 40; the t^42+ x-side terms cannot
             either), plus the leading 30x30 truncation M+(1).  The FAIL
             direction (ell+ lower bound > floor((D-1)/2)) is fully
             certified at the named completion.  PENDING for any PASS: the
             exact Ore recurrence/normal-form section itself -- a bounded
             window reading NEVER promotes ((4.5) resonance control below).
  FILTER-30  the normalization is an integral filtered Euler-differential
             expression, no hidden negative t-shift, every localized
             denominator a unit.  Executable part: measured causality
             (no operator entry with n < r), nonnegative-shift audit,
             chart-unit audit (W_i, HW_i, uW_i = W_i^-1, h32, A_i, r3, z;
             scalar denominators 2,3,5,7^-free prime), Ore affinity
             (A + B*Theta structure) in every populated bin.  PENDING: the
             restricted-series property on the whole ball s+F^1X incl. the
             t^42+ x-side terms (Lemma 4.2 hypotheses + the two-point
             inverse telescope, grok-newton-review Issue 1).

e+ SEMANTICS (sol-newton-lemma.md section 8): e+_cert = a proved upper
bound on ell(L_s^+) realized by a section satisfying (7.2).  This tool
constructs NO section, so e_plus_certified is ALWAYS None (fail-closed).
The window scan returns ell_lb = a CERTIFIED LOWER BOUND on ell+ at the
named completion; it is reported as E_PLUS_CANDIDATE (window floor), never
as an upper bound, never as a DEPTH e.  The index route (8.5) needs a
stabilized d+ from M+(N); N >= 2 reaches the t^42 band of H_29, which the
pure-y build does not contain (sol-round6.md sect 1.1), so d+ and
(e+)^idx are None here (fail-closed), NOT computed from a truncation that
silently deletes the x-side.

PROMOTION CONDITION (stated, never satisfied by this tool alone): a
witness at which all four gates hold at the PROVED tier, with a certified
e+ satisfying 2 e+ + 1 <= D (D = 23 here: e+ <= 11), is a certified
scoped mod-p formal germ by Theorem 6.1.  E_PLUS_CANDIDATE-tier gate
results do NOT promote.

OBJECT + COMPLETION: identical to cases/valuation_e2.py (banked 8.S7
engine, reused verbatim): E = (theta Phi - 12 Phi) Gamma_eta - Phi_eta
(theta Gamma - 18 Gamma) + 42 t^20, dual-jet rebuild mod p, DBUILD = 42
(pure-y exact below t^42), deterministic hashed ZERO completion, measured
DEEP_RELABEL involution, PIN42 never a tangent direction, column mode
tails.  The CORRECTED grading (sol-round6.md sect 1 = sol-newton-lemma.md
(1.0)-(1.4)): 30 inputs (sum r_q = 288) x 30 outputs H_0..H_29
(s_29 = 36, sum s_a = 276), ONE square operator, no free stream, no
29-minor minimization.  Scope box as 8.S6/8.S7: one radical fiber
(radical_point) of 36, residue-A B-frozen no-log W1W2 != 0 chart with
PIN42, mod p, chart-local.

USAGE
  python3 cases/eplus_certify.py --selftest
  python3 cases/eplus_certify.py --gates [--prime P]
  python3 cases/eplus_certify.py --point 105337 0 0     # per-witness mode
  python3 cases/eplus_certify.py --run [--out cases/d23_eplus.json]
        [--heavy]   # add per-point zeta^5 + path-A independence rebuilds
  python3 cases/eplus_certify.py --file WITNESS.json    # any d23-format file
"""
import sys, os, json, time, hashlib, argparse, collections

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import valuation_e as V                  # banked 1a plumbing
import valuation_e2 as V2                # banked 8.S7 engine (reused)

TOOL = "cases/eplus_certify.py"
CAND = "E_PLUS_CANDIDATE"
BANNER = (
    "e+ CERTIFIER (filtered differential Newton lemma application gates). "
    "The lemma (D >= 2e+1 with e = loss of an exact causal right section) "
    "is PROMOTED; the four *-30 application gates are NOT.  This tool "
    "constructs no section: e_plus_certified is always None, every window "
    "number is a certified LOWER bound / %s only, and NO germ is "
    "certified unless every gate reaches the PROVED tier AND "
    "2 e+ + 1 <= D.  Fail-closed; nothing is fabricated." % CAND)

PRIMES = V2.PRIMES                       # (105337, 105673)
RMAX = V2.RMAX                           # 40: window bands <= 40 exact
S30 = list(V2.S_A) + [V2.S_29]           # corrected 30-output shifts
SUM_S30 = sum(S30)                       # 276
SUM_R30 = sum(V2.r_start(rho) for _, rho in V2.STREAMS)   # 288
DEPTH_DEFAULT = 23

PENDING = {
    "CYCLIC-30": ("all-depth 30-stream identity (9.1); band-41 regression "
                  "only -- the H_29 discovery warns against extrapolation"),
    "BRIDGE-30": ("universal levelwise two-sided identities (5.9) on the "
                  "whole Newton ball; point-evaluated identities are "
                  "explicitly insufficient (sol-newton-lemma.md sect 5)"),
    "PARAM-30": ("exact all-depth causal Ore section realizing a finite "
                 "loss with every p-periodic resonance closed; a bounded "
                 "window reading never promotes ((4.5) control)"),
    "FILTER-30": ("restricted Euler-differential series property of the "
                  "source-dependent normalization on s+F^1X incl. the "
                  "t^42+ x-side terms (Lemma 4.2 + inverse telescope)"),
}

# ------------------------------------------------------------------ gates
_RESULTS = []
def rec(name, cond, hard=True, quiet=False):
    _RESULTS.append((name, bool(cond), hard))
    if not quiet or not cond:
        print(("PASS " if cond else ("FAIL " if hard else "WARN ")) + name,
              flush=True)
    if hard and not cond:
        raise SystemExit("EPLUS GATE FAILS at " + name)

def stream_ladders():
    """The 30 input ladders: stream (fam, rho) owns the tangent levels
    r == rho (mod 6) of allowed_r(fam).  Must partition GIDX exactly with
    starts r_start(rho) and step 6 (PIN42 level 10 absent by census)."""
    lad = {}
    for (f, rho) in V2.STREAMS:
        lad[(f, rho)] = sorted(r for r in V2.allowed_r(f)
                               if r % 6 == rho % 6)
    return lad

def gate_cyclic30(E, p):
    """Executable band-41 regression of the corrected 30-output grading."""
    Vv = E.V.astype(np.int64)
    Gg = E.G.astype(np.int64)
    checks = {}
    checks["c1_eta30_33_vanish"] = bool(not Vv[30:].any() and
                                        not Gg[30:].any())
    odd = [n for n in range(V2._S) if n % 2 == 1]
    checks["c2_odd_bands_vanish"] = bool(not Vv[:, odd].any() and
                                         not Gg[:, odd].any())
    ok_cong = True
    starts = []
    for a in range(30):
        nz = [n for n in range(V2._S) if Vv[a][n] or Gg[a][n].any()]
        if any(n % 6 != S30[a] % 6 or n < S30[a] for n in nz):
            ok_cong = False
        starts.append(next((n for n in range(V2._S) if Gg[a][n].any()),
                           None))
    checks["c3_graded_support_bijection"] = bool(ok_cong)
    checks["c4_support_starts_exact"] = bool(starts == S30)
    lad = stream_ladders()
    allr = sorted((f, r) for (f, rho), rs in lad.items() for r in rs)
    checks["c5_input_ladder_partition"] = bool(
        allr == sorted(V2.GIDX.keys()) and
        all(min(rs) == V2.r_start(rho) and
            all(b - a == 6 for a, b in zip(rs, rs[1:]))
            for (f, rho), rs in lad.items()))
    checks["c6_constants_30x30"] = bool(
        len(V2.STREAMS) == 30 and len(S30) == 30 and
        SUM_R30 == 288 and SUM_S30 == 276 and
        S30[28] == 16 and S30[29] == 36)
    ok = all(checks.values())
    return {"checks": checks, "check_pass": ok,
            "status": CAND if ok else "FAIL",
            "pending": PENDING["CYCLIC-30"],
            "support_starts": starts}

def gate_bridge30(E, p, point, D):
    """Executable finite-level bridge: direct pristine replay at the point."""
    Vv = E.V.astype(np.int64)
    Gg = E.G.astype(np.int64)
    checks = {}
    # b1: residual below D directly from raw coefficients, per (1.11)
    below = sorted({int(n) for n in range(min(D, V2._S))
                    if Vv[:30, n].any()})
    checks["b1_residual_below_D_vanishes"] = bool(not below)
    val_bands = sorted({int(n) for n in range(V2._S) if Vv[:30, n].any()})
    nu_window = val_bands[0] if val_bands else None
    checks["b2_nu_window_ge_D"] = bool(nu_window is None or nu_window >= D)
    # b3: banked-pipeline cross-match (76 raw D21 + 10 pristine Row_22)
    ok6, nex, nrows, ratios = V2.banked_row_match(
        E, p, V2.dval_for_banked(p, point))
    checks["b3_banked_86row_match"] = bool(ok6 and nrows == 86)
    # b4: certified band-22 deep Schur rank 4 through this operator
    deepcols = [(f, 17) for f in ("tf1", "tf2", "tg1", "tg2")] + \
               [(f, 22) for f in V2.FAMS]
    rows22 = [a for a in range(29) if V2.S_A[a] == 10] + [28]
    M22 = np.zeros((10, 10), dtype=np.int64)
    for i, a in enumerate(rows22):
        for j, (f, r) in enumerate(deepcols):
            M22[i][j] = Gg[a][22][V2.GIDX[(f, r)]]
    checks["b4_deep_schur_rank_4"] = bool(V2.rankp(M22, p) == 4)
    ok = all(checks.values())
    return {"checks": checks, "check_pass": ok,
            "status": CAND if ok else "FAIL",
            "pending": PENDING["BRIDGE-30"],
            "banked_match": {"rows": nrows, "exact": nex,
                             "unit_rescaled": len(ratios)},
            "nu_window": nu_window,
            "value_bands_le41": val_bands}

def gate_filter30(E, p, point, wit72):
    """Executable syntax/causality/unit audit of the window operator."""
    Gg = E.G.astype(np.int64)
    checks = {}
    viol = 0
    for (f, r), col in V2.GIDX.items():
        if Gg[:30, :min(r, V2._S), col].any():
            viol += 1
    checks["f1_causality_no_entry_below_r"] = bool(viol == 0)
    first = next((n for n in range(V2._S) if Gg[:30, n].any()), None)
    checks["f2_no_negative_shift"] = bool(first is None or first >= min(S30))
    pt, r3, h32 = V.radical_env(p)
    fx = point["fixed"]
    u = {}
    u["r3_sq_3"] = pow(r3, 2, p) == 3 % p
    u["h32_2h2_3"] = (2 * h32 * h32 - 3) % p == 0
    u["A1_cube"] = pow(pt["A1"], 3, p) == (3 + r3) % p
    u["A2_cube"] = pow(pt["A2"], 3, p) == (3 - r3) % p
    u["W_units"] = fx["W1"] % p != 0 and fx["W2"] % p != 0
    u["uW_saturation"] = all(
        int(wit72["uW%d" % i]) * int(wit72["W%d" % i]) % p == 1
        for i in (1, 2))
    u["HW_law"] = all(fx["HW%d" % i] == h32 * fx["W%d" % i] % p
                      for i in (1, 2))
    u["z_order_42"] = (pow(pt["z"], 42, p) == 1 and
                       all(pow(pt["z"], 42 // q, p) != 1 for q in (2, 3, 7)))
    u["scalar_denoms_units"] = all(p % q for q in (2, 3, 5, 7)) and p > 7
    checks["f3_unit_audit"] = all(u.values())
    n3, naff, support = V2.ore_affinity_gate(E, p)
    checks["f4_ore_affinity"] = bool(naff == n3)
    checks["f5_pin42_never_tangent"] = bool(
        all(r != 10 for (_f, r) in V2.GIDX))
    ok = all(checks.values())
    return {"checks": checks, "check_pass": ok,
            "status": CAND if ok else "FAIL",
            "pending": PENDING["FILTER-30"],
            "unit_audit": u, "ore_bins_3plus": [n3, naff]}

# ---------------------------------------------- PARAM-30: the loss scan
def window_object(E):
    """The corrected square operator's exact window: 174 output coords
    (a, j), s_a + 6j <= 40, x 170 tangent coords (GIDX order).  Entries
    are the ACTUAL gradient values (causality is measured, not imposed)."""
    Gg = E.G.astype(np.int64)
    rows = [(a, j) for a in range(30)
            for j in range((RMAX - S30[a]) // 6 + 1)]
    row_lv = np.array([S30[a] + 6 * j for a, j in rows])
    ncol = len(V2.GIDX)
    col_lv = np.zeros(ncol, dtype=np.int64)
    for (f, r), i in V2.GIDX.items():
        col_lv[i] = r
    M = np.zeros((len(rows), ncol), dtype=np.int64)
    for ri, (a, j) in enumerate(rows):
        M[ri, :] = Gg[a][S30[a] + 6 * j][:]
    return rows, row_lv, col_lv, M

def delayed_loss_scan(row_lv, col_lv, M, p):
    """Certified lower bound on ell(L) per (2.1) with the LITERAL n >= 0
    convention: for every n, the window part of L(F^nX) is spanned by the
    columns of level >= n (causality); an in-window unit target of level
    b >= n outside that span certifies ell > b - n, i.e. ell >= b - n + 1.
    Scan evaluates every constant-coverage interval at its LOWER endpoint
    (incl. n = 0), so the bound is the sharpest the window supports."""
    levels = sorted({int(v) for v in col_lv}, reverse=True)
    order = np.argsort(-col_lv, kind="stable")
    cs = V2.Colspace(len(row_lv), p)
    oi = 0
    ell_lb = 0
    profile = []
    for k, v in enumerate(levels):
        while oi < len(order) and col_lv[order[oi]] >= v:
            cs.add(M[:, order[oi]].copy())
            oi += 1
        n_eval = (levels[k + 1] + 1) if k + 1 < len(levels) else 0
        cov = cs.covered_rows()
        bad = row_lv[(~cov) & (row_lv >= n_eval)]
        bound = (int(bad.max()) - n_eval + 1) if len(bad) else 0
        profile.append([int(n_eval), int(v), int((~cov).sum()),
                        (int(bad.max()) if len(bad) else None),
                        max(0, bound)])
        ell_lb = max(ell_lb, bound)
    return int(ell_lb), len(cs.basis), profile

def gate_param30(E, p, D):
    """Executable PARAM-30 content: the square object, M+(1), and the
    certified delayed-loss floor.  FAIL direction fully certified at the
    named completion; PASS direction only ever candidate-tier."""
    Gg = E.G.astype(np.int64)
    checks = {}
    rows, row_lv, col_lv, M = window_object(E)
    checks["p1_square_object_174x170"] = bool(
        M.shape == (174, 170) and len(V2.STREAMS) == 30)
    # M+(1): leading 30x30 truncation of (8.1)
    M1 = np.zeros((30, 30), dtype=np.int64)
    for a in range(30):
        for q, (f, rho) in enumerate(V2.STREAMS):
            M1[a][q] = Gg[a][S30[a]][V2.GIDX[(f, V2.r_start(rho))]]
    rank1 = V2.rankp(M1.copy(), p)
    delta1 = 30 - rank1
    checks["p2_M1_computed"] = True
    ell_lb, wrank, profile = delayed_loss_scan(row_lv, col_lv, M, p)
    checks["p3_loss_scan_ran"] = bool(len(profile) > 0)
    thresh = (D - 1) // 2
    # The threshold comparison is the per-point VERDICT, not an integrity
    # check: ell_lb > thresh is the certified refutation direction.
    refuted = ell_lb > thresh
    if not all(checks.values()):
        status = "FAIL"
    elif refuted:
        status = ("FAIL-CERTIFIED (ell+ >= %d > %d at the named zero "
                  "completion; no causal section of loss <= %d exists "
                  "for this operator)" % (ell_lb, thresh, thresh))
    else:
        status = CAND
    return {"checks": checks, "check_pass": all(checks.values()),
            "verdict_ell_le_threshold": bool(not refuted),
            "status": status, "pending": PENDING["PARAM-30"],
            "window_rank_174x170": int(wrank),
            "delta_plus_N1": int(delta1),
            "delta_plus_N2plus": ("NOT COMPUTABLE from the pure-y build: "
                                  "H_29 row j >= 1 sits at band >= 42 = "
                                  "the unbanked x-side (sol-round6 1.1); "
                                  "fail-closed"),
            "d_plus_stabilized": None, "e_plus_idx": None,
            "ell_lb_certified": int(ell_lb),
            "ell_scan_profile": profile,
            "ell_profile_key": ("[n_eval, cols>=level, n_uncovered, "
                                "max_uncovered_level, ell_ge]"),
            "threshold_floor_Dm1_2": thresh}

# --------------------------------------------------------------- verdict
def certify_point(p, wit72, deep_tails, D=DEPTH_DEFAULT, heavy=False,
                  tag=""):
    t0 = time.time()
    pt, r3, h32 = V.radical_env(p)
    Z = [pow(pt["z"], m, p) for m in range(42)]
    point = V2.build_point(p, wit72, deep_tails)
    jf, jg = V2.build_jets(point, p, Z)
    E = V2.euler_rows(jf, jg, p)
    res = {"tool": TOOL, "prime": p, "depth_D": D,
           "zc_hash": point["zc_hash"],
           "operator_hash": V2.operator_hash(E, p)}
    gates = {}
    gates["CYCLIC-30"] = gate_cyclic30(E, p)
    gates["BRIDGE-30"] = gate_bridge30(E, p, point, D)
    gates["FILTER-30"] = gate_filter30(E, p, point, wit72)
    gates["PARAM-30"] = gate_param30(E, p, D)
    if heavy:
        Z2r = pow(pt["z"], 5, p)
        Z2 = [pow(Z2r, m, p) for m in range(42)]
        jf2, jg2 = V2.build_jets(point, p, Z2)
        E2 = V2.euler_rows(jf2, jg2, p)
        gates["FILTER-30"]["checks"]["f6_zeta_branch_invariance"] = bool(
            V2.operator_hash(E2, p) == res["operator_hash"])
        DG = V2.path_A_rows(jf, jg, p)
        gates["FILTER-30"]["checks"]["f7_second_diff_path"] = bool(
            np.array_equal(DG, E.G))
        ok = all(gates["FILTER-30"]["checks"].values())
        gates["FILTER-30"]["check_pass"] = ok
        gates["FILTER-30"]["status"] = CAND if ok else "FAIL"
    res["gates"] = gates
    pr = gates["PARAM-30"]
    nu = gates["BRIDGE-30"]["nu_window"]
    thresh = pr["threshold_floor_Dm1_2"]
    ell_lb = pr["ell_lb_certified"]
    res["residual"] = {
        "nu_window": nu,
        "nu_note": ("nu = actual residual order (7.1); a nonzero band "
                    "<= 41 is exact, so nu_window is exact when not None"),
        "nu_ge_D": bool(nu is None or nu >= D)}
    res["e_plus"] = {
        "certified": None,
        "certified_note": ("fail-closed: no exact all-depth causal "
                           "section is constructed (PARAM-30 pending); "
                           "there is NO promoted e+ at this point"),
        "candidate_window_floor": ell_lb,
        "tag": CAND,
        "semantics": ("certified LOWER bound on ell(L_s^+) at the named "
                      "zero completion (literal n >= 0 in (2.1)); the "
                      "all-depth loss can only be >= this"),
        "threshold_2e1_le_D": thresh,
        "at_or_below_threshold": bool(ell_lb <= thresh)}
    all_cand = all(g["check_pass"] for g in gates.values())
    blockers = [k for k, g in gates.items() if g["status"] != "PROVED"]
    res["certification"] = {
        "formal_germ_certified": False,
        "condition": ("Theorem 6.1: ALL four gates at the PROVED tier + "
                      "legal completion + nu >= D + certified e+ with "
                      "2 e+ + 1 <= D (D = %d: e+ <= %d)" % (D, thresh)),
        "blockers": blockers,
        "param30_refuted_at_completion": bool(ell_lb > thresh),
        "executable_checks_all_pass": bool(all_cand)}
    res["seconds"] = round(time.time() - t0, 1)
    return res, E

# --------------------------------------------------------------- selftest
def selftest():
    p = 105337
    # scanner control 1: L = t^e * id on one shift-0 stream has loss e
    for e in (0, 1, 3):
        K = 12
        row_lv = np.arange(K + 1)
        col_lv = np.arange(K + 1)
        M = np.zeros((K + 1, K + 1), dtype=np.int64)
        for r in range(K + 1 - e):
            M[r + e][r] = 1
        ell, rank, _ = delayed_loss_scan(row_lv, col_lv, M, p)
        assert ell == e, "diag t^e control broken (e=%d got %d)" % (e, ell)
    # scanner control 2: the (4.5) resonance -- (Theta+1) u^j has entry
    # (j+1); over F_q with window K < q-1 every truncation is invertible,
    # ell_window = 0, but the TRUE all-depth loss is infinite (the u^{q-1}
    # target is missed).  The scan must return 0 on the short window
    # (proving the window reading is only ever a lower bound) and must
    # DETECT the resonance once the window contains it.
    q = 5
    for K, want in ((3, 0), (6, 5)):
        row_lv = np.arange(K + 1)
        col_lv = np.arange(K + 1)
        M = np.zeros((K + 1, K + 1), dtype=np.int64)
        for j in range(K + 1):
            M[j][j] = (j + 1) % q
        ell, rank, _ = delayed_loss_scan(row_lv, col_lv, M, q)
        assert ell == want, "resonance control broken (K=%d)" % K
    # control 3: uncovered target strictly between column levels uses the
    # interval lower endpoint (n = 0 here), not the column level
    row_lv = np.array([0, 4])
    col_lv = np.array([2])
    M = np.array([[1], [0]], dtype=np.int64)
    ell, rank, _ = delayed_loss_scan(row_lv, col_lv, M, p)
    assert ell == 5, "n>=0 literal convention broken (got %d)" % ell
    print("PASS selftest: diag-t^e exact loss (e = 0,1,3); char-p (4.5) "
          "resonance invisible at K=3 (ell=0) and detected at K=6 "
          "(ell=5); literal n>=0 interval endpoints")

# ------------------------------------------------------------ gate suite
def run_gates(primes, quiet=False):
    print("== EPLUS-CERTIFY GATE SUITE (corrected 30x30 Euler/Ore) ==")
    print("   " + BANNER)
    selftest()
    rec("A1 corrected constants: 30 inputs sum r_q = 288; 30 outputs "
        "H_0..H_29, s_28 = 16, s_29 = 36, sum s_a = 276; index formula "
        "6 d+ - 12", SUM_R30 == 288 and SUM_S30 == 276 and
        6 * 2 - 12 == 0 and S30[29] == 36)
    lad = stream_ladders()
    rec("A2 input ladder partition: 170 tangent coords = 30 disjoint "
        "6-step ladders starting at r_q; PIN42 (level 10) absent",
        sorted((f, r) for (f, rho), rs in lad.items() for r in rs) ==
        sorted(V2.GIDX.keys()) and
        all(r != 10 for (_f, r) in V2.GIDX))
    rec("A3 window shape: 174 output x 170 input coordinates at bands "
        "<= %d (= the Round-6 banked weighted-window shape)" % RMAX,
        sum((RMAX - s) // 6 + 1 for s in S30) == 174 and V2.GD == 170)
    for p in primes:
        got, want = V2.zero_config_crosscheck(p)
        rec("A4-p%d char-0 crosscheck: d(eta29 t^36)/d(tf1_48) at the "
            "zero configuration == %d/%d mod p" %
            (p, V2.ETA29_NUM, V2.ETA29_DEN), got == want)
    per_prime = {}
    for p in primes:
        print("-- p = %d: witness 0 / kernel draw 0 full battery --" % p)
        w0 = next(V2.iter_points(p))
        res, E = certify_point(p, w0[2], w0[3], heavy=True,
                               tag="p%d " % p)
        for gname, g in res["gates"].items():
            for cname, ok in g["checks"].items():
                rec("p%d %s %s" % (p, gname, cname), ok, quiet=quiet)
        pr = res["gates"]["PARAM-30"]
        print("   p%d w0k0: window rank %d/174, delta+(1) = %d, "
              "ell+ >= %d (certified), nu_window = %s, PARAM-30: %s"
              % (p, pr["window_rank_174x170"], pr["delta_plus_N1"],
                 pr["ell_lb_certified"], res["residual"]["nu_window"],
                 pr["status"].split(" (")[0]))
        per_prime[p] = res
    if len(per_prime) == 2:
        a, b = (per_prime[p] for p in primes)
        rec("A5 cross-prime: support starts identical",
            a["gates"]["CYCLIC-30"]["support_starts"] ==
            b["gates"]["CYCLIC-30"]["support_starts"])
        rec("A6 cross-prime: certified ell+ floor, window rank, "
            "delta+(1), nu identical on w0k0",
            (a["gates"]["PARAM-30"]["ell_lb_certified"],
             a["gates"]["PARAM-30"]["window_rank_174x170"],
             a["gates"]["PARAM-30"]["delta_plus_N1"],
             a["residual"]["nu_window"]) ==
            (b["gates"]["PARAM-30"]["ell_lb_certified"],
             b["gates"]["PARAM-30"]["window_rank_174x170"],
             b["gates"]["PARAM-30"]["delta_plus_N1"],
             b["residual"]["nu_window"]), hard=False)
    bad = [n for n, c, h in _RESULTS if h and not c]
    print("RESULT: %d/%d gates pass%s" % (
        sum(1 for _, c, _ in _RESULTS if c), len(_RESULTS),
        "" if not bad else "; HARD FAIL %s" % bad))
    print(BANNER)
    return not bad

# -------------------------------------------------------------- full run
def slim(res):
    """Bank-size record: drop nothing load-bearing, compress check maps."""
    out = dict(res)
    out["gates"] = {}
    for k, g in res["gates"].items():
        gg = dict(g)
        gg["checks"] = {c: bool(v) for c, v in g["checks"].items()}
        out["gates"][k] = gg
    return out

def run_all(primes, out_path, heavy=False, files=None, D=DEPTH_DEFAULT):
    print("== EPLUS-CERTIFY FULL RUN ==")
    print("   " + BANNER)
    t00 = time.time()
    results = []
    sources = {}
    def points():
        if files:
            for fp in files:
                W = json.load(open(fp))
                p = int(W["prime"])
                sources[os.path.basename(fp)] = V.sha256(fp)
                for w in W["witnesses"]:
                    wit72 = w["draws"][0]["witness72"]
                    for dd in w["deep_draws"]:
                        yield p, w["index"], dd["kernel_draw"], wit72, \
                            dd["deep_tails"]
        else:
            for p in primes:
                fp = V2.witness_file(p)
                sources[os.path.basename(fp)] = V.sha256(fp)
                for widx, kdraw, wit72, deep in V2.iter_points(p):
                    yield p, widx, kdraw, wit72, deep
    for p, widx, kdraw, wit72, deep in points():
        tag = "p%d w%d k%d" % (p, widx, kdraw)
        res, E = certify_point(p, wit72, deep, D=D, heavy=heavy, tag=tag)
        res["witness"] = widx
        res["kernel_draw"] = kdraw
        gs = {k: ("cand" if g["status"] == CAND else
                  ("REFUTED" if "FAIL-CERTIFIED" in g["status"]
                   else g["status"])) for k, g in res["gates"].items()}
        print("%s: ell+>=%d (certified) nu=%s rank=%d/174 d+(1)=%d "
              "gates[C/B/F/P]=%s/%s/%s/%s e+cert=None (%.0fs)"
              % (tag, res["gates"]["PARAM-30"]["ell_lb_certified"],
                 res["residual"]["nu_window"],
                 res["gates"]["PARAM-30"]["window_rank_174x170"],
                 res["gates"]["PARAM-30"]["delta_plus_N1"],
                 gs["CYCLIC-30"], gs["BRIDGE-30"], gs["FILTER-30"],
                 gs["PARAM-30"], res["seconds"]), flush=True)
        results.append(slim(res))
    ell_dist = collections.Counter(
        r["gates"]["PARAM-30"]["ell_lb_certified"] for r in results)
    rank_dist = collections.Counter(
        r["gates"]["PARAM-30"]["window_rank_174x170"] for r in results)
    nu_dist = collections.Counter(
        str(r["residual"]["nu_window"]) for r in results)
    thresh = (D - 1) // 2
    n_at = sum(1 for r in results
               if r["e_plus"]["candidate_window_floor"] <= thresh)
    n_cert = sum(1 for r in results
                 if r["certification"]["formal_germ_certified"])
    n_refuted = sum(1 for r in results
                    if r["certification"]["param30_refuted_at_completion"])
    checks_fail = [
        (r["prime"], r["witness"], r["kernel_draw"], k, c)
        for r in results for k, g in r["gates"].items()
        for c, v in g["checks"].items() if not v]
    out = {
        "tool": TOOL,
        "date": time.strftime("%Y-%m-%d"),
        "object": ("corrected 30-input/30-output Euler/Ore linearization "
                   "L_s^+ (sol-round6.md sect 1 = sol-newton-lemma.md "
                   "(1.0)-(1.9)); one square operator, no free stream; "
                   "dual-jet rebuild mod p at DBUILD=42 (pure-y exact "
                   "below t^42), deterministic hashed zero completion, "
                   "measured DEEP_RELABEL, PIN42 pinned, tails mode"),
        "status": "INTERNAL / UNREVIEWED; fail-closed; " + CAND + " only",
        "banner": BANNER,
        "scope": ("one radical fiber (radical_point) of 36; residue-A "
                  "B-frozen no-log W1W2 != 0 chart with PIN42; mod p "
                  "ONLY; chart-local; per named zero completion"),
        "depth_D": D,
        "threshold_e_le": thresh,
        "promotion_condition": (
            "Theorem 6.1 (sol-newton-lemma.md): all four gates at the "
            "PROVED tier + legal completion + nu >= D + certified e+ "
            "with 2 e+ + 1 <= D => scoped mod-p formal germ.  %s-tier "
            "gate results do NOT promote." % CAND),
        "gate_tiers": {
            "CYCLIC-30": "executable band-41 regression; PASS pending "
                         "the all-depth identity",
            "BRIDGE-30": "executable point-level pristine replay + 86-row "
                         "banked match; PASS pending the universal (5.9) "
                         "identities",
            "FILTER-30": "executable causality/shift/unit/Ore audit; PASS "
                         "pending the restricted-series lemma on the ball",
            "PARAM-30": "FAIL direction fully certified in-window "
                        "(causal lower bound); PASS direction would need "
                        "the exact all-depth Ore section (unproved)"},
        "primes": sorted({r["prime"] for r in results}),
        "n_points": len(results),
        "n_executable_check_failures": len(checks_fail),
        "executable_check_failures": checks_fail,
        "ell_lb_certified_distribution": {str(k): v for k, v
                                          in sorted(ell_dist.items())},
        "window_rank_distribution": {str(k): v for k, v
                                     in sorted(rank_dist.items())},
        "nu_window_distribution": dict(nu_dist),
        "n_points_at_or_below_threshold": n_at,
        "n_param30_refuted_at_completion": n_refuted,
        "n_formal_germs_certified": n_cert,
        "e_plus_certified_all_points": None,
        "witness_files_sha256": sources,
        "points": results,
        "seconds": round(time.time() - t00),
    }
    if out_path:
        with open(out_path, "w") as f:
            json.dump(out, f, indent=1, sort_keys=True)
        print("-> wrote %s" % out_path)
    print("ell+ floor distribution (certified lower bounds): %s"
          % dict(sorted(ell_dist.items())))
    print("points at/below the D=%d certification threshold e+ <= %d: "
          "%d/%d; PARAM-30 refuted-at-completion: %d/%d; formal germs "
          "certified: %d" % (D, thresh, n_at, len(results), n_refuted,
                             len(results), n_cert))
    print(BANNER)
    return out

def main():
    ap = argparse.ArgumentParser(description="e+ certifier (Newton-lemma "
                                 "application gates; fail-closed)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--gates", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--heavy", action="store_true",
                    help="per-point zeta^5 + path-A rebuilds on --run")
    ap.add_argument("--point", nargs=3, type=int, metavar=("P", "W", "K"))
    ap.add_argument("--prime", type=int, default=None)
    ap.add_argument("--file", action="append", default=None,
                    help="witness JSON (d23_witnesses format); repeatable")
    ap.add_argument("--depth", type=int, default=DEPTH_DEFAULT)
    ap.add_argument("--out", default=os.path.join(HERE, "d23_eplus.json"))
    args = ap.parse_args()
    primes = (args.prime,) if args.prime else PRIMES
    if args.selftest:
        selftest()
        return
    if args.gates:
        ok = run_gates(primes, quiet=True)
        sys.exit(0 if ok else 1)
    if args.point:
        p, widx, k = args.point
        for w, kd, wit72, deep in V2.iter_points(p):
            if w == widx and kd == k:
                res, E = certify_point(p, wit72, deep, D=args.depth,
                                       heavy=True)
                res["witness"] = widx
                res["kernel_draw"] = kd
                out = slim(res)
                out["gates"]["PARAM-30"].pop("ell_scan_profile", None)
                print(json.dumps(out, indent=1, sort_keys=True,
                                 default=str))
                return
        raise SystemExit("point not found")
    if args.run:
        run_all(primes, args.out, heavy=args.heavy, files=args.file,
                D=args.depth)
        return
    ap.print_help()

if __name__ == "__main__":
    main()
