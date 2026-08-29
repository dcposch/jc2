#!/usr/bin/env python3
"""Exact AWS-only K00 V27 R3 recursion: test B+I2(A)."""

from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import combinations
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess


CASE_REL = "cases/max12_812_order2_u2_62_k00_rank_compressed_atlas_v27_20260827"
V26_REL = "cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827"
COMPILED_REL = V26_REL + "/aws_box02_r2_held_compile/output"
R1_REL = CASE_REL + "/aws_r6a_r1_exact_base4"
R2_REL = CASE_REL + "/aws_r6a_r2_exact_base3"
ORIGIN_REL = CASE_REL + "/aws_r6a_aux_origin_replay"
PINNED_SHA256 = {
    COMPILED_REL + "/ATLAS_EXACT_POLYNOMIALS.json":
        "d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501",
    COMPILED_REL + "/COMPILED_SOURCE.sha256":
        "5de20da0d3501db668fca38db3c678ba4719745e3df7b32d0d0a8d2867e4da32",
    COMPILED_REL + "/RESULT.json":
        "f1a6f1fc988fc77816daaab13b294b1321de7e476d2891cf7fbfa2e033868d97",
    CASE_REL + "/RESULT_V27_BASE4_R1_EXACT_PREPASS.md":
        "19c8795589ce076c2414474a6341c7929d578958ea122a6745f26ea6ab46bd9c",
    CASE_REL + "/REVIEW_PACKET_BASE4_R1.sha256":
        "41d1107589f33b7f7fab4ec5cac6e47ffc72368dfeeb93981ae2e921a9eb0205",
    R1_REL + "/output/RESULT.json":
        "f886f17ca2c626ec476e695418002185d2223d556721759900f6cdbe89635073",
    CASE_REL + "/RESULT_V27_BASE3_R2_EXACT_PREPASS.md":
        "c42c0482f0b5861f5099e6e121c60a93d018c87a9619749ee1844f5954545c39",
    CASE_REL + "/REVIEW_PACKET_BASE3_R2.sha256":
        "e3cd6586c2db1b51aabedb613f3de5a18c81a14b26bd8a6f9ae42af4b68626f3",
    R2_REL + "/output/RESULT.json":
        "d9d9d9dba1b06f1cb9773066924268a5162774779de9f86339d2c3306fbffdb3",
    R2_REL + "/EVIDENCE.sha256":
        "75ff30e00b95c4901103f38bce9668eb22f9ced9fc831692d44ceff7486f6b9e",
    CASE_REL + "/RESULT_V27_ORIGIN_EXACT_REPLAY.md":
        "35653d3e5fdc04566ed7cca2b42ec56e9c9133e74f85cbcb6ad84f1d92640971",
    ORIGIN_REL + "/output/RESULT.json":
        "e9534c0c31b326b17e3c4e183751776529cdf28b6addabed6d3e6ac337ce8096",
    ORIGIN_REL + "/EVIDENCE.sha256":
        "de36a93c77a4001d6059aa21d4ed974194d4468400a78a1f1122837c7afac7e4",
}
COMPILER_STATUS = "PASS_V26_FITTING_ATLAS_COMPILED_NO_STRATUM_DECISION"
R1_STATUS = "PASS_V27_BASE4_EXACT_RANK_LE3_SURVIVES_PRODUCER_UNREVIEWED"
R2_STATUS = "PASS_V27_R2_EXACT_RANK_LE2_SURVIVES_PRODUCER_UNREVIEWED_ROLLBACK_R1"
ORIGIN_STATUS = "PASS_V27_AUX_ORIGIN_B_I5_EXACT_TRIVIAL_Q_POINT"
STATUS = "PASS_V27_R3_EXACT_RANK_LE1_SURVIVES_PRODUCER_UNREVIEWED_ROLLBACK_R1_R2"


class ResourceCap(RuntimeError):
    """A registered inner wall cap fired."""


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def qpath(path: Path) -> str:
    value = str(path.resolve())
    if '"' in value or "\n" in value:
        fail(("unsafe output path", value))
    return value


