#!/usr/bin/env python3
"""Exact AWS-only K00 V27 R2 recursion: test B+I3(A)."""

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
V26_PREPASS_REL = V26_REL + "/aws_box02_r1f_exact_prepass/output"
R1_REL = CASE_REL + "/aws_r6a_r1_exact_base4"

PINNED_SHA256 = {
    COMPILED_REL + "/ATLAS_EXACT_POLYNOMIALS.json":
        "d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501",
    COMPILED_REL + "/COMPILED_SOURCE.sha256":
        "5de20da0d3501db668fca38db3c678ba4719745e3df7b32d0d0a8d2867e4da32",
    COMPILED_REL + "/RESULT.json":
        "f1a6f1fc988fc77816daaab13b294b1321de7e476d2891cf7fbfa2e033868d97",
    V26_REL + "/RESULT_V26R1F_EXACT_PREPASS.md":
        "86742147085332881b3c44ba041172ac5a032d656df3992ceff5da7d0a5b46dc",
    V26_PREPASS_REL + "/RESULT.json":
        "f455c7b2177eb260df2ebfa97f174381591792683c80fdeb779f1184f6e6d70e",
    "xmodel/max12-812-order2-k00-v26r1f-leading-base-rank-prepass-hostile-review-20260827.md":
        "6790ec5c06c6bbdca5e08ddf0194a88b5b68d85b6f74070477ae12ba85701865",
    "xmodel/max12-812-order2-k00-v24r6r1-leading-base-dw-hostile-review-sol-ultra-20260827.md":
        "f9d2afcb01c1ad1161783d0ff51d9d47d1a6aa5831b508936072f0c9170012b9",
    "xmodel/promotion-crossaudit-d5g-r6-k00r6r1-opus5-20260827.md":
        "d9e653150d14bc2791e366c2e425de5790f0f4390ab5790469bb9fe6ef4b644b",
    "xmodel/max12-812-order2-k00-v27-rank-compressed-atlas-successor-design-sol-20260827.md":
        "a1b1865ab5d491b04d3876a72328893b6f25e7f867ace3b9c44f80ff551100af",
    CASE_REL + "/SOURCE_FREEZE_BASE4.sha256":
        "7ffc61ba3aa1286205f3fc6e9f8b77792e3eff6f6790d91b737beb8d0f18d060",
    CASE_REL + "/HARVEST_REPLAY_BASE4_R1.sha256":
        "279bdc80febfe7a309bcd279f30caeb25d58e74476aa7bcf62dd13557bbbe2f4",
    CASE_REL + "/RESULT_V27_BASE4_R1_EXACT_PREPASS.md":
        "19c8795589ce076c2414474a6341c7929d578958ea122a6745f26ea6ab46bd9c",
    CASE_REL + "/REVIEW_PACKET_BASE4_R1.sha256":
        "41d1107589f33b7f7fab4ec5cac6e47ffc72368dfeeb93981ae2e921a9eb0205",
    R1_REL + "/output/RESULT.json":
        "f886f17ca2c626ec476e695418002185d2223d556721759900f6cdbe89635073",
    R1_REL + "/EVIDENCE.sha256":
        "3e7fac6cd993c8afa581fa037d6f69df757a6a8db08ccdeda6c5770d1d7e8d9c",
    R1_REL + "/output/BASE4_STANDARD_BASIS.txt":
        "c8aa23e46f909e70c2c8d302ca67a415496df9a969f99817d2ef593f60f614c0",
}

COMPILER_STATUS = "PASS_V26_FITTING_ATLAS_COMPILED_NO_STRATUM_DECISION"
R1_STATUS = "PASS_V27_BASE4_EXACT_RANK_LE3_SURVIVES_PRODUCER_UNREVIEWED"
UNIT_STATUS = "PASS_V27_R2_EXACT_RANK3_PURE_PRODUCER_UNREVIEWED_ROLLBACK_R1"
PROPER_STATUS = (
    "PASS_V27_R2_EXACT_RANK_LE2_SURVIVES_PRODUCER_UNREVIEWED_ROLLBACK_R1"
)


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
        fail(("missing or empty replay byte artifact", str(path)))


