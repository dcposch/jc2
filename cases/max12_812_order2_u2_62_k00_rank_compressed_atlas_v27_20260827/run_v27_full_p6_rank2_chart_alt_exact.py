#!/usr/bin/env python3
"""Exact AWS-only alternate K00 V27 full-P6 selected rank-two chart."""

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
R3_REL = CASE_REL + "/aws_r6a_r3_exact_base2"
SELECT_REL = CASE_REL + "/aws_r6a_aux_r3_minor_selection"
FABLE_REVIEW_REL = "xmodel/k00-v27-base4-base3-base2-hostile-review-fable5-20260827.md"
MINOR_REL = SELECT_REL + "/SELECTED_LABEL_MINOR_R5R7_C6C7.txt"
NF_REL = SELECT_REL + "/SELECTED_LABEL_MINOR_NORMAL_FORM_MOD_J2.txt"
PINNED_SHA256 = {
    COMPILED_REL + "/ATLAS_EXACT_POLYNOMIALS.json":
        "d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501",
    COMPILED_REL + "/COMPILED_SOURCE.sha256":
        "5de20da0d3501db668fca38db3c678ba4719745e3df7b32d0d0a8d2867e4da32",
    COMPILED_REL + "/RESULT.json":
        "f1a6f1fc988fc77816daaab13b294b1321de7e476d2891cf7fbfa2e033868d97",
    CASE_REL + "/RESULT_V27_BASE4_R1_EXACT_PREPASS.md":
        "19c8795589ce076c2414474a6341c7929d578958ea122a6745f26ea6ab46bd9c",
    R1_REL + "/output/RESULT.json":
        "f886f17ca2c626ec476e695418002185d2223d556721759900f6cdbe89635073",
    CASE_REL + "/RESULT_V27_BASE3_R2_EXACT_PREPASS.md":
        "c42c0482f0b5861f5099e6e121c60a93d018c87a9619749ee1844f5954545c39",
    R2_REL + "/output/RESULT.json":
        "d9d9d9dba1b06f1cb9773066924268a5162774779de9f86339d2c3306fbffdb3",
    CASE_REL + "/RESULT_V27_BASE2_R3_EXACT_PREPASS.md":
        "8e4b545d72e2dc62a1c60090e2d956969320d738c6c35968944039e3bccb80a2",
    CASE_REL + "/DESIGN_ERRATUM_R3_SIZE_NCOLS.md":
        "ceb69e22c43cb366d52a2e7d9bd3ec9d5ae4befd18368202d711a20e4b5e3f99",
    CASE_REL + "/REVIEW_PACKET_BASE2_R3_NCOLS_REPAIR.sha256":
        "b9c70bf5afa00a9857693cc53f80304c4ddd143c2dad4471941b040fed55b93a",
    CASE_REL + "/SOURCE_FREEZE_FULL_P6_RANK2_CHART_ALTERNATIVE_R0_FAILED.sha256":
        "ffd2e4da109e2701499152eb5561f97005b06f536077abc6fd7242b87fc9f7f7",
    CASE_REL + "/RESULT_V27_FULL_P6_RANK2_CHART_ALTERNATIVE.md":
        "a4fb6079d1f05d1d411928d17f56e6ed13ad6af14510020ed75dbec19aa87e08",
    CASE_REL + "/DESIGN_ERRATUM_SUCCESSOR_MINOR_STORAGE_NCOLS.md":
        "a902d4ad61c48378fdd94e78ed58a47d307dc39e8ae5090a6661d9057b917dd9",
    CASE_REL + "/aws_r6a_alt_full_p6_rank2_chart_r5r7_c6c7/EVIDENCE.sha256":
        "ff7ff169ee327df91b76249f88cb9b2b31ca6df76bd8eed517c0f61868082df1",
    CASE_REL + "/aws_r6a_alt_full_p6_rank2_chart_r5r7_c6c7/HARVEST_REPLAY.sha256":
        "ce2a00d59d1b8165a5400606178e815b27f791af2365937df104792867551e7f",
    FABLE_REVIEW_REL:
        "738f46030a73fea2a06a8e3139ed9aa5e2001b72a579e459357af81f6801647a",
    R3_REL + "/output/RESULT.json":
        "bd12daa1e1e6545b8c61bef7dcb18913854146bd9c61e0b04c795fa486b4a228",
    R3_REL + "/EVIDENCE.sha256":
        "b42e23d2e12e3ef45221b387a2dd091486bfbe9b6c5bc253d240a74dc3a9f996",
    SELECT_REL + "/EVIDENCE.sha256":
        "8895592dbf85cbc0cae73db1e448d54281ac686c964248688983eafaa6084336",
    MINOR_REL:
        "51007fc35085e65bd7b19936b492949c9edcd04f4f34716c1ff6fc9e8f6d5616",
    NF_REL:
        "8748e6f901332974919b80383deb9a3cca37f84f46da5252e34885485380157c",
    CASE_REL + "/HARVEST_REPLAY_R3_MINOR_SELECTION.sha256":
        "60c9745600c275b8876927f11d2441f5267536dd3e653a667ea884d13d385119",
}
COMPILER_STATUS = "PASS_V26_FITTING_ATLAS_COMPILED_NO_STRATUM_DECISION"
R1_STATUS = "PASS_V27_BASE4_EXACT_RANK_LE3_SURVIVES_PRODUCER_UNREVIEWED"
R2_STATUS = "PASS_V27_R2_EXACT_RANK_LE2_SURVIVES_PRODUCER_UNREVIEWED_ROLLBACK_R1"
R3_STATUS = "PASS_V27_R3_EXACT_RANK_LE1_SURVIVES_PRODUCER_UNREVIEWED_ROLLBACK_R1_R2"
PROPER_STATUS = (
    "PASS_V27_ALT_FULL_P6_SELECTED_I2_CHART_PROPER_ALGEBRAIC_RANK2_POINT_"
    "PRODUCER_UNREVIEWED_ROLLBACK_R1_R2_R3"
)
UNIT_STATUS = (
    "PASS_V27_ALT_FULL_P6_SELECTED_I2_CHART_UNIT_ONLY_THIS_CHART_EMPTY_"
    "PRODUCER_UNREVIEWED_ROLLBACK_R1_R2_R3"
)
EXPECTED_PRIOR = tuple(
    [f"d{i}_{j}" for i in range(6) for j in range(1, 6)] +
    ["k10_0", "k10_1", "k10_2"]
)


