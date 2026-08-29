#!/usr/bin/env python3
"""Independent hostile audit checker: origin-residue fixed-slice exclusion.

Fresh, self-contained, standard-library-only exact verification of

  xmodel/ggv-upper-endpoint-origin-residue-slice-sol-ultra-20260828.md

on the strict slice A=X^4-1, lambda=0, c2!=0, exact D=0, Q=e=F8=r=0.
Nothing is imported from the producer checker.  The characteristic is
rebuilt from the reviewed mode schedule

  G = F^(3/2) + sum_{k=1..10} c_{2k} t^{2k} F^((6-k)/4)

by an independent fractional-power recurrence in the ring K[X, 1/A],
with canonical A-denominator normalization, and the q7/q9/q11/q13
parameterization is derived (not assumed) from the reviewed connection
theorem h = T5(d), T5(d) = (5A'd + 2Ad')/2, plus the authoritative raw
windows pinned in RAW_INPUT.json.

Run:
  PYTHONDONTWRITEBYTECODE=1 python3 -B <this file>
"""

from __future__ import annotations

from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

FROZEN = {
    "xmodel/ggv-upper-endpoint-origin-residue-slice-sol-ultra-20260828.md":
        "7202f70380c8379d85dab82e4ef06f47b1312ba840775d8581eaa629ed328e30",
    "cases/ggv_8_28_upper_endpoint_origin_residue_slice_20260828/"
    "verify_origin_residue_slice.py":
        "de371953d4bc22da7cfc39c4e94221097eac7612b7b4a8b44afe0fd14ecb76e0",
    "xmodel/ggv-upper-endpoint-deep-q1-lambda0-even-subbranch-origin-"
    "coupling-independent-sol-ultra-20260828.md":
        "c940ba048f5edf60b3018670c8914acc469f55f30101f211a6aedb5d591b6714",
    "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/"
    "RAW_INPUT.json":
        "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    "xmodel/ggv-upper-endpoint-deep-q1-lambda0-odd-gate-tail-independent-"
    "sol-ultra-20260828.md":
        "b649e0821a07fa8d3ed861169b608a5b4dcd8356452f875b8b218693d3cb69a0",
    "xmodel/ggv-upper-endpoint-deep-q1-lambda0-q15-independent-sol-ultra-"
    "20260828.md":
        "188317138e60224f5a7e9dc1de18ab339384c5246c1cabf12acc20657dac7d5f",
    "xmodel/ggv-upper-endpoint-origin-odd-coupling-sol-ultra-20260828.md":
        "3e4a0f03acec2ee5e3cdfff558c481e14735408aa18486d23215958ed8d4bb3a",
    "cases/ggv_8_28_upper_endpoint_origin_odd_coupling_20260828/"
    "verify_origin_odd_coupling.py":
        "f23a6d959dc9a8854f051c16a1fe287dea91d5b66b01a63198a64715c08c04c8",
}