def validate_sources(root: Path) -> dict:
    for relative, expected in PINNED_SHA256.items():
        path = root / relative
        if not path.is_file() or digest(path) != expected:
            fail(("pinned source mismatch", relative, expected,
                  digest(path) if path.is_file() else "MISSING"))

    manifest = root / (COMPILED_REL + "/COMPILED_SOURCE.sha256")
    entries = {}
    for line in manifest.read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
        if match is None:
            fail(("malformed V26 compiled manifest", line))
        entries[match.group(2)] = match.group(1)
    atlas_relative = COMPILED_REL + "/ATLAS_EXACT_POLYNOMIALS.json"
    if entries.get("ATLAS_EXACT_POLYNOMIALS.json") != \
            PINNED_SHA256[atlas_relative]:
        fail("V26 compiled manifest does not bind frozen atlas")

    compiler_result = json.loads(
        (root / (COMPILED_REL + "/RESULT.json")).read_text())
    if compiler_result.get("status") != COMPILER_STATUS or \
            compiler_result.get("A_shape") != [7, 7] or \
            compiler_result.get("generic_rank_A") != 5:
        fail("V26 compiler endpoint metadata mismatch")
    stats = compiler_result.get("A_minor_statistics", {})
    expected_stats = {
        "3": (1225, 412, 725),
        "4": (1225, 631, 491),
        "5": (441, 351, 54),
        "6": (49, 49, 0),
    }
    for rank, (total, zero, unique_nonzero) in expected_stats.items():
        item = stats.get(rank, {})
        if item.get("total") != total or item.get("zero") != zero or \
                item.get("unique_nonzero_exact_polynomials") != unique_nonzero:
            fail(("V26 minor census mismatch", rank, item))

    r1 = json.loads((root / (R1_REL + "/output/RESULT.json")).read_text())
    if r1.get("status") != R1_STATUS or r1.get("J3base_unit") is not False or \
            r1.get("exact_affine_dimension") != 3 or \
            r1.get("I4_entries_nonzero_mod_fresh_J4base_basis") != 0 or \
            r1.get("full_literal_minor_reverse_inclusion") is not True or \
            r1.get("serialized_second_process_replay") is not True:
        fail("BASE4 R1 endpoint metadata mismatch")

    atlas = json.loads((root / atlas_relative).read_text())
    matrix = atlas.get("A")
    if not isinstance(matrix, list) or len(matrix) != 7 or \
            any(not isinstance(row, list) or len(row) != 7 for row in matrix):
        fail("frozen A is not 7 x 7")
    if atlas.get("honest_newest_variables") != [
            "d0_6", "d1_6", "d2_6", "d3_6", "d4_6", "d5_6", "k10_3"]:
        fail("frozen atlas newest-variable metadata mismatch")
    qlist = atlas.get("Q1_to_Q6")
    if not isinstance(qlist, list) or len(qlist) != 6:
        fail("six-nonzero-grade2 list mismatch")
    return atlas


def poly_text(item: dict) -> str:
    value = item.get("singular")
    if not isinstance(value, str) or not value:
        fail("compiled exact polynomial serialization missing")
    return value


def matrix_line(name: str, matrix: list[list[dict]]) -> str:
    return f"matrix {name}[7][7]=" + ",".join(
        f"({poly_text(entry)})" for row in matrix for entry in row) + ";"


def emit_minor_labels(output: Path) -> Path:
    path = output / "MINOR_SOURCE_LABELS_RANK3_TO_6.json"
    labels = {}
    for rank in (3, 4, 5, 6):
        labels[str(rank)] = [
            {"rows_one_based": list(rows), "columns_one_based": list(columns)}
            for rows in combinations(range(1, 8), rank)
            for columns in combinations(range(1, 8), rank)
        ]
    path.write_text(json.dumps({
        "matrix": "A_frozen_7_by_7",
        "meaning": "complete literal row/column subset sets; no compressed substitution",
        "ordering": "lexicographic labels only; every label is consumed",
        "ranks": labels,
    }, sort_keys=True, indent=2) + "\n")
    require_nonempty(path)
    return path


def singular_version(singular: str) -> str:
    completed = subprocess.run(
        [singular, "--version"], text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, timeout=30, check=False)
    first = completed.stdout.splitlines()[0] if completed.stdout else ""
    if completed.returncode != 0 or not first:
        fail("Singular version custody missing")
    return first


