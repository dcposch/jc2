#!/usr/bin/env python3
"""Independent custody and structural replay for the reduced tail-7 seed."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BRANCH = ROOT / "cases/ggv_8_28_upper_endpoint_branch_p_20260827"
D3 = ROOT / "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827"
TAIL_DIR = HERE / "TAIL7_REDUCED"

HASHES = {
    BRANCH / "tail_deformation.py": "a411d66158b01e3baf611067e29b223d88370bf01e7c8d84e09e87e72023f626",
    BRANCH / "RAW_DIRECT_SYSTEM.json": "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0",
    D3 / "RAW_INPUT.json": "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    TAIL_DIR / "TAIL_DEFORMATION_SYSTEM.json": "7edd5ccd471e9eb3e27f0f163b0b337e0fb5057126ec69869f988093defba7aa",
    TAIL_DIR / "tail_q.sing": "569b1ab1da9a2ba9cd063ab98252a395b948368ad0e8d7e80da3794faeb3f8bb",
    TAIL_DIR / "TAIL7_REDUCED_SYSTEM.json": "770ba6d9b312e235e491b4ad948707c41ad4a622b3a17239fdfe62f353606e11",
    TAIL_DIR / "tail7_reduced_q.sing": "a90ca7d9b0ed14d335e20d44308830ff6f0d90ca4dab247658cc75842883e93f",
    TAIL_DIR / "tail7_reduced_p65521.sing": "55c1bfe67fe21413f20c5cbf420728552edd3722c536337ea4879eee050f44a9",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def endpoint_constant_terms(system):
    records = [
        record for record in system["constraints"]
        if int(record["row"]) == 22 and int(record["x_degree"]) == 0
    ]
    assert len(records) == 1
    return records[0]["terms"]


def main():
    for path, expected in HASHES.items():
        assert sha256(path) == expected, path

    tail_module = load_module("tail_deformation_frozen", BRANCH / "tail_deformation.py")
    tail7 = tail_module.compile_tail(7)
    assert hashlib.sha256(tail_module.pretty(tail7)).hexdigest() == HASHES[
        TAIL_DIR / "TAIL_DEFORMATION_SYSTEM.json"
    ]
    assert tail7["retained_variable_count"] == 190
    assert tail7["prefix_rank"] == 102
    assert tail7["nullity"] == 88
    assert endpoint_constant_terms(tail7) == [
        [[], "-1"],
        [[32, 87], "-1"],
    ]
    assert ["f_0_1", "1"] in tail7["nullspace_basis"][87]
    assert tail7["nullspace_basis"][32] == [["g_1_0", "1"]]

    # The two cheaper tails are identically empty at the endpoint constant;
    # this is a direct exact compile, not a Gröbner inference.
    for cutoff in (8, 9):
        tail = tail_module.compile_tail(cutoff)
        assert endpoint_constant_terms(tail) == [[[], "-1"]], cutoff

    reducer = load_module("tail7_reducer_frozen", HERE / "reduce_tail7_endpoint.py")
    reduced = reducer.compile_reduced()
    assert hashlib.sha256(reducer.pretty(reduced)).hexdigest() == HASHES[
        TAIL_DIR / "TAIL7_REDUCED_SYSTEM.json"
    ]
    assert reduced["remaining_parameter_count"] == 41
    assert reduced["constraint_count"] == 152
    assert reduced["maximum_constraint_degree"] == 3
    assert reduced["fixed_chart"]["endpoint_constant_identity"] == "D22[X^0]=-p32*p87=1"
    assert reduced["linear_cleanup_log"] == [
        {"equation_count": 1, "candidate_parameter_count": 1,
         "rank": 1, "pivot_parameters": [86]},
        {"equation_count": 1, "candidate_parameter_count": 1,
         "rank": 1, "pivot_parameters": [76]},
        {"equation_count": 1, "candidate_parameter_count": 2,
         "rank": 1, "pivot_parameters": [67]},
    ]
    assert len(reduced["raw_value_polynomial_map"]) == 303
    remaining = set(reduced["remaining_parameters"])
    for encoded in reduced["p_reconstruction"].values():
        assert all(set(monomial).issubset(remaining) for monomial, _ in encoded)
    for encoded in reduced["raw_value_polynomial_map"].values():
        assert all(set(monomial).issubset(remaining) for monomial, _ in encoded)

    # Re-emit both engines into a disposable directory and demand byte-level
    # identity.  This also exercises the full reducer, not only static JSON.
    with tempfile.TemporaryDirectory(prefix="tail7-replay-") as temp:
        output = Path(temp)
        payloads = {
            "TAIL7_REDUCED_SYSTEM.json": reducer.pretty(reduced),
            "tail7_reduced_q.sing": reducer.singular_text(reduced).encode(),
            "tail7_reduced_p65521.sing": reducer.singular_text(reduced, 65521).encode(),
        }
        for name, payload in payloads.items():
            path = output / name
            path.write_bytes(payload)
            assert path.read_bytes() == (TAIL_DIR / name).read_bytes(), name

    print(json.dumps({
        "status": "PASS",
        "tail8_tail9_endpoint_constant": "literal_-1",
        "tail7_endpoint_chart": "p87=1,p32=-1",
        "remaining_parameters": 41,
        "constraints": 152,
        "maximum_degree": 3,
        "raw_reconstruction_slots": 303,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
