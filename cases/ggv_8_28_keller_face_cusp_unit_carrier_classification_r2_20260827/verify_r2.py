#!/usr/bin/env python3
"""Exact R2 verifier for the rootwise cusp unit-carrier classification.

This is deliberately local/formal.  It proves the low-u channel identities
and the first-carrier dichotomy after parametric Morse normalization.  It
does not claim a raw polynomial normal-form compiler or a global E22 image
classification.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent
PINS = {
    "r1_freeze": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/FREEZE.sha256",
        "05cbb5c046f9aa4b89e1104448e77fd38ec3a146d2422bf84773f81d668bfe3c",
    ),
    "r1_report": (
        "xmodel/ggv-8_28-keller-face-cusp-jet-pinning-r1-sol-20260827.md",
        "66121bddbe0b004ad1b8960f896d3691c4dd3963068fbfddb6ad3ba15dda7027",
    ),
    "r1_verifier": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/verify_r1.py",
        "f21f6435796f197376f76fc9c57c50743e9a356614591ce88e41dcfad4c3e5f0",
    ),
    "r1_result": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/RESULT_R1.json",
        "392f6c0c3ca70a35b9b466944c243a927430838abe022eb960d7f2315e1684f3",
    ),
    "r1_readme": (
        "cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/README.md",
        "238f51d031b81be14cbbd6756778efbf742a7471b9247e964d78d9f4b1050781",
    ),
    "r0_hostile_review": (
        "xmodel/ggv-8_28-keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md",
        "171ff47c844331da8971a731c1ffaf20c31ed5b2ba86fdee2d0d81219eb002b0",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# A tiny exact polynomial ring in named indeterminates.  A monomial is a
# sorted tuple of variable names; all expressions below have degree <= 2.
def snorm(terms):
    out = {}
    for monomial, coefficient in terms.items():
        coefficient = Q(coefficient)
        if coefficient:
            monomial = tuple(sorted(monomial))
            out[monomial] = out.get(monomial, Q(0)) + coefficient
    return {m: c for m, c in out.items() if c}


def sconst(value):
    value = Q(value)
    return {} if not value else {(): value}


def svar(name):
    return {(name,): Q(1)}


def sadd(a, b):
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = out.get(monomial, Q(0)) + coefficient
    return snorm(out)


def sneg(a):
    return {m: -c for m, c in a.items()}


def ssub(a, b):
    return sadd(a, sneg(b))


def sscale(a, value):
    value = Q(value)
    return snorm({m: value * c for m, c in a.items()})


def smul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            monomial = tuple(sorted(ma + mb))
            out[monomial] = out.get(monomial, Q(0)) + ca * cb
    return snorm(out)


TMAX = 22
UMAX = 6


def zseries():
    return {}


def series_add(a, b):
    out = dict(a)
    for key, value in b.items():
        out[key] = sadd(out.get(key, {}), value)
        if not out[key]:
            del out[key]
    return out


def series_neg(a):
    return {key: sneg(value) for key, value in a.items()}


def series_sub(a, b):
    return series_add(a, series_neg(b))


def series_scale(a, value):
    return {key: sscale(term, value) for key, term in a.items() if sscale(term, value)}


def series_mul(a, b):
    out = {}
    for (ta, ua), ca in a.items():
        for (tb, ub), cb in b.items():
            key = (ta + tb, ua + ub)
            if key[0] > TMAX or key[1] > UMAX:
                continue
            out[key] = sadd(out.get(key, {}), smul(ca, cb))
            if not out[key]:
                del out[key]
    return out


def series_dt(a):
    out = {}
    for (tn, un), value in a.items():
        if tn:
            out[(tn - 1, un)] = sscale(value, tn)
    return out


def series_du(a):
    out = {}
    for (tn, un), value in a.items():
        if un:
            out[(tn, un - 1)] = sscale(value, un)
    return out


def series_times_t(a):
    return {(tn + 1, un): value for (tn, un), value in a.items() if tn + 1 <= TMAX}


def coeff(a, tn, un):
    return a.get((tn, un), {})


def named(prefix, n):
    return svar(f"{prefix}{n}")


def local_channel_replay():
    # Parametric Morse normal form F=u^2+U(t).  G is kept arbitrary through
    # u^4: W+Vu+Qu^2+Gamma*u^3+R*u^4.  Terms u^4 and above cannot enter the
    # constant, u, or u^2 channels, but R is included to test that fact.
    F = {(0, 2): sconst(1)}
    G = {(0, 3): sconst(1)}
    for n in range(1, TMAX + 1):
        F[(n, 0)] = named("U", n)
        G[(n, 0)] = named("W", n)
        G[(n, 1)] = named("V", n)
        G[(n, 2)] = named("Q", n)
        G[(n, 3)] = named("Gamma", n)
        G[(n, 4)] = named("R", n)

    Fu = series_du(F)
    Ft = series_dt(F)
    Gu = series_du(G)
    Gt = series_dt(G)
    L = series_sub(
        series_sub(series_scale(series_mul(Fu, G), 12), series_scale(series_mul(F, Gu), 8)),
        series_times_t(series_sub(series_mul(Fu, Gt), series_mul(Ft, Gu))),
    )

    def U(n):
        return named("U", n) if 1 <= n <= TMAX else {}

    def V(n):
        return named("V", n) if 1 <= n <= TMAX else {}

    def W(n):
        return named("W", n) if 1 <= n <= TMAX else {}

    def Qc(n):
        return named("Q", n) if 1 <= n <= TMAX else {}

    def Gamma(n):
        if n == 0:
            return sconst(1)
        return named("Gamma", n) if 1 <= n <= TMAX else {}

    for n in range(0, TMAX + 1):
        constant_expected = {}
        u_expected = sscale(W(n), 24 - 2 * n)
        u2_expected = sscale(V(n), 2 * (8 - n))
        for i in range(0, n + 1):
            j = n - i
            constant_expected = sadd(
                constant_expected, sscale(smul(V(i), U(j)), j - 8)
            )
            u_expected = sadd(
                u_expected, sscale(smul(Qc(i), U(j)), 2 * (j - 8))
            )
            u2_expected = sadd(
                u2_expected, sscale(smul(Gamma(i), U(j)), 3 * (j - 8))
            )
        assert coeff(L, n, 0) == constant_expected, ("constant", n)
        assert coeff(L, n, 1) == u_expected, ("u", n)
        assert coeff(L, n, 2) == u2_expected, ("u2", n)

    return {
        "constant": "[t^n u^0]L=sum_(i+j=n) V_i*(j-8)*U_j",
        "u": "[t^n u^1]L=(24-2n)W_n+2*sum_(i+j=n)Q_i*(j-8)*U_j",
        "u2": "[t^n u^2]L=2*(8-n)V_n+3*sum_(i+j=n)Gamma_i*(j-8)*U_j",
        "sidecar": "Q affects only the u channel; Gamma affects u2; all u^4-and-higher G terms miss u<=2",
    }


def coordinate_change_replay():
    # Exact cancellation of u_t in the determinant under u=u(X,t).
    Fu, Ft, Gu, Gt = map(svar, ("Fu", "Ft", "Gu", "Gt"))
    ux, ut, t, F, G = map(svar, ("ux", "ut", "t", "F", "G"))
    FX = smul(Fu, ux)
    Ft_at_X = sadd(Ft, smul(Fu, ut))
    GX = smul(Gu, ux)
    Gt_at_X = sadd(Gt, smul(Gu, ut))
    wedge_left = ssub(smul(FX, Gt_at_X), smul(Ft_at_X, GX))
    wedge_right = smul(ux, ssub(smul(Fu, Gt), smul(Ft, Gu)))
    assert wedge_left == wedge_right
    E_left = ssub(
        ssub(sscale(smul(FX, G), 12), sscale(smul(F, GX), 8)),
        smul(t, wedge_left),
    )
    L = ssub(
        ssub(sscale(smul(Fu, G), 12), sscale(smul(F, Gu), 8)),
        smul(t, ssub(smul(Fu, Gt), smul(Ft, Gu))),
    )
    assert E_left == smul(ux, L)


def trim(a):
    a = list(map(Q, a))
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def padd(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return trim(out)


def psub(a, b):
    return padd(a, tuple(-x for x in b))


def pscale(a, value):
    return trim(tuple(Q(value) * x for x in a))


def pmul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def pdivmod(a, b):
    a = list(trim(a))
    b = trim(b)
    assert b != (Q(0),)
    q = [Q(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and any(a):
        shift = len(a) - len(b)
        factor = a[-1] / b[-1]
        q[shift] += factor
        for i, value in enumerate(b):
            a[i + shift] -= factor * value
        a = list(trim(a))
    return trim(q), trim(a)


def pmonic(a):
    a = trim(a)
    return pscale(a, 1 / a[-1])


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while b != (Q(0),):
        _, remainder = pdivmod(a, b)
        a, b = b, remainder
    return pmonic(a)


def factor_split_replay():
    # H=(X^4-1)(X^4+1).  V8=X^4+1 vanishes on one entire etale factor
    # and is the unit 2 on the complementary factor.  Hence classification
    # must be factor/root tagged rather than globally binary.
    h_zero = trim((1, 0, 0, 0, 1))
    h_unit = trim((-1, 0, 0, 0, 1))
    H = trim((-1,) + (0,) * 7 + (1,))
    V8 = h_zero
    assert pmul(h_zero, h_unit) == H
    assert pgcd(H, V8) == h_zero
    assert pdivmod(V8, h_zero)[1] == (Q(0),)
    assert pdivmod(V8, h_unit)[1] == (Q(2),)
    return {
        "example": "H=(X^4+1)(X^4-1), V8=X^4+1",
        "zero_factor": "mod X^4+1, V8=0: U11^2 case",
        "unit_factor": "mod X^4-1, V8=2: V8*U14 case",
    }


def classification_replay():
    lower = []
    for k in range(1, 8):
        order = 2 * k
        scalar = Q(3, 2) * (k - 8)
        assert order < 22 and scalar != 0
        lower.append({"k": k, "first_constant_order": order, "scalar_over_Uk2": str(scalar)})

    with_v8 = []
    for k in range(9, 23):
        order = 8 + k
        status = "FORBIDDEN-BEFORE-22" if order < 22 else "UNIT-SLOT" if order == 22 else "TOO-LATE"
        if k == 14:
            assert order == 22 and k - 8 == 6
        with_v8.append({"k": k, "first_constant_order": order, "status": status})

    without_v8 = []
    for k in range(9, 23):
        order = 2 * k
        scalar = Q(3, 2) * (k - 8)
        status = "FORBIDDEN-BEFORE-22" if order < 22 else "UNIT-SLOT" if order == 22 else "TOO-LATE"
        if k == 11:
            assert order == 22 and scalar == Q(9, 2)
        without_v8.append(
            {"k": k, "first_constant_order": order, "scalar_over_Uk2": str(scalar), "status": status}
        )

    assert [row["k"] for row in with_v8 if row["status"] == "UNIT-SLOT"] == [14]
    assert [row["k"] for row in without_v8 if row["status"] == "UNIT-SLOT"] == [11]
    return {
        "lower_k_1_through_7": lower,
        "V8_nonzero": with_v8,
        "V8_zero": without_v8,
        "carrier_A": "6*V8*U14 in L22, hence 6*H'(c)*V8(c)*U14(c)=1",
        "carrier_B": "(9/2)*U11^2 in L22, hence (9/2)*H'(c)*U11(c)^2=1",
    }


def main():
    pins = {}
    for key, (relative, expected) in PINS.items():
        got = sha256(ROOT / relative)
        assert got == expected, (key, got, expected)
        pins[key] = {"path": relative, "sha256": got}

    coordinate_change_replay()
    channels = local_channel_replay()
    classification = classification_replay()
    factor_split = factor_split_replay()

    result = {
        "status": "PASS-R2-ROOTWISE-UNIT-CARRIER-CLASSIFICATION",
        "scope": "formal simple-root cusp normal form through weight 22, including arbitrary G higher-u sidecar; no global polynomial image or face exclusion",
        "pins": pins,
        "coordinate_interface": {
            "normalization": "at a simple root c, parametric formal Morse normalization F=u^2+U(t), with u=H mod t and G=W+Vu+Qu^2+Gamma*u^3+sum_(m>=4)G_m*u^m, Gamma_0=1",
            "jacobian_naturality": "E=u_X*L exactly; u_t cancels in the wedge",
            "endpoint": "if E_0..E_21=0 and E_22=1, then L_<22=0 and H'(c)*[t^22 u^0]L=1",
            "orientation": "u=H mod t fixes the deck orientation and u_X(c,0)=H'(c)",
        },
        "low_u_channels": channels,
        "classification": classification,
        "factorwise_typing": factor_split,
        "theorem": {
            "statement": "over each geometric simple-root residue field, the first constant-channel unit carrier is exactly V8*U14 when V8 is nonzero, or U11^2 when V8 is zero",
            "higher_u_robustness": "Q, Gamma-1, and all u^4+ terms cannot change the first-carrier alternatives; Gamma enters the u2 recursion but its earlier convolutions vanish at the first post-weight-8 U coefficient",
            "mixed_decks": "the two cases may occur on different etale factors and must retain root/factor/deck/chart tags",
        },
        "remaining_gap": {
            "raw_provenance": "compile raw 2S/3S coefficients through the formal cleanup with source provenance",
            "global_sidecar_image": "classify the H-multiple contributed at E22 by all cleaned higher-u sidecar terms, not only R1's two-slot ansatzes",
            "gluing": "retain conjugation, etale-factor, chart, and determinant-unit data when assembling rootwise packets",
        },
        "claims_not_made": [
            "global typed-normal-form/image completeness",
            "M(Y) describes every raw higher-u sidecar",
            "exclusion of the 8_28 face or family",
            "a Keller pair, counterexample, G2-PSC, G2-BD, or JC2",
        ],
    }
    if "--print-candidate" in sys.argv:
        print(json.dumps(result, sort_keys=True, indent=2))
        return
    frozen = json.loads((CASE / "RESULT_R2.json").read_text())
    assert result == frozen
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
