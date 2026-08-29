#!/usr/bin/env python3
"""Compile the frozen full 59-row generic Q(t) ordered-a1 decision."""

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
V43 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/compile_total_dvr_w30_v43.py"
V43_SHA256 = "0de6a2b279aeeab8c5a635c1d7658958f3f49f0f94f8473355d281cae9438b00"
CENSUS_ADDENDUM = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/PREREGISTRATION_CENSUS_ADDENDUM.md"
CENSUS_ADDENDUM_SHA256 = "266dfb8962cbeb1af73d4f03947670148b71a00eebd5e2a91fce9c78b99bf658"
FABLE_REVIEW = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-v43-compiler-postreview-delta-hostile-review-fable5-20260827.md"
FABLE_REVIEW_SHA256 = "ae8ecf1887a62afd873fc795d0eeec50ff0aac6e4954813931d09a34c8bfc31a"
TWO_FIBRE_REVIEW = ROOT / "xmodel/max12-812-order2-p0-total-rees-j2-a1-two-fibre-generic-eliminant-hostile-review-grok-20260827.md"
TWO_FIBRE_REVIEW_SHA256 = "bc539ba91600b95e5400e96635e8973ef6cb6454b9641c0c68d09a99aef0690f"
PREREG = HERE / "PREREGISTRATION.md"
TAG_PREFIX = "max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_v43g1_"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v43():
    if digest(V43) != V43_SHA256:
        fail(("V43 compiler hash", digest(V43), V43_SHA256))
    spec = importlib.util.spec_from_file_location("v43g1_source", V43)
    if spec is None or spec.loader is None:
        fail("V43 compiler import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def require_aws(phase: str) -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith(TAG_PREFIX)
        or f"_exact_{phase}_" not in tag
    ):
        fail("registered V43G1 AWS exact lane required")
    return tag


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"({value.numerator}/{value.denominator})"


def t_polynomial_text(tpoly: dict[int, Fraction]) -> str:
    pieces = []
    for degree, coefficient in sorted(tpoly.items()):
        if not coefficient:
            continue
        piece = fraction_text(coefficient)
        if degree:
            piece += "*t" if degree == 1 else f"*t^{degree}"
        pieces.append(piece)
    if not pieces:
        return "0"
    return ("+".join(pieces)).replace("+-", "-")


def monomial_factors(monomial, remove: frozenset[str]) -> list[str]:
    factors = []
    for name, exponent in sorted(monomial):
        if name in remove:
            continue
        factors.append(name if exponent == 1 else f"{name}^{exponent}")
    return factors


def generic_dehom_text(polynomial) -> str:
    pieces = []
    for monomial, tpoly in sorted(polynomial.items()):
        coefficient = t_polynomial_text(tpoly)
        if coefficient == "0":
            continue
        factors = monomial_factors(monomial, frozenset({"a1"}))
        pieces.append("*".join([f"({coefficient})", *factors]))
    return ("+".join(pieces) if pieces else "0").replace("+-", "-")


def special_dehom_text(polynomial) -> str:
    pieces = []
    for monomial, tpoly in sorted(polynomial.items()):
        coefficient = tpoly.get(0, Fraction(0))
        if not coefficient:
            continue
        factors = monomial_factors(monomial, frozenset({"a1", "ez9"}))
        pieces.append("*".join([fraction_text(coefficient), *factors]))
    return ("+".join(pieces) if pieces else "0").replace("+-", "-")


