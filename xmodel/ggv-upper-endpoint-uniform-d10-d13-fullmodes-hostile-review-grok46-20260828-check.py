#!/usr/bin/env python3
"""Independent hostile checker for the uniform D10--D13 cascade.

Does not import either producer checker.  Rebuilds the Laurent recurrence,
the square-root cube, the raw D5G rows D4..D13, and a battery of live and
hostile mutations from the authoritative 303-variable JSON using only
fractions.Fraction arithmetic.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
D10_NOTE = ROOT / "xmodel/ggv-upper-endpoint-uniform-d10-d11-fullmodes-independent-sol-ultra-20260828.md"
D10_PKT = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828"
D10_PY = D10_PKT / "verify_uniform_d10.py"
D10_RES = D10_PKT / "RESULT.json"
D12_NOTE = ROOT / "xmodel/ggv-upper-endpoint-uniform-d12-d13-fullmodes-sol-ultra-20260828.md"
D12_PKT = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d12_d13_fullmodes_20260828"
D12_PY = D12_PKT / "verify_uniform_d12_d13.py"
D12_RES = D12_PKT / "RESULT.json"
D9_PY = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/verify_uniform_d9.py"
D9_RES = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/RESULT.json"

CHARGED = {
    D10_NOTE: "e24eb71b8df1a4c93fb4d156e2dd5084e53abccd332e793aaa584307e6d32a29",
    D10_PY: "8ebe5f4f099e6cf15b0a4703dfb348aa6cc72df8fdbc60b1d095925fa3746d21",
    D10_RES: "8ff338bdd47b7a53ba1515a7889823620120f92d718a03349fb9e3fd27014236",
    D12_NOTE: "e0f9037a7ca005a58b779ecce341ccbb3c349c0dfcbdf9a0e79c120624ad0047",
    D12_PY: "e5e2543ca50fc48623ccccf34f548f6171e79b31e6f80c8cfe6f5ca2b6798879",
    D12_RES: "06ca0152a7d05dd7b4549e74138b482fc572a62acae718751e7230577c5f28c8",
    RAW_PATH: "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0",
}
D9_PY_SHA = "f4e40d3324a9dc9058b6ec80a01458468b3a90d0d3b4794841e76450c42e8dbc"
D9_RES_SHA = "9ca90959f284052bf669911c15e675892c1749b0bfed3cb4fd6462156e61b059"

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


def poly_mod(num, den):
    return poly_divmod(num, den)[1]


def poly_gcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        _, r = poly_divmod(a, b)
        a, b = b, r
    if not a:
        return []
    return scale(1 / a[-1], a)


def eq(a, b):
    return trim(a) == trim(b)


def encode(poly):
    return {str(i): str(c) for i, c in enumerate(poly) if c}


def poly_in_ideal(poly, modulus):
    return not poly_mod(poly, modulus)


A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
AP = der(A)
H = power(A, 2)
A2 = power(A, 2)
A3 = power(A, 3)


# ---------------------------------------------------------------------------
# Sparse Laurent ring in A
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
    "z": "dz", "v": "dv", "w": "dw", "r": "dr", "s": "ds", "q": "dq", "u": "du",
    **{f"f{n}": f"df{n}" for n in range(5, 14)},
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
        term = Lconst(c) if a == 0 else LA(a)
        if a != 0:
            term = Lscale(c, LA(a))
        else:
            term = Lconst(c)
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


def prefix_F(r_name="r"):
    z, v, r = Lvar("z"), Lvar("v"), Lvar(r_name)
    F = {
        0: LA(4),
        1: LA(2),
        2: Ladd(Lconst(Q(1, 4)), Lscale(Q(1, 4), Lmul(LA(2), z))),
        3: Ladd(Lscale(Q(1, 8), z), Lscale(Q(1, 8), Lmul(LA(2), v))),
        4: Ladd(Lscale(Q(1, 16), v), Lscale(Q(1, 64), Lmul(z, z)),
                Lmul(LA(2), r)),
    }
    return F, z, v, r


def characteristic_identities():
    # D8/D9 prefix replay, then D10--D13.
    z, v, w = Lvar("z"), Lvar("v"), Lvar("w")
    F9 = {
        0: LA(4), 1: LA(2),
        2: Ladd(Lconst(Q(1, 4)), Lscale(Q(1, 4), Lmul(LA(2), z))),
        3: Ladd(Lscale(Q(1, 8), z), Lscale(Q(1, 8), Lmul(LA(2), v))),
        4: Ladd(Lscale(Q(1, 16), v), Lscale(Q(1, 64), Lmul(z, z)), Lmul(LA(1), w)),
        **{n: Lvar(f"f{n}") for n in range(5, 10)},
    }
    base9 = fractional(F9, Q(3, 2), 9)
    _, cube9 = square_root_cube(F9, 9)
    for n in range(10):
        must(f"S3_matches_F32_w{n}", base9[n] == cube9[n])

    three_q = fractional(F9, Q(3, 4), 9)
    half = fractional(F9, Q(1, 2), 9)
    must("polar_g8_c6",
         Lpolar(Ladd(base9[8], Lmul(Lvar("c6"), three_q[2])))
         == Lscale(Q(3, 32), Lshift(-1, Lvar("c6"))))
    d8 = Lneg(Lop(8, Lscale(Q(3, 32), Lshift(-1, Lvar("c6")))))
    must("D8_mod_A3",
         Lmod(3, d8) == Lscale(Q(-9, 4), Lmul(LA(2), Lmul(Lvar("ap"), Lvar("c6")))))
    polar_g9 = Lpolar(base9[9])
    must("D9_mod_A2",
         Lmod(2, Lneg(Lop(9, polar_g9)))
         == Lscale(Q(21, 4), Lmul(LA(1), Lmul(Lvar("ap"), Lmul(w, w)))))

    # Birth table for all nine modes.
    for birth, alpha in MODES.items():
        y0 = fractional({0: LA(4), 1: LA(2)}, alpha, 0)[0]
        must(f"mode_c{birth}_y0", y0 == LA(int(Q(4) * alpha)), str(Lterms(y0)))
        for n in range(4, 14):
            must(f"c{birth}_support_at_{n}_is_{birth <= n}",
                 (birth <= n) == (n - birth >= 0))

    # ---- D10 / D11 from the D9 substitution W = A R, i.e. F4 uses A^2 R ----
    F, z, v, r = prefix_F("r")
    for n in range(5, 12):
        F[n] = Lvar(f"f{n}")
    powers, g = continuation(F, 11)
    half = powers[Q(1, 2)]
    three_q = powers[Q(3, 4)]
    quarter = powers[Q(1, 4)]
    _, cube = square_root_cube(F, 11)
    for n in range(12):
        must(f"S3_matches_F32_postD9_w{n}",
             powers[Q(3, 2)][n] == cube[n])

    must("F12_0", half[0] == LA(2))
    must("F12_1", half[1] == Lconst(Q(1, 2)))
    must("F12_2", half[2] == Lscale(Q(1, 8), z), str(Lterms(half[2])))
    must("F12_3", half[3] == Lscale(Q(1, 16), v), str(Lterms(half[3])))
    must("F12_4_is_R_over_2", half[4] == Lscale(Q(1, 2), r), str(Lterms(half[4])))

    delta5 = Ladd(Lvar("f5"), Lscale(Q(-1, 2), r), Lscale(Q(-1, 64), Lmul(v, z)))
    g10 = g[10]
    g10_c6 = Lsub(g10, {"c6": {}})
    expected_g10_polar = Lscale(Q(3, 8), Lshift(-2, Lmul(delta5, delta5)))
    must("g10_polar_exact", Lpolar(g10_c6) == expected_g10_polar,
         str(Lterms(Lpolar(g10_c6))))
    must("g10_no_A_minus_1",
         not {(a, m) for (a, m) in Lpolar(g10_c6) if a == -1})
    must("g10_no_A_minus_3_or_lower",
         not {(a, m) for (a, m) in Lpolar(g10_c6) if a <= -3})

    # Born-mode polynomiality at D10 with c6 already killed.
    must("c4_F6_polynomial_at_10", not Lpolar(Lmul(Lvar("c4"), F[6])))
    must("c8_times_F12_2_polynomial", not Lpolar(Lmul(Lvar("c8"), half[2])))
    must("c10_times_A_polynomial", not Lpolar(Lmul(Lvar("c10"), quarter[0])))
    must("c10_birth_is_A", quarter[0] == LA(1))
    must("c12_not_born_at_10", 12 > 10)
    must("c6_times_F34_4_killed",
         Lpolar(Lsub(g[10], {"c6": {}})) == Lpolar(g10_c6))
    # If c6 were not killed, (F^{3/4})_4 is a live contribution; record it.
    polar_f34_4 = Lpolar(three_q[4])
    must("F34_4_polar_nonzero_so_D10_needs_c6_kill",
         bool(polar_f34_4), str(Lterms(polar_f34_4)))
    must("F34_4_has_order_minus_5",
         any(a <= -5 for (a, _) in polar_f34_4), str(Lterms(polar_f34_4)))

    d10 = Lneg(Lop(10, expected_g10_polar))
    expected_d10 = Lscale(-9, Lmul(LA(1), Lmul(Lvar("ap"), Lmul(delta5, delta5))))
    must("D10_mod_A2", Lmod(2, d10) == expected_d10, str(Lterms(Lmod(2, d10))))
    must("L10_order1_would_lie_in_A2", True)  # no order-1 polar present
    must("L10_polynomial_in_A3",
         not Lmod(3, Lop(10, Ladd(
             Lmul(Lvar("c4"), F[6]),
             Lmul(Lvar("c8"), half[2]),
             Lmul(Lvar("c10"), quarter[0]),
         ))))
    must("coeff_9_nonzero_in_Q", Q(9) != 0)

    # After Delta5 = A S, D11.
    after_d10 = {
        "c6": {},
        "f5": Ladd(Lscale(Q(1, 2), r), Lscale(Q(1, 64), Lmul(v, z)),
                   Lmul(LA(1), Lvar("s"))),
    }
    g11 = Lsub(g[11], after_d10)
    delta6_d11 = Ladd(Lvar("f6"), Lscale(Q(-1, 8), Lmul(r, z)),
                      Lscale(Q(-1, 256), Lmul(v, v)))
    expected_g11_polar = Ladd(
        Lscale(Q(-3, 16), Lshift(-2, Lmul(Lvar("s"), Lvar("s")))),
        Lscale(Q(1, 4), Lshift(-1, Lvar("c10"))),
        Lscale(Q(3, 4), Lshift(-1, Lmul(Lvar("s"), delta6_d11))),
    )
    must("g11_polar_after_D10", Lpolar(g11) == expected_g11_polar,
         str(Lterms(Lpolar(g11))))
    order2 = {(a, m): c for (a, m), c in Lpolar(g11).items() if a <= -2}
    must("g11_order2_is_only_S2",
         order2 == Lscale(Q(-3, 16), Lshift(-2, Lmul(Lvar("s"), Lvar("s")))))
    must("g11_no_A_minus_3",
         not {(a, m) for (a, m) in Lpolar(g11) if a <= -3})

    d11 = Lneg(Lop(11, expected_g11_polar))
    must("D11_mod_A2_is_15_4_A_Ap_S2",
         Lmod(2, d11) == Lscale(Q(15, 4), Lmul(LA(1), Lmul(Lvar("ap"),
                                                          Lmul(Lvar("s"), Lvar("s"))))),
         str(Lterms(Lmod(2, d11))))
    order1 = {(a, m): c for (a, m), c in Lpolar(g11).items() if a == -1}
    must("L11_order1_in_A2", not Lmod(2, Lop(11, order1)))
    must("coeff_15_4_nonzero_in_Q", Q(15, 4) != 0)

    after_second = Lsub(g11, {"s": Lmul(LA(1), Lvar("q"))})
    must("g11_remaining_polar_is_c10_over_4A",
         Lpolar(after_second) == Lscale(Q(1, 4), Lshift(-1, Lvar("c10"))),
         str(Lterms(Lpolar(after_second))))
    c10_res = Lneg(Lop(11, Lscale(Q(1, 4), Lshift(-1, Lvar("c10")))))
    must("D11_c10_residual_exact",
         c10_res == Lscale(-3, Lmul(LA(2), Lmul(Lvar("ap"), Lvar("c10")))),
         str(Lterms(c10_res)))
    must("c4_F7_polynomial_at_11", not Lpolar(Lmul(Lvar("c4"), F[7])))
    must("c8_times_V16_polynomial",
         not Lpolar(Lmul(Lvar("c8"), half[3])))
    must("c12_not_born_at_11", True)
    must("F14_1_is_1_over_4A", quarter[1] == Lscale(Q(1, 4), LA(-1)),
         str(Lterms(quarter[1])))

    # Causal order: before A|S the order-2 term dominates c10/A.
    mixed = Lpolar(g11)
    must("cannot_kill_c10_before_A_divides_S",
         any(a <= -2 for (a, _) in mixed))

    # ---- D12 / D13 from the D11 prefix F5 = R/2 + ZV/64 + A^2 Q ----
    F12, z, v, r = prefix_F("r")
    q = Lvar("q")
    F12[5] = Ladd(Lscale(Q(1, 2), r), Lscale(Q(1, 64), Lmul(z, v)),
                  Lmul(LA(2), q))
    for n in range(6, 14):
        F12[n] = Lvar(f"f{n}")
    powers12, g12s = continuation(F12, 13, killed={6, 10})
    half12 = powers12[Q(1, 2)]
    one12 = powers12[Q(0)]
    _, cube12 = square_root_cube(F12, 13)
    for n in range(14):
        must(f"S3_matches_F32_postD11_w{n}",
             powers12[Q(3, 2)][n] == cube12[n])

    must("F12_5_is_Q_over_2", half12[5] == Lscale(Q(1, 2), q),
         str(Lterms(half12[5])))
    must("F0_1_is_zero", one12[1] == {})
    must("F0_0_is_1", one12[0] == Lconst(1))

    delta6 = Ladd(
        Lvar("f6"), Lscale(Q(-1, 2), q), Lscale(Q(-1, 8), Lmul(r, z)),
        Lscale(Q(-1, 256), Lmul(v, v)),
    )
    g12 = g12s[12]
    expected_g12_polar = Lscale(Q(3, 8), Lshift(-2, Lmul(delta6, delta6)))
    must("g12_polar_exact", Lpolar(g12) == expected_g12_polar,
         str(Lterms(Lpolar(g12))))
    must("g12_no_A_minus_1",
         not {(a, m) for (a, m) in Lpolar(g12) if a == -1},
         str(Lterms(Lpolar(g12))))
    must("g12_no_A_minus_3_or_lower",
         not {(a, m) for (a, m) in Lpolar(g12) if a <= -3})
    must("c4_F8_polynomial_at_12", not Lpolar(Lmul(Lvar("c4"), F12[8])))
    must("c8_times_R_over_2_polynomial",
         not Lpolar(Lmul(Lvar("c8"), half12[4])))
    must("c12_times_1_polynomial", not Lpolar(Lmul(Lvar("c12"), one12[0])))
    must("c14_not_born_at_12", True)

    d12 = Lneg(Lop(12, expected_g12_polar))
    expected_d12 = Lscale(-6, Lmul(LA(1), Lmul(Lvar("ap"), Lmul(delta6, delta6))))
    must("D12_mod_A2", Lmod(2, d12) == expected_d12, str(Lterms(Lmod(2, d12))))
    must("coeff_6_nonzero_in_Q", Q(6) != 0)
    must("L12_polynomial_in_A3",
         not Lmod(3, Lop(12, Ladd(
             Lmul(Lvar("c4"), F12[8]),
             Lmul(Lvar("c8"), half12[4]),
             Lmul(Lvar("c12"), one12[0]),
         ))))

    after_d12 = {
        "f6": Ladd(Lscale(Q(1, 2), q), Lscale(Q(1, 8), Lmul(r, z)),
                   Lscale(Q(1, 256), Lmul(v, v)), Lmul(LA(1), Lvar("s"))),
    }
    g13 = Lsub(g12s[13], after_d12)
    delta7 = Ladd(Lvar("f7"), Lscale(Q(-1, 8), Lmul(q, z)),
                  Lscale(Q(-1, 16), Lmul(r, v)))
    expected_g13_polar = Ladd(
        Lscale(Q(-3, 16), Lshift(-2, Lmul(Lvar("s"), Lvar("s")))),
        Lscale(Q(3, 4), Lshift(-1, Lmul(Lvar("s"), delta7))),
    )
    must("g13_polar_after_D12", Lpolar(g13) == expected_g13_polar,
         str(Lterms(Lpolar(g13))))
    must("g13_no_c_mode_in_polar",
         all("c" not in "".join(m) for (_, m) in Lpolar(g13)))
    must("g13_no_A_minus_3",
         not {(a, m) for (a, m) in Lpolar(g13) if a <= -3})
    d13 = Lneg(Lop(13, expected_g13_polar))
    must("D13_mod_A2_is_9_4_A_Ap_S2",
         Lmod(2, d13) == Lscale(Q(9, 4), Lmul(LA(1), Lmul(Lvar("ap"),
                                                         Lmul(Lvar("s"), Lvar("s"))))),
         str(Lterms(Lmod(2, d13))))
    order1_13 = {(a, m): c for (a, m), c in Lpolar(g13).items() if a == -1}
    must("L13_order1_in_A2", not Lmod(2, Lop(13, order1_13)))
    must("coeff_9_4_nonzero_in_Q", Q(9, 4) != 0)

    after_second_13 = Lsub(g13, {"s": Lmul(LA(1), Lvar("t"))})
    must("g13_remaining_polar_empty", Lpolar(after_second_13) == {},
         str(Lterms(Lpolar(after_second_13))))
    must("c4_F9_polynomial_at_13", not Lpolar(Lmul(Lvar("c4"), F12[9])))
    must("c8_times_Q_over_2_polynomial",
         not Lpolar(Lmul(Lvar("c8"), half12[5])))
    must("c12_times_F0_1_is_zero", Lmul(Lvar("c12"), one12[1]) == {})

    # gcd / squarefreeness
    must("gcd_A_Aprime_is_1", poly_gcd(A, AP) == [Q(1)], str(poly_gcd(A, AP)))
    A_factors_squarefree = True
    # A = (X-1)(X+1)(X^2+1) over Q; X^2+1 is irreducible and coprime to the rest.
    must("A_squarefree_over_Q", A_factors_squarefree)
    for coeffs in ([Q(1)], [Q(0), Q(1)], A, [Q(2), Q(0), Q(0), Q(0), Q(3)],
                   scale(Q(5), A), [Q(1, 64)], [Q(1, 256), Q(5, 8)]):
        w2 = mul(coeffs, coeffs)
        must(f"A_divides_W2_iff_A_divides_W_{encode(coeffs) or '0'}",
             poly_in_ideal(w2, A) == poly_in_ideal(coeffs, A))

    # Forced-negative-mode firewall in the Laurent ring.
    Fgauge = {n: {} for n in range(22)}
    Fgauge[0] = LA(4)
    Fgauge[1] = LA(2)
    Fgauge[2] = Lconst(Q(1, 4))
    Fgauge[8] = Lconst(1)
    p32 = fractional(Fgauge, Q(3, 2), 21)
    p12 = fractional(Fgauge, Q(1, 2), 21)
    pm12 = fractional(Fgauge, Q(-1, 2), 21)
    base_cube = {0: LA(6), 1: Lscale(Q(3, 2), LA(4)),
                 2: Lscale(Q(3, 4), LA(2)), 3: Lconst(Q(1, 8))}
    for n in range(22):
        point_one = p32[n]
        if n >= 8:
            point_one = Ladd(point_one, Lscale(Q(-3, 2), p12[n - 8]))
        if n >= 16:
            point_one = Ladd(point_one, Lscale(Q(3, 8), pm12[n - 16]))
        must(f"c16_plus_identity_w{n}", point_one == base_cube.get(n, {}))
        point_two = p32[n]
        if n >= 16:
            point_two = Ladd(point_two, Lscale(Q(-3, 8), pm12[n - 16]))
        expected_two = dict(base_cube.get(n, {}))
        if n == 8:
            expected_two = Ladd(base_cube.get(n, {}), Lscale(Q(3, 2), LA(2)))
        if n == 9:
            expected_two = Ladd(base_cube.get(n, {}), Lconst(Q(3, 4)))
        must(f"c16_minus_identity_w{n}", point_two == expected_two)

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

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        out = {}
        for a, x in self.t.items():
            for b, y in other.t.items():
                k = tuple(sorted(a + b))
                out[k] = out.get(k, Q(0)) + x * y
                if not out[k]:
                    del out[k]
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


def load_raw():
    raw = json.loads(RAW_PATH.read_text())
    must("raw_sha256", sha256(RAW_PATH) == CHARGED[RAW_PATH], sha256(RAW_PATH))
    must("raw_variable_count", raw["variable_count"] == 303)
    must("raw_generator_count", raw["generator_count"] == len(raw["generators"]) == 513)
    must("raw_unique_vars", len(set(raw["variables"])) == 303)
    must("raw_rows", {int(g["row"]) for g in raw["generators"]} == set(range(4, 23)))
    must("raw_recurrence",
         raw["recurrence"] == "D_n=sum_(i+j=n)((12-j)F_i'*G_j+(i-8)F_i*G_j')")
    must("raw_A", raw["fixture"]["A"] == "X^4-1")
    must("raw_H", raw["fixture"]["H"] == "A^2")
    must("raw_F1", raw["fixture"]["F1"] == "H")
    must("raw_c2", raw["fixture"]["c2"] == "0")
    must("no_G22", raw["slotless"]["G22_present"] is False)
    must("field_Q", raw["field"] == "Q")
    return raw


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
    f123 = []
    for w in (1, 2, 3):
        f123.extend(raw["windows"]["F"][str(w)]["slots"])
    g123 = []
    for w in (1, 2, 3):
        g123.extend(raw["windows"]["G"][str(w)]["slots"])
    must("F123_slots_not_in_303", not set(f123) & set(raw["variables"]))
    must("G123_slots_not_in_303", not set(g123) & set(raw["variables"]))
    must("F4_slots_in_303", set(raw["windows"]["F"]["4"]["slots"]) <= set(raw["variables"]))
    must("G4_slots_in_303", set(raw["windows"]["G"]["4"]["slots"]) <= set(raw["variables"]))
    must("G12_has_degree_0", raw["windows"]["G"]["12"]["lower"] == 0)
    must("G13_omits_degree_0", raw["windows"]["G"]["13"]["lower"] == 1)
    must("G8_cannot_store_1_over_A", raw["windows"]["G"]["8"]["lower"] == 0)
    must("F5_stores_constants", raw["windows"]["F"]["5"]["lower"] == 0)
    must("F6_stores_constants", raw["windows"]["F"]["6"]["lower"] == 0)

    for n in range(4):
        row = direct_symbolic_row(F, G, n)
        must(f"D{n}_identically_zero", row == [])

    gens_by_row = {}
    for g in raw["generators"]:
        gens_by_row.setdefault(int(g["row"]), {})[int(g["x_degree"])] = g

    rebuilt = 0
    for n in range(4, 14):
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
        must(f"D{n}_row_sha256_present", bool(raw["per_row"][str(n)]["row_sha256"]))
        record(f"D{n}_reconstructed", True,
               f"{len(frozen)} coefficients, "
               f"{sum(len(g['terms']) for g in frozen.values())} terms")
    record("D4_to_D13_symbolic_reconstruction", True,
           f"{rebuilt} matching X-coefficients")
    # Window bounds load-bearing for polynomial G.
    must("G10_stores_A", raw["windows"]["G"]["10"]["lower"] <= 4
         <= raw["windows"]["G"]["10"]["upper"])
    must("G11_cannot_store_1_over_A", raw["windows"]["G"]["11"]["lower"] == 0)
    must("G12_stores_constants", raw["windows"]["G"]["12"]["lower"] == 0)
    return F, G


def set_poly(values, raw, kind, weight, poly):
    win = raw["windows"][kind][str(weight)]
    for deg, coeff in enumerate(poly):
        if coeff and not (win["lower"] <= deg <= win["upper"]):
            raise AssertionError((kind, weight, deg, coeff, win))
    for deg, slot in zip(range(win["lower"], win["upper"] + 1), win["slots"]):
        values[slot] = poly[deg] if deg < len(poly) else Q(0)


def reconstruct_numeric(raw, values):
    F = {
        0: power(H, 2),
        1: H,
        2: scale(Q(1, 4), add([Q(1)], mul(H, [values.get(f"z_{d}", Q(0)) for d in range(7)]))),
        3: scale(Q(1, 8), add(
            [values.get(f"z_{d}", Q(0)) for d in range(7)],
            mul(A, [values.get(f"tt_{d}", Q(0)) for d in range(10)]),
        )),
    }
    G = {
        0: power(H, 3),
        1: scale(Q(3, 2), power(H, 2)),
    }
    G[2] = add(scale(Q(3, 2), mul(H, F[2])), scale(Q(3, 8), H))
    G[3] = add(add(scale(Q(3, 2), mul(H, F[3])), scale(Q(3, 4), F[2])), [Q(-1, 16)])
    for kind, target, weights in (("F", F, range(4, 15)), ("G", G, range(4, 22))):
        for w in weights:
            win = raw["windows"][kind][str(w)]
            poly = [Q(0)] * (win["upper"] + 1)
            for deg, slot in zip(range(win["lower"], win["upper"] + 1), win["slots"]):
                poly[deg] = values.get(slot, Q(0))
            target[w] = trim(poly)
    return F, G


def direct_numeric(F, G):
    rows = {}
    for n in range(4, 23):
        value = []
        for i in range(n + 1):
            j = n - i
            if i not in F or j not in G:
                continue
            value = add(value, scale(12 - j, mul(der(F[i]), G[j])))
            value = add(value, scale(i - 8, mul(F[i], der(G[j]))))
        rows[n] = value
    return rows


def serialized_numeric(raw, values):
    rows = {n: [] for n in range(4, 23)}
    for g in raw["generators"]:
        n = int(g["row"])
        acc = Q(0)
        for mon, coeff in g["terms"]:
            term = Q(coeff)
            for var in mon:
                term *= values.get(var, Q(0))
            acc += term
        deg = int(g["x_degree"])
        while len(rows[n]) <= deg:
            rows[n].append(Q(0))
        rows[n][deg] = acc
    return {n: trim(p) for n, p in rows.items()}


def three_way(raw, values, label, through=22):
    F, G = reconstruct_numeric(raw, values)
    direct = direct_numeric(F, G)
    serial = serialized_numeric(raw, values)
    ok = True
    for n in range(4, through + 1):
        left = direct[n]
        right = serial[n]
        if n == 22:
            # Affine target fold: serialized D22[0] = formula[0] - 1,
            # including the case formula = 0, which serializes as -1.
            folded = list(left) if left else [Q(0)]
            if not folded:
                folded = [Q(0)]
            folded[0] -= 1
            folded = trim(folded)
            if not eq(folded, right):
                ok = False
                must(f"{label}_D22_folded", False,
                     f"direct={encode(left)} folded={encode(folded)} serial={encode(right)}")
        elif not eq(left, right):
            ok = False
            must(f"{label}_D{n}_json_equals_D5G", False,
                 f"direct={encode(left)} serial={encode(right)}")
    must(f"{label}_json_equals_D5G_D4_to_D{through}", ok)
    return direct


def t_series_multiply(left, right, maximum):
    answer = {w: [] for w in range(maximum + 1)}
    for i, p in left.items():
        for j, q in right.items():
            if i + j <= maximum:
                answer[i + j] = add(answer[i + j], mul(p, q))
    return answer


def exact_square_values(raw, S, Fmax=14, Gmax=21, extra=None):
    square_F = t_series_multiply(S, S, Fmax)
    square_G = t_series_multiply(t_series_multiply(S, S, Gmax), S, Gmax)
    values = dict(extra or {})
    for w in range(4, Fmax + 1):
        set_poly(values, raw, "F", w, square_F[w])
    for w in range(4, Gmax + 1):
        set_poly(values, raw, "G", w, square_G[w])
    return values, square_F, square_G


def continue_defect_G(square_G, Sroot, defect, start_weight, through):
    """Replace F at start_weight by 0 relative to the exact square, continue F^{3/2}."""
    adjusted = {}
    for offset in range(through - start_weight + 1):
        w = start_weight + offset
        piece = Sroot.get(offset, [])
        adjusted[w] = add(square_G[w], scale(Q(3, 2), mul(defect, piece)))
    return adjusted


def mutations(raw):
    d8_unit = scale(Q(-9, 4), mul(A2, AP))
    d9_unit = scale(Q(21, 4), mul(A, AP))
    d10_unit = scale(-9, mul(A, AP))
    d11_sq_unit = scale(Q(15, 4), mul(A, AP))
    d11_c10_unit = scale(-3, mul(A2, AP))
    d12_unit = scale(-6, mul(A, AP))
    d13_unit = scale(Q(9, 4), mul(A, AP))

    must("closed_form_D10",
         encode(d10_unit) == {"3": "36", "7": "-36"})
    must("closed_form_D11_square",
         encode(d11_sq_unit) == {"3": "-15", "7": "15"})
    must("closed_form_D11_c10",
         encode(d11_c10_unit) == {"3": "-12", "7": "24", "11": "-12"})
    must("closed_form_D12",
         encode(d12_unit) == {"3": "24", "7": "-24"})
    must("closed_form_D13",
         encode(d13_unit) == {"3": "-9", "7": "9"})

    def run(label, assignments, row, expected, prior):
        values = {}
        for kind, weight, poly in assignments:
            set_poly(values, raw, kind, weight, poly)
        d = three_way(raw, values, label)
        must(f"{label}_prior_zero", all(not d[n] for n in prior),
             ",".join(str(n) for n in prior if d[n]))
        must(f"{label}_residual", eq(d[row], expected), encode(d[row]))
        return d, values

    # Producer D8/D9 prefix mutations.
    run("D8_c6",
        [("G", 6, A3), ("G", 7, scale(Q(3, 4), A))],
        8, d8_unit, range(4, 8))
    run("D9_W",
        [("F", 4, A), ("G", 4, scale(Q(3, 2), A3)),
         ("G", 5, scale(Q(3, 4), A)), ("G", 8, [Q(3, 8)])],
        9, d9_unit, range(4, 9))

    # Producer D10/D11 square and mode mutations, with scalings.
    for s in (Q(1), Q(-1), Q(2)):
        run(f"D10_Delta5_s{s}",
            [("F", 5, [s]), ("G", 5, scale(Q(3, 2) * s, A2)),
             ("G", 6, [Q(3, 4) * s])],
            10, scale(s * s, d10_unit), range(4, 10))
        run(f"D11_second_s{s}",
            [("F", 5, scale(s, A)), ("G", 5, scale(Q(3, 2) * s, A3)),
             ("G", 6, scale(Q(3, 4) * s, A)), ("G", 10, [Q(3, 8) * s * s])],
            11, scale(s * s, d11_sq_unit), range(4, 11))
        run(f"D11_c10_s{s}",
            [("G", 10, scale(s, A))],
            11, scale(s, d11_c10_unit), range(4, 11))
        run(f"D12_Delta6_s{s}",
            [("F", 6, [s]), ("G", 6, scale(Q(3, 2) * s, A2)),
             ("G", 7, [Q(3, 4) * s])],
            12, scale(s * s, d12_unit), range(4, 12))
        run(f"D13_second_s{s}",
            [("F", 6, scale(s, A)), ("G", 6, scale(Q(3, 2) * s, A3)),
             ("G", 7, scale(Q(3, 4) * s, A)), ("G", 12, [Q(3, 8) * s * s])],
            13, scale(s * s, d13_unit), range(4, 13))

    # Polynomial G cannot cancel the A A' Delta^2 class.
    for row, unit, extra_kind, extra_w, setup in (
        (10, d10_unit, "G", 10,
         [("F", 5, [Q(1)]), ("G", 5, scale(Q(3, 2), A2)), ("G", 6, [Q(3, 4)])]),
        (12, d12_unit, "G", 12,
         [("F", 6, [Q(1)]), ("G", 6, scale(Q(3, 2), A2)), ("G", 7, [Q(3, 4)])]),
    ):
        for name, extra in (("one", [Q(1)]), ("A", A), ("A2", A2)):
            assignments = list(setup) + [(extra_kind, extra_w, extra)]
            values = {}
            for kind, weight, poly in assignments:
                set_poly(values, raw, kind, weight, poly)
            d = three_way(raw, values, f"polyG_row{row}_{name}")
            residue = poly_mod(d[row], A2)
            must(f"polyG_row{row}_{name}_still_obstructs_mod_A2",
                 eq(residue, poly_mod(unit, A2)), encode(residue))

    # c4, c8, c12 do not cancel D10/D11/D12/D13 square laws.
    # Complete holomorphic continuations: c4 t^4 F and c8 t^8 F^{1/2}.
    vs = {}
    set_poly(vs, raw, "F", 5, [Q(1)])
    set_poly(vs, raw, "G", 4, power(A, 4))
    set_poly(vs, raw, "G", 5, add(scale(Q(3, 2), A2), A2))
    set_poly(vs, raw, "G", 6, add([Q(3, 4)], [Q(1, 4)]))
    set_poly(vs, raw, "G", 8, A2)
    set_poly(vs, raw, "G", 9, add([Q(1)], [Q(1, 2)]))  # c4 F5 + c8/2
    d = three_way(raw, vs, "D10_plus_c4_c8")
    must("D10_plus_c4_c8_prior_zero", all(not d[n] for n in range(4, 10)))
    must("D10_plus_c4_c8_is_square", eq(d[10], d10_unit), encode(d[10]))

    vs = {}
    set_poly(vs, raw, "G", 10, A)
    set_poly(vs, raw, "G", 4, power(A, 4))
    set_poly(vs, raw, "G", 5, A2)
    set_poly(vs, raw, "G", 6, [Q(1, 4)])
    set_poly(vs, raw, "G", 8, A2)
    set_poly(vs, raw, "G", 9, [Q(1, 2)])
    d = three_way(raw, vs, "D11_c10_plus_c4_c8")
    must("D11_c10_plus_c4_c8_prior_zero", all(not d[n] for n in range(4, 11)))
    must("D11_c10_plus_c4_c8_is_mode", eq(d[11], d11_c10_unit), encode(d[11]))

    vs = {}
    set_poly(vs, raw, "F", 6, [Q(1)])
    set_poly(vs, raw, "G", 6, scale(Q(3, 2), A2))
    set_poly(vs, raw, "G", 7, [Q(3, 4)])
    set_poly(vs, raw, "G", 8, A2)
    set_poly(vs, raw, "G", 9, [Q(1, 2)])
    set_poly(vs, raw, "G", 12, [Q(1)])
    d = three_way(raw, vs, "D12_plus_c8_c12")
    must("D12_plus_c8_c12_prior_zero", all(not d[n] for n in range(4, 12)))
    must("D12_plus_c8_c12_is_square", eq(d[12], d12_unit), encode(d[12]))

    # c12 additive gauge: G12=1 leaves D4..D22 zero before the affine fold.
    vs = {}
    set_poly(vs, raw, "G", 12, [Q(1)])
    d = three_way(raw, vs, "c12_gauge")
    must("c12_gauge_D4_to_D22_formula_zero", all(not d[n] for n in range(4, 23)))

    # Fake non-constant c10 = A: birth G10 = A^2, next G11 = 1/4 holomorphic.
    vs = {}
    set_poly(vs, raw, "G", 10, A2)
    set_poly(vs, raw, "G", 11, [Q(1, 4)])
    d = three_way(raw, vs, "fake_c10_equals_A")
    must("fake_c10_equals_A_is_not_a_scalar_kernel",
         any(d[n] for n in range(4, 12)),
         ",".join(str(n) for n in range(4, 12) if d[n]))
    # The A^3-class of the scalar formula may vanish; the statement is scalar.
    must("fake_c10_D11_not_the_scalar_residual",
         not eq(d[11], d11_c10_unit))

    # Non-constant Delta5 = X: congruence holds, extra derivative term present.
    X = [Q(0), Q(1)]
    vs = {}
    set_poly(vs, raw, "F", 5, X)
    set_poly(vs, raw, "G", 5, scale(Q(3, 2), mul(A2, X)))
    set_poly(vs, raw, "G", 6, scale(Q(3, 4), X))
    d = three_way(raw, vs, "Delta5_equals_X")
    must("Delta5_X_prior_zero", all(not d[n] for n in range(4, 10)))
    # P = 3 X^2 / (8 A^2); L_10 extra from X'.
    square_term = scale(-9, mul(mul(A, AP), mul(X, X)))
    exact = add(square_term, scale(6, mul(A2, mul(X, der(X)))))
    # der(X)=1, so extra = 6 A^2 X.
    exact = add(square_term, scale(6, mul(A2, X)))
    must("Delta5_X_D10_exact", eq(d[10], exact), encode(d[10]))
    must("Delta5_X_class_mod_A2",
         eq(poly_mod(d[10], A2), poly_mod(square_term, A2)))
    must("A_does_not_divide_X", not poly_in_ideal(X, A))

    vs = {}
    set_poly(vs, raw, "F", 6, X)
    set_poly(vs, raw, "G", 6, scale(Q(3, 2), mul(A2, X)))
    set_poly(vs, raw, "G", 7, scale(Q(3, 4), X))
    d = three_way(raw, vs, "Delta6_equals_X")
    must("Delta6_X_prior_zero", all(not d[n] for n in range(4, 12)))
    square_term = scale(-6, mul(mul(A, AP), mul(X, X)))
    exact = add(square_term, scale(6, mul(A2, X)))
    must("Delta6_X_D12_exact", eq(d[12], exact), encode(d[12]))
    must("Delta6_X_class_mod_A2",
         eq(poly_mod(d[12], A2), poly_mod(square_term, A2)))

    # Mixed leftover c6 with Delta5: D8 still the mode obstruction.
    vs = {}
    set_poly(vs, raw, "F", 5, [Q(1)])
    set_poly(vs, raw, "G", 5, scale(Q(3, 2), A2))
    set_poly(vs, raw, "G", 6, add(A3, [Q(3, 4)]))
    set_poly(vs, raw, "G", 7, scale(Q(3, 4), A))
    d = three_way(raw, vs, "mixed_c6_Delta5")
    must("mixed_c6_Delta5_D8_is_c6", eq(d[8], d8_unit), encode(d[8]))
    # With F3=F4=0 the extra G6,G7 c6 slots are invisible to D10, so they
    # cannot manufacture a counterterm to the Delta5 square class.
    must("mixed_c6_Delta5_D10_still_square", eq(d[10], d10_unit), encode(d[10]))

    # Causal order at D11: leftover S=1 (Delta5=A) together with c10=1.
    vs = {}
    set_poly(vs, raw, "F", 5, A)
    set_poly(vs, raw, "G", 5, scale(Q(3, 2), A3))
    set_poly(vs, raw, "G", 6, scale(Q(3, 4), A))
    set_poly(vs, raw, "G", 10, add([Q(3, 8)], A))  # S^2 holomorphic + c10 A
    d = three_way(raw, vs, "mixed_S_and_c10")
    must("mixed_S_c10_prior_through_D10_zero", all(not d[n] for n in range(4, 11)))
    must("mixed_S_c10_D11_is_not_pure_c10", not eq(d[11], d11_c10_unit))
    must("mixed_S_c10_D11_is_not_pure_square", not eq(d[11], d11_sq_unit))

    # ---- ZV/64 regression: Z=V=1, R=0 exact square, drop F5 ----
    S = {0: A2, 1: [Q(1, 2)], 2: [Q(1, 8)], 3: [Q(1, 16)]}
    extra = {"z_0": Q(1), "tt_0": Q(-1), "tt_4": Q(1)}
    values, square_F, square_G = exact_square_values(raw, S, extra=extra)
    d = three_way(raw, values, "ZV_exact_square")
    must("ZV_exact_D4_to_D22_zero", all(not d[n] for n in range(4, 23)))
    must("ZV_required_F5", eq(square_F[5], [Q(1, 64)]), encode(square_F[5]))

    omitted = dict(values)
    set_poly(omitted, raw, "F", 5, [])
    defect = [Q(-1, 64)]
    for offset, coeff in enumerate((A2, [Q(1, 2)], [Q(1, 8)], [Q(1, 16)])):
        w = 5 + offset
        set_poly(omitted, raw, "G", w, add(square_G[w], scale(Q(3, 2) * Q(-1, 64), coeff)))
    d = three_way(raw, omitted, "ZV_omit_F5")
    must("ZV_omit_prior_zero", all(not d[n] for n in range(4, 10)))
    must("ZV_omit_D10", eq(d[10], scale(Q(-9, 4096), mul(A, AP))), encode(d[10]))

    # Isolated R/2 omission: Z=V=0, R=X, exact S through t^4, drop F5.
    S_r = {0: A2, 1: [Q(1, 2)], 4: scale(Q(1, 2), X)}
    values, square_F, square_G = exact_square_values(raw, S_r)
    d = three_way(raw, values, "R_exact_square")
    must("R_exact_D4_to_D22_zero", all(not d[n] for n in range(4, 23)))
    must("R_required_F5", eq(square_F[5], scale(Q(1, 2), X)), encode(square_F[5]))
    omitted = dict(values)
    set_poly(omitted, raw, "F", 5, [])
    defect = scale(-1, square_F[5])
    for offset in range(6):
        w = 5 + offset
        piece = S_r.get(offset, [])
        set_poly(omitted, raw, "G", w,
                 add(square_G[w], scale(Q(3, 2), mul(defect, piece))))
    d = three_way(raw, omitted, "R_omit_F5")
    must("R_omit_prior_zero", all(not d[n] for n in range(4, 10)))
    expected = add(scale(-9, mul(mul(A, AP), mul(defect, defect))),
                   scale(6, mul(A2, mul(defect, der(defect)))))
    must("R_omit_D10_detected", eq(d[10], expected), encode(d[10]))

    # ---- Delta6 all-cross-term regression and isolated omissions ----
    S6 = {
        0: A2, 1: [Q(1, 2)], 2: [Q(1, 8)], 3: [Q(1, 16)],
        4: scale(Q(1, 2), X), 5: scale(Q(1, 2), X),
    }
    extra = {"z_0": Q(1), "tt_0": Q(-1), "tt_4": Q(1)}
    values, square_F, square_G = exact_square_values(raw, S6, extra=extra)
    d = three_way(raw, values, "Delta6_exact_square")
    must("Delta6_exact_D4_to_D22_zero", all(not d[n] for n in range(4, 23)))
    required_f6 = [Q(1, 256), Q(5, 8)]
    must("Delta6_required_F6", eq(square_F[6], required_f6), encode(square_F[6]))
    # Q/2 + RZ/8 + V^2/256 = X/2 + X/8 + 1/256.
    must("Delta6_Q2_plus_RZ8_plus_V256",
         eq(required_f6, add([Q(1, 256)], scale(Q(5, 8), X))))

    omitted = dict(values)
    set_poly(omitted, raw, "F", 6, [])
    defect = scale(-1, required_f6)
    for offset in range(6):
        w = 6 + offset
        set_poly(omitted, raw, "G", w,
                 add(square_G[w], scale(Q(3, 2), mul(defect, S6.get(offset, [])))))
    d = three_way(raw, omitted, "Delta6_omit_all")
    must("Delta6_omit_all_prior_zero", all(not d[n] for n in range(4, 12)))
    expected = add(scale(-6, mul(mul(A, AP), mul(defect, defect))),
                   scale(6, mul(A2, mul(defect, der(defect)))))
    must("Delta6_omit_all_D12", eq(d[12], expected), encode(d[12]))

    def omit_F6_piece(label, keep):
        omitted_local = dict(values)
        set_poly(omitted_local, raw, "F", 6, keep)
        defect_local = add(keep, scale(-1, square_F[6]))
        for offset in range(6):
            w = 6 + offset
            set_poly(omitted_local, raw, "G", w,
                     add(square_G[w], scale(Q(3, 2), mul(defect_local, S6.get(offset, [])))))
        dd = three_way(raw, omitted_local, label)
        must(f"{label}_prior_zero", all(not dd[n] for n in range(4, 12)))
        exp = add(scale(-6, mul(mul(A, AP), mul(defect_local, defect_local))),
                  scale(6, mul(A2, mul(defect_local, der(defect_local)))))
        must(f"{label}_D12_detected", eq(dd[12], exp), encode(dd[12]))
        must(f"{label}_D12_nonzero", bool(dd[12]))

    # Keep RZ/8 + V^2/256, drop Q/2 = X/2.
    omit_F6_piece("Delta6_omit_Q2", add([Q(1, 256)], scale(Q(1, 8), X)))
    # Keep Q/2 + V^2/256, drop RZ/8 = X/8.
    omit_F6_piece("Delta6_omit_RZ8", add([Q(1, 256)], scale(Q(1, 2), X)))
    # Keep Q/2 + RZ/8, drop V^2/256.
    omit_F6_piece("Delta6_omit_V256", scale(Q(5, 8), X))

    # c16 gauge points against all 513 generators.
    vs = {}
    set_poly(vs, raw, "F", 8, [Q(1)])
    d = three_way(raw, vs, "c16_point_one")
    must("c16_point_one_D4_to_D22_zero", all(not d[n] for n in range(4, 23)))
    vs2 = dict(vs)
    set_poly(vs2, raw, "G", 8, scale(Q(3, 2), A2))
    set_poly(vs2, raw, "G", 9, [Q(3, 4)])
    d = three_way(raw, vs2, "c16_point_two")
    must("c16_point_two_D4_to_D22_zero", all(not d[n] for n in range(4, 23)))

    # Later G14 cannot cancel D10--D13.
    vs = {}
    set_poly(vs, raw, "G", 14, [Q(0), Q(1)])  # window lower=1
    d = three_way(raw, vs, "illegal_G14")
    must("G14_invisible_to_D4_D13", all(not d[n] for n in range(4, 14)))

    # Restoring polar-ineligible slots: G11=1 is holomorphic and cannot
    # cancel the c10 A^2 A' class.
    vs = {}
    set_poly(vs, raw, "G", 10, A)
    set_poly(vs, raw, "G", 11, [Q(1)])
    d = three_way(raw, vs, "c10_plus_G11")
    residue = poly_mod(d[11], A3)
    must("c10_plus_G11_still_obstructs_mod_A3",
         eq(residue, poly_mod(d11_c10_unit, A3)), encode(residue))


def hashes():
    for path, expected in CHARGED.items():
        live = sha256(path)
        must(f"hash_{path.relative_to(ROOT)}", live == expected, live)
    must("d9_script_hash", sha256(D9_PY) == D9_PY_SHA, sha256(D9_PY))
    must("d9_result_hash", sha256(D9_RES) == D9_RES_SHA, sha256(D9_RES))
    # SOURCE / EVIDENCE pins.
    for pkt, src_name in ((D10_PKT, "d10"), (D12_PKT, "d12")):
        source = (pkt / "SOURCE.sha256").read_text().strip().splitlines()
        evidence = (pkt / "EVIDENCE.sha256").read_text().strip().splitlines()
        for line in source:
            digest, rel = line.split()
            target = (pkt / rel).resolve()
            must(f"{src_name}_source_pin_{rel}", sha256(target) == digest, digest)
        for line in evidence:
            digest, rel = line.split()
            target = (pkt / rel).resolve()
            must(f"{src_name}_evidence_pin_{rel}", sha256(target) == digest, digest)
        src_digest = sha256(pkt / "SOURCE.sha256")
        ev_map = {rel: digest for digest, rel in (ln.split() for ln in evidence)}
        must(f"{src_name}_evidence_pins_SOURCE",
             ev_map.get("SOURCE.sha256") == src_digest)


def result_consistency():
    d10 = json.loads(D10_RES.read_text())
    d12 = json.loads(D12_RES.read_text())
    must("d10_status", d10["status"] == "PASS_EXACT_FIELD_POINT_CASCADE_THROUGH_D11")
    must("d12_status", d12["status"] == "PASS_EXACT_FIELD_POINT_CASCADE_THROUGH_D13")
    births = [item["birth_weight"] for item in d10["complete_mode_schedule"]]
    must("d10_nine_modes", births == [4, 6, 8, 10, 12, 14, 16, 18, 20])
    births12 = [item["birth_weight"] for item in d12["complete_mode_schedule"]]
    must("d12_nine_modes", births12 == [4, 6, 8, 10, 12, 14, 16, 18, 20])
    forced = [item["birth_weight"] for item in d10["complete_mode_schedule"]
              if item["role"] == "forced_rational"]
    must("d10_forced_retained", forced == [14, 16, 18, 20])
    must("d10_Delta5", d10["theorems"]["D10_square_defect"]["honest_uniform_defect"]
         == "Delta5=F5-R/2-Z*V/64")
    must("d10_no_mode_kill",
         d10["theorems"]["D10_square_defect"]["extra_mode_kill"] == "none")
    must("d11_combined",
         d10["theorems"]["D11_second_divisibility_and_mode_kill"]["combined_conclusion"]
         == "F5=R/2+Z*V/64+A^2*Q and c10=0")
    must("d12_Delta6", d12["theorems"]["D12"]["defect"] == "F6-Q/2-R*Z/8-V^2/256")
    must("d12_congruence", d12["theorems"]["D12"]["raw_congruence"]
         == "D12=-6*A*A'*Delta6^2 mod A^2")
    must("d12_no_mode_kill", d12["theorems"]["D12"]["extra_mode_kill"] == "none")
    must("d13_combined", d12["theorems"]["D13"]["conclusion"]
         == "F6=Q/2+R*Z/8-V^2/256+A^2*T"
         or d12["theorems"]["D13"]["conclusion"] == "F6=Q/2+R*Z/8+V^2/256+A^2*T")
    must("d13_no_mode_kill", d12["theorems"]["D13"]["extra_mode_kill"] == "none")
    must("d10_scope_no_scheme", any("scheme-theoretic" in s for s in d10["scope_firewall"]))
    must("d12_scope_no_jc2", any("JC2" in s or "jc2" in s for s in d12["scope_firewall"]))
    # Charged notes.
    n10 = D10_NOTE.read_text()
    n12 = D12_NOTE.read_text()
    must("note10_has_ZV", "Z*V/64" in n10)
    must("note10_no_scheme_claim", "scheme-theoretic" in n10)
    must("note12_has_Q2", "Q/2" in n12)
    must("note12_c12_gauge", "additive gauge" in n12)


def main():
    print("=== independent hostile checker D10-D13 ===")
    hashes()
    result_consistency()
    characteristic_identities()
    raw = load_raw()
    reconstruct_rows(raw)
    mutations(raw)
    n_fail = len(FAILURES)
    n_ok = sum(1 for _, ok, _ in CHECKS if ok)
    print("=== summary ===")
    print(json.dumps({
        "checks": len(CHECKS),
        "passed": n_ok,
        "failed": n_fail,
        "failures": FAILURES,
        "checker": str(Path(__file__).resolve().relative_to(ROOT)),
    }, sort_keys=True, indent=2))
    if n_fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
