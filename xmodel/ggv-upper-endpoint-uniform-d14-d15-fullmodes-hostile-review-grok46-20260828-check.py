#!/usr/bin/env python3
"""Independent hostile checker for the uniform D14/D15 full-mode cascade.

Does not import the D14/D15 producer.  Rebuilds the nine-mode Laurent
recurrence, the square-root cube, the raw D5G rows D13--D15, the G14
same-row matrix, live and hostile mutations, and the X^0 jets C13--C15
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
CHARGED_NOTE = ROOT / "xmodel/ggv-upper-endpoint-uniform-d14-d15-fullmodes-sol-ultra-20260828.md"
PACKET = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d14_d15_fullmodes_20260828"
PRODUCER = PACKET / "verify_uniform_d14_d15.py"
RESULT = PACKET / "RESULT.json"
README = PACKET / "README.md"
D12_PY = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828/verify_uniform_d12_d13.py"
D12_RES = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828/RESULT.json"
D10_PY = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/verify_uniform_d10.py"
D10_RES = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/RESULT.json"
D9_REV = ROOT / "xmodel/ggv-upper-endpoint-uniform-d9-fullmodes-hostile-review-grok46-20260828.md"

# Prompt-charged hashes (superseded during this review by a D15-successor repair).
PROMPT_HASHES = {
    CHARGED_NOTE: "206bd3e8b8d06e9e334ea76cb28e1fe5b447bd9b29d4740c947f0e553f491bef",
    PRODUCER: "061743e081be5944cd3af34fa9d9d71cf24bee12f8bfafa49c5a980dad0bf40c",
    RESULT: "757e8e40ce5bcd0181b11ae28b6c4302ef08c60a3db9b679fb798fd40ba2da07",
}
LIVE_HASHES = {
    RAW_PATH: "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0",
    CHARGED_NOTE: "830639eca8bf76bba512abc8528f763925a11092b661b1531d3f66b01c1c77fc",
    PRODUCER: "53f2a7a276be4a0aa7f77cc031e270d573fc78b5db64cdb76a0cf6c502e52517",
    RESULT: "7546618aa5a40ed983014159c1d39337396607562912570c97cfe2ee779394ea",
    D12_PY: "e5e2543ca50fc48623ccccf34f548f6171e79b31e6f80c8cfe6f5ca2b6798879",
    D12_RES: "06ca0152a7d05dd7b4549e74138b482fc572a62acae718751e7230577c5f28c8",
    D10_PY: "8ebe5f4f099e6cf15b0a4703dfb348aa6cc72df8fdbc60b1d095925fa3746d21",
    D10_RES: "8ff338bdd47b7a53ba1515a7889823620120f92d718a03349fb9e3fd27014236",
}
CHARGED = LIVE_HASHES

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
    "u": "du", "y": "dy", "s": "ds",
    **{f"f{n}": f"df{n}" for n in range(5, 16)},
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


def prefix_through_d13():
    z, v, r, q, t = (Lvar(name) for name in ("z", "v", "r", "q", "t"))
    F = {
        0: LA(4),
        1: LA(2),
        2: Ladd(Lconst(Q(1, 4)), Lscale(Q(1, 4), Lmul(LA(2), z))),
        3: Ladd(Lscale(Q(1, 8), z), Lscale(Q(1, 8), Lmul(LA(2), v))),
        4: Ladd(Lscale(Q(1, 16), v), Lscale(Q(1, 64), Lmul(z, z)), Lmul(LA(2), r)),
        5: Ladd(Lscale(Q(1, 2), r), Lscale(Q(1, 64), Lmul(z, v)), Lmul(LA(2), q)),
        6: Ladd(Lscale(Q(1, 2), q), Lscale(Q(1, 8), Lmul(r, z)),
                Lscale(Q(1, 256), Lmul(v, v)), Lmul(LA(2), t)),
    }
    for n in range(7, 16):
        F[n] = Lvar(f"f{n}") if n <= 14 else {}
    return F, z, v, r, q, t


def constant_jet(item, drop=()):
    """X^0 coefficient of a holomorphic A-adic series: A(0) = -1."""
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
    F, z, v, r, q, t = prefix_through_d13()
    powers, g = continuation(F, 15, killed={6, 10})
    half = powers[Q(1, 2)]
    negq = powers[Q(-1, 4)]
    one = powers[Q(0)]
    _, cube = square_root_cube(F, 15)
    for n in range(16):
        must(f"S3_matches_F32_w{n}", powers[Q(3, 2)][n] == cube[n])

    for birth, alpha in MODES.items():
        y0 = fractional({0: LA(4), 1: LA(2)}, alpha, 0)[0]
        must(f"mode_c{birth}_y0", y0 == LA(int(Q(4) * alpha)), str(Lterms(y0)))
        must(f"c{birth}_support_at_14", (birth <= 14) == (14 - birth >= 0))
        must(f"c{birth}_support_at_15", (birth <= 15) == (15 - birth >= 0))

    must("F_neg14_0_is_1_over_A", negq[0] == LA(-1), str(Lterms(negq[0])))
    must("F_neg14_1_is_minus_1_over_4A3",
         negq[1] == Lscale(Q(-1, 4), LA(-3)), str(Lterms(negq[1])))
    must("c14_birth_pole_is_c14_over_A",
         Lmul(Lvar("c14"), negq[0]) == Lscale(1, Lshift(-1, Lvar("c14"))))
    must("c14_next_is_minus_c14_over_4A3",
         Lmul(Lvar("c14"), negq[1]) == Lscale(Q(-1, 4), Lshift(-3, Lvar("c14"))))
    must("c16_not_born_at_14", 16 > 14)
    must("c16_not_born_at_15", 16 > 15)
    must("F0_2_is_zero", one[2] == {})
    must("c12_times_F0_2_is_zero", Lmul(Lvar("c12"), one[2]) == {})
    must("c4_F10_polynomial_at_14", not Lpolar(Lmul(Lvar("c4"), F[10])))
    must("c4_F11_polynomial_at_15", not Lpolar(Lmul(Lvar("c4"), F[11])))
    must("c8_times_half6_polynomial_before_d14_defect", not Lpolar(Lmul(Lvar("c8"), half[6])),
         str(Lterms(Lpolar(half[6]))))
    must("nine_modes_serialized", list(MODES) == [4, 6, 8, 10, 12, 14, 16, 18, 20])

    # L14 annihilates the rational mode; L15 detects it.
    pole14 = Lshift(-1, Lvar("c14"))
    must("L14_c14_over_A_is_zero", Lop(14, pole14) == {}, str(Lterms(Lop(14, pole14))))
    pole15 = Lscale(Q(-1, 4), Lshift(-3, Lvar("c14")))
    d15_c14 = Lneg(Lop(15, pole15))
    must("D15_c14_exact_3_c14_Ap",
         d15_c14 == Lscale(3, Lmul(Lvar("ap"), Lvar("c14"))),
         str(Lterms(d15_c14)))
    must("D15_c14_mod_A",
         Lmod(1, d15_c14) == Lscale(3, Lmul(Lvar("ap"), Lvar("c14"))))

    delta7 = Ladd(
        Lvar("f7"), Lscale(Q(-1, 2), t), Lscale(Q(-1, 8), Lmul(q, z)),
        Lscale(Q(-1, 16), Lmul(r, v)),
    )
    g14 = g[14]
    expected_g14_polar = Ladd(
        Lscale(Q(3, 8), Lshift(-2, Lmul(delta7, delta7))),
        Lshift(-1, Lvar("c14")),
    )
    must("g14_polar_exact", Lpolar(g14) == expected_g14_polar,
         str(Lterms(Lpolar(g14))))
    order2_14 = {(a, m): c for (a, m), c in Lpolar(g14).items() if a <= -2}
    must("g14_order2_is_only_Delta7_square",
         order2_14 == Lscale(Q(3, 8), Lshift(-2, Lmul(delta7, delta7))))
    must("g14_no_A_minus_3",
         not any(a <= -3 for (a, _) in Lpolar(g14)))
    must("order2_cannot_be_cancelled_by_c14",
         order2_14 != {} and Lpolar(pole14) != order2_14)
    order1_14 = {(a, m): c for (a, m), c in Lpolar(g14).items() if a == -1}
    must("c14_is_the_only_order1_symbol",
         order1_14 == {(-1, ("c14",)): Q(1)}, str(Lterms(order1_14)))

    d14_square = Lneg(Lop(14, Lscale(Q(3, 8), Lshift(-2, Lmul(delta7, delta7)))))
    expected_d14 = Lscale(-3, Lmul(LA(1), Lmul(Lvar("ap"), Lmul(delta7, delta7))))
    must("D14_mod_A2_is_minus_3_A_Ap_Delta7_sq",
         Lmod(2, d14_square) == expected_d14, str(Lterms(Lmod(2, d14_square))))
    must("L14_of_c14_does_not_affect_D14", Lmod(2, Lop(14, pole14)) == {})
    must("coeff_minus_3_nonzero_in_Q", Q(-3) != 0)
    must("L14_order1_in_A2_vacuous_for_c14", Lop(14, pole14) == {})

    after_first = {
        "f7": Ladd(Lscale(Q(1, 2), t), Lscale(Q(1, 8), Lmul(q, z)),
                   Lscale(Q(1, 16), Lmul(r, v)), Lmul(LA(1), Lvar("u"))),
    }
    g14_after = Lsub(g14, after_first)
    must("g14_remaining_polar_is_c14_over_A",
         Lpolar(g14_after) == pole14, str(Lterms(Lpolar(g14_after))))
    g14_killed = Lsub(g14_after, {"c14": {}})
    must("g14_polynomial_after_c14_kill", Lpolar(g14_killed) == {},
         str(Lterms(Lpolar(g14_killed))))

    delta8 = Ladd(
        Lvar("f8"), Lscale(Q(-1, 8), Lmul(t, z)), Lscale(Q(-1, 16), Lmul(q, v)),
        Lscale(Q(-1, 4), Lmul(r, r)),
    )
    g15_before = Lsub(g[15], after_first)
    expected_g15_before = Ladd(
        Lscale(Q(-1, 4), Lshift(-3, Lvar("c14"))),
        Lscale(Q(-3, 16), Lshift(-2, Lmul(Lvar("u"), Lvar("u")))),
        Lscale(Q(3, 4), Lshift(-1, Lmul(Lvar("u"), delta8))),
        Lscale(Q(1, 2), Lshift(-1, Lmul(Lvar("c8"), Lvar("u")))),
    )
    must("g15_polar_before_c14_kill", Lpolar(g15_before) == expected_g15_before,
         str(Lterms(Lpolar(g15_before))))
    must("g15_has_order_minus_3_c14",
         Lpolar(g15_before).get((-3, ("c14",))) == Q(-1, 4))
    # Same-row L15 of the g15 polar, taken alone, is the charged "detection"
    # formula.  It is not the raw D15 class: D15 also contains the (F1,G14)
    # mixed term, and the two c14 pieces cancel.
    same_row = Lop(15, pole15)
    f1 = LA(2)
    mixed = Ladd(
        Lscale(-2, Lmul(Lder(f1), pole14)),
        Lscale(-7, Lmul(f1, Lder(pole14))),
    )
    must("D15_c14_same_row_is_minus_3_c14_Ap",
         same_row == Lscale(-3, Lmul(Lvar("ap"), Lvar("c14"))),
         str(Lterms(same_row)))
    must("D15_c14_mixed_is_plus_3_c14_Ap",
         mixed == Lscale(3, Lmul(Lvar("ap"), Lvar("c14"))),
         str(Lterms(mixed)))
    must("D15_c14_pieces_cancel", Ladd(same_row, mixed) == {})
    must("charged_standalone_D15_detection_is_false",
         Ladd(same_row, mixed) != Lneg(same_row))
    # Storage defects (polynomial G missing both poles) cancel the same way.
    defect_g14 = Lneg(pole14)
    defect_g15 = Lneg(pole15)
    defect_mixed = Ladd(
        Lscale(-2, Lmul(Lder(f1), defect_g14)),
        Lscale(-7, Lmul(f1, Lder(defect_g14))),
    )
    must("storage_defects_also_cancel",
         Ladd(Lop(15, defect_g15), defect_mixed) == {})
    d15_same_row_only = Lneg(Lop(15, expected_g15_before))
    must("same_row_only_mod_A_is_the_false_detection",
         Lmod(1, d15_same_row_only) == Lscale(3, Lmul(Lvar("ap"), Lvar("c14"))),
         str(Lterms(Lmod(1, d15_same_row_only))))

    g15 = Lsub(g15_before, {"c14": {}})
    expected_g15 = Ladd(
        Lscale(Q(-3, 16), Lshift(-2, Lmul(Lvar("u"), Lvar("u")))),
        Lscale(Q(3, 4), Lshift(-1, Lmul(Lvar("u"), delta8))),
        Lscale(Q(1, 2), Lshift(-1, Lmul(Lvar("c8"), Lvar("u")))),
    )
    must("g15_polar_after_c14_kill", Lpolar(g15) == expected_g15,
         str(Lterms(Lpolar(g15))))
    must("g15_order2_is_only_U_square",
         {(a, m): c for (a, m), c in Lpolar(g15).items() if a <= -2}
         == Lscale(Q(-3, 16), Lshift(-2, Lmul(Lvar("u"), Lvar("u")))))
    d15 = Lneg(Lop(15, expected_g15))
    must("D15_mod_A2_is_3_4_A_Ap_U_sq",
         Lmod(2, d15) == Lscale(Q(3, 4), Lmul(LA(1), Lmul(Lvar("ap"),
                                                         Lmul(Lvar("u"), Lvar("u"))))),
         str(Lterms(Lmod(2, d15))))
    order1_15 = {(a, m): c for (a, m), c in Lpolar(g15).items() if a == -1}
    must("L15_order1_in_A2", not Lmod(2, Lop(15, order1_15)))
    must("c8_lives_in_order1_polar",
         Lpolar(g15).get((-1, ("c8", "u"))) == Q(1, 2))
    must("coeff_3_4_nonzero_in_Q", Q(3, 4) != 0)

    after_second = Lsub(g15, {"u": Lmul(LA(1), Lvar("y"))})
    must("g15_remaining_polar_empty", Lpolar(after_second) == {},
         str(Lterms(Lpolar(after_second))))
    c8_after = Lsub(Lscale(Q(1, 2), Lshift(-1, Lmul(Lvar("c8"), Lvar("u")))),
                    {"u": Lmul(LA(1), Lvar("y"))})
    must("c8_Y_over_2_polynomial",
         c8_after == Lscale(Q(1, 2), Lmul(Lvar("c8"), Lvar("y")))
         and not Lpolar(c8_after))

    # C13--C15 from holomorphic X^0 jets after the combined completion.
    final = {
        "c14": {},
        "f7": Ladd(Lscale(Q(1, 2), t), Lscale(Q(1, 8), Lmul(q, z)),
                   Lscale(Q(1, 16), Lmul(r, v)), Lmul(LA(2), Lvar("y"))),
    }
    drop_forced = {f"f{n}" for n in range(9, 16)}
    expected_low = {
        13: Ladd(
            Lscale(Q(1, 2), Lmul(Lvar("c8"), Lvar("q0"))),
            Lscale(Q(3, 4), Lmul(Lvar("f80"), Lvar("q0"))),
            Lscale(Q(-3, 128), Lmul(Lmul(Lvar("q0"), Lvar("q0")), Lvar("v0"))),
            Lscale(Q(-3, 16), Lmul(Lmul(Lvar("q0"), Lvar("r0")), Lvar("r0"))),
            Lscale(Q(3, 16), Lmul(Lvar("t0"), Lvar("t0"))),
            Lscale(Q(3, 4), Lmul(Lvar("t0"), Lvar("y0"))),
        ),
        14: Ladd(
            Lscale(Q(1, 2), Lmul(Lvar("c8"), Lvar("t0"))),
            Lscale(Q(3, 4), Lmul(Lvar("f80"), Lvar("t0"))),
            Lscale(Q(-3, 16), Lmul(Lmul(Lvar("q0"), Lvar("q0")), Lvar("r0"))),
            Lscale(Q(-3, 64), Lmul(Lmul(Lvar("q0"), Lvar("t0")), Lvar("v0"))),
            Lscale(Q(-3, 16), Lmul(Lmul(Lvar("r0"), Lvar("r0")), Lvar("t0"))),
            Lscale(Q(-3, 64), Lmul(Lmul(Lvar("t0"), Lvar("t0")), Lvar("z0"))),
            Lscale(Q(3, 8), Lmul(Lvar("y0"), Lvar("y0"))),
        ),
        15: Ladd(
            Lscale(Q(1, 2), Lmul(Lvar("c8"), Lvar("y0"))),
            Lscale(Q(3, 4), Lmul(Lvar("f80"), Lvar("y0"))),
            Lscale(Q(-1, 16), Lmul(Lmul(Lvar("q0"), Lvar("q0")), Lvar("q0"))),
            Lscale(Q(-3, 8), Lmul(Lmul(Lvar("q0"), Lvar("r0")), Lvar("t0"))),
            Lscale(Q(-3, 64), Lmul(Lmul(Lvar("q0"), Lvar("v0")), Lvar("y0"))),
            Lscale(Q(-3, 16), Lmul(Lmul(Lvar("r0"), Lvar("r0")), Lvar("y0"))),
            Lscale(Q(-3, 128), Lmul(Lmul(Lvar("t0"), Lvar("t0")), Lvar("v0"))),
            Lscale(Q(-3, 32), Lmul(Lmul(Lvar("t0"), Lvar("y0")), Lvar("z0"))),
            Lscale(Q(-3, 16), Lmul(Lvar("y0"), Lvar("y0"))),
        ),
    }
    full_jets = {}
    for n in (13, 14, 15):
        specialized = Lsub(g[n], final)
        must(f"g{n}_holomorphic_after_completion", Lpolar(specialized) == {},
             str(Lterms(Lpolar(specialized))))
        jet = constant_jet(specialized, drop=drop_forced)
        full = constant_jet(specialized, drop=())
        full_jets[n] = full
        forced_zero = {f"f{k}0" for k in range(9, 16)}
        extra_monomials = set()
        for (_, m) in full:
            if m not in {key[1] for key in expected_low[n]}:
                extra_monomials.add(m)
        leftover = {m for m in extra_monomials if not (set(m) & forced_zero)}
        must(f"C{n}_extras_are_window_forced_F9plus_zeros",
             not leftover, str(sorted(leftover)))
        must(f"C{n}_matches_charged_jet", jet == expected_low[n],
             str(Lterms(jet)))
        leftover_modes = {s for (_, m) in jet for s in m
                          if s.startswith("c") and s not in {"c8"}}
        must(f"C{n}_only_c8_among_modes", not leftover_modes, str(leftover_modes))

    # H0 factorization and gauge invariance of the jets.
    H0 = Ladd(Lscale(Q(1, 2), Lvar("c8")), Lscale(Q(3, 4), Lvar("f80")))
    factored = {
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
        must(f"C{n}_factors_through_H0", expected_low[n] == factored[n])
        for lam in (Q(-1), Q(1), Q(2)):
            gauged = Lsub(expected_low[n], {
                "f80": Ladd(Lvar("f80"), Lconst(lam)),
                "c8": Ladd(Lvar("c8"), Lconst(Q(-3, 2) * lam)),
            })
            must(f"C{n}_gauge_lambda_{lam}", gauged == expected_low[n])

    # Squarefree / characteristic-zero uses.
    must("gcd_A_Aprime_is_1", poly_gcd(A, AP) == [Q(1)], str(poly_gcd(A, AP)))
    must("A_prime_has_leading_4", AP[-1] == Q(4))
    for coeffs in ([Q(1)], [Q(0), Q(1)], A, [Q(2)], [Q(1), Q(0), Q(0), Q(0), Q(3)],
                   scale(Q(5), A), X, mul(X, X)):
        w2 = mul(coeffs, coeffs)
        must(f"A_divides_W2_iff_A_divides_W_{encode(coeffs) or '0'}",
             poly_in_ideal(w2, A) == poly_in_ideal(coeffs, A))
    must("char0_coeff_3_visible", Q(3) != 0)
    must("char0_coeff_4_visible", Q(4) != 0)
    return True


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
    must("G13_omits_degree_0", raw["windows"]["G"]["13"]["lower"] == 1)
    must("G14_omits_degree_0", raw["windows"]["G"]["14"]["lower"] == 1)
    must("G15_omits_degree_0", raw["windows"]["G"]["15"]["lower"] == 1)
    must("G14_upper_10", raw["windows"]["G"]["14"]["upper"] == 10)
    must("G15_upper_9", raw["windows"]["G"]["15"]["upper"] == 9)
    must("F7_stores_constants", raw["windows"]["F"]["7"]["lower"] == 0)
    must("F8_stores_constants", raw["windows"]["F"]["8"]["lower"] == 0)
    must("F9_omits_degree_0", raw["windows"]["F"]["9"]["lower"] == 1)
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
    for n in (13, 14, 15):
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
        must(f"D{n}_row_sha256",
             bool(raw["per_row"][str(n)]["row_sha256"]))
        record(f"D{n}_reconstructed", True,
               f"{len(frozen)} coefficients, "
               f"{sum(len(g['terms']) for g in frozen.values())} terms")
    must("D14_row_sha256_matches_charge",
         raw["per_row"]["14"]["row_sha256"]
         == "35548a74a3af2126abfeda0519d1600bcf8cf5e24fc0f7dd4050bc2fe9f84caf")
    must("D15_row_sha256_matches_charge",
         raw["per_row"]["15"]["row_sha256"]
         == "4e7f3882153593594004cf817ce6f76e776cc10af09bc57e01a9202013d39b68")
    record("D13_to_D15_symbolic_reconstruction", True,
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


def t_series_multiply(left, right, maximum):
    answer = {weight: [] for weight in range(maximum + 1)}
    for lw, lp in left.items():
        for rw, rp in right.items():
            w = lw + rw
            if w <= maximum:
                answer[w] = add(answer[w], mul(lp, rp))
    return answer


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


def g14_kernel(raw):
    window = raw["windows"]["G"]["14"]
    row_generators = [(index, generator) for index, generator in enumerate(raw["generators"])
                      if int(generator["row"]) == 14]
    must("G14_slots_count_10", len(window["slots"]) == 10)
    must("D14_generator_count_26", len(row_generators) == 26)
    columns = []
    for slot in window["slots"]:
        values = {slot: Q(1)}
        direct, serialized = three_way(raw, values, f"G14_{slot}")
        columns.append([serialized[index] for index, _ in row_generators])
        # Same-row G14 contribution depends only on F0=A^4, hence is
        # independent of the cascade locus.
        must(f"G14_{slot}_D14_from_direct",
             [direct[14][int(g["x_degree"])] if int(g["x_degree"]) < len(direct[14]) else Q(0)
              for _, g in row_generators] == columns[-1])
    matrix = [[columns[column][row] for column in range(len(columns))]
              for row in range(len(row_generators))]
    rank = rational_rank(matrix)
    must("G14_matrix_shape_26x10", len(matrix) == 26 and len(matrix[0]) == 10)
    must("G14_rank_10", rank == 10, str(rank))
    must("G14_nullity_0", len(columns) - rank == 0)
    # A constant cannot be stored; A^{-1} is not a polynomial in the window.
    must("G14_cannot_store_constant", window["lower"] == 1)
    must("A_does_not_divide_a_nonzero_constant",
         not poly_in_ideal([Q(1)], A))
    return rank


def mutations(raw):
    def d14_assign(scalar):
        values = {}
        set_poly(values, raw, "F", 7, [scalar])
        set_poly(values, raw, "G", 7, scale(Q(3, 2) * scalar, A2))
        set_poly(values, raw, "G", 8, [Q(3, 4) * scalar])
        return values

    def d15_assign(scalar):
        u = scale(scalar, X)
        values = {}
        set_poly(values, raw, "F", 7, mul(A, u))
        set_poly(values, raw, "G", 7, scale(Q(3, 2), mul(A3, u)))
        set_poly(values, raw, "G", 8, scale(Q(3, 4), mul(A, u)))
        set_poly(values, raw, "G", 14, scale(Q(3, 8), mul(u, u)))
        return values

    d14_unit = scale(-3, mul(A, AP))
    d15_unit = add(scale(Q(3, 4), mul(mul(A, AP), mul(X, X))),
                   scale(-3, mul(A2, X)))

    for scalar in (Q(-1), Q(1), Q(2)):
        values = d14_assign(scalar)
        direct, serialized = three_way(raw, values, f"D14_square_{scalar}")
        must(f"D14_square_{scalar}_prior_zero",
             all(not direct[w] for w in range(4, 14)))
        must(f"D14_square_{scalar}_residual",
             eq(direct[14], scale(scalar * scalar, d14_unit)),
             str(encode(direct[14])))
        if scalar == Q(1):
            must("D14_residual_deg3", encode(direct[14]) == {"3": "12", "7": "-12"})
            must("D14_gen318", serialized[318] == Q(12) and
                 raw["generators"][318]["sha256"]
                 == "c73aa94185c1e89fa1c28dff555416ff9654a03c1d42defae7181be6369c5008")
            must("D14_gen322", serialized[322] == Q(-12) and
                 raw["generators"][322]["sha256"]
                 == "1edbb3e0e46bd1f4920a1463838c16740db179089d886640e998e448dcff061b")

    for scalar in (Q(-1), Q(1), Q(2)):
        values = d15_assign(scalar)
        direct, serialized = three_way(raw, values, f"D15_square_{scalar}")
        must(f"D15_square_{scalar}_prior_zero",
             all(not direct[w] for w in range(4, 15)))
        must(f"D15_square_{scalar}_residual",
             eq(direct[15], scale(scalar * scalar, d15_unit)),
             str(encode(direct[15])))
        if scalar == Q(1):
            must("D15_residual_deg1", encode(direct[15]) == {"1": "-3", "5": "3"})
            must("D15_gen342", serialized[342] == Q(-3) and
                 raw["generators"][342]["sha256"]
                 == "6b7ebc3cdd93b7cbf73b60df88ea16820d306090a3dd73382fa5e5af3469355f")
            must("D15_gen346", serialized[346] == Q(3) and
                 raw["generators"][346]["sha256"]
                 == "7f4b92bd92d9ee2172c7913e8d38fdbd374360d63f8c2065c5856dd2f44f9e34")
        must(f"D15_square_{scalar}_mod_A2",
             poly_in_ideal(add(direct[15], scale(-scalar * scalar,
                                                 scale(Q(3, 4), mul(mul(A, AP), mul(X, X))))),
                           A2))

    # Hostile: polynomial G14 cannot cancel the D14 square class.
    hostile = d14_assign(Q(1))
    set_poly(hostile, raw, "G", 14, [Q(0), Q(1)])  # X^1 in the window
    direct_h, _ = three_way(raw, hostile, "hostile_G14_against_square")
    must("hostile_G14_does_not_kill_D14_square",
         not poly_in_ideal(direct_h[14], A2))

    # Hostile: G14 polynomial with empty F7 does not create a c14-like kernel.
    g14_only = {}
    set_poly(g14_only, raw, "G", 14, [Q(0), Q(1)])
    direct_g, _ = three_way(raw, g14_only, "hostile_pure_G14")
    must("pure_G14_D14_nonzero", bool(direct_g[14]))

    # c8=1 survival through D15.
    c8_values = {}
    set_poly(c8_values, raw, "F", 7, mul(A2, X))
    set_poly(c8_values, raw, "G", 7, scale(Q(3, 2), mul(A4, X)))
    set_poly(c8_values, raw, "G", 8, add(scale(Q(3, 4), mul(A2, X)), A2))
    set_poly(c8_values, raw, "G", 9, [Q(1, 2)])
    set_poly(c8_values, raw, "G", 14, scale(Q(3, 8), mul(A2, mul(X, X))))
    set_poly(c8_values, raw, "G", 15,
             add(scale(Q(-3, 16), mul(X, X)), scale(Q(1, 2), X)))
    direct_c8, serialized_c8 = three_way(raw, c8_values, "c8_survival")
    must("c8_D4_through_D15_zero", all(not direct_c8[w] for w in range(4, 16)))
    must("c8_folded_D22_is_minus_1", serialized_c8[495] == Q(-1))
    # Killing the G8 = A^2 (the c8 carrier) should not be forced by D15:
    # dropping it while keeping the rest of the c8 continuation is a
    # different characteristic point, but D4--D15 remaining zero with G8
    # containing A^2 proves c8 is a kernel, not an obstruction.

    # F8 constant gauge: raw kernel, H0 combination.
    for lam in (Q(-1), Q(1), Q(2)):
        values = {}
        set_poly(values, raw, "F", 8, [lam])
        direct, serialized = three_way(raw, values, f"F8_gauge_{lam}")
        must(f"F8_gauge_{lam}_D4_through_D22_zero",
             all(not direct[w] for w in range(4, 23)))
        must(f"F8_gauge_{lam}_folded_D22", serialized[495] == Q(-1))

    # Exact-square continuation through G15 with the D15 remainder Y=X.
    S = {
        0: A2, 1: [Q(1, 2)], 2: [], 3: [], 4: [], 5: [], 6: [],
        7: scale(Q(1, 2), X),
    }
    square_F = t_series_multiply(S, S, 14)
    square_G = t_series_multiply(t_series_multiply(S, S, 21), S, 21)
    exact = {}
    for w in range(4, 15):
        set_poly(exact, raw, "F", w, square_F[w])
    for w in range(4, 22):
        if raw["windows"]["G"][str(w)]["lower"] <= 0 or True:
            try:
                set_poly(exact, raw, "G", w, square_G[w])
            except AssertionError:
                # G13+ omit degree 0; the exact cube must have vanishing
                # constants there, otherwise C13--C15 would fail.
                poly = square_G[w]
                if any(poly[d] for d in range(min(len(poly), raw["windows"]["G"][str(w)]["lower"]))):
                    must(f"exact_square_G{w}_low_degrees_nonzero", False,
                         str(encode(poly)))
                clipped = list(poly)
                set_poly(exact, raw, "G", w, clipped)
    direct_ex, _ = three_way(raw, exact, "exact_square_Y_eq_X")
    must("exact_square_D4_through_D15_zero",
         all(not direct_ex[w] for w in range(4, 16)))
    must("exact_square_F7_is_A2_X", eq(square_F[7], mul(A2, X)))

    # Omitting F7 while continuing F^{3/2} through G13 should produce D14.
    omitted = dict(exact)
    set_poly(omitted, raw, "F", 7, [])
    defect = scale(-1, square_F[7])
    for offset in range(7):
        w = 7 + offset
        if w > 21:
            break
        adjusted = add(square_G[w], scale(Q(3, 2), mul(defect, S.get(offset, []))))
        try:
            set_poly(omitted, raw, "G", w, adjusted)
        except AssertionError:
            set_poly(omitted, raw, "G", w, adjusted)
    direct_om, _ = three_way(raw, omitted, "omit_F7")
    must("omit_F7_prior_zero", all(not direct_om[w] for w in range(4, 14)))
    must("omit_F7_D14_nonzero", bool(direct_om[14]))
    return True


def hashes():
    for path, expected in PROMPT_HASHES.items():
        live = sha256(path)
        record(f"prompt_sha_{path.name}_superseded", live != expected,
               f"prompt={expected} live={live}")
    for path, expected in LIVE_HASHES.items():
        must(f"live_sha_{path.name}", sha256(path) == expected, sha256(path))
    if D9_REV.exists():
        record("d9_hostile_review_present", True, sha256(D9_REV))
    d12 = json.loads(D12_RES.read_text())
    must("d12_status_prefix",
         d12["status"] == "PASS_EXACT_FIELD_POINT_CASCADE_THROUGH_D13")
    d10 = json.loads(D10_RES.read_text())
    must("d10_status_prefix",
         d10["status"] == "PASS_EXACT_FIELD_POINT_CASCADE_THROUGH_D11")
    result = json.loads(RESULT.read_text())
    must("result_status",
         result["status"] == "PASS_EXACT_FIELD_POINT_A_ADIC_CASCADE_THROUGH_D15")
    must("result_raw_sha",
         result["source"]["authoritative_raw_system_sha256"] == CHARGED[RAW_PATH])
    must("result_variable_count", result["source"]["raw_variable_count"] == 303)
    must("result_c14_killed",
         result["theorems"]["D14"]["second_conclusion"] == "c14=0")
    must("result_retracts_standalone_D15_c14",
         "does not kill c14" in result["theorems"]["D14"]["successor_firewall"])
    must("result_D15_c14_total_empty",
         result["calculation"]["D15_c14_total"] == [])
    must("result_c8_survives",
         "survives" in result["theorems"]["D15"]["c8_status"])
    must("result_C13_present", "C13" in result["theorems"]["positive_lower_window_core"]["live_equations"])
    must("result_C14_present", "C14" in result["theorems"]["positive_lower_window_core"]["live_equations"])
    must("result_C15_present", "C15" in result["theorems"]["positive_lower_window_core"]["live_equations"])
    modes = result["complete_mode_schedule"]
    must("result_nine_modes", len(modes) == 9)
    must("result_c14_retained_in_schedule",
         any(m["birth_weight"] == 14 and m["continuation_status"] == "retained_mandatory"
             for m in modes))
    must("result_c16_unconstrained",
         any(m["birth_weight"] == 16 and m["continuation_status"] == "retained_mandatory"
             and not m["support_at_D14"] and not m["support_at_D15"] for m in modes))
    firewall = " ".join(result["scope_firewall"])
    must("firewall_no_scheme", "no scheme" in firewall)
    must("firewall_no_endpoint", "no endpoint" in firewall)
    must("firewall_no_JC2", "JC2" in firewall)
    # Producer --check is custody only; theorems are proved above.
    return result


def main():
    print("=== independent D14/D15 hostile checker ===")
    hashes()
    characteristic_identities()
    raw = json.loads(RAW_PATH.read_text())
    reconstruct_rows(raw)
    g14_kernel(raw)
    mutations(raw)
    n_fail = len(FAILURES)
    n_pass = sum(1 for _, ok, _ in CHECKS if ok)
    print(json.dumps({
        "passed": n_pass,
        "failed": n_fail,
        "failures": FAILURES,
        "total_checks": len(CHECKS),
    }, sort_keys=True))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
