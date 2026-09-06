#!/usr/bin/env python3
"""Emit a pruned exact-Q liftstd job for an original-index generator subset."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("metadata", type=Path)
    ap.add_argument("indices", help="comma-separated original one-based indices")
    ap.add_argument("output", type=Path)
    args = ap.parse_args()
    lines = args.source.read_text(encoding="utf-8").splitlines()
    if lines[1].strip() != "0":
        raise SystemExit("source is not characteristic zero")
    variables = [v.strip() for v in lines[0].split(",") if v.strip()]
    body = "\n".join(lines[2:]).strip().rstrip(",")
    generators = [g.strip() for g in body.split(",\n") if g.strip()]
    indices = [int(i) for i in args.indices.split(",") if i]
    if indices != sorted(set(indices)) or not all(1 <= i <= len(generators) for i in indices):
        raise SystemExit("indices must be sorted unique original one-based positions")
    selected = [generators[i - 1] for i in indices]
    used = set().union(*(set(re.findall(r"(?<![A-Za-z0-9_])v[0-9]+(?![A-Za-z0-9_])", g)) for g in selected))
    kept_variables = [v for v in variables if v in used]
    meta = json.loads(args.metadata.read_text(encoding="utf-8"))
    weight_map = dict(zip(variables, meta["weights"], strict=True))
    kept_weights = [weight_map[v] for v in kept_variables]
    stem = args.source.name.removesuffix("_p0.ms")
    digest = sha256(args.source)
    order = f"wp({','.join(map(str, kept_weights))})"
    out = [
        "option(redSB); short=0;",
        f"// chart={stem}",
        f"// source={args.source.resolve()}",
        f"// source_sha256={digest}",
        f"// original_indices={','.join(map(str, indices))}",
        f"// monomial_order={order}",
        f"ring R=0,({','.join(kept_variables)}),{order};",
        "ideal I=",
        ",\n".join(selected) + ";",
        f'print("CERT__CHART {stem}");',
        f'print("CERT__SOURCE_SHA256 {digest}");',
        f'print("CERT__ORIGINAL_INDICES {','.join(map(str, indices))}");',
        f'print("CERT__ORDER {order}");',
        'print("CERT__COEFFICIENT_FIELD Q");',
        'print("CERT__NVARS "+string(nvars(basering)));',
        'print("CERT__NGEN "+string(size(I)));',
        "int t=timer; option(prot); matrix T; ideal G=liftstd(I,T); option(noprot);",
        'print("CERT__SECONDS "+string(timer-t));',
        'print("CERT__GB_SIZE "+string(size(G)));',
        "int UNITCONST=(size(G)==1 && deg(G[1])==0);",
        "number UNITCOEF; if (UNITCONST) { UNITCOEF=leadcoef(G[1]); T=(1/UNITCOEF)*T; G=ideal(1); }",
        'print("CERT__UNIT "+string(size(G)==1 && G[1]==1));',
        "matrix C=matrix(I)*T;",
        'print("CERT__INPROCESS_CHECK "+string(ncols(C)==1 && C[1,1]==1));',
        'print("CERT__COFACTORS_BEGIN");',
    ]
    for local_i, original_i in enumerate(indices, 1):
        out.append(f'if (T[{local_i},1]!=0) {{ print("CERT__COFACTOR {original_i} "+string(T[{local_i},1])); }}')
    out.extend(['print("CERT__COFACTORS_END");', "quit;"])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
