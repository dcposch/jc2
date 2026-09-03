#!/usr/bin/env python3
"""Effective quasi-approximate-root bridge T2, T3 in K[f,g].

SOURCE-READ:
  Moh printed p.150: characteristic data {M_j, d_j}, n_j=d_j/d_{j+1},
    q1=M1, q_j=M_j-M_{j-1}, lambda_j = sum_{i<=j} q_i d_i, mu_j = lambda_j/d_j.
  Moh printed p.151: F(f,g) = prod_i (f - Omega_i(eta^{-m} + sum f_j eta^j)).
  Moh printed p.152: T_r^psi is the d_r-th approximate root of F^psi, with
    T_r^psi(f,g) = f^{n/d_r} + sum_{i=1}^{n/d_r} alpha_i(0,g) f^{n/d_r-i}
    and deg_y T_r^psi(f(x,y),g(x,y)) = -mu_r  (Prop 2.2, M_r <= e).
  Xu §7.3 (printed p.10): T_i(f,g) in K[f,g], T0=g, T1=f, deg T_i = -mu_i.

Chart convention: F = Moh g (deg 99), G = Moh f (deg 66), so
  T0 = F, T1 = G, T2 = T2^psi(G, F), T3 = T3^psi(G, F).

The alpha_i are polynomials in one variable of weighted degree
  deg alpha_i <= floor(m i / n) = floor(2i/3), because the i-th correction
  in F^{1/d_r} has y-weight m i.

Face evaluation on the minor leading forms (Xu §8 / design (2.4)(2.6))
cannot produce the T2 leader p^5 from the Tschirnhausen span of
{p^{18}, p^{15}, p^{12}, p^9, p^6, p^0}.  The p^5 (and the degree-40 T3
leader R or q) require subleading F,G jets.  That identification is
OPEN[EFFECTIVE-T2-T3-BRIDGE] as a complete linear row block.

For u_s=1 (the (64,48)->(16,12) control) the principal packet does not
split, T_i(sigma) are powers of a common linear polynomial by Xu Prop 7.3
/ Moh Prop 4.4, and the bridge is trivial.
"""
from __future__ import annotations

from math import gcd


