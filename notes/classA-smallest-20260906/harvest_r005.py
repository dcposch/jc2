#!/usr/bin/env python3
"""Summarize completed R005 fleet jobs without promoting modular evidence."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

S = Path("/home/ubuntu/classA-smallest-20260906.xpXroy")


def text(path):
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def sha(path):
    if not path.exists(): return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""): h.update(block)
    return h.hexdigest()


def time_data(path):
    value = text(path)
    def last(pattern, cast=str):
        hits = re.findall(pattern, value)
        return cast(hits[-1]) if hits else None
    return {"elapsed": last(r"Elapsed \(wall clock\) time \(h:mm:ss or m:ss\):\s*(\S+)"),
            "maximum_rss_kib": last(r"Maximum resident set size \(kbytes\):\s*(\d+)", int),
            "termination_signal": last(r"Command terminated by signal (\d+)", int),
            "exit_status_field": last(r"Exit status:\s*(\d+)", int)}


def wrapper(path, letter):
    value = text(path)
    start = re.findall(rf"JOB_{letter}_START (\S+)", value)
    end = re.findall(rf"JOB_{letter}_END (\S+) RC=(\d+)", value)
    cpeak = re.findall(rf"JOB_{letter}_CGROUP_MEMORY_PEAK_BYTES (\d+)", value)
    return {"start_utc": start[-1] if start else None,
            "end_utc": end[-1][0] if end else None,
            "returncode": int(end[-1][1]) if end else None,
            "cgroup_memory_peak_bytes": int(cpeak[-1]) if cpeak else None}


def f4(log):
    pattern = re.compile(r"^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+x\s+(\d+)\s+([0-9.]+)%\s+(\d+)\s+new\s+(\d+)\s+zero\s+([0-9.]+)\s+\|\s+([0-9.]+)", re.M)
    rounds = []
    for hit in pattern.finditer(log):
        d, sel, pairs, rows, cols, density, new, zero, real, cpu = hit.groups()
        rounds.append({"degree": int(d), "selected": int(sel), "pairs": int(pairs),
                       "matrix_rows": int(rows), "matrix_columns": int(cols),
                       "density_percent": float(density), "new": int(new), "zero": int(zero),
                       "real_seconds": float(real), "cpu_seconds": float(cpu),
                       "selected_balance_ok": int(new) + int(zero) == int(sel)})
    highest = max((r["degree"] for r in rounds), default=None)
    at_highest = [r for r in rounds if r["degree"] == highest]
    largest = max(rounds, key=lambda r: r["matrix_rows"] * r["matrix_columns"], default=None)
    return {"completed_round_count": len(rounds), "highest_completed_degree": highest,
            "last_completed_round_at_highest_degree": at_highest[-1] if at_highest else None,
            "largest_completed_matrix": largest,
            "all_selected_balances_ok": all(r["selected_balance_ok"] for r in rounds)}


def markers(log, prefix):
    return [line.strip() for line in log.splitlines() if prefix in line]


def singular_protocol(log):
    """Parse Singular's terse std protocol (this is not F4 telemetry)."""
    tail = log.split("R005__STD_BEGIN", 1)[-1]
    tail = tail.split("\nhalt 1", 1)[0]
    counters = [int(value) for value in re.findall(r"s\((\d+)\)", tail)]
    stripped = re.sub(r"\([^)]*\)|\[[^]]*\]", "", tail)
    degrees = [int(hit.group()) for hit in re.finditer(r"(?<!\d)([2-9][0-9])(?!\d)", stripped)]
    # A newly printed degree means the preceding protocol degree closed.
    return {"current_degree": degrees[-1] if degrees else None,
            "highest_closed_degree": degrees[-2] if len(degrees) > 1 else None,
            "degree_markers": degrees,
            "last_s_counter": counters[-1] if counters else None,
            "telemetry_kind": "Singular std protocol, not F4; no matrix dimensions emitted"}


def systemd(unit):
    keys = ("ActiveState", "SubState", "Result", "ExecMainStatus", "ExecMainPID",
            "ExecMainStartTimestamp", "ExecMainExitTimestamp", "MemoryCurrent",
            "MemoryPeak", "MemoryHigh", "MemoryMax", "MemorySwapMax", "CPUUsageNSec")
    command = ["systemctl", "show", unit]
    for key in keys:
        command += ["-p", key]
    raw = subprocess.run(command, check=False, capture_output=True, text=True).stdout
    return dict(line.split("=", 1) for line in raw.splitlines() if "=" in line)