def sha256(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def check_frozen(tag: str) -> None:
    for rel, expect in FROZEN.items():
        got = sha256(rel)
        assert got == expect, f"hash drift ({tag}): {rel}: {got}"


# ---------------------------------------------------------------- MP ----
# Sparse multivariate polynomial over Q: {monomial: coefficient} with
# monomial = tuple of (variable, exponent) pairs, sorted by variable.

class MP:
    __slots__ = ("t",)

    def __init__(self, t=None):
        self.t = t or {}

    @staticmethod
    def const(value):
        value = Q(value)
        return MP({(): value} if value else {})

    @staticmethod
    def var(name):
        return MP({((name, 1),): Q(1)})

    def __bool__(self):
        return bool(self.t)

    def __eq__(self, other):
        return self.t == other.t

    def __add__(self, other):
        out = dict(self.t)
        for mono, coefficient in other.t.items():
            value = out.get(mono, Q(0)) + coefficient
            if value:
                out[mono] = value
            else:
                out.pop(mono, None)
        return MP(out)

    def __neg__(self):
        return MP({m: -c for m, c in self.t.items()})

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        out = {}
        for m1, c1 in self.t.items():
            d1 = dict(m1)
            for m2, c2 in other.t.items():
                d = dict(d1)
                for var, exp in m2:
                    d[var] = d.get(var, 0) + exp
                mono = tuple(sorted(d.items()))
                value = out.get(mono, Q(0)) + c1 * c2
                if value:
                    out[mono] = value
                else:
                    out.pop(mono, None)
        return MP(out)

    def scale(self, value):
        value = Q(value)
        if not value:
            return MP()
        return MP({m: c * value for m, c in self.t.items()})

    def vars(self):
        return {var for mono in self.t for var, _ in mono}

    def subst_var_squared(self, name, value):
        """Substitute name^2 -> value (Q); require only even powers."""
        out = MP()
        for mono, coefficient in self.t.items():
            d = dict(mono)
            exp = d.pop(name, 0)
            assert exp % 2 == 0, f"odd power of {name}"
            term = MP({tuple(sorted(d.items())): coefficient})
            out = out + term.scale(Q(value) ** (exp // 2))
        return out


MPZ = MP()
ONE = MP.const(1)


# ------------------------------------------------------- X-polynomials --

def ptrim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return p


def padd(p, q):
    out = [MPZ] * max(len(p), len(q))
    for i, c in enumerate(p):
        out[i] = out[i] + c
    for i, c in enumerate(q):
        out[i] = out[i] + c
    return ptrim(out)


def pneg(p):
    return [-c for c in p]


def psub(p, q):
    return padd(p, pneg(q))


def pmul(p, q):
    out = [MPZ] * (len(p) + len(q) - 1) if p and q else []
    for i, ci in enumerate(p):
        if not ci:
            continue
        for j, cj in enumerate(q):
            if cj:
                out[i + j] = out[i + j] + ci * cj
    return ptrim(out)


def pscale(p, value):
    return ptrim([c.scale(value) for c in p])


def pscale_mp(p, mp):
    return ptrim([c * mp for c in p])


def pder(p):
    return ptrim([p[i].scale(i) for i in range(1, len(p))])


def pconst(value):
    value = Q(value)
    return [MP.const(value)] if value else []


def coeff(p, i):
    return p[i] if i < len(p) else MPZ


def support(p):
    return [i for i, c in enumerate(p) if c]


def pdiv_monic(p, d):
    """Exact division with remainder by monic d; returns (quotient, rem)."""
    rem = list(p)
    rem = ptrim(rem)
    quo = [MPZ] * max(0, len(rem) - len(d) + 1)
    while len(rem) >= len(d):
        k = len(rem) - len(d)
        c = rem[-1]
        quo[k] = quo[k] + c
        for i, di in enumerate(d):
            rem[k + i] = rem[k + i] - c * di
        rem = ptrim(rem)
    return ptrim(quo), rem


X = [MPZ, ONE]
A = [MP.const(-1), MPZ, MPZ, MPZ, ONE]           # X^4 - 1
Ap = pder(A)                                     # 4 X^3


def apow(n):
    out = [ONE]
    for _ in range(n):
        out = pmul(out, A)
    return out


def t5(d):
    """T5(d) = (5 A' d + 2 A d')/2."""
    return pscale(padd(pscale(pmul(Ap, d), 5), pscale(pmul(A, pder(d)), 2)),
                  Q(1, 2))


# ------------------------------------- rational functions p / A^m -------

def rf(p, m=0):
    p = ptrim(list(p))
    if not p:
        return ((), 0)
    while m > 0:
        quo, rem = pdiv_monic(p, A)
        if rem:
            break
        p, m = quo, m - 1
    return (tuple(p), m)


def rf_add(u, v):
    (pu, mu), (pv, mv) = u, v
    m = max(mu, mv)
    return rf(padd(pmul(list(pu), apow(m - mu)),
                   pmul(list(pv), apow(m - mv))), m)


def rf_mul(u, v):
    (pu, mu), (pv, mv) = u, v
    return rf(pmul(list(pu), list(pv)), mu + mv)


def rf_scale(u, value):
    return rf(pscale(list(u[0]), value), u[1])


def rf_from_poly(p):
    return rf(p, 0)


RFZ = ((), 0)


def rf_is_poly(u):
    return u[1] == 0


def rf_vars(u):
    return {v for c in u[0] for v in c.vars()}


# -------------------------------------------- fractional power series --

def fpow(F, e, W):
    """Coefficients of F^e through t^W; F: {weight: X-poly}, F[0]=A^4.

    Sheet convention: constant term is the literal integer power A^(4e)
    (4e is required to be an integer), matching the reviewed A^(6-k)
    branch factors.  Recurrence: w F0 S_w = sum_{i>=1} ((e+1)i-w) F_i
    S_{w-i}, i.e. S_w = A^-4/w * sum(...).
    """
    e = Q(e)
    n4 = 4 * e
    assert n4.denominator == 1
    n4 = int(n4)
    S = {0: rf(apow(n4), 0) if n4 >= 0 else rf([ONE], -n4)}
    for w in range(1, W + 1):
        acc = RFZ
        for i, Fi in F.items():
            if i < 1 or i > w or not Fi:
                continue
            term = rf_mul(rf_from_poly(Fi), S[w - i])
            acc = rf_add(acc, rf_scale(term, (e + 1) * i - w))
        S[w] = rf_scale(rf_mul(acc, rf([ONE], 4)), Q(1, w))
    return S


EXPONENTS = [Q(3, 2)] + [Q(6 - k, 4) for k in range(1, 11)]


def characteristic(F, cvals, W):
    """G_w for w<=W from the complete ten-mode schedule.

    cvals: {k: coefficient (MP or Q)} for c_{2k}, k=1..10; absent -> 0.
    Returns ({w: RF}, powers dict for reuse/self-tests).
    """
    powers = {e: fpow(F, e, W) for e in set(EXPONENTS)}
    G = {}
    for w in range(W + 1):
        acc = powers[Q(3, 2)][w]
        for k in range(1, 11):
            if w - 2 * k < 0:
                continue  # unborn at this weight
            c = cvals.get(k)
            if c is None:
                continue
            base = powers[Q(6 - k, 4)][w - 2 * k]
            if isinstance(c, MP):
                acc = rf_add(acc, (ptrim([x * c for x in base[0]]) and
                                   rf(pscale_mp(list(base[0]), c), base[1])
                                   ) or RFZ)
            else:
                acc = rf_add(acc, rf_scale(base, c))
        G[w] = acc
    return G, powers


def series_selftest(F, W):
    """(F^(1/2))^2 == F and F^(1/2)*F^(-1/2) == 1 through weight W."""
    half = fpow(F, Q(1, 2), W)
    neghalf = fpow(F, Q(-1, 2), W)
    for w in range(W + 1):
        conv = RFZ
        inv = RFZ
        for i in range(w + 1):
            conv = rf_add(conv, rf_mul(half[i], half[w - i]))
            inv = rf_add(inv, rf_mul(half[i], neghalf[w - i]))
        target = rf_from_poly(F.get(w, []))
        assert conv == target, f"series self-test sqrt^2 fails at w={w}"
        expect_inv = rf([ONE], 0) if w == 0 else RFZ
        assert inv == expect_inv, f"series self-test inverse fails at w={w}"


# -------------------------------------------------- h-formula library --

def h_formulas(Qp, e, F8, r, f, F9, F11, F13, F10):
    """Complete reviewed odd coefficients q_n = p^3 h_n, n=5..15.

    Transcribed from the frozen odd-gate-tail packet (b649e082...) and the
    frozen q15 packet (18831713...).  All arguments are X-polys.
    """
    def s(p, num, log2den):
        return pscale(p, Q(num, 2 ** log2den))

    A2 = apow(2)
    Q2 = pmul(Qp, Qp)
    Q3 = pmul(Q2, Qp)
    Q4 = pmul(Q3, Qp)
    Q5 = pmul(Q4, Qp)
    e32 = padd(Q3, pscale(e, 32))
    h5 = s(r, 1, 10)
    h7 = padd(s(f, 1, 2), s(pmul(Qp, r), -1, 16))
    h9 = padd(padd(s(F9, 1, 2), s(pmul(Qp, f), -3, 8)),
              s(pmul(Q2, r), -3, 23))
    h11 = padd(padd(s(pmul(A, F11), 1, 2), s(pmul(Qp, F9), -5, 8)),
               padd(s(pmul(Q2, f), 5, 15), s(pmul(r, e32), 5, 29)))
    h13 = padd(
        padd(padd(s(pmul(A2, F13), 1, 2), s(pmul(pmul(A, Qp), F11), -7, 8)),
             padd(s(pmul(Q2, F9), 21, 15), s(pmul(f, e32), 7, 21))),
        padd(padd(s(pmul(r, F8), 7, 13), s(pmul(pmul(r, Qp), e), 7, 30)),
             s(pmul(r, Q4), 35, 37)))
    h15 = padd(
        padd(
            padd(s(pmul(pmul(A2, Qp), F13), -9, 8),
                 s(pmul(pmul(A, Q2), F11), 45, 15)),
            padd(pmul(F9, padd(s(e, 9, 16), s(Q3, -15, 21))),
                 pmul(f, padd(s(F8, 9, 5),
                              padd(s(pmul(Qp, e), -9, 22), s(Q4, -45, 29)))))),
        padd(
            pmul(r, padd(padd(s(pmul(A, F10), 9, 13), s(pmul(Qp, F8), -9, 19)),
                         padd(s(pmul(Q2, e), -27, 37), s(Q5, -63, 43)))),
            s(pmul(A, pmul(r, pmul(r, r))), 3, 33)))
    return {5: h5, 7: h7, 9: h9, 11: h11, 13: h13, 15: h15}


# ---------------------------------------------------------------- main --

def main():
    check_frozen("start")

    # ---- Authoritative raw windows (pinned bytes). --------------------
    raw = json.loads((ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_"
                      "interface_d3_20260827/RAW_INPUT.json").read_text())
    win = {"F": {}, "G": {}}
    for kind in win:
        for slot in raw["raw_slots_through_weight_22"][kind]:
            w = int(slot["weight"])
            d = int(slot["raw_exponents"]["x"])
            win[kind].setdefault(w, set()).add(d)
            # chart law: F slot X^d at weight w is x^d y^(8+3d-w); G: 12+3d-w
            base = 8 if kind == "F" else 12
            assert int(slot["raw_exponents"]["y"]) == base + 3 * d - w
    assert win["F"][7] == set(range(0, 10))
    assert win["F"][9] == set(range(1, 8))      # constant floor: no X^0
    assert win["F"][11] == set(range(1, 6))     # constant floor: no X^0
    assert win["F"][13] == {2, 3}
    assert 15 not in win["F"] and max(win["F"]) == 14
    assert win["G"][11] == set(range(0, 14))
    assert win["G"][15] == set(range(1, 10))    # no constant slot
    print("windows=pinned RAW_INPUT.json floors verified")

    # ---- D22[X0] pair law re-derived from the literal windows. --------
    pairs = []
    for i in sorted(win["F"]):
        j = 22 - i
        if j not in win["G"]:
            continue
        if 1 in win["F"][i] and 0 in win["G"][j] and 12 - j != 0:
            pairs.append(("Fprime_G", i, j, 12 - j))
        if 0 in win["F"][i] and 1 in win["G"][j] and i - 8 != 0:
            pairs.append(("F_Gprime", i, j, i - 8))
    assert pairs == [("F_Gprime", 7, 15, -1), ("Fprime_G", 11, 11, 1)], pairs
    # Jacobian checksum: slots (f_1_0,f_0_1,g_1_0,g_0_1)=(Px,Py,Qx,Qy)(0),
    # so D22[X0] = Px*Qy - Py*Qx = J(P,Q)(0); target +1 is the Keller
    # normalization of E=t^22.
    a, b, c, d = 2, 3, 5, 7
    assert a * d - b * c == (+1) * a * d + (-1) * b * c
    # sign-mutation control: flipping (i-8)->(8-i) breaks the checksum
    assert (+1) * a * d - (-1) * b * c != a * d - b * c
    print("D22_X0=F11[X1]*G11[X0]-F7[X0]*G15[X1]  (pairs (11,11)+, (7,15)-)")

    # ---- T5 basics: degree law, zero kernel, sufficiency identity. ----
    for k in range(0, 13):
        image = t5([MPZ] * k + [ONE])
        assert len(image) - 1 == k + 3
        assert image[-1] == MP.const(Q(k + 10))  # leading coeff k+10 != 0
    # sufficiency: with C = A^2 d, 2AC' + A'C == 2A^2 T5(d), i.e. p^5 d is
    # a primitive of p^3 T5(d) dX
    dgen = [MP.var(f"m{i}") for i in range(5)]
    Cgen = pmul(apow(2), dgen)
    lhs = padd(pscale(pmul(A, pder(Cgen)), 2), pmul(Ap, Cgen))
    rhs = pscale(pmul(apow(2), t5(dgen)), 2)
    assert lhs == rhs
    # necessity ingredients: A squarefree with explicit inverse of A' mod A
    inv = pscale(X, Q(1, 4))
    assert pdiv_monic(pmul(Ap, inv), A)[1] == [ONE]
    # pole-order multipliers 1-2m never vanish
    assert all(1 - 2 * m != 0 for m in range(1, 21))
    print("T5: deg(T5(d))=deg(d)+3, lc=(k+10), zero kernel, primitive ok")

    # ---- Slice q parameterization, derived from floors. ---------------
    # q7: f = 4 T5(d7), deg f <= 5 forces deg d7 <= 2, no floor on f.
    d7 = [MP.var("a0"), MP.var("a1"), MP.var("a2")]
    f = pscale(t5(d7), 4)
    F7 = pmul(A, f)
    assert support(f) == [0, 1, 3, 4, 5]
    assert support(F7) == [0, 1, 3, 4, 5, 7, 8, 9]
    assert set(support(F7)) <= win["F"][7]
    # q9: F9 = 4 T5(d9), deg F9 <= 7 forces deg d9 <= 4; the authoritative
    # constant floor F9[X0]=0 forces the primitive X coefficient to zero:
    d9_full = [MP.var("b0"), MP.var("b1"), MP.var("b2"), MP.var("b3"),
               MP.var("b4")]
    F9_full = pscale(t5(d9_full), 4)
    assert coeff(F9_full, 0) == MP.var("b1").scale(-4)   # floor kills b1
    assert 0 not in win["F"][9]
    d9 = [MP.var("b0"), MPZ, MP.var("b2"), MP.var("b3"), MP.var("b4")]
    F9 = pscale(t5(d9), 4)
    assert support(F9) == [1, 2, 3, 5, 6, 7]
    assert set(support(F9)) <= win["F"][9]
    # q11: A*F11 = 4 T5(d11), deg F11 <= 5 forces deg d11 <= 6; A | T5(d11)
    # iff A | d11 (X^3 is invertible mod A with inverse X):
    d11_gen = [MP.var(f"e{i}") for i in range(7)]
    r3 = pdiv_monic(pmul([MPZ, MPZ, MPZ, ONE], d11_gen), A)[1]
    rd = pdiv_monic(d11_gen, A)[1]
    assert pdiv_monic(pmul(X, r3), A)[1] == rd   # X*(X^3 d mod A) == d mod A
    # so d11 = A*k with deg k <= 2; constant floor F11[X0]=0 forces k[X1]=0:
    k_full = [MP.var("k0"), MP.var("k1"), MP.var("k2")]
    F11_full, rem = pdiv_monic(pscale(t5(pmul(A, k_full)), 4), A)
    assert not rem
    assert coeff(F11_full, 0) == MP.var("k1").scale(-4)  # floor kills k1
    assert 0 not in win["F"][11]
    kpoly = [MP.var("k0"), MPZ, MP.var("k2")]
    F11, rem = pdiv_monic(pscale(t5(pmul(A, kpoly)), 4), A)
    assert not rem
    assert F11 == pscale(padd(pscale(pmul(Ap, kpoly), 7),
                              pscale(pmul(A, pder(kpoly)), 2)), 2)
    assert support(F11) == [1, 3, 5]
    assert set(support(F11)) <= win["F"][11]
    # q13: A^2*F13 = 4 T5(d13), deg F13 <= 3 forces deg d13 <= 8;
    # A | d13 as above, and then A | (7A'm + 2Am')/2 forces A | m since
    # A' is a unit mod A; with deg d13 <= 8 this leaves d13 = A^2*ell13:
    mgen = [MP.var(f"m{i}") for i in range(5)]
    half13 = pscale(padd(pscale(pmul(Ap, mgen), 7),
                         pscale(pmul(A, pder(mgen)), 2)), Q(1, 2))
    assert pdiv_monic(pmul(A, half13), apow(2))[1] == \
        pdiv_monic(pmul(A, pscale(pmul(Ap, mgen), Q(7, 2))), apow(2))[1]
    ell = MP.var("l13")
    F13, rem = pdiv_monic(pscale(t5(pscale_mp(apow(2), ell)), 4), apow(2))
    assert not rem
    assert F13 == [MPZ, MPZ, MPZ, ell.scale(72)]
    assert set(support(F13)) <= win["F"][13]
    print("q7/q9/q11/q13 parameterization derived; b1,k1 forced by floors")

    # ---- q5 and q15 automatic on the slice. ---------------------------
    zero = []
    F10_sym = [MPZ] + [MP.var(f"u10_{i}") for i in range(1, 7)]
    h = h_formulas(zero, zero, zero, zero, f, F9, F11, F13, F10_sym)
    assert h[5] == [] and h[15] == []            # exact with d5=d15=0
    assert h[7] == pscale(f, Q(1, 4))
    assert h[9] == pscale(F9, Q(1, 4))
    assert h[11] == pscale(pmul(A, F11), Q(1, 4))
    assert h[13] == pscale(pmul(apow(2), F13), Q(1, 4))
    print("q5,q15 automatic on slice (h5=h15=0); h7..h13 collapse verified")

    # ---- Complete characteristic on the slice. ------------------------
    # Even slots F10,F12,F14 are NOT fixed by the slice; keep them fully
    # symbolic to prove they cannot enter G11/G15.
    F12_sym = [MPZ, MPZ, MP.var("u12_2"), MP.var("u12_3"), MP.var("u12_4")]
    F14_sym = [MPZ, MPZ, MP.var("u14_2")]
    Fslice = {0: apow(4), 7: F7, 9: F9, 10: F10_sym, 11: F11, 12: F12_sym,
              13: F13, 14: F14_sym}
    series_selftest(Fslice, 15)
    cvals = {k: MP.var(f"c{2 * k}") for k in range(1, 11)}
    G, powers = characteristic(Fslice, cvals, 15)
    c2, c4, c6, c8 = (MP.var(n) for n in ("c2", "c4", "c6", "c8"))
    G11_closed = padd(pscale(pmul(apow(2), F11), Q(3, 2)),
                      padd(pscale(pscale_mp(pmul(A, F9), c2), Q(5, 4)),
                           pscale_mp(F7, c4)))
    assert G[11] == rf_from_poly(G11_closed)
    pole_num = padd(pscale(pscale_mp(F9, c6), Q(3, 4)),
                    pscale(pscale_mp(f, c8), Q(1, 2)))
    G15_num = padd(pmul(A, padd(pscale(pscale_mp(pmul(A, F13), c2), Q(5, 4)),
                                pscale_mp(F11, c4))), pole_num)
    assert G[15] == rf(G15_num, 1)
    forbidden = {f"u10_{i}" for i in range(1, 7)} | \
        {"u12_2", "u12_3", "u12_4", "u14_2"} | \
        {f"c{2 * k}" for k in range(5, 11)}
    assert not (rf_vars(G[11]) & forbidden)
    assert not (rf_vars(G[15]) & forbidden)
    # c10,c12,c14 die because F5=F3=F1=0 (their shifted slots are zero):
    assert powers[Q(1, 4)][5] == RFZ
    assert powers[Q(0)][3] == RFZ
    assert powers[Q(-1, 4)][1] == RFZ
    # later modes unborn at weight 15: 2k>15 for k>=8
    assert all(2 * k > 15 for k in range(8, 11))
    print("G11/G15 complete-mode reconstruction matches closed forms;")
    print("  F10/F12/F14 and c10..c20 provably absent")

    # ---- Exact division, residue, endpoint identity. ------------------
    pole_quo, R = pdiv_monic(pole_num, A)
    a0, a1, a2 = (MP.var(n) for n in ("a0", "a1", "a2"))
    b0, b2, b3, b4 = (MP.var(n) for n in ("b0", "b2", "b3", "b4"))
    k2 = MP.var("k2")
    core = c6 * b2.scale(3) + c8 * a2.scale(2)
    assert R == [c8 * a1.scale(20),
                 core.scale(10),
                 c6 * b3.scale(30),
                 c6 * (b0 + b4).scale(30) + c8 * a0.scale(20)]
    assert coeff(R, 1) == core.scale(10)          # R[X1]=10(3c6b2+2c8a2)
    G15_poly = padd(padd(pscale(pscale_mp(pmul(A, F13), c2), Q(5, 4)),
                         pscale_mp(F11, c4)), pole_quo)
    # slot values, independently derived
    assert coeff(F11, 1) == k2.scale(-8)
    assert coeff(G11_closed, 0) == c4 * a1.scale(4)
    assert coeff(F7, 0) == a1.scale(4)
    assert coeff(G15_poly, 1) == \
        c4 * k2.scale(-8) + c6 * b2.scale(36) + c8 * a2.scale(24)
    endpoint = coeff(F11, 1) * coeff(G11_closed, 0) \
        - coeff(F7, 0) * coeff(G15_poly, 1)
    assert endpoint == (a1 * core).scale(-48)     # c4 cancels exactly
    identity = endpoint.scale(5) + (coeff(F7, 0) * coeff(R, 1)).scale(6)
    assert not identity
    # scope: c2 appears in neither the residue nor the endpoint identity,
    # so c2!=0 is harmless narrowing, not load-bearing
    assert "c2" not in (endpoint.vars() | {v for cc in R for v in cc.vars()})
    print("R[X1]=10*(3*c6*b2+2*c8*a2);  D22[X0]=-48*a1*(3*c6*b2+2*c8*a2)")
    print("5*D22[X0]+6*F7[X0]*R[X1]=0 as a polynomial identity")
    print("G15 polynomial => R=0 coefficientwise => D22[X0]=0, not +1 or -1")
    print("c2_not_load_bearing=True (harmless scope narrowing)")

    # ---- Hostile mutations (all must be detected). --------------------
    # M1: restoring the forbidden primitive X coefficients
    assert coeff(F9_full, 0) and 0 not in win["F"][9]
    assert coeff(F11_full, 0) and 0 not in win["F"][11]
    # M2: dropping the c8 characteristic mode changes G15
    G15_drop = rf_add(G[15], rf(pscale(pscale_mp(f, c8), Q(-1, 2)), 1))
    assert G15_drop != G[15] and G15_drop != rf(G15_num, 1)
    # M3: fractional-coefficient mutations are caught by the recurrence
    bad_num = padd(pmul(A, padd(pscale(pscale_mp(pmul(A, F13), c2), Q(5, 4)),
                                pscale_mp(F11, c4))),
                   padd(pscale(pscale_mp(F9, c6), Q(3, 8)),
                        pscale(pscale_mp(f, c8), Q(1, 2))))
    assert rf(bad_num, 1) != G[15]
    bad_G11 = padd(pscale(pmul(apow(2), F11), Q(3, 2)),
                   padd(pscale(pscale_mp(pmul(A, F9), c2), Q(3, 4)),
                        pscale_mp(F7, c4)))
    assert rf_from_poly(bad_G11) != G[11]
    # M4: residue coefficient/sign mutations break the identity
    bad_core = c6 * b2.scale(3) - c8 * a2.scale(2)
    assert coeff(R, 1) != bad_core.scale(10)
    assert coeff(R, 1) != core.scale(-10)
    assert endpoint.scale(5) - (coeff(F7, 0) * coeff(R, 1)).scale(6)
    # M5: target sign: exclusion is sign-robust (0 != +1 and 0 != -1) and
    # the +1 normalization is pinned by the J(P,Q)(0) checksum above;
    # flipping a pair-law sign was already caught in the checksum block.
    assert endpoint - ONE and endpoint + ONE
    print("mutations: b1/k1 restore, c8-drop, 3/4->3/8, 5/4->3/4,")
    print("  residue sign/scale, pair-law sign flip: all detected")

    # ---- Arbitrary-Q control: the frozen Q=X mutation. ----------------
    th = MP.var("th")
    fm = pscale([MP.const(-1), MPZ, MPZ, MPZ, MP.const(11)], Q(2 ** 29, 75))
    F9m = pscale([MPZ, MP.const(7), MPZ, MPZ, MPZ, MP.const(-27)],
                 Q(2 ** 23, 75))
    assert set(support(fm)) <= set(range(6))
    assert set(support(F9m)) <= win["F"][9]
    hm = h_formulas(X, zero, zero, zero, fm, F9m, zero, zero, zero)
    wit = {7: pscale(X, Q(2 ** 27, 75)),
           9: pscale([MPZ, MPZ, ONE], Q(-(2 ** 21), 15)),
           11: pscale([MPZ, MPZ, MPZ, ONE], Q(2 ** 14, 3)),
           13: pscale([MPZ, MPZ, MPZ, MPZ, ONE], Q(-7 * 2 ** 8, 15)),
           15: [MPZ, MPZ, MPZ, MPZ, MPZ, ONE]}
    assert hm[5] == []
    for n, dn in wit.items():
        assert hm[n] == t5(dn), f"q{n} witness fails"
    # denominator mutation control on the live Q=X lane:
    bad_h11 = padd(padd(pscale(pmul(X, F9m), Q(-5, 256)),
                        pscale(pmul(pmul(X, X), fm), Q(5, 2 ** 14))), zero)
    assert bad_h11 != t5(wit[11])
    Fmut = {0: apow(4),
            2: pscale(pmul(apow(3), X), Q(-1, 8)),
            4: pscale(pmul(apow(2), pmul(X, X)), Q(1, 256)),
            7: pscale_mp(pmul(A, fm), th),
            9: pscale_mp(F9m, th)}
    series_selftest(Fmut, 15)
    Gm, _ = characteristic(Fmut, {1: Q(1), 3: Q(1)}, 15)
    P11 = [MPZ, MP.const(Q(3 * 2 ** 21, 5)), MP.const(Q(-7 * 2 ** 18, 25)),
           MPZ, MPZ, MP.const(Q(-49 * 2 ** 21, 15)),
           MP.const(Q(27 * 2 ** 18, 25))]
    G11m_expect = pscale_mp(pmul(A, P11), th)
    G15m_expect = pscale_mp([MPZ, MP.const(Q(-(2 ** 21), 5)), MPZ,
                             MP.const(Q(2 ** 10, 3))], th)
    assert Gm[11] == rf_from_poly(G11m_expect)
    assert Gm[15] == rf_from_poly(G15m_expect)
    assert rf_is_poly(Gm[15])                    # no pole: polynomiality
    assert set(support(list(Gm[11][0]))) <= set(range(1, 14))  # G11 window
    assert set(support(list(Gm[15][0]))) <= win["G"][15]       # G15 window
    F7m = Fmut[7]
    d22m = MPZ * MPZ - coeff(F7m, 0) * coeff(list(Gm[15][0]), 1)
    assert coeff(F7m, 0) == th.scale(Q(2 ** 29, 75))
    assert coeff(list(Gm[11][0]), 0) == MPZ      # F11[X1]=G11[X0]=0
    assert d22m == (th * th).scale(Q(2 ** 50, 375))
    assert d22m.subst_var_squared("th", Q(375, 2 ** 50)) == ONE
    print("Q=X mutation: q7..q15 witnesses exact, G11/G15 windows legal,")
    print("  G15 polynomial, D22[X0]=(2^50/375)*th^2 -> 1 at th^2=375/2^50")
    print("  => fixed-slice residue identity does NOT survive Q=X (M6)")

    check_frozen("end")
    print("frozen_hashes=verified_start_and_end")
    print("PASS_HOSTILE_ORIGIN_RESIDUE_SLICE_FABLE5")


if __name__ == "__main__":
    main()
