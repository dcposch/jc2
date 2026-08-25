#!/usr/bin/env python3
"""Source-pinned 79-base list emitter for the Q5 Cartier fanout."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_vertical_q9_state_gate_20260825"
          / "compile_shard.py")
EXPECTED_PARENT_SHA = (
    "54d05ebf86af9d75da0cc509e3094ce2e26516b84c73b8a50a36e71dbc9282b2")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()
old = '''    compatible_per_base[local_compatible] += 1
    completion_per_base[local_completions] += 1
'''
new = '''    if local_compatible:
        print("Q9_COMPATIBLE_BASE", base_index,
              "".join(str(value) for value in svalues),
              local_compatible, local_completions)
    compatible_per_base[local_compatible] += 1
    completion_per_base[local_completions] += 1
'''
assert source.count(old) == 1
source = source.replace(old, new)
scope = {"__file__": str(PARENT), "__name__": "__q9_base_list__"}
exec(compile(source, str(PARENT), "exec"), scope)
