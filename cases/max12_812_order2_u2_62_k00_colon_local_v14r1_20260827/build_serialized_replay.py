#!/usr/bin/env python3
"""Build a fresh Singular replay solely from frozen row and polynomial bytes."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def expression(path: Path) -> str:
    text = path.read_text().strip()
    if not text or any(token in text for token in (";", '"', "\n", "\r")):
        raise RuntimeError(("unsafe/malformed serialized polynomial", str(path)))
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prelude", type=Path)
    parser.add_argument("artifacts", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("result", type=Path)
    parser.add_argument("--field", choices=("Q", "65521"), required=True)
    args = parser.parse_args()
    prelude = args.prelude.read_text()
    if prelude.count("ring R=") != 1 or sum(prelude.count(f"poly r{i}=") for i in range(1, 8)) != 7:
        raise RuntimeError("malformed replay prelude")
    witness_path = args.artifacts / "LOCAL_UNIT_WITNESS_R1.txt"
    multiplier_paths = [args.artifacts / f"UNIT_MULTIPLIER_{i}.txt" for i in range(1, 7)]
    h = expression(witness_path)
    multipliers = [expression(path) for path in multiplier_paths]
    lines = [prelude.rstrip(), f'print("K00_SERIALIZED_REPLAY_FIELD={args.field}");', f"poly h=({h});"]
    lines.extend(f"poly u{i}=({value});" for i, value in enumerate(multipliers, 1))
    lines.extend([
        "poly residual=-h*r7+u1*r1+u2*r2+u3*r3+u4*r4+u5*r5+u6*r6;",
        "poly h0=h;",
        "h0=subst(h0,d0,0); h0=subst(h0,d1,0); h0=subst(h0,d2,0);",
        "h0=subst(h0,d3,0); h0=subst(h0,d4,0); h0=subst(h0,d5,0);",
        "int replay_ok=(residual==0); int unit_ok=(h0!=0);",
        'print("K00_SERIALIZED_IDENTITY_REPLAY="+string(replay_ok));',
        'print("K00_SERIALIZED_UNIT_CONSTANT_NONZERO="+string(unit_ok));',
        'write("SERIALIZED_IDENTITY_RESIDUAL.txt",residual);',
        'write("SERIALIZED_UNIT_WITNESS.txt",h);',
        'if (replay_ok*unit_ok!=1) { print("K00_SERIALIZED_FAIL=IDENTITY_OR_UNIT"); quit; }',
        'print("K00_SERIALIZED_ENDPOINT=PASS_FRESH_PROCESS");',
        "quit;",
    ])
    args.output.write_text("\n".join(lines) + "\n")
    result = {
        "status": "PASS-K00-SERIALIZED-REPLAY-BUILDER",
        "field": args.field,
        "prelude_sha256": digest(args.prelude),
        "witness_sha256": digest(witness_path),
        "multiplier_sha256": {str(i): digest(path) for i, path in enumerate(multiplier_paths, 1)},
        "replay_input_sha256": digest(args.output),
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

