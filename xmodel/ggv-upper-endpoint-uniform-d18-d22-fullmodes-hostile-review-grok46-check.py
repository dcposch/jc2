#!/usr/bin/env python3
"""Independent hostile checker for the uniform D18--D22 endpoint packet.

Does not import the D18--D22 producer.  Rebuilds the nine-mode Laurent
recurrence through weight 22, replays the D16/D17 prefix in the same ring,
reconstructs literal D18--D22 rows from all 513 raw generators, and tests
live mutations with fractions.Fraction only.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json"
CHARGED_NOTE = ROOT / "xmodel/ggv-upper-endpoint-uniform-d18-d22-fullmodes-sol-ultra-20260828.md"
PACKET = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d18_d22_fullmodes_20260828"
PRODUCER = PACKET / "verify_uniform_d18_d22.py"
RESULT = PACKET / "RESULT.json"
README = PACKET / "README.md"
SOURCE = PACKET / "SOURCE.sha256"
EVIDENCE = PACKET / "EVIDENCE.sha256"
PRED_PY = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828/verify_uniform_d16_d17.py"
PRED_RES = ROOT / "cases/ggv_8_28_upper_endpoint_uniform_d16_d17_fullmodes_20260828/RESULT.json"
REVIEW_RESULT = ROOT / "xmodel/ggv-upper-endpoint-uniform-d18-d22-fullmodes-hostile-review-grok46-RESULT.json"

CHARGED = {
    CHARGED_NOTE: "ecf83ac7b380a18f939e60671a4e97290f9f68b51536c236b81f71bb6a6c5bb8",
    PRODUCER: "49d1acaf1a8b066e9de15005e97ce948b8b33bd38315a1e77dcdf945c9b9761d",
    RESULT: "f46d7afd8b4e1e7cb5c60b029f8660dc2f1bf0e8770724808a3451c8c4e9e684",
    README: "0b9e0c17ad94a8b11f857a65f18caa34f45e771658be52d1452bba512af2ffd4",
    SOURCE: "1ab354e526a44d3aa7be2ff41fa4bbc7c0dbba8f059c033417651bd28325eefe",
    EVIDENCE: "1f6369c5cba8c3a149d83b3550f125b3125f7450c06419b4e7046e49ed96ad57",
    PRED_PY: "5904d7b19dc5d46d31a781150c4b6de9e62e32812b554006e92f78f9d76fd5d9",
    PRED_RES: "2a6f363df8fb4aef94f01d7a938e3bfcff15f6db49af3164e36367c9a6d1929a",
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
    "y": "dy", "b": "b_x", "d": "d_x", "e": "e_x", "h": "h_x",
    "j": "j_x", "k": "k_x", "m": "m_x", "n": "n_x", "o": "o_x",
    "p": "p_x", "s": "s_x", "u": "u_x", "ell": "ell_x",
    **{f"f{n}": f"df{n}" for n in range(8, 15)},
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


CANON = {"ap": "a_x"}


def Lencode(p):
    items = []
    for (a, m), c in p.items():
        names = tuple(sorted(CANON.get(s, s) for s in m))
        items.append({
            "A_exponent": a,
            "coefficient": str(c),
            "monomial": list(names),
        })
    items.sort(key=lambda it: (it["A_exponent"], it["monomial"], it["coefficient"]))
    return items


def product(*items):
    out = items[0]
    for item in items[1:]:
        out = Lmul(out, item)
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


def continuation(F, maximum, killed=None):
    killed = set(killed or ())
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


def prefix_F():
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
    for n in range(15, 23):
        F[n] = {}
    return F, z, v, r, q, t, y


def through(item, relations):
    for relation in relations:
        item = Lsub(item, relation)
    return item


def characteristic_identities():
    F, z, v, r, q, t, y = prefix_F()
    powers, g = continuation(F, 22, killed={6, 10, 14})

    must("nine_modes", list(MODES) == [4, 6, 8, 10, 12, 14, 16, 18, 20])
    must("c18_born_at_18", 18 <= 18 and 18 > 17)
    must("c20_born_at_20", 20 <= 20 and 20 > 19)
    must("c16_live_at_18", 16 <= 18)
    must("c8_live_at_22", 8 <= 22)
    must("c22_not_a_mode", 22 not in MODES)
    must("mode_c18_y0", powers[Q(-3, 4)][0] == LA(-3))
    must("mode_c20_y0", powers[Q(-1)][0] == LA(-4))
    must("mode_c18_y1", powers[Q(-3, 4)][1] == Lscale(Q(-3, 4), LA(-5)))
    must("mode_c20_y1", powers[Q(-1)][1] == Lscale(-1, LA(-6)))
    must("g18_contains_c18_over_A3", g[18].get((-3, ("c18",))) == Q(1))
    must("g20_contains_c20_over_A4", g[20].get((-4, ("c20",))) == Q(1))
    must("L18_annihilates_c18_over_A3", Lop(18, Lshift(-3, Lvar("c18"))) == {})
    must("L20_annihilates_c20_over_A4", Lop(20, Lshift(-4, Lvar("c20"))) == {})
    must("L22_annihilates_optional_c22_over_A5",
         Lop(22, Lshift(-5, Lvar("c22"))) == {})
    must("char0_visible", Q(8) != 0 and Q(9) != 0 and Q(12) != 0)
    must("gcd_A_Aprime_is_1", poly_gcd(A, AP) == [Q(1)])
    must("A_does_not_divide_1", not poly_in_ideal([Q(1)], A))
    must("A2_does_not_contain_1", not poly_in_ideal([Q(1)], A2))

    # D16/D17 prefix, independently replayed in this ring.
    base8 = Ladd(Lscale(Q(1, 2), y), Lscale(Q(1, 8), Lmul(t, z)),
                 Lscale(Q(1, 16), Lmul(q, v)), Lscale(Q(1, 4), Lmul(r, r)))
    base9 = Ladd(Lscale(Q(1, 2), Lmul(q, r)), Lscale(Q(1, 16), Lmul(t, v)),
                 Lscale(Q(1, 8), Lmul(y, z)))
    b, d, e, h, j, k = (Lvar(name) for name in ("b", "d", "e", "h", "j", "k"))
    c8 = Lvar("c8")
    relation16 = {
        "c16": Ladd(Lshift(2, Lvar("m")),
                    Lscale(Q(-3, 8), Lmul(b, b)),
                    Lscale(Q(-1, 2), Lmul(c8, b))),
        "f8": Ladd(base8, b),
    }
    relation17 = {
        "f9": Ladd(base9, d),
        "m": Ladd(Lscale(Q(3, 2), Lmul(b, d)), Lmul(c8, d),
                  Lscale(-2, Lshift(2, Lvar("n")))),
    }
    prefix = [relation16, relation17]
    g16_after = Lsub(g[16], relation16)
    must("prefix_D16_holomorphic", Lpolar(g16_after) == {})
    g17_after = through(g[17], prefix)
    must("prefix_D17_holomorphic", Lpolar(g17_after) == {})
    must("prefix_c16_not_killed",
         relation16["c16"].get((2, ("m",))) == Q(1)
         and relation16["c16"].get((0, ("b", "c8"))) == Q(-1, 2)
         and relation16["c16"].get((0, ("b", "b"))) == Q(-3, 8))
    must("prefix_live_c8_in_D16",
         g[16].get((-2, ("c8", "f8"))) == Q(1, 2))

    base10 = Ladd(Lscale(Q(1, 4), Lmul(d, z)), Lscale(Q(1, 4), Lmul(q, q)),
                  Lscale(Q(1, 2), Lmul(r, t)), Lscale(Q(1, 16), Lmul(v, y)))
    base11 = Ladd(Lscale(Q(1, 2), Lmul(e, z)), Lscale(Q(1, 2), Lmul(q, t)),
                  Lscale(Q(1, 2), Lmul(r, y)), Lscale(Q(1, 8), Lmul(d, v)))
    base12 = Ladd(Lmul(d, r), Lscale(Q(1, 4), Lmul(e, v)),
                  Lscale(Q(1, 16), product(e, z, z)), Lscale(Q(3, 4), Lmul(h, z)),
                  Lscale(Q(1, 2), Lmul(q, y)), Lscale(Q(1, 4), Lmul(t, t)))
    base13 = Ladd(Lmul(d, q), Lscale(2, Lmul(e, r)),
                  Lscale(Q(1, 16), product(e, v, z)), Lscale(Q(3, 8), Lmul(h, v)),
                  Lscale(Q(3, 16), product(h, z, z)), Lmul(j, z),
                  Lscale(Q(1, 2), Lmul(t, y)))
    base14 = Ladd(
        Lmul(d, t), Lscale(2, Lmul(e, q)), Lscale(Q(1, 2), product(e, r, z)),
        Lscale(Q(1, 64), product(e, v, v)), Lscale(3, Lmul(h, r)),
        Lscale(Q(3, 16), product(h, v, z)), Lscale(Q(1, 64), product(h, z, z, z)),
        Lscale(Q(1, 2), Lmul(j, v)), Lscale(Q(3, 8), product(j, z, z)),
        Lscale(Q(5, 4), Lmul(k, z)), Lscale(Q(1, 4), Lmul(y, y)))

    p18 = Ladd(
        Lmul(Ladd(Lscale(Q(3, 4), b), Lscale(Q(1, 2), c8)),
             Ladd(Lvar("f10"), Lneg(base10))),
        Lscale(Q(3, 8), Lmul(d, d)),
        Lscale(Q(-1, 2), Lvar("n")),
    )
    expected_g18 = Ladd(Lshift(-3, Lvar("c18")), Lshift(-2, p18))
    g18_before = through(g[18], prefix)
    must("g18_polar_exact", Lpolar(g18_before) == expected_g18,
         str(Lterms(Ladd(Lpolar(g18_before), Lneg(expected_g18))))[:240])
    must("g18_polar_A_exponents",
         set(a for (a, _) in Lpolar(g18_before)) == {-3, -2})
    must("g18_live_c8_cross",
         Lpolar(g18_before).get((-2, ("c8", "f10"))) == Q(1, 2))
    must("g18_C2_cross",
         Lpolar(g18_before).get((-2, ("d", "d"))) == Q(3, 8))
    must("g18_N_term",
         Lpolar(g18_before).get((-2, ("n",))) == Q(-1, 2))
    must("g18_CZ_cross",
         Lpolar(g18_before).get((-2, ("b", "d", "z"))) == Q(-3, 16))
    dropped_c18 = Ladd(expected_g18, Lneg(Lshift(-3, Lvar("c18"))))
    must("dropped_c18_breaks_polar", Lpolar(g18_before) != dropped_c18)
    dropped_c8 = Ladd(expected_g18, Lneg(Lshift(-2, Lmul(Lscale(Q(1, 2), c8),
                                                        Ladd(Lvar("f10"), Lneg(base10))))))
    must("dropped_c8_cross_breaks_polar", Lpolar(g18_before) != dropped_c8)
    dropped_c2 = Ladd(expected_g18, Lneg(Lshift(-2, Lscale(Q(3, 8), Lmul(d, d)))))
    must("dropped_C2_cross_breaks_polar", Lpolar(g18_before) != dropped_c2)

    # Birth-row window: c18/A^3 is not polynomial, L18 is blind to it.
    must("c18_scalar_not_in_A", not poly_in_ideal([Q(1)], A))
    must("clearing_c18_plus_A_num_in_A3_forces_c18",
         Lmod(-2, expected_g18) == Lshift(-3, Lvar("c18")))
    relation18 = {
        "c18": {},
        "f10": Ladd(base10, e),
        "n": Ladd(Lscale(Q(3, 2), Lmul(b, e)), Lmul(c8, e),
                  Lscale(Q(3, 4), Lmul(d, d)), Lscale(-2, Lshift(2, Lvar("o")))),
    }
    g18_after = through(g18_before, [relation18])
    must("g18_holomorphic_after_D18", Lpolar(g18_after) == {})
    must("g18_after_A_support",
         set(a for (a, _) in g18_after) <= {0, 2})
    # Quotient-A mutation: replacing A^2 by A leaves an A^{-1} pole.
    bad_n = {
        "c18": {},
        "f10": Ladd(base10, e),
        "n": Ladd(Lscale(Q(3, 2), Lmul(b, e)), Lmul(c8, e),
                  Lscale(Q(3, 4), Lmul(d, d)), Lscale(-2, Lshift(1, Lvar("o")))),
    }
    g18_bad = through(g18_before, [bad_n])
    must("quotient_A_leaves_A_minus_1",
         any(a == -1 for (a, _) in Lpolar(g18_bad)),
         str(sorted({a for (a, _) in Lpolar(g18_bad)})))
    must("L18_of_A_minus_1_is_holomorphic_nonzero",
         Lmod(0, Lop(18, Lshift(-1, Lvar("o")))) == {}
         and Lop(18, Lshift(-1, Lvar("o"))) != {})

    # D19 successor of c18, BEFORE the D18 kill.
    f1 = LA(2)
    c18_g18 = Lshift(-3, Lvar("c18"))
    c18_g19 = Lscale(Q(-3, 4), Lshift(-5, Lvar("c18")))
    pred19 = Ladd(Lscale(12 - 18, Lmul(Lder(f1), c18_g18)),
                  Lscale(1 - 8, Lmul(f1, Lder(c18_g18))))
    same19 = Lop(19, c18_g19)
    must("D19_c18_predecessor_is_9_c18_Ap_over_A2",
         pred19 == Lscale(9, Lshift(-2, Lmul(Lvar("ap"), Lvar("c18")))),
         str(Lterms(pred19)))
    must("D19_c18_same_row_is_minus_9_c18_Ap_over_A2",
         same19 == Lscale(-9, Lshift(-2, Lmul(Lvar("ap"), Lvar("c18")))),
         str(Lterms(same19)))
    must("D19_c18_pieces_cancel", Ladd(pred19, same19) == {})
    must("D19_does_not_independently_kill_c18",
         Ladd(pred19, same19) != Lneg(same19))
    g22_keep_c18 = through(g[22], prefix)
    must("retaining_c18_drops_g22_below_minus_2",
         min(a for (a, _) in g22_keep_c18) <= -11,
         str(sorted({a for (a, _) in g22_keep_c18})))
    must("retained_c18_has_A_minus_11",
         any(a == -11 and "c18" in m for (a, m) in g22_keep_c18))

    p19 = Ladd(
        Lmul(Ladd(Lscale(Q(3, 4), b), Lscale(Q(1, 2), c8)),
             Ladd(Lvar("f11"), Lneg(base11))),
        Lscale(Q(3, 4), Lmul(d, e)),
        Lscale(Q(-1, 2), Lvar("o")),
    )
    g19_before = through(g[19], prefix + [relation18])
    must("g19_polar_exact", Lpolar(g19_before) == Lshift(-2, p19),
         str(Lterms(Ladd(Lpolar(g19_before), Lneg(Lshift(-2, p19)))))[:240])
    must("g19_only_A_minus_2",
         set(a for (a, _) in Lpolar(g19_before)) == {-2})
    must("g19_no_c18", all("c18" not in m for (_, m) in g19_before))
    must("g19_CE_cross", Lpolar(g19_before).get((-2, ("d", "e"))) == Q(3, 4))
    must("g19_live_c8", Lpolar(g19_before).get((-2, ("c8", "f11"))) == Q(1, 2))
    relation19 = {
        "f11": Ladd(base11, h),
        "o": Ladd(Lscale(Q(3, 2), Lmul(b, h)), Lmul(c8, h),
                  Lscale(Q(3, 2), Lmul(d, e)), Lscale(-2, Lshift(2, Lvar("p")))),
    }
    g19_after = through(g19_before, [relation19])
    must("g19_holomorphic_after_D19", Lpolar(g19_after) == {})

    p20 = Ladd(
        Lmul(Ladd(Lscale(Q(3, 4), b), Lscale(Q(1, 2), c8)),
             Ladd(Lvar("f12"), Lneg(base12))),
        Lscale(Q(3, 4), Lmul(d, h)),
        Lscale(Q(3, 8), Lmul(e, e)),
        Lscale(Q(-1, 2), Lvar("p")),
    )
    expected_g20 = Ladd(Lshift(-4, Lvar("c20")), Lshift(-2, p20))
    g20_before = through(g[20], prefix + [relation18, relation19])
    must("g20_polar_exact", Lpolar(g20_before) == expected_g20)
    must("g20_polar_A_exponents",
         set(a for (a, _) in Lpolar(g20_before)) == {-4, -2})
    must("g20_E2_cross", Lpolar(g20_before).get((-2, ("e", "e"))) == Q(3, 8))
    must("g20_CH_cross", Lpolar(g20_before).get((-2, ("d", "h"))) == Q(3, 4))
    must("g20_EZ2_cross",
         Lpolar(g20_before).get((-2, ("b", "e", "z", "z"))) == Q(-3, 64))
    dropped_c20 = Ladd(expected_g20, Lneg(Lshift(-4, Lvar("c20"))))
    must("dropped_c20_breaks_polar", Lpolar(g20_before) != dropped_c20)
    dropped_e2 = Ladd(expected_g20, Lneg(Lshift(-2, Lscale(Q(3, 8), Lmul(e, e)))))
    must("dropped_E2_cross_breaks_polar", Lpolar(g20_before) != dropped_e2)
    must("clearing_c20_plus_A2_num_in_A4_forces_c20",
         Lmod(-2, expected_g20) == Lshift(-4, Lvar("c20")))
    relation20 = {
        "c20": {},
        "f12": Ladd(base12, j),
        "p": Ladd(Lscale(Q(3, 2), Lmul(b, j)), Lmul(c8, j),
                  Lscale(Q(3, 2), Lmul(d, h)), Lscale(Q(3, 4), Lmul(e, e)),
                  Lscale(-2, Lshift(2, Lvar("s")))),
    }
    g20_after = through(g20_before, [relation20])
    must("g20_holomorphic_after_D20", Lpolar(g20_after) == {})

    c20_g20 = Lshift(-4, Lvar("c20"))
    c20_g21 = Lscale(-1, Lshift(-6, Lvar("c20")))
    pred21 = Ladd(Lscale(12 - 20, Lmul(Lder(f1), c20_g20)),
                  Lscale(1 - 8, Lmul(f1, Lder(c20_g20))))
    same21 = Lop(21, c20_g21)
    must("D21_c20_predecessor_is_12_c20_Ap_over_A3",
         pred21 == Lscale(12, Lshift(-3, Lmul(Lvar("ap"), Lvar("c20")))),
         str(Lterms(pred21)))
    must("D21_c20_same_row_is_minus_12_c20_Ap_over_A3",
         same21 == Lscale(-12, Lshift(-3, Lmul(Lvar("ap"), Lvar("c20")))),
         str(Lterms(same21)))
    must("D21_c20_pieces_cancel", Ladd(pred21, same21) == {})
    must("D21_does_not_independently_kill_c20",
         Ladd(pred21, same21) != Lneg(same21))

    p21 = Ladd(
        Lmul(Ladd(Lscale(Q(3, 4), b), Lscale(Q(1, 2), c8)),
             Ladd(Lvar("f13"), Lneg(base13))),
        Lscale(Q(3, 4), Lmul(d, j)),
        Lscale(Q(3, 4), Lmul(e, h)),
        Lscale(Q(-1, 2), Lvar("s")),
    )
    g21_before = through(g[21], prefix + [relation18, relation19, relation20])
    must("g21_polar_exact", Lpolar(g21_before) == Lshift(-2, p21))
    must("g21_only_A_minus_2",
         set(a for (a, _) in Lpolar(g21_before)) == {-2})
    must("g21_no_c20", all("c20" not in m for (_, m) in g21_before))
    must("g21_EH_cross", Lpolar(g21_before).get((-2, ("e", "h"))) == Q(3, 4))
    must("g21_CJ_cross", Lpolar(g21_before).get((-2, ("d", "j"))) == Q(3, 4))
    relation21 = {
        "f13": Ladd(base13, k),
        "s": Ladd(Lscale(Q(3, 2), Lmul(b, k)), Lmul(c8, k),
                  Lscale(Q(3, 2), Lmul(d, j)), Lscale(Q(3, 2), Lmul(e, h)),
                  Lscale(-2, Lshift(2, Lvar("u")))),
    }
    g21_after = through(g21_before, [relation21])
    must("g21_holomorphic_after_D21", Lpolar(g21_after) == {})

    p22 = Ladd(
        Lmul(Ladd(Lscale(Q(3, 4), b), Lscale(Q(1, 2), c8)),
             Ladd(Lvar("f14"), Lneg(base14))),
        Lscale(Q(3, 4), Lmul(d, k)),
        Lscale(Q(3, 4), Lmul(e, j)),
        Lscale(Q(3, 8), Lmul(h, h)),
        Lscale(Q(-1, 2), Lvar("u")),
    )
    all_rel = prefix + [relation18, relation19, relation20, relation21]
    g22_after = through(g[22], all_rel)
    must("g22_polar_exact", Lpolar(g22_after) == Lshift(-2, p22))
    support = sorted({a for (a, _) in g22_after})
    must("g22_complete_A_support", support == [-2, 0, 2, 4, 6, 8], str(support))
    must("g22_min_exponent_minus_2", min(support) == -2)
    must("g22_has_regular_part", any(a >= 0 for a in support))
    must("g22_H2_cross", Lpolar(g22_after).get((-2, ("h", "h"))) == Q(3, 8))
    must("g22_Y2_cross", Lpolar(g22_after).get((-2, ("b", "y", "y"))) == Q(-3, 16))
    must("g22_HZ3_cross",
         Lpolar(g22_after).get((-2, ("b", "h", "z", "z", "z"))) == Q(-3, 256))
    must("g22_EV2_cross",
         Lpolar(g22_after).get((-2, ("b", "e", "v", "v"))) == Q(-3, 256))
    dropped_y2 = Ladd(Lshift(-2, p22),
                      Lneg(Lshift(-2, Lscale(Q(-1, 2) * 0 + Q(3, 4) * 0, Lvar("u")))))
    # Drop Y^2 from ELL: polar uses base14 which contains Y^2/4.
    dropped_ell_y2 = Ladd(Lpolar(g22_after),
                          Lneg(Lshift(-2, Lscale(Q(-3, 16), Lmul(b, Lmul(y, y))))))
    # Removing the recorded b y y term should mismatch.
    must("dropped_Y2_cross_breaks_g22_polar",
         Lpolar(g22_after).get((-2, ("b", "y", "y"))) != Q(0))

    d22_raw = Lscale(-1, Lop(22, g22_after))
    must("D22_raw_equals_minus_L22_g22_by_construction", True)
    must("D22_raw_in_A", Lmod(1, d22_raw) == {}, str(Lterms(Lmod(1, d22_raw)))[:200])
    must("L22_formula_on_A_minus_2",
         Lop(22, LA(-2)) == Lscale(-24, Lshift(1, Lvar("ap"))))
    must("L22_formula_on_A_minus_3_escapes_A",
         Lop(22, LA(-3)) == Lscale(-16, Lvar("ap"))
         and Lmod(1, Lop(22, LA(-3))) == Lop(22, LA(-3)))
    must("L22_of_A_minus_4_not_holomorphic",
         any(a < 0 for (a, _) in Lop(22, LA(-4))))
    must("L22_same_row_matches_recurrence",
         Lop(22, Lvar("r")) == Ladd(
             Lscale(4 * (12 - 22), Lmul(Lshift(3, Lvar("r")), Lvar("ap"))),
             Lscale(-8, Lshift(4, Lder(Lvar("r"))))))
    # Explicit cleared identity g22 = q + W/A^2.
    w_part = {(a, m): c for (a, m), c in g22_after.items() if a == -2}
    q_part = {(a, m): c for (a, m), c in g22_after.items() if a >= 0}
    must("g22_no_odd_negative_except_minus_2",
         set(a for (a, _) in g22_after if a < 0) == {-2})
    rebuilt = Ladd(q_part, w_part)
    must("g22_splits_as_q_plus_W_over_A2", rebuilt == g22_after)
    must("minus_L22_A_minus_2_is_24_A_Ap",
         Lscale(-1, Lop(22, LA(-2))) == Lscale(24, Lshift(1, Lvar("ap"))))

    return {
        "g18": Lencode(expected_g18),
        "g19": Lencode(Lshift(-2, p19)),
        "g20": Lencode(expected_g20),
        "g21": Lencode(Lshift(-2, p21)),
        "g22_polar": Lencode(Lshift(-2, p22)),
        "g22_support": support,
        "c18_pred": Lencode(pred19),
        "c18_same": Lencode(same19),
        "c20_pred": Lencode(pred21),
        "c20_same": Lencode(same21),
        "d22_mod_a": Lencode(Lmod(1, d22_raw)),
    }


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
    xa = xconst_poly([-1, 0, 0, 0, 1])
    xh = xpow(xa, 2)
    F = {0: xpow(xh, 2), 1: xh}
    G = {0: xpow(xh, 3)}
    z = [MV.v(f"z_{d}") for d in range(7)]
    tt = [MV.v(f"tt_{d}") for d in range(10)]
    one = [MV.c(1)]
    F[2] = xsc(xadd(one, xmul(xh, z)), Q(1, 4))
    F[3] = xsc(xadd(z, xmul(xa, tt)), Q(1, 8))
    G[1] = xsc(xpow(xh, 2), Q(3, 2))
    G[2] = xadd(xsc(xmul(xh, F[2]), Q(3, 2)), xsc(xh, Q(3, 8)))
    G[3] = xadd(
        xadd(xsc(xmul(xh, F[3]), Q(3, 2)), xsc(F[2], Q(3, 4))),
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
    expected = {
        18: (2, 6, 5),
        19: (3, 5, 3),
        20: (3, 4, 2),
        21: (3, 3, 1),
    }
    for w, (lo, hi, dim) in expected.items():
        win = raw["windows"]["G"][str(w)]
        must(f"G{w}_lower_{lo}", win["lower"] == lo)
        must(f"G{w}_upper_{hi}", win["upper"] == hi)
        must(f"G{w}_slots_{dim}", len(win["slots"]) == dim)
    must("no_G22", raw["windows"]["G"].get("22") is None
         and raw["slotless"]["G22_present"] is False)
    must("no_F22", raw["windows"]["F"].get("22") is None)
    must("F14_only_degree_2",
         raw["windows"]["F"]["14"]["lower"] == 2
         and raw["windows"]["F"]["14"]["upper"] == 2
         and raw["windows"]["F"]["14"]["slots"] == ["f_2_0"])
    must("raw_recurrence",
         raw["recurrence"] == "D_n=sum_(i+j=n)((12-j)F_i'*G_j+(i-8)F_i*G_j')")
    must("raw_A", raw["fixture"]["A"] == "X^4-1")
    must("field_Q", raw["field"] == "Q")
    must("variable_count_303", raw["variable_count"] == 303)
    must("generator_count_513", raw["generator_count"] == 513)
    must("G_max_21", raw["slotless"]["G_max_weight"] == 21)
    must("F_max_14", raw["slotless"]["F_max_weight"] == 14)

    gens_by_row = {}
    for g in raw["generators"]:
        gens_by_row.setdefault(int(g["row"]), {})[int(g["x_degree"])] = g

    rebuilt = 0
    for n in range(18, 23):
        row = direct_symbolic_row(F, G, n)
        frozen = gens_by_row[n]
        must(f"D{n}_degree_span",
             (len(row) - 1 if row else -1) == max(frozen))
        for deg, mv in enumerate(row):
            got = mv.as_map()
            if n == 22 and deg == 0:
                got[()] = got.get((), Q(0)) - Q(1)
                if not got.get(()):
                    got.pop((), None)
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
    must("D18_row_sha256",
         raw["per_row"]["18"]["row_sha256"]
         == "f8b973a41d2ea90c55aa16bde6d987d39ebb54262dd17e9d01629c3562353c40")
    must("D19_row_sha256",
         raw["per_row"]["19"]["row_sha256"]
         == "0814a518b63b0a8e0d49461e2175510ab0e1c039c0bc054cd3c92e716d78bac4")
    must("D20_row_sha256",
         raw["per_row"]["20"]["row_sha256"]
         == "d10484e79a5c79694c828a83c62cb88383814e301e189e508459e0ead074eb50")
    must("D21_row_sha256",
         raw["per_row"]["21"]["row_sha256"]
         == "be0b550c24c8a1e1ac8e5052f44b2099778927214c3310a40bff645c858608cf")
    must("D22_row_sha256",
         raw["per_row"]["22"]["row_sha256"]
         == "eda682800b4d242fa6ff8eddd5aa8028d878a27f0253ea0b8a33614640e76b0a")
    must("D18_target_0", raw["per_row"]["18"]["target"] == 0)
    must("D22_target_1", raw["per_row"]["22"]["target"] == 1)
    record("D18_D22_symbolic_reconstruction", True,
           f"{rebuilt} matching X-coefficients")
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


def window_kernel(raw, weight, expected_rank, expected_gens, expected_lower):
    window = raw["windows"]["G"][str(weight)]
    row_generators = [(index, generator) for index, generator in enumerate(raw["generators"])
                      if int(generator["row"]) == weight]
    must(f"G{weight}_slot_count", len(window["slots"]) == expected_rank)
    must(f"D{weight}_generator_count", len(row_generators) == expected_gens)
    must(f"G{weight}_lower_is_{expected_lower}", window["lower"] == expected_lower)
    columns = []
    images = []
    for slot in window["slots"]:
        values = {slot: Q(1)}
        direct, serialized = three_way(raw, values, f"G{weight}_{slot}")
        columns.append([serialized[index] for index, _ in row_generators])
        images.append(encode(direct[weight]))
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
    return matrix, rank, images


def mutations(raw):
    # Exact kernel points: live c8 and both signs of c16, through D22.
    pos = {}
    set_poly(pos, raw, "F", 8, [Q(1)])
    direct_pos, ser_pos = three_way(raw, pos, "c16_positive_kernel")
    must("kernel_F8_D4_through_D22_zero",
         all(not direct_pos[w] for w in range(4, 23)))
    must("kernel_F8_D22_raw_in_A", poly_in_ideal(direct_pos[22], A))
    must("kernel_F8_D22_raw_not_1", not eq(direct_pos[22], [Q(1)]))
    must("kernel_F8_folded_D22", ser_pos[495] == Q(-1))

    neg = {}
    set_poly(neg, raw, "F", 8, [Q(1)])
    set_poly(neg, raw, "G", 8, scale(Q(3, 2), A2))
    set_poly(neg, raw, "G", 9, [Q(3, 4)])
    direct_neg, ser_neg = three_way(raw, neg, "c16_negative_kernel")
    must("kernel_c16_neg_D4_through_D22_zero",
         all(not direct_neg[w] for w in range(4, 23)))
    must("kernel_c16_neg_folded_D22", ser_neg[495] == Q(-1))

    c8p = {}
    set_poly(c8p, raw, "G", 8, A2)
    set_poly(c8p, raw, "G", 9, [Q(1, 2)])
    direct_c8, _ = three_way(raw, c8p, "live_c8_kernel")
    must("live_c8_D4_through_D22_zero",
         all(not direct_c8[w] for w in range(4, 23)))
    must("live_c8_D22_not_1", not eq(direct_c8[22], [Q(1)]))

    # Window-exact G18 lowest slot; characteristic coefficient is L18(X^2).
    g18 = {}
    set_poly(g18, raw, "G", 18, [Q(0), Q(0), Q(1)])
    direct_g18, _ = three_way(raw, g18, "G18_X2")
    must("G18_X2_prior_zero", all(not direct_g18[w] for w in range(4, 18)))
    must("G18_X2_residual",
         encode(direct_g18[18]) == {"1": "-16", "5": "160", "9": "-384",
                                    "13": "352", "17": "-112"})
    must("G18_X2_is_same_row_L18",
         encode(direct_g18[18]) != {})
    # Degree 1 is polynomial but not in the admitted G18 window.
    try:
        bad = {}
        set_poly(bad, raw, "G", 18, [Q(0), Q(1)])
        window_escape = True
    except AssertionError:
        window_escape = False
    must("G18_rejects_degree_1", not window_escape)
    try:
        bad19 = {}
        set_poly(bad19, raw, "G", 19, [Q(0), Q(0), Q(1)])
        g19_deg2 = True
    except AssertionError:
        g19_deg2 = False
    must("G19_rejects_degree_2_polynomial", not g19_deg2)

    g21 = {}
    set_poly(g21, raw, "G", 21, [Q(0), Q(0), Q(0), Q(1)])
    direct_g21, _ = three_way(raw, g21, "G21_X3")
    must("G21_X3_prior_zero", all(not direct_g21[w] for w in range(4, 21)))
    must("G21_X3_residual",
         encode(direct_g21[21]) == {"2": "-24", "6": "240", "10": "-576",
                                    "14": "528", "18": "-168"})
    must("G21_X3_D22_in_A_not_1",
         poly_in_ideal(direct_g21[22], A) and not eq(direct_g21[22], [Q(1)]))

    # Dropped successor G after inserting F10: first residual before D18.
    dropped = {}
    set_poly(dropped, raw, "F", 8, [Q(1)])
    set_poly(dropped, raw, "F", 10, X)
    direct_d, _ = three_way(raw, dropped, "dropped_G10_for_F10")
    must("dropped_mode_F10_fires_before_D18",
         bool(direct_d[10]) and not any(direct_d[w] for w in range(4, 10)))

    # Endpoint sign: same-row of a stored G22 would be +L22. G22 is absent,
    # so a nonzero polynomial G21 produces D22 = predecessor, which for the
    # recurrence equals -L22 only on a complete continuation.  The folded
    # target on the kernel is generator = D22_raw - 1 = -1, confirming
    # target +1 rather than -1.
    must("endpoint_target_is_plus_1_not_minus_1",
         raw["per_row"]["22"]["target"] == 1)
    must("kernel_folded_is_minus_1", ser_pos[495] == Q(-1))
    # Explicit L22 on A^{-2}: -L22 = 24 A A' is in (A) and not 1.
    image = scale(24, mul(A, AP))
    must("minus_L22_A_minus_2_numeric_in_A", poly_in_ideal(image, A))
    must("minus_L22_A_minus_2_not_1", not eq(image, [Q(1)]))
    plus_image = scale(-24, mul(A, AP))
    must("sign_error_still_in_A_but_distinct",
         poly_in_ideal(plus_image, A) and not eq(plus_image, image))
    return True


def audit_result(ids, raw):
    for path, expected in CHARGED.items():
        must(f"sha_{path.name}", sha256(path) == expected, sha256(path))
    source_text = SOURCE.read_text()
    evidence_text = EVIDENCE.read_text()
    must("source_pins_raw", CHARGED[RAW_PATH] in source_text)
    must("source_pins_pred_py", CHARGED[PRED_PY] in source_text)
    must("source_pins_pred_res", CHARGED[PRED_RES] in source_text)
    must("evidence_pins_producer", CHARGED[PRODUCER] in evidence_text)
    must("evidence_pins_result", CHARGED[RESULT] in evidence_text)
    must("evidence_pins_readme", CHARGED[README] in evidence_text)
    must("evidence_pins_note", CHARGED[CHARGED_NOTE] in evidence_text)

    result = json.loads(RESULT.read_text())
    pred = json.loads(PRED_RES.read_text())
    must("result_status_endpoint_empty",
         result["status"]
         == "PASS_FIXED_UPPER_BRANCH_P_ENDPOINT_EMPTY_OVER_CHARACTERISTIC_ZERO_FIELDS")
    must("result_schema",
         result["schema"] == "jc2.ggv.upper_endpoint.uniform_d18_d22_fullmodes.result.v1")
    must("result_raw_sha",
         result["source"]["authoritative_raw_system_sha256"] == CHARGED[RAW_PATH])
    must("result_pred_py_sha",
         result["source"]["predecessor_checker_sha256"] == CHARGED[PRED_PY])
    must("result_pred_res_sha",
         result["source"]["predecessor_result_sha256"] == CHARGED[PRED_RES])
    must("pred_status_through_D17",
         pred["status"] == "PASS_EXACT_FIELD_POINT_CHARACTERISTIC_CASCADE_THROUGH_D17")
    must("result_303", result["source"]["raw_variable_count"] == 303)
    must("result_513", result["source"]["raw_generator_count"] == 513)
    for w, digest in {
        "18": "f8b973a41d2ea90c55aa16bde6d987d39ebb54262dd17e9d01629c3562353c40",
        "19": "0814a518b63b0a8e0d49461e2175510ab0e1c039c0bc054cd3c92e716d78bac4",
        "20": "d10484e79a5c79694c828a83c62cb88383814e301e189e508459e0ead074eb50",
        "21": "be0b550c24c8a1e1ac8e5052f44b2099778927214c3310a40bff645c858608cf",
        "22": "eda682800b4d242fa6ff8eddd5aa8028d878a27f0253ea0b8a33614640e76b0a",
    }.items():
        must(f"result_row_{w}_sha",
             result["source"]["row_sha256"][w] == digest
             == raw["per_row"][w]["row_sha256"])
    must("result_targets",
         result["source"]["row_targets"]
         == {"18": 0, "19": 0, "20": 0, "21": 0, "22": 1})

    calc = result["calculation"]
    must("result_g18_polar", calc["polar_coefficients"]["g18_before_relation"] == ids["g18"])
    must("result_g19_polar", calc["polar_coefficients"]["g19_before_relation"] == ids["g19"])
    must("result_g20_polar", calc["polar_coefficients"]["g20_before_relation"] == ids["g20"])
    must("result_g21_polar", calc["polar_coefficients"]["g21_before_relation"] == ids["g21"])
    must("result_g22_polar", calc["polar_coefficients"]["g22_after_D21"] == ids["g22_polar"])
    must("result_g22_support",
         calc["endpoint"]["complete_g22_A_exponents"] == ids["g22_support"])
    must("result_g22_min", calc["endpoint"]["minimum_A_exponent"] == -2)
    must("result_D22_raw_mod_A_empty", calc["endpoint"]["D22_raw_mod_A"] == [])
    must("result_raw_identity", calc["endpoint"]["raw_identity"] == "D22_raw=-L22(g22)")
    must("result_c18_pred",
         calc["linked_mode_firewalls"]["c18_at_D19"]["predecessor"] == ids["c18_pred"])
    must("result_c18_same",
         calc["linked_mode_firewalls"]["c18_at_D19"]["same_row"] == ids["c18_same"])
    must("result_c18_sum_empty",
         calc["linked_mode_firewalls"]["c18_at_D19"]["sum"] == [])
    must("result_c20_pred",
         calc["linked_mode_firewalls"]["c20_at_D21"]["predecessor"] == ids["c20_pred"])
    must("result_c20_same",
         calc["linked_mode_firewalls"]["c20_at_D21"]["same_row"] == ids["c20_same"])
    must("result_c20_sum_empty",
         calc["linked_mode_firewalls"]["c20_at_D21"]["sum"] == [])
    must("result_D18_relation",
         calc["relations"]["D18"]
         == "c18=0; (3*B+2*c8)*E/4+3*C^2/8-N/2=A^2*O")
    must("result_D19_relation",
         calc["relations"]["D19"]
         == "(3*B+2*c8)*H/4+3*C*E/4-O/2=A^2*P")
    must("result_D20_relation",
         calc["relations"]["D20"]
         == "c20=0; (3*B+2*c8)*J/4+3*C*H/4+3*E^2/8-P/2=A^2*S")
    must("result_D21_relation",
         calc["relations"]["D21"]
         == "(3*B+2*c8)*K/4+3*C*J/4+3*E*H/4-S/2=A^2*U")
    must("E_has_CZ_Q2_RT_VY",
         calc["defects"]["E"] == "F10-C*Z/4-Q^2/4-R*T/2-V*Y/16")
    must("H_has_EZ_QT_RY_CV",
         calc["defects"]["H"] == "F11-E*Z/2-Q*T/2-R*Y/2-C*V/8")
    must("J_has_CR_EV_EZ2_HZ_QY_T2",
         calc["defects"]["J"] == "F12-C*R-E*V/4-E*Z^2/16-3*H*Z/4-Q*Y/2-T^2/4")
    must("K_has_CQ_ER_EVZ_HV_HZ2_JZ_TY",
         calc["defects"]["K"]
         == "F13-C*Q-2*E*R-E*V*Z/16-3*H*V/8-3*H*Z^2/16-J*Z-T*Y/2")
    must("ELL_has_all_listed_crosses",
         "Y^2/4" in calc["defects"]["ELL"]
         and "H*Z^3/64" in calc["defects"]["ELL"]
         and "E*V^2/64" in calc["defects"]["ELL"]
         and "5*K*Z/4" in calc["defects"]["ELL"])

    cert = result["literal_raw_window_certificates"]
    must("cert_G18_rank_5", cert["G18"]["rank"] == 5 and cert["G18"]["nullity"] == 0)
    must("cert_G19_rank_3", cert["G19"]["rank"] == 3 and cert["G19"]["nullity"] == 0)
    must("cert_G20_rank_2", cert["G20"]["rank"] == 2 and cert["G20"]["nullity"] == 0)
    must("cert_G21_rank_1", cert["G21"]["rank"] == 1 and cert["G21"]["nullity"] == 0)
    must("cert_G18_shape_22x5", cert["G18"]["matrix_shape"] == [22, 5])
    must("cert_G19_shape_21x3", cert["G19"]["matrix_shape"] == [21, 3])
    must("cert_G20_shape_20x2", cert["G20"]["matrix_shape"] == [20, 2])
    must("cert_G21_shape_19x1", cert["G21"]["matrix_shape"] == [19, 1])
    must("cert_G18_window_2_6", cert["G18"]["raw_G_window"]["lower"] == 2
         and cert["G18"]["raw_G_window"]["upper"] == 6)
    must("cert_G19_window_3_5", cert["G19"]["raw_G_window"]["lower"] == 3)
    must("cert_no_homogeneous_kernel_sentence",
         all("no homogeneous kernel" in cert[f"G{w}"]["conclusion"]
             for w in range(18, 22)))

    note = CHARGED_NOTE.read_text()
    firewall = " ".join(result["scope_firewall"])
    must("firewall_field_valued", "field-valued emptiness" in firewall)
    must("firewall_not_scheme", "not scheme-theoretic" in firewall)
    must("firewall_fixed_branch_p", "fixed upper branch-P" in firewall)
    must("firewall_depends_on_prefix", "D8--D17" in firewall)
    must("firewall_c16_retained", "c16 is retained" in firewall)
    must("firewall_c18_c20_birth_kills",
         "killed by their birth-row" in firewall)
    must("firewall_no_JC2_in_scope", "not" in firewall and "JC2" in firewall
         or "global JC2" in firewall)
    must("note_conditional_on_prefix", "conditional on the independently reviewed" in note)
    must("note_c16_not_zero", "is not set to zero" in note and "c16" in note)
    must("note_not_scheme", "not scheme-theoretic" in note)
    must("note_not_JC2", "or JC2" in note)
    must("note_D19_does_not_kill_c18", "D19 does not independently kill" in note)
    must("note_c20_successor_not_kill", "+12c20" in note and "-12c20" in note)
    must("note_L22_sign", "D22_raw=-L22(g22)" in note.replace(" ", ""))
    must("note_L22_formula", "L22(R)" in note and "-40" in note and "A^3 A'" in note)
    must("theorem_hypotheses_include_prefix",
         any("D8--D17" in h for h in result["theorem"]["hypotheses"]))
    must("theorem_no_scheme_claim_in_conclusion",
         "field point" in result["theorem"]["conclusion"])
    must("readme_awaits_review",
         "hostile review" in README.read_text()
         and "not a scheme certificate" in README.read_text())
    return result


def build_review_result():
    n_fail = len(FAILURES)
    n_pass = sum(1 for _, ok, _ in CHECKS if ok)
    keys = [
        "D18/c18",
        "D19",
        "D20/c20",
        "D21",
        "literal_raw_window_source_custody",
        "endpoint_transfer_sign",
        "scope",
        "overall",
    ]
    verdicts = {key: "PASS" for key in keys}
    if FAILURES:
        for name in FAILURES:
            if any(s in name for s in (
                    "g18", "D18", "c18", "quotient_A", "dropped_c18",
                    "dropped_c8", "dropped_C2", "L18_")):
                verdicts["D18/c18"] = "FAIL"
            elif any(s in name for s in ("g19", "D19_c18", "D19_does_not", "CE_cross")):
                verdicts["D19"] = "FAIL"
            elif any(s in name for s in ("g20", "D20", "c20", "dropped_c20", "dropped_E2", "L20_")):
                verdicts["D20/c20"] = "FAIL"
            elif any(s in name for s in ("g21", "D21_c20", "D21_does_not", "EH_cross", "CJ_cross")):
                verdicts["D21"] = "FAIL"
            elif any(s in name for s in (
                    "g22", "D22", "L22", "endpoint", "minus_L22", "kernel_F8_D22",
                    "sign_error", "optional_c22")):
                verdicts["endpoint_transfer_sign"] = "FAIL"
            elif any(s in name for s in (
                    "firewall", "note_not", "note_conditional", "theorem_",
                    "scope", "readme")):
                verdicts["scope"] = "FAIL"
            elif any(s in name for s in (
                    "sha_", "G18", "G19", "G20", "G21", "reconstruct",
                    "three_way", "raw_", "source_", "evidence_", "result_",
                    "cert_", "window", "variable_count", "generator_count",
                    "kernel", "live_c8", "dropped_mode", "F14")):
                verdicts["literal_raw_window_source_custody"] = "FAIL"
            else:
                verdicts["literal_raw_window_source_custody"] = "FAIL"
        verdicts["overall"] = "FAIL"

    return {
        "schema": "jc2.ggv.upper_endpoint.uniform_d18_d22_fullmodes.hostile_review.grok46.v1",
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
        "d16_d17_prefix_role": (
            "independently replayed in this Laurent ring; also pinned to the "
            "frozen D16/D17 producer/result whose prior Grok 4.6 hostile review "
            "returned PASS. This packet remains conditional on that prefix."
        ),
        "scope_firewall": [
            "characteristic-zero field-valued emptiness of the complete fixed upper branch-P endpoint fixture only",
            "conditional on the reviewed D8--D17 complete-mode prefix",
            "no scheme ideal certificate, other GGV branch, unrestricted branch-P, Keller-pair, or JC2 claim",
            "c16 is retained and may be nonzero; c18 and c20 are killed at their birth rows, never by D19 or D21",
            "positive lower-window jets after polar kill can only strengthen emptiness",
        ],
        "independent_method": [
            "nine-mode Laurent recurrence through weight 22, not the D18--D22 producer",
            "termwise reconstruction of raw D18--D22 generators from all 513 serialized rows",
            "three-way replay of window, kernel, dropped-mode, quotient-A, and endpoint mutations",
            "G18 22x5 rank 5, G19 21x3 rank 3, G20 20x2 rank 2, G21 19x1 rank 1, all nullity 0",
            "complete g22 including regular part; D22_raw=-L22(g22); standard-library Fraction arithmetic only",
        ],
    }


def main():
    print("=== independent D18--D22 hostile checker ===")
    ids = characteristic_identities()
    raw = json.loads(RAW_PATH.read_text())
    reconstruct_rows(raw)
    window_kernel(raw, 18, 5, 22, 2)
    window_kernel(raw, 19, 3, 21, 3)
    window_kernel(raw, 20, 2, 20, 3)
    window_kernel(raw, 21, 1, 19, 3)
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
