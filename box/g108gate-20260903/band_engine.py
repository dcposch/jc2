#!/usr/bin/env python3
"""Exact joint-chart band compiler for the D=108, delta=3 client.

This is a source-compatible adaptation of the charged (99,66) engine, not a
constant-only rewrite.  It compiles the major h3/h2 order structure, the full
outer D2/D1 preblock, the delta=3 common-h3 incidence, direct-pole support,
and the Jacobian schedule.  Q-star reduction uses only nonzero rational
coefficients.  The branch dies in the common-h3 incidence preflight, so the
scheduled direct F/G pole and Jacobian rows are compiled but never imposed.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from math import ceil, comb, factorial
from pathlib import Path
import platform
import resource
import subprocess
import sys
import time
from typing import Iterable

import sympy as sp

from outer_order_bands import build_audit as build_outer_audit, rational_rank


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
RECEIPT = ROOT / "xmodel/g108-delta3-kill-gate-gpt55-20260903.run.v2"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_receipt() -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    return fields


def verify_inputs(output_dir: Path) -> dict:
    """Generate the manifest mechanically from the receipt and run sha256sum -c."""
    fields = parse_receipt()
    count = int(fields["charged_inputs"])
    frozen = Path(fields["lane_inputs_dir"])
    assert count == 17
    manifest_lines = []
    checked = []
    for index in range(1, count + 1):
        basename = fields[f"charged_input_{index}_basename"]
        expected = fields[f"charged_input_{index}_sha256"]
        assert Path(basename).name == basename
        path = frozen / basename
        manifest_lines.append(f"{expected}  {path}\n")
        actual = sha256(path)
        assert actual == expected, f"charged input mismatch: {basename}"
        checked.append({"basename": basename, "sha256": actual})
    manifest = output_dir / "inputs.sha256"
    manifest.write_text("".join(manifest_lines), encoding="utf-8")
    replay = subprocess.run(
        ["sha256sum", "-c", str(manifest)],
        text=True,
        capture_output=True,
        check=True,
    )
    (output_dir / "inputs.sha256.check.log").write_text(replay.stdout, encoding="utf-8")
    return {
        "receipt": str(RECEIPT),
        "receipt_sha256": sha256(RECEIPT),
        "lane_inputs_dir": str(frozen),
        "charged_inputs": count,
        "manifest": str(manifest),
        "manifest_sha256": sha256(manifest),
        "sha256sum_check_lines": len(replay.stdout.splitlines()),
        "all_hashes_match": True,
        "checked": checked,
    }


def lower_positions(degree: int, y_cap: int) -> set[tuple[int, int]]:
    """Fixed-top positions in t^degree Q(t^-1,w/t), excluding r=0."""
    return {
        (r, q)
        for r in range(1, degree + 1)
        for q in range(min(y_cap, degree - r) + 1)
    }


def determinant(rows: list[list[int]]) -> Fraction:
    work = [[Fraction(value) for value in row] for row in rows]
    result = Fraction(1)
    for col in range(len(work)):
        pivot = next((row for row in range(col, len(work)) if work[row][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            result *= -1
        value = work[col][col]
        result *= value
        for row in range(col + 1, len(work)):
            scalar = work[row][col] / value
            for column in range(col, len(work)):
                work[row][column] -= scalar * work[col][column]
    return result


def major_structure() -> dict:
    """Exact sparse support certificate for h3 inside h2."""
    h_fixed = {(0, 7), (0, 8), (0, 9)}
    h_all_lower = lower_positions(9, 8)
    h_below = {p for p in h_all_lower if 4 * p[0] + 6 * p[1] < 42}
    h_equal = {p for p in h_all_lower if 4 * p[0] + 6 * p[1] == 42}
    h_tail = {p for p in h_all_lower if 4 * p[0] + 6 * p[1] > 42}
    assert (len(h_all_lower), len(h_below), len(h_equal), len(h_tail)) == (45, 36, 2, 7)
    assert h_equal == {(3, 5), (6, 3)}
    assert h_tail == {(1, 7), (1, 8), (2, 6), (2, 7), (3, 6), (4, 5), (5, 4)}
    h_support = h_fixed | h_tail

    c2 = lower_positions(18, 8)
    c3 = lower_positions(27, 8)
    c4 = lower_positions(36, 8)
    assert (len(c2), len(c3), len(c4)) == (126, 207, 288)

    h_squared = {
        (r1 + r2, q1 + q2)
        for r1, q1 in h_support
        for r2, q2 in h_support
    }
    h_fourth = {
        (r1 + r2, q1 + q2)
        for r1, q1 in h_squared
        for r2, q2 in h_squared
    }
    c2_h2 = {
        (r1 + r2, q1 + q2)
        for r1, q1 in c2
        for r2, q2 in h_squared
    }
    c3_h = {
        (r1 + r2, q1 + q2)
        for r1, q1 in c3
        for r2, q2 in h_support
    }
    slots = {
        (r, q)
        for r in range(1, 37)
        for q in range(37 - r)
        if 4 * r + 6 * q <= 168
    }
    strict_slots = {p for p in slots if 4 * p[0] + 6 * p[1] < 168}
    equality_slots = {p for p in slots if 4 * p[0] + 6 * p[1] == 168}
    face_targets = {(3 * k, 28 - 2 * k) for k in range(1, 9)}
    assert (len(strict_slots), len(equality_slots), len(slots)) == (558, 8, 566)
    assert equality_slots == face_targets
    identities = slots - c4 - c3_h - c2_h2 - h_fourth - face_targets
    assert identities == {(1, 27)}

    # Unit-triangular leaders.  Ordering r upward and q downward makes the
    # top q=9 term of h3 and q=18 term of h3^2 the first incidences.
    pivots: dict[tuple[str, int, int], tuple[int, int]] = {}
    for row in sorted(slots - identities, key=lambda item: (item[0], -item[1])):
        r, q = row
        if q <= 8:
            pivot = ("C4", r, q)
            assert (r, q) in c4
            column_rows = {(r, q)}
        elif q <= 17:
            pivot = ("C3", r, q - 9)
            assert (r, q - 9) in c3
            column_rows = {
                (r + hr, q - 9 + hq)
                for hr, hq in h_support
                if (r + hr, q - 9 + hq) in slots
            }
        else:
            pivot = ("C2", r, q - 18)
            assert (r, q - 18) in c2
            column_rows = {
                (r + hr, q - 18 + hq)
                for hr, hq in h_squared
                if (r + hr, q - 18 + hq) in slots
            }
        assert pivot not in pivots
        assert min(column_rows, key=lambda item: (item[0], -item[1])) == row
        pivots[pivot] = row
    pivot_counts = {
        name: sum(pivot[0] == name for pivot in pivots)
        for name in ("C4", "C3", "C2")
    }
    assert pivot_counts == {"C4": 288, "C3": 198, "C2": 79}

    d1_q = [25, 23, 21, 19]
    d1_matrix = [[comb(q, k) for q in d1_q] for k in range(4)]
    d1_det = determinant(d1_matrix)
    assert d1_det == 64 and rational_rank(d1_matrix) == 4

    ambient = len(h_tail) + len(c2) + len(c3) + len(c4)
    d2_rank = len(pivots)
    d1_rank = 4
    assert (ambient, d2_rank, ambient - d2_rank - d1_rank) == (628, 565, 59)
    return {
        "conventions": {
            "K3": "t^9*h3(t^-1,w/t)",
            "K2": "t^36*h2(t^-1,w/t)",
            "major_coordinate": "z=w-1",
            "D2": "t=s^4, z=pi*s^6; weight 4*r+6*q",
            "D1": "s=e^2, t=e^8, z=e^12*(1+Pi*e)",
            "top_K3": "z^7*(1+z)^2",
            "top_K2": "z^28*(1+z)^8",
            "D2_K2_face": "pi^12*(pi^2-1)^8",
        },
        "h3_D2": {
            "fixed_top_lower_ambient": len(h_all_lower),
            "strict_order_rows": len(h_below),
            "strict_order_rank": len(h_below),
            "face_incidence_rows": len(h_equal),
            "face_incidence_rank": len(h_equal),
            "equality_sites": [list(p) for p in sorted(h_equal)],
            "surviving_coordinates": [list(p) for p in sorted(h_tail)],
            "surviving_count": len(h_tail),
        },
        "post_h3_ambient_516_analogue": {
            "H": len(h_tail),
            "C2": len(c2),
            "C3": len(c3),
            "C4": len(c4),
            "total": ambient,
        },
        "h2_D2": {
            "strict_Theorem_1_2_rows": len(strict_slots),
            "face_incidence_rows": len(equality_slots),
            "face_sites": [list(p) for p in sorted(equality_slots)],
            "face_values": [str((-1) ** k * comb(8, k)) for k in range(1, 9)],
            "nominal_rows": len(slots),
            "identity_sites": [list(p) for p in sorted(identities)],
            "rank": d2_rank,
            "unit_pivots": pivot_counts,
            "dimension_after_D2": ambient - d2_rank,
            "residual_rows": 0,
        },
        "h2_D1": {
            "face_leading_exponent": 344,
            "row_exponents": [340, 341, 342, 343],
            "primitive_weight": 85,
            "full_weight": 170,
            "raw_rows": 4,
            "chosen_q_values": d1_q,
            "chosen_minor_determinant": str(d1_det),
            "rank": d1_rank,
            "residual_rows": 0,
        },
        "joint_major": {
            "fixed_inner_ambient": 666,
            "h3_D2_rank": 38,
            "post_h3_ambient": ambient,
            "h2_D2_rank": d2_rank,
            "h2_D1_rank": d1_rank,
            "total_rank_from_fixed_inner": 38 + d2_rank + d1_rank,
            "free_dimension": ambient - d2_rank - d1_rank,
            "free_h3_projection_dimension": len(h_tail),
        },
        "controls": {
            "strict_below_separate_from_at_level": True,
            "all_D2_slots_enumerated": True,
            "one_identity_has_no_source_or_target_support": True,
            "every_nonidentity_D2_row_has_a_unit_triangular_leader": True,
            "D1_minor_nonzero_over_Q": True,
        },
    }


TZ = dict[tuple[int, int], sp.Expr]


def h3_template(cutoff: int = 43) -> tuple[TZ, list[sp.Symbol]]:
    """h3 chart in z=w-1; cutoff 43 fixes, cutoff 42 retains, the face."""
    result: TZ = {(0, 7): sp.Integer(1), (0, 8): sp.Integer(2), (0, 9): sp.Integer(1)}
    variables: list[sp.Symbol] = []
    for r in range(1, 10):
        vmin = max(0, ceil((cutoff - 4 * r) / 6))
        cap = 9 - r
        for degree in range(vmin, cap + 1):
            variable = sp.Symbol(f"Hc_{r}_{degree}")
            variables.append(variable)
            # z^vmin*w^(degree-vmin), expressed in z with w=1+z.
            for q in range(vmin, degree + 1):
                result[(r, q)] = result.get((r, q), sp.Integer(0)) + variable * comb(
                    degree - vmin, q - vmin
                )
    expected = {
        43: ["Hc_1_7", "Hc_1_8", "Hc_2_6", "Hc_2_7", "Hc_3_6", "Hc_4_5", "Hc_5_4"],
        42: ["Hc_1_7", "Hc_1_8", "Hc_2_6", "Hc_2_7", "Hc_3_5", "Hc_3_6", "Hc_4_5", "Hc_5_4", "Hc_6_3"],
    }
    assert cutoff in expected and [str(variable) for variable in variables] == expected[cutoff]
    return {key: sp.expand(value) for key, value in result.items()}, variables


def z_to_w(item: TZ) -> TZ:
    result: dict[tuple[int, int], sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for (r, q), coefficient in item.items():
        for j in range(q + 1):
            result[(r, j)] += coefficient * comb(q, j) * (-1) ** (q - j)
    return {key: sp.expand(value) for key, value in result.items() if value != 0}


def minor_incidence_rows(cutoff: int = 43) -> tuple[list[tuple[str, sp.Expr]], list[sp.Symbol]]:
    """Substitute w=jet1*t^2+jet2*t^3+pi*t^4 through local power 8."""
    h3, variables = h3_template(cutoff)
    wbasis = z_to_w(h3)
    jet1, jet2, c = sp.symbols("jet1 jet2 c")
    collected: dict[tuple[int, int], sp.Expr] = defaultdict(lambda: sp.Integer(0))
    for (r, j), coefficient in wbasis.items():
        for a in range(j + 1):
            for b in range(j - a + 1):
                k = j - a - b
                local_power = r + 2 * a + 3 * b + 4 * k
                if local_power > 8:
                    continue
                multinomial = factorial(j) // (factorial(a) * factorial(b) * factorial(k))
                collected[(local_power, k)] += (
                    coefficient * multinomial * jet1**a * jet2**b
                )
    # Fixed top is -w^2+O(w^3), so the scalar-compatible target is
    # -t^8*(pi^2-c)=t^8*(c-pi^2).
    collected[(8, 0)] -= c
    collected[(8, 2)] += 1
    rows = [
        (f"minor_n{power}_pi{k}", sp.expand(value))
        for (power, k), value in sorted(collected.items())
    ]
    # Thirteen coefficient labels occur after sparse cancellation; the pi^2
    # target row is the sole identically-zero label with the correct scalar.
    assert len(rows) == 13
    assert sum(value != 0 for _label, value in rows) == 12
    return rows, variables


@dataclass
class Pivot:
    label: str
    variable: sp.Symbol
    coefficient: sp.Rational
    rhs: sp.Expr


def qstar_reduce(
    rows: list[tuple[str, sp.Expr]], eligible: Iterable[sp.Symbol]
) -> tuple[list[tuple[str, sp.Expr]], dict[sp.Symbol, sp.Expr], list[Pivot], int]:
    work = [(label, sp.expand(row)) for label, row in rows if row != 0]
    zero_rows = len(rows) - len(work)
    available = set(eligible)
    substitutions: dict[sp.Symbol, sp.Expr] = {}
    pivots: list[Pivot] = []
    while True:
        selected = None
        for index, (label, row) in enumerate(work):
            for variable in sorted(row.free_symbols.intersection(available), key=str):
                coefficient = sp.diff(row, variable)
                remainder = sp.expand(row - coefficient * variable)
                if coefficient.is_Rational and coefficient != 0 and variable not in remainder.free_symbols:
                    selected = index, label, variable, sp.Rational(coefficient), remainder
                    break
            if selected is not None:
                break
        if selected is None:
            break
        index, label, variable, coefficient, remainder = selected
        rhs = sp.cancel(-remainder / coefficient)
        for old in list(substitutions):
            substitutions[old] = sp.expand(substitutions[old].subs(variable, rhs))
        substitutions[variable] = rhs
        pivots.append(Pivot(label, variable, coefficient, rhs))
        available.remove(variable)
        del work[index]
        reduced = []
        for old_label, old_row in work:
            image = sp.expand(old_row.subs(variable, rhs))
            if image == 0:
                zero_rows += 1
            else:
                reduced.append((old_label, image))
        work = reduced
    # Resolve later substitutions in earlier right sides and residuals.
    for _ in range(len(substitutions) + 2):
        changed = False
        for variable, rhs in list(substitutions.items()):
            others = {key: value for key, value in substitutions.items() if key != variable}
            image = sp.expand(rhs.subs(others, simultaneous=True))
            if image != rhs:
                substitutions[variable] = image
                changed = True
        if not changed:
            break
    residual = []
    for label, row in work:
        image = sp.expand(row.subs(substitutions, simultaneous=True))
        if image == 0:
            zero_rows += 1
        else:
            residual.append((label, image))
    return residual, substitutions, pivots, zero_rows


def incidence_audit() -> tuple[dict, list[tuple[str, sp.Expr]]]:
    rows, hvars = minor_incidence_rows()
    residual, substitutions, pivots, zeros = qstar_reduce(rows, hvars)
    assert len(pivots) == 7 and len(residual) == 5 and zeros == 1
    expected_substitutions = {
        "Hc_1_7": "0",
        "Hc_1_8": "0",
        "Hc_2_6": "0",
        "Hc_2_7": "2*jet1",
        "Hc_3_6": "0",
        "Hc_4_5": "jet1**2",
        "Hc_5_4": "0",
    }
    assert {str(key): str(sp.expand(value)) for key, value in substitutions.items()} == expected_substitutions
    expected_residual = {
        "minor_n6_pi0": "-jet2**2",
        "minor_n7_pi0": "2*jet1**2*jet2",
        "minor_n7_pi1": "-2*jet2",
        "minor_n8_pi0": "-c - jet1**4 + 9*jet1*jet2**2",
        "minor_n8_pi1": "2*jet1**2",
    }
    residual_map = {label: sp.expand(value) for label, value in residual}
    assert {label: str(value) for label, value in residual_map.items()} == expected_residual

    jet1, jet2, c, zc = sp.symbols("jet1 jet2 c Zc")
    wrapper = zc * c - 1
    certificate_coefficients = {
        "minor_n6_pi0": sp.Integer(0),
        "minor_n7_pi0": sp.Integer(0),
        "minor_n7_pi1": -sp.Rational(9, 2) * jet1 * jet2 * zc,
        "minor_n8_pi0": -zc,
        "minor_n8_pi1": -sp.Rational(1, 2) * jet1**2 * zc,
        "localization_Zc_c_minus_1": -sp.Integer(1),
    }
    identity = wrapper * certificate_coefficients["localization_Zc_c_minus_1"]
    for label, value in residual:
        identity += certificate_coefficients[label] * value
    assert sp.expand(identity) == 1

    # Negative/robustness control: retain both weight-42 equality directions
    # instead of fixing the major h3 face.  The larger nine-coordinate chart
    # is still empty after exact Q-star reduction and c-localization.
    alternate_rows, alternate_hvars = minor_incidence_rows(cutoff=42)
    alternate_residual, _alternate_subs, alternate_pivots, _alternate_zeros = qstar_reduce(
        alternate_rows, alternate_hvars
    )
    alternate_map = {label: sp.expand(value) for label, value in alternate_residual}
    assert len(alternate_pivots) == 9
    assert alternate_map == {
        "minor_n8_pi0": -c - jet1**4,
        "minor_n8_pi1": 2 * jet1**2,
    }
    alternate_identity = (
        -zc * alternate_map["minor_n8_pi0"]
        - sp.Rational(1, 2) * jet1**2 * zc * alternate_map["minor_n8_pi1"]
        - wrapper
    )
    assert sp.expand(alternate_identity) == 1

    result = {
        "type": "EXACT-QSTAR / COMMON-h3-MINOR-INCIDENCE / delta=3",
        "minor_series": "w=jet1*t^2+jet2*t^3+pi*t^4",
        "target": "K3=-t^8*(pi^2-c)+O(t^9)",
        "target_scalar_reason": "w^2*(w-1)^7=-w^2+O(w^3)",
        "branch_face": {
            "p": "pi^2-c",
            "localization": "c!=0 via Zc*c-1",
            "q": "p^23*U",
            "U_derivative": "5*p^2",
            "degree_U": 5,
            "mod_gauge_parameter": "e0 (bridge-neutral; absent from this necessary h3 block)",
            "rigid_packets": [12, 12],
            "child_final_orders": [4, 4],
        },
        "raw": {
            "coefficient_labels": len(rows),
            "nonzero_rows": sum(value != 0 for _label, value in rows),
            "zero_rows": sum(value == 0 for _label, value in rows),
            "rows": {label: str(value) for label, value in rows},
        },
        "Qstar": {
            "eligible": [str(variable) for variable in hvars],
            "excluded": ["jet1", "jet2", "c", "e0", "Zc"],
            "pivots": [
                {
                    "row": pivot.label,
                    "variable": str(pivot.variable),
                    "coefficient": str(pivot.coefficient),
                    "resolved_value": str(substitutions[pivot.variable]),
                }
                for pivot in pivots
            ],
            "rank": len(pivots),
            "dependent_zero_rows": zeros,
        },
        "residual": {label: str(value) for label, value in residual},
        "residual_count": len(residual),
        "certificate": {
            "wrapper": str(wrapper),
            "coefficients": {key: str(value) for key, value in certificate_coefficients.items()},
            "expanded_identity": str(sp.expand(identity)),
            "localized_unit_ideal": True,
        },
        "sign_control": {
            "literal_plus_p_target_pi2_residue": "-2",
            "status": "REJECTED-SPURIOUS-SCALAR-KILL",
        },
        "equality_retained_control": {
            "h3_coordinates": len(alternate_hvars),
            "Qstar_pivots": len(alternate_pivots),
            "residual": {label: str(value) for label, value in alternate_residual},
            "localized_certificate_expands_to": str(sp.expand(alternate_identity)),
            "status": "DEAD-IN-LARGER-CHART",
        },
    }
    return result, residual


def singular_text(residual: list[tuple[str, sp.Expr]]) -> str:
    names = {label: value for label, value in residual}

    def singular(expr: sp.Expr) -> str:
        return str(sp.expand(expr)).replace("**", "^")

    lines = [
        "// Exact Q replay: D=108 delta=3 common-h3 incidence.",
        "ring R=0,(jet1,jet2,c,Zc),dp;",
    ]
    for label in ("minor_n6_pi0", "minor_n7_pi0", "minor_n7_pi1", "minor_n8_pi0", "minor_n8_pi1"):
        lines.append(f"poly {label}={singular(names[label])};")
    lines.extend(
        [
            "poly L=Zc*c-1;",
            "ideal Raw=minor_n6_pi0,minor_n7_pi0,minor_n7_pi1,minor_n8_pi0,minor_n8_pi1;",
            "ideal I=Raw,L;",
            "ideal S=std(I);",
            'print("MAIN_DIM"); dim(S);',
            'print("MAIN_SIZE"); size(S);',
            'print("MAIN_NF1"); reduce(1,S);',
            "matrix U=lift(I,ideal(1));",
            'print("MAIN_LIFT"); U;',
            "ideal SR=std(Raw);",
            'print("RAW_DIM"); dim(SR);',
            'print("RAW_NF1"); reduce(1,SR);',
            "ideal EmptyControl=c,Zc*c-1;",
            "ideal SE=std(EmptyControl);",
            'print("EMPTY_CONTROL_DIM"); dim(SE);',
            'print("EMPTY_CONTROL_NF1"); reduce(1,SE);',
            "ideal PointControl=c-1,Zc*c-1;",
            "ideal SP=std(PointControl);",
            'print("POINT_CONTROL_DIM"); dim(SP);',
            'print("POINT_CONTROL_NF1"); reduce(1,SP);',
            "quit;",
        ]
    )
    return "\n".join(lines) + "\n"


def run_singular(output_dir: Path, residual: list[tuple[str, sp.Expr]]) -> dict:
    script = output_dir / "death_replay.sing"
    log = output_dir / "death_replay.log"
    script.write_text(singular_text(residual), encoding="utf-8")
    started = time.monotonic()
    replay = subprocess.run(
        ["Singular", "-q", str(script)],
        text=True,
        capture_output=True,
        timeout=600,
        check=True,
    )
    wall = time.monotonic() - started
    log.write_text(replay.stdout + replay.stderr, encoding="utf-8")
    output = replay.stdout
    # Marker/value pairs are deliberately asserted rather than inferred from
    # size alone.  Normal form of 1 is 0 exactly for a unit ideal.
    required = [
        "MAIN_DIM\n-1",
        "MAIN_SIZE\n1",
        "MAIN_NF1\n0",
        "RAW_DIM\n1",
        "RAW_NF1\n1",
        "EMPTY_CONTROL_DIM\n-1",
        "EMPTY_CONTROL_NF1\n0",
        "POINT_CONTROL_DIM\n2",
        "POINT_CONTROL_NF1\n1",
    ]
    missing = [fragment for fragment in required if fragment not in output]
    assert not missing, f"Singular replay marker mismatch: {missing}; output={output!r}"
    return {
        "executable": subprocess.run(
            ["command", "-v", "Singular"], shell=True, text=True, capture_output=True
        ).stdout.strip() or "/usr/bin/Singular",
        "script": str(script),
        "script_sha256": sha256(script),
        "log": str(log),
        "log_sha256": sha256(log),
        "wall_seconds": round(wall, 6),
        "main": {"dimension": -1, "basis_size": 1, "normal_form_of_1": 0},
        "controls": {
            "raw_without_localization": {"dimension": 1, "normal_form_of_1": 1, "note": "Zc is free"},
            "empty_c_and_c_invertible": {"dimension": -1, "normal_form_of_1": 0},
            "point_c_equals_1": {"dimension": 2, "normal_form_of_1": 1, "note": "jet1,jet2 are free"},
            "lift_printed": "MAIN_LIFT" in output,
        },
    }


def raw_minor_support(name: str) -> dict:
    """Enumerate all lower-monomial coefficient tags in the delta=3 chart."""
    if name == "F":
        degree, pole, shift = 108, 12, 96
    elif name == "G":
        degree, pole, shift = 72, 8, 64
    else:
        raise ValueError(name)
    tags: set[tuple[int, int]] = set()
    for i in range(degree):
        for j in range(degree - i):
            for b in range(j + 1):
                for k in range(j - b + 1):
                    exponent = pole - i + j + b + 2 * k
                    if exponent <= 0:
                        tags.add((exponent + shift, k))
    grouped: dict[int, list[int]] = defaultdict(list)
    for local_power, pi_degree in sorted(tags):
        grouped[local_power].append(pi_degree)
    expected = 1200 if name == "F" else 544
    assert len(tags) == expected
    return {
        "object": name,
        "degree": degree,
        "pole": pole,
        "normalizing_shift": shift,
        "formula": f"e={pole}-i+j+b+2*k; local_power=e+{shift}",
        "raw_tag_count": len(tags),
        "local_power_min": min(grouped),
        "local_power_max": max(grouped),
        "rows_by_local_power": {str(power): len(values) for power, values in grouped.items()},
        "target_at_leading_power": "(pi^2-c)^12" if name == "F" else "(pi^2-c)^8",
    }


def continuation_schedule() -> dict:
    f_support = raw_minor_support("F")
    g_support = raw_minor_support("G")
    return {
        "pole_rows": {
            "minor_series": "y=jet1*t+jet2*t^2+pi*t^3",
            "F": f_support,
            "G": g_support,
            "prior_prefix": {
                "local_powers": [1, 2, 3],
                "rows": 6,
                "cleared_exponents_F": [-95, -94, -93],
                "cleared_exponents_G": [-63, -62, -61],
            },
            "stage_rule": "stage s would add local power 4+s: F exponent -92+s, G exponent -60+s",
            "leading_targets": "subtract p^12 at F local 96 and p^8 at G local 64",
        },
        "Jacobian": {
            "formula": "108*KF*(KG)_w-t*(KF)_t*(KG)_w-72*(KF)_w*KG+(KF)_w*t*(KG)_t",
            "top_degree": 178,
            "top_degree_status": "identically zero (proportional top forms)",
            "first_nonzero_degree": 177,
            "normalization_control": "J[t^1,w^15]=1712*f0=(108-1)*16*f0",
            "required_constant": "at degree 0 subtract 1; all positive degrees target 0",
            "prior": "degree 177, w powers 15..24 (10 rows)",
            "stage_0": "degree 177, w power 25",
            "stage_1": "degree 177, w powers 26..177",
            "stage_n_ge_2": "degree 178-n, all w powers 0..178-n",
            "warning": "synchronization is a driver convention, not a theorem",
        },
    }


def software_record() -> dict:
    singular_version = subprocess.run(
        ["Singular", "--version"], text=True, capture_output=True, check=True
    ).stdout.splitlines()[0]
    return {
        "python": sys.version.splitlines()[0],
        "sympy": sp.__version__,
        "Singular": singular_version,
        "platform": platform.platform(),
        "pid_affinity": subprocess.run(
            ["taskset", "-pc", str(Path("/proc/self").resolve().name)],
            text=True,
            capture_output=True,
        ).stdout.strip(),
        "declared_max_cores": 4,
    }


def compile_result(output_dir: Path, run_stage: bool) -> dict:
    started = time.monotonic()
    output_dir.mkdir(parents=True, exist_ok=True)
    custody = verify_inputs(output_dir)
    major = major_structure()
    outer = build_outer_audit()
    incidence, residual = incidence_audit()
    schedule = continuation_schedule()
    singular = run_singular(output_dir, residual) if run_stage else {"status": "not run in skeleton-only mode"}

    fixed_chart = 8514
    branch_parameters = ["jet1", "jet2", "c", "e0"]
    major_rank = major["joint_major"]["total_rank_from_fixed_inner"]
    outer_rank = outer["totals"]["rank_D2_plus_D1"]
    pre_incidence_dimension = fixed_chart + len(branch_parameters) - major_rank - outer_rank
    assert (major_rank, outer_rank, pre_incidence_dimension) == (607, 7710, 201)
    qstar_dimension = pre_incidence_dimension - incidence["Qstar"]["rank"]
    assert qstar_dimension == 194

    stage = {
        "stage": 0,
        "branch": "delta3",
        "reached": run_stage,
        "preflight_families": [
            "major h3 D2 strict-order and face rows",
            "projected h2 D2 and h2 D1 rows",
            "outer D2 support preblock and all four D1 offsets",
            "common-h3 delta=3 minor incidence",
        ],
        "scheduled_but_unreached": [
            "prior six direct F/G pole rows",
            "prior ten Jacobian rows",
            "stage-0 F/G local-power-4 rows",
            "stage-0 Jacobian w^25 row",
        ],
        "fixed_chart_coordinates": fixed_chart,
        "branch_parameters": branch_parameters,
        "ambient_before_wrapper": fixed_chart + len(branch_parameters),
        "major_order_rank": major_rank,
        "outer_rank": outer_rank,
        "outer_D2_rank": outer["totals"]["D2_rank"],
        "outer_D1_rank": outer["totals"]["D1_rank"],
        "dimension_before_minor_incidence": pre_incidence_dimension,
        "joint_Qstar_pivots_new": incidence["Qstar"]["rank"],
        "joint_Qstar_pivots_cumulative": major_rank + outer_rank + incidence["Qstar"]["rank"],
        "dimension_after_Qstar_before_residue": qstar_dimension,
        "nonlinear_residue_rows": incidence["residual_count"],
        "residue": incidence["residual"],
        "exact_localized_dimension": -1 if run_stage else None,
        "status": "DEAD" if run_stage else "COMPILED-SKELETON",
        "killing_family": "common-h3 minor incidence" if run_stage else None,
        "stop_reason": "explicit localized unit certificate" if run_stage else None,
    }
    result = {
        "type": "D108-JOINT-BAND-ENGINE / EXACT-Q",
        "mode": "stage-0" if run_stage else "skeleton-only",
        "driver_provenance": {
            "band_engine": str(Path(__file__).resolve()),
            "band_engine_sha256": sha256(Path(__file__).resolve()),
            "outer_order_bands": str((HERE / "outer_order_bands.py").resolve()),
            "outer_order_bands_sha256": sha256(HERE / "outer_order_bands.py"),
            "charged_engine_sha256": parse_receipt()["charged_input_14_sha256"],
        },
        "custody": custody,
        "datum": {
            "degrees": [108, 72],
            "M": [-72, 81, 106],
            "d": [108, 36, 9, 1],
            "V": [7, 7],
            "u3": 2,
            "v3": 7,
            "split": {
                "delta": 3,
                "partition": [1, 1],
                "p": "pi^2-c",
                "q": "p^23*U",
                "U_prime": "5*p^2",
                "degree_U": 5,
                "mod_gauge": "one parameter e0",
                "tree": "24 -> 12+12; final order 4 on both children",
            },
        },
        "tower": {
            "h3": "P; degree 9; top y^2*(y-x)^7",
            "h2": "P^4+C2*P^2+C3*P+C4; degree 36",
            "F": "h2^3+A2*h2+A3; degree 108",
            "G": "h2^2+B1*h2+B2; degree 72",
            "raw_blocks": {"H": 54, "C2": 135, "C3": 216, "C4": 297, "A2": 1998, "A3": 3294, "B1": 702, "B2": 1998},
            "fixed_top_blocks": {"H": 45, "C2": 126, "C3": 207, "C4": 288, "A2": 1962, "A3": 3258, "B1": 666, "B2": 1962},
            "fixed_top_total": fixed_chart,
        },
        "major_structure": major,
        "outer": outer,
        "minor_incidence": incidence,
        "continuation_metadata": schedule,
        "stage": stage,
        "Singular": singular,
        "software": software_record(),
        "FALLACY_v2": {
            "flag_place_series_separated": True,
            "strict_below_and_at_level_separated": True,
            "c_localization": "Rabinowitsch wrapper; no sat()",
            "Qstar_pivots": "Q* only; c and all branch parameters excluded",
            "e0_map": "not identified with an F/G coefficient; effective-root bridge not assumed",
            "representative_claimed": False,
            "exit_price_assertion_made": False,
        },
    }
    result["stage"]["wall_seconds_internal"] = round(time.monotonic() - started, 6)
    result["stage"]["peak_RSS_KiB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--skeleton-only", action="store_true")
    mode.add_argument("--stage", type=int)
    parser.add_argument("--branch", default="delta3", choices=["delta3"])
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    if args.stage is not None and args.stage != 0:
        parser.error("stage 0 is terminal (DEAD); later stages must not run")
    result = compile_result(args.output_dir, run_stage=args.stage == 0)
    destination = args.output_dir / ("stage0.json" if args.stage == 0 else "skeleton.json")
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    destination.write_text(payload, encoding="utf-8")
    if args.stage == 0:
        certificate = {
            "type": "D108-delta3-EXACT-LOCALIZED-UNIT-CERTIFICATE",
            "ring": "Q[jet1,jet2,c,Zc]",
            "generator_order": [
                "minor_n6_pi0", "minor_n7_pi0", "minor_n7_pi1",
                "minor_n8_pi0", "minor_n8_pi1", "Zc*c-1",
            ],
            "residual": result["minor_incidence"]["residual"],
            "certificate": result["minor_incidence"]["certificate"],
            "Singular": result["Singular"],
            "status": "DEAD",
        }
        (args.output_dir / "death_certificate.json").write_text(
            json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    print(payload, end="")


if __name__ == "__main__":
    main()
