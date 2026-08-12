"""Regression gates for lib/reduce4.py (Phase 2 of SECTION4-AUTOMATION.md).

Gate 2a: the deterministic single-branch path machine-reproduces GGV22
         (arXiv:2204.14178) Props 4.1 (case (9,27)) and 4.4 (case (7,21))
         EXACTLY: the stated N(P), N(Q) corner lists and the bracket RHS,
         from Phase 1 CornerData alone (= cases/emit.py reg_9_27, reg_7_21).
Gate 2b: branch enumeration reproduces Prop 4.2's three subcases and
         Prop 4.3's two subcases exactly (corner lists + RHS x resp. x^2),
         with the branch-kill reasoning recorded in the log.
G2:      the (8,32) family exits with status 'discarded' via R8+R7
         (GGV22 S2's one-paragraph argument), producing no polygons.
G3:      step invariants: rhs == CornerData.rhs_exp, (0,0) in both supports.
Plus:    unit regressions for Algorithm 1 and the R9 divisibility table.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))
from families import section4_families, enumerate_cases, get_pllc, corner_data
from reduce4 import (reduce_family, possible_starting_points, case1_singles,
                     prop312_consistent, tail_resolve, hull)

PLLC = get_pllc(60)


def corners(seq):
    return frozenset(seq)


# ---- cases/emit.py ground truth (GGV22 S4 verbatim) ----------------------
REG_9_27 = (corners([(0, 0), (1, 1), (6, 16), (6, 18), (0, 18)]),
            corners([(0, 0), (1, 0), (9, 24), (9, 27), (0, 27)]), 1)
REG_9_24 = {
    (corners([(0, 0), (1, 1), (6, 16), (6, 18), (0, 12)]),
     corners([(0, 0), (1, 0), (9, 24), (9, 27), (0, 18)]), 1),   # subcase (1)
    (corners([(0, 0), (1, 1), (6, 16), (6, 18), (0, 6)]),
     corners([(0, 0), (1, 0), (9, 24), (9, 27), (0, 9)]), 1),    # subcase (2)
    (corners([(0, 0), (1, 1), (6, 16), (6, 18)]),
     corners([(0, 0), (1, 0), (9, 24), (9, 27)]), 1),            # subcase (3)
}
REG_7_21 = (corners([(0, 0), (4, 0), (6, 2), (0, 14)]),
            corners([(0, 0), (6, 0), (9, 3), (0, 21)]), 1)
OPEN_8_28 = {
    (corners([(0, 0), (1, 0), (8, 14), (8, 16), (0, 8)]),
     corners([(0, 0), (2, 1), (12, 21), (12, 24), (0, 12)]), 2), # subcase (1)
    (corners([(0, 0), (1, 0), (8, 14), (8, 16)]),
     corners([(0, 0), (2, 1), (12, 21), (12, 24)]), 2),          # subcase (2)
}


def emitted_set(res):
    return {(corners(c.NP), corners(c.NQ), c.rhs_exp) for c in res.cases}


def logs_contain(res, *needles):
    for needle in needles:
        assert any(needle in line for line in res.log), \
            f"{res.name}: log line matching {needle!r} not found"


# ---- unit regressions -----------------------------------------------------

def test_algorithm1():
    "GGV22 Algorithm 1 values used in the proofs (hand-checked)"
    assert set(possible_starting_points(8, 3)) == {(2, 0), (3, 1), (4, 1), (6, 2)}
    assert set(possible_starting_points(3, 1)) == {(1, 0)}
    assert set(possible_starting_points(7, 2)) == {(1, 0), (4, 1)}
    assert set(possible_starting_points(6, 2)) == {(2, 0)}
    # Prop 3.12 case-(1) single-root shapes Algorithm 1 misses: 4.3's (3,0)
    assert (3, 0) in case1_singles((7, 2))
    print("Algorithm 1 + case-(1) singles OK")


def test_prop312_filter():
    "the Prop 4.2 kill: three distinct roots are inconsistent (both variants)"
    ok, why = prop312_consistent((6, 0), (24, 9), (1, -2), [3, 3, 3], 0)
    assert not ok
    ok, why = prop312_consistent((12, 3), (24, 9), (1, -2), [3, 3], 3)
    assert not ok
    ok, why = prop312_consistent((6, 0), (24, 9), (1, -2), [6, 3], 0)
    assert ok and "case2 theta=6" in why      # {2,1} keeps a mult-6 factor
    ok, why = prop312_consistent((6, 0), (24, 9), (1, -2), [9], 0)
    assert ok and "case1" in why              # {3} is the single-root case
    print("GGV2 Prop 3.12 filter OK")


def test_r9_tables():
    "Prop 4.1's 13-gcd divisibility table and Prop 4.3's opposite vertex"
    log = []
    ros = tail_resolve((21, 8), (-1, 3), 2, 3, log)
    assert [(r[1], r[2], r[3]) for r in ros] == [((2, 1), (-1, 0), (-3, 8))]
    for a2b2, D, need in [((-2, 0), 16, 13), ((-1, 0), 8, 26), ((2, 1), 5, 13),
                          ((4, 2), 10, 13), ((7, 3), 7, 13), ((10, 4), 4, 13)]:
        assert any(f"(a',b')={a2b2} killed: {D} does not divide {need}" in l
                   for l in log), (a2b2, D, need)
    assert any("(a',b')=(1, 1) killed: on the diagonal" in l for l in log)
    # the survivors (5,2), (13,5) die on the (-3,8) colinearity contradiction
    for W in [(5, 2), (13, 5)]:
        assert any(f"aligned (a',b')={W} passes divisibility" in l for l in log)
        assert any(f"R9 at {W}: " in l and "colinearity contradiction" in l
                   for l in log)
    log2 = []
    ros2 = tail_resolve((24, 7), (-1, 4), 3, 2, log2)
    assert [(r[1], r[2], r[3]) for r in ros2] == [((2, 1), (-1, 0), (-2, 7))]
    assert any("k=2" in l and "not parallel" in l for l in log2)
    print("R9 tail resolution tables OK")


# ---- Gate 2a --------------------------------------------------------------

def test_gate_2a():
    s4 = section4_families()
    r = reduce_family(s4["9_27"], PLLC)
    assert r.status == "reduced" and len(r.cases) == 1, r.status
    assert emitted_set(r) == {REG_9_27}
    c = r.cases[0]
    assert tuple(c.NP) == ((0, 0), (1, 1), (6, 16), (6, 18), (0, 18))
    assert tuple(c.NQ) == ((0, 0), (1, 0), (9, 24), (9, 27), (0, 27))
    assert c.rhs_exp == 1 == s4["9_27"].rhs_exp
    logs_contain(r, "q=9", "en(R) = (3, 1)", "(c,0) candidates [9]",
                 "single root of multiplicity 8", "R9 at (21, 8)",
                 "psi_3 applied")
    r = reduce_family(s4["7_21"], PLLC)
    assert r.status == "reduced" and len(r.cases) == 1
    assert emitted_set(r) == {REG_7_21}
    c = r.cases[0]
    assert tuple(c.NP) == ((0, 0), (4, 0), (6, 2), (0, 14))
    assert tuple(c.NQ) == ((0, 0), (6, 0), (9, 3), (0, 21))
    assert c.rhs_exp == 1
    logs_contain(r, "q=7", "en(R) = (3, 1)", "(c,0) candidates [7]",
                 "direction step (7, 2) is not (K,1)")   # no tail stage (4.4)
    print("Gate 2a OK: Props 4.1 and 4.4 machine-reproduced exactly")


# ---- Gate 2b --------------------------------------------------------------

def test_gate_2b_924():
    s4 = section4_families()
    r = reduce_family(s4["9_24"], PLLC)
    assert r.status == "reduced" and len(r.cases) == 3, (r.status, len(r.cases))
    assert emitted_set(r) == REG_9_24
    # branch-kill ledger (which branches died and by which rule):
    logs_contain(
        r,
        # first-stage predecessor kills (vdE 10.2.6 recursion)
        "st(R)=(3, 1) dir=(2, -5) KILLED by R6",
        "st(R)=(6, 2) dir=(1, -2) KILLED by R6",
        "st(R)=(0,0) dir=(3, -8) KILLED by R6",
        # B1: three-distinct-roots partition killed by GGV2 Prop 3.12
        "shape z^0*[1, 1, 1] KILLED by R4",
        # the zero-root variant of the {2,1} shape dies on the axis check
        "hull corner (3, 0) on the positive x-axis is not an admitted",
        # R9: divisibility table + aligned colinearity contradictions
        "R9 at (21, 8): aligned (a',b')=(5, 2) passes divisibility",
        "colinearity contradiction",
    )
    print("Gate 2b OK: Prop 4.2's three subcases + kill ledger")


def test_gate_2b_828():
    s4 = section4_families()
    r = reduce_family(s4["8_28"], PLLC)
    assert r.status == "reduced" and len(r.cases) == 2, (r.status, len(r.cases))
    assert emitted_set(r) == OPEN_8_28
    assert all(c.rhs_exp == 2 for c in r.cases)          # RHS x^2
    logs_contain(
        r,
        # the two admissible predecessors (GGV6 Prop 2.5's conclusion, here
        # derived via Algorithm 1 + Prop 3.12 case (1) + R6)
        "continuations of en(R)=(7, 2) below (-1, 4): [((1, 0), (1, -3)), "
        "((3, 0), (1, -2))]",
        # R9: k=2 killed by the parallel-edge test; opposite vertex (-2,7)
        "k=2 ends P->(-2, 0) Q->(3, 1) killed: P,Q edges not parallel",
        "R9 at (24, 7): aligned (a',b')=(17, 5) passes divisibility",
        "colinearity contradiction",
    )
    # cases a) and b) of the proof merge into one emitted case
    logs_contain(r, "merged branch")
    print("Gate 2b OK: Prop 4.3's two subcases (rhs x^2) + kill ledger")


# ---- G2 + G3 --------------------------------------------------------------

def test_discard_8_32():
    for ch, fam, j, mn, deg in enumerate_cases(150):
        cd = corner_data(ch, fam, j, name="8_32")
        if (cd.A0.a, cd.A0.b) == (8, 32) and mn == (3, 2):
            r = reduce_family(cd, PLLC)
            assert r.status == "discarded" and not r.cases, r.status
            logs_contain(r, "force d0=4", "(8, 4) the last lower corner",
                         "NOT a possible last lower corner")
            print("G2 OK: (8,32) discarded via R8+R7, no polygons")
            return
    raise AssertionError("(8,32) family not found")


def test_invariants():
    s4 = section4_families()
    for key, cd in s4.items():
        r = reduce_family(cd, PLLC)
        assert r.status == "reduced"
        for c in r.cases:
            assert c.rhs_exp == cd.rhs_exp, (key, "rhs")
            assert (0, 0) in c.NP and (0, 0) in c.NQ, (key, "origin")
            assert all(x >= 0 and y >= 0 for x, y in list(c.NP) + list(c.NQ))
            # N(Q) is the max(m,n)-fold polygon: total degree ratio matches
            assert max(x + y for x, y in c.NQ) > max(x + y for x, y in c.NP)
    print("G3 OK: rhs/orign/quadrant invariants hold on all emitted cases")


# ---- Phase 2c: above-125 families (UNVALIDATED engine data) ---------------

def test_above125_unvalidated():
    """The engine's first genuinely new reductions (maxdeg > 125), banked in
    reduce4.ABOVE125_UNVALIDATED.  These are UNVALIDATED (no literature
    ground truth); the test pins the engine output for reproducibility."""
    from reduce4 import ABOVE125_UNVALIDATED, run_above125
    res = run_above125()
    for key, spec in ABOVE125_UNVALIDATED.items():
        r = res[key]
        assert r.status == "reduced", (key, r.status)
        got = {(corners(c.NP), corners(c.NQ), c.rhs_exp) for c in r.cases}
        want = {(corners(NP), corners(NQ), rhs) for NP, NQ, rhs in spec["cases"]}
        assert got == want, (key, got, want)
    # design S1 farm preview: a (7,35)-type family must give RHS x^3
    from reduce4 import family_case, reduce_family
    from families import get_pllc
    r = reduce_family(family_case(7, 35, (2, 3), 126), get_pllc(90))
    assert r.status == "reduced" and all(c.rhs_exp == 3 for c in r.cases)
    print("Phase 2c OK: above-125 reductions reproduced (UNVALIDATED bank); "
          "(7,35) farm-preview RHS x^3 confirmed")


# ---- Stuck-family closure (2026-08-11): the deg<=150 stuck set -----------

STUCK150 = {
    # name: (ncases, sorted rhs exponents).  rhs 0 = pre-psi direct emission
    # ([P,Q] = const Jacobian-pair system); full corner sets are pinned in
    # systems/farm/<name>/manifest.json (emission inventory).
    "12_36mn23d144_r0": (1, (1,)),
    "12_36mn23d144_r1": (4, (0, 1, 2, 2)),
    "12_36mn23d144_r2": (4, (0, 1, 2, 2)),
    "12_36mn23d144_r3": (3, (0, 1, 2)),
    "6_15mn27d147":     (2, (1, 1)),
    "10_40mn32d150_r0": (8, (0, 0, 0, 2, 2, 3, 3, 3)),
    "10_40mn32d150_r1": (8, (0, 0, 0, 2, 2, 3, 3, 3)),
    "12_33mn23d135":    (10, (0, 0, 0, 0, 0, 1, 1, 1, 1, 2)),
    "8_28mn34d144":     (4, (2, 2, 2, 2)),
}


def test_stuck150_closure():
    """The seven previously-stuck deg<=150 families (+ the two multi-root
    rows 12_33mn23d135 / 8_28mn34d144) now reduce: multi-root chain-edge cut
    (GGV5 Prop 2.5 (multiplicidad) + Prop `multiplicidad`(4)) + no-progress cut guard +
    pre-psi direct-emission fallback."""
    from farm import catalog
    rows = {r.name: r for r in catalog(150)}
    # flagship pins: full corner sets of the two clean multi-root reductions
    r = reduce_family(rows["12_36mn23d144_r0"].cd, PLLC)
    assert emitted_set(r) == {
        (corners([(0, 0), (1, 1), (6, 16), (6, 24), (0, 24)]),
         corners([(0, 0), (1, 0), (9, 24), (9, 36), (0, 36)]), 1)}
    r = reduce_family(rows["6_15mn27d147"].cd, PLLC)
    assert emitted_set(r) == {
        (corners([(0, 0), (1, 1), (6, 8), (6, 12)]),
         corners([(0, 0), (1, 0), (21, 28), (21, 42)]), 1),
        (corners([(0, 0), (1, 1), (6, 8), (6, 12), (0, 6)]),
         corners([(0, 0), (1, 0), (21, 28), (21, 42), (0, 21)]), 1)}
    for name, (nc, rhss) in STUCK150.items():
        r = reduce_family(rows[name].cd, PLLC)
        assert r.status == "reduced", (name, r.status)
        got = (len(r.cases), tuple(sorted(c.rhs_exp for c in r.cases)))
        assert got == (nc, rhss), (name, got)
        for c in r.cases:
            assert (0, 0) in c.NP and (0, 0) in c.NQ, name
            if c.rhs_exp == 0:      # pre-psi: polynomial polygons mandatory
                assert all(x >= 0 and y >= 0
                           for x, y in list(c.NP) + list(c.NQ)), name
    print("Stuck-family closure OK: 9 previously-stuck families reduce, "
          "pins hold (2 flagship corner sets + counts/rhs)")


if __name__ == "__main__":
    test_algorithm1()
    test_prop312_filter()
    test_r9_tables()
    test_gate_2a()
    test_gate_2b_924()
    test_gate_2b_828()
    test_discard_8_32()
    test_invariants()
    test_above125_unvalidated()
    test_stuck150_closure()
    print("ALL REDUCE4 TESTS PASS")


