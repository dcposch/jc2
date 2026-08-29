#!/usr/bin/env python3
"""Compile the additive generic-only twin of V43G1's exact Q(t) decision."""

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
G1 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_v43g1_20260827/compile_full_generic_qt_v43g1.py"
G1_SHA256 = "03b76b7b9592abf9c13ccb3a8ea716c9b43d601f7ce26a37428733435cf6e957"
G1_PREREG = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_v43g1_20260827/PREREGISTRATION.md"
G1_PREREG_SHA256 = "8a4727c2524134583885e06bd0d7d238068231ea971ac36f51f13ac13123afe3"
FIELD_BRIDGE = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_v43g1_20260827/FIELD_BRIDGE_ADDENDUM.md"
FIELD_BRIDGE_SHA256 = "25f5200017d0fb95ea0ff5aead291acfcef651c400cfcf4deb272653438a09df"
V42_REPLAY = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_radical_cascade_closure_v42_20260827/replay_a1_cascade_closure_v42.py"
V42_REPLAY_SHA256 = "f4ec72933793bf08aabc600df7cdcd47b8de2c54f45c0d30341e13ac0b676459"
V42_REPORT = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-radical-cascade-closure-v42-sol-20260827.md"
V42_REPORT_SHA256 = "5d4c42fff1ad563586e8ae8736c3938efb1ae48467dfab96ae7fd9b861e7037f"
V42_REVIEW = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-radical-cascade-closure-v42-hostile-review-opus5-20260827.md"
V42_REVIEW_SHA256 = "a4f6b93181526cd8907c6412faeef2ed2e69012a5820e939079ba4cf891f3439"
TWO_FIBRE = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-two-fibre-generic-decision-theorem-repaired-sol-20260827.md"
TWO_FIBRE_SHA256 = "a7f96b0d8ac5867cefe7984f87a44ecd30ef3780df731e8b3acc3dc9db159ec6"
TWO_FIBRE_REVIEW = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-two-fibre-generic-eliminant-hostile-review-grok-20260827.md"
TWO_FIBRE_REVIEW_SHA256 = "bc539ba91600b95e5400e96635e8973ef6cb6454b9641c0c68d09a99aef0690f"
PREREG = HERE / "PREREGISTRATION.md"
TAG_PREFIX = "max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_v43g2_"
EXPECTED_RHO_ONLY = [
    "Tg11_2", "Tg11_3", "Tg11_5", "Tg11_7",
    "Tg12_5", "Tg12_7", "Tg13_7", "Tg14_6",
]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_g1():
    if digest(G1) != G1_SHA256:
        fail(("V43G1 compiler hash", digest(G1), G1_SHA256))
    spec = importlib.util.spec_from_file_location("v43g2_g1_source", G1)
    if spec is None or spec.loader is None:
        fail("V43G1 compiler import")
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
        or "_exact_decision_" not in tag
    ):
        fail("registered V43G2 AWS exact decision lane required")
    return tag


