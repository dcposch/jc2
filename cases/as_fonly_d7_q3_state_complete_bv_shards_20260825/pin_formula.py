#!/usr/bin/env python3
"""Pin one accepted first-carry assignment into a monolithic SMT2 formula."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path


formula_path = Path(os.environ["FORMULA_INPUT"])
assignment_path = Path(os.environ["ASSIGNMENTS_JSON"])
branch = int(os.environ["BRANCH_INDEX"])
formula = formula_path.read_text()
data = json.loads(assignment_path.read_text())
assert data["status"] == "PASS-AS-Q3-FIRST-CARRY-27-ASSIGNMENTS"
assert 0 <= branch < len(data["accepted_assignments"]) == 27
assert formula.count("(check-sat)") == 1
names = data["active_variable_names"]
values = data["accepted_assignments"][branch]
assert len(names) == len(values) == 8
pins = "".join(f"(assert (= {name} (_ bv{value} 32)))\n"
               for name, value in zip(names, values))
pinned = formula.replace("(check-sat)", pins + "(check-sat)")
Path(os.environ["SMT2_OUTPUT"]).write_text(pinned)
result = {
    "status": "PASS-AS-Q3-FIRST-CARRY-PIN",
    "formula_sha256": hashlib.sha256(formula.encode()).hexdigest(),
    "assignments_sha256": hashlib.sha256(
        assignment_path.read_bytes()).hexdigest(),
    "branch_index": branch, "variable_names": names, "values": values,
    "pinned_smt2_sha256": hashlib.sha256(pinned.encode()).hexdigest(),
}
encoded = (json.dumps(result, sort_keys=True, separators=(",", ":"))
           + "\n").encode()
Path(os.environ["OUTPUT_JSON"]).write_bytes(encoded)
print("branch", branch, list(zip(names, values)))
print("pinned_smt2_sha256", result["pinned_smt2_sha256"])
print(result["status"])
