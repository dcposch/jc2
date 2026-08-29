#!/usr/bin/env python3
"""Wrap frozen a8d3 compiler and retain each grade-38 bridge residual; AWS only."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "cases/max12_812_order2_square_owner_d1_d23_a8a9_j38_r3_tail_20260826/compile_tail_r3.py"
SOURCE_FREEZE = ROOT / "cases/max12_812_order2_square_owner_d1_d23_a8a9_j38_r3_tail_20260826/FREEZE.sha256"
PINS = {
    SOURCE: "efd8fda63689e7012d2cd81e95cd8587d1e0f963e789abc885dca3e76796ec22",
    SOURCE_FREEZE: "4a36e6ff0b97800559bbef9b1366ab1e995f2e1deef341b1d009b2d4f7595dc6",
    HERE / "PREREGISTRATION.md": "c33703707a2371014e7e2d9aacc3c9473de1ed711ef5387f1b77a2ac8243986b",
}
PREFIX = "D1A8D3J38R3"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65519, 65521), required=True)
    args = parser.parse_args()
    if platform.system() != "Linux" or not Path("/sys/class/dmi/id/sys_vendor").is_file():
        fail("AWS-only diagnostic refused non-Linux host")
    if Path("/sys/class/dmi/id/sys_vendor").read_text().strip() != "Amazon EC2":
        fail("AWS-only diagnostic refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("registered AWS lane is mandatory")
    for path, expected in PINS.items():
        actual = digest(path)
        if actual != expected:
            fail(("frozen pin mismatch", str(path), actual, expected))
    output = args.output.resolve()
    subprocess.run([
        sys.executable, str(SOURCE), str(output), "--characteristic",
        str(args.characteristic), "--a", "8", "--d", "3",
    ], check=True)
    files = list(output.glob("*.sing"))
    if len(files) != 1:
        fail(("generated Singular source count", files))
    target = files[0]
    text = target.read_text()
    for row in range(1, 8):
        old = (
            f"int {PREFIX}_bridge{row}=(reduce({PREFIX}_SourcePhi{row}-"
            f"{PREFIX}_PredPhi{row},{PREFIX}_S39)==0);"
        )
        new = "\n".join([
            f"poly {PREFIX}_diff{row}=reduce({PREFIX}_SourcePhi{row}-{PREFIX}_PredPhi{row},{PREFIX}_S39);",
            f"int {PREFIX}_bridge{row}=({PREFIX}_diff{row}==0);",
            f"poly {PREFIX}_qdiff{row}={PREFIX}_diff{row};",
            f"int {PREFIX}_val{row}=0;",
            f"while (({PREFIX}_qdiff{row}!=0) && (subst({PREFIX}_qdiff{row},sigma,0)==0) && ({PREFIX}_val{row}<39))",
            "{",
            f" {PREFIX}_qdiff{row}={PREFIX}_qdiff{row}/sigma;",
            f" {PREFIX}_val{row}={PREFIX}_val{row}+1;",
            "}",
            f"poly {PREFIX}_lc{row}=subst({PREFIX}_qdiff{row},sigma,0);",
        ])
        if text.count(old) != 1:
            fail(("bridge source replacement count", row, text.count(old)))
        text = text.replace(old, new)
    marker = (
        f'int {PREFIX}_full_bridge=' + "*".join(f"{PREFIX}_bridge{row}" for row in range(1, 8)) + ";\n"
        f'print("{PREFIX}_ALL_SEVEN_SOURCE_ROWS_BRIDGED="+string({PREFIX}_full_bridge));'
    )
    diagnostics = [marker]
    for row in range(1, 8):
        diagnostics += [
            f'print("A8D3_DIAG_ROW{row}_BRIDGE="+string({PREFIX}_bridge{row}));',
            f'print("A8D3_DIAG_ROW{row}_VALUATION="+string({PREFIX}_val{row}));',
            f'print("A8D3_DIAG_ROW{row}_COEFF_TERMS="+string(size({PREFIX}_lc{row})));',
            f'print("A8D3_DIAG_ROW{row}_LEAD="+string(lead({PREFIX}_lc{row})));',
        ]
    diagnostics += ['print("A8D3_DIAG_ENDPOINT=BRIDGE_RESIDUALS_RECORDED");', "quit;"]
    if text.count(marker) != 1:
        fail(("diagnostic marker count", text.count(marker)))
    text = text.replace(marker, "\n".join(diagnostics))
    target.write_text(text)
    payload = {
        "status": "COMPILED-A8D3-BRIDGE-DIAGNOSTIC",
        "scope": "A8_D3_GRADE38_BRIDGE_FAILURE_LOCALIZATION_ONLY",
        "characteristic": args.characteristic,
        "registered_aws_lane": tag,
        "patched_singular_sha256": digest(target),
    }
    (output / "diagnostic.json").write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