def moh_mu_sequence(n: int, m: int, Ms: list[int]) -> dict:
    """Moh p.150 auxiliary sequence.  M1 = -m, then M2,...,Ms."""
    M = [-m] + list(Ms)
    s = len(M)
    d = [n]
    for idx in range(s):
        d.append(gcd(d[-1], M[idx]))
    q = [M[0]] + [M[j] - M[j - 1] for j in range(1, s)]
    lam = []
    acc = 0
    for j in range(s):
        acc += q[j] * d[j]
        lam.append(acc)
    assert all(lam[j] % d[j] == 0 for j in range(s))
    mu = [lam[j] // d[j] for j in range(s)]
    # n/d_r for r=1,2,... : T_r is the d_r-th approx root, degree n/d_r in f.
    n_over_d = [d[0] // d[j] for j in range(len(d))]
    return {
        "n": n,
        "m": m,
        "M": M,
        "d": d,
        "q": q,
        "lambda": lam,
        "mu": mu,
        "neg_mu": [-x for x in mu],
        "n_over_d_r": n_over_d,  # index 0 = n/d1 = 1 (T1=f); 1 = n/d2 = 3
    }


def alpha_coeff_count(n: int, m: int, n_over_d: int) -> dict:
    """Number of unknown k[g]-coefficients in T_r^psi = f^{n/d} + sum alpha_i(g) f^{n/d-i}.

    deg_g alpha_i <= floor(m i / n).
    """
    per_i = []
    total = 0
    for i in range(1, n_over_d + 1):
        deg = (m * i) // n
        n_coeff = deg + 1
        per_i.append({"i": i, "deg_g_bound": deg, "n_coeff": n_coeff})
        total += n_coeff
    leading_i = n_over_d
    leading_deg = (m * leading_i) // n
    # leading of alpha_{n/d} is the monomial g^{m n / (n d) wait}: y-weight
    # (n/d)*m = n m / d equals (n/d * m/n)*n = (m/d)*n = weight of g^{m/d}.
    # So [g^{m/d}] of alpha_{n/d} is the leading, fixed to -1 after monic cancel.
    return {
        "n_over_d": n_over_d,
        "per_i": per_i,
        "total_coeffs_including_leading": total,
        "leading_g_power": m * n_over_d // n,
        "unknown_after_monic_leading": total - 1,
        "unknown_after_Tschirnhausen_alpha1_zero": total - 1 - per_i[0]["n_coeff"],
    }


def t2_polynomial_shape() -> dict:
    """T2^psi in chart names.  n/d2 = 99/33 = 3, -mu2 = 55."""
    # T2 = G^3 + a(F) G^2 + b(F) G + c(F)
    # deg a <= floor(2/3)=0, deg b <= 1, deg c <= 2
    return {
        "formula_moh_p152": "T2^psi(f,g) = f^{n/d2} + alpha1(g) f^2 + alpha2(g) f + alpha3(g)",
        "chart": "T2 = G^3 + alpha1(F) G^2 + alpha2(F) G + alpha3(F)",
        "exponents": {"a": 3, "b": 2, "n": 99, "m": 66, "d2": 33, "neg_mu2": 55},
        "display": (
            "T2 = G^3 - F^2 "
            "+ c0 G^2 "
            "+ (a1 F + a0) G "
            "+ (b1 F + b0)"
        ),
        "unknown_coeffs_Moh_literal_including_leading": 6,
        "unknown_after_monic_G3_minus_F2": 5,
        "unknown_after_Tschirnhausen_alpha1_zero": 4,
        "monic_leading_identity": "[F^2] in alpha3 = -1, i.e. T2 ≡ G^3 - F^2 + lower",
        "y_degree_target": 55,
        "naive_y_degree_before_cancellation": 198,
    }


def t3_polynomial_shape() -> dict:
    """T3^psi.  n/d3 = 99/11 = 9, -mu3 = 145."""
    counts = alpha_coeff_count(99, 66, 9)
    return {
        "formula_moh_p152": "T3^psi(f,g) = f^{n/d3} + sum_{i=1}^{9} alpha_i(g) f^{9-i}",
        "chart": "T3 = G^9 + sum_{i=1}^{9} alpha_i(F) G^{9-i}",
        "exponents": {"n": 99, "m": 66, "d3": 11, "n_over_d3": 9, "neg_mu3": 145},
        "display": "T3 = G^9 - F^6 + sum_{k=0}^{8} p_k(F) G^k   (p_k = alpha_{9-k})",
        "alpha_degree_bounds": counts["per_i"],
        "unknown_coeffs_Moh_literal_including_leading": counts["total_coeffs_including_leading"],
        "unknown_after_monic_G9_minus_F6": counts["unknown_after_monic_leading"],
        "unknown_after_Tschirnhausen_alpha1_zero": counts["unknown_after_Tschirnhausen_alpha1_zero"],
        "monic_leading_identity": "[F^6] in alpha9 = -1, i.e. T3 ≡ G^9 - F^6 + lower",
        "y_degree_target": 145,
        "naive_y_degree_before_cancellation": 594,
        "principal_minor_multiplicity_Xu_73": 40,
    }


def face_span_obstruction() -> dict:
    """Weighted-homogeneous evaluation on (F,G)~(p^9, p^6) cannot make p^5."""
    # T2(p^6, p^9) after G^3-F^2 cancel lives in
    # span{ p^{15} (from F G), p^{12} (from G^2), p^9 (from F), p^6 (from G), p^0 }.
    span_T2 = [18, 15, 12, 9, 6, 0]
    target_T2 = 5
    span_T3 = [54, 48, 42, 36, 30, 24, 18, 12, 6, 0]  # G^9 ~ p^{54}, F^6 ~ p^{54}
    target_T3_delta2 = 40  # deg R = 40, not a pure power of p
    return {
        "minor_leaders_Xu_s8": {
            "F_Moh_g": "p^9",
            "G_Moh_f": "p^6",
            "T2": "p^5",
            "T3_delta2": "R = z^25 (z+3 rho)^14 (z-2 rho), deg 40",
            "T3_delta52": "q = p^{10} q1, deg q1 = 10, deg q = 40",
        },
        "T2_face_span_p_powers": span_T2,
        "T2_target_p_power": target_T2,
        "T2_target_in_face_span": target_T2 in span_T2,
        "T3_face_span_p_powers_homogeneous": span_T3,
        "T3_delta2_deg_R": target_T3_delta2,
        "conclusion": (
            "After the monic G^3-F^2 (resp. G^9-F^6) cancellation, the remaining "
            "Tschirnhausen span evaluated on the minor leading forms (p^9, p^6) "
            "does not contain p^5 nor a degree-40 polynomial with the (25,14) "
            "or p^{10} q1 shape.  Those leaders are residual, from subleading "
            "F,G jets.  Typed OPEN[EFFECTIVE-T2-T3-BRIDGE] as complete linear "
            "rows on the 7161-chart.  The polynomial *shape* of T2, T3 is PRINTED."
        ),
    }


def branch_bridge_targets() -> dict:
    return {
        "delta2": {
            "p": "z^2 (z+3 rho)",
            "T2_leader": "p^5",
            "T3_leader": "R = z^25 (z+3 rho)^14 (z-2 rho)",
            "face_ODE": "2 p R' - 25 p' R = 5 p^{14}   ('=d/dz)",
            "status": "OPEN[EFFECTIVE-T2-T3-BRIDGE]",
        },
        "delta52": {
            "p": "pi (pi^2 - c)",
            "T2_leader": "p^5",
            "T3_leader": "q = p^{10} q1, q1' = 10 p^3 (Xu normalisation), deg q1=10",
            "reduced_ODE": "D_s(Q,h) + 2 s^2 h^4 = 0  (charged; not T3 in K[F,G])",
            "status": "OPEN[EFFECTIVE-T2-T3-BRIDGE]",
        },
        "us_eq_1_triviality": {
            "statement": (
                "If u_s=1 the principal packet is a single Puiseux branch. "
                "Xu Prop 7.3 / Moh Prop 4.4 force T_i(sigma) to be powers of "
                "one linear polynomial.  There is no split leader R or q1 to "
                "identify, and no free T3 ODE.  The bridge is trivial."
            ),
            "applies_to": "(64,48) parent and reduced (16,12) Appendix II",
            "u_s_9966": 3,
        },
    }


def run() -> dict:
    data = moh_mu_sequence(99, 66, [77, 97])
    assert data["d"] == [99, 33, 11, 1]
    assert data["neg_mu"][0] == 66  # -mu1 = m = deg f = deg G
    assert data["neg_mu"][1] == 55
    assert data["neg_mu"][2] == 145
    assert data["n_over_d_r"][0] == 1  # T1 = f, degree 1 in f
    assert data["n_over_d_r"][1] == 3  # T2 degree 3 in f
    assert data["n_over_d_r"][2] == 9  # T3 degree 9 in f
    t2 = t2_polynomial_shape()
    t3 = t3_polynomial_shape()
    face = face_span_obstruction()
    assert face["T2_target_in_face_span"] is False
    return {
        "type": "DERIVED[T2-T3-SHAPE] / OPEN[EFFECTIVE-T2-T3-BRIDGE-ROWS]",
        "source": {
            "moh_p150_mu": "printed p.150 auxiliary mu from (q,d,lambda)",
            "moh_p152_Tpsi": "printed p.152 T_r^psi = truncation of F^{1/d_r}",
            "xu_s73": "printed p.10 T_i in K[f,g], T0=g, T1=f, deg=-mu_i",
        },
        "label_reversal": {
            "T0": "Moh g = chart F, deg 99",
            "T1": "Moh f = chart G, deg 66",
            "T2_in": "K[G, F] = K[f, g]",
            "T3_in": "K[G, F]",
        },
        "mu_sequence": {
            "M": data["M"],
            "d": data["d"],
            "q": data["q"],
            "lambda": data["lambda"],
            "mu": data["mu"],
            "neg_mu": data["neg_mu"],
            "n_over_d_r": data["n_over_d_r"],
        },
        "T2": t2,
        "T3": t3,
        "face_obstruction": face,
        "branch_targets": branch_bridge_targets(),
        "rows_emitted": {
            "shape_and_leading_monic": "PRINTED (2 leading identities G^3=F^2, G^9=F^6 on tops)",
            "unknown_T2_coeffs": t2["unknown_after_monic_G3_minus_F2"],
            "unknown_T3_coeffs": t3["unknown_after_monic_G9_minus_F6"],
            "pi_root_identification_with_H_and_R": "OPEN[EFFECTIVE-T2-T3-BRIDGE]",
            "linear_rows_on_7161_chart_from_bridge": 0,
        },
        "controls": {
            "mu2_55": data["neg_mu"][1] == 55,
            "mu3_145": data["neg_mu"][2] == 145,
            "d_chain": data["d"] == [99, 33, 11, 1],
            "face_p5_not_in_Tschirnhausen_span": True,
        },
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run(), indent=2, sort_keys=True))
