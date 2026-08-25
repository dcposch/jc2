#!/usr/bin/env python3
"""Fail-closed custody replay for the three rational Q8 contact orders."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
P = 127
BOUND = 35582

DEPENDENCIES = {
    ROOT / "xmodel/max12-912-order3-nu-q8-sparse-bidegree-residual-bound-20260825.md":
        "06a90ac1c0e75adef3916ef3aad5a41ea40c55bac75d9c633aaf74b8aaaf5d18",
    ROOT / "xmodel/max12-912-order3-nu-q8-p127-component-reviewed-successor-20260825.md":
        "7d28a7b4b7d3ecd3179efc73f0251754fbfea87614b6eb6daef2d7d649dba202",
    ROOT / "xmodel/max12-912-order3-nu-q8-p127-full-contact-jacobian-aws-20260825.md":
        "558d9e292ba246bf4011e71e11a28bcd8972cb76ff0aa1bc97d408ce32350afd",
    ROOT / "cases/max12_912_order3_nu_q8_p127_full_contact_jacobian_aws_20260825/aws_box02_v1/result.json":
        "804f9fbb095832e79a4f01ad870ed87a55921b78f34ff9f83ae946da04b70549",
}

PASS_LANES = {
    "linear67": {
        "root": 67,
        "order": 16384,
        "directory": HERE / "aws_box02_v5/q8_contact_linear67_order16384_box02_v5",
        "input": "6bf233323dcc72f00291d849977818d93d3fc99b9d1c93b5e42f6d74e543b539",
        "stdout": "4bff2931b472c831a17546b6f0f098a1bd4651e819f99591faf8810d978d5889",
        "stderr": "dc67e8bc1af59be0ed72571b0df13d90e3ac438785f95d8bbef1494f657f43bb",
        "meta": "be3aad74778c7690d47f152086e13e2bc870f874f3561dec1d0750a5bec885cf",
    },
    "linear58": {
        "root": 58,
        "order": 16384,
        "directory": HERE / "aws_box02_v5/q8_contact_linear58_order16384_box02_v5",
        "input": "c0581cbcc28ff7fcb80ee6edf6430bdaf64cd91ac0ba84bd128d01b58477b0ca",
        "stdout": "be897a19ca10b762badf0757fc48bf179463b13291523cc49138a07d0d3a6dbb",
        "stderr": "b10e1d77670eeb7e2934d8d518e17ece3661ea498991d7665ebe8794eef6d0a3",
        "meta": "279acc7810d9c139aace4b1e825dd1d0a7ff1f3cddf7701859466fe73c17632c",
    },
    "linear26": {
        "root": 26,
        "order": 8192,
        "directory": HERE / "dependency_linear26_order8192/q8_contact_linear26_order8192_box03_v1",
        "input": "d9f6e30cc7c5bec4eebc50b090bcf142e9a1bbc72f78851125f950840737a3a5",
        "stdout": "359cc2d3187037a741bbced81ac0bee211cea7012fdc10fd74ded84678d6a4be",
        "stderr": "bd45c4cac7d48fae5828be12daa366196839f0e0be0a090f449197cce1beb99e",
        "meta": "2d5a8f33b0f1d15bc3850efd9f0c23e88a2ed27deb320a8b740786e9166645fb",
    },
}

FACTORS = {
    "linear67": [60, 1],
    "linear58": [69, 1],
    "linear26": [101, 1],
    "quintic": [79, 118, 26, 38, 53, 1],
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_hash(path: Path, expected: str) -> None:
    got = digest(path)
    if got != expected:
        raise RuntimeError((str(path), got, expected))


def metadata(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text().splitlines():
        if "=" in line and not line.startswith("source_sha256="):
            key, value = line.split("=", 1)
            out[key] = value
    return out


def multiply(left: list[int], right: list[int]) -> list[int]:
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] = (out[i + j] + a * b) % P
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def verify_pass_lane(name: str, lane: dict) -> None:
    directory = lane["directory"]
    require_hash(directory / "input.sing", lane["input"])
    require_hash(directory / "result.out", lane["stdout"])
    require_hash(directory / "stderr.log", lane["stderr"])
    require_hash(directory / "run.meta", lane["meta"])
    require_hash(directory / "generator.stderr", sha256(b"").hexdigest())
    meta = metadata(directory / "run.meta")
    if meta.get("factor") != name or meta.get("order") != str(lane["order"]):
        raise RuntimeError((name, "metadata identity", meta))
    if meta.get("generator_rc") != "0" or meta.get("rc") != "0" or meta.get("endpoint") != "PASS":
        raise RuntimeError((name, "endpoint", meta))
    output = set((directory / "result.out").read_text().splitlines())
    required = {
        f"factor={name}",
        "base_fail=0",
        "gcd_detJ_factor_degree=0",
        f"order={lane['order']}",
        f"moving_vdim={lane['order']}",
        "final_fail=0",
        "h_contact_order=-1",
        "h_lead_coefficient=0",
        f"h_contact_at_least={lane['order']}",
    }
    missing = sorted(required - output)
    if missing:
        raise RuntimeError((name, "missing endpoint lines", missing))


def verify_negative_controls() -> None:
    expected = [
        (HERE / "aws_box03_v1_fail/q8_contact_linear67_order16384_box03_v1", "14"),
        (HERE / "aws_box03_v1_fail/q8_contact_linear58_order16384_box03_v1", "14"),
        (HERE / "aws_box02_v6_terminated/q8_contact_linear67_order16384_box02_v6_384g", "143"),
        (HERE / "aws_box02_v6_terminated/q8_contact_linear58_order16384_box02_v6_384g", "143"),
    ]
    for directory, rc in expected:
        meta = metadata(directory / "run.meta")
        if meta.get("rc") != rc or meta.get("endpoint") != "FAIL":
            raise RuntimeError((str(directory), meta))


def main() -> None:
    for path, expected in DEPENDENCIES.items():
        require_hash(path, expected)
    contact_path = next(path for path in DEPENDENCIES if path.name == "result.json")
    contact = json.loads(contact_path.read_text())
    if contact.get("status") != "PASS" or not contact.get("q8_squarefree"):
        raise RuntimeError("contact endpoint")
    product = [1]
    for factor in FACTORS.values():
        product = multiply(product, factor)
    if product != contact["q8_monic_low_to_high"]:
        raise RuntimeError(("factorization", product, contact["q8_monic_low_to_high"]))
    roots = [lane["root"] for lane in PASS_LANES.values()]
    if len(set(roots)) != 3:
        raise RuntimeError(("distinct roots", roots))
    for name, lane in PASS_LANES.items():
        factor = FACTORS[name]
        if (factor[0] + factor[1] * lane["root"]) % P:
            raise RuntimeError((name, factor, lane["root"]))
        verify_pass_lane(name, lane)
    verify_negative_controls()
    order_sum = sum(lane["order"] for lane in PASS_LANES.values())
    if order_sum != 40960 or order_sum <= BOUND:
        raise RuntimeError((order_sum, BOUND))
    print("Q8-RATIONAL-CONTACT-RESIDUAL-REPLAY")
    print("status=PASS")
    print("distinct_rational_roots=" + ",".join(map(str, sorted(roots))))
    print("contact_orders=8192,16384,16384")
    print(f"contact_sum={order_sum}")
    print(f"residual_bound={BOUND}")
    print(f"strict_margin={order_sum - BOUND}")
    print("negative_controls=2_memory_fail,2_superseded_terminated")
    print("composed_claim=PROVISIONAL_BIDEGREE_REVIEW_PENDING")


if __name__ == "__main__":
    main()
