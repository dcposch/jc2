#!/usr/bin/env python3
"""AWS-only exact export of every actual-total row at grades 13 and 14."""

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
REPLAY = ROOT / "cases/max12_812_order2_p0_odd_grade14_unit_replay_20260826/replay_row5_grade14.py"
REPLAY_SHA256 = "2c55284a3fd36e5d9eda26f759353f27d07163d87c30c9f958e84fb32b031258"
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
TAILS_SHA256 = "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848"
V9 = {
    0: (
        ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/aws_q_v9",
        "86c535a370adc2c7fb31b6ec8454128d765f581200a1730c506306d8bfa63c0e",
    ),
    65521: (
        ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_coeffexport_v9_20260826/aws_p65521_v9",
        "dc7757090bac53482ff674794e4e45cf33ff052d10c34f4e29a1de4133befde4",
    ),
}
V17 = {
    0: (
        ROOT / "cases/max12_812_order2_p0_total_rees_t_cs_row5_g14_export_v17_20260826/aws_q/compiled/Tg14_5_q.poly",
        "91d96924696ab19a59cd8661fdd778559ce8dc9c1bc0fbc886dbdf4956e838f7",
    ),
    65521: (
        ROOT / "cases/max12_812_order2_p0_total_rees_t_cs_row5_g14_export_v17_20260826/aws_p65521/compiled/Tg14_5_p65521.poly",
        "760d4f3b155decdf0e847a587254ae701f2b5948d8dd6135c52f5f213c10835b",
    ),
}
PREREG = HERE / "PREREGISTRATION.md"
ROWS = tuple(range(1, 8))
OLD_GRADES = (10, 11, 12)
NEW_GRADES = (13, 14)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_")
    ):
        fail("V20 exporter requires a registered AWS EC2 lane")
    return tag


def load_replay():
    if digest(REPLAY) != REPLAY_SHA256 or digest(TAILS) != TAILS_SHA256:
        fail("frozen replay or tail hash mismatch")
    spec = importlib.util.spec_from_file_location("odd_sparse_replay_frozen_v20", REPLAY)
    if spec is None or spec.loader is None:
        fail("cannot import frozen sparse replay")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dense_series(base, names: list[str]):
    return base.named_series(list(enumerate(names)))


def poly_pow(base, polynomial, exponent: int):
    answer = base.poly_const(1)
    factor = polynomial
    power = exponent
    while power:
        if power & 1:
            answer = base.poly_mul(answer, factor)
        power //= 2
        if power:
            factor = base.poly_mul(factor, factor)
    return answer


def poly_substitute(base, polynomial, replacements):
    answer = base.poly_const(0)
    for monomial, coefficient in polynomial.items():
        term = base.poly_const(coefficient)
        for name, exponent in monomial:
            factor = replacements.get(name, base.poly_var(name))
            term = base.poly_mul(term, poly_pow(base, factor, exponent))
            if not term:
                break
        answer = base.poly_add(answer, term)
    return answer


def variable_names(polynomials) -> list[str]:
    names = {
        name
        for polynomial in polynomials
        for monomial in polynomial
        for name, _ in monomial
    }
    priority = ["rho"]
    return [name for name in priority if name in names] + sorted(names - set(priority))


def coefficient_text(value: Fraction, characteristic: int) -> str:
    if characteristic:
        return str((value.numerator * pow(value.denominator, -1, characteristic)) % characteristic)
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def singular_text(polynomial, characteristic: int) -> str:
    if not polynomial:
        return "0"
    terms: list[str] = []
    for monomial, coefficient in sorted(polynomial.items()):
        factors = [name if exponent == 1 else f"{name}^{exponent}" for name, exponent in monomial]
        factors.insert(0, coefficient_text(coefficient, characteristic))
        terms.append("*".join(factors))
    return "+".join(terms)


def polynomial_nonzero_mod(polynomial, prime: int) -> bool:
    return any(
        (coefficient.numerator * pow(coefficient.denominator, -1, prime)) % prime
        for coefficient in polynomial.values()
    )


