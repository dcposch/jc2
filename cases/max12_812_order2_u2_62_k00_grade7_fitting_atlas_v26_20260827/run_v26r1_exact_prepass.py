#!/usr/bin/env python3
"""Exact rollback-tagged V26R1 coefficient-base rank prepass.

The V24R6R1 dependency has an internal same-family audit only.  Results remain
provisional and non-promotable while the independent Opus5 cross-audit is
pending.
"""

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


COMPILER_STATUS = "PASS_V26_FITTING_ATLAS_COMPILED_NO_STRATUM_DECISION"
RELEASE_STATUS = \
    "PASS_V26R1_W0_DESCENDANT_COMPILED_PROVISIONAL_ROLLBACK_TAG"
ROLLBACK_TAG = "PROVISIONAL_ROLLBACK_TAG_OPUS5_PENDING"


class ResourceCap(RuntimeError):
    pass


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def qpath(path: Path) -> str:
    value = str(path.resolve())
    if '"' in value or "\n" in value:
        fail(("unsafe output path", value))
    return value


def validate_manifest(directory: Path, name: str) -> None:
    path = directory / name
    if not path.is_file():
        fail(("manifest missing", str(path)))
    for line in path.read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
        if match is None:
            fail(("malformed manifest", name, line))
        artifact = directory / match.group(2)
        if not artifact.is_file() or digest(artifact) != match.group(1):
            fail(("manifest replay mismatch", str(artifact)))


def validate_inputs(compiled: Path, release: Path) -> tuple[dict, dict, dict]:
    validate_manifest(compiled, "COMPILED_SOURCE.sha256")
    validate_manifest(release, "RELEASE_FREEZE_V26R1.sha256")
    compiler_result = json.loads((compiled / "RESULT.json").read_text())
    release_result = json.loads((release / "RESULT.json").read_text())
    release_gate = json.loads((release / "RELEASE_V26R1_W0.json").read_text())
    if compiler_result.get("status") != COMPILER_STATUS or \
            release_result.get("status") != RELEASE_STATUS or \
            release_gate.get("released") is not True or \
            release_gate.get("rollback_tag") != ROLLBACK_TAG or \
            release_gate.get("external_cross_audit") != "OPUS5_PENDING" or \
            release_gate.get("promotion") != \
            "FORBIDDEN_UNTIL_OPUS5_CROSS_AUDIT_PASS_AND_ADJUDICATION":
        fail(("compiler/release endpoint mismatch",
              compiler_result.get("status"), release_result.get("status")))
    if release_gate.get("compiled_result_sha256") != \
            digest(compiled / "RESULT.json") or \
            release_gate.get("compiled_source_manifest_sha256") != \
            digest(compiled / "COMPILED_SOURCE.sha256") or \
            release_gate.get("full_rank_strata_preserved") != list(range(6)):
        fail("release/compiled binding mismatch")
    polys = json.loads((compiled / "ATLAS_EXACT_POLYNOMIALS.json").read_text())
    jobs = json.loads((compiled / "EXACT_Q_JOB_SPECS.json").read_text())
    if jobs.get("prepass", {}).get("job_id") != \
            "coefficient_base_B_plus_I5A":
        fail("exact prepass job missing")
    return compiler_result, polys, release_gate


def poly_text(item: dict) -> str:
    value = item.get("singular")
    if not isinstance(value, str) or not value:
        fail("compiled exact polynomial serialization missing")
    return value


def matrix_line(name: str, matrix: list[list[dict]]) -> str:
    if len(matrix) != 7 or any(len(row) != 7 for row in matrix):
        fail(("matrix shape", name))
    return f"matrix {name}[7][7]=" + ",".join(
        f"({poly_text(entry)})" for row in matrix for entry in row) + ";"


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
    if completed.returncode or completed.stderr or \
            re.search(r"(?m)^\s*\?", completed.stdout) or \
            "is no standard basis" in completed.stdout or \
            "K00_V26R1_PREPASS_FAIL=" in completed.stdout:
        fail(("exact prepass engine/replay failure", script.name,
              completed.returncode, completed.stderr[-2000:],
              completed.stdout[-3000:]))
    return completed.stdout


