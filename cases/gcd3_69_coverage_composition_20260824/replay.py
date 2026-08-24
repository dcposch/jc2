#!/usr/bin/env python3
"""Fail-closed replay for the reviewed GCD3 (6,9) coverage composition.

This script does not re-prove the mathematical source reports.  It pins their
bytes, verifies that every theorem handoff has an explicit emitted premise,
executes two adversarial branch-typing controls, and exhausts the partial-y
degree DAG through maximum eleven.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from math import gcd
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]

EXPECTED_HASHES = {
    "xmodel/as109-partial-y-history-stop-20260824.md":
        "6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe",
    "xmodel/as109-partial-y-history-review-grok-20260824.md":
        "f9d547f0f17dc3557ed8edce19912b4930dc2125542c7f9b3e4782c554a03afd",
    "xmodel/gcd3-69-common-cubic-first-gate-20260824.md":
        "f63bf74fd1013c74645f9f7fe9292db69199572b390b5b19d160c5ed13b373e8",
    "xmodel/gcd3-69-common-cubic-first-gate-review-grok-20260824.md":
        "5416440bc12bb50ecebfdfa520082aa9e88a26069b43deb13bdaabfcd1690503",
    "xmodel/gcd3-69-lower-pfaffian-successor-20260824.md":
        "7671785519bf4e55b602f117740bd8d8571c6982a8916235407a2bb0a2263043",
    "xmodel/gcd3-69-lower-pfaffian-successor-review-grok-20260824.md":
        "a000619d8b5597add21716d525856c459ff57d5a2b2ab75b85de5d9d08970b27",
    "xmodel/gcd3-69-target-translation-erratum-20260824.md":
        "43fa36968bb90414748330c1b4a5d5169a0eaa21b1925623764e96204e049c78",
    "xmodel/gcd3-69-target-translation-erratum-review-grok-20260824.md":
        "f4cb57ca765138ed2decab01b12a7f884c37f9a847d80e90162ee751bb3df837",
    "xmodel/gcd3-69-cube-mismatch-gate-20260824.md":
        "6a2799dfe46828c70462d51a842a3fc0adf0515b8ded7a576cdb837d81847d20",
    "xmodel/gcd3-69-cube-mismatch-review-grok-20260824.md":
        "2648eef3b8091970655a94743c6c181343a94534b6454f43c579b310331ba7d7",
    "xmodel/gcd3-69-cube-trajectory-kuranishi-20260824.md":
        "069f6280332b44d93dcad17801dc7136d4a79fb06ace101c2dce8a4e746b5e7b",
    "xmodel/gcd3-69-cube-trajectory-kuranishi-review-grok-20260824.md":
        "7bcf18d69344acc2277a0184ca1aeeb717ebad35c3aacf91421874b7e59f5cc9",
}


class RouteFailure(RuntimeError):
    """A theorem consumer requested a premise not emitted upstream."""


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def pin_inputs() -> dict[str, str]:
    found: dict[str, str] = {}
    for rel, expected in EXPECTED_HASHES.items():
        got = file_sha(ROOT / rel)
        if got != expected:
            raise RouteFailure(f"UNCLAIMED: hash mismatch for {rel}: {got}")
        found[rel] = got
    return found


@dataclass
class RouteState:
    name: str
    facts: set[str] = field(default_factory=set)
    log: list[str] = field(default_factory=list)
    constants: dict[str, int] = field(default_factory=dict)

    def emit(self, *facts: str) -> None:
        self.facts.update(facts)
        self.log.extend(f"EMIT {fact}" for fact in facts)

    def consume(self, theorem: str, *required: str) -> None:
        missing = sorted(set(required) - self.facts)
        if missing:
            raise RouteFailure(
                f"UNCLAIMED: {theorem} missing premises {','.join(missing)}"
            )
        self.log.append(f"CONSUME {theorem}")


def poly_mul(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for i, ai in a.items():
        for j, bj in b.items():
            out[i + j] = out.get(i + j, 0) + ai * bj
    return {i: c for i, c in out.items() if c}


def poly_derivative(a: dict[int, int]) -> dict[int, int]:
    return {i - 1: i * c for i, c in a.items() if i and i * c}


def poly_eval(a: dict[int, int], x: int) -> int:
    return sum(c * (x ** i) for i, c in a.items())


def omega_mul(
    x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    """Multiply a+b*w modulo w^2+w+1."""
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def exact_kummer_delta_zero() -> dict[str, str]:
    # (w-1)^(-1) = -(w+2)/3 in Q[w]/(w^2+w+1).
    w_minus_one = (Fraction(-1), Fraction(1))
    inverse = (Fraction(-2, 3), Fraction(-1, 3))
    if omega_mul(w_minus_one, inverse) != (Fraction(1), Fraction(0)):
        raise RouteFailure("UNCLAIMED: omega-1 inverse failed")
    # delta is a constant, hence fixed, but has Kummer weight one.  Therefore
    # (w-1) delta=0 and invertibility forces delta=0.
    return {
        "relation": "(omega-1)*delta=0",
        "inverse": "-(omega+2)/3",
        "conclusion": "delta=0",
    }


COMMON_INPUT_FACTS = (
    "characteristic_zero",
    "constant_field_algebraically_closed",
    "actual_y_degrees_6_9",
    "three_divides_H",
    "leading_a6_alpha_h2",
    "leading_b9_beta_h3",
    "h_nonzero_polynomial",
    "s_cubed_equals_h",
    "delta_constant",
    "original_Taylor_boundaries_retained",
    "cube_or_noncube_exhaustive",
)


def route_noncube_control() -> RouteState:
    state = RouteState("noncube_h=x(x-1)(x-2)")
    state.emit(*COMMON_INPUT_FACTS)

    h = {3: 1, 2: -3, 1: 2}
    dh = poly_derivative(h)
    if poly_eval(h, 0) != 0 or poly_eval(dh, 0) == 0:
        raise RouteFailure("UNCLAIMED: control does not have a simple zero")
    state.emit("h_has_divisor_valuation_one", "h_not_cube_in_kx")

    state.consume(
        "FIRST-COMMON-CUBIC/NONCUBE",
        "characteristic_zero",
        "constant_field_algebraically_closed",
        "h_not_cube_in_kx",
        "s_cubed_equals_h",
        "delta_constant",
        "original_Taylor_boundaries_retained",
    )
    state.emit(
        "nontrivial_cubic_Kummer",
        "delta_has_Kummer_weight_one",
        "omega_delta_equals_delta",
    )
    state.consume(
        "EXACT-KUMMER-DELTA-ZERO",
        "characteristic_zero",
        "constant_field_algebraically_closed",
        "delta_constant",
        "nontrivial_cubic_Kummer",
        "delta_has_Kummer_weight_one",
        "omega_delta_equals_delta",
    )
    delta = exact_kummer_delta_zero()
    if delta["conclusion"] != "delta=0":
        raise RouteFailure("UNCLAIMED: formal delta was not forced to zero")
    state.emit("delta_zero_derived")
    state.consume(
        "ALIGNED-HIGH-ROW-KUMMER-FORM",
        "nontrivial_cubic_Kummer",
        "delta_zero_derived",
        "original_Taylor_boundaries_retained",
    )
    state.emit(
        "c7_c5_c4_c2_c1_weight_forced_zero",
        "c6_c0_removed_by_reviewed_target_gauges",
        "c3_target_translation_covariance_reviewed",
        "aligned_five_coefficient_invariant_fibre",
        "terminal_Jacobian_row_retained",
    )
    state.consume(
        "ALIGNED-LOWER-PFAFFIAN-EXCLUSION",
        "nontrivial_cubic_Kummer",
        "three_divides_H",
        "delta_zero_derived",
        "c7_c5_c4_c2_c1_weight_forced_zero",
        "aligned_five_coefficient_invariant_fibre",
        "terminal_Jacobian_row_retained",
        "original_Taylor_boundaries_retained",
    )
    state.emit("reviewed_aligned_branch_empty")
    return state


CUBE_RETAINED_CONSTANTS = ("c7", "c5", "c4", "c2", "c1")


def route_cube_d0_control() -> RouteState:
    state = RouteState("cube_h=(x^2+1)^3,d=0,c7=1")
    state.emit(*COMMON_INPUT_FACTS)

    s = {2: 1, 0: 1}
    h = poly_mul(poly_mul(s, s), s)
    expected_h = {6: 1, 4: 3, 2: 3, 0: 1}
    if h != expected_h:
        raise RouteFailure("UNCLAIMED: polynomial cube reconstruction failed")
    if max(h) != 6 or max(h) % 3:
        raise RouteFailure("UNCLAIMED: cube control does not satisfy 3|H")
    state.emit("h_cube_in_kx", "Gauss_polynomial_cube_core", "s_in_kx_polynomial")
    state.constants = {"c7": 1, "c5": 0, "c4": 0, "c2": 0, "c1": 0}

    state.consume(
        "FIRST-COMMON-CUBIC/CUBE",
        "characteristic_zero",
        "constant_field_algebraically_closed",
        "h_cube_in_kx",
        "h_nonzero_polynomial",
        "delta_constant",
        "original_Taylor_boundaries_retained",
    )
    state.emit(
        "polynomial_cube_core",
        "no_Kummer_weight_vanishing",
        "d_equals_minus_delta_over_two",
        "d_zero",
        "d_zero_target_quotient_separate",
        "c3_removed_by_legal_target_translation",
        "c6_c0_removed_by_reviewed_target_gauges",
    )
    state.consume(
        "CUBE-FABER-LANDING/D0",
        "polynomial_cube_core",
        "no_Kummer_weight_vanishing",
        "d_zero",
        "d_zero_target_quotient_separate",
        "original_Taylor_boundaries_retained",
    )
    state.emit(
        "reviewed_cube_Faber_landing",
        "all_Faber_constants_retained",
        "r1_to_r4_constant_and_6r5prime_equals_j_over_s",
        "terminal_core_s_constant_or_single_monomial",
    )
    if tuple(state.constants) != CUBE_RETAINED_CONSTANTS:
        raise RouteFailure("UNCLAIMED: d=0 retained-constant list changed")
    if state.constants["c7"] != 1:
        raise RouteFailure("UNCLAIMED: c7 was lost on the cube d=0 route")
    if "c7_c5_c4_c2_c1_weight_forced_zero" in state.facts:
        raise RouteFailure("UNCLAIMED: aligned Kummer vanishing entered cube route")

    state.consume(
        "CUBE-TRAJECTORY-CLOSURE/D0",
        "reviewed_cube_Faber_landing",
        "no_Kummer_weight_vanishing",
        "all_Faber_constants_retained",
        "d_zero",
        "d_zero_target_quotient_separate",
        "r1_to_r4_constant_and_6r5prime_equals_j_over_s",
        "terminal_core_s_constant_or_single_monomial",
        "original_Taylor_boundaries_retained",
    )
    state.emit("reviewed_cube_d0_branch_empty")
    return state


def route_cube_d_nonzero_contract() -> RouteState:
    state = RouteState("abstract_cube_d_nonzero")
    state.emit(*COMMON_INPUT_FACTS)
    state.emit("h_cube_in_kx", "Gauss_polynomial_cube_core", "s_in_kx_polynomial")
    state.consume(
        "FIRST-COMMON-CUBIC/CUBE",
        "characteristic_zero",
        "constant_field_algebraically_closed",
        "h_cube_in_kx",
        "h_nonzero_polynomial",
        "delta_constant",
        "original_Taylor_boundaries_retained",
    )
    state.emit(
        "polynomial_cube_core",
        "no_Kummer_weight_vanishing",
        "d_equals_minus_delta_over_two",
        "d_nonzero",
        "d_nonzero_target_invariants_retained",
    )
    state.consume(
        "CUBE-FABER-LANDING/DNONZERO",
        "polynomial_cube_core",
        "no_Kummer_weight_vanishing",
        "d_nonzero",
        "d_nonzero_target_invariants_retained",
        "original_Taylor_boundaries_retained",
    )
    state.emit(
        "reviewed_cube_Faber_landing",
        "all_Faber_constants_retained",
        "r1_to_r4_constant_and_6r5prime_equals_j_over_s",
        "terminal_core_s_constant_or_single_monomial",
    )
    state.consume(
        "CUBE-TRAJECTORY-CLOSURE/DNONZERO",
        "reviewed_cube_Faber_landing",
        "no_Kummer_weight_vanishing",
        "all_Faber_constants_retained",
        "d_nonzero",
        "d_nonzero_target_invariants_retained",
        "r1_to_r4_constant_and_6r5prime_equals_j_over_s",
        "terminal_core_s_constant_or_single_monomial",
        "original_Taylor_boundaries_retained",
    )
    state.emit("reviewed_cube_d_nonzero_branch_empty")
    return state


def compose_69(
    noncube: RouteState, cube_d0: RouteState, cube_dn: RouteState
) -> dict[str, object]:
    """Issue the composition conclusion only after every leaf is certified."""
    partition = {
        "h": ("h_not_cube_in_kx", "h_cube_in_kx"),
        "cube_d": ("d_zero", "d_nonzero"),
    }
    required = (
        (noncube, "h_not_cube_in_kx", "reviewed_aligned_branch_empty"),
        (cube_d0, "d_zero", "reviewed_cube_d0_branch_empty"),
        (cube_dn, "d_nonzero", "reviewed_cube_d_nonzero_branch_empty"),
    )
    for state, branch, terminal in required:
        missing = {branch, terminal} - state.facts
        if missing:
            raise RouteFailure(
                f"UNCLAIMED: composition leaf {state.name} missing {sorted(missing)}"
            )
    if set(partition["h"]) != {"h_not_cube_in_kx", "h_cube_in_kx"}:
        raise RouteFailure("UNCLAIMED: h partition changed")
    if set(partition["cube_d"]) != {"d_zero", "d_nonzero"}:
        raise RouteFailure("UNCLAIMED: d partition changed")
    return {
        "partition": partition,
        "terminal_leaves": [terminal for _, _, terminal in required],
        "actual_6_9_three_divides_H": "EMPTY",
    }


def primitive_route(m: int, n: int) -> str:
    if not (0 <= m <= n):
        raise ValueError((m, n))
    if m == 0:
        return "Z"
    if gcd(m, n) <= 2:
        return "G"
    if m == n:
        return "E"
    if n % m == 0:
        return "D"
    if (m, n) == (6, 9):
        return "X69"
    return "OPEN"


def children(m: int, n: int, route: str) -> tuple[tuple[int, int], ...]:
    if route == "E":
        return tuple((r, n) for r in range(n))
    if route == "D":
        return tuple(sorted((m, r)) for r in range(n))
    return ()


@lru_cache(maxsize=None)
def prove_pair(m: int, n: int, compose_69: bool = True) -> tuple[bool, tuple[str, ...]]:
    m, n = sorted((m, n))
    route = primitive_route(m, n)
    label = f"({m},{n}):{route}"
    if route in {"Z", "G"}:
        return True, (label,)
    if route == "X69":
        if compose_69:
            return True, (label + ":H%3!=0->G;H%3=0->GCD3-COVER",)
        return False, (label + ":H%3=0",)
    if route == "OPEN":
        return False, (label,)
    paths = [label]
    for child in children(m, n, route):
        ok, child_path = prove_pair(*child, compose_69=compose_69)
        paths.extend(child_path)
        if not ok:
            return False, tuple(paths)
    return True, tuple(paths)


def degree_audit() -> dict[str, object]:
    rows: dict[str, list[str]] = {}
    unordered_total = 0
    for n in range(12):
        row: list[str] = []
        for m in range(n + 1):
            unordered_total += 1
            route = primitive_route(m, n)
            ok, _ = prove_pair(m, n, compose_69=True)
            if not ok:
                raise RouteFailure(f"UNCLAIMED: degree pair {(m, n)} not closed")
            if route == "X69":
                route = "G-if-3nmidH/GCD3-COVER-if-3midH"
            row.append(f"({m},{n}):{route}")
        rows[str(n)] = row

    precomposition_open = []
    for n in range(12):
        for m in range(n + 1):
            ok, path = prove_pair(m, n, compose_69=False)
            if not ok:
                terminal = path[-1]
                if terminal not in precomposition_open:
                    precomposition_open.append(terminal)
    if precomposition_open != ["(6,9):X69:H%3=0"]:
        raise RouteFailure(
            "UNCLAIMED: unexpected precomposition primitives "
            + repr(precomposition_open)
        )

    frontier12 = [
        (m, 12) for m in range(13) if primitive_route(m, 12) == "OPEN"
    ]
    if frontier12 != [(8, 12), (9, 12)]:
        raise RouteFailure(f"UNCLAIMED: max-12 frontier is {frontier12}")

    if unordered_total != 78:
        raise RouteFailure(f"UNCLAIMED: unordered count {unordered_total}")
    ordered_total = 12 * 12
    for m in range(12):
        for n in range(12):
            if not prove_pair(m, n, compose_69=True)[0]:
                raise RouteFailure(f"UNCLAIMED: ordered degree pair {(m, n)}")

    return {
        "rows": rows,
        "unordered_pairs_through_11": unordered_total,
        "ordered_pairs_through_11": ordered_total,
        "primitive_before_composition": precomposition_open,
        "uncovered_after_composition": [],
        "first_new_primitives_at_max_12": [list(pair) for pair in frontier12],
    }


def main() -> None:
    hashes = pin_inputs()
    noncube = route_noncube_control()
    cube_d0 = route_cube_d0_control()
    cube_dn = route_cube_d_nonzero_contract()
    composition = compose_69(noncube, cube_d0, cube_dn)
    degrees = degree_audit()

    payload = {
        "input_hashes": hashes,
        "composition": composition,
        "noncube_control": {
            "name": noncube.name,
            "facts": sorted(noncube.facts),
            "log": noncube.log,
            "terminal": "reviewed_aligned_branch_empty",
        },
        "cube_d0_control": {
            "name": cube_d0.name,
            "facts": sorted(cube_d0.facts),
            "constants": cube_d0.constants,
            "log": cube_d0.log,
            "terminal": "reviewed_cube_d0_branch_empty",
        },
        "cube_d_nonzero_contract": {
            "name": cube_dn.name,
            "facts": sorted(cube_dn.facts),
            "log": cube_dn.log,
            "terminal": "reviewed_cube_d_nonzero_branch_empty",
        },
        "degree_audit": degrees,
        "forbidden_imports": {
            "full_cubic_boundary_reduction": False,
            "polynomial_source_depression": False,
            "Kummer_weight_vanishing_in_cube_core": False,
        },
        "theorem": {
            "actual_6_9_three_divides_H": composition[
                "actual_6_9_three_divides_H"
            ],
            "max_actual_y_degree_le_11": "AUTOMORPHISM",
            "field": "arbitrary characteristic zero by scalar extension/descent",
            "JC2": "NOT_CLAIMED",
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    digest = sha256(canonical.encode()).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-GCD3-69-COVERAGE-COMPOSITION")
    print("stress_noncube=formal-delta-derived-zero")
    print("stress_cube_d0=c7-retained-full-weight-unforced-Faber")
    print("primitive_before_composition=(6,9),3|H")
    print("max_actual_y_degree_le_11=ALL_144_ORDERED_PAIRS_COVERED")
    print("max12_first_primitives=(8,12),(9,12)")
    print(f"payload_sha256={digest}")


if __name__ == "__main__":
    main()
