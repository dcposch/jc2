#!/usr/bin/env python3
"""BOOK-OFFAXIS engine: off-axis (some b_i >= 2) entry census + mixed-merge
cells.  Additive over cases/book_enum.py (reuses entries/tdu_rows verbatim);
exact integer/Fraction arithmetic throughout.

Sector: BOOK-ENUM.md erratum — the book enumerated only the all-b=1 axis;
entries with b_i >= 2 carry M = b_i (MP4) down their chains (mu_e | M by
St 8.4) and can meet in mixed merges (all mu_e >= 2), never enumerated.

Step-1 census filters (all printed/promoted tier):
  - layer E reused: global type (al,be), td = sum Lambda_i, per-pole
    (a,b,nu) from tdu_rows(Lambda_i) (St 5.2 + Prop 5.6), MP4 pin M_i = b_i.
  - L6 primitivity (TEMPLATE-ATTACK 1a, on-page verified, cap-free):
    gcd(kbar_P, nu_P) = 1 with kbar_P = a(al+be).  At entries this is
    equivalent to N1 gcd(a, nu) = 1 (TDUNIFORM 2: al+be is coprime to nu
    by R2) — asserted below.

GATE: book_enum.gate() must PASS (on-axis td=6 record unchanged) before
any off-axis output is produced.
"""
from math import gcd
from fractions import Fraction as Fr
import book_enum as BE

TDMAX = 14


def l6_pole_ok(al, be, a, nu):
    """L6 at a pole: gcd(a(al+be), nu) = 1.  Assert N1-equivalence."""
    ok = gcd(a * (al + be), nu) == 1
    assert ok == (gcd(a, nu) == 1), "L6/N1 equivalence broken (R2 violated?)"
    return ok


