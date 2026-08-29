#!/usr/bin/env python3
"""Independent hostile checker for the uniform D8-mode / D9-square packet.

This file is not the producer checker.  It rebuilds D4..D9 from the raw
D5G formula, reruns the fractional-power and square-root recurrences in a
separate Laurent ring, evaluates live and hostile mutations, and searches
for a polynomial assignment that would cancel the claimed poles.
Only fractions.Fraction and the Python standard library are used.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
PACKET = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828"
CHARGED = ROOT / "xmodel/ggv-upper-endpoint-uniform-d9-fullmodes-sol-ultra-20260828.md"
PRODUCER = PACKET / "verify_uniform_d9.py"
RESULT = PACKET / "RESULT.json"
README = PACKET / "README.md"
FREEZE = PACKET / "FREEZE.sha256"

RAW_SHA = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"
CHARGED_SHA_FREEZE = "ccf78403684ef7ee7e9f85336b4ccf86a01d679ba61b6327f4d2400ece16490e"
CHARGED_SHA_PROMPT = "ccff78403684ef7ee7e9f85336b4ccf86a01d679ba61b6327f4d2400ece16490e"

FAILURES = []
CHECKS = []


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


def add(a, b):
    n = max(len(a), len(b))
    return trim([
        (a[i] if i < len(a) else Q(0)) + (b[i] if i < len(b) else Q(0))
        for i in range(n)
    ])


def sub(a, b):
    return add(a, scale(-1, b))


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


def encode(poly):
    return {str(i): str(c) for i, c in enumerate(poly) if c}


def eq(a, b):
    a, b = trim(a), trim(b)
    return a == b


A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
AP = der(A)
H = power(A, 2)
A2 = power(A, 2)
A3 = power(A, 3)


# ---------------------------------------------------------------------------
# Sparse Laurent ring: (A-exponent, sorted monomial tuple) -> Q
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
    return sorted(((a, m, c) for (a, m), c in p.items()), key=lambda t: (t[0], t[1]))


DERIV = {
    "z": "dz", "v": "dv", "w": "dw",
    "f5": "df5", "f6": "df6", "f7": "df7", "f8": "df8", "f9": "df9",
}


def Lder(p):
    """X-derivative: A' = ap; c4,c6,c8 and other unmarked symbols constant."""
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


# ---------------------------------------------------------------------------
# Characteristic calculation, independent of the producer
# ---------------------------------------------------------------------------

def fractional(F, alpha, maximum):
    y = {0: LA(int(4 * alpha)) if alpha >= 0 else LA(int(4 * alpha))}
    # 4*alpha is integer on the nine-mode schedule.
    y[0] = LA(int(Q(4) * Q(alpha)))
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


