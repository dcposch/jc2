#!/usr/bin/env python3
"""Build and solve one canonical G_i-only class chart over exact Q.

This driver is deliberately promotion-strict:

* it refuses charts without the G_i subset/specialization/orientation receipt;
* the production calculation is Singular ``std`` in characteristic zero;
* the standard control battery and every input/output hash are recorded;
* a modular result is never consumed here and can never produce ``DEAD``;
* a completed non-unit basis is called ``BASIS_FOUND`` only when an exact
  rational sample point is also checked against every coefficient generator
  and ``T*c-1``.  Otherwise the public bucket remains ``COMPUTE_BOUND``.

The canonical G_i chart is class-uniform, so this is one solve per class, not
one solve per fibre alias.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shlex
import shutil
import signal
import subprocess
import sys
import threading
import time
from typing import Any, Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
GUIDED_PATH = ROOT / "box/lib/guided_gb.py"
GUIDED_SHA256 = "501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3"
TIME_SINGULAR = HERE / "time_singular.sh"
MSOLVE_CHART = ROOT / "box/moh14-charts-20260905/msolve_chart.py"
CLASS_ID_RE = re.compile(r"^C_[A-Za-z0-9_]+$")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


def artifact(path: Path) -> dict[str, Any]:
    return {
        "path": str(path.resolve()),
        "bytes": path.stat().st_size,
        "sha256": sha256_file(path),
    }


def repo_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def cpu_model() -> str:
    try:
        for line in Path("/proc/cpuinfo").read_text(encoding="utf-8", errors="replace").splitlines():
            if line.startswith("model name"):
                return line.split(":", 1)[1].strip()
    except OSError:
        pass
    return platform.processor()


def utc_now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def parse_max_rss_kib(stderr: str) -> int | None:
    matches = re.findall(r"Maximum resident set size \(kbytes\):\s*(\d+)", stderr)
    return int(matches[-1]) if matches else None


def parse_time_wall(stderr: str) -> str | None:
    matches = re.findall(r"Elapsed \(wall clock\) time \(h:mm:ss or m:ss\):\s*(\S+)", stderr)
    return matches[-1] if matches else None


def process_group_rss_kib(process_group: int) -> int:
    """Best-effort sum of resident pages for every process in one POSIX group."""

    total_pages = 0
    proc_root = Path("/proc")
    try:
        page_kib = os.sysconf("SC_PAGE_SIZE") // 1024
    except (OSError, ValueError):
        page_kib = 4
    for entry in proc_root.iterdir():
        if not entry.name.isdigit():
            continue
        try:
            stat = (entry / "stat").read_text(encoding="ascii", errors="strict")
            # comm is parenthesized and may contain spaces/parentheses; fields
            # after its final ')' begin with state, ppid, pgrp.
            fields = stat[stat.rfind(")") + 2 :].split()
            if len(fields) < 3 or int(fields[2]) != process_group:
                continue
            statm = (entry / "statm").read_text(encoding="ascii", errors="strict").split()
            total_pages += int(statm[1])
        except (FileNotFoundError, ProcessLookupError, PermissionError, ValueError, IndexError, OSError):
            continue
    return total_pages * page_kib


def run_guarded(
    command: Sequence[str],
    *,
    cwd: Path,
    stdout_path: Path,
    stderr_path: Path,
    timeout_seconds: int,
    threads: int,
) -> dict[str, Any]:
    """Run one command under a hard process-group watchdog and retain logs."""

    env = os.environ.copy()
    for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        env[key] = str(max(1, threads))
    stdout_path.parent.mkdir(parents=True, exist_ok=True)
    started_utc = utc_now()
    started = time.monotonic()
    with stdout_path.open("w", encoding="utf-8", errors="replace") as stdout_handle, stderr_path.open(
        "w", encoding="utf-8", errors="replace"
    ) as stderr_handle:
        process = subprocess.Popen(
            list(command),
            cwd=str(cwd),
            env=env,
            stdout=stdout_handle,
            stderr=stderr_handle,
            start_new_session=True,
            text=True,
        )
        rss_stop = threading.Event()
        rss_samples: list[int] = []

        def sample_rss() -> None:
            while not rss_stop.wait(0.1):
                rss_samples.append(process_group_rss_kib(process.pid))

        rss_thread = threading.Thread(target=sample_rss, daemon=True)
        rss_thread.start()
        timed_out = False
        try:
            returncode = process.wait(timeout=timeout_seconds)
        except subprocess.TimeoutExpired:
            timed_out = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                returncode = process.wait(timeout=30)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                returncode = process.wait()
        rss_samples.append(process_group_rss_kib(process.pid))
        rss_stop.set()
        rss_thread.join(timeout=2)
    elapsed = round(time.monotonic() - started, 6)
    stderr = stderr_path.read_text(encoding="utf-8", errors="replace")
    gnu_peak_rss = parse_max_rss_kib(stderr)
    sampled_peak_rss = max(rss_samples, default=0) or None
    return {
        "command": list(command),
        "command_shell_quoted": shlex.join(command),
        "cwd": str(cwd.resolve()),
        "started_utc": started_utc,
        "finished_utc": utc_now(),
        "watchdog_seconds": timeout_seconds,
        "timed_out": timed_out,
        "returncode": returncode,
        "elapsed_seconds": elapsed,
        "gnu_time_elapsed": parse_time_wall(stderr),
        "peak_rss_kib": gnu_peak_rss if gnu_peak_rss is not None else sampled_peak_rss,
        "peak_rss_source": "gnu_time" if gnu_peak_rss is not None else "sampled_process_group_100ms",
        "sampled_process_group_peak_rss_kib": sampled_peak_rss,
        "rss_sample_count": len(rss_samples),
        "stdout": artifact(stdout_path),
        "stderr": artifact(stderr_path),
    }


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def load_rows(path: Path) -> tuple[str, list[str]]:
    with path.open(encoding="utf-8", errors="strict") as handle:
        header = handle.readline().rstrip("\n")
        if not header.startswith("source_index|"):
            raise ValueError(f"bad coefficient-row header in {path}: {header!r}")
        rows: list[str] = []
        for line_number, line in enumerate(handle, start=2):
            line = line.rstrip("\n")
            if not line:
                continue
            pieces = line.split("|", 4)
            if len(pieces) != 5:
                raise ValueError(f"bad coefficient row {path}:{line_number}")
            expression = pieces[4].strip()
            if expression and expression not in {"0", "(0)"}:
                rows.append(expression)
    if not rows:
        raise ValueError(f"no nonzero coefficient generators in {path}")
    return header, rows


def receipt_gate(class_id: str, stem: str, meta: Mapping[str, Any]) -> tuple[Path, dict[str, Any]]:
    required = {
        "gi_only": True,
        "blockwise_subset_verified": True,
        "specialization_verified": True,
        "jacobian_orientation": "J(P,Q)-c*x^ell",
        "production_sign_isomorphism_verified": True,
        "production_coordinate_only_specialization_verified": True,
    }
    failures = {key: {"expected": expected, "actual": meta.get(key)} for key, expected in required.items() if meta.get(key) != expected}
    if failures:
        raise ValueError(f"G_i solve gate failed in metadata: {failures}")
    receipt_value = meta.get("verification_receipt")
    if not isinstance(receipt_value, str) or not receipt_value:
        raise ValueError("metadata has no verification_receipt")
    receipt_path = repo_path(receipt_value)
    receipt = load_json(receipt_path)
    top_required = {
        "status": "PASS",
        "all_blockwise_subset": True,
        "all_specializations": True,
        "all_orientation_checks": True,
        "all_native_zero_specializations": True,
        "all_production_sign_isomorphisms": True,
        "all_production_coordinate_only_specializations": True,
    }
    top_failures = {
        key: {"expected": expected, "actual": receipt.get(key)}
        for key, expected in top_required.items()
        if receipt.get(key) != expected
    }
    matches = [item for item in receipt.get("results", []) if isinstance(item, dict) and item.get("class_id") == class_id]
    if len(matches) != 1:
        raise ValueError(f"verification receipt has {len(matches)} entries for {class_id}")
    class_result = matches[0]
    class_required = {
        "canonical_stem": stem,
        "status": "PASS",
        "blockwise_subset_verified": True,
        "specialization_verified": True,
        "orientation_verified": True,
        "production_sign_isomorphism_verified": True,
        "production_coordinate_only_specialization_verified": True,
    }
    class_failures = {
        key: {"expected": expected, "actual": class_result.get(key)}
        for key, expected in class_required.items()
        if class_result.get(key) != expected
    }
    if top_failures or class_failures:
        raise ValueError(f"verification receipt gate failed: top={top_failures}, class={class_failures}")
    return receipt_path, class_result


def singular_command(script: Path, singular: str, threads: int) -> list[str]:
    env_path = Path(singular)
    if env_path.is_absolute() and not env_path.exists():
        raise FileNotFoundError(env_path)
    os.environ["GI_SINGULAR_BIN"] = singular
    return [
        str(TIME_SINGULAR),
        f"--cpus={max(1, threads)}",
        f"--threads={max(1, threads)}",
        f"--flint-threads={max(1, threads)}",
        "--no-rc",
        "-q",
        str(script.resolve()),
    ]


def run_builder(
    builder: Path,
    class_dir: Path,
    output_dir: Path,
    singular: str,
    timeout_seconds: int,
) -> dict[str, Any]:
    command = singular_command(builder, singular, 1)
    return run_guarded(
        command,
        cwd=class_dir,
        stdout_path=output_dir / "builder.stdout",
        stderr_path=output_dir / "builder.stderr",
        timeout_seconds=timeout_seconds,
        threads=1,
    )


def run_emitter(class_id: str, output_dir: Path) -> dict[str, Any]:
    stdout = output_dir / "emit-guided.stdout"
    stderr = output_dir / "emit-guided.stderr"
    command = [sys.executable, str(HERE / "gi_only_emit.py"), "emit-guided", "--class-id", class_id]
    record = run_guarded(
        command,
        cwd=HERE,
        stdout_path=stdout,
        stderr_path=stderr,
        timeout_seconds=180,
        threads=1,
    )
    if record["timed_out"] or record["returncode"] != 0:
        raise RuntimeError(f"emit-guided failed: {record}")
    return record


def run_modular_screen(
    *,
    stem: str,
    meta_path: Path,
    rows_path: Path,
    builder_path: Path,
    output_dir: Path,
    characteristic: int,
    timeout_seconds: int,
    threads: int,
    msolve: str,
) -> dict[str, Any]:
    """Run full-chart msolve over F_p, retaining a non-promotional screen."""

    screen_dir = output_dir / "modular-screen"
    screen_dir.mkdir(parents=True, exist_ok=True)
    record: dict[str, Any] = {
        "schema": "moh-gi-only-modular-screen-v1",
        "label": "MODULAR SCREEN ONLY — NEVER A CHARACTERISTIC-ZERO KILL",
        "promotion_allowed": False,
        "characteristic": characteristic,
        "watchdog_seconds": timeout_seconds,
        "msolve_chart_tool": artifact(MSOLVE_CHART),
        "state": "EMIT",
    }
    if characteristic <= 2:
        record.update(state="UNAVAILABLE", detail="screen characteristic must be an odd prime")
        return record
    resolved_msolve = shutil.which(msolve)
    if resolved_msolve is None:
        record.update(state="UNAVAILABLE", detail=f"msolve executable not found: {msolve}")
        return record
    ms_input = screen_dir / f"{stem}_p{characteristic}.ms"
    manifest = screen_dir / f"{stem}_p{characteristic}.manifest.json"
    emit_json = screen_dir / f"{stem}_p{characteristic}.emit.json"
    emit_command = [
        sys.executable,
        str(MSOLVE_CHART),
        "emit",
        "--meta",
        str(meta_path),
        "--rows",
        str(rows_path),
        "--builder",
        str(builder_path),
        "--characteristic",
        str(characteristic),
        "--output",
        str(ms_input),
        "--manifest",
        str(manifest),
        "--json-output",
        str(emit_json),
    ]
    emit_run = run_guarded(
        emit_command,
        cwd=HERE,
        stdout_path=screen_dir / "emit.stdout",
        stderr_path=screen_dir / "emit.stderr",
        timeout_seconds=min(180, timeout_seconds),
        threads=1,
    )
    record["emit_run"] = emit_run
    if emit_run["timed_out"] or emit_run["returncode"] != 0 or not ms_input.exists() or not manifest.exists():
        record.update(state="UNAVAILABLE", detail="custody-preserving modular input emission failed")
        return record
    record["input"] = artifact(ms_input)
    record["manifest"] = artifact(manifest)
    record["emission"] = artifact(emit_json)
    output = screen_dir / f"{stem}_p{characteristic}.g2.out"
    stdout_path = screen_dir / f"{stem}_p{characteristic}.g2.stdout"
    stderr_path = screen_dir / f"{stem}_p{characteristic}.g2.stderr"
    command = [
        "/usr/bin/time",
        "-v",
        resolved_msolve,
        "-g",
        "2",
        "-t",
        str(threads),
        "-v",
        "2",
        "-l",
        "44",
        "-m",
        "1000",
        "-f",
        str(ms_input),
        "-o",
        str(output),
    ]
    record["state"] = "RUNNING"
    solve_run = run_guarded(
        command,
        cwd=screen_dir,
        stdout_path=stdout_path,
        stderr_path=stderr_path,
        timeout_seconds=timeout_seconds,
        threads=threads,
    )
    record["run"] = solve_run
    record["solver"] = artifact(Path(resolved_msolve))
    status_json = screen_dir / f"{stem}_p{characteristic}.status.json"
    status_command = [
        sys.executable,
        str(MSOLVE_CHART),
        "status",
        "--output",
        str(output),
        "--stderr",
        str(stderr_path),
        "--rc",
        # run_guarded terminates the process group itself, so its raw return
        # code is normally -SIGTERM.  The charged status parser reserves 124
        # for a watchdog expiry; preserve that semantic in screen custody.
        str(124 if solve_run["timed_out"] else solve_run["returncode"]),
        "--manifest",
        str(manifest),
        "--json-output",
        str(status_json),
    ]
    status_run = run_guarded(
        status_command,
        cwd=HERE,
        stdout_path=screen_dir / "status.stdout",
        stderr_path=screen_dir / "status.stderr",
        timeout_seconds=60,
        threads=1,
    )
    record["status_parse_run"] = status_run
    if status_json.exists():
        parsed = load_json(status_json)
        record["parsed_status"] = parsed
        record["status_artifact"] = artifact(status_json)
        screen_status = parsed.get("status")
        if parsed.get("unit_ideal") is True:
            record["screen_signal"] = "MODULAR_UNIT_SCREEN"
        elif screen_status == "NONUNIT":
            record["screen_signal"] = "MODULAR_NONUNIT_SCREEN"
        else:
            record["screen_signal"] = f"MODULAR_{screen_status or 'INCONCLUSIVE'}_SCREEN"
    else:
        record["screen_signal"] = "MODULAR_INCONCLUSIVE_SCREEN"
    if output.exists():
        record["output"] = artifact(output)
    record.update(
        state="FINISHED",
        public_effect="none; exact-Q production run is mandatory regardless of this screen",
    )
    return record


def control_summary(stdout: str, expected_generators: int, guided: Any) -> dict[str, Any]:
    main = guided.parse_marker_controls(stdout, "main")
    generator_counts = [int(value) for value in re.findall(r"^GG__GENERATOR_COUNT main (\d+)\s*$", stdout, re.MULTILINE)]
    std_seconds = [int(value) for value in re.findall(r"^GG__STD_SECONDS main (\d+)\s*$", stdout, re.MULTILINE)]
    nf_rows = re.findall(r"^GG__NF_ZERO main (\d+) ([01])\s*$", stdout, re.MULTILINE)
    named = {}
    for token in ("RING", "EMPTY", "NONEMPTY"):
        named[token.lower()] = {
            "pass_count": len(re.findall(rf"^CONTROL_{token}_PASS(?:\s|$)", stdout, re.MULTILINE)),
            "fail_count": len(re.findall(rf"^CONTROL_{token}_FAIL(?:\s|$)", stdout, re.MULTILINE)),
        }
    named_controls_pass = all(item["pass_count"] >= 1 and item["fail_count"] == 0 for item in named.values())
    singular_errors = [line for line in stdout.splitlines() if line.lstrip().startswith("?")]
    complete = (
        named_controls_pass
        and not main.missing_markers
        and main.accepted
        and main.nf_all_zero
        and generator_counts == [expected_generators]
        and len(nf_rows) == expected_generators
        and all(bit == "1" for _, bit in nf_rows)
        and stdout.count("GG__SCRIPT_DONE main 1") == 1
        and not singular_errors
    )
    return {
        "named": named,
        "named_controls_pass": named_controls_pass,
        "guided_main": asdict(main),
        "guided_generator_counts": generator_counts,
        "expected_generators_including_Tc_minus_1": expected_generators,
        "nf_generator_rows": len(nf_rows),
        "std_seconds_markers": std_seconds,
        "script_done_count": stdout.count("GG__SCRIPT_DONE main 1"),
        "singular_error_lines": singular_errors[:20],
        "complete": complete,
    }


def rational_literal(value: Any) -> str:
    if isinstance(value, bool):
        raise ValueError("boolean is not a rational coordinate")
    text = str(value).strip()
    if not re.fullmatch(r"[+-]?\d+(?:/[1-9]\d*)?", text):
        raise ValueError(f"not an integer/rational literal: {value!r}")
    return text


def point_check_script(variables: list[str], generators: list[str], point: Mapping[str, Any]) -> str:
    solver_variables = variables + ["T"]
    if set(point) != set(solver_variables):
        missing = sorted(set(solver_variables) - set(point))
        extra = sorted(set(point) - set(solver_variables))
        raise ValueError(f"sample-point coordinates mismatch: missing={missing}, extra={extra}")
    assignments = [f"({name})-({rational_literal(point[name])})" for name in solver_variables]
    lines = [
        "// exact rational sample-point checker",
        "ring R=0,(%s),dp;" % ",".join(solver_variables),
        "ideal M=" + ",".join(assignments) + ";",
        "ideal GM=std(M);",
        "int GI_POINT_OK=1;",
    ]
    for index, expression in enumerate(generators + ["T*c-1"]):
        lines.extend(
            [
                f"poly GI_POINT_NF_{index}=reduce(({expression}),GM);",
                f"if (GI_POINT_NF_{index}!=0) {{ GI_POINT_OK=0; }}",
                f'print("GI__POINT_NF_ZERO {index} "+string(GI_POINT_NF_{index}==0));',
            ]
        )
    lines.extend(
        [
            'print("GI__POINT_ALL_ZERO "+string(GI_POINT_OK));',
            'print("GI__POINT_C_NONZERO "+string(reduce(c,GM)!=0));',
            "quit;",
            "",
        ]
    )
    return "\n".join(lines)


def verify_sample_point(
    point: Mapping[str, Any],
    *,
    variables: list[str],
    generators: list[str],
    output_dir: Path,
    singular: str,
    timeout_seconds: int,
) -> dict[str, Any]:
    script = output_dir / "sample-point-check.sing"
    script.write_text(point_check_script(variables, generators, point), encoding="utf-8")
    run = run_guarded(
        singular_command(script, singular, 1),
        cwd=output_dir,
        stdout_path=output_dir / "sample-point-check.stdout",
        stderr_path=output_dir / "sample-point-check.stderr",
        timeout_seconds=timeout_seconds,
        threads=1,
    )
    stdout = Path(run["stdout"]["path"]).read_text(encoding="utf-8", errors="replace")
    expected = len(generators) + 1
    rows = re.findall(r"^GI__POINT_NF_ZERO (\d+) ([01])$", stdout, re.MULTILINE)
    verified = (
        not run["timed_out"]
        and run["returncode"] == 0
        and len(rows) == expected
        and all(bit == "1" for _, bit in rows)
        and stdout.count("GI__POINT_ALL_ZERO 1") == 1
        and stdout.count("GI__POINT_C_NONZERO 1") == 1
    )
    return {
        "kind": "exact_rational_full_assignment",
        "coordinates": {name: rational_literal(point[name]) for name in variables + ["T"]},
        "verified": verified,
        "residual_count": len(rows),
        "expected_residual_count_including_Tc_minus_1": expected,
        "script": artifact(script),
        "run": run,
    }


def try_sample_points(
    sample_path: Path | None,
    *,
    variables: list[str],
    generators: list[str],
    output_dir: Path,
    singular: str,
    timeout_seconds: int,
) -> dict[str, Any]:
    candidates: list[tuple[str, Mapping[str, Any]]] = []
    if sample_path is not None:
        supplied = load_json(sample_path)
        coordinates = supplied.get("coordinates", supplied)
        if not isinstance(coordinates, dict):
            raise ValueError("sample point must be an object or have an object-valued coordinates key")
        candidates.append(("supplied", coordinates))
    else:
        plus = {name: "0" for name in variables + ["T"]}
        plus.update(c="1", T="1")
        minus = dict(plus)
        minus.update(c="-1", T="-1")
        candidates.extend((("canonical_all_zero_c1", plus), ("canonical_all_zero_cminus1", minus)))
    attempts = []
    for index, (label, point) in enumerate(candidates):
        candidate_dir = output_dir / f"point-{index}-{label}"
        candidate_dir.mkdir(parents=True, exist_ok=True)
        record = verify_sample_point(
            point,
            variables=variables,
            generators=generators,
            output_dir=candidate_dir,
            singular=singular,
            timeout_seconds=timeout_seconds,
        )
        record["label"] = label
        attempts.append(record)
        if record["verified"]:
            return {"verified": True, "selected": record, "attempts": attempts}
    return {"verified": False, "selected": None, "attempts": attempts}


def software_record(singular: str) -> dict[str, Any]:
    resolved = subprocess.run(["bash", "-lc", f"command -v {shlex.quote(singular)}"], capture_output=True, text=True, check=True).stdout.strip()
    binary = Path(resolved)
    version = subprocess.run([resolved, "--version"], capture_output=True, text=True, check=False).stdout.splitlines()[:8]
    return {
        "singular": {"path": resolved, "sha256": sha256_file(binary), "version_head": version},
        "guided_gb": artifact(GUIDED_PATH),
        "time_wrapper": artifact(TIME_SINGULAR),
        "python": {"executable": sys.executable, "version": sys.version},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--class-id", required=True)
    parser.add_argument("--timeout", type=int, default=600, help="exact-Q std watchdog; maximum permitted is 600")
    parser.add_argument("--build-timeout", type=int, default=1800, help="coefficient-extraction watchdog (not the std watchdog)")
    parser.add_argument("--point-timeout", type=int, default=60)
    parser.add_argument("--threads", type=int, default=1)
    parser.add_argument("--singular", default="Singular")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--sample-point", type=Path, help="optional exact rational full assignment JSON")
    parser.add_argument("--modular-screen", action="store_true", help="run a non-promotional full-chart F_p msolve screen before exact Q")
    parser.add_argument("--screen-prime", type=int, default=1073741827)
    parser.add_argument("--screen-timeout", type=int, default=600)
    parser.add_argument("--msolve", default="msolve")
    parser.add_argument("--msolve-threads", type=int, default=8)
    args = parser.parse_args()

    if not CLASS_ID_RE.fullmatch(args.class_id):
        raise SystemExit(f"unsafe/invalid class id: {args.class_id!r}")
    if not 1 <= args.timeout <= 600:
        raise SystemExit("--timeout must lie in [1,600]")
    if not 1 <= args.build_timeout <= 3600:
        raise SystemExit("--build-timeout must lie in [1,3600]")
    if not 1 <= args.point_timeout <= 600:
        raise SystemExit("--point-timeout must lie in [1,600]")
    if args.threads < 1:
        raise SystemExit("--threads must be positive")
    if not 1 <= args.screen_timeout <= 600:
        raise SystemExit("--screen-timeout must lie in [1,600]")
    if args.msolve_threads < 1:
        raise SystemExit("--msolve-threads must be positive")
    if sha256_file(GUIDED_PATH) != GUIDED_SHA256:
        raise SystemExit("charged box/lib/guided_gb.py content mismatch")

    sys.path.insert(0, str(GUIDED_PATH.parent))
    import guided_gb as guided  # type: ignore

    class_dir = HERE / "classes" / args.class_id
    class_json_path = class_dir / "class.json"
    class_json = load_json(class_json_path)
    stem = class_json.get("canonical_stem")
    if not isinstance(stem, str) or stem != f"{args.class_id}_G":
        raise SystemExit(f"unexpected canonical stem in {class_json_path}: {stem!r}")
    output_dir = (args.output_dir or (class_dir / "solve")).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    status_path = output_dir / "solve-result.json"
    status: dict[str, Any] = {
        "schema": "moh-gi-only-exact-q-solve-v1",
        "class_id": args.class_id,
        "canonical_stem": stem,
        "class_uniform_chart": True,
        "one_chart_per_class_suffices": True,
        "promotion_scope": "EXACT_Q_ONLY",
        "modular_policy": "SCREEN_ONLY_NEVER_PROMOTED",
        "state": "PREFLIGHT",
        "verdict": "COMPUTE_BOUND",
        "started_utc": utc_now(),
    }
    atomic_json(status_path, status)

    meta_path = class_dir / "meta" / f"{stem}.json"
    meta = load_json(meta_path)
    receipt_path, receipt_class = receipt_gate(args.class_id, stem, meta)
    variables = meta.get("variables")
    if not isinstance(variables, list) or not variables or not all(isinstance(value, str) for value in variables):
        raise ValueError("metadata variables must be a nonempty string list")
    if len(variables) != len(set(variables)) or variables.count("c") != 1 or "T" in variables:
        raise ValueError("metadata variables must be distinct, contain c exactly once, and omit inverse T")
    parameter_count = meta.get("parameter_count")
    if parameter_count != len(variables):
        raise ValueError(f"parameter_count {parameter_count!r} != len(variables) {len(variables)}")
    rows_path = repo_path(meta["rows_path"])
    builder_path = repo_path(meta["builder"])
    status.update(
        state="BUILD",
        unknowns_without_T=parameter_count,
        solver_variables_with_T=parameter_count + 1,
        verification={"receipt": artifact(receipt_path), "class_result": receipt_class},
        inputs={"class_json": artifact(class_json_path), "meta_prebuild": artifact(meta_path), "builder": artifact(builder_path)},
    )
    atomic_json(status_path, status)

    if not rows_path.exists():
        build = run_builder(builder_path, class_dir, output_dir, args.singular, args.build_timeout)
        status["builder_run"] = build
        atomic_json(status_path, status)
        if build["timed_out"] or build["returncode"] != 0 or not rows_path.exists():
            status.update(
                state="FINISHED",
                verdict="COMPUTE_BOUND",
                verdict_detail="builder did not produce coefficient rows within its guarded run",
                finished_utc=utc_now(),
            )
            atomic_json(status_path, status)
            print(json.dumps(status, indent=2, sort_keys=True))
            return 0
    else:
        status["builder_run"] = {"skipped": True, "reason": "custodied rows already exist"}

    header, generators = load_rows(rows_path)
    status["coefficient_generators"] = len(generators)
    status["ideal_generators_including_Tc_minus_1"] = len(generators) + 1
    status["rows"] = {**artifact(rows_path), "header": header}
    if args.modular_screen:
        status["state"] = "MODULAR_SCREEN_RUNNING"
        atomic_json(status_path, status)
        status["modular_screen"] = run_modular_screen(
            stem=stem,
            meta_path=meta_path,
            rows_path=rows_path,
            builder_path=builder_path,
            output_dir=output_dir,
            characteristic=args.screen_prime,
            timeout_seconds=args.screen_timeout,
            threads=args.msolve_threads,
            msolve=args.msolve,
        )
        # This result is intentionally never consulted in exact classification.
        atomic_json(status_path, status)
    else:
        status["modular_screen"] = {
            "state": "NOT_REQUESTED",
            "label": "MODULAR SCREEN ONLY — NEVER A CHARACTERISTIC-ZERO KILL",
            "promotion_allowed": False,
        }
    status["state"] = "EMIT_GUIDED"
    atomic_json(status_path, status)
    emitter_run = run_emitter(args.class_id, output_dir)
    status["emitter_run"] = emitter_run
    meta = load_json(meta_path)
    # Re-run the refusal gate after emit-guided mutates generator-count metadata.
    receipt_path_after, _ = receipt_gate(args.class_id, stem, meta)
    if receipt_path_after.resolve() != receipt_path.resolve():
        raise ValueError("verification receipt path changed during emit-guided")
    declared_generators = meta.get("jacobian_coefficient_generator_count", meta.get("generator_count"))
    if declared_generators != len(generators):
        raise ValueError(f"declared coefficient generator count {declared_generators} != extracted {len(generators)}")
    declared_total = meta.get("generator_count_including_inverse")
    if declared_total != len(generators) + 1:
        raise ValueError(f"declared total generator count {declared_total} != extracted+inverse {len(generators) + 1}")
    guided_value = meta.get("guided_job", f"classes/{args.class_id}/jobs/{stem}_Q_guided.sing")
    guided_path = repo_path(guided_value)
    script_text = guided_path.read_text(encoding="utf-8", errors="strict")
    if not re.search(r"(?m)^ring\s+R\s*=\s*0\s*,", script_text):
        raise ValueError("guided production script is not a characteristic-zero polynomial ring")
    if "GG__UNIT" not in script_text or "T*c-1" not in script_text:
        raise ValueError("guided production script lacks guided unit control or Tc-1")

    exact_stdout = output_dir / f"{stem}_Q.stdout"
    exact_stderr = output_dir / f"{stem}_Q.stderr"
    status.update(
        state="EXACT_Q_RUNNING",
        meta_postemit=artifact(meta_path),
        guided_script=artifact(guided_path),
        software=software_record(args.singular),
        host={
            "hostname": platform.node(),
            "platform": platform.platform(),
            "cpu_model": cpu_model(),
            "pid": os.getpid(),
        },
    )
    atomic_json(status_path, status)
    exact_run = run_guarded(
        singular_command(guided_path, args.singular, args.threads),
        cwd=class_dir,
        stdout_path=exact_stdout,
        stderr_path=exact_stderr,
        timeout_seconds=args.timeout,
        threads=args.threads,
    )
    stdout = exact_stdout.read_text(encoding="utf-8", errors="replace")
    controls = control_summary(stdout, len(generators) + 1, guided)
    exact_complete = not exact_run["timed_out"] and exact_run["returncode"] == 0 and controls["complete"]
    main_controls = controls["guided_main"]
    exact_unit = exact_complete and main_controls["unit"] is True
    status.update(state="CLASSIFY", exact_q={"run": exact_run, "controls": controls})

    sample: dict[str, Any] | None = None
    if exact_complete and not exact_unit and main_controls["dimension"] is not None:
        sample = try_sample_points(
            args.sample_point.resolve() if args.sample_point else None,
            variables=variables,
            generators=generators,
            output_dir=output_dir / "sample",
            singular=args.singular,
            timeout_seconds=args.point_timeout,
        )
        status["sample_point"] = sample

    if exact_unit:
        status.update(
            verdict="DEAD",
            verdict_detail="exact-Q Singular std is UNIT with the full control battery; modular evidence was not used",
            report_label="DEAD — EXACT-Q UNIT ON THE FULL G_i CHART",
        )
    elif exact_complete and not exact_unit and sample and sample["verified"]:
        status.update(
            verdict="BASIS_FOUND",
            dimension=main_controls["dimension"],
            verdict_detail="exact-Q non-unit basis plus an exactly verified rational sample point",
            report_label="BASIS FOUND — NONEMPTY EXACT-Q SAMPLE POINT VERIFIED (LOUD)",
        )
    else:
        reasons = []
        if exact_run["timed_out"]:
            reasons.append(f"{args.timeout} s exact-Q watchdog expired")
        if exact_run["returncode"] != 0:
            reasons.append(f"Singular return code {exact_run['returncode']}")
        if not controls["complete"]:
            reasons.append("control-complete exact-Q basis markers absent")
        if exact_complete and not exact_unit:
            reasons.append("non-unit basis has no exactly verified full sample point")
            status["dimension_if_basis_completed"] = main_controls["dimension"]
            status["basis_size_if_completed"] = main_controls["basis_size"]
        status.update(
            verdict="COMPUTE_BOUND",
            verdict_detail="; ".join(reasons) or "no promotable exact-Q conclusion",
            report_label="COMPUTE-BOUND — NO EXACT-Q UNIT OR VERIFIED SAMPLE POINT",
        )
    status.update(state="FINISHED", finished_utc=utc_now())
    atomic_json(status_path, status)
    print(json.dumps(status, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"GI_SOLVE_DRIVER_ERROR {exc!r}", file=sys.stderr, flush=True)
        raise
