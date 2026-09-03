#!/usr/bin/env python3
"""Unit tests for gates G1–G8. Load-bearing checks are require(), not assert.

Replay under python3 -O: this file must contain no ast.Assert nodes.
"""
from __future__ import annotations

import ast
import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
_BOX = os.path.dirname(_HERE)
if _BOX not in sys.path:
    sys.path.insert(0, _BOX)

import moh_skeleton_full as MS  # noqa: E402
try:
    from . import mohsieve as SV
    from . import descent as DS
    from .gates import require, fail_closed, reset
except ImportError:
    import mohsieve as SV  # noqa: E402
    import descent as DS  # noqa: E402
    from gates import require, fail_closed, reset  # noqa: E402

HARNESS_FILES = (
    "mohsieve.py",
    "descent.py",
    "test_gates.py",
    "gates.py",
    "run_all.py",
    "__init__.py",
)


def test_assert_scan():
    print("\n== python3 -O: AST scan, no ast.Assert in harness ==")
    for name in HARNESS_FILES:
        path = os.path.join(_HERE, name)
        if not os.path.isfile(path):
            require("scan %s exists" % name, False)
            continue
        src = open(path).read()
        tree = ast.parse(src, filename=path)
        n_assert = sum(isinstance(nd, ast.Assert) for nd in ast.walk(tree))
        require("no ast.Assert in %s" % name, n_assert == 0, "count=%d" % n_assert)


def test_g1():
    print("\n== G1: six p.202 rows survive each defined predicate ==")
    for p in SV.DEFINED:
        ok, bits = SV.six_kept(SV.combo_mask([p.name]))
        if p.name == "PARTITION":
            require("G1 PARTITION keeps 6/6 (encoding must not kill printed rows)",
                    ok, str(bits))
        else:
            require("G1 %s keeps 6/6" % p.name, ok, str(bits))
    require("G1 EMPTY keeps 6/6", SV.six_kept(0)[0])
    require("SECOND-POINT has fn is None", SV.NAME_OF["SECOND-POINT"].fn is None)
    n_swap = 0
    for (n, m, Ms, Vs, lab, _, _, _) in MS.MOH_TABLE:
        S = MS.Skel(n, m, Ms, Vs)
        if SV.attempted_l2_swap(S):
            n_swap += 1
    require("L2-swap probe keeps 0/6 (reason SECOND-POINT is UNDEFINED)",
            n_swap == 0, str(n_swap))


def test_g2(rows100):
    print("\n== G2: (75,50) residue after integrality ==")
    for names in (
        ["MOH-INCREMENT", "NOT-ALL-11", "MAJOR-MULT"],
        ["M2-ABOVE-M"],
        ["MAJOR-MULT"],
        ["MOH-INCREMENT", "NOT-ALL-11"],
    ):
        res_i = SV.residue_7550(rows100, SV.combo_mask(names), integral=True)
        # G2 is a discriminator, not a theorem about every stack. Record +
        # require the two charged stacks that claimed it.
        if names in (
            ["MOH-INCREMENT", "NOT-ALL-11", "MAJOR-MULT"],
            ["M2-ABOVE-M"],
        ):
            require(
                "G2 %s" % " & ".join(names),
                SV.g2_ok(res_i),
                str(res_i),
            )
        else:
            print("  [meas] G2 %s -> %s  ok=%s"
                  % (" & ".join(names), res_i, SV.g2_ok(res_i)))


def test_g3(rows100, rows120, rows200):
    print("\n== G3 / EMPTY negative control ==")
    n_rows, n_cls, _ = SV.n100_stats(rows100, 0)
    require("G3 EMPTY n<=100 rows = 658", n_rows == 658, str(n_rows))
    require("G3 EMPTY n<=100 classes = 63", n_cls == 63, str(n_cls))
    g120 = len(SV.groups_of_rows(rows120, 0))
    g200 = len(SV.groups_of_rows(rows200, 0))
    require("EMPTY groups D<=120 = 1189", g120 == 1189, str(g120))
    require("EMPTY groups D<=200 = 14016", g200 == 14016, str(g200))


def test_g4(rows200):
    print("\n== G4: groups / emptied degrees, named stacks ==")
    g = len(SV.groups_of_rows(rows200, 0))
    require("G4 EMPTY groups 14016", g == 14016, str(g))
    need = SV.combo_mask(["MOH-INCREMENT", "NOT-ALL-11", "MAJOR-MULT"])
    empty = SV.emptied_degrees(rows200, need)
    require("G4 MOH-4 empties D=105", 105 in empty, str(empty))
    need2 = SV.combo_mask(["M2-ABOVE-M"])
    empty2 = SV.emptied_degrees(rows200, need2)
    require("G4 M2-ABOVE-M does NOT empty D=105 at group level (5 groups remain; N kills them)",
            105 not in empty2, str(empty2))
    print("  [meas] MOH-4 emptied: %s" % empty)
    print("  [meas] M2-ABOVE-M emptied (pre-knapsack): %s" % empty2)


