#!/usr/bin/env python3
"""Exact desk certificate for the full-fixture uniform D9 defect.

The calculation uses only ``fractions.Fraction``.  It has two independent
parts:

* a sparse Laurent-polynomial recurrence for the complete characteristic
  continuation through weight nine; and
* literal evaluation of the pinned 513-generator raw JSON on two source-level
  mutations that fix the signs of the D8 mode obstruction and D9 square
  obstruction.

No CAS, numerical interpolation, root evaluation, or cutoff specialization is
used.  The negative modes born at weights 14,16,18,20 are kept in the serialized
mode schedule; causality certifies that their weight-nine support is empty.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RAW = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
CROSSCHECK = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/CHARACTERISTIC_CROSSCHECK.md"
UNIFORM_AUDIT = ROOT / "xmodel/ggv-upper-endpoint-uniform-tail-local-obstruction-hostile-audit-sol-ultra-20260828.md"
FULLMODE_AUDIT = ROOT / "xmodel/ggv-upper-endpoint-tail2-fullfixture-ideation-hostile-audit-sol-ultra-20260828.md"
RESULT = HERE / "RESULT.json"

RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"

# These record the exact contextual bytes consulted.  Unlike the raw source,
# CHARACTERISTIC_CROSSCHECK.md is a living firewall and is expected to gain
# reviewed successor rows, so replay does not require its live file to remain
# byte-identical to this historical pin.
CONTEXT_PINS = {
    CROSSCHECK: "e74ce3db552e34585c7a312d2e7bb093beca1da6d6afd4ff8ffa830bfe61c56a",
    UNIFORM_AUDIT: "d2ab35e1d417645d597070df8b1d75cf50cd062307a5a4a88988712cbf148192",
    FULLMODE_AUDIT: "a080f03b0656561b6b7f0b4d1ecd856c2d2fa99c45dc1bee75c29f397665de6a",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# A Laurent polynomial is keyed by (A-exponent, sorted commutative monomial).
# Symbols z,v,w,f5,... stand for arbitrary polynomials in X.  The fractional
# power recurrence itself contains no X derivative, so they may be treated as
# algebraically independent commuting indeterminates here.
def lp_const(value=0):
    value = Q(value)
    return {(0, ()): value} if value else {}


def lp_var(name):
    return {(0, (name,)): Q(1)}


def lp_A(exponent=1):
    return {(exponent, ()): Q(1)}


def lp_add(*polys):
    out = {}
    for poly in polys:
        for monomial, coefficient in poly.items():
            out[monomial] = out.get(monomial, Q(0)) + coefficient
            if not out[monomial]:
                del out[monomial]
    return out


def lp_neg(poly):
    return {monomial: -coefficient for monomial, coefficient in poly.items()}


def lp_sub(left, right):
    return lp_add(left, lp_neg(right))


def lp_scale(value, poly):
    value = Q(value)
    return {monomial: value * coefficient for monomial, coefficient in poly.items()
            if value * coefficient}


def lp_mul(left, right):
    out = {}
    for (a, m), coefficient in left.items():
        for (b, n), other in right.items():
            monomial = (a + b, tuple(sorted(m + n)))
            out[monomial] = out.get(monomial, Q(0)) + coefficient * other
            if not out[monomial]:
                del out[monomial]
    return out


def lp_shift(exponent, poly):
    return {(a + exponent, monomial): coefficient
            for (a, monomial), coefficient in poly.items()}


def lp_mod_A(exponent, poly):
    return {(a, monomial): coefficient for (a, monomial), coefficient in poly.items()
            if a < exponent}


def lp_terms(poly):
    return [
        {"A_exponent": exponent, "coefficient": str(coefficient), "monomial": list(monomial)}
        for (exponent, monomial), coefficient in sorted(poly.items())
    ]


DERIVATIVE_SYMBOL = {
    "z": "dz", "v": "dv", "w": "dw",
    "f5": "df5", "f6": "df6", "f7": "df7", "f8": "df8", "f9": "df9",
    "ap": "d_ap",
}


def lp_derivative(poly):
    """Formal X derivative with A'=ap and c4,c6,c8 constant."""
    out = {}
    for (exponent, monomial), coefficient in poly.items():
        if exponent:
            term = (exponent - 1, tuple(sorted(monomial + ("ap",))))
            out[term] = out.get(term, Q(0)) + coefficient * exponent
        for index, symbol in enumerate(monomial):
            derivative = DERIVATIVE_SYMBOL.get(symbol)
            if derivative is None:
                continue
            changed = list(monomial)
            changed[index] = derivative
            term = (exponent, tuple(sorted(changed)))
            out[term] = out.get(term, Q(0)) + coefficient
    return {monomial: coefficient for monomial, coefficient in out.items() if coefficient}


