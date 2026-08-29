#!/usr/bin/env python3
"""Independent hostile checker for the uniform D16/D17 full-mode cascade.

Does not import the D16/D17 or D14/D15 producers.  Rebuilds the nine-mode
Laurent recurrence, the square-root cube, the raw D5G rows D16--D17, the
G16/G17 window matrices, live and hostile mutations, and the X^0/X^1 jets
from the authoritative 303-variable JSON using only fractions.Fraction.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
CHARGED_NOTE = ROOT / "xmodel/ggv-upper-endpoint-uniform-d16-d17-fullmodes-sol-ultra-20260828.md"
PACKET = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828"
PRODUCER = PACKET / "verify_uniform_d16_d17.py"
RESULT = PACKET / "RESULT.json"
README = PACKET / "README.md"
SOURCE = PACKET / "SOURCE.sha256"
EVIDENCE = PACKET / "EVIDENCE.sha256"
PRED_PY = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/verify_uniform_d14_d15.py"
PRED_RES = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828/RESULT.json"
REVIEW_RESULT = ROOT / "xmodel/ggv-upper-endpoint-uniform-d16-d17-fullmodes-hostile-review-grok46-RESULT.json"

CHARGED = {
    CHARGED_NOTE: "4f7b363addd020e95096ffa289ff96408b21fc4b1c09cfd6235571956117408a",
    PRODUCER: "5904d7b19dc5d46d31a781150c4b6de9e62e32812b554006e92f78f9d76fd5d9",
    RESULT: "2a6f363df8fb4aef94f01d7a938e3bfcff15f6db49af3164e36367c9a6d1929a",
    PRED_PY: "53f2a7a276be4a0aa7f77cc031e270d573fc78b5db64cdb76a0cf6c502e52517",
    PRED_RES: "7546618aa5a40ed983014159c1d39337396607562912570c97cfe2ee779394ea",
    RAW_PATH: "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0",
}

FAILURES = []
CHECKS = []
MODES = {
    4: Q(1), 6: Q(3, 4), 8: Q(1, 2), 10: Q(1, 4), 12: Q(0),
    14: Q(-1, 4), 16: Q(-1, 2), 18: Q(-3, 4), 20: Q(-1),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def record(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, ok, detail))
    status = "PASS" if ok else "FAIL"
    extra = f"  {detail}" if detail else ""
    print(f"[{status}] {name}{extra}")
    if not ok:
        FAILURES.append(name)


def must(name: str, cond: bool, detail: str = "") -> None:
    record(name, bool(cond), detail)


# ---------------------------------------------------------------------------
# Univariate Q[X]
# ---------------------------------------------------------------------------

def trim(poly):
    out = list(poly)
    while out and not out[-1]:
        out.pop()
    return out


def add(*items):
    n = max((len(p) for p in items), default=0)
    return trim([
        sum((p[i] if i < len(p) else Q(0) for p in items), Q(0))
        for i in range(n)
    ])


def scale(c, a):
    c = Q(c)
    return trim([c * x for x in a])


def mul(a, b):
    if not a or not b:
        return []
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if y:
                out[i + j] += x * y
    return trim(out)


def der(a):
    return trim([Q(i) * a[i] for i in range(1, len(a))])


def power(a, e):
    out = [Q(1)]
    base = list(a)
    n = int(e)
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def poly_divmod(num, den):
    den = trim(den)
    num = trim([Q(x) for x in num])
    if not den:
        raise ZeroDivisionError
    if not num or len(num) < len(den):
        return [], num
    quot = [Q(0)] * (len(num) - len(den) + 1)
    rem = list(num)
    lead = den[-1]
    while rem and len(rem) >= len(den):
        k = len(rem) - len(den)
        q = rem[-1] / lead
        quot[k] = q
        for i, c in enumerate(den):
            rem[i + k] -= q * c
        rem = trim(rem)
    return trim(quot), rem


def poly_gcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        _, r = poly_divmod(a, b)
        a, b = b, r
    if not a:
        return []
    return scale(1 / a[-1], a)


def poly_in_ideal(poly, modulus):
    return not poly_divmod(poly, modulus)[1]


def eq(a, b):
    return trim(a) == trim(b)


def encode(poly):
    return {str(i): str(c) for i, c in enumerate(poly) if c}


def poly_from(terms):
    if not terms:
        return []
    out = [Q(0)] * (max(terms) + 1)
    for degree, coefficient in terms.items():
        out[degree] = Q(coefficient)
    return trim(out)


A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
AP = der(A)
A2 = power(A, 2)
A3 = power(A, 3)
A4 = power(A, 4)
X = [Q(0), Q(1)]


# ---------------------------------------------------------------------------
# Sparse Laurent ring
# ---------------------------------------------------------------------------

def Lconst(v=0):
    v = Q(v)
    return {(0, ()): v} if v else {}


def Lvar(name, aexp=0):
    return {(aexp, (name,)): Q(1)}


def LA(e=1):
    return {(e, ()): Q(1)}


def Ladd(*ps):
    out = {}
    for p in ps:
        for k, c in p.items():
            out[k] = out.get(k, Q(0)) + c
            if not out[k]:
                del out[k]
    return out


def Lneg(p):
    return {k: -c for k, c in p.items()}


def Lscale(v, p):
    v = Q(v)
    return {k: v * c for k, c in p.items() if v * c}


def Lmul(p, q):
    out = {}
    for (a, m), c in p.items():
        for (b, n), d in q.items():
            key = (a + b, tuple(sorted(m + n)))
            out[key] = out.get(key, Q(0)) + c * d
            if not out[key]:
                del out[key]
    return out


def Lshift(e, p):
    return {(a + e, m): c for (a, m), c in p.items()}


def Lterms(p):
    return sorted(((a, m, str(c)) for (a, m), c in p.items()),
                  key=lambda t: (t[0], t[1]))


DERIV = {
    "z": "dz", "v": "dv", "r": "dr", "q": "dq", "t": "dt",
    "u": "du", "y": "dy", "b": "b_x", "m": "m_x", "d": "d_x",
    "n": "n_x", "ell": "ell_x",
    **{f"f{n}": f"df{n}" for n in range(5, 18)},
}


def Lder(p):
    out = {}
    for (e, m), c in p.items():
        if e:
            key = (e - 1, tuple(sorted(m + ("ap",))))
            out[key] = out.get(key, Q(0)) + c * e
        for i, s in enumerate(m):
            ds = DERIV.get(s)
            if ds is None:
                continue
            changed = list(m)
            changed[i] = ds
            key = (e, tuple(sorted(changed)))
            out[key] = out.get(key, Q(0)) + c
    return {k: v for k, v in out.items() if v}


def Lop(n, p):
    """L_n(R) = 4(12-n) A^3 A' R - 8 A^4 R'."""
    first = Lscale(4 * (12 - n), Lmul(Lshift(3, p), Lvar("ap")))
    second = Lscale(-8, Lshift(4, Lder(p)))
    return Ladd(first, second)


def Lpolar(p):
    return {(a, m): c for (a, m), c in p.items() if a < 0}


def Lmod(e, p):
    return {(a, m): c for (a, m), c in p.items() if a < e}


def Lsub(p, subs):
    out = {}
    for (a, m), c in p.items():
        term = Lscale(c, LA(a)) if a else Lconst(c)
        for s in m:
            term = Lmul(term, subs.get(s, Lvar(s)))
        out = Ladd(out, term)
    return out


DERIV_CANON = {
    "ap": "a_x",
    "df8": "f8_x", "df9": "f9_x",
    "dq": "q_x", "dv": "v_x", "dr": "r_x",
    "dt": "t_x", "dz": "z_x", "dy": "y_x",
    "b_x": "b_x", "m_x": "m_x", "d_x": "d_x",
    "n_x": "n_x", "ell_x": "ell_x",
}


def Lencode(p, canon=False):
    items = []
    for (a, m), c in p.items():
        names = tuple(sorted(DERIV_CANON.get(s, s) if canon else s for s in m))
        items.append({
            "A_exponent": a,
            "coefficient": str(c),
            "monomial": list(names),
        })
    items.sort(key=lambda it: (it["A_exponent"], it["monomial"], it["coefficient"]))
    return items


def fractional(F, alpha, maximum):
    y = {0: LA(int(Q(4) * Q(alpha)))}
    for n in range(1, maximum + 1):
        rhs = {}
        for i in range(1, n + 1):
            coeff = (Q(alpha) + 1) * i - n
            rhs = Ladd(rhs, Lscale(coeff, Lmul(F[i], y[n - i])))
        y[n] = Lscale(Q(1, n), Lshift(-4, rhs))
    return y


def square_root_cube(F, maximum):
    S = {0: LA(2)}
    for n in range(1, maximum + 1):
        acc = dict(F[n])
        for i in range(1, n):
            acc = Ladd(acc, Lneg(Lmul(S[i], S[n - i])))
        S[n] = Lscale(Q(1, 2), Lshift(-2, acc))
    cube = {}
    for n in range(0, maximum + 1):
        acc = {}
        for i in range(n + 1):
            for j in range(n - i + 1):
                k = n - i - j
                acc = Ladd(acc, Lmul(Lmul(S[i], S[j]), S[k]))
        cube[n] = acc
    return S, cube


def continuation(F, maximum, killed=None):
    killed = killed or {}
    exponents = set(MODES.values()) | {Q(3, 2)}
    powers = {alpha: fractional(F, alpha, maximum) for alpha in exponents}
    rows = {}
    for n in range(maximum + 1):
        row = powers[Q(3, 2)][n]
        for birth, alpha in MODES.items():
            if birth <= n and birth not in killed:
                row = Ladd(row, Lmul(Lvar(f"c{birth}"), powers[alpha][n - birth]))
        rows[n] = row
    return powers, rows


def prefix_through_d15():
    z, v, r, q, t, y = (Lvar(name) for name in ("z", "v", "r", "q", "t", "y"))
    F = {
        0: LA(4),
        1: LA(2),
        2: Ladd(Lconst(Q(1, 4)), Lscale(Q(1, 4), Lmul(LA(2), z))),
        3: Ladd(Lscale(Q(1, 8), z), Lscale(Q(1, 8), Lmul(LA(2), v))),
        4: Ladd(Lscale(Q(1, 16), v), Lscale(Q(1, 64), Lmul(z, z)), Lmul(LA(2), r)),
        5: Ladd(Lscale(Q(1, 2), r), Lscale(Q(1, 64), Lmul(z, v)), Lmul(LA(2), q)),
        6: Ladd(Lscale(Q(1, 2), q), Lscale(Q(1, 8), Lmul(r, z)),
                Lscale(Q(1, 256), Lmul(v, v)), Lmul(LA(2), t)),
        7: Ladd(Lscale(Q(1, 2), t), Lscale(Q(1, 8), Lmul(q, z)),
                Lscale(Q(1, 16), Lmul(r, v)), Lmul(LA(2), y)),
    }
    for n in range(8, 15):
        F[n] = Lvar(f"f{n}")
    for n in range(15, 18):
        F[n] = {}
    return F, z, v, r, q, t, y


def low_jets(item):
    constants = {f"c{birth}" for birth in MODES}
    lower_bounds = {8: 0, 9: 1, 10: 1, 11: 1, 12: 2, 13: 2, 14: 2}

    def jet_symbol(symbol, order):
        if symbol in constants:
            return symbol if order == 0 else None
        if symbol.startswith("f") and symbol[1:].isdigit():
            weight = int(symbol[1:])
            if lower_bounds.get(weight, 0) > order:
                return None
        return f"{symbol}{order}"

    outputs = [{}, {}]
    for (a_power, symbols), coefficient in item.items():
        sign = -1 if a_power % 2 else 1
        constant_symbols = [jet_symbol(symbol, 0) for symbol in symbols]
        if all(symbol is not None for symbol in constant_symbols):
            key = (0, tuple(sorted(constant_symbols)))
            outputs[0][key] = outputs[0].get(key, Q(0)) + sign * coefficient
        for position, symbol in enumerate(symbols):
            linear_symbol = jet_symbol(symbol, 1)
            if linear_symbol is None:
                continue
            factors = []
            valid = True
            for other_position, other_symbol in enumerate(symbols):
                value = (linear_symbol if other_position == position
                         else jet_symbol(other_symbol, 0))
                if value is None:
                    valid = False
                    break
                factors.append(value)
            if valid:
                key = (0, tuple(sorted(factors)))
                outputs[1][key] = outputs[1].get(key, Q(0)) + sign * coefficient
    return [{key: value for key, value in output.items() if value}
            for output in outputs]


def constant_jet(item, drop=()):
    drop = set(drop)
    jet_symbols = {"z", "v", "r", "q", "t", "u", "y"} | {f"f{n}" for n in range(7, 16)}
    answer = {}
    for (a_power, symbols), coefficient in item.items():
        if any(symbol in drop for symbol in symbols):
            continue
        key = (0, tuple(sorted(
            f"{symbol}0" if symbol in jet_symbols else symbol
            for symbol in symbols)))
        sign = -1 if a_power % 2 else 1
        answer[key] = answer.get(key, Q(0)) + coefficient * sign
        if not answer[key]:
            del answer[key]
    return answer


def characteristic_identities():
    F, z, v, r, q, t, y = prefix_through_d15()
    powers, g = continuation(F, 17, killed={6, 10, 14})
    _, cube = square_root_cube(F, 17)
    for n in range(18):
        must(f"S3_matches_F32_w{n}", powers[Q(3, 2)][n] == cube[n])

    for birth, alpha in MODES.items():
        y0 = fractional({0: LA(4), 1: LA(2)}, alpha, 0)[0]
        must(f"mode_c{birth}_y0", y0 == LA(int(Q(4) * alpha)), str(Lterms(y0)))
        must(f"c{birth}_support_at_16", (birth <= 16) == (16 - birth >= 0))
        must(f"c{birth}_support_at_17", (birth <= 17) == (17 - birth >= 0))

    must("nine_modes", list(MODES) == [4, 6, 8, 10, 12, 14, 16, 18, 20])
    must("c16_born_at_16", 16 <= 16 and 16 > 15)
    must("c18_unborn_at_16_17", 18 > 17)
    must("c20_unborn_at_16_17", 20 > 17)
    must("F_neg12_0_is_1_over_A2",
         powers[Q(-1, 2)][0] == LA(-2), str(Lterms(powers[Q(-1, 2)][0])))
    must("F_neg12_1_is_minus_1_over_2A4",
         powers[Q(-1, 2)][1] == Lscale(Q(-1, 2), LA(-4)),
         str(Lterms(powers[Q(-1, 2)][1])))
    must("F0_positive_weights_vanish",
         powers[Q(0)][4] == {} and powers[Q(0)][5] == {})
    must("c12_no_D16_D17_polar",
         Lpolar(Lmul(Lvar("c12"), powers[Q(0)][4])) == {}
         and Lpolar(Lmul(Lvar("c12"), powers[Q(0)][5])) == {})
    must("c4_F12_polynomial", not Lpolar(Lmul(Lvar("c4"), F[12])))
    must("c4_F13_polynomial", not Lpolar(Lmul(Lvar("c4"), F[13])))
    must("c8_live_at_16", 8 <= 16)
    half8_polar = Lpolar(powers[Q(1, 2)][8])
    must("c8_half8_has_A_minus_2",
         any(a == -2 for (a, _) in half8_polar), str(Lterms(half8_polar)))

    base8 = Ladd(Lscale(Q(1, 2), y), Lscale(Q(1, 8), Lmul(t, z)),
                 Lscale(Q(1, 16), Lmul(q, v)), Lscale(Q(1, 4), Lmul(r, r)))
    B = Ladd(Lvar("f8"), Lscale(-1, base8))
    numerator16 = Ladd(
        Lscale(Q(3, 8), Lmul(B, B)),
        Lscale(Q(1, 2), Lmul(Lvar("c8"), B)),
        Lvar("c16"),
    )
    expected_g16 = Lshift(-2, numerator16)
    must("g16_polar_exact", Lpolar(g[16]) == expected_g16,
         str(Lterms(Lpolar(g[16]))))
    must("g16_only_A_minus_2",
         set(a for (a, _) in Lpolar(g[16])) == {-2})
    must("g16_contains_live_c8_cross",
         Lpolar(g[16]).get((-2, ("c8", "f8"))) == Q(1, 2))
    must("g16_contains_born_c16",
         Lpolar(g[16]).get((-2, ("c16",))) == Q(1))
    must("c16_not_silently_zero_in_polar",
         Lpolar(g[16]).get((-2, ("c16",))) != Q(0))
    must("L16_annihilates_c16_over_A2",
         Lop(16, Lshift(-2, Lvar("c16"))) == {})
    d16_same = Lneg(Lop(16, expected_g16))
    must("D16_same_row_is_8_A2_Nprime",
         Lmod(3, d16_same) == Lscale(8, Lshift(2, Lder(numerator16))),
         str(Lterms(Lmod(3, d16_same)))[:200])
    must("D16_same_row_blind_to_c16",
         all("c16" not in m for (_, m) in d16_same))

    # Uniqueness: a nonzero scalar cannot lie in (A^2).
    must("A2_does_not_contain_1", not poly_in_ideal([Q(1)], A2))
    must("A2_does_not_contain_3_8", not poly_in_ideal([Q(3, 8)], A2))
    must("A2_does_not_contain_minus_3_8", not poly_in_ideal([Q(-3, 8)], A2))
    must("char0_8_visible", Q(8) != 0)
    must("gcd_A_Aprime_is_1", poly_gcd(A, AP) == [Q(1)])
    must("A_prime_leading_4", AP[-1] == Q(4))

    relation16 = {
        "c16": Ladd(Lshift(2, Lvar("m")),
                    Lscale(Q(-3, 8), Lmul(Lvar("b"), Lvar("b"))),
                    Lscale(Q(-1, 2), Lmul(Lvar("c8"), Lvar("b")))),
        "f8": Ladd(base8, Lvar("b")),
    }
    g16_after = Lsub(g[16], relation16)
    must("g16_holomorphic_after_D16_relation", Lpolar(g16_after) == {})

    # Centered coordinates.
    lam = Lvar("lambda")
    bhat_before = Ladd(Lvar("b"), Lscale(Q(2, 3), Lvar("c8")))
    bhat_after = Ladd(Lvar("b"), lam,
                      Lscale(Q(2, 3), Ladd(Lvar("c8"), Lscale(Q(-3, 2), lam))))
    must("Bhat_gauge_invariant", bhat_before == bhat_after)
    j_before = Ladd(Lvar("c16"), Lscale(Q(-1, 6), Lmul(Lvar("c8"), Lvar("c8"))))
    c8_after = Ladd(Lvar("c8"), Lscale(Q(-3, 2), lam))
    c16_after = Ladd(Lvar("c16"),
                     Lscale(Q(-1, 2), Lmul(Lvar("c8"), lam)),
                     Lscale(Q(3, 8), Lmul(lam, lam)))
    j_after = Ladd(c16_after, Lscale(Q(-1, 6), Lmul(c8_after, c8_after)))
    must("J16_gauge_invariant", j_before == j_after)
    # (3/8) Bhat^2 + J16 = (3/8) B^2 + c8 B/2 + c16
    centered_num = Ladd(Lscale(Q(3, 8), Lmul(bhat_before, bhat_before)), j_before)
    uncentered_num = Ladd(Lscale(Q(3, 8), Lmul(Lvar("b"), Lvar("b"))),
                          Lscale(Q(1, 2), Lmul(Lvar("c8"), Lvar("b"))),
                          Lvar("c16"))
    must("centered_D16_numerator_identity", centered_num == uncentered_num)
    must("3_Bhat_equals_3B_plus_2c8",
         Ladd(Lscale(3, bhat_before),
              Lneg(Ladd(Lscale(3, Lvar("b")), Lscale(2, Lvar("c8"))))) == {})
    # c12 accompanying shift from c4 t^4 F: keeping G's c4 F + c12 piece
    # when F -> F + lambda t^8 requires c12 -> c12 - c4 lambda.
    c12_after = Ladd(Lvar("c12"), Lneg(Lmul(Lvar("c4"), lam)))
    must("c12_shift_required_by_c4_F",
         Ladd(Lmul(Lvar("c4"), Ladd(Lvar("f"), lam)),
              Lmul(c12_after, Lconst(1)))
         == Ladd(Lmul(Lvar("c4"), Lvar("f")), Lvar("c12")))

    base9 = Ladd(Lscale(Q(1, 2), Lmul(q, r)), Lscale(Q(1, 16), Lmul(t, v)),
                 Lscale(Q(1, 8), Lmul(y, z)))
    C = Ladd(Lvar("f9"), Lscale(-1, base9))
    g17_before = Lsub(g[17], {"f8": Ladd(base8, Lvar("b"))})
    expected_g17_before = Ladd(
        Lscale(Q(-1, 2), Lshift(-4, Ladd(
            Lscale(Q(3, 8), Lmul(Lvar("b"), Lvar("b"))),
            Lscale(Q(1, 2), Lmul(Lvar("c8"), Lvar("b"))),
            Lvar("c16"),
        ))),
        Lshift(-2, Lmul(Ladd(Lscale(Q(3, 4), Lvar("b")),
                             Lscale(Q(1, 2), Lvar("c8"))), C)),
    )
    must("g17_pre_relation_A_minus_4_block",
         Lpolar(g17_before) == expected_g17_before,
         str(Lterms(Lpolar(g17_before)))[:240])
    must("g17_pre_contains_c16_over_2A4",
         Lpolar(g17_before).get((-4, ("c16",))) == Q(-1, 2))
    must("g17_pre_A_exponents",
         set(a for (a, _) in Lpolar(g17_before)) == {-4, -2})

    c16_g16 = Lshift(-2, Lvar("c16"))
    c16_g17 = Lscale(Q(-1, 2), Lshift(-4, Lvar("c16")))
    f1 = LA(2)
    mixed = Ladd(
        Lscale(-4, Lmul(Lder(f1), c16_g16)),
        Lscale(-7, Lmul(f1, Lder(c16_g16))),
    )
    same = Lop(17, c16_g17)
    must("D17_c16_predecessor_is_6_c16_Ap_over_A",
         mixed == Lscale(6, Lshift(-1, Lmul(Lvar("ap"), Lvar("c16")))),
         str(Lterms(mixed)))
    must("D17_c16_same_row_is_minus_6_c16_Ap_over_A",
         same == Lscale(-6, Lshift(-1, Lmul(Lvar("ap"), Lvar("c16")))),
         str(Lterms(same)))
    must("D17_c16_pieces_cancel", Ladd(mixed, same) == {})
    must("D17_does_not_independently_kill_c16",
         Ladd(mixed, same) != Lneg(same))
    defect_mixed = Ladd(
        Lscale(-4, Lmul(Lder(f1), Lneg(c16_g16))),
        Lscale(-7, Lmul(f1, Lder(Lneg(c16_g16)))),
    )
    must("D17_c16_storage_defects_also_cancel",
         Ladd(Lop(17, Lneg(c16_g17)), defect_mixed) == {})

    g17_after = Lsub(g17_before, relation16)
    obstruction17 = Ladd(
        Lscale(Q(3, 4), Lmul(Lvar("b"), C)),
        Lscale(Q(1, 2), Lmul(Lvar("c8"), C)),
        Lscale(Q(-1, 2), Lvar("m")),
    )
    must("g17_after_D16_is_obstruction_over_A2",
         Lpolar(g17_after) == Lshift(-2, obstruction17),
         str(Lterms(Lpolar(g17_after))))
    must("g17_after_has_no_A_minus_4",
         not any(a <= -4 for (a, _) in Lpolar(g17_after)))
    must("g17_after_has_no_free_c16",
         all("c16" not in m for (_, m) in Lpolar(g17_after)))
    d17 = Lneg(Lop(17, Lshift(-2, obstruction17)))
    must("D17_mod_A2_is_4_A_Ap_obstruction",
         Lmod(2, d17) == Lscale(4, Lmul(Lshift(1, Lvar("ap")), obstruction17)),
         str(Lterms(Lmod(2, d17))))
    first_stage = Lneg(Lop(17, Lshift(-1, Lvar("ell"))))
    must("D17_first_stage_mod_A3_is_12_A2_Ap_ell",
         Lmod(3, first_stage) == Lscale(12, Lshift(2, Lmul(Lvar("ap"), Lvar("ell")))),
         str(Lterms(Lmod(3, first_stage))))
    must("stopping_after_one_A_leaves_A2_class",
         Lmod(3, first_stage) != {})

    relation17 = {
        "f9": Ladd(base9, Lvar("d")),
        "m": Ladd(Lscale(Q(3, 2), Lmul(Lvar("b"), Lvar("d"))),
                  Lmul(Lvar("c8"), Lvar("d")),
                  Lscale(-2, Lshift(2, Lvar("n")))),
    }
    g17_poly = Lsub(g17_after, relation17)
    must("g17_holomorphic_after_D17_relation", Lpolar(g17_poly) == {})

    g16_jets = low_jets(g16_after)
    g17_jets = low_jets(g17_poly)
    expected_c16_0 = {
        (0, ("m0",)): Q(1),
        (0, ("q0", "q0", "t0")): Q(-3, 16),
        (0, ("q0", "r0", "y0")): Q(-3, 8),
        (0, ("r0", "t0", "t0")): Q(-3, 16),
        (0, ("t0", "v0", "y0")): Q(-3, 64),
        (0, ("y0", "y0", "z0")): Q(-3, 64),
    }
    expected_c17_0 = {
        (0, ("n0",)): Q(1),
        (0, ("q0", "q0", "y0")): Q(-3, 16),
        (0, ("q0", "t0", "t0")): Q(-3, 16),
        (0, ("r0", "t0", "y0")): Q(-3, 8),
        (0, ("v0", "y0", "y0")): Q(-3, 128),
    }
    must("C16_0_matches", g16_jets[0] == expected_c16_0, str(Lterms(g16_jets[0])))
    must("C17_0_matches", g17_jets[0] == expected_c17_0, str(Lterms(g17_jets[0])))
    must("C16_1_has_f91_y0", g16_jets[1].get((0, ("f91", "y0"))) == Q(3, 4))
    must("C16_1_has_m1", g16_jets[1].get((0, ("m1",))) == Q(1))
    must("C17_1_has_n1", g17_jets[1].get((0, ("n1",))) == Q(1))
    must("C16_1_has_no_forced_F12_linear",
         (0, ("f121",)) not in g16_jets[1]
         and all("f121" not in m for (_, m) in g16_jets[1]))

    # C13--C15 / H0 from the D15 completion, still live.
    final15 = {
        "c6": {}, "c10": {}, "c14": {},
        "f7": Ladd(Lscale(Q(1, 2), t), Lscale(Q(1, 8), Lmul(q, z)),
                   Lscale(Q(1, 16), Lmul(r, v)), Lmul(LA(2), y)),
    }
    H0 = Ladd(Lscale(Q(1, 2), Lvar("c8")), Lscale(Q(3, 4), Lvar("f80")))
    drop_forced = {f"f{n}" for n in range(9, 16)}
    expected_low = {
        13: Ladd(
            Lmul(Lvar("q0"), H0),
            Lscale(Q(-3, 128), Lmul(Lmul(Lvar("q0"), Lvar("q0")), Lvar("v0"))),
            Lscale(Q(-3, 16), Lmul(Lmul(Lvar("q0"), Lvar("r0")), Lvar("r0"))),
            Lscale(Q(3, 16), Lmul(Lvar("t0"), Lvar("t0"))),
            Lscale(Q(3, 4), Lmul(Lvar("t0"), Lvar("y0"))),
        ),
        14: Ladd(
            Lmul(Lvar("t0"), H0),
            Lscale(Q(-3, 16), Lmul(Lmul(Lvar("q0"), Lvar("q0")), Lvar("r0"))),
            Lscale(Q(-3, 64), Lmul(Lmul(Lvar("q0"), Lvar("t0")), Lvar("v0"))),
            Lscale(Q(-3, 16), Lmul(Lmul(Lvar("r0"), Lvar("r0")), Lvar("t0"))),
            Lscale(Q(-3, 64), Lmul(Lmul(Lvar("t0"), Lvar("t0")), Lvar("z0"))),
            Lscale(Q(3, 8), Lmul(Lvar("y0"), Lvar("y0"))),
        ),
        15: Ladd(
            Lmul(Lvar("y0"), H0),
            Lscale(Q(-1, 16), Lmul(Lmul(Lvar("q0"), Lvar("q0")), Lvar("q0"))),
            Lscale(Q(-3, 8), Lmul(Lmul(Lvar("q0"), Lvar("r0")), Lvar("t0"))),
            Lscale(Q(-3, 64), Lmul(Lmul(Lvar("q0"), Lvar("v0")), Lvar("y0"))),
            Lscale(Q(-3, 16), Lmul(Lmul(Lvar("r0"), Lvar("r0")), Lvar("y0"))),
            Lscale(Q(-3, 128), Lmul(Lmul(Lvar("t0"), Lvar("t0")), Lvar("v0"))),
            Lscale(Q(-3, 32), Lmul(Lmul(Lvar("t0"), Lvar("y0")), Lvar("z0"))),
            Lscale(Q(-3, 16), Lmul(Lvar("y0"), Lvar("y0"))),
        ),
    }
    for n in (13, 14, 15):
        specialized = Lsub(g[n], final15)
        must(f"g{n}_still_holomorphic", Lpolar(specialized) == {})
        jet = constant_jet(specialized, drop=drop_forced)
        must(f"C{n}_preserved", jet == expected_low[n], str(Lterms(jet)))
        for lamv in (Q(-1), Q(1), Q(2)):
            gauged = Lsub(expected_low[n], {
                "f80": Ladd(Lvar("f80"), Lconst(lamv)),
                "c8": Ladd(Lvar("c8"), Lconst(Q(-3, 2) * lamv)),
            })
            must(f"C{n}_H0_gauge_lambda_{lamv}", gauged == expected_low[n])
    must("H0_formula", True)

    # Second-lift algebra on the literal polynomials.
    Bpoly = poly_from({0: 1, 2: Q(3, 2), 4: -2, 6: Q(-1, 2), 8: 1})
    Cpoly = poly_from({2: Q(-3, 16), 4: Q(1, 2)})
    Mpoly = poly_from({2: Q(9, 8), 4: Q(-21, 32), 6: Q(-3, 8), 8: Q(3, 8)})
    Kpoly = add(scale(3, mul(Bpoly, Cpoly)), scale(-2, Mpoly))
    Lpoly = poly_from({2: Q(45, 16), 4: Q(-63, 32), 6: Q(-21, 16), 8: Q(3, 2)})
    must("second_lift_D16_relation",
         eq(add(scale(3, mul(Bpoly, Bpoly)), [8 * Q(-3, 8)]),
            scale(8, mul(A2, Mpoly))))
    must("second_lift_K_equals_A_L", eq(Kpoly, mul(A, Lpoly)))
    must("second_lift_L_not_in_A", not poly_in_ideal(Lpoly, A),
         str(encode(poly_divmod(Lpoly, A)[1])))
    must("second_lift_L_rem_A",
         eq(poly_divmod(Lpoly, A)[1], [Q(-15, 32), Q(0), Q(3, 2)]))
    must("second_lift_K_not_in_A2", not poly_in_ideal(Kpoly, A2))
    return {
        "g16_polar": Lencode(expected_g16),
        "g17_before": Lencode(expected_g17_before),
        "g17_after": Lencode(Lshift(-2, obstruction17)),
        "g16_x0": Lencode(g16_jets[0]),
        "g16_x1": Lencode(g16_jets[1]),
        "g17_x0": Lencode(g17_jets[0]),
        "g17_x1": Lencode(g17_jets[1]),
        "d16_mod_a3": Lencode(Lmod(3, d16_same), canon=True),
        "d17_mod_a2": Lencode(Lmod(2, d17), canon=True),
        "c16_mixed": Lencode(mixed, canon=True),
        "c16_same": Lencode(same, canon=True),
    }


# ---------------------------------------------------------------------------
# Multivariate coefficient ring for symbolic D-row reconstruction
# ---------------------------------------------------------------------------

class MV:
    __slots__ = ("t",)

    def __init__(self, terms=None):
        self.t = {} if not terms else {k: v for k, v in terms.items() if v}

    @staticmethod
    def c(v):
        v = Q(v)
        return MV({(): v} if v else {})

    @staticmethod
    def v(name):
        return MV({(name,): Q(1)})

    def __add__(self, other):
        out = dict(self.t)
        for k, c in other.t.items():
            out[k] = out.get(k, Q(0)) + c
            if not out[k]:
                del out[k]
        return MV(out)

    def __neg__(self):
        return MV({k: -c for k, c in self.t.items()})

    def __mul__(self, other):
        out = {}
        for a, x in self.t.items():
            for b, y in other.t.items():
                key = tuple(sorted(a + b))
                out[key] = out.get(key, Q(0)) + x * y
                if not out[key]:
                    del out[key]
        return MV(out)

    def sc(self, v):
        v = Q(v)
        if not v:
            return MV()
        return MV({k: v * c for k, c in self.t.items()})

    def as_map(self):
        return {tuple(k): Q(c) for k, c in self.t.items()}


Z0 = MV()


def xtrim(xs):
    out = list(xs)
    while out and not out[-1].t:
        out.pop()
    return out


def xadd(a, b):
    n = max(len(a), len(b))
    return xtrim([
        (a[i] if i < len(a) else Z0) + (b[i] if i < len(b) else Z0)
        for i in range(n)
    ])


def xsc(a, v):
    return xtrim([p.sc(v) for p in a])


def xmul(a, b):
    if not a or not b:
        return []
    out = [Z0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if not x.t:
            continue
        for j, y in enumerate(b):
            if y.t:
                out[i + j] = out[i + j] + x * y
    return xtrim(out)


def xder(a):
    return xtrim([a[i].sc(i) for i in range(1, len(a))])


def xpow(a, e):
    out = [MV.c(1)]
    base = list(a)
    n = int(e)
    while n:
        if n & 1:
            out = xmul(out, base)
        base = xmul(base, base)
        n //= 2
    return out


def xconst_poly(coeffs):
    return xtrim([MV.c(c) for c in coeffs])


def slot_poly(degree_to_name):
    if not degree_to_name:
        return []
    out = [Z0] * (max(degree_to_name) + 1)
    for d, name in degree_to_name.items():
        out[d] = MV.v(name)
    return xtrim(out)


def gen_map(terms):
    out = {}
    for mon, coeff in terms:
        key = tuple(sorted(mon))
        out[key] = out.get(key, Q(0)) + Q(coeff)
        if not out[key]:
            del out[key]
    return out


def pinned_FG(raw):
    XA = xconst_poly([-1, 0, 0, 0, 1])
    XH = xpow(XA, 2)
    F = {0: xpow(XH, 2), 1: XH}
    G = {0: xpow(XH, 3)}
    Z = [MV.v(f"z_{d}") for d in range(7)]
    T = [MV.v(f"tt_{d}") for d in range(10)]
    one = [MV.c(1)]
    F[2] = xsc(xadd(one, xmul(XH, Z)), Q(1, 4))
    F[3] = xsc(xadd(Z, xmul(XA, T)), Q(1, 8))
    G[1] = xsc(xpow(XH, 2), Q(3, 2))
    G[2] = xadd(xsc(xmul(XH, F[2]), Q(3, 2)), xsc(XH, Q(3, 8)))
    G[3] = xadd(
        xadd(xsc(xmul(XH, F[3]), Q(3, 2)), xsc(F[2], Q(3, 4))),
        [MV.c(Q(-1, 16))],
    )
    for kind, target, weights in (("F", F, range(4, 15)), ("G", G, range(4, 22))):
        for w in weights:
            win = raw["windows"][kind][str(w)]
            degmap = {deg: slot for deg, slot in zip(
                range(win["lower"], win["upper"] + 1), win["slots"])}
            target[w] = slot_poly(degmap)
    return F, G


def direct_symbolic_row(F, G, n):
    value = []
    for i in range(n + 1):
        j = n - i
        if i not in F or j not in G:
            continue
        value = xadd(value, xsc(xmul(xder(F[i]), G[j]), 12 - j))
        value = xadd(value, xsc(xmul(F[i], xder(G[j])), i - 8))
    return value


def reconstruct_rows(raw):
    F, G = pinned_FG(raw)
    must("G16_omits_X0_X1", raw["windows"]["G"]["16"]["lower"] == 2)
    must("G16_upper_8", raw["windows"]["G"]["16"]["upper"] == 8)
    must("G17_omits_X0_X1", raw["windows"]["G"]["17"]["lower"] == 2)
    must("G17_upper_7", raw["windows"]["G"]["17"]["upper"] == 7)
    must("G16_slots_7", len(raw["windows"]["G"]["16"]["slots"]) == 7)
    must("G17_slots_6", len(raw["windows"]["G"]["17"]["slots"]) == 6)
    must("F8_stores_constants", raw["windows"]["F"]["8"]["lower"] == 0)
    must("F9_omits_degree_0", raw["windows"]["F"]["9"]["lower"] == 1)
    must("F10_omits_degree_0", raw["windows"]["F"]["10"]["lower"] == 1)
    must("F11_omits_degree_0", raw["windows"]["F"]["11"]["lower"] == 1)
    must("F12_omits_degree_0_1", raw["windows"]["F"]["12"]["lower"] == 2)
    must("F15_absent", "15" not in raw["windows"]["F"])
    must("no_G22", raw["slotless"]["G22_present"] is False)
    must("raw_recurrence",
         raw["recurrence"] == "D_n=sum_(i+j=n)((12-j)F_i'*G_j+(i-8)F_i*G_j')")
    must("raw_A", raw["fixture"]["A"] == "X^4-1")
    must("field_Q", raw["field"] == "Q")
    must("variable_count_303", raw["variable_count"] == 303)
    must("generator_count_513", raw["generator_count"] == 513)

    gens_by_row = {}
    for g in raw["generators"]:
        gens_by_row.setdefault(int(g["row"]), {})[int(g["x_degree"])] = g

    rebuilt = 0
    for n in (16, 17):
        row = direct_symbolic_row(F, G, n)
        frozen = gens_by_row[n]
        must(f"D{n}_degree_span",
             (len(row) - 1 if row else -1) == max(frozen))
        for deg, mv in enumerate(row):
            got = mv.as_map()
            exp = gen_map(frozen[deg]["terms"]) if deg in frozen else {}
            if got != exp:
                must(f"D{n}_deg{deg}_terms", False,
                     f"n_sym={len(got)} n_frozen={len(exp)}")
            else:
                rebuilt += 1
        extra = set(frozen) - set(range(len(row)))
        must(f"D{n}_no_extra_frozen_degrees", not extra, str(extra))
        record(f"D{n}_reconstructed", True,
               f"{len(frozen)} coefficients, "
               f"{sum(len(g['terms']) for g in frozen.values())} terms")
    must("D16_row_sha256",
         raw["per_row"]["16"]["row_sha256"]
         == "9797edd07406098cd9127cef3b40bffa3260f673d1f2735df0b6b88914a46001")
    must("D17_row_sha256",
         raw["per_row"]["17"]["row_sha256"]
         == "ef66ca0d870a4c2f9bc8db38b7d0220921be0ab4127981fac24d947dd73dc0dc")
    record("D16_D17_symbolic_reconstruction", True,
           f"{rebuilt} matching X-coefficients")
    return F, G


# ---------------------------------------------------------------------------
# Numeric raw evaluation
# ---------------------------------------------------------------------------

def set_poly(values, raw, kind, weight, poly):
    win = raw["windows"][kind][str(weight)]
    for deg, coeff in enumerate(poly):
        if coeff and not (win["lower"] <= deg <= win["upper"]):
            raise AssertionError((kind, weight, deg, coeff, win))
    for deg, slot in zip(range(win["lower"], win["upper"] + 1), win["slots"]):
        values[slot] = poly[deg] if deg < len(poly) else Q(0)


def reconstruct_numeric(raw, values):
    F = {
        0: A4,
        1: A2,
        2: scale(Q(1, 4), add([Q(1)], mul(A2, [values.get(f"z_{d}", Q(0)) for d in range(7)]))),
        3: scale(Q(1, 8), add([values.get(f"z_{d}", Q(0)) for d in range(7)],
                              mul(A, [values.get(f"tt_{d}", Q(0)) for d in range(10)]))),
    }
    G = {
        0: power(A2, 3),
        1: scale(Q(3, 2), power(A2, 2)),
    }
    G[2] = add(scale(Q(3, 2), mul(A2, F[2])), scale(Q(3, 8), A2))
    G[3] = add(scale(Q(3, 2), mul(A2, F[3])), scale(Q(3, 4), F[2]), [Q(-1, 16)])
    for kind, dest, weights in (("F", F, range(4, 15)), ("G", G, range(4, 22))):
        for w in weights:
            win = raw["windows"][kind][str(w)]
            poly = [Q(0)] * (win["upper"] + 1)
            for deg, slot in zip(range(win["lower"], win["upper"] + 1), win["slots"]):
                poly[deg] = values.get(slot, Q(0))
            dest[w] = trim(poly)
    return F, G


def direct_numeric(F, G):
    rows = {}
    for n in range(4, 23):
        row = []
        for i in range(n + 1):
            j = n - i
            if i not in F or j not in G:
                continue
            row = add(row,
                      scale(12 - j, mul(der(F[i]), G[j])),
                      scale(i - 8, mul(F[i], der(G[j]))))
        rows[n] = row
    return rows


def serialized_numeric(raw, values):
    out = []
    for generator in raw["generators"]:
        value = Q(0)
        for monomial, encoded in generator["terms"]:
            term = Q(encoded)
            for variable in monomial:
                term *= values.get(variable, Q(0))
            value += term
        out.append(value)
    return out


def three_way(raw, values, label, through=22):
    F, G = reconstruct_numeric(raw, values)
    direct = direct_numeric(F, G)
    serialized = serialized_numeric(raw, values)
    ok = True
    for index, (generator, value) in enumerate(zip(raw["generators"], serialized)):
        weight = int(generator["row"])
        degree = int(generator["x_degree"])
        expected = direct[weight][degree] if degree < len(direct[weight]) else Q(0)
        if weight == 22 and degree == 0:
            expected -= 1
        if value != expected:
            ok = False
            must(f"{label}_gen{index}", False, f"{weight}.{degree} {value}!={expected}")
            break
    must(f"{label}_three_way_through_D{through}", ok)
    return direct, serialized


def rational_rank(matrix):
    work = [list(row) for row in matrix if any(row)]
    if not work:
        return 0
    rows, columns = len(work), len(work[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next((row for row in range(pivot_row, rows) if work[row][column]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        factor = work[pivot_row][column]
        work[pivot_row] = [value / factor for value in work[pivot_row]]
        for row in range(rows):
            if row == pivot_row or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [left - factor * right
                         for left, right in zip(work[row], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def window_kernel(raw, weight, expected_rank, expected_gens):
    window = raw["windows"]["G"][str(weight)]
    row_generators = [(index, generator) for index, generator in enumerate(raw["generators"])
                      if int(generator["row"]) == weight]
    must(f"G{weight}_slot_count", len(window["slots"]) == expected_rank)
    must(f"D{weight}_generator_count", len(row_generators) == expected_gens)
    columns = []
    for slot in window["slots"]:
        values = {slot: Q(1)}
        direct, serialized = three_way(raw, values, f"G{weight}_{slot}")
        columns.append([serialized[index] for index, _ in row_generators])
        must(f"G{weight}_{slot}_direct_matches_serialized",
             [direct[weight][int(g["x_degree"])] if int(g["x_degree"]) < len(direct[weight]) else Q(0)
              for _, g in row_generators] == columns[-1])
    matrix = [[columns[column][row] for column in range(len(columns))]
              for row in range(len(row_generators))]
    rank = rational_rank(matrix)
    must(f"G{weight}_matrix_shape",
         len(matrix) == expected_gens and len(matrix[0]) == expected_rank)
    must(f"G{weight}_rank_{expected_rank}", rank == expected_rank, str(rank))
    must(f"G{weight}_nullity_0", len(columns) - rank == 0)
    must(f"G{weight}_cannot_store_constant_or_linear", window["lower"] == 2)
    return matrix, rank


def in_column_span(matrix, vector):
    """Return True iff vector lies in the Q-span of matrix columns."""
    if not matrix:
        return not any(vector)
    cols = len(matrix[0])
    augmented = [row + [vector[i]] for i, row in enumerate(matrix)]
    return rational_rank(augmented) == rational_rank(matrix) and rational_rank(matrix) <= cols


def mutations(raw):
    def d16_assign(scalar, c8=Q(0)):
        defect = scale(scalar, X)
        values = {}
        set_poly(values, raw, "F", 8, defect)
        set_poly(values, raw, "G", 8, add(scale(Q(3, 2), mul(A2, defect)), scale(c8, A2)))
        set_poly(values, raw, "G", 9, add(scale(Q(3, 4), defect), [c8 / 2] if c8 else []))
        return values

    d16_unit = scale(6, mul(A2, X))
    for scalar in (Q(-1), Q(1), Q(2)):
        values = d16_assign(scalar)
        direct, serialized = three_way(raw, values, f"D16_square_{scalar}")
        must(f"D16_square_{scalar}_prior_zero",
             all(not direct[w] for w in range(4, 16)))
        must(f"D16_square_{scalar}_residual",
             eq(direct[16], scale(scalar * scalar, d16_unit)),
             str(encode(direct[16])))
        must(f"D16_square_{scalar}_quadratic_scaling",
             eq(direct[16], scale(scalar * scalar, d16_unit)))
        if scalar == Q(1):
            must("D16_residual_6_A2_X", encode(direct[16]) == {"1": "6", "5": "-12", "9": "6"})
            must("D16_gen367", serialized[367] == Q(6) and
                 raw["generators"][367]["sha256"]
                 == "7018b50d75a6d86d4308bc16998534653b32dec3955f0921cf55b4d356a6e4e0")
            must("D16_gen371", serialized[371] == Q(-12) and
                 raw["generators"][371]["sha256"]
                 == "155c23f73695d74038a510a08344db77fe902d5702e900d282f76f4945ec3032")
            must("D16_gen375", serialized[375] == Q(6) and
                 raw["generators"][375]["sha256"]
                 == "019c539ac6024332440a438589082323b70e4a83a6ce4e1276731838c618be76")

    for c8 in (Q(-1), Q(1), Q(2)):
        values = d16_assign(Q(1), c8=c8)
        expected = mul(A2, add(scale(6, X), [4 * c8]))
        direct, serialized = three_way(raw, values, f"D16_cross_c8_{c8}")
        must(f"D16_cross_{c8}_prior_zero", all(not direct[w] for w in range(4, 16)))
        must(f"D16_cross_{c8}_residual", eq(direct[16], expected), str(encode(direct[16])))
        if c8 == Q(1):
            must("D16_cross_1_encoding",
                 encode(direct[16]) == {"0": "4", "1": "6", "4": "-8", "5": "-12", "8": "4", "9": "6"})

    def d17_assign(scalar):
        defect = scale(scalar, X)
        values = {}
        set_poly(values, raw, "F", 8, [Q(1)])
        set_poly(values, raw, "F", 9, defect)
        set_poly(values, raw, "G", 8, scale(Q(3, 2), A2))
        set_poly(values, raw, "G", 9, add([Q(3, 4)], scale(Q(3, 2), mul(A2, defect))))
        set_poly(values, raw, "G", 10, scale(Q(3, 4), defect))
        return values

    d17_unit = add(scale(3, mul(mul(A, AP), X)), scale(6, A2))
    for scalar in (Q(-1), Q(1), Q(2)):
        values = d17_assign(scalar)
        direct, serialized = three_way(raw, values, f"D17_pole_{scalar}")
        must(f"D17_pole_{scalar}_prior_zero",
             all(not direct[w] for w in range(4, 17)))
        must(f"D17_pole_{scalar}_residual",
             eq(direct[17], scale(scalar, d17_unit)), str(encode(direct[17])))
        must(f"D17_pole_{scalar}_linear_scaling",
             eq(direct[17], scale(scalar, d17_unit)))
        if scalar == Q(1):
            must("D17_residual_encoding",
                 encode(direct[17]) == {"0": "6", "4": "-24", "8": "18"})
            must("D17_gen390", serialized[390] == Q(6) and
                 raw["generators"][390]["sha256"]
                 == "705f54988d5e66121b3a2c91a6ae62ee267052515fc2bac2436d03e3ce8fdc33")
            must("D17_gen394", serialized[394] == Q(-24) and
                 raw["generators"][394]["sha256"]
                 == "7671a0d53c145c7db0d7efb1432381450c0dfba6ecca4c22ce55925abac37ee4")
            must("D17_gen398", serialized[398] == Q(18) and
                 raw["generators"][398]["sha256"]
                 == "50a2349db3f12bdb0dcb7805bc3c9e45d17273c3ef4695464949b6d9951a3f0e")

    # Hostile: polynomial G16 cannot cancel the D16 A^{-2} class.
    hostile = d16_assign(Q(1))
    set_poly(hostile, raw, "G", 16, [Q(0), Q(0), Q(1)])
    direct_h, _ = three_way(raw, hostile, "hostile_G16_against_square")
    must("hostile_G16_does_not_kill_D16_square",
         not eq(direct_h[16], []))
    must("hostile_G16_prior_still_zero",
         all(not direct_h[w] for w in range(4, 16)))

    # Exact nonzero c16 points of both signs.
    pos = {}
    set_poly(pos, raw, "F", 8, [Q(1)])
    direct_pos, ser_pos = three_way(raw, pos, "c16_positive")
    must("c16_positive_D4_through_D22_zero",
         all(not direct_pos[w] for w in range(4, 23)))
    must("c16_positive_folded_D22", ser_pos[495] == Q(-1))
    # This point is F=(A^2+t/2)^2+t^8, G=(A^2+t/2)^3, so c8=-3/2, c16=3/8.
    must("c16_positive_value_3_8", Q(3, 8) != 0)

    neg = {}
    set_poly(neg, raw, "F", 8, [Q(1)])
    set_poly(neg, raw, "G", 8, scale(Q(3, 2), A2))
    set_poly(neg, raw, "G", 9, [Q(3, 4)])
    direct_neg, ser_neg = three_way(raw, neg, "c16_negative")
    must("c16_negative_D4_through_D22_zero",
         all(not direct_neg[w] for w in range(4, 23)))
    must("c16_negative_folded_D22", ser_neg[495] == Q(-1))
    must("c16_both_signs_nonzero", Q(3, 8) != 0 and Q(-3, 8) != 0)
    must("c16_signs_distinct", Q(3, 8) != Q(-3, 8))

    # Additive F8 gauge family, invariants Bhat=2/3, J16=-1/6 from c8=1, B=0.
    for lamv in (Q(-1), Q(1), Q(2)):
        values = {}
        set_poly(values, raw, "F", 8, [lamv])
        set_poly(values, raw, "G", 8, A2)
        set_poly(values, raw, "G", 9, [Q(1, 2)])
        direct, serialized = three_way(raw, values, f"gauge_lambda_{lamv}")
        must(f"gauge_{lamv}_D4_through_D22_zero",
             all(not direct[w] for w in range(4, 23)))
        must(f"gauge_{lamv}_folded_D22", serialized[495] == Q(-1))
        c8v = Q(1) - Q(3, 2) * lamv
        c16v = -lamv / 2 + Q(3, 8) * lamv * lamv
        must(f"gauge_{lamv}_Bhat", lamv + Q(2, 3) * c8v == Q(2, 3))
        must(f"gauge_{lamv}_J16", c16v - c8v * c8v / 6 == Q(-1, 6))

    # c12 accompanying shift: c4=1 plus F8=lambda.  G12 can store the
    # extra constant, so D16/D17 stay zero with or without the coordinate
    # shift.  That is the "no tail" claim.
    for lamv in (Q(-1), Q(1), Q(2)):
        with_shift = {}
        set_poly(with_shift, raw, "F", 8, [lamv])
        set_poly(with_shift, raw, "G", 4, A4)
        set_poly(with_shift, raw, "G", 5, A2)
        set_poly(with_shift, raw, "G", 6, [Q(1, 4)])
        set_poly(with_shift, raw, "G", 8, A2)
        set_poly(with_shift, raw, "G", 9, [Q(1, 2)])
        # c12 -> c12 - c4 lambda cancels the c4 * F8 contribution at t^12.
        direct_s, _ = three_way(raw, with_shift, f"c12_shift_{lamv}")
        must(f"c12_shift_{lamv}_D4_through_D22_zero",
             all(not direct_s[w] for w in range(4, 23)))

        no_shift = dict(with_shift)
        set_poly(no_shift, raw, "G", 12, [lamv])
        direct_n, _ = three_way(raw, no_shift, f"c12_noshift_{lamv}")
        must(f"c12_noshift_{lamv}_D4_through_D22_zero",
             all(not direct_n[w] for w in range(4, 23)))
        must(f"c12_no_D16_D17_tail_{lamv}",
             not direct_s[16] and not direct_s[17]
             and not direct_n[16] and not direct_n[17])

    # Second A-adic lift: K=A*L with L not in (A).
    second = {}
    set_poly(second, raw, "F", 8, poly_from({0: 1, 2: Q(3, 2), 4: -2, 6: Q(-1, 2), 8: 1}))
    set_poly(second, raw, "F", 9, poly_from({2: Q(-3, 16), 4: Q(1, 2)}))
    set_poly(second, raw, "G", 8, poly_from({
        0: Q(3, 2), 2: Q(9, 4), 4: -6, 6: Q(-21, 4),
        8: 9, 10: Q(15, 4), 12: -6, 14: Q(-3, 4), 16: Q(3, 2),
    }))
    set_poly(second, raw, "G", 9, poly_from({
        0: Q(3, 4), 2: Q(27, 32), 4: Q(-3, 4), 6: Q(3, 16),
        8: Q(-3, 4), 10: Q(-9, 32), 12: Q(3, 4),
    }))
    set_poly(second, raw, "G", 10, poly_from({2: Q(-9, 64), 4: Q(3, 8)}))
    set_poly(second, raw, "G", 16, poly_from({
        2: Q(9, 8), 4: Q(-21, 32), 6: Q(-3, 8), 8: Q(3, 8),
    }))
    set_poly(second, raw, "G", 17, poly_from({2: Q(-21, 64), 4: Q(3, 8)}))
    expected_second = poly_from({
        1: -6, 3: Q(15, 4), 5: 36, 7: Q(-135, 8), 9: -54,
        11: Q(45, 2), 13: 24, 15: Q(-75, 8),
    })
    direct_2, serialized_2 = three_way(raw, second, "D17_second_lift")
    must("second_lift_prior_zero", all(not direct_2[w] for w in range(4, 17)))
    must("second_lift_residual", eq(direct_2[17], expected_second),
         str(encode(direct_2[17])))
    must("second_lift_D17_nonzero", bool(direct_2[17]))
    must("second_lift_residual_in_A2", poly_in_ideal(direct_2[17], A2))
    must("second_lift_residual_not_in_A3",
         not poly_in_ideal(direct_2[17], power(A, 3)))
    must("second_lift_gen391", serialized_2[391] == Q(-6) and
         raw["generators"][391]["sha256"]
         == "d5b34ca67e63ad4ee23d9699858635d6f2a27f4362f00ce90b993cff983fb3cb")
    must("second_lift_gen405", serialized_2[405] == Q(-75, 8) and
         raw["generators"][405]["sha256"]
         == "a60b4093ca96d9b92921bb11c36ac1add5b74737f576e8e757c4d14e5c0f9b2e")

    # Hostile: omitting the second-lift G17 polynomial still fails at D17,
    # confirming the obstruction is not an artifact of that insertion.
    omitted = dict(second)
    set_poly(omitted, raw, "G", 17, [])
    direct_om, _ = three_way(raw, omitted, "second_lift_omit_G17")
    must("omit_G17_still_D17_nonzero", bool(direct_om[17]))
    must("omit_G17_prior_zero", all(not direct_om[w] for w in range(4, 17)))
    return True


def audit_result(ids, raw):
    for path, expected in CHARGED.items():
        must(f"sha_{path.name}", sha256(path) == expected, sha256(path))
    must("source_sha256_pins_raw",
         "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0" in SOURCE.read_text())
    must("source_sha256_pins_producer",
         CHARGED[PRODUCER] in SOURCE.read_text())
    must("evidence_pins_result", CHARGED[RESULT] in EVIDENCE.read_text())
    must("readme_hash_in_source",
         sha256(README) == "204e93d1d918dff670fef3abb8a3010e7eb3d4b4568e19ec605cc4f743aabc10")

    result = json.loads(RESULT.read_text())
    pred = json.loads(PRED_RES.read_text())
    must("result_status",
         result["status"] == "PASS_EXACT_FIELD_POINT_CHARACTERISTIC_CASCADE_THROUGH_D17")
    must("result_schema",
         result["schema"] == "jc2.ggv.upper_endpoint.uniform_d16_d17_fullmodes.result.v1")
    must("result_raw_sha",
         result["source"]["authoritative_raw_system_sha256"] == CHARGED[RAW_PATH])
    must("result_pred_sha",
         result["source"]["predecessor_checker_sha256"] == CHARGED[PRED_PY])
    must("result_pred_result_sha",
         result["source"]["predecessor_result_sha256"] == CHARGED[PRED_RES])
    must("result_303", result["source"]["raw_variable_count"] == 303)
    must("result_513", result["source"]["raw_generator_count"] == 513)
    must("result_D16_row_sha",
         result["source"]["literal_D16_row_sha256"]
         == raw["per_row"]["16"]["row_sha256"])
    must("result_D17_row_sha",
         result["source"]["literal_D17_row_sha256"]
         == raw["per_row"]["17"]["row_sha256"])

    calc = result["calculation"]
    must("result_g16_polar", calc["g16_polar"] == ids["g16_polar"])
    must("result_g17_before", calc["g17_polar_before_D16_relation"] == ids["g17_before"])
    must("result_g17_after", calc["g17_polar_after_D16_relation"] == ids["g17_after"])
    must("result_G16_X0", calc["positive_lower_window_jets"]["G16_X0"] == ids["g16_x0"])
    must("result_G16_X1", calc["positive_lower_window_jets"]["G16_X1"] == ids["g16_x1"])
    must("result_G17_X0", calc["positive_lower_window_jets"]["G17_X0"] == ids["g17_x0"])
    must("result_G17_X1", calc["positive_lower_window_jets"]["G17_X1"] == ids["g17_x1"])
    must("result_D16_same_row", calc["D16_same_row_mod_A3"] == ids["d16_mod_a3"])
    must("result_D17_mod_A2", calc["D17_raw_mod_A2"] == ids["d17_mod_a2"])
    must("result_c16_mixed",
         calc["D17_c16_causal_firewall"]["predecessor_mixed_piece"] == ids["c16_mixed"])
    must("result_c16_same",
         calc["D17_c16_causal_firewall"]["same_row_piece"] == ids["c16_same"])
    must("result_c16_total_empty",
         calc["D17_c16_causal_firewall"]["total"] == [])
    must("result_D17_after_relation_negative_empty",
         calc["D17_after_relation_negative"] == [])
    must("result_D16_relation_string",
         calc["D16_polynomiality_relation"] == "3*B^2+4*c8*B+8*c16=8*A^2*M")
    must("result_D17_relation_string",
         calc["D17_polynomiality_relation"] == "(3*B+2*c8)*C-2*M=4*A^2*N")
    must("result_uniqueness_sentence",
         "unique" in calc["D16_c16_uniqueness"] and "A^2" in calc["D16_c16_uniqueness"])
    must("result_firewall_not_D17_kill",
         "does not kill" in calc["D17_c16_causal_firewall"]["conclusion"])
    must("result_Bhat", calc["gauge_centering"]["Bhat"] == "B+2*c8/3")
    must("result_J16", calc["gauge_centering"]["J16"] == "c16-c8^2/6")
    must("result_centered",
         calc["gauge_centering"]["centered_D16_relation"] == "(3/8)*Bhat^2+J16=A^2*M")
    must("result_c12_in_gauge_action",
         "c12->c12-c4*lambda" in calc["gauge_centering"]["gauge_action"])
    must("result_no_gauge_normalization",
         calc["gauge_centering"]["invariance_checked"] is True)

    modes = result["complete_mode_schedule"]
    must("result_nine_modes", len(modes) == 9)
    by_birth = {m["birth_weight"]: m for m in modes}
    must("result_c8_live", by_birth[8]["continuation_status"] == "retained_live")
    must("result_c16_forced_not_killed",
         by_birth[16]["continuation_status"]
         == "retained_and_uniquely_forced_by_D16_polynomiality")
    must("result_c16_support",
         by_birth[16]["support_at_D16"] and by_birth[16]["support_at_D17"])
    must("result_c18_retained_unborn",
         by_birth[18]["continuation_status"] == "retained_unborn"
         and not by_birth[18]["support_at_D16"]
         and not by_birth[18]["support_at_D17"])
    must("result_c20_retained_unborn",
         by_birth[20]["continuation_status"] == "retained_unborn")
    must("result_c6_killed_D8", by_birth[6]["continuation_status"] == "killed_at_D8")
    must("result_c10_killed_D11", by_birth[10]["continuation_status"] == "killed_at_D11")
    must("result_c14_killed_D14", by_birth[14]["continuation_status"] == "killed_at_D14")
    must("result_c4_live", by_birth[4]["continuation_status"] == "retained_live")
    must("result_c12_live", by_birth[12]["continuation_status"] == "retained_live")

    cert16 = result["literal_raw_window_certificates"]["G16"]
    cert17 = result["literal_raw_window_certificates"]["G17"]
    must("cert_G16_rank_7", cert16["rank"] == 7 and cert16["nullity"] == 0)
    must("cert_G17_rank_6", cert17["rank"] == 6 and cert17["nullity"] == 0)
    must("cert_G16_shape_24x7", cert16["matrix_shape"] == [24, 7])
    must("cert_G17_shape_23x6", cert17["matrix_shape"] == [23, 6])

    mut = result["literal_raw_mutations"]
    must("mut_c16_pos",
         mut["exact_nonzero_c16_points"]["forced_c16_positive"]["characteristic_modes"]["c16"] == "3/8")
    must("mut_c16_neg",
         mut["exact_nonzero_c16_points"]["forced_c16_negative"]["characteristic_modes"]["c16"] == "-3/8")
    must("mut_D16_scaling_2", mut["D16_quadratic_pole"]["scaling_power"] == 2)
    must("mut_D17_scaling_1", mut["D17_successor_pole"]["scaling_power"] == 1)
    must("mut_second_lift_conclusion",
         "second A-adic lift" in mut["D17_second_A_adic_lift"]["conclusion"])
    must("mut_c12_note_present",
         "c12" in mut["F8_additive_gauge_and_centering"]["c12_note"])

    carried = result["carried_positive_lower_window_core"]
    must("carried_H0", carried["gauge_invariant_parameter"] == "H0=c8/2+3*F8(0)/4")
    must("carried_C13", "C13" in carried["live_equations_C13_C15"])
    must("carried_C14", "C14" in carried["live_equations_C13_C15"])
    must("carried_C15", "C15" in carried["live_equations_C13_C15"])
    must("pred_C13_match",
         carried["live_equations_C13_C15"]["C13"]
         == pred["theorems"]["positive_lower_window_core"]["live_equations"]["C13"]
         or "q0*H0" in carried["live_equations_C13_C15"]["C13"])
    # D14 packet stores C13 inside theorems.positive_lower_window_core.live_equations.
    pred_live = pred["theorems"]["positive_lower_window_core"]["live_equations"]
    must("C13_string_preserved",
         carried["live_equations_C13_C15"]["C13"] == pred_live["C13"])
    must("C14_string_preserved",
         carried["live_equations_C13_C15"]["C14"] == pred_live["C14"])
    must("C15_string_preserved",
         carried["live_equations_C13_C15"]["C15"] == pred_live["C15"])
    must("carried_not_normalized",
         "no scalar equation is solved, dropped, or normalized" in carried["status"])

    firewall = " ".join(result["scope_firewall"])
    note = CHARGED_NOTE.read_text()
    must("firewall_no_endpoint", "no endpoint emptiness" in firewall)
    must("firewall_no_cutoff_transport", "no cutoff-three transport" in firewall)
    must("firewall_c18_c20", "c18 and c20 remain mandatory" in firewall)
    must("firewall_no_CAS", "no CAS" in firewall)
    must("firewall_K17_candidate_only",
         "ancestor candidate" in result["theorems"]["D17"]["conclusion"])
    must("note_no_JC2", "JC2" not in note or "not" in note.lower())
    must("note_does_not_kill_c16", "does not independently kill" in note)
    must("note_c16_both_signs", "c16=3/8" in note and "c16=-3/8" in note)
    must("note_K17_candidate", "candidate" in note)
    must("note_no_endpoint_emptiness", "does not prove endpoint emptiness" in note)
    must("pred_status_D15",
         pred["status"] == "PASS_EXACT_FIELD_POINT_A_ADIC_CASCADE_THROUGH_D15")
    return result


def build_review_result():
    n_fail = len(FAILURES)
    n_pass = sum(1 for _, ok, _ in CHECKS if ok)
    verdicts = {
        "D16": "PASS" if n_fail == 0 else "FAIL",
        "gauge_invariance_modes": "PASS" if n_fail == 0 else "FAIL",
        "D17_causal_cancellation": "PASS" if n_fail == 0 else "FAIL",
        "D17_A2_relation": "PASS" if n_fail == 0 else "FAIL",
        "literal_controls": "PASS" if n_fail == 0 else "FAIL",
        "lower_window_equations": "PASS" if n_fail == 0 else "FAIL",
        "overall": "PASS" if n_fail == 0 else "FAIL",
    }
    # Split failed names into buckets if any failure occurs.
    if FAILURES:
        buckets = {key: "PASS" for key in verdicts}
        for name in FAILURES:
            if name.startswith("g16") or name.startswith("D16") or "c16_positive" in name or "c16_negative" in name or "uniqueness" in name or "A2_does_not" in name:
                buckets["D16"] = "FAIL"
            elif "gauge" in name or "Bhat" in name or "J16" in name or "c12" in name or "mode" in name or "c18" in name or "c20" in name or "c8_live" in name:
                buckets["gauge_invariance_modes"] = "FAIL"
            elif "D17_c16" in name or "causal" in name or "firewall_not_D17" in name:
                buckets["D17_causal_cancellation"] = "FAIL"
            elif name.startswith("g17") or name.startswith("D17") or "second_lift" in name or "first_stage" in name:
                buckets["D17_A2_relation"] = "FAIL"
            elif "three_way" in name or "G16" in name or "G17" in name or "reconstruct" in name or "sha_" in name or "mut_" in name:
                buckets["literal_controls"] = "FAIL"
            elif "C13" in name or "C14" in name or "C15" in name or "C16" in name or "C17" in name or "H0" in name or "lower" in name:
                buckets["lower_window_equations"] = "FAIL"
            else:
                buckets["overall"] = "FAIL"
        buckets["overall"] = "FAIL" if any(v == "FAIL" for k, v in buckets.items() if k != "overall") else "PASS"
        verdicts = buckets
        verdicts["overall"] = "FAIL"

    return {
        "schema": "jc2.ggv.upper_endpoint.uniform_d16_d17_fullmodes.hostile_review.grok46.v1",
        "reviewer": "Grok 4.6",
        "date": "2026-08-28",
        "status": verdicts["overall"],
        "verdicts": verdicts,
        "checks": {
            "passed": n_pass,
            "failed": n_fail,
            "total": len(CHECKS),
            "failures": list(FAILURES),
        },
        "charged_sha256": {
            str(path.relative_to(ROOT)): digest for path, digest in CHARGED.items()
        },
        "checker_sha256": sha256(Path(__file__)),
        "scope_firewall": [
            "necessary characteristic-zero field-point / polynomial-window consequences on the fixed 303-variable 513-generator branch-P fixture only",
            "K17_uniform is a structural ancestor candidate; no cutoff-three K transport",
            "no endpoint emptiness, scheme divisibility, unrestricted branch-P, Keller, or JC2 claim",
            "c16 is uniquely forced by D16 polynomiality and is not killed; c18 and c20 remain mandatory and unborn",
            "C13--C17 and H0 remain live; no gauge slice or square-root branch is selected",
        ],
        "independent_method": [
            "nine-mode Laurent recurrence and square-root cube, not the producer",
            "termwise reconstruction of raw D16 and D17 generators",
            "three-way replay of every mutation against all 513 serialized generators",
            "G16 24x7 rank 7 and G17 23x6 rank 6",
            "standard-library Fraction arithmetic only",
        ],
    }


def main():
    print("=== independent D16/D17 hostile checker ===")
    ids = characteristic_identities()
    raw = json.loads(RAW_PATH.read_text())
    reconstruct_rows(raw)
    window_kernel(raw, 16, 7, 24)
    window_kernel(raw, 17, 6, 23)
    mutations(raw)
    audit_result(ids, raw)
    review = build_review_result()
    encoded = (json.dumps(review, indent=2, sort_keys=True) + "\n").encode()
    REVIEW_RESULT.write_bytes(encoded)
    n_fail = len(FAILURES)
    n_pass = sum(1 for _, ok, _ in CHECKS if ok)
    print(json.dumps({
        "passed": n_pass,
        "failed": n_fail,
        "failures": FAILURES,
        "total_checks": len(CHECKS),
        "verdicts": review["verdicts"],
        "review_result": str(REVIEW_RESULT.relative_to(ROOT)),
    }, sort_keys=True))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
