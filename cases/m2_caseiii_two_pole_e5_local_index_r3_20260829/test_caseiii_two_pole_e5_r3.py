#!/usr/bin/env python3
"""Hostile tests for the R3 two-pole case-III E5 packet.

Run BOTH:  python3 test_caseiii_two_pole_e5_r3.py
           python3 -O test_caseiii_two_pole_e5_r3.py

All load-bearing checks use check()/require(), never bare assert, so the
-O run exercises the same battery.  The sweeps recompute every quantity
inline (independent of the module); the canonical engine
cases/book_offaxis.py is imported READ-ONLY for the cell_check
cross-check of the repaired s7.4 fibre; the ten staged mutations copy
the module to /tmp, apply one exact single-occurrence string edit each,
and require certificate() to fail -- the packet itself is never
modified.
"""

from __future__ import annotations

import importlib.util
import itertools
import json
import subprocess
import sys
import tempfile
from fractions import Fraction
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "caseiii_two_pole_e5_r3.py"
SEALED = HERE / "certificate_r3.json"


def load_module():
    spec = importlib.util.spec_from_file_location("caseiii_two_pole_e5_r3",
                                                  SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError("module spec unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


M = load_module()
CHECKS = 0


def check(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError(f"CHECK_FAILED:{label}")


def ceil_div(a: int, b: int) -> int:
    return -(-a // b)


# ---------------------------------------------------------------------------
def test_gap_sweep_inline() -> None:
    """Independent integer sweep of Lemma A + Theorem B over the box
    mu <= 6, delta <= 8, nu <= 26, k <= 3, lex <= 4, all NE-legal
    multiplicity tuples.  Equality censuses are exact.  Preserved from
    R2 (the theorem layer is unchanged in R3)."""
    plain_eq = {}
    graded_eq = {}
    legal_cells = 0
    box_cells = 0
    for mu in range(1, 7):
        for delta in range(1, 9):
            mu0 = mu + delta
            for k in range(0, 4):
                for mults in itertools.product(range(1, mu), repeat=k):
                    sm = sum(mults)
                    for lex in range(0, 5):
                        s = k + lex
                        A = mu * s - sm
                        for nu in range(2, 27):
                            dp = mu0 + nu * (mu + sm)
                            dq = 1 + nu * (1 + s)
                            D = mu * dq - dp
                            if D <= 0:
                                continue
                            box_cells += 1
                            check(D == nu * A - delta, "D-identity")
                            check(s >= 1 and A >= s, "s-A-laws")
                            Mg = gcd(dp, dq)
                            check(D % Mg == 0, "M-divides-D")
                            ne_ok = all(m * dq < dp for m in mults)
                            if not ne_ok:
                                check(dq <= D, "ne-illegal-ratio")
                                continue
                            legal_cells += 1
                            check(dq <= D * (2 * delta + 3), "lemma-A")
                            check(dq * Mg <= D * (2 * Mg + 2 * delta + 1),
                                  "theorem-B")
                            if dq == D * (2 * delta + 3):
                                check(D == 1 and Mg == 1
                                      and nu == delta + 1 and s == 1
                                      and A == 1, "plain-eq-profile")
                                plain_eq[delta] = plain_eq.get(delta, 0) + 1
                            if dq * Mg == D * (2 * Mg + 2 * delta + 1):
                                check(D == Mg and nu == delta + Mg
                                      and s == 1 and A == 1
                                      and (2 * delta + 1) % Mg == 0,
                                      "graded-eq-profile")
                                key = (delta, Mg)
                                graded_eq[key] = graded_eq.get(key, 0) + 1
                            if nu <= 8:
                                cert = M.gap_pattern_certificate(
                                    mu, mu0, nu, k, mults, lex)
                                check((cert["dp"], cert["dq"], cert["M"])
                                      == (dp, dq, Mg), "module-agrees")
    check(box_cells > 250000 and legal_cells > 40000, "sweep-nontrivial")
    for delta in range(1, 9):
        check(plain_eq.get(delta, 0) >= 1, f"plain-eq-attained-d{delta}")
        check(graded_eq.get((delta, 2 * delta + 1), 0) >= 1,
              f"graded-eq-attained-d{delta}")
        if (2 * delta + 1) % 3 == 0:
            check(graded_eq.get((delta, 3), 0) >= 1,
                  f"graded-eq-M3-d{delta}")
        check(all(m % 2 == 1 for (d, m) in graded_eq if d == delta),
              f"graded-eq-odd-only-d{delta}")


# ---------------------------------------------------------------------------
# Independent copy of the promoted s11a book (typed separately from the
# module's copy; a divergence fails the cross-check).
BOOK_INDEP = (
    (9, 15, 7, 3, 2, 5, "1/2"), (10, 15, 7, 5, 3, 6, "2/3"),
    (15, 25, 12, 5, 3, 5, "1/3"), (18, 27, 13, 9, 5, 6, "2/5"),
    (21, 35, 17, 7, 4, 5, "1/4"), (25, 35, 17, 5, 8, 7, "3/8"),
    (26, 39, 19, 13, 7, 6, "2/7"), (27, 45, 22, 9, 5, 5, "1/5"),
    (34, 51, 25, 17, 9, 6, "2/9"), (42, 63, 31, 21, 11, 6, "2/11"),
    (50, 75, 37, 25, 13, 6, "2/13"), (58, 87, 43, 29, 15, 6, "2/15"),
    (66, 99, 49, 33, 17, 6, "2/17"), (74, 111, 55, 37, 19, 6, "2/19"),
    (82, 123, 61, 41, 21, 6, "2/21"), (90, 135, 67, 45, 23, 6, "2/23"),
    (98, 147, 73, 49, 25, 6, "2/25"),
)


def test_promoted_book_inline() -> None:
    mu, w = 1, Fraction(2)
    opus_viol = 0
    graded_rows = 0
    for (dp, dq, nu_g, Mg, mu0, kbar, w_u_s) in BOOK_INDEP:
        w_u = Fraction(w_u_s)
        delta = mu0 - mu
        D = mu * dq - dp
        check(gcd(dp, dq) == Mg and D >= 1, "book-degrees")
        check(dp == mu0 + nu_g and dq == 1 + 2 * nu_g, "book-pattern")
        check(Fraction(kbar) == mu * w * Fraction(dq, D), "book-kbar-law")
        check(Fraction(kbar) <= mu * w * (2 * delta + 3), "book-lemma-A")
        check(Fraction(kbar) <= mu * w * (2 + Fraction(2 * delta + 1, Mg)),
              "book-theorem-B")
        check(mu0 * nu_g * w_u == delta * kbar + mu * w, "book-e5-identity")
        check(nu_g <= mu * w * (delta * (2 * delta + 3) + 1) / (mu0 * w_u),
              "book-nuG-bound")
        if Fraction(dq, D) == 2 + Fraction(2 * delta + 1, Mg):
            graded_rows += 1
            check(kbar == 6 and D == Mg and nu_g == delta + Mg,
                  "book-graded-eq-profile")
            check(Fraction(nu_g) ==
                  mu * w * (delta * (2 + Fraction(2 * delta + 1, Mg)) + 1)
                  / (mu0 * w_u), "book-graded-nuG-tight")
        if nu_g > mu0 * w_u.numerator:
            opus_viol += 1
        check((delta * kbar + mu * w) / (mu0 * w_u) == nu_g,
              "book-mixed-index-is-nuG")
    check(opus_viol == 16, "book-opus-16of17")
    check(graded_rows == 12, "book-graded-12rows")
    summary = M.promoted_book_battery()
    check(summary["cells"] == 17
          and summary["opus_clause4_violations"] == 16
          and summary["graded_equality_rows"] == 12
          and summary["solver_recovered"] == 17, "module-book-summary")
    # F8.1: even-m family members are N1-dead with even nu_G = 3m-2.
    for m in (4, 6, 8, 10, 12):
        cell = (4 * m - 2, 6 * m - 3)
        nu_g = 3 * m - 2
        check(gcd(6, nu_g) == 2, "even-m-family-even-nuG")
        hits = [c for c in M.e5_solve_mu1(Fraction(2), m, Fraction(2, m))
                if (c["dp"], c["dq"]) == cell]
        check(len(hits) == 1 and not hits[0]["n1_ok"], f"even-m-{m}-n1dead")


# ---------------------------------------------------------------------------
def test_regimes_and_solver() -> None:
    r1 = M.e5_regimes(3, Fraction(5), 2, Fraction(1))
    check(r1["regime"] == "mu0<mu" and r1["nu_G_menu"] == [2, 3, 4],
          "reverse-regime-menu")
    r1b = M.e5_regimes(3, Fraction(2), 2, Fraction(1))
    check(r1b["nu_G_menu"] == [], "reverse-regime-empty")
    r2 = M.e5_regimes(2, Fraction(3, 2), 2, Fraction(1, 2))
    check(r2["forced_nu_G"] == "3" and r2["legal_case_iii"] is True
          and r2["kbar_pinned"] is False, "equal-regime-forced")
    r2b = M.e5_regimes(2, Fraction(3, 2), 2, Fraction(3, 2))
    check(r2b["legal_case_iii"] is False, "equal-regime-caseI-refused")
    r2c = M.e5_regimes(2, Fraction(4, 3), 2, Fraction(1, 2))
    check(r2c["legal_case_iii"] is False, "equal-regime-nonintegral")
    r3 = M.e5_regimes(1, Fraction(2), 2, Fraction(1, 2))
    check(r3["kbar_upper"] == "10" and len(r3["kbar_menu"]) == 8,
          "difficult-regime-menu-size")
    check(any(e["kbar"] == 5 and e["nu_G"] == 7 for e in r3["kbar_menu"]),
          "difficult-regime-promoted-entry")
    # Solver: the mu0=3, w_U=2/3 menu is exactly the two DEAD56 spot
    # cells (T1-dead) plus the promoted book cell (byte-match with R2).
    menu = M.e5_solve_mu1(Fraction(2), 3, Fraction(2, 3))
    key = sorted((c["dp"], c["dq"], c["nu_G"], c["M"]) for c in menu)
    check(key == [(7, 21, 4, 7), (8, 16, 5, 8), (10, 15, 7, 5)],
          "solver-mu0-3-menu")
    check([c["t1_dead"] for c in
           sorted(menu, key=lambda c: c["dp"])] == [True, True, False],
          "solver-mu0-3-t1")
    menu25 = M.e5_solve_mu1(Fraction(2), 25, Fraction(2, 25))
    check(any((c["dp"], c["dq"]) == (98, 147) and not c["t1_dead"]
              and c["n1_ok"] and c["mp2_ok"] for c in menu25),
          "solver-mu0-25-family")
    # F2 repair: the solver is TOTAL on the exact inputs that crashed R2
    # (w = 1 and w = 3) and on a broad legal grid -- no ValueError may
    # stand in for a verdict.
    w1 = M.e5_solve_mu1(Fraction(1), 3, Fraction(1, 3))
    check([(c["dp"], c["dq"], c["kbar"], c["t1_dead"]) for c in w1]
          == [(8, 16, 2, True), (10, 15, 3, False)], "solver-w1-menu")
    w3 = M.e5_solve_mu1(Fraction(3), 3, Fraction(1))
    check([(c["dp"], c["dq"], c["kbar"], c["t1_dead"]) for c in w3]
          == [(8, 16, 6, True), (10, 15, 9, False)], "solver-w3-menu")
    for w in (Fraction(1), Fraction(2), Fraction(3), Fraction(4),
              Fraction(5), Fraction(6), Fraction(3, 2), Fraction(5, 2),
              Fraction(7, 3)):
        for mu0 in range(2, 9):
            for w_u in (Fraction(1, mu0), Fraction(2, mu0),
                        Fraction(3, mu0), Fraction(1), Fraction(2)):
                cells = M.e5_solve_mu1(w, mu0, w_u)   # must not raise
                check(isinstance(cells, list), "solver-total")
                for c in cells:
                    check(c["t1_dead"] == (c["dq"] % c["dp"] == 0)
                          == (c["M"] == c["dp"]), "solver-t1-consistent")


def test_t1_lemma() -> None:
    """Independent inline verification of Lemma T1'.

    (i) The identity kbar - w = w*dp/D at EVERY mu (not just mu = 1);
    (ii) at mu = 1: dp | dq <=> w/(kbar - w) in Z>=1 <=> M = dp (the
         divisibility leg is mu = 1 ONLY -- dq = dp + D fails at
         mu >= 2, where the law's home scope, the s11 pinned zero-chain
         solve, never applies it);
    (iii) for integer w and integer kbar: kbar in {w + d : d | w};
    (iv) w = 2 recovers the frozen td-7 encoding {3, 4}."""
    check(M.t1_divisor_menu(2) == [3, 4], "t1-w2-is-34")
    check(M.t1_divisor_menu(1) == [2] and M.t1_divisor_menu(3) == [4, 6]
          and M.t1_divisor_menu(4) == [5, 6, 8]
          and M.t1_divisor_menu(6) == [7, 8, 9, 12], "t1-menus")
    ws = (Fraction(1), Fraction(2), Fraction(3), Fraction(7, 2),
          Fraction(5, 3))
    tested = 0
    for mu in (1, 2, 3):
        for delta in range(1, 6):
            mu0 = mu + delta
            for nu in range(2, 16):
                for s in range(1, 8):
                    for sm in range(0, min(s, 3) * (mu - 1) + 1):
                        dp = mu0 + nu * (mu + sm)
                        dq = 1 + nu * (1 + s)
                        D = mu * dq - dp
                        if D < 1:
                            continue
                        if sm:
                            cap = min(mu - 1, (dp - 1) // dq)
                            if cap < 1 or ceil_div(sm, cap) > min(s, sm):
                                continue
                        for w in ws:
                            kbar = mu * w * Fraction(dq, D)
                            check(kbar - w == w * Fraction(dp, D),
                                  "t1-identity")
                            check((dq % dp == 0)
                                  == (gcd(dp, dq) == dp), "t1-M-leg")
                            if mu != 1:
                                tested += 1
                                continue
                            hit = M.t1_closed_form(kbar, w)
                            check(hit == (dq % dp == 0), "t1-iff")
                            if (w.denominator == 1
                                    and kbar.denominator == 1):
                                check(hit == (int(kbar) in
                                              M.t1_divisor_menu(int(w))),
                                      "t1-divisor-form")
                            tested += 1
    check(tested == 17610, "t1-sweep-size")


def test_charged_slice() -> None:
    s = M.charged_slice()
    check(s["kill_reading_stable"] is True, "slice-stable")
    check([r["nu_G"] for r in s["e5_rows"]] == [2, 3, 4], "slice-e5-menu")
    check(s["e5_rows"][1]["cell"] == [5, 7]
          and s["e5_rows"][1]["M"] == 1, "slice-57-cell")
    check(s["mixed_pin_rows"]["h_upper"] == 4
          and s["mixed_pin_rows"]["odd_ray_survivor"] == 3,
          "slice-mixed-pin")
    check("RETRACTED" in s["provenance"]["replays"], "slice-provenance")
    check("(9,15,7,3)" in s["provenance"]["promoted_td7_slice"],
          "slice-untouched-note")
    for h in (3, 5, 7):
        kbar = 2 * h * Fraction(3, 2) - 2
        check(kbar == 3 * h - 2, "slice-mixed-kbar")
        check((h == 3) == (kbar <= 10), "slice-mixed-kill")


# ---------------------------------------------------------------------------
def test_counterfixtures() -> None:
    f = M.counterfixtures()
    check(len(f["r0_2_breaks_constant"]) == 6, "fix-r02-count")
    check(f["r0_2_breaks_constant"][0]["cell"] == [13, 7], "fix-r02-13-7")
    check(f["r0_2_breaks_constant"][4]["cell"] == [109, 22],
          "fix-r02-109-22")
    # F3 repair: every countercell discloses M = 1 / MP2-dead and attains
    # Theorem E with equality.
    for c in f["r0_2_breaks_constant"]:
        check(c["M"] == 1 and c["mp2_dead_as_interior"] is True
              and c["theorem_E_equality"] is True, "fix-r02-mp2-status")
        check(gcd(c["cell"][0], c["cell"][1]) == 1, "fix-r02-gcd-recheck")
    for (mu, delta) in ((4, 5), (6, 2), (2, 7)):
        mu0 = mu + delta
        nu = delta + 1
        m = mu - 1
        dp = mu0 + nu * (2 * mu + m)
        dq = 1 + 3 * nu
        check(mu * dq - dp == 1 and dq == 3 * delta + 4, "fix-r02-inline")
        check(m * dq < dp < mu * dq < mu0 * dq, "fix-r02-laws")
        check(dq > 2 * delta + 3, "fix-r02-breaks")
        check(gcd(dp, dq) == 1, "fix-r02-inline-M1")
    j = f["equal_join_kbar_unbounded"]
    check([c["nu"] for c in j] == [4, 7, 100], "fix-6a-members")
    check(Fraction(j[2]["kbar"]) == 603, "fix-6a-top")
    # F1 repair: the fibre family is GONE from the fixtures.
    check("pattern_fibre_infinite_at_fixed_kbar_nu_G" not in f,
          "fix-fibre-field-deleted")
    check([g["M"] for g in f["ge_prime_out_of_scope_fixtures"]]
          == [3, 4, 2], "fix-ge-prime-Ms")
    check([g["cell"] for g in f["ge_prime_out_of_scope_fixtures"]]
          == [[15, 9], [12, 16], [44, 46]], "fix-ge-prime-cells")


def test_fibre_theorem_d() -> None:
    """Independent inline verification of Theorem D.

    (a) The s7.4 fibre is exactly {(20,10), (26,13)}; the R2 members die
        by hand: dp = 2*dq forces m_j = 1, so Sm = k <= s while the
        family needs Sm = 2s-3.
    (b) The canonical engine agrees: book_offaxis.cell_check (imported
        READ-ONLY) accepts s = 2, 3 and rejects s = 4..9, 21, 45.
    (c) Reduced-box full census (mu <= 5, delta <= 5, nu <= 15,
        s <= 40, no k/lex caps): the closed-form bound holds on every
        cell, and M.fibre_solve reproduces every fibre with bound <= 40
        member-for-member.
    """
    solved = M.fibre_solve(4, Fraction(1), 5, 2, 3)
    check([m["cell"] for m in solved["members"]] == [[20, 10], [26, 13]],
          "fibre-74-members")
    check(solved["s_bound"] == "3", "fibre-74-bound")
    for s in (4, 5, 9, 21, 45):
        dq = 1 + 3 * (1 + s)
        dp = 5 + 3 * (4 + 2 * s - 3)
        check(dp == 2 * dq, "fibre-74-dp-2dq")
        check((dp - 1) // dq == 1, "fibre-74-necap-1")
        check(2 * s - 3 > s, "fibre-74-Sm-exceeds-s")
    # (b) canonical engine cross-check (read-only import).
    sys.path.insert(0, str(HERE.parent))
    import book_offaxis as BO
    verdicts = []
    for s in (2, 3, 4, 5, 6, 7, 8, 9, 21, 45):
        dq = 1 + 3 * (1 + s)
        dp = 5 + 3 * (4 + 2 * s - 3)
        verdicts.append(BO.cell_check(2, 4, [4], 5, gcd(dp, dq)))
    check(verdicts == [True, True] + [False] * 8, "fibre-cellcheck-agrees")
    check(BO.NUCAP == 500, "engine-nucap-untouched")
    # (c) reduced-box full census, fully inline.
    fibres = {}
    cells = 0
    for mu in range(2, 6):
        for delta in range(1, 6):
            mu0 = mu + delta
            for nu in range(2, 16):
                for s in range(1, 41):
                    dq = 1 + nu * (1 + s)
                    for sm in range(0, (mu - 1) * s + 1):
                        dp = mu0 + nu * (mu + sm)
                        D = mu * dq - dp
                        if D < 1:
                            continue
                        if sm:
                            cap = min(mu - 1, (dp - 1) // dq)
                            if cap < 1 or ceil_div(sm, cap) > min(s, sm):
                                continue
                        cells += 1
                        g = gcd(dq, D)
                        P, Q = dq // g, D // g
                        cu = ceil_div(mu * P - Q, P)
                        slack_num = P + (mu * P - Q) - P * cu
                        check(1 <= slack_num <= P, "fibre-inline-slack")
                        check(s * slack_num * nu <= (1 + nu) * Q
                              + delta * P, "fibre-inline-bound")
                        fibres.setdefault((mu, mu0, nu, P, Q),
                                          set()).add((s, dp, dq))
    check(cells > 100000, "fibre-inline-nontrivial")
    multi = sorted(k for k, v in fibres.items() if len(v) >= 2)
    check(len(multi) > 300, "fibre-inline-multi-nontrivial")
    compared = 0
    for key in multi + sorted(fibres)[:400]:
        (mu, mu0, nu, P, Q) = key
        delta = mu0 - mu
        bound = M.fibre_bound(mu, Fraction(P, Q), nu, delta)
        if bound > 40:
            continue                    # inline census incomplete there
        got = M.fibre_solve(mu, Fraction(Q, mu), mu0, P, nu)
        check([tuple(m["cell"]) for m in got["members"]]
              == [(dp, dq) for (s, dp, dq) in sorted(fibres[key])],
              "fibre-solve-matches-inline")
        compared += 1
    check(compared > 500, "fibre-solve-compared-nontrivial")
    # Module box census pins (the review-replay figures).
    box = M.fibre_box_census()
    check(box["summary"]["fibres"] == 92772, "fibre-box-92772")
    check(box["summary"]["size_histogram"]
          == {"1": 92083, "2": 486, "3": 136, "4": 63, "5": 4},
          "fibre-box-histogram")
    comp = M.fibre_complete_census(box["fibres"])
    check(comp["max_fibre_size"] == 12 and comp["max_member_s"] == 1202,
          "fibre-complete-pins")
    check(comp["bound_equality_keys"] == 29444, "fibre-complete-equality")


def test_arity_theorems_e_f() -> None:
    """Independent inline reduced census for Theorems E and F, plus the
    exact (44,46) r0=4 refutation witness."""
    for r0 in (2, 3):
        inline_cells = 0
        inline_viol = []
        for mu in range(1, 6):
            for delta in range(1, 7):
                mu0 = mu + delta
                for nu in range(2, 25):
                    for k in range(0, 3):
                        for lex in range(0, 5):
                            t = r0 - 1 + k + lex
                            dq = 1 + nu * (1 + t)
                            for sm in (range(k, k * (mu - 1) + 1) if k
                                       else (0,)):
                                dp = mu0 + nu * (r0 * mu + sm)
                                D = mu * dq - dp
                                if D < 1:
                                    continue
                                if sm:
                                    cap = min(mu - 1, (dp - 1) // dq)
                                    if cap < 1 or not k <= sm <= k * cap:
                                        continue
                                if dp == mu0 * dq:
                                    continue
                                inline_cells += 1
                                Mg = gcd(dp, dq)
                                check(dq * Mg <= D * ((r0 + 1) * Mg
                                      + (r0 + 1) * delta + 1),
                                      "arity-inline-bound")
                                if dq > D * (2 * delta + 3):
                                    inline_viol.append(Mg)
        check(inline_cells > 10000, f"arity-inline-nontrivial-r{r0}")
        check(len(inline_viol) > 0 and set(inline_viol) == {1},
              f"arity-inline-theorem-F-r{r0}")
        mod = M.arity_census(r0, 5, 6, 24, 2, 4)
        check(mod["cells"] == inline_cells, f"arity-module-agrees-r{r0}")
        check(sorted(m for (_, _, m, _) in mod["violators"])
              == sorted(inline_viol), f"arity-violators-agree-r{r0}")
    # (44,46): the r0 = 4 refutation witness, inline.
    dp, dq = 44, 46
    check(dp == 8 + 9 * 4 and dq == 1 + 9 * 5, "r04-census-identity")
    D, Mg = 46 - 44, gcd(44, 46)
    check(D == 2 and Mg == 2, "r04-D-M")
    check(Fraction(dq, D) == 23 > 17 == 2 * 7 + 3, "r04-violates")
    check(dq * Mg == D * (5 * Mg + 5 * 7 + 1), "r04-graded-equality")
    # Campaign range facts.
    check(list(range(2, 14 // 3 + 1)) == [2, 3, 4], "campaign-m-range")
    ef = M.theorem_ef_certificate()
    check(ef["theorem_F"]["r0_2_violators_all_M1"] == 96
          and ef["theorem_F"]["r0_3_violators_all_M1"] == 248,
          "arity-wide-violator-counts")


def test_no_incoming_bound() -> None:
    d = M.no_incoming_bound_demo()
    check(d["cell"] == [18, 27, 13, 9] and d["mu0"] == 5, "demo-cell")
    check(len(d["samples"]) == 4, "demo-samples")
    check(all(r["kbar_E5"] == "6" for r in d["samples"]), "demo-e5-const")
    check(sum(1 for r in d["samples"] if r["mixed_matches_cell"]) == 0,
          "demo-mixed-varies")
    big = 10 ** 20 + 4
    check((big + 1) % 5 == 0, "demo-big-neutral")
    kbar_mixed_big = (5 * big * Fraction(2, 5) - 2) / 4
    check(kbar_mixed_big > 10 ** 19, "demo-mixed-huge")
    check((5 * 13 * Fraction(2, 5) - 2) / 4 == 6, "demo-u7c-value")
    # F4-charge-5 / R5 repair: nu_G = 13 is NOT arrival-legal at
    # (2/5, M5), so the mixed pin KILLS this cell.
    check((13 + 1) % 5 != 0, "demo-13-not-neutral")
    check(13 not in (2, 7, 12), "demo-13-not-direct")
    check("NOT arrival-legal" in d["mixed_pin_fate"]
          or "not arrival-legal" in d["mixed_pin_fate"].lower(),
          "demo-gloss-corrected")


# ---------------------------------------------------------------------------
def test_certificate_and_optimized() -> None:
    payload = M.certificate()
    check(payload["schema"] == "m2-caseiii-two-pole-e5-local-index-r3",
          "cert-schema")
    check("nu_G" in payload["notation_correction"]
          and "FREE" in payload["notation_correction"], "cert-notation")
    check(all(v is False for v in payload["firewall"].values()),
          "cert-firewall")
    check("r2_fibre_infinitude_reinstated" in payload["firewall"]
          and "t1_w2_encoding_reinstated" in payload["firewall"],
          "cert-firewall-new-keys")
    check("correction_direction_1" in payload["opus_adjudication"]
          and "r2_review_adjudication" in payload["opus_adjudication"],
          "cert-opus-fields")
    check(payload["engine_consequence"]["nucap"].startswith("STAYS"),
          "cert-nucap-stays")
    blob = json.dumps(payload, sort_keys=True)
    check("pattern_fibre_infinite_at_fixed_kbar_nu_G" not in blob,
          "cert-no-infinite-fibre-field")
    # No withdrawn cell may appear as a LEGAL member anywhere: the only
    # occurrences of (38,19)/(62,31)/(134,67) are in the withdrawn list.
    wd = payload["theorem_D"]["seven4_fibre"]["withdrawn_r2_members"]
    check([w["cell"] for w in wd]
          == [[32, 16], [38, 19], [62, 31], [134, 67], [278, 139]],
          "cert-withdrawn-list")
    check(all(w["legal_patterns"] == 0 for w in wd), "cert-withdrawn-0")
    fib = payload["theorem_D"]["seven4_fibre"]["fibre"]["members"]
    check([m["cell"] for m in fib] == [[20, 10], [26, 13]],
          "cert-fibre-legal-only")
    inv = payload["inventory_r2_to_r3"]
    check(all(key in inv for key in ("preserved_verbatim", "repaired",
                                     "withdrawn", "new")), "cert-inventory")
    # Determinism + optimized parity.
    again = M.certificate()
    check(again["certificate_sha256"] == payload["certificate_sha256"],
          "cert-deterministic")
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "opt.json"
        completed = subprocess.run(
            [sys.executable, "-O", str(SOURCE), "--output", str(out)],
            check=False, capture_output=True, text=True, timeout=600)
        check(completed.returncode == 0, "optimized-returncode")
        optimized = json.loads(out.read_text())
        check(optimized["certificate_sha256"]
              == payload["certificate_sha256"], "optimized-sha-match")
    check(SEALED.exists(), "sealed-json-present")
    fresh = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    check(SEALED.read_text() == fresh, "sealed-json-matches")


def test_invalid_inputs() -> None:
    bad = 0
    attempts = [
        lambda: M.gap_pattern_certificate(1, 2, 1, 0, (), 1),   # nu=1
        lambda: M.gap_pattern_certificate(2, 2, 3, 0, (), 1),   # mu0<=mu
        lambda: M.gap_pattern_certificate(2, 3, 3, 1, (2,), 0),  # m>mu-1
        lambda: M.gap_pattern_certificate(2, 3, 3, 1, (), 0),   # census
        lambda: M.gap_pattern_certificate(1, 2, 3, 0, (), 0),   # s=0
        lambda: M.gap_pattern_certificate(3, 4, 2, 1, (2,), 2),  # NE
        lambda: M.e5_regimes(0, Fraction(1), 2, Fraction(1)),
        lambda: M.e5_regimes(1, Fraction(0), 2, Fraction(1)),
        lambda: M.e5_regimes(1, Fraction(1), 2, Fraction(0)),
        lambda: M.kbar_bound(1, Fraction(2), 0),
        lambda: M.e5_solve_mu1(Fraction(2), 1, Fraction(1, 2)),  # mu0=1
        lambda: M.fibre_solve(4, Fraction(1), 4, 2, 3),   # delta=0
        lambda: M.fibre_solve(4, Fraction(1), 5, 2, 1),   # nu=1
        lambda: M.fibre_solve(4, Fraction(3), 5, 2, 3),   # kbar <= w
        lambda: M.t1_divisor_menu(0),
        lambda: M.fibre_bound(1, Fraction(1, 2), 3, 0),   # delta=0
    ]
    for fn in attempts:
        try:
            fn()
        except ValueError:
            bad += 1
    check(bad == len(attempts), "invalid-input-refusal")


# ---------------------------------------------------------------------------
MUTATIONS = {
    "MUT_A_lemmaA_constant": (
        "dq <= D * (2 * delta + 3)", "dq <= D * (2 * delta + 2)"),
    "MUT_B_graded_constant": (
        "dq * M <= D * (2 * M + 2 * delta + 1)",
        "dq * M <= D * (2 * M + 2 * delta - 1)"),
    "MUT_C_elimination_sign": (
        "return (delta * kbar + mu * w) / (mu0 * w_U)",
        "return (delta * kbar - mu * w) / (mu0 * w_U)"),
    "MUT_D_countercell_ratio": (
        "dq == 3 * delta + 4", "dq == 3 * delta + 3"),
    "MUT_E_slice_identity": (
        "3 * nu_g - 2 == kbar", "3 * nu_g + 2 == kbar"),
    "MUT_F_firewall_flip": (
        '"nucap_removal_authorized": False',
        '"nucap_removal_authorized": True'),
    # Permanent R3 mutations (prompt-mandated):
    # (38,19)-style NE bypass -- the derived proxy mu-1 replaces the true
    # strict-NE cap; must re-admit the withdrawn members and be caught.
    "MUT_G_ne_bypass": (
        "return min(mu - 1, (dp - 1) // dq)", "return mu - 1"),
    # w=1/w=3 specialisation bug -- the frozen {3,4} encoding replaces
    # Lemma T1's closed form; must crash the w=1/w=3 regressions.
    "MUT_H_t1_w2_respecialised": (
        "return q.denominator == 1 and q >= 1", "return kbar in (3, 4)"),
    # MP2-status misstatement on the Theorem F violator census.
    "MUT_I_mp2_status": (
        "all(vm == 1 for vm in violator_ms)",
        "all(vm == 2 for vm in violator_ms)"),
    # MP2-status misstatement on the r0=2 countercell disclosure.
    "MUT_J_countercell_m1": (
        "require(mg_cc == 1,", "require(mg_cc == 2,"),
}


def run_mutant(source_text: str, label: str) -> int:
    with tempfile.TemporaryDirectory() as td:
        mod = Path(td) / "caseiii_two_pole_e5_r3.py"
        mod.write_text(source_text)
        completed = subprocess.run(
            [sys.executable, "-c",
             "import sys; sys.path.insert(0, %r); "
             "import caseiii_two_pole_e5_r3 as m; m.certificate()" % td],
            check=False, capture_output=True, text=True, timeout=600)
        return completed.returncode


def test_mutations() -> None:
    text = SOURCE.read_text()
    check(run_mutant(text, "control") == 0, "mutation-control-passes")
    for label, (old, new) in MUTATIONS.items():
        check(text.count(old) == 1, f"mutation-target-unique:{label}")
        rc = run_mutant(text.replace(old, new), label)
        check(rc != 0, f"mutation-detected:{label}")


def main() -> int:
    test_gap_sweep_inline()
    test_promoted_book_inline()
    test_regimes_and_solver()
    test_t1_lemma()
    test_charged_slice()
    test_counterfixtures()
    test_fibre_theorem_d()
    test_arity_theorems_e_f()
    test_no_incoming_bound()
    test_certificate_and_optimized()
    test_invalid_inputs()
    test_mutations()
    print(f"CASEIII_TWO_POLE_E5_R3_TEST_PASS checks={CHECKS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
