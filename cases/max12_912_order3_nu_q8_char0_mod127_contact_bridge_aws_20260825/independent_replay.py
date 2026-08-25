#!/usr/bin/env python3
"""Independent reduction/frozen-endpoint replay for the cross-char producer."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import subprocess
import sys


P = 127
ROOT = Path(__file__).resolve().parents[2]
COMPILER = ROOT / "cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py"
FULL_SOURCE = ROOT / "cases/max12_912_order3_nu_q8_p127_full_contact_jacobian_aws_20260825/full_contact.py"
FULL_RESULT = ROOT / "cases/max12_912_order3_nu_q8_p127_full_contact_jacobian_aws_20260825/aws_box02_v1/result.json"
PINS = {
    COMPILER: "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545",
    FULL_SOURCE: "08a3d227accbc3c23a384db55bf44a050c5140e0034c70b95666fcd8fd51b6c8",
    FULL_RESULT: "804f9fbb095832e79a4f01ad870ed87a55921b78f34ff9f83ae946da04b70549",
}


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def reduce_exact(coefficients: list[list[int]]) -> list[int]:
    values = []
    for numerator, denominator in coefficients:
        if denominator % P == 0:
            raise RuntimeError(("nonintegral replay coefficient", numerator, denominator))
        values.append(numerator % P * pow(denominator % P, P - 2, P) % P)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values or [0]


def canonical_row_mod(exact_entries: list) -> list:
    result = []
    for monomial, numerator, denominator in exact_entries:
        if denominator % P == 0:
            raise RuntimeError(("nonintegral row scalar", numerator, denominator))
        value = numerator % P * pow(denominator % P, P - 2, P) % P
        if value:
            result.append([monomial, value])
    return result


def digest_json(value) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return sha256(encoded).hexdigest()


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: independent_replay.py producer.json")
    for path, expected in PINS.items():
        got = sha256(path.read_bytes()).hexdigest()
        if got != expected:
            raise RuntimeError((str(path), got, expected))
    producer = json.loads(Path(sys.argv[1]).read_text())
    if producer["status"] != "PASS" or producer["prime"] != P:
        raise RuntimeError("producer endpoint is not PASS/127")

    # Re-run the frozen mod-127 endpoint from its own source rather than
    # importing any arithmetic routine from producer.py.
    fresh = json.loads(subprocess.check_output([sys.executable, str(FULL_SOURCE)], text=True))
    frozen = json.loads(FULL_RESULT.read_text())
    if fresh != frozen:
        raise RuntimeError("fresh full-contact replay differs from frozen result")

    replay_coordinates = {
        name: reduce_exact(coefficients)
        for name, coefficients in producer["contact_coordinates_Q_exact"].items()
    }
    if replay_coordinates != fresh["contact_coordinates_low_to_high"]:
        raise RuntimeError("independent coordinate reduction mismatch")
    replay_det = reduce_exact(
        producer["full_relative_jacobian"]["determinant_Q_exact_low_to_high"]
    )
    if replay_det != fresh["full_relative_jacobian"]["determinant_low_to_high"]:
        raise RuntimeError("independent determinant reduction mismatch")

    replay_rows = {
        name: canonical_row_mod(entries)
        for name, entries in producer["source_rows_Q"].items()
    }
    if replay_rows != producer["source_rows_F127"]:
        raise RuntimeError("independent row reduction mismatch")
    if digest_json(replay_rows) != producer["source_rows_F127_sha256"]:
        raise RuntimeError("row reduction fingerprint mismatch")

    # An independent compiler load checks the exact row order and names.
    Q = load("q8_cross_replay_compiler", COMPILER)
    _, rows, imposed, names = Q.compile_quotient("approx")
    if tuple(imposed) != (1, 3, 5, 7, 2, 4) or names != ["w", "c", "d2", "d4", "x1", "x3", "x5"]:
        raise RuntimeError((imposed, names))

    if producer["scheme"]["localizer_does_not_invert_w"] is not True:
        raise RuntimeError("scheme identity inverted w")
    expected_rows = [
        "r1/t", "r3/t", "r5/t", "r7/t", "r2", "r4",
        "v*x5-x3+2*x5", "inv*x5*(x3-2*x5)-1",
    ]
    if producer["scheme"]["rows"] != expected_rows:
        raise RuntimeError("scheme row manifest mismatch")

    payload = {
        "case": "max12_912_order3_nu_q8_char0_mod127_contact_bridge_aws_20260825_independent_replay",
        "status": "PASS",
        "fresh_full_contact_sha256": sha256(
            json.dumps(fresh, indent=2, sort_keys=True).encode()
        ).hexdigest(),
        "coordinate_reduction_matches": True,
        "full_determinant_reduction_matches": True,
        "source_row_reduction_matches": True,
        "source_rows_F127_sha256": digest_json(replay_rows),
        "localizer_does_not_invert_w": True,
        "scope": "independent exact replay of source/contact/determinant reductions only",
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
