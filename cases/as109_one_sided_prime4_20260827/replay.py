#!/usr/bin/env python3
"""Fail-closed replay for the AS109 one-sided prime/4 composition.

This script pins every AS109-named non-prompt report present at the history
snapshot, pins the theorem inputs, checks the exact source-translation gauge,
and verifies the finite arithmetic routing used in the producer report.  It
does not re-prove the cited characteristic-zero automorphy theorems.
"""

from __future__ import annotations

from hashlib import sha256
from math import comb, gcd, isqrt
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[2]
CASE = Path(__file__).resolve().parent
P = 109


class ReplayFailure(RuntimeError):
    pass


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def verify_manifest(path: Path) -> list[str]:
    seen: list[str] = []
    for number, raw in enumerate(path.read_text().splitlines(), 1):
        if not raw.strip():
            continue
        parts = raw.split(maxsplit=1)
        if len(parts) != 2 or len(parts[0]) != 64:
            raise ReplayFailure(f"bad manifest line {path.name}:{number}")
        expected, rel = parts
        target = ROOT / rel
        if not target.is_file():
            raise ReplayFailure(f"missing pinned input: {rel}")
        got = file_sha(target)
        if got != expected:
            raise ReplayFailure(
                f"hash mismatch for {rel}: expected {expected}, got {got}"
            )
        seen.append(rel)
    if len(seen) != len(set(seen)):
        raise ReplayFailure(f"duplicate path in {path.name}")
    return seen


def require_text(rel: str, snippets: tuple[str, ...]) -> None:
    text = (ROOT / rel).read_text()
    for snippet in snippets:
        if snippet not in text:
            raise ReplayFailure(f"missing charged statement in {rel}: {snippet}")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def moskowicz_invariant_is_covered(c: int) -> bool:
    return c == 1 or c == 4 or is_prime(c)


Poly = dict[tuple[int, int], int]


def clean(poly: Poly) -> Poly:
    return {mon: value for mon, value in poly.items() if value}


def add(a: Poly, b: Poly, scale: int = 1) -> Poly:
    out = dict(a)
    for mon, value in b.items():
        out[mon] = out.get(mon, 0) + scale * value
    return clean(out)


def mul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for (i, j), av in a.items():
        for (k, ell), bv in b.items():
            mon = (i + k, j + ell)
            out[mon] = out.get(mon, 0) + av * bv
    return clean(out)


def power(a: Poly, n: int) -> Poly:
    out: Poly = {(0, 0): 1}
    base = dict(a)
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n //= 2
    return out


def derivative(a: Poly, variable: int) -> Poly:
    out: Poly = {}
    for (i, j), value in a.items():
        exponent = i if variable == 0 else j
        if exponent:
            mon = (i - 1, j) if variable == 0 else (i, j - 1)
            out[mon] = exponent * value
    return clean(out)


def jacobian(a: Poly, b: Poly) -> Poly:
    return add(mul(derivative(a, 0), derivative(b, 1)),
               mul(derivative(a, 1), derivative(b, 0)), scale=-1)


def degree_y(a: Poly) -> int:
    return max((j for (_, j), value in a.items() if value), default=-1)


def leading_y_x_degree(a: Poly) -> int:
    top = degree_y(a)
    return max((i for (i, j), value in a.items() if value and j == top), default=-1)


def x_translate(a: Poly, tau: int) -> Poly:
    out: Poly = {}
    for (i, j), value in a.items():
        for k in range(i + 1):
            mon = (k, j)
            out[mon] = out.get(mon, 0) + value * comb(i, k) * tau ** (i - k)
    return clean(out)


def gauge_a(a: Poly, tau: int) -> Poly:
    out = x_translate(a, tau)
    fermat_quotient, remainder = divmod(tau - tau**P, P)
    if remainder:
        raise ReplayFailure("source translation is not integral")
    out = add(out, {(0, 0): fermat_quotient})
    for i in range(1, P):
        coefficient, remainder = divmod(comb(P, i), P)
        if remainder:
            raise ReplayFailure(f"binomial coefficient C({P},{i}) not p-divisible")
        out = add(out, {(i, 0): -coefficient * tau ** (P - i)})
    return clean(out)