def L(weight, poly):
    # L_n(R)=4(12-n)A^3 A'R-8A^4 R'.
    first = lp_scale(4 * (12 - weight), lp_mul(lp_shift(3, poly), lp_var("ap")))
    second = lp_scale(-8, lp_shift(4, lp_derivative(poly)))
    return lp_add(first, second)


def characteristic_calculation():
    z, v, w = lp_var("z"), lp_var("v"), lp_var("w")
    f = {index: lp_var(f"f{index}") for index in range(5, 10)}
    c4, c6, c8 = lp_var("c4"), lp_var("c6"), lp_var("c8")

    # This is exactly the post-D7/post-leading-D8 substitution
    # T=A*V and F4-V/16-Z^2/64=A*W.
    F = {
        0: lp_A(4),
        1: lp_A(2),
        2: lp_add(lp_const(Q(1, 4)), lp_scale(Q(1, 4), lp_mul(lp_A(2), z))),
        3: lp_add(lp_scale(Q(1, 8), z), lp_scale(Q(1, 8), lp_mul(lp_A(2), v))),
        4: lp_add(lp_scale(Q(1, 16), v),
                  lp_scale(Q(1, 64), lp_mul(z, z)), lp_mul(lp_A(), w)),
        **f,
    }

    def fractional(alpha, maximum):
        y = {0: lp_A(int(4 * alpha))}
        for n in range(1, maximum + 1):
            rhs = {}
            for i in range(1, n + 1):
                coefficient = (alpha + 1) * i - n
                rhs = lp_add(rhs, lp_scale(coefficient, lp_mul(F[i], y[n - i])))
            y[n] = lp_scale(Q(1, n), lp_shift(-4, rhs))
        return y

    base = fractional(Q(3, 2), 9)
    three_quarters = fractional(Q(3, 4), 3)
    square_root = fractional(Q(1, 2), 1)

    expected_b7 = lp_add(
        lp_scale(Q(3, 16), lp_mul(f[5], z)), lp_scale(Q(3, 4), f[6]),
        lp_scale(Q(3, 1024), lp_mul(v, v)),
        lp_scale(Q(3, 32), lp_mul(lp_A(), lp_mul(v, w))),
        lp_scale(Q(3, 2), lp_mul(lp_A(2), f[7])),
    )
    expected_b8 = lp_add(
        lp_scale(Q(3, 32), lp_mul(f[5], v)),
        lp_scale(Q(3, 16), lp_mul(f[6], z)), lp_scale(Q(3, 4), f[7]),
        lp_scale(Q(-3, 4096), lp_mul(lp_mul(v, v), z)),
        lp_scale(Q(3, 8), lp_mul(w, w)),
        lp_scale(Q(3, 2), lp_mul(lp_A(2), f[8])),
    )
    expected_b9 = lp_add(
        lp_scale(Q(-3, 16), lp_shift(-2, lp_mul(w, w))),
        lp_scale(Q(3, 4), lp_shift(-1, lp_mul(f[5], w))),
        lp_scale(Q(-3, 256), lp_shift(-1, lp_mul(lp_mul(v, w), z))),
        lp_scale(Q(3, 32), lp_mul(f[6], v)),
        lp_scale(Q(3, 16), lp_mul(f[7], z)), lp_scale(Q(3, 4), f[8]),
        lp_scale(Q(-1, 8192), lp_mul(lp_mul(v, v), v)),
        lp_scale(Q(3, 2), lp_mul(lp_A(2), f[9])),
    )
    expected_y2 = lp_add(lp_scale(Q(3, 32), lp_A(-1)),
                         lp_scale(Q(3, 16), lp_mul(lp_A(), z)))
    expected_y3 = lp_add(lp_scale(Q(-1, 128), lp_A(-3)),
                         lp_scale(Q(3, 64), lp_shift(-1, z)),
                         lp_scale(Q(3, 32), lp_mul(lp_A(), v)))

    assert base[7] == expected_b7
    assert base[8] == expected_b8
    assert base[9] == expected_b9
    assert three_quarters[2] == expected_y2
    assert three_quarters[3] == expected_y3
    assert square_root[1] == lp_const(Q(1, 2))

    g8 = lp_add(base[8], lp_mul(c4, F[4]), lp_mul(c6, three_quarters[2]),
                lp_mul(c8, square_root[0]))
    g9 = lp_add(base[9], lp_mul(c4, F[5]), lp_mul(c6, three_quarters[3]),
                lp_mul(c8, square_root[1]))
    negative_g8 = {key: value for key, value in g8.items() if key[0] < 0}
    negative_g9 = {key: value for key, value in g9.items() if key[0] < 0}
    assert negative_g8 == lp_scale(Q(3, 32), lp_shift(-1, c6))

    expected_negative_g9 = lp_add(
        lp_scale(Q(-1, 128), lp_shift(-3, c6)),
        lp_scale(Q(-3, 16), lp_shift(-2, lp_mul(w, w))),
        lp_scale(Q(3, 64), lp_shift(-1, lp_mul(c6, z))),
        lp_scale(Q(3, 4), lp_shift(-1, lp_mul(f[5], w))),
        lp_scale(Q(-3, 256), lp_shift(-1, lp_mul(lp_mul(v, w), z))),
    )
    assert negative_g9 == expected_negative_g9

    # Once g8 is polynomial, its only polar term forces c6=0.  Under that
    # conclusion, apply the exact same-row operator and retain the relevant
    # A-adic classes of the raw rows D=-L(phi).
    d8_mod_a3 = lp_mod_A(3, lp_neg(L(8, negative_g8)))
    expected_d8 = lp_scale(Q(-9, 4), lp_mul(lp_A(2), lp_mul(lp_var("ap"), c6)))
    assert d8_mod_a3 == expected_d8

    negative_g9_c6_zero = {
        (exponent, tuple(symbol for symbol in monomial if symbol != "c6")): coefficient
        for (exponent, monomial), coefficient in negative_g9.items()
        if "c6" not in monomial
    }
    d9_mod_a2 = lp_mod_A(2, lp_neg(L(9, negative_g9_c6_zero)))
    expected_d9 = lp_scale(Q(21, 4),
                           lp_mul(lp_A(), lp_mul(lp_var("ap"), lp_mul(w, w))))
    assert d9_mod_a2 == expected_d9

    return {
        "post_substitution": {
            "T": "A*V",
            "F4": "V/16+Z^2/64+A*W",
        },
        "fractional_recurrence": (
            "n*A^4*y_n=sum_{1<=i<=n}(((alpha+1)*i-n)*F_i*y_{n-i})"
        ),
        "base_F_three_halves": {
            "weight7": lp_terms(base[7]),
            "weight8": lp_terms(base[8]),
            "weight9": lp_terms(base[9]),
        },
        "mode_coefficients": {
            "F_three_quarters_weight2": lp_terms(three_quarters[2]),
            "F_three_quarters_weight3": lp_terms(three_quarters[3]),
            "F_one_half_weight1": lp_terms(square_root[1]),
        },
        "full_negative_parts": {
            "g8": lp_terms(negative_g8),
            "g9_before_D8_mode_kill": lp_terms(negative_g9),
            "g9_after_c6_zero": lp_terms(negative_g9_c6_zero),
        },
        "raw_row_congruences": {
            "D8_mod_A3": lp_terms(d8_mod_a3),
            "D9_mod_A2_after_c6_zero": lp_terms(d9_mod_a2),
        },
    }


