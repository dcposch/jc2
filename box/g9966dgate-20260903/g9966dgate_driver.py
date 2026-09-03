#!/usr/bin/env python3
"""Independent exact checks for the (99,66) joint-chart gate. No ledger I/O."""
from __future__ import annotations

import json
from fractions import Fraction as F
from math import comb, gcd
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent


def dim_S(D: int, r: int) -> int:
    return r * (D + 1) - r * (r - 1) // 2


def main() -> None:
    out: dict = {"type": "G9966-DESIGN-GATE / EXACT-ARITHMETIC"}

    # --- 7161 chart dimensions ---
    blocks = {
        "H": dim_S(10, 11),
        "C2": dim_S(21, 11),
        "C3": dim_S(32, 11),
        "A2": dim_S(65, 33),
        "A3": dim_S(98, 33),
        "B1": dim_S(32, 33),
        "B2": dim_S(65, 33),
    }
    unfixed = {
        "H": dim_S(11, 11),
        "C2": dim_S(22, 11),
        "C3": dim_S(33, 11),
        "A2": dim_S(66, 33),
        "A3": dim_S(99, 33),
        "B1": dim_S(33, 33),
        "B2": dim_S(66, 33),
    }
    out["chart"] = {
        "fixed_top_blocks": blocks,
        "fixed_top_total": sum(blocks.values()),
        "unfixed_total": sum(unfixed.values()),
        "monic_99_66": (5050 - 1) + (2278 - 1),
        "removed_by_two_tops": 99 + 66,
    }
    assert out["chart"]["fixed_top_total"] == 7161
    assert out["chart"]["unfixed_total"] == 7326
    assert out["chart"]["monic_99_66"] == 7326
    assert 7326 - 165 == 7161

    # --- h3 D2 support ---
    h_lower = [(r, q) for r in range(1, 12) for q in range(12 - r)]
    assert len(h_lower) == 66
    below = [(r, q) for r, q in h_lower if 3 * r + 4 * q < 32]
    equal = [(r, q) for r, q in h_lower if 3 * r + 4 * q == 32]
    strict = [(r, q) for r, q in h_lower if 3 * r + 4 * q >= 33]
    out["h3_D2"] = {
        "lower": 66,
        "strict_below_32": len(below),
        "equality_sites": equal,
        "strict_ge_33": len(strict),
        "linear_rows": len(below) + len(equal),
    }
    assert equal == [(4, 5), (8, 2)]
    assert len(below) == 43 and len(strict) == 21
    assert out["h3_D2"]["linear_rows"] == 45

    c2 = {(r, q) for r in range(1, 23) for q in range(min(10, 22 - r) + 1)}
    c3 = {(r, q) for r in range(1, 34) for q in range(min(10, 33 - r) + 1)}
    assert (len(c2), len(c3)) == (187, 308)
    ambient = 21 + 187 + 308
    assert ambient == 516

    d2_slots = {
        (r, q)
        for r in range(1, 34)
        for q in range(34 - r)
        if 3 * r + 4 * q <= 96
    }
    assert len(d2_slots) == 392
    h_fixed = {(0, q) for q in range(8, 12)}
    h_tail = set(strict)
    h_support = h_fixed | h_tail
    c2h = {(a + r, b + q) for a, b in c2 for r, q in h_support}
    h3_sq = {(r1 + r2, q1 + q2) for r1, q1 in h_support for r2, q2 in h_support}
    h3_cu = {(r12 + r3, q12 + q3) for r12, q12 in h3_sq for r3, q3 in h_support}
    face_targets = {(4 * k, 24 - 3 * k) for k in range(1, 9)}
    identities = d2_slots - c3 - c2h - h3_cu - face_targets
    assert identities == {(1, 23), (1, 22), (2, 22)}
    ordered = sorted(d2_slots - identities, key=lambda p: (p[0], -p[1]))
    pivots = {}
    for r, q in ordered:
        pivot = ("C3", r, q) if q <= 10 else ("C2", r, q - 11)
        assert pivot not in pivots
        pivots[pivot] = (r, q)
        if pivot[0] == "C3":
            assert (r, q) in c3
        else:
            assert (r, q - 11) in c2
            a, b = r, q - 11
            col = {
                (a + hr, b + hq)
                for hr, hq in h_support
                if (a + hr, b + hq) in d2_slots
            }
            assert min(col, key=lambda p: (p[0], -p[1])) == (r, q)
    c3n = sum(p[0] == "C3" for p in pivots)
    c2n = sum(p[0] == "C2" for p in pivots)
    assert (len(pivots), c3n, c2n) == (389, 275, 114)
    m97 = sp.Matrix([[comb(q, j) for q in [16, 13, 10, 7, 4]] for j in range(5)])
    m98 = sp.Matrix([[comb(q, j) for q in [17, 14]] for j in range(2)])
    assert m97.det() == 59049
    assert m98.det() == -3
    out["major_516"] = {
        "ambient": ambient,
        "D2_slots": 392,
        "identities": [list(p) for p in sorted(identities)],
        "D2_rank": 389,
        "D1_rank": 7,
        "dimension": ambient - 389 - 7,
        "det97": int(m97.det()),
        "det98": int(m98.det()),
        "h3_free": 21,
    }
    assert out["major_516"]["dimension"] == 120

    # --- skeleton (99,66): M,V,d,delta,(12)/(13) ---
    n, m = 99, 66
    M = {1: -66, 2: 77, 3: 97}
    d = {1: 99, 2: 33, 3: 11, 4: 1}
    V = {2: 8, 3: 8, 4: 1}
    s = 3

    def delta(i: int) -> F:
        num, den = F(n - M[i]), F(n - M[s] - 1)
        for j in range(i + 1, s + 1):
            num *= V[j] * (n - M[j]) - d[j]
            den *= V[j] * (n - M[j - 1]) - d[j]
        return 1 - num / den

    deltas = {i: delta(i) for i in (1, 2, 3)}
    assert deltas[3] == -1 and deltas[2] == F(1, 3) and deltas[1] == F(4, 9)
    u3 = d[3] - V[3]
    assert u3 == 3
    # (12)/(13)
    L1 = 1
    for i in (2, 3):
        L1 = L1 * deltas[i].denominator // gcd(L1, deltas[i].denominator)
    A1 = (L1 * deltas[1]).denominator
    ns, ms, V2 = n // d[2], m // d[2], V[2]
    b12 = (ns * V2 % A1 == 0) and ((ms * V2 - 1) % A1 == 0)
    b13 = (ms * V2 % A1 == 0) and ((ns * V2 - 1) % A1 == 0)
    out["skeleton"] = {
        "d": [99, 33, 11, 1],
        "u3": 3,
        "v3": 8,
        "deltas": {str(k): str(v) for k, v in deltas.items()},
        "A1": A1,
        "n_star": ns,
        "m_star": ms,
        "cond12": b12,
        "cond13": b13,
        "minor_threshold_d3_over_n_M3": str(F(d[3], n - M[3])),
        "V3_is_major": V[3] > d[3] / (n - M[3]),
        "u3_is_minor": u3 <= d[3] / (n - M[3]),
    }
    assert b12 and not b13
    assert V[3] > 11 / 2 and u3 <= 11 / 2

    # multiplicities
    out["multiplicities"] = {
        "g_Moh_F_chart_minor": 99 * 3 // 11,  # 27
        "f_Moh_G_chart_minor": 66 * 3 // 11,  # 18
        "T2": 55 * 3 // 11,  # 15
        "T3": (145 - 2) * 3 // 11 + 1,  # 40
        "g_major": 99 * 8 // 11,  # 72
        "f_major": 66 * 8 // 11,  # 48
    }
    assert out["multiplicities"]["f_Moh_G_chart_minor"] == 18
    assert out["multiplicities"]["g_Moh_F_chart_minor"] == 27

    # Thm 1.2 vs design rephrase: ord h_j >= (lambda/d)*j, with lambda = d*ord h
    # D2 h3: ord=-1/3; D1 h2: ord=-1/9
    out["thm12_orders"] = {
        "printed": "ord h_j(sigma_i) >= (lambda/d)*j  (Moh p.149)",
        "design_rephrase": "ord Q_j >= j * ord h  iff  ord h = lambda/d",
        "D2_h3": {"ord_h3": str(F(-1, 3)), "F_j_bound": ">= -j/3"},
        "D1_h2": {
            "ord_h2": str(F(-1, 9)),
            "A2": str(F(-2, 9)),
            "A3": str(F(-1, 3)),
            "B1": str(F(-1, 9)),
            "B2": str(F(-2, 9)),
        },
        "no_h3_at_D1": "F-multiplicity 24 is not divisible by 9",
    }
    assert 24 % 9 != 0

    # --- Jacobian degree ---
    x, y = sp.symbols("x y")
    P = y**3 * (y - x) ** 8
    P9 = sp.expand(P**9)
    P6 = sp.expand(P**6)
    Jtops = sp.expand(
        sp.diff(P9, x) * sp.diff(P6, y) - sp.diff(P9, y) * sp.diff(P6, x)
    )
    assert Jtops == 0
    assert sp.total_degree(P9) == 99 and sp.total_degree(P6) == 66
    out["jacobian_degree"] = {
        "generic_max": 99 + 66 - 2,
        "top_vanishes": True,
        "first_possible_nonzero": 162,
        "slots_deg_0_through_162": 163 * 164 // 2,
        "first_row_1764": 98 * 18,
        "next_band_monomial": "x^135 y^27",
        "next_band_total_degree": 135 + 27,
        "in_F": "y^27 (y-x)^72",
        "in_G": "y^18 (y-x)^48",
    }
    assert out["jacobian_degree"]["slots_deg_0_through_162"] == 13366
    assert 98 * 18 == 1764
    assert 135 + 27 == 162
    P3 = sp.Poly(sp.expand(P**3), x, y)
    assert P3.coeff_monomial(x**24 * y**9) == 1
    assert sp.Poly(P9, x, y).coeff_monomial(x**98 * y) == 0
    assert sp.Poly(P6, x, y).coeff_monomial(x**65 * y) == 0

    # --- q1 ODE ---
    pi, c, b0 = sp.symbols("pi c b0")
    q1_monic = (
        pi**10
        - (sp.Rational(15, 4)) * c * pi**8
        + 5 * c**2 * pi**6
        - (sp.Rational(5, 2)) * c**3 * pi**4
        + b0
    )
    p = pi * (pi**2 - c)
    q1p = sp.diff(q1_monic, pi)
    assert sp.expand((-sp.Rational(1, 5)) * q1p + 2 * p**3) == 0
    q1_driver = -pi**10 / 5 + sp.Rational(3, 4) * pi**8 - pi**6 + pi**4 / 2 + b0
    # at c=1 the monic * (-1/5) matches driver up to b0 rescale
    assert sp.expand((-sp.Rational(1, 5)) * q1_monic.subs(c, 1) - (q1_driver - b0) * 1) == (
        -b0 / 5
    )  # b0 rescale only
    out["q1_ode"] = {
        "monic_q1_prime_times_minus_1_5_plus_2p3": 0,
        "driver_q1_at_c1_matches_up_to_b0": True,
    }

    # --- delta=2 face ODE residual ---
    z, rho, k = sp.symbols("z rho k")
    p2 = z**2 * (z + 3 * rho)
    R = z**25 * (z + 3 * rho) ** 14 * (z - 2 * rho)
    lhs = sp.expand(2 * p2 * sp.diff(R, z) - 25 * sp.diff(p2, z) * R)
    # should be a constant multiple of p2**14
    p2_14 = sp.expand(p2**14)
    # lhs / p2^14 should be a nonzero constant in rho
    q_div, rem = sp.div(sp.Poly(lhs, z), sp.Poly(p2_14, z), domain=sp.QQ[rho])
    assert rem == 0
    ratio = sp.simplify(q_div.as_expr())
    assert ratio != 0 and ratio.free_symbols <= {rho} or ratio.free_symbols == set()
    # actually ratio should be independent of z; check numeric
    out["delta2_face_ode"] = {
        "remainder_after_p2_14": 0,
        "k_ratio": str(ratio),
        "family": "p2=z^2(z+3*rho), R=z^25(z+3*rho)^14(z-2*rho)",
    }

    # packets
    out["packets"] = {
        "delta2_F_Moh_g": (18, 9),
        "delta2_G_Moh_f": (12, 6),
        "delta52_F": (9, 9, 9),
        "delta52_G": (6, 6, 6),
        "sum_F": 27,
        "sum_G": 18,
    }

    # --- automorphism ---
    a = sp.symbols("a")
    Fauto = a * x + y
    Gauto = (a - 1) * x + y
    J = sp.expand(
        sp.diff(Fauto, x) * sp.diff(Gauto, y) - sp.diff(Fauto, y) * sp.diff(Gauto, x)
    )
    assert J == 1
    xx = Fauto - Gauto
    yy = a * Gauto - (a - 1) * Fauto
    assert sp.expand(xx) == x
    assert sp.expand(yy) == y
    A, C = sp.symbols("A C")
    F2, G2 = A * x + y, C * x + y
    J2 = sp.diff(F2, x) * sp.diff(G2, y) - sp.diff(F2, y) * sp.diff(G2, x)
    assert sp.expand(J2 - 1) == A - C - 1
    out["automorphism"] = {
        "J_identically_1": True,
        "inverse_recovers_xy": True,
        "ansatz_row": "A-C-1",
        "slice_A2_witness": ("2*x+y", "x+y"),
        "two_points": "P_F=[1:-a:0], P_G=[1:1-a:0]",
    }
    wF = sp.expand((2 * x + y).subs({x: 2 * x + y, y: x + y}))  # not needed
    Jw = sp.diff(2 * x + y, x) * sp.diff(x + y, y) - sp.diff(2 * x + y, y) * sp.diff(
        x + y, x
    )
    assert Jw == 1

    # --- (16,12) spine identity ---
    z = sp.symbols("z")
    left = (20 * z - sp.Rational(10, 3)) * (sp.Rational(27, 10) - sp.Rational(27, 5) * z) - 1
    right = -2 * (54 * z**2 - 36 * z + 5)
    assert sp.expand(left - right) == 0
    out["spine_1612"] = {
        "identity": True,
        "modulus": "54z^2-36z+5",
        "unit": "20z-10/3",
    }

    # p.208 coefficient count, printed-c5 reading
    # b1,b2,b3,b4, alpha1, c1,c2,c3,c4,c5,c7,c8,c9,c10,c11,c12,c13 = 17
    out["moh_p208_count"] = {
        "printed_repeated_c5_coefficients": 17,
        "plus_kappa": 18,
        "h": "y^3(y-x)+b1 y^3+b2 y^2+b3 y+b4",
        "keeps_alpha1_h3": True,
        "f_Tschirnhausen_no_h2": True,
    }

    # W3/W6 vs joint_probe
    z, rho = sp.symbols("z rho")
    W3 = -8 * z**4 - 18 * rho * z**3
    W6 = 28 * z**5 + 45 * rho * z**4
    probe3 = -2 * z**3 * (9 * rho + 4 * z)
    probe6 = z**4 * (45 * rho + 28 * z)
    assert sp.expand(W3 - probe3) == 0
    assert sp.expand(W6 - probe6) == 0
    out["W3W6_match_joint_probe"] = True

    path = HERE / "results.json"
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"wrote": str(path), "keys": sorted(out.keys())}, indent=2))


if __name__ == "__main__":
    main()
