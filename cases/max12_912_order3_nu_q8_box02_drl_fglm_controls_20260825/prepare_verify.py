#!/usr/bin/env python3
"""Prepare fail-closed Singular reduction of an msolve elimination output."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_input(path: Path):
    lines = path.read_text().splitlines()
    variables = [item.strip() for item in lines[0].split(",") if item.strip()]
    prime = int(lines[1].strip())
    equations = [line.strip().removesuffix(",") for line in lines[2:] if line.strip()]
    if len(variables) != 8 or len(equations) != 8:
        raise RuntimeError((variables, len(equations)))
    return variables, prime, equations


def parse_basis(path: Path):
    text = path.read_text()
    marker = "#---\n["
    start = text.find(marker)
    if start < 0 or not text.rstrip().endswith("]:"):
        raise RuntimeError("unrecognized msolve elimination output")
    payload = text[start + len(marker):].rstrip()[:-2]
    basis = [item.strip() for item in payload.split(",\n") if item.strip()]
    if not basis:
        raise RuntimeError("empty candidate basis")
    return basis


def source(input_path: Path, basis_path: Path) -> str:
    variables, prime, equations = parse_input(input_path)
    basis = parse_basis(basis_path)
    lines = [
        'LIB "primdec.lib";',
        f"ring R={prime},({','.join(variables)}),(dp(7),dp(1));",
        "option(redSB);",
    ]
    for index, equation in enumerate(equations, 1):
        lines.append(f"poly f{index}={equation};")
    for index, polynomial in enumerate(basis, 1):
        lines.append(f"poly b{index}={polynomial};")
    lines.extend([
        "ideal I=" + ",".join(f"f{i}" for i in range(1, 9)) + ";",
        "ideal G=" + ",".join(f"b{i}" for i in range(1, len(basis) + 1)) + ";",
        "ideal GS=std(G);",
        'print("Q8-MSOLVE-ELIMINATION-IDEAL-VERIFY");',
        f'print("prime={prime}");',
        f'print("candidate_reported_size={len(basis)}");',
        'print("candidate_std_size="+string(size(GS)));',
        'print("candidate_std_dim="+string(dim(GS)));',
        'print("candidate_std_vdim="+string(vdim(GS)));',
        "poly one=1;",
        "poly one_rem=reduce(one,GS);",
        'print("candidate_unit_remainder="+string(one_rem));',
    ])
    for index in range(1, 9):
        lines.extend([
            f"poly rem{index}=reduce(f{index},GS);",
            f'print("original_remainder_{index}="+string(rem{index}));',
        ])
    if len(basis) >= 1:
        lines.extend([
            "poly H=b1/leadcoef(b1);",
            'print("reported_first_degree="+string(deg(H)));',
            "poly Hsf=gcd(H,diff(H,v));",
            'print("reported_first_squarefree_gcd_degree="+string(deg(Hsf)));',
        ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--basis", type=Path, required=True)
    args = parser.parse_args()
    print(source(args.input, args.basis))


if __name__ == "__main__":
    main()