def run_singular(singular: str, script: Path, stdout: Path, stderr: Path,
                 timeout: int) -> str:
    try:
        completed = subprocess.run(
            [singular, "-q", str(script)], cwd=script.parent, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    except subprocess.TimeoutExpired as error:
        captured_out = error.stdout or ""
        captured_err = error.stderr or ""
        if isinstance(captured_out, bytes):
            captured_out = captured_out.decode(errors="replace")
        if isinstance(captured_err, bytes):
            captured_err = captured_err.decode(errors="replace")
        stdout.write_text(captured_out)
        stderr.write_text(captured_err)
        raise ResourceCap((script.name, timeout)) from error
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    diagnostics = re.compile(
        r"(?mi)^\s*\?|// \*\*|warning|error occurred|K00_V27_R2_FAIL=")
    if completed.returncode != 0 or completed.stderr or \
            not completed.stdout.strip() or diagnostics.search(completed.stdout):
        fail(("exact V27 R2 engine/replay failure", script.name,
              completed.returncode, completed.stderr[-2000:],
              completed.stdout[-4000:]))
    return completed.stdout


def emit_cap(output: Path, lane: str, stage: str, script: Path,
             artifacts: list[Path]) -> None:
    payload = {
        "status": "RESOURCE_CAP_NO_VERDICT",
        "registered_aws_lane": lane,
        "stage": stage,
        "script_sha256": digest(script),
        "rollback_dependency": "BASE4_R1_PRODUCER_UNREVIEWED",
        "source_hashes": PINNED_SHA256,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in artifacts if path.is_file()
        },
        "scope": "NO_EXACT_V27_R2_RANK_RECURSION_VERDICT",
        "firewall": "NO_FULL_P6_NO_GRADE7_NO_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V27_R2=RESOURCE_CAP_NO_VERDICT")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_root", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=int, default=21000)
    args = parser.parse_args()

    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if platform.system() != "Linux" or not vendor.is_file() or \
            vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V27 R2 exact prepass refused host")
    lane = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not lane.startswith("max12_812_order2_u2_62_k00_v27_r2_base3_"):
        fail("registered V27 R2 AWS lane missing or malformed")
    if args.timeout <= 0 or args.timeout > 21000:
        fail("inner timeout outside preregistered cap")

    source_root = args.source_root.resolve()
    atlas = validate_sources(source_root)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    labels_path = emit_minor_labels(output)
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    engine_version = singular_version(singular)

    qlist = atlas["Q1_to_Q6"]
    definitions = [
        "ring R=0,(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1),dp;",
        matrix_line("A", atlas["A"]),
        "ideal B=" + ",".join(f"({poly_text(item)})" for item in qlist) +
        f",({poly_text(atlas['F10'])});",
        'if (size(B)!=7) { print("K00_V27_R2_FAIL=BASE_GENERATOR_CENSUS"); quit; }',
        "ideal I6A=minor(A,6);",
        'if (size(I6A)!=0) { print("K00_V27_R2_FAIL=I6_STORED_NONZERO_CENSUS"); quit; }',
        "ideal I5A=minor(A,5);",
        'if (size(I5A)!=90) { print("K00_V27_R2_FAIL=I5_STORED_NONZERO_CENSUS"); quit; }',
        "int i5nonzero=0; int mi; for (mi=1;mi<=size(I5A);mi++) { if (I5A[mi]!=0) { i5nonzero++; } }",
        'if (i5nonzero!=90) { print("K00_V27_R2_FAIL=I5_NONZERO_CENSUS"); quit; }',
        "ideal I4A=minor(A,4);",
        'if (size(I4A)!=594) { print("K00_V27_R2_FAIL=I4_STORED_NONZERO_CENSUS"); quit; }',
        "int i4nonzero=0; for (mi=1;mi<=size(I4A);mi++) { if (I4A[mi]!=0) { i4nonzero++; } }",
        'if (i4nonzero!=594) { print("K00_V27_R2_FAIL=I4_NONZERO_CENSUS"); quit; }',
        "ideal I3A=minor(A,3);",
        'if (size(I3A)!=813) { print("K00_V27_R2_FAIL=I3_STORED_NONZERO_CENSUS"); quit; }',
        "int i3nonzero=0; int ipick3=0; for (mi=1;mi<=size(I3A);mi++) { if (I3A[mi]!=0) { i3nonzero++; if (ipick3==0) { ipick3=mi; } } }",
        'if ((i3nonzero!=813)||(ipick3==0)) { print("K00_V27_R2_FAIL=I3_NONZERO_CENSUS"); quit; }',
        "ideal I3M=I3A; I3M[ipick3]=0;",
        'if ((I3M[ipick3]!=0)||(I3A[ipick3]==I3M[ipick3])) { print("K00_V27_R2_FAIL=I3_DELETE_MUTATION"); quit; }',
        "ideal CTRLproper=d0_1; ideal GCTRLproper=std(CTRLproper);",
        'if (reduce(1,GCTRLproper)==0) { print("K00_V27_R2_FAIL=KNOWN_PROPER_CONTROL"); quit; }',
        "ideal CTRLunit=d0_1,1; ideal GCTRLunit=std(CTRLunit);",
        'if (reduce(1,GCTRLunit)!=0) { print("K00_V27_R2_FAIL=FORCED_UNIT_CONTROL"); quit; }',
        "ideal J4=B+I5A; ideal SJ4=std(J4); poly J4N1=reduce(1,SJ4); int J4D=dim(SJ4);",
        'if ((J4N1!=1)||(J4D!=3)) { print("K00_V27_R2_FAIL=V26_J4_FRESH_CONTROL"); quit; }',
        "ideal I4MODJ4=reduce(I4A,SJ4); int i4outside=0; for (mi=1;mi<=size(I4MODJ4);mi++) { if (I4MODJ4[mi]!=0) { i4outside++; } }",
        'if (i4outside!=0) { print("K00_V27_R2_FAIL=BASE4_R1_FRESH_EQUALITY_CONTROL"); quit; }',
        "ideal J3=J4+I4A; ideal SJ3=std(J3); poly J3N1=reduce(1,SJ3); int J3D=dim(SJ3);",
        'if ((J3N1!=1)||(J3D!=3)) { print("K00_V27_R2_FAIL=BASE4_R1_FRESH_PROPER_CONTROL"); quit; }',
        "ideal I3MODJ3=reduce(I3A,SJ3); int i3outside=0; for (mi=1;mi<=size(I3MODJ3);mi++) { if (I3MODJ3[mi]!=0) { i3outside++; } }",
        "ideal J2=J3+I3A;",
    ]

    preflight = output / "base3_r2_branch.sing"
    preflight.write_text("\n".join(definitions + [
        "ideal S=slimgb(J2); poly N1=reduce(1,S); int D=dim(S);",
        "if (N1==0)", "{",
        '  if (D!=-1) { print("K00_V27_R2_FAIL=UNIT_DIMENSION"); quit; }',
        ('  print("K00_V27_R2_PREFLIGHT=UNIT"); '
         'print("K00_V27_R2_DIM=-1"); '
         'print("K00_V27_R2_NGEN="+string(size(J2))); '
         'print("K00_V27_R2_I3PICK="+string(ipick3)); '
         'print("K00_V27_R2_I3OUTSIDE="+string(i3outside)); quit;'),
        "}",
        'if ((N1!=1)||(D<0)||(D>3)) { print("K00_V27_R2_FAIL=PROPER_MARKERS"); quit; }',
        ('print("K00_V27_R2_PREFLIGHT=PROPER"); '
         'print("K00_V27_R2_DIM="+string(D)); '
         'print("K00_V27_R2_NGEN="+string(size(J2))); '
         'print("K00_V27_R2_I3PICK="+string(ipick3)); '
         'print("K00_V27_R2_I3OUTSIDE="+string(i3outside)); quit;'),
    ]) + "\n")
    require_nonempty(preflight)
    pre_stdout = output / "base3_r2_branch.stdout"
    pre_stderr = output / "base3_r2_branch.stderr"
    artifacts = [labels_path, preflight]
    try:
        markers = run_singular(
            singular, preflight, pre_stdout, pre_stderr, args.timeout)
    except ResourceCap:
        artifacts.extend([pre_stdout, pre_stderr])
        emit_cap(output, lane, "SLIMGB_R2_PREFLIGHT", preflight, artifacts)
        return
    artifacts.extend([pre_stdout, pre_stderr])

    parsed = {
        name: re.search(rf"K00_V27_R2_{name}=(-?\d+)", markers)
        for name in ("DIM", "NGEN", "I3PICK", "I3OUTSIDE")
    }
    if any(value is None for value in parsed.values()):
        fail("V27 R2 preflight custody marker missing")
    values = {
        name: int(match.group(1))
        for name, match in parsed.items() if match is not None
    }
    if values["NGEN"] <= 0 or values["I3PICK"] <= 0 or \
            values["I3OUTSIDE"] < 0:
        fail(("V27 R2 generator/minor control census", values))

    if "K00_V27_R2_PREFLIGHT=UNIT" in markers:
        cert_path = output / "BASE3_R2_UNIT_COEFFICIENTS.matrix"
        producer = output / "base3_r2_unit_lift.sing"
        producer.write_text("\n".join(definitions + [
            'matrix U; matrix C=lift(J2,ideal(1),U,"slimgb");',
            (f'if ((nrows(C)!={values["NGEN"]})||(ncols(C)!=1)||'
             '(nrows(U)!=1)||(ncols(U)!=1)) { '
             'print("K00_V27_R2_FAIL=UNIT_LIFT_SHAPE"); quit; }'),
            'if (U[1,1]!=1) { print("K00_V27_R2_FAIL=UNIT_LIFT_U"); quit; }',
            ('matrix UID=matrix(J2)*C-matrix(ideal(1)); '
             'if (UID[1,1]!=0) { print("K00_V27_R2_FAIL=UNIT_IDENTITY"); quit; }'),
            "int pick=0; int jj;",
            (f"for (jj=1;jj<={values['NGEN']};jj++) {{ if ((pick==0)&&"
             "(J2[jj]!=0)&&(C[jj,1]!=0)) { pick=jj; } }"),
            'if (pick==0) { print("K00_V27_R2_FAIL=UNIT_MUTATION_PICK"); quit; }',
            "matrix CDROP=C; CDROP[pick,1]=0;",
            ('matrix UDROPD=matrix(J2)*CDROP-matrix(ideal(1)); '
             'if (UDROPD[1,1]==0) { print("K00_V27_R2_FAIL=UNIT_DROP_MUTATION"); quit; }'),
            "matrix CADD=C; CADD[pick,1]=CADD[pick,1]+1;",
            ('matrix UADDD=matrix(J2)*CADD-matrix(ideal(1)); '
             'if (UADDD[1,1]==0) { print("K00_V27_R2_FAIL=UNIT_ADD_MUTATION"); quit; }'),
            f'write("{qpath(cert_path)}",string(C));',
            ('print("K00_V27_R2_UNIT_PRODUCER=1"); '
             'print("K00_V27_R2_CPICK="+string(pick)); quit;'),
        ]) + "\n")
        require_nonempty(producer)
        producer_stdout = output / "base3_r2_unit_lift.stdout"
        producer_stderr = output / "base3_r2_unit_lift.stderr"
        try:
            producer_markers = run_singular(
                singular, producer, producer_stdout, producer_stderr,
                args.timeout)
        except ResourceCap:
            artifacts.extend([producer, producer_stdout, producer_stderr])
            emit_cap(output, lane, "DIRECT_R2_UNIT_LIFT", producer, artifacts)
            return
        pick_match = re.search(r"K00_V27_R2_CPICK=(\d+)", producer_markers)
        require_nonempty(cert_path)
        if "K00_V27_R2_UNIT_PRODUCER=1" not in producer_markers or \
                pick_match is None:
            fail("V27 R2 unit certificate custody missing")
        pick = int(pick_match.group(1))
        replay = output / "base3_r2_unit_replay.sing"
        replay.write_text("\n".join(definitions + [
            f"matrix C[{values['NGEN']}][1]={cert_path.read_text().strip()};",
            ('matrix UID=matrix(J2)*C-matrix(ideal(1)); '
             'if (UID[1,1]!=0) { print("K00_V27_R2_FAIL=SERIALIZED_UNIT_IDENTITY"); quit; }'),
            f"matrix CDROP=C; CDROP[{pick},1]=0;",
            ('matrix UDROPD=matrix(J2)*CDROP-matrix(ideal(1)); '
             'if (UDROPD[1,1]==0) { print("K00_V27_R2_FAIL=SERIALIZED_DROP_MUTATION"); quit; }'),
            f"matrix CADD=C; CADD[{pick},1]=CADD[{pick},1]+1;",
            ('matrix UADDD=matrix(J2)*CADD-matrix(ideal(1)); '
             'if (UADDD[1,1]==0) { print("K00_V27_R2_FAIL=SERIALIZED_ADD_MUTATION"); quit; }'),
            'print("K00_V27_R2_UNIT_SECOND_PROCESS_REPLAY=1"); quit;',
        ]) + "\n")
        require_nonempty(replay)
        replay_stdout = output / "base3_r2_unit_replay.stdout"
        replay_stderr = output / "base3_r2_unit_replay.stderr"
        try:
            replay_markers = run_singular(
                singular, replay, replay_stdout, replay_stderr,
                min(args.timeout, 3600))
        except ResourceCap:
            artifacts.extend([
                producer, producer_stdout, producer_stderr, cert_path,
                replay, replay_stdout, replay_stderr])
            emit_cap(output, lane, "SERIALIZED_R2_UNIT_REPLAY", replay,
                     artifacts)
            return
        if "K00_V27_R2_UNIT_SECOND_PROCESS_REPLAY=1" not in replay_markers:
            fail("V27 R2 unit second-process marker missing")
        artifacts.extend([
            producer, producer_stdout, producer_stderr, cert_path,
            replay, replay_stdout, replay_stderr])
        status = UNIT_STATUS
        branch = "UNIT_B_PLUS_I5A_PLUS_I4A_PLUS_I3A"
        outcome = {
            "J2base_unit": True,
            "rank_le_2_geometric_points_survive": False,
            "rank_pure_on_provisional_J3base": 3,
            "unit_certificate_entries": values["NGEN"],
            "certificate_mutation_index": pick,
            "serialized_second_process_replay": True,
        }
    elif "K00_V27_R2_PREFLIGHT=PROPER" in markers:
        basis_path = output / "BASE3_R2_STANDARD_BASIS.txt"
        transform_path = output / "BASE3_R2_TRANSFORM.matrix"
        producer = output / "base3_r2_proper_tracked.sing"
        producer.write_text("\n".join(definitions + [
            "matrix T; ideal G=liftstd(J2,T);",
            (f'if ((nrows(T)!={values["NGEN"]})||(ncols(T)!=size(G))) {{ '
             'print("K00_V27_R2_FAIL=TRACKED_BASIS_SHAPE"); quit; }'),
            ('matrix TREPLAY=matrix(J2)*T-matrix(G); int treplay_bad=0; int tc; '
             'for (tc=1;tc<=ncols(TREPLAY);tc++) { '
             'if (TREPLAY[1,tc]!=0) { treplay_bad++; } }'),
            'if (treplay_bad) { print("K00_V27_R2_FAIL=TRACKED_BASIS_IDENTITY"); quit; }',
            "poly N1=reduce(1,G); int D=dim(G);",
            (f'if ((N1!=1)||(D!={values["DIM"]})||(D<0)) {{ '
             'print("K00_V27_R2_FAIL=TRACKED_PROPER_MARKERS"); quit; }'),
            "int pickr=0; int pickc=0; int rr; int cc;",
            (f"for (cc=1;cc<=ncols(T);cc++) {{ for (rr=1;rr<={values['NGEN']};rr++) "
             "{ if ((pickr==0)&&(J2[rr]!=0)&&(T[rr,cc]!=0)) "
             "{ pickr=rr; pickc=cc; } } }"),
            'if (pickr==0) { print("K00_V27_R2_FAIL=TRANSFORM_MUTATION_PICK"); quit; }',
            "matrix TBAD=T; TBAD[pickr,pickc]=0;",
            ('matrix TMUT=matrix(J2)*TBAD-matrix(G); int tmutation_nonzero=0; '
             'for (tc=1;tc<=ncols(TMUT);tc++) { '
             'if (TMUT[1,tc]!=0) { tmutation_nonzero++; } }'),
            'if (tmutation_nonzero==0) { print("K00_V27_R2_FAIL=TRANSFORM_DROP_MUTATION"); quit; }',
            "ideal JUNIT=J2,1; ideal GUNIT=std(JUNIT);",
            'if (reduce(1,GUNIT)!=0) { print("K00_V27_R2_FAIL=FORCED_UNIT_MUTATION"); quit; }',
            f'write("{qpath(basis_path)}",string(G));',
            f'write("{qpath(transform_path)}",string(T));',
            ('print("K00_V27_R2_PROPER_PRODUCER=1"); '
             'print("K00_V27_R2_GSIZE="+string(size(G))); '
             'print("K00_V27_R2_TPICKR="+string(pickr)); '
             'print("K00_V27_R2_TPICKC="+string(pickc)); quit;'),
        ]) + "\n")
        require_nonempty(producer)
        producer_stdout = output / "base3_r2_proper_tracked.stdout"
        producer_stderr = output / "base3_r2_proper_tracked.stderr"
        try:
            producer_markers = run_singular(
                singular, producer, producer_stdout, producer_stderr,
                args.timeout)
        except ResourceCap:
            artifacts.extend([producer, producer_stdout, producer_stderr])
            emit_cap(output, lane, "TRACKED_R2_PROPER_LIFTSTD", producer,
                     artifacts)
            return
        proper_matches = {
            name: re.search(rf"K00_V27_R2_{name}=(\d+)", producer_markers)
            for name in ("GSIZE", "TPICKR", "TPICKC")
        }
        require_nonempty(basis_path)
        require_nonempty(transform_path)
        if "K00_V27_R2_PROPER_PRODUCER=1" not in producer_markers or \
                any(match is None for match in proper_matches.values()):
            fail("V27 R2 proper tracked custody missing")
        proper_values = {
            name: int(match.group(1))
            for name, match in proper_matches.items() if match is not None
        }
        replay = output / "base3_r2_proper_replay.sing"
        replay.write_text("\n".join(definitions + [
            f"ideal Graw={basis_path.read_text().strip()};",
            (f"matrix T[{values['NGEN']}][{proper_values['GSIZE']}]="
             f"{transform_path.read_text().strip()};"),
            ('matrix TREPLAY=matrix(J2)*T-matrix(Graw); int treplay_bad=0; int tc; '
             'for (tc=1;tc<=ncols(TREPLAY);tc++) { '
             'if (TREPLAY[1,tc]!=0) { treplay_bad++; } }'),
            'if (treplay_bad) { print("K00_V27_R2_FAIL=SERIALIZED_TRACKED_IDENTITY"); quit; }',
            "ideal G=std(Graw);",
            "ideal BNF=reduce(B,G); ideal I5NF=reduce(I5A,G); ideal I4NF=reduce(I4A,G); ideal I3NF=reduce(I3A,G);",
            "int reverse_bad=0; int reverse_i;",
            "for (reverse_i=1;reverse_i<=size(BNF);reverse_i++) { if (BNF[reverse_i]!=0) { reverse_bad++; } }",
            "for (reverse_i=1;reverse_i<=size(I5NF);reverse_i++) { if (I5NF[reverse_i]!=0) { reverse_bad++; } }",
            "for (reverse_i=1;reverse_i<=size(I4NF);reverse_i++) { if (I4NF[reverse_i]!=0) { reverse_bad++; } }",
            "for (reverse_i=1;reverse_i<=size(I3NF);reverse_i++) { if (I3NF[reverse_i]!=0) { reverse_bad++; } }",
            'if (reverse_bad) { print("K00_V27_R2_FAIL=FULL_LITERAL_REVERSE_INCLUSION"); quit; }',
            'print("K00_V27_R2_FULL_LITERAL_REVERSE_INCLUSION=1");',
            "poly N1=reduce(1,G); int D=dim(G);",
            (f'if ((N1!=1)||(D!={values["DIM"]})) {{ '
             'print("K00_V27_R2_FAIL=SERIALIZED_PROPER_MARKERS"); quit; }'),
            (f"matrix TBAD=T; TBAD[{proper_values['TPICKR']},"
             f"{proper_values['TPICKC']}]=0;"),
            ('matrix TMUT=matrix(J2)*TBAD-matrix(Graw); int tmutation_nonzero=0; '
             'for (tc=1;tc<=ncols(TMUT);tc++) { '
             'if (TMUT[1,tc]!=0) { tmutation_nonzero++; } }'),
            'if (tmutation_nonzero==0) { print("K00_V27_R2_FAIL=SERIALIZED_TRANSFORM_MUTATION"); quit; }',
            "ideal JUNIT=J2,1; ideal GUNIT=std(JUNIT);",
            'if (reduce(1,GUNIT)!=0) { print("K00_V27_R2_FAIL=SERIALIZED_FORCED_UNIT"); quit; }',
            'print("K00_V27_R2_PROPER_SECOND_PROCESS_REPLAY=1"); quit;',
        ]) + "\n")
        require_nonempty(replay)
        replay_stdout = output / "base3_r2_proper_replay.stdout"
        replay_stderr = output / "base3_r2_proper_replay.stderr"
        try:
            replay_markers = run_singular(
                singular, replay, replay_stdout, replay_stderr,
                min(args.timeout, 3600))
        except ResourceCap:
            artifacts.extend([
                producer, producer_stdout, producer_stderr, basis_path,
                transform_path, replay, replay_stdout, replay_stderr])
            emit_cap(output, lane, "SERIALIZED_R2_PROPER_REPLAY", replay,
                     artifacts)
            return
        if "K00_V27_R2_PROPER_SECOND_PROCESS_REPLAY=1" not in replay_markers or \
                "K00_V27_R2_FULL_LITERAL_REVERSE_INCLUSION=1" not in replay_markers:
            fail("V27 R2 proper second-process marker missing")
        artifacts.extend([
            producer, producer_stdout, producer_stderr, basis_path,
            transform_path, replay, replay_stdout, replay_stderr])
        status = PROPER_STATUS
        branch = "PROPER_B_PLUS_I5A_PLUS_I4A_PLUS_I3A"
        outcome = {
            "J2base_unit": False,
            "rank_le_2_geometric_points_survive": True,
            "exact_affine_dimension": values["DIM"],
            "standard_basis_size": proper_values["GSIZE"],
            "full_literal_minor_reverse_inclusion": True,
            "serialized_recomputed_standard_basis": True,
            "serialized_second_process_replay": True,
        }
    else:
        fail("V27 R2 preflight branch marker missing")

    for artifact in artifacts:
        if artifact.suffix != ".stderr":
            require_nonempty(artifact)
        elif artifact.read_bytes():
            fail(("nonempty Singular stderr", artifact.name))

    payload = {
        "status": status,
        "lifecycle": "PRODUCER_UNREVIEWED_SPECULATIVE_ROLLBACK_BASE4_R1",
        "branch": branch,
        "field": "Q_exact",
        "ring_variables": [
            "d0_1", "d1_1", "d2_1", "d3_1", "d4_1", "d5_1"],
        "registered_aws_lane": lane,
        "singular_version": engine_version,
        "source_hashes": PINNED_SHA256,
        "rollback_dependency": {
            "claim": "BASE4_R1_PRODUCER_UNREVIEWED_EQUALITY_J3_J4",
            "endpoint_sha256": PINNED_SHA256[R1_REL + "/output/RESULT.json"],
            "report_sha256": PINNED_SHA256[
                CASE_REL + "/RESULT_V27_BASE4_R1_EXACT_PREPASS.md"],
            "consumption": "SCHEDULING_ONLY_FRESHLY_RECOMPUTED_IN_R2",
        },
        "literal_minor_census": {
            "I6A": {"total": 49, "nonzero": 0},
            "I5A": {"total": 441, "nonzero": 90},
            "I4A": {"total": 1225, "nonzero": 594},
            "I3A": {"total": 1225, "nonzero": 813},
        },
        "fresh_BASE4_R1_control": {
            "proper": True,
            "exact_affine_dimension": 3,
            "I4_entries_nonzero_mod_fresh_J4base_basis": 0,
        },
        "I3_entries_nonzero_mod_fresh_J3base_basis": values["I3OUTSIDE"],
        "I3_generator_deletion_mutation": True,
        "certificate_or_transform_mutations": "DROP_AND_ADD_EXACT_IDENTITY_FAILURES",
        **outcome,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in artifacts
        },
        "scope": "EXACT_SIX_VARIABLE_V27_R2_B_PLUS_I3A_RECURSION_ONLY",
        "firewall": (
            "NO_RATIONAL_POINT_NO_FULL_P6_NO_GRADE7_COMPATIBILITY_"
            "NO_LATER_GRADE_NO_JET_NO_ARC_NO_SOURCE_REACHABILITY_"
            "NO_CLOSURE_NO_COUNTEREXAMPLE_NO_JC2"
        ),
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    require_nonempty(result_path)
    print("K00_V27_R2=" + status)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