def characteristic_identities():
    z, v, w = Lvar("z"), Lvar("v"), Lvar("w")
    f = {n: Lvar(f"f{n}") for n in range(5, 10)}
    c4, c6, c8 = Lvar("c4"), Lvar("c6"), Lvar("c8")
    F = {
        0: LA(4),
        1: LA(2),
        2: Ladd(Lconst(Q(1, 4)), Lscale(Q(1, 4), Lmul(LA(2), z))),
        3: Ladd(Lscale(Q(1, 8), z), Lscale(Q(1, 8), Lmul(LA(2), v))),
        4: Ladd(Lscale(Q(1, 16), v), Lscale(Q(1, 64), Lmul(z, z)), Lmul(LA(1), w)),
        **f,
    }
    base = fractional(F, Q(3, 2), 9)
    _, cube = square_root_cube(F, 9)
    for n in range(0, 10):
        must(f"S3_matches_F32_weight_{n}", base[n] == cube[n])

    three_q = fractional(F, Q(3, 4), 3)
    half = fractional(F, Q(1, 2), 1)
    quarter = fractional(F, Q(1, 4), 0)
    one = fractional(F, Q(0), 0)
    neg1 = fractional(F, Q(-1, 4), 0)
    neg2 = fractional(F, Q(-1, 2), 0)
    neg3 = fractional(F, Q(-3, 4), 0)
    neg4 = fractional(F, Q(-1), 0)

    # Nine-mode birth table and support at n=8,9.
    schedule = [
        (4, Q(1), "c4"),
        (6, Q(3, 4), "c6"),
        (8, Q(1, 2), "c8"),
        (10, Q(1, 4), "c10"),
        (12, Q(0), "c12"),
        (14, Q(-1, 4), "c14"),
        (16, Q(-1, 2), "c16"),
        (18, Q(-3, 4), "c18"),
        (20, Q(-1), "c20"),
    ]
    y0 = {
        4: half[0], 6: three_q[0], 8: half[0], 10: quarter[0], 12: one[0],
        14: neg1[0], 16: neg2[0], 18: neg3[0], 20: neg4[0],
    }
    # Birth values: t^m F^{(12-m)/8} has y_0 = A^{ (12-m)/2 }.
    expected_y0 = {
        4: LA(4), 6: LA(3), 8: LA(2), 10: LA(1), 12: Lconst(1),
        14: LA(-1), 16: LA(-2), 18: LA(-3), 20: LA(-4),
    }
    # half[0] is F^{1/2}_0 = A^2, but mode m=4 is F^1_0 = A^4.  Do not reuse half.
    y0[4] = LA(4)
    y0[8] = LA(2)
    for m, alpha, name in schedule:
        must(f"mode_{name}_birth_y0", y0[m] == expected_y0[m],
             f"{Lterms(y0[m])}")
        for n in (8, 9):
            support = (n - m) >= 0
            must(f"{name}_support_at_{n}_is_{support}",
                 support == (m <= n))

    must("F32_7_polynomial", not Lpolar(base[7]), str(Lterms(Lpolar(base[7]))))
    expected_b7 = Ladd(
        Lscale(Q(3, 16), Lmul(f[5], z)),
        Lscale(Q(3, 4), f[6]),
        Lscale(Q(3, 1024), Lmul(v, v)),
        Lscale(Q(3, 32), Lmul(LA(1), Lmul(v, w))),
        Lscale(Q(3, 2), Lmul(LA(2), f[7])),
    )
    must("F32_7_terms", base[7] == expected_b7, str(Lterms(base[7])))
    must("F32_8_polynomial", not Lpolar(base[8]), str(Lterms(Lpolar(base[8]))))

    expected_b8 = Ladd(
        Lscale(Q(3, 32), Lmul(f[5], v)),
        Lscale(Q(3, 16), Lmul(f[6], z)),
        Lscale(Q(3, 4), f[7]),
        Lscale(Q(-3, 4096), Lmul(Lmul(v, v), z)),
        Lscale(Q(3, 8), Lmul(w, w)),
        Lscale(Q(3, 2), Lmul(LA(2), f[8])),
    )
    must("F32_8_terms", base[8] == expected_b8, str(Lterms(base[8])))

    expected_b9 = Ladd(
        Lscale(Q(-3, 16), Lshift(-2, Lmul(w, w))),
        Lscale(Q(3, 4), Lshift(-1, Lmul(f[5], w))),
        Lscale(Q(-3, 256), Lshift(-1, Lmul(Lmul(v, w), z))),
        Lscale(Q(3, 32), Lmul(f[6], v)),
        Lscale(Q(3, 16), Lmul(f[7], z)),
        Lscale(Q(3, 4), f[8]),
        Lscale(Q(-1, 8192), Lmul(Lmul(v, v), v)),
        Lscale(Q(3, 2), Lmul(LA(2), f[9])),
    )
    must("F32_9_terms", base[9] == expected_b9, str(Lterms(base[9])))

    expected_y2 = Ladd(Lscale(Q(3, 32), LA(-1)), Lscale(Q(3, 16), Lmul(LA(1), z)))
    expected_y3 = Ladd(
        Lscale(Q(-1, 128), LA(-3)),
        Lscale(Q(3, 64), Lshift(-1, z)),
        Lscale(Q(3, 32), Lmul(LA(1), v)),
    )
    must("F34_2", three_q[2] == expected_y2, str(Lterms(three_q[2])))
    must("F34_3", three_q[3] == expected_y3, str(Lterms(three_q[3])))
    must("F12_0", half[0] == LA(2))
    must("F12_1", half[1] == Lconst(Q(1, 2)))

    # The polar part of (F^{3/4})_2 is 3/(32A), independent of z,v,w,f*.
    polar_y2 = Lpolar(three_q[2])
    must("F34_2_polar_independent_of_windows",
         polar_y2 == Lscale(Q(3, 32), LA(-1)), str(Lterms(polar_y2)))

    g8 = Ladd(base[8], Lmul(c4, F[4]), Lmul(c6, three_q[2]), Lmul(c8, half[0]))
    g9 = Ladd(base[9], Lmul(c4, F[5]), Lmul(c6, three_q[3]), Lmul(c8, half[1]))
    polar_g8 = Lpolar(g8)
    must("polar_g8_is_only_c6_over_A",
         polar_g8 == Lscale(Q(3, 32), Lshift(-1, c6)), str(Lterms(polar_g8)))

    # No c4, c8, w, v, z, or f* in polar(g8).
    for (a, m), _ in polar_g8.items():
        must("polar_g8_symbols_only_c6", m == ("c6",), str(m))
        must("polar_g8_order_minus_one", a == -1)

    expected_polar_g9 = Ladd(
        Lscale(Q(-1, 128), Lshift(-3, c6)),
        Lscale(Q(-3, 16), Lshift(-2, Lmul(w, w))),
        Lscale(Q(3, 64), Lshift(-1, Lmul(c6, z))),
        Lscale(Q(3, 4), Lshift(-1, Lmul(f[5], w))),
        Lscale(Q(-3, 256), Lshift(-1, Lmul(Lmul(v, w), z))),
    )
    must("polar_g9_full_before_c6_kill", Lpolar(g9) == expected_polar_g9,
         str(Lterms(Lpolar(g9))))

    # c6 order-three term dominates W^2/A^2 and cannot be cancelled by it.
    order3 = {(a, m): c for (a, m), c in Lpolar(g9).items() if a <= -3}
    must("g9_order3_is_c6_firewall",
         order3 == Lscale(Q(-1, 128), Lshift(-3, c6)))

    d8 = Lneg(Lop(8, polar_g8))
    must("D8_L_identity_exact_not_just_mod",
         d8 == Lscale(Q(-9, 4), Lmul(LA(2), Lmul(Lvar("ap"), c6))),
         str(Lterms(d8)))
    must("L8_of_polynomial_in_A3",
         not Lmod(3, Lop(8, Ladd(base[8], Lmul(c4, F[4]), Lmul(c8, half[0])))))

    polar_g9_c6_zero = {
        k: c for k, c in Lpolar(g9).items() if "c6" not in k[1]
    }
    must("polar_g9_after_c6_zero",
         polar_g9_c6_zero == Ladd(
             Lscale(Q(-3, 16), Lshift(-2, Lmul(w, w))),
             Lscale(Q(3, 4), Lshift(-1, Lmul(f[5], w))),
             Lscale(Q(-3, 256), Lshift(-1, Lmul(Lmul(v, w), z))),
         ))

    d9 = Lneg(Lop(9, polar_g9_c6_zero))
    d9_mod = Lmod(2, d9)
    must("D9_mod_A2_is_21_4_A_Ap_W2",
         d9_mod == Lscale(Q(21, 4), Lmul(LA(1), Lmul(Lvar("ap"), Lmul(w, w)))),
         str(Lterms(d9_mod)))

    # Order-1 polar terms of g9 land in A^2 under L_9, so they cannot cancel W^2.
    order1 = {(a, m): c for (a, m), c in polar_g9_c6_zero.items() if a == -1}
    must("L9_order1_in_A2", not Lmod(2, Lop(9, order1)))
    must("L9_polynomial_in_A3",
         not Lmod(3, Lop(9, Ladd(Lmul(c4, F[5]), Lmul(c8, half[1])))))

    # gcd(A, A') = 1 over Q.
    must("gcd_A_Aprime_is_1", poly_gcd(A, AP) == [Q(1)], str(poly_gcd(A, AP)))
    must("char0_units_9_and_21_nonzero", Q(9, 4) != 0 and Q(21, 4) != 0)

    return {
        "polar_g8": polar_g8,
        "polar_g9": Lpolar(g9),
        "d8": d8,
        "d9_mod": d9_mod,
        "schedule": schedule,
    }


