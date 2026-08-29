#!/usr/bin/env python3
"""Light custody and result replay for the AWS quadratic-Q navigation grid."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
EVIDENCE = HERE / "aws_grid_r1"
FILES = {
    "aws_exact_lane.sh": "ebe06a100ae8f6bcdbdc580be89954d4cbc560c97cd75014153d61292415959b",
    "aws_probe_quadratic_q.py": "2c9c6d0245fdb20b1c826584d852ec54b3bb63d7488698116b05754d206be527",
    "verify_even_subbranch_reduction.py": "23f46a95170fb77f2f5c340b1c6fb570881062d67102fca6dfdeae2f5ea37c4d",
    "verify_lambda0_q15.py": "6c63fe47ebf35dd56e286ab358b0932f1dad9143875fde30c216a425119e442a",
    "ggv-lambda0-quadratic-q-g15-grid-r1-20260828.meta": "2271216930b839eda22c9cab7b61c98627d47e9f73612ea735a84028138545cf",
    "ggv-lambda0-quadratic-q-g15-grid-r1-20260828.stdout": "68447f9a40fa1d902049b327d793be1132426418bf0c6a642f162bb8c17242f0",
    "ggv-lambda0-quadratic-q-g15-grid-r1-20260828.stderr": "16e91dd15e26d191d116fbfc01013fa6e26b0dbcb47a8e1189bf638b1d75716b",
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    for name, expected in FILES.items():
        assert sha256(EVIDENCE / name) == expected, name
    meta = (EVIDENCE / "ggv-lambda0-quadratic-q-g15-grid-r1-20260828.meta").read_text()
    assert "lane=ggv-lambda0-quadratic-q-g15-grid-r1-20260828" in meta
    assert "host=ip-172-30-0-249" in meta
    assert "rc=0" in meta
    assert "stdout_sha256=68447f9a40fa1d902049b327d793be1132426418bf0c6a642f162bb8c17242f0" in meta
    assert "stderr_sha256=16e91dd15e26d191d116fbfc01013fa6e26b0dbcb47a8e1189bf638b1d75716b" in meta
    source = (EVIDENCE / "aws_probe_quadratic_q.py").read_text()
    assert 'platform.system() == "Linux"' in source
    assert '"Amazon" in Path("/sys/class/dmi/id/sys_vendor").read_text()' in source
    assert "qm.h7_to_h15" in source
    assert "for weight in range(9, 16, 2)" in source
    assert "endpoint_nonzero_witness" in source
    result = json.loads(
        (EVIDENCE / "ggv-lambda0-quadratic-q-g15-grid-r1-20260828.stdout").read_text()
    )
    assert result["run_tag"] == "ggv-lambda0-quadratic-q-g15-grid-r1-20260828"
    assert result["mode_grid"] == [-2, -1, 0, 1, 2]
    assert result["mode_variables"] == ["c4", "c6", "c8"]
    assert set(result["fixtures"]) == {
        "X", "1", "1+X", "X2", "1+X2", "X+X2", "1+X+X2",
    }
    assert result["first_nonzero_endpoint_witness"] is None
    total = 0
    dimensions = set()
    for record in result["fixtures"].values():
        assert record["nonzero_endpoint_mode_count"] == 0
        total += sum(record["dimension_counts"].values())
        dimensions.update(map(int, record["dimension_counts"]))
    assert total == 7 * 5**3 == 875
    assert min(dimensions) == 0 and max(dimensions) == 6
    stderr = (EVIDENCE / "ggv-lambda0-quadratic-q-g15-grid-r1-20260828.stderr").read_text()
    assert "Maximum resident set size (kbytes): 21032" in stderr
    assert "Exit status: 0" in stderr
    print("AWS_host=ip-172-30-0-249;rc=0;max_RSS_kB=21032")
    print("sampled_Q=7;sampled_modes_per_Q=125;total=875")
    print("endpoint_nonzero_witnesses=0;survivor_dimensions_include_0_through_6_extremes")
    print("scope=navigation_grid_not_universal_theorem")
    print("PASS_QUADRATIC_Q_GRID_CUSTODY")


if __name__ == "__main__":
    main()
