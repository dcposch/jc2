#!/usr/bin/env python3
"""Bind internally audited R6R1 W=0 evidence to a held V26 atlas.

This bridge releases only rollback-tagged computation.  It is not a theorem
promotion: the independent Opus5 cross-audit of V24R6R1 is still pending.
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


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REVIEW = ROOT / "xmodel/max12-812-order2-k00-v24r6r1-leading-base-dw-hostile-review-sol-ultra-20260827.md"
ADJUDICATION = ROOT / "cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/ADJUDICATION_V24R6R1.md"
REVIEWED_BUNDLE = ROOT / "cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/REVIEWED_BUNDLE_R6R1.sha256"
SYZYGY_RESULT = ROOT / "cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/aws_box02_r6r1_w_syzygy_replay/output/RESULT.json"
A_PATHS = {
    1: ROOT / "cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/aws_box02_r6r1_w_syzygy_replay/output/W_SYZYGY_A1.txt",
    3: ROOT / "cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/aws_box02_r6r1_w_syzygy_replay/output/W_SYZYGY_A3.txt",
    4: ROOT / "cases/max12_812_order2_u2_62_k00_grade7_cokernel_v24_20260827/aws_box02_r6r1_w_syzygy_replay/output/W_SYZYGY_A4.txt",
}
NOTATION = HERE / "NOTATION_CLARIFICATION_R1_GRADE2_ROWS.md"
PREREG = HERE / "PREREGISTRATION_R1_W0_DESCENDANT.md"
EXPECTED = {
    REVIEW: "f9d2afcb01c1ad1161783d0ff51d9d47d1a6aa5831b508936072f0c9170012b9",
    ADJUDICATION: "1883b74bca991064582c0d7d7180155e05eb0cb985d931b11c980d306bd7e238",
    REVIEWED_BUNDLE: "82056ca4b91bfb29dc0d77eaca5cbb8faf5228ee9f8e770cdec905b9ce8d99f2",
    SYZYGY_RESULT: "8cd2afdd86f3f94749cbfcefa57055c437fc95ece2480ab9455e138aa56dc9ce",
    A_PATHS[1]: "577d1327c2bdb3b99efbd83a95857a308ae9de1207b1544b9b12213ef6a44b3b",
    A_PATHS[3]: "806f0d799bfd657d79582e8cf3c8d7cff026e8623361a32a314ecfdbd60726ec",
    A_PATHS[4]: "9193acca0c63f157878ab9f71c10ad8940d4481e23c9f7ee5e14765740fd0d42",
    NOTATION: "794b1d8e399e8b331a45acfa5df94d4552b47890c23686ce215948c0ea749995",
    PREREG: "1a8f75008c97d0dd3a3ac380c6ec7067c7add564094ae3a93fc28ee6ff8997b1",
}
EXPECTED_COMPILED_RESULT = "f1a6f1fc988fc77816daaab13b294b1321de7e476d2891cf7fbfa2e033868d97"
EXPECTED_COMPILED_SOURCE = "5de20da0d3501db668fca38db3c678ba4719745e3df7b32d0d0a8d2867e4da32"


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n"


def map_leading(text: str) -> str:
    mapped = text
    for index in range(6):
        mapped = re.sub(rf"\bx{index}\b", f"d{index}_1", mapped)
    if re.search(r"\bx[0-5]\b", mapped):
        fail("incomplete leading-variable source map")
    return mapped


def validate_manifest(directory: Path, name: str) -> dict[str, str]:
    manifest = directory / name
    if not manifest.is_file():
        fail(("compiled manifest missing", str(manifest)))
    checked: dict[str, str] = {}
    for line in manifest.read_text().splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+)", line)
        if match is None:
            fail(("malformed compiled manifest", name, line))
        path = directory / match.group(2)
        if not path.is_file() or digest(path) != match.group(1):
            fail(("compiled manifest mismatch", str(path)))
        checked[path.name] = match.group(1)
    return checked


def run_replay(singular: str, script: Path, stdout: Path,
               stderr: Path) -> None:
    completed = subprocess.run(
        [singular, "-q", str(script)], cwd=script.parent, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1800)
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    if completed.returncode or completed.stderr or \
            re.search(r"(?m)^\s*\?", completed.stdout) or \
            "K00_V26R1_RELEASE_FAIL=" in completed.stdout or \
            "K00_V26R1_W0_BRIDGE_REPLAY=1" not in completed.stdout:
        fail(("W=0 release bridge replay failure", completed.returncode,
              completed.stderr[-1000:], completed.stdout[-2000:]))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("compiled", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if platform.system() != "Linux" or \
            Path("/sys/class/dmi/id/sys_vendor").read_text().strip() != "Amazon EC2":
        fail("AWS-only V26R1 release compiler refused host")
    lane = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not lane:
        fail("registered AWS lane missing")
    for path, wanted in EXPECTED.items():
        if digest(path) != wanted:
            fail(("internally audited dependency byte mismatch", str(path),
                  digest(path), wanted))
    syzygy = json.loads(SYZYGY_RESULT.read_text())
    if syzygy.get("status") != "PASS_EXACT_Q_W_IN_IDEAL_Q1_Q3_Q4_REPLAYED":
        fail("internally audited syzygy status mismatch")

    compiled = args.compiled.resolve()
    source_hashes = validate_manifest(compiled, "COMPILED_SOURCE.sha256")
    result_path = compiled / "RESULT.json"
    if not result_path.is_file():
        fail("held compiler result missing")
    if digest(result_path) != EXPECTED_COMPILED_RESULT or digest(
            compiled / "COMPILED_SOURCE.sha256") != EXPECTED_COMPILED_SOURCE:
        fail("frozen held compiler byte mismatch")
    result = json.loads(result_path.read_text())
    if result.get("status") != \
            "PASS_V26_FITTING_ATLAS_COMPILED_NO_STRATUM_DECISION" or \
            result.get("dependency", {}).get("release_allowed") is not False:
        fail(("held compiler endpoint mismatch", result.get("status"),
              result.get("dependency")))
    for name, metadata in result.get("artifacts", {}).items():
        path = compiled / name
        if not path.is_file() or not isinstance(metadata, dict) or \
                digest(path) != metadata.get("sha256"):
            fail(("compiled result artifact mismatch", name))

    polys = json.loads((compiled / "ATLAS_EXACT_POLYNOMIALS.json").read_text())
    jobs = json.loads((compiled / "EXACT_Q_JOB_SPECS.json").read_text())
    qlist = polys.get("Q1_to_Q6")
    literal = polys.get("P6_literal_rows_through_grade6")
    if not isinstance(qlist, list) or len(qlist) != 6 or \
            not isinstance(literal, list):
        fail("compiled grade-two payload shape")
    grade2 = [(item.get("row"), item.get("poly")) for item in literal
              if item.get("Lambda_grade") == 2 and item.get("poly", {}).get("terms")]
    if [row for row, _ in grade2] != [1, 2, 3, 4, 5, 7] or \
            [poly for _, poly in grade2] != qlist:
        fail(("six-nonzero-grade2 provenance mismatch",
              [row for row, _ in grade2]))
    if set(jobs.get("rank_strata", {})) != {str(index) for index in range(6)} or \
            any(not jobs["rank_strata"][str(index)].get("charts")
                for index in range(6)):
        fail("full rank/Fitting atlas was not preserved")
    if jobs.get("prepass", {}).get("job_id") != \
            "coefficient_base_B_plus_I5A":
        fail("prepass job missing")

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    replay = output / "compiled_w0_bridge_replay.sing"
    q1 = qlist[0]["singular"]
    q3 = qlist[2]["singular"]
    q4 = qlist[3]["singular"]
    w = polys["W"]["singular"]
    all_q = [item["singular"] for item in qlist]
    a1 = map_leading(A_PATHS[1].read_text().strip())
    a3 = map_leading(A_PATHS[3].read_text().strip())
    a4 = map_leading(A_PATHS[4].read_text().strip())
    replay.write_text("\n".join([
        "ring R=0,(d0_1,d1_1,d2_1,d3_1,d4_1,d5_1),dp;",
        f"poly G2row1=({q1}); poly G2row3=({q3}); poly G2row4=({q4});",
        f"poly W=({w}); poly A1=({a1}); poly A3=({a3}); poly A4=({a4});",
        'if (A1*G2row1+A3*G2row3+A4*G2row4-W!=0) { print("K00_V26R1_RELEASE_FAIL=COMPILED_W_IDENTITY"); quit; }',
        'if (A3*G2row3+A4*G2row4-W==0) { print("K00_V26R1_RELEASE_FAIL=DROP_MUTATION"); quit; }',
        'if ((A1+1)*G2row1+A3*G2row3+A4*G2row4-W==0) { print("K00_V26R1_RELEASE_FAIL=ADD_MUTATION"); quit; }',
        "ideal B=" + ",".join(f"({item})" for item in all_q) + ",(" +
        polys["F10"]["singular"] + ");",
        "ideal GB=slimgb(B);",
        'if (reduce(W,GB)!=0) { print("K00_V26R1_RELEASE_FAIL=B_NORMAL_FORM"); quit; }',
        'print("K00_V26R1_W0_BRIDGE_REPLAY=1"); quit;',
    ]) + "\n")
    singular = shutil.which("Singular")
    if singular is None:
        fail("Singular missing")
    replay_outputs: list[Path] = []
    for index in (1, 2):
        stdout = output / f"compiled_w0_bridge_replay_{index}.stdout"
        stderr = output / f"compiled_w0_bridge_replay_{index}.stderr"
        run_replay(singular, replay, stdout, stderr)
        replay_outputs.extend([stdout, stderr])
    if replay_outputs[0].read_bytes() != replay_outputs[2].read_bytes():
        fail("two-process bridge marker bytes differ")

    release = {
        "released": True,
        "release_kind": "BOUNDED_COMPUTE_ONLY_UNDER_ROLLBACK_TAG",
        "dependency": "V24R6R1_INTERNAL_SOL_AUDIT_PASS_OPUS5_CROSS_AUDIT_PENDING",
        "dependency_internal_review_sha256": digest(REVIEW),
        "dependency_review_sha256": digest(REVIEW),
        "dependency_adjudication_sha256": digest(ADJUDICATION),
        "dependency_bundle_sha256": digest(REVIEWED_BUNDLE),
        "rollback_tag": "PROVISIONAL_ROLLBACK_TAG_OPUS5_PENDING",
        "external_cross_audit": "OPUS5_PENDING",
        "promotion": "FORBIDDEN_UNTIL_OPUS5_CROSS_AUDIT_PASS_AND_ADJUDICATION",
        "compiled_result_sha256": digest(result_path),
        "compiled_source_manifest_sha256": digest(
            compiled / "COMPILED_SOURCE.sha256"),
        "compiled_source_entries": source_hashes,
        "grade2_nonzero_literal_rows": [1, 2, 3, 4, 5, 7],
        "W_zero_redundant_mod_B_and_P6_by_explicit_syzygy": True,
        "full_rank_strata_preserved": list(range(6)),
        "permission": "rollback-tagged V26R1 exact prepass may run; atlas charts remain independently capped",
        "scope": "RELEASE_AND_W0_STRUCTURAL_BRIDGE_ONLY_NO_STRATUM_DECISION",
        "firewall": "NO_GRADE7_ATLAS_VERDICT_NO_LATER_GRADE_NO_JET_NO_ARC_NO_CLOSURE_NO_JC2",
    }
    release_path = output / "RELEASE_V26R1_W0.json"
    release_path.write_text(canonical_json(release))
    artifacts = [replay, *replay_outputs, release_path]
    freeze = output / "RELEASE_FREEZE_V26R1.sha256"
    freeze.write_text("".join(
        f"{digest(path)}  {path.name}\n" for path in artifacts))
    payload = {
        "status": "PASS_V26R1_W0_DESCENDANT_COMPILED_PROVISIONAL_ROLLBACK_TAG",
        "registered_aws_lane": lane,
        "rollback_tag": release["rollback_tag"],
        "external_cross_audit": release["external_cross_audit"],
        "promotion": release["promotion"],
        "release_sha256": digest(release_path),
        "release_freeze_sha256": digest(freeze),
        "two_process_compiled_W_syzygy_and_B_normal_form_replay": True,
        "rank_strata_preserved": list(range(6)),
        "artifacts": {path.name: {"sha256": digest(path),
                                    "bytes": path.stat().st_size}
                      for path in [*artifacts, freeze]},
        "scope": release["scope"],
        "firewall": release["firewall"],
    }
    (output / "RESULT.json").write_text(canonical_json(payload))
    print("K00_V26R1_RELEASE=" + payload["status"])
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
