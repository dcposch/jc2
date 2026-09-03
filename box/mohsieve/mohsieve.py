#!/usr/bin/env python3
"""Typed predicate registry over box/moh_skeleton_full.py.

MEASURED leaderboard for OPEN[MOH-PROGRAM] candidates. Provenance is typed
(PRINTED | DERIVED | CONJECTURE | SOURCE-UNVERIFIED | UNDEFINED). No predicate
is claimed to BE Moh's program.

Fail-closed gates G1–G5 live in `require()` so they survive `python3 -O`.
Load-bearing exact-division checks are explicit (they do not use `assert`).
"""
from __future__ import annotations

import itertools
import os
import sys
import time
from collections import namedtuple
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_BOX = os.path.dirname(_HERE)
if _BOX not in sys.path:
    sys.path.insert(0, _BOX)

import moh_skeleton_full as MS  # noqa: E402
try:
    from .gates import require, fail_closed, reset, FAILURES
except ImportError:
    from gates import require, fail_closed, reset, FAILURES  # noqa: E402

NLO, NHI = 6, 16
LISTING = (105, 108, 112, 117, 120)
MOH_KEYS = set(
    (n, m, tuple(Ms), tuple(sorted(Vs.items())))
    for (n, m, Ms, Vs, _, _, _, _) in MS.MOH_TABLE
)


def Q_of(S, j):
    """Q = V_{j+1} d_j / d_{j+1}. Exact in Z because d_{j+1} | d_j."""
    num = S.V[j + 1] * S.d[j]
    den = S.d[j + 1]
    if den == 0 or num % den != 0:
        raise RuntimeError(
            "GATE-FAIL: d_{j+1} does not divide V_{j+1} d_j "
            "(n=%s j=%s num=%s den=%s)" % (S.n, j, num, den)
        )
    return num // den


# ---------------------------------------------------------------------------
# Card I — Prop 4.6 partition (Grok ideation, untested until this lane)
# ---------------------------------------------------------------------------
def _ok_part(p, tri, sq, A, lo):
    if p <= 0:
        return False
    minor = p <= lo
    major = (p <= tri) or ((p - sq) % A == 0)
    return minor or major


def _reachable_T(Tmax, tri, sq, A, lo):
    """Totals writable as a sum of ok part sizes."""
    if Tmax < 0:
        return set()
    if Tmax == 0:
        return {0}
    if _ok_part(1, tri, sq, A, lo):
        return set(range(Tmax + 1))
    ok_sizes = [p for p in range(1, Tmax + 1) if _ok_part(p, tri, sq, A, lo)]
    reach = [False] * (Tmax + 1)
    reach[0] = True
    for s in range(Tmax + 1):
        if not reach[s]:
            continue
        for p in ok_sizes:
            nxt = s + p
            if nxt > Tmax:
                break
            reach[nxt] = True
    return {t for t, r in enumerate(reach) if r}


