#!/usr/bin/env python3
"""Compile the literal reviewed GGV 8_28 lower determinant rows Dtil_0..Dtil_40."""

from __future__ import annotations

from dataclasses import dataclass
import gzip
from hashlib import sha256
from math import comb
import json
from pathlib import Path
import sys
from typing import Any

from lf40_common import (
    RAW_REL,
    SparsePoly,
    add_term,
    canonical_bytes,
    digest_file,
    fail,
    freeze_directory,
    multiply_monomials,
    normalize_monomial,
    serialize_poly,
    singular_poly,
    verify_source_pins,
    write_json,
)


EXPECTED_F_PROFILE = [15, 14, 13, 12, 12, 11, 10, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
EXPECTED_G_PROFILE = [22, 21, 20, 19, 19, 18, 17, 16, 16, 15, 14, 13, 13,
                      12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
EXPECTED_RAW_COUNTS = [
    34, 35, 34, 33, 32, 32, 31, 30, 29, 29, 28, 27, 26, 26, 25, 24, 23,
    23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5,
    4, 3, 2, 1, 0,
]
EXPECTED_MIN_DEGREE = [5, 4, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, None]
EXPECTED_MAX_DEGREE = [38] + [39 - row for row in range(1, 40)] + [None]
EXACT_SATURATION_FACTORS = ("a", "b", "rho", "f_0_8", "g_0_12")


@dataclass(frozen=True)
class Slot:
    side: str
    name: str
    i: int
    j: int
    weight: int

    def record(self) -> dict[str, Any]:
        return {
            "side": self.side,
            "slot": self.name,
            "raw_exponents": {"x": self.i, "y": self.j},
            "lower_weight": self.weight,
        }


def ceil_div(numerator: int, denominator: int) -> int:
    return -((-numerator) // denominator)


def expected_side(shift: int, x_ceiling: int, row_ceiling: int) -> dict[int, set[tuple[int, int]]]:
    out: dict[int, set[tuple[int, int]]] = {}
    for row in range(row_ceiling + 1):
        lo = max(0, ceil_div(shift - row, 4))
        hi = x_ceiling - row
        out[row] = {(i, row - shift + 4 * i) for i in range(lo, hi + 1)} if lo <= hi else set()
    return out


def load_slots(root: Path) -> tuple[list[Slot], list[Slot], dict[str, Any]]:
    blob = json.loads((root / RAW_REL).read_text(encoding="utf-8"))
    if blob.get("control_id") != "R0_ARTIFICIAL_CUSP_CONTROL":
        fail(("unexpected D3 control id", blob.get("control_id")))
    result: dict[str, list[Slot]] = {"F": [], "G": []}
    for side, prefix, shift in (("F", "f", 8), ("G", "g", 12)):
        records = blob["raw_slots_through_weight_22"][side]
        for record in records:
            i = record["raw_exponents"]["x"]
            j = record["raw_exponents"]["y"]
            name = f"{prefix}_{i}_{j}"
            if record["slot"] != name:
                fail(("slot/exponent mismatch", record["slot"], name))
            result[side].append(Slot(side, name, i, j, shift - 4 * i + j))
    return result["F"], result["G"], blob


def validate_slots(f_slots: list[Slot], g_slots: list[Slot], raw_blob: dict[str, Any]) -> dict[str, Any]:
    expected_f = expected_side(8, 16, 16)
    expected_g = expected_side(12, 24, 24)
    actual_f = {row: {(slot.i, slot.j) for slot in f_slots if slot.weight == row} for row in range(17)}
    actual_g = {row: {(slot.i, slot.j) for slot in g_slots if slot.weight == row} for row in range(25)}
    if actual_f != expected_f or actual_g != expected_g:
        fail("lower regrade does not equal formula windows on all slots")
    if any(slot.weight < 0 for slot in (*f_slots, *g_slots)):
        fail("negative lower weight")
    f_profile = [len(actual_f[row]) for row in range(17)]
    g_profile = [len(actual_g[row]) for row in range(25)]
    if f_profile != EXPECTED_F_PROFILE or g_profile != EXPECTED_G_PROFILE:
        fail(("row profile mismatch", f_profile, g_profile))
    if len(f_slots) != 141 or len(g_slots) != 301:
        fail(("raw slot census", len(f_slots), len(g_slots)))
    stored_upper_matches = 0
    coincident_weights = 0
    for side, slots, shift in (("F", f_slots, 8), ("G", g_slots, 12)):
        by_name = {record["slot"]: record for record in raw_blob["raw_slots_through_weight_22"][side]}
        for slot in slots:
            stored = by_name[slot.name]["weight"]
            if stored == shift + 3 * slot.i - slot.j:
                stored_upper_matches += 1
            if stored == slot.weight:
                coincident_weights += 1
    if stored_upper_matches != 442 or coincident_weights != 22:
        fail(("stored upper-weight custody changed", stored_upper_matches, coincident_weights))
    return {
        "raw_slots": {"F": len(f_slots), "G": len(g_slots), "total": len(f_slots) + len(g_slots)},
        "lower_zero_weight": {"F": f_profile[0], "G": g_profile[0], "total": f_profile[0] + g_profile[0]},
        "positive_weight": {"F": len(f_slots) - f_profile[0], "G": len(g_slots) - g_profile[0], "total": 405},
        "profiles": {"F_0_through_16": f_profile, "G_0_through_24": g_profile},
        "tail": {"F_17": 0, "G_17_through_24": g_profile[17:]},
        "stored_weight_field": "verified upper grading on all 442 slots but not consumed",
        "upper_equals_lower_coincidences": coincident_weights,
    }


def new_row_polys() -> dict[int, dict[int, SparsePoly]]:
    return {row: {} for row in range(41)}


def add_generator_term(rows: dict[int, dict[int, SparsePoly]], row: int, degree: int,
                       coefficient: int, variables: tuple[str, ...]) -> None:
    if degree < 0:
        if coefficient:
            fail(("negative xi degree with nonzero contribution", row, degree, variables))
        return
    poly = rows[row].setdefault(degree, {})
    add_term(poly, coefficient, normalize_monomial((variable, 1) for variable in variables))
    if not poly:
        del rows[row][degree]


def recurrence_engine(f_slots: list[Slot], g_slots: list[Slot]) -> tuple[
        dict[int, dict[int, SparsePoly]], dict[int, list[dict[str, Any]]]]:
    """Tau-row recurrence engine; does not call the direct-coordinate engine."""
    f_rows = {row: [slot for slot in f_slots if slot.weight == row] for row in range(17)}
    g_rows = {row: [slot for slot in g_slots if slot.weight == row] for row in range(25)}
    combined = new_row_polys()
    contributions: dict[int, list[dict[str, Any]]] = {row: [] for row in range(41)}
    for r in range(17):
        for s in range(25):
            row = r + s
            for f_slot in f_rows[r]:
                for g_slot in g_rows[s]:
                    degree = f_slot.i + g_slot.i - 1
                    left_coefficient = (12 - s) * f_slot.i
                    if left_coefficient:
                        add_generator_term(combined, row, degree, left_coefficient,
                                           (f_slot.name, g_slot.name))
                        contributions[row].append({
                            "source_F": f_slot.record(),
                            "source_G": g_slot.record(),
                            "derivative_side": "F_prime_times_G",
                            "scalar": left_coefficient,
                            "output_xi_degree": degree,
                        })
                    right_coefficient = (r - 8) * g_slot.i
                    if right_coefficient:
                        add_generator_term(combined, row, degree, right_coefficient,
                                           (f_slot.name, g_slot.name))
                        contributions[row].append({
                            "source_F": f_slot.record(),
                            "source_G": g_slot.record(),
                            "derivative_side": "F_times_G_prime",
                            "scalar": right_coefficient,
                            "output_xi_degree": degree,
                        })
    return combined, contributions


def direct_engine(f_slots: list[Slot], g_slots: list[Slot]) -> tuple[
        dict[int, dict[int, SparsePoly]], dict[int, list[dict[str, Any]]]]:
    """Literal original-coordinate Jacobian engine; no recurrence calls."""
    combined = new_row_polys()
    contributions: dict[int, list[dict[str, Any]]] = {row: [] for row in range(41)}
    for f_slot in f_slots:
        for g_slot in g_slots:
            jacobian_scalar = f_slot.i * g_slot.j - f_slot.j * g_slot.i
            mapped_scalar = -jacobian_scalar
            recurrence_pair_scalar = ((12 - g_slot.weight) * f_slot.i
                                      + (f_slot.weight - 8) * g_slot.i)
            if recurrence_pair_scalar != mapped_scalar:
                fail(("pairwise direct/recurrence scalar identity", f_slot.name,
                      g_slot.name, mapped_scalar, recurrence_pair_scalar))
            p = f_slot.i + g_slot.i - 1
            q = f_slot.j + g_slot.j - 1
            row = 17 - 4 * p + q
            if row != f_slot.weight + g_slot.weight:
                fail(("direct row identity", f_slot.name, g_slot.name, row))
            if not 0 <= row <= 40:
                fail(("direct row outside LF40", row))
            if mapped_scalar:
                add_generator_term(combined, row, p, mapped_scalar,
                                   (f_slot.name, g_slot.name))
                contributions[row].append({
                    "source_F": f_slot.record(),
                    "source_G": g_slot.record(),
                    "jacobian_scalar_i_l_minus_j_k": jacobian_scalar,
                    "mapped_scalar": mapped_scalar,
                    "jacobian_raw_exponents": {"x": p, "y": q},
                    "output_tau_degree": row,
                    "output_xi_degree": p,
                })
    return combined, contributions


def with_target(poly: SparsePoly, row: int, degree: int) -> SparsePoly:
    out = dict(poly)
    if row == 17 and degree == 0:
        add_term(out, 1, ())
    return out


def face_substitutions(f_slots: list[Slot], g_slots: list[Slot]) -> dict[str, tuple[int, tuple[tuple[str, int], ...]]]:
    substitutions: dict[str, tuple[int, tuple[tuple[str, int], ...]]] = {}
    for slot in f_slots:
        if slot.weight == 0:
            coefficient = comb(14, slot.i - 2) * ((-1) ** (16 - slot.i))
            substitutions[slot.name] = (coefficient, normalize_monomial((("a", 1), ("rho", 16 - slot.i))))
    for slot in g_slots:
        if slot.weight == 0:
            coefficient = comb(21, slot.i - 3) * ((-1) ** (24 - slot.i))
            substitutions[slot.name] = (coefficient, normalize_monomial((("b", 1), ("rho", 24 - slot.i))))
    if len(substitutions) != 37:
        fail(("FACEPIN substitution count", len(substitutions)))
    return substitutions


def substitute(poly: SparsePoly,
               substitutions: dict[str, tuple[int, tuple[tuple[str, int], ...]]]) -> SparsePoly:
    out: SparsePoly = {}
    for monomial, coefficient in poly.items():
        new_coefficient = coefficient
        new_monomial: tuple[tuple[str, int], ...] = ()
        for variable, exponent in monomial:
            if exponent != 1:
                fail(("unexpected raw determinant exponent", variable, exponent))
            if variable in substitutions:
                factor_coefficient, factor_monomial = substitutions[variable]
                new_coefficient *= factor_coefficient
                new_monomial = multiply_monomials(new_monomial, factor_monomial)
            else:
                new_monomial = multiply_monomials(new_monomial, ((variable, 1),))
        add_term(out, new_coefficient, new_monomial)
    return out


def validate_raw_census(rows: dict[int, dict[int, SparsePoly]]) -> dict[str, Any]:
    counts = [len(rows[row]) for row in range(41)]
    if counts != EXPECTED_RAW_COUNTS or sum(counts) != 774:
        fail(("raw generator census", counts, sum(counts)))
    windows = []
    for row in range(41):
        degrees = sorted(rows[row])
        lo = degrees[0] if degrees else None
        hi = degrees[-1] if degrees else None
        if lo != EXPECTED_MIN_DEGREE[row] or hi != EXPECTED_MAX_DEGREE[row]:
            fail(("raw xi window", row, lo, hi))
        if hi is not None and hi > 39 - row:
            fail(("degree ceiling", row, hi, 39 - row))
        windows.append({"row": row, "min_xi_degree": lo, "max_xi_degree": hi,
                        "generators": len(degrees)})
    if rows[40] or len(rows[39]) != 1:
        fail("row 39/40 structural control")
    return {"counts": counts, "total": sum(counts), "windows": windows,
            "structural_zero_positions_excluded": [[0, 4], [0, 39], [4, 3],
                                                     [8, 2], [12, 1], [16, 0]]}


def row_payload(row: int, combined: dict[int, SparsePoly],
                contributions: list[dict[str, Any]], engine: str) -> dict[str, Any]:
    coefficients = []
    for degree, determinant in sorted(combined.items()):
        coefficients.append({
            "xi_degree": degree,
            "Dtil_coefficient": serialize_poly(determinant),
            "target_generator": serialize_poly(with_target(determinant, row, degree)),
        })
    return {
        "schema": "GGV-8_28-LF40-raw-row-v1",
        "engine": engine,
        "row": row,
        "pre_combination_contributions": contributions,
        "combined_coefficients": coefficients,
        "generator_count": len(coefficients),
        "target": -1 if row == 17 else 0,
    }


def face_row_payload(row: int, combined: dict[int, SparsePoly]) -> dict[str, Any]:
    coefficients = []
    for degree, determinant in sorted(combined.items()):
        generator = with_target(determinant, row, degree)
        if not generator:
            fail(("zero target generator survived filtering", row, degree))
        coefficients.append({
            "xi_degree": degree,
            "Dtil_coefficient_after_FACEPIN": serialize_poly(determinant),
            "target_generator": serialize_poly(generator),
            "singular": singular_poly(generator),
        })
    return {
        "schema": "GGV-8_28-LF40-facepin-row-v1",
        "base_ring": "QQ[a,b,rho,405 positive-weight raw slots]",
        "row": row,
        "combined_coefficients": coefficients,
        "generator_count": len(coefficients),
        "target": -1 if row == 17 else 0,
    }


def write_jsonl_gzip(path: Path, payloads: list[dict[str, Any]]) -> tuple[list[str], str]:
    row_digests: list[str] = []
    cumulative = sha256(b"GGV-8_28-LF40-cumulative-v1\n")
    with path.open("wb") as raw_stream:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw_stream, compresslevel=9, mtime=0) as stream:
            for payload in payloads:
                body = canonical_bytes(payload)
                row_digest = sha256(body).hexdigest()
                cumulative.update(bytes.fromhex(row_digest))
                decorated = dict(payload)
                decorated["row_sha256"] = row_digest
                decorated["cumulative_sha256"] = cumulative.hexdigest()
                stream.write(canonical_bytes(decorated))
                row_digests.append(row_digest)
    return row_digests, cumulative.hexdigest()


def compiler_mutations(f_slots: list[Slot], g_slots: list[Slot], root: Path) -> dict[str, Any]:
    mutated_weight_f = {slot.name: 8 - 3 * slot.i + slot.j for slot in f_slots}
    mutated_weight_g = {slot.name: 12 - 3 * slot.i + slot.j for slot in g_slots}
    swapped_f_weights = [8 - 4 * slot.i + slot.j for slot in g_slots]
    swapped_g_weights = [12 - 4 * slot.i + slot.j for slot in f_slots]
    gate_mutations = json.loads((root / "cases/ggv_8_28_lower_facepin_lf40_v1_20260827/desk_gate/mutations.json").read_text())
    outcomes = {
        "lower_weight_minus3": {
            "status": "EXPECTED_REJECTION",
            "changed_slots": sum(mutated_weight_f[s.name] != s.weight for s in f_slots)
                             + sum(mutated_weight_g[s.name] != s.weight for s in g_slots),
            "reason": "all-slot set equality with the reviewed -4 grading fails",
        },
        "target_sign_row17_plus1": {
            "status": "EXPECTED_REJECTION",
            "correct_anchor_Dtil17_plus_delta": 0,
            "mutated_anchor_Dtil17_minus_delta": -2,
        },
        "truncate_after_17": {"status": "EXPECTED_REJECTION", "missing_rows": list(range(18, 41))},
        "truncate_after_24": {"status": "EXPECTED_REJECTION", "missing_rows": list(range(25, 41))},
        "delete_g_0_12": {"status": "EXPECTED_REJECTION", "mutated_G_count": len(g_slots) - 1},
        "gamma6_degree_drop_smoke": gate_mutations["gamma6_degree_drop_smoke"],
        "degree_preserving_two_root": gate_mutations["degree_preserving_two_root"],
        "rho_zero": gate_mutations["rho_zero"],
        "omit_rho_saturation": {
            "status": "EXPECTED_REJECTION",
            "required": list(EXACT_SATURATION_FACTORS),
            "mutated": [factor for factor in EXACT_SATURATION_FACTORS if factor != "rho"],
        },
        "import_upper_H": {
            "status": "EXPECTED_REJECTION",
            "reason": "solver generator registry accepts exactly 740 target generators plus the one licensed Rabinowitsch equation",
        },
        "swap_polygons_without_sign": {
            "status": "EXPECTED_REJECTION",
            "minimum_mutated_F_weight": min(swapped_f_weights),
            "minimum_mutated_G_weight": min(swapped_g_weights),
            "reason": "per-side nu>=0/type check fails before the independently wrong sign can be consumed",
        },
    }
    if outcomes["lower_weight_minus3"]["changed_slots"] == 0:
        fail("-3 weight mutation was not detected")
    if outcomes["delete_g_0_12"]["mutated_G_count"] != 300:
        fail("deleted-slot mutation did not change census")
    if min(swapped_f_weights) >= 0:
        fail("polygon swap mutation was not detected")
    if gate_mutations["degree_preserving_two_root"]["family_single_root_gate"] != "EXPECTED_REJECTION":
        fail("two-root mutation custody missing")
    return {"schema": "GGV-8_28-LF40-compiler-mutations-v1", "outcomes": outcomes}


def singular_program(face_rows: dict[int, dict[int, SparsePoly]], variables: list[str]) -> str:
    lines = [
        "// GGV-8_28-LF40-v1 substituted compute form, exact QQ, sequential rows 0..40.",
        "// Lifecycle: producer-unreviewed; no modular verdict and no promotion.",
        f"ring R=0,({','.join(variables)}),dp;",
        "option(redSB);",
        'print("LF40_FIELD=QQ_EXACT");',
        'print("LF40_VARIABLES=409");',
        'print("LF40_TARGET_GENERATORS=740");',
        'print("LF40_RABINOWITSCH_EQUATIONS=1");',
        "ideal CONTROL_PROPER=w*a-1;",
        "ideal CONTROL_PROPER_G=std(CONTROL_PROPER);",
        "poly CONTROL_REM=reduce(1,CONTROL_PROPER_G);",
        'if (CONTROL_REM==0) { print("LF40_FATAL_CONTROL_PROPER_BECAME_UNIT"); exit; }',
        "ideal CONTROL_UNIT=w*a-1,a;",
        "ideal CONTROL_UNIT_G=std(CONTROL_UNIT);",
        "CONTROL_REM=reduce(1,CONTROL_UNIT_G);",
        'if (CONTROL_REM!=0) { print("LF40_FATAL_CONTROL_UNIT_NOT_UNIT"); exit; }',
        'print("LF40_SYNTHETIC_CONTROLS=PASS");',
        "ideal J=w*a*b*rho*f_0_8*g_0_12-1;",
        "ideal G=slimgb(J);",
        "poly REMONE=reduce(1,G);",
    ]
    cumulative = 0
    for row in range(41):
        generators = [
            singular_poly(with_target(face_rows[row][degree], row, degree))
            for degree in sorted(face_rows[row])
        ]
        if row > 0:
            lines.append(f"ideal ROW_{row}=" + (",\n".join(generators) if generators else "0") + ";")
            lines.append(f"J=G+ROW_{row};")
            lines.append("G=slimgb(J);")
            lines.append("REMONE=reduce(1,G);")
        cumulative += len(generators)
        lines.extend([
            f'print("LF40_STAGE_ROW_{row}_BEGIN");',
            f'print("LF40_CUMULATIVE_TARGET_GENERATORS={cumulative}");',
            "print(size(G));",
            f'print("LF40_STAGE_ROW_{row}_END");',
            (f'if (REMONE==0) {{ print("LF40_FIRST_EXACT_INCONSISTENCY_ROW={row}"); '
             f'print("LF40_LISTED_EQUATIONS_AT_STOP={cumulative + 1}"); print(G); exit; }}'),
        ])
    if cumulative != 740:
        fail(("Singular cumulative generator count", cumulative))
    lines.extend([
        'print("LF40_FULL_PROPER_IDEAL_FIXTURE_ROWS_0_THROUGH_40");',
        'print("LF40_LISTED_EQUATIONS_AT_STOP=741");',
        "print(G);",
        "exit;",
    ])
    program = "\n".join(lines) + "\n"
    row17_target = singular_poly(with_target(face_rows[17][0], 17, 0))
    row17_homogeneous = singular_poly(face_rows[17][0])
    if (row17_target == row17_homogeneous or
            f"ideal ROW_17={row17_target}," not in program):
        fail("Singular program dropped the inhomogeneous Dtil_17=-1 target")
    # Ordinary expanded determinant coefficients may naturally contain the
    # substrings ``rho-1`` or ``a-1`` across term boundaries.  Reject only
    # actual foreign-face/ring imports here; the exact 741-generator registry
    # above separately prevents normalization equations from being appended.
    forbidden = ("X^8-1", "ideal H=", "ring R=655")
    if any(token in program for token in forbidden):
        fail(("forbidden solver import/normalization", [token for token in forbidden if token in program]))
    return program


def main() -> int:
    if len(sys.argv) != 3:
        fail("usage: compile_lf40.py SOURCE_ROOT OUTPUT_DIR")
    root = Path(sys.argv[1]).resolve()
    output = Path(sys.argv[2]).resolve()
    if output.exists():
        fail(("output must be fresh", str(output)))
    output.mkdir(parents=True)
    source_hashes = verify_source_pins(root)
    gate_result_path = root / "cases/ggv_8_28_lower_facepin_lf40_v1_20260827/desk_gate/RESULT.json"
    gate_result = json.loads(gate_result_path.read_text())
    if gate_result.get("status") != "PASS_FACEPIN_CUSTODY_GATE_REVIEWED_REPAIR":
        fail("reviewed FACEPIN desk gate is not frozen PASS")

    f_slots, g_slots, raw_blob = load_slots(root)
    census = validate_slots(f_slots, g_slots, raw_blob)
    recurrence_rows, recurrence_contributions = recurrence_engine(f_slots, g_slots)
    direct_rows, direct_contributions = direct_engine(f_slots, g_slots)
    if recurrence_rows != direct_rows:
        differing = [row for row in range(41) if recurrence_rows[row] != direct_rows[row]]
        fail(("recurrence/direct engine mismatch", differing))
    raw_census = validate_raw_census(recurrence_rows)

    substitutions = face_substitutions(f_slots, g_slots)
    face_rows = new_row_polys()
    for row in range(41):
        for degree, poly in recurrence_rows[row].items():
            substituted = substitute(poly, substitutions)
            if substituted:
                face_rows[row][degree] = substituted
    if face_rows[0]:
        fail(("Dtil_0 not identically zero after FACEPIN", face_rows[0]))
    face_counts = [len(face_rows[row]) for row in range(41)]
    if face_counts != [0] + EXPECTED_RAW_COUNTS[1:] or sum(face_counts) != 740:
        fail(("post-FACEPIN census", face_counts, sum(face_counts)))
    if face_rows[40] or len(face_rows[39]) != 1:
        fail("post-FACEPIN row 39/40 structural control")
    # The direct engine is independently substituted too, not assumed from raw equality.
    direct_face_rows = new_row_polys()
    for row in range(41):
        for degree, poly in direct_rows[row].items():
            substituted = substitute(poly, substitutions)
            if substituted:
                direct_face_rows[row][degree] = substituted
    if direct_face_rows != face_rows:
        fail("post-FACEPIN direct/recurrence engine mismatch")

    recurrence_payloads = [row_payload(row, recurrence_rows[row], recurrence_contributions[row],
                                       "tau_recurrence") for row in range(41)]
    direct_payloads = [row_payload(row, direct_rows[row], direct_contributions[row],
                                   "literal_original_coordinate_Jacobian_map") for row in range(41)]
    face_payloads = [face_row_payload(row, face_rows[row]) for row in range(41)]
    recurrence_digests, recurrence_cumulative = write_jsonl_gzip(
        output / "raw_recurrence_rows.jsonl.gz", recurrence_payloads)
    direct_digests, direct_cumulative = write_jsonl_gzip(
        output / "raw_direct_rows.jsonl.gz", direct_payloads)
    face_digests, face_cumulative = write_jsonl_gzip(
        output / "facepin_rows.jsonl.gz", face_payloads)
    if recurrence_digests != direct_digests:
        # The full payloads intentionally differ by engine/contribution serialization; compare combined digests below.
        combined_recurrence = [sha256(canonical_bytes({
            degree: serialize_poly(poly) for degree, poly in sorted(recurrence_rows[row].items())
        })).hexdigest() for row in range(41)]
        combined_direct = [sha256(canonical_bytes({
            degree: serialize_poly(poly) for degree, poly in sorted(direct_rows[row].items())
        })).hexdigest() for row in range(41)]
        if combined_recurrence != combined_direct:
            fail("combined row digest mismatch between engines")
    else:
        fail("engine payload digests unexpectedly identical; independence labels disappeared")

    positive_slots = sorted((slot for slot in (*f_slots, *g_slots) if slot.weight > 0),
                            key=lambda slot: (slot.weight, slot.side, slot.i, slot.j, slot.name))
    if len(positive_slots) != 405 or len({slot.name for slot in positive_slots}) != 405:
        fail("positive slot variable census")
    compute_variables = ["a", "b", "rho"] + [slot.name for slot in positive_slots]
    solver_variables = ["w"] + compute_variables
    if len(compute_variables) != 408 or len(solver_variables) != 409:
        fail(("variable census", len(compute_variables), len(solver_variables)))

    program = singular_program(face_rows, solver_variables)
    (output / "lf40_sequential_QQ.sing").write_text(program, encoding="utf-8")
    (output / "ring_variables.txt").write_text("\n".join(solver_variables) + "\n", encoding="utf-8")
    substitution_records = []
    for variable, (coefficient, monomial) in sorted(substitutions.items()):
        substitution_records.append({
            "raw_slot": variable,
            "coefficient": coefficient,
            "monomial": [{"variable": name, "exponent": exponent} for name, exponent in monomial],
        })
    write_json(output / "facepin_substitution.json", {
        "schema": "GGV-8_28-LF40-FACEPIN-substitution-v1",
        "relations": substitution_records,
        "count": len(substitution_records),
        "source_facepin_derivation_sha256": digest_file(root / "cases/ggv_8_28_lower_facepin_lf40_v1_20260827/desk_gate/facepin_derivation.json"),
    })
    mutations = compiler_mutations(f_slots, g_slots, root)
    write_json(output / "mutation_results.json", mutations)
    write_json(output / "slot_census.json", census)
    result = {
        "status": "PASS-LF40-COMPILER-CUSTODY",
        "schema": "GGV-8_28-LF40-v1-reviewed-repair",
        "field": "QQ exact",
        "source_hashes": source_hashes,
        "source_FACEPIN_gate_sha256": digest_file(gate_result_path),
        "raw_slot_count": 442,
        "raw_coefficient_generators": 774,
        "raw_row_0_generators": 34,
        "facepin_relations_substituted": 37,
        "facepin_killed_positions": 34,
        "compute_variables": 408,
        "target_generators": 740,
        "row_39_generators": 1,
        "row_40_generators": 0,
        "saturation_policy": "exactly a*b*rho*f_0_8*g_0_12",
        "rabinowitsch": {"variables": 409, "equations": 741,
                           "equation": "w*a*b*rho*f_0_8*g_0_12-1"},
        "target": {"Dtil_17": -1, "all_other_rows_0_through_40": 0},
        "row_counts_raw": EXPECTED_RAW_COUNTS,
        "row_counts_facepin": face_counts,
        "recurrence_row_sha256": recurrence_digests,
        "direct_row_sha256": direct_digests,
        "facepin_row_sha256": face_digests,
        "recurrence_cumulative_sha256": recurrence_cumulative,
        "direct_cumulative_sha256": direct_cumulative,
        "facepin_cumulative_sha256": face_cumulative,
        "raw_census": raw_census,
        "dual_engine_scope": "same-source consistency check, not independent-model review",
        "lifecycle": "PRODUCER_UNREVIEWED_NOT_PROMOTED_EVIDENCE",
        "scope": "actual-GGV 8_28 raw pre-final lower necessary system only; conditional on reviewed GGV reduction",
    }
    write_json(output / "compiler_result.json", result)
    freeze_directory(output, "COMPILER_EVIDENCE.sha256")
    print(result["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
