#!/usr/bin/env python3
"""Positive/negative controls for audit_triangular_quotient.py."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import tempfile

import audit_triangular_quotient as audit_module


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
META = ROOT / "box/s56-recert-20260905/source-complete/meta/S5_n9_m6_M2_V1_k8_part_2_source_complete.json"
PLAN = HERE / "S5_part2.plan.json"
SCRIPT = HERE / "S5_part2_p32003_reduced_dump.sing"
DUMP = HERE / "S5_part2_p32003_reduced_dump.out"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def arguments(script: Path = SCRIPT, dump: Path | None = None, characteristic: int = 32003):
    return argparse.Namespace(
        meta=META,
        plan=PLAN,
        script=script,
        characteristic=characteristic,
        dump=dump,
        output=Path("unused"),
    )


def expect_failure(label: str, args, wanted: str) -> dict:
    try:
        audit_module.audit(args)
    except Exception as exc:
        message = str(exc)
        if wanted not in message:
            raise AssertionError(f"{label}: wrong failure {message!r}; wanted {wanted!r}") from exc
        return {"label": label, "status": "PASS", "observed_failure": message}
    raise AssertionError(f"{label}: mutation incorrectly passed")


def main() -> None:
    positive_static = audit_module.audit(arguments())
    positive_dump = audit_module.audit(arguments(dump=DUMP))
    controls = []
    controls.append(
        expect_failure("wrong_characteristic", arguments(characteristic=32009), "differs from script")
    )
    script_text = SCRIPT.read_text(encoding="utf-8", errors="strict")
    dump_text = DUMP.read_text(encoding="utf-8", errors="strict")
    with tempfile.TemporaryDirectory(prefix="s56-quotient-audit-") as temporary:
        temporary_path = Path(temporary)

        unknown_drop = temporary_path / "unknown_drop.sing"
        unknown_drop.write_text(
            script_text.replace(
                "ring Reduced=32003,(A1_0_0,", "ring Reduced=32003,(", 1
            ),
            encoding="utf-8",
        )
        controls.append(
            expect_failure(
                "unexplained_unknown_drop", arguments(script=unknown_drop), "Reduced ring variables differ"
            )
        )

        row_inventory = temporary_path / "row_inventory.sing"
        row_inventory.write_text(
            script_text.replace("ideal JOld=", "ideal JOld=0,\n", 1), encoding="utf-8"
        )
        controls.append(
            expect_failure(
                "changed_nonpivot_row_inventory", arguments(script=row_inventory), "JOld is not exactly"
            )
        )

        corrupt_replacement = temporary_path / "corrupt_replacement.sing"
        corrupted, count = re.subn(
            r"^poly REP_000=.*;$", "poly REP_000=0;", script_text, count=1, flags=re.MULTILINE
        )
        if count != 1:
            raise AssertionError("could not construct replacement negative control")
        corrupt_replacement.write_text(corrupted, encoding="utf-8")
        controls.append(
            expect_failure(
                "corrupt_pivot_replacement",
                arguments(script=corrupt_replacement),
                "pivot proof instruction at step 0",
            )
        )

        truncated_dump = temporary_path / "truncated.out"
        truncated_dump.write_text(
            dump_text.replace("SCRIPT_DONE\n", "", 1), encoding="utf-8"
        )
        controls.append(
            expect_failure(
                "truncated_dump", arguments(dump=truncated_dump), "unique SCRIPT_DONE"
            )
        )

        reordered_dump = temporary_path / "reordered.out"
        first = "PIVOT_OK step=0 variable=A1_1_2"
        second = "PIVOT_OK step=1 variable=A1_4_2"
        reordered = dump_text.replace(first, "__FIRST__", 1).replace(second, first, 1).replace(
            "__FIRST__", second, 1
        )
        reordered_dump.write_text(reordered, encoding="utf-8")
        controls.append(
            expect_failure(
                "reordered_runtime_pivots",
                arguments(dump=reordered_dump),
                "runtime PIVOT_OK sequence",
            )
        )

    record = {
        "schema": "jc2.s56-recert.independent-triangular-audit-controls/v1",
        "status": "PASS",
        "positive_controls": {
            "static": positive_static["status"],
            "runtime_dump": positive_dump["status"],
        },
        "negative_controls": controls,
        "custody": {
            "audit_script": str((HERE / "audit_triangular_quotient.py").relative_to(ROOT)),
            "audit_script_sha256": sha256(HERE / "audit_triangular_quotient.py"),
            "meta_sha256": sha256(META),
            "plan_sha256": sha256(PLAN),
            "script_sha256": sha256(SCRIPT),
            "dump_sha256": sha256(DUMP),
        },
    }
    output = HERE / "audit-negative-controls.json"
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
