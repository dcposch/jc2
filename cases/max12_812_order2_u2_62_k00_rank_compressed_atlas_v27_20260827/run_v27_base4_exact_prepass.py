#!/usr/bin/env python3
"""Exact AWS-only K00 V27 BASE4 rank-purity prepass."""

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
}

COMPILER_STATUS = "PASS_V26_FITTING_ATLAS_COMPILED_NO_STRATUM_DECISION"
V26_STATUS = (
    "PASS_V26R1_EXACT_PREPASS_LOWER_RANK_LOCUS_SURVIVES_"
    "PROVISIONAL_ROLLBACK_TAG"
)
UNIT_STATUS = "PASS_V27_BASE4_EXACT_RANK4_PURE_PRODUCER_UNREVIEWED"
PROPER_STATUS = (
    "PASS_V27_BASE4_EXACT_RANK_LE3_SURVIVES_PRODUCER_UNREVIEWED"
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

    compiled_manifest = root / (COMPILED_REL + "/COMPILED_SOURCE.sha256")
    atlas_name = "ATLAS_EXACT_POLYNOMIALS.json"
    manifest_entries = {}
    for line in compiled_manifest.read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
        if match is None:
            fail(("malformed V26 compiled manifest", line))
        manifest_entries[match.group(2)] = match.group(1)
    if manifest_entries.get(atlas_name) != PINNED_SHA256[
            COMPILED_REL + "/" + atlas_name]:
        fail("V26 compiled manifest does not bind frozen atlas")

    compiler_result = json.loads(
        (root / (COMPILED_REL + "/RESULT.json")).read_text())
    stats = compiler_result.get("A_minor_statistics", {})
    if compiler_result.get("status") != COMPILER_STATUS or \
            compiler_result.get("A_shape") != [7, 7] or \
            compiler_result.get("generic_rank_A") != 5:
        fail("V26 compiler endpoint metadata mismatch")
    expected_stats = {
        "4": (1225, 631, 491),
        "5": (441, 351, 54),
        "6": (49, 49, 0),
    }
    for rank, (total, zero, unique_nonzero) in expected_stats.items():
        item = stats.get(rank, {})
        if item.get("total") != total or item.get("zero") != zero or \
                item.get("unique_nonzero_exact_polynomials") != unique_nonzero:
            fail(("V26 minor census mismatch", rank, item))

    v26_result = json.loads(
        (root / (V26_PREPASS_REL + "/RESULT.json")).read_text())
    if v26_result.get("status") != V26_STATUS or \
            v26_result.get("branch") != "PROPER_B_PLUS_I5A" or \
            v26_result.get("field") != "Q_exact" or \
            v26_result.get("exact_affine_dimension") != 3 or \
            v26_result.get("I6A_exact_zero") is not True or \
            v26_result.get("serialized_second_process_replay") is not True:
        fail("V26R1F endpoint metadata mismatch")

    atlas = json.loads(
        (root / (COMPILED_REL + "/ATLAS_EXACT_POLYNOMIALS.json")).read_text())
    if atlas.get("format") is None or atlas.get("honest_newest_variables") != [
            "d0_6", "d1_6", "d2_6", "d3_6", "d4_6", "d5_6", "k10_3"]:
        fail("frozen atlas metadata mismatch")
    matrix = atlas.get("A")
    if not isinstance(matrix, list) or len(matrix) != 7 or \
            any(not isinstance(row, list) or len(row) != 7 for row in matrix):
        fail("frozen A is not 7 x 7")
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
    path = output / "MINOR_SOURCE_LABELS.json"
    labels = {}
    for rank in (4, 5, 6):
        labels[str(rank)] = [
            {"rows_one_based": list(rows), "columns_one_based": list(columns)}
            for rows in combinations(range(1, 8), rank)
            for columns in combinations(range(1, 8), rank)
        ]
    payload = {
        "matrix": "A_frozen_7_by_7",
        "meaning": "complete literal row/column subset set; no compressed-class substitution",
        "ordering": "lexicographic labels only; target ideal consumes every label",
        "ranks": labels,
    }
    path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
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
        r"(?mi)^\s*\?|// \*\*|warning|error occurred|K00_V27_BASE4_FAIL=")
    if completed.returncode != 0 or completed.stderr or \
            not completed.stdout.strip() or diagnostics.search(completed.stdout):
        fail(("exact BASE4 engine/replay failure", script.name,
              completed.returncode, completed.stderr[-2000:],
              completed.stdout[-4000:]))
    return completed.stdout


