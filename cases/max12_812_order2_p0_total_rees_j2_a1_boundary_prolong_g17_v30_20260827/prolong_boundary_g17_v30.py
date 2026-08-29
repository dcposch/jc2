#!/usr/bin/env python3
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
V28_MODULE = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/prolong_boundary_g16_v28.py"
V28_MODULE_SHA = "6c76dc541d27b436a289f1decccd6e90c1424b3a586685e128331c8490b06480"
V20_MODULE = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/export_allrows_g13_g14_v20.py"
V20_SHA = "5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587"
V23 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827"
V23_PARSER = V23 / "census_j2_typed_v23.py"
V23_PARSER_SHA = "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501"
V23_RESULT = V23 / "output_r1/RESULT.json"
V23_RESULT_SHA = "ce4d0adbbe94e1337bed5047da0417e3b17cb86530715fb62316086cabd14641"
V28_Q = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/aws_q/compiled"
V28_RESULT = V28_Q / "result.json"
V28_RESULT_SHA = "7e00fc2ca8de3fee8ddf9cfa7b9adfef526cc8f1cc2efcb90fb7290e8fece3ae"
PREREG = HERE / "PREREGISTRATION.md"
ROWS = tuple(range(1, 8))
POINT = {
    "a1": Fraction(48), "aa0": Fraction(48), "cs1": Fraction(8),
    "ec3": Fraction(384), "rs2": Fraction(-32),
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_module(path: Path, expected: str, name: str):
    if digest(path) != expected:
        fail(("module hash", str(path)))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("module import", str(path)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def dense_series(base, names):
    return base.named_series(list(enumerate(names)))


def build_source_series(base):
    p = base.series_zero()
    p[0] = base.poly_scale(-2, base.poly_mul(base.poly_var("rho"), base.poly_var("rho")))
    for degree in range(1, 18):
        p[degree] = base.poly_scale(2, base.poly_var(f"ell{degree}"))
    c0 = dense_series(base, ["cs"] + [f"cs{i}" for i in range(1, 16)])
    c = base.series_shift(c0, 2)
    r0 = dense_series(base, ["rs"] + [f"rs{i}" for i in range(1, 16)])
    r = base.series_scale(Fraction(1, 4), base.series_add(base.series_mul(p, p), base.series_shift(r0, 2)))
    az = dense_series(base, ["a1", "aa1", "aaa1"] + [f"az{i}" for i in range(3, 13)])
    ac = dense_series(base, ["a0", "aa0", "aaa0"] + [f"ac{i}" for i in range(3, 13)])
    ez = dense_series(base, ["c1", "e1", "ee1"] + [f"ez{i}" for i in range(3, 13)])
    ec = dense_series(base, ["c0", "e0", "ee0"] + [f"ec{i}" for i in range(3, 13)])
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
    k10 = dense_series(base, ["k", "k1", "k2c"] + [f"k10_{i}" for i in range(3, 14)])
    k6 = dense_series(base, ["k6", "k6_1", "k6_2", "k6_3", "k6_4", "k6_5"])
    k2 = dense_series(base, ["k2"])
    return coefficients, {7: base.series_shift(k10, 4), 8: base.series_shift(k6, 12), 9: base.series_shift(k2, 20)}


def specialize_point(polynomial, sigma_weight):
    answer = {}
    for monomial, coefficient in polynomial.items():
        kept = []
        value = coefficient
        for name, exponent in monomial:
            if name in POINT:
                value *= POINT[name] ** exponent
            elif sigma_weight(name) == 17:
                kept.append((name, exponent))
            else:
                value = 0
                break
        if value:
            key = tuple(kept)
            answer[key] = answer.get(key, Fraction(0)) + value
            if not answer[key]:
                del answer[key]
    return answer


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--characteristic", type=int, choices=(0, 65521), required=True)
    args = cli.parse_args()
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if platform.system() != "Linux" or not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2" or not tag:
        fail("registered AWS EC2 lane required")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)

    v28 = load_module(V28_MODULE, V28_MODULE_SHA, "v30_v28")
    v20 = load_module(V20_MODULE, V20_SHA, "v30_v20")
    parser = load_module(V23_PARSER, V23_PARSER_SHA, "v30_parser")
    if digest(V23_RESULT) != V23_RESULT_SHA or digest(V28_RESULT) != V28_RESULT_SHA:
        fail("upstream result hash")
    v23_result = json.loads(V23_RESULT.read_text())
    v28_result = json.loads(V28_RESULT.read_text())
    base = v20.load_replay()
    base.MAX_DEGREE = 17
    tails = json.loads(v20.TAILS.read_text())
    coefficients, loads = build_source_series(base)
    totals = {row: v28.build_row(base, tails[str(row)], row, coefficients, loads) for row in ROWS}
    killed = parser.J1 | frozenset({"a0", "rho"})

    bridge_count = 0
    point_zero_count = 0
    for name, record in sorted(v23_result["records"].items(), key=lambda item: (item[1]["grade"], item[1]["row"])):
        grade = int(record["grade"]); row = int(record["row"])
        chart = record["charts"]["a1_ordered"]
        path = V23 / "output_r1" / chart["output"]
        if digest(path) != chart["output_sha256"]:
            fail(("V23 hash", name))
        expected = parser.specialize(parser.parse(path), frozenset({"rho"}), {})
        rebuilt = parser.specialize(totals[row][grade], killed, {})
        if rebuilt != expected:
            fail(("V23 bridge", name))
        if v28.evaluate(rebuilt, POINT):
            fail(("point old row", name))
        bridge_count += 1; point_zero_count += 1

    grade16 = {}
    for row in ROWS:
        name = f"Tg16_{row}"
        raw = Path(v28_result["coefficient_paths"][name])
        path = V28_Q / raw.name
        if digest(path) != v28_result["coefficient_sha256"][name]:
            fail(("V28 hash", name))
        expected = parser.parse(path)
        rebuilt = parser.specialize(totals[row][16], killed, {})
        if rebuilt != expected:
            fail(("V28 bridge", name))
        if v28.evaluate(rebuilt, POINT):
            fail(("point grade16", name))
        grade16[row] = rebuilt
        bridge_count += 1; point_zero_count += 1
    if bridge_count != 49 or point_zero_count != 49:
        fail("bridge census")

    face = {row: parser.specialize(totals[row][17], killed, {}) for row in ROWS}
    affine = {row: specialize_point(face[row], parser.sigma_weight) for row in ROWS}
    new_variables = sorted(
        {name for polynomial in affine.values() for monomial in polynomial for name, _ in monomial},
        key=lambda name: (parser.sigma_weight(name), name),
    )
    if any(parser.sigma_weight(name) != 17 for name in new_variables):
        fail(("new variable weight", new_variables))
    solved = v28.solve_affine([affine[row] for row in ROWS], new_variables)

    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    paths = {}; hashes = {}; affine_paths = {}; affine_hashes = {}
    for row in ROWS:
        name = f"Tg17_{row}"
        path = output / f"{name}_{label}.poly"
        path.write_text(v20.singular_text(face[row], args.characteristic) + "\n")
        paths[name] = str(path); hashes[name] = digest(path)
        apath = output / f"{name}_at_point_{label}.poly"
        apath.write_text(v20.singular_text(affine[row], args.characteristic) + "\n")
        affine_paths[name] = str(apath); affine_hashes[name] = digest(apath)

    all_variables = v20.variable_names(list(face.values()) + [grade16[4]])
    control = output / f"boundary_prolong_g17_{label}.sing"
    lines = [f"ring R={args.characteristic},({','.join(all_variables)}),dp;"]
    mutation = dict(POINT); mutation["rs2"] += 1
    lines.append(f"poly Bad={v20.singular_text(grade16[4], args.characteristic)};")
    for variable in all_variables:
        lines.append(f"Bad=subst(Bad,{variable},{v20.coefficient_text(mutation.get(variable, Fraction(0)), args.characteristic)});")
    if not v28.evaluate(grade16[4], mutation):
        fail("zero mutation control")
    lines.append("if (Bad==0) { print(\"FAIL_POINT_MUTATION\"); quit; }")
    lines.append('print("V30_POINT_MUTATION=1");')

    if solved["outcome"] == "consistent":
        extension = dict(POINT); extension.update(solved["solution"])
        for row in ROWS:
            if v28.evaluate(face[row], extension):
                fail(("extension replay", row))
            name = f"Tg17_{row}"
            lines.append(f"poly E_{name}={v20.singular_text(face[row], args.characteristic)};")
            for variable in all_variables:
                lines.append(f"E_{name}=subst(E_{name},{variable},{v20.coefficient_text(extension.get(variable, Fraction(0)), args.characteristic)});")
            lines.append(f"if (E_{name}!=0) {{ print(\"FAIL_EXTENSION_{name}\"); quit; }}")
            lines.append(f'print("V30_EXTENSION_{name}=1");')
        outcome_record = {
            "outcome": "consistent",
            "solution": {name: v28.encode_fraction(value) for name, value in sorted(solved["solution"].items())},
            "extended_nonzero_point": {name: v28.encode_fraction(value) for name, value in sorted(extension.items()) if value},
        }
    else:
        dual = solved["dual"]
        combination = {}
        for row, coefficient in zip(ROWS, dual):
            combination = base.poly_add(combination, base.poly_scale(coefficient, affine[row]))
        if combination != base.poly_const(1):
            fail(("dual replay", combination))
        for row in ROWS:
            lines.append(f"poly A_Tg17_{row}={v20.singular_text(affine[row], args.characteristic)};")
        terms = [f"({v20.coefficient_text(c, args.characteristic)})*A_Tg17_{r}" for r, c in zip(ROWS, dual) if c]
        lines.append(f"poly Dual={'+'.join(terms) if terms else '0'};")
        lines.append("if (Dual-1!=0) { print(\"FAIL_DUAL\"); quit; }")
        lines.append('print("V30_DUAL=1");')
        outcome_record = {"outcome": "inconsistent", "dual": {f"Tg17_{r}": v28.encode_fraction(c) for r, c in zip(ROWS, dual) if c}}
    lines += [f'print("V30_OUTCOME={solved["outcome"]}");', 'print("PASS_A1_BOUNDARY_PROLONG_G17_V30");', "quit;"]
    control.write_text("\n".join(lines) + "\n")

    result = {
        "status": "PASS-A1-BOUNDARY-PROLONG-G17-V30-COMPILER",
        "registered_aws_lane": tag,
        "characteristic": args.characteristic,
        "preregistration_sha256": digest(PREREG),
        "v28_module_sha256": V28_MODULE_SHA,
        "v28_result_sha256": V28_RESULT_SHA,
        "old_bridges": bridge_count,
        "old_point_zero_rows": point_zero_count,
        "point": {name: v28.encode_fraction(value) for name, value in sorted(POINT.items())},
        "new_variables": new_variables,
        "linear_rank": solved["rank"],
        "grade17_term_counts": {f"Tg17_{row}": len(face[row]) for row in ROWS},
        "grade17_affine_term_counts": {f"Tg17_{row}": len(affine[row]) for row in ROWS},
        "coefficient_paths": paths, "coefficient_sha256": hashes,
        "affine_paths": affine_paths, "affine_sha256": affine_hashes,
        "control_script": str(control), "control_script_sha256": digest(control),
        **outcome_record,
        "scope": "literal ordered-a1 rho=0 actual-total source rows through grade17 only",
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-BOUNDARY-PROLONG-G17-V30-COMPILER")
    print(f"OUTCOME={result['outcome']}")
    print(f"NEW_VARIABLES={len(new_variables)}")
    print(f"LINEAR_RANK={solved['rank']}")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()