def emit_ideal(lines: list[str], name: str, texts: list[str]) -> None:
    if not texts:
        fail(("empty ideal", name))
    lines.append(f"ideal {name}=")
    for index, text in enumerate(texts):
        lines.append(text + ("," if index + 1 < len(texts) else ";"))


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--phase", choices=("decision", "lift"), required=True)
    args = cli.parse_args()
    tag = require_aws(args.phase)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)

    for path, expected in (
        (CENSUS_ADDENDUM, CENSUS_ADDENDUM_SHA256),
        (FABLE_REVIEW, FABLE_REVIEW_SHA256),
        (TWO_FIBRE_REVIEW, TWO_FIBRE_REVIEW_SHA256),
    ):
        if digest(path) != expected:
            fail(("custody hash", str(path), digest(path), expected))

    source = load_v43()
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
    if len(rho_only) != 8:
        fail(("rho-only row census", rho_only))

    ez9_records = []
    for row_index, item in enumerate(total_rows):
        for monomial, tpoly in sorted(item["polynomial"].items()):
            if dict(monomial).get("ez9", 0):
                ez9_records.append((row_index, item, monomial, tpoly))
    if len(ez9_records) != 1:
        fail(("ez9 occurrence census", len(ez9_records)))
    pivot_index, pivot, pivot_monomial, pivot_tpoly = ez9_records[0]
    pivot_after_dehom = {
        name: exponent for name, exponent in pivot_monomial if name != "a1"
    }
    if pivot_after_dehom != {"ez9": 1} or not pivot_tpoly:
        fail(("ez9 is not a Q(t)-linear pivot", pivot["name"], pivot_monomial, pivot_tpoly))

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
        fail(("post-elimination alphabet", len(reduced_variables), reduced_variables, special_variables))

    special_rows = [
        (item["name"], special_dehom_text(item["polynomial"]))
        for item in total_rows
        if item["name"] not in rho_only
    ]
    if len(special_rows) != 51 or any(text == "0" for _, text in special_rows):
        fail(("special-row census", special_rows))
    generic_rows = [(item["name"], generic_dehom_text(item["polynomial"])) for item in reduced_rows]
    if len(generic_rows) != 58 or any(text == "0" for _, text in generic_rows):
        fail(("generic-row census", generic_rows))

    script = output / f"full_generic_qt_{args.phase}.sing"
    special_basis = output / "special_groebner_basis.txt"
    generic_basis = output / "generic_groebner_basis.txt"
    generic_nf = output / "generic_normal_form.poly"
    multiplier_paths = [
        output / f"generic_multiplier_{index:02d}_{name}.poly"
        for index, (name, _) in enumerate(generic_rows, start=1)
    ]
    lines = [
        f"ring S0=0,({','.join(special_variables)}),dp;",
        "option(redSB);",
    ]
    emit_ideal(lines, "J0", [text for _, text in special_rows])
    lines += [
        "ideal G0=std(J0);",
        "poly nf0=reduce(1,G0);",
        f"write(\"{special_basis}\",G0);",
        "if (nf0!=0) { print(\"FAIL_V43G1_SPECIAL_FIBRE_CONTROL\"); quit; }",
        "print(\"V43G1_SPECIAL_FIBRE_UNIT=1\");",
        "kill S0;",
        f"ring K=(0,t),({','.join(reduced_variables)}),dp;",
        "option(redSB);",
    ]
    emit_ideal(lines, "J", [text for _, text in generic_rows])
    if args.phase == "decision":
        lines += ["ideal G=std(J);"]
    else:
        lines += [
            "matrix T;",
            "ideal G=liftstd(J,T);",
            "matrix BASISREPLAY=matrix(J)*T-matrix(G);",
            "if (BASISREPLAY!=0) { print(\"FAIL_V43G1_LIFTSTD_BASIS_REPLAY\"); quit; }",
            "print(\"V43G1_LIFTSTD_BASIS_REPLAY=1\");",
        ]
    lines += [
        "poly nf=reduce(1,G);",
        f"write(\"{generic_basis}\",G);",
        f"write(\"{generic_nf}\",nf);",
        "print(\"V43G1_GENERIC_BASIS_SIZE=\"+string(size(G)));",
        "if (nf!=0)",
        "{",
        "  print(\"V43G1_GENERIC_OUTCOME=nonunit\");",
        "  print(\"PASS_A1_FULL_GENERIC_QT_V43G1\");",
        "  quit;",
        "}",
        "print(\"V43G1_GENERIC_OUTCOME=unit\");",
    ]
    if args.phase == "decision":
        lines.append("print(\"V43G1_UNIT_STATUS=requires-tracked-lift\");")
    else:
        lines += [
            "matrix H=lift(G,ideal(1));",
            "matrix C=T*H;",
            "matrix UNITREPLAY=matrix(J)*C;",
            "if ((nrows(UNITREPLAY)!=1)||(ncols(UNITREPLAY)!=1)||(UNITREPLAY[1,1]!=1))",
            "{ print(\"FAIL_V43G1_GENERIC_UNIT_REPLAY\"); quit; }",
        ]
        for index, path in enumerate(multiplier_paths, start=1):
            lines.append(f"write(\"{path}\",C[{index},1]);")
        lines += [
            "print(\"V43G1_GENERIC_UNIT_REPLAY=1\");",
            "print(\"V43G1_UNIT_STATUS=exact-replayed-reduced-58-row-certificate\");",
        ]
    lines += ["print(\"PASS_A1_FULL_GENERIC_QT_V43G1\");", "quit;"]
    script.write_text("\n".join(lines) + "\n")

    result = {
        "schema_version": 1,
        "status": "PASS-A1-FULL-GENERIC-QT-V43G1-COMPILER",
        "registered_aws_lane": tag,
        "phase": args.phase,
        "coefficient_field": "Q(t), t=rho^2",
        "source_ring": "Q[t,a1,65 other positive variables]",
        "generic_ring": "Q(t)[64 positive variables after a1=1 and linear ez9 elimination]",
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
        "special_nonzero_row_count": len(special_rows),
        "special_nonzero_rows": [name for name, _ in special_rows],
        "v43_sha256": V43_SHA256,
        "census_addendum_sha256": CENSUS_ADDENDUM_SHA256,
        "fable_review_sha256": FABLE_REVIEW_SHA256,
        "two_fibre_review_sha256": TWO_FIBRE_REVIEW_SHA256,
        "preregistration_sha256": digest(PREREG),
        "singular_script": str(script),
        "singular_script_sha256": digest(script),
        "special_basis_path": str(special_basis),
        "generic_basis_path": str(generic_basis),
        "generic_normal_form_path": str(generic_nf),
        "multiplier_paths": [str(path) for path in multiplier_paths] if args.phase == "lift" else [],
        "outcome_semantics": {
            "nonunit": "decisive only after completed exact full standard basis",
            "unit_decision": "provisional until tracked multiplier and converter replay",
            "failed_or_incomplete": "no verdict",
        },
    }
    result_path = output / "compiler_result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("V43G1_RHO_ONLY_ROWS=" + ",".join(rho_only), flush=True)
    print(f"V43G1_EZ9_PIVOT={pivot['name']}", flush=True)
    print("PASS-A1-FULL-GENERIC-QT-V43G1-COMPILER")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()

