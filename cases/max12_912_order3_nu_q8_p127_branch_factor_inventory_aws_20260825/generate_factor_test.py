#!/usr/bin/env python3
"""Test one discriminant factor for a common zero of H,H_v,H_w."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
INVENTORY = Path(__file__).resolve().parent / "aws_r6d_v1/result.out"
INVENTORY_SHA256 = "c1f120d7b98d814a56da3e3886efef5f19a522baba513fa930b7e6c44f87507b"
CANDIDATE = ROOT / (
    "cases/max12_912_order3_nu_q8_p127_generic_candidate_certificate_aws_20260825/"
    "interpolation_candidate.json"
)
CANDIDATE_SHA256 = "9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce"
P = 127


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def inventory() -> list[tuple[int, str]]:
    if digest(INVENTORY) != INVENTORY_SHA256:
        raise RuntimeError((str(INVENTORY), digest(INVENTORY), INVENTORY_SHA256))
    text = INVENTORY.read_text()
    block = text.split("factors_begin\n", 1)[1].split("factors_end\n", 1)[0]
    lines = block.splitlines()
    result: list[tuple[int, str]] = []
    index = 0
    while index < len(lines):
        match_index = re.fullmatch(r"factor_index=(\d+)", lines[index])
        match_degree = re.fullmatch(r"factor_degree=(\d+)", lines[index + 1])
        if not match_index or not match_degree:
            raise RuntimeError(("factor block", index, lines[index : index + 3]))
        expected_index = len(result) + 1
        if int(match_index.group(1)) != expected_index:
            raise RuntimeError(("factor index", match_index.group(1), expected_index))
        polynomial = lines[index + 2]
        if not polynomial or any(character.isspace() for character in polynomial):
            raise RuntimeError(("factor polynomial", expected_index))
        result.append((int(match_degree.group(1)), polynomial))
        index += 3
    if len(result) != 18 or sum(degree for degree, _ in result) != 1746:
        raise RuntimeError((len(result), sum(degree for degree, _ in result)))
    return result


def monomial(coefficient: int, a_degree: int, v_degree: int) -> str:
    coefficient %= P
    factors: list[str] = []
    if coefficient != 1 or (a_degree == 0 and v_degree == 0):
        factors.append(str(coefficient))
    if a_degree:
        factors.append("a" if a_degree == 1 else f"a^{a_degree}")
    if v_degree:
        factors.append("v" if v_degree == 1 else f"v^{v_degree}")
    return "*".join(factors) if factors else "1"


def polynomial(payload: dict, derivative: str | None = None) -> str:
    terms: list[str] = []
    for raw_v_degree, entries in payload["nonzero_support"].items():
        v_degree = int(raw_v_degree)
        for w_degree, coefficient in entries:
            if derivative == "v":
                if v_degree == 0:
                    continue
                coefficient = coefficient * v_degree
                output_v_degree = v_degree - 1
                output_a_degree = w_degree
            elif derivative == "w":
                if w_degree == 0:
                    continue
                coefficient = coefficient * w_degree
                output_v_degree = v_degree
                output_a_degree = w_degree - 1
            else:
                output_v_degree = v_degree
                output_a_degree = w_degree
            coefficient %= P
            if coefficient:
                terms.append(monomial(coefficient, output_a_degree, output_v_degree))
    return "+".join(terms) or "0"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=int, required=True)
    args = parser.parse_args()
    factors = inventory()
    if not 1 <= args.index <= len(factors):
        raise RuntimeError(args.index)
    factor_degree, factor_w = factors[args.index - 1]
    factor_a = factor_w.replace("w", "a")
    if digest(CANDIDATE) != CANDIDATE_SHA256:
        raise RuntimeError((str(CANDIDATE), digest(CANDIDATE)))
    payload = json.loads(CANDIDATE.read_text())
    if payload.get("status") != "PASS" or payload.get("degree_v") != 190:
        raise RuntimeError("candidate endpoint")

    print("ring Q=127,(a),lp;")
    print(f"poly q={factor_a};")
    print('print("Q8-P127-BRANCH-FACTOR-PREFLIGHT");')
    print(f'print("factor_index={args.index}");')
    print(f'print("factor_degree_expected={factor_degree}");')
    print('print("factor_degree_computed="+string(deg(q)));')
    print("ring E=(127,a),(v),lp;")
    print(f"minpoly={factor_a};")
    print(f"poly H={polynomial(payload)};")
    print(f"poly Hv={polynomial(payload, 'v')};")
    print(f"poly Hw={polynomial(payload, 'w')};")
    print("poly G2=gcd(H,Hv);")
    print("poly G3=gcd(G2,Hw);")
    print('print("ramification_gcd_degree="+string(deg(G2)));')
    print('print("singular_gcd_degree="+string(deg(G3)));')
    print('if(deg(G3)==0){print("nonsingular_branch_factor=1");}else{print("nonsingular_branch_factor=0");}')
    print('print("factor_test_end");')


if __name__ == "__main__":
    main()
