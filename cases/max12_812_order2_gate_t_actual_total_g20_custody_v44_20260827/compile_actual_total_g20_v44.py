#!/usr/bin/env python3
"""AWS-only exact construction of the seven unspecialized total G20 rows."""

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
ROWS = tuple(range(1, 8))
PRIME = 65521

V33 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827/prolong_boundary_g18_v33.py"
V35 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_grade19_rational_orbit_v35_20260827/evaluate_grade19_orbit_v35.py"
V20 = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/export_allrows_g13_g14_v20.py"
V28 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/prolong_boundary_g16_v28.py"
PARSER = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/census_j2_typed_v23.py"
REPLAY = ROOT / "cases/max12_812_order2_p0_odd_grade14_unit_replay_20260826/replay_row5_grade14.py"
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
V33_G18 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827/aws_q/compiled"
V35_G19 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_grade19_rational_orbit_v35_20260827/aws_q/compiled"
PREREG = HERE / "PREREGISTRATION.md"

PINS = {
    V33: "5941bf876e3ace184190130841046ccc2573615be5cc159608698c5bbdcac36d",
    V35: "843a66318dc36ecacee05f1df3616d36e375d8f93f714cf667b1fb67992543dc",
    V20: "5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587",
    V28: "6c76dc541d27b436a289f1decccd6e90c1424b3a586685e128331c8490b06480",
    PARSER: "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501",
    REPLAY: "2c55284a3fd36e5d9eda26f759353f27d07163d87c30c9f958e84fb32b031258",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    V33_G18 / "result.json": "22f64fbb9d2107508f7218a9aabaea03d6c502219baef84bb918352f7e38df0f",
    V35_G19 / "result.json": "074c7b817d115805ea6e784225fc1dad64d54769ae89421a78ba65769903e256",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load(path: Path, expected: str, name: str):
    if digest(path) != expected:
        fail(("module pin", str(path), digest(path), expected))
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
        or not tag.startswith("max12_812_order2_gate_t_actual_total_g20_custody_v44_")
    ):
        fail("registered ACT-TOT-G20 AWS EC2 lane required")
    return tag


def dense(base, names: list[str]):
    return base.named_series(list(enumerate(names)))


def build_source_series_20(base):
    # This is the V33/V35 actual-total source, extended by exactly one jet in
    # every family which can enter at grade 20.  Nothing is specialized here.
    p = base.series_zero()
    p[0] = base.poly_scale(-2, base.poly_mul(base.poly_var("rho"), base.poly_var("rho")))
    for degree in range(1, 21):
        p[degree] = base.poly_scale(2, base.poly_var(f"ell{degree}"))

    c = base.series_shift(dense(base, ["cs"] + [f"cs{i}" for i in range(1, 19)]), 2)
    r0 = dense(base, ["rs"] + [f"rs{i}" for i in range(1, 19)])
    r = base.series_scale(Fraction(1, 4), base.series_add(base.series_mul(p, p), base.series_shift(r0, 2)))

    az = dense(base, ["a1", "aa1", "aaa1"] + [f"az{i}" for i in range(3, 16)])
    ac = dense(base, ["a0", "aa0", "aaa0"] + [f"ac{i}" for i in range(3, 16)])
    ez = dense(base, ["c1", "e1", "ee1"] + [f"ez{i}" for i in range(3, 16)])
    ec = dense(base, ["c0", "e0", "ee0"] + [f"ec{i}" for i in range(3, 16)])
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
    k10 = dense(base, ["k", "k1", "k2c"] + [f"k10_{i}" for i in range(3, 17)])
    k6 = dense(base, ["k6"] + [f"k6_{i}" for i in range(1, 9)])
    k2 = dense(base, ["k2"])
    loads = {
        7: base.series_shift(k10, 4),
        8: base.series_shift(k6, 12),
        9: base.series_shift(k2, 20),
    }
    return coefficients, loads


def canonical_polynomial(polynomial) -> bytes:
    record = [
        [[list(pair) for pair in monomial], [coefficient.numerator, coefficient.denominator]]
        for monomial, coefficient in sorted(polynomial.items())
    ]
    return json.dumps(record, separators=(",", ":")).encode()


def canonical_series(series) -> bytes:
    record = [json.loads(canonical_polynomial(polynomial)) for polynomial in series]
    return json.dumps(record, separators=(",", ":")).encode()


