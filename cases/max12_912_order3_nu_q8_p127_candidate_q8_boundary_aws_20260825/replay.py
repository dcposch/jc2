#!/usr/bin/env python3
"""Exact F_127 boundary divisibility check for the Q8 candidate H(w,v)."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / (
    "cases/max12_912_order3_nu_q8_p127_eliminant_interpolation_aws_20260825/"
    "aws/p127-eliminant-interpolation-root-v6/result.json"
)
CANDIDATE_SHA256 = (
    "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
)
P = 127

# Low-to-high coefficients of the sign-normalized corrected Q8 over Z.
Q8_Z = [-24, -296, -1548, -4428, -7320, -6498, -1782, 1539, 999]


def trim(f: list[int]) -> list[int]:
    f = [value % P for value in f]
    while len(f) > 1 and f[-1] == 0:
        f.pop()
    return f


def monic(f: list[int]) -> list[int]:
    f = trim(f)
    if f == [0]:
        return f
    scale = pow(f[-1], -1, P)
    return trim([scale * value for value in f])


def divmod_poly(f: list[int], g: list[int]) -> tuple[list[int], list[int]]:
    f = trim(f)
    g = trim(g)
    if g == [0]:
        raise ZeroDivisionError
    if len(f) < len(g):
        return [0], f
    quotient = [0] * (len(f) - len(g) + 1)
    lead_inverse = pow(g[-1], -1, P)
    while f != [0] and len(f) >= len(g):
        shift = len(f) - len(g)
        coefficient = f[-1] * lead_inverse % P
        quotient[shift] = coefficient
        for index, value in enumerate(g):
            f[index + shift] = (f[index + shift] - coefficient * value) % P
        f = trim(f)
    return trim(quotient), f


def gcd_poly(f: list[int], g: list[int]) -> list[int]:
    f = trim(f)
    g = trim(g)
    while g != [0]:
        _, remainder = divmod_poly(f, g)
        f, g = g, remainder
    return monic(f)


def derivative(f: list[int]) -> list[int]:
    if len(f) <= 1:
        return [0]
    return trim([index * f[index] for index in range(1, len(f))])


def dense_sha256(f: list[int]) -> str:
    payload = json.dumps(trim(f), separators=(",", ":")).encode()
    return sha256(payload).hexdigest()


def main() -> None:
    got = sha256(CANDIDATE.read_bytes()).hexdigest()
    if got != CANDIDATE_SHA256:
        raise RuntimeError((str(CANDIDATE), got, CANDIDATE_SHA256))
    candidate = json.loads(CANDIDATE.read_text())
    if candidate["status"] != "PASS" or candidate["prime"] != P:
        raise RuntimeError("candidate metadata mismatch")

    support = candidate["nonzero_support"]
    h0 = [0] * (candidate["degree_v"] + 1)
    maximum_w_degree = 0
    for v_degree in range(candidate["degree_v"] + 1):
        seen_w_degrees: set[int] = set()
        for w_degree, coefficient in support[str(v_degree)]:
            if w_degree in seen_w_degrees:
                raise RuntimeError(("duplicate support", v_degree, w_degree))
            seen_w_degrees.add(w_degree)
            maximum_w_degree = max(maximum_w_degree, w_degree)
            if w_degree == 0:
                h0[v_degree] = coefficient % P

    h0 = trim(h0)
    q8 = monic(Q8_Z)
    quotient, remainder = divmod_poly(h0, q8)
    second_quotient, second_remainder = divmod_poly(quotient, q8)
    q8_squarefree_gcd = gcd_poly(q8, derivative(q8))
    cofactor_gcd = gcd_poly(q8, quotient)
    hv_remainder = divmod_poly(derivative(h0), q8)[1]
    hv_gcd = gcd_poly(q8, hv_remainder)

    checks = {
        "candidate_v_degree_190": len(h0) - 1 == 190,
        "candidate_w_degree_21": maximum_w_degree == 21,
        "q8_degree_8": len(q8) - 1 == 8,
        "q8_squarefree": q8_squarefree_gcd == [1],
        "q8_divides_h0": remainder == [0],
        "q8_does_not_divide_h0_twice": second_remainder != [0],
        "q8_cofactor_coprime": cofactor_gcd == [1],
        "v_derivative_unit_at_q8": hv_gcd == [1],
    }
    if not all(checks.values()):
        raise RuntimeError(checks)

    result = {
        "case": "max12_912_order3_nu_q8_p127_candidate_q8_boundary_aws_20260825",
        "status": "PASS",
        "prime": P,
        "candidate_sha256": got,
        "candidate_v_degree": len(h0) - 1,
        "candidate_w_degree": maximum_w_degree,
        "h0_dense_sha256": dense_sha256(h0),
        "q8_monic_coefficients_low_to_high": q8,
        "q8_cofactor_degree": len(quotient) - 1,
        "q8_cofactor_dense_sha256": dense_sha256(quotient),
        "second_division_remainder_degree": len(second_remainder) - 1,
        "v_derivative_mod_q8_coefficients_low_to_high": hv_remainder,
        "checks": checks,
        "scope": (
            "exact (w,v)-projection boundary statement only; no generic ideal "
            "membership, lifted component, coordinate-limit, trajectory, max12, "
            "or JC2 conclusion"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

