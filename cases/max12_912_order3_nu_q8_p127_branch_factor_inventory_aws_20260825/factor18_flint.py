#!/usr/bin/env python3
"""Independent FLINT certificate for the degree-1243 branch factor.

This deliberately does not consume the Singular factor-test output.  It reads
the pinned factor inventory and candidate H, constructs
E = F_127[a]/(q_18), and computes gcd(H,H_v,H_w) in E[v].
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re

from flint import fmpz_mod_poly_ctx, fq_default_ctx, fq_default_poly_ctx, nmod_poly


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent
INVENTORY = CASE / "aws_r6d_v1/result.out"
INVENTORY_SHA256 = "c1f120d7b98d814a56da3e3886efef5f19a522baba513fa930b7e6c44f87507b"
CANDIDATE = ROOT / (
    "cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/"
    "interpolation_candidate.json"
)
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
P = 127


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def factor18_text() -> str:
    if digest(INVENTORY) != INVENTORY_SHA256:
        raise RuntimeError("inventory hash mismatch")
    text = INVENTORY.read_text()
    match = re.search(
        r"^factor_index=18\nfactor_degree=1243\n([^\n]+)$", text, re.MULTILINE
    )
    if match is None:
        raise RuntimeError("factor 18 not found uniquely")
    return match.group(1)


def parse_singular_univariate(text: str) -> list[int]:
    """Parse Singular's compact form `w1243-49w1242+...-16`."""
    terms = re.findall(r"[+-]?[^+-]+", text)
    coefficients: dict[int, int] = {}
    for term in terms:
        match = re.fullmatch(r"([+-]?)(\d*)w(\d*)", term)
        if match is not None:
            sign, raw_coefficient, raw_degree = match.groups()
            coefficient = int(raw_coefficient) if raw_coefficient else 1
            degree = int(raw_degree) if raw_degree else 1
        else:
            match = re.fullmatch(r"([+-]?)(\d+)", term)
            if match is None:
                raise RuntimeError(("unparsed term", term))
            sign, raw_coefficient = match.groups()
            coefficient = int(raw_coefficient)
            degree = 0
        if sign == "-":
            coefficient = -coefficient
        if degree in coefficients:
            raise RuntimeError(("duplicate degree", degree))
        coefficients[degree] = coefficient % P
    if max(coefficients) != 1243 or coefficients[1243] != 1:
        raise RuntimeError((max(coefficients), coefficients.get(1243)))
    return [coefficients.get(degree, 0) for degree in range(1244)]


def main() -> None:
    if digest(CANDIDATE) != CANDIDATE_SHA256:
        raise RuntimeError("candidate hash mismatch")
    payload = json.loads(CANDIDATE.read_text())
    if payload.get("status") != "PASS" or payload.get("degree_v") != 190:
        raise RuntimeError("candidate endpoint mismatch")

    factor_text = factor18_text()
    factor_sha = sha256((factor_text + "\n").encode()).hexdigest()
    factor_coefficients = parse_singular_univariate(factor_text)
    q = nmod_poly(factor_coefficients, P)
    factor_unit, factorization = q.factor()
    irreducible = (
        len(factorization) == 1
        and factorization[0][1] == 1
        and factorization[0][0] == q
    )
    if q.degree() != 1243 or q.leading_coefficient() != 1 or not irreducible:
        raise RuntimeError(
            ("bad factor", q.degree(), q.leading_coefficient(), factor_unit, factorization)
        )

    modulus_ring = fmpz_mod_poly_ctx(P)
    field = fq_default_ctx(
        modulus=modulus_ring(factor_coefficients), var="a", fq_type="FQ_NMOD"
    )
    poly_ring = fq_default_poly_ctx(field)
    powers = [field.one()]
    a = field.gen()
    for _ in range(21):
        powers.append(powers[-1] * a)

    h_coefficients = [field.zero() for _ in range(191)]
    hv_coefficients = [field.zero() for _ in range(190)]
    hw_coefficients = [field.zero() for _ in range(191)]
    for raw_v_degree, entries in payload["nonzero_support"].items():
        v_degree = int(raw_v_degree)
        for w_degree, coefficient in entries:
            coefficient %= P
            h_coefficients[v_degree] += coefficient * powers[w_degree]
            if v_degree:
                hv_coefficients[v_degree - 1] += (
                    coefficient * v_degree % P
                ) * powers[w_degree]
            if w_degree:
                hw_coefficients[v_degree] += (
                    coefficient * w_degree % P
                ) * powers[w_degree - 1]

    h = poly_ring(h_coefficients)
    hv = poly_ring(hv_coefficients)
    hw = poly_ring(hw_coefficients)
    if h.degree() != 190 or hv.degree() != 189 or hw.degree() > 190:
        raise RuntimeError(("degree check", h.degree(), hv.degree(), hw.degree()))
    g2 = h.gcd(hv)
    g3 = g2.gcd(hw)

    print("Q8-P127-BRANCH-FACTOR18-FLINT")
    print(f"inventory_sha256={INVENTORY_SHA256}")
    print(f"candidate_sha256={CANDIDATE_SHA256}")
    print(f"factor_text_sha256={factor_sha}")
    print(f"factor_degree={q.degree()}")
    print(f"factor_irreducible={int(irreducible)}")
    print(f"degree_H={h.degree()}")
    print(f"degree_Hv={hv.degree()}")
    print(f"degree_Hw={hw.degree()}")
    print(f"ramification_gcd_degree={g2.degree()}")
    print(f"singular_gcd_degree={g3.degree()}")
    print(f"nonsingular_branch_factor={int(g3.degree() == 0)}")
    print("factor18_flint_end")
    if g3.degree() != 0:
        raise SystemExit(92)


if __name__ == "__main__":
    main()
