#!/usr/bin/env python3
"""Compile the fixed-fixture weighted homogenization of the literal raw ideal."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


HERE = Path(__file__).resolve().parent
RAW_SHA256 = "ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0"


def load_compiler():
    path = HERE / "compile_endpoint.py"
    spec = importlib.util.spec_from_file_location("ggv_endpoint_hom_compiler", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


ce = load_compiler()
MV = ce.MV


def variable_weights(raw, source):
    slot_weights = {
        slot["slot"]: int(slot["weight"])
        for kind in ("F", "G")
        for slot in source["raw_slots_through_weight_22"][kind]
    }
    weights = {}
    for name in raw["variables"]:
        if name.startswith("z_"):
            weights[name] = 2
        elif name.startswith("tt_"):
            weights[name] = 3
        else:
            weights[name] = slot_weights[name]
    return weights


def homogenize(raw, weights):
    records = []
    target_replaced = 0
    for raw_index, record in enumerate(raw["generators"]):
        row = int(record["row"])
        terms = {}
        for encoded_mon, encoded_coefficient in record["terms"]:
            mon = tuple(encoded_mon)
            coefficient = Q(encoded_coefficient)
            if row == 22 and not mon and coefficient == -1:
                new_mon = ("lambda",)
                target_replaced += 1
            else:
                deficit = row - sum(weights[name] for name in mon)
                assert deficit >= 0, (raw_index, row, mon, deficit)
                new_mon = tuple(sorted(mon + ("u",) * deficit))
            terms[new_mon] = terms.get(new_mon, Q(0)) + coefficient
            if not terms[new_mon]:
                del terms[new_mon]
        poly = MV(terms)
        records.append({
            "source_raw_index": raw_index,
            "row": row,
            "x_degree": int(record["x_degree"]),
            "terms": poly.encode(),
            "sha256": hashlib.sha256(ce.compact(poly.encode())).hexdigest(),
        })
    assert target_replaced == 1
    normalization = MV({("lambda",): Q(1), ("u",) * 22: Q(-1)})
    return records, normalization


def compile_system():
    raw_path = HERE / "RAW_DIRECT_SYSTEM.json"
    assert ce.sha256(raw_path) == RAW_SHA256
    raw = json.loads(raw_path.read_text())
    source = json.loads(ce.RAW_INPUT.read_text())
    weights = variable_weights(raw, source)
    records, normalization = homogenize(raw, weights)
    all_weights = {"lambda": 22, "u": 1, **weights}
    return {
        "schema": "GGV-8_28-UPPER-ENDPOINT-BRANCH-P-HOMOGENIZED-v1",
        "authoritative_raw_system_sha256": RAW_SHA256,
        "method": "row-weight homogenization with fixed-fixture scale u",
        "variables": ["lambda", "u", *raw["variables"]],
        "variable_weights": all_weights,
        "raw_generator_count": len(raw["generators"]),
        "generators": records,
        "generator_count": len(records) + 1,
        "normalization": {
            "equation": "lambda-u^22",
            "terms": normalization.encode(),
        },
        "saturation_variable": "lambda",
        "dehomogenization": {"lambda": 1, "u": 1},
        "D23_imposed": False,
        "G22_present": False,
    }


def singular_text(system):
    variables = system["variables"]
    weights = [system["variable_weights"][name] for name in variables]
    expressions = [MV({tuple(mon): Q(c) for mon, c in record["terms"]}).expression()
                   for record in system["generators"]]
    normalization = MV({tuple(mon): Q(c)
                        for mon, c in system["normalization"]["terms"]}).expression()
    lines = [
        'LIB "elim.lib";',
        f"ring endpoint_hom=0,({','.join(variables)}),wp({','.join(map(str, weights))});",
        "option(redSB);",
        "ideal I=",
        ",\n".join([*expressions, normalization]) + ";",
        'print("HOMOGENIZED variables="+string(nvars(basering))+" generators="+string(size(I)));',
        'print("START_SAT");',
        "int start_time=timer;",
        "list S=sat(I,ideal(lambda));",
        "ideal J=std(S[1]);",
        "int elapsed=timer-start_time;",
        'print("END_SAT seconds="+string(elapsed));',
        'print("SAT_EXPONENT="+string(S[2]));',
        'print("BASIS_SIZE="+string(size(J)));',
        "int is_unit=(size(J)==1 && J[1]==1);",
        'print("UNIT="+string(is_unit));',
        'if(!is_unit){print("DIM="+string(dim(J)));}',
        "J;",
        "quit;",
        "",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    system = compile_system()
    payloads = {
        "HOMOGENIZED_SYSTEM.json": ce.pretty(system),
        "homogenized_q_sat.sing": singular_text(system).encode(),
    }
    args.output.mkdir(parents=True, exist_ok=True)
    for name, payload in payloads.items():
        path = args.output / name
        if args.check:
            assert path.read_bytes() == payload, f"stale generated file: {path}"
        else:
            path.write_bytes(payload)
    print(json.dumps({
        "status": "PASS",
        "raw_generators": system["raw_generator_count"],
        "homogeneous_generators": system["generator_count"],
        "system_sha256": hashlib.sha256(payloads["HOMOGENIZED_SYSTEM.json"]).hexdigest(),
        "singular_sha256": hashlib.sha256(payloads["homogenized_q_sat.sing"]).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
