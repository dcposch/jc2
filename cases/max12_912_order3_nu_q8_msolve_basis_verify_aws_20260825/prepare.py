#!/usr/bin/env python3
"""Turn a completed msolve fixed-fibre lane into an exact Singular verifier."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_input(path: Path):
    lines = path.read_text().splitlines()
    if len(lines) < 3:
        raise RuntimeError("short msolve input")
    variables = [item.strip() for item in lines[0].split(",") if item.strip()]
    prime = int(lines[1].strip())
    equations = []
    for line in lines[2:]:
        value = line.strip()
        if not value:
            continue
        if value.endswith(","):
            value = value[:-1]
        equations.append(value)
    if len(variables) != 8 or len(equations) != 8:
        raise RuntimeError((variables, len(equations)))
    return variables, prime, equations


def parse_basis(path: Path):
    text = path.read_text()
    marker = "#---\n["
    start = text.find(marker)
    if start < 0 or not text.rstrip().endswith("]:"):
        raise RuntimeError("unrecognized msolve basis output")
    payload = text[start + len(marker):].rstrip()
    payload = payload[:-2]
    basis = [item.strip() for item in payload.split(",\n") if item.strip()]
    if len(basis) != 8:
        raise RuntimeError(("basis length", len(basis)))
    return basis


def singular_source(input_path: Path, result_path: Path) -> str:
    variables, prime, equations = parse_input(input_path)
    basis = parse_basis(result_path)
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
        "ideal I=f1,f2,f3,f4,f5,f6,f7,f8;",
        "ideal G=b1,b2,b3,b4,b5,b6,b7,b8;",
        'print("Q8-MSOLVE-BASIS-VERIFY");',
        f'print("prime={prime}");',
        'print("basis_size="+string(size(G)));',
        'print("basis_dim="+string(dim(G)));',
        'print("basis_vdim="+string(vdim(G)));',
    ])
    for index in range(1, 9):
        lines.extend([
            f"poly rem{index}=reduce(f{index},G);",
            f'print("original_remainder_{index}="+string(rem{index}));',
        ])
    lines.extend([
        "poly H=b1/leadcoef(b1);",
        'print("v_eliminant_degree="+string(deg(H)));',
        "poly Hsf=gcd(H,diff(H,v));",
        'print("v_eliminant_squarefree_gcd_degree="+string(deg(Hsf)));',
        "list RF=factorize(H,1);",
        'print("rational_factor_entries="+string(size(RF[1])));',
        "RF;",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--basis", type=Path, required=True)
    args = parser.parse_args()
    print(singular_source(args.input, args.basis))


if __name__ == "__main__":
    main()
