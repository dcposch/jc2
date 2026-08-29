#!/usr/bin/env python3
"""AWS-only exact finite-jet map for the total (a,c,r)=(2,5,>=3) contact."""

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
V44_DIR = ROOT / "cases/max12_812_order2_gate_t_actual_total_g20_custody_v44_20260827"
V44_COMPILER = V44_DIR / "compile_actual_total_g20_v44.py"
V44R1_DIR = ROOT / "cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r1_20260827"
V44R1_COMPILER = V44R1_DIR / "compile_actual_total_g20_v44r1.py"
V44_RESULT = V44R1_DIR / "compiler_pass_validator_failed_v1_aws_q_r6a/compiled/result.json"
V44R3_DIR = ROOT / "cases/max12_812_order2_gate_t_actual_total_g20_custody_v44r3_20260827"
V44R3_FREEZE = V44R3_DIR / "FREEZE.sha256"
V44R3_VALIDATOR = V44R3_DIR / "validate_frozen_v44r1_v44r3.py"
V44R3_CROSS_VALIDATOR = V44R3_DIR / "validate_crosslane_v44r3.py"
V44R3_Q = V44R3_DIR / "aws_qcross_r6a/RESULT_q.json"
V44R3_P = V44R3_DIR / "aws_p65521_r6b/RESULT_p65521.json"
V44R3_CROSS = V44R3_DIR / "aws_qcross_r6a/RESULT_CROSS.json"
V20 = ROOT / "cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827/export_allrows_g13_g14_v20.py"
V28 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/prolong_boundary_g16_v28.py"
PARSER = ROOT / "cases/max12_812_order2_p0_total_rees_j2_typed_census_v23_20260827/census_j2_typed_v23.py"
REPLAY = ROOT / "cases/max12_812_order2_p0_odd_grade14_unit_replay_20260826/replay_row5_grade14.py"
TAILS = ROOT / "cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json"
D1_DIR = ROOT / "cases/max12_812_order2_square_owner_d1_unique_ac_d23_lowa6_local_row_20260826"
D1_COMPILER = D1_DIR / "compile_local_row.py"
D1_INVENTORY = D1_DIR / "aws_v7_q/compiled/source_inventory.json"
D1_STDOUT = D1_DIR / "aws_v7_q/run/max12_812_order2_square_d1_unique_ac_d23_lowa6_localrow_v7_q_20260826.stdout"
D1_PROMOTION = ROOT / "xmodel/max12-812-order2-square-d1-unique-ac-d23-lowa6-local-row-promotion-20260826.md"
D1_REVIEW = ROOT / "xmodel/max12-812-order2-square-d1-unique-ac-d23-lowa6-local-row-hostile-review-grok-20260826.md"
KUMMER = ROOT / "xmodel/max12-812-order2-gate-t-kummer-row-bridge-discriminator-sol-20260827.md"
KUMMER_REVIEW = ROOT / "xmodel/max12-812-order2-gate-t-kummer-row-bridge-hostile-review-opus5-20260827.md"
KUMMER_ERRATUM = ROOT / "xmodel/max12-812-order2-gate-t-kummer-row-bridge-erratum-sol-20260827.md"
PREREG = HERE / "PREREGISTRATION.md"

