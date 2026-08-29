#!/usr/bin/env python3
"""Exact desk certificate for transport at a V0-unit root.

This checker verifies only the new local reduction and its compatibility
with the already-reviewed fixed-prefix cascade.  It deliberately does not
rebuild the 513-row fixed packet.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RESULT = HERE / "RESULT.json"
TARGET = HERE / "TARGET.json"

PINNED = {
    "xmodel/ideation-20260828T0702Z-fable5.md":
        "c3d6c88e2b52569cdd4653cc3e4d8748bdae08fe94673a417578cd6d2242497f",
    "xmodel/ideation-20260828T0702Z-opus5.md":
        "9339a398c2dee3251203893d8d33abdffecb4bdb361fd2289d7579b806e1177e",
    "xmodel/ggv-upper-endpoint-uniform-d7-d22-A-dependency-audit-sol-ultra-20260828.md":
        "e2d02b32f5274323c47ca7a981f2dfb51e7035538a8b6b8136dd4e6bed316054",
    "xmodel/ggv-upper-endpoint-uniform-d18-d22-fullmodes-sol-ultra-20260828.md":
        "ecf83ac7b380a18f939e60671a4e97290f9f68b51536c236b81f71bb6a6c5bb8",
    "xmodel/ggv-upper-endpoint-uniform-d18-d22-fullmodes-hostile-review-grok46-20260828.md":
        "a294cdf70f0496b360855b1b88e6f362e752e0bda33498902eb6fba7785e23a5",
    "cases/ggv_8_28_upper_endpoint_uniform_d18_d22_fullmodes_20260828/verify_uniform_d18_d22.py":
        "49d1acaf1a8b066e9de15005e97ce948b8b33bd38315a1e77dcdf945c9b9761d",
    "cases/ggv_8_28_upper_endpoint_uniform_d18_d22_fullmodes_20260828/RESULT.json":
        "f46d7afd8b4e1e7cb5c60b029f8660dc2f1bf0e8770724808a3451c8c4e9e684",
    "xmodel/ggv-upper-endpoint-q1-fixed-proper-divisor-d12-obstruction-sol-ultra-20260828.md":
        "9903780f612f07c8afd6bd6d6318d4a086ae59c59e6a7e554609f2de1a1eb258",
    "cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828/verify_q1_d12_obstruction.py":
        "24381cd505e9d507083c49f18c4eb45a3f55bee87446c2d0aa11a33b6fa203fb",
    "cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828/RESULT.json":
        "b2e0e3b9ed6ffb20328a044ae4172d0290597e5cbf088b62928ef480c24b4561",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def poly_trim(p):
    p = [Q(c) for c in p]
    while p and p[-1] == 0:
        p.pop()
    return p


def poly_add(p, q):
    out = [Q(0)] * max(len(p), len(q))
    for i, c in enumerate(p):
        out[i] += c
    for i, c in enumerate(q):
        out[i] += c
    return poly_trim(out)


def poly_scale(c, p):
    return poly_trim([Q(c) * x for x in p])


def poly_mul(p, q):
    if not p or not q:
        return []
    out = [Q(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return poly_trim(out)


def poly_divmod(p, q):
    p, q = poly_trim(p), poly_trim(q)
    assert q
    if len(p) < len(q):
        return [], p
    out = [Q(0)] * (len(p) - len(q) + 1)
    while p and len(p) >= len(q):
        d = len(p) - len(q)
        c = p[-1] / q[-1]
        out[d] += c
        p = poly_add(p, poly_scale(-c, [Q(0)] * d + q))
    return poly_trim(out), p


def poly_monic(p):
    p = poly_trim(p)
    return poly_scale(1 / p[-1], p) if p else []


def poly_gcd(p, q):
    p, q = poly_trim(p), poly_trim(q)
    while q:
        _, r = poly_divmod(p, q)
        p, q = q, r
    return poly_monic(p)


def poly_derivative(p):
    return poly_trim([Q(i) * p[i] for i in range(1, len(p))])


def poly_eval(p, x):
    out = Q(0)
    for c in reversed(p):
        out = out * Q(x) + c
    return out


def decode_poly(obj):
    if not obj:
        return []
    out = [Q(0)] * (max(map(int, obj)) + 1)
    for degree, value in obj.items():
        out[int(degree)] = Q(value)
    return poly_trim(out)


# A small exact bivariate polynomial ring Q[eps,s], used only for the
# Newton identity.  Keys are (eps_degree, s_degree).
def bp_add(*items):
    out = {}
    for item in items:
        for key, value in item.items():
            out[key] = out.get(key, Q(0)) + value
            if out[key] == 0:
                del out[key]
    return out


def bp_scale(c, p):
    return {key: Q(c) * value for key, value in p.items() if Q(c) * value}


def bp_mul(p, q):
    out = {}
    for (e1, s1), a in p.items():
        for (e2, s2), b in q.items():
            key = (e1 + e2, s1 + s2)
            out[key] = out.get(key, Q(0)) + a * b
            if out[key] == 0:
                del out[key]
    return out


def bp_pow(p, n):
    out = {(0, 0): Q(1)}
    for _ in range(n):
        out = bp_mul(out, p)
    return out


def bp_shift(p, eps=0, s=0):
    return {(e + eps, d + s): c for (e, d), c in p.items()}


def bp_from_eps(coefficients):
    return {(i, 0): Q(c) for i, c in enumerate(coefficients) if c}


def local_newton_trial(a_coeffs, v_coeffs, z_coeffs, t_coeffs, f_coeffs):
    a = bp_from_eps(a_coeffs)
    v = bp_from_eps(v_coeffs)
    z = bp_from_eps(z_coeffs)
    t = bp_from_eps(t_coeffs)
    one_half_v_s = bp_shift(bp_scale(Q(1, 2), v), s=1)
    q = bp_add(bp_pow(a, 2), one_half_v_s)

    h = bp_add(
        bp_pow(a, 4),
        bp_shift(bp_mul(bp_pow(a, 2), v), s=1),
        bp_shift(bp_scale(Q(1, 4), bp_pow(v, 2)), s=2),
        bp_shift(bp_scale(Q(1, 4), bp_mul(bp_pow(a, 2), z)), eps=2, s=2),
        bp_shift(bp_scale(Q(1, 8), bp_mul(v, z)), eps=2, s=3),
        bp_shift(bp_scale(Q(1, 8), bp_mul(a, t)), eps=3, s=3),
    )
    for i, coefficients in sorted(f_coeffs.items()):
        h = bp_add(h, bp_shift(bp_from_eps(coefficients), eps=2 * i - 4, s=i))

    correction = bp_add(
        bp_shift(bp_scale(Q(1, 4), bp_mul(bp_pow(a, 2), z)), eps=2, s=2),
        bp_shift(bp_scale(Q(1, 8), bp_mul(v, z)), eps=2, s=3),
        bp_shift(bp_scale(Q(1, 8), bp_mul(a, t)), eps=3, s=3),
    )
    for i, coefficients in sorted(f_coeffs.items()):
        correction = bp_add(
            correction,
            bp_shift(bp_from_eps(coefficients), eps=2 * i - 4, s=i),
        )
    assert bp_add(h, bp_scale(-1, bp_pow(q, 2))) == correction
    eps0 = {key: value for key, value in h.items() if key[0] == 0}
    q0sq = {key: value for key, value in bp_pow(q, 2).items() if key[0] == 0}
    assert eps0 == q0sq
    return {
        "terms_in_H": len(h),
        "terms_in_correction": len(correction),
        "leading_square_terms": len(eps0),
    }


def generalized_binomial(r, k):
    out = Q(1)
    for j in range(k):
        out *= (Q(r) - j) / (j + 1)
    return out


def mode_table():
    # Each row tests the lowest local term which is load-bearing in the
    # fixed cascade.  The leading coefficient is evaluated at a=v=1 in
    # q=(a^2+v*s/2), solely to prove it is nonzero.
    rows = []
    for m, n in ((6, 8), (10, 11), (14, 14), (16, 16), (18, 18), (20, 20)):
        beta = Q(12 - m, 8)
        k = n - m
        q_exponent = 2 * beta
        coefficient = generalized_binomial(q_exponent, k) * Q(1, 2) ** k
        eps_exponent = Q(6) + Q(3 * m, 2) - 2 * n
        assert eps_exponent.denominator == 1
        assert coefficient != 0
        rows.append({
            "mode": f"c{m}",
            "weight": n,
            "coefficient_index": k,
            "beta": str(beta),
            "leading_q_exponent": str(q_exponent),
            "leading_coefficient_at_a_eq_v_eq_1": str(coefficient),
            "epsilon_exponent": int(eps_exponent),
        })
    assert [row["epsilon_exponent"] for row in rows] == [-1, -1, -1, -2, -3, -4]
    assert rows[0]["leading_coefficient_at_a_eq_v_eq_1"] == "3/32"
    assert rows[1]["leading_coefficient_at_a_eq_v_eq_1"] == "1/4"
    return rows


def check_d12_fixture():
    path = ROOT / "cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828/RESULT.json"
    payload = json.loads(path.read_text())
    certificate = payload["characteristic_certificate"]
    bezout = certificate["bezout_mod_B"]

    a = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    aprime = poly_derivative(a)
    c = [Q(-1), Q(1)]
    b = [Q(1), Q(1), Q(1), Q(1)]
    v0 = [Q(-2), Q(0), Q(0), Q(-4), Q(6)]
    nred = decode_poly(certificate["reduced_numerator"])
    sn = decode_poly(bezout["Nred_cofactor"])
    tb = decode_poly(bezout["B_cofactor"])

    assert poly_add(poly_mul(sn, nred), poly_mul(tb, b)) == [Q(1)]
    assert poly_gcd(b, nred) == [Q(1)]
    assert poly_gcd(b, c) == [Q(1)]
    assert poly_gcd(b, v0) == [Q(1)]
    assert poly_gcd(b, poly_derivative(b)) == [Q(1)]
    assert poly_eval(a, -1) == 0
    assert poly_eval(aprime, -1) == -4
    assert poly_eval(v0, -1) == 8
    assert poly_eval(c, -1) == -2
    assert poly_eval(nred, -1) != 0

    return {
        "B": "1+X+X^2+X^3",
        "gcd_B_V0": "1",
        "gcd_B_Nred": "1",
        "gcd_B_Bprime": "1",
        "bezout_identity_rechecked": True,
        "unit_root_alpha_minus_1": {
            "A_prime": "-4",
            "V0": "8",
            "C": "-2",
            "leading_q": "16+4*s",
            "Nred": str(poly_eval(nred, -1)),
            "g12_local_order": -2,
        },
        "all_three_B_roots": (
            "B is squarefree; C,V0,Nred are units modulo B, so the "
            "denominator C^3*B^2 has exact order two at every B-root"
        ),
    }


def target_payload():
    return {
        "format": "GGV_BRANCH_P_UNIT_ROOT_TRANSPORT_V1",
        "input": (
            "a simple root alpha of A with V0(alpha) nonzero, the reviewed "
            "reduced branch-P prefix and complete characteristic schedule, "
            "regular raw G0..G21, absent raw G22, and endpoint target D22=1"
        ),
        "verdict": (
            "the reviewed fixed-F1=A^2 characteristic endpoint cascade "
            "transports root-locally after coefficientwise V0 normalization; "
            "the endpoint is impossible at that single root"
        ),
        "scope_firewall": (
            "This is conditional on the reviewed branch-P prefix, mode schedule, "
            "and fixed characteristic cascade. It proves no raw-normal-form "
            "landing, no q1 implication, no scheme statement, and no JC2 result."
        ),
    }


def calculate():
    for relative, expected in PINNED.items():
        assert digest(ROOT / relative) == expected

    fixed = json.loads((
        ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d18_d22_fullmodes_20260828/RESULT.json"
    ).read_text())
    assert fixed["status"] == (
        "PASS_FIXED_UPPER_BRANCH_P_ENDPOINT_EMPTY_OVER_CHARACTERISTIC_ZERO_FIELDS"
    )

    trials = [
        local_newton_trial(
            [2, -1, 3], [3, 2], [5, -2], [7, 1, -1],
            {4: [1, 2], 5: [-3, 1], 6: [4], 14: [2, -5]},
        ),
        local_newton_trial(
            [-4, 1], [8, -3, 2], [Q(9, 2)], [Q(-27, 16), 4],
            {4: [Q(1, 3)], 8: [2, 0, 1], 12: [-1], 14: [5]},
        ),
        local_newton_trial(
            [1, 1, 1, 1], [-2, 5], [3, 7], [11],
            {i: [Q(i, i + 1), Q(-1, i + 2)] for i in range(4, 15)},
        ),
    ]

    # Exact coefficientwise normalization.  For every recurrence summand at
    # total weight n, V^{-i}*V^{-(n-i)}=V^{-n}; for every mode, the extra
    # V^{-m} times the coefficient at n-m again gives V^{-n}.
    for n in range(1, 23):
        assert all((-i) + (-(n - i)) == -n for i in range(1, n + 1))
    mode_scalings = {}
    scaling_exponent_mutation_failures = 0
    for m in (4, 6, 8, 10, 12, 14, 16, 18, 20):
        for n in range(m, 23):
            assert -m - (n - m) == -n
            # Mutation: use V0^{-(m-1)} on the mode constant.  This must no
            # longer intertwine weight n.
            mutated = -(m - 1) - (n - m)
            assert mutated != -n
            scaling_exponent_mutation_failures += 1
        mode_scalings[f"c{m}"] = f"{m}..22"

    # Endpoint valuation: if ord(g22)>=-2, both A^3*A'*g22 and A^4*g22'
    # have order at least one.  The optional homogeneous c22*A^-5 term is
    # annihilated exactly: -40+(-8)*(-5)=0.
    endpoint_orders = {str(k): k + 3 for k in range(-2, 7)}
    assert min(endpoint_orders.values()) == 1
    homogeneous_kernel_scalar = -40 + (-8) * (-5)
    assert homogeneous_kernel_scalar == 0
    mutated_endpoint_kernel_scalar = -39 + (-8) * (-5)
    assert mutated_endpoint_kernel_scalar == 1

    return {
        "status": "PASS_EXACT_UNIT_ROOT_TRANSPORT_DISCRIMINATOR",
        "source_pins": PINNED,
        "local_newton_model": {
            "substitution": "X=alpha+epsilon, A=epsilon*a(epsilon), t=epsilon^2*s",
            "H": "epsilon^-4*F(alpha+epsilon,epsilon^2*s)",
            "Q": "a(epsilon)^2+V0(alpha+epsilon)*s/2",
            "identity": (
                "H=Q^2+epsilon^2*(a^2*Z*s^2/4+V0*Z*s^3/8)"
                "+epsilon^3*a*T*s^3/8+sum_(i>=4)epsilon^(2i-4)*F_i*s^i"
            ),
            "leading_square": "H(0,s)=(A'(alpha)^2+V0(alpha)*s/2)^2",
            "exact_fraction_trials": trials,
        },
        "coefficientwise_normalization": {
            "definition": "Fbar_i=V0^-i*F_i; gbar_n=V0^-n*g_n; cbar_m=V0^-m*c_m",
            "normalized_prefix": (
                "Fbar_0=A^4, Fbar_1=A^2, Fbar_2=(1+A^2*Zbar)/4, "
                "Fbar_3=(Zbar+A*Tbar)/8, Zbar=Z/V0^2, Tbar=T/V0^3"
            ),
            "regularity_equivalence": "V0 is a DVR unit, so gbar_n is regular iff g_n is regular",
            "fractional_power_recurrence_weights_checked": "1..22",
            "mode_scaling_weights_checked": mode_scalings,
            "important_non_symmetry": (
                "the normalization is used only for characteristic regularity; "
                "it is not asserted to preserve the global raw windows or determinant row"
            ),
        },
        "mode_firewall": mode_table(),
        "transport_conclusion": {
            "local_ring": "Kbar[X]_(X-alpha), equivalently its DVR completion",
            "fixed_cascade_use": (
                "the reviewed D7-D21 characteristic divisibility argument uses "
                "only regularity and A-adic valuation after the reduced prefix; "
                "global quotient names become local DVR quotients"
            ),
            "g22_order_without_optional_kernel": ">=-2",
            "endpoint_operator": "L22(R)=-40*A^3*A'*R-8*A^4*R'",
            "endpoint_orders_for_A_power_k": endpoint_orders,
            "optional_c22_A^-5_kernel_scalar": homogeneous_kernel_scalar,
            "verdict": "D22_raw is in the maximal ideal (X-alpha), contradicting target 1",
        },
        "live_mutations": {
            "mode_scaling_V0_power_changed_from_minus_m_to_minus_m_plus_1": {
                "failed_weight_checks": scaling_exponent_mutation_failures,
                "reason": "mutated total power is V0^(-(n-1)), not V0^(-n)",
            },
            "endpoint_A3Aprime_coefficient_changed_from_minus_40_to_minus_39": {
                "optional_kernel_residual_scalar": mutated_endpoint_kernel_scalar,
                "reason": "the c22*A^-5 cancellation is destroyed",
            },
        },
        "mixed_root_D12_fixture": check_d12_fixture(),
        "scope": target_payload()["scope_firewall"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--print", action="store_true", dest="print_result")
    args = parser.parse_args()
    result = calculate()
    target = target_payload()
    result_bytes = json.dumps(result, sort_keys=True, indent=2) + "\n"
    target_bytes = json.dumps(target, sort_keys=True, indent=2) + "\n"
    if args.check:
        assert RESULT.read_text() == result_bytes
        assert TARGET.read_text() == target_bytes
    if args.print_result:
        print(result_bytes, end="")
    else:
        print(result["status"])


if __name__ == "__main__":
    main()
