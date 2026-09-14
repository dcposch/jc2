#!/usr/bin/env python3
"""Emit a Singular lift computation over Q(q), dropping q's inverse relation.

This is an acceleration experiment for obtaining explicit cofactors.  Its
output is not by itself the requested polynomial-ring certificate; a separate
lifting step must replace q^-n by q_inv^n and add the localizer cofactor.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--prune-unused", action="store_true")
    ap.add_argument("--clear-power", type=int,
                    help="print q^N times each cofactor (polynomial when N is large enough)")
    args = ap.parse_args()
    lines = args.source.read_text(encoding="utf-8").splitlines()
    variables = [v.strip() for v in lines[0].split(",") if v.strip()]
    body = "\n".join(lines[2:]).strip()
    if body.endswith(","):
        body = body[:-1]
    generators = [x.strip() for x in body.split(",\n") if x.strip()]
    localizer = generators[-1]
    match = re.fullmatch(r"(v[0-9]+)\*(v[0-9]+)-1", localizer)
    if not match:
        raise SystemExit(f"unexpected localizer {localizer!r}")
    a, b = match.groups()
    q_inv = variables[-1]
    if q_inv not in (a, b):
        raise SystemExit("last variable is not in localizer")
    q = b if a == q_inv else a
    polynomial_variables = [v for v in variables if v not in (q, q_inv)]
    generators = generators[:-1]
    if args.prune_unused:
        used: set[str] = set()
        for generator in generators:
            used.update(re.findall(r"(?<![A-Za-z0-9_])v[0-9]+(?![A-Za-z0-9_])", generator))
        polynomial_variables = [v for v in polynomial_variables if v in used]
    source_hash = hashlib.sha256(args.source.read_bytes()).hexdigest()
    out = [
        "option(redSB); short=0;",
        f"// source={args.source.resolve()}",
        f"// source_sha256={source_hash}",
        f"// localized_parameter={q} inverse_variable={q_inv}",
        f"ring R=(0,{q}),({','.join(polynomial_variables)}),dp;",
        "ideal I=",
        ",\n".join(generators) + ";",
        f'print("CERT__LOCALIZED_Q {q} QINV {q_inv}");',
        'print("CERT__NGEN "+string(size(I)));',
        "int t=timer; matrix T; ideal G=liftstd(I,T);",
        'print("CERT__SECONDS "+string(timer-t));',
        'print("CERT__GB_SIZE "+string(size(G)));',
        "int UNITCONST=(size(G)==1 && deg(G[1])==0);",
        "number UNITCOEF;",
        "if (UNITCONST) { UNITCOEF=leadcoef(G[1]); T=(1/UNITCOEF)*T; G=ideal(1); }",
        'print("CERT__UNIT_CONSTANT "+string(UNITCONST));',
        'print("CERT__UNIT "+string(size(G)==1 && G[1]==1));',
        'print("CERT__GB "+string(G));',
        "matrix CHECK=matrix(I)*T;",
        'print("CERT__DIRECT_CHECK_LOCALIZED "+string(CHECK[1,1]==1));',
        f'print("CERT__CLEAR_POWER {args.clear_power if args.clear_power is not None else -1}");',
        'print("CERT__COFACTORS_BEGIN");',
        (f"int ci; for (ci=1; ci<=nrows(T); ci++) {{ print(\"CERT__COFACTOR \"+string(ci)+\" \"+string({q}^{args.clear_power}*T[ci,1])); }}"
         if args.clear_power is not None else
         "int ci; for (ci=1; ci<=nrows(T); ci++) { print(\"CERT__COFACTOR \"+string(ci)+\" \"+string(T[ci,1])); }"),
        'print("CERT__COFACTORS_END");',
        "quit;",
    ]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
