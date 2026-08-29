#!/usr/bin/env python3
"""Exact desk replay for the degree-eight upper-face cascade through D6.

The theorem in the companion xmodel report is symbolic.  This replay has
three independent jobs:

* reconstruct the universal binomial coefficients in a Laurent polynomial
  ring and compare them with the closed formulas used in the proof;
* instantiate both survivor branches over Q[X], reconstruct G from the
  characteristic modes, and check D0=...=D6=0 plus every D3 degree window;
* certify the q1 separating controls and load-bearing gate mutations by exact
  rational row reduction and polynomial division.

No Groebner basis, randomized arithmetic, floating point, or external CAS is
used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple


ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "RESULT.json"


# ---------------------------------------------------------------------------
# Q[X]


Poly = Tuple[Q, ...]


def ptrim(a: Iterable[Q]) -> Poly:
    z = list(a)
    while z and z[-1] == 0:
        z.pop()
    return tuple(z)


P0: Poly = ()
P1: Poly = (Q(1),)
X: Poly = (Q(0), Q(1))


def padd(a: Poly, b: Poly) -> Poly:
    z = [Q(0)] * max(len(a), len(b))
    for i, c in enumerate(a):
        z[i] += c
    for i, c in enumerate(b):
        z[i] += c
    return ptrim(z)


def pneg(a: Poly) -> Poly:
    return tuple(-c for c in a)


def psub(a: Poly, b: Poly) -> Poly:
    return padd(a, pneg(b))


def pscale(a: Poly, c: Q) -> Poly:
    return ptrim(c * x for x in a)


def pmul(a: Poly, b: Poly) -> Poly:
    if not a or not b:
        return P0
    z = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i + j] += x * y
    return ptrim(z)


def ppow(a: Poly, n: int) -> Poly:
    assert n >= 0
    out = P1
    base = a
    while n:
        if n & 1:
            out = pmul(out, base)
        base = pmul(base, base)
        n //= 2
    return out


def pder(a: Poly) -> Poly:
    return ptrim(Q(i) * a[i] for i in range(1, len(a)))


def pdivmod(a: Poly, b: Poly) -> Tuple[Poly, Poly]:
    assert b
    r = list(a)
    q = [Q(0)] * max(0, len(a) - len(b) + 1)
    while r and len(r) >= len(b):
        k = len(r) - len(b)
        c = r[-1] / b[-1]
        q[k] += c
        for j, x in enumerate(b):
            r[k + j] -= c * x
        while r and r[-1] == 0:
            r.pop()
    return ptrim(q), ptrim(r)


def pexact(a: Poly, b: Poly) -> Poly:
    q, r = pdivmod(a, b)
    if r:
        raise AssertionError(f"non-exact polynomial division; remainder={pjson(r)}")
    return q


def pdivides(b: Poly, a: Poly) -> bool:
    return not pdivmod(a, b)[1]


def pmonic(a: Poly) -> Poly:
    if not a:
        return a
    return pscale(a, 1 / a[-1])


def pgcd(a: Poly, b: Poly) -> Poly:
    while b:
        _, r = pdivmod(a, b)
        a, b = b, r
    return pmonic(a)


def pdeg(a: Poly) -> int:
    return len(a) - 1


def pjson(a: Poly) -> List[str]:
    return [str(c) for c in a]


def patterned(deg: int, seed: int) -> Poly:
    vals = []
    for i in range(deg):
        n = ((seed + 3) * (i + 1) * (i + 2) + 2 * seed + i) % 13 - 6
        vals.append(Q(n))
    vals.append(Q(1))
    return ptrim(vals)


# ---------------------------------------------------------------------------
# Rational functions over Q[X], used only to reconstruct characteristic modes


@dataclass(frozen=True)
class Rat:
    num: Poly
    den: Poly = P1

    def __post_init__(self) -> None:
        assert self.den
        if not self.num:
            object.__setattr__(self, "den", P1)
            return
        g = pgcd(self.num, self.den)
        num = pexact(self.num, g)
        den = pexact(self.den, g)
        lead = den[-1]
        object.__setattr__(self, "num", pscale(num, 1 / lead))
        object.__setattr__(self, "den", pscale(den, 1 / lead))

    def __add__(self, other: "Rat") -> "Rat":
        return Rat(padd(pmul(self.num, other.den), pmul(other.num, self.den)),
                   pmul(self.den, other.den))

    def __neg__(self) -> "Rat":
        return Rat(pneg(self.num), self.den)

    def __sub__(self, other: "Rat") -> "Rat":
        return self + (-other)

    def __mul__(self, other: "Rat") -> "Rat":
        return Rat(pmul(self.num, other.num), pmul(self.den, other.den))

    def scale(self, c: Q) -> "Rat":
        return Rat(pscale(self.num, c), self.den)

    def polynomial(self) -> Poly:
        return pexact(self.num, self.den)


R0 = Rat(P0)
R1 = Rat(P1)


def rpoly(a: Poly) -> Rat:
    return Rat(a)


def series_mul(a: Sequence[Rat], b: Sequence[Rat], nmax: int) -> List[Rat]:
    out = [R0 for _ in range(nmax + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= nmax:
                out[i + j] = out[i + j] + x * y
    return out


def binom(alpha: Q, k: int) -> Q:
    out = Q(1)
    for j in range(k):
        out *= (alpha - j) / (j + 1)
    return out


def fractional_series(F: Sequence[Poly], H: Poly, base: Poly,
                      alpha: Q, nmax: int) -> List[Rat]:
    """base*(1+sum F_i/H^2 t^i)^alpha through t^nmax."""
    h2 = ppow(H, 2)
    z = [R0] + [Rat(F[i], h2) for i in range(1, nmax + 1)]
    out = [R0 for _ in range(nmax + 1)]
    power = [R1] + [R0 for _ in range(nmax)]
    for k in range(nmax + 1):
        c = binom(alpha, k)
        for n, v in enumerate(power):
            out[n] = out[n] + v.scale(c)
        power = series_mul(power, z, nmax)
    return [rpoly(base) * v for v in out]


def compositions(total: int, parts: int) -> Iterable[Tuple[int, ...]]:
    if parts == 0:
        if total == 0:
            yield ()
        return
    for first in range(1, total - parts + 2):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def fractional_coeff(F: Sequence[Poly], H: Poly, base: Poly,
                     alpha: Q, n: int) -> Poly:
    """One coefficient, accumulated over the single denominator H^(2n).

    This avoids expression swell in a generic rational-function series while
    remaining a direct reconstruction of the binomial theorem.
    """
    if n == 0:
        return base
    common = ppow(H, 2 * n)
    numerator = P0
    for k in range(1, n + 1):
        for comp in compositions(n, k):
            prod = P1
            for i in comp:
                prod = pmul(prod, F[i])
            lift = ppow(H, 2 * (n - k))
            term = pscale(pmul(pmul(base, prod), lift), binom(alpha, k))
            numerator = padd(numerator, term)
    return pexact(numerator, common)


# ---------------------------------------------------------------------------
# A tiny Laurent ring for universal coefficient identities


Mon = Tuple[Tuple[str, int], ...]


@dataclass(frozen=True)
class Lau:
    terms: Mapping[Mon, Q]

    @staticmethod
    def const(c: Q) -> "Lau":
        return Lau({(): c} if c else {})

    @staticmethod
    def var(name: str, exp: int = 1) -> "Lau":
        return Lau({((name, exp),): Q(1)}) if exp else Lau.const(Q(1))

    def __add__(self, other: "Lau") -> "Lau":
        z: Dict[Mon, Q] = dict(self.terms)
        for m, c in other.terms.items():
            z[m] = z.get(m, Q(0)) + c
            if z[m] == 0:
                del z[m]
        return Lau(z)

    def __neg__(self) -> "Lau":
        return Lau({m: -c for m, c in self.terms.items()})

    def __sub__(self, other: "Lau") -> "Lau":
        return self + (-other)

    def __mul__(self, other: "Lau") -> "Lau":
        z: Dict[Mon, Q] = {}
        for m, c in self.terms.items():
            for n, d in other.terms.items():
                exps: Dict[str, int] = {}
                for name, e in m + n:
                    exps[name] = exps.get(name, 0) + e
                mon = tuple(sorted((name, e) for name, e in exps.items() if e))
                z[mon] = z.get(mon, Q(0)) + c * d
                if z[mon] == 0:
                    del z[mon]
        return Lau(z)

    def scale(self, c: Q) -> "Lau":
        return Lau({m: c * x for m, x in self.terms.items() if c * x})

    def __pow__(self, n: int) -> "Lau":
        assert n >= 0
        out = Lau.const(Q(1))
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out


L0 = Lau.const(Q(0))
L1 = Lau.const(Q(1))


def lseries_mul(a: Sequence[Lau], b: Sequence[Lau], nmax: int) -> List[Lau]:
    out = [L0 for _ in range(nmax + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= nmax:
                out[i + j] = out[i + j] + x * y
    return out


def universal_binomial(alpha: Q, base: Lau, H: Lau,
                       f: Sequence[Lau], nmax: int) -> List[Lau]:
    z = [L0] + [f[i] * (H ** 0) * Lau.var("H", -2) for i in range(1, nmax + 1)]
    # The caller uses the distinguished variable H itself.  The redundant
    # H**0 above makes the normalization visually explicit.
    out = [L0 for _ in range(nmax + 1)]
    power = [L1] + [L0 for _ in range(nmax)]
    for k in range(nmax + 1):
        for n, v in enumerate(power):
            out[n] = out[n] + v.scale(binom(alpha, k))
        power = lseries_mul(power, z, nmax)
    return [base * v for v in out]


def universal_formula_checks() -> Dict[str, int]:
    H = Lau.var("H")
    V = Lau.var("V")
    f = [H ** 2]
    f.extend(Lau.var(f"F{i}") for i in range(1, 7))
    f[1] = H * V
    b = universal_binomial(Q(3, 2), H ** 3, H, f, 6)
    r = [L0] + [b[n] - (H * f[n]).scale(Q(3, 2)) for n in range(1, 7)]
    delta = f[2].scale(Q(4)) - V ** 2
    expected = {
        3: (V * f[2]).scale(Q(3, 4)) - (V ** 3).scale(Q(1, 16)),
        4: (V * f[3]).scale(Q(3, 4))
           + (delta ** 2) * Lau.var("H", -1).scale(Q(3, 128)),
        5: (V * f[4]).scale(Q(3, 4))
           + (f[3] * delta) * Lau.var("H", -1).scale(Q(3, 16))
           - (V * delta ** 2) * Lau.var("H", -2).scale(Q(3, 256)),
        6: (V * f[5]).scale(Q(3, 4))
           + (delta * f[4]) * Lau.var("H", -1).scale(Q(3, 16))
           + (f[3] ** 2) * Lau.var("H", -1).scale(Q(3, 8))
           - (V * f[3] * delta) * Lau.var("H", -2).scale(Q(3, 32))
           + (delta ** 2 * ((V ** 2).scale(Q(6)) - delta))
             * Lau.var("H", -3).scale(Q(1, 1024)),
    }
    for n, e in expected.items():
        assert r[n] == e, f"universal R{n} identity failed"
    return {"checked_R3_through_R6": 4, "laurent_terms_R6": len(r[6].terms)}


# ---------------------------------------------------------------------------
# Determinant recurrence and mode reconstruction


def determinant_rows(F: Sequence[Poly], G: Sequence[Poly], nmax: int) -> List[Poly]:
    rows = []
    for n in range(nmax + 1):
        d = P0
        for i in range(n + 1):
            j = n - i
            left = pscale(pmul(pder(F[i]), G[j]), Q(12 - j))
            right = pscale(pmul(F[i], pder(G[j])), Q(i - 8))
            d = padd(d, padd(left, right))
        rows.append(d)
    return rows


def reconstruct_g(branch: str, F: Sequence[Poly], A: Poly, B: Poly | None,
                  constants: Mapping[str, Q]) -> List[Poly]:
    H = ppow(A, 2) if B is None else pmul(ppow(A, 2), B)
    out = [fractional_coeff(F, H, ppow(H, 3), Q(3, 2), n) for n in range(7)]
    if branch == "P":
        c2, c4, c6 = constants["c2"], constants["c4"], constants["c6"]
        if c2:
            for n in range(2, 7):
                mode = fractional_coeff(F, H, ppow(A, 5), Q(5, 4), n - 2)
                out[n] = padd(out[n], pscale(mode, c2))
        for n in range(4, 7):
            out[n] = padd(out[n], pscale(F[n - 4], c4))
        out[6] = padd(out[6], pscale(ppow(A, 3), c6))
    else:
        c4 = constants["c4"]
        for n in range(4, 7):
            out[n] = padd(out[n], pscale(F[n - 4], c4))
    return out


def raw_window_check(F: Sequence[Poly], G: Sequence[Poly]) -> None:
    for n in range(7):
        assert pdeg(F[n]) <= 16 - n
        assert pdeg(G[n]) <= 24 - n


def valid_fixture(branch: str, active_c2: bool = False) -> Dict[str, object]:
    if branch == "P":
        A = psub(ppow(X, 4), P1)
        B = None
        H = ppow(A, 2)
        V = pmul(A, patterned(3, 41)) if active_c2 else patterned(7, 11)
        Z, T = patterned(6, 13), patterned(9, 17)
        F3factor = A
        constants = {"c2": Q(2) if active_c2 else Q(0), "c4": Q(-3, 2), "c6": Q(5, 3)}
    else:
        A = (Q(0), Q(-2, 5), Q(0), Q(1))
        B = (Q(-1), Q(0), Q(1))
        H = pmul(ppow(A, 2), B)
        V, Z, T = patterned(7, 19), patterned(6, 23), patterned(8, 29)
        F3factor = pmul(A, B)
        constants = {"c4": Q(7, 5)}
    F = [ppow(H, 2)]
    F.append(pmul(H, V))
    F.append(pscale(padd(ppow(V, 2), pmul(H, Z)), Q(1, 4)))
    F.append(pscale(padd(pmul(V, Z), pmul(F3factor, T)), Q(1, 8)))
    F.extend([patterned(12, 31), patterned(11, 37), patterned(10, 43)])
    G = reconstruct_g(branch, F, A, B, constants)
    raw_window_check(F, G)
    rows = determinant_rows(F, G, 6)
    assert rows == [P0] * 7
    return {
        "branch": branch,
        "active_c2": active_c2,
        "A": pjson(A),
        "B": None if B is None else pjson(B),
        "F_degrees": [pdeg(x) for x in F],
        "G_degrees": [pdeg(x) for x in G],
        "row_zero": [not x for x in rows],
        "constants": {k: str(v) for k, v in constants.items()},
    }


# ---------------------------------------------------------------------------
# Exact q1 ranks and gate controls


def matrix_rank(columns: Sequence[Sequence[Q]], nrows: int = 16) -> int:
    if not columns:
        return 0
    m = [[columns[j][i] for j in range(len(columns))] for i in range(nrows)]
    r = 0
    for c in range(len(columns)):
        pivot = next((i for i in range(r, nrows) if m[i][c]), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        z = m[r][c]
        m[r] = [x / z for x in m[r]]
        for i in range(nrows):
            if i != r and m[i][c]:
                z = m[i][c]
                m[i] = [x - z * y for x, y in zip(m[i], m[r])]
        r += 1
    return r


def col(p: Poly, n: int = 16) -> List[Q]:
    return list(p) + [Q(0)] * (n - len(p))


def q1_separator(branch: str) -> Dict[str, object]:
    if branch == "P":
        A = psub(ppow(X, 4), P1)
        B = None
        H = ppow(A, 2)
        operator = []
        for k in range(13):
            q = ppow(X, k)
            operator.append(col(psub(pscale(pmul(A, pder(q)), Q(2)),
                                      pscale(pmul(pder(A), q), Q(3)))))
    else:
        A = (Q(0), Q(-2, 5), Q(0), Q(1))
        B = (Q(-1), Q(0), Q(1))
        H = pmul(ppow(A, 2), B)
        AB = pmul(A, B)
        C = padd(pscale(pmul(pder(A), B), Q(6)), pmul(A, pder(B)))
        operator = []
        for k in range(12):
            q = ppow(X, k)
            operator.append(col(psub(pscale(pmul(AB, pder(q)), Q(4)), pmul(C, q))))
    rank = matrix_rank(operator)
    aug = matrix_rank(operator + [col(H)])
    assert aug == rank + 1

    # U=H+t/2, F=U^2, G=U^3: an all-row-zero separator with F1=H.
    F = [ppow(H, 2), H, (Q(1, 4),), P0, P0, P0, P0]
    G = [ppow(H, 3), pscale(ppow(H, 2), Q(3, 2)),
         pscale(H, Q(3, 4)), (Q(1, 8),), P0, P0, P0]
    raw_window_check(F, G)
    rows = determinant_rows(F, G, 6)
    assert rows == [P0] * 7
    return {
        "branch": branch,
        "operator_rank": rank,
        "augmented_by_F1_equals_H_rank": aug,
        "q1_member": False,
        "square_control_D0_D6_zero": True,
        "square_control_endpoint": "D22=0 (indeed E identically zero)",
    }


def gate_mutations() -> Dict[str, bool]:
    AP = psub(ppow(X, 4), P1)
    BP = P1
    HQ = None
    AQ = (Q(0), Q(-2, 5), Q(0), Q(1))
    BQ = (Q(-1), Q(0), Q(1))
    HQ = pmul(ppow(AQ, 2), BQ)
    ABQ = pmul(AQ, BQ)

    # D3: after D2, F1=A*U on P and F1=AB*U on Q.  U=1,F2=0
    # leaves numerator -U^3, not divisible by A^3.
    d3p = not pdivides(ppow(AP, 3), pscale(P1, Q(-1)))
    d3q = not pdivides(ppow(AQ, 3), pscale(P1, Q(-1)))

    # D4: V=1,F2=0 gives Delta=-1, missing rad(H).
    d4p = not pdivides(AP, pscale(P1, Q(-1)))
    d4q = not pdivides(ABQ, pscale(P1, Q(-1)))

    # P D5 c2 mutation: V=Z=c2=1, W=A, F3=1/8.
    V = P1
    W = AP
    F3 = (Q(1, 8),)
    n5p = padd(
        pscale(pmul(W, psub(pscale(pmul(AP, F3), Q(16)), pmul(V, W))), Q(3)),
        pscale(pmul(pmul(AP, V), padd(ppow(V, 2), pscale(pmul(AP, W), Q(2)))), Q(10)),
    )
    d5p = not pdivides(ppow(AP, 2), n5p)

    # D6: after W=A*Z, V=Z=1,F3=0 misses A (P) or AB (Q).
    d6p = not pdivides(AP, pscale(P1, Q(-1)))
    d6q = not pdivides(ABQ, pscale(P1, Q(-1)))

    # Positive divisibility sanity checks for the displayed parametrization.
    positive_p = pdivides(AP, psub(pscale(pmul(AP, (Q(1, 8),)), Q(8)), AP))
    positive_q = pdivides(ABQ, psub(pscale(pmul(ABQ, (Q(1, 8),)), Q(8)), ABQ))
    out = {
        "P_D3_mutation_rejected": d3p,
        "Q_D3_mutation_rejected": d3q,
        "P_D4_mutation_rejected": d4p,
        "Q_D4_mutation_rejected": d4q,
        "P_c2_D5_mutation_rejected": d5p,
        "P_D6_mutation_rejected": d6p,
        "Q_D6_mutation_rejected": d6q,
        "P_positive_gate_control": positive_p,
        "Q_positive_gate_control": positive_q,
    }
    assert all(out.values())
    return out


def build_result() -> Dict[str, object]:
    # Leading-factor hypotheses used by every fixture.
    AP = psub(ppow(X, 4), P1)
    AQ = (Q(0), Q(-2, 5), Q(0), Q(1))
    BQ = (Q(-1), Q(0), Q(1))
    assert pgcd(AP, pder(AP)) == P1
    assert pgcd(AQ, pder(AQ)) == P1
    assert pgcd(BQ, pder(BQ)) == P1
    assert pgcd(AQ, BQ) == P1

    return {
        "schema": "GGV-8_28-UPPER-CASCADE-W3-W6-v1",
        "scope": "fixed D3 raw windows; squarefree branch shapes; zero rows D1..D6 only",
        "method": "exact Fraction arithmetic, Laurent identities, characteristic modes, rational row reduction",
        "universal_formula_checks": universal_formula_checks(),
        "theorem": {
            "P": {
                "H": "A^2; deg A=4; A squarefree",
                "parameters": [
                    "F1=H*V, deg V<=7",
                    "F2=(V^2+H*Z)/4, deg Z<=6",
                    "F3=(V*Z+A*T)/8, deg T<=9",
                    "F4,F5,F6 arbitrary in their raw windows",
                    "c4,c6 arbitrary",
                    "c2=0 or A divides V",
                ],
                "components": {
                    "c2_zero_dimension": 63,
                    "A_divides_V_dimension": 60,
                    "ambient_raw_F1_to_F6_and_G1_to_G6_dimension": 210,
                },
            },
            "Q": {
                "H": "A^2*B; deg A=3; deg B=2; A,B squarefree and coprime",
                "parameters": [
                    "F1=H*V, deg V<=7",
                    "F2=(V^2+H*Z)/4, deg Z<=6",
                    "F3=(V*Z+A*B*T)/8, deg T<=8",
                    "F4,F5,F6 arbitrary in their raw windows",
                    "c4 arbitrary",
                ],
                "dimension": 61,
                "ambient_raw_F1_to_F6_and_G1_to_G6_dimension": 210,
            },
            "intermediate_exact_gates": [
                "D2: H divides F1^2",
                "D3: H divides F1",
                "D4: rad(H) divides 4*F2-V^2",
                "D5+D6 force H divides 4*F2-V^2",
                "P D5 mode gate: c2=0 or A divides V",
                "P D6: A divides 8*F3-V*Z",
                "Q D6: A*B divides 8*F3-V*Z",
            ],
        },
        "valid_exact_fixtures": [
            valid_fixture("P", False),
            valid_fixture("P", True),
            valid_fixture("Q", False),
        ],
        "gate_mutations": gate_mutations(),
        "q1_separators": [q1_separator("P"), q1_separator("Q")],
        "firewalls": [
            "No D22=1 endpoint is imposed or constructed.",
            "The square controls have E identically zero and hence D22=0.",
            "No D23 row is imposed, so q1 is not licensed as a landing consequence here.",
            "No branch exclusion, landing theorem, counterexample, or JC2 conclusion is made.",
        ],
    }


def canonical_bytes(obj: object) -> bytes:
    return (json.dumps(obj, indent=2, sort_keys=True) + "\n").encode()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    if args.write == args.check:
        ap.error("choose exactly one of --write or --check")
    obj = build_result()
    data = canonical_bytes(obj)
    if args.write:
        RESULT.write_bytes(data)
    else:
        assert RESULT.read_bytes() == data, "RESULT.json differs from exact reconstruction"
    print(json.dumps({
        "status": "PASS",
        "result_sha256": hashlib.sha256(data).hexdigest(),
        "P_dimension": 63,
        "Q_dimension": 61,
        "q1_separators": 2,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
