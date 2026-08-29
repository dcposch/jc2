#!/usr/bin/env python3
"""Exact restricted-AST specialization of exported grades 10--15 to J2 charts."""

from __future__ import annotations

import ast
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V9 = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/aws_q_v9"
V20 = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/aws_q_v20"
V22 = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/aws_q_r1"
V9_MANIFEST = V9 / "COEFFICIENTS.json"
V20_RESULT = V20 / "RESULT.json"
V22_RESULT = V22 / "RESULT.json"
EXPECTED_INPUT_HASHES = {
    V9_MANIFEST: "86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e",
    V20_RESULT: "b23ffacd1e4e26abccaeb94a5e83f301cd98a9918a3a84e207fc462a880fe68d",
    V22_RESULT: "829239c93c9a8bcb34a0428391c378ddd662dbc70cfdd27a6b2cc3b6cdcf00b8",
}
J1 = frozenset({"rs", "cs", "c0", "c1"})

Monomial = tuple[tuple[str, int], ...]
Polynomial = dict[Monomial, Fraction]


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def clean(polynomial: Polynomial) -> Polynomial:
    return {monomial: coefficient for monomial, coefficient in polynomial.items() if coefficient}


def const(value: int | Fraction) -> Polynomial:
    value = Fraction(value)
    return {} if not value else {(): value}


def add(left: Polynomial, right: Polynomial, scale: Fraction = Fraction(1)) -> Polynomial:
    answer = dict(left)
    for monomial, coefficient in right.items():
        answer[monomial] = answer.get(monomial, Fraction(0)) + scale * coefficient
    return clean(answer)


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            exponents = dict(left_monomial)
            for name, exponent in right_monomial:
                exponents[name] = exponents.get(name, 0) + exponent
            monomial = tuple(sorted((name, exponent) for name, exponent in exponents.items() if exponent))
            answer[monomial] = answer.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
    return clean(answer)


def power(polynomial: Polynomial, exponent: int) -> Polynomial:
    if exponent < 0:
        fail(("negative exponent", exponent))
    answer = const(1)
    base = polynomial
    while exponent:
        if exponent & 1:
            answer = multiply(answer, base)
        exponent //= 2
        if exponent:
            base = multiply(base, base)
    return answer


def scalar(polynomial: Polynomial) -> Fraction:
    if set(polynomial) != {()}:
        fail(("nonconstant scalar", polynomial))
    return polynomial[()]


def parse_node(node: ast.AST) -> Polynomial:
    if isinstance(node, ast.Expression):
        return parse_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return const(node.value)
    if isinstance(node, ast.Name):
        return {((node.id, 1),): Fraction(1)}
    if isinstance(node, ast.UnaryOp):
        item = parse_node(node.operand)
        if isinstance(node.op, ast.UAdd):
            return item
        if isinstance(node.op, ast.USub):
            return {monomial: -coefficient for monomial, coefficient in item.items()}
    if isinstance(node, ast.BinOp):
        left = parse_node(node.left)
        right = parse_node(node.right)
        if isinstance(node.op, ast.Add):
            return add(left, right)
        if isinstance(node.op, ast.Sub):
            return add(left, right, Fraction(-1))
        if isinstance(node.op, ast.Mult):
            return multiply(left, right)
        if isinstance(node.op, ast.Div):
            divisor = scalar(right)
            if not divisor:
                fail("division by zero")
            return {monomial: coefficient / divisor for monomial, coefficient in left.items()}
        if isinstance(node.op, ast.Pow):
            exponent = scalar(right)
            if exponent.denominator != 1:
                fail(("nonintegral exponent", exponent))
            return power(left, int(exponent))
    fail(("unsupported syntax", ast.dump(node)))


def parse(path: Path) -> Polynomial:
    return parse_node(ast.parse(path.read_text().strip().replace("^", "**"), mode="eval"))


