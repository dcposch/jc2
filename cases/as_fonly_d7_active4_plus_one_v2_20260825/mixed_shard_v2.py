#!/usr/bin/env python3
"""Pinned output-routing correction for active4-plus-one V1."""
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
V1 = ROOT / "cases/as_fonly_d7_active4_plus_one_20260825/mixed_shard.py"
EXPECTED_V1_SHA = "f039af4bee4e3de03fc53c068fda3b22b8b7f8bb80eb0b7b44a4f757bbce6833"
payload = V1.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_V1_SHA
source = payload.decode()

bootstrap_needle = 'os.environ["OUTPUT_JSON"] = os.environ["BOOTSTRAP_JSON"]'
bootstrap_fix = ('FINAL_OUTPUT_JSON = os.environ["OUTPUT_JSON"]\n'
                 'os.environ["OUTPUT_JSON"] = os.environ["BOOTSTRAP_JSON"]')
write_needle = 'Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)'
write_fix = 'Path(FINAL_OUTPUT_JSON).write_bytes(encoded)'
assert source.count(bootstrap_needle) == 1
assert source.count(write_needle) == 1
source = source.replace(bootstrap_needle, bootstrap_fix)
source = source.replace(write_needle, write_fix)
exec(compile(source, str(V1), "exec"), {"__file__": str(V1),
                                       "__name__": "__main__"})

