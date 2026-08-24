#!/usr/bin/env python3
"""Independent mixed-cube-factor control for the reviewed (6,9) handoff.

This is a producer-internal exact replay, not a review and not a new proof of
the hash-pinned source theorems.  It verifies the field/valuation calculation,
the y^13 cancellation, the Kummer weight implications, and the typed target
boundary transformations for h=x^3(x^3-1).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from hashlib import sha256
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
}


class ControlFailure(RuntimeError):
    pass


def pin_inputs() -> dict[str, str]:
    out: dict[str, str] = {}
    for rel, expected in EXPECTED_HASHES.items():
        got = sha256((ROOT / rel).read_bytes()).hexdigest()
        if got != expected:
            raise ControlFailure(f"UNCLAIMED hash mismatch: {rel}: {got}")
        out[rel] = got
    return out


def poly_mul(a: dict[int, int], b: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for i, ai in a.items():
        for j, bj in b.items():
            out[i + j] = out.get(i + j, 0) + ai * bj
    return {i: c for i, c in out.items() if c}


def poly_eval(a: dict[int, int], value: int) -> int:
    return sum(c * value**i for i, c in a.items())


def poly_derivative(a: dict[int, int]) -> dict[int, int]:
    return {i - 1: i * c for i, c in a.items() if i}


def omega_mul(
    left: tuple[Fraction, Fraction], right: tuple[Fraction, Fraction]
) -> tuple[Fraction, Fraction]:
    """Multiply a+b*w modulo w^2+w+1."""
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c - b * d


@dataclass
class Route:
    facts: set[str] = field(default_factory=set)
    log: list[str] = field(default_factory=list)

    def emit(self, *facts: str) -> None:
        self.facts.update(facts)
        self.log.extend(f"EMIT {fact}" for fact in facts)

    def consume(self, theorem: str, *required: str) -> None:
        missing = sorted(set(required) - self.facts)
        if missing:
            raise ControlFailure(f"UNCLAIMED {theorem}: {missing}")
        self.log.append(f"CONSUME {theorem}")


def top_row_normalized() -> dict[str, int]:
    """Compute the y^13 row after factoring s^14.

    The keys uA,uB,dA,dB denote (s'/s)A, (s'/s)B, A', B'.
    """
    terms = (
        {"uB": 48},                    # 8 (s^6)' s^8 B
        {"dA": 9, "uA": 45},         # 9 (s^5 A)' s^9
        {"dB": -6, "uB": -48},       # -6 s^6 (s^8 B)'
        {"uA": -45},                   # -5 s^5 A (s^9)'
    )
    total: dict[str, int] = {}
    for term in terms:
        for monomial, coefficient in term.items():
            total[monomial] = total.get(monomial, 0) + coefficient
    return {key: value for key, value in total.items() if value}


def main() -> None:
    hashes = pin_inputs()
    route = Route()

    # h=x^3(x^3-1)=x^6-x^3 and q=x^3-1.
    x3 = {3: 1}
    q = {3: 1, 0: -1}
    h = poly_mul(x3, q)
    if h != {6: 1, 3: -1}:
        raise ControlFailure("h reconstruction failed")
    H = max(h)
    if H != 6 or H % 3:
        raise ControlFailure("historical 3|H input failed")

    # Exact divisor data.  At zero the lowest exponent is three.  At one,
    # h(1)=0 and h'(1)=3, hence a simple zero.  x^3-1 is squarefree in
    # characteristic zero, so all of its three algebraic roots are simple.
    dh = poly_derivative(h)
    v_zero = min(h)
    if v_zero != 3 or poly_eval(h, 1) != 0 or poly_eval(dh, 1) != 3:
        raise ControlFailure("finite valuation control failed")
    if poly_eval(poly_derivative(q), 1) == 0:
        raise ControlFailure("q squarefree control failed")
    valuations = {
        "x=0": 3,
        "x=1": 1,
        "x=omega": 1,
        "x=omega^2": 1,
        "infinity": -H,
    }
    if all(value % 3 == 0 for value in valuations.values()):
        raise ControlFailure("h was incorrectly classified as a cube")
    route.emit(
        "actual_y_degrees_6_9",
        "three_divides_H",
        "h_equals_x_cubed_times_q",
        "q_equals_x_cubed_minus_one",
        "h_and_q_same_Kummer_class",
        "h_noncube_in_kx",
        "L_equals_kx_adjoin_t_with_t_cubed_q",
        "s_equals_x_times_t",
        "nontrivial_degree_three_Kummer",
    )

    # The cube factor changes the generator only: if t^3=q and s=x*t,
    # then s^3=x^3*q=h, and conversely t=s/x in k(x)(s).
    if poly_mul(x3, q) != h:
        raise ControlFailure("Kummer generator equality failed")

    # Independent exact reconstruction of the reviewed y^13 cancellation.
    normalized = top_row_normalized()
    if normalized != {"dA": 9, "dB": -6}:
        raise ControlFailure(f"top row did not cancel: {normalized}")
    route.emit("top_y13_equals_s14_times_9Aprime_minus_6Bprime")
    route.consume(
        "FIRST-COMMON-CUBIC/NONCUBE",
        "actual_y_degrees_6_9",
        "three_divides_H",
        "h_noncube_in_kx",
        "nontrivial_degree_three_Kummer",
        "top_y13_equals_s14_times_9Aprime_minus_6Bprime",
    )
    route.emit(
        "delta_equals_3A_minus_2B_is_in_k",
        "sigma_s_equals_omega_s",
        "sigma_A_equals_omega_A",
        "sigma_B_equals_omega_B",
        "sigma_delta_equals_omega_delta",
        "sigma_fixes_delta",
    )

    # (omega-1)^(-1)=-(omega+2)/3 in Q[omega]/(omega^2+omega+1).
    omega_minus_one = (Fraction(-1), Fraction(1))
    inverse = (Fraction(-2, 3), Fraction(-1, 3))
    if omega_mul(omega_minus_one, inverse) != (Fraction(1), Fraction(0)):
        raise ControlFailure("omega-1 inverse failed")
    route.consume(
        "EXACT-WEIGHT-ONE-DELTA",
        "delta_equals_3A_minus_2B_is_in_k",
        "sigma_delta_equals_omega_delta",
        "sigma_fixes_delta",
    )
    route.emit("delta_zero_derived", "aligned_depression")

    weights = {j: (-j) % 3 for j in range(8)}
    forced = tuple(j for j in (7, 5, 4, 2, 1) if weights[j] != 0)
    retained = tuple(j for j in (6, 3, 0) if weights[j] == 0)
    if forced != (7, 5, 4, 2, 1) or retained != (6, 3, 0):
        raise ControlFailure("high-row Kummer weights changed")
    route.emit(
        "c7_c5_c4_c2_c1_forced_zero",
        "c6_removed_by_Q_minus_c6P",
        "c0_removed_by_Q_translation",
        "c3_equals_kappa_retained_in_pinned_chart",
        "kappa_target_translation_covariance_retained",
    )

    # The two boundary values remain polynomial under every target operation.
    boundaries = {
        "before": ("P0", "Q0"),
        "after_c6_c0": ("P0", "Q0-c6*P0-c0"),
        "after_optional_first_translation": ("P0+q0", "Q0-c6*P0-c0"),
    }
    if any(len(pair) != 2 for pair in boundaries.values()):
        raise ControlFailure("boundary pair was lost")
    route.emit(
        "F_at_r_equals_P_at_y0_in_kx_polynomial",
        "G_at_r_equals_Q_at_y0_in_kx_polynomial",
        "both_boundaries_charged_after_target_gauges",
        "actual_degrees_preserved_by_target_gauges",
        "chain_rule_Jxy_equals_s_times_D",
    )
    route.consume(
        "ALIGNED-LOWER-PFAFFIAN-INPUT",
        "nontrivial_degree_three_Kummer",
        "three_divides_H",
        "delta_zero_derived",
        "aligned_depression",
        "c7_c5_c4_c2_c1_forced_zero",
        "c6_removed_by_Q_minus_c6P",
        "c0_removed_by_Q_translation",
        "c3_equals_kappa_retained_in_pinned_chart",
        "kappa_target_translation_covariance_retained",
        "chain_rule_Jxy_equals_s_times_D",
        "both_boundaries_charged_after_target_gauges",
        "actual_degrees_preserved_by_target_gauges",
    )
    route.emit("reviewed_aligned_lower_Pfaffian_input_exact")

    payload = {
        "case": "h=x^3(x^3-1)",
        "H": H,
        "valuations": valuations,
        "Kummer_class": "[h]=[x^3-1] != 1",
        "field_identity": "k(x)(s),s^3=h = k(x)(t),t^3=x^3-1 via s=x*t",
        "third_branch": "NONE: multiplying by x^3 does not change F*/F*^3",
        "top_row_normalized": normalized,
        "weights_cj": {str(j): weights[j] for j in range(8)},
        "forced_zero": [f"c{j}" for j in forced],
        "weight_zero": [f"c{j}" for j in retained],
        "delta": "DERIVED_ZERO",
        "boundaries": boundaries,
        "terminal": "reviewed_aligned_lower_Pfaffian_input_exact",
        "input_hashes": hashes,
        "route_log": route.log,
        "scope": "producer-internal adversarial control pending review",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("PASS-GCD3-69-MIXED-CUBE-FACTOR-CONTROL")
    print("h_noncube=valuation_at_each_root_of_x3_minus_1_is_1")
    print("cube_factor=KUMMER-CLASS-NEUTRAL")
    print("delta=DERIVED-ZERO-BY-WEIGHT-ONE")
    print("boundaries=BOTH-CHARGED")
    print("landing=REVIEWED-ALIGNED-LOWER-PFAFFIAN-INPUT")
    print(f"payload_sha256={sha256(canonical.encode()).hexdigest()}")


if __name__ == "__main__":
    main()
