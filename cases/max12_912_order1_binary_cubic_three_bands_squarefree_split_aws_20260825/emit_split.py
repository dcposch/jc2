#!/usr/bin/env python3
"""Split a pinned emitted Singular ideal into its 7+8 registered blocks."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


PIN = "80261b2d528a6c1e85631795be11ff99bbb54c5313a6b5980077c9cdf48aea11"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    src = Path(args.input)
    raw = src.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == PIN
    text = raw.decode()
    lines = text.splitlines()
    ring = next(line for line in lines if line.startswith("ring R="))
    start = next(i for i, line in enumerate(lines) if line.startswith("ideal I="))
    end = next(i for i in range(start, len(lines)) if lines[i].endswith(";"))
    payload = "\n".join(lines[start:end + 1])
    assert payload.startswith("ideal I=") and payload.endswith(";")
    generators = payload[len("ideal I="):-1].split(",\n  ")
    assert len(generators) == 15
    i17 = generators[:7]
    i16 = generators[7:]
    out = [
        "// Exact split-basis overlap control.",
        "option(redSB);",
        ring,
        "ideal I17=" + ",\n  ".join(i17) + ";",
        "ideal I16=" + ",\n  ".join(i16) + ";",
        "ideal G17=std(I17);",
        "ideal R16=reduce(I16,G17);",
        "ideal J=G17+R16;",
        "ideal G=slimgb(J);",
        "ideal O=I17+I16;",
        "int ok=1;",
        "for (int ii=1; ii<=size(O); ii++){ if (reduce(O[ii],G)!=0){ ok=0; } }",
        'if (ok==1){ print("ORIGINAL_REMAINDERS_ZERO"); }',
        'else { print("ORIGINAL_REMAINDERS_NONZERO"); }',
        'print("INPUT17 "+string(size(I17)));',
        'print("INPUT16 "+string(size(I16)));',
        'print("REDUCED16 "+string(size(R16)));',
        'print("GB_GENERATORS "+string(size(G)));',
        'print("DIMENSION "+string(dim(G)));',
        'print("GROEBNER_BEGIN");',
        "print(G);",
        'print("GROEBNER_END");',
        'print("PASS");',
        "quit;",
    ]
    target = Path(args.output)
    target.write_text("\n".join(out) + "\n")
    print("PASS_EMIT", len(i17), len(i16), hashlib.sha256(target.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()

