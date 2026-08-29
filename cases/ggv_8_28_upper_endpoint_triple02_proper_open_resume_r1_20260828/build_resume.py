#!/usr/bin/env python3
"""Build the exact TRIPLE02 node-1 chart from an archived proper-open basis."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys


FROZEN_R5_SHA256 = "d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90"
FROZEN_ARCHIVE_SHA256 = "e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1"
PREFIX_STDOUT_SHA256 = "4ee63095327d80572764eb3783d0e77c7a6cf385f47cf93c1cafcea843b29418"
OPEN_BASIS_SHA256 = "e2d240e369e516ad8e3fb3ac221061abe465a241ce91ceeef96a4e7c0947493c"
OPEN_BASIS_TEXT = (
    "9*q0-80,159432300*q2^4*c6+20503125*q2^4-391820820480*q2^2*c6^2"
    "+75582720000*q2^2*c6+240734712102912*c6^3-3240000000*q2^2"
    "-61917364224000*c6^2+995328000000*c6+128000000000"
)
EXPECTED_GENERATOR_SHA256 = (
    "2b9d29b706ce5d7e58e2dc5a28799782f5610c5ccb7b71987ebd694fd8b83206",
    "fecd1d43f3f55e1c65bec858303b7688c0db83dbe9c3a60f51f70130a4149336",
)
EXPECTED_FILES = {
    "output/INPUT_MANIFEST.json":
        "0025f3eafe43b06d8d4cdd7b99870a52b7da331e8985baf7dd3de09a6e48257e",
    "output/node_001/NODE_INPUT.json":
        "b8bf5ec7f09f53211b00d5aafcee0d5b1b45c997c254437a3edb0f647376f68f",
    "output/node_001/NODE_001_STANDARD_BASIS.txt":
        "bd95508c3d0441d18d2538810e2c40ac85ccd5da57f09a560d2d9a93a483640d",
    "output/node_001/reduce.sing":
        "28385a7044bf6b3a2d79c42738860039b687f32f13d5a43c0e67c50b247af609",
    "output/node_001/NODE_001_REDUCE_PIVOTS.tsv":
        "2edaa006dae3f63e90973d40de5c7cdda00437570283429c69b353023645e7fc",
    "output/node_001/NODE_001_REDUCE_RESIDUAL.tsv":
        "f24a4a23aa99d2864c468cce73d7a3affbb7f7baa7344af29a86060dad1a0bfb",
    "output/node_001/NODE_001_SIZE_6_WITNESS.tsv":
        "fa0428864a2e15b65b89c0fee2c8f91a557571b0c2c7502f1c9230a6f88d8632",
    "output/node_001/NODE_001_SIZE_6_MINORS.tsv":
        "1c6e57a4551de1f97f31444b771c8b7255b1e270fa1f4fbcd5198795bef07b86",
    "output/node_001/rank_size_6.support.json":
        "bb8f7ee0faabbdb8e40be15bd4d6b3df319acbb5d6d6df7643954a65503d8c51",
    "output/node_001/saturation.sing":
        "196cb1205291c8cae0e047adf2a759cfa798fbda5a78ceefd9c18b7ec7a5f670",
    "output/node_001/saturation.result.json":
        "4bac13693064e6a1ae16963b4cc3fd9ff5044641e3352e491c2f99b1be4851f5",
    "output/node_001/saturation.stdout.txt": PREFIX_STDOUT_SHA256,
    "output/node_001/saturation.stderr.txt":
        "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "output/node_001/NODE_001_OPEN_SAT_STANDARD_BASIS.txt": OPEN_BASIS_SHA256,
}

REQUIRED_SCRIPT_TOKENS = (
    "ARCHIVED_SATURATION_PREFIX_BOUND=1",
    "ARCHIVED_SATURATION_STABILITY_FAILURES=0",
    "ARCHIVED_SATURATION_RESULT_USED_AS_PROVENANCE_ONLY=1",
    "RESUME_NODE_INCLUSION_FAILURES=",
    "RESUME_OPEN_BASIS_REPLAY_FAILURES=",
    "RESUME_CANDIDATE_STABILITY_FAILURES=",
    "RESUME_STABILITY_SLOT1_TYPE=",
    "RESUME_ACTIVE_UNIT_NF_NONZERO=",
    "RESUME_DELTA_NF_NONZERO=",
    "REVERSE_CONTAINMENT_BASIS_GENERATOR_COUNT=",
    "REVERSE_CONTAINMENT_WITNESS_FOUND_COUNT=",
    "REVERSE_CONTAINMENT_MEMBERSHIP_REDUCTION_COUNT=",
    "REVERSE_CONTAINMENT_SEARCH_BOUND=64",
    "SELF_CONTAINED_TWO_CONTAINMENT_SATURATION_CERTIFICATE=1",
    "PROPER_OPEN_IDEAL_CERTIFICATE=1",
    "NODE_SATURATION_RECOMPUTATION_ENTERED=0",
    "CANDIDATE_STABILITY_SATURATION_ENTERED=1",
    "PURE_DELTA_POWER_SEARCH_ENTERED=0",
    "CLOSED_SUCCESSOR_ENTERED=0",
    "PROPER_OPEN_ROUTING_PASS=1",
    "RING_ORDER=Q[q0,q2,c4,c6]_dp",
    "C4_SOURCE_TOKEN_CENSUS=30",
    "INHERITED_RANK_UPPER_BOUND=6",
    "INHERITED_RANK_CERTIFICATE_BOUND=1",
    "SELECTED_MINOR_ROWS=1,2,4,7,9,11",
    "SELECTED_MINOR_COLS=1,2,3,5,6,7",
    "SELECTED_MINOR_LITERAL_SHA256=84b4c2c4c0bfe5aa7414c35813cc1cf63d7d5416358a394b8e8bdc35820f1d02",
    "CHART_PIVOT_REDUCER=NODE_SB",
    "CHART_BASE_CHANGE_REDUCTION_COUNT=",
    "RESIDUAL_BASE_CHANGE_ENTRY_COUNT=",
    "RIGHT_TRANSFORM_ENTRY_COUNT=",
    "RIGHT_TRANSFORM_RECORDED_ENTRY_COUNT=",
    "FULL_RIGHT_TRANSFORM_RECONSTRUCTED=1",
    "NODE_TRANSFORM_BASE_CHANGED_TO_ACTIVE_SB=1",
    "NF_RATIONAL_UNIT_PIVOT_COUNT=",
    "ADJUGATE_KERNEL_VECTOR_COUNT=",
    "BORDERED_IDENTITY_FAILURES=",
    "FULL_106_ROW_KERNEL_REPLAY_FAILURES=",
    "LIFTED_KERNEL_ENTRY_COUNT=",
    "BORDERED_NONZERO_PLANT_NF_NONZERO=",
    "BORDERED_NONZERO_PLANT_EQUALS_DELTA=",
    "ENDPOINT_PLUS_ONE_PLANT_NF_NONZERO=",
    "ENDPOINT_PLUS_ONE_PLANT_AFFINE_REPLAY=",
    "ENDPOINT_PLUS_TWO_PLANT_NF_NONZERO=",
    "ENDPOINT_PLUS_TWO_PLANT_AFFINE_REPLAY=",
    "ENDPOINT_TWO_SHIFT_AT_LEAST_ONE_NONZERO=",
    "ENDPOINT_QUADRATIC=x14*x72+x1*x97",
    "ENDPOINT_DELTA2_DENOMINATOR_CLEARED=1",
    "NO_FACTOR_GCD_CONTENT_RADICAL_NORMALIZATION=1",
    "RECURSIVE_ENDPOINT_CHART_COMPLETE=1",
)
FORBIDDEN_PRODUCTION_TOKENS = (
    "sat(NODE_IDEAL",
    "OPEN_SAT_RESULT=sat(NODE_IDEAL",
    "EMPTY_CERT_POWER",
    "for(ek=",
    "NEXT_IDEAL=",
    "NEXT_SB=",
    "OPEN_CHART_EMPTY=",
    "REDUCER_PLACEHOLDER",
    "PLACEHOLDER",
    "TODO",
)

RING_DECLARATION = "ring ambient=0,(q0,q2,c4,c6),dp;"
EXPECTED_DELTA_SHA256 = "84b4c2c4c0bfe5aa7414c35813cc1cf63d7d5416358a394b8e8bdc35820f1d02"
ENDPOINT_CROSS_EXPRESSION = (
    "K[14,i]*K[72,j]+K[14,j]*K[72,i]+K[1,i]*K[97,j]+K[1,j]*K[97,i]")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def clean_ideal(text: str) -> str:
    value = "".join(text.split())
    if not value or any(token in value for token in (";", "|", '"', "'")):
        raise SystemExit("UNSAFE_OR_EMPTY_IDEAL_TEXT")
    return value


def load_r5(path: Path):
    if sha256(path) != FROZEN_R5_SHA256:
        raise SystemExit("FROZEN_R5_SOURCE_SHA_DRIFT")
    sys.path.insert(0, str(path.parent))
    try:
        spec = importlib.util.spec_from_file_location("frozen_r5_recursor", path)
        if spec is None or spec.loader is None:
            raise SystemExit("FROZEN_R5_IMPORT_FAILURE")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.pop(0)


def validate_script(script: str) -> None:
    present = [token for token in FORBIDDEN_PRODUCTION_TOKENS if token in script]
    if present:
        raise RuntimeError("FORBIDDEN_PROPER_OPEN_ROUTE_TOKEN:" + ",".join(present))
    missing = [token for token in REQUIRED_SCRIPT_TOKENS if script.count(token) != 1]
    if missing:
        raise RuntimeError("REQUIRED_RESUME_TOKEN_CENSUS:" + ",".join(missing))
    if script.count(PREFIX_STDOUT_SHA256) != 1:
        raise RuntimeError("ARCHIVED_PREFIX_HASH_BINDING_CENSUS")
    if script.count(OPEN_BASIS_TEXT) != 1:
        raise RuntimeError("ARCHIVED_OPEN_BASIS_LITERAL_CENSUS")
    open_matches = re.findall(r"^ideal ARCHIVED_OPEN_LITERAL=(.+);$", script,
                              flags=re.MULTILINE)
    if len(open_matches) != 1 or open_matches[0] != OPEN_BASIS_TEXT:
        raise RuntimeError("ARCHIVED_OPEN_BASIS_LITERAL_OR_HASH_DRIFT")
    if script.count(RING_DECLARATION) != 1:
        raise RuntimeError("RING_DECLARATION_OR_ORDER_CENSUS")
    if len(re.findall(r"\bc4\b", script)) != 31:
        raise RuntimeError("C4_SOURCE_TOKEN_CENSUS_DRIFT")
    delta_matches = re.findall(r"^poly SCANNED_DELTA_NODE=(.+);$", script,
                               flags=re.MULTILINE)
    if (len(delta_matches) != 1
            or hashlib.sha256(delta_matches[0].encode()).hexdigest()
            != EXPECTED_DELTA_SHA256):
        raise RuntimeError("SELECTED_DELTA_LITERAL_OR_HASH_DRIFT")
    if script.count("sat(ACTIVE_SB,RESUME_DELTA_IDEAL)") != 1:
        raise RuntimeError("CANDIDATE_STABILITY_SATURATION_CENSUS")
    if "PURE_DELTA_POWER_SEARCH_ENTERED=1" in script:
        raise RuntimeError("PROPER_PATH_CAN_ENTER_PURE_DELTA_POWER_SEARCH")
    if "CLOSED_SUCCESSOR_ENTERED=1" in script:
        raise RuntimeError("PROPER_PATH_CAN_ENTER_CLOSED_SUCCESSOR")
    transform_marker = "NODE_TRANSFORM_BASE_CHANGED_TO_ACTIVE_SB=1"
    if script.count(transform_marker) != 1 or "while(step" in script.split(
            transform_marker, 1)[1]:
        raise RuntimeError("POST_BASE_CHANGE_REPIVOT_OR_MARKER_DRIFT")
    if script.count(ENDPOINT_CROSS_EXPRESSION) != 1:
        raise RuntimeError("ENDPOINT_CROSS_TERM_CENSUS")
    literal_gates = (
        "base_change_reductions!=11135",
        "residual_base_change_entry_count!=110",
        "transform_entry_count!=11025",
        "transform_recorded_entry_count!=11025",
        "identity_count!=44",
        "kernel_entry_count!=420",
        "full_count!=424",
        "endpoint_count!=10",
        "ncols(Y)!=4",
    )
    if any(script.count(token) != 1 for token in literal_gates):
        raise RuntimeError("EXACT_OPERATION_COUNT_GATE_CENSUS")
    transform_contract = (
        "matrix C[105][105]",
        "for(i=1;i<=105;i=i+1){ C[i,i]=1; }",
        "swap_entry=C[i,step]; C[i,step]=C[i,pj]; C[i,pj]=swap_entry;",
        "C[i,j]=reduce(C[i,j]-multiple*C[i,step],NODE_SB)",
        "C[i,j]=reduce(C[i,j],ACTIVE_SB)",
        "transform_entry_count=transform_entry_count+1",
        "transform_recorded_entry_count=transform_recorded_entry_count+1",
        'write(CTFILE,string(i)+"|"+string(j)+"|"+string(C[i,j]))',
        "CHECK+C[i,95+k]*Y[k,j]",
        "kernel_entry_count=kernel_entry_count+1",
    )
    if any(script.count(token) != 1 for token in transform_contract):
        raise RuntimeError("FULL_RIGHT_TRANSFORM_CONTRACT_CENSUS")
    if script.count("CHART_CLASSIFICATION=ENDPOINT_DEAD_ONLY_ON_D_DELTA") != 1:
        raise RuntimeError("DEAD_CLASSIFICATION_SOURCE_CENSUS")
    if script.count(
            "CHART_CLASSIFICATION=RING_LEVEL_SURVIVOR_ON_CHART_PENDING_NILPOTENCE_RADICAL") != 1:
        raise RuntimeError("SURVIVOR_CLASSIFICATION_SOURCE_CENSUS")


def verify_pivots(path: Path) -> None:
    lines = path.read_text().splitlines()
    if len(lines) != 96 or lines[0] != "step|source_row|source_col|pivot":
        raise SystemExit("ARCHIVED_PIVOT_CENSUS")
    for expected_step, line in enumerate(lines[1:], 1):
        fields = line.split("|", 3)
        if len(fields) != 4 or int(fields[0]) != expected_step:
            raise SystemExit("ARCHIVED_PIVOT_STEP_DISAGREEMENT")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"FROZEN_R5_TAIL_REWRITE_CENSUS:{label}:{text.count(old)}")
    return text.replace(old, new, 1)


def harden_tail(tail: str) -> str:
    tail = replace_once(
        tail,
        "matrix Y[10][4];",
        'matrix Y[10][4]; print("ADJUGATE_KERNEL_VECTOR_COUNT="+string(ncols(Y))); if(ncols(Y)!=4){ print("FATAL_ADJUGATE_KERNEL_VECTOR_CENSUS"); quit; }',
        "kernel-vector-count")
    tail = replace_once(
        tail,
        "int base_change_reductions=0;",
        "int base_change_reductions=0; int residual_base_change_entry_count=0; int transform_entry_count=0; int transform_recorded_entry_count=0;",
        "base-change-counters")
    tail = replace_once(
        tail,
        "for(i=1;i<=11;i=i+1){ for(j=1;j<=10;j=j+1){ R[i,j]=reduce(R[i,j],ACTIVE_SB); base_change_reductions=base_change_reductions+1; } }",
        "for(i=1;i<=11;i=i+1){ for(j=1;j<=10;j=j+1){ R[i,j]=reduce(R[i,j],ACTIVE_SB); base_change_reductions=base_change_reductions+1; residual_base_change_entry_count=residual_base_change_entry_count+1; } }",
        "residual-base-change-count")
    tail = replace_once(
        tail,
        "for(i=1;i<=105;i=i+1){ for(j=1;j<=105;j=j+1){ C[i,j]=reduce(C[i,j],ACTIVE_SB); base_change_reductions=base_change_reductions+1; } }",
        "for(i=1;i<=105;i=i+1){ for(j=1;j<=105;j=j+1){ C[i,j]=reduce(C[i,j],ACTIVE_SB); base_change_reductions=base_change_reductions+1; transform_entry_count=transform_entry_count+1; } }\nstring CTFILE=\"NODE_001_BASE_CHANGED_RIGHT_TRANSFORM.tsv\"; write(CTFILE,\"row|col|normal_form\"); for(i=1;i<=105;i=i+1){ for(j=1;j<=105;j=j+1){ write(CTFILE,string(i)+\"|\"+string(j)+\"|\"+string(C[i,j])); transform_recorded_entry_count=transform_recorded_entry_count+1; } }",
        "transform-base-change-count")
    tail = replace_once(
        tail,
        'print("CHART_BASE_CHANGE_REDUCTION_COUNT="+string(base_change_reductions));\nif(base_change_reductions!=11135){ print("FATAL_CHART_BASE_CHANGE_CENSUS"); quit; }\nprint("NODE_TRANSFORM_BASE_CHANGED_TO_ACTIVE_SB=1");',
        'print("CHART_BASE_CHANGE_REDUCTION_COUNT="+string(base_change_reductions)); print("RESIDUAL_BASE_CHANGE_ENTRY_COUNT="+string(residual_base_change_entry_count)); print("RIGHT_TRANSFORM_ENTRY_COUNT="+string(transform_entry_count)); print("RIGHT_TRANSFORM_RECORDED_ENTRY_COUNT="+string(transform_recorded_entry_count));\nif(base_change_reductions!=11135 || residual_base_change_entry_count!=110 || transform_entry_count!=11025 || transform_recorded_entry_count!=11025){ print("FATAL_CHART_BASE_CHANGE_CENSUS"); quit; }\nprint("FULL_RIGHT_TRANSFORM_RECONSTRUCTED=1"); print("NODE_TRANSFORM_BASE_CHANGED_TO_ACTIVE_SB=1");',
        "base-change-gates")
    tail = replace_once(
        tail,
        "matrix K[105][4];\nfor(i=1;i<=105;i=i+1){ for(j=1;j<=ncols(Y);j=j+1){ CHECK=0; for(k=1;k<=10;k=k+1){ CHECK=reduce(CHECK+C[i,95+k]*Y[k,j],ACTIVE_SB); } K[i,j]=CHECK; } }",
        "matrix K[105][4]; int kernel_entry_count=0;\nfor(i=1;i<=105;i=i+1){ for(j=1;j<=ncols(Y);j=j+1){ CHECK=0; for(k=1;k<=10;k=k+1){ CHECK=reduce(CHECK+C[i,95+k]*Y[k,j],ACTIVE_SB); } K[i,j]=CHECK; kernel_entry_count=kernel_entry_count+1; } }\nprint(\"LIFTED_KERNEL_ENTRY_COUNT=\"+string(kernel_entry_count)); if(kernel_entry_count!=420){ print(\"FATAL_LIFTED_KERNEL_ENTRY_CENSUS\"); quit; }",
        "kernel-entry-count")
    tail = replace_once(
        tail,
        'print("FULL_106_ROW_KERNEL_REPLAY_COUNT="+string(full_count)); print("FULL_106_ROW_KERNEL_REPLAY_FAILURES="+string(full_failures)); if(full_failures!=0){ print("FATAL_FULL_KERNEL_REPLAY"); quit; }',
        'print("FULL_106_ROW_KERNEL_REPLAY_COUNT="+string(full_count)); print("FULL_106_ROW_KERNEL_REPLAY_FAILURES="+string(full_failures)); if(full_count!=424 || full_failures!=0){ print("FATAL_FULL_KERNEL_REPLAY"); quit; }',
        "full-row-count")
    tail = replace_once(
        tail,
        "poly ENDPOINT_PLANT_BASE_RAW=K[14,1]*K[72,1]+K[1,1]*K[97,1]; poly ENDPOINT_PLANT_BASE_NF=reduce(ENDPOINT_PLANT_BASE_RAW,ACTIVE_SB); poly ENDPOINT_PLUS_ONE_PLANT_NF=reduce(ENDPOINT_PLANT_BASE_RAW+1,ACTIVE_SB); poly ENDPOINT_PLANT_AFFINE_FAILURE=reduce(ENDPOINT_PLUS_ONE_PLANT_NF-ENDPOINT_PLANT_BASE_NF-1,ACTIVE_SB);",
        "poly ENDPOINT_PLANT_BASE_RAW=K[14,1]*K[72,1]+K[1,1]*K[97,1]; poly ENDPOINT_PLANT_BASE_NF=reduce(ENDPOINT_PLANT_BASE_RAW,ACTIVE_SB); poly ENDPOINT_PLUS_ONE_PLANT_NF=reduce(ENDPOINT_PLANT_BASE_RAW+1,ACTIVE_SB); poly ENDPOINT_PLUS_TWO_PLANT_NF=reduce(ENDPOINT_PLANT_BASE_RAW+2,ACTIVE_SB); poly ENDPOINT_PLUS_ONE_AFFINE_FAILURE=reduce(ENDPOINT_PLUS_ONE_PLANT_NF-ENDPOINT_PLANT_BASE_NF-1,ACTIVE_SB); poly ENDPOINT_PLUS_TWO_AFFINE_FAILURE=reduce(ENDPOINT_PLUS_TWO_PLANT_NF-ENDPOINT_PLANT_BASE_NF-2,ACTIVE_SB);",
        "endpoint-two-shift-definition")
    tail = replace_once(
        tail,
        'write("NODE_001_ENDPOINT_PLUS_ONE_PLANT.txt","endpoint_nf|"+string(ENDPOINT_PLANT_BASE_NF)+"|plus_one_nf|"+string(ENDPOINT_PLUS_ONE_PLANT_NF)+"|affine_failure|"+string(ENDPOINT_PLANT_AFFINE_FAILURE));',
        'write("NODE_001_ENDPOINT_TWO_SHIFT_PLANT.txt","endpoint_nf|"+string(ENDPOINT_PLANT_BASE_NF)+"|plus_one_nf|"+string(ENDPOINT_PLUS_ONE_PLANT_NF)+"|plus_two_nf|"+string(ENDPOINT_PLUS_TWO_PLANT_NF)+"|plus_one_affine_failure|"+string(ENDPOINT_PLUS_ONE_AFFINE_FAILURE)+"|plus_two_affine_failure|"+string(ENDPOINT_PLUS_TWO_AFFINE_FAILURE));',
        "endpoint-two-shift-artifact")
    tail = replace_once(
        tail,
        'print("ENDPOINT_PLUS_ONE_PLANT_NF_NONZERO="+string(ENDPOINT_PLUS_ONE_PLANT_NF!=0)); print("ENDPOINT_PLUS_ONE_PLANT_AFFINE_REPLAY="+string(ENDPOINT_PLANT_AFFINE_FAILURE==0));',
        'print("ENDPOINT_PLUS_ONE_PLANT_NF_NONZERO="+string(ENDPOINT_PLUS_ONE_PLANT_NF!=0)); print("ENDPOINT_PLUS_ONE_PLANT_AFFINE_REPLAY="+string(ENDPOINT_PLUS_ONE_AFFINE_FAILURE==0)); print("ENDPOINT_PLUS_TWO_PLANT_NF_NONZERO="+string(ENDPOINT_PLUS_TWO_PLANT_NF!=0)); print("ENDPOINT_PLUS_TWO_PLANT_AFFINE_REPLAY="+string(ENDPOINT_PLUS_TWO_AFFINE_FAILURE==0)); print("ENDPOINT_TWO_SHIFT_AT_LEAST_ONE_NONZERO="+string(ENDPOINT_PLUS_ONE_PLANT_NF!=0 || ENDPOINT_PLUS_TWO_PLANT_NF!=0));',
        "endpoint-two-shift-markers")
    tail = replace_once(
        tail,
        'if(ENDPOINT_PLUS_ONE_PLANT_NF==0 || ENDPOINT_PLANT_AFFINE_FAILURE!=0){ print("FATAL_ENDPOINT_PLUS_ONE_PLANT"); quit; }',
        'if(ENDPOINT_PLUS_ONE_AFFINE_FAILURE!=0 || ENDPOINT_PLUS_TWO_AFFINE_FAILURE!=0 || (ENDPOINT_PLUS_ONE_PLANT_NF==0 && ENDPOINT_PLUS_TWO_PLANT_NF==0)){ print("FATAL_ENDPOINT_TWO_SHIFT_PLANT"); quit; }',
        "endpoint-two-shift-gate")
    tail = replace_once(
        tail,
        'print("ENDPOINT_QUADRATIC=x14*x72+x1*x97"); print("ENDPOINT_DELTA2_DENOMINATOR_CLEARED=1"); print("ENDPOINT_COEFFICIENT_COUNT="+string(endpoint_count)); print("ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT="+string(endpoint_nonzero));',
        'print("ENDPOINT_QUADRATIC=x14*x72+x1*x97"); print("ENDPOINT_DELTA2_DENOMINATOR_CLEARED=1"); print("ENDPOINT_COEFFICIENT_COUNT="+string(endpoint_count)); print("ENDPOINT_COEFFICIENT_NF_NONZERO_COUNT="+string(endpoint_nonzero)); if(endpoint_count!=10){ print("FATAL_ENDPOINT_COEFFICIENT_CENSUS"); quit; }',
        "endpoint-count-gate")
    return tail


def build_resume_script(r5, remaining: list[str], generators: list[str],
                        label: str, assignment: str,
                        residual: list[list[str]], rank: int,
                        rows: tuple[int, ...], cols: tuple[int, ...],
                        scanned_delta: str, archived_open_basis: str,
                        rank_archive_sha256: str,
                        rank_member_sha256: str) -> str:
    original = r5.build_chart_script(
        remaining, generators, 1, label, assignment, residual,
        rank, rows, cols, scanned_delta)
    sentinel = 'print("OPEN_CHART_SATURATION_PROPER=1");'
    if original.count(sentinel) != 1:
        raise RuntimeError("FROZEN_R5_CHART_SPLICE_SENTINEL_CENSUS")
    tail = harden_tail(original.split(sentinel, 1)[1].lstrip("\n"))
    lines = ["// Exact TRIPLE02 node-1 proper-open certificate resume."]
    lines += r5.node_header(remaining, generators, 1)
    lines += [
        f"poly SCANNED_DELTA_NODE={scanned_delta};",
        "poly SCANNED_DELTA_NODE_NF=reduce(SCANNED_DELTA_NODE,NODE_SB);",
        'if(SCANNED_DELTA_NODE_NF==0 || SCANNED_DELTA_NODE_NF!=SCANNED_DELTA_NODE){ print("FATAL_RESUME_NODE_DELTA_REPLAY"); quit; }',
        f"ideal ARCHIVED_OPEN_LITERAL={archived_open_basis};",
        "ideal ACTIVE_SB=std(ARCHIVED_OPEN_LITERAL);",
        "poly ACTIVE_UNIT_NF=reduce(1,ACTIVE_SB);",
        "poly DELTA=reduce(SCANNED_DELTA_NODE,ACTIVE_SB);",
        'LIB "elim.lib";',
        "ideal RESUME_DELTA_IDEAL=SCANNED_DELTA_NODE_NF;",
        "list RESUME_STABLE_RESULT=sat(ACTIVE_SB,RESUME_DELTA_IDEAL);",
        'print("RESUME_STABILITY_OBJECT_TYPE="+typeof(RESUME_STABLE_RESULT)); print("RESUME_STABILITY_OBJECT_SIZE="+string(size(RESUME_STABLE_RESULT)));',
        'if(typeof(RESUME_STABLE_RESULT)!="list" || size(RESUME_STABLE_RESULT)!=1 || typeof(RESUME_STABLE_RESULT[1])!="ideal"){ print("FATAL_RESUME_STABILITY_OBJECT"); quit; }',
        'print("RESUME_STABILITY_SLOT1_TYPE="+typeof(RESUME_STABLE_RESULT[1]));',
        "ideal RESUME_STABLE_SB=std(RESUME_STABLE_RESULT[1]);",
        "int si; int resume_node_inclusion_failures=0; int resume_open_basis_replay_failures=0; int resume_candidate_stability_failures=0;",
        "for(si=1;si<=size(NODE_IDEAL);si=si+1){ if(reduce(NODE_IDEAL[si],ACTIVE_SB)!=0){ resume_node_inclusion_failures=resume_node_inclusion_failures+1; } }",
        "for(si=1;si<=size(ARCHIVED_OPEN_LITERAL);si=si+1){ if(reduce(ARCHIVED_OPEN_LITERAL[si],ACTIVE_SB)!=0){ resume_open_basis_replay_failures=resume_open_basis_replay_failures+1; } }",
        "for(si=1;si<=size(ACTIVE_SB);si=si+1){ if(reduce(ACTIVE_SB[si],RESUME_STABLE_SB)!=0){ resume_candidate_stability_failures=resume_candidate_stability_failures+1; } }",
        "for(si=1;si<=size(RESUME_STABLE_SB);si=si+1){ if(reduce(RESUME_STABLE_SB[si],ACTIVE_SB)!=0){ resume_candidate_stability_failures=resume_candidate_stability_failures+1; } }",
        'string REVERSE_ATTEMPT_FILE="NODE_001_REVERSE_CONTAINMENT_ATTEMPTS.tsv"; string REVERSE_WITNESS_FILE="NODE_001_REVERSE_CONTAINMENT_WITNESSES.tsv";',
        'write(REVERSE_ATTEMPT_FILE,"basis_generator|exponent|normal_form"); write(REVERSE_WITNESS_FILE,"basis_generator|found|exponent|normal_form");',
        "int reverse_basis_index; int reverse_exponent; int reverse_found; int reverse_found_exponent; int reverse_found_count=0; int reverse_membership_reduction_count=0; poly REVERSE_POWER; poly REVERSE_NF;",
        "for(reverse_basis_index=1;reverse_basis_index<=size(ARCHIVED_OPEN_LITERAL);reverse_basis_index=reverse_basis_index+1){ REVERSE_POWER=1; REVERSE_NF=1; reverse_found=0; reverse_found_exponent=-1; for(reverse_exponent=0;reverse_exponent<=64;reverse_exponent=reverse_exponent+1){ if(reverse_found==0){ REVERSE_NF=reduce(REVERSE_POWER*ARCHIVED_OPEN_LITERAL[reverse_basis_index],NODE_SB); reverse_membership_reduction_count=reverse_membership_reduction_count+1; write(REVERSE_ATTEMPT_FILE,string(reverse_basis_index)+\"|\"+string(reverse_exponent)+\"|\"+string(REVERSE_NF)); if(REVERSE_NF==0){ reverse_found=1; reverse_found_exponent=reverse_exponent; reverse_found_count=reverse_found_count+1; } else { REVERSE_POWER=REVERSE_POWER*SCANNED_DELTA_NODE_NF; } } } write(REVERSE_WITNESS_FILE,string(reverse_basis_index)+\"|\"+string(reverse_found)+\"|\"+string(reverse_found_exponent)+\"|\"+string(REVERSE_NF)); }",
        'print("ARCHIVED_SATURATION_PREFIX_STDOUT_SHA256='
        + PREFIX_STDOUT_SHA256 + '");',
        'print("ARCHIVED_SATURATION_PREFIX_BOUND=1");',
        'print("ARCHIVED_SATURATION_OBJECT_TYPE=list");',
        'print("ARCHIVED_SATURATION_OBJECT_SIZE=1");',
        'print("ARCHIVED_SATURATION_SLOT1_TYPE=ideal");',
        'print("ARCHIVED_SATURATION_STABILITY_FAILURES=0");',
        'print("ARCHIVED_SATURATION_RESULT_USED_AS_PROVENANCE_ONLY=1");',
        'print("RESUME_NODE_INCLUSION_FAILURES="+string(resume_node_inclusion_failures));',
        'print("RESUME_OPEN_BASIS_REPLAY_FAILURES="+string(resume_open_basis_replay_failures));',
        'print("RESUME_CANDIDATE_STABILITY_FAILURES="+string(resume_candidate_stability_failures));',
        'print("RESUME_ACTIVE_UNIT_NF_NONZERO="+string(ACTIVE_UNIT_NF!=0));',
        'print("RESUME_DELTA_NF_NONZERO="+string(DELTA!=0));',
        'print("REVERSE_CONTAINMENT_BASIS_GENERATOR_COUNT="+string(size(ARCHIVED_OPEN_LITERAL))); print("REVERSE_CONTAINMENT_WITNESS_FOUND_COUNT="+string(reverse_found_count)); print("REVERSE_CONTAINMENT_MEMBERSHIP_REDUCTION_COUNT="+string(reverse_membership_reduction_count)); print("REVERSE_CONTAINMENT_SEARCH_BOUND=64");',
        'if(reverse_found_count!=size(ARCHIVED_OPEN_LITERAL)){ print("REVERSE_CONTAINMENT_WITNESS_SEARCH_EXHAUSTED_NO_VERDICT=1"); quit; }',
        'if(resume_node_inclusion_failures!=0 || resume_open_basis_replay_failures!=0 || resume_candidate_stability_failures!=0 || ACTIVE_UNIT_NF==0 || DELTA==0){ print("FATAL_PROPER_OPEN_RESUME_CERTIFICATE"); quit; }',
        'write("NODE_001_RESUMED_ACTIVE_STANDARD_BASIS.txt",string(ACTIVE_SB));',
        'print("SELF_CONTAINED_TWO_CONTAINMENT_SATURATION_CERTIFICATE=1");',
        'print("PROPER_OPEN_IDEAL_CERTIFICATE=1");',
        'print("NODE_SATURATION_RECOMPUTATION_ENTERED=0");',
        'print("CANDIDATE_STABILITY_SATURATION_ENTERED=1");',
        'print("PURE_DELTA_POWER_SEARCH_ENTERED=0");',
        'print("CLOSED_SUCCESSOR_ENTERED=0");',
        'print("PROPER_OPEN_ROUTING_PASS=1");',
        'print("RING_ORDER=Q[q0,q2,c4,c6]_dp");',
        'print("C4_SOURCE_TOKEN_CENSUS=30");',
        'print("INHERITED_RANK_UPPER_BOUND=6");',
        f'print("INHERITED_RANK_CERTIFICATE_ARCHIVE_SHA256={rank_archive_sha256}");',
        f'print("INHERITED_RANK_CERTIFICATE_MEMBER_SHA256={rank_member_sha256}");',
        'print("INHERITED_RANK_CERTIFICATE_BOUND=1");',
        'print("SELECTED_MINOR_ROWS=1,2,4,7,9,11");',
        'print("SELECTED_MINOR_COLS=1,2,3,5,6,7");',
        f'print("SELECTED_MINOR_LITERAL_SHA256={EXPECTED_DELTA_SHA256}");',
    ]
    script = "\n".join(lines) + "\n" + tail
    validate_script(script)
    return script


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepared", required=True, type=Path)
    parser.add_argument("--frozen-r5-source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    prepared = args.prepared.resolve()
    r5 = load_r5(args.frozen_r5_source.resolve())
    prepared_manifest = json.loads((prepared / "PREPARED_INPUTS.json").read_text())
    if prepared_manifest.get("archive_sha256") != FROZEN_ARCHIVE_SHA256:
        raise SystemExit("PREPARED_ARCHIVE_BINDING_DRIFT")
    for relative, expected in EXPECTED_FILES.items():
        path = prepared / relative
        if sha256(path) != expected:
            raise SystemExit(f"PREPARED_FILE_SHA_DRIFT:{relative}")
    input_manifest = json.loads((prepared / "output/INPUT_MANIFEST.json").read_text())
    if (input_manifest.get("component") != "triple02"
            or input_manifest.get("label") != "TRIPLE02"
            or input_manifest.get("remaining") != ["q0", "q2", "c4", "c6"]
            or input_manifest.get("root_rank_upper_bound") != 6):
        raise SystemExit("FROZEN_INPUT_MANIFEST_SCOPE_DRIFT")
    node_input = json.loads((prepared / "output/node_001/NODE_INPUT.json").read_text())
    generators = [r5.clean_poly(value) for value in node_input.get("generators", [])]
    generator_hashes = tuple(hashlib.sha256(value.encode()).hexdigest()
                             for value in generators)
    if (node_input.get("node") != 1 or node_input.get("inherited_rank_upper_bound") != 6
            or generator_hashes != EXPECTED_GENERATOR_SHA256
            or tuple(node_input.get("generator_sha256", [])) != EXPECTED_GENERATOR_SHA256):
        raise SystemExit("FROZEN_NODE_INPUT_DRIFT")
    rank_support = json.loads(
        (prepared / "output/node_001/rank_size_6.support.json").read_text())
    if rank_support != {
            "formal_slots": 97020, "node": 1, "size": 6,
            "structural_zero": 95920, "support_entries": 36,
            "support_matchable": 1100}:
        raise SystemExit("FROZEN_RANK_SUPPORT_CENSUS_DRIFT")
    pivot_path = prepared / "output/node_001/NODE_001_REDUCE_PIVOTS.tsv"
    verify_pivots(pivot_path)
    residual = r5.read_residual(
        prepared / "output/node_001/NODE_001_REDUCE_RESIDUAL.tsv")
    if sum(value != "0" for row in residual for value in row) != 36:
        raise SystemExit("FROZEN_RESIDUAL_SUPPORT_DRIFT")
    rows, cols, delta = r5.read_witness(
        prepared / "output/node_001/NODE_001_SIZE_6_WITNESS.tsv", 6)
    if rows != (1, 2, 4, 7, 9, 11) or cols != (1, 2, 3, 5, 6, 7):
        raise SystemExit("FROZEN_WITNESS_INDEX_DRIFT")
    open_basis = clean_ideal(
        (prepared / "output/node_001/NODE_001_OPEN_SAT_STANDARD_BASIS.txt").read_text())
    if open_basis != OPEN_BASIS_TEXT:
        raise SystemExit("FROZEN_OPEN_BASIS_LITERAL_DRIFT")
    old_saturation = (prepared / "output/node_001/saturation.sing").read_text()
    if "for(ek=0;ek<=256;ek=ek+1)" not in old_saturation:
        raise SystemExit("FROZEN_TIMEOUT_CAUSE_TOKEN_MISSING")
    old_stdout = (prepared / "output/node_001/saturation.stdout.txt").read_text().splitlines()
    old_required = {
        "NODE_REDUCER_FIXTURES_PASS=1",
        "SATURATION_OBJECT_TYPE=list",
        "SATURATION_OBJECT_SIZE=1",
        "SATURATION_SLOT1_TYPE=ideal",
        "SATURATION_NODE_INCLUSION_FAILURES=0",
        "SATURATION_STABILITY_FAILURES=0",
    }
    if not old_required.issubset(set(old_stdout)):
        raise SystemExit("FROZEN_PREFIX_MARKER_DRIFT")
    if any(line.startswith("SATURATION_CERTIFICATE_COMPLETE=") for line in old_stdout):
        raise SystemExit("FROZEN_TIMEOUT_FALSE_COMPLETION")
    base = prepared / "work/base"
    label, zeros, factor, remaining, assignment, counts = r5.source_inputs(
        base, "triple02")
    root_delta = r5.clean_poly(
        (base / "output/triple02/TRIPLE02_CHART_DELTA.txt").read_text())
    reconstructed_generators = (r5.clean_poly(factor), root_delta)
    if (label != "TRIPLE02" or tuple(zeros) != ("q1", "c8")
            or remaining != ["q0", "q2", "c4", "c6"]
            or tuple(reconstructed_generators) != tuple(generators)
            or counts != {"q1": 566, "c8": 6}):
        raise SystemExit("FROZEN_SOURCE_RECONSTRUCTION_DRIFT")
    reconstructed_reduce = r5.build_reduce_script(
        remaining, generators, 1, label, assignment)
    archived_reduce = (prepared / "output/node_001/reduce.sing").read_text()
    if (reconstructed_reduce != archived_reduce
            or hashlib.sha256(reconstructed_reduce.encode()).hexdigest()
            != EXPECTED_FILES["output/node_001/reduce.sing"]
            or reconstructed_reduce.count(RING_DECLARATION) != 1
            or len(re.findall(r"\bc4\b", reconstructed_reduce)) != 30):
        raise SystemExit("FULL_MATRIX_RECONSTRUCTION_OR_C4_DRIFT")
    rank_provenance = r5.verify_rank_bound(base, "triple02", 6)
    script = build_resume_script(
        r5, remaining, generators, label, assignment, residual,
        6, rows, cols, delta, open_basis,
        str(rank_provenance["archive_sha256"]),
        str(rank_provenance["certificate_member_sha256"]))
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(script)
    metadata = {
        "archived_open_basis_sha256": OPEN_BASIS_SHA256,
        "archived_prefix_stdout_sha256": PREFIX_STDOUT_SHA256,
        "component": "triple02",
        "forbidden_production_token_census": {
            token: script.count(token) for token in FORBIDDEN_PRODUCTION_TOKENS},
        "free_kernel_columns": 4,
        "full_ring_and_order": "Q[q0,q2,c4,c6],dp",
        "full_matrix_reconstruction_sha256": hashlib.sha256(
            reconstructed_reduce.encode()).hexdigest(),
        "generated_source_c4_token_count_including_order_marker": len(
            re.findall(r"\bc4\b", script)),
        "generated_script_sha256": hashlib.sha256(script.encode()).hexdigest(),
        "inherited_exact_quotient_rank": 6,
        "inherited_rank_provenance": rank_provenance,
        "node": 1,
        "proper_open_resume_only": True,
        "saturation_certificate_model": (
            "SELF_CONTAINED_TWO_CONTAINMENT_WITH_FRESH_CANDIDATE_STABILITY_"
            "AND_PER_GENERATOR_REVERSE_WITNESSES"),
        "selected_minor_sha256": hashlib.sha256(delta.encode()).hexdigest(),
        "source_reconstruction_counts": counts,
        "whole_stratum_inference_authorized": False,
    }
    metadata_path = output.with_suffix(".build.json")
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(f"GENERATED_RESUME_SCRIPT_SHA256={metadata['generated_script_sha256']}")
    print("FROZEN_SOURCE_RECONSTRUCTION_PASS=1")
    print("FULL_C4_MATRIX_RECONSTRUCTION_PASS=1")
    print("ARCHIVED_PROPER_OPEN_PREFIX_BOUND=1")
    print("NODE_SATURATION_RECOMPUTATION_CENSUS=0")
    print("CANDIDATE_STABILITY_SATURATION_CENSUS=1")
    print("PROPER_PATH_PURE_DELTA_POWER_SEARCH_CENSUS=0")
    print("PROPER_PATH_CLOSED_SUCCESSOR_CENSUS=0")
    print("TRIPLE02_PROPER_OPEN_RESUME_BUILD_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
