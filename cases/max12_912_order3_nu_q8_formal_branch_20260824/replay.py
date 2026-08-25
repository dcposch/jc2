#!/usr/bin/env python3
"""Fresh exact replay for the Q8 equivariant formal-branch theorem.

No quarantined Q12 branch artifact is imported.  The script reconstructs all
eight rows, uses the corrected parity chart, and verifies the two rank-three
minors and loaded-curve transversality at Q8.
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
GENUS_REPLAY = ROOT / "cases/max12_912_order3_nu_parity_genus5_20260824/replay.py"
GENUS_REPLAY_SHA256 = "c965bb660cf2f0f55c7ebbed3126b22bfb5d67e178565426aa94ce56f6ce1d9a"
Q8_REPLAY = ROOT / "cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/replay.py"
Q8_REPLAY_SHA256 = "51168609a477905b25cb551ddd40931d1a6d752d7a1569bdc1b9a394cf8dcd23"
Q8_REPORT = ROOT / "xmodel/max12-912-order3-nu-parity-normal-q8-erratum-20260824.md"
Q8_REPORT_SHA256 = "7f1ed3c7874c743b35ba4f519acdc2555f65c93c467ccb2e894d8d0b7ade1cc2"


def load_module(name, path, expected_sha256):
    if sha256(path.read_bytes()).hexdigest() != expected_sha256:
        raise RuntimeError(f"dependency hash mismatch: {path}")
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    if sha256(Q8_REPORT.read_bytes()).hexdigest() != Q8_REPORT_SHA256:
        raise RuntimeError("Q8 report hash mismatch")
    parent = load_module("q8_branch_parent", PARENT, PARENT_SHA256)
    genus = load_module("q8_branch_genus", GENUS_REPLAY, GENUS_REPLAY_SHA256)
    erratum = load_module("q8_branch_erratum", Q8_REPLAY, Q8_REPLAY_SHA256)
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
    normal_indices = (0, 2, 4, 6)
    for ell in range(1, 9):
        for monomial in tails[ell]:
            assert sum(monomial[index] for index in normal_indices) % 2 == ell % 2

    ring = M.Ring(["p", "x1", "x3", "x5"])
    p = ring.var("p")
    x1 = ring.var("x1")
    x3 = ring.var("x3")
    x5 = ring.var("x5")
    zero = {}
    images = [
        zero, x1, zero,
        M.cadd(M.cmul(M.cmul(p, p), p), x3),
        zero, M.cadd(M.cscale(3, M.cmul(p, p)), x5),
        zero, M.cscale(3, p), zero,
    ]
    parity_tails = {
        ell: parent.substitute_coeff(tails[ell], images, ring)
        for ell in range(1, 9)
    }
    assert all(not parity_tails[ell] for ell in (1, 3, 5, 7))
    for ell in (2, 4, 6, 8):
        for column in normal_indices:
            assert not parent.substitute_coeff(
                M.cpartial(tails[ell], column), images, ring
            )

    normal_matrix = [
        [
            parent.substitute_coeff(
                M.cpartial(tails[ell], column), images, ring
            )
            for column in normal_indices
        ]
        for ell in (1, 3, 5, 7)
    ]
    invariant_matrix = [
        [M.cpartial(parity_tails[ell], column) for column in range(4)]
        for ell in (2, 4, 6)
    ]

    vpoly = (Fraction(0), Fraction(1))
    Dpoly = (Fraction(-2), Fraction(0), Fraction(3))
    A2poly = (Fraction(1), Fraction(3), Fraction(3))
    A5poly = (
        Fraction(2), Fraction(18), Fraction(69), Fraction(131),
        Fraction(117), Fraction(33),
    )
    Q8poly = (
        Fraction(24), Fraction(296), Fraction(1548), Fraction(4428),
        Fraction(7320), Fraction(6498), Fraction(1782), Fraction(-1539),
        Fraction(-999),
    )
    v = genus.Rat(vpoly)
    D = genus.Rat(Dpoly)
    A2 = genus.Rat(A2poly)
    Q8 = genus.Rat(Q8poly)
    x5hat = genus.Rat.constant(-36) * (v ** 2) * A2 / D
    x3hat = x5hat * (v + genus.Rat.constant(2))
    x1hat = (
        x5hat * (v + genus.Rat.constant(1))
        + (x5hat ** 2) * genus.Rat((Fraction(1), Fraction(3)))
        / (genus.Rat.constant(9) * v)
    )
    bases = [genus.Rat.constant(1), x1hat, x3hat, x5hat]

    determinant = erratum.sparse_determinant(normal_matrix, M, ring)
    determinant_hat = erratum.evaluate_rat(determinant, bases, genus)
    expected_determinant = (
        genus.Rat.constant(226492416)
        * (v ** 16) * (A2 ** 8) * Q8 / (D ** 10)
    )
    assert determinant_hat.equal(expected_determinant)

    normal_minor = erratum.sparse_determinant(
        [row[1:] for row in normal_matrix[1:]], M, ring
    )
    normal_minor_hat = erratum.evaluate_rat(normal_minor, bases, genus)
    invariant_minor = erratum.sparse_determinant(
        [row[1:] for row in invariant_matrix], M, ring
    )
    invariant_minor_hat = erratum.evaluate_rat(invariant_minor, bases, genus)
    one = (Fraction(1),)
    for certificate in (normal_minor_hat, invariant_minor_hat):
        assert genus.pgcd(certificate.numerator, Q8poly) == one
        assert genus.pgcd(certificate.denominator, Q8poly) == one

    assert genus.pgcd(Q8poly, genus.derivative(Q8poly)) == one
    for factor in (A2poly, Dpoly, A5poly):
        assert genus.pgcd(Q8poly, factor) == one
    r6_numerator = genus.pmul(
        genus.ppow(vpoly, 6),
        genus.pmul(genus.ppow(A2poly, 3), A5poly),
    )
    r6_derivative_numerator = genus.padd(
        genus.pmul(genus.derivative(r6_numerator), Dpoly),
        genus.pscale(
            -4, genus.pmul(r6_numerator, genus.derivative(Dpoly))
        ),
    )
    assert genus.pgcd(Q8poly, r6_derivative_numerator) == one

    payload = {
        "case": "max12_912_order3_nu_q8_formal_branch_20260824",
        "dependency_sha256": {
            "genus5_replay": GENUS_REPLAY_SHA256,
            "order3_fibre_compiler": PARENT_SHA256,
            "q8_erratum_replay": Q8_REPLAY_SHA256,
            "q8_erratum_report": Q8_REPORT_SHA256,
        },
        "fresh_lineage": {
            "correct_x1_factor": "1+3*v",
            "quarantined_q12_branch_consumed": False,
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
            "q8_squarefree": True,
            "q8_coprime_to_r6_derivative_numerator": True,
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
            "Every loaded Q8 contact point of the genuine parity fixed curve "
            "lies on a second smooth non-parity formal component of the "
            "seven-row constant-invariant fibre."
        ),
        "scope": (
            "formal high-row coefficient fibre only; not an algebraic or "
            "rational Keller trajectory, and no terminal-r8, Taylor, "
            "coprimality, disjoint-component, all-(9,12), maximum-twelve, "
            "counterexample, or JC2 conclusion"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
