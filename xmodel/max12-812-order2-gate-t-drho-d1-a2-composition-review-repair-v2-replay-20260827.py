#!/usr/bin/env python3
"""Additive R1 custody repair for the reviewed D(rho) / D1 a=2 contact."""

from __future__ import annotations

from hashlib import sha256
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = ROOT / "xmodel/max12-812-order2-gate-t-drho-d1-a2-composition-replay-20260827.py"

PINS = {
    ROOT / "xmodel/max12-812-order2-gate-t-drho-d1-a2-composition-sol-20260827.md":
        "db0ecebf37cf8283c27e36ed8f0ba10ae9bcf1887d1854affe73cf61c8f367cd",
    ORIGINAL:
        "33514275318db4ce7ba01adae1f1260f416d3b47734cc4bc10b0217acbed51cd",
    ROOT / "xmodel/max12-812-order2-gate-t-drho-d1-a2-composition-hostile-review-fable5-20260827.md":
        "518d4b250fa797d64d748017488f5f9daa3900b900f2e91000ca7124d08a220f",
    ROOT / "xmodel/max12-812-order2-gate-t-kummer-row-bridge-erratum-sol-20260827.md":
        "614ddcdb17ae233cd2babea5b45f329f57a7e28e13c7bc0616e78c6bc1731571",
    ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/export_allrows_g15_v22r1.py":
        "d9f23a279b39b45ca27717a00493a6e928d1042007bc2c3c183eb2d239882768",
    ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/compiled/Tg15_1_q.poly":
        "4d237049cdd6fbaf05a14dcda0710fdb1660058241b0b3a72e1c0c473e7a40ba",
    ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/compiled/Tg15_2_q.poly":
        "5a438032b3d558131246d3022006b68cc424f4c09bfcef0215e8ce8ea76e0e69",
    ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/compiled/Tg15_3_q.poly":
        "53d513df5003c5b0e60a50aff59779d9c921374e8878dea8e7ba9f3152d294d4",
    ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/compiled/Tg15_4_q.poly":
        "2cf0b1d34df224ba0df2b60bdd7b8144fd733d35133edd851c91d27a9b830748",
    ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/compiled/Tg15_5_q.poly":
        "26e2f4ef586955dddd1d694343f1bf29f28f050e4da61f386b2e11fb44a08f08",
    ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/compiled/Tg15_6_q.poly":
        "786c6bb976305614cc0945b2ebf0d78600fb9a96aefa1553248ff8f473b5c51e",
    ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1/compiled/Tg15_7_q.poly":
        "1b3eb2ae0963ee0044a209d91f8dc3ca9ef4d11c3dd47633d799219449bfcddd",
    ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json":
        "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    ROOT / "cases/max12_812_order2_square_owner_cge3_universal_20260826/compile_cge3_universal.py":
        "352ad4f2d10df80e7edcc5179a8c46dfc55b4f7ce07762fb06d2109a9da1da23",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_original():
    spec = importlib.util.spec_from_file_location("a2_original_replay", ORIGINAL)
    if spec is None or spec.loader is None:
        raise RuntimeError("original replay import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    for path, expected in PINS.items():
        actual = digest(path)
        if actual != expected:
            raise RuntimeError(("pin", str(path.relative_to(ROOT)), actual, expected))
    original = load_original()
    if len(original.custody_check()) != 12:
        raise RuntimeError("original custody census")
    if not all(original.construction_path_check()["sentinels"].values()):
        raise RuntimeError("construction sentinels")
    if original.support_window_check()["grades"] != [15, 16]:
        raise RuntimeError("window")
    if len(original.deck_allocation_check()["samples"]) != 3:
        raise RuntimeError("allocation samples")
    if original.coverage_negative_control()["ambient_nonempty"] is not True:
        raise RuntimeError("coverage negative control")
    explicit_later_zero = {
        "k1", "k2c", "k10_i(i>=3)", "k6_i(i>=1)", "k2_i(i>=1)",
    }
    if len(explicit_later_zero) != 5:
        raise RuntimeError("explicit later-zero map")
    print("PASS-GATE-T-DRHO-D1-A2-REVIEW-REPAIR-V2")
    print("ORIGINAL_PINS=12")
    print("ADDITIONAL_ERRATUM_PINS=10")
    print("REPAIR_TOTAL_PINS=14")
    print("ROW_LEVEL_MATH=IMPORTED_FROM_FABLE5_INDEPENDENT_RECONSTRUCTION")
    print("REPLAY_ROLE=CUSTODY_AND_TRANSCRIPTION_ONLY")


if __name__ == "__main__":
    main()

