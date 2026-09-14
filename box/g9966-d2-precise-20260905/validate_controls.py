#!/usr/bin/env python3
"""Fail closed unless both pristine endpoint controls reproduce exactly."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PIN = "3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(branch: str, stage: int) -> dict:
    root = HERE / "control" / branch
    assert (root / f"stage{stage}.rc").read_text().strip() == "0"
    return json.loads((root / f"stage{stage}.json").read_text())


def constant_row(data: dict, label: str, value: str) -> None:
    rows = {row["label"]: row["expression"] for row in data["joint_elimination"]["residual_rows"]}
    assert rows[label] == value, (label, rows.get(label))


assert sha256(HERE / "original_band_engine.py") == PIN
d2 = load("delta2", 4)
d52 = load("delta52", 8)
assert d2["driver_sha256"] == PIN and d52["driver_sha256"] == PIN
assert d2["verdict"] == "DEAD"
assert d2["joint_elimination"]["Qstar_pivots"] == 35
assert d2["joint_elimination"]["singular"]["unit_ideal"] is True
constant_row(d2, "stage4_J_d159_k35", "6264")
assert d52["verdict"] == "DEAD"
assert d52["joint_elimination"]["Qstar_pivots"] == 66
assert d52["joint_elimination"]["singular"]["unit_ideal"] is True
constant_row(d52, "stage8_G_local16_coord0", "64")

result = {
    "status": "PASS",
    "coefficient_field": "Q",
    "original_engine_sha256": PIN,
    "delta2": {
        "stage": 4,
        "verdict": "DEAD",
        "Qstar_pivots": 35,
        "unit_generator": {"label": "stage4_J_d159_k35", "value": 6264, "inverse": "1/6264"},
        "json_sha256": sha256(HERE / "control/delta2/stage4.json"),
    },
    "delta52": {
        "stage": 8,
        "verdict": "DEAD",
        "Qstar_pivots": 66,
        "unit_generator": {"label": "stage8_G_local16_coord0", "value": 64, "inverse": "1/64"},
        "json_sha256": sha256(HERE / "control/delta52/stage8.json"),
    },
}
print(json.dumps(result, indent=2, sort_keys=True))
