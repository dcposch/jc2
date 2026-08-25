#!/usr/bin/env python3
"""Lightweight dependency-custody audit for repaired V76 review surface."""

from hashlib import sha256
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    expected = {
        ROOT / "cases/td6_c1_c2_c3_q2_fixed_a3_complete_union_v76_aws_20260825/MANIFEST.sha256":
            "e46ad84030c75342844f3fe50ec23cf475eb2afcf45faec12b9c298afcffc980",
        ROOT / "cases/td6_c1_c2_c3_q2_fixed_a3_complete_union_v76_aws_20260825/FREEZE.sha256":
            "41990e3d6cbdfe0deee6be1abb21d00721cbe29f2d618c3a54cfb4b2dce59c41",
        ROOT / "cases/td6_c1_c2_c3_q2_generic_source_dag_v57_review_repair_20260825/FREEZE.sha256":
            "3d68c16dc608cf3a89bc6211558e32988c31690c041cd53f3213c5a338493950",
        ROOT / "cases/td6_c1_c2_c3_q2_b3_atlas_union_v75_review_repair_20260825/FREEZE.sha256":
            "4327e42f77edef0f47b665d700c416c360bddfd3a5f2309ddd05197e2b673328",
        ROOT / "xmodel/td6-c1-c2-c3-q2-fixed-a3-v76-review-v2-prompt-20260825.md":
            "53eb132dbae7961804fac592aa2e3f26d2e9eee7900ed47a989c7ae53b3f6ef3",
    }
    for path, value in expected.items():
        assert digest(path) == value, path
    prompt = (ROOT / "xmodel/td6-c1-c2-c3-q2-fixed-a3-v76-review-v2-prompt-20260825.md").read_text()
    assert "xmodel/td6_v76_fixed_a3_hostile_review_v2_20260825.md" in prompt
    assert "edit no other" in prompt
    print("TD6 V76 repaired review surface custody PASS")


if __name__ == "__main__":
    main()
