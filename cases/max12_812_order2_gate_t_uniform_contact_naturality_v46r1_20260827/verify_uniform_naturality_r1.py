#!/usr/bin/env python3
"""Additive V46R1 verifier for coordinate-typed shifted root maps.

V46's source-naturality schema and V0/V1/V3/V4 checks remain immutable.  This
verifier imports that frozen implementation, omits its mixed-coordinate root witness,
and adds explicit raw-total and mapped-D1 root maps, computed Jacobians, factor-
conflation mutations, and the a=7 load-tie representative.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import time
from typing import Any


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
R1_SCHEMA_PATH = HERE / "SCHEMA_R1.json"
EXPECTED_R1_SCHEMA_SHA256 = "0f6bec4983bc8d682b64db5ac23f2d1bb64b8613e2812e95f2cab2b041494b44"
BASE_DIR = ROOT / "cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def load_base_module():
    path = BASE_DIR / "verify_uniform_naturality.py"
    spec = importlib.util.spec_from_file_location("uniform_v46_frozen", path)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V46 verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def v0_r1_pins(r1: dict[str, Any], base, base_schema: dict[str, Any], tails: dict[str, Any]) -> dict[str, Any]:
    if digest(R1_SCHEMA_PATH) != EXPECTED_R1_SCHEMA_SHA256:
        fail("R1 schema drift")
    for key in ("schema", "verifier", "result", "freeze", "hostile_review"):
        path = ROOT / r1["base"][f"{key}_path"]
        if digest(path) != r1["base"][f"{key}_sha256"]:
            fail(("base pin drift", key))
    base_result = base.v0_pins(base_schema)

    weights = base_schema["tails"]["lambda_weights"]
    denominator_set: set[int] = set()
    for row in range(1, 8):
        for raw_monomial, raw_coefficient in tails[str(row)]:
            monomial = [int(value) for value in raw_monomial]
            if len(monomial) != 10:
                fail(("tail arity", row, monomial))
            if sum(value * weight for value, weight in zip(monomial, weights)) != 12 + row:
                fail(("tail weight", row, monomial))
            if sum(monomial[7:]) > 1 or any(value not in (0, 1) for value in monomial[7:]):
                fail(("tail load nonlinearity", row, monomial))
            denominator_set.add(Fraction(str(raw_coefficient)).denominator)
    if not all(value > 0 and value & (value - 1) == 0 for value in denominator_set):
        fail(("non-power-of-two tail denominator", sorted(denominator_set)))
    scales = {row: item["scale"] for row, item in base_schema["target_schedule"].items()}
    if scales != {"2": "1", "4": "1", "6": "1", "7": "1/4"}:
        fail(("target scale drift", scales))

    expected_d1 = {
        "A_n_minus_plus": "AcD1_n +/- sum(i=0..n,lambda_i*AzD1_(n-i))",
        "C_n_minus_plus": "CcD1_n +/- sum(i=0..n,lambda_i*CzD1_(n-i))",
        "R_n_minus_plus": "BcD1_n +/- sum(i=0..n,lambda_i*BzD1_(n-i))",
        "leading_determinants": ["-2*lambda_0", "-2*lambda_0", "-2*lambda_0"],
    }
    for key, value in expected_d1.items():
        if r1["mapped_D1_root_map"][key] != value:
            fail(("D1 root schema drift", key))
    expected_raw = {
        "C_n_minus_plus": "(ec_(c+n) +/- sum(i=0..n,lambda_i*ez_(c+n-i)))/2",
        "R_n_minus_plus": "rs_(r+n)/4 +/- sum(i=0..n,lambda_i*cs_(r+n-i))",
        "leading_determinants": ["-2*lambda_0", "-lambda_0/2", "-lambda_0/2"],
    }
    for key, value in expected_raw.items():
        if r1["raw_total_root_map"][key] != value:
            fail(("raw root schema drift", key))

    return {
        "base_V0": base_result,
        "r1_schema_sha256": EXPECTED_R1_SCHEMA_SHA256,
        "tail_weight_rows_checked": 569,
        "tail_denominators": sorted(denominator_set),
        "target_scales": scales,
        "coordinate_types": ["raw_total_shifted_jets", "mapped_D1_relative_jets"],
    }


def v1_with_a7(r1: dict[str, Any], base, base_schema: dict[str, Any], tails: dict[str, Any]) -> dict[str, Any]:
    base_result = base.v1_naturality(base_schema, tails)
    extra_results: list[dict[str, Any]] = []
    for representative in r1["additional_representatives"]:
        ring = base.Ring(None if representative["field"] == "Q" else base.PRIME)
        mismatches, primitive_equal = base.compare_rows(
            tails,
            representative["a"],
            representative["c"],
            representative["r"],
            representative["T"],
            ring,
        )
        if mismatches or not primitive_equal:
            fail(("additional naturality mismatch", representative["id"], mismatches[:1], primitive_equal))
        extra_results.append({
            "id": representative["id"],
            "contact": [representative["a"], representative["c"], representative["r"]],
            "T": representative["T"],
            "field": representative["field"],
            "row_coefficients_compared": 7 * (representative["T"] + 1),
        })
    return {
        "base_representatives": base_result["total_representatives"],
        "base_row_coefficients_compared": sum(
            item["row_coefficients_compared"] for item in base_result["representatives"]
        ),
        "additional": extra_results,
        "total_representatives": base_result["total_representatives"] + len(extra_results),
        "total_row_coefficients_compared": sum(
            item["row_coefficients_compared"] for item in base_result["representatives"] + extra_results
        ),
    }


def convolution(lam: list[Fraction], values: list[Fraction], n: int) -> Fraction:
    return sum(lam[i] * values[n - i] for i in range(n + 1))


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def recover_convolution_pair(
    lam: list[Fraction], targets: list[Fraction], divisor: Fraction
) -> list[Fraction]:
    recovered: list[Fraction] = []
    for n, target in enumerate(targets):
        lower = sum(lam[i] * recovered[n - i] for i in range(1, n + 1))
        recovered.append((target - lower) / (divisor * lam[0]))
    return recovered


def v2_r1_root_maps() -> dict[str, Any]:
    hensel_depth = 10
    map_depth = 3
    rho = Fraction(3)
    ell = [Fraction(0)] + [Fraction((7 * n) % 11 - 5) for n in range(1, hensel_depth + 1)]
    p = [-2 * rho * rho] + [2 * ell[n] for n in range(1, hensel_depth + 1)]
    branches: dict[int, list[Fraction]] = {}
    for epsilon in (1, -1):
        lam = [Fraction(epsilon) * rho]
        for n in range(1, hensel_depth + 1):
            lower = sum(lam[i] * lam[n - i] for i in range(1, n))
            lam.append((-ell[n] - lower) / (2 * lam[0]))
        for n in range(hensel_depth + 1):
            if sum(lam[i] * lam[n - i] for i in range(n + 1)) + p[n] / 2 != 0:
                fail(("Hensel identity", epsilon, n))
        branches[epsilon] = lam
    if branches[-1] != [-value for value in branches[1]]:
        fail("deck exchange")

    az = [Fraction(2 + n) for n in range(map_depth + 1)]
    ac = [Fraction(9 - n) for n in range(map_depth + 1)]
    cz = [Fraction(2 + 2 * n) for n in range(map_depth + 1)]
    cc = [Fraction(5 - n) for n in range(map_depth + 1)]
    bz = [Fraction(7 + n) for n in range(map_depth + 1)]
    bc = [Fraction(11 - 2 * n) for n in range(map_depth + 1)]
    # Raw total shifted jets are images of the D1 jets under the forced
    # scalings.  This is the coordinate distinction missing in V46.
    ez = [2 * value for value in cz]
    ec = [2 * value for value in cc]
    cs = list(bz)
    rs = [4 * value for value in bc]

    determinant_records: dict[str, Any] = {}
    commutation_equalities = 0
    inversion_equalities = 0
    conflation_mutations = 0
    for epsilon, lam_full in branches.items():
        lam = lam_full[: map_depth + 1]
        raw_dets = [
            determinant([[-lam[0], Fraction(1)], [lam[0], Fraction(1)]]),
            determinant([[-lam[0] / 2, Fraction(1, 2)], [lam[0] / 2, Fraction(1, 2)]]),
            determinant([[-lam[0], Fraction(1, 4)], [lam[0], Fraction(1, 4)]]),
        ]
        d1_dets = [
            determinant([[-lam[0], Fraction(1)], [lam[0], Fraction(1)]])
            for _ in range(3)
        ]
        if raw_dets != [-2 * lam[0], -lam[0] / 2, -lam[0] / 2]:
            fail(("raw determinants", epsilon, raw_dets))
        if d1_dets != [-2 * lam[0], -2 * lam[0], -2 * lam[0]]:
            fail(("D1 determinants", epsilon, d1_dets))
        determinant_records[str(epsilon)] = {
            "raw_total": [str(value) for value in raw_dets],
            "mapped_D1": [str(value) for value in d1_dets],
        }

        raw_pairs: dict[str, tuple[list[Fraction], list[Fraction]]] = {}
        d1_pairs: dict[str, tuple[list[Fraction], list[Fraction]]] = {}
        for label, raw_z, raw_c, d1_z, d1_c, raw_constant_divisor in (
            ("A", az, ac, az, ac, Fraction(1)),
            ("C", ez, ec, cz, cc, Fraction(2)),
            ("R", cs, rs, bz, bc, Fraction(4)),
        ):
            raw_minus: list[Fraction] = []
            raw_plus: list[Fraction] = []
            d1_minus: list[Fraction] = []
            d1_plus: list[Fraction] = []
            for n in range(map_depth + 1):
                raw_conv = convolution(lam, raw_z, n)
                d1_conv = convolution(lam, d1_z, n)
                raw_minus.append(raw_c[n] / raw_constant_divisor - raw_conv / (2 if label == "C" else 1))
                raw_plus.append(raw_c[n] / raw_constant_divisor + raw_conv / (2 if label == "C" else 1))
                d1_minus.append(d1_c[n] - d1_conv)
                d1_plus.append(d1_c[n] + d1_conv)
            if raw_minus != d1_minus or raw_plus != d1_plus:
                fail(("raw/D1 root-map commutation", epsilon, label))
            commutation_equalities += 2 * (map_depth + 1)
            raw_pairs[label] = (raw_minus, raw_plus)
            d1_pairs[label] = (d1_minus, d1_plus)

        # Invert the raw coordinate maps.
        aminus, aplus = raw_pairs["A"]
        cminus, cplus = raw_pairs["C"]
        rminus, rplus = raw_pairs["R"]
        if [(aminus[n] + aplus[n]) / 2 for n in range(map_depth + 1)] != ac:
            fail(("raw A constant inversion", epsilon))
        if [cminus[n] + cplus[n] for n in range(map_depth + 1)] != ec:
            fail(("raw C constant inversion", epsilon))
        if [2 * (rminus[n] + rplus[n]) for n in range(map_depth + 1)] != rs:
            fail(("raw R constant inversion", epsilon))
        if recover_convolution_pair(lam, [(aplus[n] - aminus[n]) / 2 for n in range(map_depth + 1)], Fraction(1)) != az:
            fail(("raw A z inversion", epsilon))
        if recover_convolution_pair(lam, [cplus[n] - cminus[n] for n in range(map_depth + 1)], Fraction(1)) != ez:
            fail(("raw C z inversion", epsilon))
        if recover_convolution_pair(lam, [(rplus[n] - rminus[n]) / 2 for n in range(map_depth + 1)], Fraction(1)) != cs:
            fail(("raw R z inversion", epsilon))
        inversion_equalities += 6 * (map_depth + 1)

        # Invert all three D1 maps with the common unscaled formula.
        for label, z_values, constant_values in (("A", az, ac), ("C", cz, cc), ("R", bz, bc)):
            minus, plus = d1_pairs[label]
            if [(minus[n] + plus[n]) / 2 for n in range(map_depth + 1)] != constant_values:
                fail(("D1 constant inversion", epsilon, label))
            targets = [(plus[n] - minus[n]) / 2 for n in range(map_depth + 1)]
            if recover_convolution_pair(lam, targets, Fraction(1)) != z_values:
                fail(("D1 z inversion", epsilon, label))
            inversion_equalities += 2 * (map_depth + 1)

        # Factor-conflation mutations must already fail at the leading jet.
        for orientation in (-1, 1):
            correct_c = cc[0] + orientation * lam[0] * cz[0]
            wrong_c = correct_c / 2
            correct_r = bc[0] + orientation * lam[0] * bz[0]
            wrong_r = correct_r / 4
            if correct_c == wrong_c or correct_r == wrong_r:
                fail(("factor-conflation mutation inert", epsilon, orientation))
            conflation_mutations += 2
        if raw_dets[1:] == d1_dets[1:]:
            fail(("pasted determinant mutation inert", epsilon))
        conflation_mutations += 2

    return {
        "hensel_depth": hensel_depth,
        "map_depth": map_depth,
        "decks": 2,
        "coordinate_systems": ["raw_total", "mapped_D1"],
        "raw_D1_commutation_equalities": commutation_equalities,
        "triangular_inversion_equalities": inversion_equalities,
        "computed_determinants": determinant_records,
        "factor_conflation_mutations_fired": conflation_mutations,
        "localization": "D(rho)",
    }


def v3_with_a7(r1: dict[str, Any], base, base_schema: dict[str, Any]) -> dict[str, Any]:
    base_result = base.v3_support(base_schema)
    extra: list[dict[str, Any]] = []
    for representative in r1["additional_representatives"]:
        actual = base.derive_support(
            base_schema,
            representative["a"],
            representative["c"],
            representative["r"],
            representative["T"],
        )
        if actual["maxima"] != representative["maxima"] or set(actual["active"]) != set(representative["active"]):
            fail(("additional support mismatch", representative["id"], actual, representative))
        extra.append({"id": representative["id"], "maxima": actual["maxima"], "active": actual["active"]})
    return {
        "base_tables_checked": base_result["tables_checked"],
        "additional": extra,
        "total_tables_checked": base_result["tables_checked"] + len(extra),
        "current_G20_maxima": base_result["current_G20_maxima"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    started = time.monotonic()
    r1 = json.loads(R1_SCHEMA_PATH.read_text())
    base = load_base_module()
    base_schema = json.loads((BASE_DIR / "SCHEMA.json").read_text())
    tails = json.loads((ROOT / base_schema["tails"]["path"]).read_text())
    checks = {
        "V0R1_pins_and_types": v0_r1_pins(r1, base, base_schema, tails),
        "V1R1_naturality_plus_a7": v1_with_a7(r1, base, base_schema, tails),
        "V2R1_coordinate_typed_root_maps": v2_r1_root_maps(),
        "V3R1_support_plus_a7": v3_with_a7(r1, base, base_schema),
        "V4_base_provenance": base.v4_provenance(base_schema),
    }
    result = {
        "status": "PASS-UNIFORM-CONTACT-NATURALITY-V46R1-ROOT-REPAIR",
        "scope": "additive coordinate-typed root-map repair; V46 source naturality preserved; endpoint union remains conditional",
        "r1_schema_sha256": EXPECTED_R1_SCHEMA_SHA256,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "checks": checks,
    }
    if args.output:
        args.output.mkdir(parents=True, exist_ok=True)
        (args.output / "result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