PINS = {
    V44_COMPILER: "dd8681a66f150069db3e4553caa0fd66e70f360994b9a1328a34a4a50cac5003",
    V44R1_COMPILER: "f25b6204457c707a549a2bee06c467452d35abebc337f715b8012302ddad1a23",
    V44_RESULT: "229695dc89f7746f9f664d368c82fa618a43f6b0a0e58c45e13fa9881ea390c2",
    V44R3_FREEZE: "7a25171d5685d8db3b1c9d2ca5f293209d60f07bdb4adf2fa7a3bf9ff9dec0ae",
    V44R3_VALIDATOR: "68045c27895d9d9d056010812e4e1fa7dc016cdeba3f5d6549508114745d9efe",
    V44R3_CROSS_VALIDATOR: "14097472d6ac02fb2bdb5482e346041d67fdf3098e41acaab499f36da2301afe",
    V44R3_Q: "c8a14e4fc4c627263e75f963838293dbe88ee46d17c770b7be16eb76799418cf",
    V44R3_P: "4b4b49b52e29a69c4bae6d88e7bc456dc96db7b299a67652d74287b2696df9e2",
    V44R3_CROSS: "6b3f87e68cd30fe9cb35934bad4fa8cebd1ad0181d5212aa7165ee728f6567bb",
    V20: "5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587",
    V28: "6c76dc541d27b436a289f1decccd6e90c1424b3a586685e128331c8490b06480",
    PARSER: "14f2de22d8cabaea12ac7fc7bf72cca275edbbb6a35dc7c0556a6e18e67c4501",
    REPLAY: "2c55284a3fd36e5d9eda26f759353f27d07163d87c30c9f958e84fb32b031258",
    TAILS: "d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848",
    D1_COMPILER: "b2fe07fdd2f855598dde5c6ef9828909c94496eb5e196756eff504056cde2769",
    D1_INVENTORY: "c8eb56409a49ff6ad76d496c7ba38645eceb82b02a9bb67a5cce987e128d5f48",
    D1_STDOUT: "ad447f4daae1c62374c392e8fb297052fde2eafe20efcf8ba1595384ff457775",
    D1_PROMOTION: "8b92c22bebae73e3efd793c7c7541c53caf8e956f5ce181240c164f3362864da",
    D1_REVIEW: "841f0d6ccbb596fa4ace3f08760f039eb288030efa91075112e915d1320592a3",
    KUMMER: "1b583d5a58ae3c26edd2f394e85e2540871ccfd996ec0bc798b84235c564361a",
    KUMMER_REVIEW: "d62b3f22bcad7de1bacecfa13c455f90bd654b578dd23cc5d2439054993f76f3",
    KUMMER_ERRATUM: "614ddcdb17ae233cd2babea5b45f329f57a7e28e13c7bc0616e78c6bc1731571",
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
        or not tag.startswith("max12_812_order2_gate_t_drho_a2d3_composition_v45_")
    ):
        fail("registered A2D3 AWS EC2 lane required")
    return tag


def dense(base, names: list[str]):
    return base.named_series(list(enumerate(names)))


def variables(polynomial) -> set[str]:
    return {name for monomial in polynomial for name, _ in monomial}


def canonical(polynomial) -> str:
    record = [
        [[list(pair) for pair in monomial], [coefficient.numerator, coefficient.denominator]]
        for monomial, coefficient in sorted(polynomial.items())
    ]
    return sha256(json.dumps(record, separators=(",", ":")).encode()).hexdigest()


def kill(polynomial, killed: set[str]):
    return {
        monomial: coefficient
        for monomial, coefficient in polynomial.items()
        if not any(name in killed for name, _ in monomial)
    }


def linear_map(polynomial, mapping: dict[str, tuple[str, Fraction]]):
    answer = {}
    for monomial, coefficient in polynomial.items():
        exponents = {}
        value = coefficient
        for name, exponent in monomial:
            if name not in mapping:
                fail(("unmapped surviving variable", name))
            target, scale = mapping[name]
            value *= scale ** exponent
            exponents[target] = exponents.get(target, 0) + exponent
        key = tuple(sorted((name, exponent) for name, exponent in exponents.items() if exponent))
        answer[key] = answer.get(key, Fraction(0)) + value
        if not answer[key]:
            del answer[key]
    return answer


