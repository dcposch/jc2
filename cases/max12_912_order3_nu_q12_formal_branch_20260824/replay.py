#!/usr/bin/env python3
"""Exact replay for the Q12 equivariant formal-branch theorem.

The script reconstructs all eight tail rows from the frozen coefficient
compiler, checks the involution, and certifies the two rank-three minors and
the simple contact divisor needed by the formal implicit-function argument.
Only Python's standard library is used.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "cases/max12_912_order3_fibre_20260824/order3_fibre.py"
PARENT_SHA256 = "a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf"
GENUS_REPLAY = (
    ROOT / "cases/max12_912_order3_nu_parity_genus5_20260824/replay.py"
)
GENUS_REPLAY_SHA256 = (
    "c965bb660cf2f0f55c7ebbed3126b22bfb5d67e178565426aa94ce56f6ce1d9a"
)
Q12_REPLAY = (
    ROOT / "cases/max12_912_order3_nu_parity_normal_q12_20260824/replay.py"
)
Q12_REPLAY_SHA256 = (
    "bff291fcf01fcb9cfc33e70161be4df59cc0a98315c174ac083cbb3ba8049658"
)
Q12_REPORT = ROOT / "xmodel/max12-912-order3-nu-parity-normal-q12-20260824.md"
Q12_REPORT_SHA256 = (
    "9616396705d071efac3cf52332c5007a4a045989940bcc8743a545e87f763a1c"
)


def load_module(name: str, path: Path, expected_sha256: str):
    if sha256(path.read_bytes()).hexdigest() != expected_sha256:
        raise RuntimeError(f"dependency hash mismatch: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load dependency: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def evaluate_rat(value, bases, genus):
    total = genus.Rat.constant(0)
    for monomial, coefficient in value.items():
        term = genus.Rat.constant(coefficient)
        for exponent, base in zip(monomial, bases):
            term = term * (base ** exponent)
        total = total + term
    return total


def main() -> None:
    if sha256(Q12_REPORT.read_bytes()).hexdigest() != Q12_REPORT_SHA256:
        raise RuntimeError("Q12 report dependency hash mismatch")
    parent = load_module("max12_q12_branch_parent", PARENT, PARENT_SHA256)
    genus = load_module(
        "max12_q12_branch_genus", GENUS_REPLAY, GENUS_REPLAY_SHA256
    )
    qcase = load_module(
        "max12_q12_branch_checkpoint", Q12_REPLAY, Q12_REPLAY_SHA256
    )
    M = parent.M
    compiled = parent.compile_fibre()
    tails = compiled["tails"]

    expected_supports = {
        "r1": 25, "r2": 36, "r3": 42, "r4": 55,
        "r5": 63, "r6": 84, "r7": 94, "r8": 121,
    }
    expected_digests = {
        "r1": "2b69e9de7171f6d36e8b829f779a516edbbd858efe8590b489198fd00420e862",
        "r2": "89f14d6c4c87bfdd05686f14b954ed95c538fb30184dd606b2acd2ff2f27e1b0",
        "r3": "f2d6fcc68f54a8706f8006acf486202fc10d7ec3e185cc499dbfa88f68947411",
        "r4": "1b00e72f56ef539d52f49d63ea5af428bacc84ef8d43099433597e250bb18af5",
        "r5": "1a94d04018f26444d56fe6093c6fda3e02d50567f2daf57bd1032d555dbe76ae",
        "r6": "b4842f92db54265db4c6a81da527e23198da06a480663fbb7813cc52fa436c6b",
        "r7": "cfa591979bc8bc4405d19362a71f6ef6330ef904b64879eb4edad49375074e2f",
        "r8": "d727c41fa3f32b4bef54d22b8b33659d1077526a2e86b03f3ae0cbf228b1126f",
    }
    assert compiled["payload"]["tail_supports"] == expected_supports
    assert compiled["payload"]["tail_sha256"] == expected_digests

    # Under f(z) -> -f(-z), the even-index a coefficients change sign.
    # Every monomial of r_l has the asserted character (-1)^l.
    normal_indices = (0, 2, 4, 6)
    for ell in range(1, 9):
        for monomial in tails[ell]:
            assert sum(monomial[index] for index in normal_indices) % 2 == ell % 2

    parity_ring = M.Ring(["p", "x1", "x3", "x5"])
    p = parity_ring.var("p")
    x1 = parity_ring.var("x1")
    x3 = parity_ring.var("x3")
    x5 = parity_ring.var("x5")
    zero = {}
    parity_images = [
        zero,
        x1,
        zero,
        M.cadd(M.cmul(M.cmul(p, p), p), x3),
        zero,
        M.cadd(M.cscale(3, M.cmul(p, p)), x5),
        zero,
        M.cscale(3, p),
        zero,
    ]
    parity_tails = {
        ell: parent.substitute_coeff(tails[ell], parity_images, parity_ring)
        for ell in range(1, 9)
    }
    assert all(not parity_tails[ell] for ell in (1, 3, 5, 7))
    for ell in (2, 4, 6, 8):
        for column in normal_indices:
            derivative = M.cpartial(tails[ell], column)
            assert not parent.substitute_coeff(
                derivative, parity_images, parity_ring
            )

    odd_rows = (1, 3, 5, 7)
    normal_matrix = [
        [
            parent.substitute_coeff(
                M.cpartial(tails[ell], column),
                parity_images,
                parity_ring,
            )
            for column in normal_indices
        ]
        for ell in odd_rows
    ]
    normal_determinant = qcase.sparse_determinant(
        normal_matrix, M, parity_ring
    )

    # Reviewed generic parity chart, normalized temporarily by p=1.
    vpoly = (Fraction(0), Fraction(1))
    Dpoly = (Fraction(-2), Fraction(0), Fraction(3))
    A2poly = (Fraction(1), Fraction(3), Fraction(3))
    A5poly = (
        Fraction(2), Fraction(18), Fraction(69), Fraction(131),
        Fraction(117), Fraction(33),
    )
    Q12poly = (
        Fraction(480), Fraction(4688), Fraction(8664), Fraction(4608),
        Fraction(111060), Fraction(391932), Fraction(-503280),
        Fraction(-5322618), Fraction(-12251574), Fraction(-12217797),
        Fraction(-2488077), Fraction(4809213), Fraction(2893401),
    )
    v = genus.Rat(vpoly)
    D = genus.Rat(Dpoly)
    A2 = genus.Rat(A2poly)
    Q12 = genus.Rat(Q12poly)
    x5hat = genus.Rat.constant(-36) * (v ** 2) * A2 / D
    x3hat = x5hat * (v + genus.Rat.constant(2))
    x1hat = (
        x5hat * (v + genus.Rat.constant(1))
        + (x5hat ** 2) * genus.Rat.constant(Fraction(1, 3))
        / (genus.Rat.constant(9) * v)
    )
    chart_bases = [genus.Rat.constant(1), x1hat, x3hat, x5hat]

    determinant_hat = evaluate_rat(normal_determinant, chart_bases, genus)
    expected_determinant = (
        genus.Rat.constant(Fraction(-8388608, 243))
        * (v ** 14) * (A2 ** 7) * Q12 / (D ** 10)
    )
    assert determinant_hat.equal(expected_determinant)

    # The unit normal minor leaves row r1 and column a0 uneliminated.
    normal_minor = qcase.sparse_determinant(
        [row[1:] for row in normal_matrix[1:]], M, parity_ring
    )
    normal_minor_hat = evaluate_rat(normal_minor, chart_bases, genus)

    # The unit invariant minor solves r2,r4,r6 for x1,x3,x5, leaving p.
    invariant_matrix = [
        [M.cpartial(parity_tails[ell], column) for column in range(4)]
        for ell in (2, 4, 6)
    ]
    invariant_minor = qcase.sparse_determinant(
        [row[1:] for row in invariant_matrix], M, parity_ring
    )
    invariant_minor_hat = evaluate_rat(invariant_minor, chart_bases, genus)

    one = (Fraction(1),)
    for certificate in (normal_minor_hat, invariant_minor_hat):
        assert genus.pgcd(certificate.numerator, Q12poly) == one
        assert genus.pgcd(certificate.denominator, Q12poly) == one

    assert genus.pgcd(Q12poly, genus.derivative(Q12poly)) == one
    assert Q12poly[0] != 0
    for factor in (A2poly, A5poly, Dpoly):
        assert genus.pgcd(Q12poly, factor) == one

    # R6=-2304*N/D^4.  This numerator is the numerator of R6' after
    # removing the invertible D^3 factor and the irrelevant scalar.
    r6_numerator = genus.pmul(
        genus.ppow(vpoly, 6),
        genus.pmul(genus.ppow(A2poly, 3), A5poly),
    )
    r6_derivative_numerator = genus.padd(
        genus.pmul(genus.derivative(r6_numerator), Dpoly),
        genus.pscale(
            -4,
            genus.pmul(r6_numerator, genus.derivative(Dpoly)),
        ),
    )
    assert genus.pgcd(Q12poly, r6_derivative_numerator) == one

    payload = {
        "case": "max12_912_order3_nu_q12_formal_branch_20260824",
        "dependency_sha256": {
            "genus5_replay": GENUS_REPLAY_SHA256,
            "order3_fibre_compiler": PARENT_SHA256,
            "q12_checkpoint_replay": Q12_REPLAY_SHA256,
            "q12_checkpoint_report": Q12_REPORT_SHA256,
        },
        "original_eight_rows": {
            "sha256": expected_digests,
            "supports": expected_supports,
            "involution_character_checked": "r_l has character (-1)^l",
        },
        "contact": {
            "fixed_fibre_dimension": 1,
            "full_jacobian_rank": 6,
            "full_tangent_dimension": 2,
            "invariant_rank": 3,
            "invariant_unit_minor": "rows r2,r4,r6; columns x1,x3,x5",
            "normal_rank": 3,
            "normal_unit_minor": "rows r3,r5,r7; columns a2,a4,a6",
            "q12_squarefree": True,
            "q12_coprime_to_r6_derivative_numerator": True,
        },
        "equivariant_formal_normal_form": {
            "coordinates": "s invariant, t anti-invariant",
            "equation": "t*Phi(s,t^2)=0",
            "parity_component": "t=0",
            "contact_derivative": "dPhi/ds is a unit",
            "second_component": "Phi(s,t^2)=0, smooth and non-parity",
            "local_geometry": "two reduced formal curve branches with distinct tangents",
        },
        "producer_conclusion": (
            "Every loaded Q12 contact point of the parity fixed curve lies "
            "on a second smooth non-parity formal component of the seven-row "
            "constant-invariant fibre."
        ),
        "scope": (
            "formal high-row coefficient fibre only; not an algebraic or "
            "rational Keller trajectory, and no terminal-r8, Taylor, "
            "coprimality, all-(9,12), maximum-twelve, counterexample, or JC2 "
            "conclusion"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
