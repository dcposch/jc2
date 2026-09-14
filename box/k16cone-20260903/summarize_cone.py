#!/usr/bin/env python3
"""Summarize emitted CONE Singular jobs."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re


HERE = pathlib.Path(__file__).resolve().parent


def next_value(lines: list[str], label: str) -> str | None:
    for index, line in enumerate(lines):
        if line.strip() == label and index + 1 < len(lines):
            return lines[index + 1].strip()
    return None


def parse_out(path: pathlib.Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    lines = text.splitlines()
    answer: dict[str, object] = {
        "out": str(path),
        "out_exists": path.exists(),
        "out_sha256": hashlib.sha256(text.encode()).hexdigest() if path.exists() else None,
        "job_done": "CONE_JOB_DONE" in lines,
        "verdict_lines": [line for line in lines if line.startswith("CONE_VERDICT")],
    }
    for label, key in [
        ("T=", "t"),
        ("MODE=", "mode"),
        ("PRIME=", "prime"),
        ("BRANCH=", "branch"),
    ]:
        for line in lines:
            if line.startswith(label):
                answer[key] = line.split("=", 1)[1]
                break
    for label, key in [
        ("CONE_BASIS_SIZE", "basis_size"),
        ("CONE_DIM", "dim"),
        ("RAB_BASIS_SIZE", "rab_basis_size"),
        ("TAU_IN_RADICAL", "tau_in_radical"),
        ("STD_TIMER", "std_timer"),
    ]:
        value = next_value(lines, label)
        if value is not None:
            answer[key] = value
    if "CONE_VERDICT_NOT_REFUTATION_CANDIDATE" in lines:
        answer["refutation_candidate"] = True
    elif "CONE_VERDICT_DIM0" in lines or "CONE_VERDICT_TAU_CRITERION" in lines:
        answer["refutation_candidate"] = False
    err = path.with_suffix(".err")
    err_text = err.read_text(encoding="utf-8", errors="replace") if err.exists() else ""
    answer["err"] = str(err)
    answer["err_exists"] = err.exists()
    answer["err_sha256"] = hashlib.sha256(err_text.encode()).hexdigest() if err.exists() else None
    answer["err_nonempty"] = bool(err_text.strip())
    answer["error_markers"] = bool(re.search(r"\\? error occurred|halt [1-9]", text + "\n" + err_text))
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("stems", nargs="*")
    args = parser.parse_args()
    stems = args.stems
    if not stems:
        stems = sorted(path.stem for path in HERE.glob("cone_*.out"))
    summary = [parse_out(HERE / f"{stem}.out") for stem in stems]
    path = HERE / "status_summary.json"
    path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"summary": str(path), "jobs": len(summary)}, sort_keys=True))


if __name__ == "__main__":
    main()
