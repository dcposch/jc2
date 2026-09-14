#!/usr/bin/env python3
"""Emit exact normal-form screens of candidate dump rows against a base subset."""

from __future__ import annotations

import argparse
from pathlib import Path
import re

from emit_reduced_subset_singular import parse_dump, parse_indices, sha256


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dump", type=Path, required=True)
    parser.add_argument("--characteristic", type=int, required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--candidates", required=True)
    parser.add_argument("--solve", action="store_true")
    parser.add_argument("--print-nf", action="store_true")
    parser.add_argument("--algorithm", choices=("std", "slimgb"), default="std")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    dump = args.dump.resolve()
    variables, rows = parse_dump(dump)
    base = parse_indices(args.base, len(rows))
    candidates = parse_indices(args.candidates, len(rows))
    if set(base) & set(candidates):
        raise ValueError("base and candidate indices overlap")
    lines = [
        f"// dump_sha256={sha256(dump)}",
        f"// base_indices={','.join(map(str, base))}",
        f"// candidate_indices={','.join(map(str, candidates))}",
        f"ring R={args.characteristic},({','.join(variables)}),dp;",
        "option(redSB);",
        "ideal B=" + ",\n".join(rows[index] for index in base) + ";",
        '"BASE_STD_BEGIN";',
        "ideal G=std(B);",
        '"BASE_STD_DONE size="+string(size(G))+" dim="+string(dim(G));',
    ]
    for serial, index in enumerate(candidates):
        lines += [
            f"poly C_{serial:03d}={rows[index]};",
            f"poly N_{serial:03d}=reduce(C_{serial:03d},G);",
            f"if (N_{serial:03d}==0) "
            f'{{ "NF_ROW index={index} zero=1"; }} else '
            f'{{ "NF_ROW index={index} zero=0 degree="+string(deg(N_{serial:03d}))'
            f'+" chars="+string(size(string(N_{serial:03d}))); }}',
        ]
        if args.print_nf:
            lines.append(f'"NF_POLY index={index} "+string(N_{serial:03d});')
    if args.solve:
        nf_names = [f"N_{serial:03d}" for serial in range(len(candidates))]
        lines += [
            "ideal COMBINED=G," + ",".join(nf_names) + ";",
            f'"COMBINED_STD_BEGIN generators="+string(size(COMBINED))+" algorithm={args.algorithm}";',
            "timer=1; int COMBINED_T0=timer;",
            f"ideal G2={args.algorithm}(COMBINED);",
            "int COMBINED_DT=timer-COMBINED_T0;",
            "poly COMBINED_ONE=reduce(1,G2);",
            "ideal COMBINED_NF=reduce(COMBINED,G2);",
            "int COMBINED_NF_ZERO=1; int COMBINED_I;",
            "for (COMBINED_I=1;COMBINED_I<=size(COMBINED_NF);COMBINED_I++) "
            "{ if (COMBINED_NF[COMBINED_I]!=0) { COMBINED_NF_ZERO=0; } }",
            '"COMBINED_STD_DONE ms="+string(COMBINED_DT)+" basis_size="+string(size(G2))'
            '+" dim="+string(dim(G2));',
            '"COMBINED_NF_ALL_ZERO "+string(COMBINED_NF_ZERO);',
            'if (COMBINED_ONE==0) { "COMBINED_UNIT 1"; } else { "COMBINED_UNIT 0"; }',
            'if (COMBINED_NF_ZERO!=1) { "COMBINED_CONTROL_FAIL"; exit(95); }',
        ]
    lines.append('"SCRIPT_DONE";')
    args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
