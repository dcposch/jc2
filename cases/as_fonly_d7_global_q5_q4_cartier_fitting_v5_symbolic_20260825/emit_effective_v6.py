#!/usr/bin/env python3
"""Emit the fully transformed V6 parent source without executing the CAS gate."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
V6 = (ROOT / "cases/as_fonly_d7_global_q5_q4_cartier_fitting_v5_symbolic_20260825"
      / "analyze_cartier_fitting_v6.py")
EXPECTED = "f6c72654ff2be0f1dfdc78179f987c58f37c8ef469d0ce221c7f81e052956f01"
payload = V6.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
wrapper = payload.decode()

old = '''source = payload.decode()

marker ='''
new = '''source = payload.decode()
v5_terminal = ''' + "'''" + '''namespace = {"__file__": str(PARENT), "__name__": "__cartier_fitting_v5__"}
exec(compile(source, str(PARENT), "exec"), namespace)
''' + "'''" + '''
v5_emitter = ''' + "'''" + '''Path(os.environ["EFFECTIVE_V6_SOURCE"]).write_text(source)
''' + "'''" + '''
assert source.count(v5_terminal) == 1
source = source.replace(v5_terminal, v5_emitter)

marker ='''
assert wrapper.count(old) == 1
wrapper = wrapper.replace(old, new)

scope = {"__file__": str(V6), "__name__": "__emit_effective_v6__"}
exec(compile(wrapper, str(V6), "exec"), scope)

