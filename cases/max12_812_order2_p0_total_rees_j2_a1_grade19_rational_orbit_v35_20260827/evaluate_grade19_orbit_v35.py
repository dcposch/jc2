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
V33_MODULE = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827/prolong_boundary_g18_v33.py"
V33_MODULE_SHA = "5941bf876e3ace184190130841046ccc2573615be5cc159608698c5bbdcac36d"
V34_Q = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_grade18_curve_cut_v34_20260827/aws_q"
V34_P = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_grade18_curve_cut_v34_20260827/aws_p65521"
V34_Q_RESULT_SHA = "7796c99ab5bdc2253754b3ca5f86adb42f2c192c6a2a575dd1f81d9cc69226fe"
V34_P_RESULT_SHA = "f293aaa2bb005778209e1ecbf9b3e12e9a3c59554f24989737b3d8b031babd46"
V34_Q_BASIS_SHA = "1e81e737cdab19a9a1b3cb2c6253fecc82c266db236af6fcf67aa03dbd419e40"
PREREG = HERE / "PREREGISTRATION.md"
ROWS = tuple(range(1, 8))
PRIME = 65521
POINT = {
    "a1": Fraction(192), "ell2": Fraction(21, 4), "cs1": Fraction(11),
    "rs2": Fraction(-35), "aa0": Fraction(-96), "ee1": Fraction(576),
    "ec3": Fraction(2400),
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load(path: Path, expected: str, name: str):
    if digest(path) != expected:
        fail(("module hash", str(path)))
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        fail(("module import", str(path)))
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def dense(base, names):
    return base.named_series(list(enumerate(names)))


def build_source_series_19(base):
    p = base.series_zero(); p[0] = base.poly_scale(-2, base.poly_mul(base.poly_var("rho"), base.poly_var("rho")))
    for degree in range(1, 20):
        p[degree] = base.poly_scale(2, base.poly_var(f"ell{degree}"))
    c = base.series_shift(dense(base, ["cs"] + [f"cs{i}" for i in range(1, 18)]), 2)
    r0 = dense(base, ["rs"] + [f"rs{i}" for i in range(1, 18)])
    r = base.series_scale(Fraction(1, 4), base.series_add(base.series_mul(p, p), base.series_shift(r0, 2)))
    az = dense(base, ["a1", "aa1", "aaa1"] + [f"az{i}" for i in range(3, 15)])
    ac = dense(base, ["a0", "aa0", "aaa0"] + [f"ac{i}" for i in range(3, 15)])
    ez = dense(base, ["c1", "e1", "ee1"] + [f"ez{i}" for i in range(3, 15)])
    ec = dense(base, ["c0", "e0", "ee0"] + [f"ec{i}" for i in range(3, 15)])
    n3 = base.series_shift(az, 3); n2 = base.series_shift(ac, 3)
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
    k10 = dense(base, ["k", "k1", "k2c"] + [f"k10_{i}" for i in range(3, 16)])
    k6 = dense(base, ["k6"] + [f"k6_{i}" for i in range(1, 8)])
    loads = {7: base.series_shift(k10, 4), 8: base.series_shift(k6, 12),
             9: base.series_shift(dense(base, ["k2"]), 20)}
    return coefficients, loads


def homogeneous(polynomial, parser, grade: int) -> bool:
    return all(sum(parser.sigma_weight(name) * exponent for name, exponent in monomial) == grade
               for monomial in polynomial)


def modular(value: Fraction) -> int:
    return (value.numerator * pow(value.denominator, -1, PRIME)) % PRIME


def main() -> None:
    cli = argparse.ArgumentParser(); cli.add_argument("output", type=Path)
    cli.add_argument("--characteristic", type=int, choices=(0, PRIME), required=True)
    args = cli.parse_args(); tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith("max12_812_order2_p0_total_rees_j2_a1_grade19_rational_orbit_v35_")):
        fail("registered AWS EC2 lane required")
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=False)
    for path, expected in ((V34_Q / "RESULT.json", V34_Q_RESULT_SHA),
                           (V34_P / "RESULT.json", V34_P_RESULT_SHA),
                           (V34_Q / "compiled/BASIS_G18_q.txt", V34_Q_BASIS_SHA)):
        if digest(path) != expected: fail(("V34 hash", str(path)))

    v33 = load(V33_MODULE, V33_MODULE_SHA, "v35_v33")
    v28 = v33.load_module(v33.V28_MODULE, v33.V28_MODULE_SHA, "v35_v28")
    v20 = v33.load_module(v33.V20_MODULE, v33.V20_SHA, "v35_v20")
    parser = v33.load_module(v33.V23_PARSER, v33.V23_PARSER_SHA, "v35_parser")
    pins = ((v33.V23_RESULT, v33.V23_RESULT_SHA), (v33.V28_RESULT, v33.V28_RESULT_SHA),
            (v33.V30_RESULT, v33.V30_RESULT_SHA))
    for path, expected in pins:
        if digest(path) != expected: fail(("upstream result hash", str(path)))
    # V33 is the current module itself, so its grade-18 manifest is addressed explicitly.
    grade18_dir = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827/aws_q/compiled"
    grade18_result = grade18_dir / "result.json"
    if digest(grade18_result) != "22f64fbb9d2107508f7218a9aabaea03d6c502219baef84bb918352f7e38df0f":
        fail("grade18 result hash")

    base = v20.load_replay(); base.MAX_DEGREE = 19
    tails = json.loads(v20.TAILS.read_text()); coefficients, loads = build_source_series_19(base)
    totals = {row: v28.build_row(base, tails[str(row)], row, coefficients, loads) for row in ROWS}
    killed = parser.J1 | frozenset({"a0", "rho"})
    v23_result = json.loads(v33.V23_RESULT.read_text())
    old_faces = {}; bridge_count = 0
    for name, record in sorted(v23_result["records"].items(), key=lambda item: (item[1]["grade"], item[1]["row"])):
        grade = int(record["grade"]); row = int(record["row"]); chart = record["charts"]["a1_ordered"]
        path = v33.V23 / "output_r1" / chart["output"]
        if digest(path) != chart["output_sha256"]: fail(("V23 hash", name))
        expected = parser.specialize(parser.parse(path), frozenset({"rho"}), {})
        rebuilt = parser.specialize(totals[row][grade], killed, {})
        if rebuilt != expected: fail(("V23 bridge", name))
        old_faces[name] = rebuilt; bridge_count += 1
    manifests = (
        (16, v33.V28_Q, json.loads(v33.V28_RESULT.read_text())),
        (17, v33.V30_Q, json.loads(v33.V30_RESULT.read_text())),
        (18, grade18_dir, json.loads(grade18_result.read_text())),
    )
    for grade, directory, manifest in manifests:
        for row in ROWS:
            name = f"Tg{grade}_{row}"; path = directory / Path(manifest["coefficient_paths"][name]).name
            if digest(path) != manifest["coefficient_sha256"][name]: fail(("row hash", name))
            expected = parser.parse(path); rebuilt = parser.specialize(totals[row][grade], killed, {})
            if rebuilt != expected: fail(("row bridge", name))
            old_faces[name] = rebuilt; bridge_count += 1
    if bridge_count != 63: fail(("bridge count", bridge_count))
    old_nonzero = {name: v28.evaluate(poly, POINT) for name, poly in old_faces.items() if v28.evaluate(poly, POINT)}
    if old_nonzero: fail(("old point", old_nonzero))
    mutation = dict(POINT); mutation["rs2"] += 1
    mutation_nonzero = {name: v28.evaluate(poly, mutation) for name, poly in old_faces.items() if v28.evaluate(poly, mutation)}
    if not mutation_nonzero: fail("mutation control")

    faces = {row: parser.specialize(totals[row][19], killed, {}) for row in ROWS}
    if not all(homogeneous(poly, parser, 19) for poly in faces.values()): fail("grade19 homogeneity")
    values = {row: v28.evaluate(faces[row], POINT) for row in ROWS}
    nonzero_q = {f"Tg19_{row}": value for row, value in values.items() if value}
    lane_nonzero = nonzero_q if args.characteristic == 0 else {name: value for name, value in nonzero_q.items() if modular(value)}
    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    paths = {}; hashes = {}
    for row in ROWS:
        name = f"Tg19_{row}"; path = output / f"{name}_{label}.poly"
        path.write_text(v20.singular_text(faces[row], args.characteristic) + "\n")
        paths[name] = str(path); hashes[name] = digest(path)
    result = {
        "status": "PASS-A1-GRADE19-RATIONAL-ORBIT-V35-COMPILER",
        "registered_aws_lane": tag, "characteristic": args.characteristic,
        "preregistration_sha256": digest(PREREG), "old_bridges": bridge_count,
        "old_point_zero_rows": len(old_faces), "mutation_nonzero_rows": len(mutation_nonzero),
        "point": {name: v28.encode_fraction(value) for name, value in sorted(POINT.items())},
        "grade19_term_counts": {f"Tg19_{row}": len(faces[row]) for row in ROWS},
        "grade19_values_q": {f"Tg19_{row}": v28.encode_fraction(value) for row, value in values.items()},
        "nonzero_rows_q": {name: v28.encode_fraction(value) for name, value in nonzero_q.items()},
        "lane_nonzero_rows": sorted(lane_nonzero),
        "outcome": "survives" if not lane_nonzero else "killed",
        "coefficient_paths": paths, "coefficient_sha256": hashes,
        "v34_q_result_sha256": V34_Q_RESULT_SHA, "v34_p_result_sha256": V34_P_RESULT_SHA,
        "v34_q_basis_sha256": V34_Q_BASIS_SHA,
        "scope": "fixed-support rational representative of the ordered-a1 rho=0 V34 orbit through grade19",
    }
    result_path = output / "result.json"; result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-A1-GRADE19-RATIONAL-ORBIT-V35-COMPILER")
    print(f"V35_OUTCOME={result['outcome']}")
    print(f"V35_NONZERO_ROWS={len(lane_nonzero)}")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
