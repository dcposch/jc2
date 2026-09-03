#!/usr/bin/env python3
"""Orchestrate the nonlinear T2/T3 bridge add-on.  Does not modify charged drivers."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RECEIPT = ROOT / "xmodel/g9966-bridge-nonlinear-grok46-20260903.run.v2"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_frozen() -> dict:
    fields: dict[str, str] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    count = int(fields["charged_inputs"])
    frozen = Path(fields["lane_inputs_dir"])
    for index in range(1, count + 1):
        name = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        actual = sha256(frozen / name)
        if actual != expected:
            raise SystemExit(f"hash mismatch: {name}")
    proc = subprocess.run(
        ["sha256sum", "-c", str(HERE / "inputs.sha256")],
        capture_output=True,
        text=True,
        check=False,
    )
    ok = [line for line in proc.stdout.splitlines() if line.endswith(": OK")]
    return {
        "charged_inputs": count,
        "manifest_ok_count": len(ok),
        "all_hashes_match": len(ok) == count,
    }


def load_json(name: str) -> dict:
    path = HERE / f"{name}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"missing": True}


def main() -> None:
    started = time.perf_counter()
    custody = verify_frozen()
    assert custody["all_hashes_match"]
    assert custody["charged_inputs"] == 24
    out = {
        "type": "OPEN[EFFECTIVE-T2-T3-BRIDGE] linearized/Q*/modular add-on",
        "frozen_input_verification": custody,
        "jet_support": load_json("jet_support"),
        "residual_linear": load_json("residual_linear"),
        "residual_d52": load_json("residual_d52"),
        "controls_bridge": load_json("controls_bridge"),
        "elapsed_seconds": round(time.perf_counter() - started, 4),
    }
    (HERE / "results.json").write_text(json.dumps(out, indent=2, sort_keys=True, default=str) + "\n")
    print("wrote results.json", "keys", list(out))


if __name__ == "__main__":
    main()
