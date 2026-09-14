#!/usr/bin/env python3
"""Insert source-row tags before simplify() in a full triangular script."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--meta", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--script", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    meta = json.loads(args.meta.read_text(encoding="utf-8"))
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    source_rows = Path(__file__).resolve().parents[3] / meta["rows_path"]
    row_count = len(source_rows.read_text(encoding="utf-8").splitlines()) - 1
    pivots = {item["row_index"] for item in plan["pivot_order"]}
    residual = [index for index in range(row_count) if index not in pivots]
    # The final raw slot is the Rabinowitsch generator for branch=none.
    raw_labels = [f"source:{index}" for index in residual] + ["rabinowitsch"]
    script = args.script.read_text(encoding="utf-8")
    needle = '"IMAP_APPLIED_OK raw_rows="+string(size(JReduced));\n'
    if script.count(needle) != 1:
        raise ValueError("cannot locate unique post-imap insertion point")
    label_literal = ",".join(raw_labels)
    insertion = needle + "list TAG_LABELS=" + ",".join(f'\"{x}\"' for x in raw_labels) + ";\n"
    insertion += "int TAG_I;\n"
    insertion += (
        'for (TAG_I=1;TAG_I<=size(JReduced);TAG_I++) { '
        'if (JReduced[TAG_I]!=0) { print("TAG__ROW raw="+string(TAG_I-1)'
        '+" label="+string(TAG_LABELS[TAG_I])+" "+string(JReduced[TAG_I])); } }\n'
    )
    insertion += '"TAG__DONE raw_count="+string(size(JReduced));\nexit;\n'
    output_text = script.replace(needle, insertion, 1)
    args.output.write_text(output_text, encoding="utf-8")
    record = {
        "schema": "jc2.s56-recert.tagged-raw-dump/v1",
        "meta_sha256": sha256(args.meta),
        "plan_sha256": sha256(args.plan),
        "input_script_sha256": sha256(args.script),
        "output_script_sha256": sha256(args.output),
        "raw_label_count": len(raw_labels),
        "nonpivot_source_rows": len(residual),
        "rabinowitsch_rows": 1,
        "raw_labels_sha256": hashlib.sha256(label_literal.encode()).hexdigest(),
    }
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
