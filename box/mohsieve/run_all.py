#!/usr/bin/env python3
"""Exact replay entry: enumerate once, then sieve + descent + tests.

    python3 box/mohsieve/run_all.py
    python3 -O box/mohsieve/run_all.py
"""
from __future__ import annotations

import os
import sys
import time

_HERE = os.path.dirname(os.path.abspath(__file__))
_BOX = os.path.dirname(_HERE)
_ROOT = os.path.dirname(_BOX)
# Drop the script directory so `mohsieve` is the package under box/, not this file.
sys.path[:] = [p for p in sys.path
               if os.path.abspath(p) != os.path.abspath(_HERE)]
if _BOX not in sys.path:
    sys.path.insert(0, _BOX)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
os.chdir(_ROOT)

from mohsieve import mohsieve as SV  # noqa: E402
from mohsieve import descent as DS  # noqa: E402
from mohsieve import test_gates as TG  # noqa: E402
from mohsieve.gates import reset, fail_closed, FAILURES  # noqa: E402


def main():
    t0 = time.time()
    reset()
    print("box/mohsieve/run_all.py")
    print("cwd=%s" % os.getcwd())
    print("python=%s" % sys.version.replace("\n", " "))
    print("optimize=%s (python3 -O => 1)" % sys.flags.optimize)

    print("\n== enumerate n<=100 ==")
    t1 = time.time()
    rows100 = SV.census_moh_space()
    print("   %d rows  [%.2fs]" % (len(rows100), time.time() - t1))
    print("== enumerate 48<=D<=200 ==")
    t1 = time.time()
    rows200 = SV.census_campaign(48, 200, 16)
    print("   %d V-assignments  [%.2fs]" % (len(rows200), time.time() - t1))
    rows120 = [r for r in rows200 if r.n <= 120]

    # --- sieve gates + leaderboard (reuse cache; do not re-enumerate) ---
    print("\n######## SIEVE ########")
    SV.run_g1_g3_controls(rows100, rows120, rows200)
    print("\n== SOLO kill counts ==")
    for rec in SV.solo_kills(rows100, rows120, rows200):
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
    print("\n== G2 on charged stacks ==")
    SV.run_g2_on_named(rows100, ["MOH-INCREMENT", "NOT-ALL-11", "MAJOR-MULT"])
    SV.run_g2_on_named(rows100, ["M2-ABOVE-M"])

    cells = SV.two_by_two(rows100)
    print("\n== M2-ABOVE-M vs MAJOR-MULT 2x2 (n<=100) ==")
    print("            MAJOR-MULT=1   MAJOR-MULT=0")
    print("  M2>m =1   %12d   %12d" % (cells[(1, 1)], cells[(1, 0)]))
    print("  M2>m =0   %12d   %12d" % (cells[(0, 1)], cells[(0, 0)]))
    print("  M2-ABOVE-M => MAJOR-MULT? %s" % (cells[(1, 0)] == 0))
    print("  MAJOR-MULT => M2-ABOVE-M? %s" % (cells[(0, 1)] == 0))

    passing, combos = SV.combo_names()
    print("\n== LEADERBOARD (G1-passing: %s) ==" % passing)
    board = []
    for names, label in combos:
        row = SV.leaderboard_row(rows100, rows200, label, names)
        board.append(row)
        SV.print_lb(row)

    print("\n######## DESCENT ########")
    DS.p207_check()
    DS.gpt55_signatures()
    DS.g7_on_us1_moh()
    trio = DS.trio_descent()
    sink = os.path.join(_HERE, "descent_terminal.txt")
    table = DS.campaign_table_from_rows(rows200, sink=sink)

    print("\n######## UNIT TESTS (reuse cache) ########")
    # test_gates.main would re-enumerate; call the pieces.
    TG.test_assert_scan()
    TG.test_g1()
    TG.test_g2(rows100)
    TG.test_opus_cascade(rows100)
    TG.test_g3(rows100, rows120, rows200)
    TG.test_g4(rows200)
    TG.test_g5(rows200)
    # G6–G8 already run above.

    print("\n######## D=105 trio through SIEVE ########")
    specs = [
        ("G1", 105, 70, (28, 103), {2: 1, 3: 5}),
        ("G2", 105, 70, (28, 103), {2: 1, 3: 6}),
        ("G3", 105, 70, (40, 103), {2: 1, 3: 4}),
    ]
    for lab, n, m, Ms, V in specs:
        hits = [r for r in rows200
                if r.n == n and r.m == m and r.Ms == Ms and r.S.V[3] == V[3]]
        if not hits:
            print("   %s NOT IN CENSUS" % lab)
            continue
        r = hits[0]
        flags = []
        for p in SV.DEFINED:
            flags.append("%s=%s" % (p.name, bool(r.mask & SV.combo_mask([p.name]))))
        print("   %s mask: %s" % (lab, " ".join(flags)))

    wall = time.time() - t0
    print("\nwall run_all %.1fs  optimize=%s  failures=%s"
          % (wall, sys.flags.optimize, FAILURES))
    fail_closed()
    print("ALL GREEN.")
    return dict(board=board, cells=cells, trio=trio, table=table, wall=wall)


if __name__ == "__main__":
    main()
