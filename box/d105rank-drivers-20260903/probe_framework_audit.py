#!/usr/bin/env python3
"""Bounded audit probe for the sealed GLOBAL-INTERPOLATION driver.

This is deliberately not a D=105 rank driver.  It verifies the frozen inputs,
runs the sealed checks, derives the three level paths, and demonstrates two
interface limits which a real D=105 driver must repair:

* ``verified`` orbit metadata is trusted rather than checked; and
* the all-branch quadratic lift is too large for the requested first-order
  experiment, even in an artificially cheap valuation pattern.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import math
import sys
from fractions import Fraction
from pathlib import Path


INPUT = Path("/tmp/jc2-lane.syVtTr/inputs")
EXPECTED = {
    "global-interpolation-sol56-20260902.md": "20d554a0b19c563093ec35caad58664f800d7517490f530a07f511d7042393b6",
    "globalinterp.py": "49ba5a019714e30a952c998fb39a88aff38505a80fcac6df3c5883bb16599588",
    "census-rebase-opus5-20260902.md": "fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948",
    "survivors-D48-120.txt": "47f59906927ff9d2b38b25b11c2e46cef3c472b3d8db300f12c12f22906848e1",
    "ideation-20260903T1015Z-gpt55.md": "5e1646f507e946b831dcb77d542f7ab367eb398227a3032b96bcd7a45d2f320d",
    "time-function-endgame-review-sol56-20260902.md": "9e485492940818ea25b955af1713de53bc823af78f9f00a8991aaba9372f527d",
    "bottomode.py": "69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473",
    "moh_skeleton_full.py": "d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2",
}


def hash_gate() -> None:
    for name, wanted in EXPECTED.items():
        got = hashlib.sha256((INPUT / name).read_bytes()).hexdigest()
        if got != wanted:
            raise SystemExit(f"HASH MISMATCH {name}: {got} != {wanted}")
    print(f"hash_gate=PASS files={len(EXPECTED)}")


def load_framework():
    path = INPUT / "globalinterp.py"
    spec = importlib.util.spec_from_file_location("sealed_globalinterp_probe", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def group_rows() -> None:
    raw = [
        ("A", 28, 5, Fraction(7, 12), Fraction(7, 18), 25),
        ("B", 28, 6, Fraction(11, 26), Fraction(2, 13), 30),
        ("C", 40, 4, Fraction(19, 34), Fraction(4, 17), 28),
    ]
    for label, m2, v3, delta1, delta2, u in raw:
        d3 = math.gcd(35, m2)
        dchain = (105, 35, d3, 1)
        rmin = math.lcm(delta1.denominator, delta2.denominator)
        j2 = delta1 - delta2
        # Moh's A_1 uses L_1=lcm(den(delta_2),den(delta_3)); delta_3=-1.
        a1 = (delta2.denominator * delta1).denominator
        a2 = delta2.denominator
        q_outer = v3 * 35 // d3
        triangle, square = divmod(q_outer, a2)
        branch10 = 1 <= triangle
        branch11 = (1 - square) % a2 == 0
        print(
            "group=%s dchain=%s delta=(%s,%s,-1) Rmin=%d J2_t=%s J2_z=%s "
            "A1=%d A2=%d Q=%d=u divmod=(%d,%d) branch10=%s branch11=%s "
            "cover_factor_orbit=%d displayed_leading_label_cycles_if_extra_closure=(%d,%d)"
            % (
                label,
                dchain,
                delta1,
                delta2,
                rmin,
                j2,
                rmin * j2,
                a1,
                a2,
                q_outer,
                triangle,
                square,
                branch10,
                branch11,
                a2,
                a2,
                2 * a2,
            )
        )


def trusted_orbit_probe(gi) -> None:
    data = copy.deepcopy(gi.example_config())
    # For x=z^-2, equivariance would send I*z^-1 to -I*z^-1.  Deliberately
    # replace the alleged conjugate by -2I*z^-1 while retaining verified=true.
    data["branches"][1]["terms"]["-1"] = "-2*I"
    result = gi.GlobalInterpolationSystem(data).result(rank_method="none")
    print(
        "trusted_orbit_probe=ACCEPTED effective_no_log=%d orbit_constants=%d "
        "leading_difference=%s"
        % (
            result["direct_conditions"]["no_log"]["effective_over_base_field"],
            result["direct_conditions"]["integration_constants"][
                "variables_after_verified_orbit_descent"
            ],
            result["contacts"]["plus,minus"]["leading_difference"],
        )
    )


def lift_size_probe() -> None:
    n, m = 105, 70
    products = n * (n - 1)
    inverses = n
    powers_floor = n * (m - 1)
    # Artificially favorable tau_i=(i+1)z^-1, L=1, qmax=0.  The current
    # desired_power recurrence requests m+1 coefficients for every power.
    powers_illustrative = n * (m - 1) * (m + 1)
    print(
        "lift_lower_bound products=%d inverses=%d powers_one_each=%d total=%d"
        % (products, inverses, powers_floor, products + inverses + powers_floor)
    )
    print(
        "lift_illustrative_tauval_minus1_L1_qmax0 powers=%d "
        "total_before_time_and_evaluation=%d"
        % (powers_illustrative, products + inverses + powers_illustrative)
    )


def main() -> int:
    hash_gate()
    gi = load_framework()
    checks = gi._selftest(verbose=False)
    print(f"sealed_selftest checks={checks.count} failures={len(checks.failures)}")
    if checks.failures:
        return 1
    group_rows()
    trusted_orbit_probe(gi)
    lift_size_probe()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
