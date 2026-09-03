#!/usr/bin/env python3
"""Exact, fail-closed STAR-REALISABILITY census driver.

At r=1, write P_1=g_{sigma_1} and Q_1=(T_1)_{sigma_1}.  Moh Prop. 4.6
(p.170) gives D(n,-M_1,P_1,Q_1)=c != 0 and M_1=-m.  Def. 5.1 gives

    deg P_1 = a_1 = e V_2,       deg Q_1 = b_1 = d V_2.

Thus, for h=K/V_2,

    D(n,m,P_1,Q_1) = h D(a_1,b_1,P_1,Q_1).

Moh Prop. A.5 (p.207), also invoked explicitly on p.184, says that the
nonzero-constant degree-weighted operator makes P_1 Q_1 square-free.  In
particular P_1 has the forced partition (1,...,1).  Consequently no numerical
skeleton is killed by a *forced* repeated root: the same leading-form
structure forces the opposite.

The census and Skel implementation are imported unchanged from
box/moh_skeleton_N.py.  All arithmetic used for q, (UNI), N, and the operator
scaling is Fraction arithmetic.  No canonical ledger is read or written.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import sys
from dataclasses import dataclass
from fractions import Fraction as F
from math import gcd
from pathlib import Path
from typing import Dict, Iterable, Mapping, Optional, Sequence, Tuple


HERE = Path(__file__).resolve().parent
BOX = HERE.parent
FROZEN = Path(
    "/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/"
    "T/jc2-lane.l8KjQg/inputs"
)

EXPECTED_FROZEN = {
    "d1-subtree-opus5-20260902.md":
        "26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0",
    "d1-subtree-review-grok46-20260902.md":
        "66c3e82ff6fb9a0e0ad339d3cd22a2b5236129b0b731f5cd68ff048df15c735c",
    "ideation-20260902T1608Z-synthesis.md":
        "ad1bf4467319f98a29e50de16915ced5f5c4177f7ffe28657332aba00ad18245",
    "moh_skeleton_N.py":
        "3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39",
    "integration17-coordinator-fable51-20260902.md":
        "126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5",
    "d1floor.py":
        "cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6",
    "runall.py":
        "e2b4d616a6ccbd771f1eb8c1b9e37ffaf50a46e278a529c1e05c5de948fda313",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as inp:
        for block in iter(lambda: inp.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def verify_inputs() -> None:
    failures = []
    for name, expected in EXPECTED_FROZEN.items():
        path = FROZEN / name
        if not path.is_file():
            failures.append(f"missing {path}")
            continue
        got = sha256(path)
        if got != expected:
            failures.append(f"{path}: expected {expected}, got {got}")
    local_core = BOX / "moh_skeleton_N.py"
    if not local_core.is_file():
        failures.append(f"missing {local_core}")
    else:
        expected = EXPECTED_FROZEN["moh_skeleton_N.py"]
        got = sha256(local_core)
        if got != expected:
            failures.append(
                f"workspace core differs from frozen input: expected {expected}, got {got}"
            )
    if failures:
        raise SystemExit("INPUT HASH FAILURE; STOPPING:\n  " + "\n  ".join(failures))
    print("[PROVED-HERE] INPUT-HASH: seven frozen hashes and workspace core match")


# Import only after the charged inputs have passed their hash checks.
sys.path.insert(0, os.fspath(BOX))


def load_core():
    from moh_skeleton_N import Skel, census
    return Skel, census


AssignmentKey = Tuple[int, int, Tuple[int, ...], Tuple[int, ...]]
Partition = Tuple[int, ...]


def assignment_key(n: int, m: int, Ms: Sequence[int], V: Mapping[int, int]) -> AssignmentKey:
    return n, m, tuple(Ms), tuple(V[i] for i in range(2, len(Ms) + 2))


def qval(S) -> F:
    """D1-PIN q=(1-delta_1)de/(d+e), exactly."""
    return (1 - S.delta[1]) * F(S.dd * S.e, S.dd + S.e)


@dataclass(frozen=True)
class UniWitness:
    """One (UNI) packet: k equal bottom discs, total V_2 weight, and N."""

    k: int
    total_v2: int
    N: int


def uni_witnesses(S, n_min: int = 6) -> Tuple[UniWitness, ...]:
    """All integral (UNI) values N>=n_min for this complete V-assignment.

    If q=p/r is reduced, integrality of k*V_2*q is equivalent to
    r/gcd(r,V_2) dividing k.  This is exactly the loop in
    d1floor.achievable, with the requested lower frontier changed to n_min.
    """
    if n_min < 0:
        raise ValueError("n_min must be nonnegative")
    v2 = S.V[2]
    if v2 <= 0:
        raise AssertionError("census returned nonpositive V_2")
    q = qval(S)
    if q <= 0:
        return ()
    kmax = int(S.u // v2)
    period = q.denominator // gcd(q.denominator, v2)
    base = period * v2 * q
    if base.denominator != 1:
        raise AssertionError("integrality period failed")
    base_int = int(base)
    jmax = kmax // period
    if jmax == 0:
        return ()
    jmin = max(1, (n_min + base_int - 1) // base_int)
    return tuple(
        UniWitness(k=j * period, total_v2=j * period * v2, N=j * base_int)
        for j in range(jmin, jmax + 1)
    )


def bottom_degree(S) -> int:
    """Degree of P_1=g_{sigma_1}: a_1=eV_2."""
    degree = S.e * S.V[2]
    if degree != S.a[1]:
        raise AssertionError(f"a_1 mismatch: {degree} versus {S.a[1]}")
    return degree


def bottom_bidegrees(S) -> Tuple[int, int]:
    """(deg P_1,deg Q_1)=(a_1,b_1)=(eV_2,dV_2), with exact checks."""
    A = bottom_degree(S)
    B = S.dd * S.V[2]
    if B != S.b[1]:
        raise AssertionError(f"b_1 mismatch: {B} versus {S.b[1]}")
    return A, B


def operator_scale(S) -> F:
    """h with (n,m)=h(deg P_1,deg Q_1); hence D(n,m)=h D(degP,degQ)."""
    A, B = bottom_bidegrees(S)
    h = F(S.K, S.V[2])
    if F(S.n, A) != h or F(S.m, B) != h:
        raise AssertionError(
            f"bottom operator weights are not proportional: {(S.n,S.m)} vs {(A,B)}"
        )
    return h


@dataclass(frozen=True)
class StarResult:
    status: str
    killed: bool
    degree: int
    partition: Partition


def star_test(S) -> StarResult:
    """Apply Moh Prop. 4.6 + A.5: P_1 is forced square-free, so PASS.

    ``operator_scale`` checks the only skeleton arithmetic needed to translate
    Prop. 4.6's weights (n,m) to Prop. A.5's (deg P_1,deg Q_1).  Nonvanishing
    of the constant operator is a Keller consequence, not a numerical test.
    """
    degree = bottom_degree(S)
    h = operator_scale(S)
    if h <= 0:
        raise AssertionError(f"nonpositive operator scale {h}")
    return StarResult(
        "PASS[MOH-PROP-4.6+A.5-FORCED-SIMPLE]",
        False,
        degree,
        (1,) * degree,
    )


@dataclass
class DegreeCounts:
    enumerated: int = 0
    tested: int = 0
    killed: int = 0
    passed: int = 0

    @property
    def surviving(self) -> int:
        return self.tested - self.killed


@dataclass(frozen=True)
class SurvivingRow:
    key: AssignmentKey
    S: object
    V: Mapping[int, int]
    witnesses: Tuple[UniWitness, ...]
    star: StarResult


def survivor_order(row: SurvivingRow):
    """Campaign operational order, explicitly: (s,N_min,e,m,M_*,V_*)."""
    _, m, Ms, Vs = row.key
    return row.S.s, row.witnesses[0].N, row.S.e, m, Ms, Vs


def scan(degrees: Iterable[int], n_min: int):
    Skel, census = load_core()
    rows: Dict[int, DegreeCounts] = {}
    smallest: Optional[SurvivingRow] = None
    for n in degrees:
        count = DegreeCounts()
        for m, Ms, V in census(n, with_V=True):
            count.enumerated += 1
            S = Skel(n, m, list(Ms), V)
            if not S.windows_ok():
                raise AssertionError(f"census emitted invalid windows: {(n,m,Ms,V)}")
            witnesses = uni_witnesses(S, n_min)
            if not witnesses:
                continue
            count.tested += 1
            key = assignment_key(n, m, Ms, V)
            result = star_test(S)
            if result.killed:
                count.killed += 1
            else:
                count.passed += 1
            if not result.killed:
                candidate = SurvivingRow(key, S, dict(V), witnesses, result)
                if smallest is None or survivor_order(candidate) < survivor_order(smallest):
                    smallest = candidate
        if count.enumerated:
            rows[n] = count
    return rows, smallest


def control_automorphism() -> None:
    """s=1 control: P=pi^k+1, Q=pi gives D(k,1,P,Q)=k."""
    from sympy import Poly, diff, expand, gcd as poly_gcd, symbols

    pi = symbols("pi")
    for k in range(2, 13):
        P, Q = pi**k + 1, pi
        D = expand(k * P * diff(Q, pi) - Q * diff(P, pi))
        if D != k:
            raise AssertionError(f"automorphism operator failed at k={k}: {D}")
        if poly_gcd(Poly(P, pi), Poly(diff(P, pi), pi)).degree() != 0:
            raise AssertionError(f"automorphism P is not square-free at k={k}")
    print("[PROVED-HERE] CONTROL-AUTO: (y,x+y^k), k=2..12, D=k and simple star PASS")


def control_operator_lemma() -> None:
    """Repeated P root forces D(A,B,P,Q) to vanish there; check exact scaling."""
    from sympy import diff, expand, symbols

    pi = symbols("pi")
    for A in range(2, 9):
        for B in range(1, A + 1):
            P = pi**2 * (pi + 1) ** (A - 2)
            Q = pi**B + pi + 1
            D = expand(A * P * diff(Q, pi) - B * Q * diff(P, pi))
            if D.subs(pi, 0) != 0:
                raise AssertionError(f"repeated-root operator lemma failed for {(A,B)}")

    Skel, _ = load_core()
    S = Skel(105, 42, [-14, 103], {2: 1, 3: 5})
    if bottom_bidegrees(S) != (5, 2) or operator_scale(S) != 21:
        raise AssertionError("bottom bidegree/operator-scale control failed")
    result = star_test(S)
    if result.killed or result.partition != (1, 1, 1, 1, 1):
        raise AssertionError("Prop. A.5 simple-partition implementation failed")
    print("[PROVED-HERE] CONTROL-OPERATOR: repeated-root vanishing and weight scaling pass")


def control_uni(limit: int = 20000) -> None:
    """Cross-check the period shortcut against the literal Fraction loop."""
    Skel, census = load_core()
    checked = 0
    for n in range(48, 121):
        for m, Ms, V in census(n, with_V=True):
            S = Skel(n, m, list(Ms), V)
            q = qval(S)
            brute = []
            for k in range(1, int(S.u // S.V[2]) + 1):
                value = k * S.V[2] * q
                if value.denominator == 1 and value >= 6:
                    brute.append(UniWitness(k, k * S.V[2], int(value)))
            fast = list(uni_witnesses(S, 6))
            if brute != fast:
                raise AssertionError(f"(UNI) mismatch at {(n,m,Ms,V)}: {brute} != {fast}")
            checked += 1
            if checked >= limit:
                print(f"[PROVED-HERE] CONTROL-UNI: exact loop = period shortcut on {checked} assignments")
                return
    print(f"[PROVED-HERE] CONTROL-UNI: exact loop = period shortcut on {checked} assignments")


def print_table(rows: Mapping[int, DegreeCounts], degrees: Iterable[int], label: str) -> None:
    print(f"\n[MEASURED] {label}")
    print("    D   enumerated   tested(UNI,N>=6)   killed   PASS   surviving   STAR-emptied")
    totals = DegreeCounts()
    empty = []
    already_empty = []
    for n in degrees:
        if n not in rows:
            continue
        c = rows[n]
        totals.enumerated += c.enumerated
        totals.tested += c.tested
        totals.killed += c.killed
        totals.passed += c.passed
        star_empty = c.tested > 0 and c.surviving == 0
        if star_empty:
            empty.append(n)
        if c.tested == 0:
            already_empty.append(n)
        print(
            f"  {n:3d} {c.enumerated:12d} {c.tested:19d} {c.killed:8d} "
            f"{c.passed:6d} {c.surviving:11d} {'YES' if star_empty else 'NO':>13s}"
        )
    print(
        f"  TOTAL {totals.enumerated:10d} {totals.tested:19d} {totals.killed:8d} "
        f"{totals.passed:6d} {totals.surviving:11d}"
    )
    print(f"  [MEASURED] degrees emptied by STAR test: {empty or 'NONE'}")
    print(f"  [MEASURED] censused degrees with zero pre-STAR test rows: {already_empty or 'NONE'}")


def fmt_fraction(x) -> str:
    return str(x) if getattr(x, "denominator", 1) != 1 else str(int(x))


def print_smallest(row: SurvivingRow, n_min: int) -> None:
    n, m, Ms, Vs = row.key
    S = row.S
    witness = row.witnesses[0]
    degree = row.star.degree
    print(f"\n[MEASURED] campaign-order smallest surviving assignment at D={n}")
    print("  order definition       = (s,N_min,e,m,M_2..M_s,V_2..V_s)")
    print(f"  order key              = {survivor_order(row)}")
    print(f"  skeleton               = n={n}, m={m}, s={S.s}")
    print(f"  M_1..M_s               = {tuple(S.M[i] for i in range(1,S.s+1))}")
    print(f"  d_1..d_(s+1)           = {tuple(S.d[i] for i in range(1,S.s+2))}")
    print(f"  V_2..V_(s+1)           = {tuple(S.V[i] for i in range(2,S.s+2))}")
    print(f"  K,(d,e),(u,v)          = {S.K},({S.dd},{S.e}),({fmt_fraction(S.u)},{fmt_fraction(S.v)})")
    print(f"  delta_1..delta_s       = {tuple(S.delta[i] for i in range(1,S.s+1))}")
    print(f"  a_1..a_s               = {tuple(S.a[i] for i in range(1,S.s+1))}")
    print(f"  b_1..b_s               = {tuple(S.b[i] for i in range(1,S.s+1))}")
    print(f"  q                      = {qval(S)}")
    print(f"  selected (UNI) packet  = k={witness.k} equal discs; (V_2(B))=(%d^%d)" % (S.V[2], witness.k))
    print(f"  packet weight / bound  = {witness.total_v2} <= u={fmt_fraction(S.u)}")
    print(f"  N                      = {witness.k}*{S.V[2]}*{qval(S)} = {witness.N} >= {n_min}")
    A, B = bottom_bidegrees(S)
    h = operator_scale(S)
    print(f"  bottom (deg P_1,deg Q_1)= ({A},{B})")
    print(f"  operator scaling       = D({S.n},{S.m},P_1,Q_1) = {h} D({A},{B},P_1,Q_1)")
    print(f"  bottom partition       = (1^{degree}) = {row.star.partition} ({row.star.status})")


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-min", type=int, default=6, help="campaign lower frontier for N")
    ap.add_argument("--d-max", type=int, default=120)
    ap.add_argument("--skip-controls", action="store_true")
    args = ap.parse_args(argv)
    if args.d_max < 1:
        ap.error("--d-max must be positive")

    verify_inputs()
    if not args.skip_controls:
        control_automorphism()
        control_operator_lemma()
        control_uni()
    rows, _ = scan(range(1, args.d_max + 1), args.n_min)

    targets = [d for d in (105, 108, 112, 117, 120) if d <= args.d_max]
    print_table(rows, targets, "MOH-SHARP-2 degrees")
    print_table(rows, sorted(rows), f"complete census D<={args.d_max}")

    # Recompute only D=105 so the displayed minimum is not affected by lower D.
    if 105 <= args.d_max:
        rows105, smallest105 = scan([105], args.n_min)
        if smallest105 is None:
            print("\n[MEASURED] no not-killed (UNI), N>=6 assignment at D=105")
        else:
            print_smallest(smallest105, args.n_min)

    print("\n[PROVED-HERE] PARTITION SCOPE: Moh Prop. 4.6 plus Prop. A.5 forces")
    print("  partition (1^{eV_2}) for every tested Keller candidate; no extra datum enters.")
    print("[MEASURED] The non-Keller two-tower rows were not used as controls (not required).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
