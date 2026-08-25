#!/usr/bin/env python3
"""Standalone exact controls for the Stage-B ``C[x]`` membership test.

This harness needs no Stage-A section certificate.  It runs only on a
registered Amazon EC2 lane and tests the exact criterion used by
``stage_b_taylor.py`` for ``x=s/(s-1)``.  It emits deterministic JSON whose
control digest excludes only the run tag.
"""

from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import platform


class MembershipControlFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor_path = Path("/sys/class/dmi/id/sys_vendor")
    vendor = vendor_path.read_text().strip() if vendor_path.is_file() else ""
    if vendor != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def run_controls(tag: str) -> dict[str, object]:
    # Import SymPy only after the EC2/tag guard has passed.  The registered
    # AWS interpreter supplies SymPy 1.13.3; every Poly below has domain QQ.
    import sympy  # type: ignore
    from sympy import Poly, QQ, cancel, div, fraction, symbols  # type: ignore

    if sympy.__version__ != "1.13.3":
        raise SystemExit("REFUSE_UNPINNED_SYMPY")
    s = symbols("s")
    x = cancel(s / (s - 1))

    def poly_string(value: Poly) -> str:
        return str(value.as_expr())

    def inspect(label: str, value, expected_member: bool) -> dict[str, object]:
        value = cancel(value)
        numerator_expression, denominator_expression = fraction(value)
        numerator = Poly(numerator_expression, s, domain=QQ)
        denominator = Poly(denominator_expression, s, domain=QQ)
        if denominator.is_zero:
            raise MembershipControlFailure((label, "zero denominator"))

        leading = denominator.LC()
        numerator = Poly(numerator.as_expr() / leading, s, domain=QQ)
        denominator = Poly(denominator.as_expr() / leading, s, domain=QQ)
        normalized_numerator = numerator
        normalized_denominator = denominator

        s_minus_one = Poly(s - 1, s, domain=QQ)
        pole_order = 0
        while denominator.eval(1) == 0:
            next_denominator, remainder = div(
                denominator, s_minus_one, domain=QQ
            )
            if not remainder.is_zero:
                raise MembershipControlFailure((label, "s=1 division failed"))
            denominator = next_denominator
            pole_order += 1

        quotient, remainder = div(numerator, denominator, domain=QQ)
        quotient_zero = quotient.is_zero
        # This branch is load-bearing: SymPy represents degree(0) by
        # -Infinity, which must never be coerced to an integer or range bound.
        quotient_degree = None if quotient_zero else int(quotient.degree())

        remainder_obstructions = [] if remainder.is_zero else [
            {"degree": degree, "coefficient": str(remainder.nth(degree))}
            for degree in range(int(remainder.degree()) + 1)
            if remainder.nth(degree) != 0
        ]
        degree_obstructions = []
        if not quotient_zero and quotient_degree is not None:
            degree_obstructions = [
                {"degree": degree, "coefficient": str(quotient.nth(degree))}
                for degree in range(pole_order + 1, quotient_degree + 1)
                if quotient.nth(degree) != 0
            ]

        actual_member = not remainder_obstructions and not degree_obstructions
        if actual_member != expected_member:
            raise MembershipControlFailure((
                label, "unexpected membership result", actual_member,
                expected_member,
            ))
        return {
            "label": label,
            "input": str(value),
            "normalized_numerator": poly_string(normalized_numerator),
            "normalized_denominator": poly_string(normalized_denominator),
            "denominator_away_from_s1": poly_string(denominator),
            "s1_pole_bound": pole_order,
            "quotient": poly_string(quotient),
            "quotient_zero": quotient_zero,
            "quotient_degree": quotient_degree,
            "remainder": poly_string(remainder),
            "remainder_obstructions": remainder_obstructions,
            "degree_obstructions": degree_obstructions,
            "expected_member": expected_member,
            "actual_member": actual_member,
            "pass": True,
        }

    controls = [
        inspect(
            "positive_polynomial_in_x",
            1 + 2 * x + 3 * x**2,
            True,
        ),
        inspect("positive_zero", 0, True),
        inspect(
            "negative_pole_away_from_s1",
            1 / (s + 1),
            False,
        ),
        inspect(
            "negative_degree_exceeds_s1_pole_bound",
            s**2 / (s - 1),
            False,
        ),
    ]
    digest_payload = {
        "schema": "d1_stage_b_membership_controls_v1",
        "criterion": (
            "remove (s-1)^B from D; require D_other|N and "
            "deg(N/D_other)<=B; handle zero quotient separately"
        ),
        "controls": controls,
    }
    canonical = json.dumps(
        digest_payload, sort_keys=True, separators=(",", ":")
    )
    return {
        **digest_payload,
        "aws_tag": tag,
        "control_sha256": sha256(canonical.encode()).hexdigest(),
        "status": "PASS-EXACT-CX-MEMBERSHIP-CONTROLS",
        "scope": "synthetic Stage-B membership controls only; no Stage-A section",
    }


def main() -> None:
    tag = require_aws()
    payload = run_controls(tag)
    print(json.dumps(payload, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
