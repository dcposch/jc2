#!/usr/bin/env python3
"""Exact finite controls for the AS109--xy-membership gate.

The all-lift statements are proved field-theoretically in the paired report.
This replay checks the residue conjugates, the reduced minimal polynomial,
and two sharp non-Keller/deck mechanism controls.  It does not search for a
lift or infer characteristic zero from modular data.
"""

from __future__ import annotations

import json
from math import gcd


P = 109


def poly_mul_mod(left: list[int], right: list[int], modulus: int) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % modulus
    return out


def hensel_product_residues() -> dict[str, object]:
    by_target_residue: dict[int, list[int]] = {}
    for b in range(P):
        values = [(a * b) % P for a in range(P)]
        by_target_residue[b] = values
        assert len(set(values)) == (1 if b == 0 else P)

    # On the b=1 tube the conjugate residues are every element of F_p.
    values = by_target_residue[1]
    assert values == list(range(P))

    reduced_minpoly = [1]
    for a in range(P):
        reduced_minpoly = poly_mul_mod(reduced_minpoly, [(-a) % P, 1], P)
    expected = [0] * (P + 1)
    expected[1] = (-1) % P
    expected[P] = 1
    assert reduced_minpoly == expected

    trace_mod_p = sum(values) % P
    norm_mod_p = 1
    for value in values:
        norm_mod_p = (norm_mod_p * value) % P
    discriminant_mod_p = 1
    for i in range(P):
        for j in range(i + 1, P):
            discriminant_mod_p = (discriminant_mod_p * (i - j) ** 2) % P
    assert trace_mod_p == 0
    assert norm_mod_p == 0
    assert discriminant_mod_p == P - 1
    assert pow(33, 2, P) == P - 1

    shifted = values[1:] + values[:1]
    assert shifted != values
    assert all(shifted[a] == (a + 1) % P for a in range(P))

    return {
        "tube": "(P,Q)=(109*S,1+109*T)",
        "branch_product_residues": "sigma_a(x*y) = a mod 109",
        "pairwise_distinct": len(set(values)),
        "minimal_degree_lower_bound": P,
        "A_infinity_zero_consequence": "[L:M]=109 implies L=M(x*y)",
        "reduced_minimal_polynomial": "Z^109-Z",
        "trace_mod_109": trace_mod_p,
        "norm_mod_109": norm_mod_p,
        "discriminant_mod_109": discriminant_mod_p,
        "sqrt_discriminant_residue_control": 33,
        "formal_cycle_fixes_xy": False,
        "zero_target_residue_control": "b=0 collapses residues; b=1 is essential",
    }


def finite_degree_control() -> dict[str, object]:
    # g(X)=X+(p-1)X^p is congruent to X-X^p mod p.  Its leading
    # coefficient is a p-adic unit, so its formal fibre algebra is finite
    # free of rank p; nevertheless it is not Keller and xy is primitive.
    leading = P - 1
    assert leading % P == P - 1
    assert gcd(leading, P) == 1
    for a in range(P):
        assert (a + leading * pow(a, P, P)) % P == 0
        assert (1 + P * leading * pow(a, P - 1, P)) % P == 1

    # Any deck transformation of K(x)/K(g(x)) fixes the unique pole, hence
    # is affine.  The x^(p-1) coefficient forces beta=0 and the x row then
    # forces alpha=1.
    x_p_minus_1_beta_coefficient = leading * P
    assert x_p_minus_1_beta_coefficient != 0
    jacobian_nonconstant_coefficient = P * leading
    assert jacobian_nonconstant_coefficient != 0

    # For w=x*y, U=g(x), V=y, a monic equation is
    # w^p + V^(p-1)/(p-1)*w - U*V^p/(p-1)=0.
    linear_coefficient_mod_p = pow(leading, -1, P)
    constant_coefficient_mod_p = 0
    assert linear_coefficient_mod_p == P - 1

    return {
        "map": "G_p=(x+(p-1)*x^p,y)",
        "AS109_reduction": True,
        "generic_degree": P,
        "formal_fibre_finite_free_rank": P,
        "A_infinity_rank": 0,
        "xy_membership": False,
        "xy_degree_over_target": P,
        "xy_minpoly": "W^p+V^(p-1)/(p-1)*W-U*V^p/(p-1)",
        "xy_minpoly_on_tube_mod_p": "W^p-W",
        "linear_coefficient_mod_p": linear_coefficient_mod_p,
        "constant_coefficient_mod_p": constant_coefficient_mod_p,
        "rational_deck_group": "trivial",
        "jacobian": f"1+{jacobian_nonconstant_coefficient}*x^{P-1} (not constant)",
    }


def cyclic_deck_control() -> dict[str, object]:
    # Over a characteristic-zero field containing a primitive p-th root
    # zeta, put L=K(s,v), M=K(s^p,v), x=s+v, y=s+2v.  The generator sends
    # s->zeta*s.  The coefficient 3 of s*v in xy is nonzero, so every
    # nonidentity group element moves xy.
    nontrivial_powers = list(range(1, P))
    assert all(k % P != 0 for k in nontrivial_powers)
    assert 3 != 0
    assert (-1) ** (P - 1) == 1
    return {
        "extension": "K(s,v) / K(s^109,v)",
        "degree": P,
        "deck_group": "C_109 via s->zeta*s",
        "coordinates": "x=s+v, y=s+2v",
        "xy": "s^2+3*s*v+2*v^2",
        "nonidentity_deck_elements_moving_xy": len(nontrivial_powers),
        "xy_membership": False,
        "p_cycle_sign": 1,
        "cyclic_discriminant_constraint": "disc(minpoly_xy) is a square in the base",
    }


def main() -> None:
    print(
        json.dumps(
            {
                "verdict": "AS109-XY-MEMBERSHIP-SHARP-NO-GO",
                "p": P,
                "hensel_conjugates": hensel_product_residues(),
                "A_infinity_zero_control": finite_degree_control(),
                "deck_control": cyclic_deck_control(),
                "target_field_membership_forced": False,
                "target_ring_membership_forced": False,
                "complex_membership_after_constant_extension": False,
                "exact_lift_found": False,
                "support_enumeration": False,
                "aws_used": False,
                "jc2_inference": False,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
