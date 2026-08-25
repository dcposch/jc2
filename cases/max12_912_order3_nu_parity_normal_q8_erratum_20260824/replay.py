#!/usr/bin/env python3
"""Exact stdlib erratum replay for the genuine parity-normal Q8 boundary.

The old Q12 slice used x5^2*(1/3)/(9v).  The reviewed fibre uses
x5^2*(1+3v)/(9v).  This replay keeps both formulae in separate variables,
reproduces the old off-fibre Q12 identity, makes that old identity fail on the
genuine fibre, and proves the replacement Q8 determinant identity.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import importlib.util
from itertools import permutations
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
REFUTATION = ROOT / "xmodel/max12-912-order3-nu-parity-normal-q12-review-grok-20260824.md"
REFUTATION_SHA256 = (
    "fc0b0216784bdcec8f9b0955c5a6c71d57870ae2265ed927f306d19d31a79c30"
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


def sparse_determinant(matrix, arithmetic, ring):
    size = len(matrix)
    out = {}
    for permutation in permutations(range(size)):
        inversions = sum(
            1
            for left in range(size)
            for right in range(left + 1, size)
            if permutation[left] > permutation[right]
        )
        term = ring.one
        for row, column in enumerate(permutation):
            term = arithmetic.cmul(term, matrix[row][column])
        out = arithmetic.cadd(
            out,
            arithmetic.cscale(-1 if inversions % 2 else 1, term),
        )
    return out


def evaluate_rat(value, bases, genus):
    total = genus.Rat.constant(0)
    for monomial, coefficient in value.items():
        term = genus.Rat.constant(coefficient)
        for exponent, base in zip(monomial, bases):
            term = term * (base ** exponent)
        total = total + term
    return total


def evaluate_at_one(value, genus):
    return (
        sum(value.numerator, Fraction(0))
        / sum(value.denominator, Fraction(0))
    )


def main() -> None:
    if sha256(REFUTATION.read_bytes()).hexdigest() != REFUTATION_SHA256:
        raise RuntimeError("refutation-review hash mismatch")
    parent = load_module("max12_q8_erratum_parent", PARENT, PARENT_SHA256)
    genus = load_module(
        "max12_q8_erratum_genus", GENUS_REPLAY, GENUS_REPLAY_SHA256
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

    parity_ring = M.Ring(["p", "x1", "x3", "x5"])
    p = parity_ring.var("p")
    x1 = parity_ring.var("x1")
    x3 = parity_ring.var("x3")
    x5 = parity_ring.var("x5")
    zero = {}
    images = [
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
    odd_rows = (1, 3, 5, 7)
    normal_columns = (0, 2, 4, 6)
    normal_matrix = [
        [
            parent.substitute_coeff(
                M.cpartial(tails[ell], column), images, parity_ring
            )
            for column in normal_columns
        ]
        for ell in odd_rows
    ]
    normal_determinant = sparse_determinant(
        normal_matrix, M, parity_ring
    )
    parity_tails = {
        ell: parent.substitute_coeff(tails[ell], images, parity_ring)
        for ell in range(1, 9)
    }
    assert all(not parity_tails[ell] for ell in odd_rows)

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
    Q12poly = (
        Fraction(480), Fraction(4688), Fraction(8664), Fraction(4608),
        Fraction(111060), Fraction(391932), Fraction(-503280),
        Fraction(-5322618), Fraction(-12251574), Fraction(-12217797),
        Fraction(-2488077), Fraction(4809213), Fraction(2893401),
    )
    v = genus.Rat(vpoly)
    D = genus.Rat(Dpoly)
    A2 = genus.Rat(A2poly)
    A5 = genus.Rat(A5poly)
    Q8 = genus.Rat(Q8poly)
    Q12 = genus.Rat(Q12poly)
    x5hat = genus.Rat.constant(-36) * (v ** 2) * A2 / D
    x3hat = x5hat * (v + genus.Rat.constant(2))

    # Correct numerator polynomial 1+3v.  Do not replace by a constant.
    correct_factor = genus.Rat((Fraction(1), Fraction(3)))
    x1_correct = (
        x5hat * (v + genus.Rat.constant(1))
        + (x5hat ** 2) * correct_factor
        / (genus.Rat.constant(9) * v)
    )
    # Exact regression of the quarantined off-fibre substitution.
    wrong_factor = genus.Rat.constant(Fraction(1, 3))
    x1_wrong = (
        x5hat * (v + genus.Rat.constant(1))
        + (x5hat ** 2) * wrong_factor
        / (genus.Rat.constant(9) * v)
    )

    correct_bases = [genus.Rat.constant(1), x1_correct, x3hat, x5hat]
    wrong_bases = [genus.Rat.constant(1), x1_wrong, x3hat, x5hat]
    correct_r2 = evaluate_rat(parity_tails[2], correct_bases, genus)
    correct_r4 = evaluate_rat(parity_tails[4], correct_bases, genus)
    wrong_r2 = evaluate_rat(parity_tails[2], wrong_bases, genus)
    wrong_r4 = evaluate_rat(parity_tails[4], wrong_bases, genus)
    assert correct_r2.equal(genus.Rat.constant(0))
    assert correct_r4.equal(genus.Rat.constant(0))
    assert not wrong_r2.equal(genus.Rat.constant(0))
    assert not wrong_r4.equal(genus.Rat.constant(0))

    determinant_correct = evaluate_rat(
        normal_determinant, correct_bases, genus
    )
    determinant_wrong = evaluate_rat(
        normal_determinant, wrong_bases, genus
    )
    old_q12_identity = (
        genus.Rat.constant(Fraction(-8388608, 243))
        * (v ** 14) * (A2 ** 7) * Q12 / (D ** 10)
    )
    new_q8_identity = (
        genus.Rat.constant(226492416)
        * (v ** 16) * (A2 ** 8) * Q8 / (D ** 10)
    )
    assert determinant_wrong.equal(old_q12_identity)
    assert not determinant_correct.equal(old_q12_identity)
    assert determinant_correct.equal(new_q8_identity)

    correct_r6 = evaluate_rat(parity_tails[6], correct_bases, genus)
    expected_r6 = (
        genus.Rat.constant(-2304)
        * (v ** 6) * (A2 ** 3) * A5 / (D ** 4)
    )
    assert correct_r6.equal(expected_r6)

    one = (Fraction(1),)
    assert Q8poly[0] != 0
    assert genus.pgcd(Q8poly, genus.derivative(Q8poly)) == one
    for factor in (A2poly, Dpoly, A5poly, Q12poly):
        assert genus.pgcd(Q8poly, factor) == one

    correct_at_one = evaluate_at_one(determinant_correct, genus)
    old_at_one = evaluate_at_one(old_q12_identity, genus)
    assert correct_at_one == 25275425185572323328
    assert old_at_one == Fraction(169664962152837939200, 243)

    payload = {
        "case": "max12_912_order3_nu_parity_normal_q8_erratum_20260824",
        "dependency_sha256": {
            "genus5_replay": GENUS_REPLAY_SHA256,
            "order3_fibre_compiler": PARENT_SHA256,
            "q12_hostile_refutation": REFUTATION_SHA256,
        },
        "chart_control": {
            "correct_factor": "1+3*v",
            "correct_r2_r4": "0,0",
            "wrong_factor": "1/3",
            "wrong_r2_r4_nonzero": True,
        },
        "determinant": {
            "correct_identity": (
                "p^20*226492416*v^16*(3*v^2+3*v+1)^8*Q8(v)/"
                "(3*v^2-2)^10"
            ),
            "old_q12_identity_fails_on_correct_chart": True,
            "old_q12_identity_reproduced_on_wrong_slice": True,
            "p1_v1_correct": str(correct_at_one),
            "p1_v1_old_q12": str(old_at_one),
        },
        "q8": {
            "polynomial": (
                "-999*v^8-1539*v^7+1782*v^6+6498*v^5+7320*v^4+"
                "4428*v^3+1548*v^2+296*v+24"
            ),
            "squarefree": True,
            "coprime_to": ["v", "A2", "D", "A5", "Q12"],
            "sole_residual_rank_boundary_on_generic_chart": True,
        },
        "quarantine": {
            "q12_checkpoint": "REFUTED; preserved for audit only",
            "q12_formal_branch_descendant": "INVALID DEPENDENCY; preserved for audit only",
        },
        "producer_conclusion": (
            "On the genuine reviewed parity chart, the first-order normal "
            "rank boundary is Q8=0, not Q12=0."
        ),
        "scope": (
            "erratum and exact first-order replacement only; no Q8 formal-"
            "branch, trajectory, Taylor, non-parity exhaustion, all-(9,12), "
            "maximum-twelve, counterexample, or JC2 conclusion"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
