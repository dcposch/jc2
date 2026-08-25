#!/usr/bin/env python3
"""Fail-closed aggregate for the frozen localized w=0 fibre matrix.

This parser is intentionally independent of the source generator.  It consumes
only harvested immutable AWS run directories and checks the complete expected
matrix, source pins, endpoint markers, and the numerical invariants used in the
classification report.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re


GENERATOR_SHA256 = "90b13704a850a70593a2c2d057637f1e2b4180534c5832890ce6814bfe03925a"
RUNNER_SHA256 = "4717772835703a9eef8cc17a47f0d28e2ab8bebc704a143948ffb231bca489d1"
PREREG_SHA256 = "3fe8e56af3e20d4661d7ba7c4c00d83353a5f6fcbf195587f2a1668c2cd84754"
PREREG_MANIFEST_SHA256 = "a46bd2e229bf8f8056f57ddebe8146deba684bd41aa63baa7126c1eea633bf81"
COMPILER_SHA256 = "22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545"
PARENT_MANIFEST_SHA256 = "3d60b5675ac623ce66f3b718ca79161de7f24d6d05f82cf910fe060680c93ac4"


FINITE = {"base", "loaded", "q8", "q8_smooth"}
EMPTY = {
    "nu0",
    "q8_singular",
    "nonq8",
    "nonq8_smooth",
    "nonq8_singular",
    "nonq8_rho0",
    "nonq8_rho_loaded",
}


def expected() -> dict[str, dict[str, object]]:
    rows: dict[str, dict[str, object]] = {}
    for mode in ("base", "nu0", "loaded", "q8", "q8_smooth", "q8_singular", "nonq8"):
        rows[f"q8_w0_{mode}_Q_std_block_box02_v1"] = {
            "root": "aws_box02_v1", "prime": "0", "mode": mode,
            "engine": "std", "order": "block", "host": "ip-172-30-0-186",
        }
    for mode in (
        "base", "nu0", "loaded", "q8", "q8_smooth", "q8_singular", "nonq8",
        "nonq8_smooth", "nonq8_singular", "nonq8_rho0", "nonq8_rho_loaded",
    ):
        rows[f"q8_w0_{mode}_p127_std_block_box02_v1"] = {
            "root": "aws_box02_v1", "prime": "127", "mode": mode,
            "engine": "std", "order": "block", "host": "ip-172-30-0-186",
        }
    for mode in ("base", "nu0", "loaded", "q8_smooth", "q8_singular", "nonq8"):
        rows[f"q8_w0_{mode}_Q_slimgb_dp_box03_v1"] = {
            "root": "aws_box03_v1", "prime": "0", "mode": mode,
            "engine": "slimgb", "order": "dp", "host": "ip-172-30-0-249",
        }
    for mode in (
        "base", "nu0", "loaded", "q8_smooth", "q8_singular", "nonq8",
        "nonq8_smooth", "nonq8_singular", "nonq8_rho0", "nonq8_rho_loaded",
    ):
        rows[f"q8_w0_{mode}_p32003_slimgb_block_box03_v1"] = {
            "root": "aws_box03_v1", "prime": "32003", "mode": mode,
            "engine": "slimgb", "order": "block", "host": "ip-172-30-0-249",
        }
    assert len(rows) == 34
    return rows


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def field(text: str, name: str) -> str:
    matches = re.findall(rf"(?m)^{re.escape(name)}=(.*)$", text)
    if len(matches) != 1:
        raise AssertionError((name, matches))
    return matches[0].strip()


def audit_run(case: Path, tag: str, spec: dict[str, object]) -> dict[str, object]:
    directory = case / str(spec["root"]) / tag
    required = ("input.sing", "run.meta", "singular.stdout", "singular.stderr")
    for name in required:
        assert (directory / name).is_file(), (tag, name)
    meta = (directory / "run.meta").read_text()
    stdout = (directory / "singular.stdout").read_text()
    stderr = (directory / "singular.stderr").read_text()

    assert field(meta, "tag") == tag
    assert field(meta, "host") == spec["host"]
    assert field(meta, "prime") == spec["prime"]
    assert field(meta, "mode") == spec["mode"]
    assert field(meta, "engine") == spec["engine"]
    assert field(meta, "order") == spec["order"]
    assert field(meta, "rc") == "0"
    for digest in (
        GENERATOR_SHA256, RUNNER_SHA256, PREREG_SHA256, PREREG_MANIFEST_SHA256,
        COMPILER_SHA256, PARENT_MANIFEST_SHA256, sha256(directory / "input.sing"),
        sha256(directory / "singular.stdout"), sha256(directory / "singular.stderr"),
    ):
        assert digest in meta, (tag, digest)

    assert stdout.count("Q8_W0_FIBRE_STRATUM_PASS") == 1
    assert field(stdout, "prime") == spec["prime"]
    assert field(stdout, "mode") == spec["mode"]
    assert field(stdout, "engine") == spec["engine"]
    assert field(stdout, "order") == spec["order"]
    assert field(stdout, "original_remainder_zero") == "1"
    lowered = stdout.lower() + "\n" + stderr.lower()
    for token in ("not defined", "error occurred", "segmentation fault", "killed", "timed out"):
        assert token not in lowered, (tag, token)
    assert "Exit status: 0" in stderr

    mode = str(spec["mode"])
    if mode in FINITE:
        assert field(stdout, "dim") == "0"
        assert field(stdout, "vdim") == "8"
        assert field(stdout, "v_elimination_size") == "1"
        assert field(stdout, "v_eliminant_degree") == "8"
        assert field(stdout, "v_eliminant_squarefree_gcd_degree") == "0"
        assert field(stdout, "v_eliminant_q8_gcd_degree") == "8"
        state = "reduced_length_8_q8"
    elif mode in EMPTY:
        assert field(stdout, "dim") == "-1"
        assert field(stdout, "size") == "1"
        assert field(stdout, "vdim") == "0"
        state = "unit_ideal"
    else:
        raise AssertionError(mode)

    return {
        "tag": tag,
        "host": spec["host"],
        "prime": int(str(spec["prime"])),
        "mode": mode,
        "engine": spec["engine"],
        "order": spec["order"],
        "state": state,
        "input_sha256": sha256(directory / "input.sing"),
        "stdout_sha256": sha256(directory / "singular.stdout"),
        "stderr_sha256": sha256(directory / "singular.stderr"),
        "run_meta_sha256": sha256(directory / "run.meta"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    case = args.case.resolve()
    matrix = [audit_run(case, tag, spec) for tag, spec in sorted(expected().items())]
    summary = {
        "status": "PASS",
        "runs": len(matrix),
        "box02_runs": sum(row["host"] == "ip-172-30-0-186" for row in matrix),
        "box03_runs": sum(row["host"] == "ip-172-30-0-249" for row in matrix),
        "finite_runs": sum(row["state"] == "reduced_length_8_q8" for row in matrix),
        "empty_runs": sum(row["state"] == "unit_ideal" for row in matrix),
        "matrix": matrix,
    }
    assert summary == {**summary, "runs": 34, "box02_runs": 18, "box03_runs": 16,
                       "finite_runs": 14, "empty_runs": 20}
    args.json.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print("Q8_W0_AGGREGATE_PASS")
    print("runs=34")
    print("box02_runs=18")
    print("box03_runs=16")
    print("finite_runs=14")
    print("empty_runs=20")


if __name__ == "__main__":
    main()
