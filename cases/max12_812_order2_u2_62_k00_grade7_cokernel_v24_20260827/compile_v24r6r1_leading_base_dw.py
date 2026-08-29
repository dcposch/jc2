#!/usr/bin/env python3
"""Exact seven-generator/eight-logical-slot D(W) gate with full embedding."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
QUADRICS = ROOT / "cases/max12_812_order2_u2_62_k00_weighted_first_stratum_v22_20260827/aws_r6b_r1_pass/output/UNLOADED_QUADRATIC_INITIALS.txt"
F10 = ROOT / "cases/max12_812_order2_u2_62_k00_weighted_first_stratum_v22_20260827/aws_r6b_r1_pass/output/F10_QUARTIC.txt"
V22_REPORT = ROOT / "cases/max12_812_order2_u2_62_k00_weighted_first_stratum_v22_20260827/RESULT_V22R1.md"
V22_REVIEW = ROOT / "xmodel/max12-812-order2-k00-v22r1-first-weighted-stratum-hostile-review-20260827.md"
WITNESS = ROOT / "cases/max12_812_order2_u2_62_k00_grade7_newest_block_v23_20260827/aws_r6b_pass/output/GENERIC_RANK_WITNESS_MINOR.txt"
V24_REVIEW = ROOT / "xmodel/max12-812-order2-k00-v24-grade7-cokernel-hostile-review-20260827.md"
ORIGINAL = HERE / "aws_r6b_pass/output/modular_prior_reduction_v24.sing"
V24_RESULT = HERE / "aws_r6b_pass/output/RESULT.json"
R6_PREREG = HERE / "PREREGISTRATION_R6_LEADING_BASE_DW.md"
R6_COMPILER = HERE / "compile_v24r6_leading_base_dw.py"
ERRATUM = HERE / "DESIGN_ERRATUM_R6_LEADING_BASE_DW.md"
PREREG = HERE / "PREREGISTRATION_R6R1_LEADING_BASE_DW.md"
EXPECTED = {
    QUADRICS: "fd90f064ca43715c37fd7b02c99c842b0b21a6ecd7f5f2eeaf7b8645f95e62a2",
    F10: "c8e214ae21b058dddb063dcd7a9075a34b02a14f01f54386822cf85f0dc2c8e8",
    V22_REPORT: "494075c5675a2571808aec8606ed5744c2362bf3abc470304226b6fee699e293",
    V22_REVIEW: "f834cb99afb5c7c1820c64c92825c274c8451633d860d5268f47556463e8309b",
    WITNESS: "957181065328c7ef930c6c400272f45ab93a055ff1069ced7f3cca8b3c89bbde",
    V24_REVIEW: "d547baa2f5a56ae7d8551ad115384dc1888e87226e726c1ad5c90b35369882bf",
    ORIGINAL: "6f5e8fac9d8f1d06c5a06a3b3f67b1bce776418d977bf6ea80ca064c9fc5b96a",
    V24_RESULT: "22cbd6acb79fc5788afc4b1220cc9eaa19d0a987a2126a49eace67e89ce7921b",
    R6_PREREG: "914e037406be3d121974fd7666ba55144b5ae3b9593af80408bf0e988eb16340",
    R6_COMPILER: "1513f48790bc49b2f470ef459b659d8458f7865c8d7ac1b098376b151eaa12ff",
    ERRATUM: "d4412519fec8123c703df5eb5cb7c81f31bdb4fdf8c9dbd3fbe90bee0bfb19dc",
    PREREG: "925dad8f37a705021797769af75a596c4fa7c7406f9cf3d25f2d33696149c4bd",
}


class ResourceCap(RuntimeError):
    pass


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V24R6R1 compiler refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V24R6R1 compiler refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def qpath(path: Path) -> str:
    value = str(path.resolve())
    if '"' in value or "\n" in value:
        fail(("unsafe output path", value))
    return value


def exact_assignments(path: Path, names: tuple[str, ...]) -> dict[str, str]:
    result: dict[str, str] = {}
    for line in path.read_text().splitlines():
        if "=" not in line:
            fail(("malformed exact assignment", path, line[:100]))
        name, value = line.split("=", 1)
        if name in result or not value:
            fail(("duplicate/empty exact assignment", path, name))
        result[name] = value
    if set(result) != set(names):
        fail(("exact assignment census", path, sorted(result), names))
    return result


def substitute_full(text: str) -> str:
    result = text
    for index in range(6):
        result = re.sub(rf"\bx{index}\b", f"d{index}_1", result)
    result = re.sub(r"\bz\b", "(zinv*k10_0)", result)
    if re.search(r"\bx[0-5]\b|\bz\b", result):
        fail(("incomplete full-ring substitution", result[:200]))
    return result


def run_singular(singular: str, script: Path, stdout: Path, stderr: Path,
                 timeout: int) -> str:
    try:
        completed = subprocess.run(
            [singular, "-q", str(script)], cwd=script.parent, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    except subprocess.TimeoutExpired as error:
        stdout.write_text(error.stdout or "")
        stderr.write_text(error.stderr or "")
        raise ResourceCap((script.name, timeout)) from error
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    singular_error = re.search(r"(?m)^\s*\?", completed.stdout) is not None
    if completed.returncode or completed.stderr or singular_error or \
            "K00_V24R6R1_FAIL=" in completed.stdout:
        fail(("exact leading-base engine/replay failure", script.name,
              completed.returncode, completed.stderr[-2000:],
              completed.stdout[-3000:]))
    return completed.stdout


def emit_cap(output: Path, tag: str, stage: str, script: Path) -> None:
    payload = {
        "status": "RESOURCE_CAP_NO_VERDICT",
        "registered_aws_lane": tag,
        "stage": stage,
        "script_sha256": digest(script),
        "scope": "NO_EXACT_LEADING_BASE_DW_VERDICT",
        "firewall": "NO_W_ZERO_NO_GRADES7TO19_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V24R6R1=RESOURCE_CAP_NO_VERDICT")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    for path, wanted in EXPECTED.items():
        got = digest(path)
        if got != wanted:
            fail(("frozen input mismatch", str(path), got, wanted))
    if "PASS" not in V22_REVIEW.read_text() or \
            "PASS" not in V24_REVIEW.read_text():
        fail("reviewed dependency PASS marker missing")

    quadrics = exact_assignments(
        QUADRICS, ("Q1", "Q2", "Q3", "Q4", "Q5", "Q6"))
    if any(quadrics[f"Q{index}"] == "0" for index in range(1, 6)) or \
            quadrics["Q6"] != "0":
        fail("reviewed quadratic profile drift")
    f10 = "".join(F10.read_text().split())
    witness = "".join(WITNESS.read_text().split())
    if not f10 or not witness or any(char in f10 + witness for char in ';,"'):
        fail("malformed F10/W exact source")
    original = ORIGINAL.read_text().splitlines()
    if len(original) != 11 or not original[0].startswith("ring R=65521,") or \
            not original[1].startswith("ideal P=") or \
            not re.fullmatch(r"P=P,zinv\*k10_0\*\(.+\)-1;", original[2]):
        fail("full V24 source shape mismatch")
    ring_full = original[0].replace("ring R=65521,", "ring R=0,", 1)
    if not ring_full.startswith("ring R=0,") or "65521" in ring_full:
        fail("full exact-Q ring conversion failed")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    logical_paths = [output / f"LEADING_BASE_CERT_{index:02d}.txt"
                     for index in range(1, 9)]
    basis_path = output / "EXACT_PROPER_STANDARD_BASIS.txt"
    transform_path = output / "EXACT_PROPER_TRANSFORM.matrix"
    small_defs = ["ring R=0,(x0,x1,x2,x3,x4,x5,z),dp;"]
    small_defs.extend(f"poly Q{index}=({quadrics[f'Q{index}']});"
                      for index in range(1, 7))
    small_defs.extend([
        f"poly F10=({f10});", f"poly W=({witness});",
        "ideal B=Q1,Q2,Q3,Q4,Q5,F10,z*W-1;",
        'if ((size(B)!=7)||(Q6!=0)||(W==0)||(F10==0)) { print("K00_V24R6R1_FAIL=SOURCE_PROFILE"); quit; }',
    ])

    preflight = output / "exact_leading_base_dw_preflight.sing"
    preflight.write_text("\n".join(small_defs + [
        "ideal S=slimgb(B); poly N1=reduce(1,S); int D=dim(S);",
        "if (N1==0)", "{",
        '  if (D!=-1) { print("K00_V24R6R1_FAIL=UNIT_DIMENSION"); quit; }',
        '  print("K00_V24R6R1_PREFLIGHT=UNIT"); print("K00_V24R6R1_DIM=-1"); quit;',
        "}",
        'if ((N1!=1)||(D<0)) { print("K00_V24R6R1_FAIL=PROPER_MARKERS"); quit; }',
        'print("K00_V24R6R1_PREFLIGHT=PROPER");',
        'print("K00_V24R6R1_DIM="+string(D)); quit;',
    ]) + "\n")
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    pre_stdout = output / "exact_leading_base_dw_preflight.stdout"
    pre_stderr = output / "exact_leading_base_dw_preflight.stderr"
    try:
        markers = run_singular(singular, preflight, pre_stdout, pre_stderr,
                               21000)
    except ResourceCap:
        emit_cap(output, tag, "SLIMGB_BRANCH_PREFLIGHT", preflight)
        return
    dim_match = re.search(r"K00_V24R6R1_DIM=(-?\d+)", markers)
    if dim_match is None:
        fail("preflight dimension marker missing")
    pre_dim = int(dim_match.group(1))
    artifact_paths = [preflight, pre_stdout, pre_stderr]

    if "K00_V24R6R1_PREFLIGHT=UNIT" in markers:
        producer = output / "exact_leading_base_dw_unit_lift.sing"
        producer_lines = list(small_defs) + [
            'matrix U; matrix C=lift(B,ideal(1),U,"slimgb");',
            'if ((nrows(C)!=7)||(ncols(C)!=1)||(nrows(U)!=1)||(ncols(U)!=1)||(U!=matrix(ideal(1)))) { print("K00_V24R6R1_FAIL=UNIT_LIFT_SHAPE_OR_U"); quit; }',
            'if (matrix(B)*C-matrix(ideal(1))!=0) { print("K00_V24R6R1_FAIL=UNIT_IDENTITY"); quit; }',
            "int pick=0; int jj;",
            "for (jj=1;jj<=7;jj++) { if ((pick==0)&&(B[jj]!=0)&&(C[jj,1]!=0)) { pick=jj; } }",
            'if (pick==0) { print("K00_V24R6R1_FAIL=NO_UNIT_MUTATION_ENTRY"); quit; }',
            "matrix CDROP=C; CDROP[pick,1]=0;",
            'if (matrix(B)*CDROP-matrix(ideal(1))==0) { print("K00_V24R6R1_FAIL=UNIT_DROP_MUTATION"); quit; }',
            "matrix CADD=C; CADD[pick,1]=CADD[pick,1]+1;",
            'if (matrix(B)*CADD-matrix(ideal(1))==0) { print("K00_V24R6R1_FAIL=UNIT_ADD_MUTATION"); quit; }',
        ]
        actual_for_logical = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5,
                              7: 6, 8: 7}
        for logical_index, path in enumerate(logical_paths, 1):
            value = "0" if logical_index == 6 else \
                f"C[{actual_for_logical[logical_index]},1]"
            producer_lines.append(f'write("{qpath(path)}",{value});')
        producer_lines.extend([
            'print("K00_V24R6R1_UNIT_PRODUCER=1");',
            'print("K00_V24R6R1_ACTUAL_PICK="+string(pick)); quit;',
        ])
        producer.write_text("\n".join(producer_lines) + "\n")
        producer_stdout = output / "exact_leading_base_dw_unit_lift.stdout"
        producer_stderr = output / "exact_leading_base_dw_unit_lift.stderr"
        try:
            producer_markers = run_singular(
                singular, producer, producer_stdout, producer_stderr, 21000)
        except ResourceCap:
            emit_cap(output, tag, "DIRECT_UNIT_LIFT", producer)
            return
        pick_match = re.search(r"K00_V24R6R1_ACTUAL_PICK=(\d+)",
                               producer_markers)
        if "K00_V24R6R1_UNIT_PRODUCER=1" not in producer_markers or \
                pick_match is None or not all(path.is_file()
                                              for path in logical_paths):
            fail("unit producer custody marker missing")
        actual_pick = int(pick_match.group(1))
        if not (1 <= actual_pick <= 7):
            fail(("actual mutation index", actual_pick))
        logical_values = [path.read_text().strip() for path in logical_paths]
        if any(not value or ";" in value for value in logical_values) or \
                logical_values[5] != "0":
            fail("malformed logical eight-slot certificate")
        logical_pick = actual_pick if actual_pick <= 5 else actual_pick + 1

        small_replay = output / "exact_leading_base_dw_unit_replay.sing"
        replay_lines = list(small_defs) + ["matrix C[7][1];"]
        for logical_index, actual_index in actual_for_logical.items():
            replay_lines.append(
                f"C[{actual_index},1]={logical_values[logical_index - 1]};")
        replay_lines.extend([
            'if (matrix(B)*C-matrix(ideal(1))!=0) { print("K00_V24R6R1_FAIL=SMALL_SERIALIZED_IDENTITY"); quit; }',
            f"matrix CDROP=C; CDROP[{actual_pick},1]=0;",
            'if (matrix(B)*CDROP-matrix(ideal(1))==0) { print("K00_V24R6R1_FAIL=SMALL_REPLAY_DROP_MUTATION"); quit; }',
            f"matrix CADD=C; CADD[{actual_pick},1]=CADD[{actual_pick},1]+1;",
            'if (matrix(B)*CADD-matrix(ideal(1))==0) { print("K00_V24R6R1_FAIL=SMALL_REPLAY_ADD_MUTATION"); quit; }',
            'print("K00_V24R6R1_SMALL_SECOND_PROCESS_REPLAY=1"); quit;',
        ])
        small_replay.write_text("\n".join(replay_lines) + "\n")
        small_stdout = output / "exact_leading_base_dw_unit_replay.stdout"
        small_stderr = output / "exact_leading_base_dw_unit_replay.stderr"
        try:
            small_markers = run_singular(
                singular, small_replay, small_stdout, small_stderr, 1800)
        except ResourceCap:
            emit_cap(output, tag, "SMALL_SERIALIZED_REPLAY", small_replay)
            return
        if "K00_V24R6R1_SMALL_SECOND_PROCESS_REPLAY=1" not in small_markers:
            fail("small serialized replay marker missing")

        mapped = [substitute_full(value) for value in logical_values]
        full_positions = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5,
                          7: 35, 8: 36}
        full_pick = full_positions[logical_pick]
        full_replay = output / "exact_full_36_generator_embedding_replay.sing"
        full_lines = [
            ring_full, original[1], original[2],
            'if (size(P)!=36) { print("K00_V24R6R1_FAIL=FULL_GENERATOR_CENSUS"); quit; }',
        ]
        full_lines.extend(
            f"poly Q{index}F=({substitute_full(quadrics[f'Q{index}'])});"
            for index in range(1, 6))
        full_lines.extend([
            f"poly F10F=({substitute_full(f10)});",
            f"poly WF=({substitute_full(witness)});",
            'if ((P[1]-Q1F!=0)||(P[2]-Q2F!=0)||(P[3]-Q3F!=0)||(P[4]-Q4F!=0)||(P[5]-Q5F!=0)) { print("K00_V24R6R1_FAIL=FULL_Q_SOURCE_MAP"); quit; }',
            'if (P[35]-F10F!=0) { print("K00_V24R6R1_FAIL=FULL_F10_SOURCE_MAP"); quit; }',
            'if (P[36]-(zinv*k10_0*WF-1)!=0) { print("K00_V24R6R1_FAIL=FULL_LOCALIZER_SOURCE_MAP"); quit; }',
            "matrix CF[36][1];",
        ])
        for logical_index, full_index in full_positions.items():
            full_lines.append(
                f"CF[{full_index},1]={mapped[logical_index - 1]};")
        full_lines.extend([
            'if (matrix(P)*CF-matrix(ideal(1))!=0) { print("K00_V24R6R1_FAIL=FULL_EMBEDDED_IDENTITY"); quit; }',
            f"matrix CFDROP=CF; CFDROP[{full_pick},1]=0;",
            'if (matrix(P)*CFDROP-matrix(ideal(1))==0) { print("K00_V24R6R1_FAIL=FULL_DROP_MUTATION"); quit; }',
            f"matrix CFADD=CF; CFADD[{full_pick},1]=CFADD[{full_pick},1]+1;",
            'if (matrix(P)*CFADD-matrix(ideal(1))==0) { print("K00_V24R6R1_FAIL=FULL_ADD_MUTATION"); quit; }',
            'print("K00_V24R6R1_FULL_36_GENERATOR_EMBEDDED_REPLAY=1"); quit;',
        ])
        full_replay.write_text("\n".join(full_lines) + "\n")
        full_stdout = output / "exact_full_36_generator_embedding_replay.stdout"
        full_stderr = output / "exact_full_36_generator_embedding_replay.stderr"
        try:
            full_markers = run_singular(
                singular, full_replay, full_stdout, full_stderr, 1800)
        except ResourceCap:
            emit_cap(output, tag, "FULL_36_GENERATOR_EMBEDDED_REPLAY",
                     full_replay)
            return
        if "K00_V24R6R1_FULL_36_GENERATOR_EMBEDDED_REPLAY=1" not in full_markers:
            fail("full embedded replay marker missing")
        artifact_paths.extend([
            producer, producer_stdout, producer_stderr, *logical_paths,
            small_replay, small_stdout, small_stderr, full_replay,
            full_stdout, full_stderr,
        ])
        status = "PASS_EXACT_LEADING_BASE_DW_UNIT_WITH_FULL_36_GENERATOR_EMBEDDED_IDENTITY"
        outcome = {
            "branch": "UNIT", "actual_generator_count": 7,
            "logical_certificate_entries": 8,
            "logical_q6_coefficient": "0",
            "actual_mutation_index": actual_pick,
            "logical_mutation_index": logical_pick,
            "full_mutation_index": full_pick,
            "small_serialized_second_process_replay": True,
            "full_36_generator_embedded_identity_replay": True,
            "source_map": {
                "Q1..Q5": "P1..P5", "Q6": "ZERO_SLOT",
                "F10": "P35", "zW-1": "P36 via z=zinv*k10_0",
            },
        }
        scope = "EXACT_Q_LEADING_BASE_DW_UNIT_IMPLIES_FULL_NORMALIZED_PREFIX_D_K10_0_W_EMPTY"
    elif "K00_V24R6R1_PREFLIGHT=PROPER" in markers:
        tracked = output / "exact_leading_base_dw_proper_tracked.sing"
        tracked.write_text("\n".join(small_defs + [
            "matrix T; ideal G=liftstd(B,T);",
            'if ((nrows(T)!=7)||(matrix(B)*T-matrix(G)!=0)) { print("K00_V24R6R1_FAIL=PROPER_BASIS_REPLAY"); quit; }',
            "poly N1=reduce(1,G); int D=dim(G);",
            f'if ((N1!=1)||(D!={pre_dim})||(D<0)) {{ print("K00_V24R6R1_FAIL=PROPERNESS_MARKERS"); quit; }}',
            "ideal BUNIT=B,1; ideal GUNIT=std(BUNIT);",
            'if (reduce(1,GUNIT)!=0) { print("K00_V24R6R1_FAIL=FORCED_UNIT_MUTATION"); quit; }',
            "int pickr=0; int pickc=0; int rr; int cc;",
            "for (cc=1;cc<=ncols(T);cc++) { for (rr=1;rr<=7;rr++) { if ((pickr==0)&&(B[rr]!=0)&&(T[rr,cc]!=0)) { pickr=rr; pickc=cc; } } }",
            'if (pickr==0) { print("K00_V24R6R1_FAIL=NO_TRANSFORM_MUTATION_ENTRY"); quit; }',
            "matrix TBAD=T; TBAD[pickr,pickc]=0;",
            'if (matrix(B)*TBAD-matrix(G)==0) { print("K00_V24R6R1_FAIL=TRANSFORM_DROP_MUTATION"); quit; }',
            f'write("{qpath(basis_path)}",string(G));',
            f'write("{qpath(transform_path)}",string(T));',
            'print("K00_V24R6R1_PROPER_TRACKED=1");',
            'print("K00_V24R6R1_GSIZE="+string(size(G)));',
            'print("K00_V24R6R1_TCOLS="+string(ncols(T)));',
            'print("K00_V24R6R1_TPICKR="+string(pickr));',
            'print("K00_V24R6R1_TPICKC="+string(pickc)); quit;',
        ]) + "\n")
        tracked_stdout = output / "exact_leading_base_dw_proper_tracked.stdout"
        tracked_stderr = output / "exact_leading_base_dw_proper_tracked.stderr"
        try:
            tracked_markers = run_singular(
                singular, tracked, tracked_stdout, tracked_stderr, 21000)
        except ResourceCap:
            emit_cap(output, tag, "PROPER_TRACKED_LIFTSTD", tracked)
            return
        patterns = {
            name: re.search(rf"K00_V24R6R1_{name}=(\d+)", tracked_markers)
            for name in ("GSIZE", "TCOLS", "TPICKR", "TPICKC")
        }
        if "K00_V24R6R1_PROPER_TRACKED=1" not in tracked_markers or \
                any(value is None for value in patterns.values()) or \
                not basis_path.is_file() or not transform_path.is_file():
            fail("proper tracked-basis custody marker missing")
        values = {name: int(match.group(1))
                  for name, match in patterns.items() if match}
        if values["TCOLS"] != values["GSIZE"] or \
                not (1 <= values["TPICKR"] <= 7) or \
                not (1 <= values["TPICKC"] <= values["TCOLS"]):
            fail(("proper tracked-basis shape", values))
        proper_replay = output / "exact_leading_base_dw_proper_replay.sing"
        proper_replay.write_text("\n".join(small_defs + [
            f"ideal G={basis_path.read_text().strip()};",
            f"matrix T[7][{values['TCOLS']}]={transform_path.read_text().strip()};",
            'if (matrix(B)*T-matrix(G)!=0) { print("K00_V24R6R1_FAIL=PROPER_SERIALIZED_BASIS_REPLAY"); quit; }',
            "poly N1=reduce(1,G); int D=dim(G);",
            f'if ((N1!=1)||(D!={pre_dim})) {{ print("K00_V24R6R1_FAIL=PROPER_SERIALIZED_MARKERS"); quit; }}',
            f"matrix TBAD=T; TBAD[{values['TPICKR']},{values['TPICKC']}]=0;",
            'if (matrix(B)*TBAD-matrix(G)==0) { print("K00_V24R6R1_FAIL=PROPER_REPLAY_TRANSFORM_MUTATION"); quit; }',
            "ideal BUNIT=B,1; ideal GUNIT=std(BUNIT);",
            'if (reduce(1,GUNIT)!=0) { print("K00_V24R6R1_FAIL=PROPER_REPLAY_FORCED_UNIT"); quit; }',
            'print("K00_V24R6R1_PROPER_SECOND_PROCESS_REPLAY=1"); quit;',
        ]) + "\n")
        proper_stdout = output / "exact_leading_base_dw_proper_replay.stdout"
        proper_stderr = output / "exact_leading_base_dw_proper_replay.stderr"
        try:
            proper_markers = run_singular(
                singular, proper_replay, proper_stdout, proper_stderr, 1800)
        except ResourceCap:
            emit_cap(output, tag, "PROPER_TRACKED_SERIALIZED_REPLAY",
                     proper_replay)
            return
        if "K00_V24R6R1_PROPER_SECOND_PROCESS_REPLAY=1" not in proper_markers:
            fail("proper second-process replay marker missing")
        artifact_paths.extend([
            tracked, tracked_stdout, tracked_stderr, basis_path,
            transform_path, proper_replay, proper_stdout, proper_stderr,
        ])
        status = "PASS_EXACT_LEADING_BASE_DW_PROPER_WITH_TRACKED_BASIS_AND_DIMENSION"
        outcome = {
            "branch": "PROPER", "actual_generator_count": 7,
            "logical_generator_slots": 8, "logical_q6_slot": "ZERO",
            "exact_affine_dimension": pre_dim,
            "standard_basis_size": values["GSIZE"],
            "tracked_basis_identity_replay": True,
            "serialized_second_process_replay": True,
            "forced_unit_and_transform_drop_mutations": True,
        }
        scope = "EXACT_Q_LEADING_BASE_DW_PROPER_ONLY_NO_FULL_PRIOR_SURVIVAL_CLAIM"
    else:
        fail(("missing leading-base endpoint branch", markers[-3000:]))

    payload = {
        "status": status,
        "registered_aws_lane": tag,
        "field": "Q_exact",
        "ring": "Q[x0,x1,x2,x3,x4,x5,z]",
        "generator_order": ["Q1", "Q2", "Q3", "Q4", "Q5",
                            "Q6=0_LOGICAL_ONLY", "F10", "z*W-1"],
        "preflight_algorithm": "slimgb_then_exact_NF1_and_dimension",
        **outcome,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in artifact_paths
        },
        "input_sha256": {
            str(path.relative_to(ROOT)): digest(path) for path in EXPECTED
        },
        "scope": scope,
        "firewall": "NO_W_ZERO_NO_GRADES7TO19_NO_FULL_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V24R6R1=" + status)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
