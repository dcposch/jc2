#!/usr/bin/env python3
"""Patched Hilbert-seed then exact-Q guided std under one 8,880 s budget."""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import re
import sys
import time
import traceback
from pathlib import Path

SCRATCH = Path(os.environ.get("JC2_SCRATCH", "/home/ubuntu/classA-smallest-20260906.xpXroy"))
OUT = SCRATCH / "results/a_guided"
HELPER = SCRATCH / "repo/box/lib/guided_gb.py"
EXPECTED_HELPER_SHA = "95d12f5b23975e8699b634b1ba8c6f0e6fc4e24abfcd4bad2db936e1c74e9826"
TOTAL_SECONDS = 8880


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def weights(names: list[str]) -> tuple[int, ...]:
    answer = []
    for name in names:
        if name == "c":
            b, d = 3, 44
        elif (hit := re.fullmatch(r"h_(\d+)_(\d+)", name)):
            b, a = map(int, hit.groups()); d = 9 - a
        elif (hit := re.fullmatch(r"[AB](\d+)_(\d+)_(\d+)", name)):
            i, b, a = map(int, hit.groups()); d = i * 9 - a
        else:
            raise AssertionError(name)
        answer.append(19 * b + d)
    assert all(value > 0 for value in answer)
    return tuple(answer)


def write_result(payload: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    temporary = OUT / ".job_result.json.tmp"
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(OUT / "job_result.json")
    print(json.dumps(payload, sort_keys=True), flush=True)


def main() -> int:
    began_utc = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    began = time.monotonic()
    OUT.mkdir(parents=True, exist_ok=True)
    if sha256(HELPER) != EXPECTED_HELPER_SHA:
        write_result({"status": "TYPED_INSTRUMENT_ERROR", "reason": "guided helper digest mismatch"})
        return 2
    spec = importlib.util.spec_from_file_location("r005_guided_gb", HELPER)
    gb = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = gb
    spec.loader.exec_module(gb)
    metadata = json.loads((SCRATCH / "repo/box/lambda-lowweight-20260906/R005.rows.json").read_text())
    names = [str(name) for name in metadata["variables"]]
    wts = weights(names)
    seed = gb.SingularSystem(
        name="R005_sat_seed", prelude=(SCRATCH / "data/R005_sat_p32003.prelude.sing").read_text(),
        generators=("S",), characteristic=32003, variables=tuple(names), homogeneous=True,
        positive_weights=wts, metadata={"role": "modular Hilbert seed only"})
    exact = gb.SingularSystem(
        name="R005_sat_exact", prelude=(SCRATCH / "data/R005_sat_Q.prelude.sing").read_text(),
        generators=("S",), characteristic=0, variables=tuple(names), homogeneous=True,
        positive_weights=wts, metadata={"role": "exact-Q target"})
    remaining = max(1, int(TOTAL_SECONDS - (time.monotonic() - began) - 20))
    seed_config = gb.RunConfig(
        output_dir=OUT, timeout_seconds=None, total_cores=8, run_perturbed_control=False,
        outer_watchdog_seconds=8940, hilbert_seed_timeout_seconds=remaining)
    hint, seed_run = gb.run_hilbert_seed(seed, seed_config, 8)
    seed_json = seed_run.to_json()
    if seed_run.timed_out:
        write_result({"status": "TYPED_TIMEOUT", "timeout_stage": "hilbert_seed",
                      "began_utc": began_utc, "elapsed_seconds": round(time.monotonic()-began, 3),
                      "helper_sha256": EXPECTED_HELPER_SHA, "seed_run": seed_json})
        return 0
    if hint is None:
        write_result({"status": "TYPED_INSTRUMENT_ERROR", "reason": "completed seed emitted no Hilbert numerator",
                      "began_utc": began_utc, "elapsed_seconds": round(time.monotonic()-began, 3),
                      "seed_run": seed_json})
        return 2
    remaining = max(1, int(TOTAL_SECONDS - (time.monotonic() - began) - 20))
    exact_config = gb.RunConfig(
        output_dir=OUT, timeout_seconds=None, total_cores=8, run_perturbed_control=False,
        outer_watchdog_seconds=8940, std_timeout_seconds=remaining)
    result = gb.guided_groebner(
        exact, hint=hint, policy=gb.PromotionPolicy.exact_q("R005 exact saturation target"),
        config=exact_config)
    write_result({"status": "COMPLETED_GUIDED_PIPELINE", "timeout_stage": result.certificate.get("timeout_stage"),
                  "verdict": result.verdict.value, "began_utc": began_utc,
                  "elapsed_seconds": round(time.monotonic()-began, 3),
                  "helper_sha256": EXPECTED_HELPER_SHA, "seed_run": seed_json,
                  "guided_result": result.to_json()})
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except BaseException as exc:
        write_result({"status": "TYPED_INSTRUMENT_ERROR", "reason": repr(exc),
                      "traceback": traceback.format_exc()})
        raise
