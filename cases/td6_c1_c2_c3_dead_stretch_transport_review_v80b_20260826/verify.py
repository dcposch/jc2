#!/usr/bin/env python3
"""Lightweight review-custody verifier; no producer execution."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
EXPECTED = {
    "evidence/prompt.md": "2f2dd5cc03e6aa42703963a05cd957cc535d421321b2fc98aa1491759fff63f4",
    "evidence/report.md": "3dad10e57ba372298ba0b766adaeb8d452591bb08e5e11c7bee8ec25cfd488ca",
    "evidence/review.log": "c23a1e025ba8179ee6362d749c6e08d89881304a5a0185d920306e73be8d253f",
    "evidence/review.run": "8475d6d5d416753d9953c3b7940661f3a11ce6f86559ccdb5a0f3eb2eef71fdf",
}
for relative, expected in EXPECTED.items():
    assert sha256((HERE / relative).read_bytes()).hexdigest() == expected
report = (HERE / "evidence/report.md").read_text()
assert report.rstrip().endswith("CONFIRMED")
assert "not a joint 11-axis kernel" in report
assert "not a generic-center statement" in report
run = (HERE / "evidence/review.run").read_text()
assert "final_status=DONE" in run
assert "exit_code=0" in run
print("TD6 V80B HOSTILE-REVIEW CUSTODY PASS")