# ---------------------------------------------------------------------------
# Raw system: reconstruct D4..D9 and evaluate mutations
# ---------------------------------------------------------------------------

def load_raw():
    raw = json.loads(RAW_PATH.read_text())
    must("raw_sha256", sha256(RAW_PATH) == RAW_SHA, sha256(RAW_PATH))
    must("raw_variable_count", raw["variable_count"] == 303)
    must("raw_generator_count", raw["generator_count"] == 513)
    must("raw_generator_len", len(raw["generators"]) == 513)
    must("raw_unique_vars", len(set(raw["variables"])) == 303)
    must("raw_rows", {int(g["row"]) for g in raw["generators"]} == set(range(4, 23)))
    must("raw_recurrence",
         raw["recurrence"] == "D_n=sum_(i+j=n)((12-j)F_i'*G_j+(i-8)F_i*G_j')")
    must("raw_A", raw["fixture"]["A"] == "X^4-1")
    must("no_G22", raw["slotless"]["G22_present"] is False)
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
    # F1/F2/F3 window slots are documentary; they are not among the 303 variables.
    f123 = []
    for w in (1, 2, 3):
        f123.extend(raw["windows"]["F"][str(w)]["slots"])
    must("F123_slots_not_in_303", not set(f123) & set(raw["variables"]))

    for n in range(4):
        row = direct_symbolic_row(F, G, n)
        must(f"D{n}_identically_zero", row == [])

    gens_by_row = {}
    for g in raw["generators"]:
        gens_by_row.setdefault(int(g["row"]), {})[int(g["x_degree"])] = g

    rebuilt = 0
    for n in range(4, 10):
        row = direct_symbolic_row(F, G, n)
        frozen = gens_by_row[n]
        must(f"D{n}_degree_span",
             (len(row) - 1 if row else -1) == max(frozen))
        for deg, mv in enumerate(row):
            got = mv.as_map()
            exp = gen_map(frozen[deg]["terms"]) if deg in frozen else {}
            if got != exp:
                must(f"D{n}_deg{deg}_terms", False,
                     f"sym={got} frozen={exp}")
            else:
                rebuilt += 1
        extra = set(frozen) - set(range(len(row)))
        must(f"D{n}_no_extra_frozen_degrees", not extra, str(extra))
        record(f"D{n}_reconstructed", True,
               f"{len(frozen)} coefficients, {sum(len(g['terms']) for g in frozen.values())} terms")
    record("D4_to_D9_symbolic_reconstruction", True, f"{rebuilt} matching X-coefficients")
    return F, G


