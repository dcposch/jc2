#!/usr/bin/env python3
"""Build a fresh branch-aware replay from serialized V16R1 bytes."""

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
    branch_path = args.artifacts / "BRANCH.txt"
    branch = branch_path.read_text().strip()
    if branch not in ("M6_FORCED", "M6_FREEDOM"):
        raise RuntimeError(("invalid branch", branch))
    base_paths = [args.artifacts / f"BASE_SYZYGY_{i}.txt" for i in range(1, 8)]
    base = [expression(path) for path in base_paths]
    freedom_paths = [args.artifacts / f"FREEDOM_SYZYGY_{i}.txt" for i in range(1, 8)]
    freedom = [expression(path) for path in freedom_paths] if branch == "M6_FREEDOM" else []
    if branch == "M6_FORCED" and any(path.exists() for path in freedom_paths):
        raise RuntimeError("forced branch unexpectedly contains freedom witness")
    lines = [prelude.rstrip(), f'print("K00_SYZPROJ_R1_SERIALIZED_FIELD={args.field}");']
    lines.extend(f"poly b{i}=({value});" for i, value in enumerate(base, 1))
    lines.extend([
        "poly rb=b1*r1+b2*r2+b3*r3+b4*r4+b5*r5+b6*r6+b7*r7;",
        "poly b70=b7;",
        "b70=subst(b70,d0,0); b70=subst(b70,d1,0); b70=subst(b70,d2,0); b70=subst(b70,d3,0); b70=subst(b70,d4,0); b70=subst(b70,d5,0);",
        "int base_ok=((rb==0)&&(b70!=0));",
        'print("K00_SYZPROJ_R1_SERIALIZED_BASE_REPLAY="+string(base_ok));',
        'write("BASE_RESIDUAL.txt",rb);',
        'if (base_ok!=1) { print("K00_SYZPROJ_R1_SERIALIZED_FAIL=BASE_REPLAY"); quit; }',
    ])
    if branch == "M6_FREEDOM":
        lines.extend(f"poly w{i}=({value});" for i, value in enumerate(freedom, 1))
        lines.extend([
            "poly rw=w1*r1+w2*r2+w3*r3+w4*r4+w5*r5+w6*r6+w7*r7;",
            "poly w70=w7; poly w60=w6;",
            "w70=subst(w70,d0,0); w70=subst(w70,d1,0); w70=subst(w70,d2,0); w70=subst(w70,d3,0); w70=subst(w70,d4,0); w70=subst(w70,d5,0);",
            "w60=subst(w60,d0,0); w60=subst(w60,d1,0); w60=subst(w60,d2,0); w60=subst(w60,d3,0); w60=subst(w60,d4,0); w60=subst(w60,d5,0);",
            "int freedom_ok=((rw==0)&&(w70==0)&&(w60!=0));",
            'print("K00_SYZPROJ_R1_SERIALIZED_FREEDOM_REPLAY="+string(freedom_ok));',
            'write("FREEDOM_RESIDUAL.txt",rw);',
            'if (freedom_ok!=1) { print("K00_SYZPROJ_R1_SERIALIZED_FAIL=FREEDOM_REPLAY"); quit; }',
        ])
    lines.extend([
        f'print("K00_SYZPROJ_R1_SERIALIZED_BRANCH={branch}");',
        'print("K00_SYZPROJ_R1_SERIALIZED_ENDPOINT=PASS_FRESH_PROCESS");',
        "quit;",
    ])
    args.output.write_text("\n".join(lines) + "\n")
    result = {
        "status": "PASS-K00-SYZPROJ-V16R1-REPLAY-BUILDER",
        "field": args.field,
        "branch": branch,
        "branch_sha256": digest(branch_path),
        "prelude_sha256": digest(args.prelude),
        "base_component_sha256": {str(i): digest(path) for i, path in enumerate(base_paths, 1)},
        "freedom_component_sha256": (
            {str(i): digest(path) for i, path in enumerate(freedom_paths, 1)}
            if branch == "M6_FREEDOM" else {}
        ),
        "replay_input_sha256": digest(args.output),
    }
    args.result.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

