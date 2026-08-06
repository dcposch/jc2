"""Regression gates for lib/families.py (Phase 1 of SECTION4-AUTOMATION.md).

Gate A: the enumeration reproduces the 10-case table of arXiv:2204.14178 S2
        (all cases with max(deg P, deg Q) < 125) exactly -- every row present,
        no spurious extras below 125.
Gate B: the four GGV22 S4 families (9,27), (9,24), (8,28), (7,21) carry the
        exact corner data the reductions consume (SECTION4-AUTOMATION.md S2).
Plus:   the GGV5 (arXiv:1708.07936) S5 family tables (F1-F24, corners with
        a+b < 36) and the S6 tables of all 34 cases with maxdeg <= 150.
"""
import sys, os
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from families import (Corner, Edge, get_pllc, get_starting_edges,
                      admissible_complete_chains, chain_path, chain_dirs_pq,
                      get_mn_families, family_members, enumerate_families,
                      case_rows, section4_families, supports, v11)


def geo(x, y):
    "path point: x int or (num, den)"
    return (Fr(*x) if isinstance(x, tuple) else Fr(x), y)


def test_pllc():
    P = get_pllc(25)
    # every (a,0) is a possible last lower corner; b=0 row of Algorithm 1
    assert all((a, 0) in P for a in range(1, 26))
    # (2,1) is not: this is what discards Moh's ((7,21),(2,1)) case (GGV5 S6)
    assert (2, 1) not in P
    # b < a and b <= (a-b-1)^2 hold throughout (GGV2 Prop 3.25)
    assert all(b < a and b <= (a - b - 1) ** 2 for a, b in P)
    # spot checks used by the S4 chains
    assert (1, 0) in P and (2, 0) in P and (6, 2) in P and (9, 4) in P
    assert (6, 3) not in P and (4, 2) not in P
    print("PLLC OK")


def test_qk_machinery():
    """(q_k) regression values from SECTION4-AUTOMATION.md S2 item 4:
    (9,27): q0=9 on the (1,0)-edge [the q=9 certificate GGV22 uses at the
    flipped (-2,1) edge], q1=3 at (3,-1); (9,24): q=3 at (3,-1);
    (8,28): q=4 at (4,-1); (7,21): q=7 at (7,-2)."""
    s4 = section4_families()
    assert s4["9_27"].steps == ((1, 0, 1, 9), (3, -1, 2, 3))
    assert s4["9_24"].steps == ((3, -1, 2, 3),)
    assert s4["8_28"].steps == ((4, -1, 3, 4),)
    assert s4["7_21"].steps == ((7, -2, 5, 7),)
    # en(F) = (p/q) A must be a lattice point of the 1/m polygon
    assert s4["9_24"].steps[0][2:] == (2, 3)   # (2/3)(9,24) = (6,16)
    assert s4["8_28"].steps[0][2:] == (3, 4)   # (3/4)(8,28) = (6,21)
    print("(q_k) machinery OK")