def pred_partition(S):
    """Existence of a Prop 4.6 partition of deg p = Q at each level j = s-1..2.

    Q = V_{j+1} d_j/d_{j+1}. One part equals V_j; other parts are major
    ((10)∨(11)) or minor (≤ d_j/(n-M_j), Prop 6.1); a≠0 parts come in Galois
    orbits of size A_j. At most one a=0 part (the factor π).
    """
    for j in range(S.s - 1, 1, -1):
        Q = Q_of(S, j)
        tri, sq, A, Q2 = S.div9(j)
        if Q2 != Q:
            raise RuntimeError("GATE-FAIL: div9 Q mismatch at n=%s j=%s" % (S.n, j))
        if A < 1:
            return False
        V = S.V[j]
        lo = F(S.d[j], S.n - S.M[j])
        if not _ok_part(V, tri, sq, A, lo):
            return False
        Tmax = Q // A
        reach = _reachable_T(Tmax, tri, sq, A, lo)
        ok = False
        if (Q - V) % A == 0 and ((Q - V) // A) in reach:
            ok = True
        if (not ok) and A * V <= Q:
            R = Q - A * V
            for n0 in range(0, R + 1):
                if n0 != 0 and not _ok_part(n0, tri, sq, A, lo):
                    continue
                if (R - n0) % A == 0 and ((R - n0) // A) in reach:
                    ok = True
                    break
        if not ok:
            return False
    return True


def pred_increment(S):
    return all(S.A(j) >= 2 for j in range(1, S.s))


def pred_not_all_11(S):
    return S.any10()


def pred_major_mult(S):
    return all(S.V[j] >= 2 for j in range(2, S.s + 1))


def pred_m2_above_m(S):
    return S.M[2] > S.m


def attempted_l2_swap(S):
    """Probe only: replace V_s by d_s - V_s (u ↔ v at the top form). Not a filter."""
    us = S.d[S.s] - S.V[S.s]
    if us <= 0:
        return False
    V2 = dict(S.V)
    V2[S.s] = us
    T = MS.Skel(S.n, S.m, [S.M[i] for i in range(2, S.s + 1)], {i: V2[i] for i in range(2, S.s + 1)})
    return T.windows_ok() and T.full_ok()


Predicate = namedtuple("Predicate", "name source fn note")

SECOND_POINT_NOTE = (
    "UNDEFINED from the printed text. Def 5.1 constructs ONE tower of major "
    "discs D_s ⊃ ⋯ ⊃ D_1 (census-rebase §1.2, p.179). Prop 4.5 / the top of "
    "p(π) (moh.txt p.186, p.172): q has degree n-M_s = 2, so p has two roots; "
    "one multiplicity is V_s > d_s/2, the complementary multiplicity is "
    "d_s-V_s < d_s/2. The top form of g is L_1^u L_2^v with "
    "u = V_s K/d_s and v = K-u (moh_skeleton_N comment; u+v=K, u>v). "
    "The phrase 'L_2 tower (v roots, u ↔ v)' would mean the Def 5.1 recursion "
    "started from the complementary root, sharing (n, m) and the gcd-chain "
    "d_j = gcd{n, M_1, …, M_{j-1}} (independent of V). That swap is not a "
    "major tower: Def 5.1(2) requires V_s > d_s/(n-M_s) = d_s/2, so "
    "V_s^{L2} = d_s-V_s fails the window and is a MINOR disc (Prop 6.1). "
    "Def 5.1 does not assign lower V_j to the complementary factor; those "
    "are not a function of the L_1 skeleton. Joint admissibility is therefore "
    "not a predicate of a single (n,m,M_*,V_*) row. Probe attempted_l2_swap "
    "(replace V_s by d_s-V_s, keep M_*): 0/6 printed rows survive windows."
)

REGISTRY = [
    Predicate(
        "MOH-INCREMENT",
        "DERIVED",
        pred_increment,
        "A_j ≥ 2 for j=1..s-1. j=1 is the exclusive-or of Moh p.188 "
        "(A|n*V_2 and A∤m*V_2 or vice versa), false at A_1=1; j≥2 is by "
        "analogy with the same automorphism sentence (CONJECTURE residue).",
    ),
    Predicate(
        "NOT-ALL-11",
        "DERIVED",
        pred_not_all_11,
        "Some j in {2..s-1} takes (10). Numerical shadow of Prop 5.6; "
        "r=2 branch datum is OPEN[PROP-5.6-SHADOW].",
    ),
    Predicate(
        "MAJOR-MULT",
        "SOURCE-UNVERIFIED",
        pred_major_mult,
        "V_j ≥ 2 for j=2..s. Opus reading of a major-disc factor as non-simple; "
        "not recovered from the charged transcription of Def 5.1 / p.200 (4)–(7).",
    ),
    Predicate(
        "M2-ABOVE-M",
        "CONJECTURE",
        pred_m2_above_m,
        "M_2 > m. Fable did not find the inequality on the pages read; "
        "OPEN[M2-ABOVE-M]. AM semigroup is AUTOMATIC (not registered).",
    ),
    Predicate(
        "PARTITION",
        "CONJECTURE",
        pred_partition,
        "Card I: Prop 4.6 partition of Q at levels j=s-1..2. Untested encoding "
        "of Def 5.1(4)+Prop 4.6+Prop 6.1. Not claimed to be PROGRAM.",
    ),
    Predicate(
        "SECOND-POINT",
        "UNDEFINED",
        None,
        SECOND_POINT_NOTE,
    ),
]

DEFINED = [p for p in REGISTRY if p.fn is not None]
NAME_OF = {p.name: p for p in REGISTRY}


def eval_pred(pred, S):
    if pred.fn is None:
        raise RuntimeError("SECOND-POINT is UNDEFINED; it is not a filter")
    return bool(pred.fn(S))


def eval_mask(S):
    """Bit i of the mask is DEFINED[i] on S."""
    m = 0
    for i, p in enumerate(DEFINED):
        if p.fn(S):
            m |= 1 << i
    return m


def combo_mask(names):
    m = 0
    for n in names:
        for i, p in enumerate(DEFINED):
            if p.name == n:
                m |= 1 << i
                break
        else:
            raise RuntimeError("unknown predicate %s" % n)
    return m


def holds(mask, need):
    return (mask & need) == need


# ---------------------------------------------------------------------------
# census cache
# ---------------------------------------------------------------------------
Row = namedtuple("Row", "n m Ms V mask S")


def _row_of(n, m, Ms, V):
    S = MS.Skel(n, m, list(Ms), V)
    return Row(n, m, tuple(Ms), dict(V), eval_mask(S), S)


def census_moh_space():
    """(1)–(13) at n≤100, Kmin=2 (Moh's own space)."""
    out = []
    for n in range(4, 101):
        for (m, Ms, V) in MS.census(n, Kmin=2, full=True):
            out.append(_row_of(n, m, Ms, V))
    return out


def census_campaign(dlo=48, dhi=200, Kmin=16):
    """(1)–(13) V-assignments on the campaign space."""
    out = []
    for n in range(dlo, dhi + 1):
        for (m, Ms, V) in MS.census(n, Kmin=Kmin, full=True):
            out.append(_row_of(n, m, Ms, V))
    return out


def group_key(row):
    return (row.n, row.m, row.Ms, row.S.V[row.S.s])


def filter_rows(rows, need):
    if need == 0:
        return list(rows)
    return [r for r in rows if holds(r.mask, need)]


def n100_stats(rows, need=0):
    kept = filter_rows(rows, need)
    classes = set((r.n, r.m) for r in kept)
    return len(kept), len(classes), kept


def six_kept(need=0):
    ok = []
    for (n, m, Ms, Vs, lab, _, _, _) in MS.MOH_TABLE:
        S = MS.Skel(n, m, Ms, Vs)
        mask = eval_mask(S)
        ok.append(holds(mask, need) if need else True)
    return all(ok), ok


def residue_7550(rows_or_n75, need=0, integral=False):
    """(M_2, V_2) pairs at (75,50). If integral, require UNI integer N≥6."""
    pairs = []
    src = rows_or_n75
    for r in src:
        if r.n != 75 or r.m != 50:
            continue
        if need and not holds(r.mask, need):
            continue
        if integral:
            items = [(r.S.V[2], r.S.q(), r.S.u)]
            if not MS.uni_hits(items, NLO, None):
                continue
        pairs.append((r.Ms[0], r.S.V[2]))
    return sorted(set(pairs))


def g2_ok(pairs):
    return set(pairs) == {(55, 2), (55, 3)}


def groups_of_rows(rows, need=0):
    G = {}
    for r in filter_rows(rows, need):
        G.setdefault(group_key(r), []).append(r)
    return G


def emptied_degrees(rows, need, dlo=48, dhi=200):
    base = set(r.n for r in rows)
    G = groups_of_rows(rows, need)
    live = set(k[0] for k in G)
    return sorted(n for n in range(dlo, dhi + 1) if n in base and n not in live)


def knapsack_degree(rows, n, need=0):
    """UNI N≥6, UNI [6,16], mixed [6,16], D=108 UNI-rows in [6,16]."""
    G = groups_of_rows([r for r in rows if r.n == n], need)
    uni6 = uni16 = mixed16 = rows16 = 0
    for items_rows in G.values():
        items = [(R.S.V[2], R.S.q(), R.S.u) for R in items_rows]
        h1 = bool(MS.uni_hits(items, NLO, None))
        h2 = bool(MS.uni_hits(items, NLO, NHI))
        hm, _c = MS.mixed_hit(items, NLO, NHI)
        if h1:
            uni6 += 1
        if h2:
            uni16 += 1
        if hm or h2:
            mixed16 += 1
        if n == 108:
            for R in items_rows:
                if MS.uni_hits([(R.S.V[2], R.S.q(), R.S.u)], NLO, NHI):
                    rows16 += 1
    return dict(
        groups=len(G),
        uni_ge6=uni6,
        uni_6_16=uni16,
        mixed_6_16=mixed16,
        rows_6_16=rows16,
    )


def combo_names():
    """EMPTY + every singleton + every pair/triple of G1-passing defined preds."""
    passing = []
    for p in DEFINED:
        kept, _ = six_kept(combo_mask([p.name]))
        if kept:
            passing.append(p.name)
    combos = [([], "EMPTY")]
    for r in range(1, 4):
        for c in itertools.combinations(passing, r):
            combos.append((list(c), " & ".join(c)))
    return passing, combos


def two_by_two(rows_n100):
    """Four cells of M2-ABOVE-M vs MAJOR-MULT on the n≤100 census."""
    i_m2 = next(i for i, p in enumerate(DEFINED) if p.name == "M2-ABOVE-M")
    i_mm = next(i for i, p in enumerate(DEFINED) if p.name == "MAJOR-MULT")
    cells = {(1, 1): 0, (1, 0): 0, (0, 1): 0, (0, 0): 0}
    for r in rows_n100:
        a = 1 if (r.mask >> i_m2) & 1 else 0
        b = 1 if (r.mask >> i_mm) & 1 else 0
        cells[(a, b)] += 1
    return cells


def solo_kills(rows_n100, rows_d120, rows_d200):
    base100 = len(rows_n100)
    base120 = len(groups_of_rows(rows_d120, 0))
    base200 = len(groups_of_rows(rows_d200, 0))
    out = []
    for p in DEFINED:
        need = combo_mask([p.name])
        k100 = base100 - n100_stats(rows_n100, need)[0]
        g120 = len(groups_of_rows(rows_d120, need))
        g200 = len(groups_of_rows(rows_d200, need))
        out.append(
            dict(
                name=p.name,
                source=p.source,
                solo_kill_n100=k100,
                vacuous_n100=(k100 == 0),
                groups_d120=g120,
                groups_d200=g200,
                solo_kill_g120=base120 - g120,
                solo_kill_g200=base200 - g200,
            )
        )
    return out


def leaderboard_row(rows_n100, rows_camp, label, names):
    need = combo_mask(names) if names else 0
    n_rows, n_cls, kept = n100_stats(rows_n100, need)
    six_ok, _ = six_kept(need)
    res = residue_7550(rows_n100, need, integral=False)
    res_i = residue_7550(rows_n100, need, integral=True)
    G = groups_of_rows(rows_camp, need)
    n_g = len(G)
    empty = emptied_degrees(rows_camp, need)
    listing = {}
    d108_rows = 0
    for d in LISTING:
        ks = knapsack_degree(rows_camp, d, need)
        listing[d] = ks
        if d == 108:
            d108_rows = ks["rows_6_16"]
    return dict(
        label=label,
        names=names,
        rows100=n_rows,
        classes100=n_cls,
        six=six_ok,
        res7550=res,
        res7550_int=res_i,
        g2=g2_ok(res_i),
        groups200=n_g,
        emptied=empty,
        listing=listing,
        d108_rows_6_16=d108_rows,
    )


def print_lb(row):
    listing = row["listing"]
    alive = ",".join(
        str(listing[d]["uni_ge6"]) + "/" + str(listing[d]["mixed_6_16"])
        for d in LISTING
    )
    print(
        "  %-40s %4d/%-2d  %3s  %-18s  g=%5d  empty=%s  "
        "N>=6|mix[6,16]@105..120=%s  D108_rows[6,16]=%d"
        % (
            row["label"][:40],
            row["rows100"],
            row["classes100"],
            "6/6" if row["six"] else "NO",
            str(row["res7550_int"])[:18],
            row["groups200"],
            str(row["emptied"]) if row["emptied"] else "none",
            alive,
            row["d108_rows_6_16"],
        )
    )


def run_g1_g3_controls(rows_n100, rows_d120, rows_d200):
    print("\n== G1–G3 / EMPTY negative control ==")
    kept, bits = six_kept(0)
    require("G1 EMPTY keeps 6/6", kept, str(bits))
    n_rows, n_cls, _ = n100_stats(rows_n100, 0)
    require("G3 EMPTY rows n<=100 = 658", n_rows == 658, str(n_rows))
    require("G3 EMPTY classes n<=100 = 63", n_cls == 63, str(n_cls))
    g120 = len(groups_of_rows(rows_d120, 0))
    g200 = len(groups_of_rows(rows_d200, 0))
    require("EMPTY groups 48<=D<=120 = 1189", g120 == 1189, str(g120))
    require("EMPTY groups 48<=D<=200 = 14016", g200 == 14016, str(g200))
    res = residue_7550(rows_n100, 0, integral=False)
    require(
        "EMPTY (75,50) is the 9-row superset (not yet G2)",
        len(res) >= 2 and (55, 2) in res and (55, 3) in res,
        str(res),
    )
    for p in DEFINED:
        need = combo_mask([p.name])
        k6, bits = six_kept(need)
        tag = "G1 %s keeps 6/6" % p.name
        if p.name in ("MOH-INCREMENT", "NOT-ALL-11", "MAJOR-MULT", "M2-ABOVE-M"):
            require(tag, k6, str(bits))
        else:
            print("  [meas] %s -> %s  bits=%s" % (tag, k6, bits))


def run_g2_on_named(rows_n100, names, expect=True):
    need = combo_mask(names)
    res_i = residue_7550(rows_n100, need, integral=True)
    ok = g2_ok(res_i)
    require(
        "G2 %s after integrality is {(55,2),(55,3)}" % (" & ".join(names),),
        ok == expect if not expect else ok,
        str(res_i),
    )
    return res_i


def main(argv=None):
    t0 = time.time()
    reset()
    print("box/mohsieve/mohsieve.py — typed predicate harness")
    print("DEFINED: %s" % [p.name for p in DEFINED])
    print("UNDEFINED: SECOND-POINT")
    print("\n-- SECOND-POINT (not a filter) --")
    print(SECOND_POINT_NOTE)
    print("\n-- L2-swap probe on Moh's six (not registered as a sieve) --")
    for (n, m, Ms, Vs, lab, _, _, _) in MS.MOH_TABLE:
        S = MS.Skel(n, m, Ms, Vs)
        print("   %-24s attempted_l2_swap=%s  u_s=%s  u=%s v=%s"
              % (lab, attempted_l2_swap(S), S.d[S.s] - S.V[S.s],
                 S.u, (S.K - S.u)))

    print("\n== enumerating n<=100 (Kmin=2) ==")
    t1 = time.time()
    rows100 = census_moh_space()
    print("   %d rows  [%.2fs]" % (len(rows100), time.time() - t1))

    print("== enumerating 48<=D<=200 (Kmin=16) ==")
    t1 = time.time()
    rows_camp = census_campaign(48, 200, 16)
    print("   %d V-assignments  [%.2fs]" % (len(rows_camp), time.time() - t1))
    rows120 = [r for r in rows_camp if r.n <= 120]

    run_g1_g3_controls(rows100, rows120, rows_camp)

    print("\n== SOLO kill counts (vacuous iff solo kill = 0 on the base) ==")
    for rec in solo_kills(rows100, rows120, rows_camp):
        print(
            "  %-16s source=%-18s  n100 kill %3d%s  g120 kill %4d  g200 kill %5d"
            % (
                rec["name"],
                rec["source"],
                rec["solo_kill_n100"],
                " VACUOUS" if rec["vacuous_n100"] else "",
                rec["solo_kill_g120"],
                rec["solo_kill_g200"],
            )
        )

    print("\n== G2 on the charged candidate stacks ==")
    run_g2_on_named(rows100, ["MOH-INCREMENT", "NOT-ALL-11", "MAJOR-MULT"])
    run_g2_on_named(rows100, ["M2-ABOVE-M"])

    cells = two_by_two(rows100)
    print("\n== M2-ABOVE-M vs MAJOR-MULT 2x2 on n<=100 (658 rows) ==")
    print("            MAJOR-MULT=1   MAJOR-MULT=0")
    print("  M2>m =1   %12d   %12d" % (cells[(1, 1)], cells[(1, 0)]))
    print("  M2>m =0   %12d   %12d" % (cells[(0, 1)], cells[(0, 0)]))
    impl_m2_mm = cells[(1, 0)] == 0
    impl_mm_m2 = cells[(0, 1)] == 0
    print("  M2-ABOVE-M => MAJOR-MULT? %s (off-diag M2&~MM = %d)"
          % (impl_m2_mm, cells[(1, 0)]))
    print("  MAJOR-MULT => M2-ABOVE-M? %s (off-diag MM&~M2 = %d)"
          % (impl_mm_m2, cells[(0, 1)]))

    passing, combos = combo_names()
    print("\n== LEADERBOARD (passing G1 names: %s) ==" % passing)
    print("  (alive columns = uni N>=6 / mixed [6,16] at D=105,108,112,117,120)")
    board = []
    for names, label in combos:
        row = leaderboard_row(rows100, rows_camp, label, names)
        board.append(row)
        print_lb(row)

    print("\nwall mohsieve %.1fs" % (time.time() - t0))
    fail_closed()
    print("ALL mohsieve GATES GREEN.")
    return dict(
        rows100=rows100,
        rows_camp=rows_camp,
        board=board,
        cells=cells,
        passing=passing,
    )


if __name__ == "__main__":
    main()