def gauge_b(b: Poly, tau: int) -> Poly:
    return x_translate(b, tau)


def gauge_checks() -> dict[str, object]:
    a: Poly = {(108, 0): 7, (107, 2): 5, (3, 12): 11, (0, 0): -4}
    b: Poly = {(9, 6): 2, (1, 1): 3, (0, 0): 5}
    tau, upsilon = 2, 3
    a_tau = gauge_a(a, tau)
    b_tau = gauge_b(b, tau)
    if a_tau.get((108, 0), 0) != 7 - tau:
        raise ReplayFailure("degree-108 gauge section formula failed")
    if degree_y(a_tau) != degree_y(a) or degree_y(b_tau) != degree_y(b):
        raise ReplayFailure("source translation changed an actual y-degree")
    if leading_y_x_degree(a_tau) != leading_y_x_degree(a):
        raise ReplayFailure("source translation changed deg_x of A's top y coefficient")
    if leading_y_x_degree(b_tau) != leading_y_x_degree(b):
        raise ReplayFailure("source translation changed deg_x of B's top y coefficient")
    if gauge_a(a_tau, upsilon) != gauge_a(a, tau + upsilon):
        raise ReplayFailure("A source translations do not compose additively")
    if gauge_b(b_tau, upsilon) != gauge_b(b, tau + upsilon):
        raise ReplayFailure("B source translations do not compose additively")
    normalized = gauge_a(a, a[(108, 0)])
    if normalized.get((108, 0), 0) != 0:
        raise ReplayFailure("gauge section did not set [x^108 y^0]A to zero")
    return {
        "action": "free additive x-source translation (formula checked)",
        "section_scope": "deg_x(A)<=108",
        "section": "[x^108*y^0]A=0",
        "degree_y_preserved": True,
        "top_y_leading_x_degree_preserved": True,
        "proof_dependency": False,
    }


def degree_route_checks() -> dict[str, object]:
    # If n is prime or four, C=gcd(n,deg_x q_n) is always 1, 4, or prime.
    for n in (2, 3, 4, 5):
        for q_degree in range(0, 12 * n + 1):
            c = gcd(n, q_degree)
            if not moskowicz_invariant_is_covered(c):
                raise ReplayFailure(f"n={n}, deg_x(q_n)={q_degree} escaped")

    # Six is the first degree with an unhandled invariant, and exactly C=6
    # survives the cited theorem.
    for q_degree in range(0, 145):
        c = gcd(6, q_degree)
        open_by_prime4 = not moskowicz_invariant_is_covered(c)
        if open_by_prime4 != (q_degree % 6 == 0):
            raise ReplayFailure("n=6 residual invariant classification failed")

    # At n=6 the history shear requires d=gcd(m,6)>2, hence 3|m.
    for m in range(1, 241):
        open_by_gcd_shear = gcd(m, 6) > 2
        if open_by_gcd_shear != (m % 3 == 0):
            raise ReplayFailure("n=6 partial-degree gcd classification failed")

    # Common-core translation: q_6=beta*h^(6/d).  C=6 is equivalent to
    # 3|H for d=3 and to 6|H for d=6, including H=0.
    for m in range(1, 241):
        d = gcd(m, 6)
        if d not in (3, 6):
            continue
        b = 6 // d
        for h_degree in range(0, 121):
            c = gcd(6, b * h_degree)
            expected = h_degree % (3 if d == 3 else 6) == 0
            if (c == 6) != expected:
                raise ReplayFailure("common-core n=6 translation failed")

    excluded = [n for n in range(1, 6) if n == 1 or n == 4 or is_prime(n)]
    if excluded != [1, 2, 3, 4, 5]:
        raise ReplayFailure("small target-degree exclusion list changed")
    return {
        "excluded_actual_target_y_degrees": excluded,
        "first_not_excluded": 6,
        "n6_required": {
            "deg_y_P_min_by_max11": 12,
            "three_divides_deg_y_P": True,
            "six_divides_deg_x_q6": True,
            "common_core": "d=3 => 3|H; d=6 => 6|H",
        },
    }


