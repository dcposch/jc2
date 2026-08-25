#!/usr/bin/env python3
"""AWS-only exact controls for the squarefree order-20 obstruction.

Controls:
1. the K^-2 numerator-to-tail map is lower triangular with unit diagonal;
2. z/K^3 has first nonzero tail r8, so excluding K^-3 through weight 20
   is genuinely load-bearing;
3. a nonirrelevant double-root cubic admits an explicitly hidden lower
   normal term, so the Delta=0 firewall is necessary;
4. direct weight enumeration shows that K^-3 first occurs at weight 21.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = (ROOT / "cases" /
          "max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825" /
          "independent_reconstruct.py")
SOURCE_SHA256 = "67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623"


class FirewallControlFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_firewall_controls_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_source():
    got = sha256(SOURCE.read_bytes()).hexdigest()
    if got != SOURCE_SHA256:
        raise FirewallControlFailure(("source hash", got, SOURCE_SHA256))
    spec = importlib.util.spec_from_file_location("d1_firewall_control_source", SOURCE)
    if spec is None or spec.loader is None:
        raise FirewallControlFailure("cannot load source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def pclean(value):
    return {degree: coefficient for degree, coefficient in value.items()
            if coefficient}


def padd(left, right):
    out = dict(left)
    for degree, coefficient in right.items():
        out[degree] = out.get(degree, Fraction(0)) + coefficient
    return pclean(out)


def pscale(scalar, value):
    scalar = Fraction(scalar)
    return pclean({degree: scalar * coefficient
                   for degree, coefficient in value.items()})


def pmul(left, right):
    out = {}
    for ld, lv in left.items():
        for rd, rv in right.items():
            out[ld + rd] = out.get(ld + rd, Fraction(0)) + lv * rv
    return pclean(out)


def ppow(value, exponent):
    out = {0: Fraction(1)}
    for _ in range(exponent):
        out = pmul(out, value)
    return out


def double_root_control():
    z_minus_one = {1: Fraction(1), 0: Fraction(-1)}
    z_plus_two = {1: Fraction(1), 0: Fraction(2)}
    K = pmul(ppow(z_minus_one, 2), z_plus_two)
    Q = pmul(z_minus_one, z_plus_two)
    R = {0: Fraction(1, 3)}
    hidden = pmul(Q, padd(pscale(9, pmul(R, K)), pscale(-1, ppow(Q, 2))))
    expected = pscale(-1, ppow(K, 2))
    if hidden != expected:
        raise FirewallControlFailure(("double-root hidden term", hidden, expected))
    if K != {3: Fraction(1), 1: Fraction(-3), 0: Fraction(2)}:
        raise FirewallControlFailure(("double-root K", K))
    p, c = Fraction(-3), Fraction(2)
    discriminant = -4 * p ** 3 - 27 * c ** 2
    if discriminant != 0 or (p == 0 and c == 0):
        raise FirewallControlFailure("double-root discriminant control")
    return {
        "K": "(z-1)^2*(z+2)=z^3-3z+2",
        "Q": "(z-1)*(z+2)",
        "R": "1/3",
        "identity": "Q*(9*R*K-Q^2)=-K^2",
        "Delta": 0,
        "projectively_nonirrelevant": True,
    }


def tail_profile_controls(source):
    ring = source.Ring(("a0", "a1"))
    inverse = source.inverse_root_by_cancellation(ring, 12, m=3)
    one = ring.one
    matrix = []
    # Columns z^5,...,1 over K^2=w^6; rows r1,...,r6.
    for ell in range(1, 7):
        row = []
        for degree in range(5, -1, -1):
            row.append(source.coefficient_of_power(
                inverse, degree, 6 - ell, one
            ))
        matrix.append(row)
    for row in range(6):
        for column in range(6):
            if column > row and matrix[row][column]:
                raise FirewallControlFailure(("profile above diagonal", row, column))
            if column == row and matrix[row][column] != one:
                raise FirewallControlFailure(("profile diagonal", row, column,
                                              matrix[row][column]))

    # z/K^3=z_0(w)/w^9 starts with w^-8 and no earlier tail.
    sharp = []
    for ell in range(1, 9):
        sharp.append(source.coefficient_of_power(inverse, 1, 9 - ell, one))
    if any(sharp[index] for index in range(7)) or sharp[7] != one:
        raise FirewallControlFailure(("K^-3 sharpness", sharp))
    return {
        "K_minus_2_first_six_matrix_lower_triangular": True,
        "K_minus_2_diagonal": ["1"] * 6,
        "K_minus_3_sharp_control": "z/K^3 has r1=...=r7=0,r8=1",
        "inverse_root_sha256": source.laurent_digest(inverse),
    }


def weight_cutoff_control():
    terms = []
    # F12: K^(4-2j-r) Q^(j-r) R^r.
    for j in range(2, 8):
        for r_count in range(j + 1):
            denominator_power = max(0, 2 * j + r_count - 4)
            weight = 6 * (j - r_count) + 9 * r_count
            if denominator_power:
                terms.append(("F12", j, r_count, denominator_power, weight))
    # kbar*F6: K^(2-2j-r) Q^(j-r) R^r, plus weight six.
    for j in range(1, 8):
        for r_count in range(j + 1):
            denominator_power = max(0, 2 * j + r_count - 2)
            weight = 6 + 6 * (j - r_count) + 9 * r_count
            if denominator_power:
                terms.append(("kF6", j, r_count, denominator_power, weight))
    through20 = sorted(term for term in terms if term[4] <= 20)
    expected = sorted([
        ("F12", 2, 1, 1, 15),
        ("F12", 2, 2, 2, 18),
        ("F12", 3, 0, 2, 18),
        ("kF6", 1, 1, 1, 15),
        ("kF6", 2, 0, 2, 18),
    ])
    if through20 != expected:
        raise FirewallControlFailure(("terms through 20", through20, expected))
    later = [term for term in terms if term[4] > 20]
    next_weight = min(term[4] for term in later)
    next_terms = sorted(term for term in later if term[4] == next_weight)
    if next_weight != 21 or not all(term[3] >= 3 for term in next_terms):
        raise FirewallControlFailure(("next denominator layer", next_weight,
                                      next_terms))
    return {
        "negative_terms_through_weight_20": through20,
        "next_negative_weight": next_weight,
        "next_negative_terms": next_terms,
        "all_next_denominator_powers_at_least_3": True,
    }


def main() -> None:
    tag = require_aws()
    source = load_source()
    payload = {
        "aws_tag": tag,
        "source_sha256": SOURCE_SHA256,
        "tail_profile_controls": tail_profile_controls(source),
        "double_root_negative_control": double_root_control(),
        "weight_cutoff_control": weight_cutoff_control(),
        "scope": (
            "exact controls for the squarefree order-20 theorem only; "
            "the double-root identity is a negative control, not an arc"
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-D1-SQUAREFREE-ORDER20-FIREWALL-CONTROLS")
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