def sigma_weight(name: str) -> int:
    fixed = {
        "rho": 0, "cs": 2, "rs": 2, "k": 4, "qa1": 0,
        "a0": 5, "a1": 5, "c0": 5, "c1": 5,
        "aa0": 6, "aa1": 6, "e0": 6, "e1": 6,
        "aaa0": 7, "aaa1": 7, "ee0": 7, "ee1": 7,
        "k1": 5, "k2c": 6, "k6": 12, "k2": 20,
    }
    if name in fixed:
        return fixed[name]
    for prefix, offset in (
        ("ell", 0), ("cs", 2), ("rs", 2), ("az", 5), ("ac", 5),
        ("ez", 5), ("ec", 5), ("k10_", 4), ("k6_", 12),
    ):
        suffix = name[len(prefix):] if name.startswith(prefix) else ""
        if suffix.isdigit():
            return offset + int(suffix)
    fail(("unknown sigma weight", name))


def specialize(polynomial: Polynomial, killed: frozenset[str], replacements: dict[str, Monomial]) -> Polynomial:
    answer: Polynomial = {}
    for monomial, coefficient in polynomial.items():
        if any(name in killed for name, _ in monomial):
            continue
        exponents: dict[str, int] = {}
        for name, exponent in monomial:
            replacement = replacements.get(name, ((name, 1),))
            for replacement_name, replacement_exponent in replacement:
                exponents[replacement_name] = exponents.get(replacement_name, 0) + exponent * replacement_exponent
        new_monomial = tuple(sorted((name, exponent) for name, exponent in exponents.items() if exponent))
        answer[new_monomial] = answer.get(new_monomial, Fraction(0)) + coefficient
    return clean(answer)


def serialize_term(monomial: Monomial, coefficient: Fraction) -> dict[str, object]:
    return {
        "coefficient": [coefficient.numerator, coefficient.denominator],
        "powers": {name: exponent for name, exponent in monomial},
    }


def polynomial_text(polynomial: Polynomial) -> str:
    if not polynomial:
        return "0"
    pieces = []
    for monomial, coefficient in sorted(polynomial.items()):
        coefficient_text = str(coefficient.numerator) if coefficient.denominator == 1 else f"({coefficient.numerator}/{coefficient.denominator})"
        factors = [coefficient_text]
        for name, exponent in monomial:
            factors.append(name if exponent == 1 else f"{name}^{exponent}")
        pieces.append("*".join(factors))
    return "+".join(pieces).replace("+-", "-")


