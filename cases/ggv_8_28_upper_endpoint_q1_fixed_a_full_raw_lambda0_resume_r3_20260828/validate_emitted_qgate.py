#!/usr/bin/env python3
"""Validate an emitted q-gate packet without recompiling its equations.

For the frozen lambda=0 packet this checks the exact bytes recovered from the
timed-out predecessor.  For any packet it also replays every embedded equation
hash and regenerates all five Singular programs from the JSON representation.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
COMPILER = HERE / "compile_q_gates.py"
COMPILER_SHA256 = "b487d8b532d303421386c66638a6d7953aa5a4dcf74208cd07c6db885c511201"

FROZEN_LAMBDA0 = {
    "Q_GATE_SYSTEM.json": (
        58_975_191,
        "7c4beff1ec5b6e64fafcf800d965e2ea614bcd5d53d14195551f5322f418ab78",
    ),
    "qgates_p65497_dp_slimgb.sing": (
        2_995_909,
        "22e9471e6dea9fc2fb28bd03d5dd4920a4a4d46e04fd6cbe9400a73fa6334a00",
    ),
    "qgates_p65519_dp_slimgb.sing": (
        3_007_030,
        "f719353450c7ffa388a2f05d7908fe74afe730278c65762dc8f1acf94d34c610",
    ),
    "qgates_p65521_lp_std.sing": (
        2_962_714,
        "acc863503d0ad258b42a22211ed4d87e4f58c68c043bb816e4f139678b75dd53",
    ),
    "qgates_q_lp_std.sing": (
        3_717_972,
        "3c96a8e7188af3da3c88081d79d51161b47be81d5ca49af9417aef6a0b1a55eb",
    ),
    "qgates_q_lp_tracked.sing": (
        3_718_299,
        "8813547c3dcf01cf0ae3d8be30aaaa9108191219125cd6be385e2de91c976bd1",
    ),
}

FROZEN_LAMBDA0_SYSTEM_PINS = {
    "cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json":
        "28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876",
    "cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/RESULT.json":
        "568934cecfd224cfdff6f8af0791f71f54426ccc0fc5384fc4d0d90a2712c02e",
    "cases/ggv_8_28_upper_endpoint_active_c2_d11_d13_extension_20260828/verify_active_c2_extension.py":
        "112650dc27b0e13d76979d5adca9315919ee65cb8d9eaf717c1685f99d96de26",
    "cases/ggv_8_28_upper_endpoint_branch_p_20260827/compile_endpoint.py":
        "7f840af57695eb0f4e124885a39eabdd0059dad984c917b826d077c77d396be1",
    "cases/ggv_8_28_upper_endpoint_deep_q1_composition_r1_20260828/verify_deep_q1_composition_r1.py":
        "a5e6479f20cd7fcd50b317e174fd192512e5295de9c2126e717c005cb22acf69",
    "cases/ggv_8_28_upper_endpoint_q1_fixed_a_full_raw_20260828/compile_fixed_q1_raw.py":
        "82284effbd507693cb8deb00e33b108d0f62d3d3861ce487e75d2e3f98b8fbea",
    "cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828/verify_q1_prefix_target.py":
        "fceb189badafad877c1142b8925480516111790707954d2000421b8190fde119",
    "cases/ggv_quarter_root_characteristic_r7_20260827/verify_r7.py":
        "c40820e300f39d92d757de698ecf6c8a5ad0b79711e369275b2de93dd6488244",
    "cases/ggv_quarter_root_characteristic_r7r1_20260827/verify_r7r1.py":
        "1cdf577a2775e7cb1b9c44d0f92edeb6f612a1b52aa659a280390b37d49babaa",
}


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_compiler():
    assert sha256(COMPILER) == COMPILER_SHA256
    spec = importlib.util.spec_from_file_location("ggv_split_qgate_compiler", COMPILER)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def expected_scripts(qg, system):
    return {
        "qgates_p65521_lp_std.sing": qg.singular_script(system, 65521, "lp", "std").encode(),
        "qgates_p65519_dp_slimgb.sing": qg.singular_script(system, 65519, "dp", "slimgb").encode(),
        "qgates_p65497_dp_slimgb.sing": qg.singular_script(system, 65497, "dp", "slimgb").encode(),
        "qgates_q_lp_std.sing": qg.singular_script(system, 0, "lp", "std").encode(),
        "qgates_q_lp_tracked.sing": qg.singular_script(
            system, 0, "lp", "std", tracked=True
        ).encode(),
    }


def validate(system_dir: Path, expected_id: str, frozen_lambda0: bool):
    qg = load_compiler()
    for path, expected in qg.PINS.items():
        assert sha256(path) == expected, (path, sha256(path), expected)

    required = set(FROZEN_LAMBDA0)
    found = {path.name for path in system_dir.iterdir() if path.is_file()}
    allowed = required if frozen_lambda0 else required | {"GENERATED.sha256.json"}
    assert required <= found <= allowed, {
        "missing": sorted(required - found), "extra": sorted(found - allowed)
    }

    byte_custody = {}
    for name in sorted(required):
        path = system_dir / name
        size = path.stat().st_size
        digest = sha256(path)
        byte_custody[name] = {"bytes": size, "sha256": digest}
        if frozen_lambda0:
            expected_size, expected_digest = FROZEN_LAMBDA0[name]
            assert (size, digest) == (expected_size, expected_digest), (
                name, size, digest, expected_size, expected_digest
            )

    raw = (system_dir / "Q_GATE_SYSTEM.json").read_bytes()
    system = json.loads(raw)
    assert qg.ce.pretty(system) == raw, "system JSON is not the frozen canonical pretty encoding"
    assert system["schema"] == "GGV-8_28-UPPER-ENDPOINT-Q1-Q13-DE-RHAM-GATES-v1"
    assert system["system_id"] == expected_id
    assert system["field"] == "Q"
    variables = system["variables"]
    assert len(variables) == len(set(variables)) == system["variable_count"]
    assert system["source_variable_count"] == len(system["source_variables"])
    assert system["primitive_variable_count"] == len(system["primitive_variables"])
    assert variables == system["source_variables"] + system["primitive_variables"]
    assert [gate["q"] for gate in system["gates"]] == list(range(1, 14))

    flattened = []
    equation_hashes = []
    for gate in system["gates"]:
        assert gate["new_variables"] == gate["new_source_variables"] + gate["primitive_variables"]
        for item in gate["equations"]:
            assert item["q"] == gate["q"]
            digest = sha256_bytes(qg.ce.compact(item["terms"]))
            assert digest == item["sha256"], (gate["q"], item["x_degree"], digest, item["sha256"])
            equation_hashes.append(digest)
        flattened.extend(gate["equations"])
    assert flattened == system["equations"]
    assert len(flattened) == system["equation_count"]
    used = {name for item in flattened for mon, _ in item["terms"] for name in mon}
    assert used <= set(variables), sorted(used - set(variables))
    if frozen_lambda0:
        # The recovered JSON must retain its original provenance path.  The
        # executable successor copy is separately byte-pinned above through
        # qg.PINS, so relocation never rewrites historical provenance.
        expected_pins = FROZEN_LAMBDA0_SYSTEM_PINS
        for relative, digest in expected_pins.items():
            if relative.endswith(
                "ggv_8_28_upper_endpoint_q1_fixed_a_full_raw_20260828/compile_fixed_q1_raw.py"
            ):
                actual_path = qg.RAW_COMPILER
            else:
                actual_path = qg.ROOT / relative
            assert sha256(actual_path) == digest, (relative, sha256(actual_path), digest)
    else:
        expected_pins = {str(path.relative_to(qg.ROOT)): digest for path, digest in qg.PINS.items()}
    assert system["pins"] == expected_pins

    regenerated = {}
    for name, payload in expected_scripts(qg, system).items():
        actual = (system_dir / name).read_bytes()
        assert actual == payload, f"regenerated Singular mismatch: {name}"
        regenerated[name] = sha256_bytes(payload)

    if "GENERATED.sha256.json" in found:
        generated_raw = (system_dir / "GENERATED.sha256.json").read_bytes()
        generated = json.loads(generated_raw)
        assert qg.ce.pretty(generated) == generated_raw
        expected_generated = {
            "Q_GATE_SYSTEM.json": byte_custody["Q_GATE_SYSTEM.json"]["sha256"],
            **regenerated,
        }
        assert generated == expected_generated, (generated, expected_generated)

    if frozen_lambda0:
        assert expected_id == "lambda_0_full_qgates"
        assert system["variable_count"] == 318
        assert system["equation_count"] == 263

    return {
        "schema": "GGV-8_28-QGATE-EMISSION-VALIDATION-v1",
        "status": "EMITTED_QGATE_PACKET_VALID",
        "validation_mode": "frozen_lambda0_exact_bytes" if frozen_lambda0 else "structural_regeneration",
        "system_id": system["system_id"],
        "variable_count": system["variable_count"],
        "equation_count": system["equation_count"],
        "equation_hash_count": len(equation_hashes),
        "equation_hash_aggregate_sha256": sha256_bytes(("\n".join(equation_hashes) + "\n").encode()),
        "canonical_json_replay": True,
        "singular_regeneration_replay": True,
        "source_pin_replay": True,
        "byte_custody": byte_custody,
        "regenerated_sha256": regenerated,
        "scope": (
            "This validates an emitted necessary q1..q13 de Rham gate packet. "
            "It does not itself prove emptiness, produce a raw endpoint witness, "
            "or turn a nonunit/incomplete screen into a survivor."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--system-dir", type=Path, required=True)
    parser.add_argument("--system-id", required=True)
    parser.add_argument("--frozen-lambda0", action="store_true")
    parser.add_argument("--exact-output", type=Path, required=True)
    args = parser.parse_args()
    result = validate(args.system_dir, args.system_id, args.frozen_lambda0)
    args.exact_output.parent.mkdir(parents=True, exist_ok=True)
    args.exact_output.write_bytes((json.dumps(result, indent=2, sort_keys=True) + "\n").encode())
    print(json.dumps({
        "status": result["status"],
        "system_id": result["system_id"],
        "variables": result["variable_count"],
        "equations": result["equation_count"],
        "validation_sha256": sha256(args.exact_output),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