def n6_keller_control() -> dict[str, object]:
    # u=x+y, v=y+u^6, P=u+v^2, Q=v.  This determinant-one automorphism
    # occupies numerical type (m,n)=(12,6), with constant leading terms.
    x: Poly = {(1, 0): 1}
    y: Poly = {(0, 1): 1}
    u = add(x, y)
    v = add(y, power(u, 6))
    p_coord = add(u, power(v, 2))
    q_coord = v
    if jacobian(p_coord, q_coord) != {(0, 0): 1}:
        raise ReplayFailure("n=6 Keller control lost determinant one")
    if (degree_y(p_coord), degree_y(q_coord)) != (12, 6):
        raise ReplayFailure("n=6 Keller control has wrong partial degrees")
    q6 = {i: value for (i, j), value in q_coord.items() if j == 6}
    p12 = {i: value for (i, j), value in p_coord.items() if j == 12}
    if q6 != {0: 1} or p12 != {0: 1}:
        raise ReplayFailure("n=6 Keller control has wrong leading coefficients")
    return {
        "map": "u=x+y; v=y+u^6; (P,Q)=(u+v^2,v)",
        "jacobian": 1,
        "actual_y_degrees": [12, 6],
        "leading_x_degrees": [0, 0],
        "role": "scope control only; not an AS109 lift",
    }


def main() -> None:
    history = verify_manifest(CASE / "HISTORY.sha256")
    inputs = verify_manifest(CASE / "INPUTS.sha256")
    if len(history) != 40:
        raise ReplayFailure(f"expected 40 AS109 history reports, got {len(history)}")

    require_text(
        "xmodel/as109-partial-y-history-stop-20260824.md",
        (
            "`A=gcd(deg_y P,deg_x a_m)`",
            "`C=gcd(deg_y Q,deg_x b_n)`",
            "`{1,4} union primes`",
            "case uses `gcd(N,0)=N` and is explicitly handled in the paper.",
            "`ca974bd7a3603262952c9a5751bc7466c71b2ed47693489e5991096846674419`",
        ),
    )
    require_text(
        "xmodel/as109-partial-y-history-review-grok-20260824.md",
        (
            "GGV and Moskowicz are written over an arbitrary characteristic-zero field.",
            "Theorem 2.7 covers a coordinate of actual `y`-degree prime or four, including constant leadings via `gcd(N,0)=N`.",
        ),
    )
    require_text(
        "xmodel/as109-support-review-grok-20260824.md",
        ("noninjective over `Q_109`", "109-to-1 onto balls over `(0,b)`"),
    )
    require_text(
        "xmodel/gcd3-69-coverage-composition-20260824.md",
        ("MAXIMUM ACTUAL y-DEGREE AT MOST ELEVEN",),
    )

    payload = {
        "schema": "as109-one-sided-prime4-composition-v1",
        "verdict": "PASS-AS109-ONE-SIDED-TARGET-FLOOR-SIX",
        "history_reports_pinned": len(history),
        "theorem_inputs_pinned": len(inputs),
        "theorem": "exact AS109 lift => deg_y(Q)=deg_y(B)>=6",
        "gauge": gauge_checks(),
        "degree_routing": degree_route_checks(),
        "n6_scope_control": n6_keller_control(),
        "newton_n2_job": "STOP-AS-HISTORY-DUPLICATE",
        "next_arithmetic_corner": "n=6 on the residual invariant stratum",
        "support_rectangle_run": False,
        "aws_used": False,
        "heavy_computation": False,
        "lift_found": False,
        "lift_excluded_in_all_degrees": False,
        "jc2_inference": False,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except ReplayFailure as exc:
        raise SystemExit(f"FAIL-CLOSED: {exc}") from exc
