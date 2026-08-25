#!/usr/bin/env python3
"""Hash-pinned adapter replacing Rabinowitsch elimination by elim.lib sat."""

from __future__ import annotations

import argparse
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
from pathlib import Path
import runpy
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = ROOT / "cases/max12_912_order3_nu_q8_projective_fibre_boundary_saturated_aws_20260825/generate.py"
BASE_SHA256 = "cc25cc817ad9d1f5eacd471548fec898af6cf52f8dd97f75817f52cbf9f678f3"
OLD = "ideal K=J,z*t-1;\nideal C=eliminate(K,z);"
NEW = 'LIB "elim.lib";\nlist Sat=sat(J,ideal(t));\nideal C=Sat[1];'


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--w-value", type=int, default=25)
    args = parser.parse_args()
    raw = BASE.read_bytes()
    if sha256(raw).hexdigest() != BASE_SHA256:
        raise RuntimeError("base generator hash")
    old_argv = sys.argv
    output = StringIO()
    try:
        sys.argv = [str(BASE), "--w-value", str(args.w_value)]
        with redirect_stdout(output):
            runpy.run_path(str(BASE), run_name="__main__")
    finally:
        sys.argv = old_argv
    source = output.getvalue()
    if source.count(OLD) != 1 or NEW in source:
        raise RuntimeError("saturation adapter anchor")
    print(source.replace(OLD, NEW), end="")


if __name__ == "__main__":
    main()