def emit_cap(output: Path, lane: str, stage: str, script: Path) -> None:
    payload = {
        "status": "RESOURCE_CAP_NO_VERDICT",
        "registered_aws_lane": lane,
        "stage": stage,
        "script_sha256": digest(script),
        "scope": "NO_EXACT_COEFFICIENT_BASE_RANK_PREPASS_VERDICT",
        "firewall": "NO_GRADE7_STRATUM_NO_LATER_GRADE_NO_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V26R1_PREPASS=RESOURCE_CAP_NO_VERDICT")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("compiled", type=Path)
    parser.add_argument("release", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=int, default=21000)
    args = parser.parse_args()
    if platform.system() != "Linux" or \
            Path("/sys/class/dmi/id/sys_vendor").read_text().strip() != "Amazon EC2":
        fail("AWS-only V26R1 exact prepass refused host")
    lane = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not lane:
        fail("registered AWS lane missing")
    compiled = args.compiled.resolve()
    release = args.release.resolve()
    compiler_result, polys, release_gate = validate_inputs(compiled, release)
    qlist = polys.get("Q1_to_Q6")
    if not isinstance(qlist, list) or len(qlist) != 6:
        fail("six-nonzero-grade2 list mismatch")
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    definitions = [
        "ring R=0,(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1),dp;",
        matrix_line("A", polys["A"]),
        "ideal B=" + ",".join(f"({poly_text(item)})" for item in qlist) +
        f",({poly_text(polys['F10'])});",
        'if (size(B)!=7) { print("K00_V26R1_PREPASS_FAIL=BASE_GENERATOR_CENSUS"); quit; }',
        "ideal I6A=minor(A,6);",
        "int i6bad=0; int i6i; for (i6i=1;i6i<=size(I6A);i6i++) { if (I6A[i6i]!=0) { i6bad=1; } }",
        'if (i6bad) { print("K00_V26R1_PREPASS_FAIL=I6A_NONZERO"); quit; }',
        "ideal I5A=minor(A,5);",
        "int i5nonzero=0; int i5i; for (i5i=1;i5i<=size(I5A);i5i++) { if (I5A[i5i]!=0) { i5nonzero=1; } }",
        'if (i5nonzero==0) { print("K00_V26R1_PREPASS_FAIL=I5A_ZERO"); quit; }',
        "int ipick=0; int ii;",
        "for (ii=1;ii<=size(I5A);ii++) { if ((ipick==0)&&(I5A[ii]!=0)) { ipick=ii; } }",
        'if (ipick==0) { print("K00_V26R1_PREPASS_FAIL=I5_MUTATION_PICK"); quit; }',
        "ideal I5M=I5A; I5M[ipick]=0;",
        'if ((I5M[ipick]!=0)||(I5A[ipick]==I5M[ipick])) { print("K00_V26R1_PREPASS_FAIL=I5_DELETE_MUTATION"); quit; }',
        "ideal CTRLproper=d0_1; ideal GCTRLproper=std(CTRLproper);",
        'if (reduce(1,GCTRLproper)==0) { print("K00_V26R1_PREPASS_FAIL=KNOWN_PROPER_CONTROL"); quit; }',
        "ideal CTRLunit=d0_1,1; ideal GCTRLunit=std(CTRLunit);",
        'if (reduce(1,GCTRLunit)!=0) { print("K00_V26R1_PREPASS_FAIL=FORCED_UNIT_CONTROL"); quit; }',
        "ideal J=B+I5A;",
    ]
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    preflight = output / "exact_prepass_branch.sing"
    preflight.write_text("\n".join(definitions + [
        "ideal S=slimgb(J); poly N1=reduce(1,S); int D=dim(S);",
        "if (N1==0)", "{",
        '  if (D!=-1) { print("K00_V26R1_PREPASS_FAIL=UNIT_DIMENSION"); quit; }',
        '  print("K00_V26R1_PREFLIGHT=UNIT"); print("K00_V26R1_DIM=-1"); print("K00_V26R1_NGEN="+string(size(J))); print("K00_V26R1_IPICK="+string(ipick)); quit;',
        "}",
        'if ((N1!=1)||(D<0)) { print("K00_V26R1_PREPASS_FAIL=PROPER_MARKERS"); quit; }',
        'print("K00_V26R1_PREFLIGHT=PROPER"); print("K00_V26R1_DIM="+string(D)); print("K00_V26R1_NGEN="+string(size(J))); print("K00_V26R1_IPICK="+string(ipick)); quit;',
    ]) + "\n")
    pre_stdout = output / "exact_prepass_branch.stdout"
    pre_stderr = output / "exact_prepass_branch.stderr"
    try:
        markers = run_singular(singular, preflight, pre_stdout, pre_stderr,
                               args.timeout)
    except ResourceCap:
        emit_cap(output, lane, "SLIMGB_BRANCH_PREFLIGHT", preflight)
        return
    parsed = {
        name: re.search(rf"K00_V26R1_{name}=(-?\d+)", markers)
        for name in ("DIM", "NGEN", "IPICK")
    }
    if any(value is None for value in parsed.values()):
        fail("preflight custody marker missing")
    values = {name: int(match.group(1))
              for name, match in parsed.items() if match}
    if values["NGEN"] <= 7 or values["IPICK"] <= 0:
        fail(("preflight generator/minor census", values))
    artifacts = [preflight, pre_stdout, pre_stderr]

    if "K00_V26R1_PREFLIGHT=UNIT" in markers:
        cert_path = output / "EXACT_PREPASS_UNIT_COEFFICIENTS.matrix"
        producer = output / "exact_prepass_unit_lift.sing"
        producer.write_text("\n".join(definitions + [
            'matrix U; matrix C=lift(J,ideal(1),U,"slimgb");',
            f'if ((nrows(C)!={values["NGEN"]})||(ncols(C)!=1)||(nrows(U)!=1)||(ncols(U)!=1)) {{ print("K00_V26R1_PREPASS_FAIL=UNIT_LIFT_SHAPE"); quit; }}',
            'if (U[1,1]!=1) { print("K00_V26R1_PREPASS_FAIL=UNIT_LIFT_U"); quit; }',
            'matrix UID=matrix(J)*C-matrix(ideal(1)); if (UID[1,1]!=0) { print("K00_V26R1_PREPASS_FAIL=UNIT_IDENTITY"); quit; }',
            "int pick=0; int jj;",
            f"for (jj=1;jj<={values['NGEN']};jj++) {{ if ((pick==0)&&(J[jj]!=0)&&(C[jj,1]!=0)) {{ pick=jj; }} }}",
            'if (pick==0) { print("K00_V26R1_PREPASS_FAIL=UNIT_MUTATION_PICK"); quit; }',
            "matrix CDROP=C; CDROP[pick,1]=0;",
            'matrix UDROPD=matrix(J)*CDROP-matrix(ideal(1)); if (UDROPD[1,1]==0) { print("K00_V26R1_PREPASS_FAIL=UNIT_DROP_MUTATION"); quit; }',
            "matrix CADD=C; CADD[pick,1]=CADD[pick,1]+1;",
            'matrix UADDD=matrix(J)*CADD-matrix(ideal(1)); if (UADDD[1,1]==0) { print("K00_V26R1_PREPASS_FAIL=UNIT_ADD_MUTATION"); quit; }',
            f'write("{qpath(cert_path)}",string(C));',
            'print("K00_V26R1_UNIT_PRODUCER=1"); print("K00_V26R1_CPICK="+string(pick)); quit;',
        ]) + "\n")
        producer_stdout = output / "exact_prepass_unit_lift.stdout"
        producer_stderr = output / "exact_prepass_unit_lift.stderr"
        try:
            producer_markers = run_singular(
                singular, producer, producer_stdout, producer_stderr,
                args.timeout)
        except ResourceCap:
            emit_cap(output, lane, "DIRECT_UNIT_LIFT", producer)
            return
        pick_match = re.search(r"K00_V26R1_CPICK=(\d+)", producer_markers)
        if "K00_V26R1_UNIT_PRODUCER=1" not in producer_markers or \
                pick_match is None or not cert_path.is_file():
            fail("unit certificate custody missing")
        pick = int(pick_match.group(1))
        replay = output / "exact_prepass_unit_replay.sing"
        replay.write_text("\n".join(definitions + [
            f"matrix C[{values['NGEN']}][1]={cert_path.read_text().strip()};",
            'matrix UID=matrix(J)*C-matrix(ideal(1)); if (UID[1,1]!=0) { print("K00_V26R1_PREPASS_FAIL=SERIALIZED_UNIT_IDENTITY"); quit; }',
            f"matrix CDROP=C; CDROP[{pick},1]=0;",
            'matrix UDROPD=matrix(J)*CDROP-matrix(ideal(1)); if (UDROPD[1,1]==0) { print("K00_V26R1_PREPASS_FAIL=SERIALIZED_DROP_MUTATION"); quit; }',
            f"matrix CADD=C; CADD[{pick},1]=CADD[{pick},1]+1;",
            'matrix UADDD=matrix(J)*CADD-matrix(ideal(1)); if (UADDD[1,1]==0) { print("K00_V26R1_PREPASS_FAIL=SERIALIZED_ADD_MUTATION"); quit; }',
            'print("K00_V26R1_UNIT_SECOND_PROCESS_REPLAY=1"); quit;',
        ]) + "\n")
        replay_stdout = output / "exact_prepass_unit_replay.stdout"
        replay_stderr = output / "exact_prepass_unit_replay.stderr"
        try:
            replay_markers = run_singular(
                singular, replay, replay_stdout, replay_stderr,
                min(args.timeout, 3600))
        except ResourceCap:
            emit_cap(output, lane, "SERIALIZED_UNIT_REPLAY", replay)
            return
        if "K00_V26R1_UNIT_SECOND_PROCESS_REPLAY=1" not in replay_markers:
            fail("unit second-process marker missing")
        artifacts.extend([producer, producer_stdout, producer_stderr,
                          cert_path, replay, replay_stdout, replay_stderr])
        status = \
            "PASS_V26R1_EXACT_PREPASS_RANK5_EVERYWHERE_PROVISIONAL_ROLLBACK_TAG"
        branch = "UNIT_B_PLUS_I5A"
        outcome = {"unit_certificate_entries": values["NGEN"],
                   "certificate_mutation_index": pick,
                   "serialized_second_process_replay": True}
    elif "K00_V26R1_PREFLIGHT=PROPER" in markers:
        basis_path = output / "EXACT_PREPASS_STANDARD_BASIS.txt"
        transform_path = output / "EXACT_PREPASS_TRANSFORM.matrix"
        producer = output / "exact_prepass_proper_tracked.sing"
        producer.write_text("\n".join(definitions + [
            "matrix T; ideal G=liftstd(J,T);",
            f'if ((nrows(T)!={values["NGEN"]})||(ncols(T)!=size(G))) {{ print("K00_V26R1_PREPASS_FAIL=TRACKED_BASIS_SHAPE"); quit; }}',
            'matrix TREPLAY=matrix(J)*T-matrix(G); int treplay_bad=0; int tc;',
            'for (tc=1;tc<=ncols(TREPLAY);tc++) { if (TREPLAY[1,tc]!=0) { treplay_bad=1; } }',
            'if (treplay_bad) { print("K00_V26R1_PREPASS_FAIL=TRACKED_BASIS_IDENTITY"); quit; }',
            "poly N1=reduce(1,G); int D=dim(G);",
            f'if ((N1!=1)||(D!={values["DIM"]})||(D<0)) {{ print("K00_V26R1_PREPASS_FAIL=TRACKED_PROPER_MARKERS"); quit; }}',
            "int pickr=0; int pickc=0; int rr; int cc;",
            f"for (cc=1;cc<=ncols(T);cc++) {{ for (rr=1;rr<={values['NGEN']};rr++) {{ if ((pickr==0)&&(J[rr]!=0)&&(T[rr,cc]!=0)) {{ pickr=rr; pickc=cc; }} }} }}",
            'if (pickr==0) { print("K00_V26R1_PREPASS_FAIL=TRANSFORM_MUTATION_PICK"); quit; }',
            "matrix TBAD=T; TBAD[pickr,pickc]=0;",
            'matrix TMUTREPLAY=matrix(J)*TBAD-matrix(G); int tmutation_nonzero=0;',
            'for (tc=1;tc<=ncols(TMUTREPLAY);tc++) { if (TMUTREPLAY[1,tc]!=0) { tmutation_nonzero=1; } }',
            'if (tmutation_nonzero==0) { print("K00_V26R1_PREPASS_FAIL=TRANSFORM_DROP_MUTATION"); quit; }',
            "ideal JUNIT=J,1; ideal GUNIT=std(JUNIT);",
            'if (reduce(1,GUNIT)!=0) { print("K00_V26R1_PREPASS_FAIL=FORCED_UNIT_MUTATION"); quit; }',
            f'write("{qpath(basis_path)}",string(G));',
            f'write("{qpath(transform_path)}",string(T));',
            'print("K00_V26R1_PROPER_PRODUCER=1"); print("K00_V26R1_GSIZE="+string(size(G))); print("K00_V26R1_TPICKR="+string(pickr)); print("K00_V26R1_TPICKC="+string(pickc)); quit;',
        ]) + "\n")
        producer_stdout = output / "exact_prepass_proper_tracked.stdout"
        producer_stderr = output / "exact_prepass_proper_tracked.stderr"
        try:
            producer_markers = run_singular(
                singular, producer, producer_stdout, producer_stderr,
                args.timeout)
        except ResourceCap:
            emit_cap(output, lane, "TRACKED_PROPER_LIFTSTD", producer)
            return
        proper_matches = {
            name: re.search(rf"K00_V26R1_{name}=(\d+)", producer_markers)
            for name in ("GSIZE", "TPICKR", "TPICKC")
        }
        if "K00_V26R1_PROPER_PRODUCER=1" not in producer_markers or \
                any(match is None for match in proper_matches.values()) or \
                not basis_path.is_file() or not transform_path.is_file():
            fail("proper tracked custody missing")
        proper_values = {name: int(match.group(1))
                         for name, match in proper_matches.items() if match}
        replay = output / "exact_prepass_proper_replay.sing"
        replay.write_text("\n".join(definitions + [
            f"ideal Graw={basis_path.read_text().strip()};",
            f"matrix T[{values['NGEN']}][{proper_values['GSIZE']}]={transform_path.read_text().strip()};",
            'matrix TREPLAY=matrix(J)*T-matrix(Graw); int treplay_bad=0; int tc;',
            'for (tc=1;tc<=ncols(TREPLAY);tc++) { if (TREPLAY[1,tc]!=0) { treplay_bad=1; } }',
            'if (treplay_bad) { print("K00_V26R1_PREPASS_FAIL=SERIALIZED_TRACKED_IDENTITY"); quit; }',
            'ideal G=std(Graw); ideal JNF=reduce(J,G);',
            'int reverse_bad=0; int reverse_i; for (reverse_i=1;reverse_i<=size(JNF);reverse_i++) { if (JNF[reverse_i]!=0) { reverse_bad=1; } }',
            'if (reverse_bad) { print("K00_V26R1_PREPASS_FAIL=SERIALIZED_REVERSE_INCLUSION"); quit; }',
            'print("K00_V26R1_SERIALIZED_RECOMPUTED_SB_REVERSE_INCLUSION=1");',
            "poly N1=reduce(1,G); int D=dim(G);",
            f'if ((N1!=1)||(D!={values["DIM"]})) {{ print("K00_V26R1_PREPASS_FAIL=SERIALIZED_PROPER_MARKERS"); quit; }}',
            f"matrix TBAD=T; TBAD[{proper_values['TPICKR']},{proper_values['TPICKC']}]=0;",
            'matrix TMUTREPLAY=matrix(J)*TBAD-matrix(Graw); int tmutation_nonzero=0;',
            'for (tc=1;tc<=ncols(TMUTREPLAY);tc++) { if (TMUTREPLAY[1,tc]!=0) { tmutation_nonzero=1; } }',
            'if (tmutation_nonzero==0) { print("K00_V26R1_PREPASS_FAIL=SERIALIZED_TRANSFORM_MUTATION"); quit; }',
            "ideal JUNIT=J,1; ideal GUNIT=std(JUNIT);",
            'if (reduce(1,GUNIT)!=0) { print("K00_V26R1_PREPASS_FAIL=SERIALIZED_FORCED_UNIT"); quit; }',
            'print("K00_V26R1_PROPER_SECOND_PROCESS_REPLAY=1"); quit;',
        ]) + "\n")
        replay_stdout = output / "exact_prepass_proper_replay.stdout"
        replay_stderr = output / "exact_prepass_proper_replay.stderr"
        try:
            replay_markers = run_singular(
                singular, replay, replay_stdout, replay_stderr,
                min(args.timeout, 3600))
        except ResourceCap:
            emit_cap(output, lane, "SERIALIZED_PROPER_REPLAY", replay)
            return
        if "K00_V26R1_PROPER_SECOND_PROCESS_REPLAY=1" not in replay_markers:
            fail("proper second-process marker missing")
        if "K00_V26R1_SERIALIZED_RECOMPUTED_SB_REVERSE_INCLUSION=1" not in \
                replay_markers:
            fail("recomputed serialized standard-basis marker missing")
        artifacts.extend([producer, producer_stdout, producer_stderr,
                          basis_path, transform_path, replay, replay_stdout,
                          replay_stderr])
        status = \
            "PASS_V26R1_EXACT_PREPASS_LOWER_RANK_LOCUS_SURVIVES_PROVISIONAL_ROLLBACK_TAG"
        branch = "PROPER_B_PLUS_I5A"
        outcome = {"exact_affine_dimension": values["DIM"],
                   "standard_basis_size": proper_values["GSIZE"],
                   "serialized_recomputed_standard_basis_reverse_inclusion": True,
                   "serialized_second_process_replay": True}
    else:
        fail("preflight branch marker missing")

    payload = {
        "status": status,
        "branch": branch,
        "field": "Q_exact",
        "registered_aws_lane": lane,
        "compiled_result_sha256": digest(compiled / "RESULT.json"),
        "release_sha256": digest(release / "RELEASE_V26R1_W0.json"),
        "dependency_review_sha256": release_gate["dependency_review_sha256"],
        "dependency_review_kind": "INTERNAL_SAME_FAMILY_SOL_ULTRA_ONLY",
        "rollback_tag": ROLLBACK_TAG,
        "external_cross_audit": "OPUS5_PENDING",
        "promotion": "FORBIDDEN_UNTIL_OPUS5_CROSS_AUDIT_PASS_AND_ADJUDICATION",
        "base_generator_provenance": [
            "G2_row1", "G2_row2", "G2_row3", "G2_row4", "G2_row5",
            "G2_row7", "F10"],
        "I6A_exact_zero": True,
        "I5_generator_deletion_mutation": True,
        **outcome,
        "artifacts": {path.name: {"sha256": digest(path),
                                    "bytes": path.stat().st_size}
                      for path in artifacts},
        "scope": "EXACT_SIX_VARIABLE_BASE_RANK_PREPASS_ONLY",
        "firewall": "NO_FULL_P6_GRADE7_COMPATIBILITY_NO_LATER_GRADE_NO_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print("K00_V26R1_PREPASS=" + status)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
