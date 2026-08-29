#!/usr/bin/env python3
"""Desk custody/logic replay for the reviewed A2D2 additive repair."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT / "xmodel/max12-812-order2-gate-t-drho-unique-ac-ledger-a2d2-composition-replay-20260827.py"
SYZYGY = ROOT / "xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-replay-20260827.py"
G20_Q = ROOT / "cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r3_20260827/aws_qcross_r6a/RESULT_q.json"
G20_P = ROOT / "cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r3_20260827/aws_p65521_r6b/RESULT_p65521.json"
G20_CROSS = ROOT / "cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r3_20260827/aws_qcross_r6a/RESULT_CROSS.json"

PINS = {
    ROOT / "xmodel/max12-812-order2-gate-t-drho-unique-ac-ledger-a2d2-composition-sol-20260827.md":
        "1d086a79b0d4e7a6a9905391dc13acf4571d766292c58c7b2f25b1c673141457",
    ORIGINAL:
        "0c124179041b1a3cc115e24d1e5bce4f7ca9edcbc0e3224c302dd20d85b8867e",
    ROOT / "xmodel/max12-812-order2-gate-t-drho-unique-ac-ledger-a2d2-composition-hostile-review-opus5-20260827.md":
        "23007a2bb15e866f87a05bdff9f7a0ea0f1b05588d721d4b03bd377f0b89ce12",
    ROOT / "cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r3_20260827/RESULT.md":
        "4be1ca0afc027e73661f3ceeecb639ecdaf3606043d408df8cdbfa22f7937fc8",
    ROOT / "cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r3_20260827/PASS_EVIDENCE.sha256":
        "3b9065705c06fc79e54fba83de2c1caa591d2970c6cbf0c62f773313d6a91506",
    G20_Q:
        "c8a14e4fc4c627263e75f963838293dbe88ee46d17c770b7be16eb76799418cf",
    G20_P:
        "4b4b49b52e29a69c4bae6d88e7bc456dc96db7b299a67652d74287b2696df9e2",
    G20_CROSS:
        "6b3f87e68cd30fe9cb35934bad4fa8cebd1ad0181d5212aa7165ee728f6567bb",
    ROOT / "xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-sol-20260827.md":
        "2354703a559a5da2b4f2032560a5740b2cda1f3160f5c6598dcdbe1c4c1432be",
    SYZYGY:
        "56edb06f57c657534b46f1c406363de7821e240ccc1eb7d8529be7eeb2c5c3f4",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(("import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    for path, expected in PINS.items():
        actual = digest(path)
        if actual != expected:
            raise RuntimeError(("pin", str(path.relative_to(ROOT)), actual, expected))

    original = load(ORIGINAL, "a2d2_original")
    ledger = original.coverage_ledger_check()
    if (
        not original.custody_check()
        or "18 baselines" not in ledger["parametric_groups"]["d2_d3_finite"]
        or ledger["sentinel_baselines_checked"] != 119
    ):
        raise RuntimeError("original ledger/custody")
    shift = original.finite_jet_map_check()["shift_check"]
    if (shift["D1_A_order"], shift["D1_C_order"], shift["D1_R_order"]) != (2, 4, 3):
        raise RuntimeError("original map contact")

    q, p, cross = (json.loads(path.read_text()) for path in (G20_Q, G20_P, G20_CROSS))
    if q["status"] != "PASS-ACT-TOT-G20-CUSTODY-V44R3-Q":
        raise RuntimeError("G20 Q")
    if p["status"] != "PASS-ACT-TOT-G20-CUSTODY-V44R3-P65521":
        raise RuntimeError("G20 p")
    if cross["status"] != "PASS-ACT-TOT-G20-CUSTODY-V44R3-CROSSLANE":
        raise RuntimeError("G20 cross")
    if len(q["row_truncation_through20_canonical_sha256"]) != 7:
        raise RuntimeError("G20 truncation census")

    syzygy = load(SYZYGY, "a2d2_syzygy")
    syzygy.main()

    # The two cells preceding the old base are named only as (a,c,r_floor).
    preceding = [(1, 3, 2), (1, 4, 2)]
    if preceding != sorted(preceding, key=lambda cell: (10 + cell[0] + cell[1], cell)):
        raise RuntimeError("preceding-cell convention")

    print("PASS-KGT-DRHO-UAC-A2D2-REVIEW-REPAIR-V2")
    print("TUPLE_CONVENTION=(a,c,r_floor)")
    print("G20_GENERAL_RHO_CONSTRUCTION_CUSTODY=Q_P_CROSS_PASS")
    print("PRIMARY_PROOF=THREE_ROW_RADICAL_SYZYGY")
    print("MOVING_ROOT_ENDPOINT=CORROBORATING_ONLY")


if __name__ == "__main__":
    main()
