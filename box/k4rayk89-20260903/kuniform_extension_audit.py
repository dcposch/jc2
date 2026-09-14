#!/usr/bin/env python3
"""Exact, bounded REC3 audit for the next pinned rows K=10,11.

This is deliberately not a chart builder.  It verifies the closed PIN12-to-REC3
identity, records the resulting pointwise branch covers, and estimates the
post-RREF ring sizes before any expensive Groebner computation is attempted.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path

import sympy as sp


def theta_data(K: int) -> dict[str, object]:
    coeffs = [Fraction(1, 5 * K - 6)]
    for i in range(1, 5):
        coeffs.append(coeffs[-1] * Fraction((5 - i) * K, (5 - i) * K - 6))
    denominator = 1
    for coefficient in coeffs:
        denominator = lcm(denominator, coefficient.denominator)
    numerators = [coefficient.numerator * (denominator // coefficient.denominator) for coefficient in coeffs]
    common = 0
    for numerator in numerators:
        common = gcd(common, abs(numerator))
    return {
        "factor": f"y^{K}*(y-x)^2/{denominator // common}",
        "x4_through_y4_numerators": [numerator // common for numerator in numerators],
        "rational_coefficients": [str(coefficient) for coefficient in coeffs],
    }


def raw_geometric_count(K: int) -> int:
    h_count = (K - 1) * (K + 2) // 2
    beta_lower_count = (K - 2) * (K - 1) // 2
    return h_count + beta_lower_count + 1  # mu


def pin_count(K: int) -> int:
    p3_down = (K - 4) * (K - 3) // 2
    h3_down = (K - 2) * (K - 1) // 2
    return 1 + (K - 6) + (K - 7) + (K - 7) + (K - 3) + p3_down + h3_down


def rec3_identity(K: int) -> dict[str, object]:
    mu, y, L = sp.symbols("mu y L")
    tau, phi, chi, p2, p3, h3, q3 = sp.symbols("tau phi chi p2 p3 h3 q3")
    s = (K - 4) // 2  # ceil((K-5)/2), for integer K
    e = 2 * s - (K - 5)
    H = y ** (K - 1) * L
    P = mu * y ** (K - 3) * L
    p1 = 3 * y**4 * tau - y**s * L * phi
    h1 = 3 * y**6 * tau / mu - 3 * y ** (s + 2) * L * phi / (2 * mu)
    h2 = 3 * (mu * y**2 * p2 + sp.Rational(1, 4) * L * y**e * phi**2 - y**6 * chi) / (2 * mu**2)
    q0 = mu**3 * y ** (K - 7) * L
    q1 = 3 * mu**2 * tau
    q2 = 3 * mu * chi
    T3 = 3 * P**2 * p3 + 6 * P * p1 * p2 + p1**3
    S1 = 2 * H * h1
    S2 = 2 * H * h2 + h1**2
    S3 = 2 * H * h3 + 2 * h1 * h2
    residual = sp.expand(T3 - S1 * q2 - S2 * q1 - S3 * q0 - H**2 * q3)
    displayed_left = sp.expand(
        L * phi**3
        + 36 * chi * phi * y ** (6 - e)
        - 16 * mu**3 * h3 * y ** (2 * K - 3 * s - 8)
        + 24 * mu**2 * p3 * y ** (2 * K - 3 * s - 6)
        - 12 * mu * p2 * phi * y ** (2 - e)
        - 18 * phi**2 * tau * y ** (4 - s)
    )
    expected = sp.expand(L**2 * y ** (3 * s) * (displayed_left - 8 * q3 * y ** (2 * K - 3 * s - 2)) / 8)
    if sp.expand(residual - expected) != 0:
        raise AssertionError(f"REC3 factor identity failed at K={K}")
    return {
        "K": K,
        "s": s,
        "e": e,
        "factor_identity": "PASS",
        "common_factor": f"(y-x)^2*y^{3*s}/8",
        "equation_left": sp.sstr(displayed_left).replace("**", "^"),
        "equation_right": f"8*q3*y^{2 * K - 3 * s - 2}",
        "q3_degree": K - 9,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("topprobe-artifacts")
        / "kuniform-rec3"
        / "K10K11_REC3_V1"
        / "audit.json",
    )
    args = parser.parse_args()

    identities = {K: rec3_identity(K) for K in range(8, 12)}
    result = {
        "type": "K4RAY-KUNIFORM-REC3-EXACT-Q-AUDIT",
        "status": "EXACT_IDENTITIES_PASS_NO_GROEBNER_RUN",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "common_pin": {
            "s": "ceil((K-5)/2)",
            "psi": "y^s*phi",
            "deg_tau": "K-7",
            "deg_phi": "K-4-s",
            "deg_chi": "K-8",
            "monic_relation": "coeff_y^(deg phi)(phi)=2*coeff_y^(K-7)(tau)",
            "q0": "mu^3*y^(K-7)*(y-x)",
            "q1": "3*mu^2*tau",
            "q2": "3*mu*chi",
        },
        "rec3_identity_checks": identities,
        "K10": {
            "r": 4,
            "q_schedule": "q0..q3=3*rho4..rho1; q4=3*rho0+lambda; q5..q7=0; N8=Theta10",
            "after_phi_equals_yv": "polynomial h3 iff y divides p2*v",
            "exact_cover": ["A10: v=y*w", "B10: p2=y*zeta"],
            "overlap": "retained; no localization of v or p2",
            "h3": "(L*v^3+36*chi*v*y^3+24*mu^2*p3*y^2-12*mu*(p2*v/y)-18*v^2*tau-8*q3*y^6)/(16*mu^3)",
            "theta": theta_data(10),
            "counts": {
                "raw_geometric": raw_geometric_count(10),
                "after_PIN12": pin_count(10),
                "after_REC3_including_q3": 67,
                "predicted_after_full_rank_h4_through_h8_including_q4": 43,
                "predicted_solver_ring_with_mu_inv": 44,
                "terminal_recurrence_indices": [4, 5, 6, 7, 8],
                "split_chart_count": 2,
            },
        },
        "K11": {
            "r": 5,
            "q_schedule": "q0..q4=3*rho5..rho1; q5=3*rho0+lambda; q6..q9=0; N10=Theta11",
            "after_phi_equals_yv": "polynomial h3 iff y^2 divides v*W, W=(y-x)*v^2-18*v*tau-12*mu*p2",
            "exact_cover": [
                "A11: v=y^2*w",
                "B11: v=y*v1 and W=y*zeta",
                "C11: W=y^2*zeta",
            ],
            "overlap": "retained; valuation cases ord_y(v)>=2, ord_y(v)=1, ord_y(v)=0 are covered without localization",
            "h3": "(omega+36*chi*v*y^2+24*mu^2*p3*y^2-8*q3*y^6)/(16*mu^3), omega=v*W/y^2",
            "theta": theta_data(11),
            "counts": {
                "raw_geometric": raw_geometric_count(11),
                "after_PIN12": pin_count(11),
                "after_REC3_including_q3": 86,
                "predicted_after_full_rank_h4_through_h10_including_q4_q5": 54,
                "predicted_solver_ring_with_mu_inv": 55,
                "terminal_recurrence_indices": [4, 5, 6, 7, 8, 9, 10],
                "split_chart_count": 3,
            },
        },
        "decision": {
            "full_chart_built": False,
            "groebner_run": False,
            "reason": "not a cheap reuse: PIN exponent changes at K=10; K10 needs two new charts and five terminal bands, K11 needs three valuation charts and seven terminal bands; K9 one-core exact construction already cost 205s/368s for only three terminal bands",
            "next_builder_target": "implement branch-aware constant-Q RREF for N4..N_(2r), then sparse alpha/remainder matching through rho degree 1 before any modular screen",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output": str(args.output.resolve()), "status": result["status"]}, sort_keys=True))


if __name__ == "__main__":
    main()