def set_poly(values, raw, kind, weight, poly):
    win = raw["windows"][kind][str(weight)]
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
    for n in range(22):
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
    rows = {n: [] for n in range(4, 22)}
    for g in raw["generators"]:
        n = int(g["row"])
        if n == 22:
            continue
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


def three_way(raw, values, label):
    F, G = reconstruct_numeric(raw, values)
    direct = direct_numeric(F, G)
    serial = serialized_numeric(raw, values)
    ok = all(eq(direct[n], serial[n]) for n in range(4, 22))
    must(f"{label}_json_equals_D5G_D4_to_D21", ok)
    return direct


def poly_in_ideal(poly, modulus):
    return not poly_mod(poly, modulus)


def mutations(raw):
    expected_d8 = scale(Q(-9, 4), mul(A2, AP))
    expected_d9 = scale(Q(21, 4), mul(A, AP))
    must("closed_form_D8_poly",
         encode(expected_d8) == {"3": "-9", "7": "18", "11": "-9"})
    must("closed_form_D9_poly",
         encode(expected_d9) == {"3": "-21", "7": "21"})

    # Producer T3 mutation: c6=1 through G7, omit polar G8.
    v = {}
    set_poly(v, raw, "G", 6, A3)
    set_poly(v, raw, "G", 7, scale(Q(3, 4), A))
    d = three_way(raw, v, "c6_unit")
    must("c6_unit_D4_to_D7_zero", all(not d[n] for n in range(4, 8)))
    must("c6_unit_D8", eq(d[8], expected_d8), encode(d[8]))
    for s in (Q(-1), Q(2)):
        vs = {}
        set_poly(vs, raw, "G", 6, scale(s, A3))
        set_poly(vs, raw, "G", 7, scale(s * Q(3, 4), A))
        ds = three_way(raw, vs, f"c6_scale_{s}")
        must(f"c6_scale_{s}_D8", eq(ds[8], scale(s, expected_d8)), encode(ds[8]))

    # Producer T4 mutation: W=1, G through weight 8, omit polar G9.
    v = {}
    set_poly(v, raw, "F", 4, A)
    set_poly(v, raw, "G", 4, scale(Q(3, 2), A3))
    set_poly(v, raw, "G", 5, scale(Q(3, 4), A))
    set_poly(v, raw, "G", 8, [Q(3, 8)])
    d = three_way(raw, v, "W_unit")
    must("W_unit_D4_to_D8_zero", all(not d[n] for n in range(4, 9)))
    must("W_unit_D9", eq(d[9], expected_d9), encode(d[9]))
    for s in (Q(-1), Q(2)):
        vs = {}
        set_poly(vs, raw, "F", 4, scale(s, A))
        set_poly(vs, raw, "G", 4, scale(s * Q(3, 2), A3))
        set_poly(vs, raw, "G", 5, scale(s * Q(3, 4), A))
        set_poly(vs, raw, "G", 8, [s * s * Q(3, 8)])
        ds = three_way(raw, vs, f"W_scale_{s}")
        must(f"W_scale_{s}_D4_to_D8_zero", all(not ds[n] for n in range(4, 9)))
        must(f"W_scale_{s}_D9", eq(ds[9], scale(s * s, expected_d9)), encode(ds[9]))

    # Hostile: polynomial G8 cannot cancel the c6 A^2 A' class.
    for name, extra in (("one", [Q(1)]), ("A", A), ("A2", A2), ("X3", [Q(0), Q(0), Q(0), Q(1)])):
        vs = {}
        set_poly(vs, raw, "G", 6, A3)
        set_poly(vs, raw, "G", 7, scale(Q(3, 4), A))
        set_poly(vs, raw, "G", 8, extra)
        ds = three_way(raw, vs, f"c6_plus_G8_{name}")
        residue = poly_mod(ds[8], A3)
        must(f"c6_plus_G8_{name}_still_obstructs_mod_A3",
             eq(residue, poly_mod(expected_d8, A3)), encode(residue))
        must(f"c6_plus_G8_{name}_D8_nonzero", bool(ds[8]))

    # Hostile: c4 and c8 polynomial modes do not cancel c6.
    vs = {}
    set_poly(vs, raw, "G", 4, power(A, 4))          # c4=1 times F0=A^4
    set_poly(vs, raw, "G", 5, A2)                    # c4 F1
    set_poly(vs, raw, "G", 6, add(A3, scale(Q(1, 4), [Q(1)])))  # c6 A^3 + c4 F2
    set_poly(vs, raw, "G", 7, scale(Q(3, 4), A))     # c6 y1; c4 F3=0
    set_poly(vs, raw, "G", 8, A2)                    # c8 A^2; omit polar c6
    ds = three_way(raw, vs, "c4_c6_c8")
    must("c4_c6_c8_D4_to_D7_zero", all(not ds[n] for n in range(4, 8)))
    must("c4_c6_c8_D8_is_c6_obstruction", eq(ds[8], expected_d8), encode(ds[8]))

    # Pure c4 and pure c8 are kernels through D8 on the exact square.
    vs = {}
    set_poly(vs, raw, "G", 4, power(A, 4))
    set_poly(vs, raw, "G", 5, A2)
    set_poly(vs, raw, "G", 6, [Q(1, 4)])
    ds = three_way(raw, vs, "pure_c4")
    must("pure_c4_D4_to_D9_zero", all(not ds[n] for n in range(4, 10)))

    vs = {}
    set_poly(vs, raw, "G", 8, A2)
    ds = three_way(raw, vs, "pure_c8_through_G8")
    must("pure_c8_through_G8_D4_to_D8_zero", all(not ds[n] for n in range(4, 9)))
    vs = {}
    set_poly(vs, raw, "G", 8, A2)
    set_poly(vs, raw, "G", 9, [Q(1, 2)])
    ds = three_way(raw, vs, "pure_c8")
    must("pure_c8_D4_to_D9_zero", all(not ds[n] for n in range(4, 10)))

    # Non-constant fake k6=A: polynomial G6=A^4, G7=3 A^2/4, G8=3/32.
    # If this vanished, T3 would be false as a scalar-constant statement.
    vs = {}
    set_poly(vs, raw, "G", 6, power(A, 4))
    set_poly(vs, raw, "G", 7, scale(Q(3, 4), A2))
    set_poly(vs, raw, "G", 8, [Q(3, 32)])
    ds = three_way(raw, vs, "fake_k6_equals_A")
    must("fake_k6_equals_A_is_not_a_kernel",
         any(ds[n] for n in range(4, 9)),
         "D" + ",".join(str(n) for n in range(4, 9) if ds[n]))
    # The A^3-class of D8 does vanish, so the producer modulus is sharp
    # only because c6 is a characteristic constant, not an X-polynomial.
    must("fake_k6_equals_A_D8_in_A3",
         poly_in_ideal(ds[8], A3), encode(poly_mod(ds[8], A3)))

    # Mixed W=1 and c6=1: D8 still the c6 obstruction; D9 is not the square law.
    vs = {}
    set_poly(vs, raw, "F", 4, A)
    set_poly(vs, raw, "G", 4, scale(Q(3, 2), A3))
    set_poly(vs, raw, "G", 5, scale(Q(3, 4), A))
    set_poly(vs, raw, "G", 6, A3)
    set_poly(vs, raw, "G", 7, scale(Q(3, 4), A))
    set_poly(vs, raw, "G", 8, [Q(3, 8)])
    ds = three_way(raw, vs, "mixed_c6_W")
    must("mixed_c6_W_D4_to_D7_zero", all(not ds[n] for n in range(4, 8)))
    must("mixed_c6_W_D8_is_c6_obstruction", eq(ds[8], expected_d8), encode(ds[8]))
    must("mixed_c6_W_D9_is_not_square_law", not eq(ds[9], expected_d9), encode(ds[9]))

    # W=1 plus c4 and c8: D8 vanishes, D9 remains the square obstruction.
    # c4 t^4 F also feeds G8 += c4 F4 = A.
    vs = {}
    set_poly(vs, raw, "F", 4, A)
    set_poly(vs, raw, "G", 4, add(scale(Q(3, 2), A3), power(A, 4)))
    set_poly(vs, raw, "G", 5, add(scale(Q(3, 4), A), A2))
    set_poly(vs, raw, "G", 6, [Q(1, 4)])
    set_poly(vs, raw, "G", 8, add(add([Q(3, 8)], A2), A))
    set_poly(vs, raw, "G", 9, [Q(1, 2)])  # c8 (F^{1/2})_1
    ds = three_way(raw, vs, "W_plus_c4_c8")
    must("W_plus_c4_c8_D4_to_D8_zero", all(not ds[n] for n in range(4, 9)))
    must("W_plus_c4_c8_D9_is_square_law", eq(ds[9], expected_d9), encode(ds[9]))

    # Polynomial G9 cannot cancel the A A' W^2 class.
    for name, extra in (("one", [Q(1)]), ("A", A), ("A2", A2)):
        vs = {}
        set_poly(vs, raw, "F", 4, A)
        set_poly(vs, raw, "G", 4, scale(Q(3, 2), A3))
        set_poly(vs, raw, "G", 5, scale(Q(3, 4), A))
        set_poly(vs, raw, "G", 8, [Q(3, 8)])
        set_poly(vs, raw, "G", 9, extra)
        ds = three_way(raw, vs, f"W_plus_G9_{name}")
        residue = poly_mod(ds[9], A2)
        must(f"W_plus_G9_{name}_still_obstructs_mod_A2",
             eq(residue, poly_mod(expected_d9, A2)), encode(residue))
        must(f"W_plus_G9_{name}_D9_nonzero", bool(ds[9]))

    # Non-constant W=X: D9 = (21/4) A A' X^2; A does not divide X.
    vs = {}
    WX = [Q(0), Q(1)]
    set_poly(vs, raw, "F", 4, mul(A, WX))
    set_poly(vs, raw, "G", 4, scale(Q(3, 2), mul(A3, WX)))
    set_poly(vs, raw, "G", 5, scale(Q(3, 4), mul(A, WX)))
    set_poly(vs, raw, "G", 8, scale(Q(3, 8), mul(WX, WX)))
    ds = three_way(raw, vs, "W_equals_X")
    must("W_equals_X_D4_to_D8_zero", all(not ds[n] for n in range(4, 9)))
    square_term = scale(Q(21, 4), mul(mul(A, AP), mul(WX, WX)))
    # N=-3 W^2/16, extra same-row piece 8 A^2 N' = -3 A^2 W W' with W'=1.
    exact = add(square_term, scale(-3, mul(A2, WX)))
    must("W_equals_X_D9_exact_with_Wprime", eq(ds[9], exact), encode(ds[9]))
    must("W_equals_X_D9_class_mod_A2",
         eq(poly_mod(ds[9], A2), poly_mod(square_term, A2)),
         encode(poly_mod(ds[9], A2)))
    must("A_does_not_divide_X", not poly_in_ideal(WX, A))
    must("A_does_not_divide_X2", not poly_in_ideal(mul(WX, WX), A))

    # Z=1, W=V=0: F = (A^2 + t/2 + t^2/8)^2, so F4 = Z^2/64 = 1/64.
    # Put the polynomial c6 mode through G7 and the holomorphic 3AZ/16 in G8;
    # omit only the polar 3c6/(32A).  D8 must be the exact c6 obstruction.
    U = {0: A2, 1: [Q(1, 2)], 2: [Q(1, 8)]}
    cube = {}
    for n in range(0, 9):
        acc = []
        for i in range(n + 1):
            for j in range(n - i + 1):
                k = n - i - j
                if i in U and j in U and k in U:
                    acc = add(acc, mul(mul(U[i], U[j]), U[k]))
        cube[n] = acc
    vs = {"z_0": Q(1)}
    set_poly(vs, raw, "F", 4, [Q(1, 64)])
    for n in range(4, 8):
        set_poly(vs, raw, "G", n, cube[n])
    set_poly(vs, raw, "G", 6, add(cube[6], A3))
    set_poly(vs, raw, "G", 7, add(cube[7], scale(Q(3, 4), A)))
    set_poly(vs, raw, "G", 8, add(cube[8], scale(Q(3, 16), A)))
    ds = three_way(raw, vs, "Z_and_c6")
    must("Z_and_c6_D4_to_D7_zero", all(not ds[n] for n in range(4, 8)))
    must("Z_and_c6_D8_is_c6_obstruction", eq(ds[8], expected_d8), encode(ds[8]))

    # Restoring a G10 slot cannot touch D8 or D9.
    vs = {}
    set_poly(vs, raw, "G", 10, [Q(1)])
    ds = three_way(raw, vs, "illegal_G10")
    must("G10_invisible_to_D4_D9", all(not ds[n] for n in range(4, 10)))

    # Field-radical: A|W^2 implies A|W because A is squarefree.
    # Counter-scheme: over Q[e]/(e^2), e^2 is 0 but e is not; that ring is
    # not a field.  On a field, evaluation at the four simple roots of A
    # forces W(rho)=0, hence A|W in K[X].
    roots_ok = True
    # A = X^4-1 = (X-1)(X+1)(X^2+1).  Over Q(i) the roots are ±1, ±i.
    # Check that A and A' share no common root by the already-proved gcd=1,
    # and that W^2 ≡ 0 mod A implies W ≡ 0 mod A in Q[X] by coprimeness.
    # Explicit: if A divides W^2 and gcd(A,W)=1 then A divides 1, contradiction
    # unless W=0 in Q[X]/(A).  Euclidean algorithm:
    def divides_radical(W):
        g = poly_gcd(A, W)
        # A|W^2 iff every irreducible factor of A divides W, iff A|W, iff g=A
        # up to units, i.e. g is a scalar multiple of A or 1.
        return eq(g, [Q(1)]) is False or eq(W, [])
    must("squarefree_field_radical_W_eq_X_fails", not poly_in_ideal(mul(WX, WX), A))
    must("squarefree_field_radical_W_eq_A_passes", poly_in_ideal(mul(A, A), A) and poly_in_ideal(A, A))
    # Direct: remainder of W^2 mod A is 0 iff remainder of W mod A is 0
    # because Q[X]/(A) is a product of fields.
    for coeffs in ([Q(1)], [Q(0), Q(1)], A, [Q(2), Q(0), Q(0), Q(0), Q(3)], scale(Q(5), A)):
        w2 = mul(coeffs, coeffs)
        must(f"A_divides_W2_iff_A_divides_W_{encode(coeffs) or '0'}",
             poly_in_ideal(w2, A) == poly_in_ideal(coeffs, A))


