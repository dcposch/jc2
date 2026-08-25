#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "$0")/../.." && pwd)
CASE="$ROOT/cases/as_fonly_d7_sat_survivor_q6_high_20260825"
cd "$ROOT"
sha256sum -c "$CASE/SOURCE_CLOSURE.sha256"
sha256sum -c "$CASE/RESULT_MANIFEST.sha256"

python3 - "$CASE" <<'PY'
import json
import pathlib
import sys

case = pathlib.Path(sys.argv[1])
expected = {
    "0303_0102020": [0, 0, 0, 0, 0, 0, 0, 0, 2],
    "0513_0201000": [0, 0, 0, 0, 0, 0, 0, 0, 2],
    "0519_0201020": [0] * 9,
}
for name, row in expected.items():
    data = json.loads((case / "aws_results" / f"final_g8_{name}"
                       / "result.json").read_text())
    assert data["status"] == "PASS-FINAL-G8-SOURCE-AUDIT"
    assert data["final_reimposed_G8_rows"] == row
    assert data["final_G7_rows"] == [0] * 8
    assert data["terminal_R12_to_R9"] == [0] * 46

data = json.loads((case / "aws_results" / "q6_high_0519_0201020_v2"
                   / "result.json").read_text())
assert data["status"] == "PASS-Q6-HIGH-AFFINE-GATE"
assert data["equation_shape"] == [70, 16]
assert data["rank_pair"] == [16, 17]
assert data["compatible"] is False
assert data["left_null_active_rows"] == {
    "Q6:x^4y^2": 2,
    "Q6:x^5y^1": 2,
    "R9:x^7y^2": 1,
}
assert data["left_null_rhs_pairing"] == 2
assert data["matrix_sha256"] == "20d945bef43b865be1ccb2b3592af6e82a14e9f3cea4e5029c22bddacb29ccf0"
assert data["rhs_sha256"] == "779b2d4f5c575159ac17500a4792ea9f5aad6b52415f99680153f19309e9f0b0"
PY

echo PASS-AS-SAT-SURVIVOR-Q6-HIGH-FROZEN
