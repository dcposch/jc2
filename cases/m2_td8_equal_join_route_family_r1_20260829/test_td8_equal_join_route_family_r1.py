#!/usr/bin/env python3
"""Hostile bounded tests for the td=8 equal-join affine route family."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "td8_equal_join_route_family_r1.py"


def load_module():
    spec = importlib.util.spec_from_file_location("td8_equal_join_route_r1",
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


def test_fixed_step() -> None:
    a = M.validate_A_step()
    check(a["shape"]["dp"] == 21 and a["shape"]["dq"] == 15,
          "A-degrees")
    check(a["frame"] == {"nu": 7, "kbar": "5", "X": "7",
                         "rho": "1/3", "w": "2/3", "M": 3},
          "A-frame")
    check(a["lambda_lower_bound"] == 2, "A-price")


def test_family_large_box() -> None:
    for t in range(0, 10001):
        r = M.validate_route(t)
        g = r["merge"]
        check(g["nu_G"] == 4 + 3 * t, f"nu-{t}")
        check(g["M"] == 3, f"M-{t}")
        check(g["kbar"] == 6 + 4 * t, f"kbar-{t}")
        check(g["incoming_edge_label_each"] == 37 + 28 * t,
              f"incoming-label-{t}")
        check(r["trunk"]["parent_edge_label"] == 22 + 17 * t,
              f"trunk-label-{t}")
        check(r["terminal"] == {"w": "2/5", "M": 5,
                                "j": 3, "psi": 1}, f"terminal-{t}")
        check(r["lambda_lower_bound_total"] ==
              r["lambda_budget_ceiling"] == 6,
              f"budget-{t}")
        check(r["recorded_budget_fit_at_equality"] is True,
              f"budget-equality-{t}")


def test_progression_mutations() -> None:
    # The neighboring congruence classes cannot carry integral kbar.
    for nu in range(2, 80):
        kb = Fraction(2, 3) * (2 * nu + 1)
        legal = kb.denominator == 1
        check(legal == (nu % 3 == 1), f"integrality-class-{nu}")
    # The family really has infinitely many distinct full cells despite its
    # constant reduced successor.
    rows = [M.validate_route(t)["merge"] for t in range(40)]
    check(len({(r["dp"], r["dq"], r["kbar"]) for r in rows}) == 40,
          "distinct-full-cells")
    check({(r["w_tr"], r["M"]) for r in rows} == {("4/3", 3)},
          "single-reduced-successor")


def test_certificate_and_optimized() -> None:
    p = M.family_certificate()
    costs = p["fixed_recorded_lambda_lower_bounds"]
    check(costs["total"] == costs["td8_budget_ceiling"],
          "certificate-exact-budget")
    check(p["firewall"]["prop_8_1_iv_solved"] is False,
          "equation-firewall")
    check(p["firewall"]["jc2"] is False, "jc2-firewall")
    cp = subprocess.run([sys.executable, "-O", str(SOURCE)], check=False,
                        capture_output=True, text=True, timeout=20)
    check(cp.returncode == 0, "optimized-returncode")
    q = json.loads(cp.stdout)
    check(q["certificate_sha256"] == p["certificate_sha256"],
          "optimized-certificate")


def test_invalid_parameter() -> None:
    bad = 0
    for t in (-1, Fraction(1, 2), "0"):
        try:
            M.validate_route(t)
        except ValueError:
            bad += 1
    check(bad == 3, "invalid-t-refusal")


def main() -> int:
    test_fixed_step()
    test_family_large_box()
    test_progression_mutations()
    test_certificate_and_optimized()
    test_invalid_parameter()
    print(f"TD8_EQUAL_JOIN_ROUTE_FAMILY_R1_TEST_PASS checks={CHECKS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
