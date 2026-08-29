#!/usr/bin/env python3
"""Exact desk verifier for the bounded 8_28 Keller-face jet-pinning control.

This checks a local/formal obstruction and a typed cusp coefficient map.  It
does not construct a Keller pair and does not prove G2-PSC.
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
    "prior_report": (
        "xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-sol-20260827.md",
        "7647f2f118d4fe9fdd060b9e3e9450b58a62e287a80e942cad6de752a3f34ae8",
    ),
    "prior_freeze": (
        "cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/FREEZE.sha256",
        "676bdd3ce960221072f037e7160d457a9d1d64c8e7353891f69e9931ae71149b",
    ),
    "approximate_root_design": (
        "xmodel/sol-connections.md",
        "3fe165e55704e0a4b5dba3b5968ea995846a81f58b65968fa89521ef8595895c",
    ),
    "transport_scope": (
        "ladder/TRANSPORT.md",
        "9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c",
    ),
    "g2_scope": (
        "ladder/REDUCTION.md",
        "1ff57e1f8a632f33d3558c924dadf26bdd1d389797d48be43515b88718a2e725",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


# Univariate Q[X], low coefficient first.
def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def padd(a, b):
    out = [Q(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def pscale(a, c):
    return trim([Q(c) * x for x in a])


def psub(a, b):
    return padd(a, pscale(b, -1))


def pmul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def ppow(a, n):
    out = (Q(1),)
    for _ in range(n):
        out = pmul(out, a)
    return out


def pder(a):
    return trim([Q(i) * a[i] for i in range(1, len(a))] or [Q(0)])


def pdivmod(a, b):
    a = list(trim(a))
    b = trim(b)
    assert b != (Q(0),)
    out = [Q(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and trim(a) != (Q(0),):
        k = len(a) - len(b)
        c = a[-1] / b[-1]
        out[k] = c
        for j, x in enumerate(b):
            a[j + k] -= c * x
        a = list(trim(a))
    return trim(out), trim(a)


def pmod(a, b):
    return pdivmod(a, b)[1]


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while b != (Q(0),):
        a, b = b, pmod(a, b)
    return pscale(a, 1 / a[-1])


def pencode(a):
    return [str(x) for x in trim(a)]


# Sparse Q[t,X].  Keys are (t exponent, X exponent).
def bx(poly):
    return {(0, i): c for i, c in enumerate(poly) if c}


def bt(poly, n):
    return {(n, i): c for i, c in enumerate(poly) if c}


def badd(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, Q(0)) + c
        if out[m] == 0:
            del out[m]
    return out


def bscale(a, c):
    return {m: Q(c) * x for m, x in a.items() if Q(c) * x}


def bmul(a, b):
    out = {}
    for (ta, xa), ca in a.items():
        for (tb, xb), cb in b.items():
            m = (ta + tb, xa + xb)
            out[m] = out.get(m, Q(0)) + ca * cb
            if out[m] == 0:
                del out[m]
    return out


def bdt(a):
    return {(t - 1, x): Q(t) * c for (t, x), c in a.items() if t}


def bdx(a):
    return {(t, x - 1): Q(x) * c for (t, x), c in a.items() if x}


def tshift(a, n=1):
    return {(t + n, x): c for (t, x), c in a.items()}


def tcoefficient(a, n):
    if not a:
        return (Q(0),)
    top = max((x for (t, x) in a if t == n), default=0)
    return trim([a.get((n, x), Q(0)) for x in range(top + 1)])


# Tiny commutative symbolic ring for the universal E1/E2 formulas.
VARS = ("H", "Hp", "A", "Ap", "B", "Bp", "C", "Cp", "D", "Dp", "a", "ap")


def sconst(c):
    return {(0,) * len(VARS): Q(c)} if c else {}


def svar(name):
    e = [0] * len(VARS)
    e[VARS.index(name)] = 1
    return {tuple(e): Q(1)}


def sadd(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, Q(0)) + c
        if out[m] == 0:
            del out[m]
    return out


def sscale(a, c):
    return {m: Q(c) * x for m, x in a.items() if Q(c) * x}


def smul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(x + y for x, y in zip(ma, mb))
            out[m] = out.get(m, Q(0)) + ca * cb
            if out[m] == 0:
                del out[m]
    return out


def spow(a, n):
    out = sconst(1)
    for _ in range(n):
        out = smul(out, a)
    return out


def ssum(*items):
    out = {}
    for item in items:
        out = sadd(out, item)
    return out


def symbolic_recurrence_checks():
    H, Hp = svar("H"), svar("Hp")
    A, Ap = svar("A"), svar("Ap")
    B, Bp = svar("B"), svar("Bp")
    C, Cp = svar("C"), svar("Cp")
    D, Dp = svar("D"), svar("Dp")
    F0, F0p = spow(H, 2), sscale(smul(H, Hp), 2)
    G0, G0p = spow(H, 3), sscale(smul(spow(H, 2), Hp), 3)

    # E_1 from sum_{i+j=1} ((12-j)F_i'G_j+(i-8)F_iG_j').
    e1 = ssum(
        sscale(smul(F0p, B), 11),
        sscale(smul(F0, Bp), -8),
        sscale(smul(Ap, G0), 12),
        sscale(smul(A, G0p), -7),
    )
    d = sadd(B, sscale(smul(H, A), Q(-3, 2)))
    dp = sadd(Bp, sscale(ssum(smul(Hp, A), smul(H, Ap)), Q(-3, 2)))
    expected_e1 = sscale(
        smul(H, ssum(sscale(smul(Hp, d), 11), sscale(smul(H, dp), -4))),
        2,
    )
    assert e1 == expected_e1

    G1 = sscale(smul(H, A), Q(3, 2))
    G1p = sscale(ssum(smul(Hp, A), smul(H, Ap)), Q(3, 2))
    e2 = ssum(
        sscale(smul(F0p, D), 10),
        sscale(smul(F0, Dp), -8),
        sscale(smul(Ap, G1), 11),
        sscale(smul(A, G1p), -7),
        sscale(smul(Cp, G0), 12),
        sscale(smul(C, G0p), -6),
    )
    expected_e2 = ssum(
        sscale(smul(smul(H, Hp), D), 20),
        sscale(smul(spow(H, 2), Dp), -8),
        sscale(smul(smul(H, A), Ap), 6),
        sscale(smul(Hp, spow(A, 2)), Q(-21, 2)),
        sscale(smul(spow(H, 3), Cp), 12),
        sscale(smul(smul(spow(H, 2), Hp), C), -18),
    )
    assert e2 == expected_e2
    mod_h = {m: c for m, c in e2.items() if m[VARS.index("H")] == 0}
    assert mod_h == sscale(smul(Hp, spow(A, 2)), Q(-21, 2))
    a, ap = svar("a"), svar("ap")
    Adiv = smul(H, a)
    Apdiv = ssum(smul(Hp, a), smul(H, ap))
    G1div = sscale(smul(spow(H, 2), a), Q(3, 2))
    G1pdiv = sscale(
        ssum(sscale(smul(smul(H, Hp), a), 2), smul(spow(H, 2), ap)),
        Q(3, 2),
    )
    Dexp = ssum(
        sscale(smul(H, C), Q(3, 2)),
        sscale(smul(H, spow(a, 2)), Q(3, 8)),
    )
    Dpexp = ssum(
        sscale(ssum(smul(Hp, C), smul(H, Cp)), Q(3, 2)),
        sscale(
            ssum(smul(Hp, spow(a, 2)), sscale(smul(smul(H, a), ap), 2)),
            Q(3, 8),
        ),
    )
    e2div = ssum(
        sscale(smul(F0p, Dexp), 10),
        sscale(smul(F0, Dpexp), -8),
        sscale(smul(Apdiv, G1div), 11),
        sscale(smul(Adiv, G1pdiv), -7),
        sscale(smul(Cp, G0), 12),
        sscale(smul(C, G0p), -6),
    )
    assert e2div == {}
    return {
        "E1_factor": "2*H*(11*H'*(G1-(3/2)H*F1)-4*H*(G1-(3/2)H*F1)')",
        "E2_mod_H_after_E1": "-(21/2)*H'*F1^2 mod H",
        "E2_solution_after_F1=H*a": "G2=(3/2)*H*F2+(3/8)*H*a^2",
    }


# Sparse Q[x,y] for the two face checks.
def xyadd(a, b):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, Q(0)) + c
        if out[m] == 0:
            del out[m]
    return out


def xyscale(a, c):
    return {m: Q(c) * x for m, x in a.items() if Q(c) * x}


def xymul(a, b):
    out = {}
    for (ia, ja), ca in a.items():
        for (ib, jb), cb in b.items():
            m = (ia + ib, ja + jb)
            out[m] = out.get(m, Q(0)) + ca * cb
            if out[m] == 0:
                del out[m]
    return out


def xypow(a, n):
    out = {(0, 0): Q(1)}
    for _ in range(n):
        out = xymul(out, a)
    return out


def initial_face(a, weight):
    best = max(weight(i, j) for i, j in a)
    return best, {m: c for m, c in a.items() if weight(*m) == best}


def y_edge(a, scale):
    out = {}
    for (i, j), c in a.items():
        if scale + 3 * i - j == 0:
            out[i] = out.get(i, Q(0)) + c
    top = max(out, default=0)
    return trim([out.get(i, Q(0)) for i in range(top + 1)])


def main():
    observed = {}
    for key, (rel, expected) in PINS.items():
        got = sha256(ROOT / rel)
        assert got == expected, (key, got, expected)
        observed[key] = {"path": rel, "sha256": got}

    symbolic = symbolic_recurrence_checks()

    X = (Q(0), Q(1))
    H = trim([Q(-1)] + [Q(0)] * 7 + [Q(1)])
    Hp = pder(H)
    assert pgcd(H, Hp) == (Q(1),)

    # The proposed replacement has y-edge H^2/H^3 and retains the complete
    # maximum (4,-1) B^2/B^3 face.
    z_minus_1 = {(1, 4): Q(1), (0, 0): Q(-1)}
    Bxy = xymul({(1, 0): Q(1)}, xypow(z_minus_1, 7))
    B2, B3 = xypow(Bxy, 2), xypow(Bxy, 3)
    fface = xyadd(B2, {(8, 32): Q(-2), (0, 8): Q(1)})
    gface = xyadd(
        B3,
        {(16, 60): Q(-3), (8, 36): Q(3), (0, 12): Q(-1)},
    )
    wf, ff = initial_face(fface, lambda i, j: 4 * i - j)
    wg, fg = initial_face(gface, lambda i, j: 4 * i - j)
    assert (wf, wg, ff, fg) == (8, 12, B2, B3)
    assert y_edge(fface, 8) == ppow(H, 2)
    assert y_edge(gface, 12) == ppow(H, 3)

    # A tempting first-jet pole mutation passes E1 but cannot pass E2.
    naive_remainders = {}
    for lam in (13, 14):
        A = trim([Q(lam)] + [Q(0)] * 14 + [Q(-14)])
        rem = pmod(pscale(pmul(Hp, ppow(A, 2)), Q(-21, 2)), H)
        assert rem != (Q(0),)
        naive_remainders[str(lam)] = pencode(rem)

    # Two same-support root-sign packets.  Each is a nonconstant involution
    # modulo H, but their + signs occur on different deck/Galois factors.
    S_plus = tuple(
        map(Q, (Q(3, 4), Q(1, 4), Q(-1, 4), Q(1, 4), Q(-1, 4), Q(1, 4), Q(-1, 4), Q(1, 4)))
    )
    S_minus = tuple(
        map(Q, (Q(-1, 4), Q(1, 4), Q(-1, 4), Q(1, 4), Q(3, 4), Q(1, 4), Q(-1, 4), Q(1, 4)))
    )
    factors = {
        "X-1": ((Q(-1), Q(1)), 1),
        "X+1": ((Q(1), Q(1)), 1),
        "X2+1": ((Q(1), Q(0), Q(1)), 2),
        "X4+1": ((Q(1), Q(0), Q(0), Q(0), Q(1)), 4),
    }
    sign_expectations = {
        "S_plus": {"X-1": 1, "X+1": -1, "X2+1": 1, "X4+1": 1},
        "S_minus": {"X-1": 1, "X+1": -1, "X2+1": 1, "X4+1": -1},
    }
    sign_packets = {}
    for name, S in (("S_plus", S_plus), ("S_minus", S_minus)):
        assert [i for i, c in enumerate(S) if c] == list(range(8))
        assert pmod(ppow(S, 2), H) == (Q(1),)
        signs = {}
        plus_degree = 0
        for factor_name, (factor, degree) in factors.items():
            rem = pmod(S, factor)
            expected = sign_expectations[name][factor_name]
            assert rem == (Q(expected),)
            signs[factor_name] = expected
            if expected == 1:
                plus_degree += degree
        q, rem = pdivmod(psub(ppow(S, 2), (Q(1),)), H)
        assert rem == (Q(0),)
        q = pscale(q, Q(3, 8))
        assert [i for i, c in enumerate(q) if c] == list(range(7))
        assert q[0] and q[1]

        # F=H^2+t^8*S, G=H^3+(3/2)t^8*H*S+t^16*q.
        F = badd(bx(ppow(H, 2)), bt(S, 8))
        G = badd(
            badd(bx(ppow(H, 3)), bt(pscale(pmul(H, S), Q(3, 2)), 8)),
            bt(q, 16),
        )
        E = badd(
            badd(bscale(bmul(bdx(F), G), 12), bscale(bmul(F, bdx(G)), -8)),
            bscale(tshift(badd(bmul(bdx(F), bdt(G)), bscale(bmul(bdt(F), bdx(G)), -1))), -1),
        )
        for n in range(22):
            assert tcoefficient(E, n) == (Q(0),), (name, n, tcoefficient(E, n))
        assert tcoefficient(E, 22) == (Q(0),)
        sign_packets[name] = {
            "coefficients": pencode(S),
            "E16_correction_coefficients": pencode(q),
            "full_truncated_support": "identical: F at (0,0..16),(8,0..7); G at (0,0..24),(8,0..15),(16,0..6)",
            "polynomial_source_status": "REJECTED: G_16 X^0 and X^1 pull back to y^-4 and x*y^-1",
            "factor_signs": signs,
            "tagged_fibre_a1_degenerate_root_degree": plus_degree,
            "generic_a2_finite_residue_square_by_sign": {"+1": "25/4", "-1": "27/4"},
            "E_0_through_E_21": "zero",
            "E_22": "zero (pre-Keller control only)",
        }

    # First local cusp coefficient map and the first rootwise determinant
    # carrier.  U_14=X, V_8=1/48 passes every H-root but leaves an H-multiple
    # in the global coefficient, so a higher-u/global lift is still required.
    U14 = X
    V8 = (Q(1, 48),)
    root_condition = pmod(pscale(pmul(pmul(Hp, U14), V8), 6), H)
    assert root_condition == (Q(1),)
    raw_e22 = padd(
        pmul(H, padd(pscale(pmul(V8, pder(U14)), 4), pscale(pmul(U14, pder(V8)), 6))),
        pscale(pmul(pmul(Hp, U14), V8), 6),
    )
    assert raw_e22 == padd((Q(1),), pscale(H, Q(13, 12)))

    result = {
        "status": "PASS-BOUNDED-KELLER-FACE-JET-PINNING-CONTROL",
        "scope": "one 8_28 y-infinity face; exact recurrence and cusp packet prototype; formal root-sign packets fail polynomial-source provenance; not a Keller pair; not G2-PSC",
        "pins": observed,
        "face": {
            "H": "X^8-1",
            "y_edge": ["F_0=H^2", "G_0=H^3"],
            "native_(4,-1)_faces": ["B^2 at weight 8", "B^3 at weight 12"],
        },
        "jacobian": {
            "coordinate_identity": "Jac(f,g)=t^-22*E",
            "E": "12*F_X*G-8*F*G_X-t*(F_X*G_t-F_t*G_X)",
            "recurrence": "E_n=sum_(i+j=n)((12-j)F_i'G_j+(i-8)F_iG_j')",
            **symbolic,
            "squarefree_H": True,
            "consequence": "E1=E2=0 forces H|F1 and the F^(3/2) second coefficient",
        },
        "naive_first_jet": {
            "F1_lambda": "-14*X^15+lambda",
            "G1_lambda": "(3/2)*H*F1_lambda",
            "E1": "zero",
            "E2_mod_H": naive_remainders,
            "verdict": "NONEXTENDABLE; cannot be a Keller-compatible pole mutation",
        },
        "same_support_root_sign_packets": sign_packets,
        "polynomial_provenance_filter": {
            "t16_Xi_pullback": "G term x^i*y^(3*i-4)",
            "observed_failure": "both nonconstant packets have nonzero i=0,1 coefficients",
            "general_low_coefficient_test": "if S^2=1 mod (X^8-1), q=(S^2-1)/(X^8-1), then q0=q1=0 forces s0^2=1 and s0*s1=0; for root signs S(c)=+/-1, s0=+/-1 forces all signs uniform",
            "verdict": "nonconstant root-sign mutation is rejected in this bounded source window",
        },
        "fibre_ode": {
            "on_F=a*t^8": "d(t^-12*G)/dt=-t^9/F_X when E=t^22",
            "generic_square_edge": "ord_t(F_X)=4, hence g is finite and g-g(0)=O(t^6)",
            "pole_mutation": "PINNED-FINITE for generic tagged fibres",
        },
        "cusp_map": {
            "normal_form": "F=u^2+U(t), G=u^3+V(t)u+W(t), u=H(X)",
            "first_raw_map": "U1(c)=F1(c), V1(c)=(3/2)F1(c), W1(c)=0",
            "E2_effect": "U1(c)=0 at every simple H-root",
            "first_determinant_carrier": "6*H'(c)*V8(c)*U14(c)=1",
            "rootwise_example": "U14=X, V8=1/48",
            "rootwise_remainder_mod_H": pencode(root_condition),
            "raw_global_E22": "1+(13/12)H",
            "global_lift_status": "GAP: the H-multiple needs higher-u/global polynomial correction",
        },
        "claims_not_made": [
            "the root-sign packets extend to E22=1",
            "a polynomial Keller pair or counterexample",
            "a global GGV-to-Eggers-Wall functor",
            "G2-PSC, G2-BD, or JC2",
        ],
    }
    if "--print-candidate" in sys.argv:
        print(json.dumps(result, sort_keys=True, indent=2))
        return
    frozen = json.loads((CASE / "RESULT.json").read_text())
    assert result == frozen
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