def require_nonempty(path: Path) -> None:
    if not path.is_file() or path.stat().st_size == 0:
        fail(("missing or empty replay artifact", str(path)))


def validate_sources(root: Path) -> dict:
    for relative, expected in PINNED_SHA256.items():
        path = root / relative
        if not path.is_file() or digest(path) != expected:
            fail(("pinned source mismatch", relative))
    compiler = json.loads((root / (COMPILED_REL + "/RESULT.json")).read_text())
    if compiler.get("status") != COMPILER_STATUS or \
            compiler.get("A_shape") != [7, 7] or \
            compiler.get("generic_rank_A") != 5:
        fail("compiler endpoint metadata mismatch")
    expected_stats = {
        "2": (441, 90, 326), "3": (1225, 412, 725),
        "4": (1225, 631, 491), "5": (441, 351, 54),
        "6": (49, 49, 0),
    }
    stats = compiler.get("A_minor_statistics", {})
    for rank, (total, zero, unique) in expected_stats.items():
        item = stats.get(rank, {})
        if item.get("total") != total or item.get("zero") != zero or \
                item.get("unique_nonzero_exact_polynomials") != unique:
            fail(("compiler minor census mismatch", rank, item))
    r1 = json.loads((root / (R1_REL + "/output/RESULT.json")).read_text())
    if r1.get("status") != R1_STATUS or r1.get("J3base_unit") is not False or \
            r1.get("exact_affine_dimension") != 3 or \
            r1.get("I4_entries_nonzero_mod_fresh_J4base_basis") != 0:
        fail("R1 endpoint metadata mismatch")
    r2 = json.loads((root / (R2_REL + "/output/RESULT.json")).read_text())
    if r2.get("status") != R2_STATUS or r2.get("J2base_unit") is not False or \
            r2.get("exact_affine_dimension") != 3 or \
            r2.get("I3_entries_nonzero_mod_fresh_J3base_basis") != 0 or \
            r2.get("full_literal_minor_reverse_inclusion") is not True:
        fail("R2 endpoint metadata mismatch")
    origin = json.loads(
        (root / (ORIGIN_REL + "/output/RESULT.json")).read_text())
    if origin.get("status") != ORIGIN_STATUS or \
            origin.get("all_vanish_at_origin") is not True or \
            origin.get("mere_rational_point_target_is_trivial") is not True:
        fail("origin endpoint metadata mismatch")
    atlas = json.loads(
        (root / (COMPILED_REL + "/ATLAS_EXACT_POLYNOMIALS.json")).read_text())
    matrix = atlas.get("A")
    if not isinstance(matrix, list) or len(matrix) != 7 or \
            any(not isinstance(row, list) or len(row) != 7 for row in matrix):
        fail("frozen A shape mismatch")
    if not isinstance(atlas.get("Q1_to_Q6"), list) or \
            len(atlas["Q1_to_Q6"]) != 6:
        fail("frozen B source mismatch")
    return atlas


def poly(item: dict) -> str:
    value = item.get("singular")
    if not isinstance(value, str) or not value:
        fail("missing exact polynomial serialization")
    return value


def matrix_line(matrix: list[list[dict]]) -> str:
    return "matrix A[7][7]=" + ",".join(
        f"({poly(entry)})" for row in matrix for entry in row) + ";"


def emit_labels(output: Path) -> Path:
    path = output / "MINOR_SOURCE_LABELS_RANK2_TO_6.json"
    labels = {}
    for rank in (2, 3, 4, 5, 6):
        labels[str(rank)] = [
            {"rows_one_based": list(rows), "columns_one_based": list(columns)}
            for rows in combinations(range(1, 8), rank)
            for columns in combinations(range(1, 8), rank)
        ]
    path.write_text(json.dumps({
        "matrix": "A_frozen_7_by_7",
        "ordering": "complete lexicographic literal row/column labels",
        "ranks": labels,
    }, sort_keys=True, indent=2) + "\n")
    require_nonempty(path)
    return path