def build_source_series(base):
    p = base.series_zero()
    p[0] = base.poly_scale(-2, base.poly_mul(base.poly_var("rho"), base.poly_var("rho")))
    for degree in range(1, 15):
        p[degree] = base.poly_scale(2, base.poly_var(f"ell{degree}"))

    c0 = dense_series(base, ["cs"] + [f"cs{i}" for i in range(1, 13)])
    c = base.series_shift(c0, 2)
    r0 = dense_series(base, ["rs"] + [f"rs{i}" for i in range(1, 13)])
    r = base.series_scale(Fraction(1, 4), base.series_add(base.series_mul(p, p), base.series_shift(r0, 2)))

    az = dense_series(base, ["a1", "aa1", "aaa1"] + [f"az{i}" for i in range(3, 10)])
    ac = dense_series(base, ["a0", "aa0", "aaa0"] + [f"ac{i}" for i in range(3, 10)])
    ez = dense_series(base, ["c1", "e1", "ee1"] + [f"ez{i}" for i in range(3, 10)])
    ec = dense_series(base, ["c0", "e0", "ee0"] + [f"ec{i}" for i in range(3, 10)])

    n3 = base.series_shift(az, 3)
    n2 = base.series_shift(ac, 3)
    n1 = base.series_shift(base.series_scale(Fraction(1, 2), base.series_add(base.series_mul(p, az), ez)), 3)
    n0 = base.series_shift(base.series_scale(Fraction(1, 2), base.series_add(base.series_mul(p, ac), ec)), 3)
    coefficients = {
        6: base.series_scale(2, p),
        5: base.series_scale(2, c),
        4: base.series_add(base.series_mul(p, p), base.series_scale(2, r)),
        3: base.series_add(base.series_scale(2, base.series_mul(p, c)), base.series_shift(n3, 2)),
        2: base.series_add(base.series_mul(c, c), base.series_scale(2, base.series_mul(p, r)), base.series_shift(n2, 2)),
        1: base.series_add(base.series_scale(2, base.series_mul(c, r)), base.series_shift(n1, 2)),
        0: base.series_add(base.series_mul(r, r), base.series_shift(n0, 2)),
    }
    k10 = dense_series(base, ["k", "k1", "k2c"] + [f"k10_{i}" for i in range(3, 11)])
    k6 = dense_series(base, ["k6", "k6_1", "k6_2"])
    k2 = dense_series(base, ["k2"])
    loads = {7: base.series_shift(k10, 4), 8: base.series_shift(k6, 12), 9: base.series_shift(k2, 20)}
    return coefficients, loads


def build_row(base, entries, row: int, coefficients, loads):
    total = base.series_zero()
    contribution_counts = [0] * 15
    negative_delta = None
    weights = [8 - index for index in range(7)] + [2, 6, 10]
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        if len(monomial) != 10 or sum(a * b for a, b in zip(monomial, weights)) != 12 + row:
            fail(("row tail contract", row, monomial))
        coefficient = Fraction(str(raw_coefficient))
        if not coefficient:
            fail(("zero frozen tail coefficient", row, monomial))
        unit_term = base.series_zero()
        unit_term[0] = base.poly_const(1)
        for index, exponent in enumerate(monomial[:7]):
            if exponent:
                unit_term = base.series_mul(unit_term, base.series_pow(coefficients[index], exponent))
        for index, exponent in enumerate(monomial[7:], start=7):
            if exponent not in (0, 1):
                fail(("load nonlinearity", row, monomial))
            if exponent:
                unit_term = base.series_mul(unit_term, loads[index])
        term = base.series_scale(coefficient, unit_term)
        for degree in range(15):
            if term[degree]:
                contribution_counts[degree] += 1
        total = base.series_add(total, term)
        if negative_delta is None:
            for degree in OLD_GRADES:
                delta = unit_term[degree]
                if delta and polynomial_nonzero_mod(delta, 65521):
                    negative_delta = (degree, monomial, delta)
                    break
    if negative_delta is None:
        fail(("no dual-characteristic source-sensitivity delta", row))
    return total, contribution_counts, negative_delta


def section_residual(base, polynomial, one: str | None):
    names = {name for monomial in polynomial for name, _ in monomial}
    replacements = {
        name: (
            base.poly_var("rho") if name == "rho"
            else base.poly_const(1) if name == one
            else base.poly_const(0)
        )
        for name in names
    }
    return poly_substitute(base, polynomial, replacements)


