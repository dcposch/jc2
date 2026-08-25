#!/usr/bin/env python3
"""Emit the exact 79 compatible structural bases from the frozen Q9 census."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
Q9 = (ROOT / "cases/as_fonly_d7_vertical_q9_state_gate_20260825"
      / "compile_shard.py")
EXPECTED_Q9_SHA = (
    "54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2")
payload = Q9.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_Q9_SHA
source = payload.decode()
anchor = "    compatible_per_base[local_compatible] += 1\n"
assert source.count(anchor) == 1
replacement = anchor + (
    "    if local_compatible:\n"
    "        print(\"Q9_COMPATIBLE_BASE\", base_index, \"\".join(\n"
    "            str(value) for value in svalues), local_compatible,\n"
    "            local_completions)\n")
patched = source.replace(anchor, replacement)
scope = {"__file__": str(Q9), "__name__": "__compatible_base_emitter__"}
exec(compile(patched, str(Q9), "exec"), scope)
print("PASS-Q9-COMPATIBLE-BASE-EMITTER")