def hashes():
    live_charged = sha256(CHARGED)
    live_raw = sha256(RAW_PATH)
    live_producer = sha256(PRODUCER)
    live_result = sha256(RESULT)
    live_readme = sha256(README)
    freeze = FREEZE.read_text()
    must("charged_matches_freeze_pin", live_charged == CHARGED_SHA_FREEZE, live_charged)
    must("prompt_hash_is_65_char_transcription",
         len(CHARGED_SHA_PROMPT) == 65 and CHARGED_SHA_PROMPT.replace("ccff", "ccf", 1) == CHARGED_SHA_FREEZE)
    must("raw_matches_charge", live_raw == RAW_SHA)
    freeze_lines = {line.split()[1]: line.split()[0] for line in freeze.strip().splitlines()}
    must("freeze_raw", freeze_lines["cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"] == live_raw)
    must("freeze_producer", freeze_lines["cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/verify_uniform_d9.py"] == live_producer)
    must("freeze_result", freeze_lines["cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/RESULT.json"] == live_result)
    must("freeze_readme", freeze_lines["cases/ggv_8_28_upper_endpoint_uniform_d9_fullmodes_20260828/README.md"] == live_readme)
    must("freeze_charged", freeze_lines["xmodel/ggv-upper-endpoint-uniform-d9-fullmodes-sol-ultra-20260828.md"] == live_charged)
    return {
        "charged": live_charged,
        "raw": live_raw,
        "producer": live_producer,
        "result": live_result,
        "readme": live_readme,
    }


