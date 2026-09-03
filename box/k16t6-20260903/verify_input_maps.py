#!/usr/bin/env python3
"""Mechanical provenance checks for the patched Laurent and exact drivers."""

from pathlib import Path
import difflib
import hashlib
import re


ROOT = Path("/home/ubuntu/jc2")
BOX = ROOT / "box/k16t6-20260903"
FROZEN = Path("/tmp/jc2-lane.Gp5PbG/inputs")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


frozen_model = FROZEN / "terminal_laurent_model.py"
local_model = BOX / "terminal_laurent_model.py"
print("terminal_model_frozen_sha256=" + sha(frozen_model))
print("terminal_model_local_sha256=" + sha(local_model))
diff = list(difflib.unified_diff(
    frozen_model.read_text().splitlines(),
    local_model.read_text().splitlines(), lineterm=""))
changed = [line for line in diff
           if line.startswith(("+", "-"))
           and not line.startswith(("+++", "---"))]
expected = [
    '-OUT = pathlib.Path("/home/ubuntu/jc2/box/k16spine-20260903")',
    '+OUT = pathlib.Path("/home/ubuntu/jc2/box/k16t6-20260903")',
]
assert changed == expected, changed
print("TERMINAL_MODEL_PATH_ONLY_PATCH_PASS")

qhy = FROZEN / "t6_heuristic_exact_QHy_std.sing"
at3 = BOX / "t6_heuristic_exact_At_nfmodStd_3c.sing"


def generators(path: Path) -> list[str]:
    match = re.search(r"ideal I=(.*?);\nideal G=", path.read_text(), re.S)
    assert match
    return [item.strip() for item in match.group(1).split(",\n")]


q_generators = generators(qhy)
a_generators = generators(at3)
assert len(q_generators) == 13 and len(a_generators) == 12
assert q_generators[1:] == a_generators
assert ("minpoly=" + q_generators[0] + ";") in at3.read_text()
print("EXACT_AT_MAP_PASS source_sha256=" + sha(qhy)
      + " rows=12 rows_byte_identical=true minpoly_byte_identical=true")

origin = ROOT / "box/k16t56-20260903/t6_heuristic_exact_At_nfmodStd.sing"
assert at3.read_text() == origin.read_text().replace(
    "setcores(1);", "setcores(3);", 1)
print("EXACT_AT_SETCORES_ONLY_PATCH_PASS origin_sha256=" + sha(origin)
      + " run_sha256=" + sha(at3))

manifest = ROOT / "box/k16spine-20260903/final_manifest.sha256"
expected_reference_hashes = {}
for line in manifest.read_text().splitlines():
    if "terminal_laurent_t" in line and line.endswith(".json"):
        digest, name = line.split(maxsplit=1)
        expected_reference_hashes[Path(name).name] = digest
for t in range(2, 6):
    name = f"terminal_laurent_t{t}.json"
    path = ROOT / "box/k16spine-20260903" / name
    assert name in expected_reference_hashes
    assert sha(path) == expected_reference_hashes[name]
    print(f"LAURENT_REFERENCE_HASH_PASS t={t} sha256={sha(path)}")
