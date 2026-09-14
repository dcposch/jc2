#!/usr/bin/env python3
"""Build the polynomial-ring checker for a cleared localized Singular lift."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re


def parse_ms(path: Path) -> tuple[list[str], list[str]]:
    lines = path.read_text().splitlines()
    variables = lines[0].split(",")
    body = "\n".join(lines[2:]).strip().rstrip(",")
    return variables, body.split(",\n")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("cleared_lift_output", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--indices", required=True)
    ap.add_argument("--q", required=True)
    ap.add_argument("--q-inv", required=True)
    ap.add_argument("--power", required=True, type=int)
    args = ap.parse_args()

    variables, all_generators = parse_ms(args.source)
    indices = [int(x) for x in args.indices.split(",")]
    generators = [all_generators[i - 1] for i in indices]
    assert generators[-1] == f"{args.q}*{args.q_inv}-1"
    rows = generators[:-1]

    cofactors: dict[int, str] = {}
    for line in args.cleared_lift_output.read_text().splitlines():
        match = re.fullmatch(r"CERT__COFACTOR (\d+) (.*)", line)
        if match:
            cofactors[int(match.group(1))] = match.group(2)
    assert sorted(cofactors) == list(range(1, len(rows) + 1))
    assert f"CERT__CLEAR_POWER {args.power}" in args.cleared_lift_output.read_text()
    # The cleared expressions must be polynomials in q, never Laurent terms.
    assert not any(re.search(rf"/[^+\-]*{re.escape(args.q)}", c) for c in cofactors.values())

    polynomial_cofactors = [f"{args.q_inv}^{args.power}*({cofactors[i]})"
                            for i in range(1, len(rows) + 1)]
    t = f"({args.q}*{args.q_inv})"
    geometric = "+".join("1" if i == 0 else (t if i == 1 else f"{t}^{i}")
                         for i in range(args.power))
    polynomial_cofactors.append(f"-({geometric})")

    used: set[str] = set()
    for expression in rows + [generators[-1]] + polynomial_cofactors:
        used.update(re.findall(r"(?<![A-Za-z0-9_])v[0-9]+(?![A-Za-z0-9_])", expression))
    ring_variables = [v for v in variables if v in used]

    source_hash = hashlib.sha256(args.source.read_bytes()).hexdigest()
    lift_hash = hashlib.sha256(args.cleared_lift_output.read_bytes()).hexdigest()
    out = [
        "option(redSB); short=0;",
        f"// full_source={args.source.resolve()}",
        f"// full_source_sha256={source_hash}",
        f"// original_indices={','.join(map(str, indices))}",
        f"// cleared_lift_output_sha256={lift_hash}",
        f"// clearing_identity=sum(c_i*g_i)={args.q}^{args.power}",
        f"ring R=0,({','.join(ring_variables)}),dp;",
        "ideal I=",
        ",\n".join(generators) + ";",
        f"matrix T[{len(generators)}][1]=",
        ",\n".join(polynomial_cofactors) + ";",
        "int t0=timer;",
        "matrix CHECK=matrix(I)*T;",
        'print("CERT__FULL_SOURCE_SHA256 ' + source_hash + '");',
        f'print("CERT__ORIGINAL_INDICES {args.indices}");',
        f'print("CERT__CLEAR_POWER {args.power}");',
        'print("CERT__NGEN "+string(size(I)));',
        'print("CERT__DIRECT_CHECK_POLYNOMIAL "+string(CHECK[1,1]==1));',
        'print("CERT__CHECK_VALUE "+string(CHECK[1,1]));',
        'print("CERT__CHECK_SECONDS "+string(timer-t0));',
        "quit;",
    ]
    args.output.write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
