#!/usr/bin/env python3
"""Read-only replay check for the current parameterized emitter.

The builders were emitted before process-affinity/resource monitoring was
added to the driver.  Preserve their historical metadata hashes, but prove
that the current emitter still renders the exact same algebra byte-for-byte.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
EMITTER = HERE / "s56_emitter.py"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


spec = importlib.util.spec_from_file_location("s56_emitter_replay", EMITTER)
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

checks = []
for name, part in module.TARGETS:
    meta_path = HERE / "source-complete" / "meta" / f"{module.stem_for(name, part, 'source-complete')}.json"
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    rows_path = ROOT / payload["rows_path"]
    builder_path = ROOT / payload["builder"]
    rendered = module.ob.native_builder_text(module.build_spec(module.ROWS[name], part, "source-complete"), rows_path)
    actual = builder_path.read_text(encoding="utf-8")
    check = {
        "row": name,
        "partition": list(part),
        "current_render_matches_builder_bytes": rendered == actual,
        "builder_sha256": sha256(builder_path),
        "metadata_builder_sha256": payload["builder_sha256"],
        "historical_emitter_sha256": payload["emitter_sha256"],
    }
    assert check["current_render_matches_builder_bytes"]
    assert check["builder_sha256"] == check["metadata_builder_sha256"]
    checks.append(check)

record = {
    "schema": "jc2.s56-recert.emitter-replay-check/v1",
    "status": "PASS",
    "current_emitter": str(EMITTER.relative_to(ROOT)),
    "current_emitter_sha256": sha256(EMITTER),
    "note": "historical metadata retained so downstream plan/run hashes remain immutable",
    "checks": checks,
}
output = HERE / "emitter-replay-check.json"
output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(record, indent=2, sort_keys=True))
