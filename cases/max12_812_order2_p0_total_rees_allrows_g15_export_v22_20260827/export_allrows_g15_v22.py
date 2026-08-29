#!/usr/bin/env python3
"""AWS-only exact export of every actual-total row at grade 15."""

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
V20_MODULE = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/export_allrows_g13_g14_v20.py"
V20_MODULE_SHA256 = "5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587"
V20_COMPILED = {
    0: (
        ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/aws_q_v20/compiled/result.json",
        "b37b95646e5deb381de1edfd3a15a336065855402267c3044f111ca63c3b0f9e",
    ),
    65521: (
        ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/aws_p65521_v20/compiled/result.json",
        "3e763bd4ae482494e11ca351b11619aa5d734c4c35e6f55b61146fa7021830ce",
    ),
}
V21_RESULT = ROOT / "cases/max12_812_order2_p0_total_rees_section_all_depth_v21_20260827/RESULT.json"
V21_RESULT_SHA256 = "f702630d71ea4b1168ab993848dc334e67fac4f436273e27fc5fb93637bd34ff"
PREREG = HERE / "PREREGISTRATION.md"
ROWS = tuple(range(1, 8))
OLD_GRADES = (10, 11, 12, 13, 14)
NEW_GRADE = 15


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
        or not tag.startswith("max12_812_order2_p0_total_rees_allrows_g15_export_v22_")
    ):
        fail("V22 exporter requires a registered AWS EC2 lane")
    return tag


def load_v20():
    if digest(V20_MODULE) != V20_MODULE_SHA256:
        fail("V20 emitter hash mismatch")
    spec = importlib.util.spec_from_file_location("total_rees_v20_frozen_for_v22", V20_MODULE)
    if spec is None or spec.loader is None:
        fail("cannot import V20 emitter")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dense_series(base, names: list[str]):
    return base.named_series(list(enumerate(names)))


def build_source_series(base):
    p = base.series_zero()
    p[0] = base.poly_scale(-2, base.poly_mul(base.poly_var("rho"), base.poly_var("rho")))
    for degree in range(1, 16):
        p[degree] = base.poly_scale(2, base.poly_var(f"ell{degree}"))

    c0 = dense_series(base, ["cs"] + [f"cs{i}" for i in range(1, 14)])
    c = base.series_shift(c0, 2)
    r0 = dense_series(base, ["rs"] + [f"rs{i}" for i in range(1, 14)])
    r = base.series_scale(Fraction(1, 4), base.series_add(base.series_mul(p, p), base.series_shift(r0, 2)))

    az = dense_series(base, ["a1", "aa1", "aaa1"] + [f"az{i}" for i in range(3, 11)])
    ac = dense_series(base, ["a0", "aa0", "aaa0"] + [f"ac{i}" for i in range(3, 11)])
    ez = dense_series(base, ["c1", "e1", "ee1"] + [f"ez{i}" for i in range(3, 11)])
    ec = dense_series(base, ["c0", "e0", "ee0"] + [f"ec{i}" for i in range(3, 11)])

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
    k10 = dense_series(base, ["k", "k1", "k2c"] + [f"k10_{i}" for i in range(3, 12)])
    k6 = dense_series(base, ["k6", "k6_1", "k6_2", "k6_3"])
    k2 = dense_series(base, ["k2"])
    loads = {7: base.series_shift(k10, 4), 8: base.series_shift(k6, 12), 9: base.series_shift(k2, 20)}
    return coefficients, loads


def build_row(base, entries, row: int, coefficients, loads):
    total = base.series_zero()
    contribution_counts = [0] * 16
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
        for degree in range(16):
            if term[degree]:
                contribution_counts[degree] += 1
        total = base.series_add(total, term)
        if negative_delta is None:
            for degree in (10, 11, 12):
                delta = unit_term[degree]
                if delta and any(
                    (value.numerator * pow(value.denominator, -1, 65521)) % 65521
                    for value in delta.values()
                ):
                    negative_delta = degree, monomial, delta
                    break
    if negative_delta is None:
        fail(("no source-sensitivity delta", row))
    return total, contribution_counts, negative_delta