def resolve_inputs() -> list[tuple[str, int, int, Path, str]]:
    for path, expected in EXPECTED_INPUT_HASHES.items():
        if digest(path) != expected:
            fail(("input manifest hash", str(path), digest(path), expected))
    manifests = {
        "V9": json.loads(V9_MANIFEST.read_text()),
        "V20": json.loads(V20_RESULT.read_text()),
        "V22": json.loads(V22_RESULT.read_text()),
    }
    answer = []
    for grade in range(10, 16):
        source = "V9" if grade <= 12 else "V20" if grade <= 14 else "V22"
        base = V9 / "compiled" if source == "V9" else V20 / "compiled" if source == "V20" else V22 / "compiled"
        suffix = "" if source == "V9" else "_q"
        for row in range(1, 8):
            name = f"Tg{grade}_{row}"
            path = base / f"{name}{suffix}.poly"
            expected = manifests[source]["coefficient_sha256"].get(name)
            if expected is None:
                # V9's manifest stores the same table at top level; fail if a
                # future schema changes instead of guessing.
                fail(("missing coefficient manifest entry", source, name))
            if digest(path) != expected:
                fail(("coefficient hash", source, name, digest(path), expected))
            answer.append((name, grade, row, path, expected))
    return answer


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: census_j2_typed_v23.py OUTPUT_DIRECTORY")
    output = Path(sys.argv[1]).resolve()
    if output.exists():
        fail(("refuse overwrite", str(output)))
    output.mkdir(parents=True)
    (output / "a0_chart").mkdir()
    (output / "a1_ordered").mkdir()

    inputs = resolve_inputs()
    records: dict[str, object] = {}
    grade10_zero = {"a0_chart": 0, "a1_ordered": 0}
    expected_controls = {
        "a0_chart": {"Tg15_6": {(("a0", 3),): Fraction(-1, 16)}},
        "a1_ordered": {
            "Tg15_3": {(("a1", 3),): Fraction(-1, 16)},
            "Tg15_5": {(("a1", 3), ("rho", 2)): Fraction(-3, 32)},
            "Tg15_7": {(("a1", 3), ("rho", 4)): Fraction(-3, 128)},
        },
    }
    observed_controls: dict[str, dict[str, Polynomial]] = {"a0_chart": {}, "a1_ordered": {}}

    for name, grade, row, path, input_hash in inputs:
        polynomial = parse(path)
        if any(sum(sigma_weight(variable) * exponent for variable, exponent in monomial) != grade for monomial in polynomial):
            fail(("input sigma homogeneity", name))
        if any(next((exponent for variable, exponent in monomial if variable == "rho"), 0) % 2 for monomial in polynomial):
            fail(("input rho parity", name))
        chart_polynomials = {
            "a0_chart": specialize(polynomial, J1, {"a1": (("a0", 1), ("qa1", 1))}),
            "a1_ordered": specialize(polynomial, J1 | {"a0"}, {}),
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
                observed_controls[chart][name] = pure
            if grade == 10 and not specialized:
                grade10_zero[chart] += 1
            out_path = output / chart / f"{name}.poly"
            out_path.write_text(polynomial_text(specialized) + "\n")
            variables = sorted({variable for monomial in specialized for variable, _ in monomial})
            nuisance = sorted(set(variables) - permitted)
            chart_record[chart] = {
                "term_count": len(specialized),
                "variables": variables,
                "nuisance_variables": nuisance,
                "pure_exceptional_terms": [serialize_term(monomial, coefficient) for monomial, coefficient in sorted(pure.items())],
                "output": str(out_path.relative_to(output)),
                "output_sha256": digest(out_path),
            }
        records[name] = {
            "grade": grade,
            "row": row,
            "input": str(path.relative_to(ROOT)),
            "input_sha256": input_hash,
            "charts": chart_record,
        }

    if grade10_zero != {"a0_chart": 7, "a1_ordered": 7}:
        fail(("grade-10 J1-zero negative control", grade10_zero))
    if observed_controls != expected_controls:
        fail(("V21 pure-section control", observed_controls, expected_controls))

    final = {
        "status": "PASS-J2-TYPED-PREFIX-CENSUS-V23",
        "input_manifest_sha256": {str(path.relative_to(ROOT)): expected for path, expected in EXPECTED_INPUT_HASHES.items()},
        "input_rows": len(inputs),
        "grade10_zero_controls": grade10_zero,
        "pure_exceptional_nonzero_rows": {
            chart: {
                name: [serialize_term(monomial, coefficient) for monomial, coefficient in sorted(polynomial.items())]
                for name, polynomial in rows.items()
            }
            for chart, rows in observed_controls.items()
        },
        "records": records,
        "scope": "literal exact-Q exported source rows grades 10--15 after named source substitutions; no ideal or chart verdict",
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(final, sort_keys=True, indent=2) + "\n")
    print("PASS-J2-TYPED-PREFIX-CENSUS-V23")
    print("INPUT_ROWS=42")
    print("GRADE10_ZERO_A0=7")
    print("GRADE10_ZERO_A1=7")
    print("PURE_A0=Tg15_6:-1/16*a0^3")
    print("PURE_A1=Tg15_3:-1/16*a1^3,Tg15_5:-3/32*a1^3*rho^2,Tg15_7:-3/128*a1^3*rho^4")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
