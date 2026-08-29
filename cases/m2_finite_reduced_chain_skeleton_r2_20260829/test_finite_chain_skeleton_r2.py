#!/usr/bin/env python3
"""Bounded mutation/regression tests for finite_chain_skeleton_r1.py."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "finite_chain_skeleton_r2.py"


def load_module():
    spec = importlib.util.spec_from_file_location("finite_chain_skeleton_r1",
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


def test_divisors() -> None:
    check(M.divisors(1) == [1], "divisors-one")
    check(M.divisors(36) == [1, 2, 3, 4, 6, 9, 12, 18, 36],
          "divisors-36")


def test_pure_epsilon_congruences() -> None:
    w, l, eps = Fraction(3, 5), 4, 1
    classes = M.pure_epsilon_classes(w, l, eps)
    check(set(classes) == {1, 3}, "pure-class-set")
    modulus = next(iter(classes.values()))["nu_plus_one_modulus"]
    check(modulus == 15, "pure-modulus")
    observed: dict[int, set[int]] = {}
    E = l - eps
    for N in range(0, 4 * modulus):
        if (w.denominator * E) and \
                (l * w.numerator * N) % (w.denominator * E) == 0:
            observed.setdefault(__import__("math").gcd(E, N), set()).add(
                N % modulus)
    expected = {
        g: set(data["nu_plus_one_residues"])
        for g, data in classes.items()
    }
    check(observed == expected, "pure-bruteforce-residues")


def test_derived_lex_bounds() -> None:
    # epsilon>0: T positivity is both necessary and sufficient for this bound.
    b = M.dirty_lex_bound(Fraction(3, 2), l=6, eps=2, k=1, Sm=4)
    check(b == 2, "eps-lex-bound")
    for lex in range(0, b + 1):
        T = 4 + 6 - 2 * (1 + 1 + lex)
        check(T >= 1, f"eps-T-positive-{lex}")
    T_after = 4 + 6 - 2 * (1 + 1 + b + 1)
    check(T_after <= 0, "eps-T-stops")

    # epsilon=0: any lex above the bound violates E>=l+2C together
    # with E<=l*num(w)*T before a divisor is even considered.
    w, l, k, Sm = Fraction(3, 2), 6, 2, 5
    b = M.dirty_lex_bound(w, l=l, eps=0, k=k, Sm=Sm)
    check(b >= 0, "zero-eps-bound-nonnegative")
    C_after = l * (k + b + 1) - Sm
    T = Sm + l
    check(l + 2 * C_after > l * w.numerator * T,
          "zero-eps-bound-stops")


def test_charged_closure() -> None:
    payload = M.close_reduced_skeleton(Fraction(3, 2), 2, 5)
    expected = {
        "state_count": 69,
        "expanded_edge_count": 295,
        "max_reduced_w_numerator": 3,
        "max_M": 25,
        "max_k_observed": 2,
        "max_lex_observed": 0,
        "max_derived_lex_bound": 27,
        "state_table_sha256":
            "c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad",
    }
    for key, value in expected.items():
        check(payload[key] == value, f"charged-{key}")
    check(payload["cap_free"] is True, "charged-cap-free")
    check(payload["hard_loop_caps"] == [], "charged-no-caps")
    check(payload["zero_cost_reduced_nonincrease"] is True,
          "charged-zero-cost-monotonicity")
    check(payload["firewall"]["merges_enumerated"] is False,
          "charged-merge-firewall")
    check(payload["firewall"]["jc2"] is False, "charged-jc2-firewall")
    second = M.close_reduced_skeleton(Fraction(3, 2), 2, 5)
    check(M.canonical(payload) == M.canonical(second),
          "charged-determinism")


def test_predecessors_are_minimal() -> None:
    payload = M.close_reduced_skeleton(Fraction(3, 2), 2, 5)
    costs = {f"{row['w']}|{row['M']}": row["lambda_min"]
             for row in payload["states"]}
    pred = payload["first_predecessor"]
    check(len(pred) == payload["state_count"] - 1,
          "predecessor-tree-census")
    coherent = all(
        record["parent"]["lambda"] + record["step"]["lambda"] == costs[child]
        for child, record in pred.items()
    )
    check(coherent, "predecessor-minimum-cost-coherence")


def test_secondary_lex_regression() -> None:
    payload = M.close_reduced_skeleton(Fraction(2), 4, 4)
    expected = {
        "state_count": 152,
        "expanded_edge_count": 658,
        "max_reduced_w_numerator": 8,
        "max_M": 25,
        "max_k_observed": 4,
        "max_lex_observed": 2,
        "max_derived_lex_bound": 99,
        "state_table_sha256":
            "255f1fe24efce6921703a80155646f5a78f949f678c96043d47c0beec6ddfd7d",
    }
    for key, value in expected.items():
        check(payload[key] == value, f"secondary-{key}")
    check(payload["zero_cost_reduced_nonincrease"] is True,
          "secondary-zero-cost-monotonicity")


def test_no_historical_caps() -> None:
    text = SOURCE.read_text()
    forbidden = ("PCAP", "10 ** 4", "10**4", "M > 200",
                 "range(0, 41)", "range(0,41)")
    for token in forbidden:
        check(token not in text, f"source-forbids-{token}")


def test_optimized_replay() -> None:
    command = [sys.executable, "-O", str(SOURCE), "--w", "3/2",
               "--M", "2", "--budget", "5"]
    completed = subprocess.run(command, check=False, capture_output=True,
                               text=True, timeout=30)
    check(completed.returncode == 0, "optimized-returncode")
    payload = json.loads(completed.stdout)
    check(payload["state_table_sha256"] ==
          "c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad",
          "optimized-state-hash")
    check(payload["state_count"] == 69, "optimized-state-count")


def main() -> int:
    test_divisors()
    test_pure_epsilon_congruences()
    test_derived_lex_bounds()
    test_charged_closure()
    test_predecessors_are_minimal()
    test_secondary_lex_regression()
    test_no_historical_caps()
    test_optimized_replay()
    print(f"FINITE_CHAIN_SKELETON_R2_TEST_PASS checks={CHECKS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