def compile_export(output: Path, characteristic: int, tag: str) -> dict[str, object]:
    base = load_replay()
    tails = json.loads(TAILS.read_text())
    if sorted(tails) != [str(row) for row in ROWS]:
        fail("all-row tail census")
    coefficients, loads = build_source_series(base)
    totals = {}
    contribution_counts = {}
    negative_controls = {}
    for row in ROWS:
        total, counts, negative = build_row(base, tails[str(row)], row, coefficients, loads)
        totals[row] = total
        contribution_counts[row] = counts
        negative_controls[row] = negative

    for row in ROWS:
        for grade in NEW_GRADES:
            polynomial = totals[row][grade]
            if any(exponent % 2 for monomial in polynomial for name, exponent in monomial if name == "rho"):
                fail(("rho-deck parity failure", grade, row))

    v9_dir, v9_manifest_sha = V9[characteristic]
    v9_manifest = v9_dir / "COEFFICIENTS.json"
    if digest(v9_manifest) != v9_manifest_sha:
        fail("V9 coefficient manifest mismatch")
    v9_data = json.loads(v9_manifest.read_text())
    v9_hashes = v9_data.get("coefficient_sha256")
    if (
        v9_data.get("status") != "PASS-T-RS0-EXACT-COEFFICIENT-EXPORT-V9"
        or v9_data.get("characteristic") != characteristic
        or not isinstance(v9_hashes, dict)
    ):
        fail("V9 coefficient manifest fields")
    refs = {}
    for grade in OLD_GRADES:
        for row in ROWS:
            label = f"Tg{grade}_{row}"
            path = v9_dir / "compiled" / f"{label}.poly"
            if digest(path) != v9_hashes.get(label):
                fail(("V9 coefficient hash mismatch", label))
            text = path.read_text().strip()
            if not text or ";" in text or "qring" in text:
                fail(("unsafe V9 coefficient", label))
            refs[(grade, row)] = (path, text)

    v17_path, v17_sha = V17[characteristic]
    if digest(v17_path) != v17_sha:
        fail("V17 coefficient hash mismatch")
    v17_text = v17_path.read_text()
    if singular_text(totals[5][14], characteristic) + "\n" != v17_text:
        fail("V17 row-five grade-14 byte bridge")

    sections = {"CS0": "cs", "A00": "a0", "A10": "a1", "Z00": None}
    section_results: dict[str, dict[str, str]] = {}
    for section, one in sections.items():
        nonzero = {}
        for grade in NEW_GRADES:
            for row in ROWS:
                residual = section_residual(base, totals[row][grade], one)
                if residual:
                    nonzero[f"Tg{grade}_{row}"] = singular_text(residual, 0)
        section_results[section] = nonzero

    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if characteristic == 0 else f"p{characteristic}"
    coefficient_paths = {}
    coefficient_hashes = {}
    coefficient_counts = {}
    coefficient_supports = {}
    new_polynomials = []
    for grade in NEW_GRADES:
        for row in ROWS:
            name = f"Tg{grade}_{row}"
            polynomial = totals[row][grade]
            path = output / f"{name}_{label}.poly"
            path.write_text(singular_text(polynomial, characteristic) + "\n")
            coefficient_paths[name] = str(path)
            coefficient_hashes[name] = digest(path)
            coefficient_counts[name] = len(polynomial)
            coefficient_supports[name] = variable_names([polynomial])
            new_polynomials.append(polynomial)

    variables = variable_names(
        [totals[row][grade] for grade in OLD_GRADES + NEW_GRADES for row in ROWS]
        + [negative_controls[row][2] for row in ROWS]
    )
    control = output / f"allrows_g13_g14_bridge_{label}.sing"
    lines = [
        f"ring R={characteristic},({','.join(variables)}),dp;",
        'print("V20_QRING_DISABLED=1");',
    ]
    for grade in OLD_GRADES:
        for row in ROWS:
            name = f"Tg{grade}_{row}"
            lines += [
                f"poly Mine_{name}={singular_text(totals[row][grade], characteristic)};",
                f"poly Ref_{name}={refs[(grade, row)][1]};",
                f"if (Mine_{name}-Ref_{name}!=0) {{ print(\"FAIL_V9_BRIDGE_{name}\"); quit; }}",
                f'print("V20_V9_BRIDGE_{name}=1");',
            ]
    for grade in NEW_GRADES:
        for row in ROWS:
            name = f"Tg{grade}_{row}"
            polynomial = totals[row][grade]
            lines += [
                f"poly Mine_{name}={singular_text(polynomial, characteristic)};",
                f"if (subst(Mine_{name},rho,-rho)-Mine_{name}!=0) {{ print(\"FAIL_RHO_PARITY_{name}\"); quit; }}",
                f'print("V20_RHO_EVEN_{name}=1");',
            ]
            if polynomial:
                lines += [
                    f"if (Mine_{name}==0) {{ print(\"FAIL_NONZERO_{name}\"); quit; }}",
                    f'print("V20_NONZERO_{name}=1");',
                ]
            else:
                lines += [
                    f"if (Mine_{name}!=0) {{ print(\"FAIL_ZERO_{name}\"); quit; }}",
                    f'print("V20_ZERO_{name}=1");',
                ]
    lines += [
        "if (Mine_Tg14_5-(" + v17_text.strip() + ")!=0) { print(\"FAIL_V17_BRIDGE_Tg14_5\"); quit; }",
        'print("V20_V17_BRIDGE_Tg14_5=1");',
    ]
    for row in ROWS:
        grade, _, delta = negative_controls[row]
        name = f"Tg{grade}_{row}"
        lines += [
            f"poly Wrong_{name}=Mine_{name}+({singular_text(delta, characteristic)});",
            f"if (Wrong_{name}-Ref_{name}==0) {{ print(\"FAIL_SOURCE_SENSITIVITY_{name}\"); quit; }}",
            f'print("V20_SOURCE_SENSITIVITY_{name}=1");',
        ]
    for section in sections:
        lines.append(f'print("V20_SECTION_{section}_NONZERO={len(section_results[section])}");')
    lines += ['print("PASS_TOTAL_REES_ALLROWS_G13_G14_EXPORT_V20");', "quit;"]
    control.write_text("\n".join(lines) + "\n")
    control_text = control.read_text()
    if "qring " in control_text or control_text.count("PASS_TOTAL_REES_ALLROWS_G13_G14_EXPORT_V20") != 1:
        fail("control script sentinel")

    result = {
        "status": "PASS-TOTAL-REES-ALLROWS-G13-G14-EXPORT-V20-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": characteristic,
        "replay_sha256": REPLAY_SHA256,
        "tails_sha256": TAILS_SHA256,
        "v9_manifest_sha256": v9_manifest_sha,
        "v17_reference_sha256": v17_sha,
        "preregistration_sha256": digest(PREREG),
        "tail_rows_checked": len(ROWS),
        "tail_terms_checked": sum(len(tails[str(row)]) for row in ROWS),
        "tail_terms_by_row": {str(row): len(tails[str(row)]) for row in ROWS},
        "weight_contracts": {str(row): 12 + row for row in ROWS},
        "v9_bridges_checked": len(OLD_GRADES) * len(ROWS),
        "v17_byte_bridge": True,
        "rho_even_coefficients": len(NEW_GRADES) * len(ROWS),
        "source_sensitivity_controls": {
            str(row): {
                "grade": negative_controls[row][0],
                "tail_monomial": negative_controls[row][1],
                "delta_term_count": len(negative_controls[row][2]),
            }
            for row in ROWS
        },
        "section_nonzero_residuals_exact_qrho": section_results,
        "coefficient_paths": coefficient_paths,
        "coefficient_sha256": coefficient_hashes,
        "coefficient_term_counts": coefficient_counts,
        "coefficient_variable_supports": coefficient_supports,
        "contributing_tail_counts": {
            f"Tg{grade}_{row}": contribution_counts[row][grade]
            for grade in NEW_GRADES for row in ROWS
        },
        "control_script": str(control),
        "control_script_sha256": digest(control),
        "ring_variable_count": len(variables),
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    compile_export(args.output, args.characteristic, require_aws())


if __name__ == "__main__":
    main()

