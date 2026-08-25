#!/usr/bin/env python3
"""Exact stdlib replay for the parity-normal Q12 rank boundary.

This is a first-order Kuranishi checkpoint only.  It computes the normal
Jacobian from the reviewed order-three fibre compiler and reduces its
determinant on the reviewed generic parity chart.  It does not infer that a
formal arc is trapped in parity at the residual Q12 boundary.
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


def main() -> None:
    parent = load_module("max12_parity_normal_parent", PARENT, PARENT_SHA256)
    genus = load_module(
        "max12_parity_normal_genus", GENUS_REPLAY, GENUS_REPLAY_SHA256
    )
    M = parent.M
    compiled = parent.compile_fibre()
    tails = compiled["tails"]

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
    normal_matrix = []
    for ell in odd_rows:
        row = []
        for column in normal_columns:
            derivative = M.cpartial(tails[ell], column)
            row.append(
                parent.substitute_coeff(derivative, images, parity_ring)
            )
        normal_matrix.append(row)
    normal_determinant = sparse_determinant(normal_matrix, M, parity_ring)

    for ell in odd_rows:
        assert not parent.substitute_coeff(tails[ell], images, parity_ring)
    for ell in (2, 4, 6, 8):
        for column in normal_columns:
            derivative = M.cpartial(tails[ell], column)
            assert not parent.substitute_coeff(
                derivative, images, parity_ring
            )

    # Generic reviewed chart: p*x5*A != 0 and v=A/(p*x5).
    v = genus.Rat((Fraction(0), Fraction(1)))
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

    quotient = genus.evaluate_weighted(
        normal_determinant,
        [genus.Rat.constant(1), x1hat, x3hat, x5hat],
        [1, 4, 3, 2],
        20,
    )
    scalar = Fraction(-8388608, 243)
    expected = (
        genus.Rat.constant(scalar)
        * (v ** 14)
        * (A2 ** 7)
        * Q12
        / (D ** 10)
    )
    assert quotient.equal(expected)

    one = (Fraction(1),)
    assert Q12poly[0] != 0
    assert genus.pgcd(Q12poly, genus.derivative(Q12poly)) == one
    assert genus.pgcd(Q12poly, A5poly) == one
    assert genus.pgcd(Q12poly, A2poly) == one
    assert genus.pgcd(Q12poly, Dpoly) == one
    assert genus.pgcd(A2poly, Dpoly) == one

    q12_display = (
        "2893401*v^12+4809213*v^11-2488077*v^10-12217797*v^9"
        "-12251574*v^8-5322618*v^7-503280*v^6+391932*v^5"
        "+111060*v^4+4608*v^3+8664*v^2+4688*v+480"
    )
    payload = {
        "case": "max12_912_order3_nu_parity_normal_q12_20260824",
        "dependency_sha256": {
            "genus5_replay": GENUS_REPLAY_SHA256,
            "order3_fibre_compiler": PARENT_SHA256,
        },
        "involution": {
            "fixed_locus": "a0=a2=a4=a6=k=0",
            "normal_columns": ["a0", "a2", "a4", "a6"],
            "normal_rows": ["r1", "r3", "r5", "r7"],
            "odd_rows_vanish_on_fixed_locus": True,
            "even_rows_have_zero_normal_linearization": True,
        },
        "generic_chart": {
            "conditions": "p*x5*A!=0, A=x3-2*p*x5",
            "determinant_identity": (
                "det=p^20*(-8388608/243)*v^14*"
                "(3*v^2+3*v+1)^7*Q12(v)/(3*v^2-2)^10"
            ),
            "v": "A/(p*x5)",
        },
        "q12": {
            "polynomial": q12_display,
            "squarefree": True,
            "coprime_to": ["v", "A2=3*v^2+3*v+1", "D=3*v^2-2", "A5"],
            "is_only_remaining_normal_rank_boundary_on_generic_chart": True,
            "loaded_points_are_not_removed_by_r6_zero": True,
        },
        "producer_conclusion": (
            "Away from Q12=0 and the already separated p,x5,A chart "
            "boundaries, the loaded fibre is scheme-theoretically normal-"
            "unramified along the parity fixed locus at first order."
        ),
        "scope": (
            "exact first-order normal-rank checkpoint only; no exclusion of "
            "Q12, no formal-arc trapping claim at Q12, and no non-parity, "
            "all-(9,12), maximum-twelve, counterexample, or JC2 conclusion"
        ),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
