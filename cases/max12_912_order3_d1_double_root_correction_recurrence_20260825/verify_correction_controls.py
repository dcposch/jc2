#!/usr/bin/env python3
"""AWS-only exact replay of two correction-enabled double-root controls.

The replay consumes the independent ordinary tail dictionaries directly.  It
evaluates them in truncated Q[[t]] after substituting K0^3+K0*Q+R.  No
binomial-layer formula is used by the computation being checked.
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
SOURCE = (
    ROOT / "cases" /
    "max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825" /
    "independent_reconstruct.py"
)
SOURCE_SHA256 = (
    "67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623"
)


class CorrectionControlFailure(RuntimeError):
    pass


def require_aws() -> str:
    if platform.system() != "Linux":
        raise SystemExit("REFUSE_NON_LINUX")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        raise SystemExit("REFUSE_NON_AWS_EC2")
    tag = os.environ.get("JC2_AWS_TAG", "")
    if not tag.startswith("max12_912_order3_d1_double_root_correction_"):
        raise SystemExit("REFUSE_UNREGISTERED_AWS_TAG")
    return tag


def load_source():
    got = sha256(SOURCE.read_bytes()).hexdigest()
    if got != SOURCE_SHA256:
        raise CorrectionControlFailure(("source hash", got, SOURCE_SHA256))
    spec = importlib.util.spec_from_file_location(
        "d1_double_root_correction_source", SOURCE
    )
    if spec is None or spec.loader is None:
        raise CorrectionControlFailure("cannot load source")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def clean(series):
    return {exponent: coefficient for exponent, coefficient in series.items()
            if coefficient}


def add(left, right):
    out = dict(left)
    for exponent, coefficient in right.items():
        out[exponent] = out.get(exponent, Fraction(0)) + coefficient
    return clean(out)


def scale(scalar, series):
    scalar = Fraction(scalar)
    return clean({exponent: scalar * coefficient
                  for exponent, coefficient in series.items()})


def multiply(left, right, cutoff):
    out = {}
    for le, lv in left.items():
        for re, rv in right.items():
            exponent = le + re
            if exponent > cutoff:
                continue
            out[exponent] = out.get(exponent, Fraction(0)) + lv * rv
    return clean(out)


def power(series, exponent, cutoff):
    out = {0: Fraction(1)}
    for _ in range(exponent):
        out = multiply(out, series, cutoff)
    return out


def atom(exponent, coefficient=1):
    coefficient = Fraction(coefficient)
    return {} if not coefficient else {exponent: coefficient}


def coefficient_images(q, r):
    """a0,...,a7,kbar for K0^3+K0*Q+R, K0=z^3-3z+2."""
    q2, q1, q0 = q
    r2, r1, r0 = r
    return (
        add(add(atom(0, 8), scale(2, q0)), r0),
        add(add(add(atom(0, -36), scale(-3, q0)), scale(2, q1)), r1),
        add(add(add(atom(0, 54), scale(-3, q1)), scale(2, q2)), r2),
        add(add(atom(0, -15), q0), scale(-3, q2)),
        add(atom(0, -36), q1),
        add(atom(0, 27), q2),
        atom(0, 6),
        atom(0, -9),
        {},
    )


def evaluate(source_poly, images, cutoff):
    table = []
    maxima = [0] * len(images)
    for source_monomial in source_poly:
        for index, exponent in enumerate(source_monomial):
            maxima[index] = max(maxima[index], exponent)
    for image, maximum in zip(images, maxima):
        table.append([power(image, exponent, cutoff)
                      for exponent in range(maximum + 1)])
    out = {}
    for source_monomial, scalar in source_poly.items():
        term = atom(0, scalar)
        for index, exponent in enumerate(source_monomial):
            term = multiply(term, table[index][exponent], cutoff)
        out = add(out, term)
    return clean(out)


def evaluate_all(tails, q, r, cutoff):
    images = coefficient_images(q, r)
    return {ell: evaluate(tails[ell], images, cutoff)
            for ell in range(1, 9)}


def digest(rows):
    serial = {
        str(ell): [[exponent, coefficient.numerator, coefficient.denominator]
                   for exponent, coefficient in sorted(row.items())]
        for ell, row in rows.items()
    }
    encoded = json.dumps(serial, sort_keys=True, separators=(",", ":"))
    return sha256(encoded.encode()).hexdigest()


def require_zero_through(rows, cutoff, label):
    bad = {ell: {e: q for e, q in row.items() if e <= cutoff}
           for ell, row in rows.items()}
    bad = {ell: row for ell, row in bad.items() if row}
    if bad:
        raise CorrectionControlFailure((label, bad))


def main() -> None:
    tag = require_aws()
    source = load_source()
    tails = source.build()["tails"]

    # Lambda=t^4, tau=t gives a strict slope.  Normalized beta=4,alpha=7.
    # Q=t^16*N; R=t^28*L+t^32*U/9.
    q_a = (atom(16), atom(16), atom(16, -2))
    r_a = (
        {},
        add(atom(28), atom(32, Fraction(1, 9))),
        add(atom(28, -1), atom(32, Fraction(2, 9))),
    )
    rows_a = evaluate_all(tails, q_a, r_a, 48)
    require_zero_through(rows_a, 48, "non-target correction did not cancel")

    r_a_wrong = ({}, atom(28), atom(28, -1))
    wrong_a = evaluate_all(tails, q_a, r_a_wrong, 48)
    if not any(row.get(48) for row in wrong_a.values()):
        raise CorrectionControlFailure("omitted U/9 correction negative control")

    # Normalized beta=11/2,alpha=15/2.  Q=t^22*L;
    # R=t^30*N-(1/2)t^38.  The weight-15 target is t^60.
    q_b = ({}, atom(22), atom(22, -1))
    r_b = (
        atom(30),
        atom(30),
        add(atom(30, -2), atom(38, Fraction(-1, 2))),
    )
    rows_b = evaluate_all(tails, q_b, r_b, 60)
    for ell, row in rows_b.items():
        for exponent, coefficient in row.items():
            if exponent < 60 and coefficient:
                raise CorrectionControlFailure(
                    ("target control early tail", ell, exponent, coefficient)
                )
    expected = {ell: Fraction(2, 3) if ell == 3 else Fraction(0)
                for ell in range(1, 9)}
    got = {ell: rows_b[ell].get(60, Fraction(0)) for ell in range(1, 9)}
    if got != expected:
        raise CorrectionControlFailure(("weight-15 target", got, expected))

    r_b_wrong = (atom(30), atom(30), atom(30, -2))
    wrong_b = evaluate_all(tails, q_b, r_b_wrong, 60)
    wrong_pattern = {
        ell: wrong_b[ell].get(60, Fraction(0)) for ell in range(1, 9)
    }
    if wrong_pattern == expected:
        raise CorrectionControlFailure("omitted -1/2 correction control")

    payload = {
        "aws_tag": tag,
        "charged_source_sha256": SOURCE_SHA256,
        "strict_slope": "Lambda=t^4,tau=t,rho=t",
        "control_1": {
            "normalized_beta": "4",
            "normalized_alpha": "7",
            "Q": "t^16*(z-1)*(z+2)",
            "R": "t^28*(z-1)+t^32*(z+2)/9",
            "tails_through_t48": "all zero",
            "row_digest": digest(rows_a),
            "omitted_correction_has_nonzero_t48": True,
        },
        "control_2": {
            "normalized_beta": "11/2",
            "normalized_alpha": "15/2",
            "Q": "t^22*(z-1)",
            "R": "t^30*(z-1)*(z+2)-t^38/2",
            "tails_below_t60": "all zero",
            "tails_at_t60": {str(ell): str(got[ell])
                              for ell in range(1, 9)},
            "row_digest": digest(rows_b),
            "omitted_correction_changes_t60_pattern": True,
        },
        "firewall": (
            "finite successors only; no formal lift and no complete fan"
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")
    print("PASS_D1_DOUBLE_ROOT_CORRECTION_CONTROLS")


if __name__ == "__main__":
    main()