def build_d1_series(base):
    p = base.series_zero()
    p[0] = base.poly_scale(-2, base.poly_mul(base.poly_var("lam"), base.poly_var("lam")))
    for degree in range(1, 4):
        p[degree] = base.poly_scale(2, base.poly_var(f"ell{degree}"))
    az = base.series_shift(dense(base, ["a1D", "a1D_1", "a1D_2", "a1D_3"]), 2)
    ac = base.series_shift(dense(base, ["a0D", "a0D_1", "a0D_2", "a0D_3"]), 2)
    cz = base.series_shift(dense(base, ["c1D", "c1D_1", "c1D_2", "c1D_3"]), 5)
    cc = base.series_shift(dense(base, ["c0D", "c0D_1", "c0D_2", "c0D_3"]), 5)
    rz = base.series_shift(dense(base, ["b1", "b1_1"]), 3)
    rc = base.series_shift(dense(base, ["b0", "b0_1"]), 3)
    kc = base.series_shift(rz, 2)
    kr = base.series_add(base.series_scale(Fraction(1, 4), base.series_mul(p, p)), base.series_shift(rc, 2))
    n3 = base.series_shift(az, 3)
    n2 = base.series_shift(ac, 3)
    n1 = base.series_shift(base.series_add(base.series_scale(Fraction(1, 2), base.series_mul(p, az)), cz), 3)
    n0 = base.series_shift(base.series_add(base.series_scale(Fraction(1, 2), base.series_mul(p, ac)), cc), 3)
    coefficients = {
        6: base.series_scale(2, p),
        5: base.series_scale(2, kc),
        4: base.series_add(base.series_mul(p, p), base.series_scale(2, kr)),
        3: base.series_add(base.series_scale(2, base.series_mul(p, kc)), base.series_shift(n3, 2)),
        2: base.series_add(base.series_mul(kc, kc), base.series_scale(2, base.series_mul(p, kr)), base.series_shift(n2, 2)),
        1: base.series_add(base.series_scale(2, base.series_mul(kc, kr)), base.series_shift(n1, 2)),
        0: base.series_add(base.series_mul(kr, kr), base.series_shift(n0, 2)),
    }
    loads = {
        7: base.series_shift(dense(base, ["k0", "k0_1", "k0_2"]), 4),
        8: base.series_shift(dense(base, ["k60"]), 12),
        9: base.series_shift(dense(base, ["k20"]), 20),
    }
    return coefficients, loads


def total_jet_name(family: str, index: int) -> str:
    aliases = {
        "Az": ("a1", "aa1", "aaa1"),
        "Ac": ("a0", "aa0", "aaa0"),
        "Ez": ("c1", "e1", "ee1"),
        "Ec": ("c0", "e0", "ee0"),
        "K10": ("k", "k1", "k2c"),
    }
    if family in aliases and index < len(aliases[family]):
        return aliases[family][index]
    stems = {
        "Az": "az", "Ac": "ac", "Ez": "ez", "Ec": "ec",
        "Cs": "cs", "Rs": "rs", "K10": "k10_", "K6": "k6_", "K2": "k2_",
    }
    if family in ("Cs", "Rs") and index == 0:
        return stems[family]
    if family == "K6" and index == 0:
        return "k6"
    if family == "K2" and index == 0:
        return "k2"
    return f"{stems[family]}{index}"


def d1_jet_name(stem: str, index: int) -> str:
    return stem if index == 0 else f"{stem}_{index}"


def derive_contact_map(block: dict[str, object]):
    a = int(block["a"])
    c = a + int(block["d"])
    r = int(block["r_floor"])
    maxima = block["jet_maxima"]
    if not isinstance(maxima, dict):
        fail("malformed endpoint maxima")
    mapping: dict[str, tuple[str, Fraction]] = {"rho": ("lam", Fraction(1))}
    for index in range(1, int(maxima["p"]) + 1):
        mapping[f"ell{index}"] = (f"ell{index}", Fraction(1))
    shifted = (
        ("Az", a, "a1D", "A", Fraction(1)),
        ("Ac", a, "a0D", "A", Fraction(1)),
        ("Ez", c, "c1D", "C", Fraction(2)),
        ("Ec", c, "c0D", "C", Fraction(2)),
        ("Cs", r, "b1", "R", Fraction(1)),
        ("Rs", r, "b0", "R", Fraction(4)),
    )
    for family, start, target, maximum_key, scale in shifted:
        for relative in range(int(maxima[maximum_key]) + 1):
            mapping[total_jet_name(family, start + relative)] = (
                d1_jet_name(target, relative), scale,
            )
    for family, target, maximum_key in (
        ("K10", "k0", "k10"), ("K6", "k60", "k6"), ("K2", "k20", "k2"),
    ):
        for relative in range(int(maxima[maximum_key]) + 1):
            mapping[total_jet_name(family, relative)] = (d1_jet_name(target, relative), Fraction(1))
    lower_killed = {
        total_jet_name(family, index)
        for family, order in (("Az", a), ("Ac", a), ("Ez", c), ("Ec", c), ("Cs", r), ("Rs", r))
        for index in range(order)
    }
    derived = {
        key: int(maxima[key]) for key in ("p", "A", "C", "R", "k10", "k6", "k2")
    }
    return mapping, lower_killed, derived


