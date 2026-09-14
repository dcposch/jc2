#!/usr/bin/env python3
"""Convert a frozen msolve integral-generator file to exact-Q Singular input.

The conversion is syntax-only: variable order and generator order are preserved.
The emitted runner computes a reduced standard basis with option(redSB).
With --lift it instead runs liftstd and records/checks the coefficient column
for the unit generator.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re


def parse_ms(path: Path) -> tuple[list[str], str, list[str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) < 3:
        raise ValueError("short msolve input")
    variables = [v.strip() for v in lines[0].split(",") if v.strip()]
    characteristic = lines[1].strip()
    if characteristic != "0":
        raise ValueError(f"expected characteristic 0, got {characteristic!r}")
    body = "\n".join(lines[2:]).strip()
    if body.endswith(","):
        body = body[:-1]
    # The producer emits one polynomial per line, separated by a trailing comma.
    generators = [g.strip() for g in body.split(",\n") if g.strip()]
    return variables, characteristic, generators


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--lift", action="store_true")
    ap.add_argument("--direct-lift", action="store_true",
                    help="use lift(I,ideal(1)) rather than liftstd")
    ap.add_argument("--indices", help="comma-separated 1-based generator subset")
    ap.add_argument("--prune-unused", action="store_true")
    args = ap.parse_args()

    variables, _, generators = parse_ms(args.source)
    if args.indices:
        indices = [int(x) for x in args.indices.split(",") if x]
        generators = [generators[i - 1] for i in indices]
    else:
        indices = list(range(1, len(generators) + 1))
    if args.prune_unused:
        used: set[str] = set()
        for generator in generators:
            used.update(re.findall(r"(?<![A-Za-z0-9_])v[0-9]+(?![A-Za-z0-9_])", generator))
        variables = [v for v in variables if v in used]

    source_hash = hashlib.sha256(args.source.read_bytes()).hexdigest()
    out: list[str] = [
        "option(redSB); short=0;",
        f"// source={args.source.resolve()}",
        f"// source_sha256={source_hash}",
        f"// original_indices={','.join(map(str, indices))}",
        f"ring R=0,({','.join(variables)}),dp;",
        "ideal I=",
        ",\n".join(generators) + ";",
        'print("CERT__NGEN "+string(size(I)));',
        "int t=timer;",
    ]
    if args.lift or args.direct_lift:
        lift_lines = (
            ["matrix T=lift(I,ideal(1));", "ideal G=ideal(1);"]
            if args.direct_lift
            else ["matrix T;", "ideal G=liftstd(I,T);"]
        )
        out.extend(
            lift_lines + [
                'print("CERT__SECONDS "+string(timer-t));',
                'print("CERT__GB_SIZE "+string(size(G)));',
                "int UNITCONST=(size(G)==1 && deg(G[1])==0);",
                "number UNITCOEF;",
                "if (UNITCONST) { UNITCOEF=leadcoef(G[1]); T=(1/UNITCOEF)*T; G=ideal(1); }",
                'print("CERT__UNIT_CONSTANT "+string(UNITCONST));',
                'print("CERT__UNIT "+string(size(G)==1 && G[1]==1));',
                "matrix CHECK=matrix(I)*T;",
                'print("CERT__DIRECT_CHECK "+string(CHECK[1,1]==1));',
                'print("CERT__COFACTORS_BEGIN");',
                "int ci; for (ci=1; ci<=nrows(T); ci++) { print(\"CERT__COFACTOR \"+string(ci)+\" \"+string(T[ci,1])); }",
                'print("CERT__COFACTORS_END");',
            ]
        )
    else:
        out.extend(
            [
                "ideal G=std(I);",
                'print("CERT__SECONDS "+string(timer-t));',
                'print("CERT__GB_SIZE "+string(size(G)));',
                'print("CERT__UNIT "+string(size(G)==1 && G[1]==1));',
                'print("CERT__GB_BEGIN");',
                "print(G);",
                'print("CERT__GB_END");',
            ]
        )
    out.append("quit;")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
