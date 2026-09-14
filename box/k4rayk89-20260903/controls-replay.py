#!/usr/bin/env python3
"""Single-core replay of the charged k=4-ray controls.

The mathematical driver is the frozen charged input.  This wrapper changes
only its output root and its row-count runner so all generated evidence stays
under ``box/k4rayk89-20260903/controls-*`` and every Singular call carries
explicit one-core flags.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import time
from typing import Any


ROOT = Path("/home/ubuntu/jc2")
FROZEN = Path("/tmp/jc2-lane.HDMqeS/inputs")
OUT = ROOT / "box" / "k4rayk89-20260903" / "controls-artifacts"
RUNS = OUT / "runs"

THREAD_ENV = {
    "OMP_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1",
    "FLINT_NUM_THREADS": "1",
}
os.environ.update(THREAD_ENV)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def load_frozen_driver() -> Any:
    driver_path = FROZEN / "pinned_chart.py"
    spec = importlib.util.spec_from_file_location("frozen_pinned_chart", driver_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {driver_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


pinned = load_frozen_driver()
pinned.HERE = OUT
pinned.RUNS = RUNS

from box.lib.guided_gb import RunConfig, run_singular_script  # noqa: E402


def single_core_count(prelude: str, tag: str, timeout: int) -> dict[str, Any]:
    """Drop-in row-count runner with process-group timeout and one CPU."""

    RUNS.mkdir(parents=True, exist_ok=True)
    cache = RUNS / f"{tag}.rowcount.json"
    script = RUNS / f"{tag}.count.sing"
    pinned.atomic_write(
        script,
        prelude + '\nprint("PRE__ROWS_FINAL "+string(size(ROWS)));\nquit;\n',
    )
    cfg = RunConfig(
        output_dir=RUNS,
        timeout_seconds=timeout,
        total_cores=1,
        max_parallel_jobs=1,
        run_perturbed_control=False,
    )
    started = time.monotonic()
    command, stdout, stderr, returncode, timed_out, elapsed = run_singular_script(
        script,
        RUNS / f"{tag}.count.run",
        cfg,
        1,
    )
    markers: dict[str, str] = {}
    for line in stdout.splitlines():
        if line.startswith("PRE__"):
            pieces = line.split(maxsplit=1)
            markers[pieces[0]] = pieces[1] if len(pieces) > 1 else ""
    info = {
        "tag": tag,
        "wall": round(time.monotonic() - started, 6),
        "singular_elapsed_seconds": round(elapsed, 6),
        "timed_out": timed_out,
        "returncode": returncode,
        "n": int(markers["PRE__ROWS_FINAL"])
        if "PRE__ROWS_FINAL" in markers
        else None,
        "markers": markers,
        "command": command,
        "script": str(script),
        "script_sha256": sha256(script),
        "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
        "stderr_sha256": hashlib.sha256(stderr.encode()).hexdigest(),
    }
    pinned.atomic_write(cache, json.dumps(info, indent=2, sort_keys=True) + "\n")
    return info


pinned.run_singular_count = single_core_count


def guided_record(tag: str, label: str) -> dict[str, Any]:
    path = RUNS / tag / f"{label}.guided.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    return {
        "certificate": str(path.relative_to(ROOT)),
        "command": payload["command"],
        "returncode": payload["returncode"],
        "timed_out": payload["timed_out"],
        "elapsed_seconds": payload["elapsed_seconds"],
        "script_sha256": payload["script_sha256"],
        "stdout_sha256": payload["stdout_sha256"],
        "stderr_sha256": payload["stderr_sha256"],
        "main": payload["main"],
        "perturbed": payload["perturbed"],
    }


def assert_controls(results: dict[str, dict[str, Any]]) -> None:
    k7 = results["k7"]
    assert k7["verdict"] == "UNIT_IDEAL_CHAR0"
    assert k7["accepted_run_count"] == 1
    assert k7["runs"][0]["unit"] is True
    assert k7["runs"][0]["nf_all_zero"] is True

    for key in ("k4", "k5"):
        row = results[key]
        assert row["verdict"] == "UNIT_IDEAL_CHAR0"
        assert row["accepted_run_count"] == 1
        assert row["runs"][0]["unit"] is True
        assert row["runs"][0]["nf_all_zero"] is True

    tame = results["tame"]
    assert tame["verdict"] == "DIM0_CHAR0"
    assert tame["runs"][0]["dimension"] == 0
    assert tame["runs"][0]["vdim"] == 2
    assert tame["runs"][0]["unit"] is False
    assert tame["counts"]["markers"]["PRE__CTRL_J"] == "6*x*mu^2"

    hint = results["hint"]
    assert hint["verdict"] == "DIM0_CHAR0"
    assert hint["predicted_length"] == 3640
    assert hint["main_lead_vdim"] == 3640
    assert hint["perturbed_lead_vdim"] == 3640
    assert hint["main_accepted"] is True
    assert hint["perturbed_accepted"] is False


def main() -> None:
    started = time.monotonic()
    OUT.mkdir(parents=True, exist_ok=True)

    frozen_driver = FROZEN / "pinned_chart.py"
    frozen_guided = FROZEN / "guided_gb.py"
    live_driver = ROOT / "box" / "k4raypinned-20260903" / "pinned_chart.py"
    live_guided = ROOT / "box" / "lib" / "guided_gb.py"
    if sha256(frozen_driver) != sha256(live_driver):
        raise RuntimeError("frozen/live pinned_chart.py mismatch")
    if sha256(frozen_guided) != sha256(live_guided):
        raise RuntimeError("frozen/live guided_gb.py mismatch")

    results: dict[str, dict[str, Any]] = {}
    results["k7"] = pinned.run_chart(
        "CTRL_REPLAY_K7_PIN_LIGHT",
        7,
        b=5,
        s=4,
        timeout=120,
        count_timeout=60,
        cores=1,
        theorem_cut=False,
        rho_level4=True,
    )
    results["k4"] = pinned.run_chart(
        "CTRL_REPLAY_K4_B3",
        4,
        b=3,
        s=2,
        timeout=60,
        count_timeout=60,
        cores=1,
        theorem_cut=True,
        rho_level4=True,
    )
    results["k5"] = pinned.run_chart(
        "CTRL_REPLAY_K5_B4",
        5,
        b=4,
        s=3,
        timeout=60,
        count_timeout=60,
        cores=1,
        theorem_cut=True,
        rho_level4=True,
    )
    results["tame"] = pinned.positive_control(timeout=60, cores=1)
    results["hint"] = pinned.perturbed_hint_control(timeout=120, cores=1)
    assert_controls(results)

    guided = {
        "k7": guided_record(
            "CTRL_REPLAY_K7_PIN_LIGHT", "CTRL_REPLAY_K7_PIN_LIGHT_p0_Q"
        ),
        "k4": guided_record("CTRL_REPLAY_K4_B3", "CTRL_REPLAY_K4_B3_p0_Q"),
        "k5": guided_record("CTRL_REPLAY_K5_B4", "CTRL_REPLAY_K5_B4_p0_Q"),
        "tame": guided_record("CTRL_TAME_K1", "CTRL_TAME_K1_p0_Q"),
        "hint": guided_record(
            "CTRL_HINT_K4_B3", "CTRL_HINT_K4_B3_p1009_p1009"
        ),
    }
    rowcounts = {
        key: results[key]["counts"][0]
        for key in ("k7", "k4", "k5")
    }
    rowcounts["tame"] = results["tame"]["counts"]

    evidence = {
        "schema": "jc2.k4ray.controls-replay/v1",
        "status": "PASS",
        "outer_command": [
            "env",
            *[f"{key}=1" for key in THREAD_ENV],
            "timeout",
            "300s",
            "python3",
            "box/k4rayk89-20260903/controls-replay.py",
        ],
        "wall_seconds": round(time.monotonic() - started, 6),
        "thread_environment": THREAD_ENV,
        "singular_version": subprocess.run(
            ["Singular", "--version"],
            capture_output=True,
            text=True,
            timeout=10,
            check=False,
        ).stdout.splitlines()[0],
        "source_hashes": {
            str(frozen_driver): sha256(frozen_driver),
            str(frozen_guided): sha256(frozen_guided),
            str(ROOT / "box/lib/staged_band_emitter.py"): sha256(
                ROOT / "box/lib/staged_band_emitter.py"
            ),
            "box/k16stdhilb-20260903/t5_p1009_b0_tail_guided.sing": sha256(
                ROOT / "box/k16stdhilb-20260903/t5_p1009_b0_tail_guided.sing"
            ),
            "box/k4rayk89-20260903/controls-replay.py": sha256(Path(__file__)),
        },
        "chains": {
            key: {
                "formation": rowcounts.get(key),
                "guided_gb": guided[key],
                "summary": results[key],
            }
            for key in ("k7", "k4", "k5", "tame", "hint")
        },
        "assertions": {
            "k7_exact_q_unit": True,
            "charged_k4_exact_q_unit": True,
            "charged_k5_exact_q_unit": True,
            "tame_survives_as_dim0_length2_nonunit": True,
            "guided_main_accepts_and_perturbed_control_fails": True,
        },
    }
    atomic_write(
        OUT / "controls-summary.json",
        json.dumps(evidence, indent=2, sort_keys=True) + "\n",
    )
    manifest_path = OUT / "artifacts.sha256"
    artifact_lines = []
    for path in sorted(OUT.rglob("*")):
        if path.is_file() and path != manifest_path and not path.name.endswith(".tmp"):
            artifact_lines.append(f"{sha256(path)}  {path.relative_to(ROOT)}")
    atomic_write(manifest_path, "\n".join(artifact_lines) + "\n")
    print(json.dumps({"status": "PASS", "wall_seconds": evidence["wall_seconds"]}))


if __name__ == "__main__":
    main()
