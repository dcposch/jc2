#!/usr/bin/env python3
import importlib.util
import json
import os
import sys
from pathlib import Path

scratch = Path(os.environ.get("JC2_SCRATCH", "/home/ubuntu/classA-smallest-20260906.xpXroy"))
source = scratch / "repo/box/lambda-lowweight-20260906/roster_rows.py"
spec = importlib.util.spec_from_file_location("classa_roster_rows", source)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
rows = [json.loads(line) for line in (scratch / "inputs/roster.jsonl").read_text().splitlines()]
row = next(item for item in rows if item["row_id"] == "R005")
result = module.build(row)
src = Path(result["rows_path"])
dst = scratch / "data/R005_rows.tsv"
src.replace(dst)
result["rows_path"] = str(dst)
(scratch / "results/build_result.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"status": "BUILD_COMPLETE", "rows_path": str(dst), "rows_bytes": dst.stat().st_size,
                  "rows_sha256": result["rows_sha256"], "coefficient_rows": result["coefficient_rows"],
                  "coordinate_sha256": result["coefficient_coordinate_sha256"]}, sort_keys=True), flush=True)
