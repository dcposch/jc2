#!/usr/bin/env python3
"""Run one held V26 exact-Q job on a registered AWS lane.

Every output is deliberately chart/prepass/agreement-local and marked as
requiring a fresh second-process replay.  This worker cannot aggregate or
promote an atlas theorem.
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


ALLOWED_COMPILER_STATUS = "PASS_V26_FITTING_ATLAS_COMPILED_NO_STRATUM_DECISION"


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n"


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V26 exact worker refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V26 exact worker refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def qpath(path: Path) -> str:
    text = str(path.resolve())
    if '"' in text or "\n" in text:
        fail(("unsafe output path", text))
    return text


def validate_compiled(compiled: Path) -> tuple[dict, dict, dict]:
    required = ("RESULT.json", "ATLAS_EXACT_POLYNOMIALS.json", "EXACT_Q_JOB_SPECS.json",
                "A_COMPOUND_MINORS.json", "DETERMINANT_DAG.json", "CONTROLS.json",
                "SOURCE_RECONSTRUCTION_FIXTURES.json", "V24R2_DEPENDENCY.json",
                "COMPILED_SOURCE.sha256", "RELEASE_V24R2_EXACT.json",
                "RELEASE_FREEZE.sha256")
    for name in required:
        if not (compiled / name).is_file():
            fail(("compiled/release artifact missing", str(compiled / name)))
    result = json.loads((compiled / "RESULT.json").read_text())
    if result.get("status") != ALLOWED_COMPILER_STATUS:
        fail(("compiler status not consumable", result.get("status")))
    release = json.loads((compiled / "RELEASE_V24R2_EXACT.json").read_text())
    if release.get("released") is not True or not release.get("dependency", {}).get("release_allowed"):
        fail("exact-Q V24R2 release is absent or false")
    if release.get("compiled_source_sha256") != digest(compiled / "COMPILED_SOURCE.sha256"):
        fail("release/compiled-source binding mismatch")
    for line in (compiled / "RELEASE_FREEZE.sha256").read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
        if match is None:
            fail(("malformed release freeze line", line))
        path = compiled / match.group(2)
        if not path.is_file() or digest(path) != match.group(1):
            fail(("release freeze mismatch", str(path)))
    for line in (compiled / "COMPILED_SOURCE.sha256").read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
        if match is None:
            fail(("malformed compiled freeze line", line))
        path = compiled / match.group(2)
        if not path.is_file() or digest(path) != match.group(1):
            fail(("compiled freeze mismatch", str(path)))
    polys = json.loads((compiled / "ATLAS_EXACT_POLYNOMIALS.json").read_text())
    jobs = json.loads((compiled / "EXACT_Q_JOB_SPECS.json").read_text())
    if polys.get("format") != "K00_V26_EXACT_SPARSE_POLYNOMIALS_V1" or jobs.get("format") != "K00_V26_EXACT_Q_JOB_SPECS_V1":
        fail("compiled source format drift")
    return result, polys, jobs


def poly_text(item: dict) -> str:
    text = item.get("singular")
    if not isinstance(text, str) or not text:
        fail("missing Singular polynomial serialization")
    return text


def matrix_line(name: str, matrix: list[list[dict]]) -> str:
    rows = len(matrix)
    columns = len(matrix[0]) if rows else 0
    if not rows or any(len(row) != columns for row in matrix):
        fail(("matrix shape", name))
    return f"matrix {name}[{rows}][{columns}]=" + ",".join(
        f"({poly_text(entry)})" for row in matrix for entry in row) + ";"


def control_lines() -> list[str]:
    return [
        "ideal CTRLproper=d0_1; ideal GCTRLproper=std(CTRLproper);",
        'if (reduce(1,GCTRLproper)==0) { print("K00_V26_WORKER_FAIL=KNOWN_PROPER_CONTROL"); quit; }',
        "ideal CTRLunit=d0_1,1; ideal GCTRLunit=std(CTRLunit);",
        'if (reduce(1,GCTRLunit)!=0) { print("K00_V26_WORKER_FAIL=FORCED_UNIT_CONTROL"); quit; }',
        'print("K00_V26_WORKER_CONTROLS=PASS");',
    ]


def tracked_decision_lines(ideal_name: str, prefix: str, output: Path) -> list[str]:
    basis = output / "EXACT_STANDARD_BASIS.txt"
    transform = output / "EXACT_LIFTSTD_TRANSFORM.matrix"
    unit = output / "EXACT_UNIT_COEFFICIENTS.matrix"
    return [
        f"matrix T; ideal G=liftstd({ideal_name},T);",
        f"matrix BASISREPLAY=matrix({ideal_name})*T-matrix(G);",
        f'if (BASISREPLAY!=0) {{ print("K00_V26_WORKER_FAIL={prefix}_LIFTSTD_REPLAY"); quit; }}',
        "poly N1=reduce(1,G); int D=dim(G);",
        f'print("K00_V26_{prefix}_DIM="+string(D));',
        f'if ((N1==0)&&(D!=-1)) {{ print("K00_V26_WORKER_FAIL={prefix}_UNIT_DIMENSION_MARKER"); quit; }}',
        "if (N1==0)",
        "{",
        f"  matrix Hunit=lift(G,ideal(1)); matrix Cunit=T*Hunit;",
        f"  matrix UNITREPLAY=matrix({ideal_name})*Cunit-matrix(ideal(1));",
        f'  if (UNITREPLAY!=0) {{ print("K00_V26_WORKER_FAIL={prefix}_UNIT_REPLAY"); quit; }}',
        f'  write("{qpath(unit)}",Cunit);',
        f'  print("K00_V26_{prefix}_BRANCH=UNIT");',
        "  quit;",
        "}",
        f'if ((N1!=1)||(D<0)) {{ print("K00_V26_WORKER_FAIL={prefix}_PROPERNESS_MARKERS"); quit; }}',
        f'write("{qpath(basis)}",G); write("{qpath(transform)}",T);',
        f'print("K00_V26_{prefix}_BRANCH=PROPER");',
        "quit;",
    ]


def find_chart(jobs: dict, job_id: str) -> tuple[int, dict] | None:
    for rank, data in jobs["rank_strata"].items():
        for chart in data["charts"]:
            if chart["chart_id"] == job_id:
                return int(rank), chart
    return None


def build_script(job_id: str, polys: dict, jobs: dict, output: Path) -> tuple[str, dict[str, object]]:
    prior = list(polys["ring_variables"])
    a = polys["A"]
    b = polys["b"]
    e = [a[row] + [{**b[row], "singular": "-(" + poly_text(b[row]) + ")"}]
         for row in range(7)]
    if job_id == "coefficient_base_B_plus_I5A":
        lines = [f"ring R=0,({','.join(prior[:30:5])}),dp;"]
        # prior[:30:5] is d0_1,...,d5_1 by the frozen ordering.
        if prior[:30:5] != [f"d{i}_1" for i in range(6)]:
            fail("leading-variable ordering drift")
        lines += control_lines()
        lines.append(matrix_line("A", a))
        q = [poly_text(item) for item in polys["Q1_to_Q6"]]
        lines.append("ideal B=" + ",".join(f"({item})" for item in q + [poly_text(polys["F10"])]) + ";")
        lines.append("ideal I6A=minor(A,6);")
        lines.append('if (I6A!=0) { print("K00_V26_WORKER_FAIL=PREPASS_I6A_NONZERO"); quit; }')
        lines.append("ideal I5A=minor(A,5); ideal J=B+I5A;")
        lines += tracked_decision_lines("J", "PREPASS", output)
        return "\n".join(lines) + "\n", {"kind": "prepass", "job_id": job_id}

    if job_id == "D_W_I6E_equals_Comp6_Comp7":
        lines = [f"ring R=0,({','.join(prior)},zinv),dp;"] + control_lines()
        lines += [matrix_line("A", a), matrix_line("E", e)]
        lines.append(f"poly W=({poly_text(polys['W'])});")
        lines.append(f"poly Comp6=({poly_text(polys['Comp6_Comp7'][0])}); poly Comp7=({poly_text(polys['Comp6_Comp7'][1])});")
        lines.append("ideal I6A=minor(A,6);")
        lines.append('if (I6A!=0) { print("K00_V26_WORKER_FAIL=AGREEMENT_I6A_NONZERO"); quit; }')
        lines.append("ideal TARGET=minor(E,6); ideal J=Comp6,Comp7,zinv*W-1;")
        lines.append("matrix T; ideal G=liftstd(J,T); matrix BASISREPLAY=matrix(J)*T-matrix(G);")
        lines.append('if (BASISREPLAY!=0) { print("K00_V26_WORKER_FAIL=AGREEMENT_LIFTSTD_REPLAY"); quit; }')
        lines.append("ideal NT=reduce(TARGET,G);")
        lines.append('if (NT!=0) { print("K00_V26_WORKER_FAIL=I6E_NOT_IN_COMP_LOCALIZED"); quit; }')
        lines.append("matrix H=lift(G,TARGET); matrix C=T*H; matrix MEMBERREPLAY=matrix(J)*C-matrix(TARGET);")
        lines.append('if (MEMBERREPLAY!=0) { print("K00_V26_WORKER_FAIL=AGREEMENT_MEMBER_REPLAY"); quit; }')
        lines.append(f'write("{qpath(output / "AGREEMENT_COEFFICIENTS.matrix")}",C);')
        lines.append('print("K00_V26_AGREEMENT_BRANCH=PASS_EXACT_LOCALIZED_INCLUSION"); quit;')
        return "\n".join(lines) + "\n", {"kind": "agreement", "job_id": job_id}

    located = find_chart(jobs, job_id)
    if located is None:
        fail(("unknown exact job id", job_id))
    rank, chart = located
    lines = [f"ring R=0,({','.join(prior)},zinv),dp;"] + control_lines()
    lines += [matrix_line("A", a), matrix_line("E", e)]
    p6 = [poly_text(item) for item in polys["P6_nonzero_generators_plus_F10"]]
    lines.append("ideal P6=" + ",".join(f"({item})" for item in p6) + ";")
    lines.append(f"ideal IA=minor(A,{rank + 1}); ideal IE=minor(E,{rank + 1});")
    localizer = poly_text(chart["localizer"])
    lines.append(f"poly chartMinor=({localizer});")
    lines.append('if (chartMinor==0) { print("K00_V26_WORKER_FAIL=ZERO_CHART_LOCALIZER"); quit; }')
    lines.append("ideal J=P6+IA+IE,zinv*k10_0*chartMinor-1;")
    lines += tracked_decision_lines("J", f"RANK{rank}", output)
    return "\n".join(lines) + "\n", {
        "kind": "rank_chart", "job_id": job_id, "rank": rank,
        "localizer_sha256": chart["localizer"]["sha256"],
        "minor_sources": chart["minor_sources"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("compiled", type=Path)
    parser.add_argument("job_id")
    parser.add_argument("output", type=Path)
    parser.add_argument("--timeout", type=int, default=21600)
    args = parser.parse_args()
    lane = require_aws()
    compiled = args.compiled.resolve()
    compiler_result, polys, jobs = validate_compiled(compiled)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    script_text, metadata = build_script(args.job_id, polys, jobs, output)
    script = output / "exact_job.sing"
    script.write_text(script_text)
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    try:
        completed = subprocess.run([singular, "-q", str(script)], cwd=output, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   timeout=args.timeout)
    except subprocess.TimeoutExpired as error:
        (output / "singular.stdout").write_text(error.stdout or "")
        (output / "singular.stderr").write_text(error.stderr or "")
        payload = {"status": "RESOURCE_CAP_NO_VERDICT", "job": metadata,
                   "registered_aws_lane": lane, "timeout_seconds": args.timeout,
                   "requires_second_process_replay": True,
                   "scope": "NO_PREPASS_CHART_OR_ATLAS_VERDICT"}
        (output / "RESULT.json").write_text(canonical_json(payload))
        print("K00_V26_WORKER=RESOURCE_CAP_NO_VERDICT")
        return
    stdout = output / "singular.stdout"
    stderr = output / "singular.stderr"
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    if completed.returncode != 0 or completed.stderr or "K00_V26_WORKER_FAIL=" in completed.stdout:
        fail(("Singular exact worker failure", completed.returncode, completed.stderr[-2000:], completed.stdout[-3000:]))
    if "K00_V26_WORKER_CONTROLS=PASS" not in completed.stdout:
        fail("worker controls marker missing")

    if metadata["kind"] == "agreement":
        marker = "K00_V26_AGREEMENT_BRANCH=PASS_EXACT_LOCALIZED_INCLUSION"
        if marker not in completed.stdout or not (output / "AGREEMENT_COEFFICIENTS.matrix").is_file():
            fail("agreement endpoint/certificate missing")
        status = "PASS_EXACT_V24_DW_AGREEMENT_UNREVIEWED"
        branch = "I6E_LOCALIZED_AT_W_GENERATED_BY_COMP6_COMP7"
    else:
        prefix = "PREPASS" if metadata["kind"] == "prepass" else f"RANK{metadata['rank']}"
        if f"K00_V26_{prefix}_BRANCH=UNIT" in completed.stdout:
            status = ("PASS_EXACT_PREPASS_UNIT_UNREVIEWED" if metadata["kind"] == "prepass"
                      else "PASS_EXACT_RANK_CHART_EMPTY_UNREVIEWED")
            branch = "UNIT"
        elif f"K00_V26_{prefix}_BRANCH=PROPER" in completed.stdout:
            status = ("PASS_EXACT_PREPASS_PROPER_UNREVIEWED" if metadata["kind"] == "prepass"
                      else "PASS_EXACT_RANK_CHART_PROPER_UNREVIEWED")
            branch = "PROPER"
        else:
            fail(("worker endpoint marker missing", prefix, completed.stdout[-2000:]))

    artifacts = {}
    for path in sorted(output.iterdir()):
        if path.is_file() and path.name != "RESULT.json":
            artifacts[path.name] = {"sha256": digest(path), "bytes": path.stat().st_size}
    payload = {
        "status": status, "branch": branch, "job": metadata,
        "registered_aws_lane": lane,
        "compiled_result_sha256": digest(compiled / "RESULT.json"),
        "compiled_source_sha256": digest(compiled / "COMPILED_SOURCE.sha256"),
        "v24r2_release_sha256": digest(compiled / "RELEASE_V24R2_EXACT.json"),
        "artifacts": artifacts,
        "requires_second_process_replay": True,
        "promotion": "FORBIDDEN_UNTIL_SECOND_PROCESS_REPLAY_AND_ATLAS_AGGREGATION",
        "scope": "ONE_EXACT_PREPASS_OR_LOCALIZED_AGREEMENT_OR_RANK_MINOR_CHART_ONLY",
        "firewall": "NO_AGGREGATE_STRATUM_NO_LATER_GRADE_NO_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    (output / "RESULT.json").write_text(canonical_json(payload))
    print("K00_V26_WORKER=" + status)
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
