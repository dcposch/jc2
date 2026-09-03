#!/usr/bin/env python3
"""Gate-local checks for the K=16, t=5 replay artifacts."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path("box/k16t5gate-20260903")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def contains(path: Path, *needles: str) -> None:
    text = path.read_text(encoding="utf-8")
    for needle in needles:
        require(needle in text, f"{path}: missing {needle}")


def main() -> None:
    audit = json.loads((ROOT / "t5_heuristic_audit.json").read_text())
    require(audit["t"] == 5, "wrong t")
    require(audit["tuple"] == [64, 44, 61, 3], "wrong tuple")
    require(audit["phi"] == [-1, "5/16"], "wrong Phi")
    require(audit["chart"]["unknowns_including_c"] == 54, "wrong unknown count")
    require(audit["chart"]["equations"] == 79, "wrong equation count")

    q = audit["q_pivots"]
    require(q["count"] == 19 and q["expected"] == 19, "wrong Q-pivot count")
    require(q["all_Qstar"] is True, "non-Qstar Q pivot")
    require(q["highest"] == 21 and q["lowest"] == 10, "wrong Q-pivot bands")
    require(q["residual_unknowns_including_c"] == 35, "wrong residual count")
    require(q["coefficients"] == [
        "11", "11", "11", "11", "11",
        "22", "11", "22", "11", "22", "11", "22", "11",
        "22", "11", "22", "11", "-44", "-33/4",
    ], "wrong Q-pivot coefficients")

    norm = audit["normalizer"]
    require(norm["H_primitive"] == "242*q11_1**2 - 132*q11_1 + 17", "wrong H5")
    require(norm["irreducible_over_Q"] is True, "H5 reducible")
    require(norm["square_free_part_of_3_t_plus_1"] == 2, "wrong field squarefree part")
    require(norm["cbar"] == "40*q11_1*(6 - 66*q11_1)/3993", "wrong cbar")

    grading = audit["grading"]
    require(grading["positive"] is True, "nonpositive grading")
    require((grading["x"], grading["wt_x"]) == ("q6_1", 21), "wrong x grading")
    require((grading["y"], grading["wt_y"]) == ("q11_1", 42), "wrong y grading")
    require(grading["wt_c"] == 105, "wrong c grading")

    require(audit["slice"]["q_rows_after_dedup"] == 48, "wrong sliced rows")
    require(len(audit["slice"]["q_duplicates"]) == 10, "wrong duplicate count")
    require(len(audit["slice"]["auxiliaries"]) == 32, "wrong auxiliary count")

    ap = audit["a_pivots"]
    require(ap["order"] == "heuristic", "wrong A-pivot order")
    require(ap["count"] == 27, "wrong A-pivot count")
    require(ap["every_resultant_nonzero"] is True, "zero A-pivot resultant")
    require(ap["terminal_unit"] is None, "unexpected terminal unit before Singular")
    for pivot in ap["pivots"]:
        require(str(pivot["resultant"]) != "0", "zero resultant in pivot list")

    pattern = audit["terminal"]["pattern"]
    require(pattern["matches_2t_by_t"] is True, "terminal is not 10x5")
    require(pattern["terminal_rows"] == 10, "wrong terminal rows")
    require(pattern["terminal_vars"] == 5, "wrong terminal variable count")
    require(pattern["bands"] == list(range(10)), "wrong terminal bands")
    require(pattern["degrees"] == list(range(21, 11, -1)), "wrong degrees")
    require(pattern["all_tags_0_1"] is True, "wrong terminal tags")
    require(
        audit["terminal"]["variables"] == ["q6_0", "q7_1", "q8_1", "q9_1", "q10_1"],
        "wrong terminal variables",
    )

    with (ROOT / "t5_Q_pivots.tsv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    require(len(rows) == 19, "Q TSV row count mismatch")
    require([row["coefficient"] for row in rows] == q["coefficients"], "Q TSV coeff mismatch")

    with (ROOT / "t5_heuristic_A_pivots.tsv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    require(len(rows) == 27, "A TSV row count mismatch")
    require(all(row["resultant"] != "0" for row in rows), "A TSV zero resultant")

    contains(
        ROOT / "t5_heuristic_exact_At_nfmodStd.out",
        "CONTROL_C_UNIT_PASS",
        "CONTROL_RK_RING_PASS",
        "MAIN_EXACT_UNIT",
        "G[1]=1",
    )
    contains(
        ROOT / "t5_heuristic_exact_At_nfmodStd_reverse_vars.out",
        "CONTROL_C_UNIT_PASS",
        "MAIN_EXACT_UNIT",
        "G[1]=1",
    )
    for prime in (32003, 32009, 32027):
        contains(
            ROOT / f"t5_heuristic_mod_p{prime}_std.out",
            "CONTROL_RING_PASS R",
            "CONTROL_R_EMPTY_PASS",
            "CONTROL_R_NONEMPTY_PASS",
            "MAIN_SATURATED_EMPTY",
            "G[1]=1",
        )

    print("T5_GATE_AUDIT_PASS")
    print("chart=54/79 q_pivots=19 A_pivots=27 terminal=10x5")
    print("H5=242*q11_1^2-132*q11_1+17 irreducible cbar_unit_checked")
    print("exact_nfmodStd=[1] reverse_var_nfmodStd=[1] modular_32003_32009_32027=[1]")


if __name__ == "__main__":
    main()
