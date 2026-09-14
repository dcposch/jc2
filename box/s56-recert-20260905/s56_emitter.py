#!/usr/bin/env python3
"""Source-complete S5/S6 chart emitter and guarded solve driver.

The support is an explicit parameter.  ``legacy-capped`` reproduces the
2026-09-03 order-basis inventory, while ``source-complete`` uses

    S_i = D_i union G_i,
    D_i = {(b,a): 0 <= a < K, b <= floor(delta1*a-i*B)},
    G_i = {(b,a): 0 <= a < K, b <= floor(d*(i*K-a))},

where ``d=-delta_s``.  Ordered pairs are always ``(x power, y power)``.

Generated builders retain the old partition face as an affine origin.  Since
S_1 contains all of its non-monic terms, this is affinely isomorphic to the
canonical source chart with top ``y^K``; the coordinate map is serialized in
every metadata file.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import signal
import socket
import subprocess
import sys
import threading
import time
from datetime import datetime, timezone
from fractions import Fraction as F
from typing import Any, Iterable, Sequence

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
INPUTS = Path("/tmp/jc2-lane.eKMomd/inputs")
RECEIPT = ROOT / "xmodel" / "s56-recert-sol56-20260905.run.v2"
ORDER_BASIS = ROOT / "box" / "orderbasis-20260903" / "order_basis_full.py"
GUIDED_GB = INPUTS / "guided_gb.py"
TIMED_SINGULAR = HERE / "timed_singular.sh"
SUPPORTS = ("legacy-capped", "source-complete")
PRIMES = (32003, 32009, 32027)


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ob = load_module("s56_order_basis", ORDER_BASIS)
gg = load_module("s56_guided_gb", GUIDED_GB)


ROWS = {
    "S5": ob.Row("S5_n9_m6_M2_V1_k8", "S5 source-complete", 9, 6, 2, 1, 8),
    "S6": ob.Row("S6_n9_m6_M5_V2_k8", "S6 source-complete", 9, 6, 5, 2, 8),
}
TARGETS = (("S5", (2,)), ("S5", (1, 1)), ("S6", (1,)))


def process_group_sample(group: int, requested_cpu: int | None = None) -> tuple[int, list[int]]:
    """Return process-group RSS/PIDs and enforce an optional one-CPU pin.

    Singular resets its own affinity while starting.  Reapplying the requested
    mask while sampling keeps concurrently dispatched one-core jobs isolated.
    """
    total = 0
    members: list[int] = []
    for stat_path in Path("/proc").glob("[0-9]*/stat"):
        try:
            stat = stat_path.read_text(encoding="utf-8")
            tail = stat[stat.rfind(")") + 2:].split()
            if int(tail[2]) != group:  # pgrp is field 5, tail starts at field 3
                continue
            pid = int(stat_path.parent.name)
            members.append(pid)
            if requested_cpu is not None:
                os.sched_setaffinity(pid, {requested_cpu})
            status = stat_path.with_name("status").read_text(encoding="utf-8")
            match = re.search(r"^VmRSS:\s+(\d+)\s+kB$", status, re.M)
            if match:
                total += int(match.group(1))
        except (FileNotFoundError, PermissionError, ProcessLookupError, ValueError, OSError):
            continue
    return total, members


def monitored_run_singular_script(
    script_path: Path,
    output_prefix: Path,
    config: Any,
    cpus: int,
) -> tuple[list[str], str, str, int | None, bool, float]:
    """Drop-in guided_gb runner with durable process-group RSS sampling."""
    env = os.environ.copy()
    thread_count = str(max(1, cpus))
    for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        env[key] = thread_count
    command = [
        "stdbuf", "-oL", "-eL", config.singular,
        f"--cpus={cpus}", f"--threads={cpus}", f"--flint-threads={cpus}",
    ]
    if config.no_rc:
        command.append("--no-rc")
    command.extend(["-q", str(script_path)])
    stdout_path = output_prefix.with_suffix(".out")
    stderr_path = output_prefix.with_suffix(".err")
    stdout_chunks: list[str] = []
    stderr_chunks: list[str] = []
    started = time.monotonic()
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
        env=env,
        start_new_session=True,
    )
    assert process.stdout is not None and process.stderr is not None
    streamers = [
        threading.Thread(target=gg._stream_pipe, args=(process.stdout, stdout_path, stdout_chunks), daemon=True),
        threading.Thread(target=gg._stream_pipe, args=(process.stderr, stderr_path, stderr_chunks), daemon=True),
    ]
    for worker in streamers:
        worker.start()
    stop_monitor = threading.Event()
    samples = 0
    peak_rss_kb = 0
    requested_cpu_text = env.get("S56_CPU")
    requested_cpu = int(requested_cpu_text) if requested_cpu_text else None
    last_members: list[int] = []

    def monitor() -> None:
        nonlocal samples, peak_rss_kb, last_members
        while not stop_monitor.wait(0.1):
            samples += 1
            rss_kb, last_members = process_group_sample(process.pid, requested_cpu)
            peak_rss_kb = max(peak_rss_kb, rss_kb)

    monitor_thread = threading.Thread(target=monitor, daemon=True)
    monitor_thread.start()
    timed_out = False
    try:
        returncode = process.wait(timeout=config.timeout_seconds)
    except subprocess.TimeoutExpired:
        timed_out = True
        os.killpg(process.pid, signal.SIGTERM)
        try:
            returncode = process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            returncode = process.wait()
    stop_monitor.set()
    monitor_thread.join(timeout=2)
    final_rss_kb, last_members = process_group_sample(process.pid, requested_cpu)
    peak_rss_kb = max(peak_rss_kb, final_rss_kb)
    for worker in streamers:
        worker.join(timeout=5)
    elapsed = time.monotonic() - started
    resource_path = output_prefix.with_suffix(".resource.json")
    atomic_write(resource_path, json.dumps({
        "schema": "jc2.s56-recert.process-group-resource/v1",
        "process_group": process.pid,
        "maximum_process_group_rss_kb": peak_rss_kb,
        "requested_cpu": requested_cpu,
        "last_observed_members": last_members,
        "samples": samples,
        "sample_period_seconds": 0.1,
        "elapsed_seconds": round(elapsed, 6),
        "returncode": returncode,
        "timed_out": timed_out,
        "command": command,
    }, indent=2, sort_keys=True) + "\n")
    return command, "".join(stdout_chunks), "".join(stderr_chunks), returncode, timed_out, elapsed


# Retain the frozen emitter/parser/promotion logic, replacing only its process
# launcher so compute-bound runs have independently sampled RSS custody.
gg.run_singular_script = monitored_run_singular_script


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def json_dump(path: Path, payload: Any) -> None:
    atomic_write(path, json.dumps(payload, indent=2, sort_keys=True) + "\n")


def receipt_fields() -> tuple[Path, list[dict[str, Any]]]:
    values: dict[str, str] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            values[key] = value
    count = int(values["charged_inputs"])
    records = []
    for index in range(1, count + 1):
        records.append({
            "index": index,
            "basename": values[f"charged_input_{index}_basename"],
            "expected": values[f"charged_input_{index}_sha256"],
        })
    return Path(values["lane_inputs_dir"]), records


def verify_inputs() -> dict[str, Any]:
    input_dir, records = receipt_fields()
    checks = []
    lines = []
    for record in records:
        path = input_dir / record["basename"]
        got = sha256(path)
        checks.append({**record, "path": str(path), "got": got, "ok": got == record["expected"]})
        lines.append(f"{record['expected']}  {path}")
    manifest = HERE / "frozen-inputs.sha256"
    atomic_write(manifest, "\n".join(lines) + "\n")
    payload = {
        "schema": "jc2.s56-recert.frozen-input-check/v1",
        "method": "receipt numbered basename/sha256 join; independently replayed with awk | sha256sum -c before code actions",
        "receipt": str(RECEIPT.relative_to(ROOT)),
        "receipt_sha256": sha256(RECEIPT),
        "input_dir": str(input_dir),
        "manifest": str(manifest.relative_to(ROOT)),
        "manifest_sha256": sha256(manifest),
        "checks": checks,
        "ok": bool(checks) and all(item["ok"] for item in checks),
    }
    json_dump(HERE / "frozen-inputs-check.json", payload)
    if not payload["ok"]:
        raise RuntimeError("charged-input content mismatch")
    return payload


def parse_part(text: str) -> tuple[int, ...]:
    part = tuple(int(piece) for piece in re.split(r"[+,]", text) if piece)
    if not part or tuple(sorted(part, reverse=True)) != part:
        raise ValueError(f"bad descending partition {text!r}")
    return part


def ordered(mons: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    return sorted(set(mons), key=lambda mon: (-mon[1], mon[0]))


def d_inventory(C: dict[str, Any], deficit: int) -> list[tuple[int, int]]:
    out = []
    for a in range(C["K"]):
        maximum = math.floor(C["delta1"] * a - deficit * C["B"])
        out.extend((b, a) for b in range(maximum + 1))
    return ordered(out)


def g_inventory(C: dict[str, Any], deficit: int) -> list[tuple[int, int]]:
    d = -C["delta2"]
    out = []
    for a in range(C["K"]):
        maximum = math.floor(d * (deficit * C["K"] - a))
        out.extend((b, a) for b in range(maximum + 1))
    return ordered(out)


def source_inventory(C: dict[str, Any], deficit: int) -> list[tuple[int, int]]:
    return ordered(set(d_inventory(C, deficit)) | set(g_inventory(C, deficit)))


def selected_inventories(row: Any, C: dict[str, Any], support: str) -> dict[str, Any]:
    if support not in SUPPORTS:
        raise ValueError(f"unknown support {support!r}")
    if support == "legacy-capped":
        h = ob.h_inventory(row, C)
        alpha = {i: ob.coeff_inventory(C, i) for i in range(1, C["e"] + 1)}
        beta = {i: ob.coeff_inventory(C, i) for i in range(2, C["q"] + 1)}
    else:
        h = source_inventory(C, 1)
        alpha = {i: source_inventory(C, i) for i in range(1, C["e"] + 1)}
        beta = {i: source_inventory(C, i) for i in range(2, C["q"] + 1)}
    return {"h": ordered(h), "alpha": alpha, "beta": beta}


def mon_list(mons: Iterable[tuple[int, int]]) -> list[list[int]]:
    return [list(mon) for mon in ordered(mons)]


def support_record(row: Any, support: str) -> dict[str, Any]:
    C = ob.closed_form(row)
    selected = selected_inventories(row, C, support)
    return {
        "support": support,
        "D": {str(i): mon_list(d_inventory(C, i)) for i in range(1, C["e"] + 1)},
        "G": {str(i): mon_list(g_inventory(C, i)) for i in range(1, C["e"] + 1)},
        "S": {str(i): mon_list(source_inventory(C, i)) for i in range(1, C["e"] + 1)},
        "selected": {
            "h": mon_list(selected["h"]),
            "alpha": {str(i): mon_list(mons) for i, mons in selected["alpha"].items()},
            "beta": {str(i): mon_list(mons) for i, mons in selected["beta"].items()},
        },
    }


def apply_terminal_gauges(C: dict[str, Any], inventories: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    alpha = {i: list(mons) for i, mons in inventories["alpha"].items()}
    beta = {i: list(mons) for i, mons in inventories["beta"].items()}
    gauges: list[str] = []
    if (0, 0) in beta[C["q"]]:
        beta[C["q"]] = [mon for mon in beta[C["q"]] if mon != (0, 0)]
        gauges.append(f"Q -> Q - const(beta_{C['q']})")
    if (0, 0) in alpha[C["e"]]:
        alpha[C["e"]] = [mon for mon in alpha[C["e"]] if mon != (0, 0)]
        gauges.append(f"P -> P - const(alpha_{C['e']})")
    return {"h": list(inventories["h"]), "alpha": alpha, "beta": beta}, gauges


def affine_origin_map(face: dict[str, Any], h_mons: Sequence[tuple[int, int]], x: Any, y: Any) -> dict[str, Any]:
    top = sp.Poly(sp.expand(face["top"] - y ** sp.Poly(face["top"], y).degree()), x, y)
    forward = []
    inverse = []
    for b, a in h_mons:
        coeff = sp.expand(top.coeff_monomial(x**b * y**a))
        z = f"h_{b}_{a}"
        u = f"u_{b}_{a}"
        forward.append({"canonical": u, "partition_origin": z, "formula": f"{z}+({ob.sstr(coeff)})"})
        inverse.append({"partition_origin": z, "canonical": u, "formula": f"{u}-({ob.sstr(coeff)})"})
    return {
        "statement": "h=y^K+sum u_ba*x^b*y^a; u_ba=h_ba+coefficient_ba(partition_face-y^K)",
        "forward_partition_to_canonical": forward,
        "inverse_canonical_to_partition": inverse,
        "triangular_affine_ring_isomorphism": True,
    }


def build_spec(row: Any, part: Sequence[int], support: str) -> dict[str, Any]:
    C = ob.closed_form(row)
    if C["B"] >= 0:
        raise ValueError("nonnegative B outside chart")
    if sum(part) != C["u"]:
        raise ValueError("partition does not sum to u'")
    x, y = sp.symbols("x y")
    face = ob.top_face(row, part, x, y)
    before = selected_inventories(row, C, support)
    inv, gauges = apply_terminal_gauges(C, before)
    if inv["alpha"][C["e"] - C["q"]] == [(0, 0)]:
        raise AssertionError("unexpected scalar shear; source-complete chart must retain alpha_1")

    h_params = [sp.Symbol(f"h_{b}_{a}") for b, a in inv["h"]]
    h = sp.expand(face["top"] + sum(
        param * ob.monomial_expr(mon, x, y) for param, mon in zip(h_params, inv["h"])
    ))
    params: list[Any] = h_params + list(face["slopes"])
    setup = [f"poly h = {ob.sstr(h)};"]
    for i in range(1, C["e"] + 1):
        expr = sp.Integer(0)
        for b, a in inv["alpha"][i]:
            symbol = sp.Symbol(f"A{i}_{b}_{a}")
            params.append(symbol)
            expr += symbol * x**b * y**a
        setup.append(f"poly AA{i} = {ob.sstr(expr)};")
    for i in range(2, C["q"] + 1):
        expr = sp.Integer(0)
        for b, a in inv["beta"][i]:
            symbol = sp.Symbol(f"B{i}_{b}_{a}")
            params.append(symbol)
            expr += symbol * x**b * y**a
        setup.append(f"poly BB{i} = {ob.sstr(expr)};")
    c = sp.Symbol("c")
    params.append(c)
    sat = sp.expand(c * face["omega"])

    source = support_record(row, support)
    source["selected_post_gauge"] = {
        "h": mon_list(inv["h"]),
        "alpha": {str(i): mon_list(mons) for i, mons in inv["alpha"].items()},
        "beta": {str(i): mon_list(mons) for i, mons in inv["beta"].items()},
    }
    meta = {
        "row": {**row.__dict__, "ell": row.k},
        "partition": list(part),
        "partition_label": "+".join(map(str, part)),
        "chart": support,
        "closed_form": ob.serial_closed_form(C),
        "delta_s": ob.qstr(C["delta2"]),
        "d": ob.qstr(-C["delta2"]),
        "source_support": source,
        "source_recentring": {
            "N": C["q"] * C["K"],
            "eta": f"-[y^{C['q'] * C['K'] - 1}]Q/{C['q'] * C['K']}",
            "group_element": "phi(x,y)=(x,y+eta(x))",
            "inverse": "phi^-1(x,y)=(x,y-eta(x))",
            "determinant": 1,
            "x_fixed": True,
            "jacobian_target_preserved": f"c*x^{row.k}",
        },
        "top_face_factored": face["factored"],
        "partition_face_origin": ob.sstr(face["top"]),
        "partition_to_canonical_map": affine_origin_map(face, inv["h"], x, y),
        "omega": ob.sstr(face["omega"]),
        "saturation_factor": ob.sstr(sat),
        "h_inventory": mon_list(inv["h"]),
        "h_inventory_count": len(inv["h"]),
        "h_parameters": [str(param) for param in h_params],
        "alpha_inventories": {str(i): mon_list(mons) for i, mons in inv["alpha"].items()},
        "beta_inventories": {str(i): mon_list(mons) for i, mons in inv["beta"].items()},
        "alpha_dims": [len(inv["alpha"][i]) for i in range(1, C["e"] + 1)],
        "beta_dims": [len(inv["beta"][i]) for i in range(2, C["q"] + 1)],
        "beta1": "structurally_zero_unique_qth_approximate_root",
        "gauges": gauges,
        "gauge_group_elements": [
            "tau_Q_kappa:(P,Q)->(P,Q-kappa), inverse tau_Q_-kappa, det on target values 1",
            "tau_P_lambda:(P,Q)->(P-lambda,Q), inverse tau_P_-lambda, det on target values 1",
        ],
        "scalar_shear_used": False,
        "params_without_T": len(params),
        "levels_cap": C["e"] + C["q"] + 2 * C["K"] + 12,
    }
    low_terms = [("1", C["q"])] + [(f"BB{i}", C["q"] - i) for i in range(2, C["q"] + 1)]
    high_terms = [("1", C["e"])] + [(f"AA{i}", C["e"] - i) for i in range(1, C["e"] + 1)]
    return {"meta": meta, "setup": setup, "params": params, "sat": sat, "low_terms": low_terms, "high_terms": high_terms}


def stem_for(name: str, part: Sequence[int], support: str) -> str:
    tag = "legacy" if support == "legacy-capped" else "source_complete"
    return f"{ROWS[name].key}_part_{'_'.join(map(str, part))}_{tag}"


def emit_one(name: str, part: tuple[int, ...], support: str) -> dict[str, Any]:
    spec = build_spec(ROWS[name], part, support)
    stem = stem_for(name, part, support)
    base = HERE / support
    rows_path = base / "rows" / f"{stem}_rows.tsv"
    builder_path = base / "builders" / f"{stem}_builder.sing"
    meta_path = base / "meta" / f"{stem}.json"
    rows_path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(builder_path, ob.native_builder_text(spec, rows_path))
    payload = {
        "schema": "jc2.s56-recert.source-complete-order-chart/v1",
        "emitter": str(Path(__file__).relative_to(ROOT)),
        "emitter_sha256": sha256(Path(__file__)),
        "dependencies": {
            str(ORDER_BASIS.relative_to(ROOT)): sha256(ORDER_BASIS),
            str(GUIDED_GB): sha256(GUIDED_GB),
        },
        "support_parameter": support,
        "source_correction": {
            "target": f"c*x^{ROWS[name].k}",
            "formula": "ell=v_s-u_s-1",
            "ell": ROWS[name].k,
            "citation": "Moh 1983 Proposition 6.3(3), printed p.197; frozen gate report section 4",
        },
        "meta": spec["meta"],
        "variables": [str(symbol) for symbol in spec["params"]],
        "sat": ob.sstr(spec["sat"]),
        "builder": str(builder_path.relative_to(ROOT)),
        "builder_sha256": sha256(builder_path),
        "rows_path": str(rows_path.relative_to(ROOT)),
    }
    if meta_path.exists():
        previous = json.loads(meta_path.read_text(encoding="utf-8"))
        previous_run = previous.get("builder_run")
        if (
            previous.get("builder_sha256") == payload["builder_sha256"]
            and previous.get("rows_path") == payload["rows_path"]
            and previous_run
            and previous_run.get("native_done")
            and previous_run.get("target_gate")
            and previous_run.get("returncode") == 0
        ):
            payload["builder_run"] = previous_run
    json_dump(meta_path, payload)
    return {"meta_path": str(meta_path.relative_to(ROOT)), **payload}


def emit_all(support: str) -> list[dict[str, Any]]:
    return [emit_one(name, part, support) for name, part in TARGETS]


def inventory_diff() -> dict[str, Any]:
    out: dict[str, Any] = {
        "schema": "jc2.s56-recert.inventory-diff/v1",
        "pair_order": "(b,a)=(x_power,y_power)",
        "support_formula": {
            "D_i": "0<=a<K and 0<=b<=floor(delta1*a-i*B)",
            "G_i": "0<=a<K and 0<=b<=floor(d*(i*K-a)), d=-delta_s",
            "S_i": "D_i union G_i",
        },
        "rows": {},
    }
    for name, row in ROWS.items():
        C = ob.closed_form(row)
        old = selected_inventories(row, C, "legacy-capped")
        new = selected_inventories(row, C, "source-complete")
        old_g, _ = apply_terminal_gauges(C, old)
        new_g, gauges = apply_terminal_gauges(C, new)
        record: dict[str, Any] = {
            "datum": {"n": row.n, "m": row.m, "M2": row.M2, "V2": row.V2, "K": C["K"], "ell": row.k},
            "delta1": ob.qstr(C["delta1"]),
            "delta_s": ob.qstr(C["delta2"]),
            "B": ob.qstr(C["B"]),
            "d": ob.qstr(-C["delta2"]),
            "gauges": gauges,
            "blocks": {},
        }
        blocks = [("h", 1, old_g["h"], new_g["h"])]
        blocks.extend((f"alpha_{i}", i, old_g["alpha"][i], new_g["alpha"][i]) for i in old_g["alpha"])
        blocks.extend((f"beta_{i}", i, old_g["beta"][i], new_g["beta"][i]) for i in old_g["beta"])
        for block, deficit, old_mons, new_mons in blocks:
            old_set, new_set = set(old_mons), set(new_mons)
            record["blocks"][block] = {
                "deficit": deficit,
                "old": mon_list(old_set),
                "new": mon_list(new_set),
                "added": mon_list(new_set - old_set),
                "removed": mon_list(old_set - new_set),
                "old_count": len(old_set),
                "new_count": len(new_set),
                "added_count": len(new_set - old_set),
                "D_i": mon_list(d_inventory(C, deficit)),
                "G_i": mon_list(g_inventory(C, deficit)),
                "S_i_pre_gauge": mon_list(source_inventory(C, deficit)),
            }
            if old_set - new_set:
                raise AssertionError(f"legacy support not contained in source-complete support: {name} {block}")
        base = len(new_g["h"]) + sum(map(len, new_g["alpha"].values())) + sum(map(len, new_g["beta"].values())) + 1
        record["new_parameter_count_without_T_or_slopes"] = base
        record["partition_parameter_counts_without_T"] = {
            "+".join(map(str, part)): base + max(0, len(part) - 1)
            for row_name, part in TARGETS if row_name == name
        }
        out["rows"][name] = record
    json_dump(HERE / "inventory-diff.json", out)
    return out


def parse_time_verbose(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {}
    if not path.exists():
        return result
    patterns = {
        "maximum_rss_kb": r"Maximum resident set size \(kbytes\):\s*(\d+)",
        "elapsed_wall": r"Elapsed \(wall clock\) time.*:\s*(\S+)",
        "user_seconds": r"User time \(seconds\):\s*(\S+)",
        "system_seconds": r"System time \(seconds\):\s*(\S+)",
        "exit_status": r"Exit status:\s*(\d+)",
    }
    text = path.read_text(encoding="utf-8", errors="replace")
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            value: Any = match.group(1)
            if key in {"maximum_rss_kb", "exit_status"}:
                value = int(value)
            result[key] = value
    return result


def run_builder(meta_path: Path, timeout: int) -> dict[str, Any]:
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    builder = ROOT / payload["builder"]
    stem = meta_path.stem
    run_dir = HERE / "build-runs"
    out = run_dir / f"{stem}.out"
    err = run_dir / f"{stem}.err"
    timing = run_dir / f"{stem}.time"
    run_dir.mkdir(parents=True, exist_ok=True)
    command = [
        "timeout", str(timeout), "/usr/bin/time", "-v", "-o", str(timing),
        "Singular", "--cpus=1", "--threads=1", "--flint-threads=1", "--no-rc", "-q", str(builder),
    ]
    env = os.environ.copy()
    for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS", "FLINT_NUM_THREADS"):
        env[key] = "1"
    started_utc = utc_now()
    started = time.monotonic()
    with out.open("w", encoding="utf-8") as stdout, err.open("w", encoding="utf-8") as stderr:
        result = subprocess.run(command, cwd=ROOT, env=env, stdout=stdout, stderr=stderr, text=True, check=False)
    elapsed = time.monotonic() - started
    text = out.read_text(encoding="utf-8", errors="replace")
    rows_path = ROOT / payload["rows_path"]
    row_count = None
    if rows_path.exists():
        with rows_path.open(encoding="utf-8") as source:
            row_count = max(0, sum(1 for _ in source) - 1)
    record = {
        "schema": "jc2.s56-recert.builder-run/v1",
        "host": socket.gethostname(),
        "started_utc": started_utc,
        "finished_utc": utc_now(),
        "command": command,
        "returncode": result.returncode,
        "timed_out": result.returncode == 124,
        "elapsed_seconds": round(elapsed, 6),
        "resource": parse_time_verbose(timing),
        "meta": str(meta_path.relative_to(ROOT)),
        "meta_sha256": sha256(meta_path),
        "builder": payload["builder"],
        "builder_sha256": sha256(builder),
        "stdout": str(out.relative_to(ROOT)),
        "stdout_sha256": sha256(out),
        "stderr": str(err.relative_to(ROOT)),
        "stderr_sha256": sha256(err),
        "time_file": str(timing.relative_to(ROOT)),
        "time_sha256": sha256(timing) if timing.exists() else None,
        "native_done": "NATIVE_DONE" in text and "? error occurred" not in text,
        "target_gate": "NATIVE_GATE target_xk_level0_nonzero=1" in text,
        "rows_exists": rows_path.exists(),
        "row_count": row_count,
        "rows_sha256": sha256(rows_path) if rows_path.exists() else None,
    }
    json_dump(run_dir / f"{stem}.json", record)
    if record["native_done"] and record["target_gate"] and result.returncode == 0:
        payload["builder_run"] = record
        json_dump(meta_path, payload)
    return record


def read_rows(path: Path) -> list[str]:
    expressions = []
    with path.open(encoding="utf-8") as source:
        header = source.readline().rstrip("\n")
        if header != "source_index|h_power|x_power|y_power|expr":
            raise ValueError(f"unexpected rows header in {path}")
        for line in source:
            if line.strip():
                expressions.append(line.rstrip("\n").split("|", 4)[4])
    return expressions


def coefficient_first(names: Iterable[str]) -> list[str]:
    return sorted(names, key=lambda name: (
        0 if name.startswith("A1_") else
        1 if name.startswith("A2_") else
        2 if name.startswith("A3_") else
        3 if name.startswith("B") else
        4 if name.startswith("h_") else 5,
        name,
    ))


def parse_part_label(payload: dict[str, Any]) -> str:
    return payload["meta"]["partition_label"]


def branch_spec(branch: str, characteristic: int) -> tuple[list[str], str | None, str | None, str]:
    if branch == "none":
        return [], None, None, "full"
    if branch == "q2":
        return ["s2^2-s2+1"], None, None, "q2_faithful_base_change"
    if branch == "q6-coeff":
        if characteristic != 0:
            raise ValueError("q6-coeff is the exact characteristic-zero number-field run")
        q6 = "11*s2^6-33*s2^5+12*s2^4+31*s2^3+12*s2^2-33*s2+11"
        return [], "s2", q6, "q6_old_top_pin_diagnostic_only"
    raise ValueError(branch)


def solve_one(meta_path: Path, characteristic: int, timeout: int, branch: str, singular: Path) -> dict[str, Any]:
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    if "builder_run" not in payload:
        raise RuntimeError("refusing solve without a successful builder run in metadata")
    if payload["source_correction"]["ell"] != 8:
        raise AssertionError("ell correction lost")
    rows_path = ROOT / payload["rows_path"]
    rows = read_rows(rows_path)
    extras, coefficient_variable, minpoly, branch_scope = branch_spec(branch, characteristic)
    variables = coefficient_first(payload["variables"])
    if coefficient_variable is not None:
        if coefficient_variable not in variables:
            raise ValueError("coefficient variable absent")
        variables.remove(coefficient_variable)
    variables.append("T")
    generators = rows + extras + [f"T*({payload['sat']})-1"]
    if coefficient_variable is None:
        prelude = f"ring R={characteristic},({','.join(variables)}),dp;\noption(redSB);\n"
    else:
        prelude = (
            f"ring R=({characteristic},{coefficient_variable}),({','.join(variables)}),dp;\n"
            f"minpoly={minpoly};\noption(redSB);\n"
        )
    label = f"{meta_path.stem}_coefficient_first_{branch}"
    system = gg.SingularSystem(
        name=label,
        prelude=prelude,
        generators=tuple(generators),
        characteristic=characteristic,
        variables=tuple(variables),
        homogeneous=False,
        metadata={},
    )
    suffix = "Q" if characteristic == 0 else f"p{characteristic}"
    output_dir = HERE / "solves" / meta_path.stem / branch / suffix
    started_utc = utc_now()
    result = gg.guided_groebner(
        system,
        policy=gg.PromotionPolicy.exact_q("inhomogeneous completed chart; exact Q required"),
        config=gg.RunConfig(
            output_dir=output_dir,
            timeout_seconds=timeout,
            total_cores=1,
            max_parallel_jobs=1,
            singular=str(singular),
            run_perturbed_control=False,
        ),
    ).to_json()
    run = result["certificate"]["runs"][0]
    stderr_path = Path(run["stderr"])
    resource_files = list(output_dir.glob("*.resource.json"))
    if len(resource_files) != 1:
        raise RuntimeError(f"expected one resource sidecar in {output_dir}, got {len(resource_files)}")
    resource_path = resource_files[0]
    monitored_resource = json.loads(resource_path.read_text(encoding="utf-8"))
    record = {
        "schema": "jc2.s56-recert.solve-run/v1",
        "host": socket.gethostname(),
        "started_utc": started_utc,
        "finished_utc": utc_now(),
        "meta": str(meta_path.relative_to(ROOT)),
        "meta_sha256": sha256(meta_path),
        "builder_sha256": payload["builder_sha256"],
        "rows": payload["rows_path"],
        "rows_sha256": sha256(rows_path),
        "row_count": len(rows),
        "characteristic": characteristic,
        "ring_prelude": prelude,
        "ordered_variables": variables,
        "variable_count_with_T": len(variables),
        "branch": branch,
        "branch_scope": branch_scope,
        "extra_generators": extras,
        "coefficient_variable": coefficient_variable,
        "minpoly": minpoly,
        "saturation": payload["sat"],
        "rabinowitsch": f"T*({payload['sat']})-1",
        "generator_count": len(generators),
        "generator_sha256": hashlib.sha256("\n".join(generators).encode()).hexdigest(),
        "guided_result": result,
        "resource": {
            "process_group_monitor": monitored_resource,
            "gnu_time": parse_time_verbose(stderr_path),
            "sidecar": str(resource_path.relative_to(ROOT)),
            "sidecar_sha256": sha256(resource_path),
        },
        "singular_wrapper": str(singular),
        "singular_wrapper_sha256": sha256(singular),
        "script_sha256_recomputed": sha256(Path(run["script"])),
        "stdout_sha256_recomputed": sha256(Path(run["stdout"])),
        "stderr_sha256_recomputed": sha256(stderr_path),
    }
    json_dump(output_dir / "solve-record.json", record)
    return record


def artifacts_manifest() -> dict[str, Any]:
    manifest = HERE / "artifacts.sha256"
    lines = []
    for path in sorted(HERE.rglob("*")):
        if path.is_file() and path != manifest and not path.name.endswith(".tmp") and "__pycache__" not in path.parts:
            lines.append(f"{sha256(path)}  {path.relative_to(ROOT)}")
    atomic_write(manifest, "\n".join(lines) + "\n")
    return {"files": len(lines), "manifest": str(manifest.relative_to(ROOT)), "sha256": sha256(manifest)}


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("verify-inputs")
    sub.add_parser("inventory-diff")
    emit = sub.add_parser("emit")
    emit.add_argument("--row", choices=sorted(ROWS), required=True)
    emit.add_argument("--part", required=True)
    emit.add_argument("--support", choices=SUPPORTS, required=True)
    emit_all_parser = sub.add_parser("emit-all")
    emit_all_parser.add_argument("--support", choices=SUPPORTS, required=True)
    build = sub.add_parser("build")
    build.add_argument("--meta", type=Path, required=True)
    build.add_argument("--timeout", type=int, default=900)
    solve = sub.add_parser("solve")
    solve.add_argument("--meta", type=Path, required=True)
    solve.add_argument("--char", type=int, required=True)
    solve.add_argument("--timeout", type=int, default=1800)
    solve.add_argument("--branch", choices=("none", "q2", "q6-coeff"), default="none")
    solve.add_argument("--singular", type=Path, default=TIMED_SINGULAR)
    sub.add_parser("manifest")
    args = parser.parse_args()

    if args.cmd == "verify-inputs":
        result: Any = verify_inputs()
    elif args.cmd == "inventory-diff":
        result = inventory_diff()
    elif args.cmd == "emit":
        result = emit_one(args.row, parse_part(args.part), args.support)
    elif args.cmd == "emit-all":
        result = emit_all(args.support)
    elif args.cmd == "build":
        result = run_builder(args.meta.resolve(), args.timeout)
    elif args.cmd == "solve":
        result = solve_one(args.meta.resolve(), args.char, args.timeout, args.branch, args.singular.resolve())
    else:
        result = artifacts_manifest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