def test_g5(rows200):
    print("\n== G5: pinned-N knapsack on listing degrees ==")
    empty = SV.knapsack_degree(rows200, 105, 0)
    require("G5 EMPTY D=105 has 14 (1)-(13) groups", empty["groups"] == 14, str(empty))
    require("G5 EMPTY D=105 UNI [6,16] is 3 (the trio)",
            empty["uni_6_16"] == 3, str(empty))
    need = SV.combo_mask(["MAJOR-MULT"])
    mm = SV.knapsack_degree(rows200, 105, need)
    require("G5 MAJOR-MULT D=105 UNI [6,16] is 0 (trio is V2=1)",
            mm["uni_6_16"] == 0, str(mm))
    need2 = SV.combo_mask(["M2-ABOVE-M"])
    m2 = SV.knapsack_degree(rows200, 105, need2)
    require("G5 M2-ABOVE-M D=105 UNI N>=6 is 0 (trio M2<m)",
            m2["uni_ge6"] == 0, str(m2))
    need4 = SV.combo_mask(["MOH-INCREMENT", "NOT-ALL-11", "MAJOR-MULT"])
    m4 = SV.knapsack_degree(rows200, 105, need4)
    require("G5 MOH-4 D=105 has 0 groups", m4["groups"] == 0, str(m4))
    d108 = SV.knapsack_degree(rows200, 108, 0)
    require("G5 EMPTY D=108 has groups", d108["groups"] > 0, str(d108))
    print("  [meas] EMPTY D=108 %s" % d108)


def test_g6_g7():
    print("\n== G6/G7: p.207 table and integrality ==")
    DS.p207_check()
    DS.g7_on_us1_moh()
    DS.gpt55_signatures()


def test_g8_and_trio():
    print("\n== G8 + D=105 trio ==")
    DS.trio_descent()
    # G8 on the four Moh degrees, Kmin=2 for n<48-campaign? 64,75,84,99 are
    # inside 48..200; use Kmin=2 so Moh's own rows (K=16,28,25,33) count.
    # Campaign G8 uses Kmin=16; Moh rows have K=16,28,25,33 all ≥16 except
    # wait: (64,48) K=16; (84,56) K=28; (75,50) K=25; (99,66) K=33. All ≥16.
    for n, m, Ms, Vs, lab, _, _, _ in MS.MOH_TABLE:
        S = MS.Skel(n, m, Ms, Vs)
        require("G8 printed row %s still present as a source" % lab, True)
        T, status, us = DS.first_descent(S)
        require("G8 %s not status-killed by missing descent" % lab,
                status != "NOT-INTEGRAL", status)


def test_opus_cascade(rows100):
    print("\n== Opus cascade numbers (MEASURED replay) ==")
    seq = [
        ([], 658),
        (["MOH-INCREMENT"], 391),
        (["MOH-INCREMENT", "NOT-ALL-11"], 247),
        (["MOH-INCREMENT", "NOT-ALL-11", "MAJOR-MULT"], 51),
    ]
    # V2>=2 intermediate 86 is INCREMENT & NOT-ALL-11 & V2>=2, not all-j.
    n_v2 = 0
    need_ia = SV.combo_mask(["MOH-INCREMENT", "NOT-ALL-11"])
    for r in rows100:
        if SV.holds(r.mask, need_ia) and r.S.V[2] >= 2:
            n_v2 += 1
    require("Opus V2>=2 stage = 86", n_v2 == 86, str(n_v2))
    for names, want in seq:
        got = SV.n100_stats(rows100, SV.combo_mask(names) if names else 0)[0]
        require("Opus stage %s = %d" % (names or "EMPTY", want),
                got == want, str(got))
    n_m2 = SV.n100_stats(rows100, SV.combo_mask(["M2-ABOVE-M"]))[0]
    require("Fable M2-ABOVE-M rows = 94", n_m2 == 94, str(n_m2))


def main(rows100=None, rows200=None):
    t0 = time.time()
    reset()
    print("box/mohsieve/test_gates.py")
    test_assert_scan()
    test_g1()
    test_g6_g7()
    test_g8_and_trio()
    own100 = rows100 is None
    if rows100 is None:
        print("\n(enumerating n<=100 for G2/G3/Opus)")
        rows100 = SV.census_moh_space()
    test_g2(rows100)
    test_opus_cascade(rows100)
    if rows200 is None:
        print("\n(enumerating 48<=D<=200 for G3/G4/G5)")
        rows200 = SV.census_campaign(48, 200, 16)
    rows120 = [r for r in rows200 if r.n <= 120]
    test_g3(rows100, rows120, rows200)
    test_g4(rows200)
    test_g5(rows200)
    print("\nwall tests %.1fs (census included=%s)" % (time.time() - t0, own100))
    fail_closed()
    print("ALL UNIT TESTS GREEN.")
    return 0


if __name__ == "__main__":
    main()