# Independent literal raw replay: ordinary univariate Q[X] arithmetic.
def trim(poly):
    out = list(poly)
    while out and not out[-1]:
        out.pop()
    return out


def xadd(left, right):
    return trim([
        (left[index] if index < len(left) else Q(0))
        + (right[index] if index < len(right) else Q(0))
        for index in range(max(len(left), len(right)))
    ])


def xscale(value, poly):
    return trim([Q(value) * coefficient for coefficient in poly])


def xmul(left, right):
    if not left or not right:
        return []
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, coefficient in enumerate(left):
        for j, other in enumerate(right):
            out[i + j] += coefficient * other
    return trim(out)


def xder(poly):
    return trim([Q(index) * poly[index] for index in range(1, len(poly))])


def xpow(poly, exponent):
    out = [Q(1)]
    base = list(poly)
    while exponent:
        if exponent & 1:
            out = xmul(out, base)
        base = xmul(base, base)
        exponent //= 2
    return out


def encode_xpoly(poly):
    return {str(index): str(coefficient) for index, coefficient in enumerate(poly) if coefficient}


def set_window(raw, values, kind, weight, poly):
    window = raw["windows"][kind][str(weight)]
    for degree, slot in zip(range(window["lower"], window["upper"] + 1), window["slots"]):
        values[slot] = poly[degree] if degree < len(poly) else Q(0)


