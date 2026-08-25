#!/usr/bin/env python3
"""AWS-only V2 wrapper: preserve exact tails and add mandatory j saturation."""

from __future__ import annotations

import contextlib
from hashlib import sha256
import importlib.util
import io
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = HERE / "compile_rees.py"
ERRATUM = ROOT / "xmodel/max12-812-order2-u2-62-strict-rees-client-erratum-v2-20260825.md"
EXPECTED_BASE_SHA256 = "840a12e29386d37801f986e39273c3fb34f5542019cc1da7043ee1730dcb31f2"
EXPECTED_ERRATUM_SHA256 = "5aa954cbe6396ef5de353519eaf10aed567aec55964bb197c9eb1576b131c10b"
EXPECTED_ALL_TAILS_SHA256 = "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_base():
    if digest(BASE) != EXPECTED_BASE_SHA256:
        fail("V1 exact-tail compiler hash mismatch")
    if digest(ERRATUM) != EXPECTED_ERRATUM_SHA256:
        fail("V2 client erratum hash mismatch")
    spec = importlib.util.spec_from_file_location("max12_812_rees_v1_frozen", BASE)
    if spec is None or spec.loader is None:
        fail("cannot load frozen V1 compiler")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_base()
    original_emit = module.emit_singular
    old_block = "\n".join([
        "list SR=sat(KT,ideal(rho)); ideal K=SR[1];",
        "ideal boundary=K,tau,rho;",
    ])
    new_block = "\n".join([
        "list SR=sat(KT,ideal(rho)); ideal KR=SR[1];",
        "list SJ=sat(KR,ideal(j)); ideal K=SJ[1];",
        "ideal boundary=K,tau,rho;",
    ])

    def emit_v2(path: Path, ring, tails) -> None:
        original_emit(path, ring, tails)
        text = path.read_text()
        if text.count(old_block) != 1:
            fail("V1 saturation block absent or non-unique")
        text = text.replace(old_block, new_block)
        marker = 'print("STRICT_REES_H_SIZE="+string(size(H)));'
        if text.count(marker) != 1:
            fail("V1 endpoint marker absent or non-unique")
        text = text.replace(
            marker,
            'print("STRICT_REES_J_NONZERO_SATURATED=1");\n' + marker,
        )
        path.write_text(text)

    module.emit_singular = emit_v2
    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        module.main()

    if len(sys.argv) != 2:
        fail("usage: compile_rees_v2.py OUTPUT_DIRECTORY")
    output = Path(sys.argv[1]).resolve()
    v1_path = output / "strict_rees.sing"
    v2_path = output / "strict_rees_v2.sing"
    if not v1_path.is_file():
        fail("patched V2 Singular input was not emitted")
    text = v1_path.read_text()
    required = [
        "list ST=sat(I,ideal(tau)); ideal KT=ST[1];",
        "list SR=sat(KT,ideal(rho)); ideal KR=SR[1];",
        "list SJ=sat(KR,ideal(j)); ideal K=SJ[1];",
        "STRICT_REES_J_NONZERO_SATURATED=1",
    ]
    if any(token not in text for token in required):
        fail("V2 source audit failed")
    if "ideal lowerloads=" in text or "sat(KR,ideal(k10" in text:
        fail("DS lower-load optimization leaked into canonical V2")
    v1_path.rename(v2_path)

    result_path = output / "result.json"
    payload = json.loads(result_path.read_text())
    if payload.get("all_tails_sha256") != EXPECTED_ALL_TAILS_SHA256:
        fail("exact tails changed in V2 wrapper")
    payload["base_compiler_status"] = payload.get("status")
    payload["base_compiler_stdout_sha256"] = sha256(
        captured.getvalue().encode()
    ).hexdigest()
    payload["client_erratum_v2_sha256"] = EXPECTED_ERRATUM_SHA256
    payload["compiler_v1_sha256"] = EXPECTED_BASE_SHA256
    payload["scope"]["j_nonzero_localization"] = "SATURATED"
    payload["scope"]["lower_load_ds_optimization"] = "NOT_APPLIED"
    payload["scope"]["strict_saturation"] = "EMITTED_V2_NOT_RUN"
    payload["status"] = "PASS-MAX12-812-ORDER2-U2-62-TAIL-COMPILER-V2-JSAT"
    payload["strict_rees_v2_sha256"] = digest(v2_path)
    result_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