def emit_cap(output: Path, lane: str, stage: str, script: Path,
             artifacts: list[Path], source_hashes: dict[str, str]) -> None:
    payload = {
        "status": "RESOURCE_CAP_NO_VERDICT",
        "registered_aws_lane": lane,
        "stage": stage,
        "script_sha256": digest(script),
        "source_hashes": source_hashes,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in artifacts if path.is_file()
        },
        "scope": "NO_EXACT_BASE4_RANK_PURITY_VERDICT",
        "firewall": (
            "NO_FULL_P6_NO_GRADE7_COMPATIBILITY_NO_LATER_GRADE_NO_JET_"
            "NO_ARC_NO_CLOSURE_NO_JC2"
        ),
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V27_BASE4=RESOURCE_CAP_NO_VERDICT")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_root", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=int, default=21000)
    args = parser.parse_args()

    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if platform.system() != "Linux" or not vendor.is_file() or \
            vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V27 BASE4 exact prepass refused host")
    lane = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not lane.startswith("max12_812_order2_u2_62_k00_v27_base4_"):
        fail("registered V27 BASE4 AWS lane missing or malformed")
    if args.timeout <= 0 or args.timeout > 21000:
        fail("inner timeout outside preregistered cap")

    source_root = args.source_root.resolve()
    source_hashes = dict(PINNED_SHA256)
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
        ('if (size(B)!=7) { print("K00_V27_BASE4_FAIL='
         'BASE_GENERATOR_CENSUS"); quit; }'),
        "ideal I6A=minor(A,6);",
        ('if (size(I6A)!=0) { print("K00_V27_BASE4_FAIL='
         'I6_STORED_NONZERO_CENSUS"); quit; }'),
        "int i6bad=0; int i6i; for (i6i=1;i6i<=size(I6A);i6i++) { if (I6A[i6i]!=0) { i6bad++; } }",
        ('if (i6bad!=0) { print("K00_V27_BASE4_FAIL='
         'I6A_NONZERO"); quit; }'),
        "ideal I5A=minor(A,5);",
        ('if (size(I5A)!=90) { print("K00_V27_BASE4_FAIL='
         'I5_STORED_NONZERO_CENSUS"); quit; }'),
        "int i5nonzero=0; int i5i; for (i5i=1;i5i<=size(I5A);i5i++) { if (I5A[i5i]!=0) { i5nonzero++; } }",
        ('if (i5nonzero!=90) { print("K00_V27_BASE4_FAIL='
         'I5_NONZERO_CENSUS"); quit; }'),
        "ideal I4A=minor(A,4);",
        ('if (size(I4A)!=594) { print("K00_V27_BASE4_FAIL='
         'I4_STORED_NONZERO_CENSUS"); quit; }'),
        "int i4nonzero=0; int i4i; int ipick4=0; for (i4i=1;i4i<=size(I4A);i4i++) { if (I4A[i4i]!=0) { i4nonzero++; if (ipick4==0) { ipick4=i4i; } } }",
        ('if ((i4nonzero!=594)||(ipick4==0)) { print("K00_V27_BASE4_FAIL='
         'I4_NONZERO_CENSUS"); quit; }'),
        "ideal I4M=I4A; I4M[ipick4]=0;",
        ('if ((I4M[ipick4]!=0)||(I4A[ipick4]==I4M[ipick4])) '
         '{ print("K00_V27_BASE4_FAIL=I4_DELETE_MUTATION"); quit; }'),
        "ideal CTRLproper=d0_1; ideal GCTRLproper=std(CTRLproper);",
        ('if (reduce(1,GCTRLproper)==0) { print("K00_V27_BASE4_FAIL='
         'KNOWN_PROPER_CONTROL"); quit; }'),
        "ideal CTRLunit=d0_1,1; ideal GCTRLunit=std(CTRLunit);",
        ('if (reduce(1,GCTRLunit)!=0) { print("K00_V27_BASE4_FAIL='
         'FORCED_UNIT_CONTROL"); quit; }'),
        "ideal J4=B+I5A; ideal SJ4=std(J4); poly J4N1=reduce(1,SJ4); int J4D=dim(SJ4);",
        ('if ((J4N1!=1)||(J4D!=3)) { print("K00_V27_BASE4_FAIL='
         'V26R1F_FRESH_CONTROL"); quit; }'),
        "ideal I4MODJ4=reduce(I4A,SJ4); int i4outside=0; for (i4i=1;i4i<=size(I4MODJ4);i4i++) { if (I4MODJ4[i4i]!=0) { i4outside++; } }",
        "ideal J=J4+I4A;",
    ]

    preflight = output / "base4_branch.sing"
    preflight.write_text("\n".join(definitions + [
        "ideal S=slimgb(J); poly N1=reduce(1,S); int D=dim(S);",
        "if (N1==0)", "{",
        ('  if (D!=-1) { print("K00_V27_BASE4_FAIL='
         'UNIT_DIMENSION"); quit; }'),
        ('  print("K00_V27_BASE4_PREFLIGHT=UNIT"); '
         'print("K00_V27_BASE4_DIM=-1"); '
         'print("K00_V27_BASE4_NGEN="+string(size(J))); '
         'print("K00_V27_BASE4_I4PICK="+string(ipick4)); '
         'print("K00_V27_BASE4_I4OUTSIDE="+string(i4outside)); quit;'),
        "}",
        ('if ((N1!=1)||(D<0)||(D>3)) { print("K00_V27_BASE4_FAIL='
         'PROPER_MARKERS"); quit; }'),
        ('print("K00_V27_BASE4_PREFLIGHT=PROPER"); '
         'print("K00_V27_BASE4_DIM="+string(D)); '
         'print("K00_V27_BASE4_NGEN="+string(size(J))); '
         'print("K00_V27_BASE4_I4PICK="+string(ipick4)); '
         'print("K00_V27_BASE4_I4OUTSIDE="+string(i4outside)); quit;'),
    ]) + "\n")
    require_nonempty(preflight)
    pre_stdout = output / "base4_branch.stdout"
    pre_stderr = output / "base4_branch.stderr"
    artifacts = [labels_path, preflight]
    try:
        markers = run_singular(
            singular, preflight, pre_stdout, pre_stderr, args.timeout)
    except ResourceCap:
        artifacts.extend([pre_stdout, pre_stderr])
        emit_cap(output, lane, "SLIMGB_BASE4_PREFLIGHT", preflight,
                 artifacts, source_hashes)
        return
    artifacts.extend([pre_stdout, pre_stderr])

    parsed = {
        name: re.search(rf"K00_V27_BASE4_{name}=(-?\d+)", markers)
        for name in ("DIM", "NGEN", "I4PICK", "I4OUTSIDE")
    }
    if any(value is None for value in parsed.values()):
        fail("BASE4 preflight custody marker missing")
    values = {
        name: int(match.group(1))
        for name, match in parsed.items() if match is not None
    }
    if values["NGEN"] <= 0 or values["I4PICK"] <= 0 or \
            values["I4OUTSIDE"] < 0:
        fail(("BASE4 generator/minor control census", values))

    if "K00_V27_BASE4_PREFLIGHT=UNIT" in markers:
        cert_path = output / "BASE4_UNIT_COEFFICIENTS.matrix"
        producer = output / "base4_unit_lift.sing"
        producer.write_text("\n".join(definitions + [
            'matrix U; matrix C=lift(J,ideal(1),U,"slimgb");',
            (f'if ((nrows(C)!={values["NGEN"]})||(ncols(C)!=1)||'
             '(nrows(U)!=1)||(ncols(U)!=1)) { '
             'print("K00_V27_BASE4_FAIL=UNIT_LIFT_SHAPE"); quit; }'),
            ('if (U[1,1]!=1) { print("K00_V27_BASE4_FAIL='
             'UNIT_LIFT_U"); quit; }'),
            ('matrix UID=matrix(J)*C-matrix(ideal(1)); '
             'if (UID[1,1]!=0) { print("K00_V27_BASE4_FAIL='
             'UNIT_IDENTITY"); quit; }'),
            "int pick=0; int jj;",
            (f"for (jj=1;jj<={values['NGEN']};jj++) {{ if ((pick==0)&&"
             "(J[jj]!=0)&&(C[jj,1]!=0)) { pick=jj; } }"),
            ('if (pick==0) { print("K00_V27_BASE4_FAIL='
             'UNIT_MUTATION_PICK"); quit; }'),
            "matrix CDROP=C; CDROP[pick,1]=0;",
            ('matrix UDROPD=matrix(J)*CDROP-matrix(ideal(1)); '
             'if (UDROPD[1,1]==0) { print("K00_V27_BASE4_FAIL='
             'UNIT_DROP_MUTATION"); quit; }'),
            "matrix CADD=C; CADD[pick,1]=CADD[pick,1]+1;",
            ('matrix UADDD=matrix(J)*CADD-matrix(ideal(1)); '
             'if (UADDD[1,1]==0) { print("K00_V27_BASE4_FAIL='
             'UNIT_ADD_MUTATION"); quit; }'),
            f'write("{qpath(cert_path)}",string(C));',
            ('print("K00_V27_BASE4_UNIT_PRODUCER=1"); '
             'print("K00_V27_BASE4_CPICK="+string(pick)); quit;'),
        ]) + "\n")
        require_nonempty(producer)
        producer_stdout = output / "base4_unit_lift.stdout"
        producer_stderr = output / "base4_unit_lift.stderr"
        try:
            producer_markers = run_singular(
                singular, producer, producer_stdout, producer_stderr,
                args.timeout)
        except ResourceCap:
            artifacts.extend([producer, producer_stdout, producer_stderr])
            emit_cap(output, lane, "DIRECT_BASE4_UNIT_LIFT", producer,
                     artifacts, source_hashes)
            return
        pick_match = re.search(
            r"K00_V27_BASE4_CPICK=(\d+)", producer_markers)
        require_nonempty(cert_path)
        if "K00_V27_BASE4_UNIT_PRODUCER=1" not in producer_markers or \
                pick_match is None:
            fail("BASE4 unit certificate custody missing")
        pick = int(pick_match.group(1))
        replay = output / "base4_unit_replay.sing"
        replay.write_text("\n".join(definitions + [
            f"matrix C[{values['NGEN']}][1]={cert_path.read_text().strip()};",
            ('matrix UID=matrix(J)*C-matrix(ideal(1)); '
             'if (UID[1,1]!=0) { print("K00_V27_BASE4_FAIL='
             'SERIALIZED_UNIT_IDENTITY"); quit; }'),
            f"matrix CDROP=C; CDROP[{pick},1]=0;",
            ('matrix UDROPD=matrix(J)*CDROP-matrix(ideal(1)); '
             'if (UDROPD[1,1]==0) { print("K00_V27_BASE4_FAIL='
             'SERIALIZED_DROP_MUTATION"); quit; }'),
            f"matrix CADD=C; CADD[{pick},1]=CADD[{pick},1]+1;",
            ('matrix UADDD=matrix(J)*CADD-matrix(ideal(1)); '
             'if (UADDD[1,1]==0) { print("K00_V27_BASE4_FAIL='
             'SERIALIZED_ADD_MUTATION"); quit; }'),
            'print("K00_V27_BASE4_UNIT_SECOND_PROCESS_REPLAY=1"); quit;',
        ]) + "\n")
        require_nonempty(replay)
        replay_stdout = output / "base4_unit_replay.stdout"
        replay_stderr = output / "base4_unit_replay.stderr"
        try:
            replay_markers = run_singular(
                singular, replay, replay_stdout, replay_stderr,
                min(args.timeout, 3600))
        except ResourceCap:
            artifacts.extend([
                producer, producer_stdout, producer_stderr, cert_path,
                replay, replay_stdout, replay_stderr])
            emit_cap(output, lane, "SERIALIZED_BASE4_UNIT_REPLAY", replay,
                     artifacts, source_hashes)
            return
        if "K00_V27_BASE4_UNIT_SECOND_PROCESS_REPLAY=1" not in replay_markers:
            fail("BASE4 unit second-process marker missing")
        artifacts.extend([
            producer, producer_stdout, producer_stderr, cert_path,
            replay, replay_stdout, replay_stderr])
        status = UNIT_STATUS
        branch = "UNIT_B_PLUS_I5A_PLUS_I4A"
        outcome = {
            "J3base_unit": True,
            "rank_le_3_geometric_points_survive": False,
            "rank_pure_on_promoted_J4base": 4,
            "unit_certificate_entries": values["NGEN"],
            "certificate_mutation_index": pick,
            "serialized_second_process_replay": True,
        }
    elif "K00_V27_BASE4_PREFLIGHT=PROPER" in markers:
        basis_path = output / "BASE4_STANDARD_BASIS.txt"
        transform_path = output / "BASE4_TRANSFORM.matrix"
        producer = output / "base4_proper_tracked.sing"
        producer.write_text("\n".join(definitions + [
            "matrix T; ideal G=liftstd(J,T);",
            (f'if ((nrows(T)!={values["NGEN"]})||(ncols(T)!=size(G))) {{ '
             'print("K00_V27_BASE4_FAIL=TRACKED_BASIS_SHAPE"); quit; }'),
            ('matrix TREPLAY=matrix(J)*T-matrix(G); int treplay_bad=0; int tc; '
             'for (tc=1;tc<=ncols(TREPLAY);tc++) { '
             'if (TREPLAY[1,tc]!=0) { treplay_bad++; } }'),
            ('if (treplay_bad) { print("K00_V27_BASE4_FAIL='
             'TRACKED_BASIS_IDENTITY"); quit; }'),
            "poly N1=reduce(1,G); int D=dim(G);",
            (f'if ((N1!=1)||(D!={values["DIM"]})||(D<0)) {{ '
             'print("K00_V27_BASE4_FAIL=TRACKED_PROPER_MARKERS"); quit; }'),
            "int pickr=0; int pickc=0; int rr; int cc;",
            (f"for (cc=1;cc<=ncols(T);cc++) {{ for (rr=1;rr<={values['NGEN']};rr++) "
             "{ if ((pickr==0)&&(J[rr]!=0)&&(T[rr,cc]!=0)) "
             "{ pickr=rr; pickc=cc; } } }"),
            ('if (pickr==0) { print("K00_V27_BASE4_FAIL='
             'TRANSFORM_MUTATION_PICK"); quit; }'),
            "matrix TBAD=T; TBAD[pickr,pickc]=0;",
            ('matrix TMUT=matrix(J)*TBAD-matrix(G); int tmutation_nonzero=0; '
             'for (tc=1;tc<=ncols(TMUT);tc++) { '
             'if (TMUT[1,tc]!=0) { tmutation_nonzero++; } }'),
            ('if (tmutation_nonzero==0) { print("K00_V27_BASE4_FAIL='
             'TRANSFORM_DROP_MUTATION"); quit; }'),
            "ideal JUNIT=J,1; ideal GUNIT=std(JUNIT);",
            ('if (reduce(1,GUNIT)!=0) { print("K00_V27_BASE4_FAIL='
             'FORCED_UNIT_MUTATION"); quit; }'),
            f'write("{qpath(basis_path)}",string(G));',
            f'write("{qpath(transform_path)}",string(T));',
            ('print("K00_V27_BASE4_PROPER_PRODUCER=1"); '
             'print("K00_V27_BASE4_GSIZE="+string(size(G))); '
             'print("K00_V27_BASE4_TPICKR="+string(pickr)); '
             'print("K00_V27_BASE4_TPICKC="+string(pickc)); quit;'),
        ]) + "\n")
        require_nonempty(producer)
        producer_stdout = output / "base4_proper_tracked.stdout"
        producer_stderr = output / "base4_proper_tracked.stderr"
        try:
            producer_markers = run_singular(
                singular, producer, producer_stdout, producer_stderr,
                args.timeout)
        except ResourceCap:
            artifacts.extend([producer, producer_stdout, producer_stderr])
            emit_cap(output, lane, "TRACKED_BASE4_PROPER_LIFTSTD", producer,
                     artifacts, source_hashes)
            return
        proper_matches = {
            name: re.search(rf"K00_V27_BASE4_{name}=(\d+)", producer_markers)
            for name in ("GSIZE", "TPICKR", "TPICKC")
        }
        require_nonempty(basis_path)
        require_nonempty(transform_path)
        if "K00_V27_BASE4_PROPER_PRODUCER=1" not in producer_markers or \
                any(match is None for match in proper_matches.values()):
            fail("BASE4 proper tracked custody missing")
        proper_values = {
            name: int(match.group(1))
            for name, match in proper_matches.items() if match is not None
        }
        replay = output / "base4_proper_replay.sing"
        replay.write_text("\n".join(definitions + [
            f"ideal Graw={basis_path.read_text().strip()};",
            (f"matrix T[{values['NGEN']}][{proper_values['GSIZE']}]="
             f"{transform_path.read_text().strip()};"),
            ('matrix TREPLAY=matrix(J)*T-matrix(Graw); int treplay_bad=0; int tc; '
             'for (tc=1;tc<=ncols(TREPLAY);tc++) { '
             'if (TREPLAY[1,tc]!=0) { treplay_bad++; } }'),
            ('if (treplay_bad) { print("K00_V27_BASE4_FAIL='
             'SERIALIZED_TRACKED_IDENTITY"); quit; }'),
            "ideal G=std(Graw);",
            "ideal BNF=reduce(B,G); ideal I5NF=reduce(I5A,G); ideal I4NF=reduce(I4A,G);",
            "int reverse_bad=0; int reverse_i;",
            "for (reverse_i=1;reverse_i<=size(BNF);reverse_i++) { if (BNF[reverse_i]!=0) { reverse_bad++; } }",
            "for (reverse_i=1;reverse_i<=size(I5NF);reverse_i++) { if (I5NF[reverse_i]!=0) { reverse_bad++; } }",
            "for (reverse_i=1;reverse_i<=size(I4NF);reverse_i++) { if (I4NF[reverse_i]!=0) { reverse_bad++; } }",
            ('if (reverse_bad) { print("K00_V27_BASE4_FAIL='
             'FULL_LITERAL_REVERSE_INCLUSION"); quit; }'),
            'print("K00_V27_BASE4_FULL_LITERAL_REVERSE_INCLUSION=1");',
            "poly N1=reduce(1,G); int D=dim(G);",
            (f'if ((N1!=1)||(D!={values["DIM"]})) {{ '
             'print("K00_V27_BASE4_FAIL=SERIALIZED_PROPER_MARKERS"); quit; }'),
            (f"matrix TBAD=T; TBAD[{proper_values['TPICKR']},"
             f"{proper_values['TPICKC']}]=0;"),
            ('matrix TMUT=matrix(J)*TBAD-matrix(Graw); int tmutation_nonzero=0; '
             'for (tc=1;tc<=ncols(TMUT);tc++) { '
             'if (TMUT[1,tc]!=0) { tmutation_nonzero++; } }'),
            ('if (tmutation_nonzero==0) { print("K00_V27_BASE4_FAIL='
             'SERIALIZED_TRANSFORM_MUTATION"); quit; }'),
            "ideal JUNIT=J,1; ideal GUNIT=std(JUNIT);",
            ('if (reduce(1,GUNIT)!=0) { print("K00_V27_BASE4_FAIL='
             'SERIALIZED_FORCED_UNIT"); quit; }'),
            'print("K00_V27_BASE4_PROPER_SECOND_PROCESS_REPLAY=1"); quit;',
        ]) + "\n")
        require_nonempty(replay)
        replay_stdout = output / "base4_proper_replay.stdout"
        replay_stderr = output / "base4_proper_replay.stderr"
        try:
            replay_markers = run_singular(
                singular, replay, replay_stdout, replay_stderr,
                min(args.timeout, 3600))
        except ResourceCap:
            artifacts.extend([
                producer, producer_stdout, producer_stderr, basis_path,
                transform_path, replay, replay_stdout, replay_stderr])
            emit_cap(output, lane, "SERIALIZED_BASE4_PROPER_REPLAY", replay,
                     artifacts, source_hashes)
            return
        if "K00_V27_BASE4_PROPER_SECOND_PROCESS_REPLAY=1" not in replay_markers or \
                "K00_V27_BASE4_FULL_LITERAL_REVERSE_INCLUSION=1" not in replay_markers:
            fail("BASE4 proper second-process marker missing")
        artifacts.extend([
            producer, producer_stdout, producer_stderr, basis_path,
            transform_path, replay, replay_stdout, replay_stderr])
        status = PROPER_STATUS
        branch = "PROPER_B_PLUS_I5A_PLUS_I4A"
        outcome = {
            "J3base_unit": False,
            "rank_le_3_geometric_points_survive": True,
            "exact_affine_dimension": values["DIM"],
            "standard_basis_size": proper_values["GSIZE"],
            "full_literal_minor_reverse_inclusion": True,
            "serialized_recomputed_standard_basis": True,
            "serialized_second_process_replay": True,
        }
    else:
        fail("BASE4 preflight branch marker missing")

    for artifact in artifacts:
        if artifact.suffix != ".stderr":
            require_nonempty(artifact)
        elif artifact.read_bytes():
            fail(("nonempty Singular stderr", artifact.name))

    payload = {
        "status": status,
        "lifecycle": "PRODUCER_UNREVIEWED_SPECULATIVE",
        "branch": branch,
        "field": "Q_exact",
        "ring_variables": [
            "d0_1", "d1_1", "d2_1", "d3_1", "d4_1", "d5_1"],
        "registered_aws_lane": lane,
        "singular_version": engine_version,
        "source_hashes": source_hashes,
        "base_generator_provenance": [
            "G2_row1", "G2_row2", "G2_row3", "G2_row4", "G2_row5",
            "G2_row7", "F10"],
        "literal_minor_census": {
            "I6A": {"total": 49, "nonzero": 0},
            "I5A": {"total": 441, "nonzero": 90},
            "I4A": {"total": 1225, "nonzero": 594},
        },
        "fresh_V26_J4base_control": {
            "proper": True,
            "exact_affine_dimension": 3,
        },
        "I4_entries_nonzero_mod_fresh_J4base_basis": values["I4OUTSIDE"],
        "I4_generator_deletion_mutation": True,
        "certificate_or_transform_mutations": "DROP_AND_ADD_EXACT_IDENTITY_FAILURES",
        "b_sign_control": "NOT_APPLICABLE_BASE4_NO_b_CONSUMED",
        "restored_k6_0_control": "NOT_APPLICABLE_BASE4_NO_PRIOR_COMPILER_CONSUMED",
        "max5class_representative_mutation": "DEFERRED_TO_REGISTERED_MAX5CLASS_STAGE",
        **outcome,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in artifacts
        },
        "scope": "EXACT_SIX_VARIABLE_V27_BASE4_RANK_PURITY_PREPASS_ONLY",
        "firewall": (
            "NO_RATIONAL_POINT_NO_FULL_P6_NO_GRADE7_COMPATIBILITY_"
            "NO_LATER_GRADE_NO_JET_NO_ARC_NO_SOURCE_REACHABILITY_"
            "NO_CLOSURE_NO_COUNTEREXAMPLE_NO_JC2"
        ),
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    require_nonempty(result_path)
    print("K00_V27_BASE4=" + status)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
