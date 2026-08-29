#!/usr/bin/env python3
"""Fail-closed validator for exact cutoff-three chart custody."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


HEX64 = re.compile(r"^[0-9a-f]{64}$")
HOST_ASSIGNMENT = {
    "i-02cb2b4a379ffcc64": ("r6a", [0, 1]),
    "i-040b7a1c2ed72d4cc": ("r6c", [2, 3]),
    "i-07eeaf8ba6f0bc419": ("r6d", [4, 5]),
}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def metadata(path):
    out = {}
    for line in path.read_text().splitlines():
        key, value = line.split("=", 1)
        assert key not in out
        out[key] = value
    return out


def verify_manifest(run_dir):
    manifest = run_dir / "RUN_EVIDENCE.sha256"
    assert manifest.is_file()
    covered = set()
    for line in manifest.read_text().splitlines():
        digest, relative = line.split("  ", 1)
        assert HEX64.fullmatch(digest)
        assert relative.startswith("./")
        path = (run_dir / relative[2:]).resolve()
        assert path.parent == run_dir.resolve()
        assert path.name != manifest.name
        assert path.is_file()
        assert sha256(path) == digest, path
        covered.add(path.name)
    actual = {path.name for path in run_dir.iterdir()
              if path.is_file() and path.name != manifest.name}
    assert covered == actual, (sorted(actual - covered), sorted(covered - actual))
    return sha256(manifest)


def parse_charts(text):
    assert re.fullmatch(r"[0-5](,[0-5])*", text)
    charts = [int(value) for value in text.split(",")]
    assert len(charts) == len(set(charts))
    return charts


def verify_single(run_dir, expected_charts=None, allow_precompletion=False):
    run_dir = run_dir.resolve()
    assert run_dir.is_dir() and run_dir.name.startswith("tail3_")
    meta = metadata(run_dir / "METADATA.txt")
    assert meta["MODE"] == "exact"
    assert meta["SCOPE"] in ("core", "full")
    charts = parse_charts(meta["SELECTED_CHARTS"])
    assert meta["COVERAGE_STATUS"] == "PARTIAL_NONPROMOTABLE_ALONE"
    assert meta["TOTAL_JOBS"] == str(len(charts))
    assert meta["INSTANCE_ID"] in HOST_ASSIGNMENT
    host_alias, assigned_charts = HOST_ASSIGNMENT[meta["INSTANCE_ID"]]
    assert meta["HOST_ALIAS"] == host_alias
    assert charts == assigned_charts, (meta["INSTANCE_ID"], charts)
    if expected_charts is not None:
        assert charts == expected_charts, (charts, expected_charts)
    for key in ("SOURCE_MANIFEST_SHA256", "EVIDENCE_MANIFEST_SHA256",
                "TARGET_JSON_SHA256"):
        assert HEX64.fullmatch(meta[key])
    if allow_precompletion:
        assert (run_dir / "WORKERS_COMPLETED").is_file()
    else:
        assert (run_dir / "RUN_COMPLETED").is_file()
        assert not (run_dir / "RUN_INCOMPLETE_OR_FAILED").exists()

    rc_charts = sorted(int(match.group(1)) for path in run_dir.glob("chart*.rc")
                       if (match := re.fullmatch(r"chart([0-5])\.rc", path.name)))
    assert rc_charts == sorted(charts), (rc_charts, charts)
    jobs = []
    for chart in charts:
        label = f"chart{chart}"
        job = run_dir / f"{label}.sing"
        job_manifest = run_dir / f"{label}.sing.sha256"
        output_manifest = run_dir / f"{label}.output.sha256"
        log = run_dir / f"{label}.log"
        rc = run_dir / f"{label}.rc"
        assert all(path.is_file()
                   for path in (job, job_manifest, output_manifest, log, rc))
        assert rc.read_text().strip() == "0"
        digest, named_path = job_manifest.read_text().strip().split(None, 1)
        assert HEX64.fullmatch(digest) and sha256(job) == digest
        assert named_path == job.name
        log_digest, log_name = output_manifest.read_text().strip().split(None, 1)
        assert HEX64.fullmatch(log_digest) and log_name == log.name
        assert sha256(log) == log_digest
        required = [f"CHART={chart}", "FIELD=q", "UNIT=1",
                    "CERTIFICATE_CHECK=PASS",
                    "Maximum resident set size (kbytes):",
                    "Elapsed (wall clock) time", "Exit status: 0"]
        seen = {marker: False for marker in required}
        failed = False
        with log.open("r", errors="strict") as stream:
            for line in stream:
                for marker in required:
                    if marker in line:
                        seen[marker] = True
                if "CERTIFICATE_CHECK=FAIL" in line:
                    failed = True
        assert all(seen.values()), (chart, seen)
        assert not failed
        jobs.append({"chart": chart, "job_sha256": digest,
                     "log_sha256": log_digest})
    evidence_sha = verify_manifest(run_dir)
    return {
        "run_dir": str(run_dir),
        "scope": meta["SCOPE"],
        "charts": charts,
        "coverage_status": meta["COVERAGE_STATUS"],
        "host_alias": meta["HOST_ALIAS"],
        "instance_id": meta["INSTANCE_ID"],
        "source_manifest_sha256": meta["SOURCE_MANIFEST_SHA256"],
        "evidence_manifest_sha256": meta["EVIDENCE_MANIFEST_SHA256"],
        "target_json_sha256": meta["TARGET_JSON_SHA256"],
        "run_evidence_sha256": evidence_sha,
        "jobs": jobs,
    }


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    one = subparsers.add_parser("run")
    one.add_argument("run_dir", type=Path)
    one.add_argument("--expected-charts", required=True)
    one.add_argument("--allow-precompletion", action="store_true")
    combined = subparsers.add_parser("combine")
    combined.add_argument("run_dirs", nargs="+", type=Path)
    args = parser.parse_args()

    if args.command == "run":
        expected = parse_charts(args.expected_charts)
        result = verify_single(args.run_dir, expected, args.allow_precompletion)
        result["status"] = "PASS"
        print(json.dumps(result, sort_keys=True, indent=2))
        return

    results = [verify_single(path) for path in args.run_dirs]
    assert len(results) == 3
    common_keys = ("scope", "source_manifest_sha256",
                   "evidence_manifest_sha256", "target_json_sha256")
    for key in common_keys:
        assert len({result[key] for result in results}) == 1, key
    charts = [chart for result in results for chart in result["charts"]]
    assert {result["instance_id"] for result in results} == set(HOST_ASSIGNMENT)
    assert len(charts) == len(set(charts)), charts
    assert sorted(charts) == list(range(6)), charts
    print(json.dumps({
        "status": "PASS",
        "coverage": "DISJOINT_COMPLETE_UNION_0_THROUGH_5",
        "scope": results[0]["scope"],
        "charts": sorted(charts),
        "runs": results,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