def endpoint_custody() -> dict[str, object]:
    inventory = json.loads(D1_INVENTORY.read_text())
    block = next(item for item in inventory["blocks"] if item["a"] == 2 and item["d"] == 3)
    expected = {
        "G": 17, "T": 20, "a": 2, "d": 3,
        "jet_maxima": {"A": 3, "C": 3, "R": 1, "k10": 2, "k2": 0,
                       "k6": 0, "mu2": 0, "mu4": 0, "p": 3},
        "maxpole": 2, "negative": False, "primitive_count": 6,
        "r_floor": 3, "s_min": 1,
    }
    if block != expected:
        fail(("B23 inventory", block))
    markers = (
        "B23_BASELINE=A2_D3_S1_G17_T20",
        "B23_PRIMITIVE_COUNT=6",
        "B23_GLOBAL_POLE_CEILING=2",
        "B23_MOVING_L2_RECURRENCE=1",
        "B23_TARGET_FREE_LOCAL_ROWS=1",
        "B23_BOTH_ORIENTATIONS=1",
        "B23_LOCAL_COEFFICIENT=3/2*lam^2*cv^2",
        "B23_ENDPOINT=PASS_EMPTY_CLOSED_R_TAIL",
    )
    transcript = D1_STDOUT.read_text()
    if any(transcript.count(marker) != 1 for marker in markers):
        fail("B23 transcript marker")
    return {"inventory": block, "markers": list(markers)}