def reconstruct(raw, values):
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    H = xpow(A, 2)
    Z = [values.get(f"z_{degree}", Q(0)) for degree in range(7)]
    T = [values.get(f"tt_{degree}", Q(0)) for degree in range(10)]
    F = {
        0: xpow(H, 2),
        1: H,
        2: xscale(Q(1, 4), xadd([Q(1)], xmul(H, Z))),
        3: xscale(Q(1, 8), xadd(Z, xmul(A, T))),
    }
    G = {0: xpow(H, 3), 1: xscale(Q(3, 2), xpow(H, 2))}
    G[2] = xadd(xscale(Q(3, 2), xmul(H, F[2])), xscale(Q(3, 8), H))
    G[3] = xadd(xadd(xscale(Q(3, 2), xmul(H, F[3])),
                     xscale(Q(3, 4), F[2])), [Q(-1, 16)])
    for kind, target, weights in (("F", F, range(4, 15)), ("G", G, range(4, 22))):
        for weight in weights:
            window = raw["windows"][kind][str(weight)]
            poly = [Q(0)] * (window["upper"] + 1)
            for degree, slot in zip(range(window["lower"], window["upper"] + 1),
                                    window["slots"]):
                poly[degree] = values.get(slot, Q(0))
            target[weight] = trim(poly)
    return A, F, G


def direct_rows(F, G):
    rows = {}
    for n in range(22):
        value = []
        for i in range(n + 1):
            j = n - i
            if i not in F or j not in G:
                continue
            value = xadd(value, xscale(12 - j, xmul(xder(F[i]), G[j])))
            value = xadd(value, xscale(i - 8, xmul(F[i], xder(G[j]))))
        rows[n] = value
    return rows


def serialized_rows(raw, values):
    rows = {n: [] for n in range(4, 22)}
    for generator in raw["generators"]:
        n = int(generator["row"])
        if n == 22:
            continue
        value = Q(0)
        for monomial, coefficient in generator["terms"]:
            term = Q(coefficient)
            for variable in monomial:
                term *= values.get(variable, Q(0))
            value += term
        degree = int(generator["x_degree"])
        while len(rows[n]) <= degree:
            rows[n].append(Q(0))
        rows[n][degree] = value
    return {n: trim(poly) for n, poly in rows.items()}


