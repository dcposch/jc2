#!/usr/bin/env python3
"""V23R1: retain the chart census; compare A00 only after qa1=0."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
V1 = HERE / "census_j2_typed_v23.py"
V1_SHA256 = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_v1():
    if digest(V1) != V1_SHA256:
        fail(("V1 implementation hash", digest(V1), V1_SHA256))
    spec = importlib.util.spec_from_file_location("j2_typed_v23_frozen", V1)
    if spec is None or spec.loader is None:
        fail("cannot import V1")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: census_j2_typed_v23r1.py OUTPUT_DIRECTORY")
    output = Path(sys.argv[1]).resolve()
    if output.exists():
        fail(("refuse overwrite", str(output)))
    output.mkdir(parents=True)
    (output / "a0_chart").mkdir()
    (output / "a1_ordered").mkdir()
    v1 = load_v1()

    inputs = v1.resolve_inputs()
    records: dict[str, object] = {}
    grade10_zero = {"a0_chart": 0, "a1_ordered": 0}
    pure_rows: dict[str, dict[str, object]] = {"a0_chart": {}, "a1_ordered": {}}
    point_rows: dict[str, dict[str, object]] = {"A00": {}, "A10": {}}

    for name, grade, row, path, input_hash in inputs:
        polynomial = v1.parse(path)
        if any(sum(v1.sigma_weight(variable) * exponent for variable, exponent in monomial) != grade for monomial in polynomial):
            fail(("input sigma homogeneity", name))
        if any(next((exponent for variable, exponent in monomial if variable == "rho"), 0) % 2 for monomial in polynomial):
            fail(("input rho parity", name))
        chart_polynomials = {
            "a0_chart": v1.specialize(polynomial, v1.J1, {"a1": (("a0", 1), ("qa1", 1))}),
            "a1_ordered": v1.specialize(polynomial, v1.J1 | {"a0"}, {}),
        }
        chart_record: dict[str, object] = {}
        for chart, specialized in chart_polynomials.items():
            exceptional = "a0" if chart == "a0_chart" else "a1"
            permitted = {exceptional, "qa1", "rho"} if chart == "a0_chart" else {exceptional, "rho"}
            pure = {
                monomial: coefficient
                for monomial, coefficient in specialized.items()
                if {variable for variable, _ in monomial} <= permitted
            }
            if pure:
                pure_rows[chart][name] = pure
            point = (
                v1.specialize(pure, frozenset({"qa1"}), {})
                if chart == "a0_chart" else pure
            )
            point_label = "A00" if chart == "a0_chart" else "A10"
            if point:
                point_rows[point_label][name] = point
            if grade == 10 and not specialized:
                grade10_zero[chart] += 1
            out_path = output / chart / f"{name}.poly"
            out_path.write_text(v1.polynomial_text(specialized) + "\n")
            variables = sorted({variable for monomial in specialized for variable, _ in monomial})
            chart_record[chart] = {
                "term_count": len(specialized),
                "variables": variables,
                "nuisance_variables": sorted(set(variables) - permitted),
                "pure_exceptional_terms": [
                    v1.serialize_term(monomial, coefficient)
                    for monomial, coefficient in sorted(pure.items())
                ],
                "output": str(out_path.relative_to(output)),
                "output_sha256": digest(out_path),
            }
        records[name] = {
            "grade": grade,
            "row": row,
            "input": str(path.relative_to(v1.ROOT)),
            "input_sha256": input_hash,
            "charts": chart_record,
        }

    expected_points = {
        "A00": {"Tg15_6": {(("a0", 3),): Fraction(-1, 16)}},
        "A10": {
            "Tg15_3": {(("a1", 3),): Fraction(-1, 16)},
            "Tg15_5": {(("a1", 3), ("rho", 2)): Fraction(-3, 32)},
            "Tg15_7": {(("a1", 3), ("rho", 4)): Fraction(-3, 128)},
        },
    }
    if grade10_zero != {"a0_chart": 7, "a1_ordered": 7}:
        fail(("grade-10 J1-zero negative control", grade10_zero))
    if point_rows != expected_points:
        fail(("V21 point controls", point_rows, expected_points))

    final = {
        "status": "PASS-J2-TYPED-PREFIX-CENSUS-V23R1",
        "v1_implementation_sha256": V1_SHA256,
        "input_manifest_sha256": {
            str(path.relative_to(v1.ROOT)): expected
            for path, expected in v1.EXPECTED_INPUT_HASHES.items()
        },
        "input_rows": len(inputs),
        "grade10_zero_controls": grade10_zero,
        "point_controls": {
            label: {
                name: [v1.serialize_term(monomial, coefficient) for monomial, coefficient in sorted(polynomial.items())]
                for name, polynomial in rows.items()
            }
            for label, rows in point_rows.items()
        },
        "pure_exceptional_nonzero_rows": {
            chart: {
                name: [v1.serialize_term(monomial, coefficient) for monomial, coefficient in sorted(polynomial.items())]
                for name, polynomial in rows.items()
            }
            for chart, rows in pure_rows.items()
        },
        "records": records,
        "scope": "literal exact-Q exported source rows grades 10--15 after named source substitutions; no ideal or chart verdict",
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-J2-TYPED-PREFIX-CENSUS-V23R1")
    print("INPUT_ROWS=42")
    print("GRADE10_ZERO_A0=7")
    print("GRADE10_ZERO_A1=7")
    print("A00_CONTROL=Tg15_6:-1/16*a0^3")
    print("A10_CONTROL=Tg15_3:-1/16*a1^3,Tg15_5:-3/32*a1^3*rho^2,Tg15_7:-3/128*a1^3*rho^4")
    print("A0_PURE_ROWS=" + ",".join(pure_rows["a0_chart"]))
    print("A1_PURE_ROWS=" + ",".join(pure_rows["a1_ordered"]))
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