def emit_ideal(lines: list[str], name: str, texts: list[str]) -> None:
    if not texts:
        fail(("empty ideal", name))
    lines.append(f"ideal {name}=")
    for index, text in enumerate(texts):
        lines.append(text + ("," if index + 1 < len(texts) else ";"))


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    args = cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)

    for path, expected in (
        (G1_PREREG, G1_PREREG_SHA256),
        (FIELD_BRIDGE, FIELD_BRIDGE_SHA256),
        (V42_REPLAY, V42_REPLAY_SHA256),
        (V42_REPORT, V42_REPORT_SHA256),
        (V42_REVIEW, V42_REVIEW_SHA256),
        (TWO_FIBRE, TWO_FIBRE_SHA256),
        (TWO_FIBRE_REVIEW, TWO_FIBRE_REVIEW_SHA256),
    ):
        actual = digest(path)
        if actual != expected:
            fail(("custody hash", str(path), actual, expected))

    g1 = load_g1()
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
        or "a1" not in variables
        or "ez9" not in variables
        or "t" in variables
    ):
        fail("literal full-total census")

    rho_only = [
        item["name"] for item in total_rows
        if not any(tpoly.get(0, Fraction(0)) for tpoly in item["polynomial"].values())
    ]
    if rho_only != EXPECTED_RHO_ONLY:
        fail(("rho-only row census", rho_only, EXPECTED_RHO_ONLY))

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
    if len(reduced_rows) != 58 or any(
        dict(monomial).get("ez9", 0)
        for item in reduced_rows
        for monomial in item["polynomial"]
    ):
        fail("ez9 elimination scope")
    reduced_variables = sorted(set(variables) - {"a1", "ez9"})
    special_variables = sorted(set(frozen_variables) - {"a1"})
    if len(reduced_variables) != 64 or reduced_variables != special_variables:
        fail(("post-elimination alphabet", reduced_variables, special_variables))
    generic_rows = [
        (item["name"], g1.generic_dehom_text(item["polynomial"]))
        for item in reduced_rows
    ]
    if len(generic_rows) != 58 or any(text == "0" for _, text in generic_rows):
        fail(("generic-row census", generic_rows))

    script = output / "generic_only_qt_decision.sing"
    generic_basis = output / "generic_groebner_basis.txt"
    generic_nf = output / "generic_normal_form.poly"
    lines = [
        f"ring K=(0,t),({','.join(reduced_variables)}),dp;",
        "option(redSB);",
    ]
    emit_ideal(lines, "J", [text for _, text in generic_rows])
    lines += [
        "ideal G=std(J);",
        "poly nf=reduce(1,G);",
        f"write(\"{generic_basis}\",G);",
        f"write(\"{generic_nf}\",nf);",
        "print(\"V43G2_GENERIC_BASIS_SIZE=\"+string(size(G)));",
        "if (nf!=0)",
        "{",
        "  print(\"V43G2_GENERIC_OUTCOME=nonunit\");",
        "  print(\"PASS_A1_GENERIC_ONLY_QT_V43G2\");",
        "  quit;",
        "}",
        "print(\"V43G2_GENERIC_OUTCOME=unit\");",
        "print(\"V43G2_UNIT_STATUS=requires-tracked-lift\");",
        "print(\"PASS_A1_GENERIC_ONLY_QT_V43G2\");",
        "quit;",
    ]
    script.write_text("\n".join(lines) + "\n")

    result = {
        "schema_version": 1,
        "status": "PASS-A1-GENERIC-ONLY-QT-V43G2-COMPILER",
        "registered_aws_lane": tag,
        "coefficient_field": "Q(t), t=rho^2",
        "source_ring": "Q[t,a1,65 other positive variables]",
        "generic_ring": "Q(t)[64 positive variables after a1=1 and linear ez9 elimination]",
        "term_order": "dp",
        "special_control": "external pinned reviewed V42; not recomputed in V43G2",
        "named_source_slots": len(frozen_hashes),
        "total_nonzero_rows": len(total_rows),
        "total_positive_variables": len(variables),
        "rho0_positive_variables": len(frozen_variables),
        "general_only_variables": general_only,
        "rho_only_rows": rho_only,
        "rho_only_row_sha256": {name: total_hashes[name] for name in rho_only},
        "ez9_pivot_row": pivot["name"],
        "ez9_pivot_row_sha256": total_hashes[pivot["name"]],
        "ez9_pivot_monomial": [[name, exponent] for name, exponent in pivot_monomial],
        "ez9_pivot_t_coefficients": [
            [degree, value.numerator, value.denominator]
            for degree, value in sorted(pivot_tpoly.items())
        ],
        "reduced_row_count": len(reduced_rows),
        "reduced_rows": [item["name"] for item in reduced_rows],
        "reduced_row_sha256": {item["name"]: total_hashes[item["name"]] for item in reduced_rows},
        "reduced_variables": reduced_variables,
        "v43g1_compiler_sha256": G1_SHA256,
        "v43g1_preregistration_sha256": G1_PREREG_SHA256,
        "field_bridge_sha256": FIELD_BRIDGE_SHA256,
        "v42_replay_sha256": V42_REPLAY_SHA256,
        "v42_report_sha256": V42_REPORT_SHA256,
        "v42_review_sha256": V42_REVIEW_SHA256,
        "two_fibre_theorem_sha256": TWO_FIBRE_SHA256,
        "two_fibre_review_sha256": TWO_FIBRE_REVIEW_SHA256,
        "preregistration_sha256": digest(PREREG),
        "singular_script": str(script),
        "singular_script_sha256": digest(script),
        "generic_basis_path": str(generic_basis),
        "generic_normal_form_path": str(generic_nf),
        "outcome_semantics": {
            "nonunit": "decisive only after completed exact full standard basis",
            "unit_decision": "provisional until tracked multiplier and converter replay",
            "failed_or_incomplete": "no verdict",
        },
    }
    result_path = output / "compiler_result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("V43G2_RHO_ONLY_ROWS=" + ",".join(rho_only), flush=True)
    print(f"V43G2_EZ9_PIVOT={pivot['name']}", flush=True)
    print("V43G2_SPECIAL_CONTROL=external-pinned-reviewed-V42", flush=True)
    print("PASS-A1-GENERIC-ONLY-QT-V43G2-COMPILER")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