class ResourceCap(RuntimeError):
    """A registered inner wall cap fired."""


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def object_digest(text: str) -> str:
    return sha256((text.strip() + "\n").encode()).hexdigest()


def qpath(path: Path) -> str:
    value = str(path.resolve())
    if '"' in value or "\n" in value:
        fail(("unsafe output path", value))
    return value


def require_nonempty(path: Path) -> None:
    if not path.is_file() or path.stat().st_size == 0:
        fail(("missing or empty replay artifact", str(path)))


def write_checked_script(path: Path, lines: list[str]) -> None:
    text = "\n".join(lines) + "\n"
    if "<=size(" in re.sub(r"\s+", "", text):
        fail(("generated positional size() loop refused", path.name))
    path.write_text(text)


def poly(item: dict) -> str:
    value = item.get("singular")
    if not isinstance(value, str) or not value:
        fail("missing exact polynomial serialization")
    return value


def validate_sources(root: Path) -> tuple[dict, list[dict], list[dict], str, str]:
    for relative, expected in PINNED_SHA256.items():
        path = root / relative
        if not path.is_file() or digest(path) != expected:
            fail(("pinned source mismatch", relative))
    compiler = json.loads((root / (COMPILED_REL + "/RESULT.json")).read_text())
    if compiler.get("status") != COMPILER_STATUS or \
            compiler.get("A_shape") != [7, 7] or \
            compiler.get("generic_rank_A") != 5:
        fail("compiler endpoint metadata mismatch")
    for rank, expected in {
        "2": (441, 90, 326), "3": (1225, 412, 725),
        "4": (1225, 631, 491), "5": (441, 351, 54),
        "6": (49, 49, 0),
    }.items():
        item = compiler.get("A_minor_statistics", {}).get(rank, {})
        if (item.get("total"), item.get("zero"),
                item.get("unique_nonzero_exact_polynomials")) != expected:
            fail(("compiler minor census mismatch", rank, item))
    for relative, status, unit_key, dimension in (
        (R1_REL, R1_STATUS, "J3base_unit", 3),
        (R2_REL, R2_STATUS, "J2base_unit", 3),
        (R3_REL, R3_STATUS, "J1base_unit", 2),
    ):
        result = json.loads((root / (relative + "/output/RESULT.json")).read_text())
        if result.get("status") != status or result.get(unit_key) is not False or \
                result.get("exact_affine_dimension") != dimension:
            fail(("upstream endpoint metadata mismatch", relative))
    historical_r3 = json.loads(
        (root / (R3_REL + "/output/RESULT.json")).read_text())
    if historical_r3.get("I2_entries_nonzero_mod_fresh_J2base_basis") != 237 or \
            historical_r3.get("full_literal_minor_reverse_inclusion") is not True:
        fail("historical R3 endpoint metadata mismatch")
    atlas = json.loads(
        (root / (COMPILED_REL + "/ATLAS_EXACT_POLYNOMIALS.json")).read_text())
    if tuple(atlas.get("ring_variables", ())) != EXPECTED_PRIOR:
        fail("full prior ring variable order mismatch")
    matrix = atlas.get("A")
    if not isinstance(matrix, list) or len(matrix) != 7 or \
            any(not isinstance(row, list) or len(row) != 7 for row in matrix):
        fail("frozen A shape mismatch")
    literal = atlas.get("P6_literal_rows_through_grade6")
    if not isinstance(literal, list) or len(literal) != 49:
        fail("P6 literal provenance census mismatch")
    for index, item in enumerate(literal):
        expected_grade, expected_row = divmod(index, 7)
        if item.get("Lambda_grade") != expected_grade or \
                item.get("row") != expected_row + 1:
            fail(("P6 literal label ordering drift", index))
        poly(item.get("poly", {}))
    nonzero_literal = [item["poly"] for item in literal if poly(item["poly"]) != "0"]
    if len(nonzero_literal) != 34:
        fail("P6 literal nonzero census mismatch")
    p6 = atlas.get("P6_nonzero_generators_plus_F10")
    if not isinstance(p6, list) or len(p6) != 35 or \
            p6 != nonzero_literal + [atlas.get("F10")]:
        fail("P6 raw nonzero list differs from literal provenance plus F10")
    grade2 = [item["poly"] for item in literal
              if item["Lambda_grade"] == 2 and poly(item["poly"]) != "0"]
    if grade2 != atlas.get("Q1_to_Q6") or len(grade2) != 6:
        fail("B does not match six nonzero literal grade-two rows")
    selected = (root / MINOR_REL).read_text().strip()
    normal_form = (root / NF_REL).read_text().strip()
    if not selected or not normal_form:
        fail("selected polynomial serialization empty")
    return atlas, literal, p6, selected, normal_form


