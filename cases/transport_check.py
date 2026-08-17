#!/usr/bin/env python3
"""Exact regression checks for TRANSPORT.md.

The live GGV fixture is the conditional pre-Laurent (8,28) CornerData record.
The residue-A and td-7 fixtures are independent Sigray-frame controls.  Their
different formal normalized degree pairs are incompatible with the (72,108)
equivalence class if the filed frames are realized by polynomial pairs.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "lib"))

from families import geom, section4_families, supports  # noqa: E402


Point = tuple[Fraction, Fraction]


def point(x: int | Fraction, y: int | Fraction) -> Point:
    return Fraction(x), Fraction(y)


def transpose(p: Point) -> Point:
    """Exponent transport for the signed source rotation (x,y)->(y,-x)."""
    return p[1], p[0]


def scale(n: int, p: Point) -> Point:
    return n * p[0], n * p[1]


def dot(w: tuple[int, int], p: Point) -> Fraction:
    return w[0] * p[0] + w[1] * p[1]


def cross(p: tuple[int, int], q: Point) -> Fraction:
    return p[0] * q[1] - p[1] * q[0]


def direction_transport(w: tuple[int, int]) -> tuple[int, int]:
    return w[1], w[0]


def check_sigray_frame(
    low: Point, high: Point, kind: tuple[int, int]
) -> tuple[int, int]:
    """Check the numerical corner conditions of a Sigray rectangle frame."""
    alpha, beta = kind
    kf, lf = low
    kg, lg = high
    assert 1 < alpha < beta and gcd(alpha, beta) == 1
    assert Fraction(alpha, beta) == Fraction(kf, kg)
    assert Fraction(kf, kg) == Fraction(lf, lg)
    assert 0 < lf < kf and kf < kg and lf < lg
    assert Fraction(kg, kf).denominator != 1
    assert all(x.denominator == 1 for x in low + high)
    return int(kf + lf), int(kg + lg)


def pole_mass(alpha: int, beta: int, pole: tuple[int, int, int]) -> int:
    """Lambda=a*b*alpha*beta/nu for a filed pole (a,b,nu)."""
    a, b, nu = pole
    value = Fraction(a * b * alpha * beta, nu)
    assert value.denominator == 1
    return value.numerator


def ggv_8_28_transport() -> dict[str, object]:
    cd = section4_families()["8_28"]
    supp_p, supp_q = supports(cd)

    assert cd.mn == (3, 2)
    assert (cd.degP, cd.degQ) == (108, 72)
    assert cd.S == ((0, 0), (1, 0), (8, 28), (0, 4))
    assert supp_p == [(0, 0), (3, 0), (24, 84), (0, 12)]
    assert supp_q == [(0, 0), (2, 0), (16, 56), (0, 8)]

    # Target rotation (P,Q)->(Q,-P) sorts the coprime multipliers (2,3).
    # The signed source rotation transports exponent points by transpose.
    low = transpose(point(16, 56))
    high = transpose(point(24, 84))
    degrees = check_sigray_frame(low, high, (2, 3))
    assert (low, high, degrees) == (
        point(56, 16),
        point(84, 24),
        (72, 108),
    )

    a0 = point(*geom(cd.A0))
    a0p = point(*geom(cd.A0p))
    final = point(*geom(cd.final))
    # Exact pointwise images retain the campaign labels.  Since transpose
    # reverses orientation, the transported (en,st) edge swaps those images.
    named_chain = tuple(map(transpose, (a0, a0p, final)))
    assert named_chain == (
        point(28, 8),
        point(0, 1),
        point(7, Fraction(11, 4)),
    )

    rho, sigma, p, q = cd.steps[0]
    w = (rho, sigma)
    wt = direction_transport(w)
    edge = point(a0[0] - a0p[0], a0[1] - a0p[1])
    named_edge_t = point(
        named_chain[0][0] - named_chain[1][0],
        named_chain[0][1] - named_chain[1][1],
    )
    oriented_endpoints_t = (named_chain[1], named_chain[0])  # (en, st)
    oriented_edge_t = point(
        oriented_endpoints_t[0][0] - oriented_endpoints_t[1][0],
        oriented_endpoints_t[0][1] - oriented_endpoints_t[1][1],
    )
    assert dot(w, edge) == dot(wt, named_edge_t) == 0
    assert cross(w, edge) > 0
    assert cross(wt, named_edge_t) < 0
    assert cross(wt, oriented_edge_t) > 0
    assert Fraction(rho + sigma, dot(w, a0)) == Fraction(p, q)
    assert Fraction(wt[0] + wt[1], dot(wt, transpose(a0))) == Fraction(p, q)
    assert (wt, p, q) == ((-1, 4), 3, 4)

    return {
        "fixture": "GGV conditional pre-Laurent 8_28 family record",
        "ggv_degrees": [108, 72],
        "sigray_degrees": list(degrees),
        "sigray_corners": [[int(x) for x in low], [int(x) for x in high]],
        "type": [2, 3],
        "named_chain": [
            [str(x) for x in named_chain[0]],
            [str(x) for x in named_chain[1]],
            [str(x) for x in named_chain[2]],
        ],
        "oriented_first_edge": {
            "en": [str(x) for x in oriented_endpoints_t[0]],
            "st": [str(x) for x in oriented_endpoints_t[1]],
        },
        "direction": list(wt),
        "pq": [p, q],
    }


def residue_a_frame_control(ggv_degrees: tuple[int, int]) -> dict[str, object]:
    low, high = point(126, 42), point(189, 63)
    degrees = check_sigray_frame(low, high, (2, 3))
    assert degrees == (168, 252)

    sigray_base = point(low[0] / 2, low[1] / 2)
    inverse_ggv_base = transpose(sigray_base)
    assert inverse_ggv_base == point(21, 63)
    assert transpose(scale(2, inverse_ggv_base)) == low
    assert transpose(scale(3, inverse_ggv_base)) == high

    masses = [pole_mass(2, 3, pole) for pole in ((1, 1, 2), (1, 1, 2))]
    assert masses == [3, 3] and sum(masses) == 6
    assert degrees != ggv_degrees

    return {
        "fixture": "residue-A formal frame",
        "role": "independent frame_schema control",
        "sigray_degrees": list(degrees),
        "inverse_ggv_base": [int(x) for x in inverse_ggv_base],
        "pole_masses": masses,
        "td": sum(masses),
        "compatible_with_8_28_normalized_degrees": False,
    }


def td7_frame_control(ggv_degrees: tuple[int, int]) -> dict[str, object]:
    certificate_path = ROOT / "cases" / "towers" / "t9_15_direct.json"
    certificate = json.loads(certificate_path.read_text())
    root = next(v for v in certificate["vertices"] if v["name"] == "R0")

    low = point(root["deg_p_f"], root["D_f"])
    high = point(root["deg_p_g"], root["d_g"])
    degrees = check_sigray_frame(low, high, (2, 3))
    assert degrees == (271320, 406980)

    inverse_ggv_base = transpose(point(low[0] / 2, low[1] / 2))
    assert inverse_ggv_base == point(33915, 101745)
    assert transpose(scale(2, inverse_ggv_base)) == low
    assert transpose(scale(3, inverse_ggv_base)) == high

    poles = ((1, 1, 2), (1, 2, 3))
    masses = [pole_mass(2, 3, pole) for pole in poles]
    assert masses == [3, 4] and sum(masses) == 7
    assert [pole[1] for pole in poles] == [1, 2]  # M=b in the filed entry.
    assert degrees != ggv_degrees
    assert "TOWER-OBSTRUCTED" in certificate["status"]

    return {
        "fixture": certificate["cell"],
        "role": "independent frame_schema control; filed cell is tower-obstructed",
        "sigray_degrees": list(degrees),
        "inverse_ggv_base": [int(x) for x in inverse_ggv_base],
        "pole_masses": masses,
        "M": [1, 2],
        "td": sum(masses),
        "compatible_with_8_28_normalized_degrees": False,
    }


def main() -> None:
    ggv = ggv_8_28_transport()
    ggv_degrees = tuple(ggv["sigray_degrees"])
    results = {
        "status": "PASS",
        "ggv_transport": ggv,
        "residue_A": residue_a_frame_control(ggv_degrees),
        "td7": td7_frame_control(ggv_degrees),
    }
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