# ---- GGV5 S5: the (m,n)-family tables for corners with a+b < 36 (F1-F24) ---
# rows: edges [((a,l,b),(a',l,b')), ...], final (a,l,b), k -> (m0, n0, d1, d2)
# with members (m0 + j*d1, n0 + j*d2).  All entries as printed in the paper,
# except F6 where the paper prints the non-coprime-base progression
# (3j+4, 8j+10); its coprime members (odd j) are exactly (7+6j, 18+16j),
# which is what GetmnFamilies (and this port) produces -- checked separately.
E1 = lambda A, Ap: ((A, Ap),)
FTABLE = {
    "F1":  (E1((4, 1, 12), (1, 1, 0)), (7, 4, 3), 1, (3, 4, 2, 3)),
    "F2":  (E1((5, 1, 20), (1, 1, 0)), (7, 5, 2), 1, (2, 3, 1, 2)),
    "F3":  (E1((5, 1, 20), (1, 1, 0)), (8, 5, 3), 1, (3, 2, 4, 3)),
    "F4":  (E1((5, 1, 20), (1, 1, 0)), (8, 5, 3), 2, (3, 16, 2, 12)),
    "F5":  (E1((5, 1, 20), (1, 1, 0)), (9, 5, 4), 1, (9, 5, 7, 4)),
    "F6":  (E1((5, 1, 20), (1, 1, 0)), (9, 5, 4), 2, (7, 18, 6, 16)),
    "F7":  (E1((6, 1, 15), (1, 1, 0)), (7, 3, 4), 1, (2, 7, 1, 4)),
    "F8":  (E1((6, 1, 15), (1, 1, 0)), (8, 3, 5), 1, (3, 7, 2, 5)),
    "F9":  (E1((7, 1, 21), (1, 1, 0)), (11, 7, 2), 1, (2, 3, 1, 2)),
    "F10": (E1((7, 1, 21), (1, 1, 0)), (13, 7, 3), 1, (7, 4, 5, 3)),
    "F11": (E1((7, 1, 21), (1, 1, 0)), (13, 7, 3), 2, (2, 5, 1, 3)),
    "F12": (E1((8, 1, 24), (2, 1, 0)), (13, 4, 5), 1, (3, 7, 2, 5)),
    "F13": (E1((9, 1, 21), (2, 1, 0)), (13, 3, 7), 1, (2, 13, 1, 7)),
    "F14": (E1((9, 1, 24), (1, 1, 0)), (7, 3, 4), 1, (2, 7, 1, 4)),
    "F15": (E1((9, 1, 24), (1, 1, 0)), (8, 3, 5), 1, (3, 7, 2, 5)),
    "F16": (E1((9, 1, 24), (1, 1, 0)), (10, 3, 7), 1, (3, 5, 4, 7)),
    "F17": (E1((9, 1, 24), (1, 1, 0)), (11, 3, 8), 1, (2, 3, 5, 8)),
    "F18": ((((6, 1, 18), (6, 1, 15)), ((6, 1, 15), (1, 1, 0))),
            (7, 3, 4), 1, (2, 7, 1, 4)),
    "F19": ((((6, 1, 18), (6, 1, 15)), ((6, 1, 15), (1, 1, 0))),
            (8, 3, 5), 1, (3, 7, 2, 5)),
    "F20": ((((6, 1, 24), (6, 1, 15)), ((6, 1, 15), (1, 1, 0))),
            (7, 3, 4), 1, (2, 7, 1, 4)),
    "F21": ((((6, 1, 24), (6, 1, 15)), ((6, 1, 15), (1, 1, 0))),
            (8, 3, 5), 1, (3, 7, 2, 5)),
    "F22": ((((8, 1, 24), (2, 1, 0)), ((14, 4, 6), (5, 4, 2))),
            (5, 4, 2), 1, (2, 3, 1, 2)),
    "F23": ((((8, 1, 24), (2, 1, 0)), ((14, 4, 6), (11, 4, 4))),
            (11, 4, 4), 1, (2, 7, 1, 4)),
    "F24": ((((8, 1, 24), (2, 1, 0)), ((14, 4, 6), (5, 4, 0))),
            (19, 8, 3), 1, (3, 4, 2, 3)),
}


def test_family_table_a_plus_b_lt_36():
    got = {}
    for ch, fam in enumerate_families(35):
        key = (tuple((tuple(e.A), tuple(e.Ap)) for e in ch.edges),
               tuple(ch.final), fam.k)
        assert key not in got, f"duplicate family {key}"
        got[key] = (fam.m0, fam.n0, fam.d1, fam.d2)
    want = {(edges, fin, k): mn for edges, fin, k, mn in FTABLE.values()}
    assert set(got) == set(want), (
        f"chain/k mismatch:\n missing {sorted(set(want)-set(got), key=str)}"
        f"\n extra {sorted(set(got)-set(want), key=str)}")
    for key in want:
        assert got[key] == want[key], (key, got[key], want[key])
    assert len(got) == 24
    # distinct corners A0 with a+b < 36 carrying families
    corners = {edges[0][0] for edges in (k[0] for k in got)}
    assert corners == {(4, 1, 12), (5, 1, 20), (6, 1, 15), (6, 1, 18),
                       (6, 1, 24), (7, 1, 21), (8, 1, 24), (9, 1, 21),
                       (9, 1, 24)}
    # F6 divergence check: the paper prints (3j+4, 8j+10) whose coprime
    # members (odd j) must equal our family's members exactly
    printed = {(3 * j + 4, 8 * j + 10) for j in range(100)}
    from math import gcd
    printed = {mn for mn in printed if gcd(*mn) == 1}
    ours = {(7 + 6 * j, 18 + 16 * j) for j in range(50)}
    assert printed == ours
    print("GGV5 S5 family table (24 families, 9 corners) OK")