def matrix_line(matrix: list[list[dict]]) -> str:
    return "matrix A[7][7]=" + ",".join(
        f"({poly(entry)})" for row in matrix for entry in row) + ";"


def emit_provenance(output: Path, literal: list[dict]) -> tuple[Path, Path]:
    p6_path = output / "P6_LITERAL_SOURCE_LABELS.json"
    p6_path.write_text(json.dumps({
        "ordering": "Lambda_grade_major_then_row",
        "literal_count": 49,
        "literal_nonzero": 34,
        "nonzero_plus_F10": 35,
        "labels": [
            {
                "Lambda_grade": item["Lambda_grade"],
                "row": item["row"],
                "zero": poly(item["poly"]) == "0",
                "singular_text_sha256": object_digest(poly(item["poly"])),
            }
            for item in literal
        ],
    }, sort_keys=True, indent=2) + "\n")
    minor_path = output / "MINOR_SOURCE_LABELS_RANK2_RANK3.json"
    minor_path.write_text(json.dumps({
        "matrix": "A_frozen_7_by_7",
        "ordering": "independent complete lexicographic literal label universe",
        "not_a_singular_minor_object_slot_map": True,
        "selected": {
            "singular_minor_object_column": 37,
            "rows_one_based": [5, 7],
            "columns_one_based": [6, 7],
            "stored_sign": -1,
            "label_binding": "exhaustive exact polynomial match, not list-index identity",
        },
        "ranks": {
            str(rank): [
                {"rows_one_based": list(rows), "columns_one_based": list(columns)}
                for rows in combinations(range(1, 8), rank)
                for columns in combinations(range(1, 8), rank)
            ]
            for rank in (2, 3)
        },
    }, sort_keys=True, indent=2) + "\n")
    require_nonempty(p6_path)
    require_nonempty(minor_path)
    return p6_path, minor_path


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
        r"(?mi)^\s*\?|// \*\*|warning|error occurred|K00_V27_P6R4_FAIL=")
    if completed.returncode or completed.stderr or not completed.stdout.strip() or \
            diagnostics.search(completed.stdout):
        fail(("full-P6 exact engine/replay failure", script.name,
              completed.returncode, completed.stderr[-2000:],
              completed.stdout[-4000:]))
    return completed.stdout


def emit_cap(output: Path, lane: str, stage: str, script: Path,
             artifacts: list[Path]) -> None:
    payload = {
        "status": "RESOURCE_CAP_NO_VERDICT",
        "registered_aws_lane": lane,
        "stage": stage,
        "rollback_dependency": "BASE4_R1_BASE3_R2_BASE2_R3_PRODUCER_UNREVIEWED",
        "script_sha256": digest(script),
        "source_hashes": PINNED_SHA256,
        "selected_minor_sha256": PINNED_SHA256[MINOR_REL],
        "rational_point_claim": False,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in artifacts if path.is_file()
        },
        "scope": "NO_EXACT_V27_FULL_P6_SELECTED_CHART_VERDICT",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V27_P6R4=RESOURCE_CAP_NO_VERDICT")


