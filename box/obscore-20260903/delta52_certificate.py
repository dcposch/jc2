#!/usr/bin/env python3
"""Exact certificate slice for the (99,66), delta=5/2 stage-8 kill.

This is deliberately a small replay, not a rerun of the 7,161-coordinate
charged engine.  It reconstructs the post-outer-D2 inner system with the
independent clean-room row builders, checks it against the charged stage-8
pivot ledger, traces the terminal pole row backwards, and verifies the unique
support-minimal Schur certificate over Q in that quotient.

The literal identity proved here lives after the source-forced outer-D2
support projector and the declared common-h3 branch map.  The script also
replays the exact B1 weight-93 D1 lift and audits the h3 incidence dependence.
The charged artifacts do not serialize multipliers for a complete lift before
the outer-D2 projector or before the hard-coded h3 map; this script does not
invent them.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction as Fr
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
INDEP = ROOT / "box/g9966indep-20260903"
STAGE8 = ROOT / "box/g9966s8-20260903/runs/delta52/stage8.json"
STAGE8_MANIFEST = ROOT / "box/g9966s8-20260903/artifact-manifest.sha256"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def check_manifest_entry(manifest: Path, path: Path) -> None:
    entries = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, name = line.split(None, 1)
        entries[name.strip()] = digest
    relative = str(path.relative_to(ROOT))
    assert relative in entries, (manifest, relative)
    assert sha256(path) == entries[relative], relative


# Verify the completed clean-room files mechanically from their own manifest.
indep_manifest = {}
for line in (INDEP / "artifacts.sha256").read_text(encoding="utf-8").splitlines():
    digest, name = line.split(None, 1)
    indep_manifest[name.strip()] = digest
for name in ("indep_engine.py", "ring.py", "run_delta52.json"):
    assert sha256(INDEP / name) == indep_manifest[name]
check_manifest_entry(STAGE8_MANIFEST, STAGE8)

sys.path.insert(0, str(INDEP))
import indep_engine as E  # noqa: E402
from ring import (  # noqa: E402
    add,
    as_const,
    const,
    is_zero,
    lin_coeff,
    mul,
    smul,
    subst,
    var,
    vars_of,
)


def poly_text(p: dict) -> str:
    """Stable compact text for the clean-room sparse polynomial format."""
    pieces = []
    for monomial, coefficient in sorted(p.items()):
        factors = [v if exponent == 1 else f"{v}^{exponent}"
                   for v, exponent in monomial]
        pieces.append(f"({coefficient})*{'*'.join(factors) or '1'}")
    return " + ".join(pieces) or "0"


class TraceElim(E.Elim):
    """The clean-room Q* eliminator with its pre-later-pivot DAG retained."""

    def __init__(self, forbidden):
        super().__init__(forbidden)
        self.steps = []

    def feed(self, label, p):
        p = self.reduce(p)
        if is_zero(p):
            self.zero += 1
            return "zero"
        candidate = None
        for variable in sorted(vars_of(p), key=self.rank_key):
            if variable in self.forbidden:
                continue
            coefficient = lin_coeff(p, variable)
            if coefficient and all(
                (variable not in dict(monomial))
                or monomial == ((variable, 1),)
                for monomial in p
            ):
                candidate = (variable, coefficient)
                break
        if candidate is None:
            self.residues.append((label, p))
            return "residue"
        variable, coefficient = candidate
        rest = {m: co for m, co in p.items() if m != ((variable, 1),)}
        rhs = smul(rest, Fr(-1) / coefficient)
        self.steps.append({
            "label": label,
            "variable": variable,
            "coefficient": coefficient,
            "rhs": rhs,
            "rhs_variables": sorted(vars_of(rhs)),
        })
        for old in list(self.sub):
            self.sub[old] = subst(self.sub[old], variable, rhs)
        self.sub[variable] = rhs
        self.pivots.append((label, variable, str(coefficient)))
        return "pivot"


def to_sympy(p: dict, symbols: dict[str, sp.Symbol]) -> sp.Expr:
    out = sp.Integer(0)
    for monomial, coefficient in p.items():
        term = sp.Rational(coefficient.numerator, coefficient.denominator)
        for name, exponent in monomial:
            # The independent engine calls the charged parameter v "vv".
            display_name = "v" if name == "vv" else name
            term *= symbols.setdefault(display_name, sp.Symbol(display_name)) ** exponent
        out += term
    return sp.expand(out)


def branch_and_inner_rows():
    branch = E.Branch("delta52")

    # Common-h3 incidence map.  Hc_11_0/Xu compatibility is intentionally not
    # fed: the clean-room no-ODE control shows it is not a kill dependency.
    incidence = TraceElim(forbidden={"c"})
    incidence_rows = E.leader_rows(branch, E.build_K3(12))
    for label, row in incidence_rows:
        incidence.feed(label, row)
    assert len(incidence.pivots) == 20
    assert len(incidence.residues) == 0

    K3 = E.series_subst(E.build_K3(E.NT), incidence.sub)
    K2, _low_free, _low_const, violations = E.build_K2(K3)
    assert not violations
    B1, _used = E.build_B1(E.NT)
    KF, KG = E.build_KFKG(K2, B1)
    KJ = E.build_KJ_factored(KF, B1, K2)

    # Terminal pole row before any outer-D1 or cumulative joint substitution.
    pole = E.split_z(
        branch.sub_series(KG, 16).get(16, {}), branch.zvar
    ).get(0, {})

    # The sole relevant outer-D1 face.  Normalize labels to the charged names.
    d1_rows = []
    for offset, _label, row in E.d1_rows_for(
        "B1", 32, 33, Fr(-1), Fr(-1, 9),
        lambda r, q: f"B1c_{r}_{q}",
    ):
        if offset == 0:
            k = len(d1_rows)
            d1_rows.append((f"B1_D1_s0_k{k}", row))
    assert len(d1_rows) == 8

    # Exactly the four earlier Jacobian levels whose B1 variables occur in the
    # terminal pole row.  Stage 1 finishes t^1/degree 162.
    joint_rows = []
    for stage, t_power, ks in (
        (1, 1, range(35, 44)),
        (2, 2, range(35, 44)),
        (3, 3, range(35, 44)),
        (4, 4, range(35, 43)),
    ):
        band = E.to_w(KJ[t_power])
        for k in ks:
            joint_rows.append((
                f"stage{stage}_J_d{163 - t_power}_k{k}",
                band.get(k, {}),
            ))
    assert len(joint_rows) == 35
    return branch, incidence, pole, d1_rows, joint_rows


branch, incidence, pole_pre_d1, d1_rows, joint_rows = branch_and_inner_rows()


# Replay the engine-order ancestry: outer D1 first, then the 35 joint pivots.
path_elim = TraceElim(forbidden={"c"})
for label, row in d1_rows:
    assert path_elim.feed(label, row) == "pivot"
after_d1_step = len(path_elim.steps)
pole_pre_joint = path_elim.reduce(pole_pre_d1)
for label, row in joint_rows:
    assert path_elim.feed(label, row) == "pivot"

assert after_d1_step == 8
assert len(path_elim.steps) == 43
assert as_const(path_elim.reduce(pole_pre_d1)) == Fr(64)

raw_pole_b1 = sorted(v for v in vars_of(pole_pre_d1)
                     if v.startswith("B1c_"))
post_d1_pole_b1 = sorted(v for v in vars_of(pole_pre_joint)
                         if v.startswith("B1c_"))
assert len(raw_pole_b1) == 36
assert len(post_d1_pole_b1) == 35

joint_steps = path_elim.steps[after_d1_step:]
terminal_joint_variables = sorted(
    vars_of(pole_pre_joint).intersection({s["variable"] for s in joint_steps})
)
assert len(terminal_joint_variables) == 35
assert not any(name.startswith("B1c_7_") for name in terminal_joint_variables)

# In the reduced-row elimination DAG only k6 and k7 are ancestors: k6 removes
# B1c_3_21, and its reduced RHS contains B1c_7_18, removed by k7.  Re-expressing
# that reduced fact in the eight ORIGINAL D1 rows is a different count below.
d1_step_by_variable = {step["variable"]: step
                       for step in path_elim.steps[:8]}
pending_d1 = list(vars_of(pole_pre_d1).intersection(d1_step_by_variable))
pending_d1.extend(
    variable
    for _label, row in joint_rows
    for variable in vars_of(row).intersection(d1_step_by_variable)
)
d1_reduced_dag_labels = set()
while pending_d1:
    variable = pending_d1.pop()
    step = d1_step_by_variable[variable]
    if step["label"] in d1_reduced_dag_labels:
        continue
    d1_reduced_dag_labels.add(step["label"])
    pending_d1.extend(v for v in step["rhs_variables"]
                      if v in d1_step_by_variable)
assert d1_reduced_dag_labels == {"B1_D1_s0_k6", "B1_D1_s0_k7"}


# Cross-check every one of those 35 pivots against the charged ledger, and
# separately verify that the seven new stage-8 pivots are not ancestors.
charged = json.loads(STAGE8.read_text(encoding="utf-8"))
ledger = charged["joint_elimination"]["pivot_ledger"]
assert len(ledger) == 66
for got, expected in zip(joint_steps, ledger[:35]):
    assert got["label"] == expected["row"]
    assert got["variable"] == expected["variable"]
    assert str(got["coefficient"]) == expected["coefficient"]
new_stage8 = ledger[59:]
assert [entry["coefficient"] for entry in new_stage8] == [
    "675", "576", "477", "378", "279", "180", "81",
]
assert not set(terminal_joint_variables).intersection(
    entry["variable"] for entry in new_stage8
)
assert charged["joint_elimination"]["residual_rows"] == [
    {"expression": "64", "label": "stage8_G_local16_coord0"}
]


# Exact D1 lift of the boundary zero.  The raw W=93 rows have columns
# q=21,18,...,0.  The unique expression for B1c_3_21 has zero k=0
# coefficient and nonzero coefficients on k=1..7.
sym: dict[str, sp.Symbol] = {}
d1_sym = [(label, to_sympy(row, sym)) for label, row in d1_rows]
w93_variables = [sym[f"B1c_{r}_{q}"] for r, q in (
    (3, 21), (7, 18), (11, 15), (15, 12),
    (19, 9), (23, 6), (27, 3), (31, 0),
)]
D = sp.Matrix([[row.coeff(variable) for variable in w93_variables]
               for _label, row in d1_sym])
e3 = sp.Matrix([1] + [0] * 7)
d1_lift = [sp.cancel(x) for x in D.T.inv() * e3]
assert d1_lift == [
    0,
    sp.Rational(374, 19683),
    sp.Rational(-20, 729),
    sp.Rational(166, 6561),
    sp.Rational(-112, 6561),
    sp.Rational(55, 6561),
    sp.Rational(-2, 729),
    sp.Rational(1, 2187),
]
assert sp.expand(
    sum(a * row for a, (_label, row) in zip(d1_lift, d1_sym))
    - sym["B1c_3_21"]
) == 0

d1_by_variable = {step["variable"]: step for step in path_elim.steps[:8]}
assert d1_by_variable["B1c_3_21"]["label"] == "B1_D1_s0_k6"
assert d1_by_variable["B1c_3_21"]["rhs_variables"] == ["B1c_7_18"]
assert d1_by_variable["B1c_7_18"]["label"] == "B1_D1_s0_k7"
assert not d1_by_variable["B1c_7_18"]["rhs_variables"]


# Build the 43 x 43 filtered B1 obstruction block (8 outer-D1 rows followed
# by 35 Jacobian rows) and take the pole functional's Schur complement.
all_rows = d1_sym + [(label, to_sympy(row, sym)) for label, row in joint_rows]
pole_sym = to_sympy(pole_pre_d1, sym)
b1_variables = sorted(
    {x for _label, row in all_rows for x in row.free_symbols
     if str(x).startswith("B1c_")},
    key=str,
)
assert len(all_rows) == len(b1_variables) == 43
A = sp.Matrix([[row.coeff(variable) for variable in b1_variables]
               for _label, row in all_rows])
ell = sp.Matrix([pole_sym.coeff(variable) for variable in b1_variables])
alpha = [sp.cancel(x) for x in A.T.inv() * ell]
schur = sp.expand(
    pole_sym - sum(a * row for a, (_label, row) in zip(alpha, all_rows))
)
assert schur == 64

nonzero_alpha = [
    (label, sp.factor(a))
    for a, (label, _row) in zip(alpha, all_rows)
    if sp.cancel(a) != 0
]
assert [label for label, _a in nonzero_alpha] == [
    "stage1_J_d162_k35",
    "stage1_J_d162_k36",
    "stage2_J_d161_k35",
    "stage2_J_d161_k36",
    "stage3_J_d160_k35",
    "stage4_J_d159_k35",
]
assert all(sp.cancel(a) == 0 for a in alpha[:8])

# The literal minimal certificate in the post-D2, declared-branch quotient is
# 1 = pole/64 + sum_i certificate_i * row_i.
certificate = [("stage8_G_local16_coord0", sp.Rational(1, 64))]
certificate.extend((label, sp.factor(-a / 64)) for label, a in nonzero_alpha)
certificate_lhs = pole_sym / 64 - sum(
    a * row / 64 for a, (_label, row) in zip(alpha, all_rows)
)
assert sp.expand(certificate_lhs - 1) == 0


# Negative control: perturb one consumed Jacobian source row while retaining
# the extracted multipliers.  The old certificate must cease to be an identity.
perturbed_rows = list(all_rows)
target = next(i for i, (label, _row) in enumerate(perturbed_rows)
              if label == "stage4_J_d159_k35")
perturbed_rows[target] = (
    perturbed_rows[target][0],
    perturbed_rows[target][1] + sym["B1c_3_22"],
)
perturbed_lhs = pole_sym / 64 - sum(
    a * row / 64 for a, (_label, row) in zip(alpha, perturbed_rows)
)
perturbation_error = sp.factor(perturbed_lhs - 1)
assert perturbation_error != 0


# Incidence audit.  Before the hard-coded common-h3 map, the raw terminal pole
# row contains 17 Hc variables.  They close on exactly 17 of the 20 clean-room
# incidence pivots.  After the B1-linear obstruction is cancelled, its K2^2
# constant component has ten direct Hc variables and closes on eleven pivots;
# reducing those rows gives 64.  These establish dependency counts, not a
# serialized charged pre-major multiplier certificate.
K3_unreduced = E.build_K3(E.NT)
K2_unreduced, _lf, _lc, _viol = E.build_K2(K3_unreduced)
B1_unreduced, _used = E.build_B1(E.NT)
_KF0, KG_unreduced = E.build_KFKG(K2_unreduced, B1_unreduced)
pole_pre_incidence = E.split_z(
    branch.sub_series(KG_unreduced, 16).get(16, {}), branch.zvar
).get(0, {})
direct_h = sorted(v for v in vars_of(pole_pre_incidence) if v.startswith("Hc_"))
step_by_h = {step["variable"]: step for step in incidence.steps}
pending = list(direct_h)
incidence_variables = set()
while pending:
    variable = pending.pop()
    if variable in incidence_variables or variable not in step_by_h:
        continue
    incidence_variables.add(variable)
    pending.extend(v for v in step_by_h[variable]["rhs_variables"]
                   if v.startswith("Hc_"))
incidence_labels = [step_by_h[v]["label"] for v in sorted(incidence_variables)]
assert len(incidence_labels) == 17
assert "Hc_11_0" not in incidence_variables

K2sq_unreduced = E.tmul(K2_unreduced, K2_unreduced, E.NT)
constant_pre_incidence = E.split_z(
    branch.sub_series(K2sq_unreduced, 16).get(16, {}), branch.zvar
).get(0, {})
constant_direct_h = sorted(
    v for v in vars_of(constant_pre_incidence) if v.startswith("Hc_")
)
pending = list(constant_direct_h)
constant_incidence_variables = set()
while pending:
    variable = pending.pop()
    if variable in constant_incidence_variables or variable not in step_by_h:
        continue
    constant_incidence_variables.add(variable)
    pending.extend(v for v in step_by_h[variable]["rhs_variables"]
                   if v.startswith("Hc_"))
constant_incidence_labels = [
    step_by_h[v]["label"] for v in sorted(constant_incidence_variables)
]
assert len(constant_direct_h) == 10
assert len(constant_incidence_labels) == 11
assert len(constant_pre_incidence) == 230
assert as_const(incidence.reduce(constant_pre_incidence)) == Fr(64)
assert "Hc_11_0" not in constant_incidence_variables


# The seven h2-D1 pivot variables are absent from the terminal/Jacobian core.
h2_pivots = {
    "K2c_11_16", "K2c_15_13", "K2c_19_10", "K2c_23_7",
    "K2c_27_4", "K2c_10_17", "K2c_14_14",
}
core_symbols = set(pole_sym.free_symbols)
for _label, row in all_rows:
    core_symbols.update(row.free_symbols)
assert not h2_pivots.intersection(map(str, core_symbols))

# No live A2/A3/B2 coefficient or T2/T3 bridge row is present post-D2.
assert not any(str(x).startswith(("A2c_", "A3c_", "B2c_"))
               for x in core_symbols)
assert not any("T2" in label or "T3" in label
               for label, _row in all_rows)

# Exact size of the source-forced D2 coordinate projector.  This is a global
# prerequisite count.  The charged artifacts do not retain the multipliers
# needed to identify a support-minimal subset in a literal pre-D2 certificate.
d2_specs = {
    "A2": (65, 189), "A3": (98, 285),
    "B1": (32, 93), "B2": (65, 189),
}
d2_deleted = {}
for block, (degree, threshold) in d2_specs.items():
    positions = [
        (r, q)
        for r in range(degree + 1)
        for q in range(min(32, degree - r) + 1)
    ]
    d2_deleted[block] = sum(3 * r + 4 * q < threshold
                            for r, q in positions)
assert d2_deleted == {"A2": 1386, "A3": 2442,
                      "B1": 384, "B2": 1386}
assert sum(d2_deleted.values()) == 5598


# c != 0 is explicit but has coefficient zero in the raw unit certificate.
c = sym["c"]
Zc = sp.Symbol("Zc")
localization_row = Zc * c - 1
assert sp.expand(certificate_lhs + 0 * localization_row - 1) == 0


result = {
    "branch": "delta52",
    "terminal": {
        "label": "stage8_G_local16_coord0",
        "local_power": 16,
        "deepest_t_power_in_terminal_construction": 8,
        "normal_form": "64",
    },
    "mechanical_backward_DAG": {
        "post_major_post_outer_D1": {
            "pole_rows": 1,
            "Jacobian_pivot_rows": 35,
            "Jacobian_stages": [1, 2, 3, 4],
            "deepest_Jacobian_t_power": 4,
            "total_source_rows": 36,
        },
        "outer_D1_path_lift": {
            "engine_pivot_rows_touched": 8,
            "engine_pivot_rows_are_audited_prerequisites_not_all_ancestors": True,
            "reduced_pivot_DAG_rows": len(d1_reduced_dag_labels),
            "reduced_pivot_DAG_labels": sorted(d1_reduced_dag_labels),
            "support_minimal_rows_for_B1c_3_21_zero": 7,
            "support_labels": [f"B1_D1_s0_k{k}" for k in range(1, 8)],
            "B1c_3_21_step": {
                "row": "B1_D1_s0_k6",
                "coefficient": "5103",
                "rhs": "-B1c_7_18/7",
            },
            "B1c_7_18_step": {
                "row": "B1_D1_s0_k7",
                "coefficient": "-2187/7",
                "rhs": "0",
            },
        },
        "incidence_dependency_audit": {
            "raw_terminal": {
                "direct_Hc_variables": len(direct_h),
                "recursive_incidence_pivots": len(incidence_labels),
                "labels": incidence_labels,
            },
            "K2_squared_constant_component_after_B1_cancellation": {
                "pre_reduction_terms": len(constant_pre_incidence),
                "direct_Hc_variables": len(constant_direct_h),
                "recursive_incidence_pivots": len(constant_incidence_labels),
                "labels": constant_incidence_labels,
                "normal_form": "64",
            },
            "literal_pre_major_multipliers_serialized": False,
        },
        "terminal_B1_coordinate_counts": {
            "raw_post_D2_before_outer_D1": len(raw_pole_b1),
            "after_outer_D1": len(post_d1_pole_b1),
        },
        "h2_D1_rows_touched": 0,
        "new_stage8_Jacobian_pivots_touched": 0,
        "T2_T3_bridge_rows_touched": 0,
    },
    "support_minimal_post_D2_certificate": {
        "row_count": len(certificate),
        "family_counts": {"pole": 1, "Jacobian": 6, "outer": 0,
                          "incidence": 0, "localization": 0},
        "schur_complement": str(schur),
        "identity_coefficients": {label: str(value)
                                  for label, value in certificate},
        "unique_in_43_row_B1_linear_core": True,
    },
    "outer_test": {
        "live_A2_A3_B2_coefficients": False,
        "outer_D2_onsets": {"A2": 21, "A3": 53, "B2": 21},
        "global_D2_zero_fact_count": sum(d2_deleted.values()),
        "global_D2_zero_facts_by_family": d2_deleted,
        "support_minimal_D2_zero_facts_for_this_certificate":
            "OPEN[PRE-D2-MULTIPLIER-LIFT-NOT-SERIALIZED]",
        "fully_lifted_pre_D2_multiplier_certificate": "OPEN[NOT-SERIALIZED]",
    },
    "localization": {
        "ring": "Q[core variables,c,Zc]",
        "nonvanishing": "c != 0",
        "wrapper": str(localization_row),
        "wrapper_multiplier_in_certificate": "0",
        "J0_factor": "NOT-PRESENT-IN-THIS-(99,66)-BRANCH-RING",
    },
    "negative_control": {
        "perturbed_row": "stage4_J_d159_k35 += B1c_3_22",
        "old_certificate_error": str(perturbation_error),
        "passes": True,
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
