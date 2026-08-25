#!/usr/bin/env python3
"""Direct integer replay of a SAT model from the leading-form gate."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
import re
from pathlib import Path


ROOT = Path(os.environ["JC2_ROOT"])
EMITTER = (ROOT / "cases/as_b9_max12_leading_proportional_3p11_20260825"
           / "emit_leading_proportional.py")
EXPECTED = os.environ["EXPECTED_EMITTER_SHA256"]
payload = EMITTER.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED
scope = {"__file__": str(EMITTER), "__name__": "__leading_emitter__"}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(payload, str(EMITTER), "exec"), scope)

text = Path(os.environ["MODEL_PATH"]).read_text()
if "define-fun" in text:
    values = {name: int(value, 16) for name, value in re.findall(
        r"\(define-fun ([sw][0-9]+).*?\n\s+#x([0-9a-fA-F]+)\)", text, re.S)}
else:
    values = {name: int(value, 2) for name, value in re.findall(
        r"^([sw][0-9]+) ([01]+)$", text, re.M)}
assert all(values.get(f"s{i}") in (0, 1, 2) for i in range(165))
assert all(values.get(f"w{i}") in (0, 1, 2) for i in range(182))

T = list(scope["T_base"])
for index, direction in enumerate(scope["directions"]):
    scalar = values[f"s{index}"]
    T = [value + scalar * delta for value, delta in zip(T, direction)]
left_T, right_T = scope["correction"](T)
fresh = [values[f"w{i}"] for i in range(182)]
left_W, right_W = scope["correction"](fresh)
P = scope["add"](scope["p5"], scope["sc"](243, left_T),
                 scope["sc"](3 ** 10, left_W))
Q = scope["add"](scope["q5"], scope["sc"](243, right_T),
                 scope["sc"](3 ** 10, right_W))
determinant = scope["jac"](P, Q)
modulus = 3 ** 11
assert all(scope["coefficient"](determinant, xy) % modulus
           == (1 if xy == (0, 0) else 0) for xy in scope["slots"])
y12 = (0, 12)
qy = Q.get(y12, 0)
assert qy % 3
for xy in scope["support"]:
    if sum(xy) == 12:
        assert (P.get(xy, 0) * qy - P.get(y12, 0) * Q.get(xy, 0)) % modulus == 0
result = {
    "status": "PASS-AS-B9-D12-LEADING-PROPORTIONAL-SAT-REPLAY",
    "model_sha256": hashlib.sha256(
        Path(os.environ["MODEL_PATH"]).read_bytes()).hexdigest(),
    "literal_determinant_mod177147_passed": True,
    "literal_leading_cross_products_mod177147_passed": True,
    "q_y12_mod3": qy % 3,
    "P12_zero_mod177147": all(P.get(xy, 0) % modulus == 0
                               for xy in scope["support"] if sum(xy) == 12),
    "P_support": [[i, j, value] for (i, j), value in sorted(P.items())],
    "Q_support": [[i, j, value] for (i, j), value in sorted(Q.items())],
    "determinant_sha256": hashlib.sha256(
        repr(sorted(determinant.items())).encode()).hexdigest(),
}
encoded = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
Path(os.environ["REPLAY_OUTPUT_JSON"]).write_bytes(encoded + b"\n")
print(result["status"])
print("P12_zero", result["P12_zero_mod177147"])
print("determinant_sha256", result["determinant_sha256"])
print("result_sha256", hashlib.sha256(encoded + b"\n").hexdigest())