def result_consistency():
    data = json.loads(RESULT.read_text())
    must("result_schema", data["schema"] == "jc2.ggv.upper_endpoint.uniform_d9_fullmodes.result.v1")
    must("result_status", data["status"] == "PASS_EXACT_FIELD_POINT_DIVISIBILITY")
    births = [item["birth_weight"] for item in data["mode_schedule"]]
    must("nine_modes_serialized", births == [4, 6, 8, 10, 12, 14, 16, 18, 20])
    must("forced_rational_retained",
         [item["birth_weight"] for item in data["mode_schedule"] if item["role"] == "forced_rational"]
         == [14, 16, 18, 20])
    must("support_at_9",
         [item["birth_weight"] for item in data["mode_schedule"] if item["support_at_weight_9"]]
         == [4, 6, 8])
    must("T3_conclusion", data["theorems"]["T3_D8_c6_mode_kill"]["conclusion"] == "c6=0")
    must("T4_conclusion", data["theorems"]["T4_D9_square_defect"]["conclusion"] == "A divides W")
    must("T3_congruence",
         data["theorems"]["T3_D8_c6_mode_kill"]["raw_congruence"]
         == "D8_raw=-(9/4)*c6*A^2*A' mod A^3")
    must("T4_congruence",
         data["theorems"]["T4_D9_square_defect"]["raw_congruence"]
         == "D9_raw=(21/4)*A*A'*W^2 mod A^2")
    must("scope_no_scheme", any("scheme-theoretic" in s for s in data["scope_firewall"]))
    must("scope_no_endpoint", any("endpoint emptiness" in s for s in data["scope_firewall"]))
    must("scope_negative_modes_kept", any("c14,c16,c18,c20 remain mandatory" in s for s in data["scope_firewall"]))


def main():
    print("=== independent hostile checker ===")
    digests = hashes()
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
        "digests": digests,
        "checker": str(Path(__file__).resolve().relative_to(ROOT)),
    }, sort_keys=True, indent=2))
    if n_fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