def raw_mutations(raw):
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    Aprime = xder(A)

    # Mutation 1: exact-square F and the c6 characteristic mode only through
    # its polynomial coefficients.  D4..D7 vanish; D8 is the mode-kill row.
    c6_values = {}
    set_window(raw, c6_values, "G", 6, xpow(A, 3))
    set_window(raw, c6_values, "G", 7, xscale(Q(3, 4), A))
    _, F, G = reconstruct(raw, c6_values)
    direct = direct_rows(F, G)
    serialized = serialized_rows(raw, c6_values)
    assert all(direct[n] == serialized[n] for n in range(4, 22))
    assert all(not direct[n] for n in range(4, 8))
    expected_d8 = xscale(Q(-9, 4), xmul(xpow(A, 2), Aprime))
    assert direct[8] == expected_d8

    c6_scaling = {}
    for scalar in (Q(-1), Q(2)):
        values = {}
        set_window(raw, values, "G", 6, xscale(scalar, xpow(A, 3)))
        set_window(raw, values, "G", 7, xscale(scalar * Q(3, 4), A))
        _, F, G = reconstruct(raw, values)
        direct_scaled = direct_rows(F, G)
        serialized_scaled = serialized_rows(raw, values)
        assert all(direct_scaled[n] == serialized_scaled[n] for n in range(4, 22))
        assert direct_scaled[8] == xscale(scalar, expected_d8)
        c6_scaling[str(scalar)] = encode_xpoly(direct_scaled[8])

    # Mutation 2: F=(A^2+t/2)^2+A*t^4.  Its F^(3/2) coefficients through
    # eight are polynomial; omit the polar ninth coefficient.  The first raw
    # residual is exactly +(21/4)A A'.
    d9_values = {}
    set_window(raw, d9_values, "F", 4, A)
    set_window(raw, d9_values, "G", 4, xscale(Q(3, 2), xpow(A, 3)))
    set_window(raw, d9_values, "G", 5, xscale(Q(3, 4), A))
    set_window(raw, d9_values, "G", 8, [Q(3, 8)])
    _, F, G = reconstruct(raw, d9_values)
    direct = direct_rows(F, G)
    serialized = serialized_rows(raw, d9_values)
    assert all(direct[n] == serialized[n] for n in range(4, 22))
    assert all(not direct[n] for n in range(4, 9))
    expected_d9 = xscale(Q(21, 4), xmul(A, Aprime))
    assert direct[9] == expected_d9

    w_scaling = {}
    for scalar in (Q(-1), Q(2)):
        values = {}
        set_window(raw, values, "F", 4, xscale(scalar, A))
        set_window(raw, values, "G", 4, xscale(scalar * Q(3, 2), xpow(A, 3)))
        set_window(raw, values, "G", 5, xscale(scalar * Q(3, 4), A))
        set_window(raw, values, "G", 8, [scalar * scalar * Q(3, 8)])
        _, F, G = reconstruct(raw, values)
        direct_scaled = direct_rows(F, G)
        serialized_scaled = serialized_rows(raw, values)
        assert all(direct_scaled[n] == serialized_scaled[n] for n in range(4, 22))
        assert all(not direct_scaled[n] for n in range(4, 9))
        assert direct_scaled[9] == xscale(scalar * scalar, expected_d9)
        w_scaling[str(scalar)] = encode_xpoly(direct_scaled[9])

    return {
        "c6_mode_kill": {
            "assignment": "F=(A^2+t/2)^2; add c6*t^6*F^(3/4) through G7; all raw later slots zero",
            "rows_D4_through_D7": "zero",
            "D8": encode_xpoly(expected_d8),
            "closed_form": "-(9/4)*A^2*A'",
            "live_linear_scaling_mutations_c6_equals_minus1_and_2": c6_scaling,
            "literal_json_equals_independent_recurrence_rows_D4_through_D21": True,
        },
        "d9_square_sign": {
            "assignment": "F=(A^2+t/2)^2+A*t^4; G=F^(3/2) through G8; G9 and later raw slots zero",
            "rows_D4_through_D8": "zero",
            "D9": encode_xpoly(expected_d9),
            "closed_form": "+(21/4)*A*A'",
            "live_sign_and_power_mutations_W_equals_minus1_and_2": w_scaling,
            "mutation_law": "D9(-W)=D9(W), D9(2W)=4*D9(W)",
            "literal_json_equals_independent_recurrence_rows_D4_through_D21": True,
        },
    }


