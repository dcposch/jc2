#!/usr/bin/env python3
"""Source-pinned V2 repair of the global Q5/H6 direct replay."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_d7_global_q5_h6_20260825"
          / "replay_global_q5_h6.py")
EXPECTED_PARENT_SHA = (
    "75e153c3ea2a0de9ce2bf26ba13893e44a4092cd8b1bdd1d45256f12ac023eea")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()

old = '''P5 = nadd(P, nscale(81, H6))
Q5 = nadd(Q, nscale(81, J6))
'''
new = '''P = nadd({(1, 0): 1, (3, 0): -1}, nscale(3, source_data["U"]),
         nscale(9, C), nscale(27, W), nscale(81, H7))
Q = nadd({(0, 1): 1}, nscale(3, source_data["V"]),
         nscale(9, D), nscale(27, Z), nscale(81, J7))
P5 = nadd(P, nscale(81, H6))
Q5 = nadd(Q, nscale(81, J6))
'''
assert source.count(old) == 1
source = source.replace(old, new)

scope = {"__file__": str(PARENT), "__name__": "__global_q5_h6_replay_v2__"}
exec(compile(source, str(PARENT), "exec"), scope)
