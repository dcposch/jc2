#!/usr/bin/env python3
"""Hostile tests for the R2 two-pole case-III E5 packet.

Run BOTH:  python3 test_caseiii_two_pole_e5_r2.py
           python3 -O test_caseiii_two_pole_e5_r2.py

All load-bearing checks use check()/require(), never bare assert, so the
-O run exercises the same battery.  The sweep recomputes every quantity
inline (independent of the module); the six staged mutations copy the
module to /tmp, apply one exact single-occurrence string edit each, and
require certificate() to fail -- the packet itself is never modified.
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
SOURCE = HERE / "caseiii_two_pole_e5_r2.py"
SEALED = HERE / "certificate_r2.json"


def load_module():
    spec = importlib.util.spec_from_file_location("caseiii_two_pole_e5_r2",
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


# ---------------------------------------------------------------------------
def test_gap_sweep_inline() -> None:
    """Independent integer sweep of Lemma A + Theorem B over the box
    mu <= 6, delta <= 8, nu <= 26, k <= 3, lex <= 4, all NE-legal
    multiplicity tuples.  Equality censuses are exact."""
    plain_eq = {}     # delta -> count (must all have D = M = 1)
    graded_eq = {}    # (delta, M) -> count (must have D = M, nu = delta+M)
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
                                # NE-illegal: not a sheet cell; bound is
                                # trivial there (dp <= (mu-1)dq => D >= dq)
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
        # M = 2*delta+1 graded equality (the kbar=6-family shape) exists
        # for every delta; M = 3 whenever 3 | 2*delta+1.
        check(graded_eq.get((delta, 2 * delta + 1), 0) >= 1,
              f"graded-eq-attained-d{delta}")
        if (2 * delta + 1) % 3 == 0:
            check(graded_eq.get((delta, 3), 0) >= 1,
                  f"graded-eq-M3-d{delta}")
        # No graded equality at any even M anywhere (M | 2*delta+1 is odd).
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


# ---------------------------------------------------------------------------
def test_regimes_and_solver() -> None:
    # Regime 1 (mu0 < mu): strict bound nu_G < w/w_U.
    r1 = M.e5_regimes(3, Fraction(5), 2, Fraction(1))
    check(r1["regime"] == "mu0<mu" and r1["nu_G_menu"] == [2, 3, 4],
          "regime1-menu")
    r1b = M.e5_regimes(3, Fraction(2), 2, Fraction(1))
    check(r1b["nu_G_menu"] == [], "regime1-empty")
    # Regime 2 (mu0 = mu): forced value; nu_G = 1 is case-I territory.
    r2 = M.e5_regimes(2, Fraction(3, 2), 2, Fraction(1, 2))
    check(r2["forced_nu_G"] == "3" and r2["legal_case_iii"] is True,
          "regime2-forced")
    r2b = M.e5_regimes(2, Fraction(3, 2), 2, Fraction(3, 2))
    check(r2b["legal_case_iii"] is False, "regime2-caseI-refused")
    r2c = M.e5_regimes(2, Fraction(4, 3), 2, Fraction(1, 2))
    check(r2c["legal_case_iii"] is False, "regime2-nonintegral")
    # Regime 3: menu finiteness and the promoted @2 entry.
    r3 = M.e5_regimes(1, Fraction(2), 2, Fraction(1, 2))
    check(r3["kbar_upper"] == "10" and len(r3["kbar_menu"]) == 8,
          "regime3-menu-size")
    check(any(e["kbar"] == 5 and e["nu_G"] == 7 for e in r3["kbar_menu"]),
          "regime3-promoted-entry")
    # Solver: the mu0=3, w_U=2/3 menu is exactly the two DEAD56 spot
    # cells (T1-dead) plus the promoted book cell.
    menu = M.e5_solve_mu1(Fraction(2), 3, Fraction(2, 3))
    key = sorted((c["dp"], c["dq"], c["nu_G"], c["M"]) for c in menu)
    check(key == [(7, 21, 4, 7), (8, 16, 5, 8), (10, 15, 7, 5)],
          "solver-mu0-3-menu")
    check([c["t1_dead"] for c in
           sorted(menu, key=lambda c: c["dp"])] == [True, True, False],
          "solver-mu0-3-t1")
    # Family endpoint: mu0=25 recovers (98,147,73,49) alive.
    menu25 = M.e5_solve_mu1(Fraction(2), 25, Fraction(2, 25))
    check(any((c["dp"], c["dq"]) == (98, 147) and not c["t1_dead"]
              and c["n1_ok"] and c["mp2_ok"] for c in menu25),
          "solver-mu0-25-family")


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
    # Inline mixed-pin replay: kbar = 3*h - 2 on the odd ray.
    for h in (3, 5, 7):
        kbar = 2 * h * Fraction(3, 2) - 2
        check(kbar == 3 * h - 2, "slice-mixed-kbar")
        check((h == 3) == (kbar <= 10), "slice-mixed-kill")


def test_counterfixtures() -> None:
    f = M.counterfixtures()
    check(len(f["r0_2_breaks_constant"]) == 6, "fix-r02-count")
    check(f["r0_2_breaks_constant"][0]["cell"] == [13, 7], "fix-r02-13-7")
    check(f["r0_2_breaks_constant"][4]["cell"] == [109, 22],
          "fix-r02-109-22")
    # Inline r0=2 family on extra parameters: D = 1 and ratio 3*delta+4.
    for (mu, delta) in ((4, 5), (6, 2), (2, 7)):
        mu0 = mu + delta
        nu = delta + 1
        m = mu - 1
        dp = mu0 + nu * (2 * mu + m)
        dq = 1 + 3 * nu
        check(mu * dq - dp == 1 and dq == 3 * delta + 4, "fix-r02-inline")
        check(m * dq < dp < mu * dq < mu0 * dq, "fix-r02-laws")
        check(dq > 2 * delta + 3, "fix-r02-breaks")
    j = f["equal_join_kbar_unbounded"]
    check([c["nu"] for c in j] == [4, 7, 100], "fix-6a-members")
    check(Fraction(j[2]["kbar"]) == 603, "fix-6a-top")
    fib = f["pattern_fibre_infinite_at_fixed_kbar_nu_G"]
    check([c["M"] for c in fib] == [10, 13, 19, 31, 67], "fix-fibre-M")
    # Inline fibre member beyond the module's list: s = 45.
    s = 45
    dq = 1 + 3 * (1 + s)
    dp = 5 + 3 * (4 + 2 * s - 3)
    check(4 * dq - dp == 2 * dq and Fraction(4 * dq, 2 * dq) == 2,
          "fix-fibre-inline")


def test_no_incoming_bound() -> None:
    d = M.no_incoming_bound_demo()
    check(d["cell"] == [18, 27, 13, 9] and d["mu0"] == 5, "demo-cell")
    check(len(d["samples"]) == 4, "demo-samples")
    check(all(r["kbar_E5"] == "6" for r in d["samples"]), "demo-e5-const")
    check(sum(1 for r in d["samples"] if r["mixed_matches_cell"]) == 0,
          "demo-mixed-varies")
    # Inline: the huge neutral arrival is legal and mixed-pin kbar there
    # is enormous (nu_U-dependent), while nu_U = nu_G = 13 gives 6.
    big = 10 ** 20 + 4
    check((big + 1) % 5 == 0, "demo-big-neutral")
    kbar_mixed_big = (5 * big * Fraction(2, 5) - 2) / 4
    check(kbar_mixed_big > 10 ** 19, "demo-mixed-huge")
    check((5 * 13 * Fraction(2, 5) - 2) / 4 == 6, "demo-u7c-value")


# ---------------------------------------------------------------------------
def test_certificate_and_optimized() -> None:
    payload = M.certificate()
    check(payload["schema"] == "m2-caseiii-two-pole-e5-local-index-r2",
          "cert-schema")
    check("nu_G" in payload["notation_correction"]
          and "FREE" in payload["notation_correction"], "cert-notation")
    check(all(v is False for v in payload["firewall"].values()),
          "cert-firewall")
    check("correction_direction_1" in payload["opus_adjudication"]
          and "correction_direction_2" in payload["opus_adjudication"],
          "cert-opus-both-directions")
    check(payload["engine_consequence"]["nucap"].startswith("STAYS"),
          "cert-nucap-stays")
    # Determinism + optimized parity.
    again = M.certificate()
    check(again["certificate_sha256"] == payload["certificate_sha256"],
          "cert-deterministic")
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "opt.json"
        completed = subprocess.run(
            [sys.executable, "-O", str(SOURCE), "--output", str(out)],
            check=False, capture_output=True, text=True, timeout=60)
        check(completed.returncode == 0, "optimized-returncode")
        optimized = json.loads(out.read_text())
        check(optimized["certificate_sha256"]
              == payload["certificate_sha256"], "optimized-sha-match")
    # The sealed in-packet JSON must equal a fresh regeneration
    # byte-for-byte (guards producer-authored drift).
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
        lambda: M.e5_regimes(0, Fraction(1), 2, Fraction(1)),
        lambda: M.e5_regimes(1, Fraction(0), 2, Fraction(1)),
        lambda: M.e5_regimes(1, Fraction(1), 2, Fraction(0)),
        lambda: M.kbar_bound(1, Fraction(2), 0),
    ]
    # NE-illegal pattern (m*dq >= dp): mu=3, mu0=4, nu=2, one orbit m=2,
    # lex=2: dp = 4+2*5 = 14, dq = 1+2*4 = 9? m*dq = 18 >= 14 -> reject.
    attempts.append(lambda: M.gap_pattern_certificate(3, 4, 2, 1, (2,), 2))
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
}


def run_mutant(source_text: str, label: str) -> int:
    with tempfile.TemporaryDirectory() as td:
        mod = Path(td) / "caseiii_two_pole_e5_r2.py"
        mod.write_text(source_text)
        completed = subprocess.run(
            [sys.executable, "-c",
             "import sys; sys.path.insert(0, %r); "
             "import caseiii_two_pole_e5_r2 as m; m.certificate()" % td],
            check=False, capture_output=True, text=True, timeout=120)
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
    test_charged_slice()
    test_counterfixtures()
    test_no_incoming_bound()
    test_certificate_and_optimized()
    test_invalid_inputs()
    test_mutations()
    print(f"CASEIII_TWO_POLE_E5_R2_TEST_PASS checks={CHECKS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