def calculate_result():
    actual = sha256(RAW)
    assert actual == RAW_SHA256, (str(RAW), actual, RAW_SHA256)
    assert all(path.is_file() for path in CONTEXT_PINS)
    raw = json.loads(RAW.read_text())
    assert raw["variable_count"] == 303
    assert raw["generator_count"] == 513
    assert len(raw["generators"]) == 513
    assert {int(item["row"]) for item in raw["generators"]} == set(range(4, 23))

    characteristic = characteristic_calculation()
    mutations = raw_mutations(raw)

    mode_schedule = []
    for weight in range(4, 21, 2):
        exponent = Q(12 - weight, 8)
        mode_schedule.append({
            "birth_weight": weight,
            "F_exponent": str(exponent),
            "support_at_weight_9": weight <= 9,
            "role": "free_polynomial" if weight <= 12 else "forced_rational",
        })
    assert [item["birth_weight"] for item in mode_schedule
            if item["support_at_weight_9"]] == [4, 6, 8]
    assert [item["birth_weight"] for item in mode_schedule
            if item["role"] == "forced_rational"] == [14, 16, 18, 20]

    return {
        "schema": "jc2.ggv.upper_endpoint.uniform_d9_fullmodes.result.v1",
        "status": "PASS_EXACT_FIELD_POINT_DIVISIBILITY",
        "source": {
            "raw_system": str(RAW.relative_to(ROOT)),
            "raw_system_sha256": RAW_SHA256,
            "variable_count": 303,
            "generator_count": 513,
            "context_bytes_consulted_sha256": {
                str(path.relative_to(ROOT)): digest for path, digest in CONTEXT_PINS.items()
            },
        },
        "mode_schedule": mode_schedule,
        "calculation": characteristic,
        "literal_raw_mutations": mutations,
        "theorems": {
            "T3_D8_c6_mode_kill": {
                "setting": "characteristic-zero field point of the complete fixed branch-P 303-variable fixture",
                "hypotheses": [
                    "D4=...=D8=0",
                    "the reviewed D7 conclusion T=A*V",
                    "the reviewed leading D8 conclusion F4-V/16-Z^2/64=A*W",
                ],
                "complete_weight8_modes": [
                    "c4*F4 (polynomial)",
                    "c6*(3/(32*A)+3*A*Z/16) (sole polar term)",
                    "c8*A^2 (polynomial)",
                ],
                "causality": "modes c10,c12,c14,c16,c18,c20 are not born by weight 8",
                "laurent_obstruction": "polar(g8)=3*c6/(32*A)",
                "raw_congruence": "D8_raw=-(9/4)*c6*A^2*A' mod A^3",
                "conclusion": "c6=0",
            },
            "T4_D9_square_defect": {
                "setting": "same field point, after T3",
                "hypotheses": ["D9=0", "c6=0"],
                "complete_weight9_modes": [
                    "c4*F5 (polynomial)",
                    "c6*(F^(3/4))_3=0 by T3",
                    "c8*(F^(1/2))_1=c8/2 (polynomial)",
                ],
                "causality": "modes c10,c12,c14,c16,c18,c20 are not born by weight 9",
                "laurent_obstruction": "polar(g9)=-3*W^2/(16*A^2)+W*(3*F5/4-3*V*Z/256)/A",
                "raw_congruence": "D9_raw=(21/4)*A*A'*W^2 mod A^2",
                "conclusion": "A divides W",
                "reason": "A=X^4-1 is squarefree, so A|W^2 implies A|W at a field point",
            },
        },
        "scope_firewall": [
            "field-radical divisibility only; no scheme-theoretic A|W claim",
            "no endpoint emptiness, unrestricted branch-P, Keller-pair, or JC2 conclusion",
            "c14,c16,c18,c20 remain mandatory in every continuation reaching their birth weights; they have empty causal support at weight 9, not permission for deletion",
            "no AWS or heavy CAS was used",
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = calculate_result()
    encoded = (json.dumps(result, indent=2, sort_keys=True) + "\n").encode()
    if args.write:
        RESULT.write_bytes(encoded)
    if args.check:
        assert RESULT.read_bytes() == encoded
    print(json.dumps({
        "status": result["status"],
        "raw_system_sha256": result["source"]["raw_system_sha256"],
        "D8_mode_kill": result["theorems"]["T3_D8_c6_mode_kill"]["conclusion"],
        "D9_congruence": result["theorems"]["T4_D9_square_defect"]["raw_congruence"],
        "conclusion": result["theorems"]["T4_D9_square_defect"]["conclusion"],
        "check": args.check,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