def variables(polynomial) -> set[str]:
    return {name for monomial in polynomial for name, _ in monomial}


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--characteristic", type=int, choices=(0, PRIME), required=True)
    args = cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)

    for path, expected in PINS.items():
        if digest(path) != expected:
            fail(("input pin", str(path), digest(path), expected))
    v33 = load(V33, PINS[V33], "v44_v33")
    v35 = load(V35, PINS[V35], "v44_v35")
    v20 = load(V20, PINS[V20], "v44_v20")
    v28 = load(V28, PINS[V28], "v44_v28")
    parser = load(PARSER, PINS[PARSER], "v44_parser")
    base = v20.load_replay()
    tails = json.loads(TAILS.read_text())
    counts = {key: len(value) for key, value in sorted(tails.items())}
    if counts != {"1": 36, "2": 54, "3": 58, "4": 81, "5": 89, "6": 120, "7": 131}:
        fail(("569-tail census", counts))
    canonical_tails = sha256(json.dumps(tails, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if canonical_tails != "6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8":
        fail(("canonical tails", canonical_tails))

    # Reconstruct the reviewed grade-19 prefix first.
    base.MAX_DEGREE = 19
    coefficients19, loads19 = v35.build_source_series_19(base)
    totals19 = {row: v28.build_row(base, tails[str(row)], row, coefficients19, loads19) for row in ROWS}

    # Construct every literal unspecialized general-rho row through grade 20.
    # No face map has been called before this point.
    base.MAX_DEGREE = 20
    coefficients20, loads20 = build_source_series_20(base)
    totals20 = {row: v28.build_row(base, tails[str(row)], row, coefficients20, loads20) for row in ROWS}
    prefix_equalities = 0
    for row in ROWS:
        for grade in range(20):
            if totals20[row][grade] != totals19[row][grade]:
                fail(("V35 prefix mismatch", row, grade))
            prefix_equalities += 1
    if prefix_equalities != 140:
        fail(("prefix census", prefix_equalities))

    terminal_expected = {
        "ell20", "cs18", "rs18", "az15", "ac15", "ez15", "ec15",
        "k10_16", "k6_8", "k2",
    }
    terminal_source = set()
    for family in coefficients20.values():
        terminal_source |= {name for name in variables(family[20]) if parser.sigma_weight(name) == 20}
    for family in loads20.values():
        terminal_source |= {name for name in variables(family[20]) if parser.sigma_weight(name) == 20}
    if terminal_source != terminal_expected:
        fail(("terminal source inventory", sorted(terminal_source), sorted(terminal_expected)))

    grade20 = {row: totals20[row][20] for row in ROWS}
    for row, polynomial in grade20.items():
        if not polynomial:
            fail(("zero grade-20 row", row))
        for monomial in polynomial:
            weight = sum(parser.sigma_weight(name) * exponent for name, exponent in monomial)
            if weight != 20:
                fail(("inhomogeneous grade-20 row", row, monomial, weight))
            if any(name == "rho" and exponent % 2 for name, exponent in monomial):
                fail(("rho parity", row, monomial))

    # Only now apply the unrelated ordered-a1 rho=0 face, as an anchor check.
    killed = parser.J1 | frozenset({"a0", "rho"})
    bridge_count = 0
    for grade, directory, manifest_path in (
        (18, V33_G18, V33_G18 / "result.json"),
        (19, V35_G19, V35_G19 / "result.json"),
    ):
        manifest = json.loads(manifest_path.read_text())
        for row in ROWS:
            name = f"Tg{grade}_{row}"
            path = directory / Path(manifest["coefficient_paths"][name]).name
            if digest(path) != manifest["coefficient_sha256"][name]:
                fail(("frozen face row hash", name))
            expected = parser.parse(path)
            observed = parser.specialize(totals20[row][grade], killed, {})
            if observed != expected:
                fail(("face bridge", name))
            bridge_count += 1
    if bridge_count != 14:
        fail(("face bridge census", bridge_count))

    label = "q" if args.characteristic == 0 else f"p{args.characteristic}"
    row_paths = {}
    row_hashes = {}
    rational_hashes = {}
    truncation_hashes = {}
    term_counts = {}
    supports = {}
    receiver_rows = {name: [] for name in sorted(terminal_expected)}
    for row, polynomial in grade20.items():
        name = f"Tg20_{row}"
        path = output / f"{name}_{label}.poly"
        path.write_text(v20.singular_text(polynomial, args.characteristic) + "\n")
        row_paths[name] = str(path)
        row_hashes[name] = digest(path)
        rational_hashes[name] = sha256(canonical_polynomial(polynomial)).hexdigest()
        truncation_hashes[f"Trow{row}_through20"] = sha256(canonical_series(totals20[row])).hexdigest()
        term_counts[name] = len(polynomial)
        supports[name] = sorted(variables(polynomial))
        for receiver in terminal_expected & variables(polynomial):
            receiver_rows[receiver].append(row)
    if any(not rows for rows in receiver_rows.values()):
        fail(("terminal receiver absent from all rows", receiver_rows))

    exact_input_hashes = {str(path.relative_to(ROOT)): expected for path, expected in PINS.items()}
    result = {
        "status": "PASS-ACT-TOT-G20-CUSTODY-V44-COMPILER",
        "registered_aws_lane": tag,
        "host": platform.node(),
        "characteristic": args.characteristic,
        "preregistration_sha256": digest(PREREG),
        "compiler_sha256": digest(Path(__file__)),
        "exact_input_sha256": exact_input_hashes,
        "tails_byte_sha256": PINS[TAILS],
        "tails_canonical_sha256": canonical_tails,
        "tail_counts": counts,
        "tail_total": sum(counts.values()),
        "general_rho_rows_constructed_before_face": True,
        "v35_prefix_polynomial_equalities": prefix_equalities,
        "frozen_face_bridges_after_construction": bridge_count,
        "terminal_source_variables": sorted(terminal_source),
        "terminal_receiver_rows": receiver_rows,
        "grade20_term_counts": term_counts,
        "grade20_supports": supports,
        "grade20_rational_canonical_sha256": rational_hashes,
        "row_truncation_through20_canonical_sha256": truncation_hashes,
        "row_paths": row_paths,
        "row_sha256": row_hashes,
        "target_schedule": {"2": 28, "4": 32, "6": 36, "7": 38},
        "target_terms_through_grade20": 0,
        "scope": (
            "seven literal unspecialized general-rho actual-total raw rows through grade20; "
            "custody only; no contact fidelity, cover, ramified-fibre, G2, Gate-T, order-two, "
            "maximum-twelve, JC2, or counterexample verdict"
        ),
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-ACT-TOT-G20-CUSTODY-V44-COMPILER")
    print(f"CHARACTERISTIC={args.characteristic}")
    print(f"PREFIX_EQUALITIES={prefix_equalities}")
    print(f"FACE_BRIDGES={bridge_count}")
    print(f"TAIL_TOTAL={sum(counts.values())}")
    print(f"GRADE20_TOTAL_TERMS={sum(term_counts.values())}")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()