def sigma_weight(name: str) -> int:
    fixed = {
        "rho": 0, "cs": 2, "rs": 2, "k": 4,
        "a0": 5, "a1": 5, "c0": 5, "c1": 5,
        "aa0": 6, "aa1": 6, "e0": 6, "e1": 6,
        "aaa0": 7, "aaa1": 7, "ee0": 7, "ee1": 7,
        "k1": 5, "k2c": 6, "k6": 12, "k2": 20,
    }
    if name in fixed:
        return fixed[name]
    for prefix, offset in (("ell", 0), ("cs", 2), ("rs", 2), ("az", 5), ("ac", 5), ("ez", 5), ("ec", 5), ("k10_", 4), ("k6_", 12)):
        if name.startswith(prefix) and name[len(prefix):].isdigit():
            return offset + int(name[len(prefix):])
    fail(("unknown sigma weight", name))


def compile_export(output: Path, characteristic: int, tag: str) -> None:
    v20 = load_v20()
    base = v20.load_replay()
    base.MAX_DEGREE = 15
    tails = json.loads(v20.TAILS.read_text())
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

    grade15 = {row: totals[row][15] for row in ROWS}
    for row, polynomial in grade15.items():
        if not polynomial:
            fail(("unexpected zero grade-15 row", row))
        if any(exponent % 2 for monomial in polynomial for name, exponent in monomial if name == "rho"):
            fail(("rho parity", row))
        if any(sum(sigma_weight(name) * exponent for name, exponent in monomial) != 15 for monomial in polynomial):
            fail(("sigma homogeneity", row))

    refs = {}
    v9_dir, v9_manifest_sha = v20.V9[characteristic]
    v9_manifest = v9_dir / "COEFFICIENTS.json"
    if digest(v9_manifest) != v9_manifest_sha:
        fail("V9 manifest hash")
    v9_data = json.loads(v9_manifest.read_text())
    for grade in (10, 11, 12):
        for row in ROWS:
            name = f"Tg{grade}_{row}"
            path = v9_dir / "compiled" / f"{name}.poly"
            if digest(path) != v9_data["coefficient_sha256"][name]:
                fail(("V9 coefficient hash", name))
            refs[(grade, row)] = path.read_text().strip()

    v20_result_path, v20_result_sha = V20_COMPILED[characteristic]
    if digest(v20_result_path) != v20_result_sha:
        fail("V20 compiled-result hash")
    v20_data = json.loads(v20_result_path.read_text())
    for grade in (13, 14):
        for row in ROWS:
            name = f"Tg{grade}_{row}"
            path = Path(v20_data["coefficient_paths"][name])
            if not path.is_file():
                path = v20_result_path.parent / path.name
            if digest(path) != v20_data["coefficient_sha256"][name]:
                fail(("V20 coefficient hash", name))
            refs[(grade, row)] = path.read_text().strip()

    for (grade, row), reference in refs.items():
        if v20.singular_text(totals[row][grade], characteristic) != reference:
            fail(("old coefficient byte bridge", grade, row))

    if digest(V21_RESULT) != V21_RESULT_SHA256:
        fail("V21 result hash")
    v21 = json.loads(V21_RESULT.read_text())
    sections = {"CS0": "cs", "A00": "a0", "A10": "a1", "Z00": None}
    section_results = {
        section: {
            f"Tg15_{row}": v20.singular_text(v20.section_residual(base, grade15[row], one), 0)
            for row in ROWS if v20.section_residual(base, grade15[row], one)
        }
        for section, one in sections.items()
    }
    expected_sections = {
        "CS0": {}, "Z00": {}, "A00": {"Tg15_6": "(-1/16)"},
        "A10": {"Tg15_3": "(-1/16)", "Tg15_5": "(-3/32)*rho^2", "Tg15_7": "(-3/128)*rho^4"},
    }
    if section_results != expected_sections or v21.get("first_nonzero_grade") != {"A00": 15, "A10": 15, "CS0": None, "Z00": None}:
        fail(("V21 section bridge", section_results))

    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if characteristic == 0 else f"p{characteristic}"
    paths = {}; hashes = {}; counts = {}; supports = {}
    for row, polynomial in grade15.items():
        name = f"Tg15_{row}"
        path = output / f"{name}_{label}.poly"
        path.write_text(v20.singular_text(polynomial, characteristic) + "\n")
        paths[name] = str(path); hashes[name] = digest(path); counts[name] = len(polynomial)
        supports[name] = v20.variable_names([polynomial])

    variables = v20.variable_names([totals[row][grade] for grade in OLD_GRADES + (15,) for row in ROWS] + [negative_controls[row][2] for row in ROWS])
    control = output / f"allrows_g15_bridge_{label}.sing"
    lines = [f"ring R={characteristic},({','.join(variables)}),dp;", 'print("V22_QRING_DISABLED=1");']
    for (grade, row), reference in refs.items():
        name = f"Tg{grade}_{row}"
        lines += [
            f"poly Mine_{name}={v20.singular_text(totals[row][grade], characteristic)};",
            f"poly Ref_{name}={reference};",
            f"if (Mine_{name}-Ref_{name}!=0) {{ print(\"FAIL_OLD_BRIDGE_{name}\"); quit; }}",
            f'print("V22_OLD_BRIDGE_{name}=1");',
        ]
    for row, polynomial in grade15.items():
        name = f"Tg15_{row}"
        lines += [
            f"poly Mine_{name}={v20.singular_text(polynomial, characteristic)};",
            f"if (Mine_{name}==0) {{ print(\"FAIL_NONZERO_{name}\"); quit; }}",
            f"if (subst(Mine_{name},rho,-rho)-Mine_{name}!=0) {{ print(\"FAIL_RHO_PARITY_{name}\"); quit; }}",
            f'print("V22_NONZERO_RHO_EVEN_{name}=1");',
        ]
    for row in ROWS:
        grade, _, delta = negative_controls[row]
        name = f"Tg{grade}_{row}"
        lines += [
            f"poly Wrong_{name}=Mine_{name}+({v20.singular_text(delta, characteristic)});",
            f"if (Wrong_{name}-Ref_{name}==0) {{ print(\"FAIL_SOURCE_SENSITIVITY_{name}\"); quit; }}",
            f'print("V22_SOURCE_SENSITIVITY_{name}=1");',
        ]
    lines += ['print("PASS_TOTAL_REES_ALLROWS_G15_EXPORT_V22");', "quit;"]
    control.write_text("\n".join(lines) + "\n")
    if "qring " in control.read_text():
        fail("qring sentinel")

    result = {
        "status": "PASS-TOTAL-REES-ALLROWS-G15-EXPORT-V22-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": characteristic,
        "v20_emitter_sha256": V20_MODULE_SHA256,
        "v20_compiled_result_sha256": v20_result_sha,
        "v21_result_sha256": V21_RESULT_SHA256,
        "preregistration_sha256": digest(PREREG),
        "tail_rows_checked": 7,
        "tail_terms_checked": sum(len(tails[str(row)]) for row in ROWS),
        "old_coefficient_byte_bridges": 35,
        "rho_even_coefficients": 7,
        "sigma_homogeneous_coefficients": 7,
        "source_sensitivity_controls": 7,
        "source_sensitivity_control_details": {
            str(row): {
                "grade": negative_controls[row][0],
                "tail_monomial": negative_controls[row][1],
                "delta_term_count": len(negative_controls[row][2]),
            }
            for row in ROWS
        },
        "section_nonzero_residuals_exact_qrho": section_results,
        "coefficient_paths": paths,
        "coefficient_sha256": hashes,
        "coefficient_term_counts": counts,
        "coefficient_variable_supports": supports,
        "contributing_tail_counts": {f"Tg15_{row}": contribution_counts[row][15] for row in ROWS},
        "control_script": str(control),
        "control_script_sha256": digest(control),
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = parser.parse_args()
    compile_export(args.output, args.characteristic, require_aws())


if __name__ == "__main__":
    main()
