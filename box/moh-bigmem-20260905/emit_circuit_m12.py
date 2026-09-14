#!/usr/bin/env python3
"""Emit the missing s'=4 graph/circuit presentation into the bigmem workdir."""
from pathlib import Path
import importlib.util
import json
import shutil

REPO = Path("/home/ubuntu/jc2")
SRC = REPO / "box/moh14-charts-20260905/hsupport-gate-20260905/source-complete"
OPS = SRC / "ops/circuit_emit.py"
DEST_BASE = REPO / "box/moh-bigmem-20260905/circuit-src"
STEM = "C_n24m16_Mm12_m2_5_ell1_s4_V1_1_6"
CLS = "C_n24m16_Mm12_m2_5_ell1_s4"

cls_src = SRC / "classes" / CLS
cls_dst = DEST_BASE / "classes" / CLS
(cls_dst / "builders").mkdir(parents=True, exist_ok=True)
(cls_dst / "meta").mkdir(parents=True, exist_ok=True)
shutil.copy2(cls_src / "builders" / f"{STEM}_builder.sing", cls_dst / "builders" / f"{STEM}_builder.sing")
shutil.copy2(cls_src / "meta" / f"{STEM}.json", cls_dst / "meta" / f"{STEM}.json")

spec = importlib.util.spec_from_file_location("circuit_emit", OPS)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.BASE = DEST_BASE
result = mod.emit({"stem": STEM, "host": "local-m12-circuit"})
out = REPO / "box/moh-bigmem-20260905/m12_circuit_emit.json"
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
