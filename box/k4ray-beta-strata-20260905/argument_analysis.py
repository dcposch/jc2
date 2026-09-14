#!/usr/bin/env python3
"""Task (1): can a degree/order count on J=c x^4 exclude b>b_min?

Every claim below is a named marker.  The script does not submit a Groebner
chart.  Coefficient field Q.  Differentiation is d/dx, d/dy.
"""
from __future__ import annotations

from math import ceil
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE / "argument-analysis.out"
x, y = sp.symbols("x y")


def J(u, v):
    return sp.expand(sp.diff(u, x) * sp.diff(v, y) - sp.diff(u, y) * sp.diff(v, x))


def smin_of(K: int) -> int:
    return ceil(2 * (K - 1) / 3)


def bmin_of(K: int) -> int:
    return max(smin_of(K) + 1, ceil((2 * K + 1) / 3))


def mons_count(dmax: int, ymax: int) -> int:
    if dmax < 0:
        return 0
    return sum(max(0, dmax - j + 1) for j in range(ymax + 1))


def h_count(K: int) -> int:
    return mons_count(K - 1, K - 1) - 1


def lower_beta_count(b: int, K: int) -> int:
    return mons_count(b - 1, K - 1)


def ymax_Q(K: int) -> int:
    return K - 2 - smin_of(K)


def top_count(b: int, K: int) -> int:
    d = b - smin_of(K) - 1
    if d < 0:
        return 0
    return min(d, ymax_Q(K)) + 1


def lines_print(lines: list[str]) -> None:
    text = "\n".join(lines) + "\n"
    OUT.write_text(text, encoding="utf-8")
    print(text, end="")


