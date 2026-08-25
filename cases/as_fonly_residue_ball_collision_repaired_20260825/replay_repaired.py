#!/usr/bin/env python3
"""Source-pinned replay successor with an explicit AS-special-fibre check."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
PARENT = (ROOT / "cases/as_fonly_residue_ball_collision_20260825"
          / "replay_controls.py")
EXPECTED_PARENT_SHA = (
    "6835141d2b5eabcc41897e1280698902c39f65d12cabc89c10f3ddb6e9b10509")
payload = PARENT.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_PARENT_SHA
source = payload.decode()

old = '''    determinant = jacobian(left, right)
    expected = {
'''
new = '''    left_mod3 = {monomial: coefficient % 3
                 for monomial, coefficient in left.items()
                 if coefficient % 3}
    right_mod3 = {monomial: coefficient % 3
                  for monomial, coefficient in right.items()
                  if coefficient % 3}
    assert left_mod3 == {(1, 0): 1, (3, 0): 2}
    assert right_mod3 == {(0, 1): 1}
    determinant = jacobian(left, right)
    expected = {
'''
assert source.count(old) == 1
source = source.replace(old, new)

scope = {"__file__": str(PARENT), "__name__": "__main__"}
exec(compile(source, str(PARENT), "exec"), scope)