def census(tdmax=TDMAX):
    """Off-axis entry census: {(m, td): {'raw': n, 'l6': [entries...]}}.
    Each surviving entry: (al, be, poles) with poles = ((L,a,b,nu), ...)."""
    out = {}
    for td in range(6, tdmax + 1):
        for m in range(2, td // 3 + 1):
            raw, l6 = 0, []
            for al, be, poles in BE.entries(td, m):
                if not any(b >= 2 for (L, a, b, nu) in poles):
                    continue                       # on-axis: already booked
                raw += 1
                if all(l6_pole_ok(al, be, a, nu) for (L, a, b, nu) in poles):
                    l6.append((al, be, poles))
            out[(m, td)] = {'raw': raw, 'l6': l6}
    return out


def mp4_sanity(tdmax=TDMAX):
    """MP4 forcing is arithmetic: at prime Lambda or Lambda == beta all
    tdu_rows have b = 1 (checked for every Lambda <= tdmax - 3)."""
    for L in range(3, tdmax - 2):
        for (al, be), (D, Dg), (P, Pg), nu, _ in BE.tdu_rows(L):
            b = P // al
            if any(L % k == 0 for k in range(2, L)) is False:   # L prime
                assert b == 1, f"MP4 prime pin fails at Lambda={L}"
            if L == be:
                assert b == 1, f"MP4 beta-minimal pin fails at Lambda={L}"


def fmt_entry(al, be, poles):
    return (f"({al},{be})" + "+".join(
        f"L{L}a{a}b{b}n{nu}" for (L, a, b, nu) in poles))


# ---------------------------------------------------- step 3: merge cells
def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def hierarchies(leaves):
    """All rooted merge hierarchies on the given leaf tuple: nested tuples,
    internal nodes = frozensets of >= 2 children (MP1: sum(r-1) = m-1)."""
    leaves = list(leaves)
    if len(leaves) == 1:
        return [leaves[0]]
    # choose the root's r >= 2 child-subtrees = set partition into >= 2
    # blocks, each singleton block a leaf, each larger block a sub-merge
    out = []
    for blocks in BE.set_partitions(leaves):
        if len(blocks) < 2:
            continue
        subs = []
        for blk in blocks:
            if len(blk) == 1:
                subs.append([('leaf', blk[0])])
            else:
                subs.append([h for h in hierarchies(tuple(blk))
                             if h[0] == 'G'])
        combos = [()]
        for s in subs:
            combos = [c + (x,) for c in combos for x in s]
        for c in combos:
            out.append(('G', tuple(sorted(c, key=repr))))
    return out


def merge_cells(bs):
    """All (hierarchy, mu-assignment, emitted-M) cells for pole M-vector bs
    (indexed leaves).  Constraints used (printed tier only):
      St 8.4/8.5: leaf arrival mu | b_i (M non-increasing in divisibility);
      MP6(d)/subadditivity (valid incl. mixed, MP-REVIEW l.120): M_G | sum mu_e;
      inner-merge arrival mu_e | emitted M of the child merge;
      MP2: interior G* emits M >= 2 (root-merge G* = (0,y) cells kept, tagged).
    Returns list of dicts {tree, mus, Ms, classes, root_interior}."""
    leaves = tuple(range(len(bs)))
    cells = []

    def expand(node):
        """Yield (emitted_M, class_list, desc) for a subtree."""
        if node[0] == 'leaf':
            for mu in divisors(bs[node[1]]):
                yield mu, [], f"P{node[1]}mu{mu}"
            return
        _, children = node
        child_opts = [list(expand(ch)) for ch in children]
        combos = [()]
        for co in child_opts:
            combos = [c + (o,) for c in combos for o in co]
        for combo in combos:
            mus = [o[0] for o in combo]          # arriving mu_e at this merge
            klass = 'MIXED' if all(mu >= 2 for mu in mus) else 'MP6'
            inner = [k for o in combo for k in o[1]]
            desc = "(" + ",".join(o[2] for o in combo) + ")"
            for MG in divisors(sum(mus)):        # M_G | sum mu_e
                yield MG, inner + [klass], f"{desc}->M{MG}"

    for tree in set(hierarchies(leaves)):
        if tree[0] != 'G':
            continue
        for MG, classes, desc in expand(tree):
            for root_interior in (True, False):
                if root_interior and MG == 1:
                    continue                     # MP2: trunk M != 1
                cells.append({'desc': desc, 'classes': classes,
                              'M_out': MG, 'interior': root_interior})
    return cells


def merge_census(cen):
    """Per (m,td): classify all merge cells of the L6-surviving entries."""
    out = {}
    for (m, td), d in sorted(cen.items()):
        rows = []
        for al, be, poles in d['l6']:
            bs = [b for (L, a, b, nu) in poles]
            cells = merge_cells(bs)
            nmix = sum(1 for c in cells if 'MIXED' in c['classes'])
            allmp6 = sum(1 for c in cells if 'MIXED' not in c['classes'])
            rows.append({'entry': fmt_entry(al, be, poles), 'bs': bs,
                         'cells': len(cells), 'mixed': nmix, 'mp6': allmp6})
        out[(m, td)] = rows
    return out


def report(cen):
    print("== OFF-AXIS ENTRY CENSUS (td<=%d): raw -> L6 survivors ==" % TDMAX)
    tot_raw = tot_l6 = 0
    for (m, td), d in sorted(cen.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        tot_raw += d['raw']; tot_l6 += len(d['l6'])
        star = ' PRIME-td' if td in (7, 11, 13) else ''
        print(f"m={m} td={td:2d}: raw={d['raw']:3d} l6={len(d['l6']):3d}{star}")
        for al, be, poles in d['l6']:
            ws = [BE.fstr(BE.w0_of(al, be, a, b, nu)) for (L, a, b, nu) in poles]
            Ms = [b for (L, a, b, nu) in poles]
            print(f"    {fmt_entry(al, be, poles)}  M={Ms} w0={ws}")
    print(f"TOTAL raw={tot_raw} l6-surviving={tot_l6}")
    pr = {td: sum(len(d['l6']) for (m, t), d in cen.items() if t == td)
          for td in (7, 11, 13)}
    print(f"PRIME-td L6 survivors: {pr}")
    return pr


if __name__ == '__main__':
    okc, _ = BE.gate()
    assert okc, "ON-AXIS GATE FAIL: aborting off-axis census"
    mp4_sanity()
    print("MP4 sanity (prime/beta-minimal Lambda force b=1): PASS")
    cen = census()
    report(cen)
    print("\n== MERGE-CELL CENSUS (hierarchies x mu x M, printed-tier) ==")
    mc = merge_census(cen)
    tot_mix = tot_mp6 = 0
    for (m, td), rows in sorted(mc.items(), key=lambda kv: (kv[0][1], kv[0][0])):
        for r in rows:
            tot_mix += r['mixed']; tot_mp6 += r['mp6']
            star = ' PRIME-td' if td in (7, 11, 13) else ''
            print(f"m={m} td={td:2d} {r['entry']}: cells={r['cells']} "
                  f"mixed={r['mixed']} mp6-anatomy={r['mp6']}{star}")
    print(f"TOTAL cells: mixed={tot_mix} mp6-anatomy={tot_mp6}")
