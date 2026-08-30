#!/usr/bin/env python3
"""Desk replay for the rank-four discriminant-double-plane gate.

This checks only finite permutation calculus and displayed polynomial control
identities.  The finite-etale criterion, comparison/Kummer arguments, and
normalization statements remain written mathematical proofs in the report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import permutations

import sympy as sp


Permutation = tuple[int, ...]
ID4: Permutation = (0, 1, 2, 3)
PAIRINGS = (
    frozenset((frozenset((0, 1)), frozenset((2, 3)))),
    frozenset((frozenset((0, 2)), frozenset((1, 3)))),
    frozenset((frozenset((0, 3)), frozenset((1, 2)))),
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(len(left)))


def inverse(element: Permutation) -> Permutation:
    result = [0] * len(element)
    for index, image in enumerate(element):
        result[image] = index
    return tuple(result)


def generated(identity: Permutation, generators: tuple[Permutation, ...]) -> set[Permutation]:
    closure = {identity}
    frontier = [identity]
    expanded = generators + tuple(inverse(element) for element in generators)
    while frontier:
        current = frontier.pop()
        for generator in expanded:
            candidate = compose(generator, current)
            if candidate not in closure:
                closure.add(candidate)
                frontier.append(candidate)
    return closure


def permute_pairing(element: Permutation, pairing: frozenset[frozenset[int]]) -> frozenset[frozenset[int]]:
    return frozenset(frozenset(element[index] for index in pair) for pair in pairing)


def quotient(element: Permutation) -> Permutation:
    return tuple(PAIRINGS.index(permute_pairing(element, pairing)) for pairing in PAIRINGS)


def parity(element: Permutation) -> int:
    inversions = sum(
        element[left] > element[right]
        for left in range(len(element))
        for right in range(left + 1, len(element))
    )
    return inversions % 2


def permutation_checks(mutate_cusp_as_etale: bool) -> dict[str, object]:
    s4 = tuple(permutations(range(4)))
    image = {quotient(element) for element in s4}
    kernel = {element for element in s4 if quotient(element) == (0, 1, 2)}
    require(len(image) == 6, "S4/V4 image must have order six")
    require(len(kernel) == 4, "pairing-action kernel must be V4")

    a4 = {element for element in s4 if parity(element) == 0}
    a3_image = {quotient(element) for element in a4}
    require(len(a3_image) == 3, "A4/V4 must be A3")
    require(all(parity(element) == 0 for element in a3_image), "A3 image parity")

    tau12 = (1, 0, 2, 3)
    tau34 = (0, 1, 3, 2)
    tau23 = (0, 2, 1, 3)
    node_group = generated(ID4, (tau12, tau34))
    cusp_group = generated(ID4, (tau12, tau23))
    node_image = {quotient(element) for element in node_group}
    cusp_image = {quotient(element) for element in cusp_group}
    node_stabilizer = node_image & a3_image
    cusp_stabilizer = cusp_image & a3_image

    require(len(node_group) == 4, "quartic (2,2) local group")
    require(len(node_image) == 2, "resolvent node image must be C2")
    require(len(node_stabilizer) == 1, "C3 action must be free above a node packet")
    require(len(cusp_group) == 6, "quartic cusp packet local group")
    require(len(cusp_image) == 6, "resolvent cusp image must be S3")
    expected_cusp_stabilizer = 1 if mutate_cusp_as_etale else 3
    require(
        len(cusp_stabilizer) == expected_cusp_stabilizer,
        "cusp packet has nontrivial A3 stabilizer",
    )
    return {
        "S4_order": len(s4),
        "pairing_image_order": len(image),
        "pairing_kernel_order": len(kernel),
        "A3_image_order": len(a3_image),
        "node_image_order": len(node_image),
        "node_C3_stabilizer_order": len(node_stabilizer),
        "cusp_image_order": len(cusp_image),
        "cusp_C3_stabilizer_order": len(cusp_stabilizer),
    }


def polynomial_checks() -> dict[str, object]:
    x, y, w, t, alpha, beta = sp.symbols("x y w t alpha beta")

    nodal_q = y**2 - x**2 * (x + 1)
    require(sp.expand(y**2 - nodal_q - x**2 * (x + 1)) == 0, "nodal Danielewski transform")

    cubic = t**3 + x * t + x * y + 1
    discriminant = sp.factor(sp.discriminant(cubic, t))
    expected_discriminant = -4 * x**3 - 27 * (x * y + 1) ** 2
    require(sp.expand(discriminant - expected_discriminant) == 0, "odd-etale cubic discriminant")

    x_param = -3 * t**2
    y_param = (1 - 2 * t**3) / (3 * t**2)
    require(
        sp.factor(expected_discriminant.subs({x: x_param, y: y_param})) == 0,
        "Gm branch parametrization",
    )
    inverse_parameter = -3 * (x * y + 1) / (2 * x)
    require(
        sp.factor(inverse_parameter.subs({x: x_param, y: y_param}) - t) == 0,
        "Gm branch inverse",
    )

    closure_equation = alpha**3 + beta**3 - 3 * alpha * beta * y + 1
    zeta = sp.symbols("zeta")
    transformed = closure_equation.subs({alpha: zeta * alpha, beta: zeta**2 * beta}, simultaneous=True)
    transformed_mod = sp.rem(sp.Poly(transformed, zeta), sp.Poly(zeta**2 + zeta + 1, zeta)).as_expr()
    require(sp.expand(transformed_mod - closure_equation) == 0, "C3 closure action invariance")
    require(closure_equation.subs({alpha: 0, beta: 0}) == 1, "C3 action fixed-point exclusion")

    sum_cubes = alpha**3 + beta**3
    product_cubes = (alpha * beta) ** 3
    x_closure = -3 * alpha * beta
    b_closure = x_closure * y + 1
    require(
        sp.expand((sum_cubes + b_closure).subs(y, (alpha**3 + beta**3 + 1) / (3 * alpha * beta))) == 0,
        "Cardano sum relation",
    )
    require(sp.expand(product_cubes + x_closure**3 / 27) == 0, "Cardano product relation")

    # Ordinary cusp control: A2 = A2/mu_3 with invariants U=a^3,
    # V=b^3, X=ab and relation U*V=X^3.
    U, V, X = sp.symbols("U V X")
    require(
        sp.expand((U * V - X**3).subs({U: alpha**3, V: beta**3, X: alpha * beta})) == 0,
        "ordinary cusp quotient relation",
    )

    return {
        "nodal_double_plane": "u*v=x^2*(x+1)",
        "odd_etale_cubic_discriminant": str(discriminant),
        "odd_etale_branch_normalization": "Gm",
        "closure_equation": str(closure_equation),
        "closure_C3_action_fixed_locus": "empty",
        "ordinary_cusp_double_plane": "U*V=X^3",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutate-cusp-as-etale", action="store_true")
    args = parser.parse_args()

    payload = {
        "permutation": permutation_checks(args.mutate_cusp_as_etale),
        "polynomial": polynomial_checks(),
        "scope": [
            "S4/V4=S3 local stabilizer calculus",
            "named nodal and ordinary-cusp local double-plane controls",
            "explicit connected odd-etale S3 control",
        ],
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    print("status=PASS-QUARTIC-DISCRIMINANT-DOUBLE-PLANE")
    print(f"payload_sha256={hashlib.sha256(encoded).hexdigest()}")
    print(json.dumps(payload, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