def orientation_check() -> dict[str, object]:
    samples = [
        (Fraction(1), Fraction(2), Fraction(3), Fraction(5), Fraction(7), Fraction(11)),
        (Fraction(3, 2), Fraction(-4), Fraction(9, 5), Fraction(-2), Fraction(11, 3), Fraction(5, 7)),
    ]
    records = []
    for rho, ell1, ell2, ell3, au, cv in samples:
        for epsilon in (1, -1):
            lam0 = epsilon * rho
            lam1 = -ell1 / (2 * lam0)
            lam2 = -(ell2 + lam1 * lam1) / (2 * lam0)
            lam3 = -(ell3 + 2 * lam1 * lam2) / (2 * lam0)
            equations = (
                lam0 * lam0 - rho * rho,
                2 * lam0 * lam1 + ell1,
                lam1 * lam1 + 2 * lam0 * lam2 + ell2,
                2 * lam0 * lam3 + 2 * lam1 * lam2 + ell3,
            )
            if equations != (0, 0, 0, 0):
                fail(("Hensel", samples, epsilon, equations))
            # Constant,z,z^2 coefficients of the complementary allocation.
            product = (-au * lam0 * cv * lam0, Fraction(0), au * cv)
            wanted = (-au * cv * rho * rho, Fraction(0), au * cv)
            if product != wanted:
                fail(("allocation", product, wanted))
            residue = Fraction(3, 2) * rho * rho * cv * cv
            if not residue:
                fail("zero sample residue")
            records.append({
                "epsilon": epsilon, "rho": str(rho), "lambda": [str(lam0), str(lam1), str(lam2), str(lam3)],
                "A0": "au*(z-lambda0)", "C0": "cv*(z+lambda0)",
                "terminal_residue": str(residue),
            })
    return {
        "hensel": [
            "lambda0=epsilon*rho",
            "lambda1=-ell1/(2*lambda0)",
            "lambda2=-(ell2+lambda1^2)/(2*lambda0)",
            "lambda3=-(ell3+2*lambda1*lambda2)/(2*lambda0)",
        ],
        "deck": "epsilon=+1 and epsilon=-1 are exchanged by rho |-> -rho",
        "terminal_functional": "Phi4+lambda(sigma)*(Phi3+(P/4)*Phi1)",
        "terminal_residue": "(3/2)*rho^2*cv^2",
        "samples": records,
    }


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    args = cli.parse_args()
    tag = require_aws()
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    for path, expected in PINS.items():
        if digest(path) != expected:
            fail(("input pin", str(path), digest(path), expected))

    v44 = load(V44_COMPILER, PINS[V44_COMPILER], "v45_v44")
    v20 = load(V20, PINS[V20], "v45_v20")
    v28 = load(V28, PINS[V28], "v45_v28")
    parser = load(PARSER, PINS[PARSER], "v45_parser")
    tails = json.loads(TAILS.read_text())
    base = v20.load_replay()
    base.MAX_DEGREE = 20
    total_coefficients, total_loads = v44.build_source_series_20(base)
    total_rows = {row: v28.build_row(base, tails[str(row)], row, total_coefficients, total_loads) for row in ROWS}

    v44_result = json.loads(V44_RESULT.read_text())
    if (
        v44_result.get("status") != "PASS-ACT-TOT-G20-CUSTODY-V44R1-COMPILER"
        or v44_result.get("characteristic") != 0
        or v44_result.get("compiler_sha256") != PINS[V44R1_COMPILER]
        or v44_result.get("base_compiler_sha256") != PINS[V44_COMPILER]
        or v44_result.get("terminal_grade20_receiver_free") is not True
    ):
        fail("V44R1 result contract")
    v44r3_q = json.loads(V44R3_Q.read_text())
    v44r3_p = json.loads(V44R3_P.read_text())
    v44r3_cross = json.loads(V44R3_CROSS.read_text())
    if (
        v44r3_q.get("status") != "PASS-ACT-TOT-G20-CUSTODY-V44R3-Q"
        or v44r3_p.get("status") != "PASS-ACT-TOT-G20-CUSTODY-V44R3-P65521"
        or v44r3_cross.get("status") != "PASS-ACT-TOT-G20-CUSTODY-V44R3-CROSSLANE"
        or v44r3_q.get("v44r1_compiler_result_sha256") != PINS[V44_RESULT]
        or v44r3_cross.get("q_result_sha256") != PINS[V44_RESULT]
    ):
        fail("V44R3 custody contract")
    for row in ROWS:
        name = f"Tg20_{row}"
        path = V44_RESULT.parent / Path(v44_result["row_paths"][name]).name
        if digest(path) != v44_result["row_sha256"][name]:
            fail(("V44R1 row hash", name))
        if canonical(total_rows[row][20]) != v44_result["grade20_rational_canonical_sha256"][name]:
            fail(("V44R1 canonical row rebuild", name))

    endpoint = endpoint_custody()
    mapping, lower_killed, derived_maxima = derive_contact_map(endpoint["inventory"])
    expected_maxima = {"p": 3, "A": 3, "C": 3, "R": 1, "k10": 2, "k6": 0, "k2": 0}
    if derived_maxima != expected_maxima:
        fail(("derived endpoint maxima", derived_maxima, expected_maxima))
    allowed = set(mapping)
    surviving = {}
    prefix_zero = 0
    support_occurrence = {name: [] for name in sorted(allowed)}
    for row in ROWS:
        surviving[row] = []
        for grade in range(21):
            polynomial = kill(total_rows[row][grade], lower_killed)
            excess = variables(polynomial) - allowed
            if excess:
                fail(("later-jet dependence", row, grade, sorted(excess)))
            if grade < 17:
                if polynomial:
                    fail(("pre-G contact row", row, grade, polynomial))
                prefix_zero += 1
            for name in variables(polynomial):
                support_occurrence[name].append([row, grade])
            surviving[row].append(polynomial)
    if prefix_zero != 119:
        fail(("pre-G zero census", prefix_zero))

    maximal_witnesses = {
        "p": ("ell3",),
        "A": ("az5", "ac5"),
        "C": ("ez8", "ec8"),
        "R": ("cs4", "rs4"),
        "k10": ("k2c",),
    }
    for family, names in maximal_witnesses.items():
        if any(not support_occurrence.get(name) for name in names):
            fail(("unwitnessed derived maximum", family, names, support_occurrence))

    d1_coefficients, d1_loads = build_d1_series(base)
    d1_rows = {row: v28.build_row(base, tails[str(row)], row, d1_coefficients, d1_loads) for row in ROWS}
    deck_mappings = {
        "rho_to_plus_lam": mapping,
        "rho_to_minus_lam": {
            **mapping,
            "rho": ("lam", Fraction(-1)),
        },
    }
    row_equalities_by_deck = {}
    mapped_hashes = {}
    for deck, deck_mapping in deck_mappings.items():
        row_equalities = 0
        for row in ROWS:
            window = []
            for grade in range(21):
                mapped = linear_map(surviving[row][grade], deck_mapping)
                if mapped != d1_rows[row][grade]:
                    fail(("total/D1 coefficient", deck, row, grade, canonical(mapped), canonical(d1_rows[row][grade])))
                row_equalities += 1
                if grade >= 17:
                    window.append([grade, canonical(mapped), len(mapped)])
            mapped_hashes[f"{deck}_row{row}_g17_g20"] = sha256(
                json.dumps(window, separators=(",", ":")).encode()
            ).hexdigest()
        if row_equalities != 147:
            fail(("row equality census", deck, row_equalities))
        row_equalities_by_deck[deck] = row_equalities
    for row in ROWS:
        if mapped_hashes[f"rho_to_plus_lam_row{row}_g17_g20"] != mapped_hashes[f"rho_to_minus_lam_row{row}_g17_g20"]:
            fail(("deck row hash", row))

    orientations = orientation_check()
    result = {
        "status": "PASS-KGT-DRHO-UAC-A2D3-V45-COMPILER",
        "registered_aws_lane": tag,
        "host": platform.node(),
        "preregistration_sha256": digest(PREREG),
        "compiler_sha256": digest(Path(__file__)),
        "exact_input_sha256": {str(path.relative_to(ROOT)): expected for path, expected in PINS.items()},
        "g20_custody": {
            "v44r1_q_compiler_result_sha256": PINS[V44_RESULT],
            "v44r3_q_validation_sha256": PINS[V44R3_Q],
            "v44r3_p65521_validation_sha256": PINS[V44R3_P],
            "v44r3_crosslane_sha256": PINS[V44R3_CROSS],
        },
        "contact": {"ord_A": 2, "ord_C": 5, "ord_R_floor": 3, "d": 3, "G": 17, "T": 20},
        "lower_contact_vanishings": sorted(lower_killed),
        "finite_jet_map": {name: [target, [scale.numerator, scale.denominator]] for name, (target, scale) in sorted(mapping.items())},
        "derived_maxima": derived_maxima,
        "maximal_source_witnesses": maximal_witnesses,
        "surviving_support_occurrence": support_occurrence,
        "pre_G_zero_coefficients": prefix_zero,
        "total_D1_coefficient_equalities_by_deck": row_equalities_by_deck,
        "total_D1_coefficient_equalities": sum(row_equalities_by_deck.values()),
        "deck_row_hash_agreement": True,
        "mapped_row_window_sha256": mapped_hashes,
        "D1_B23": endpoint,
        "orientations": orientations,
        "outcome": (
            "PROVISIONAL PENDING HOSTILE REVIEW: after reviewed generic-square gates, "
            "ord(A)=2,ord(C)=5,ord(R)>=3 is excluded on D(rho*k)"
        ),
        "scope": (
            "one strict unit-load unique-AC contact only; no cover, equality face, positive-order load, "
            "k=0, rho=0, Rees chart/receiver, G2, Gate-T, order-two, maximum-twelve, JC2, or counterexample verdict"
        ),
    }
    result_path = output / "result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("PASS-KGT-DRHO-UAC-A2D3-V45-COMPILER")
    print(f"PRE_G_ZERO={prefix_zero}")
    print(f"TOTAL_D1_EQUALITIES={sum(row_equalities_by_deck.values())}")
    print("TOTAL_D1_EQUALITIES_PER_DECK=147")
    print("BOTH_ORIENTATIONS=1")
    print("TERMINAL_RESIDUE=3/2*rho^2*cv^2")
    print(f"RESULT_SHA256={digest(result_path)}")


if __name__ == "__main__":
    main()