# ---- GGV5 S6: all 34 cases with max(deg P, deg Q) <= 150 ----------------
DEG150 = [
    # 13 rows instantiating S5 families
    ([4, ((7, 4), 3)], (3, 4), 64, 12), ([4, ((7, 4), 3)], (5, 7), 112, 12),
    ([5, ((7, 5), 2)], (2, 3), 75, 20), ([5, ((7, 5), 2)], (3, 5), 125, 20),
    ([5, ((8, 5), 3)], (3, 2), 75, 20),
    ([6, ((7, 3), 4)], (2, 7), 147, 15), ([6, ((8, 3), 5)], (3, 7), 147, 15),
    ([7, ((11, 7), 2)], (2, 3), 84, 21), ([7, ((11, 7), 2)], (3, 5), 140, 21),
    ([7, ((13, 7), 3)], (2, 5), 140, 21),
    ([9, ((11, 3), 8)], (2, 3), 99, 24),
    ([8, ((14, 4), 6), ((5, 4), 2)], (2, 3), 96, 24),
    ([8, ((14, 4), 6), ((19, 8), 3)], (3, 4), 128, 24),
    # 9 further length-1 chains
    ([7, ((19, 7), 5)], (2, 3), 126, 35),
    ([7, ((13, 7), 6)], (3, 2), 147, 42), ([7, ((13, 7), 6)], (2, 3), 147, 42),
    ([8, ((7, 4), 3)], (3, 4), 144, 28), ([8, ((11, 4), 7)], (3, 2), 108, 28),
    ([9, ((17, 9), 4)], (3, 2), 135, 36), ([9, ((17, 9), 4)], (2, 3), 135, 36),
    ([11, ((19, 4), 8)], (2, 3), 132, 33), ([12, ((11, 3), 8)], (2, 3), 135, 33),
    # 11 further length-2 chains
    ([8, 32, 28, ((11, 4), 7)], (3, 2), 120, None),
    ([8, 40, 28, ((11, 4), 7)], (3, 2), 144, None),
    ([9, 27, 24, ((11, 3), 8)], (2, 3), 108, None),
    ([9, 36, 24, ((11, 3), 8)], (2, 3), 135, None),
    ([10, 40, ((16, 5), 6), ((23, 10), 3)], (3, 2), 150, None),
    ([10, 40, ((18, 5), 8), ((8, 5), 3)], (3, 2), 150, None),
    ([12, 30, ((16, 3), 10), ((11, 6), 3)], (3, 2), 126, None),
    ([12, 36, 33, ((11, 3), 8)], (2, 3), 144, None),
    ([12, 36, ((9, 1), 24), ((11, 3), 8)], (2, 3), 144, None),
    ([12, 36, ((21, 4), 9), ((19, 4), 8)], (2, 3), 144, None),
    ([12, 36, ((21, 4), 9), ((12, 4), 5)], (2, 3), 144, None),
    # 1 length-3 chain
    ([12, 36, 30, ((16, 3), 10), ((11, 6), 3)], (3, 2), 144, None),
]


def _decode(spec, b0):
    "table row path: [a0, <b's for same-x integral corners>, (x-frac, b)...]"
    a0 = spec[0]
    path = [geo(a0, b0)] if b0 is not None else None
    if b0 is None:                       # length >= 2 spec: a0, b0, then rest
        path = [geo(a0, spec[1])]
        rest = spec[2:]
    else:
        rest = spec[1:]
    for item in rest:
        if isinstance(item, int):        # same a0, integral corner (a0, item)
            path.append(geo(a0, item))
        else:
            path.append(geo(*item))
    return tuple(path)


def test_deg150_table():
    want = set()
    for spec, mn, deg, b0 in DEG150:
        path = _decode(spec, b0)
        assert int(sum(path[0])) * max(mn) == deg   # maxdeg = max(m,n)*v11(A0)
        want.add((path, mn, deg))
    assert len(want) == 34
    got = case_rows(150)
    assert got == want, (f"deg<=150 mismatch:\n missing "
                         f"{sorted(want-got, key=str)}\n extra "
                         f"{sorted(got-want, key=str)}")
    print("GGV5 S6 tables (34 cases, maxdeg <= 150) OK")


# ---- Gate A: the 10-case table of arXiv:2204.14178 S2 (maxdeg < 125) ----
GATE_A = {
    ((4, 12),  (3, 4), 64),
    ((4, 12),  (5, 7), 112),
    ((5, 20),  (2, 3), 75),
    ((5, 20),  (3, 2), 75),
    ((7, 21),  (2, 3), 84),
    ((8, 24),  (2, 3), 96),
    ((8, 28),  (3, 2), 108),
    ((8, 32),  (3, 2), 120),
    ((9, 24),  (2, 3), 99),
    ((9, 27),  (2, 3), 108),
}


def test_gate_a():
    got = {((int(p[0][0]), p[0][1]), mn, d)
           for p, mn, d in case_rows(150) if d < 125}
    assert got == GATE_A, (f"GATE A FAIL:\n missing {sorted(GATE_A-got)}"
                           f"\n extra {sorted(got-GATE_A)}")
    print("Gate A OK: 10-case table of arXiv:2204.14178 S2 reproduced, "
          "no extras below 125")


