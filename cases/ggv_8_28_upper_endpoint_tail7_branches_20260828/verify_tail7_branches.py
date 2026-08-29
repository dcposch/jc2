#!/usr/bin/env python3
"""Custody replay for the exact tail-seven field split and shared block."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import tempfile
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / (
    "cases/ggv_8_28_upper_endpoint_tail7_reduced_20260828/"
    "TAIL7_REDUCED/TAIL7_REDUCED_SYSTEM.json"
)
OUTPUT = HERE / "BRANCHES"
EXPECTED = {
    "a3_4.json": "a887e6197293f0b0229ed27f06e40149912d2c4fb7a0f9de1a2c8d69ddec6e4d",
    "a3_4_q.sing": "457726da9ff0949e025a331b8e27349d4c4461374a865c0700d3e0f64b5d90cd",
    "a3_4_p65521.sing": "27eb51b3df27b789886771acbefe22e38729779f87e95ab859fce1b3764bee79",
    "a3_2.json": "b1bb657096e6e7936f86ab76adadf39a62f85d57c14b592f450689d09f4051a4",
    "a3_2_q.sing": "714117a4562f9e284b2f46f7260774d7819ff6ef171af5776ac9b08008aa6dde",
    "a3_2_p65521.sing": "8de0614656f75d5147c3d2888cb05fe29366c54009f9b66143c2917f621bb665",
    "shared_block.json": "3e586cc283526efa9c12f51f5be5535d31eaa1b03ee0296783438acabf9feaab",
    "shared_block_q.sing": "458dce839bce84004be992e146603f05dbce4a1716c5717a4c7ac130e2e1707c",
    "shared_block_p65521.sing": "06d4b9ca32dd56960ea24e040dca681bcde56574898063838c87e2ccb91b4951",
}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_module(path):
    spec = importlib.util.spec_from_file_location("tail7_branch_compiler", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def variables(record):
    return {variable for monomial, _coefficient in record["terms"]
            for variable in monomial}


def evaluate(record, values):
    total = Q(0)
    for monomial, coefficient in record["terms"]:
        term = Q(coefficient)
        for variable in monomial:
            term *= values[variable]
        total += term
    return total


def main():
    assert sha256(SOURCE) == "770ba6d9b312e235e491b4ad948707c41ad4a622b3a17239fdfe62f353606e11"
    for name, expected in EXPECTED.items():
        assert sha256(OUTPUT / name) == expected, name

    source = json.loads(SOURCE.read_text())
    sparse = [record for record in source["constraints"]
              if variables(record) and variables(record).issubset({54, 60, 68})]
    assert [record["index"] for record in sparse] == [48, 65, 83, 101]
    expected_terms = [
        [[[], "4"], [[60], "6"], [[68], "-8"], [[68, 68], "32/9"]],
        [[[], "3/2"], [[54], "6"], [[60], "-3/4"], [[60, 68], "4"],
         [[68], "-3"], [[68, 68], "4/3"]],
        [[[54], "-3/4"], [[54, 68], "4"], [[60], "-9/8"],
         [[60, 68], "3/2"]],
        [[[54], "-9/8"], [[54, 68], "3/2"]],
    ]
    assert [record["terms"] for record in sparse] == expected_terms
    for point in ({68: Q(3, 4), 60: Q(0), 54: Q(0)},
                  {68: Q(3, 2), 60: Q(0), 54: Q(0)}):
        assert all(evaluate(record, point) == 0 for record in sparse)
    # Algebraic completeness of the split:
    # E20=(3/2)c(a-3/4); off a=3/4, E19=(3/2)b(a-3/4);
    # then E17=(32/9)(a-3/4)(a-3/2).
    assert Q(32, 9) * Q(-3, 4) * Q(-3, 2) == Q(4)

    compiler = load_module(HERE / "compile_tail7_branches.py")
    compiled = {
        name: compiler.compile_branch(name, fixed)
        for name, fixed in compiler.BRANCHES.items()
    }
    assert compiled["a3_4"]["remaining_parameter_count"] == 33
    assert compiled["a3_2"]["remaining_parameter_count"] == 33
    for name, result in compiled.items():
        operative = set(variable for record in result["constraints"]
                        for monomial, _coefficient in record["terms"]
                        for variable in monomial)
        assert len(operative) == 31
        assert result["constraint_count"] == 143
        assert result["maximum_degree"] == 3
        assert result["raw_slot_count"] == 303
        assert sha256(OUTPUT / f"{name}.json") == hashlib.sha256(
            compiler.pretty(result)
        ).hexdigest()

    block_variables = set(range(78, 86))
    blocks = []
    for result in compiled.values():
        blocks.append([record for record in result["constraints"]
                       if variables(record) and variables(record).issubset(block_variables)])
    assert len(blocks[0]) == 16
    assert [record["terms"] for record in blocks[0]] == [
        record["terms"] for record in blocks[1]
    ]
    block = json.loads((OUTPUT / "shared_block.json").read_text())
    assert block["remaining_parameter_count"] == 8
    assert block["constraint_count"] == 16
    assert block["maximum_degree"] == 2
    assert [record["terms"] for record in block["constraints"]] == [
        record["terms"] for record in blocks[0]
    ]

    print(json.dumps({
        "status": "PASS",
        "field_branches": ["a3_4", "a3_2"],
        "operative_parameters_each": 31,
        "constraints_each": 143,
        "shared_block": "8_variables_16_quadrics",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
