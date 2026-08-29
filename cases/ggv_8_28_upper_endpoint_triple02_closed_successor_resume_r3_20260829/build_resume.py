#!/usr/bin/env python3
"""Build the closed-successor resume inputs from the validated frozen packet.

Establishes node 2 of the TRIPLE02 recursion as exactly

    I_node2 = ( branch_factor, root_chart_delta, Delta_node1 )

with inherited rank upper bound 6, where the three literals are bound by hash
to the R3 terminal archive, and Delta_node1 is additionally bound semantically
by a generated witness-replay Singular stage (exact node-1 reducer replay plus
determinant replay of the archived rank-six minor).  The settled node-1
proper open D(Delta_node1) is never re-entered.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys


FROZEN_R5_SHA256 = "d679a4d7fb4bf2619fbb3ff47ea6f386ba1c75fdc477276cabf3bec8a2b2cd90"
R3_ARCHIVE_SHA256 = "e5bdd2b25cde0dccd8f1e6b8f0e1fcc815d409426308afb49c45df86af53a1e1"
PROPER_OPEN_ARCHIVE_SHA256 = (
    "4b8ffc1c16828b22b2e76a3aa92a25e8c1f472190a708f30a7b71ba952cbef7e")
GENERATOR_SHA256 = (
    "2b9d29b706ce5d7e58e2dc5a28799782f5610c5ccb7b71987ebd694fd8b83206",
    "fecd1d43f3f55e1c65bec858303b7688c0db83dbe9c3a60f51f70130a4149336",
)
DELTA_NODE1_SHA256 = (
    "84b4c2c4c0bfe5aa7414c35813cc1cf63d7d5416358a394b8e8bdc35820f1d02")
WITNESS_ROWS = (1, 2, 4, 7, 9, 11)
WITNESS_COLS = (1, 2, 3, 5, 6, 7)
RING_DECLARATION = "ring ambient=0,(q0,q2,c4,c6),dp;"
EXPECTED_PREPARED_FILES = {
    "r3/output/INPUT_MANIFEST.json":
        "0025f3eafe43b06d8d4cdd7b99870a52b7da331e8985baf7dd3de09a6e48257e",
    "r3/output/node_001/NODE_INPUT.json":
        "b8bf5ec7f09f53211b00d5aafcee0d5b1b45c997c254437a3edb0f647376f68f",
    "r3/output/node_001/NODE_001_STANDARD_BASIS.txt":
        "bd95508c3d0441d18d2538810e2c40ac85ccd5da57f09a560d2d9a93a483640d",
    "r3/output/node_001/reduce.sing":
        "28385a7044bf6b3a2d79c42738860039b687f32f13d5a43c0e67c50b247af609",
    "r3/output/node_001/NODE_001_REDUCE_PIVOTS.tsv":
        "2edaa006dae3f63e90973d40de5c7cdda00437570283429c69b353023645e7fc",
    "r3/output/node_001/NODE_001_REDUCE_RESIDUAL.tsv":
        "f24a4a23aa99d2864c468cce73d7a3affbb7f7baa7344af29a86060dad1a0bfb",
    "r3/output/node_001/rank_size_6.sing":
        "9f9e76085fb6c53b73176daff005d1843c2dd0e362432c4bbb9bfb6eefd8a071",
    "r3/output/node_001/rank_size_6.support.json":
        "bb8f7ee0faabbdb8e40be15bd4d6b3df319acbb5d6d6df7643954a65503d8c51",
    "r3/output/node_001/NODE_001_SIZE_6_MINORS.tsv":
        "1c6e57a4551de1f97f31444b771c8b7255b1e270fa1f4fbcd5198795bef07b86",
    "r3/output/node_001/NODE_001_SIZE_6_WITNESS.tsv":
        "fa0428864a2e15b65b89c0fee2c8f91a557571b0c2c7502f1c9230a6f88d8632",
    "settled_open_provenance/output/VERDICT.txt":
        "75645210fa8d7a9cebada5680b6608dfeb1ebada23e8e1cebaba49bf9fc63a05",
    "settled_open_provenance/output/SUMMARY.json":
        "a976536e24f81bc22fb360827d4123edaa87df0a7eadba7bb4146143512ec188",
}
EXPECTED_RANK6_SUPPORT = {
    "formal_slots": 97020, "node": 1, "size": 6, "structural_zero": 95920,
    "support_entries": 36, "support_matchable": 1100}
EXPECTED_RANK_ARCHIVE_SHA256 = (
    "b947a2d3e81525902a93500026020c2cf9580f070767757389daadb9a6bbe3b2")
EXPECTED_RANK_MEMBER_SHA256 = (
    "cc6dc1c4edbceeecf31c17b96ab9a0ac9744720100e7bf3f20ba41c4e4cd99d2")

WITNESS_REQUIRED_TOKENS = (
    "NODE_REDUCER_FIXTURES_PASS=1",
    "WITNESS_MINOR_ROWS=1,2,4,7,9,11",
    "WITNESS_MINOR_COLS=1,2,3,5,6,7",
    "WITNESS_DELTA_NF_NONZERO=",
    "WITNESS_DELTA_EQUALS_ARCHIVED=",
    "WITNESS_DELTA_NF_STABLE=1",
    "CLOSED_SUCCESSOR_GENERATOR_COUNT=3",
    "CLOSED_SUCCESSOR_CONTAINS_DELTA=",
    "CLOSED_SUCCESSOR_EMPTY=",
    "NODE1_OPEN_SATURATION_ENTERED=0",
    "NODE1_PURE_DELTA_POWER_SEARCH_ENTERED=0",
    "NODE1_PROPER_OPEN_CHART_ENTERED=0",
    "SETTLED_OPEN_ROUTE_NOT_REENTERED=1",
    "WITNESS_REPLAY_COMPLETE=1",
)
WITNESS_FORBIDDEN_TOKENS = (
    "sat(", 'LIB "elim.lib"', "OPEN_SAT_RESULT", "OPEN_SAT_IDEAL",
    "OPEN_SB", "EMPTY_CERT", "for(ek=", "NEXT_IDEAL", "NEXT_SB",
    "REDUCER_PLACEHOLDER", "PLACEHOLDER", "TODO",
)
NODE2_FORBIDDEN_TOKENS = (
    "sat(", 'LIB "elim.lib"', "OPEN_SAT_RESULT", "OPEN_SAT_IDEAL",
    "OPEN_SB", "EMPTY_CERT", "for(ek=", "NEXT_IDEAL", "NEXT_SB",
    "REDUCER_PLACEHOLDER", "PLACEHOLDER", "TODO",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


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


def verify_pivots(path: Path) -> None:
    lines = path.read_text().splitlines()
    if len(lines) != 96 or lines[0] != "step|source_row|source_col|pivot":
        raise SystemExit("ARCHIVED_PIVOT_CENSUS")
    for expected_step, line in enumerate(lines[1:], 1):
        fields = line.split("|", 3)
        if len(fields) != 4 or int(fields[0]) != expected_step:
            raise SystemExit("ARCHIVED_PIVOT_STEP_DISAGREEMENT")


def build_witness_replay_script(r5, remaining: list[str],
                                generators: list[str], label: str,
                                assignment: str, delta: str) -> str:
    lines = ["// Exact TRIPLE02 node-1 witness replay for the closed successor."]
    lines += r5.node_header(remaining, generators, 1)
    lines += r5.elimination_lines(label, assignment, False, "NODE_001_REDUCE")
    entries = [f"R[{row},{col}]" for row in WITNESS_ROWS
               for col in WITNESS_COLS]
    rows_text = ",".join(map(str, WITNESS_ROWS))
    cols_text = ",".join(map(str, WITNESS_COLS))
    lines += [
        f"poly ARCHIVED_DELTA_NODE1={delta};",
        r5.matrix_literal("WITNESS_MINOR", 6, 6, entries),
        "poly WITNESS_RAW=det(WITNESS_MINOR); poly WITNESS_NF=reduce(WITNESS_RAW,NODE_SB);",
        f'print("WITNESS_MINOR_ROWS={rows_text}"); print("WITNESS_MINOR_COLS={cols_text}");',
        'print("WITNESS_DELTA_NF_NONZERO="+string(WITNESS_NF!=0));',
        'print("WITNESS_DELTA_EQUALS_ARCHIVED="+string(WITNESS_NF==ARCHIVED_DELTA_NODE1));',
        'if(WITNESS_NF==0 || WITNESS_NF!=ARCHIVED_DELTA_NODE1){ print("FATAL_WITNESS_DELTA_REPLAY"); quit; }',
        "poly ARCHIVED_DELTA_STABLE_NF=reduce(ARCHIVED_DELTA_NODE1,NODE_SB);",
        'if(ARCHIVED_DELTA_STABLE_NF!=ARCHIVED_DELTA_NODE1){ print("FATAL_WITNESS_DELTA_NF_STABILITY"); quit; }',
        'print("WITNESS_DELTA_NF_STABLE=1");',
        f"ideal SUCCESSOR_IDEAL={','.join(generators)},ARCHIVED_DELTA_NODE1;",
        "ideal SUCCESSOR_SB=std(SUCCESSOR_IDEAL);",
        "poly SUCCESSOR_UNIT_NF=reduce(1,SUCCESSOR_SB);",
        "poly SUCCESSOR_DELTA_NF=reduce(ARCHIVED_DELTA_NODE1,SUCCESSOR_SB);",
        f'write("NODE_002_SEED_STANDARD_BASIS.txt",string(SUCCESSOR_SB));',
        'print("CLOSED_SUCCESSOR_GENERATOR_COUNT=3");',
        'print("CLOSED_SUCCESSOR_CONTAINS_DELTA="+string(SUCCESSOR_DELTA_NF==0));',
        'print("CLOSED_SUCCESSOR_EMPTY="+string(SUCCESSOR_UNIT_NF==0));',
        'if(SUCCESSOR_DELTA_NF!=0){ print("FATAL_CLOSED_SUCCESSOR_DELTA_MEMBERSHIP"); quit; }',
        'print("NODE1_OPEN_SATURATION_ENTERED=0");',
        'print("NODE1_PURE_DELTA_POWER_SEARCH_ENTERED=0");',
        'print("NODE1_PROPER_OPEN_CHART_ENTERED=0");',
        'print("SETTLED_OPEN_ROUTE_NOT_REENTERED=1");',
        'print("WITNESS_REPLAY_COMPLETE=1"); quit;',
        "",
    ]
    return r5.finalize_script([line for line in lines if line != ""])


def validate_witness_replay_script(script: str, delta: str) -> None:
    present = [token for token in WITNESS_FORBIDDEN_TOKENS if token in script]
    if present:
        raise RuntimeError(
            "FORBIDDEN_WITNESS_REPLAY_TOKEN:" + ",".join(present))
    missing = [token for token in WITNESS_REQUIRED_TOKENS
               if script.count(token) != 1]
    if missing:
        raise RuntimeError(
            "REQUIRED_WITNESS_REPLAY_TOKEN_CENSUS:" + ",".join(missing))
    if script.count(RING_DECLARATION) != 1:
        raise RuntimeError("WITNESS_RING_DECLARATION_CENSUS")
    delta_matches = re.findall(r"^poly ARCHIVED_DELTA_NODE1=(.+);$", script,
                               flags=re.MULTILINE)
    if (len(delta_matches) != 1 or delta_matches[0] != delta
            or sha256_text(delta_matches[0]) != DELTA_NODE1_SHA256):
        raise RuntimeError("WITNESS_DELTA_LITERAL_OR_HASH_DRIFT")
    if script.count("NF_RATIONAL_UNIT_PIVOT_COUNT=") != 1 \
            or script.count("pivot_count!=95") != 1:
        raise RuntimeError("WITNESS_PIVOT_GATE_CENSUS")
    if script.count("NODE_GENERATOR_COUNT=2") != 1:
        raise RuntimeError("WITNESS_NODE1_GENERATOR_COUNT_CENSUS")


def validate_node2_reduce_script(script: str, delta: str) -> None:
    present = [token for token in NODE2_FORBIDDEN_TOKENS if token in script]
    if present:
        raise RuntimeError("FORBIDDEN_NODE2_REDUCE_TOKEN:" + ",".join(present))
    if script.count(RING_DECLARATION) != 1:
        raise RuntimeError("NODE2_RING_DECLARATION_CENSUS")
    if script.count("NODE_GENERATOR_COUNT=3") != 1 \
            or script.count("NODE_INDEX=2") != 1:
        raise RuntimeError("NODE2_HEADER_CENSUS")
    for index in (1, 2, 3):
        if script.count(f"FATAL_NODE_GENERATOR_NF_{index}") != 1:
            raise RuntimeError(f"NODE2_GENERATOR_FIXTURE_CENSUS:{index}")
    if script.count(delta) != 2:
        # once inside the NODE_IDEAL literal, once as NODE_GENERATOR_3
        raise RuntimeError("NODE2_DELTA_LITERAL_CENSUS")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepared", required=True, type=Path)
    parser.add_argument("--frozen-r5-source", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    prepared = args.prepared.resolve()
    r5 = load_r5(args.frozen_r5_source.resolve())
    prepared_manifest = json.loads((prepared / "PREPARED_INPUTS.json").read_text())
    if (prepared_manifest.get("r3_archive_sha256") != R3_ARCHIVE_SHA256
            or prepared_manifest.get("proper_open_archive_sha256")
            != PROPER_OPEN_ARCHIVE_SHA256
            or prepared_manifest.get("proper_open_trust_model")
            != "ROUTING_PROVENANCE_ONLY_NEVER_AN_INPUT"):
        raise SystemExit("PREPARED_ARCHIVE_BINDING_DRIFT")
    for relative, expected in EXPECTED_PREPARED_FILES.items():
        if sha256(prepared / relative) != expected:
            raise SystemExit(f"PREPARED_FILE_SHA_DRIFT:{relative}")
    settled_verdict = (prepared / "settled_open_provenance/output/VERDICT.txt"
                       ).read_text().strip()
    if settled_verdict != "EXACT_ENDPOINT_DEAD_ON_NODE1_PROPER_OPEN_ONLY":
        raise SystemExit("SETTLED_OPEN_VERDICT_DRIFT")
    r3_root = prepared / "r3"
    input_manifest = json.loads(
        (r3_root / "output/INPUT_MANIFEST.json").read_text())
    if (input_manifest.get("component") != "triple02"
            or input_manifest.get("label") != "TRIPLE02"
            or input_manifest.get("remaining") != ["q0", "q2", "c4", "c6"]
            or input_manifest.get("root_rank_upper_bound") != 6):
        raise SystemExit("FROZEN_INPUT_MANIFEST_SCOPE_DRIFT")
    node_input = json.loads(
        (r3_root / "output/node_001/NODE_INPUT.json").read_text())
    generators = [r5.clean_poly(value)
                  for value in node_input.get("generators", [])]
    generator_hashes = tuple(sha256_text(value) for value in generators)
    if (node_input.get("node") != 1
            or node_input.get("inherited_rank_upper_bound") != 6
            or generator_hashes != GENERATOR_SHA256
            or tuple(node_input.get("generator_sha256", [])) != GENERATOR_SHA256):
        raise SystemExit("FROZEN_NODE_INPUT_DRIFT")
    rank_support = json.loads(
        (r3_root / "output/node_001/rank_size_6.support.json").read_text())
    if rank_support != EXPECTED_RANK6_SUPPORT:
        raise SystemExit("FROZEN_RANK_SUPPORT_CENSUS_DRIFT")
    verify_pivots(r3_root / "output/node_001/NODE_001_REDUCE_PIVOTS.tsv")
    residual = r5.read_residual(
        r3_root / "output/node_001/NODE_001_REDUCE_RESIDUAL.tsv")
    if sum(value != "0" for row in residual for value in row) != 36:
        raise SystemExit("FROZEN_RESIDUAL_SUPPORT_DRIFT")
    rows, cols, delta = r5.read_witness(
        r3_root / "output/node_001/NODE_001_SIZE_6_WITNESS.tsv", 6)
    if rows != WITNESS_ROWS or cols != WITNESS_COLS:
        raise SystemExit("FROZEN_WITNESS_INDEX_DRIFT")
    if sha256_text(delta) != DELTA_NODE1_SHA256:
        raise SystemExit("FROZEN_WITNESS_DELTA_HASH_DRIFT")
    if delta in generators or sha256_text(delta) in generator_hashes:
        raise SystemExit("WITNESS_DELTA_COLLIDES_WITH_NODE_GENERATOR")
    base = r3_root / "work/base"
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
    if (sha256_text(reconstructed_reduce)
            != EXPECTED_PREPARED_FILES["r3/output/node_001/reduce.sing"]
            or reconstructed_reduce
            != (r3_root / "output/node_001/reduce.sing").read_text()):
        raise SystemExit("FULL_MATRIX_RECONSTRUCTION_DRIFT")
    census_scratch = args.output_dir.resolve() / "rank_size_6.support.rebuild.json"
    args.output_dir.resolve().mkdir(parents=True, exist_ok=True)
    reconstructed_rank6 = r5.build_rank_size_script(
        remaining, generators, 1, residual, 6, census_scratch)
    if (sha256_text(reconstructed_rank6)
            != EXPECTED_PREPARED_FILES["r3/output/node_001/rank_size_6.sing"]
            or json.loads(census_scratch.read_text()) != EXPECTED_RANK6_SUPPORT):
        raise SystemExit("FULL_RANK_CENSUS_RECONSTRUCTION_DRIFT")
    rank_provenance = r5.verify_rank_bound(base, "triple02", 6)
    if (rank_provenance["archive_sha256"] != EXPECTED_RANK_ARCHIVE_SHA256
            or rank_provenance["certificate_member_sha256"]
            != EXPECTED_RANK_MEMBER_SHA256
            or rank_provenance["rank_upper_bound"] != 6):
        raise SystemExit("INHERITED_RANK_PROVENANCE_DRIFT")
    witness_script = build_witness_replay_script(
        r5, remaining, generators, label, assignment, delta)
    validate_witness_replay_script(witness_script, delta)
    successor_generators = generators + [delta]
    node2_reduce = r5.build_reduce_script(
        remaining, successor_generators, 2, label, assignment)
    validate_node2_reduce_script(node2_reduce, delta)
    output = args.output_dir.resolve()
    witness_path = output / "TRIPLE02_NODE1_WITNESS_REPLAY.sing"
    node2_reduce_path = output / "NODE_002_REDUCE_EXPECTED.sing"
    witness_path.write_text(witness_script)
    node2_reduce_path.write_text(node2_reduce)
    resume_input = {
        "node": 2,
        "generators": successor_generators,
        "generator_sha256": [sha256_text(value)
                             for value in successor_generators],
        "inherited_rank_upper_bound": 6,
        "closed_successor_of_node": 1,
        "delta_node1_sha256": DELTA_NODE1_SHA256,
        "delta_node1_witness_rows": list(WITNESS_ROWS),
        "delta_node1_witness_cols": list(WITNESS_COLS),
        "inherited_rank_provenance": rank_provenance,
        "r3_archive_sha256": R3_ARCHIVE_SHA256,
        "settled_open_archive_sha256": PROPER_OPEN_ARCHIVE_SHA256,
        "settled_open_verdict": settled_verdict,
        "settled_open_route_reentry_forbidden": True,
    }
    resume_input_path = output / "RESUME_NODE_INPUT.json"
    resume_input_path.write_text(
        json.dumps(resume_input, indent=2, sort_keys=True) + "\n")
    metadata = {
        "component": "triple02",
        "delta_node1_sha256": DELTA_NODE1_SHA256,
        "full_matrix_reconstruction_sha256": sha256_text(reconstructed_reduce),
        "full_rank_census_reconstruction_sha256": sha256_text(
            reconstructed_rank6),
        "generated_node2_reduce_sha256": sha256_text(node2_reduce),
        "generated_witness_replay_sha256": sha256_text(witness_script),
        "inherited_rank_provenance": rank_provenance,
        "node2_generator_sha256": resume_input["generator_sha256"],
        "ring_and_order": "Q[q0,q2,c4,c6],dp",
        "settled_open_route_reentry_forbidden": True,
        "source_reconstruction_counts": counts,
        "whole_stratum_inference_authorized": False,
    }
    (output / "BUILD_MANIFEST.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(f"GENERATED_WITNESS_REPLAY_SHA256={metadata['generated_witness_replay_sha256']}")
    print(f"GENERATED_NODE2_REDUCE_SHA256={metadata['generated_node2_reduce_sha256']}")
    print("FROZEN_SOURCE_RECONSTRUCTION_PASS=1")
    print("FULL_MATRIX_RECONSTRUCTION_PASS=1")
    print("FULL_RANK_CENSUS_RECONSTRUCTION_PASS=1")
    print("INHERITED_RANK_PROVENANCE_PASS=1")
    print("SETTLED_OPEN_ROUTE_REENTRY_FORBIDDEN=1")
    print("TRIPLE02_CLOSED_SUCCESSOR_BUILD_PASS=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
