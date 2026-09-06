#!/usr/bin/env python3
"""Extract a liftstd identity and emit an independent exact-Q verifier."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_ms(path: Path) -> tuple[list[str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines[1].strip() != "0":
        raise ValueError("source is not over Q")
    variables = [v.strip() for v in lines[0].split(",") if v.strip()]
    body = "\n".join(lines[2:]).strip()
    if body.endswith(","):
        body = body[:-1]
    return variables, [g.strip() for g in body.split(",\n") if g.strip()]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("metadata", type=Path)
    ap.add_argument("lift_log", type=Path)
    ap.add_argument("output_root", type=Path)
    args = ap.parse_args()
    text = args.lift_log.read_text(encoding="utf-8")
    if not re.search(r"^CERT__UNIT 1$", text, re.M):
        raise SystemExit("lift log has no exact unit marker")
    if not re.search(r"^CERT__INPROCESS_CHECK 1$", text, re.M):
        raise SystemExit("lift log has no in-process multiplication marker")
    pairs = [(int(m.group(1)), m.group(2)) for m in re.finditer(r"^CERT__COFACTOR ([0-9]+) (.*)$", text, re.M)]
    if not pairs:
        raise SystemExit("no nonzero cofactors found")
    variables, generators = parse_ms(args.source)
    meta = json.loads(args.metadata.read_text(encoding="utf-8"))
    weights = meta["weights"]
    if len(weights) != len(variables):
        raise SystemExit("weight/variable mismatch")
    if len({i for i, _ in pairs}) != len(pairs) or not all(1 <= i <= len(generators) for i, _ in pairs):
        raise SystemExit("invalid or duplicate cofactor index")
    args.output_root.mkdir(parents=True, exist_ok=True)
    stem = args.source.name.removesuffix("_p0.ms")
    identity = args.output_root / f"{stem}.identity.txt"
    source_sha = sha256(args.source)
    identity.write_text("\n".join([
        f"chart={stem}",
        f"source_sha256={source_sha}",
        "coefficient_field=Q",
        "generator_order=one-based source order, unchanged",
        f"monomial_order=wp({','.join(map(str, weights))})",
        f"source_generator_count={len(generators)}",
        f"nonzero_cofactor_count={len(pairs)}",
        *[f"{i}\t{p}" for i, p in pairs],
    ]) + "\n", encoding="utf-8")
    order = f"wp({','.join(map(str, weights))})"
    verifier = args.output_root / f"{stem}_verify.sing"
    out = [
        "option(redSB); short=0;",
        "// Independent exact-rational direct multiplication; no std/lift call.",
        f"// source={args.source.resolve()}",
        f"// source_sha256={source_sha}",
        f"// identity_sha256={sha256(identity)}",
        f"ring R=0,({','.join(variables)}),{order};",
        "ideal I=",
        ",\n".join(generators) + ";",
        f"matrix T[{len(generators)}][1];",
    ]
    out.extend(f"T[{i},1]={p};" for i, p in pairs)
    out.extend([
        "matrix C=matrix(I)*T;",
        f'print("VERIFY__CHART {stem}");',
        f'print("VERIFY__SOURCE_SHA256 {source_sha}");',
        f'print("VERIFY__IDENTITY_SHA256 {sha256(identity)}");',
        'print("VERIFY__COEFFICIENT_FIELD Q");',
        'print("VERIFY__DIRECT_PRODUCT "+string(C[1,1]));',
        'print("VERIFY__EXACT_ONE "+string(ncols(C)==1 && C[1,1]==1));',
        "quit;",
    ])
    verifier.write_text("\n".join(out) + "\n", encoding="utf-8")
    receipt = {
        "chart": stem,
        "source": str(args.source.resolve()),
        "source_sha256": source_sha,
        "lift_log": str(args.lift_log.resolve()),
        "lift_log_sha256": sha256(args.lift_log),
        "identity": str(identity.resolve()),
        "identity_sha256": sha256(identity),
        "identity_bytes": identity.stat().st_size,
        "nonzero_indices_1based": [i for i, _ in pairs],
        "verifier": str(verifier.resolve()),
        "verifier_sha256": sha256(verifier),
    }
    (args.output_root / f"{stem}.identity.json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
