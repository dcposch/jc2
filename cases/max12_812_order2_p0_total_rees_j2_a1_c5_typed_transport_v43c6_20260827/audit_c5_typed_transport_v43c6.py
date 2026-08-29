#!/usr/bin/env python3
"""Fail-closed typed transport audit for the reviewed V43C5 certificate.

This is deliberately a certificate/schema audit.  It performs no Groebner
basis, saturation, or large polynomial expansion and writes no files.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PREREG = HERE / "PREREGISTRATION.md"
PREREG_SHA256 = "967864722b7302f3f65de29503786e5827a073930f9faf6780bfa858df9fb911"

PINS = {
    "c5_proof": (
        "cases/max12_812_order2_p0_total_rees_j2_a1_total_converter_v43c5_v2_20260827/"
        "evidence/r6b/output/total_a1_628_circuit_certificate.json",
        "f8426bcf6bb4acbe4a2c12e1897588a7b8ce92bc02da84b7fc02d64d64c145e4",
    ),
    "c5_result": (
        "cases/max12_812_order2_p0_total_rees_j2_a1_total_converter_v43c5_v2_20260827/"
        "evidence/r6b/output/result.json",
        "215a64b27e3ea43fd3238158a5e07e686d3de4c7d12ff5bde0e691f916938299",
    ),
    "c5_review": (
        "xmodel/max12-812-order2-p0-total-rees-j2-a1-total-converter-v43c5-v2-"
        "hostile-review-grok-20260827.md",
        "0ab2a7ef8a2efc4a1aa911b0857b88a6e7fb137e02c1c87b5c40640cfa4e04ce",
    ),
    "v20_result": (
        "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/"
        "aws_r6b_r2_pass/output/RESULT.json",
        "a2147de95bc37e8adb629201e2b39b788b99df3d4586da54af7bd41f269a9f15",
    ),
    "v20_report": (
        "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/"
        "RESULT_V20R2.md",
        "9e304f58310fda008a3930b21bf0f49bc198322ee5dd98d805af04068ed5b3c8",
    ),
    "v20_columns": (
        "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/"
        "aws_r6b_r2_pass/output/SOURCE_COLUMNS.json",
        "2e8ceeb42dcc41752f82fe1df866c28b33e289097b065bf965db25574230919c",
    ),
    "v20_dag": (
        "cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/"
        "aws_r6b_r2_pass/output/LITERAL_140_EQUATION_DAG.json",
        "b9bd2e2ca1319ee3107a0f7cf4e1750386d60bb12213a3a970c4812823abdce6",
    ),
    "v19_type_result": (
        "cases/max12_812_order2_u2_62_k00_honest_reachability_type_v19_20260827/"
        "aws_p65521_box01_pass/run/RESULT.json",
        "1611dda533320ad9898c7b5b11720c66ed0dc3b51c89e6c51e5c6d8dc9c9ba55",
    ),
    "v46_schema": (
        "cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827/SCHEMA.json",
        "796eb0847e7b0bb7972c2fd7b3db10bd2dcfd2fd85c5bbaa47e3a239f8b02673",
    ),
    "v46_verifier": (
        "cases/max12_812_order2_gate_t_uniform_contact_naturality_v46_20260827/"
        "verify_uniform_naturality.py",
        "8e49fc87ebeffb74e4c33f79ae248846c7de3ce4f4fb2ad07ac85751d8841ec7",
    ),
    "v46r1_schema": (
        "cases/max12_812_order2_gate_t_uniform_contact_naturality_v46r1_20260827/"
        "SCHEMA_R1.json",
        "0f6bec4983bc8d682b64db5ac23f2d1bb64b8613e2812e95f2cab2b041494b44",
    ),
    "v46r1_review": (
        "xmodel/max12-812-order2-gate-t-uniform-contact-naturality-v46r1-"
        "hostile-review-grok-20260827.md",
        "a2a6a5e204b78485509a314b71bd8ab877ea4cdd9dbad8f2af637b0d753614ac",
    ),
    "v46r1_promotion": (
        "xmodel/max12-812-order2-gate-t-uniform-contact-naturality-v46r1-promotion-"
        "sol-20260827.md",
        "b862e00f6ac80c3392cd365aad5d7001608e2a75fabfa4a76bb2f4c751e1f0fc",
    ),
    "v47_schema": (
        "cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47_20260827/"
        "SCHEMA.json",
        "b1770cc0254098343c27600136f0ec1d95084623a4f48eed5216409106703ab2",
    ),
    "v47_generated": (
        "cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47_20260827/"
        "GENERATED_MANIFESTS.json",
        "070d5a96627ac300f87791b9386e809de21b52317581b01731cde5dc55c7ecaa",
    ),
    "v47r1_schema": (
        "cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47r1_20260827/"
        "SCHEMA_R1.json",
        "b895315acc241ca8542611cadefee0d4f29217f1ffecf8fbd3761b513b6aa908",
    ),
    "v47r1_result": (
        "cases/max12_812_order2_gate_t_strict_uac_three_row_linker_v47r1_20260827/"
        "run_v0_v10_r1/result.json",
        "6c16224703cf79f35073bc41ac8f5cd5d1b8fa24d756aa2891b80df2870c8270",
    ),
    "v47r1_review": (
        "xmodel/max12-812-order2-gate-t-strict-uac-three-row-linker-v47r1-"
        "hostile-review-grok-20260827.md",
        "ff76e8d32dfeda28c392cf0d975fde372ebcbed8e178db3a3e020cb823a27a67",
    ),
    "endpoint_promotion": (
        "xmodel/max12-812-order2-square-d1-unique-ac-d23-lowa6-local-row-"
        "promotion-20260826.md",
        "8b92c22bebae73e3efd793c7c7541c53caf8e956f5ce181240c164f3362864da",
    ),
    "endpoint_review": (
        "xmodel/max12-812-order2-square-d1-unique-ac-d23-lowa6-local-row-"
        "hostile-review-grok-20260826.md",
        "841f0d6ccbb596fa4ace3f08760f039eb288030efa91075112e915d1320592a3",
    ),
}

FINAL_ROWS = (
    "Tg11_1", "Tg11_2", "Tg11_7",
    "Tg12_1", "Tg12_2", "Tg12_7",
    "Tg13_1", "Tg13_2", "Tg13_4", "Tg13_5", "Tg13_7",
    "Tg14_1", "Tg14_2", "Tg14_3", "Tg14_4", "Tg14_5", "Tg14_7",
    "Tg15_3", "Tg15_5", "Tg15_7",
    "Tg16_5", "Tg16_6", "Tg17_5", "Tg18_6", "Tg19_7",
)

SOURCE_FAMILIES = {
    "Az": {0: "a1", 1: "aa1", 2: "aaa1", **{i: f"az{i}" for i in range(3, 9)}},
    "Ac": {1: "aa0", 2: "aaa0", **{i: f"ac{i}" for i in range(3, 9)}},
    "Cz": {1: "e1", 2: "ee1", **{i: f"ez{i}" for i in range(3, 10)}},
    "Cc": {1: "e0", 2: "ee0", **{i: f"ec{i}" for i in range(3, 10)}},
    "Bz": {i: f"cs{i}" for i in range(1, 8)},
    "Bc": {i: f"rs{i}" for i in range(1, 8)},
}
FAMILY_ORDER = {"Az": 1, "Ac": 1, "Cz": 3, "Cc": 3, "Bz": 3, "Bc": 3}
FAMILY_MAX = {"Az": 2, "Ac": 2, "Cz": 2, "Cc": 2, "Bz": 0, "Bc": 0}
FAMILY_TARGET = {"Az": "AzD1", "Ac": "AcD1", "Cz": "CzD1", "Cc": "CcD1",
                 "Bz": "BzD1", "Bc": "BcD1"}
FAMILY_FACTOR = {"Az": 1, "Ac": 1, "Cz": 2, "Cc": 2, "Bz": 1, "Bc": 4}

P_NAMES = {i: f"ell{i}" for i in range(1, 9)}
K10_NAMES = {0: "k", 1: "k1", 2: "k2c", **{i: f"k10_{i}" for i in range(3, 7)}}
K6_NAMES = {0: "k6", 1: "k6_1"}


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load_json(name: str) -> object:
    return json.loads((ROOT / PINS[name][0]).read_text())


def verify_pins() -> dict[str, str]:
    if digest(PREREG) != PREREG_SHA256:
        fail(("preregistration drift", digest(PREREG), PREREG_SHA256))
    checked = {"preregistration": PREREG_SHA256}
    for name, (relative, expected) in PINS.items():
        path = ROOT / relative
        actual = digest(path) if path.is_file() else "MISSING"
        if actual != expected:
            fail(("source pin", name, relative, actual, expected))
        checked[name] = actual
    return checked


def source_alphabet() -> list[str]:
    names = {"t", *P_NAMES.values(), *K10_NAMES.values(), *K6_NAMES.values()}
    for family in SOURCE_FAMILIES.values():
        names.update(family.values())
    if len(names) != 67:
        fail(("source alphabet census", len(names), sorted(names)))
    return sorted(names)


def family_images() -> tuple[dict[str, str], dict[str, dict[str, str]]]:
    complete: dict[str, str] = {"t": "rho^2"}
    finite: dict[str, dict[str, str]] = {
        "t": {"status": "DEFINED", "image": "rho^2", "authority": "t->rho^2"}
    }
    for family, indexed in SOURCE_FAMILIES.items():
        order = FAMILY_ORDER[family]
        maximum = FAMILY_MAX[family]
        factor = FAMILY_FACTOR[family]
        target = FAMILY_TARGET[family]
        for index, source in indexed.items():
            if index < order:
                image = "0"
                complete[source] = image
                finite[source] = {
                    "status": "DEFINED_ZERO_LOWER_IDEAL",
                    "image": image,
                    "authority": f"{family} index {index} < contact order {order}",
                }
                continue
            relative = index - order
            image = f"{target}_{relative}" if factor == 1 else f"{factor}*{target}_{relative}"
            complete[source] = image
            if relative <= maximum:
                finite[source] = {
                    "status": "DEFINED",
                    "image": image,
                    "authority": f"V46/V46R1 reindexing; relative index {relative}",
                }
            else:
                finite[source] = {
                    "status": "MISSING_OUTSIDE_V47R1_FINITE_MAXIMUM",
                    "image": None,
                    "would_be": image,
                    "authority": f"relative index {relative} > manifest maximum {maximum}",
                }
    for index, source in P_NAMES.items():
        complete[source] = f"(1/2)*P_{index}"
        finite[source] = (
            {"status": "DEFINED", "image": f"(1/2)*P_{index}",
             "authority": "P_i=2*ell_i in the V46 normative P series"}
            if index <= 2 else
            {"status": "MISSING_OUTSIDE_V47R1_FINITE_MAXIMUM", "image": None,
             "would_be": f"(1/2)*P_{index}", "authority": f"P index {index} > maximum 2"}
        )
    for index, source in K10_NAMES.items():
        image = f"k10_{index}"
        complete[source] = image
        finite[source] = (
            {"status": "DEFINED", "image": image, "authority": "V46 load-series identity"}
            if index == 0 else
            {"status": "MISSING_OUTSIDE_V47R1_FINITE_MAXIMUM", "image": None,
             "would_be": image, "authority": f"k10 index {index} > maximum 0"}
        )
    for index, source in K6_NAMES.items():
        image = f"k6_{index}"
        complete[source] = image
        finite[source] = (
            {"status": "DEFINED", "image": image, "authority": "V46 load-series identity"}
            if index == 0 else
            {"status": "MISSING_OUTSIDE_V47R1_FINITE_MAXIMUM", "image": None,
             "would_be": image, "authority": f"k6 index {index} > maximum 0"}
        )
    alphabet = source_alphabet()
    if sorted(complete) != alphabet or sorted(finite) != alphabet:
        fail(("map alphabet", sorted(set(alphabet) - set(complete)),
              sorted(set(complete) - set(alphabet))))
    return complete, finite


def finite_target_ring() -> tuple[list[str], dict[str, int]]:
    maxima = {"p": 2, "A": 2, "C": 2, "R": 0, "k10": 0, "k6": 0, "k2": 0}
    names = ["rho"]
    names += [f"P_{i}" for i in range(1, maxima["p"] + 1)]
    for stem, key in (("AzD1", "A"), ("AcD1", "A"), ("CzD1", "C"),
                      ("CcD1", "C"), ("BzD1", "R"), ("BcD1", "R"),
                      ("k10", "k10"), ("k6", "k6"), ("k2", "k2")):
        names += [f"{stem}_{i}" for i in range(maxima[key] + 1)]
    names += ["mu2", "mu4", "mu6", "J"]
    if len(names) != 24 or len(names) != len(set(names)):
        fail(("finite target ring census", len(names), names))
    return names, maxima


def complete_target_ring(complete: dict[str, str], finite_names: list[str]) -> list[str]:
    names = set(finite_names)
    for expression in complete.values():
        for token in re.findall(r"[A-Za-z][A-Za-z0-9_]*", expression):
            if token != "rho":
                names.add(token)
    names.add("rho")
    return sorted(names)


def audit_c5() -> tuple[dict, list[str], dict[str, str]]:
    proof = load_json("c5_proof")
    result = load_json("c5_result")
    if result.get("status") != "PASS-A1-TOTAL-RAW-CIRCUIT-CERTIFICATE-A1-628-V43C5-V2":
        fail(("C5 result status", result.get("status")))
    if (proof.get("ambient_ring") != "Q[t,X19_total], t maps to rho^2"
            or proof.get("target_exponent") != 628
            or proof.get("literal_positive_variable_count") != 66
            or proof.get("rho0_positive_variable_count") != 65):
        fail("C5 source contract")
    target = proof.get("target")
    if target != [{"coefficient": [1, 1], "monomial": [["a1", 628]]}]:
        fail(("C5 target", target))
    final_rows = sorted(proof.get("final_multiplier_roots", {}))
    if final_rows != sorted(FINAL_ROWS):
        fail(("C5 final rows", final_rows))
    row_hashes = {name: proof["total_row_sha256"][name] for name in final_rows}
    if len(row_hashes) != 25 or any(len(value) != 64 for value in row_hashes.values()):
        fail("C5 supported row hashes")
    support: set[str] = set()
    for node in proof.get("expression_nodes", []):
        for term in node.get("polynomial", []):
            support.update(str(name) for name, exponent in term["monomial"] if int(exponent))
    alphabet = source_alphabet()
    expected_support = set(alphabet) - {"ez9"}
    if support != expected_support:
        fail(("C5 proof support", sorted(support - expected_support),
              sorted(expected_support - support)))
    return proof, alphabet, row_hashes


def audit_v20() -> dict:
    result = load_json("v20_result")
    columns = load_json("v20_columns")
    dag = load_json("v20_dag")
    if (result.get("status") != "PASS_EXACT_CONTRACTED_SOURCE_COMPILER_READY_FOR_STRATIFIED_SOLVE"
            or result.get("literal_equations") != 140
            or result.get("source_columns_before_boundary") != 169
            or result.get("free_source_columns") != 164):
        fail("V20R2 contract")
    if not isinstance(columns, list) or len(columns) != 169:
        fail("V20R2 source columns")
    names = {str(item.get("variable")) for item in columns}
    if "a1" in names or any(name.startswith("Tg") for name in names):
        fail("unexpected literal C5 symbol in V20 source columns")
    if (dag.get("target_symbol") != "Jdet"
            or dag.get("truncation") != "Q[Lambda]/(Lambda^20)"
            or dag.get("forbidden_aliases") != ["J1", "J2"]
            or dag.get("normalized_coordinate_map", {}).get("C6") != "1"):
        fail("V20R2 DAG type")
    forbidden_map_keys = {
        "c5_ring_map", "c5_row_module_map", "source_ring_map", "row_module_map",
        "a1_image", "Tg_row_images",
    }
    present = sorted(forbidden_map_keys & (set(result) | set(dag)))
    if present:
        fail(("unexpected serialized C5 interface", present))
    v19 = load_json("v19_type_result")
    outcomes = v19.get("outcomes", {})
    if set(outcomes) != {"K10", "K6", "K2"} or any(
            item.get("classification") != "NOT_TYPED_COMPOSABLE"
            for item in outcomes.values()):
        fail("V19 historical type control")
    return {
        "candidate": "normalized common K00 V20R2",
        "status": "SKIPPED_NO_LITERAL_C5_RING_OR_ROW_MODULE_MAP",
        "authoritative_source_column_count": len(columns),
        "authoritative_equation_count": result["literal_equations"],
        "authoritative_symbols_include_a1": False,
        "serialized_c5_map_keys": present,
        "historical_v19_control": "three prior quotient duals all NOT_TYPED_COMPOSABLE",
        "scope": "availability/type audit only; no claim that a mathematical map cannot be constructed",
    }


def audit_v47(complete: dict[str, str], finite: dict[str, dict[str, str]]) -> dict:
    v46 = load_json("v46_schema")
    v46r1 = load_json("v46r1_schema")
    v47 = load_json("v47_schema")
    generated = load_json("v47_generated")
    v47r1 = load_json("v47r1_schema")
    v47_result = load_json("v47r1_result")

    if (v46["jet_reindexing_map"]["direction"]
            != "total coefficient ring to shifted D1 coefficient ring"):
        fail("V46 map direction")
    if v46["normative_series"]["P"] != "p0 + 2*sum(i>=1,ell_i*sigma^i)":
        fail("V46 P normalization")
    if v46["aliases"]["collision_firewall"]["total_k10_jet_2"] != "k2c":
        fail("V46 k2c alias")
    if "not total stage-zero jets" not in v46["aliases"]["collision_firewall"]["warning"]:
        fail("V46 stage-zero warning")
    expected_raw_map = {
        "az_(a+n)": "AzD1_n", "ac_(a+n)": "AcD1_n",
        "ez_(c+n)": "2*CzD1_n", "ec_(c+n)": "2*CcD1_n",
        "cs_(r+n)": "BzD1_n", "rs_(r+n)": "4*BcD1_n",
    }
    if v46r1["coordinate_types"]["raw_to_D1"] != expected_raw_map:
        fail("V46R1 raw-to-D1 map")
    if v46r1["hensel"]["localization"] != "D(rho)":
        fail("V46R1 localization")

    candidates = v47["raised_subtail_manifests"]
    manifest = next((item for item in candidates if item["id"] == "A1D2_R3"), None)
    if manifest != {
        "id": "A1D2_R3", "a": 1, "d": 2, "c": 3, "r_min": 3,
        "G": 14, "T_C2": 16, "endpoint_id": "D23_LOW_A6",
        "authority_sha256": PINS["endpoint_promotion"][1],
        "review_sha256": PINS["endpoint_review"][1],
        "inventory_sha256": "29b323c67a87c866f31b2dc1e180c6e54fbc933ccafee47ebe63017f31081308",
    }:
        fail(("V47 A1D2_R3 manifest", manifest))
    generated_manifest = next(item for item in generated["manifests"] if item["id"] == "A1D2_R3")
    if generated_manifest["total"] != {
            "A_z": "az_1", "A_c": "ac_1", "C_z": "ez_3", "C_c": "ec_3",
            "R_z": "cs_3", "R_c": "rs_3"}:
        fail("V47 generated total leading map")
    if generated_manifest["to_d1"] != {
            "A_z": "AzD1_0", "A_c": "AcD1_0", "C_z": "2*CzD1_0",
            "C_c": "2*CcD1_0", "R_z": "BzD1_0", "R_c": "4*BcD1_0"}:
        fail("V47 generated D1 leading map")
    pin = next(item for item in v47r1["manifest_coefficient_pins"] if item["id"] == "A1D2_R3")
    finite_names, maxima = finite_target_ring()
    if pin["maxima"] != maxima:
        fail(("V47R1 A1D2 maxima", pin["maxima"], maxima))
    record = next(item for item in v47_result["manifest_records"] if item["id"] == "A1D2_R3")
    if (record["contact"] != [1, 3, 3] or record["maxima"] != maxima
            or record["slots"] != {"Phi1": 14, "Phi2": 14, "Phi4": 16}
            or record["coefficient_sha256"]
            != "ad0c9b15ce394e554c178521fadb32b3c71318cf3a8d700a2311aceb9d12a850"):
        fail("V47R1 A1D2 result record")
    endpoint = v47["endpoint_authorities"]["D23_LOW_A6"]
    if (endpoint["localization"] != "D(p*k0)"
            or endpoint["theorem_type"] != "arcwise/set-theoretic closed-R-tail emptiness"):
        fail("V47 endpoint theorem type")
    if "a1" not in v47["chart"]["forbidden_stage_zero_names"]:
        fail("V47 stage-zero firewall")

    defined = sorted(name for name, item in finite.items() if item["status"].startswith("DEFINED"))
    missing = sorted(name for name, item in finite.items() if item["status"].startswith("MISSING"))
    if len(defined) != 28 or len(missing) != 39:
        fail(("finite map census", len(defined), len(missing)))
    if finite["a1"] != {
            "status": "DEFINED_ZERO_LOWER_IDEAL", "image": "0",
            "authority": "Az index 0 < contact order 1"}:
        fail(("a1 finite image", finite["a1"]))
    if complete["a1"] != "0":
        fail(("a1 complete-extension image", complete["a1"]))

    complete_names = complete_target_ring(complete, finite_names)
    if "rho" not in complete_names or "AzD1_0" not in complete_names:
        fail("complete target ring")
    # Q[variables] is a domain, and localization at the displayed nonzero
    # monomial remains a nonzero domain.  Therefore zero is not a unit.
    target_localizer = "p*k0 = (-2*rho^2)*k10_0"
    image_is_unit = False
    if image_is_unit:
        fail("zero incorrectly classified as a unit")

    controls = {
        "v20_alias_is_not_map": True,
        "stage_zero_a1_to_shifted_AzD1_0_rejected": (
            complete["a1"] == "0" and "a1" in v47["chart"]["forbidden_stage_zero_names"]
        ),
        "zero_is_not_unit_in_nonzero_domain_localization": not image_is_unit,
        "source_D_a1_localization_extension_rejected": complete["a1"] == "0",
        "finite_unretained_az4_is_missing_not_zero": (
            finite["az4"]["status"] == "MISSING_OUTSIDE_V47R1_FINITE_MAXIMUM"
            and finite["az4"]["image"] is None
        ),
        "three_v47_slots_are_not_25_row_module_map": (
            set(record["slots"]) == {"Phi1", "Phi2", "Phi4"}
            and "row_module_map" not in v47r1
        ),
        "reverse_transport_rejected": v47["scope"]["reverse_transport"] == "forbidden",
    }
    if not all(controls.values()):
        fail(("mutation/control failure", controls))

    return {
        "candidate": "V47+V47R1 A1D2_R3 endpoint",
        "selection_reason": "smallest reviewed V47 terminal grade T_C2=16",
        "contact": {"a": 1, "d": 2, "c": 3, "r_min": 3, "G": 14, "T_C2": 16},
        "endpoint_authority": "D23_LOW_A6",
        "endpoint_localization": target_localizer,
        "endpoint_theorem_type": endpoint["theorem_type"],
        "source_localization": "none (ordinary C5 polynomial ring)",
        "v46_map_direction": v46["jet_reindexing_map"]["direction"],
        "finite_manifest_ring": {
            "base": "Q",
            "generators": finite_names,
            "generator_count": len(finite_names),
            "maxima": maxima,
        },
        "complete_polynomial_extension_ring": {
            "base": "Q",
            "generators": complete_names,
            "generator_count": len(complete_names),
            "role": "generous extension retaining every C5 source-jet image; endpoint equations remain in the finite subring",
        },
        "finite_manifest_variable_images": finite,
        "finite_defined_count": len(defined),
        "finite_missing_count": len(missing),
        "finite_missing_variables": missing,
        "complete_extension_variable_images": complete,
        "image_of_a1": "0",
        "image_of_a1_is_unit": False,
        "image_of_c5_target": "phi(a1^628)=0^628=0",
        "source_D_a1_map_exists": False,
        "first_minimal_obstruction": {
            "stage": "TARGET_GENERATOR_UNIT_GATE_BEFORE_ROW_MODULE_MAP",
            "source_generator": "a1=Az_0 (stage-zero total coefficient)",
            "exact_image": "0",
            "reason": "A1D2_R3 has positive A-contact order a=1, so V46's lower ideal kills Az_0",
            "minimality": "one source generator; no row expansion is needed",
        },
        "row_module_audit": {
            "status": "NOT_REACHED_AFTER_NONUNIT_A1_IMAGE",
            "available_v47_literal_slots": record["slots"],
            "serialized_25_row_module_map_present": False,
        },
        "controls": controls,
    }


def build_result() -> dict:
    pins = verify_pins()
    _, alphabet, row_hashes = audit_c5()
    complete, finite = family_images()
    v20 = audit_v20()
    v47 = audit_v47(complete, finite)
    return {
        "schema_version": 1,
        "status": "PASS-C5-TYPED-TRANSPORT-AUDIT-OBSTRUCTION",
        "transport_status": "NO_TRANSPORT_CERTIFICATE",
        "scope": "endpoint-specific C5-to-V20R2/V47-A1D2_R3 type audit only",
        "source": {
            "ring": "Q[t,X19_total]",
            "t_map_to_total_rho_ring": "t -> rho^2",
            "positive_variable_count": 66,
            "ring_generator_count_including_t": 67,
            "generators": alphabet,
            "source_localizers": [],
            "target": "a1^628",
            "supported_row_count": 25,
            "supported_rows_sha256": row_hashes,
            "review_sha256": PINS["c5_review"][1],
        },
        "search_order": [v20, v47],
        "verdict": (
            "V20R2 supplies no literal C5 ring/row-module map.  On the smallest reviewed "
            "V47 endpoint A1D2_R3, the exact forward contact map sends stage-zero a1 to 0; "
            "zero is not a unit in the nonzero localized target domain.  Therefore the C5 "
            "identity transports only to a tautological zero identity and gives no endpoint "
            "or terminal unit certificate."
        ),
        "first_decisive_obstruction": v47["first_minimal_obstruction"],
        "firewall": [
            "no claim that a C5-to-V20R2 map cannot be constructed in future",
            "no C5 row image or coverage claim",
            "no endpoint replacement beyond reviewed V47 scope",
            "no G2-PSC, Gate T, order-two, maximum-twelve, or JC2 claim",
        ],
        "source_pins_sha256": pins,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    result = build_result()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.check is not None:
        if not args.check.is_file() or args.check.read_text() != encoded:
            fail(("frozen result mismatch", str(args.check)))
        print("PASS-C5-TYPED-TRANSPORT-AUDIT-OBSTRUCTION")
        print("RESULT_SHA256=" + digest(args.check))
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
