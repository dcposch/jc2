#!/usr/bin/env python3
"""Exact post-D9 q1 proper-divisor survivor through D11.

Standard-library only.  The symbolic lane reloads the frozen D7--D9
characteristic compiler, retaining its complete mode schedule.  The literal
lane serializes one rational survivor into the authoritative raw coefficient
windows and recomputes the determinant rows directly.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
RESULT = HERE / "RESULT.json"
TARGET = HERE / "TARGET.json"

PREFIX_CHECKER = ROOT / "cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/verify_q1_prefix_target.py"
PREFIX_RESULT = PREFIX_CHECKER.with_name("RESULT.json")
PREFIX_TARGET = PREFIX_CHECKER.with_name("TARGET.json")
RAW_INPUT = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json"

SOURCE_PINS = {
    PREFIX_CHECKER: "fceb189badafad877c1142b8925480516111790707954d2000421b8190fde119",
    PREFIX_RESULT: "ba900c6eacc7302491105bec49516d2e95dff982959a3904370b7e540216260b",
    PREFIX_TARGET: "c41f04a93f509adb1f430e808c69cd2171439c9e19fb001c6ea2bf0f29633a46",
    RAW_INPUT: "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_prefix():
    spec = importlib.util.spec_from_file_location("q1_prefix_frozen", PREFIX_CHECKER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


V = load_prefix()

# The frozen helper is deliberately binary.  A local variadic wrapper keeps
# the displayed factorizations readable while preserving its implementation.
_LA_MUL_BINARY = V.la_mul


def _la_mul_variadic(*items):
    answer = V.la_term(1)
    for item in items:
        answer = _LA_MUL_BINARY(answer, item)
    return answer


V.la_mul = _la_mul_variadic


# Q[X] wrappers around the frozen checker.
def padd(*items):
    return V.xp_add(*items)


def pscale(coefficient, item):
    return V.xp_scale(Q(coefficient), item)


def pmul(*items):
    answer = [Q(1)]
    for item in items:
        answer = V.xp_mul(answer, item)
    return answer


def ppow(item, exponent):
    return V.xp_power(item, exponent)


def pdivexact(left, right):
    quotient, remainder = V.xp_divmod(left, right)
    assert not remainder, (left, right, remainder)
    return quotient


def pencode(item):
    return {str(i): str(c) for i, c in enumerate(item) if c}


def pdegree(item):
    return len(V.xp_trim(item)) - 1


def pevaluate(item, value):
    answer = Q(0)
    for coefficient in reversed(item):
        answer = answer * value + coefficient
    return answer


def frac_series(F, A, alpha, maximum):
    """Coefficients of F**alpha via the exact differential recurrence."""
    assert F[0] == ppow(A, 4)
    exponent_at_zero = int(4 * alpha)
    assert Q(exponent_at_zero) == 4 * alpha
    answer = [ppow(A, exponent_at_zero)]
    for weight in range(1, maximum + 1):
        numerator = []
        for index in range(1, weight + 1):
            factor = (alpha + 1) * index - weight
            numerator = padd(
                numerator,
                pscale(factor, pmul(F[index], answer[weight - index])),
            )
        quotient, remainder = V.xp_divmod(numerator, F[0])
        assert not remainder, (weight, alpha, pencode(remainder))
        answer.append(pscale(Q(1, weight), quotient))
    return answer


def determinant_rows(F, G, maximum):
    rows = []
    for weight in range(maximum + 1):
        row = []
        for i in range(weight + 1):
            j = weight - i
            row = padd(
                row,
                pscale(12 - j, pmul(V.xp_derivative(F[i]), G[j])),
                pscale(i - 8, pmul(F[i], V.xp_derivative(G[j]))),
            )
        rows.append(row)
    return rows


def raw_windows():
    source = json.loads(RAW_INPUT.read_text())
    windows = {"F": {}, "G": {}}
    for kind in windows:
        for record in source["raw_slots_through_weight_22"][kind]:
            weight = int(record["weight"])
            degree = int(record["raw_exponents"]["x"])
            windows[kind].setdefault(weight, {})[degree] = record["slot"]
    expected = {
        "F": {
            0: (0, 16), 1: (0, 15), 2: (0, 14), 3: (0, 13),
            4: (0, 12), 5: (0, 11), 6: (0, 10), 7: (0, 9),
            8: (0, 8), 9: (1, 7), 10: (1, 6), 11: (1, 5),
            12: (2, 4), 13: (2, 3), 14: (2, 2),
        },
        "G": {
            0: (0, 24), 1: (0, 23), 2: (0, 22), 3: (0, 21),
            4: (0, 20), 5: (0, 19), 6: (0, 18), 7: (0, 17),
            8: (0, 16), 9: (0, 15), 10: (0, 14), 11: (0, 13),
            12: (0, 12), 13: (1, 11), 14: (1, 10), 15: (1, 9),
            16: (2, 8), 17: (2, 7), 18: (2, 6), 19: (3, 5),
            20: (3, 4), 21: (3, 3),
        },
    }
    for kind in expected:
        assert set(windows[kind]) == set(expected[kind])
        for weight, (lower, upper) in expected[kind].items():
            assert sorted(windows[kind][weight]) == list(range(lower, upper + 1))
    return windows


def serialize_into_windows(F, G):
    windows = raw_windows()
    values = {}
    census = {"F": {}, "G": {}}
    for kind, series in (("F", F), ("G", G)):
        for weight, polynomial in enumerate(series):
            allowed = windows[kind][weight]
            for degree, coefficient in enumerate(polynomial):
                if coefficient:
                    assert degree in allowed, (kind, weight, degree, coefficient)
            for degree, slot in allowed.items():
                values[slot] = polynomial[degree] if degree < len(polynomial) else Q(0)
            census[kind][str(weight)] = {
                "degree": pdegree(polynomial),
                "nonzero_slots": sum(bool(c) for c in polynomial),
                "window": [min(allowed), max(allowed)],
            }
    encoded = {name: str(value) for name, value in sorted(values.items()) if value}
    return census, hashlib.sha256(json.dumps(
        encoded, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()


def one(name):
    return V.la_term(1, 0, name)


def symbolic_post_d9():
    F = V.general_prefix(11)
    _, rows = V.continuation(F, 11)
    v0, u, z, w = map(one, ("v0", "u", "z", "w"))
    f4_lift = V.la_add(
        V.la_scale(Q(1, 16), V.la_mul(v0, u)),
        V.la_scale(Q(1, 64), V.la_power(z, 2)),
        V.la_shift(1, w),
    )
    stage = {
        "c2": {}, "c6": {}, "t": V.la_shift(1, u), "f4": f4_lift,
    }
    polar = {n: V.la_negative(V.la_substitute(rows[n], stage)) for n in (9, 10, 11)}

    C, B, r, vv = map(one, ("C", "B", "r", "v"))
    f5, f6, f7, c10 = map(one, ("f5", "f6", "f7", "c10"))
    divisor_stage = {"v0": V.la_mul(C, vv), "w": V.la_mul(B, r)}

    def numerator(weight, scale, shift):
        raw = V.la_scale(scale, V.la_shift(shift, polar[weight]))
        assert all(a_power >= 0 for a_power, _ in raw)
        raw = V.replace_a_by_cb(raw)
        return V.la_substitute(raw, divisor_stage)

    n9 = numerator(9, 256, 2)
    n10 = numerator(10, 32768, 4)
    n11 = numerator(11, 65536, 6)

    j = V.la_add(V.la_scale(64, f5), V.la_scale(-1, V.la_mul(u, z)),
                 V.la_scale(-16, V.la_mul(r, vv)))
    q = V.la_add(V.la_scale(64, f5), V.la_scale(-1, V.la_mul(u, z)),
                 V.la_scale(-32, V.la_mul(r, vv)))
    p9 = V.la_scale(3, V.la_mul(r, j))
    expected_n9 = V.la_mul(C, V.la_power(B, 2), p9)
    assert n9 == expected_n9

    p10 = V.la_add(
        V.la_scale(24576, V.la_mul(C, V.la_power(B, 2), f6, r)),
        V.la_scale(-96, V.la_mul(C, V.la_power(B, 2), r, V.la_power(u, 2))),
        V.la_scale(-1536, V.la_mul(V.la_power(B, 2), V.la_power(r, 2), z)),
        V.la_scale(12288, V.la_power(f5, 2)),
        V.la_scale(-12288, V.la_mul(f5, r, vv)),
        V.la_scale(-384, V.la_mul(f5, u, z)),
        V.la_scale(3072, V.la_mul(V.la_power(r, 2), V.la_power(vv, 2))),
        V.la_scale(192, V.la_mul(r, u, vv, z)),
        V.la_scale(3, V.la_mul(V.la_power(u, 2), V.la_power(z, 2))),
    )
    expected_n10 = V.la_mul(V.la_power(C, 2), V.la_power(B, 2), p10)
    assert n10 == expected_n10
    compact_p10 = V.la_add(
        V.la_scale(3, V.la_power(q, 2)),
        V.la_scale(96, V.la_mul(V.la_power(B, 2), r, V.la_add(
            V.la_scale(256, V.la_mul(C, f6)),
            V.la_scale(-1, V.la_mul(C, V.la_power(u, 2))),
            V.la_scale(-16, V.la_mul(r, z)),
        ))),
    )
    assert p10 == compact_p10

    p11 = V.la_add(
        V.la_scale(49152, V.la_mul(V.la_power(B, 4), V.la_power(C, 2), f7, r)),
        V.la_scale(-1536, V.la_mul(V.la_power(B, 4), C, V.la_power(r, 2), u)),
        V.la_scale(16384, V.la_mul(V.la_power(B, 3), V.la_power(C, 3), c10, vv)),
        V.la_scale(49152, V.la_mul(V.la_power(B, 2), C, f5, f6)),
        V.la_scale(-192, V.la_mul(V.la_power(B, 2), C, f5, V.la_power(u, 2))),
        V.la_scale(-24576, V.la_mul(V.la_power(B, 2), C, f6, r, vv)),
        V.la_scale(-768, V.la_mul(V.la_power(B, 2), C, f6, u, z)),
        V.la_scale(96, V.la_mul(V.la_power(B, 2), C, r, V.la_power(u, 2), vv)),
        V.la_scale(3, V.la_mul(V.la_power(B, 2), C, V.la_power(u, 3), z)),
        V.la_scale(-6144, V.la_mul(V.la_power(B, 2), f5, r, z)),
        V.la_scale(3072, V.la_mul(V.la_power(B, 2), V.la_power(r, 2), vv, z)),
        V.la_scale(96, V.la_mul(V.la_power(B, 2), r, u, V.la_power(z, 2))),
        V.la_scale(-12288, V.la_mul(V.la_power(f5, 2), vv)),
        V.la_scale(12288, V.la_mul(f5, r, V.la_power(vv, 2))),
        V.la_scale(384, V.la_mul(f5, u, vv, z)),
        V.la_scale(-3072, V.la_mul(V.la_power(r, 2), V.la_power(vv, 3))),
        V.la_scale(-192, V.la_mul(r, u, V.la_power(vv, 2), z)),
        V.la_scale(-3, V.la_mul(V.la_power(u, 2), vv, V.la_power(z, 2))),
    )
    expected_n11 = V.la_mul(V.la_power(C, 3), V.la_power(B, 2), p11)
    assert n11 == expected_n11

    relation = V.la_add(p11, V.la_mul(vv, p10))
    expected_relation = V.la_add(
        V.la_scale(49152, V.la_mul(V.la_power(B, 4), V.la_power(C, 2), f7, r)),
        V.la_scale(-1536, V.la_mul(V.la_power(B, 4), C, V.la_power(r, 2), u)),
        V.la_scale(16384, V.la_mul(V.la_power(B, 3), V.la_power(C, 3), c10, vv)),
        V.la_scale(49152, V.la_mul(V.la_power(B, 2), C, f5, f6)),
        V.la_scale(-192, V.la_mul(V.la_power(B, 2), C, f5, V.la_power(u, 2))),
        V.la_scale(-768, V.la_mul(V.la_power(B, 2), C, f6, u, z)),
        V.la_scale(3, V.la_mul(V.la_power(B, 2), C, V.la_power(u, 3), z)),
        V.la_scale(-96, V.la_mul(V.la_power(B, 2), r, z, j)),
    )
    assert relation == expected_relation

    return {
        "full_row_term_counts": {str(n): len(rows[n]) for n in (9, 10, 11)},
        "full_row_sha256": {str(n): hashlib.sha256(json.dumps(
            V.la_encode(rows[n]), sort_keys=True, separators=(",", ":")
        ).encode()).hexdigest() for n in (9, 10, 11)},
        "P9": "3*r*J, J=64*F5-u*Z-16*r*v",
        "P10": (
            "3*Q^2+96*B^2*r*(256*C*F6-C*u^2-16*r*Z), "
            "Q=64*F5-u*Z-32*r*v"
        ),
        "P11_plus_vP10": (
            "49152*B^4*C^2*F7*r-1536*B^4*C*r^2*u+16384*B^3*C^3*c10*v"
            "+49152*B^2*C*F5*F6-192*B^2*C*F5*u^2-768*B^2*C*F6*u*Z"
            "+3*B^2*C*u^3*Z-96*B^2*r*Z*J"
        ),
        "divisibility": {
            "D9": "C divides r*J",
            "D10": "C^2*B^2 divides P10",
            "D11": "C^3*B^4 divides P11",
        },
        "B_root_consequence": (
            "D10 gives B|Q.  After setting P10=0, the D11/B^2 bracket "
            "has root value -3*v*(Q/B)^2/C; since gcd(B,v)=1, D11 "
            "forces B^2|Q rather than A|W."
        ),
        "all_modes_retained": {str(k): str(value) for k, value in V.MODES.items()},
    }


def fixture():
    X = [Q(0), Q(1)]
    A = padd(ppow(X, 4), [Q(-1)])
    C = padd(X, [Q(-1)])
    B = [Q(1), Q(1), Q(1), Q(1)]
    R0 = C
    v0 = padd(pmul(V.xp_derivative(A), R0),
              pscale(2, pmul(A, V.xp_derivative(R0))))
    v = pdivexact(v0, C)
    u = [Q(-27, 16)]
    z = [Q(9, 2)]
    t = pmul(A, u)
    w = B
    f4 = padd(pscale(Q(1, 16), pmul(v0, u)),
              pscale(Q(1, 64), ppow(z, 2)), pmul(A, w))
    f5 = [Q(1421, 2048), Q(5, 8), Q(7, 16), Q(9, 4),
          Q(-9, 16), Q(-3, 8), Q(-3, 16)]
    f6 = [Q(-16551, 65536), Q(-117, 512), Q(-45, 256),
          Q(-27, 256), Q(-27, 512), Q(-9, 512)]
    f7 = [Q(117, 8192), Q(-27, 2048), Q(-135, 4096),
          Q(-27, 2048), Q(-27, 8192)]
    H = ppow(A, 2)
    F = [
        ppow(A, 4),
        pmul(H, v0),
        pscale(Q(1, 4), padd(ppow(v0, 2), pmul(H, z))),
        pscale(Q(1, 8), padd(pmul(v0, z), pmul(A, t))),
        f4, f5, f6, f7,
    ] + [[] for _ in range(4)]
    G = frac_series(F, A, Q(3, 2), 11)
    rows = determinant_rows(F, G, 11)
    assert rows == [[] for _ in range(12)]
    census, slot_hash = serialize_into_windows(F, G)

    # Direct polynomial checks of the factored P9/P10/P11 targets.
    r = [Q(1)]
    J = padd(pscale(64, f5), pscale(-1, pmul(u, z)),
             pscale(-16, pmul(r, v)))
    Qdef = padd(pscale(64, f5), pscale(-1, pmul(u, z)),
                pscale(-32, pmul(r, v)))
    assert not V.xp_divmod(J, C)[1]
    assert not V.xp_divmod(Qdef, ppow(B, 2))[1]
    P10 = padd(
        pscale(3, ppow(Qdef, 2)),
        pscale(96, pmul(ppow(B, 2), r, padd(
            pscale(256, pmul(C, f6)),
            pscale(-1, pmul(C, ppow(u, 2))),
            pscale(-16, pmul(r, z)),
        ))),
    )
    assert not P10

    P11 = padd(
        pscale(49152, pmul(ppow(B, 4), ppow(C, 2), f7, r)),
        pscale(-1536, pmul(ppow(B, 4), C, ppow(r, 2), u)),
        pscale(49152, pmul(ppow(B, 2), C, f5, f6)),
        pscale(-192, pmul(ppow(B, 2), C, f5, ppow(u, 2))),
        pscale(-24576, pmul(ppow(B, 2), C, f6, r, v)),
        pscale(-768, pmul(ppow(B, 2), C, f6, u, z)),
        pscale(96, pmul(ppow(B, 2), C, r, ppow(u, 2), v)),
        pscale(3, pmul(ppow(B, 2), C, ppow(u, 3), z)),
        pscale(-6144, pmul(ppow(B, 2), f5, r, z)),
        pscale(3072, pmul(ppow(B, 2), ppow(r, 2), v, z)),
        pscale(96, pmul(ppow(B, 2), r, u, ppow(z, 2))),
        pscale(-12288, pmul(ppow(f5, 2), v)),
        pscale(12288, pmul(f5, r, ppow(v, 2))),
        pscale(384, pmul(f5, u, v, z)),
        pscale(-3072, pmul(ppow(r, 2), ppow(v, 3))),
        pscale(-192, pmul(r, u, ppow(v, 2), z)),
        pscale(-3, pmul(ppow(u, 2), v, ppow(z, 2))),
    )
    assert not P11

    quotient, w_remainder = V.xp_divmod(w, A)
    assert not quotient and w_remainder == B

    # Live mutations.  The pre-Hermite F5 passes D9/D10 but fails D11.
    f5_pre = [Q(269, 2048), Q(1, 4), Q(1, 4), Q(9, 4)]
    f6_pre = [Q(729, 65536)]
    F_pre = list(F)
    F_pre[5], F_pre[6], F_pre[7] = f5_pre, f6_pre, []
    numerator11 = []
    G_pre = frac_series(F_pre[:11], A, Q(3, 2), 10)
    weight = 11
    for index in range(1, weight + 1):
        factor = (Q(5, 2) * index) - weight
        numerator11 = padd(
            numerator11,
            pscale(factor, pmul(F_pre[index], G_pre[weight - index])),
        )
    _, pre_remainder = V.xp_divmod(numerator11, F_pre[0])
    assert pre_remainder

    F_no6 = list(F)
    F_no6[6] = []
    G_no6 = frac_series(F_no6[:10], A, Q(3, 2), 9)
    numerator10 = []
    for index in range(1, 11):
        factor = (Q(5, 2) * index) - 10
        numerator10 = padd(numerator10,
                           pscale(factor, pmul(F_no6[index], G_no6[10 - index])))
    _, no6_remainder = V.xp_divmod(numerator10, F_no6[0])
    assert no6_remainder

    # c10=1 changes only G10 regularly and adds this nonpolynomial order-one
    # coefficient at G11.  Its numerator is V0 and its uncancelled denominator
    # is 4*A = 4*C*B, hence B remains after canceling C.
    qv, rv = V.xp_divmod(v0, A)
    assert rv
    _, mode_remainder = V.xp_divmod(v0, A)

    return {
        "A": pencode(A), "C": pencode(C), "B": pencode(B),
        "R0": pencode(R0), "V0": pencode(v0), "V1": pencode(v),
        "u": pencode(u), "Z": pencode(z), "T": pencode(t), "W": pencode(w),
        "F": {str(i): pencode(poly) for i, poly in enumerate(F)},
        "G": {str(i): pencode(poly) for i, poly in enumerate(G)},
        "raw_window_census": census,
        "raw_nonzero_slot_assignment_sha256": slot_hash,
        "determinant_rows_D0_D11": [pencode(row) for row in rows],
        "q1_identity": "V0=A'*R0+2*A*R0'",
        "P10_is_literal_zero": True,
        "P11_is_literal_zero": True,
        "W_div_A_quotient": pencode(quotient),
        "W_div_A_remainder": pencode(w_remainder),
        "mutations": {
            "omit_B_Hermite_F5_adjustment": {
                "first_failed_characteristic_coefficient": 11,
                "division_remainder_sha256": hashlib.sha256(json.dumps(
                    pencode(pre_remainder), sort_keys=True,
                    separators=(",", ":")
                ).encode()).hexdigest(),
                "remainder": pencode(pre_remainder),
            },
            "drop_F6": {
                "first_failed_characteristic_coefficient": 10,
                "division_remainder_sha256": hashlib.sha256(json.dumps(
                    pencode(no6_remainder), sort_keys=True,
                    separators=(",", ":")
                ).encode()).hexdigest(),
            },
            "set_c10_to_1": {
                "G11_mode_term": "V0/(4*A)=V1/(4*B)",
                "uncancelled_remainder_mod_A": pencode(mode_remainder),
            },
        },
    }


def target_payload():
    return {
        "format": "GGV_BRANCH_P_Q1_POST_D9_D11_PROPER_DIVISOR_SURVIVOR_V1",
        "field": "Q; characteristic-zero field-point semantics",
        "stratum": "c2=0, A=C*B, V0=C*v, gcd(B,v)=1, T=A*u, W=B*r",
        "exact_rows": {
            "D9": "C divides r*(64*F5-u*Z-16*r*v)",
            "D10": "C^2*B^2 divides P10",
            "D11": "C^3*B^4 divides P11",
        },
        "verdict": (
            "D10/D11 do not force A|W: an exact rational raw-window point "
            "with W=B survives D0..D11."
        ),
        "smallest_successor": (
            "Continue this single frozen rational prefix sequentially through "
            "D12..D22, retaining all modes and raw lower/upper windows."
        ),
        "scope_firewall": (
            "No D12+ lift, endpoint, existence, GGV landing, counterexample, "
            "or JC2 conclusion.  The generic RAW_INPUT is used for literal "
            "slot windows only; its unrelated leading-row fixture is not reused."
        ),
    }


def calculate_result():
    for path, expected in SOURCE_PINS.items():
        assert digest(path) == expected, (path, digest(path), expected)
    symbolic = symbolic_post_d9()
    exact_fixture = fixture()
    target = target_payload()
    return {
        "status": "PASS_EXACT_PROVISIONAL_Q1_POST_D9_D11_PROPER_DIVISOR_SURVIVOR",
        "source_pins": {str(path.relative_to(ROOT)): expected
                        for path, expected in SOURCE_PINS.items()},
        "symbolic_complete_rows": symbolic,
        "exact_rational_survivor": exact_fixture,
        "target_sha256": hashlib.sha256((json.dumps(
            target, sort_keys=True, indent=2
        ) + "\n").encode()).hexdigest(),
        "scope": target["scope_firewall"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = calculate_result()
    target = target_payload()
    encoded = json.dumps(result, sort_keys=True, indent=2) + "\n"
    target_encoded = json.dumps(target, sort_keys=True, indent=2) + "\n"
    if args.check:
        assert RESULT.read_text() == encoded
        assert TARGET.read_text() == target_encoded
    else:
        RESULT.write_text(encoded)
        TARGET.write_text(target_encoded)
    print(result["status"])


if __name__ == "__main__":
    main()
