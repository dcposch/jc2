#!/usr/bin/env python3
"""Replay the (99,66), delta=2 stage-4 certificate slice over QQ.

This is deliberately a slice, not a rerun of the 7,161-coordinate engine.  It
uses the frozen clean-room sparse-series implementation to reconstruct the
needed pole/Jacobian rows, then converts those rows to SymPy and records every
row operation.  The source rows are reconstructed *before* the B1 D2/D1
support substitutions.  Consequently the final identity is an honest linear
combination of labelled source rows, rather than merely the scalar
normalisation ``1 = 6264/6264`` in the reduced quotient.

The fixed face coefficient K2[t^4 (w-1)^21] = -8 is exposed as the variable
``face`` and imposed by the labelled row ``incidence_K2_face_t4_z21``.  No
division by ``face`` or by the branch parameter ``rho`` occurs.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import importlib
import json
from math import comb
from pathlib import Path
import sys
from typing import Iterable

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_STAGE4 = Path("/tmp/jc2-lane.C9HiZU/inputs/stage4.json")
INDEP_DIR = ROOT / "box/g9966indep-20260903"
TERMINAL = "stage4_J_d159_k35"
FACE_ROW = "incidence_K2_face_t4_z21"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def receipt_hash_for(basename: str) -> str:
    """Read, rather than retype, the charged digest from the lane receipt."""
    receipt = ROOT / "xmodel/two-place-obstruction-core-sol56-20260903.run.v2"
    fields = {}
    for line in receipt.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            fields[key] = value
    for index in range(1, int(fields["charged_inputs"]) + 1):
        if fields[f"charged_input_{index}_basename"] == basename:
            return fields[f"charged_input_{index}_sha256"]
    raise AssertionError(f"missing charged basename: {basename}")


def load_clean_room():
    sys.path.insert(0, str(INDEP_DIR))
    engine = importlib.import_module("indep_engine")
    ring = importlib.import_module("ring")
    return engine, ring


def to_sympy(poly, symbols: dict[str, sp.Symbol]) -> sp.Expr:
    """Convert the clean-room sparse-Q representation to a SymPy expression."""
    answer = sp.Integer(0)
    for monomial, coefficient in poly.items():
        term = sp.Rational(coefficient.numerator, coefficient.denominator)
        for name, exponent in monomial:
            term *= symbols.setdefault(name, sp.Symbol(name)) ** exponent
        answer += term
    return sp.expand(answer)


def labels_for_core() -> list[str]:
    labels: list[str] = []
    for stage, local, degree in ((1, 5, 162), (2, 6, 161), (3, 7, 160)):
        labels.append(f"stage{stage}_G_local{local}_coord0")
        labels.extend(f"stage{stage}_J_d{degree}_k{k}" for k in range(36, 44))
    labels.append("stage4_G_local8_coord0")
    labels.append(TERMINAL)
    return labels


def build_full_rows():
    """Return selected raw rows before B1 D2/D1 and before fixing face=-8."""
    E, R = load_clean_room()
    branch = E.Branch("delta2")

    # Reconstruct the charged branch chart.  The eventual certificate is
    # independent of the remaining h3/K2 parameters; they remain symbolic.
    h_elim = E.Elim(forbidden={"rho"})
    for label, row in E.leader_rows(branch, E.build_K3(12)):
        h_elim.feed(label, row)
    assert len(h_elim.pivots) == 18 and not h_elim.residues
    K3 = E.series_subst(E.build_K3(E.NT), h_elim.sub)
    K2, _low_free, _low_const, violations = E.build_K2(K3)
    assert not violations

    # Undo just the one fixed equality coefficient used by this core.  Its
    # equation is put back into the certificate as FACE_ROW below.
    K2[4][21] = R.var("face")

    # Full B1 support (before the D2 deletion); only variables actually touched
    # by the selected rows will enter the slice.
    B1 = [R.pzero() for _ in range(E.NT)]
    for r in range(E.NT):
        for q in range(33 - r):
            B1[r] = R.padd(B1[r], {q: R.var(f"B1c_{r}_{q}")})

    KF, KG = E.build_KFKG(K2, B1)
    KJ = E.build_KJ_factored(KF, B1, K2)
    rows = {}
    for stage, local, degree in ((1, 5, 162), (2, 6, 161), (3, 7, 160), (4, 8, 159)):
        split = E.split_z(branch.sub_series(KG, local).get(local, {}), branch.zvar)
        rows[f"stage{stage}_G_local{local}_coord0"] = split.get(0, {})
        jac = E.to_w(KJ[1 if stage == 1 else stage])
        if stage < 4:
            for k in range(36, 44):
                rows[f"stage{stage}_J_d{degree}_k{k}"] = jac.get(k, {})
        else:
            rows[TERMINAL] = jac.get(35, {})
    assert set(rows) == set(labels_for_core())
    symbols: dict[str, sp.Symbol] = {}
    return {label: to_sympy(row, symbols) for label, row in rows.items()}, symbols


@dataclass
class Pivot:
    label: str
    variable: sp.Symbol
    coefficient: sp.Rational
    equation: sp.Expr
    rhs: sp.Expr
    certificate: dict[str, sp.Expr]


class Tracer:
    """Triangular exact-Q reduction retaining ideal-membership provenance."""

    def __init__(self):
        self.pivots: list[Pivot] = []
        self.raw_rows: dict[str, sp.Expr] = {}
        self.dependencies: dict[str, list[str]] = {}

    @staticmethod
    def _add(target: dict[str, sp.Expr], label: str, value: sp.Expr) -> None:
        if value == 0:
            return
        new = sp.cancel(target.get(label, sp.Integer(0)) + value)
        if new == 0:
            target.pop(label, None)
        else:
            target[label] = new

    def reduce_new(self, label: str, raw: sp.Expr) -> tuple[sp.Expr, dict[str, sp.Expr]]:
        if label in self.raw_rows:
            raise AssertionError(f"duplicate source label: {label}")
        raw = sp.expand(raw)
        self.raw_rows[label] = raw
        expression = raw
        certificate: dict[str, sp.Expr] = {label: sp.Integer(1)}
        dependencies: list[str] = []
        for pivot in self.pivots:
            variable = pivot.variable
            if variable not in expression.free_symbols:
                continue
            image = sp.expand(expression.subs(variable, pivot.rhs))
            # The B1 eliminations are affine-linear.  The exposed face appears
            # quadratically in the final pole row, so use exact polynomial
            # division by the (linear) pivot equation in full generality.
            difference = sp.expand(expression - image)
            if difference == 0:
                continue
            dependencies.append(pivot.label)
            quotient = sp.cancel(difference / pivot.equation)
            assert sp.expand(expression - image - quotient * pivot.equation) == 0
            expression = image
            for source, multiplier in pivot.certificate.items():
                self._add(certificate, source, -quotient * multiplier)
        self.dependencies[label] = dependencies
        return sp.expand(expression), certificate

    def add_pivot(
        self, label: str, raw: sp.Expr, variable: sp.Symbol,
        expected_coefficient: int | sp.Rational | None = None,
    ) -> Pivot:
        equation, certificate = self.reduce_new(label, raw)
        coefficient = sp.diff(equation, variable)
        assert coefficient.is_Rational and coefficient != 0
        coefficient = sp.Rational(coefficient)
        if expected_coefficient is not None:
            assert coefficient == sp.Rational(expected_coefficient), (
                label, variable, coefficient, expected_coefficient
            )
        remainder = sp.expand(equation - coefficient * variable)
        assert variable not in remainder.free_symbols
        rhs = sp.cancel(-remainder / coefficient)
        pivot = Pivot(label, variable, coefficient, equation, rhs, certificate)
        self.pivots.append(pivot)
        return pivot


def charged_joint_pivots(stage4: dict) -> list[tuple[str, str, int]]:
    wanted = set(labels_for_core()) - {TERMINAL}
    found = []
    for item in stage4["joint_elimination"]["pivot_ledger"]:
        if item["row"] in wanted:
            found.append((item["row"], item["variable"], int(item["coefficient"])))
    expected_labels = labels_for_core()[:-1]
    assert [label for label, _variable, _coefficient in found] == expected_labels
    return found


def family(label: str) -> str:
    if label == FACE_ROW:
        return "incidence"
    if label.startswith("outer_"):
        return "outer"
    if "_G_local" in label or "_F_local" in label:
        return "pole"
    if "_J_d" in label:
        return "Jacobian"
    raise AssertionError(f"unclassified row: {label}")


def complete_family_counts(labels: Iterable[str]) -> dict[str, int]:
    counts = Counter(family(label) for label in labels)
    return {
        name: counts.get(name, 0)
        for name in ("incidence", "outer", "pole", "Jacobian", "localization")
    }


def transitive_dependencies(tracer: Tracer, root: str) -> set[str]:
    closure = {root}
    pending = [root]
    while pending:
        label = pending.pop()
        for dependency in tracer.dependencies.get(label, []):
            if dependency not in closure:
                closure.add(dependency)
                pending.append(dependency)
    return closure


def specialised_linear_irredundancy(
    rows: dict[str, sp.Expr], labels: list[str], face: sp.Symbol
) -> dict:
    """Show that the seven quotient rows form an inconsistent linear circuit.

    A single legal specialization (rho=1, all other non-B1 parameters zero)
    suffices to prove that each six-row subideal is proper: each has a rational
    common zero at that specialization.  The full seven rows remain
    inconsistent because their symbolic certificate is 1.
    """
    variables = sorted(
        {v for label in labels for v in rows[label].free_symbols if str(v).startswith("B1c_")},
        key=str,
    )
    parameters = {
        v for label in labels for v in rows[label].free_symbols
        if v not in variables and v != face
    }
    specialization = {
        parameter: (1 if str(parameter) in {"rho", "u"} else 0)
        for parameter in parameters
    }
    specialization[face] = -8
    equations = [sp.expand(rows[label].subs(specialization)) for label in labels]
    matrix, rhs = sp.linear_eq_to_matrix(equations, variables)
    full_coefficient_rank = matrix.rank()
    full_augmented_rank = matrix.row_join(rhs).rank()
    assert full_augmented_rank == full_coefficient_rank + 1
    leave_one_out = {}
    for index, label in enumerate(labels):
        keep = [i for i in range(len(labels)) if i != index]
        submatrix = matrix[keep, :]
        subrhs = rhs[keep, :]
        consistent = submatrix.rank() == submatrix.row_join(subrhs).rank()
        assert consistent, label
        leave_one_out[label] = True
    return {
        "specialization": "rho=u=1; face=-8; all other non-B1 parameters=0",
        "full_coefficient_rank": full_coefficient_rank,
        "full_augmented_rank": full_augmented_rank,
        "every_leave_one_out_subset_has_a_rational_common_zero": all(leave_one_out.values()),
    }


def construct_certificate(stage4_path: Path):
    expected_hash = receipt_hash_for("stage4.json")
    assert sha256(stage4_path) == expected_hash
    stage4 = json.loads(stage4_path.read_text(encoding="utf-8"))
    assert stage4["branch"] == "delta2"
    assert stage4["joint_elimination"]["residual_rows"][0] == {
        "label": TERMINAL,
        "expression": "6264",
    }

    selected_rows, symbols = build_full_rows()
    face = symbols.setdefault("face", sp.Symbol("face"))
    tracer = Tracer()

    # Fixed equality face: coefficient -8, restored as a source equation.
    tracer.add_pivot(FACE_ROW, face + 8, face, 1)

    # Exactly the D2-deleted B1 coordinates that occur in the selected raw
    # rows.  Dynamic extraction is also a guard against silently widening the
    # claimed slice.
    touched = set().union(*(row.free_symbols for row in selected_rows.values()))
    d2_symbols = []
    for variable in touched:
        name = str(variable)
        if not name.startswith("B1c_"):
            continue
        _block, r_text, q_text = name.split("_")
        r, q = int(r_text), int(q_text)
        if 3 * r + 4 * q < 93:
            d2_symbols.append(variable)
    d2_symbols.sort(key=str)
    assert len(d2_symbols) == 90
    for variable in d2_symbols:
        tracer.add_pivot(f"outer_B1_D2_zero_{variable}", variable, variable, 1)

    # The W=93 D1 system is square.  Only B1c_3_21 is syntactically touched by
    # the raw core, but deriving that zero coordinate uses the eight scalar
    # rows.  The final minimal combination is allowed to prune them if their
    # multipliers cancel.
    boundary = [(r, q) for r in range(33) for q in range(33 - r) if 3 * r + 4 * q == 93]
    assert boundary == [(3, 21), (7, 18), (11, 15), (15, 12), (19, 9), (23, 6), (27, 3), (31, 0)]
    d1_expected = [
        "B1c_11_15", "B1c_15_12", "B1c_19_9", "B1c_23_6",
        "B1c_27_3", "B1c_31_0", "B1c_3_21", "B1c_7_18",
    ]
    for k, variable_name in enumerate(d1_expected):
        row = sum(
            comb(q, k) * symbols.setdefault(f"B1c_{r}_{q}", sp.Symbol(f"B1c_{r}_{q}"))
            for r, q in boundary if q >= k
        )
        tracer.add_pivot(
            f"outer_B1_D1_s0_k{k}", row,
            symbols.setdefault(variable_name, sp.Symbol(variable_name)),
        )

    # Replay the 28 candidate Q* rows available before the terminal; the
    # transitive dependency calculation below determines which are reached.
    charged = charged_joint_pivots(stage4)
    for label, variable_name, coefficient in charged:
        tracer.add_pivot(
            label, selected_rows[label],
            symbols.setdefault(variable_name, sp.Symbol(variable_name)),
            coefficient,
        )

    terminal_reduced, terminal_certificate = tracer.reduce_new(
        TERMINAL, selected_rows[TERMINAL]
    )
    assert terminal_reduced == 6264
    certificate = {
        label: sp.cancel(multiplier / 6264)
        for label, multiplier in terminal_certificate.items()
        if multiplier != 0
    }
    certificate = {label: value for label, value in certificate.items() if value != 0}
    identity = sp.expand(sum(certificate[label] * tracer.raw_rows[label] for label in certificate))
    assert identity == 1

    # The explicit lift of the syntactically touched boundary zero fact.  This
    # is independent of whether its multiplier survives certificate pruning.
    d1_lift = {
        "outer_B1_D1_s0_k1": sp.Rational(374, 19683),
        "outer_B1_D1_s0_k2": -sp.Rational(20, 729),
        "outer_B1_D1_s0_k3": sp.Rational(166, 6561),
        "outer_B1_D1_s0_k4": -sp.Rational(112, 6561),
        "outer_B1_D1_s0_k5": sp.Rational(55, 6561),
        "outer_B1_D1_s0_k6": -sp.Rational(2, 729),
        "outer_B1_D1_s0_k7": sp.Rational(1, 2187),
    }
    b3q21 = symbols.setdefault("B1c_3_21", sp.Symbol("B1c_3_21"))
    assert sp.expand(sum(c * tracer.raw_rows[label] for label, c in d1_lift.items()) - b3q21) == 0

    # Repeat only the cumulative joint reduction in the already fixed/support
    # quotient.  The charged ledger offers 28 earlier pivots plus the terminal
    # row; recursive dependency pruning leaves the seven-node quotient DAG.
    quotient_substitution = {face: -8, **{variable: 0 for variable in d2_symbols}}
    quotient_substitution.update(
        {symbols.setdefault(f"B1c_{r}_{q}", sp.Symbol(f"B1c_{r}_{q}")): 0 for r, q in boundary}
    )
    quotient_rows = {
        label: sp.expand(row.subs(quotient_substitution)) for label, row in selected_rows.items()
    }
    quotient = Tracer()
    for label, variable_name, coefficient in charged:
        quotient.add_pivot(
            label, quotient_rows[label],
            symbols.setdefault(variable_name, sp.Symbol(variable_name)), coefficient,
        )
    quotient_reduced, quotient_terminal_certificate = quotient.reduce_new(
        TERMINAL, quotient_rows[TERMINAL]
    )
    assert quotient_reduced == 6264
    quotient_certificate = {
        label: sp.cancel(multiplier / 6264)
        for label, multiplier in quotient_terminal_certificate.items()
        if multiplier != 0
    }
    quotient_certificate = {
        label: multiplier for label, multiplier in quotient_certificate.items() if multiplier != 0
    }
    assert sp.expand(sum(
        quotient_certificate[label] * quotient.raw_rows[label]
        for label in quotient_certificate
    )) == 1
    assert set(quotient_certificate) == set(certificate) - {FACE_ROW}
    assert all(
        sp.expand(quotient_certificate[label] - certificate[label]) == 0
        for label in quotient_certificate
    )
    quotient_closure = transitive_dependencies(quotient, TERMINAL)
    full_closure = transitive_dependencies(tracer, TERMINAL)
    assert len(quotient_closure) == 7, sorted(quotient_closure)
    assert len(full_closure) == 106, (len(full_closure), sorted(full_closure))

    # Scalar normalization alone is not the raw identity: it omits every
    # dependency multiplier.  Record this as an executable distinction.
    assert sp.expand(tracer.raw_rows[TERMINAL] / 6264) != 1

    # Negative control.  Remove the unique affine 64 from the stage-4 pole row
    # while retaining the frozen certificate multipliers.  The identity becomes
    # zero, and setting every B1 coordinate to zero is then a common zero of the
    # perturbed source slice.  Thus the perturbed ideal cannot contain 1.
    perturbed_label = "stage4_G_local8_coord0"
    perturbed_rows = dict(tracer.raw_rows)
    assert sp.expand(perturbed_rows[perturbed_label].subs(face, -8)).subs(
        {v: 0 for v in touched if str(v).startswith("B1c_")}
    ) == 64
    perturbed_rows[perturbed_label] = sp.expand(perturbed_rows[perturbed_label] - face**2)
    perturbed_value = sp.expand(sum(certificate[label] * perturbed_rows[label] for label in certificate))
    assert perturbed_value != 1
    zero_point = {v: 0 for v in set().union(*(row.free_symbols for row in perturbed_rows.values())) if str(v).startswith("B1c_")}
    zero_point[face] = -8
    assert all(sp.expand(row.subs(zero_point)) == 0 for row in perturbed_rows.values())
    assert sp.expand(perturbed_value.subs(zero_point)) == 0

    used_labels = list(certificate)
    counts = complete_family_counts(used_labels)
    d1_used = [label for label in used_labels if "_D1_" in label]
    d2_used = [label for label in used_labels if "_D2_" in label]
    outer_forbidden = sorted(
        str(variable)
        for variable in set().union(*(tracer.raw_rows[label].free_symbols for label in used_labels))
        if str(variable).startswith(("A2", "A3", "B2"))
    )
    bridge_labels = [label for label in used_labels if "T2" in label or "T3" in label]
    assert not outer_forbidden and not bridge_labels
    assert all("rho" not in sp.denom(value).free_symbols for value in certificate.values())

    quotient_labels = list(quotient_certificate)
    quotient_counts = complete_family_counts(quotient_labels)
    quotient_closure_counts = complete_family_counts(quotient_closure)
    full_closure_counts = complete_family_counts(full_closure)
    irredundancy = specialised_linear_irredundancy(
        quotient.raw_rows, quotient_labels, face
    )
    # The eighth (incidence) row is necessary within this support as well:
    # after omitting face+8, all seven pole/Jacobian rows have the localized
    # common zero rho=1 and every other symbol (including face and B1c)=0.
    all_core_symbols = set().union(*(
        tracer.raw_rows[label].free_symbols for label in quotient_labels
    ))
    incidence_omitted_point = {
        variable: (1 if str(variable) == "rho" else 0)
        for variable in all_core_symbols
    }
    assert all(
        sp.expand(tracer.raw_rows[label].subs(incidence_omitted_point)) == 0
        for label in quotient_labels
    )

    summary = {
        "stage4_sha256": expected_hash,
        "terminal_row": TERMINAL,
        "terminal_normal_form": str(terminal_reduced),
        "certificate_row_count": len(certificate),
        "rows_per_family": counts,
        "certificate_rows": used_labels,
        "inclusion_minimal_on_its_eight_rows": {
            "each_core_row_omission": (
                "rational common zero certified by the quotient leave-one-out ranks"
            ),
            "incidence_row_omission_common_zero": (
                "rho=1; every other source-row symbol, including face and B1c, is 0"
            ),
        },
        "quotient_certificate": {
            "row_count": len(quotient_certificate),
            "rows_per_family": quotient_counts,
            "rows": quotient_labels,
            "inclusion_minimal_on_its_seven_rows": irredundancy,
        },
        "dependency_closure": {
            "incidence_fixed_face_rows": 1,
            "B1_D2_zero_facts_touched": len(d2_symbols),
            "B1_D1_scalar_rows_examined": 8,
            "joint_Qstar_pivots_available_before_terminal": len(charged),
            "joint_Qstar_pivots_actually_reached": len(quotient_closure) - 1,
            "terminal_rows": 1,
            "scheduled_candidate_rows_before_dependency_pruning": 1 + len(d2_symbols) + 8 + len(charged) + 1,
            "verified_full_transitive_node_count": len(full_closure),
            "verified_full_transitive_rows_per_family": full_closure_counts,
            "verified_quotient_transitive_node_count": len(quotient_closure),
            "verified_quotient_transitive_rows_per_family": quotient_closure_counts,
            "verified_quotient_direct_edges": {
                label: [
                    dependency for dependency in quotient.dependencies.get(label, [])
                    if dependency in quotient_closure
                ]
                for label in sorted(quotient_closure)
            },
            "D2_rows_retained_after_pruning": len(d2_used),
            "D1_rows_retained_after_pruning": len(d1_used),
            "B1c_3_21_D1_lift_nonzero_rows": len(d1_lift),
            "B1c_3_21_D1_lift": {label: str(value) for label, value in d1_lift.items()},
        },
        "deepest_t_power": 8,
        "outer_A2_A3_B2_coefficients": outer_forbidden,
        "T2_T3_bridge_rows": bridge_labels,
        "localization_rows": 0,
        "uses_rho_denominator": False,
        "raw_identity": "1 = sum(multiplier[label] * raw_row[label])",
        "negative_control": {
            "change": "stage4_G_local8_coord0: subtract face**2 (64 after face=-8)",
            "frozen_certificate_value": str(perturbed_value),
            "common_zero": "all B1c=0, face=-8",
        },
    }
    return summary, certificate, quotient_certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage4", type=Path, default=DEFAULT_STAGE4)
    parser.add_argument(
        "--multipliers", action="store_true",
        help="print the exact nonzero source-row multipliers after the JSON summary",
    )
    args = parser.parse_args()
    summary, certificate, quotient_certificate = construct_certificate(args.stage4)
    print(json.dumps(summary, indent=2, sort_keys=True))
    if args.multipliers:
        print("BEGIN_QUOTIENT_MULTIPLIERS")
        for label, multiplier in quotient_certificate.items():
            print(f"{label}\t{sp.sstr(multiplier)}")
        print("END_QUOTIENT_MULTIPLIERS")
        print("BEGIN_FULLY_LIFTED_MULTIPLIERS")
        for label, multiplier in certificate.items():
            print(f"{label}\t{sp.sstr(multiplier)}")
        print("END_FULLY_LIFTED_MULTIPLIERS")


if __name__ == "__main__":
    main()
