#!/usr/bin/env python3
"""Emit a generator-order-preserving subset of an msolve input."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--keep", help="comma-separated 1-based indices/ranges")
    ap.add_argument("--drop", help="comma-separated 1-based indices/ranges")
    ap.add_argument("--shortest", type=int,
                    help="keep N shortest non-extra rows plus the final two extras")
    ap.add_argument("--char", help="override field characteristic")
    ap.add_argument("--append", help="append one generator")
    args = ap.parse_args()
    lines = args.source.read_text(encoding="utf-8").splitlines()
    body = "\n".join(lines[2:]).strip()
    if body.endswith(","):
        body = body[:-1]
    generators = [x.strip() for x in body.split(",\n") if x.strip()]

    def decode(spec: str | None) -> set[int]:
        out: set[int] = set()
        for item in (spec or "").split(","):
            if not item:
                continue
            if "-" in item:
                lo, hi = map(int, item.split("-", 1))
                out.update(range(lo, hi + 1))
            else:
                out.add(int(item))
        return out

    if args.shortest is not None:
        body_indices = range(1, max(1, len(generators) - 1))
        ranked = sorted(body_indices, key=lambda i: (len(generators[i - 1]), i))
        keep = set(ranked[:args.shortest]) | {len(generators) - 1, len(generators)}
    else:
        keep = decode(args.keep) if args.keep else set(range(1, len(generators) + 1))
    keep -= decode(args.drop)
    indices = [i for i in range(1, len(generators) + 1) if i in keep]
    characteristic = args.char if args.char is not None else lines[1]
    selected = [generators[i - 1] for i in indices]
    if args.append:
        selected.append(args.append)
    text = lines[0] + "\n" + characteristic + "\n" + ",\n".join(selected) + "\n"
    args.output.write_text(text, encoding="utf-8")
    receipt = {
        "source": str(args.source.resolve()),
        "source_sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(),
        "source_generator_count": len(generators),
        "original_indices_1based": indices,
        "subset_sha256": hashlib.sha256(text.encode()).hexdigest(),
    }
    args.output.with_suffix(args.output.suffix + ".json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
