#!/usr/bin/env python3
"""Lightweight custody verifier for the V78B/V78C hostile review."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


PINS = {
    "evidence/prompt.md": "0ea1d10ca0c0d0b3cbe96c030d8557766277249e47a9d28009b88c5a0ed5f82a",
    "evidence/run.txt": "4670563f24340d04aa067165281ae967948483266c26ee5d190e3369e8802a6a",
    "evidence/log.txt": "fe8b88d9233168315ad13161740fdc0cc03fc1bb53399d09980632b8be7ddbd3",
    "evidence/review.md": "a3599e65f88015f60a3131572716affda748d8dc5963e3648bb35842246a1861",
}
for relative, expected in PINS.items():
    assert digest(HERE / relative) == expected, relative

run_lines = (HERE / "evidence/run.txt").read_text().splitlines()
assert "exit_code=0" in run_lines
assert "final_status=DONE" in run_lines
assert f"report_sha256={PINS['evidence/review.md']}" in run_lines
assert (HERE / "evidence/review.md").read_text().splitlines()[-1] == "CONFIRMED"
prompt = (HERE / "evidence/prompt.md").read_text()
assert "xmodel/td6_v78bc_all_q_p12_hostile_review_v3_20260826.md" in prompt
assert "edit no other" in prompt

external = {
    ROOT / "cases/td6_c1_c2_c3_all_q_p12_shards_v78c_aws_20260826/MANIFEST.sha256":
        "c93959e757927dc238e01aa4ff5d053ebe9154ce5e33f0a8cae2581d981154ad",
    ROOT / "cases/td6_c1_c2_c3_all_q_p12_shards_v78c_aws_20260826/FREEZE.sha256":
        "41ba8ca50c6edcbb172344deebf201646840bc343bbaa52f762faca8a478b731",
    ROOT / "cases/td6_c1_c2_c3_all_q_p12_reconciliation_v78bc_aws_20260826/MANIFEST.sha256":
        "f7cee1aa863d9ebac18c079cf5fb982659964c7877b51dac33835d03a32734a9",
    ROOT / "cases/td6_c1_c2_c3_all_q_p12_reconciliation_v78bc_aws_20260826/FREEZE.sha256":
        "7434fc4d75b32945b15c4704be44930738daf3eb5f414129c070a388ac8d3031",
    ROOT / "xmodel/td6-c1-c2-c3-all-q-p12-shards-v78c-aws-20260826.md":
        "cffa164efb6c1b19d16a11e0d75880756f3d3b54cf93585c3fcc7c1500146fc5",
    ROOT / "xmodel/td6-c1-c2-c3-all-q-p12-reconciliation-v78bc-aws-20260826.md":
        "76a0b548e40c9f234c780f11054aac1e68dcab4f4de9b4e558e61c844200c627",
}
for path, expected in external.items():
    assert digest(path) == expected, path

print("TD6 V78B/V78C hostile-review custody verification PASS")
