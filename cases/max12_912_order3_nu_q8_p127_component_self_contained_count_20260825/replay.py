#!/usr/bin/env python3
"""Self-contained contact count using only lifted fibres."""

from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BREADTH = ROOT / "cases/max12_912_order3_nu_q8_p127_breadth_order8_aws_20260825/breadth_summary.json"
ORDER64 = ROOT / "cases/max12_912_order3_nu_q8_p127_hensel_order64_aws_20260825/aws_order64_box02_v1"
SPARSE_REPORT = ROOT / "xmodel/max12-912-order3-nu-q8-sparse-contact-component-lemma-20260825.md"
EXPECTED = {
    "breadth": "7cfeb94ca1f6c36bbdaf6fd32e163f4b3a764383a45b6f1c7f1c2ad919f91d74",
    "order64_stdout": "f750d965a48634d2b47b442b47577b67b900a810ab208c2dc08f03fd5cd299aa",
    "order64_meta": "3cd0c3ca50dd6f3f956c8271b317ced35a2e3ca637ab2f6ce6f37cf99840bc9d",
    "sparse_report": "78fb3e1b08556498d79ed180f9b64e243f88dd80780936bc47e15b3749b5ce77",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    assert digest(BREADTH) == EXPECTED["breadth"]
    assert digest(ORDER64 / "result.out") == EXPECTED["order64_stdout"]
    assert digest(ORDER64 / "run.meta") == EXPECTED["order64_meta"]
    assert digest(SPARSE_REPORT) == EXPECTED["sparse_report"]
    breadth = json.loads(BREADTH.read_text())
    assert breadth["status"] == "PASS"
    assert breadth["pass_count"] == 80 and breadth["fail_count"] == 0
    assert breadth["order"] == 8 and breadth["prime"] == 127
    values = breadth["all_passing_w"]
    assert len(values) == len(set(values)) == 80 and 25 not in values
    order64 = (ORDER64 / "result.out").read_text().splitlines()
    for marker in (
        "base_fail=0", "H0_degree=190", "gcd_detJ_H0_degree=0",
        "gcd_Hv_H0_degree=0", "moving_vdim=12160", "order=64", "final_fail=0",
    ):
        assert order64.count(marker) == 1, marker
    meta = (ORDER64 / "run.meta").read_text().splitlines()
    for marker in ("base_w=25", "hensel_order=64", "rc=0", "endpoint=PASS"):
        assert meta.count(marker) == 1, marker
    contact_sum = 80 * 8 + 64
    sparse_bound = 658
    assert contact_sum == 704 and contact_sum > sparse_bound
    print("Q8-P127-SELF-CONTAINED-CONTACT-COUNT PASS")
    print("order8_fibres=80")
    print("order64_fibres=1")
    print("contact_sum=704")
    print("sparse_bound=658")
    print("strict_excess=46")


if __name__ == "__main__":
    main()
