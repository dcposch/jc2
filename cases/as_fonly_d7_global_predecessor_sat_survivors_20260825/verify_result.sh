#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "$0")/../.." && pwd)
CASE="$ROOT/cases/as_fonly_d7_global_predecessor_sat_survivors_20260825"
cd "$ROOT"

sha256sum -c "$CASE/SOURCE_CLOSURE.sha256"
sha256sum -c "$CASE/RESULT_MANIFEST.sha256"

for result in "$CASE"/aws_results/base_*; do
  (cd "$result" && sha256sum -c OUTPUTS.sha256)
  test "$(cat "$result/VERDICT.txt")" = "SAT-DIRECT-REPLAY-PASS"
  python3 - "$result/direct_replay.json" <<'PY'
import json
import sys

data = json.load(open(sys.argv[1], encoding="utf-8"))
assert data["status"] == "PASS-DIRECT-INTEGER-SOURCE-REPLAY"
assert data["recursive_literal_div243_agreement"] is True
assert data["terminal_nonzero_indices"] == []
for key in ("predecessor_rows", "q9_rows", "q8_rows", "q7_rows"):
    assert not any(data[key]), (key, data[key])
assert not any(value for block in data["top_rows"] for value in block)
PY
done

echo PASS-AS-GLOBAL-PREDECESSOR-SAT-SURVIVORS-FROZEN