# ---- Gate B: S4 corner data per SECTION4-AUTOMATION.md ------------------
GATE_B = {
    "9_27": dict(A0=(9, 1, 27), A0p=(9, 1, 24),
                 edges=(((9, 1, 27), (9, 1, 24)), ((9, 1, 24), (1, 1, 0))),
                 final=(11, 3, 8), steps=((1, 0, 1, 9), (3, -1, 2, 3)),
                 k=1, mn=(2, 3), degs=(72, 108),
                 S=((0, 0), (1, 0), (9, 24), (9, 27), (0, 9)),
                 c=9, upper_dir=(-2, 1), rhs_exp=1),
    "9_24": dict(A0=(9, 1, 24), A0p=(1, 1, 0),
                 edges=(((9, 1, 24), (1, 1, 0)),),
                 final=(11, 3, 8), steps=((3, -1, 2, 3),),
                 k=1, mn=(2, 3), degs=(66, 99),
                 S=((0, 0), (1, 0), (9, 24), (0, 6)),
                 c=6, upper_dir=(-2, 1), rhs_exp=1),
    "8_28": dict(A0=(8, 1, 28), A0p=(1, 1, 0),
                 edges=(((8, 1, 28), (1, 1, 0)),),
                 final=(11, 4, 7), steps=((4, -1, 3, 4),),
                 k=1, mn=(3, 2), degs=(108, 72),
                 S=((0, 0), (1, 0), (8, 28), (0, 4)),
                 c=4, upper_dir=(-3, 1), rhs_exp=2),
    "7_21": dict(A0=(7, 1, 21), A0p=(1, 1, 0),
                 edges=(((7, 1, 21), (1, 1, 0)),),
                 final=(11, 7, 2), steps=((7, -2, 5, 7),),
                 k=1, mn=(2, 3), degs=(56, 84),
                 S=((0, 0), (1, 0), (7, 21), (0, 7)),
                 c=7, upper_dir=(-2, 1), rhs_exp=1),
}


def test_gate_b():
    s4 = section4_families()
    assert set(s4) == set(GATE_B)
    for key, want in GATE_B.items():
        cd = s4[key]
        assert tuple(cd.A0) == want["A0"], (key, "A0")
        assert tuple(cd.A0p) == want["A0p"], (key, "A0p")
        assert tuple((tuple(e.A), tuple(e.Ap)) for e in cd.chain) == want["edges"], (key, "chain")
        assert tuple(cd.final) == want["final"], (key, "final")
        assert cd.steps == want["steps"], (key, "steps", cd.steps)
        assert cd.k == want["k"] and cd.j == 0, (key, "k/j")
        assert cd.mn == want["mn"], (key, "mn")
        assert (cd.degP, cd.degQ) == want["degs"], (key, "degs")
        assert cd.S == want["S"], (key, "S", cd.S)
        assert cd.c == want["c"] and cd.upper_dir == want["upper_dir"], (key, "c")
        assert cd.rhs_exp == want["rhs_exp"], (key, "rhs")
    # supports the reductions consume: SuppP = m*S, SuppQ = n*S
    sp, sq = supports(s4["9_27"])
    assert sp == [(0, 0), (2, 0), (18, 48), (18, 54), (0, 18)]
    assert sq == [(0, 0), (3, 0), (27, 72), (27, 81), (0, 27)]
    sp, sq = supports(s4["8_28"])                    # (deg P, deg Q) = (108,72)
    assert sp == [(0, 0), (3, 0), (24, 84), (0, 12)]
    assert sq == [(0, 0), (2, 0), (16, 56), (0, 8)]
    # RHS law: x^(ceil(b0/a0) - 2), Prop 4.3 gives x^2, the others x
    assert [s4[k].rhs_exp for k in ("9_27", "9_24", "8_28", "7_21")] == [1, 1, 2, 1]
    print("Gate B OK: S4 corner data for (9,27),(9,24),(8,28),(7,21) exact")


def test_starting_edge_guard():
    """The type II.b) (1,0)-direction exclusion (standard pairs, GGV5 proof of
    Thm 2.19): vertical first edges to a PLLC corner must not appear."""
    pllc = get_pllc(25)
    edges = get_starting_edges(9, 27, pllc)
    aps = {tuple(e.Ap) for e in edges}
    assert (9, 1, 24) in aps                    # II.a) vertical edge stays
    assert (9, 1, 0) not in aps and (9, 1, 3) not in aps
    edges = get_starting_edges(6, 18, pllc)
    aps = {tuple(e.Ap) for e in edges}
    assert (6, 1, 15) in aps and (6, 1, 0) not in aps
    print("II.b) (1,0)-guard OK")


if __name__ == "__main__":
    test_pllc()
    test_starting_edge_guard()
    test_qk_machinery()
    test_family_table_a_plus_b_lt_36()
    test_deg150_table()
    test_gate_a()
    test_gate_b()
    print("ALL FAMILIES TESTS PASS")