def definitions(atlas: dict, p6: list[dict], selected: str,
                normal_form: str) -> list[str]:
    variables = ",".join(EXPECTED_PRIOR + ("z",))
    m0 = ",".join(EXPECTED_PRIOR)
    return [
        f"ring R=0,({variables}),dp;",
        matrix_line(atlas["A"]),
        "ideal P6=" + ",".join(f"({poly(item)})" for item in p6) + ";",
        "ideal B=" + ",".join(f"({poly(item)})" for item in atlas["Q1_to_Q6"]) +
        f",({poly(atlas['F10'])});",
        ('if ((ncols(P6)!=35)||(ncols(B)!=7)||(size(P6)!=35)||(size(B)!=7)) '
         '{ print("K00_V27_P6R4_FAIL=RAW_P6_B_CENSUS"); quit; }'),
        ("ideal I6A=minor(A,6); ideal I5A=minor(A,5); ideal I4A=minor(A,4); "
         "ideal I3A=minor(A,3); ideal I2A=minor(A,2);"),
        ('if ((ncols(I6A)!=1)||(ncols(I5A)!=90)||(ncols(I4A)!=594)||'
         '(ncols(I3A)!=813)||(ncols(I2A)!=441)||'
         '(size(I6A)!=0)||(size(I5A)!=90)||(size(I4A)!=594)||'
         '(size(I3A)!=813)||(size(I2A)!=351)) '
         '{ print("K00_V27_P6R4_FAIL=STORED_MINOR_CENSUS"); quit; }'),
        "int mi; int rr; int cc;",
        "ideal I2NZ; int n2=0;",
        ("for (mi=1;mi<=ncols(I2A);mi++) { if (I2A[mi]!=0) "
         "{ n2++; I2NZ[n2]=I2A[mi]; } }"),
        ('if ((n2!=351)||(ncols(I2NZ)!=351)||(size(I2NZ)!=351)) '
         '{ print("K00_V27_P6R4_FAIL=FILTERED_MINOR_CENSUS"); quit; }'),
        "ideal J4=B,I5A; ideal SJ4=std(J4);",
        ('if ((reduce(1,SJ4)!=1)||(dim(SJ4)!=31)) '
         '{ print("K00_V27_P6R4_FAIL=FRESH_J4_CONTROL"); quit; }'),
        ("ideal I4MOD=reduce(I4A,SJ4); int i4outside=0; "
         "for (mi=1;mi<=ncols(I4MOD);mi++) { if (I4MOD[mi]!=0) { i4outside++; } }"),
        'if (i4outside!=0) { print("K00_V27_P6R4_FAIL=FRESH_R1_EQUALITY"); quit; }',
        "ideal J3=B,I5A,I4A; ideal SJ3=std(J3);",
        ('if ((reduce(1,SJ3)!=1)||(dim(SJ3)!=31)) '
         '{ print("K00_V27_P6R4_FAIL=FRESH_J3_CONTROL"); quit; }'),
        ("ideal I3MOD=reduce(I3A,SJ3); int i3outside=0; "
         "for (mi=1;mi<=ncols(I3MOD);mi++) { if (I3MOD[mi]!=0) { i3outside++; } }"),
        'if (i3outside!=0) { print("K00_V27_P6R4_FAIL=FRESH_R2_EQUALITY"); quit; }',
        "ideal J2=B,I5A,I4A,I3A; ideal SJ2=std(J2);",
        ('if ((reduce(1,SJ2)!=1)||(dim(SJ2)!=31)) '
         '{ print("K00_V27_P6R4_FAIL=FRESH_J2_CONTROL"); quit; }'),
        ("ideal I2MOD=reduce(I2A,SJ2); int i2outside=0; int firstoutside=0; "
         "for (mi=1;mi<=ncols(I2MOD);mi++) { if (I2MOD[mi]!=0) { i2outside++; "
         "if (firstoutside==0) { firstoutside=mi; } } }"),
        ('if ((i2outside!=291)||(firstoutside!=37)) '
         '{ print("K00_V27_P6R4_FAIL=FRESH_R3_SELECTION"); quit; }'),
        "ideal J1=B,I5A,I4A,I3A,I2NZ; ideal SJ1=std(J1);",
        ('if ((reduce(1,SJ1)!=1)||(dim(SJ1)!=30)) '
         '{ print("K00_V27_P6R4_FAIL=FRESH_J1_CONTROL"); quit; }'),
        "poly m=A[5,6]*A[7,7]-A[5,7]*A[7,6];",
        f"poly mfrozen=({selected});",
        f"poly nffrozen=({normal_form});",
        "poly nfm=reduce(m,SJ2);",
        ('if ((m==0)||(m!=-I2A[37])||(m!=mfrozen)||(nfm==0)||(nfm!=nffrozen)) '
         '{ print("K00_V27_P6R4_FAIL=SELECTED_MINOR_REPLAY"); quit; }'),
        "ideal SP6=std(P6); ideal BMODP6=reduce(B,SP6); int boutside=0;",
        "for (mi=1;mi<=ncols(BMODP6);mi++) { if (BMODP6[mi]!=0) { boutside++; } }",
        'if (boutside!=0) { print("K00_V27_P6R4_FAIL=B_NOT_IN_P6"); quit; }',
        "poly chart=z*m-1; ideal K=P6,I3A,chart;",
        ('if ((ncols(K)!=849)||(size(K)!=849)) '
         '{ print("K00_V27_P6R4_FAIL=RAW_TARGET_CENSUS"); quit; }'),
        f"ideal M0={m0}; ideal G0=std(M0); int originbad=0;",
        ("for (rr=1;rr<=7;rr++) { for (cc=1;cc<=7;cc++) "
         "{ if (reduce(A[rr,cc],G0)!=0) { originbad++; } } }"),
        "for (mi=1;mi<=ncols(P6);mi++) { if (reduce(P6[mi],G0)!=0) { originbad++; } }",
        "for (mi=1;mi<=ncols(I3A);mi++) { if (reduce(I3A[mi],G0)!=0) { originbad++; } }",
        "if (reduce(m,G0)!=0) { originbad++; }",
        'if (originbad!=0) { print("K00_V27_P6R4_FAIL=ORIGIN_VANISHING"); quit; }',
        "ideal ORIGINCHART=M0,chart;",
        ('if (reduce(1,std(ORIGINCHART))!=0) '
         '{ print("K00_V27_P6R4_FAIL=ORIGIN_NOT_EXCLUDED"); quit; }'),
        "ideal ORIGINDROP=M0,z*m;",
        ('if (reduce(1,std(ORIGINDROP))==0) '
         '{ print("K00_V27_P6R4_FAIL=CHART_CONSTANT_DROP_MUTATION"); quit; }'),
        "ideal P6M=P6; P6M[1]=P6M[1]+1; P6M[35]=P6M[35]+1; ideal I2M=I2A; I2M[37]=I2M[37]+1;",
        ('if ((reduce(P6M[1],G0)==0)||(reduce(P6M[35],G0)==0)||'
         '(reduce(I2M[37],G0)==0)) '
         '{ print("K00_V27_P6R4_FAIL=ORIGIN_ADD_MUTATIONS"); quit; }'),
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_root", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=int, default=21000)
    args = parser.parse_args()
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if platform.system() != "Linux" or not vendor.is_file() or \
            vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only alternate full-P6 chart runner refused host")
    lane = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not lane.startswith("max12_812_order2_u2_62_k00_v27_alt_full_p6_rank2_") or \
            not lane.endswith("_r6a"):
        fail("registered alternate full-P6 lane missing or malformed")
    if args.timeout <= 0 or args.timeout > 21000:
        fail("inner timeout outside preregistered cap")
    source_root = args.source_root.resolve()
    atlas, literal, p6, selected, normal_form = validate_sources(source_root)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    p6_labels, minor_labels = emit_provenance(output, literal)
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    version = subprocess.run(
        [singular, "--version"], text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, timeout=30, check=True).stdout.splitlines()[0]
    common = definitions(atlas, p6, selected, normal_form)
    branch = output / "full_p6_rank2_chart_branch.sing"
    write_checked_script(branch, common + [
        "ideal S=slimgb(K); poly N1=reduce(1,S); int D=dim(S);",
        ('if (N1==0) { print("K00_V27_P6R4_PREFLIGHT=UNIT"); '
         'print("K00_V27_P6R4_DIM=-1"); print("K00_V27_P6R4_NGEN="+string(ncols(K))); quit; }'),
        ('if ((N1==1)&&(D>=0)&&(D<=31)) { print("K00_V27_P6R4_PREFLIGHT=PROPER"); '
         'print("K00_V27_P6R4_DIM="+string(D)); print("K00_V27_P6R4_NGEN="+string(ncols(K))); quit; }'),
        'print("K00_V27_P6R4_FAIL=DECISION_MARKERS"); quit;',
    ])
    branch_stdout = output / "full_p6_rank2_chart_branch.stdout"
    branch_stderr = output / "full_p6_rank2_chart_branch.stderr"
    artifacts = [p6_labels, minor_labels, branch]
    try:
        markers = run_singular(
            singular, branch, branch_stdout, branch_stderr, args.timeout)
    except ResourceCap:
        artifacts.extend([branch_stdout, branch_stderr])
        emit_cap(output, lane, "SLIMGB_FULL_P6_SELECTED_CHART", branch, artifacts)
        return
    artifacts.extend([branch_stdout, branch_stderr])
    match_dim = re.search(r"K00_V27_P6R4_DIM=(-?\d+)", markers)
    match_ngen = re.search(r"K00_V27_P6R4_NGEN=(\d+)", markers)
    if match_dim is None or match_ngen is None:
        fail("full-P6 preflight telemetry missing")
    dimension = int(match_dim.group(1))
    ngen = int(match_ngen.group(1))
    if ngen != 849:
        fail("full-P6 raw generator count mismatch")
    is_proper = "K00_V27_P6R4_PREFLIGHT=PROPER" in markers
    is_unit = "K00_V27_P6R4_PREFLIGHT=UNIT" in markers
    if is_proper == is_unit or (is_proper and not 0 <= dimension <= 31) or \
            (is_unit and dimension != -1):
        fail("full-P6 branch classification mismatch")

    if is_proper:
        basis = output / "FULL_P6_RANK2_CHART_STANDARD_BASIS.txt"
        transform = output / "FULL_P6_RANK2_CHART_TRANSFORM.matrix"
        producer = output / "full_p6_rank2_chart_proper_tracked.sing"
        write_checked_script(producer, common + [
            "matrix T; ideal Graw=liftstd(K,T);",
            (f'if ((nrows(T)!={ngen})||(ncols(T)!=ncols(Graw))) '
             '{ print("K00_V27_P6R4_FAIL=TRACKED_SHAPE"); quit; }'),
            "matrix ID=matrix(K)*T-matrix(Graw); int bad=0; int tc;",
            "for (tc=1;tc<=ncols(ID);tc++) { if (ID[1,tc]!=0) { bad++; } }",
            'if (bad) { print("K00_V27_P6R4_FAIL=TRACKED_IDENTITY"); quit; }',
            (f'if ((reduce(1,Graw)!=1)||(dim(Graw)!={dimension})) '
             '{ print("K00_V27_P6R4_FAIL=TRACKED_PROPER"); quit; }'),
            "int pickr=0; int pickc=0;",
            (f"for (cc=1;cc<=ncols(T);cc++) {{ for (rr=1;rr<={ngen};rr++) "
             "{ if ((pickr==0)&&(K[rr]!=0)&&(T[rr,cc]!=0)) { pickr=rr; pickc=cc; } } }"),
            'if (pickr==0) { print("K00_V27_P6R4_FAIL=TRANSFORM_PICK"); quit; }',
            ("matrix TDROP=T; TDROP[pickr,pickc]=0; "
             "matrix DROP=matrix(K)*TDROP-matrix(Graw); int dropbad=0;"),
            "for (tc=1;tc<=ncols(DROP);tc++) { if (DROP[1,tc]!=0) { dropbad++; } }",
            'if (dropbad==0) { print("K00_V27_P6R4_FAIL=TRANSFORM_DROP"); quit; }',
            ("matrix TADD=T; TADD[pickr,pickc]=TADD[pickr,pickc]+1; "
             "matrix ADD=matrix(K)*TADD-matrix(Graw); int addbad=0;"),
            "for (tc=1;tc<=ncols(ADD);tc++) { if (ADD[1,tc]!=0) { addbad++; } }",
            'if (addbad==0) { print("K00_V27_P6R4_FAIL=TRANSFORM_ADD"); quit; }',
            "ideal KDROP=K; KDROP[pickr]=0; matrix GDROP=matrix(KDROP)*T-matrix(Graw); int genbad=0;",
            "for (tc=1;tc<=ncols(GDROP);tc++) { if (GDROP[1,tc]!=0) { genbad++; } }",
            'if (genbad==0) { print("K00_V27_P6R4_FAIL=RAW_GENERATOR_DROP"); quit; }',
            "ideal KUNIT=K,1;",
            'if (reduce(1,std(KUNIT))!=0) { print("K00_V27_P6R4_FAIL=FORCED_UNIT"); quit; }',
            f'write("{qpath(basis)}",string(Graw));',
            f'write("{qpath(transform)}",string(T));',
            ('print("K00_V27_P6R4_PRODUCER=PROPER_PASS"); '
             'print("K00_V27_P6R4_GSIZE="+string(ncols(Graw))); '
             'print("K00_V27_P6R4_PICKR="+string(pickr)); '
             'print("K00_V27_P6R4_PICKC="+string(pickc)); quit;'),
        ])
        producer_stdout = output / "full_p6_rank2_chart_proper_tracked.stdout"
        producer_stderr = output / "full_p6_rank2_chart_proper_tracked.stderr"
        try:
            producer_markers = run_singular(
                singular, producer, producer_stdout, producer_stderr, args.timeout)
        except ResourceCap:
            artifacts.extend([producer, producer_stdout, producer_stderr])
            emit_cap(output, lane, "TRACKED_FULL_P6_PROPER", producer, artifacts)
            return
        require_nonempty(basis)
        require_nonempty(transform)
        parsed = {
            key: re.search(rf"K00_V27_P6R4_{key}=(\d+)", producer_markers)
            for key in ("GSIZE", "PICKR", "PICKC")
        }
        if "K00_V27_P6R4_PRODUCER=PROPER_PASS" not in producer_markers or \
                any(value is None for value in parsed.values()):
            fail("full-P6 proper producer marker missing")
        values = {key: int(value.group(1)) for key, value in parsed.items()
                  if value is not None}
        replay = output / "full_p6_rank2_chart_proper_replay.sing"
        write_checked_script(replay, common + [
            f"ideal Graw={basis.read_text().strip()};",
            f"matrix T[{ngen}][{values['GSIZE']}]={transform.read_text().strip()};",
            "matrix ID=matrix(K)*T-matrix(Graw); int bad=0; int tc;",
            "for (tc=1;tc<=ncols(ID);tc++) { if (ID[1,tc]!=0) { bad++; } }",
            'if (bad) { print("K00_V27_P6R4_FAIL=SERIALIZED_IDENTITY"); quit; }',
            "ideal G=std(Graw); ideal P6NF=reduce(P6,G); ideal I3NF=reduce(I3A,G); poly chartNF=reduce(chart,G);",
            "int reversebad=0; int ri;",
            "for (ri=1;ri<=ncols(P6NF);ri++) { if (P6NF[ri]!=0) { reversebad++; } }",
            "for (ri=1;ri<=ncols(I3NF);ri++) { if (I3NF[ri]!=0) { reversebad++; } }",
            "if (chartNF!=0) { reversebad++; }",
            'if (reversebad) { print("K00_V27_P6R4_FAIL=RAW_REVERSE_REPLAY"); quit; }',
            (f'if ((reduce(1,G)!=1)||(dim(G)!={dimension})) '
             '{ print("K00_V27_P6R4_FAIL=SERIALIZED_PROPER"); quit; }'),
            (f"matrix TDROP=T; TDROP[{values['PICKR']},{values['PICKC']}]=0; "
             "matrix DROP=matrix(K)*TDROP-matrix(Graw); int dropbad=0;"),
            "for (tc=1;tc<=ncols(DROP);tc++) { if (DROP[1,tc]!=0) { dropbad++; } }",
            'if (dropbad==0) { print("K00_V27_P6R4_FAIL=SERIALIZED_DROP"); quit; }',
            (f"matrix TADD=T; TADD[{values['PICKR']},{values['PICKC']}]=TADD[{values['PICKR']},{values['PICKC']}]+1; "
             "matrix ADD=matrix(K)*TADD-matrix(Graw); int addbad=0;"),
            "for (tc=1;tc<=ncols(ADD);tc++) { if (ADD[1,tc]!=0) { addbad++; } }",
            'if (addbad==0) { print("K00_V27_P6R4_FAIL=SERIALIZED_ADD"); quit; }',
            (f"ideal KDROP=K; KDROP[{values['PICKR']}]=0; "
             "matrix GDROP=matrix(KDROP)*T-matrix(Graw); int genbad=0;"),
            "for (tc=1;tc<=ncols(GDROP);tc++) { if (GDROP[1,tc]!=0) { genbad++; } }",
            'if (genbad==0) { print("K00_V27_P6R4_FAIL=SERIALIZED_GENERATOR_DROP"); quit; }',
            "ideal KUNIT=K,1;",
            'if (reduce(1,std(KUNIT))!=0) { print("K00_V27_P6R4_FAIL=SERIALIZED_FORCED_UNIT"); quit; }',
            'print("K00_V27_P6R4_RAW_REVERSE=PASS"); '
            'print("K00_V27_P6R4_SECOND_PROCESS=PROPER_PASS"); quit;',
        ])
        replay_stdout = output / "full_p6_rank2_chart_proper_replay.stdout"
        replay_stderr = output / "full_p6_rank2_chart_proper_replay.stderr"
        try:
            replay_markers = run_singular(
                singular, replay, replay_stdout, replay_stderr,
                min(args.timeout, 7200))
        except ResourceCap:
            artifacts.extend([producer, producer_stdout, producer_stderr,
                              basis, transform, replay, replay_stdout, replay_stderr])
            emit_cap(output, lane, "SERIALIZED_FULL_P6_PROPER_REPLAY", replay, artifacts)
            return
        if "K00_V27_P6R4_RAW_REVERSE=PASS" not in replay_markers or \
                "K00_V27_P6R4_SECOND_PROCESS=PROPER_PASS" not in replay_markers:
            fail("full-P6 proper replay marker missing")
        artifacts.extend([producer, producer_stdout, producer_stderr, basis,
                          transform, replay, replay_stdout, replay_stderr])
        status = PROPER_STATUS
        certificate_kind = "TRACKED_PROPER_STANDARD_BASIS"
        gsize = values["GSIZE"]
        pick = [values["PICKR"], values["PICKC"]]
    else:
        certificate = output / "FULL_P6_RANK2_CHART_UNIT_BEZOUT.matrix"
        producer = output / "full_p6_rank2_chart_unit_tracked.sing"
        write_checked_script(producer, common + [
            "matrix T; ideal Graw=liftstd(K,T);",
            (f'if ((nrows(T)!={ngen})||(ncols(T)!=ncols(Graw))) '
             '{ print("K00_V27_P6R4_FAIL=UNIT_TRACKED_SHAPE"); quit; }'),
            "matrix BID=matrix(K)*T-matrix(Graw); int bad=0; int tc;",
            "for (tc=1;tc<=ncols(BID);tc++) { if (BID[1,tc]!=0) { bad++; } }",
            'if (bad) { print("K00_V27_P6R4_FAIL=UNIT_TRACKED_IDENTITY"); quit; }',
            'if (reduce(1,Graw)!=0) { print("K00_V27_P6R4_FAIL=UNIT_TRACKED_NOT_UNIT"); quit; }',
            "int unitcol=0;",
            "for (cc=1;cc<=ncols(Graw);cc++) { if ((unitcol==0)&&(Graw[cc]!=0)&&(deg(Graw[cc])==0)) { unitcol=cc; } }",
            'if (unitcol==0) { print("K00_V27_P6R4_FAIL=UNIT_CONSTANT_COLUMN"); quit; }',
            f"matrix C[{ngen}][1];",
            f"for (rr=1;rr<={ngen};rr++) {{ C[rr,1]=T[rr,unitcol]/Graw[unitcol]; }}",
            "matrix UID=matrix(K)*C;",
            'if (UID[1,1]!=1) { print("K00_V27_P6R4_FAIL=UNIT_BEZOUT_IDENTITY"); quit; }',
            "int pickr=0;",
            f"for (rr=1;rr<={ngen};rr++) {{ if ((pickr==0)&&(K[rr]!=0)&&(C[rr,1]!=0)) {{ pickr=rr; }} }}",
            'if (pickr==0) { print("K00_V27_P6R4_FAIL=UNIT_COEFFICIENT_PICK"); quit; }',
            "matrix CDROP=C; CDROP[pickr,1]=0; matrix DROP=matrix(K)*CDROP;",
            'if (DROP[1,1]==1) { print("K00_V27_P6R4_FAIL=UNIT_COEFFICIENT_DROP"); quit; }',
            "matrix CADD=C; CADD[pickr,1]=CADD[pickr,1]+1; matrix ADD=matrix(K)*CADD;",
            'if (ADD[1,1]==1) { print("K00_V27_P6R4_FAIL=UNIT_COEFFICIENT_ADD"); quit; }',
            "ideal KDROP=K; KDROP[pickr]=0; matrix GDROP=matrix(KDROP)*C;",
            'if (GDROP[1,1]==1) { print("K00_V27_P6R4_FAIL=RAW_GENERATOR_DROP"); quit; }',
            f'write("{qpath(certificate)}",string(C));',
            ('print("K00_V27_P6R4_PRODUCER=UNIT_PASS"); '
             'print("K00_V27_P6R4_GSIZE="+string(ncols(Graw))); '
             'print("K00_V27_P6R4_PICKR="+string(pickr)); quit;'),
        ])
        producer_stdout = output / "full_p6_rank2_chart_unit_tracked.stdout"
        producer_stderr = output / "full_p6_rank2_chart_unit_tracked.stderr"
        try:
            producer_markers = run_singular(
                singular, producer, producer_stdout, producer_stderr, args.timeout)
        except ResourceCap:
            artifacts.extend([producer, producer_stdout, producer_stderr])
            emit_cap(output, lane, "TRACKED_FULL_P6_UNIT", producer, artifacts)
            return
        require_nonempty(certificate)
        match_gsize = re.search(r"K00_V27_P6R4_GSIZE=(\d+)", producer_markers)
        match_pick = re.search(r"K00_V27_P6R4_PICKR=(\d+)", producer_markers)
        if "K00_V27_P6R4_PRODUCER=UNIT_PASS" not in producer_markers or \
                match_gsize is None or match_pick is None:
            fail("full-P6 unit producer marker missing")
        gsize = int(match_gsize.group(1))
        pickr = int(match_pick.group(1))
        replay = output / "full_p6_rank2_chart_unit_replay.sing"
        write_checked_script(replay, common + [
            f"matrix C[{ngen}][1]={certificate.read_text().strip()};",
            "matrix UID=matrix(K)*C;",
            'if (UID[1,1]!=1) { print("K00_V27_P6R4_FAIL=SERIALIZED_UNIT_IDENTITY"); quit; }',
            "ideal G=std(K);",
            'if (reduce(1,G)!=0) { print("K00_V27_P6R4_FAIL=SERIALIZED_NOT_UNIT"); quit; }',
            f"matrix CDROP=C; CDROP[{pickr},1]=0; matrix DROP=matrix(K)*CDROP;",
            'if (DROP[1,1]==1) { print("K00_V27_P6R4_FAIL=SERIALIZED_UNIT_DROP"); quit; }',
            f"matrix CADD=C; CADD[{pickr},1]=CADD[{pickr},1]+1; matrix ADD=matrix(K)*CADD;",
            'if (ADD[1,1]==1) { print("K00_V27_P6R4_FAIL=SERIALIZED_UNIT_ADD"); quit; }',
            f"ideal KDROP=K; KDROP[{pickr}]=0; matrix GDROP=matrix(KDROP)*C;",
            'if (GDROP[1,1]==1) { print("K00_V27_P6R4_FAIL=SERIALIZED_GENERATOR_DROP"); quit; }',
            'print("K00_V27_P6R4_RAW_RECONSTRUCTION=PASS"); '
            'print("K00_V27_P6R4_SECOND_PROCESS=UNIT_PASS"); quit;',
        ])
        replay_stdout = output / "full_p6_rank2_chart_unit_replay.stdout"
        replay_stderr = output / "full_p6_rank2_chart_unit_replay.stderr"
        try:
            replay_markers = run_singular(
                singular, replay, replay_stdout, replay_stderr,
                min(args.timeout, 7200))
        except ResourceCap:
            artifacts.extend([producer, producer_stdout, producer_stderr,
                              certificate, replay, replay_stdout, replay_stderr])
            emit_cap(output, lane, "SERIALIZED_FULL_P6_UNIT_REPLAY", replay, artifacts)
            return
        if "K00_V27_P6R4_RAW_RECONSTRUCTION=PASS" not in replay_markers or \
                "K00_V27_P6R4_SECOND_PROCESS=UNIT_PASS" not in replay_markers:
            fail("full-P6 unit replay marker missing")
        artifacts.extend([producer, producer_stdout, producer_stderr,
                          certificate, replay, replay_stdout, replay_stderr])
        status = UNIT_STATUS
        certificate_kind = "EXACT_UNIT_BEZOUT_COLUMN"
        pick = [pickr, 1]

    for artifact in artifacts:
        if artifact.suffix == ".stderr":
            if artifact.read_bytes():
                fail(("nonempty Singular stderr", artifact.name))
        else:
            require_nonempty(artifact)
    payload = {
        "status": status,
        "lifecycle": "PRODUCER_UNREVIEWED_SPECULATIVE_ROLLBACK_R1_R2_R3",
        "field": "Q_exact",
        "registered_aws_lane": lane,
        "singular_version": version,
        "target": "P6_PLUS_I3A_PLUS_Z_TIMES_SELECTED_I2_MINOR_MINUS_1",
        "P6_literal_rows": 49,
        "P6_literal_zero_rows": 15,
        "P6_raw_nonzero_generators_plus_F10": 35,
        "I3_raw_stored_generators": 813,
        "raw_target_generator_count": ngen,
        "selected_minor": {
            "singular_minor_object_column": 37,
            "rows_one_based": [5, 7],
            "columns_one_based": [6, 7],
            "stored_sign": -1,
            "sha256": PINNED_SHA256[MINOR_REL],
            "normal_form_mod_base_J2_sha256": PINNED_SHA256[NF_REL],
        },
        "Kfull_unit": is_unit,
        "exact_affine_dimension": dimension,
        "selected_chart_has_full_P6_algebraic_rank_exact_2_point": is_proper,
        "unit_kills_only_selected_full_P6_chart": is_unit,
        "grade_seven_compatibility_claim": False,
        "rational_point_claim": False,
        "exact_Q_witness_serialized": False,
        "fresh_base_R1_R2_R3_controls": {
            "J4_J3_J2_dimensions_in_full_ring_with_z": 31,
            "J1_dimension_in_full_ring_with_z": 30,
            "I4_outside_J4": 0,
            "I3_outside_J3": 0,
            "I2_outside_J2": 291,
            "I2_inside_J2": 60,
        },
        "certificate_kind": certificate_kind,
        "standard_basis_size": gsize,
        "certificate_mutation_pick": pick,
        "raw_generator_replay": True,
        "raw_generator_drop_mutation": True,
        "origin_excluded_by_chart": True,
        "chart_constant_drop_origin_mutation": True,
        "source_hashes": PINNED_SHA256,
        "sampled_pencil_claims_consumed": False,
        "artifacts": {
            path.name: {"sha256": digest(path), "bytes": path.stat().st_size}
            for path in artifacts
        },
        "scope": "ONE_SELECTED_FULL_P6_PRIOR_PREFIX_EXACT_RANK2_CHART_ONLY",
        "firewall": (
            "NO_SECOND_MINOR_NO_RATIONAL_POINT_NO_GRADE7_E_CONDITION_NO_LATER_GRADE_"
            "NO_LIFT_NO_JET_NO_ARC_NO_CLOSURE_NO_COUNTEREXAMPLE_NO_JC2"
        ),
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V27_P6R4=" + status)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