def main():
    dirs = {"a": S/"results/a_guided", "b": S/"results/b_msolve", "c": S/"results/c_singular"}
    watch = S/"results/resource_watch_latest.json"
    out = {"input_manifest": json.loads((S/"results/input_manifest.json").read_text()),
           "resource_watch": json.loads(watch.read_text()) if watch.exists() else None,
           "systemd_final": {
               "a": systemd("jc2-classa-a-guided"),
               "b": systemd("jc2-classa-b-msolve"),
               "c": systemd("jc2-classa-c-singular"),
           },
           "job_scripts": {}, "jobs": {}}
    for letter in "abc":
        script = S/f"jobs/job_{letter}.sh"
        out["job_scripts"][letter] = {"path": str(script), "bytes": script.stat().st_size,
                                              "sha256": sha(script), "text": text(script)}
    for letter, directory in dirs.items():
        stdout = text(directory/"service.stdout"); stderr = text(directory/"service.stderr")
        job = {"wrapper": wrapper(directory/"service.stdout", letter.upper()),
               "gnu_time": time_data(directory/"time.txt"),
               "process_tree_rss": json.loads((directory/"rss.json").read_text()) if (directory/"rss.json").exists() else None,
               "service_stdout": {"bytes": (directory/"service.stdout").stat().st_size,
                                  "sha256": sha(directory/"service.stdout")},
               "service_stderr": {"bytes": (directory/"service.stderr").stat().st_size,
                                  "sha256": sha(directory/"service.stderr")}}
        if letter == "a":
            p = directory/"job_result.json"
            job["typed_result"] = json.loads(p.read_text()) if p.exists() else None
            extra = "\n".join(text(p) for p in directory.glob("*.out"))
            job["stage_markers"] = markers(extra, "GG__")
        elif letter == "b":
            job["f4"] = f4(stdout + "\n" + stderr)
            basis = directory/"basis.out"; btext = text(basis)
            length = re.findall(r"#length of basis:\s*(\d+)\s+element", btext)
            job["basis"] = {"bytes": basis.stat().st_size if basis.exists() else None,
                            "sha256": sha(basis), "basis_size": int(length[-1]) if length else None,
                            "unit": bool(re.search(r"^\[1\]:\s*$", btext, re.M)) if btext else None}
        else:
            job["markers"] = markers(stdout, "R005__")
            job["protocol"] = singular_protocol(stdout)
            size = re.findall(r"R005__BASIS_SIZE (\d+)", stdout)
            unit = re.findall(r"R005__UNIT (\d+)", stdout)
            job["basis_size"] = int(size[-1]) if size else None
            job["unit"] = bool(int(unit[-1])) if unit else None
        out["jobs"][letter] = job
    target = S/"results/harvest.json"
    target.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    watch_units = (out.get("resource_watch") or {}).get("units", {})
    summary = {
        "target": {
            "row_id": out["input_manifest"]["row_id"],
            "class_id": out["input_manifest"]["class_id"],
            "receiver_key": out["input_manifest"]["receiver_key"],
            "unknowns_without_T": out["input_manifest"]["unknowns_without_T"],
            "coefficient_generators": out["input_manifest"]["coefficient_generators"],
            "full_generators": out["input_manifest"]["full_generators"],
            "coefficient_coordinate_sha256": out["input_manifest"]["coefficient_coordinate_sha256"],
        },
        "input_files": out["input_manifest"]["files"],
        "input_controls": {
            "status": out["input_manifest"]["status"],
            "total_terms": out["input_manifest"]["total_terms"],
            "all_rows_bihomogeneous": out["input_manifest"]["all_rows_bihomogeneous"],
            "weights_positive": out["input_manifest"]["weights_positive"],
            "scalar_weight_rule": out["input_manifest"]["scalar_weight_rule"],
            "weight_min": out["input_manifest"]["weight_min"],
            "weight_max": out["input_manifest"]["weight_max"],
            "scratch_data_bytes": out["input_manifest"]["scratch_data_bytes"],
        },
        "memory_policy": {
            "initial_utc": "2026-09-06T04:56:17Z",
            "initial": {"a_high_gib": 95, "a_max_gib": 105,
                        "c_high_gib": 110, "c_max_gib": 120},
            "soft_high_raise_utc": "2026-09-06T05:52:04Z",
            "final": {"a_high_bytes": 107374182400, "a_max_bytes": 112742891520,
                      "c_high_bytes": 123480309760, "c_max_bytes": 128849018880,
                      "combined_high_gib": 215, "combined_max_gib": 225,
                      "swap_max_bytes": 0, "oom_policy": "stop"},
            "raise_reason": "prolonged severe memory.high reclaim throttling; hard maxima unchanged",
        },
        "jobs": {
            "a": {
                "disposition": "TYPED_TIMEOUT_OUTER_DURING_HILBERT_SEED",
                "detail": "no completed Hilbert seed contract/job_result; exact-Q stage never started",
                "wrapper": out["jobs"]["a"]["wrapper"],
                "gnu_time": out["jobs"]["a"]["gnu_time"],
                "process_tree_rss": out["jobs"]["a"]["process_tree_rss"],
                "memory_events": watch_units.get("jc2-classa-a-guided", {}).get("last_readable_memory_events"),
                "basis_size": None, "unit": None, "stage_markers": out["jobs"]["a"]["stage_markers"],
            },
            "b": {
                "disposition": "FAILED_SIGSEGV_BEFORE_F4",
                "wrapper": out["jobs"]["b"]["wrapper"],
                "gnu_time": out["jobs"]["b"]["gnu_time"],
                "process_tree_rss": out["jobs"]["b"]["process_tree_rss"],
                "basis": out["jobs"]["b"]["basis"], "f4": out["jobs"]["b"]["f4"],
                "binary_sha256": "0436525b06fe83b1a6a00097a96d9bcafdc40d8de6315c724b9ada9a4c04ff5f",
                "elf_build_id": "b34bb9af2af3190438cf1b216f050f92f7847ffc",
                "version": "msolve 0.10.1",
                "avx512_evidence": "digest match to the named official Intel AVX-512 artifact; banner does not print ISA",
            },
            "c": {
                "disposition": "TYPED_TIMEOUT_EXACT_Q_STD",
                "wrapper": out["jobs"]["c"]["wrapper"],
                "gnu_time": out["jobs"]["c"]["gnu_time"],
                "process_tree_rss": out["jobs"]["c"]["process_tree_rss"],
                "memory_events": watch_units.get("jc2-classa-c-singular", {}).get("last_readable_memory_events"),
                "markers": out["jobs"]["c"]["markers"], "protocol": out["jobs"]["c"]["protocol"],
                "basis_size": out["jobs"]["c"]["basis_size"], "unit": out["jobs"]["c"]["unit"],
            },
        },
        "f4_degree_wall": {
            "highest_completed_degree": None, "matrix_rows": None, "matrix_columns": None,
            "reason": "msolve crashed before its first F4 step log; other two lanes emit Singular std, not F4 matrices",
        },
    }
    summary_path = S/"results/terminal_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    lines = [
        "R005 / C_n27m18_M20_ell2_s2 terminal summary",
        "a TYPED_TIMEOUT_OUTER_DURING_HILBERT_SEED rc=124 wall=2:29:00 basis=UNAVAILABLE unit=UNAVAILABLE",
        "b FAILED_SIGSEGV_BEFORE_F4 rc=139 wall=0:48.26 F4_completed=0 matrix=UNAVAILABLE basis=UNAVAILABLE unit=UNAVAILABLE",
        f"c TYPED_TIMEOUT_EXACT_Q_STD rc=124 wall=2:29:03 protocol_closed={out['jobs']['c']['protocol']['highest_closed_degree']} protocol_live={out['jobs']['c']['protocol']['current_degree']} matrix=NOT_EMITTED basis=UNAVAILABLE unit=UNAVAILABLE",
        "No job completed a basis; therefore no modular SIGNAL, exact-Q KILL, or nonunit SURVIVAL was produced.",
    ]
    (S/"results/terminal_summary.txt").write_text("\n".join(lines) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__": main()
