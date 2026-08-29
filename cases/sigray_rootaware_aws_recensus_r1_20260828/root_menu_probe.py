#!/usr/bin/env python3
"""Exact raised root-menu/parity diagnostic; no completeness claim."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import twopole_check as tp

rows = list(tp.root_pattern_menu(1, 1, kmax=8, lmax=128))
assert len(rows) == 9 * 129
assert any(r == (0, 1, 2, 3, "ROOT_ODE_EXACT_SOLVABLE_L1") for r in rows)
for k, ell, dp, dq, status in rows:
    assert dp == 2 + k and dq == k + 2 + ell
    if k == 0 and ell >= 1:
        expected = ("ROOT_ODE_LOG_DEAD_EVEN" if ell % 2 == 0 else
                    "ROOT_ODE_EXACT_SOLVABLE_L1" if ell == 1 else
                    "ROOT_ODE_NO_LOG_OBSTRUCTION_ODD")
        assert status == expected
summary = {
    "rows": len(rows),
    "lmax": 128,
    "exact_l1": sum(r[4] == "ROOT_ODE_EXACT_SOLVABLE_L1" for r in rows),
    "even_log_dead": sum(r[4] == "ROOT_ODE_LOG_DEAD_EVEN" for r in rows),
    "odd_no_log_obstruction": sum(r[4] == "ROOT_ODE_NO_LOG_OBSTRUCTION_ODD" for r in rows),
    "unchecked": sum(r[4] == "ROOT_ODE_UNCHECKED" for r in rows),
    "scope": "EXACT MENU/PARITY CENSUS ONLY; NO GLOBAL SOLVABILITY OR CAP CLAIM",
}
print(json.dumps(summary, indent=2, sort_keys=True))
print("ROOT_MENU_L128_EXACT_DIAGNOSTIC_PASS")

