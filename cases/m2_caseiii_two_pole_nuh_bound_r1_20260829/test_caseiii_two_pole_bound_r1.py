#!/usr/bin/env python3
"""Bounded hostile tests for the two-pole case-III incoming-index theorem."""

from __future__ import annotations

import importlib.util
import itertools
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "caseiii_two_pole_bound_r1.py"


def load_module():
    spec = importlib.util.spec_from_file_location("caseiii_two_pole_bound_r1",
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


def test_three_regimes() -> None:
    low = M.incoming_index_certificate(3, Fraction(2), 2, Fraction(1))
    check(low["regime"] == "mu0<mu", "low-regime")
    check(low["max_integer_h"] == 2, "low-strict-bound")
    equal = M.incoming_index_certificate(2, Fraction(3, 2),
                                         2, Fraction(1, 2))
    check(equal["regime"] == "mu0=mu", "equal-regime")
    check(equal["legal_integer_h"] == 3, "equal-forced")
    equal_bad = M.incoming_index_certificate(2, Fraction(4, 3),
                                             2, Fraction(1, 2))
    check(equal_bad["legal_integer_h"] is None, "equal-noninteger")
    high = M.incoming_index_certificate(1, Fraction(2),
                                        2, Fraction(3, 2))
    check(high["regime"] == "mu0>mu", "high-regime")
    check(high["kbar_upper"] == "10", "high-kbar-bound")
    check(high["max_integer_h"] == 4, "high-h-bound")


def test_gap_lemma_exhaustively() -> None:
    observed = 0
    equality = None
    for mu in range(1, 6):
        for delta in range(1, 7):
            mu0 = mu + delta
            for nu in range(1, 15):
                for k in range(0, 4):
                    pools = itertools.product(range(1, mu), repeat=k)
                    for mults in pools:
                        for lex in range(0, 5):
                            sm = sum(mults)
                            s = k + lex
                            dp = mu0 + nu * (mu + sm)
                            dq = 1 + nu * (1 + s)
                            D = mu * dq - dp
                            if D <= 0:
                                continue
                            observed += 1
                            check(s >= 1, f"gap-s-positive-{observed}")
                            check(Fraction(dq, D) <= 2 * delta + 3,
                                  f"gap-bound-{observed}")
                            if Fraction(dq, D) == 2 * delta + 3:
                                equality = (mu, mu0, nu, k, lex, mults)
    check(observed > 1000, "gap-enumeration-nontrivial")
    # The constant cannot be silently tightened to 2*delta+2.
    check(equality is not None, "gap-sharpness-fixture")


def test_literal_patterns() -> None:
    # Charged h=3 cell.
    p = M.pattern_certificate(1, 2, 3, 0, 1, (),
                              Fraction(2), Fraction(3, 2))
    check((p["dp"], p["dq"], p["D"]) == (5, 7, 2), "charged-degrees")
    check((p["kbar"], p["X"], p["h"]) == ("7", "5", "3"),
          "charged-handshakes")
    check(p["universal_max_integer_h"] == 4, "charged-bound")

    # The degree-gap constant is attained: delta=1, nu=2, one NE orbit of
    # maximal multiplicity mu-1 gives dq/D=5.
    sharp = M.pattern_certificate(2, 3, 2, 1, 0, (1,),
                                  Fraction(1), Fraction(1))
    check(sharp["dq_over_D"] == "5", "sharp-ratio")
    check(sharp["h"] == "4", "sharp-h")
    check(sharp["universal_max_integer_h"] == 4, "sharp-bound-attained")


def test_rational_handshake_grid() -> None:
    checked = 0
    for mu in range(1, 4):
        for mu0 in range(mu + 1, mu + 4):
            for nu in range(1, 8):
                for k in range(0, 3):
                    for mults in itertools.product(range(1, mu), repeat=k):
                        for lex in range(0, 4):
                            for w in (Fraction(1, 2), Fraction(1),
                                      Fraction(3, 2), Fraction(2)):
                                for w0 in (Fraction(1, 2), Fraction(1),
                                           Fraction(3, 2)):
                                    sm = sum(mults)
                                    dp = mu0 + nu * (mu + sm)
                                    dq = 1 + nu * (1 + k + lex)
                                    if mu * dq <= dp:
                                        continue
                                    p = M.pattern_certificate(mu, mu0, nu,
                                                              k, lex, mults,
                                                              w, w0)
                                    h = Fraction(p["h"])
                                    checked += 1
                                    check(h <= p["universal_max_integer_h"]
                                          if h.denominator == 1 else
                                          h <= Fraction(str(
                                              M.incoming_index_certificate(
                                                  mu, w, mu0, w0)["h_upper"])),
                                          f"rational-grid-{checked}")
    check(checked > 500, "rational-grid-nontrivial")


def test_certificate_and_optimized() -> None:
    payload = M.charged_certificate()
    check(payload["charged_neutral_ray"]["finite_candidates_after_bound"]
          == [3], "charged-candidate-set")
    check(payload["firewall"]["equal_nonzero_join_kbar_bounded"] is False,
          "equal-join-firewall")
    check(payload["firewall"]["jc2"] is False, "jc2-firewall")
    completed = subprocess.run([sys.executable, "-O", str(SOURCE)],
                               check=False, capture_output=True, text=True,
                               timeout=20)
    check(completed.returncode == 0, "optimized-returncode")
    optimized = json.loads(completed.stdout)
    check(optimized["certificate_sha256"] == payload["certificate_sha256"],
          "optimized-certificate")


def test_invalid_inputs() -> None:
    bad = 0
    for args in [
        (0, Fraction(1), 2, Fraction(1)),
        (1, Fraction(0), 2, Fraction(1)),
        (1, Fraction(1), 0, Fraction(1)),
        (1, Fraction(1), 2, Fraction(0)),
    ]:
        try:
            M.incoming_index_certificate(*args)
        except ValueError:
            bad += 1
    check(bad == 4, "invalid-input-refusal")


def main() -> int:
    test_three_regimes()
    test_gap_lemma_exhaustively()
    test_literal_patterns()
    test_rational_handshake_grid()
    test_certificate_and_optimized()
    test_invalid_inputs()
    print(f"CASEIII_TWO_POLE_BOUND_R1_TEST_PASS checks={CHECKS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