def run_singular(executable: str, script: Path, stdout: Path, stderr: Path,
                 timeout: int) -> str:
    try:
        completed = subprocess.run(
            [executable, "-q", str(script)], cwd=script.parent, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    except subprocess.TimeoutExpired as error:
        stdout.write_text((error.stdout or b"").decode(errors="replace")
                          if isinstance(error.stdout, bytes) else error.stdout or "")
        stderr.write_text((error.stderr or b"").decode(errors="replace")
                          if isinstance(error.stderr, bytes) else error.stderr or "")
        raise ResourceCap(script.name) from error
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    diagnostics = re.compile(
        r"(?mi)^\s*\?|// \*\*|warning|error occurred|K00_V27_R3_FAIL=")
    if completed.returncode or completed.stderr or not completed.stdout.strip() or \
            diagnostics.search(completed.stdout):
        fail(("R3 exact engine/replay failure", script.name,
              completed.returncode, completed.stderr[-2000:],
              completed.stdout[-4000:]))
    return completed.stdout


def emit_cap(output: Path, lane: str, stage: str, script: Path,
             artifacts: list[Path]) -> None:
    payload = {
        "status": "RESOURCE_CAP_NO_VERDICT",
        "registered_aws_lane": lane,
        "stage": stage,
        "rollback_dependency": "BASE4_R1_AND_BASE3_R2_PRODUCER_UNREVIEWED",
        "script_sha256": digest(script),
        "source_hashes": PINNED_SHA256,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in artifacts if path.is_file()
        },
        "scope": "NO_EXACT_V27_R3_VERDICT",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V27_R3=RESOURCE_CAP_NO_VERDICT")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_root", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=int, default=21000)
    args = parser.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if platform.system() != "Linux" or not vendor.is_file() or \
            vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only R3 exact prepass refused host")
    lane = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not lane.startswith("max12_812_order2_u2_62_k00_v27_r3_base2_"):
        fail("registered R3 lane missing")
    if args.timeout <= 0 or args.timeout > 21000:
        fail("inner timeout outside preregistered cap")
    source_root = args.source_root.resolve()
    atlas = validate_sources(source_root)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    labels = emit_labels(output)
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    version = subprocess.run(
        [singular, "--version"], text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, timeout=30, check=True).stdout.splitlines()[0]
    qlist = atlas["Q1_to_Q6"]
    definitions = [
        "ring R=0,(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1),dp;",
        matrix_line(atlas["A"]),
        "ideal B=" + ",".join(f"({poly(item)})" for item in qlist) +
        f",({poly(atlas['F10'])});",
        'if (size(B)!=7) { print("K00_V27_R3_FAIL=B_CENSUS"); quit; }',
        "ideal I6A=minor(A,6); ideal I5A=minor(A,5); ideal I4A=minor(A,4); ideal I3A=minor(A,3); ideal I2A=minor(A,2);",
        'if ((size(I6A)!=0)||(size(I5A)!=90)||(size(I4A)!=594)||(size(I3A)!=813)||(size(I2A)!=351)) { print("K00_V27_R3_FAIL=STORED_MINOR_CENSUS"); quit; }',
        "int mi; int ipick2=0; for (mi=1;mi<=size(I2A);mi++) { if ((ipick2==0)&&(I2A[mi]!=0)) { ipick2=mi; } }",
        'if (ipick2==0) { print("K00_V27_R3_FAIL=I2_PICK"); quit; }',
        "ideal I2M=I2A; I2M[ipick2]=0;",
        'if ((I2M[ipick2]!=0)||(I2M[ipick2]==I2A[ipick2])) { print("K00_V27_R3_FAIL=I2_DELETE_MUTATION"); quit; }',
        "ideal CTRLproper=d0_1; ideal GCTRLproper=std(CTRLproper);",
        'if (reduce(1,GCTRLproper)==0) { print("K00_V27_R3_FAIL=KNOWN_PROPER_CONTROL"); quit; }',
        "ideal J4=B+I5A; ideal SJ4=std(J4);",
        'if ((reduce(1,SJ4)!=1)||(dim(SJ4)!=3)) { print("K00_V27_R3_FAIL=FRESH_J4_CONTROL"); quit; }',
        "ideal I4MOD=reduce(I4A,SJ4); int i4outside=0; for (mi=1;mi<=size(I4MOD);mi++) { if (I4MOD[mi]!=0) { i4outside++; } }",
        'if (i4outside!=0) { print("K00_V27_R3_FAIL=FRESH_R1_EQUALITY"); quit; }',
        "ideal J3=J4+I4A; ideal SJ3=std(J3);",
        'if ((reduce(1,SJ3)!=1)||(dim(SJ3)!=3)) { print("K00_V27_R3_FAIL=FRESH_J3_CONTROL"); quit; }',
        "ideal I3MOD=reduce(I3A,SJ3); int i3outside=0; for (mi=1;mi<=size(I3MOD);mi++) { if (I3MOD[mi]!=0) { i3outside++; } }",
        'if (i3outside!=0) { print("K00_V27_R3_FAIL=FRESH_R2_EQUALITY"); quit; }',
        "ideal J2=J3+I3A; ideal SJ2=std(J2);",
        'if ((reduce(1,SJ2)!=1)||(dim(SJ2)!=3)) { print("K00_V27_R3_FAIL=FRESH_J2_CONTROL"); quit; }',
        "ideal M0=d0_1,d1_1,d2_1,d3_1,d4_1,d5_1; ideal G0=std(M0); int originbad=0; int rr; int cc;",
        "for (rr=1;rr<=7;rr++) { for (cc=1;cc<=7;cc++) { if (reduce(A[rr,cc],G0)!=0) { originbad++; } } }",
        "for (mi=1;mi<=size(B);mi++) { if (reduce(B[mi],G0)!=0) { originbad++; } }",
        "for (mi=1;mi<=size(I2A);mi++) { if (reduce(I2A[mi],G0)!=0) { originbad++; } }",
        'if (originbad!=0) { print("K00_V27_R3_FAIL=ORIGIN_CONTROL"); quit; }',
        "ideal BM=B; BM[1]=BM[1]+1; ideal I2OM=I2A; I2OM[ipick2]=I2OM[ipick2]+1;",
        'if ((reduce(BM[1],G0)==0)||(reduce(I2OM[ipick2],G0)==0)) { print("K00_V27_R3_FAIL=ORIGIN_MUTATIONS"); quit; }',
        "ideal I2MOD=reduce(I2A,SJ2); int i2outside=0; for (mi=1;mi<=size(I2MOD);mi++) { if (I2MOD[mi]!=0) { i2outside++; } }",
        "ideal J1=J2+I2A;",
    ]
    branch = output / "base2_r3_branch.sing"
    branch.write_text("\n".join(definitions + [
        "ideal S=slimgb(J1); poly N1=reduce(1,S); int D=dim(S);",
        'if (N1==0) { print("K00_V27_R3_FAIL=UNIT_CONTRADICTS_EXACT_ORIGIN"); quit; }',
        'if ((N1!=1)||(D<0)||(D>3)) { print("K00_V27_R3_FAIL=PROPER_MARKERS"); quit; }',
        ('print("K00_V27_R3_PREFLIGHT=PROPER"); '
         'print("K00_V27_R3_DIM="+string(D)); '
         'print("K00_V27_R3_NGEN="+string(size(J1))); '
         'print("K00_V27_R3_I2PICK="+string(ipick2)); '
         'print("K00_V27_R3_I2OUTSIDE="+string(i2outside)); quit;'),
    ]) + "\n")
    require_nonempty(branch)
    branch_stdout = output / "base2_r3_branch.stdout"
    branch_stderr = output / "base2_r3_branch.stderr"
    artifacts = [labels, branch]
    try:
        markers = run_singular(
            singular, branch, branch_stdout, branch_stderr, args.timeout)
    except ResourceCap:
        artifacts.extend([branch_stdout, branch_stderr])
        emit_cap(output, lane, "SLIMGB_R3_PREFLIGHT", branch, artifacts)
        return
    artifacts.extend([branch_stdout, branch_stderr])
    parsed = {
        name: re.search(rf"K00_V27_R3_{name}=(-?\d+)", markers)
        for name in ("DIM", "NGEN", "I2PICK", "I2OUTSIDE")
    }
    if "K00_V27_R3_PREFLIGHT=PROPER" not in markers or \
            any(match is None for match in parsed.values()):
        fail("R3 preflight marker missing")
    values = {name: int(match.group(1)) for name, match in parsed.items()
              if match is not None}
    if values["DIM"] < 0 or values["DIM"] > 3 or values["NGEN"] <= 0 or \
            values["I2PICK"] <= 0 or values["I2OUTSIDE"] < 0:
        fail(("R3 preflight value mismatch", values))
    basis = output / "BASE2_R3_STANDARD_BASIS.txt"
    transform = output / "BASE2_R3_TRANSFORM.matrix"
    producer = output / "base2_r3_proper_tracked.sing"
    producer.write_text("\n".join(definitions + [
        "matrix T; ideal G=liftstd(J1,T);",
        (f'if ((nrows(T)!={values["NGEN"]})||(ncols(T)!=size(G))) {{ '
         'print("K00_V27_R3_FAIL=TRACKED_SHAPE"); quit; }'),
        "matrix TREPLAY=matrix(J1)*T-matrix(G); int treplaybad=0; int tc;",
        "for (tc=1;tc<=ncols(TREPLAY);tc++) { if (TREPLAY[1,tc]!=0) { treplaybad++; } }",
        'if (treplaybad) { print("K00_V27_R3_FAIL=TRACKED_IDENTITY"); quit; }',
        (f'if ((reduce(1,G)!=1)||(dim(G)!={values["DIM"]})) {{ '
         'print("K00_V27_R3_FAIL=TRACKED_PROPER"); quit; }'),
        "int pickr=0; int pickc=0;",
        (f"for (cc=1;cc<=ncols(T);cc++) {{ for (rr=1;rr<={values['NGEN']};rr++) "
         "{ if ((pickr==0)&&(J1[rr]!=0)&&(T[rr,cc]!=0)) { pickr=rr; pickc=cc; } } }"),
        'if (pickr==0) { print("K00_V27_R3_FAIL=TRANSFORM_PICK"); quit; }',
        "matrix TDROP=T; TDROP[pickr,pickc]=0; matrix MDROP=matrix(J1)*TDROP-matrix(G); int dropbad=0;",
        "for (tc=1;tc<=ncols(MDROP);tc++) { if (MDROP[1,tc]!=0) { dropbad++; } }",
        'if (dropbad==0) { print("K00_V27_R3_FAIL=TRANSFORM_DROP"); quit; }',
        "matrix TADD=T; TADD[pickr,pickc]=TADD[pickr,pickc]+1; matrix MADD=matrix(J1)*TADD-matrix(G); int addbad=0;",
        "for (tc=1;tc<=ncols(MADD);tc++) { if (MADD[1,tc]!=0) { addbad++; } }",
        'if (addbad==0) { print("K00_V27_R3_FAIL=TRANSFORM_ADD"); quit; }',
        "ideal JUNIT=J1,1; if (reduce(1,std(JUNIT))!=0) { print(\"K00_V27_R3_FAIL=FORCED_UNIT\"); quit; }",
        f'write("{qpath(basis)}",string(G));',
        f'write("{qpath(transform)}",string(T));',
        ('print("K00_V27_R3_PRODUCER=PASS"); '
         'print("K00_V27_R3_GSIZE="+string(size(G))); '
         'print("K00_V27_R3_TPICKR="+string(pickr)); '
         'print("K00_V27_R3_TPICKC="+string(pickc)); quit;'),
    ]) + "\n")
    require_nonempty(producer)
    producer_stdout = output / "base2_r3_proper_tracked.stdout"
    producer_stderr = output / "base2_r3_proper_tracked.stderr"
    try:
        producer_markers = run_singular(
            singular, producer, producer_stdout, producer_stderr, args.timeout)
    except ResourceCap:
        artifacts.extend([producer, producer_stdout, producer_stderr])
        emit_cap(output, lane, "TRACKED_R3_LIFTSTD", producer, artifacts)
        return
    require_nonempty(basis)
    require_nonempty(transform)
    tracked = {
        name: re.search(rf"K00_V27_R3_{name}=(\d+)", producer_markers)
        for name in ("GSIZE", "TPICKR", "TPICKC")
    }
    if "K00_V27_R3_PRODUCER=PASS" not in producer_markers or \
            any(match is None for match in tracked.values()):
        fail("R3 tracked producer marker missing")
    tracked_values = {name: int(match.group(1)) for name, match in tracked.items()
                      if match is not None}
    replay = output / "base2_r3_proper_replay.sing"
    replay.write_text("\n".join(definitions + [
        f"ideal Graw={basis.read_text().strip()};",
        (f"matrix T[{values['NGEN']}][{tracked_values['GSIZE']}]="
         f"{transform.read_text().strip()};"),
        "matrix TREPLAY=matrix(J1)*T-matrix(Graw); int replaybad=0; int tc;",
        "for (tc=1;tc<=ncols(TREPLAY);tc++) { if (TREPLAY[1,tc]!=0) { replaybad++; } }",
        'if (replaybad) { print("K00_V27_R3_FAIL=SERIALIZED_IDENTITY"); quit; }',
        "ideal G=std(Graw); ideal BNF=reduce(B,G); ideal I5NF=reduce(I5A,G); ideal I4NF=reduce(I4A,G); ideal I3NF=reduce(I3A,G); ideal I2NF=reduce(I2A,G);",
        "int reversebad=0; int ri;",
        "for (ri=1;ri<=size(BNF);ri++) { if (BNF[ri]!=0) { reversebad++; } }",
        "for (ri=1;ri<=size(I5NF);ri++) { if (I5NF[ri]!=0) { reversebad++; } }",
        "for (ri=1;ri<=size(I4NF);ri++) { if (I4NF[ri]!=0) { reversebad++; } }",
        "for (ri=1;ri<=size(I3NF);ri++) { if (I3NF[ri]!=0) { reversebad++; } }",
        "for (ri=1;ri<=size(I2NF);ri++) { if (I2NF[ri]!=0) { reversebad++; } }",
        'if (reversebad) { print("K00_V27_R3_FAIL=FULL_LITERAL_REVERSE"); quit; }',
        (f'if ((reduce(1,G)!=1)||(dim(G)!={values["DIM"]})) {{ '
         'print("K00_V27_R3_FAIL=SERIALIZED_PROPER"); quit; }'),
        (f"matrix TDROP=T; TDROP[{tracked_values['TPICKR']},{tracked_values['TPICKC']}]=0; "
         "matrix MDROP=matrix(J1)*TDROP-matrix(Graw); int dropbad=0;"),
        "for (tc=1;tc<=ncols(MDROP);tc++) { if (MDROP[1,tc]!=0) { dropbad++; } }",
        'if (dropbad==0) { print("K00_V27_R3_FAIL=SERIALIZED_DROP"); quit; }',
        (f"matrix TADD=T; TADD[{tracked_values['TPICKR']},{tracked_values['TPICKC']}]=TADD[{tracked_values['TPICKR']},{tracked_values['TPICKC']}]+1; "
         "matrix MADD=matrix(J1)*TADD-matrix(Graw); int addbad=0;"),
        "for (tc=1;tc<=ncols(MADD);tc++) { if (MADD[1,tc]!=0) { addbad++; } }",
        'if (addbad==0) { print("K00_V27_R3_FAIL=SERIALIZED_ADD"); quit; }',
        'print("K00_V27_R3_FULL_LITERAL_REVERSE=PASS"); print("K00_V27_R3_SECOND_PROCESS=PASS"); quit;',
    ]) + "\n")
    require_nonempty(replay)
    replay_stdout = output / "base2_r3_proper_replay.stdout"
    replay_stderr = output / "base2_r3_proper_replay.stderr"
    try:
        replay_markers = run_singular(
            singular, replay, replay_stdout, replay_stderr,
            min(args.timeout, 3600))
    except ResourceCap:
        artifacts.extend([producer, producer_stdout, producer_stderr, basis,
                          transform, replay, replay_stdout, replay_stderr])
        emit_cap(output, lane, "SERIALIZED_R3_REPLAY", replay, artifacts)
        return
    if "K00_V27_R3_FULL_LITERAL_REVERSE=PASS" not in replay_markers or \
            "K00_V27_R3_SECOND_PROCESS=PASS" not in replay_markers:
        fail("R3 serialized replay marker missing")
    artifacts.extend([producer, producer_stdout, producer_stderr, basis,
                      transform, replay, replay_stdout, replay_stderr])
    for artifact in artifacts:
        if artifact.suffix == ".stderr":
            if artifact.read_bytes():
                fail(("nonempty Singular stderr", artifact.name))
        else:
            require_nonempty(artifact)
    payload = {
        "status": STATUS,
        "lifecycle": "PRODUCER_UNREVIEWED_SPECULATIVE_ROLLBACK_BASE4_R1_BASE3_R2",
        "field": "Q_exact",
        "registered_aws_lane": lane,
        "singular_version": version,
        "J1base_unit": False,
        "rank_le_1_geometric_points_survive": True,
        "exact_affine_dimension": values["DIM"],
        "I2_entries_nonzero_mod_fresh_J2base_basis": values["I2OUTSIDE"],
        "I2_contained_in_J2base": values["I2OUTSIDE"] == 0,
        "J1base_equals_J2base": values["I2OUTSIDE"] == 0,
        "fresh_R1_R2_controls": {
            "J4_J3_J2_proper_dimension": 3,
            "I4_outside_J4": 0,
            "I3_outside_J3": 0,
        },
        "literal_minor_census": {
            "I6A": {"total": 49, "nonzero": 0},
            "I5A": {"total": 441, "nonzero": 90},
            "I4A": {"total": 1225, "nonzero": 594},
            "I3A": {"total": 1225, "nonzero": 813},
            "I2A": {"total": 441, "nonzero": 351},
        },
        "origin_control": {
            "A_entries": 49, "B_generators": 7,
            "I2_stored_generators": 351, "all_vanish": True,
            "unit_endpoint_is_contradiction": True,
        },
        "standard_basis_size": tracked_values["GSIZE"],
        "full_literal_minor_reverse_inclusion": True,
        "serialized_second_process_replay": True,
        "I2_generator_deletion_mutation": True,
        "origin_add_one_mutations": True,
        "transform_drop_add_mutations": True,
        "source_hashes": PINNED_SHA256,
        "corrected_useful_point_target": (
            "NONZERO_OR_PROJECTIVE_OR_SOURCE_OPEN_OR_FULL_P6_COMPATIBLE"
        ),
        "sampled_pencil_claims_consumed": False,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in artifacts
        },
        "scope": "EXACT_SIX_VARIABLE_V27_R3_B_PLUS_I2A_RECURSION_ONLY",
        "firewall": (
            "NO_NONZERO_PROJECTIVE_POINT_NO_SOURCE_OPEN_POINT_NO_FULL_P6_"
            "NO_GRADE7_NO_JET_NO_ARC_NO_CLOSURE_NO_COUNTEREXAMPLE_NO_JC2"
        ),
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V27_R3=" + STATUS)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
