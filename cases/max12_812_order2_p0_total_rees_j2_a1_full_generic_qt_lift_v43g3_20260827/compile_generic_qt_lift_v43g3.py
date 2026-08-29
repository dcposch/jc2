#!/usr/bin/env python3
"""Compile a tracked exact Bezout lift for the frozen V43G2 unit decision."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
G2_CASE = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_v43g2_20260827"
G2_COMPILER = G2_CASE / "compile_generic_only_qt_v43g2.py"
G2_COMPILER_SHA256 = "4ce93300474ec1a86cb9a435fbb3d780b3e121a946796a07f1cd0f8a73bd0a99"
G2_PREREG = G2_CASE / "PREREGISTRATION.md"
G2_PREREG_SHA256 = "2545d70dd88700318c45a6a1a337f63b28379cef2f8760dd3481ba2d7bb2f6c8"
G2_RESULT = G2_CASE / "RESULT.md"
G2_RESULT_SHA256 = "60b76bd4d3a8106a1e670073ae1f84218e1d62ae21187d79d75abf0bbcc48028"
G2_FREEZE = G2_CASE / "FREEZE.sha256"
G2_FREEZE_SHA256 = "bbb8b2d637be3458c0e67cfabbe3fa594ea521cb6a1151a5a242f937abf4c04d"
G2_AWS = G2_CASE / "aws_box02_decision_20260827T105200Z/compiled"
G2_COMPILER_RESULT = G2_AWS / "compiler_result.json"
G2_COMPILER_RESULT_SHA256 = "fac99098b36f5875b53c8d66439f34ca59b47e7f25a58f97dba1cb8cddd3806c"
G2_SCRIPT = G2_AWS / "generic_only_qt_decision.sing"
G2_SCRIPT_SHA256 = "7e3149d9ff89274e31c1068a51903dd9e2e716168141bd6286fa6b47d56328b3"
PREREG = HERE / "PREREGISTRATION.md"
TAG_PREFIX = "max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_lift_v43g3_"
EXPECTED_RHO_ONLY = [
    "Tg11_2", "Tg11_3", "Tg11_5", "Tg11_7",
    "Tg12_5", "Tg12_7", "Tg13_7", "Tg14_6",
]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load(path: Path, expected: str, name: str):
    actual = digest(path)
    if actual != expected:
        fail(("module hash", str(path), actual, expected))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("module import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith(TAG_PREFIX)
        or "_exact_lift_" not in tag
    ):
        fail("registered V43G3 AWS exact lift lane required")
    return tag


def extract_g2_payload(result: dict) -> tuple[str, list[str]]:
    lines = G2_SCRIPT.read_text().splitlines()
    if len(lines) < 4 or not lines[0].startswith("ring K=(0,t),"):
        fail("G2 ring declaration")
    try:
        start = lines.index("ideal J=") + 1
    except ValueError:
        fail("G2 ideal declaration")
    count = result["reduced_row_count"]
    entries = lines[start:start + count]
    if len(entries) != 58 or entries[-1][-1:] != ";":
        fail("G2 ideal payload length")
    return lines[0], entries


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    args = cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)

    for path, expected in (
        (G2_PREREG, G2_PREREG_SHA256),
        (G2_RESULT, G2_RESULT_SHA256),
        (G2_FREEZE, G2_FREEZE_SHA256),
        (G2_COMPILER_RESULT, G2_COMPILER_RESULT_SHA256),
        (G2_SCRIPT, G2_SCRIPT_SHA256),
    ):
        actual = digest(path)
        if actual != expected:
            fail(("custody hash", str(path), actual, expected))

    g2_result = json.loads(G2_COMPILER_RESULT.read_text())
    if (
        g2_result["status"] != "PASS-A1-GENERIC-ONLY-QT-V43G2-COMPILER"
        or g2_result["reduced_row_count"] != 58
        or len(g2_result["reduced_variables"]) != 64
        or g2_result["singular_script_sha256"] != G2_SCRIPT_SHA256
    ):
        fail("G2 result semantics")
    g2_ring, g2_entries = extract_g2_payload(g2_result)

    g2 = load(G2_COMPILER, G2_COMPILER_SHA256, "v43g3_g2_source")
    g1 = g2.load_g1()
    source = g1.load_v43()
    (parser, _, total_rows, frozen_hashes, total_hashes, variables,
     frozen_variables, general_only, nonzero_general) = source.reconstruct_rows()
    if (
        len(frozen_hashes) != 70
        or len(total_rows) != 59
        or nonzero_general != 59
        or len(variables) != 66
        or len(frozen_variables) != 65
        or general_only != ["ez9"]
    ):
        fail("literal full-total census")
    rho_only = [
        item["name"] for item in total_rows
        if not any(tpoly.get(0, Fraction(0)) for tpoly in item["polynomial"].values())
    ]
    if rho_only != EXPECTED_RHO_ONLY:
        fail(("rho-only row census", rho_only))

    ez9_records = []
    for row_index, item in enumerate(total_rows):
        for monomial, tpoly in sorted(item["polynomial"].items()):
            if dict(monomial).get("ez9", 0):
                ez9_records.append((row_index, item, monomial, tpoly))
    if len(ez9_records) != 1:
        fail(("ez9 occurrence census", len(ez9_records)))
    pivot_index, pivot, pivot_monomial, pivot_tpoly = ez9_records[0]
    if (
        pivot["name"] != "Tg19_2"
        or dict(pivot_monomial) != {"a1": 1, "ez9": 1}
        or pivot_tpoly != {1: Fraction(3, 8)}
    ):
        fail(("exact ez9 pivot drift", pivot["name"], pivot_monomial, pivot_tpoly))

    reduced_rows = [item for index, item in enumerate(total_rows) if index != pivot_index]
    reduced_variables = sorted(set(variables) - {"a1", "ez9"})
    if len(reduced_rows) != 58 or len(reduced_variables) != 64:
        fail("reduced census")
    generic_rows = [
        (item["name"], g1.generic_dehom_text(item["polynomial"]))
        for item in reduced_rows
    ]
    expected_ring = f"ring K=(0,t),({','.join(reduced_variables)}),dp;"
    expected_entries = [
        text + ("," if index + 1 < len(generic_rows) else ";")
        for index, (_, text) in enumerate(generic_rows)
    ]
    if g2_ring != expected_ring or g2_entries != expected_entries:
        mismatch = next((i for i, pair in enumerate(zip(g2_entries, expected_entries))
                         if pair[0] != pair[1]), None)
        fail(("G2 literal ideal mismatch", mismatch))

    script = output / "generic_qt_tracked_lift.sing"
    basis = output / "generic_lift_basis.txt"
    transform = output / "generic_lift_transform.matrix"
    coefficients = output / "generic_bezout_coefficients.matrix"
    multiplier_paths = [
        output / f"generic_multiplier_{index:02d}_{name}.poly"
        for index, (name, _) in enumerate(generic_rows, start=1)
    ]
    lines = [expected_ring, "option(redSB);", "ideal J=", *expected_entries]
    lines += [
        "matrix T;",
        "ideal G=liftstd(J,T);",
        "matrix BASISREPLAY=matrix(J)*T-matrix(G);",
        "if (BASISREPLAY!=0) { print(\"FAIL_V43G3_LIFTSTD_BASIS_REPLAY\"); quit; }",
        "print(\"V43G3_LIFTSTD_BASIS_REPLAY=1\");",
        "poly nf=reduce(1,G);",
        f"write(\"{basis}\",G);",
        f"write(\"{transform}\",T);",
        "if (nf!=0) { print(\"FAIL_V43G3_INCONSISTENT_NONUNIT\"); quit; }",
        "matrix H=lift(G,ideal(1));",
        "matrix C=T*H;",
        "matrix UNITREPLAY=matrix(J)*C;",
        "if ((nrows(UNITREPLAY)!=1)||(ncols(UNITREPLAY)!=1)||(UNITREPLAY[1,1]!=1))",
        "{ print(\"FAIL_V43G3_GENERIC_UNIT_REPLAY\"); quit; }",
        f"write(\"{coefficients}\",C);",
        "int nonzero=0; int ci;",
        "for (ci=1;ci<=nrows(C);ci++) { if (C[ci,1]!=0) { nonzero=nonzero+1; } }",
    ]
    for index, path in enumerate(multiplier_paths, start=1):
        lines.append(f"write(\"{path}\",C[{index},1]);")
    lines += [
        "print(\"V43G3_GENERIC_BASIS_SIZE=\"+string(size(G)));",
        "print(\"V43G3_NONZERO_MULTIPLIERS=\"+string(nonzero));",
        "print(\"V43G3_GENERIC_UNIT_REPLAY=1\");",
        "print(\"PASS_A1_GENERIC_QT_LIFT_V43G3\");",
        "quit;",
    ]
    script.write_text("\n".join(lines) + "\n")

    result = {
        "schema_version": 1,
        "status": "PASS-A1-GENERIC-QT-LIFT-V43G3-COMPILER",
        "registered_aws_lane": tag,
        "coefficient_field": "Q(t), t=rho^2",
        "term_order": "dp",
        "literal_source_rows": len(total_rows),
        "literal_source_variables": len(variables),
        "rho0_source_variables": len(frozen_variables),
        "rho_only_rows": rho_only,
        "pivot_source_row": pivot["name"],
        "pivot_source_row_sha256": total_hashes[pivot["name"]],
        "pivot_monomial": [[name, exponent] for name, exponent in pivot_monomial],
        "pivot_t_coefficients": [[degree, value.numerator, value.denominator]
                                 for degree, value in sorted(pivot_tpoly.items())],
        "pivot_multiplier": "0 in the reconstructed 59-row identity",
        "reduced_row_count": len(generic_rows),
        "reduced_rows": [name for name, _ in generic_rows],
        "reduced_row_sha256": {item["name"]: total_hashes[item["name"]]
                               for item in reduced_rows},
        "reduced_variables": reduced_variables,
        "g2_ring_and_all_58_entries_byte_equal": True,
        "g2_compiler_result_sha256": G2_COMPILER_RESULT_SHA256,
        "g2_decision_script_sha256": G2_SCRIPT_SHA256,
        "g2_case_result_sha256": G2_RESULT_SHA256,
        "g2_case_freeze_sha256": G2_FREEZE_SHA256,
        "preregistration_sha256": digest(PREREG),
        "singular_script": str(script),
        "singular_script_sha256": digest(script),
        "basis_path": str(basis),
        "transform_path": str(transform),
        "coefficient_matrix_path": str(coefficients),
        "multiplier_paths": [str(path) for path in multiplier_paths],
        "outcome_semantics": "terminal PASS requires exact basis and unit matrix replays",
    }
    result_path = output / "compiler_result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("V43G3_LITERAL_ROWS=59", flush=True)
    print("V43G3_REDUCED_ROWS=58", flush=True)
    print("V43G3_G2_PAYLOAD_BYTE_EQUAL=1", flush=True)
    print("PASS-A1-GENERIC-QT-LIFT-V43G3-COMPILER")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
