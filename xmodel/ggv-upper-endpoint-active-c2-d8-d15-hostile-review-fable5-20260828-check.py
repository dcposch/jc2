#!/usr/bin/env python3
"""Fable 5 hostile audit of the active-c2 D8..D15 repair/extension (2026-08-28).

Fully self-contained, standard-library only.  This file reimplements from
scratch: sparse Laurent-in-A arithmetic over commutative symbol words, the
fractional-power characteristic recurrence solved from F*ydot = e*Fdot*y,
all ten characteristic modes c2,...,c20 with exponents (12-m)/8, exact
univariate polynomial/rational replay, and the determinant rows.  Nothing is
imported from any producer checker; producer files are only hash-pinned.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
CASE = ROOT / ("cases/ggv_8_28_upper_endpoint_active_c2_d8_d15_hostile_review_"
               "fable5_20260828")
RESULT_PATH = CASE / "RESULT.json"

FROZEN = {
    "cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/"
    "verify_q1_prefix_target.py":
        "fceb189badafad877c1142b8925480516111790707954d2000421b8190fde119",
    "xmodel/ggv-upper-endpoint-active-c2-d8-d11-prefix-sol-ultra-20260828.md":
        "e3b777f851dcb49c1a2caeafa3048fd20771319ecd9f74e8ca74321602b4d1f6",
    "xmodel/ggv-upper-endpoint-active-c2-d8-d11-prefix-sol-ultra-20260828"
    "-check.py":
        "00111feefcddd0532aa70204b69d90e5943b3e08b5ef7d97b44fcfa62f5b0372",
    "xmodel/ggv-upper-endpoint-active-c2-d8-d13-independent-audit-extension"
    "-20260828.md":
        "da189b7fa2ce12656dfbd965c2ed76a0f26b90255a4c99e0fa1322d0c98d5577",
    "cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/"
    "verify_active_c2_extension.py":
        "112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26",
    "cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/"
    "README.md":
        "c4c2263ec64f1a41ee0ae0f25a1fd5403a53a69041d9933950a300318ea60d2e",
    "cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/"
    "RESULT.json":
        "568934cecfd224cfdff6f8af0791f71f54426ccc0fc5384fc4d0d90a2712c02e",
}


def check_frozen():
    for rel, expected in FROZEN.items():
        actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        assert actual == expected, f"frozen input drifted: {rel}"


# ---------------------------------------------------------------------------
# Sparse Laurent-in-A arithmetic.  A key is (A_exponent, sorted symbol word).
# ---------------------------------------------------------------------------

def lt(coefficient=1, a=0, *word):
    coefficient = Q(coefficient)
    return {(a, tuple(sorted(word))): coefficient} if coefficient else {}


def ladd(*items):
    out = {}
    for item in items:
        for key, value in item.items():
            out[key] = out.get(key, Q(0)) + value
            if not out[key]:
                del out[key]
    return out


def lscale(coefficient, item):
    coefficient = Q(coefficient)
    return {key: coefficient * value for key, value in item.items()
            if coefficient * value}


def lmul(left, right):
    out = {}
    for (la, lw), lc in left.items():
        for (ra, rw), rc in right.items():
            key = (la + ra, tuple(sorted(lw + rw)))
            out[key] = out.get(key, Q(0)) + lc * rc
            if not out[key]:
                del out[key]
    return out


def lprod(*items):
    out = lt(1)
    for item in items:
        out = lmul(out, item)
    return out


def lpow(item, exponent):
    return lprod(*(item for _ in range(exponent)))


def lshift(a, item):
    return {(old + a, word): value for (old, word), value in item.items()}


def lsub(item, replacements):
    out = {}
    for (a, word), coefficient in item.items():
        piece = lt(coefficient, a)
        for name in word:
            piece = lmul(piece, replacements.get(name, lt(1, 0, name)))
        out = ladd(out, piece)
    return out


def lneg_part(item):
    return {key: value for key, value in item.items() if key[0] < 0}


def lat(item, a):
    return {key: value for key, value in item.items() if key[0] == a}


def lminpow(item):
    return min((key[0] for key in item), default=0)


def lsyms(item):
    return sorted({name for (_, word) in item for name in word})


def l_encode(item):
    return [[a, list(word), str(value)]
            for (a, word), value in sorted(item.items())]


def l_sha(item):
    return hashlib.sha256(json.dumps(
        l_encode(item), sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def lval(item, values):
    """Evaluate an A-free symbolic class at rational scalars."""
    total = Q(0)
    for (a, word), coefficient in item.items():
        assert a == 0, "scalar evaluation requires an A-free class"
        piece = coefficient
        for name in word:
            piece *= Q(values[name])
        total += piece
    return total


# ---------------------------------------------------------------------------
# Characteristic recurrence.  Derived independently: with F = sum F_n t^n,
# F_0 = A^4, and y = F^e, t-differentiation gives F*ydot = e*Fdot*y, whose
# t^(n-1) coefficient is  n*F_0*Y_n = sum_{i=1}^{n} ((e+1)i - n) F_i Y_{n-i}.
# ---------------------------------------------------------------------------

MODE_BIRTHS = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)


def mode_exponent(m):
    return Q(12 - m, 8)


EXPECTED_MODE_TABLE = {
    2: Q(5, 4), 4: Q(1), 6: Q(3, 4), 8: Q(1, 2), 10: Q(1, 4),
    12: Q(0), 14: Q(-1, 4), 16: Q(-1, 2), 18: Q(-3, 4), 20: Q(-1),
}


def frac_series(F, e, nmax):
    lead = 4 * e
    assert lead.denominator == 1
    y = {0: lt(1, int(lead))}
    for n in range(1, nmax + 1):
        numerator = {}
        for i in range(1, n + 1):
            numerator = ladd(
                numerator,
                lscale((e + 1) * i - n, lmul(F[i], y[n - i])),
            )
        y[n] = lscale(Q(1, n), lshift(-4, numerator))
    return y


def characteristic(F, nmax, exponents=None):
    table = dict(exponents) if exponents else {
        m: mode_exponent(m) for m in MODE_BIRTHS}
    powers = {e: frac_series(F, e, nmax)
              for e in set(table.values()) | {Q(3, 2)}}
    G = {}
    for n in range(nmax + 1):
        row = powers[Q(3, 2)][n]
        for m, e in table.items():
            if m <= n:
                row = ladd(row, lmul(lt(1, 0, f"c{m}"), powers[e][n - m]))
        G[n] = row
    return G


def general_F(nmax):
    F = {
        0: lt(1, 4),
        1: lt(1, 2, "v0"),
        2: lscale(Q(1, 4), ladd(lt(1, 0, "v0", "v0"), lt(1, 2, "z"))),
        3: lscale(Q(1, 8), ladd(lt(1, 0, "v0", "z"), lt(1, 1, "t"))),
    }
    for n in range(4, nmax + 1):
        F[n] = lt(1, 0, f"f{n}")
    return F


# ---------------------------------------------------------------------------
# Exact univariate polynomials over Q, coefficient list, index = degree.
# ---------------------------------------------------------------------------

def ptrim(poly):
    out = list(poly)
    while out and not out[-1]:
        out.pop()
    return out


def padd(*items):
    out = []
    for poly in items:
        size = max(len(out), len(poly))
        out = ptrim([
            (out[i] if i < len(out) else Q(0))
            + (poly[i] if i < len(poly) else Q(0))
            for i in range(size)])
    return out


def pscale(coefficient, poly):
    return ptrim([Q(coefficient) * value for value in poly])


def pmul(left, right):
    if not left or not right:
        return []
    out = [Q(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return ptrim(out)


def ppow(poly, exponent):
    out = [Q(1)]
    for _ in range(exponent):
        out = pmul(out, poly)
    return out


def pdiff(poly):
    return ptrim([Q(i) * poly[i] for i in range(1, len(poly))])


def pdivmod(dividend, divisor):
    divisor, remainder = ptrim(divisor), ptrim(dividend)
    assert divisor
    quotient = [Q(0)] * max(0, len(remainder) - len(divisor) + 1)
    while remainder and len(remainder) >= len(divisor):
        degree = len(remainder) - len(divisor)
        factor = remainder[-1] / divisor[-1]
        quotient[degree] += factor
        remainder = padd(
            remainder,
            pscale(-1, [Q(0)] * degree + pscale(factor, divisor)))
    return ptrim(quotient), ptrim(remainder)


def eval_fraction(item, A, assign):
    """Evaluate a Laurent class to (numerator, k) meaning numerator/A^k."""
    surviving = []
    for (a, word), coefficient in item.items():
        piece = [Q(coefficient)]
        for name in word:
            piece = pmul(piece, assign[name])
            if not piece:
                break
        if piece:
            surviving.append((a, piece))
    if not surviving:
        return [], 0
    k = max(0, -min(a for a, _ in surviving))
    numerator = []
    for a, piece in surviving:
        numerator = padd(numerator, pmul(piece, ppow(A, a + k)))
    return numerator, k


def polar_remainder(item, A, assign):
    numerator, k = eval_fraction(item, A, assign)
    if not numerator or k == 0:
        return []
    _, remainder = pdivmod(numerator, ppow(A, k))
    return remainder


def eval_polynomial(item, A, assign):
    numerator, k = eval_fraction(item, A, assign)
    if not numerator:
        return []
    quotient, remainder = pdivmod(numerator, ppow(A, k))
    assert not remainder, "polar failure in polynomial evaluation"
    return quotient


def determinant_rows(F, G, nmax):
    rows = {}
    for n in range(nmax + 1):
        row = []
        for i in range(n + 1):
            j = n - i
            row = padd(
                row,
                pscale(12 - j, pmul(pdiff(F[i]), G[j])),
                pscale(i - 8, pmul(F[i], pdiff(G[j]))))
        rows[n] = row
    return rows


def rational_rows(F, G_fraction, A, nmax):
    """Determinant rows for G_n given as (numerator, k); denominators cleared."""
    K = max((k for _, k in G_fraction.values()), default=0)
    M = {n: pmul(numerator, ppow(A, K - k))
         for n, (numerator, k) in G_fraction.items()}
    A_x = pdiff(A)
    rows = {}
    for n in range(nmax + 1):
        total = []
        for i in range(n + 1):
            j = n - i
            derivative = padd(pmul(pdiff(M[j]), A),
                              pscale(-K, pmul(A_x, M[j])))
            total = padd(
                total,
                pscale(12 - j, pmul(pmul(pdiff(F[i]), M[j]), A)),
                pscale(i - 8, pmul(F[i], derivative)))
        rows[n] = total
    return rows


# ---------------------------------------------------------------------------
# Main audit.
# ---------------------------------------------------------------------------

def audit():
    result = {"format": "GGV_UPPER_ACTIVE_C2_D8_D15_HOSTILE_REVIEW_FABLE5_V1"}
    check_frozen()
    result["frozen_inputs_sha256"] = dict(FROZEN)

    # -- A. modes and recurrence -------------------------------------------
    derived = {m: mode_exponent(m) for m in MODE_BIRTHS}
    assert derived == EXPECTED_MODE_TABLE
    result["modes"] = {str(m): str(e) for m, e in derived.items()}

    G = characteristic(general_F(15), 15)

    # Birth census: c_m first appears exactly at row m; nothing is deleted.
    for m in MODE_BIRTHS:
        if m <= 15:
            assert f"c{m}" in lsyms(G[m]), f"mode c{m} missing at birth row"
            assert f"c{m}" not in lsyms(G[m - 1])
    present = [f"c{m}" for m in MODE_BIRTHS if m <= 15
               and f"c{m}" in lsyms(G[15])]
    assert present == ["c2", "c4", "c6", "c8", "c10", "c14"]
    # c12 multiplies F^0 = 1 exactly: its only appearance is the constant at
    # row 12 (all higher F^0 coefficients vanish in the recurrence).
    assert {key: value for key, value in G[12].items()
            if "c12" in key[1]} == lt(1, 0, "c12")
    result["row_census"] = {
        str(n): {"terms": len(G[n]), "sha256": l_sha(G[n]),
                 "min_A_power": lminpow(G[n])}
        for n in range(8, 16)}

    # Generic rational control: the determinant rows vanish identically for
    # the full ten-mode characteristic solution.  This certifies that the
    # reconstructed recurrence solves the determinant equation, independent
    # of every producer implementation.
    A_g = [Q(-2), Q(0), Q(0), Q(0), Q(1)]
    assign_g = {
        "v0": [Q(1), Q(1)], "z": [Q(2), Q(0), Q(1)], "t": [Q(0), Q(1)],
        "f4": [Q(1)], "f5": [Q(0), Q(1)], "f6": [Q(1), Q(1)], "f7": [Q(2)],
        "f8": [Q(1)], "f9": [Q(3)], "f10": [Q(1)], "f11": [Q(1)],
        "f12": [Q(2)], "f13": [Q(1)], "f14": [Q(1)], "f15": [Q(1)],
        **{f"c{m}": [Q(1)] for m in MODE_BIRTHS},
    }

    def raw_F_from(assign, A):
        A2 = ppow(A, 2)
        F = {
            0: ppow(A, 4),
            1: pmul(A2, assign["v0"]),
            2: pscale(Q(1, 4), padd(pmul(assign["v0"], assign["v0"]),
                                    pmul(A2, assign["z"]))),
            3: pscale(Q(1, 8), padd(pmul(assign["v0"], assign["z"]),
                                    pmul(A, assign["t"]))),
        }
        for n in range(4, 16):
            F[n] = assign[f"f{n}"]
        return F

    fraction_g = {n: eval_fraction(G[n], A_g, assign_g) for n in range(16)}
    rows_g = rational_rows(raw_F_from(assign_g, A_g), fraction_g, A_g, 15)
    assert all(not rows_g[n] for n in range(16)), "generic determinant control"
    result["generic_determinant_control"] = {
        "A": "X^4-2", "all_rows_0_to_15_zero": True,
        "all_ten_modes_nonzero": True}

    # Mutation M7: a wrong mode exponent breaks the determinant identity.
    wrong_table = {m: mode_exponent(m) for m in MODE_BIRTHS}
    wrong_table[14] = Q(-1, 2)
    G_wrong = characteristic(general_F(15), 15, wrong_table)
    fraction_w = {n: eval_fraction(G_wrong[n], A_g, assign_g)
                  for n in range(16)}
    rows_w = rational_rows(raw_F_from(assign_g, A_g), fraction_w, A_g, 15)
    assert all(not rows_w[n] for n in range(14))
    assert rows_w[14], "wrong c14 exponent must break row 14"
    result["mutation_wrong_mode_exponent"] = {
        "c14_exponent": "-1/2 instead of -1/4",
        "rows_0_to_13": "still zero", "row_14": "nonzero as required"}

    # -- B. charged D8..D11 identities -------------------------------------
    s, u, z = lt(1, 0, "s"), lt(1, 0, "u"), lt(1, 0, "z")
    r, q, p1 = lt(1, 0, "r"), lt(1, 0, "q"), lt(1, 0, "p1")
    c2 = lt(1, 0, "c2")
    f4, f5, f6, f7 = (lt(1, 0, name) for name in ("f4", "f5", "f6", "f7"))

    active = {"v0": lt(1, 1, "s"), "t": lt(1, 1, "u")}
    for n in range(8):
        assert not lneg_part(lsub(G[n], active)), f"unexpected pole at D{n}"

    K = ladd(lscale(64, f4), lscale(-1, lmul(z, z)))
    row8 = lsub(G[8], active)
    assert lminpow(row8) == -2
    assert lat(row8, -2) == lscale(Q(3, 32768), lshift(-2, lmul(K, K)))

    f4_K = lscale(Q(1, 64), ladd(lmul(z, z), lt(1, 1, "r")))
    assert lsub(K, {"f4": f4_K}) == lt(1, 1, "r")
    H = ladd(lmul(s, s), lscale(-2, z))
    subs_K = dict(active, f4=f4_K)
    assert lneg_part(lsub(G[8], subs_K)) == lscale(
        Q(-5, 65536), lshift(-1, lmul(c2, lpow(H, 3))))

    z_q = lscale(Q(1, 2), ladd(lmul(s, s), lt(-1, 1, "q")))
    assert lsub(H, {"z": z_q}) == lt(1, 1, "q")
    f4_H = lscale(Q(1, 64), ladd(lmul(z_q, z_q), lt(1, 1, "r")))
    subs_H = {"v0": lt(1, 1, "s"), "t": lt(1, 1, "u"), "z": z_q, "f4": f4_H}
    for n in range(9):
        assert not lneg_part(lsub(G[n], subs_H)), f"pole at D{n} after H lift"

    D_ = ladd(r, lscale(-4, lmul(s, u)))
    P_ = ladd(lscale(256, f5), lscale(-1, lmul(r, s)),
              lscale(2, lprod(s, s, u)))
    row9 = lsub(G[9], subs_H)
    assert lminpow(row9) == -1
    assert lneg_part(row9) == lscale(Q(3, 65536), lshift(-1, lmul(D_, P_)))
    row10 = lsub(G[10], subs_H)
    assert lminpow(row10) == -2
    assert lat(row10, -2) == lscale(
        Q(3, 524288),
        lshift(-2, lmul(P_, ladd(P_, lscale(-2, lmul(s, D_))))))

    # Rootwise anchors for the D9/D10 repair A|P: numerators 3DP and
    # 3P(P-2SD) at scalars.  D=0 with P!=0 passes D9 but not the deepest
    # D10; P=0 passes both.  So each root of A forces P=0.
    n9 = lscale(3, lmul(D_, P_))
    n10 = lscale(3, lmul(P_, ladd(P_, lscale(-2, lmul(s, D_)))))
    branch_D = {"r": 4, "s": 1, "u": 1, "f5": Q(1, 256)}
    assert lval(n9, branch_D) == 0 and lval(n10, branch_D) == 3
    branch_P = {"r": 5, "s": 1, "u": 1, "f5": Q(3, 256)}
    assert lval(n9, branch_P) == 0 and lval(n10, branch_P) == 0
    result["charged_D8_D11"] = {
        "deepest_D8": "3K^2/(32768A^2) CONFIRMED complete at A^-2",
        "residual_D8": "-5c2(S^2-2Z)^3/(65536A) CONFIRMED complete",
        "D9": "3DP/(65536A) CONFIRMED complete",
        "deepest_D10": "3P(P-2SD)/(524288A^2) CONFIRMED complete at A^-2",
        "rootwise_A_divides_P": "anchors PASS: D=0,P!=0 dies at deep D10",
    }

    f5_P = lscale(Q(1, 256), ladd(lmul(r, s), lscale(-2, lprod(s, s, u)),
                                  lt(1, 1, "p1")))
    assert lsub(P_, {"f5": f5_P}) == lt(1, 1, "p1")
    subs_P = dict(subs_H, f5=f5_P)
    for n in range(10):
        assert not lneg_part(lsub(G[n], subs_P)), f"pole at D{n} after P lift"

    E_general = ladd(lscale(2048, f6), lscale(-2, lmul(s, p1)),
                     lmul(q, ladd(r, lscale(-8, lmul(s, u)))),
                     lscale(-8, lmul(u, u)))
    row10r = lsub(G[10], subs_P)
    assert lneg_part(row10r) == lscale(
        Q(1, 524288),
        lshift(-1, lmul(D_, ladd(lscale(20, lmul(c2, D_)),
                                 lscale(3, E_general)))))

    r6 = ladd(r, lscale(-6, lmul(s, u)))
    B11 = ladd(
        lscale(-10, lprod(c2, s, D_)), lscale(-3072, lmul(f6, s)),
        lscale(3, lprod(p1, s, s)),
        lscale(-3, lprod(q, s, r6)), lscale(-6, lmul(u, r6)))
    row11 = lsub(G[11], subs_P)
    assert lminpow(row11) == -2
    assert lat(row11, -2) == lscale(Q(1, 1048576),
                                    lshift(-2, lmul(D_, B11)))
    result["charged_D8_D11"]["residual_D10"] = \
        "D(20c2D+3Egen)/(524288A) CONFIRMED complete"
    result["charged_D8_D11"]["deepest_D11"] = \
        "D*B11/(1048576A^2) CONFIRMED complete at A^-2, B11 as displayed"

    # -- B/C. the valuation defect: A|D is NOT the exact equation D=0 ------
    r_ad = ladd(lscale(4, lmul(s, u)), lt(1, 1, "d1"))
    subs_AD = {
        "v0": lt(1, 1, "s"), "t": lt(1, 1, "u"), "z": z_q,
        "f4": lscale(Q(1, 64), ladd(lmul(z_q, z_q), lshift(1, r_ad))),
        "f5": lscale(Q(1, 256), ladd(lmul(r_ad, s),
                                     lscale(-2, lprod(s, s, u)),
                                     lt(1, 1, "p1"))),
    }
    E_ = ladd(lscale(2048, f6), lscale(-2, lmul(s, p1)),
              lscale(-4, lprod(q, s, u)), lscale(-8, lmul(u, u)))
    assert lsub(E_general, {"r": lscale(4, lmul(s, u))}) == E_
    L_ = ladd(lmul(q, s), lscale(4, u))
    M_ = ladd(p1, lscale(2, lmul(q, u)))
    N11 = ladd(
        lscale(5, lprod(c2, L_, ladd(lscale(4, E_), lmul(L_, L_)))),
        lscale(6, lmul(E_, M_)))
    B11_r0 = lsub(B11, {"r": lscale(4, lmul(s, u))})
    assert B11_r0 == ladd(lscale(-3072, lmul(f6, s)),
                          lscale(3, lprod(p1, s, s)),
                          lscale(6, lprod(q, s, s, u)),
                          lscale(12, lprod(s, u, u)))
    row11_ad = lsub(G[11], subs_AD)
    neg_ad = lneg_part(row11_ad)
    assert lminpow(row11_ad) == -1
    predicted = ladd(
        lscale(Q(1, 4194304), lshift(-1, N11)),
        lscale(Q(1, 1048576), lshift(-1, lmul(lt(1, 0, "d1"), B11_r0))))
    assert neg_ad == predicted, "closed form of the A|D residual pole"
    d1_part = {key: value for key, value in neg_ad.items()
               if "d1" in key[1]}
    assert d1_part, "A|D leaves a genuine d1-dependent simple pole"
    result["valuation_defect"] = {
        "charged_claim": "the branch D=0 mod A survives the deepest D11",
        "status": "REFUTED (confirming the extension's repair)",
        "exact_residual": (
            "with D=A*d1, g11^- = (N11 + 4*d1*B11r0)/(4194304*A), "
            "B11r0 = -3072F6S+3P1S^2+6QS^2U+12SU^2"),
        "impact": (
            "A|D alone survives deepest D11 only on the extra codimension "
            "condition N11+4*d1*B11r0 = 0 mod A; it is not automatic"),
    }

    # -- C. exact D=0 paired forcing ---------------------------------------
    subs_D0 = {name: lsub(item, {"d1": {}})
               for name, item in subs_AD.items()}
    for n in range(11):
        assert not lneg_part(lsub(G[n], subs_D0)), f"pole at D{n} on D=0"
    row11_d0 = lsub(G[11], subs_D0)
    assert lneg_part(row11_d0) == lscale(Q(1, 4194304), lshift(-1, N11))
    row12_d0 = lsub(G[12], subs_D0)
    assert lminpow(row12_d0) == -2
    assert lat(row12_d0, -2) == lscale(
        Q(1, 33554432),
        lshift(-2, ladd(lscale(3, lmul(E_, E_)),
                        lscale(-2, lmul(s, N11)))))
    # Rootwise: N11=0 and 3E^2-2S*N11=0 give 3E^2=0, so E=0 (char 0);
    # then N11 = 5c2*L^3 = 0 and c2 != 0 (char != 5) give L=0.  Scalar
    # anchor: E=0, L=1, c2=1 leaves N11 = 5.
    assert lval(lsub(N11, {"f6": lscale(Q(1, 2048), ladd(
        lscale(2, lmul(s, p1)), lscale(4, lprod(q, s, u)),
        lscale(8, lmul(u, u))))}),  # forces E=0 identically
        {"q": 1, "s": 1, "u": 0, "p1": 1, "c2": 1}) == 5
    result["exact_D0_forcing"] = {
        "complete_D11": "N11/(4194304A) CONFIRMED complete negative part",
        "deepest_D12": "(3E^2-2S*N11)/(33554432A^2) CONFIRMED at A^-2",
        "field_radical": (
            "at each root of squarefree A over char-0: N11=0 and 3E^2=0 "
            "force E=0, then N11=5c2L^3 forces L=0 on c2!=0; distinct "
            "roots give A|E and A|L; units used: 3, 5, c2 only"),
    }

    # -- D. post-lift D12/D13 ----------------------------------------------
    u_L = lscale(Q(1, 4), ladd(lt(1, 1, "el"), lscale(-1, lmul(q, s))))
    assert lsub(L_, {"u": u_L}) == lt(1, 1, "el")
    f6_E = lscale(Q(1, 2048), ladd(
        lt(1, 1, "e1"), lscale(2, lmul(s, p1)),
        lscale(4, lprod(q, s, u_L)), lscale(8, lmul(u_L, u_L))))
    assert lsub(E_, {"u": u_L, "f6": f6_E}) == lt(1, 1, "e1")
    r_L = lscale(4, lmul(s, u_L))
    subs_L = {
        "v0": lt(1, 1, "s"), "t": lshift(1, u_L), "z": z_q,
        "f4": lscale(Q(1, 64), ladd(lmul(z_q, z_q), lshift(1, r_L))),
        "f5": lscale(Q(1, 256), ladd(lmul(r_L, s),
                                     lscale(-2, lprod(s, s, u_L)),
                                     lt(1, 1, "p1"))),
        "f6": f6_E,
    }
    for n in range(12):
        assert not lneg_part(lsub(G[n], subs_L)), f"pole at D{n} post-lift"
    J_ = ladd(p1, lscale(Q(-1, 2), lprod(s, q, q)))
    N_ = ladd(lscale(8192, f7), lscale(-1, lmul(lt(1, 0, "e1"), s)),
              lmul(q, J_))
    rung12 = lmul(J_, ladd(lscale(20, lmul(c2, J_)), lscale(3, N_)))
    row12_l = lsub(G[12], subs_L)
    assert lneg_part(row12_l) == lscale(Q(1, 8388608), lshift(-1, rung12))
    row13_l = lsub(G[13], subs_L)
    assert lminpow(row13_l) == -2
    assert lat(row13_l, -2) == lscale(Q(-1, 33554432),
                                      lshift(-2, lmul(s, rung12)))
    subleading13 = lat(row13_l, -1)
    result["postlift_D12_D13"] = {
        "D11_poles": "all vanish after E=A*e1, L=A*ell",
        "complete_D12": "J(20c2J+3N)/(8388608A) CONFIRMED complete",
        "deepest_D13": "-S*J(20c2J+3N)/(33554432A^2) CONFIRMED entire A^-2",
        "subleading_D13_symbols": lsyms(subleading13),
        "subleading_D13_terms": len(subleading13),
    }

    # -- F. separate c2=0 companion ----------------------------------------
    subs_c0 = {"v0": lt(1, 1, "s"), "t": lt(1, 1, "u"),
               "f4": f4_K, "c2": {}}
    for n in range(9):
        assert not lneg_part(lsub(G[n], subs_c0)), f"pole at D{n}, c2=0"
    P0 = ladd(lscale(256, f5), lscale(-1, lmul(r, s)),
              lscale(2, lprod(s, s, u)), lscale(2, lmul(u, H)))
    row9_c0 = lsub(G[9], subs_c0)
    assert lminpow(row9_c0) == -1
    assert lneg_part(row9_c0) == lscale(Q(3, 65536),
                                        lshift(-1, lmul(D_, P0)))
    row10_c0 = lsub(G[10], subs_c0)
    assert lminpow(row10_c0) == -2
    assert lat(row10_c0, -2) == lscale(
        Q(3, 524288),
        lshift(-2, ladd(lmul(P0, ladd(P0, lscale(-2, lmul(s, D_)))),
                        lprod(H, D_, D_))))
    # Rootwise anchors: D=0,P0!=0 dies at deep D10 (forces P0=0);
    # P0=0,D!=0,H!=0 dies (forces per-root H=0 or D=0); P0=0,H=0 survives.
    n9c = lmul(D_, P0)
    n10c = ladd(lmul(P0, ladd(P0, lscale(-2, lmul(s, D_)))),
                lprod(H, D_, D_))
    a1 = {"r": 4, "s": 1, "u": 1, "z": 0, "f5": Q(1, 256)}
    assert lval(n9c, a1) == 0 and lval(n10c, a1) == 1
    a2 = {"r": 5, "s": 1, "u": 1, "z": 0, "f5": Q(1, 256)}
    assert lval(n9c, a2) == 0 and lval(n10c, a2) == 1
    a3 = {"r": 5, "s": 1, "u": 1, "z": Q(1, 2), "f5": Q(3, 256)}
    assert lval(n9c, a3) == 0 and lval(n10c, a3) == 0
    result["c2_zero_companion"] = {
        "D9": "3D*P0/(65536A) CONFIRMED complete",
        "deepest_D10": "3[P0(P0-2SD)+HD^2]/(524288A^2) CONFIRMED at A^-2",
        "field_radical": "A|P0; per-root H*D^2=0 split; NOT merged with c2!=0",
        "anchors": "D-branch and P0-branch scalar controls PASS",
    }
    return result, G


def fixture_audit(result, G):
    # -- E. literal raw D0..D15 survivor -----------------------------------
    A = [Q(-1), Q(0), Q(0), Q(0), Q(1)]
    Z = [Q(1), Q(0), Q(0), Q(0), Q(-1, 2)]
    assert Z == pscale(Q(1, 2), padd([Q(1)], pscale(-1, A)))
    R, U, S_, Qv, P1 = [Q(-1)], [Q(-1, 4)], [Q(1)], [Q(1)], [Q(1, 2)]
    # Branch-consistency of the fixture data.
    assert padd(R, pscale(-4, pmul(S_, U))) == []            # D=0
    assert padd(pmul(S_, S_), pscale(-2, Z)) == A            # H=A*Q, Q=1
    F4 = pscale(Q(1, 64), padd(pmul(Z, Z), pmul(A, R)))      # K=A*R
    F5 = pscale(Q(1, 512), padd(A, [Q(-1)]))
    assert pscale(256, F5) == padd(pmul(R, S_), pscale(-2, pmul(pmul(S_, S_), U)),
                                   pmul(A, P1))              # P=A*P1
    F6 = [Q(1, 4096)]
    # E = 2048F6-2SP1-4QSU-8U^2 = 1/2-1+1-1/2 = 0 and L = QS+4U = 0.
    E_val = Q(2048) * Q(1, 4096) - 2 * Q(1, 2) - 4 * Q(-1, 4) - 8 * Q(1, 16)
    assert E_val == 0
    assert Q(1) + 4 * Q(-1, 4) == 0
    c14_star = Q(-6139, 17179869184)
    assert c14_star.denominator == 2**34

    assign = {
        "v0": A, "t": pscale(Q(-1, 4), A), "z": Z,
        "f4": F4, "f5": F5, "f6": F6,
        **{f"f{n}": [] for n in range(7, 16)},
        "c2": [Q(1)], "c6": [Q(1)], "c14": [c14_star],
        **{f"c{m}": [] for m in (4, 8, 10, 12, 16, 18, 20)},
    }
    raw_G = {}
    for n in range(16):
        raw_G[n] = eval_polynomial(G[n], A, assign)
    A2 = ppow(A, 2)
    raw_F = {
        0: ppow(A, 4), 1: pmul(A2, A),
        2: pscale(Q(1, 4), padd(pmul(A, A), pmul(A2, Z))),
        3: pscale(Q(1, 8), padd(pmul(A, Z), pmul(A, pscale(Q(-1, 4), A)))),
        4: F4, 5: F5, 6: F6, **{n: [] for n in range(7, 16)},
    }
    rows = determinant_rows(raw_F, raw_G, 15)
    assert all(not rows[n] for n in range(16)), "literal D0..D15"
    for n in range(1, 16):
        assert len(raw_F[n]) - 1 <= 16 - n
        assert len(raw_G[n]) - 1 <= 24 - n
    assert len(raw_F[0]) - 1 == 16 and len(raw_G[0]) - 1 == 24
    assert raw_G[12] == [Q(4093, 268435456)]
    assert raw_G[13] == [] and raw_G[14] == [] and raw_G[15] == []

    # D14 uniquely forces c14: the weight-14 class is affine in c14 and its
    # polar residue has a unique legal root, the displayed nonzero scalar.
    c14_terms = {key: value for key, value in G[14].items()
                 if "c14" in key[1]}
    rest_terms = {key: value for key, value in G[14].items()
                  if "c14" not in key[1]}
    unit_assign = dict(assign, c14=[Q(1)])
    numerator_rest, k_rest = eval_fraction(rest_terms, A, assign)
    numerator_c14, k_c14 = eval_fraction(c14_terms, A, unit_assign)
    k = max(k_rest, k_c14)
    Ak = ppow(A, k)
    _, rem_rest = pdivmod(pmul(numerator_rest, ppow(A, k - k_rest)), Ak)
    _, rem_c14 = pdivmod(pmul(numerator_c14, ppow(A, k - k_c14)), Ak)
    assert rem_c14, "c14 must be able to move the weight-14 residue"
    assert rem_rest, "the residue must be nonzero at c14=0 (c14 forced != 0)"
    pivot = next(i for i, value in enumerate(rem_c14) if value)
    solved = -rem_rest[pivot] / rem_c14[pivot]
    assert padd(rem_rest, pscale(solved, rem_c14)) == [], \
        "affine residue must vanish identically at one scalar"
    assert solved == c14_star, "unique forced c14 equals the displayed value"
    result["literal_fixture"] = {
        "A": "X^4-1", "S": "1", "Q": "1", "U": "-1/4", "R": "-1",
        "P1": "1/2", "Z": "1-X^4/2", "c2": "1", "c6": "1",
        "c14_forced_unique": str(c14_star),
        "D0_to_D15": "all zero as literal polynomials",
        "windows": "deg F_n <= 16-n and deg G_n <= 24-n for n=1..15",
        "G12": "4093/268435456", "G13_G14_G15": "0",
    }

    # q1-freeness: no R0 with deg <= 4 solves A'*R0 + 2*A*R0' = V0 = A.
    columns = []
    for i in range(5):
        base = [Q(0)] * i + [Q(1)]
        columns.append(padd(pmul(pdiff(A), base),
                            pscale(2, pmul(A, pdiff(base)))))
    target = A
    size = max([len(c) for c in columns] + [len(target)])
    matrix = [[(columns[j][d] if d < len(columns[j]) else Q(0))
               for j in range(5)]
              + [(target[d] if d < len(target) else Q(0))]
              for d in range(size)]
    rank_row = 0
    for col in range(5):
        pivot_row = next((row for row in range(rank_row, size)
                          if matrix[row][col]), None)
        if pivot_row is None:
            continue
        matrix[rank_row], matrix[pivot_row] = (matrix[pivot_row],
                                               matrix[rank_row])
        pivot_value = matrix[rank_row][col]
        matrix[rank_row] = [value / pivot_value
                            for value in matrix[rank_row]]
        for row in range(size):
            if row != rank_row and matrix[row][col]:
                factor = matrix[row][col]
                matrix[row] = [a - factor * b for a, b
                               in zip(matrix[row], matrix[rank_row])]
        rank_row += 1
    inconsistent = any(all(not value for value in row[:5]) and row[5]
                       for row in matrix)
    assert inconsistent, "fixture must not lie on q1 (V0=A'R0+2AR0')"
    result["literal_fixture"]["q1_free"] = (
        "VERIFIED: the linear system A'R0+2AR0'=A, deg R0<=4, is "
        "inconsistent over Q")

    # -- E. sensitivity mutations ------------------------------------------
    mutations = {}
    # M1: wrong D8 factor or coefficient is caught by the equality checks.
    K2_class = lscale(Q(3, 32768), lshift(-2, lpow(ladd(
        lscale(64, lt(1, 0, "f4")), lscale(-1, lt(1, 0, "z", "z"))), 2)))
    wrong_factor = lscale(Q(3, 32768), lshift(-2, ladd(
        lscale(64, lt(1, 0, "f4")), lscale(-1, lt(1, 0, "z", "z")))))
    wrong_scale = lscale(Q(1, 2), K2_class)
    assert K2_class != wrong_factor and K2_class != wrong_scale
    mutations["M1_wrong_D8"] = "K-for-K^2 and 3/65536-for-3/32768 both caught"

    # M3: dropping the c6 mode breaks the literal survivor.
    assign_c6 = dict(assign, c6=[])
    first_fail = None
    for n in range(16):
        if polar_remainder(G[n], A, assign_c6):
            first_fail = n
            break
    assert first_fail is not None, "dropping c6 must fail"
    mutations["M3_drop_c6"] = {"first_polar_failure_weight": first_fail}
    # Is c6 forced, or only present?  Re-force c14 under c6=0 and record.
    numerator_rest_c6, k_rest_c6 = eval_fraction(rest_terms, A, assign_c6)
    kk = max(k_rest_c6, k_c14)
    _, rem_rest_c6 = pdivmod(
        pmul(numerator_rest_c6, ppow(A, kk - k_rest_c6)), ppow(A, kk))
    _, rem_c14_kk = pdivmod(
        pmul(numerator_c14, ppow(A, kk - k_c14)), ppow(A, kk))
    rescued = None
    if rem_c14_kk:
        pivot2 = next((i for i, value in enumerate(rem_c14_kk) if value),
                      None)
        if pivot2 is not None and rem_rest_c6:
            candidate = -rem_rest_c6[pivot2] / rem_c14_kk[pivot2]
            if padd(rem_rest_c6, pscale(candidate, rem_c14_kk)) == []:
                retry = dict(assign_c6, c14=[candidate])
                try:
                    for n in range(16):
                        eval_polynomial(G[n], A, retry)
                    rescued = str(candidate)
                except AssertionError:
                    rescued = None
    mutations["M3_drop_c6"]["c14_retune_rescues_D0_D15"] = (
        rescued if rescued is not None else False)

    # M4: wrong c14 leaves the weight-14 pole; forcing is affine and unique.
    for bad in ([], [c14_star + 1]):
        assert polar_remainder(G[14], A, dict(assign, c14=bad)), \
            "wrong c14 must leave a weight-14 pole"
    mutations["M4_wrong_c14"] = (
        "c14=0 and c14=c*+1 both leave the weight-14 pole; unique root c*")

    # M5: perturbing F7 from 0 to 1 gives the exact D13 pole 6139/(8192A).
    assign_f7 = dict(assign, f7=[Q(1)])
    for n in range(13):
        assert not polar_remainder(G[n], A, assign_f7)
    numerator_13, k_13 = eval_fraction(G[13], A, assign_f7)
    _, rem_13 = pdivmod(numerator_13, ppow(A, k_13))
    assert rem_13 == pscale(Q(6139, 8192), ppow(A, k_13 - 1)), \
        "F7 mutation must give exactly the 6139/(8192A) pole"
    mutations["M5_perturb_F7"] = (
        "D0..D12 stay clean; D13 pole is exactly 6139/(8192A) "
        "with c6 retained")

    # M6: deleting a born mode from the recurrence equals setting it to zero.
    table_no_c14 = {m: mode_exponent(m) for m in MODE_BIRTHS if m != 14}
    G_no_c14 = characteristic(general_F(15), 15, table_no_c14)
    rem_deleted = polar_remainder(G_no_c14[14], A, assign)
    rem_zeroed = polar_remainder(G[14], A, dict(assign, c14=[]))
    assert rem_deleted and rem_deleted == rem_zeroed, \
        "mode deletion must fail exactly like c14=0"
    mutations["M6_delete_born_mode_c14"] = (
        "recurrence without the c14 mode leaves the identical weight-14 "
        "pole as c14=0: modes may not be deleted")

    # M2 lives in the symbolic section (A|D residual pole); record it here.
    mutations["M2_A_divides_D_only"] = (
        "with D=A*d1 the full weight-11 negative part is "
        "(N11+4*d1*B11r0)/(4194304A): a surviving simple pole")
    result["mutations"] = mutations
    return result


def main():
    result, G = audit()
    result = fixture_audit(result, G)
    result["verdict"] = "REPAIR"
    result["verdict_detail"] = (
        "charged D8-D11 identities CONFIRMED; the charged claim that "
        "D=0 mod A survives the deepest D11 is REFUTED (the extension's "
        "repair is correct and is the only mathematical defect found in "
        "the charged report); the exact D=0 extension through D15, the "
        "literal survivor, and the c2=0 companion all PASS")
    result["scope"] = (
        "characteristic-zero field points, squarefree quartic A, radical "
        "semantics, plus one literal rational fixture; no scheme "
        "membership, endpoint emptiness, branch-P exclusion, Keller, or "
        "JC2 claim")
    check_frozen()
    CASE.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if RESULT_PATH.exists():
        assert RESULT_PATH.read_text() == encoded, "RESULT.json drift"
    else:
        RESULT_PATH.write_text(encoded)
    print("charged_prefix=D8,D9,D10,D11 identities independently CONFIRMED")
    print("defect=A|D_alone_leaves_(N11+4*d1*B11r0)/(4194304A); exact D=0 "
          "repair CONFIRMED")
    print("extension=R11,R12,R12r,R13 CONFIRMED; c2=0 companion separate")
    print("fixture=D0..D15 zero, windows PASS, c14 forced uniquely, q1-free")
    print("FABLE5_HOSTILE_ACTIVE_C2_D8_D15=REPAIR")


if __name__ == "__main__":
    main()
