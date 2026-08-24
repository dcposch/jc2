#!/usr/bin/env python3
"""Exact producer for the preregistered AS3-MIN-W2 cap.

No external CAS is used.  Sparse bivariate polynomials are dictionaries
``(x_exponent, y_exponent) -> integer coefficient``.  Special-fibre
identities are checked coefficientwise modulo 3, and the emitted lift is
checked coefficientwise modulo 9.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


Mon = Tuple[int, int]
Poly = Dict[Mon, int]
ROOT = Path(__file__).resolve().parents[2]
CAP_DIR = Path(__file__).resolve().parent


def clean(poly: Poly) -> Poly:
    return {mon: coefficient for mon, coefficient in poly.items() if coefficient}


def add(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for mon, coefficient in right.items():
        out[mon] = out.get(mon, 0) + coefficient
    return clean(out)


def scale(poly: Poly, scalar: int) -> Poly:
    return clean({mon: scalar * coefficient for mon, coefficient in poly.items()})


def multiply(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for (i, j), coefficient in left.items():
        for (u, v), value in right.items():
            mon = (i + u, j + v)
            out[mon] = out.get(mon, 0) + coefficient * value
    return clean(out)


def derivative(poly: Poly, variable: int) -> Poly:
    out: Poly = {}
    for (i, j), coefficient in poly.items():
        exponent = (i, j)[variable]
        if exponent:
            mon = (i - 1, j) if variable == 0 else (i, j - 1)
            out[mon] = out.get(mon, 0) + coefficient * exponent
    return clean(out)


def bracket(left: Poly, right: Poly) -> Poly:
    return add(multiply(derivative(left, 0), derivative(right, 1)),
               scale(multiply(derivative(left, 1), derivative(right, 0)), -1))


def reduce_poly(poly: Poly, modulus: int) -> Poly:
    return {mon: coefficient % modulus for mon, coefficient in poly.items()
            if coefficient % modulus}


def evaluate(poly: Poly, point: Sequence[int], modulus: int) -> int:
    x, y = point
    return sum(coefficient * pow(x, i) * pow(y, j)
               for (i, j), coefficient in poly.items()) % modulus


def encode_poly(poly: Poly, modulus: int | None = None) -> List[List[int]]:
    rows = []
    for (i, j), coefficient in sorted(poly.items()):
        value = coefficient if modulus is None else coefficient % modulus
        if value:
            rows.append([i, j, value])
    return rows


def teichmueller(residue: int, prime: int) -> int:
    modulus = prime * prime
    roots = [value for value in range(modulus)
             if value % prime == residue % prime
             and (pow(value, prime, modulus) - value) % modulus == 0]
    if len(roots) != 1:
        raise AssertionError(f"Teichmueller representative not unique: {roots}")
    return roots[0]


def divide_error(jacobian_lift: Poly, prime: int) -> Poly:
    numerator = add(jacobian_lift, {(0, 0): -1})
    if any(coefficient % prime for coefficient in numerator.values()):
        raise AssertionError("lifted Jacobian error is not divisible by p")
    return reduce_poly({mon: coefficient // prime
                        for mon, coefficient in numerator.items()}, prime)


def cartier_support(error: Poly, prime: int) -> List[Mon]:
    return sorted(mon for mon, coefficient in error.items()
                  if coefficient % prime
                  and mon[0] % prime == prime - 1
                  and mon[1] % prime == prime - 1)


def exact_primitive(two_form: Poly, prime: int) -> Tuple[Poly, Poly]:
    """Return U,V with (V_x-U_y) dx^dy equal to two_form."""
    u: Poly = {}
    v: Poly = {}
    for (i, j), coefficient in sorted(reduce_poly(two_form, prime).items()):
        if (i + 1) % prime:
            inverse = pow((i + 1) % prime, -1, prime)
            v[(i + 1, j)] = coefficient * inverse % prime
        elif (j + 1) % prime:
            inverse = pow((j + 1) % prime, -1, prime)
            u[(i, j + 1)] = -coefficient * inverse % prime
        else:
            raise ValueError("nonzero top Cartier term has no polynomial primitive")
    recovered = reduce_poly(add(derivative(v, 0), scale(derivative(u, 1), -1)), prime)
    if recovered != reduce_poly(two_form, prime):
        raise AssertionError("de Rham primitive failed")
    return reduce_poly(u, prime), reduce_poly(v, prime)


def correction(p: Poly, q: Poly, error: Poly, prime: int) -> Tuple[Poly, Poly]:
    """Construct A,B with [A,Q]+[P,B] = -error modulo prime."""
    rhs = reduce_poly(scale(error, -1), prime)
    u, v = exact_primitive(rhs, prime)
    px, py = derivative(p, 0), derivative(p, 1)
    qx, qy = derivative(q, 0), derivative(q, 1)
    # U dx+V dy=A dQ-B dP, using [P,Q]=1.
    a = reduce_poly(add(scale(multiply(py, u), -1), multiply(px, v)), prime)
    b = reduce_poly(add(scale(multiply(qy, u), -1), multiply(qx, v)), prime)
    linearized = reduce_poly(add(bracket(a, q), bracket(p, b)), prime)
    if linearized != rhs:
        raise AssertionError("linearized correction equation failed")
    return a, b


def collision_lifts(p2: Poly, q2: Poly, residues: Sequence[Mon],
                    prime: int) -> Tuple[List[Mon], Mon]:
    modulus = prime * prime
    image_banks = []
    for rx, ry in residues:
        bank: Dict[Mon, Mon] = {}
        for ux in range(prime):
            for uy in range(prime):
                point = (rx + prime * ux, ry + prime * uy)
                image = (evaluate(p2, point, modulus), evaluate(q2, point, modulus))
                bank.setdefault(image, point)
        image_banks.append(bank)
    common = sorted(set(image_banks[0]).intersection(*(set(bank) for bank in image_banks[1:])))
    if not common:
        raise AssertionError("no moving marked-point collision lift exists")
    target = common[0]
    points = [bank[target] for bank in image_banks]
    if len(set(points)) != len(points):
        raise AssertionError("distinct marked residues produced equal lifts")
    return points, target


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_digest(record: object) -> str:
    payload = json.dumps(record, sort_keys=True, separators=(",", ":")).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def run() -> Dict[str, object]:
    prime = 3
    modulus = 9
    q: Poly = {(0, 1): 1}
    residues: Tuple[Mon, Mon] = ((0, 0), (1, 0))
    target: Mon = (0, 0)
    screened = []
    survivor = None

    for coefficient in (1, 2):
        p: Poly = {(1, 0): 1, (3, 0): coefficient}
        jacobian = reduce_poly(bracket(p, q), prime)
        images = [(evaluate(p, point, prime), evaluate(q, point, prime))
                  for point in residues]
        exact_support = set(p) == {(1, 0), (3, 0)} and set(q) == {(0, 1)}
        enters = exact_support and jacobian == {(0, 0): 1} and images == [target, target]
        item: Dict[str, object] = {
            "a": coefficient,
            "P_mod3": encode_poly(p, prime),
            "Q_mod3": encode_poly(q, prime),
            "exact_support": exact_support,
            "jacobian_mod3": encode_poly(jacobian, prime),
            "marked_images_mod3": [list(image) for image in images],
            "enters_witt_gate": enters,
        }
        if not enters:
            item["rejected_at"] = "marked-collision" if images != [target, target] else "special-fibre"
            screened.append(item)
            continue

        # The exact generic fibre is
        # F_3(U,V)[x,y]/(a*x^3+x-U, y-V), with basis 1,x,x^2.
        generic_degree = 3
        generic_separable_derivative: Poly = {(0, 0): 1}
        if not generic_degree % 2:
            raise AssertionError("registered odd-degree guard failed")

        p_lift: Poly = {(1, 0): teichmueller(1, prime),
                        (3, 0): teichmueller(coefficient, prime)}
        q_lift: Poly = {(0, 1): teichmueller(1, prime)}
        error = divide_error(bracket(p_lift, q_lift), prime)
        top = cartier_support(error, prime)
        item.update({
            "generic_degree": generic_degree,
            "generic_fibre_basis": ["1", "x", "x^2"],
            "generic_separable_derivative_mod3": encode_poly(generic_separable_derivative, prime),
            "P_teich_mod9": encode_poly(p_lift, modulus),
            "Q_teich_mod9": encode_poly(q_lift, modulus),
            "error_E_mod3": encode_poly(error, prime),
            "top_cartier_support": [list(mon) for mon in top],
            "obstruction_vanishes": not bool(top),
        })
        if top:
            item["witt_gate"] = "obstructed"
            screened.append(item)
            continue

        a_corr, b_corr = correction(p, q, error, prime)
        p2 = add(p_lift, scale(a_corr, prime))
        q2 = add(q_lift, scale(b_corr, prime))
        determinant_exact = bracket(p2, q2)
        determinant_mod9 = reduce_poly(determinant_exact, modulus)
        if determinant_mod9 != {(0, 0): 1}:
            raise AssertionError("emitted W2 correction is not Keller modulo 9")
        lifted_points, lifted_target = collision_lifts(p2, q2, residues, prime)
        item.update({
            "A_mod3": encode_poly(a_corr, prime),
            "B_mod3": encode_poly(b_corr, prime),
            "P2_mod9": encode_poly(p2, modulus),
            "Q2_mod9": encode_poly(q2, modulus),
            "determinant_exact_over_Z": encode_poly(determinant_exact),
            "determinant_mod9": encode_poly(determinant_mod9, modulus),
            "lifted_points_mod9": [list(point) for point in lifted_points],
            "lifted_target_mod9": list(lifted_target),
            "witt_gate": "survivor",
        })
        screened.append(item)
        survivor = item
        break

    verdict = "W2-SURVIVOR" if survivor is not None else "CAP-EXHAUSTED-NO-SURVIVOR"
    canonical_claim = {
        "cap_id": "AS3-MIN-W2",
        "prime": prime,
        "verdict": verdict,
        "values_screened": [item["a"] for item in screened],
        "survivor": survivor,
    }
    return {
        "schema_version": 1,
        "cap_id": "AS3-MIN-W2",
        "verdict": verdict,
        "stop_rule_triggered": "first-W2-survivor" if survivor else "complete-cap-exhaustion",
        "fixed_coefficient_order": [1, 2],
        "values_screened": len(screened),
        "cap_size": 2,
        "screened": screened,
        "canonical_claim": canonical_claim,
        "canonical_claim_sha256": canonical_digest(canonical_claim),
        "preregistration_sha256": sha256_file(CAP_DIR / "PREREGISTRATION.md"),
        "provenance_sha256": sha256_file(CAP_DIR / "provenance.json"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