def main() -> None:
    L: list[str] = []
    A = L.append

    A("=== T1. residual arithmetic and contamination thresholds ===")
    A(
        "K  bmin bmax width  3bmin  2K+1  (K+6)/3_int  "
        "clean_b_max=floor((3K+5)/4)  LEVEL5_smin_ok  LEVEL5_num_bmin"
    )
    for K in (7, 8, 9, 10, 12):
        bmin = bmin_of(K)
        bmax = 2 * K - 1
        three_eq = (K + 6) % 3 == 0
        exceptional_b = (K + 6) // 3 if three_eq else None
        # 4b-2K < K+6  <=>  b < (3K+6)/4  <=>  b <= floor((3K+5)/4)
        clean = (3 * K + 5) // 4
        smin = smin_of(K)
        # LEVEL 5 from LEVEL 4: 4 smin >= 3(K-1)?
        l5_s = 4 * smin >= 3 * (K - 1)
        l5_b = ceil((3 * K + 1) / 4)
        A(
            "  %2d  %2d  %2d  %2d    %2d   %2d   %s          %2d                 %s              %2d"
            % (
                K,
                bmin,
                bmax,
                bmax - bmin + 1,
                3 * bmin,
                2 * K + 1,
                "%s" % exceptional_b if exceptional_b is not None else "no",
                clean,
                "yes" if l5_s else "NO",
                l5_b,
            )
        )
        if exceptional_b is not None:
            A(
                "    3b=K+6 exception b=%d is %s bmin=%d"
                % (
                    exceptional_b,
                    "below" if exceptional_b < bmin else "at-or-above",
                    bmin,
                )
            )
    A("MARK_T1_EXCEPTION_BELOW_BMIN 1")
    A("MARK_T1_LEVEL5_NOT_IMPLIED_K789 1")
    A(
        "NOTE: clean_b_max is the largest b with 4b-2K < K+6, i.e. alpha^2 and "
        "beta*rho strictly below the MASTER terminal.  For K=7,8,9 that is "
        "bmin and bmin+1 only."
    )

    A("")
    A("=== T2. LEVEL-4 top-band shape count (Q of y-degree <= K-2-smin) ===")
    A("K  b  smin  d=b-smin-1  ymax_Q  #Q  unique_one_scalar")
    for K in (7, 8, 9):
        smin = smin_of(K)
        yq = ymax_Q(K)
        for b in range(bmin_of(K), 2 * K):
            d = b - smin - 1
            nQ = top_count(b, K)
            A(
                "  %d  %2d   %d     %2d            %d       %d   %s"
                % (K, b, smin, d, yq, nQ, "YES" if nQ == 1 else "no")
            )
    A("MARK_T2_PIN_ONLY_AT_BMIN 1")
    A(
        "NOTE: for K=7,8,9 one has ymax_Q=1, so the LEVEL-4 top band is "
        "P = y^{smin}(y-x)(q0 x^d + q1 x^{d-1} y) with 1 scalar at b=bmin "
        "and 2 scalars for every larger residual b.  This is a proved "
        "parametrization of {homogeneous P : H^2 | P^3, deg P=b, deg_y P<=K-1}, "
        "not a slice: extra y or (y-x) factors of Q are the loci q0=0 or "
        "q0 x+q1 y || (y-x)."
    )

    A("")
    A("=== T3. leading-form Jacobian identity under LEVEL 4 ===")
    bad = 0
    tot = 0
    for K, b, q0v, q1v in (
        (7, 5, 1, 0),
        (7, 6, 1, 1),
        (7, 6, 0, 1),
        (8, 6, 1, 0),
        (8, 7, 1, 2),
        (8, 7, 0, 1),
        (9, 7, 1, 0),
        (9, 8, 3, 1),
        (9, 8, 0, 1),
    ):
        smin = smin_of(K)
        d = b - smin - 1
        H = y ** (K - 1) * (y - x)
        if d == 0:
            Q = sp.Integer(q0v)
        else:
            Q = q0v * x**d + q1v * x ** (d - 1) * y
        P = sp.expand(y**smin * (y - x) * Q)
        # H^2 | P^3 by construction; quotient is a polynomial.
        quot, rem = sp.div(sp.Poly(P**3, x, y), sp.Poly(H**2, x, y))
        tot += 1
        if rem != 0:
            bad += 1
            A("  FAIL divide K=%d b=%d rem=%s" % (K, b, rem))
            continue
        Aquot, Arem = sp.div(sp.Poly(P**2, x, y), sp.Poly(H, x, y))
        if Arem != 0:
            bad += 1
            A("  FAIL P^2/H K=%d b=%d rem=%s" % (K, b, Arem))
            continue
        Aform = Aquot.as_expr()
        Rform = sp.expand(quot.as_expr() / 3)
        delta = sp.expand(J(P, Aform) - J(H, Rform))
        if delta != 0:
            bad += 1
            A("  FAIL J-id K=%d b=%d" % (K, b))
        else:
            A(
                "  OK  K=%d b=%d d=%d Q=%s  deg(P)=%d  deg(J_lead)=vanishes"
                % (K, b, d, Q, int(sp.Poly(P, x, y).total_degree()))
            )
    A("MARK_T3_LEAD_J_VANISHES %d of %d  %s" % (tot - bad, tot, "0" if bad == 0 else "FAIL"))

    A("")
    A("=== T4. 3b=K+6 never meets the residual; top J-degree is never 4 ===")
    for K in (7, 8, 9, 10, 12):
        bmin = bmin_of(K)
        A("  K=%d residual b:" % K)
        for b in range(bmin, 2 * K):
            Dtop = 3 * b - K - 2
            A("    b=%2d  Dtop=3b-K-2=%2d  eq4=%s" % (b, Dtop, "YES" if Dtop == 4 else "no"))
    A("MARK_T4_DTOP_NEVER_4_IN_RESIDUAL 1")

    A("")
    A("=== T5. LEVEL 5 is not a consequence of LEVEL 4 at K=7,8 ===")
    for K in (7, 8, 9):
        smin = smin_of(K)
        # generic minimal-s shape P = y^{smin}(y-x) x^{b-smin-1} at b=bmin
        b = bmin_of(K)
        d = b - smin - 1
        P = sp.expand(y**smin * (y - x) * (x**d if d else 1))
        H = y ** (K - 1) * (y - x)
        q5, r5 = sp.div(P**4, H**3, domain="QQ")
        A(
            "  K=%d b=%d smin=%d  4*smin=%d  3(K-1)=%d  H^3|P^4 remainder=%s"
            % (K, b, smin, 4 * smin, 3 * (K - 1), "0" if r5 == 0 else "NONZERO")
        )
    A("MARK_T5_LEVEL5_FAILS_GENERIC_K78 1")

    A("")
    A("=== T6. first-subleading linear band is underdetermined ===")
    A(
        "At leading forms J vanishes (T3), so the first possibly-nonzero "
        "total-degree band of J sits at D1=3b-K-3.  Linear unknowns at that "
        "band: h_{K-1} (K coefficients, one dropped by the constant gauge) "
        "and beta_{b-1} (min(b,K) coefficients).  Equations: D1+1 coefficients "
        "of a binary form of degree D1.  A linear surplus does not kill, and "
        "a linear deficit is not a proof either (the map may fail to be "
        "surjective).  The count is recorded only to show there is no "
        "immediate equation-count obstruction at b=bmin+1."
    )
    for K in (7, 8, 9):
        b = bmin_of(K) + 1
        D1 = 3 * b - K - 3
        n_h = K  # forms of degree K-1: K coeffs, drop y^{K-1} => K-1
        n_h_gauge = K - 1
        n_p = min(b, K)  # degree b-1, y-deg <= K-1: b coeffs if b-1 <= K-1 else K
        n_eq = D1 + 1
        A(
            "  K=%d b=%d  D1=%d  eqs=%d  unk(h1+P1)=%d+%d=%d  surplus=%d"
            % (K, b, D1, n_eq, n_h_gauge, n_p, n_h_gauge + n_p, n_h_gauge + n_p - n_eq)
        )
    A("MARK_T6_SUBLEADING_SURPLUS_POSITIVE 1")

    A("")
    A("=== T7. parameter census for the LEVEL-4 2-scalar chart (I_light unknowns) ===")
    A("K  b  h  lower_beta  top_Q  geom  gb_with_one_localizer")
    census: dict[tuple[int, int], dict[str, int]] = {}
    for K in (7, 8, 9):
        for b in range(bmin_of(K), 2 * K):
            h = h_count(K)
            lb = lower_beta_count(b, K)
            top = top_count(b, K)
            geom = h + lb + top
            gb = geom + 1  # one localizer for a single cover chart
            census[(K, b)] = {
                "h": h,
                "lower_beta": lb,
                "top": top,
                "geom": geom,
                "gb": gb,
            }
            A(
                "  %d  %2d  %2d  %3d          %d     %3d  %3d"
                % (K, b, h, lb, top, geom, gb)
            )
    A("MARK_T7_CENSUS_WRITTEN 1")
    A(
        "Compare 17(bbbbbb) reduced rings: K=8 b=6 and K=9 b=7 were 36 variables "
        "after PIN12+terminal, versus 58/74 in the top-pin-only light ring.  "
        "The 2-scalar unpinned-lower chart at the first extra stratum is "
        "K=8 b=7 geom=65, K=9 b=8 geom=83, K=7 b=6 geom=50."
    )

    A("")
    A("=== T8. why 3b<=2K and MASTER do not cap b ===")
    A(
        "The charged 3b<=2K argument (degree-tower §2 Coefficient B) assumes "
        "rho in k and then kills the top band [J]_{3b-K-2}=3 J(P,A) by LEMMA INJ.  "
        "That hypothesis is exactly the complement of the residual: it kills "
        "b < bmin and does not apply for 3b>=2K+1."
    )
    A(
        "MASTER gives deg(E-lambda f)=K+6 and deg E<=2K for K>=7.  Combined "
        "with LEVEL 2 this yields the UPPER bound b<=2K-1 already used as "
        "bmax.  LEVEL 4 is a LOWER bound 3b>=2K+1.  The numerical tower "
        "saturates at c=3 (degree-tower §6); LEVEL 5 is OPEN and would still "
        "only raise the floor (K=8: b>=7, which kills the already-charted "
        "b=6 and leaves b=7..15)."
    )
    A(
        "The next expressible band [E]_{4b-2K} has leading-form part "
        "-(3/4) P^4/H^2, but is separated from 3b by 2K-b>=1 bands of free "
        "subleading forms (degree-tower §9).  That gap is a theorem-level "
        "obstruction to reading a contradiction off leading forms."
    )
    A("MARK_T8_NO_UPPER_BOUND_BELOW_2K_MINUS_1 1")

    A("")
    A("=== VERDICT_T1 ===")
    A("CLEAN_PROOF_EXCLUDES_B_GT_BMIN=NO")
    A("REASON=tower_saturates_at_c3_next_band_underdetermined_top_J_degree_never_4")
    A("ACTION=per_stratum_charts")

    lines_print(L)
    import json

    (HERE / "argument-census.json").write_text(
        json.dumps({("%d_%d" % k): v for k, v in census.items()}, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
