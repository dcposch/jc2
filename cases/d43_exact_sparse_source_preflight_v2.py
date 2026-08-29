#!/usr/bin/env python3
"""Revision-2 light preflight for the exact a00pp D43 row campaign.

This supersedes, but does not rewrite, the v1 preflight.  It incorporates the
sealed hostile reviews and distinguishes the raw-J emitter from the exact
E+one-unit projection of the displayed E5/E6 subsystem.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import d43_common_integral_emitter as COMMON
import d43_exact_sparse_source_preflight as V1_PREFLIGHT

V2_DIR = HERE / "d43_exact_sparse_rows_v2_20260828"
spec = importlib.util.spec_from_file_location(
    "d43_exact_sparse_rows_v2_preflight", V2_DIR / "selected_rows_v2.py")
V2 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = V2
spec.loader.exec_module(V2)


REVIEW_INPUTS = {
    "xmodel/d43-exact-sparse-rows-hostile-review-gpt56-20260828.md":
        "283d47df4f55a0e83fbf1758cc8ac71fbe5ee8549dcdb1c3a6838c8ccc42b21e",
    "xmodel/d43-exact-sparse-source-opus5-hostile-audit-20260828.md":
        "456edb3ad982da10c13ebe6f41e9ebdf7e7124e1ae4ef76363f253626ad5fea0",
    "xmodel/d43-raw-source-template-scope-fable5-audit-20260828.md":
        "69db2cd88f9f309ac047fd858134e19735f238d5c6b8d3a346cc24f3f554eda7",
    "xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md":
        "e1b99600b01f91f7b95df4f7f969481efa1e7b1ee377e83156f3f6b6a8e3c863",
}


def sha256_path(path: Path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def run():
    review_hashes = {}
    for relative, expected in REVIEW_INPUTS.items():
        actual = sha256_path(ROOT / relative)
        assert actual == expected, (relative, actual, expected)
        review_hashes[relative] = actual
    v1 = V1_PREFLIGHT.run()
    manifest, _manifest_hash = V2.load_manifest(
        V2_DIR / "PIPELINE_MANIFEST.json")
    _orbits, names, registry_hash, pin42 = V2.BASE.reconstruct_registry()
    expected = V2.expected_collapsed_d21_band20(manifest, names)
    d21_gate = V2.collapsed_d21_gate(expected, manifest, names)
    bridge = V2.template_bridge_spec()
    modular_bridge = []
    for prime in (105337, 105673):
        point = json.loads((HERE /
            ("d43_full_certificate_p%d.json" % prime)).read_text())["point"]
        W1, W2 = point["parked_28"]["W1"], point["parked_28"]["W2"]
        unit = pow(W1 * W2 % prime, -1, prime)
        modular_bridge.append(V2.template_bridge_modular_gate(
            W1, W2, unit, prime, COMMON.REGISTERED_FRAMES[prime]))
    return {
        "schema": "jc2.d43.a00pp-exact-source-preflight.v2",
        "status": "V2_LIGHT_PREFLIGHT_PASS_AWS_STILL_UNREGISTERED",
        "verdict": "GO_AFTER_FRESH_HOSTILE_PASS_AND_AWS_REGISTRATION",
        "revision_provenance": {
            "v1_report_current_sha256":
                "480c7dcd52543a438cf9588d4842273c717cc3695bade2ff87c923b9d9ea262c",
            "v1_original_sidecar_report_sha256":
                "539d640776d17305a4e257f842fe0ee74ff9edec994f2db479b86bb3e97e3e16",
            "review_inputs": review_hashes,
            "meaning": "v1 is historical and superseded; no historical "
                       "claim is silently upgraded",
        },
        "coefficient_algebra": V2.COEFFICIENT_ALGEBRA,
        "coefficient_algebra_sha256": V2.coefficient_algebra_sha256(),
        "registry_sha256": registry_hash,
        "support_sha256": V2.support_sha256(),
        "pin42_names": list(pin42),
        "v1_shape_evidence": {
            "common_support": v1["prime_audits"][0]
                ["floor_passing_modular_point_support"],
            "exact_low_source": v1["exact_low_source"],
        },
        "exact_collapsed_d21_fixture_gate": d21_gate,
        "template_bridge": bridge,
        "registered_modular_template_bridge_replays": modular_bridge,
        "one_immutable_pipeline": {
            "stages": [
                "independent concurrent f/g collapsed builds",
                "matched pair receipt",
                "exact collapsed D21 band20 gate",
                "same-manifest conditional 184-row emission and merge",
                "atomic terminal and artifact inventory",
            ],
            "solve": False,
            "aws_registered": False,
        },
        "required_real_run_checks": {
            "exact_live_rows": 29,
            "exact_zero_rows": 155,
            "live_bands": {"20": 10, "30": 9, "40": 10},
            "maximum_tail_degree": 2,
            "all_184_registered_modular_replays": True,
        },
        "claim_tiers": {
            "tier1": "exact a00pp emission of 184 raw-J rows",
            "tier2": "a solution of raw-J plus E and one W1*W2 unit row",
            "tier2_replay": "mandatory literal HM/s1F reconstruction and "
                            "E5/E6/unit replay",
            "tier3": "all other applicable residue-A/template equations",
            "NF_all_depth_Keller_JC2": None,
        },
        "remaining_blocker": "No exact D43 rows have been built by v2; "
                             "AWS launch remains prohibited until a fresh "
                             "different-agent hostile PASS and immutable "
                             "idle-host registration.",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    report = run()
    if args.json:
        print(json.dumps(report, indent=1, sort_keys=True))
    else:
        print("D43 EXACT A00PP SOURCE PREFLIGHT V2: PASS; no AWS launch; "
              "no exact D43 emission or solve performed")


if __name__ == "__main__":
    main()
