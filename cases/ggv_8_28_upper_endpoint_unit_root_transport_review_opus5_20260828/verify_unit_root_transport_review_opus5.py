#!/usr/bin/env python3
"""Independent hostile-review checker: unit-root transport to the D22 endpoint.

Opus 5 hostile lane, 2026-08-28.  Standard library only, exact `Fraction`
arithmetic.  This file imports no producer module.  It reads frozen bytes
(hashes, the authoritative raw system, the D12 RESULT) but recomputes every
identity it asserts.

What is recomputed here, independently of the charged producer:

  S1  custody of the charged bytes;
  S2  raw-fixture facts (recurrence string, row-22 target and its sign,
      absent G22/F22 windows, G18..G21 window dimensions);
  S3  the exact eps^2 Newton identity and leading square, from a literal
      substitution X=alpha+eps, t=eps^2*s into the reduced branch-P prefix;
  S4  the valuation lemma ord(P_k)>=2k, identity (3), and the exact leading
      coefficient C(2b,k)*a0^(4b-2k)*(v0/2)^k of the mode schedule, at a
      root with a0=A'(alpha)=-4 and v0=V0(alpha)=8 (neither equal to 1);
  S5  the V0-normalization law ybar_n=nu^-n*y_n by running the recurrence
      twice at exact rational points, plus a breaking mutation;
  S6  the raw differential row D_n=sum((12-j)F_i'G_j+(i-8)F_iG_j'): the
      characteristic solutions annihilate it, the j=n block is exactly L_n,
      a wrong indicial exponent fails, and a NON-CONSTANT mode coefficient
      fails (this is the sharp form of the normalization firewall);
  S7  the complete local ladder D7..D22 rebuilt from the GENERAL reduced
      prefix F3=(Zbar+A*Tbar)/8 in an independent Laurent-in-A ring, with
      every rung's polar closed form, plus five load-bearing mutations;
  S8  the endpoint operator: order law, exact c22*A^-5 kernel, the -39
      mutation, and the G22-present strengthening D22=L22(G22-g22);
  S9  the prefix-gap finding: the charged report's normalized prefix (6)
      carries A^1 in F3, the recursively pinned fixed cascade carries A^2;
  S10 the mixed-root D12 fixture: gcds, Bezout, C^3*B^2=C*A^2, pole orders,
      and a numerical square test against the locally derived (3/8)*Delta6^2
      normal form.

Run:  python3 -B verify_unit_root_transport_review_opus5.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Fr
from functools import reduce
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

FAILURES: list[str] = []
NOTES: list[str] = []


def check(label, condition, detail=""):
    if condition:
        print(f"  PASS  {label}" + (f"   [{detail}]" if detail else ""))
    else:
        print(f"  FAIL  {label}" + (f"   [{detail}]" if detail else ""))
        FAILURES.append(label)
    return bool(condition)


def note(text):
    NOTES.append(text)
    print(f"  NOTE  {text}")


# ---------------------------------------------------------------- S1 custody
CHARGED = {
    "xmodel/ggv-upper-endpoint-unit-root-transport-sol-ultra-20260828.md":
        "98f5e97d570e4d73f4824888731162eb63588e51edfba8cff9c309fae619005f",
    "cases/ggv_8_28_upper_endpoint_unit_root_transport_20260828/verify_unit_root_transport.py":
        "48d5393afff34c02925566413da07cf3578a7045413e44aa85060ebbf0ee2412",
    "cases/ggv_8_28_upper_endpoint_unit_root_transport_20260828/RESULT.json":
        "22c4ad5065cd22635c96816c118f7981c1da4235d3b27c93aee550f4ae959903",
    "cases/ggv_8_28_upper_endpoint_unit_root_transport_20260828/TARGET.json":
        "fbe61174523d4650df006dbc5ce2bf3885130e16b506da7e276cf55ea78af2b8",
    "cases/ggv_8_28_upper_endpoint_unit_root_transport_20260828/README.md":
        "203aa3482192126f3079ec90af98ce1a98c54e23cdc07cdaac659b6fefe2515f",
    "cases/ggv_8_28_upper_endpoint_unit_root_transport_20260828/SOURCE.sha256":
        "538d8b8c784d17f0544a94abba3742f880abef080122d4610cadf6bdec972e21",
    "cases/ggv_8_28_upper_endpoint_unit_root_transport_20260828/EVIDENCE.sha256":
        "d51bd6e1797ab3b7811f35ca187ae8a3a9514d8ea61d2dbb22b1c0eeac465eb4",
    # recursively pinned upstream, re-pinned here by the reviewer
    "cases/ggv_8_28_upper_endpoint_uniform_d18_d22_fullmodes_20260828/verify_uniform_d18_d22.py":
        "49d1acaf1a8b066e9de15005e97ce948b8b33bd38315a1e77dcdf945c9b9761d",
    "cases/ggv_8_28_upper_endpoint_uniform_d18_d22_fullmodes_20260828/RESULT.json":
        "f46d7afd8b4e1e7cb5c60b029f8660dc2f1bf0e8770724808a3451c8c4e9e684",
    "cases/ggv_8_28_upper_endpoint_branch_p_20260827/RAW_DIRECT_SYSTEM.json":
        "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0",
    "cases/ggv_8_28_upper_endpoint_q1_post_d11_d12_obstruction_20260828/RESULT.json":
        "b2e0e3b9ed6ffb20328a044ae4172d0290597e5cbf088b62928ef480c24b4561",
}
DESK = "cases/ggv_8_28_upper_endpoint_uniform_d10_fullmodes_audit_20260828/verify_uniform_d10.py"


def digest(rel):
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def s1_custody():
    print("S1  custody of charged bytes")
    for rel, want in sorted(CHARGED.items()):
        check(f"sha256 {rel.split('/')[-1]}", digest(rel) == want, rel)
    print(f"  INFO  desk source {DESK} sha256 = {digest(DESK)}")
    print(f"  INFO  this checker  sha256 = "
          f"{hashlib.sha256(Path(__file__).resolve().read_bytes()).hexdigest()}")


# ------------------------------------------------------------ S2 raw fixture
def s2_raw():
    print("S2  authoritative raw fixture facts")
    raw = json.loads((ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827"
                      "/RAW_DIRECT_SYSTEM.json").read_text())
    check("recurrence is the bilinear differential row",
          raw["recurrence"] == "D_n=sum_(i+j=n)((12-j)F_i'*G_j+(i-8)F_i*G_j')")
    check("303 variables / 513 generators",
          raw["variable_count"] == 303 and raw["generator_count"] == 513 ==
          len(raw["generators"]))
    check("fixture A=X^4-1, F1=H=A^2, c2=0",
          raw["fixture"] == {"A": "X^4-1", "F1": "H", "H": "A^2", "c2": "0"})
    check("charged zero rows are D7..D21, affine target row 22 value 1",
          raw["charged_rows"]["zero"] == list(range(7, 22))
          and raw["charged_rows"]["affine_target"] == {"row": 22, "value": 1}
          and raw["charged_rows"]["D23_imposed"] is False)
    check("row 22 target is the unit 1", raw["per_row"]["22"]["target"] == 1)
    check("no raw G22 and no raw F22 window",
          raw["windows"]["G"].get("22") is None
          and raw["windows"]["F"].get("22") is None
          and raw["slotless"] == {"F_max_weight": 14, "G22_present": False,
                                  "G_max_weight": 21})
    dims = [raw["windows"]["G"][str(w)]["dimension"] for w in range(18, 22)]
    lo = [raw["windows"]["G"][str(w)]["lower"] for w in range(18, 22)]
    hi = [raw["windows"]["G"][str(w)]["upper"] for w in range(18, 22)]
    check("G18..G21 window dimensions 5,3,2,1", dims == [5, 3, 2, 1],
          f"degrees {list(zip(lo, hi))}")
    # sign of the affine target: the x_degree 0 generator of row 22 carries -1
    deg0 = [g for g in raw["generators"]
            if g["row"] == 22 and g["x_degree"] == 0]
    const = [c for g in deg0 for syms, c in g["terms"] if syms == []]
    check("row-22 degree-0 generator carries the constant -1 (target +1)",
          const == ["-1"], f"generators at x_degree 0: {len(deg0)}")


# ------------------------------------------- truncated local ring Q[eps]/eps^M
MTRUNC = 46


def tr(c):
    c = [Fr(z) for z in c][:MTRUNC]
    while c and c[-1] == 0:
        c.pop()
    return c


def tad(*xs):
    n = max((len(x) for x in xs), default=0)
    o = [Fr(0)] * n
    for x in xs:
        for i, a in enumerate(x):
            o[i] += a
    return tr(o)


def tsc(q, x):
    q = Fr(q)
    return [] if q == 0 else tr([q * a for a in x])


def tmu(x, y):
    if not x or not y:
        return []
    n = min(MTRUNC, len(x) + len(y) - 1)
    o = [Fr(0)] * n
    for i, a in enumerate(x):
        if i >= n or not a:
            continue
        for j, b in enumerate(y):
            if i + j >= n:
                break
            if b:
                o[i + j] += a * b
    return tr(o)


def tpow(x, k):
    r = [Fr(1)]
    for _ in range(k):
        r = tmu(r, x)
    return r


def tshift(x, k):
    return tr([Fr(0)] * k + list(x)) if k >= 0 else tr(list(x)[-k:])


def tord(x):
    for i, a in enumerate(x):
        if a:
            return i
    return None


def teval(coeffs, x):
    r = []
    for c in reversed(coeffs):
        r = tad(tmu(r, x), [Fr(c)])
    return r


def gbinom(r, k):
    o = Fr(1)
    for j in range(k):
        o *= (Fr(r) - j) / (j + 1)
    return o


ALPHA = Fr(-1)
APOLY = [Fr(-1), Fr(0), Fr(0), Fr(0), Fr(1)]          # A = X^4-1, alpha=-1 simple
V0POLY = [Fr(-2), Fr(0), Fr(0), Fr(-4), Fr(6)]        # V0(-1) = 8, a unit
ZPOLY = [Fr(3), Fr(-2), Fr(5)]
TPOLY = [Fr(7), Fr(1), Fr(-1), Fr(2)]
FHI = {i: [Fr(i, 3), Fr(-1, i + 2), Fr(2, i + 1)] for i in range(4, 15)}
MODES = {4: Fr(1), 6: Fr(3, 4), 8: Fr(1, 2), 10: Fr(1, 4), 12: Fr(0),
         14: Fr(-1, 4), 16: Fr(-1, 2), 18: Fr(-3, 4), 20: Fr(-1)}


def local_data():
    x = [ALPHA, Fr(1)]
    A = teval(APOLY, x)
    nu = teval(V0POLY, x)
    Z = teval(ZPOLY, x)
    Tt = teval(TPOLY, x)
    a = tshift(A, -1)
    Fs = {0: tpow(A, 4),
          1: tmu(tpow(A, 2), nu),
          2: tsc(Fr(1, 4), tad(tmu(nu, nu), tmu(tpow(A, 2), Z))),
          3: tsc(Fr(1, 8), tad(tmu(nu, Z), tmu(A, Tt)))}
    for i in range(4, 15):
        Fs[i] = teval(FHI[i], x)
    return A, a, nu, Z, Tt, Fs


# ------------------------------------------------------- S3 the Newton model
def s3_newton():
    print("S3  exact eps^2 Newton model  (X=alpha+eps, t=eps^2*s)")
    A, a, nu, Z, Tt, Fs = local_data()
    check("alpha is a simple root of A", tord(A) == 1,
          f"A'(alpha)={a[0]}, V0(alpha)={nu[0]}")
    # H(eps,s) = eps^-4 F(alpha+eps, eps^2 s) = sum_i F_i eps^(2i-4) s^i
    H = {i: tshift(Fs[i], 2 * i - 4) if 2 * i - 4 >= 0
         else tshift(Fs[i], 2 * i - 4) for i in range(15)}
    for i in range(15):
        if 2 * i - 4 < 0:
            # eps^-4 F0 and eps^-2 F1 must be regular; verify by exact division
            need = 4 - 2 * i
            check(f"eps^{2*i-4} F_{i} is regular", tord(Fs[i]) >= need,
                  f"ord F_{i} = {tord(Fs[i])}")
    Q2 = {0: tpow(a, 4), 1: tmu(tpow(a, 2), nu), 2: tsc(Fr(1, 4), tmu(nu, nu))}
    corr = {2: tshift(tsc(Fr(1, 4), tmu(tpow(a, 2), Z)), 2),
            3: tad(tshift(tsc(Fr(1, 8), tmu(nu, Z)), 2),
                   tshift(tsc(Fr(1, 8), tmu(a, Tt)), 3))}
    for i in range(4, 15):
        corr[i] = H[i]
    ok = True
    for i in range(15):
        lhs = H[i]
        rhs = tad(Q2.get(i, []), corr.get(i, []))
        if tad(lhs, tsc(-1, rhs)):
            ok = False
    check("identity (1)  H = Q^2 + eps^2(a^2 Z s^2/4 + V0 Z s^3/8)"
          " + eps^3 a T s^3/8 + sum_{i>=4} eps^(2i-4) F_i s^i", ok)
    a0, v0 = a[0], nu[0]
    lead = [H[i][0] if (H[i] and tord(H[i]) == 0) else Fr(0) for i in range(5)]
    check("identity (2)  H(0,s) = (A'(alpha)^2 + V0(alpha)s/2)^2",
          lead == [a0 ** 4, a0 ** 2 * v0, v0 ** 2 / 4, Fr(0), Fr(0)],
          f"a0^2={a0**2}, v0/2={v0/2}")


# ----------------------------------- S4 valuation lemma and the mode schedule
def s4_valuations():
    print("S4  valuation lemma, identity (3), and the mode schedule")
    A, a, nu, Z, Tt, Fs = local_data()
    a0, v0 = a[0], nu[0]
    FA = {i: tmu(Fs[i], tpow(A, 4 * i - 4)) for i in range(1, 15)}
    FA = {i: v for i, v in FA.items() if v}
    NM = 22
    orders, bad_val, bad_lead = {}, [], []
    for beta in sorted(set(MODES.values()) | {Fr(3, 2)}):
        # y_k = A^(4 beta - 4k) * P_k with P_k an exact local polynomial
        P = {0: [Fr(1)]}
        for k in range(1, NM + 1):
            s = []
            for i in range(1, k + 1):
                if i not in FA:
                    continue
                fac = (beta + 1) * i - k
                if fac == 0:
                    continue
                s = tad(s, tsc(fac, tmu(FA[i], P[k - i])))
            P[k] = tsc(Fr(1, k), s)
        for k in range(NM + 1):
            o = tord(P[k])
            if o is not None and o < 2 * k:
                bad_val.append((str(beta), k, o))
            orders[(beta, k)] = (None if o is None
                                 else int(4 * beta) - 4 * k + o)
            if o == 2 * k:
                got = P[k][2 * k] * a0 ** (int(4 * beta) - 4 * k)
                e = int(4 * beta) - 2 * k
                want = (gbinom(2 * beta, k)
                        * (a0 ** e if e >= 0 else Fr(1) / a0 ** (-e))
                        * (Fr(v0, 2)) ** k)
                if got != want:
                    bad_lead.append((str(beta), k, got, want))
    check("valuation lemma ord_alpha(P_k) >= 2k, hence ord (F^b)_k >= 4b-2k,"
          " all 10 exponents, k<=22", not bad_val, str(bad_val[:3]))
    check("leading coefficient of [s^k]H^b equals C(2b,k)*a0^(4b-2k)*(v0/2)^k",
          not bad_lead, str(bad_lead[:2]))
    tbl = []
    for m, n in ((6, 8), (10, 11), (14, 14), (16, 16), (18, 18), (20, 20)):
        beta, k = MODES[m], n - m
        pred = 6 + Fr(3 * m, 2) - 2 * n
        tbl.append((m, n, orders[(beta, k)], int(pred), gbinom(2 * beta, k)))
    check("charged mode/pole schedule reproduced exactly "
          "(c6@8,c10@11,c14@14 -> -1; c16@16 -> -2; c18@18 -> -3; c20@20 -> -4)",
          [t[2] for t in tbl] == [-1, -1, -1, -2, -3, -4]
          and [t[2] for t in tbl] == [t[3] for t in tbl],
          " ".join(f"c{m}@g{n}:ord={o},C={c}" for m, n, o, _, c in tbl))
    # why c4, c8, c12 are never forced polar: C(2b,k)=0 once k>2b in Z_{>=0}
    vanish = [(m, k) for m in (4, 8, 12)
              for k in range(int(2 * MODES[m]) + 1, 6)]
    check("c4,c8,c12 have 2b in Z_{>=0}: C(2b,k)=0 for k>2b, so the bound"
          " 6+3m/2-2n is NOT attained for them",
          all(gbinom(2 * MODES[m], k) == 0 for m, k in vanish))
    check("c4 mode series is polynomial in t: (F^1)_k = F_k is regular for all k",
          all(orders[(Fr(1), k)] is None or orders[(Fr(1), k)] >= 0
              for k in range(NM + 1)))
    check("c12 mode series is (F^0)_k = delta_{k0}, always regular",
          all(orders[(Fr(0), k)] is None or orders[(Fr(0), k)] >= 0
              for k in range(NM + 1)))


# --------------------------------------------- S5 the V0-normalization law
def s5_normalization():
    print("S5  coefficientwise V0 normalization (run, not asserted)")

    def polyval(c, x):
        r = Fr(0)
        for k in reversed(c):
            r = r * x + Fr(k)
        return r

    def rec(Fv, beta, N, y0):
        y = {0: y0}
        for n in range(1, N + 1):
            s = Fr(0)
            for i in range(1, n + 1):
                if i not in Fv:
                    continue
                fac = (beta + 1) * i - n
                if fac:
                    s += fac * Fv[i] * y[n - i]
            y[n] = s / (n * Fv[0])
        return y

    bad, mut_survivors, mut_total = [], [], 0
    for x0 in (Fr(2), Fr(-3, 5), Fr(7, 3)):
        A = polyval(APOLY, x0)
        nu = polyval(V0POLY, x0)
        Z = polyval(ZPOLY, x0)
        Tt = polyval(TPOLY, x0)
        assert A and nu
        Fv = {0: A ** 4, 1: A ** 2 * nu, 2: (nu * nu + A ** 2 * Z) / 4,
              3: (nu * Z + A * Tt) / 8}
        for i in range(4, 15):
            Fv[i] = polyval(FHI[i], x0)
        Fb = {i: Fv[i] / nu ** i for i in Fv}
        Fm = {0: Fv[0]}
        Fm.update({i: Fv[i] / nu ** (i - 1) for i in range(1, 15)})
        for beta in sorted(set(MODES.values()) | {Fr(3, 2)}):
            y0 = A ** int(4 * beta) if 4 * beta >= 0 else Fr(1) / A ** int(-4 * beta)
            y = rec(Fv, beta, 22, y0)
            yb = rec(Fb, beta, 22, y0)
            ym = rec(Fm, beta, 22, y0)
            for n in range(23):
                if yb[n] != y[n] / nu ** n:
                    bad.append((str(x0), str(beta), n))
                if n and y[n] != 0:
                    mut_total += 1
                    if ym[n] == y[n] / nu ** n:
                        mut_survivors.append((str(x0), str(beta), n))
    check("Fbar_i=nu^-i F_i implies ybar_n=nu^-n y_n, 3 rational points x 10"
          " exponents x weights 0..22", not bad, str(bad[:3]))
    check("MUTATION Fbar_i=nu^-(i-1)F_i breaks the law at every nontrivial"
          " (point,exponent,weight)", not mut_survivors,
          f"{mut_total} nontrivial checks, {len(mut_survivors)} survivors")
    # the normalized prefix, and the A-power in Fbar_3
    A, a, nu, Z, Tt, Fs = local_data()
    # Fbar_2 = (1 + A^2 Zbar)/4 and Fbar_3 = (Zbar + A Tbar)/8 with
    # Zbar = Z/nu^2, Tbar = T/nu^3 -- verified by clearing denominators.
    # 4*F2 = nu^2 + A^2 Z  and  8*F3 = nu*Z + A*T, so after dividing by nu^i:
    #   Fbar_2 = (1 + A^2 Zbar)/4,  Fbar_3 = (Zbar + A^1 Tbar)/8.
    check("reduced prefix: 4*F2 = V0^2 + A^2 Z, hence Fbar_2 = (1+A^2 Zbar)/4",
          not tad(tsc(4, Fs[2]), tsc(-1, tad(tpow(nu, 2), tmu(tpow(A, 2), Z)))))
    check("reduced prefix: 8*F3 = V0*Z + A*T, hence Fbar_3 = (Zbar + A*Tbar)/8"
          "   -- A power ONE",
          not tad(tsc(8, Fs[3]), tsc(-1, tad(tmu(nu, Z), tmu(A, Tt)))))
    check("with generic T, ord_alpha(Tbar)=0, so Fbar_3 is NOT of the pinned"
          " shape (Zbar+A^2*Vbar)/8 before the local D7 rung",
          tord(Tt) == 0, f"ord_alpha(T) = {tord(Tt)}")


# ---------------------- independent Laurent-in-A ring with symbol monomials
def T(coef=1, a=0, *syms):
    c = Fr(coef)
    return {(a, tuple(sorted(syms))): c} if c else {}


def AD(*xs):
    r = {}
    for x in xs:
        for k, v in x.items():
            n = r.get(k, Fr(0)) + v
            if n:
                r[k] = n
            elif k in r:
                del r[k]
    return r


def SC(c, x):
    c = Fr(c)
    return {} if not c else {k: c * v for k, v in x.items()}


def MU(x, y):
    r = {}
    for (a1, s1), v1 in x.items():
        for (a2, s2), v2 in y.items():
            k = (a1 + a2, tuple(sorted(s1 + s2)))
            n = r.get(k, Fr(0)) + v1 * v2
            if n:
                r[k] = n
            elif k in r:
                del r[k]
    return r


def SH(a, x):
    return {(k[0] + a, k[1]): v for k, v in x.items()}


def NEG(x):
    return {k: v for k, v in x.items() if k[0] < 0}


def MODA(b, x):
    return {k: v for k, v in x.items() if k[0] < b}


def SUB(x, rules):
    r = {}
    for (a, syms), c in x.items():
        t = T(c, a)
        for s in syms:
            t = MU(t, rules.get(s, T(1, 0, s)))
        r = AD(r, t)
    return r


DERIV = {}


def dX(x):
    r = {}
    for (a, syms), c in x.items():
        if a:
            k = (a - 1, tuple(sorted(syms + ("ap",))))
            r[k] = r.get(k, Fr(0)) + c * a
        for i, s in enumerate(syms):
            d = DERIV.get(s)
            if d is None:
                continue
            ch = list(syms)
            ch[i] = d
            k = (a, tuple(sorted(ch)))
            r[k] = r.get(k, Fr(0)) + c
    return {k: v for k, v in r.items() if v}


def Lop(n, x):
    return AD(SC(4 * (12 - n), MU(SH(3, x), T(1, 0, "ap"))),
              SC(-8, SH(4, dX(x))))


def frac_coeffs(Fs, beta, N):
    y = {0: T(1, int(4 * beta))}
    for n in range(1, N + 1):
        num = {}
        for i in range(1, n + 1):
            fac = (beta + 1) * i - n
            if fac == 0 or not Fs.get(i):
                continue
            num = AD(num, SC(fac, MU(Fs[i], y[n - i])))
        y[n] = SC(Fr(1, n), SH(-4, num))
    return y


def continuation(Fs, N):
    pw = {e: frac_coeffs(Fs, e, N)
          for e in set(MODES.values()) | {Fr(3, 2)}}
    g = {}
    for n in range(N + 1):
        row = pw[Fr(3, 2)][n]
        for m, e in sorted(MODES.items()):
            if m <= n:
                row = AD(row, MU(T(1, 0, f"c{m}"), pw[e][n - m]))
        g[n] = row
    return pw, g


# --------------------------------------------- S6 the raw differential row
def s6_raw_row():
    print("S6  the raw differential row and mode scalarity")
    NF = 8
    Fs = {0: T(1, 4)}
    for i in range(1, NF + 1):
        Fs[i] = T(1, 0, f"F{i}")
        DERIV[f"F{i}"] = f"F{i}_x"

    def Drow(G, n):
        out = {}
        for i in range(0, n + 1):
            j = n - i
            if not Fs.get(i) or not G.get(j):
                continue
            out = AD(out, SC(12 - j, MU(dX(Fs[i]), G[j])),
                     SC(i - 8, MU(Fs[i], dX(G[j]))))
        return out

    DERIV["Gn"] = "Gn_x"
    check("the j=n block of the raw row is exactly L_n(G_n)"
          " = 4(12-n)A^3A'G_n - 8A^4G_n'",
          all(AD(SC(12 - n, MU(dX(Fs[0]), T(1, 0, "Gn"))),
                 SC(-8, MU(Fs[0], dX(T(1, 0, "Gn"))))) == Lop(n, T(1, 0, "Gn"))
              for n in range(4, 23)))
    y32 = frac_coeffs(Fs, Fr(3, 2), 11)
    check("G = F^(3/2) annihilates D_n for n=0..11",
          all(not Drow(y32, n) for n in range(12)))
    okm, badm = True, []
    for m, beta in sorted(MODES.items()):
        yb = frac_coeffs(Fs, beta, m + 6)
        Gm = {j: MU(T(1, 0, "cm"), yb[j - m]) for j in range(m, m + 7)}
        if any(Drow(Gm, n) for n in range(m, m + 7)):
            okm = False
            badm.append(m)
    check("G = c_m t^m F^((12-m)/8) with a CONSTANT c_m annihilates D_n,"
          " all nine modes", okm, str(badm))
    yb = frac_coeffs(Fs, Fr(1, 2), 12)
    Gw = {j: MU(T(1, 0, "cm"), yb[j - 6]) for j in range(6, 13)}
    check("MUTATION wrong indicial exponent (beta=1/2 born at m=6) fails",
          any(Drow(Gw, n) for n in range(6, 13)))
    DERIV["cm"] = "cm_x"
    yb = frac_coeffs(Fs, Fr(3, 4), 12)
    Gn = {j: MU(T(1, 0, "cm"), yb[j - 6]) for j in range(6, 13)}
    check("MUTATION NON-CONSTANT mode coefficient fails: c'(X)t^m F^b(tF_t-8F)"
          " does not vanish -> the normalized cbar_m=nu^-m c_m is NOT a raw mode",
          any(Drow(Gn, n) for n in range(6, 13)))
    del DERIV["cm"]


# --------------------------- S7 the complete local ladder from the general prefix
def sym(n):
    return T(1, 0, n)


def build(p3=2, p4=2, p5=2, p6=2, p7=2, N=22, general_T=False):
    Z, V, R, Q, TT, YY = (sym(x) for x in ("Z", "V", "R", "Q", "TT", "YY"))
    Fs = {0: T(1, 4), 1: T(1, 2),
          2: AD(T(Fr(1, 4)), SC(Fr(1, 4), MU(T(1, 2), Z)))}
    if general_T:
        Fs[3] = AD(SC(Fr(1, 8), Z), SC(Fr(1, 8), MU(T(1, 1), sym("Tt"))))
    else:
        Fs[3] = AD(SC(Fr(1, 8), Z), SC(Fr(1, 8), MU(T(1, p3), V)))
    Fs[4] = AD(SC(Fr(1, 16), V), SC(Fr(1, 64), MU(Z, Z)), MU(T(1, p4), R))
    Fs[5] = AD(SC(Fr(1, 2), R), SC(Fr(1, 64), MU(Z, V)), MU(T(1, p5), Q))
    Fs[6] = AD(SC(Fr(1, 2), Q), SC(Fr(1, 8), MU(R, Z)),
               SC(Fr(1, 256), MU(V, V)), MU(T(1, p6), TT))
    Fs[7] = AD(SC(Fr(1, 2), TT), SC(Fr(1, 8), MU(Q, Z)),
               SC(Fr(1, 16), MU(R, V)), MU(T(1, p7), YY))
    for w in range(8, 15):
        Fs[w] = sym(f"f{w}")
    for w in range(15, N + 1):
        Fs[w] = {}
    return Fs


def prod(*xs):
    return reduce(MU, xs)


def s7_ladder():
    print("S7  the complete local ladder D7..D22 from the GENERAL reduced prefix")
    Z, V, R, Q, TT, YY = (sym(x) for x in ("Z", "V", "R", "Q", "TT", "YY"))
    c8 = sym("c8")

    # --- D7 from the pre-D7 general prefix Fbar_3 = (Z + A*T)/8 -----------
    FsG = {0: T(1, 4), 1: T(1, 2),
           2: AD(T(Fr(1, 4)), SC(Fr(1, 4), MU(T(1, 2), Z))),
           3: AD(SC(Fr(1, 8), Z), SC(Fr(1, 8), MU(T(1, 1), sym("Tt"))))}
    for w in range(4, 15):
        FsG[w] = sym(f"f{w}")
    for w in range(15, 10):
        FsG[w] = {}
    _, gG = continuation({k: v for k, v in FsG.items()}, 8)
    Tt, K = sym("Tt"), AD(SC(64, sym("f4")), SC(-1, MU(Z, Z)))
    want7 = SC(Fr(3, 2048), SH(-2, MU(Tt, AD(MU(T(1, 1), K), SC(-2, Tt)))))
    check("D7 polar closed form: polar(g7) = 3*T*(A*K-2*T)/(2048*A^2),"
          " K=64F4-Z^2  (equals the q1-free lane's A^2 | T(AK-2TV0) at V0=1)",
          NEG(gG[7]) == want7)
    note("D7 rung, LOCAL: ord(T)=0 would give ord(T(AK-2T))=0<2, so "
         "ord_alpha(T)>=1 at a simple V0-unit root; write T=A*V.")

    # --- D8 / D9 --------------------------------------------------------
    Fs89 = build(p4=1, N=9)
    Fs89[4] = AD(SC(Fr(1, 16), V), SC(Fr(1, 64), MU(Z, Z)), MU(T(1, 1), sym("W")))
    Fs89[5] = sym("f5")
    Fs89[6] = sym("f6")
    Fs89[7] = sym("f7")
    _, g89 = continuation(Fs89, 9)
    W0 = AD(sym("f4"), SC(Fr(-1, 16), V), SC(Fr(-1, 64), MU(Z, Z)))
    FsW0 = build(N=9)
    FsW0[4] = sym("f4")
    FsW0[5], FsW0[6], FsW0[7] = sym("f5"), sym("f6"), sym("f7")
    _, gW0 = continuation(FsW0, 8)
    check("D8 polar closed form: polar(g8) = (3/8)*(F4-V/16-Z^2/64)^2/A^2"
          " + (3/32)*c6/A",
          NEG(gW0[8]) == AD(SC(Fr(3, 8), SH(-2, MU(W0, W0))),
                            T(Fr(3, 32), -1, "c6")))
    note("D8 rung, LOCAL: mod A gives ord(W0^2)>=1 so ord(W0)>=1 (DVR); then "
         "the A^1 class forces ord(c6)>=1, and c6 is a scalar, so c6=0.")
    Wsym = sym("W")
    check("D9 polar closed form after c6=0:"
          " -3W^2/(16A^2) + (3/4)F5*W/A - (3/256)V*W*Z/A",
          NEG(SUB(g89[9], {"c6": {}})) ==
          AD(SC(Fr(-3, 16), SH(-2, MU(Wsym, Wsym))),
             SC(Fr(3, 4), SH(-1, MU(Wsym, sym("f5")))),
             SC(Fr(-3, 256), SH(-1, prod(Wsym, V, Z)))))
    note("D9 rung, LOCAL: mod A gives ord(W^2)>=1, so ord(W)>=1; W=A*R.")

    # --- D10 / D11 ------------------------------------------------------
    Fs10 = build(N=11)
    Fs10[5], Fs10[6], Fs10[7] = sym("f5"), sym("f6"), sym("f7")
    _, g10 = continuation(Fs10, 10)
    D5 = AD(sym("f5"), SC(Fr(-1, 2), R), SC(Fr(-1, 64), MU(Z, V)))
    check("D10 polar closed form: polar(g10) = (3/8)*Delta5^2/A^2,"
          " Delta5=F5-R/2-Z*V/64",
          NEG(SUB(g10[10], {"c6": {}})) == SC(Fr(3, 8), SH(-2, MU(D5, D5))))
    Fs11 = build(p5=1, N=11)
    Fs11[5] = AD(SC(Fr(1, 2), R), SC(Fr(1, 64), MU(Z, V)), MU(T(1, 1), sym("Ss")))
    Fs11[6], Fs11[7] = sym("f6"), sym("f7")
    _, g11 = continuation(Fs11, 11)
    Ss = sym("Ss")
    want11 = AD(SC(Fr(-3, 16), SH(-2, MU(Ss, Ss))),
                SC(Fr(-3, 32), SH(-1, prod(R, Ss, Z))),
                SC(Fr(-3, 1024), SH(-1, prod(Ss, V, V))),
                SC(Fr(3, 4), SH(-1, MU(Ss, sym("f6")))),
                T(Fr(1, 4), -1, "c10"))
    check("D11 polar closed form: -3S^2/(16A^2) + A^-1(...) + c10/(4A)"
          " -> ord(S)>=1 then c10=0",
          NEG(SUB(g11[11], {"c6": {}})) == want11)

    # --- D12 / D13 / D14 / D15 -----------------------------------------
    Fs12 = build(N=13)
    Fs12[6], Fs12[7] = sym("f6"), sym("f7")
    _, g12 = continuation(Fs12, 12)
    D6 = AD(sym("f6"), SC(Fr(-1, 2), Q), SC(Fr(-1, 8), MU(R, Z)),
            SC(Fr(-1, 256), MU(V, V)))
    check("D12 polar closed form: polar(g12) = (3/8)*Delta6^2/A^2,"
          " Delta6=F6-Q/2-R*Z/8-V^2/256",
          NEG(SUB(g12[12], {"c6": {}, "c10": {}})) ==
          SC(Fr(3, 8), SH(-2, MU(D6, D6))))
    Fs13 = build(p6=1, N=13)
    Fs13[6] = AD(SC(Fr(1, 2), Q), SC(Fr(1, 8), MU(R, Z)),
                 SC(Fr(1, 256), MU(V, V)), MU(T(1, 1), sym("T1")))
    Fs13[7] = sym("f7")
    _, g13 = continuation(Fs13, 13)
    T1 = sym("T1")
    check("D13 polar: -3*T1^2/(16A^2) + O(A^-1) -> ord(T1)>=1",
          NEG(SUB(g13[13], {"c6": {}, "c10": {}}))[( -2, ("T1", "T1"))] == Fr(-3, 16))
    Fs14 = build(N=15)
    Fs14[7] = sym("f7")
    _, g14 = continuation(Fs14, 14)
    n14 = NEG(SUB(g14[14], {"c6": {}, "c10": {}}))
    D7d = AD(sym("f7"), SC(Fr(-1, 2), TT), SC(Fr(-1, 8), MU(Q, Z)),
             SC(Fr(-1, 16), MU(R, V)))
    check("D14: the A^-1 (odd) class of polar(g14) is exactly c14, and the"
          " A^-2 class contains (3/8)Delta7^2 -> c14=0 and ord(Delta7)>=1",
          {k: v for k, v in n14.items() if k[0] % 2} == T(1, -1, "c14")
          and sorted({a for a, _ in n14}) == [-2, -1])
    Fs15 = build(p7=1, N=15)
    Fs15[7] = AD(SC(Fr(1, 2), TT), SC(Fr(1, 8), MU(Q, Z)),
                 SC(Fr(1, 16), MU(R, V)), MU(T(1, 1), sym("Y1")))
    _, g15 = continuation(Fs15, 15)
    check("D15 polar: -3*Y1^2/(16A^2) + O(A^-1) -> ord(Y1)>=1",
          NEG(SUB(g15[15], {"c6": {}, "c10": {}, "c14": {}}))[(-2, ("Y1", "Y1"))]
          == Fr(-3, 16))

    # --- D16..D22 -------------------------------------------------------
    Fs = build(N=22)
    _, g = continuation(Fs, 22)
    kills = {"c6": {}, "c10": {}, "c14": {}}
    b, d, e, h, j, k = (sym(x) for x in ("b", "d", "e", "h", "j", "k"))
    base8 = AD(SC(Fr(1, 2), YY), SC(Fr(1, 8), MU(TT, Z)),
               SC(Fr(1, 16), MU(Q, V)), SC(Fr(1, 4), MU(R, R)))
    base9 = AD(SC(Fr(1, 2), MU(Q, R)), SC(Fr(1, 16), MU(TT, V)),
               SC(Fr(1, 8), MU(YY, Z)))
    base10 = AD(SC(Fr(1, 4), MU(d, Z)), SC(Fr(1, 4), MU(Q, Q)),
                SC(Fr(1, 2), MU(R, TT)), SC(Fr(1, 16), MU(V, YY)))
    base11 = AD(SC(Fr(1, 2), MU(e, Z)), SC(Fr(1, 2), MU(Q, TT)),
                SC(Fr(1, 2), MU(R, YY)), SC(Fr(1, 8), MU(d, V)))
    base12 = AD(MU(d, R), SC(Fr(1, 4), MU(e, V)), SC(Fr(1, 16), prod(e, Z, Z)),
                SC(Fr(3, 4), MU(h, Z)), SC(Fr(1, 2), MU(Q, YY)),
                SC(Fr(1, 4), MU(TT, TT)))
    base13 = AD(MU(d, Q), SC(2, MU(e, R)), SC(Fr(1, 16), prod(e, V, Z)),
                SC(Fr(3, 8), MU(h, V)), SC(Fr(3, 16), prod(h, Z, Z)),
                MU(j, Z), SC(Fr(1, 2), MU(TT, YY)))
    base14 = AD(MU(d, TT), SC(2, MU(e, Q)), SC(Fr(1, 2), prod(e, R, Z)),
                SC(Fr(1, 64), prod(e, V, V)), SC(3, MU(h, R)),
                SC(Fr(3, 16), prod(h, V, Z)), SC(Fr(1, 64), prod(h, Z, Z, Z)),
                SC(Fr(1, 2), MU(j, V)), SC(Fr(3, 8), prod(j, Z, Z)),
                SC(Fr(5, 4), MU(k, Z)), SC(Fr(1, 4), MU(YY, YY)))
    mix = AD(SC(Fr(3, 4), b), SC(Fr(1, 2), c8))

    def sub_all(x, rels):
        for r in rels:
            x = SUB(x, r)
        return x

    g16 = SUB(g[16], kills)
    num16 = AD(SC(Fr(3, 8), MU(b, b)), SC(Fr(1, 2), MU(c8, b)), sym("c16"))
    check("D16: polar(g16) = (3B^2/8 + c8*B/2 + c16)/A^2",
          NEG(SUB(g16, {"f8": AD(b, base8)})) == SH(-2, num16))
    rel16 = {"f8": AD(base8, b),
             "c16": AD(MU(T(1, 2), sym("m")), SC(Fr(-3, 8), MU(b, b)),
                       SC(Fr(-1, 2), MU(c8, b)))}
    check("D16 relation 3B^2+4c8B+8c16 = 8A^2M clears the polar part",
          not NEG(sub_all(g[16], [kills, rel16])))
    C_ = AD(sym("f9"), SC(-1, base9))
    obs17 = AD(SC(Fr(3, 4), MU(b, C_)), SC(Fr(1, 2), MU(c8, C_)),
               SC(Fr(-1, 2), sym("m")))
    g17 = sub_all(g[17], [kills, rel16])
    check("D17: polar(g17) = ((3B+2c8)C/4 - M/2)/A^2", NEG(g17) == SH(-2, obs17))
    rel17 = {"f9": AD(base9, d),
             "m": AD(SC(Fr(3, 2), MU(b, d)), MU(c8, d),
                     SC(-2, MU(T(1, 2), sym("n"))))}
    check("D17 relation (3B+2c8)C-2M = 4A^2N clears the polar part",
          not NEG(sub_all(g[17], [kills, rel16, rel17])))

    pref = [kills, rel16, rel17]
    p18 = AD(MU(mix, AD(sym("f10"), SC(-1, base10))), SC(Fr(3, 8), MU(d, d)),
             SC(Fr(-1, 2), sym("n")))
    g18b = sub_all(g[18], pref)
    check("D18: polar(g18) = c18/A^3 + ((3B+2c8)E/4+3C^2/8-N/2)/A^2",
          NEG(g18b) == AD(T(1, -3, "c18"), SH(-2, p18)))
    check("L_18 annihilates c18/A^3 (so D19 cannot kill it; the birth row does)",
          not Lop(18, T(1, -3, "c18")))
    rel18 = {"c18": {}, "f10": AD(base10, e),
             "n": AD(SC(Fr(3, 2), MU(b, e)), MU(c8, e), SC(Fr(3, 4), MU(d, d)),
                     SC(-2, MU(T(1, 2), sym("o"))))}
    check("D18 relations c18=0 and (...)=A^2 O clear the polar part",
          not NEG(sub_all(g18b, [rel18])))
    p19 = AD(MU(mix, AD(sym("f11"), SC(-1, base11))), SC(Fr(3, 4), MU(d, e)),
             SC(Fr(-1, 2), sym("o")))
    g19b = sub_all(g[19], pref + [rel18])
    rel19 = {"f11": AD(base11, h),
             "o": AD(SC(Fr(3, 2), MU(b, h)), MU(c8, h), SC(Fr(3, 2), MU(d, e)),
                     SC(-2, MU(T(1, 2), sym("p"))))}
    check("D19: polar = A^-2 only, and its relation clears it",
          NEG(g19b) == SH(-2, p19) and not NEG(sub_all(g19b, [rel19])))
    p20 = AD(MU(mix, AD(sym("f12"), SC(-1, base12))), SC(Fr(3, 4), MU(d, h)),
             SC(Fr(3, 8), MU(e, e)), SC(Fr(-1, 2), sym("p")))
    g20b = sub_all(g[20], pref + [rel18, rel19])
    rel20 = {"c20": {}, "f12": AD(base12, j),
             "p": AD(SC(Fr(3, 2), MU(b, j)), MU(c8, j), SC(Fr(3, 2), MU(d, h)),
                     SC(Fr(3, 4), MU(e, e)), SC(-2, MU(T(1, 2), sym("s"))))}
    check("D20: polar = c20/A^4 + P20/A^2, L_20 kills c20/A^4, relation clears",
          NEG(g20b) == AD(T(1, -4, "c20"), SH(-2, p20))
          and not Lop(20, T(1, -4, "c20"))
          and not NEG(sub_all(g20b, [rel20])))
    p21 = AD(MU(mix, AD(sym("f13"), SC(-1, base13))), SC(Fr(3, 4), MU(d, j)),
             SC(Fr(3, 4), MU(e, h)), SC(Fr(-1, 2), sym("s")))
    g21b = sub_all(g[21], pref + [rel18, rel19, rel20])
    rel21 = {"f13": AD(base13, k),
             "s": AD(SC(Fr(3, 2), MU(b, k)), MU(c8, k), SC(Fr(3, 2), MU(d, j)),
                     SC(Fr(3, 2), MU(e, h)), SC(-2, MU(T(1, 2), sym("u"))))}
    check("D21: polar = A^-2 only, and its relation clears it",
          NEG(g21b) == SH(-2, p21) and not NEG(sub_all(g21b, [rel21])))

    g22 = sub_all(g[22], pref + [rel18, rel19, rel20, rel21])
    p22 = AD(MU(mix, AD(sym("f14"), SC(-1, base14))), SC(Fr(3, 4), MU(d, k)),
             SC(Fr(3, 4), MU(e, j)), SC(Fr(3, 8), MU(h, h)),
             SC(Fr(-1, 2), sym("u")))
    supp = sorted({a for a, _ in g22})
    check("ENDPOINT: complete g22 has A-exponent support {-2,0,2,4,6,8},"
          " so ord_alpha(g22) >= -2", supp == [-2, 0, 2, 4, 6, 8]
          and NEG(g22) == SH(-2, p22), f"support {supp}")
    for nm in ("b", "d", "e", "h", "j", "k", "m", "n", "o", "p", "s", "u",
               "Z", "V", "R", "Q", "TT", "YY", "c16",
               "f8", "f9", "f10", "f11", "f12", "f13", "f14"):
        DERIV[nm] = nm + "_x"
    d22 = SC(-1, Lop(22, g22))
    check("D22_raw = -L22(g22) lies in (A): every term has A-exponent >= 1",
          not MODA(1, d22), f"{len(d22)} terms, min A-exponent "
          f"{min(a for a, _ in d22)}")
    return g22


def s7_mutations():
    print("S7m load-bearing mutations of the local ladder")
    depth = {}
    for lbl, ps in (("baseline", (2, 2, 2, 2, 2)),
                    ("skip D7  (F3 keeps A^1)", (1, 2, 2, 2, 2)),
                    ("skip D9  (F4 keeps A^1)", (2, 1, 2, 2, 2)),
                    ("skip D11 (F5 keeps A^1)", (2, 2, 1, 2, 2)),
                    ("skip D13 (F6 keeps A^1)", (2, 2, 2, 1, 2)),
                    ("skip D15 (F7 keeps A^1)", (2, 2, 2, 2, 1))):
        _, g = continuation(build(*ps, N=16), 16)
        n16 = NEG(SUB(g[16], {"c6": {}, "c10": {}, "c14": {}}))
        depth[lbl] = min(a for a, _ in n16) if n16 else None
    check("each prefix rung D7,D9,D11,D13,D15 is load-bearing: dropping one"
          " deepens polar(g16) from -2 to -20/-16/-12/-8/-4",
          depth["baseline"] == -2
          and [depth[k] for k in list(depth)[1:]] == [-20, -16, -12, -8, -4],
          str(depth))
    # retaining c18 breaks D18
    Fs = build(N=19)
    _, g = continuation(Fs, 19)
    Z, V, R, Q, TT, YY = (sym(x) for x in ("Z", "V", "R", "Q", "TT", "YY"))
    b, d, e, c8 = sym("b"), sym("d"), sym("e"), sym("c8")
    base8 = AD(SC(Fr(1, 2), YY), SC(Fr(1, 8), MU(TT, Z)),
               SC(Fr(1, 16), MU(Q, V)), SC(Fr(1, 4), MU(R, R)))
    base9 = AD(SC(Fr(1, 2), MU(Q, R)), SC(Fr(1, 16), MU(TT, V)),
               SC(Fr(1, 8), MU(YY, Z)))
    base10 = AD(SC(Fr(1, 4), MU(d, Z)), SC(Fr(1, 4), MU(Q, Q)),
                SC(Fr(1, 2), MU(R, TT)), SC(Fr(1, 16), MU(V, YY)))
    rels = [{"c6": {}, "c10": {}, "c14": {}},
            {"f8": AD(base8, b),
             "c16": AD(MU(T(1, 2), sym("m")), SC(Fr(-3, 8), MU(b, b)),
                       SC(Fr(-1, 2), MU(c8, b)))},
            {"f9": AD(base9, d),
             "m": AD(SC(Fr(3, 2), MU(b, d)), MU(c8, d),
                     SC(-2, MU(T(1, 2), sym("n"))))},
            {"f10": AD(base10, e),
             "n": AD(SC(Fr(3, 2), MU(b, e)), MU(c8, e),
                     SC(Fr(3, 4), MU(d, d)), SC(-2, MU(T(1, 2), sym("o"))))}]
    x = g[18]
    for r in rels:
        x = SUB(x, r)
    check("MUTATION retaining c18: the D18 quotient relation alone leaves"
          " exactly c18/A^3, so the polar part does not clear",
          NEG(x) == T(1, -3, "c18"))


# --------------------------------------------------------- S8 endpoint algebra
def s8_endpoint():
    print("S8  the endpoint operator L22 in the original coordinates")
    DERIV["Rg"] = "Rg_x"
    orders = {}
    for kk in range(-6, 7):
        img = Lop(22, T(1, kk, "Rg"))
        orders[kk] = min(a for a, _ in img) if img else None
    check("L22(R) with R of A-exponent k has A-exponent >= k+3 (exactly k+3"
          " except on the kernel direction k=-5, where 40+8k=0 gives k+4)",
          all(orders[kk] >= kk + 3 for kk in orders if orders[kk] is not None)
          and all(orders[kk] == kk + 3 for kk in orders
                  if orders[kk] is not None and kk != -5)
          and orders[-5] == -1,
          f"k=-2 -> {orders[-2]}, k=0 -> {orders[0]}, k=-5 -> {orders[-5]}")
    check("hence ord_alpha(g22) >= -2 forces D22_raw in the maximal ideal"
          " (X-alpha)", orders[-2] == 1)
    check("EXACT kernel: L22(c22*A^-5) = 0  (-40 + (-8)(-5) = 0)",
          not Lop(22, T(1, -5, "c22")))

    def Lmut(x):
        return AD(SC(-39, MU(SH(3, x), T(1, 0, "ap"))), SC(-8, SH(4, dX(x))))

    check("MUTATION -40 -> -39 destroys the c22*A^-5 cancellation"
          " (residual +1*c22*A^-2*A')",
          Lmut(T(1, -5, "c22")) == T(1, -2, "ap", "c22"))
    check("no other homogeneous endpoint mode: ker L_n is spanned by"
          " A^((12-n)/2), which for n=22 is A^-5 and for odd n is not rational",
          not Lop(22, T(1, -5, "c22")) and Lop(22, T(1, -4, "c22")))
    note("STRENGTHENING: the raw row is linear in G22 with block L22, so for "
         "ANY G22 one has D22 = L22(G22 - g22).  If a regular raw G22 receiver "
         "existed, ord(G22-g22) >= -2 still gives D22 in (X-alpha).  'Absent "
         "raw G22' is therefore not load-bearing for the contradiction.")
    note("Multiplicity: if alpha had multiplicity e>=2 the endpoint step still "
         "gives ord >= 2e-1 >= 1, but the ladder's square-root rungs "
         "(ord(Delta^2)>=e => ord(Delta)>=e) fail.  Simplicity of alpha, not "
         "squarefreeness of all of A, is what the ladder needs.")


# ------------------------------------------------------------ S9 prefix gap
def s9_prefix_gap():
    print("S9  the prefix gap between the charged (6) and the pinned cascade")
    rep = (ROOT / "xmodel/ggv-upper-endpoint-unit-root-transport-sol-ultra-"
                  "20260828.md").read_text()
    desk = (ROOT / DESK).read_text()
    check("charged report displays Fbar_3=(Zbar+A*Tbar)/8   (A power ONE)",
          "Fbar_3=(Zbar+A*Tbar)/8," in rep)
    check("charged report claims '(6) is exactly the reviewed fixed prefix'",
          "So (6) is exactly the reviewed fixed prefix in the local coefficient"
          in rep)
    pinned = ("        3: la_add(la_scale(Q(1, 8), z),\n"
              "                  la_scale(Q(1, 8), la_mul(la_term(1, 2), v))),")
    check("recursively pinned common_F_prefix has F3 = (z + A^2*v)/8"
          "   (A power TWO)", pinned in desk)
    check("pinned D8/D9 stage starts from F4 = v/16+z^2/64+A^1*w, i.e. after"
          " the D7 rung A|T", 'la_mul(la_term(1, 1), w))' in desk)
    note("The charged normalized prefix (6) is the PRE-D7 general prefix; the "
         "recursively pinned fixed cascade starts one A-power deeper at F3 "
         "(post-D7 A|T) and at F4 (post-D9 A|W).  The identification asserted "
         "in the charged section 2 is false as written; the bridge needs the "
         "local D7..D15 rungs, which S7 supplies.")


# --------------------------------------------------------- S10 D12 fixture
def pad(x, y):
    n = max(len(x), len(y))
    o = [Fr(0)] * n
    for i, a in enumerate(x):
        o[i] += a
    for i, a in enumerate(y):
        o[i] += a
    while o and o[-1] == 0:
        o.pop()
    return o


def pmul(x, y):
    if not x or not y:
        return []
    o = [Fr(0)] * (len(x) + len(y) - 1)
    for i, a in enumerate(x):
        for jj, b in enumerate(y):
            o[i + jj] += a * b
    while o and o[-1] == 0:
        o.pop()
    return o


def psc(q, x):
    q = Fr(q)
    return [] if q == 0 else [q * a for a in x]


def pdivmod(p, q):
    p = list(p)
    out = [Fr(0)] * max(0, len(p) - len(q) + 1)
    while p and len(p) >= len(q):
        dg = len(p) - len(q)
        c = p[-1] / q[-1]
        out[dg] += c
        p = pad(p, psc(-c, [Fr(0)] * dg + list(q)))
    while out and out[-1] == 0:
        out.pop()
    return out, p


def pgcd(p, q):
    p, q = list(p), list(q)
    while q:
        p, q = q, pdivmod(p, q)[1]
    return psc(1 / p[-1], p) if p else []


def pev(p, x):
    r = Fr(0)
    for c in reversed(p):
        r = r * Fr(x) + c
    return r


def pder(p):
    return [Fr(i) * p[i] for i in range(1, len(p))]


def s10_d12():
    print("S10 the mixed-root D12 fixture (independent recomputation)")
    cert = json.loads((ROOT / "cases/ggv_8_28_upper_endpoint_q1_post_d11_d12"
                              "_obstruction_20260828/RESULT.json").read_text()
                      )["characteristic_certificate"]

    def dec(o):
        if not o:
            return []
        n = max(map(int, o)) + 1
        c = [Fr(0)] * n
        for kk, v in o.items():
            c[int(kk)] = Fr(v)
        while c and c[-1] == 0:
            c.pop()
        return c

    A = [Fr(-1), Fr(0), Fr(0), Fr(0), Fr(1)]
    C = [Fr(-1), Fr(1)]
    B = [Fr(1), Fr(1), Fr(1), Fr(1)]
    V0 = [Fr(-2), Fr(0), Fr(0), Fr(-4), Fr(6)]
    Nred = dec(cert["reduced_numerator"])
    den = dec(cert["reduced_denominator_without_scalar_12"])
    sN = dec(cert["bezout_mod_B"]["Nred_cofactor"])
    tB = dec(cert["bezout_mod_B"]["B_cofactor"])
    one = [Fr(1)]
    check("C*B = A and B = (X+1)(X^2+1) has three simple roots -1, +-i",
          pmul(C, B) == A
          and pmul([Fr(1), Fr(1)], [Fr(1), Fr(0), Fr(1)]) == B
          and pgcd(B, pder(B)) == one)
    check("serialized denominator equals C^3*B^2 = C*A^2",
          den == pmul(pmul(C, pmul(C, C)), pmul(B, B)) == pmul(C, pmul(A, A)))
    check("Bezout identity s*Nred + t*B = 1 rechecked",
          pad(pmul(sN, Nred), pmul(tB, B)) == one)
    check("gcd(B,V0)=gcd(B,Nred)=gcd(B,C)=gcd(A,A')=1: every B-root is a"
          " SIMPLE V0-unit root of A",
          pgcd(B, V0) == one and pgcd(B, Nred) == one
          and pgcd(B, C) == one and pgcd(A, pder(A)) == one)
    check("pole order at each B-root is EXACTLY 2 (ord den = 2, ord Nred = 0)",
          all(pev(den, r) == 0 and pev(Nred, r) != 0 for r in (-1,))
          and pgcd(B, Nred) == one and pgcd(B, C) == one)
    check("literal local data at alpha=-1: A'=-4, V0=8, C=-2,"
          " H(0,s)=(16+4s)^2, Nred=-3969/4096",
          pev(pder(A), -1) == -4 and pev(V0, -1) == 8 and pev(C, -1) == -2
          and pev(Nred, -1) == Fr(-3969, 4096))
    check("Nred at the C-root X=1 recomputed as -12 (matches the record)",
          pev(Nred, 1) == Fr(-12) == Fr(cert["Nred_at_C_root_X1"]))
    # cross-validation against the locally derived D12 normal form:
    #   polar(gbar_12)*A^2 = (3/8) Delta6bar^2 and g12 = nu^12 gbar_12,
    # so at alpha=-1  Nred/(12*C) = (3/8)*nu^12*Delta6bar^2 must be
    # 3*nu^12/8 times a SQUARE.
    coeff = pev(Nred, -1) / (12 * pev(C, -1))
    dsq = coeff / (Fr(3, 8) * Fr(8) ** 12)
    root = Fr(21, 2 ** 24)
    check("cross-validation: the fixture's A^-2 coefficient at the B-root -1"
          " equals (3/8)*V0^12*Delta6bar^2 with Delta6bar = +-21/2^24"
          " exactly as the locally derived normal form demands",
          dsq == root * root, f"Delta6bar^2 = {dsq}")
    note("Nred itself is REPLAY-ONLY here (not recomputed from the fixture's "
         "F/G data); every structural consequence drawn from it is recomputed. "
         "The fixture is used only in the charged section 5 illustration and "
         "is not a premise of sections 1-4.")


def main():
    print("Opus 5 hostile-review checker: unit-root transport to D22")
    print("=" * 72)
    for fn in (s1_custody, s2_raw, s3_newton, s4_valuations, s5_normalization,
               s6_raw_row, s7_ladder, s7_mutations, s8_endpoint,
               s9_prefix_gap, s10_d12):
        fn()
    print("=" * 72)
    if FAILURES:
        print(f"RESULT: {len(FAILURES)} FAILED CHECK(S): {FAILURES}")
        return 1
    print("RESULT: ALL CHECKS PASSED")
    print(f"        {len(NOTES)} reviewer notes recorded above")
    return 0


if __name__ == "__main__":
    sys.exit(main())
