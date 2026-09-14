#!/usr/bin/env python3
"""Bounded, unprojected Singular runs for 99/delta=5/2 and D108 free mean.

The full exact rows come from acyclic_graph_audit_remaining.py.  They are
streamed as primitive integral polynomials; no .sing artifact is produced.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import math
import os
import re
import resource
import signal
import subprocess
import sys
import threading
import time
from collections import deque
from pathlib import Path

from flint import fmpq_mpoly, fmpq_mpoly_ctx


HERE = Path(__file__).resolve().parent
RSS_CAP = 12 * 1024**3
# Polling cannot prevent an allocation between samples.  Stop with explicit
# headroom so every observed aggregate remains below the contractual cap.
RSS_STOP = RSS_CAP - 256 * 1024**2
DEFAULT_SECONDS = 300
OUTPUT_CAP = 2 * 1024**2
IDENT = re.compile(r"\b[A-Za-z_]\w*\b")
EXPECTED = {
    "99-delta52": {
        "input_sha256": "3f81dc99770d235099249a818a55b19f0c828d36109e30aa738995177f97dc46",
        "generator_count": 7583,
        "generator_order_sha256": "774d9263cb704a457810942b1e25aed4c42fdbcae2fb6e83fb9cb962f509f859",
        "graph_count": 7136,
        "row_count": 11606,
        "row_expressions_sha256": "7c3743a6512851df24084bb6d64c3589422f5466c64a1510086660f0fdc7fa42",
        "t2_vector_sha256": "031a1cb74948da83995f6d0d9d561c00fda5e7295e21dbaf88cf0e7d21c9a280",
        "t3_vector_sha256": "2ce824418b57ab57d41704d3f53f45583ca049455040ada2dc588866e2dcbe84",
        "source_residual_rows": 0,
    },
    "108-free-mean": {
        "input_sha256": "1c927d83aa4684ae91bfffc8d03500fbabb73a500faa222fa349a6d129a10814",
        "generator_count": 17815,
        "generator_order_sha256": "2d9f1dc53d03fc1393fc11e723b2f76bdecef4fab359976af38068377f597de4",
        "graph_count": 17308,
        "row_count": 24330,
        "row_expressions_sha256": "ad969715b8cc5e27b8daa224695c14def085bbbdd00db0ea68f97a9416a8d47c",
        "t2_vector_sha256": "17a759e831749505003b2d5d850a29fe7d2692e3f9438d1dc51f3f0e3c44c654",
        "t3_vector_sha256": "b2f336ed92c6f0174cf64931eae379c7290c3933577142af2058485626d25b18",
        "source_residual_rows": 14,
    },
}


def seqsha(items) -> str:
    return hashlib.sha256("".join(str(item) + "\n" for item in items).encode()).hexdigest()


def primitive_expression(expression: str) -> tuple[str, bool]:
    names = sorted(set(IDENT.findall(expression)))
    if not names:
        assert expression in {"0", "0-(0)"}
        return "0", True
    ctx = fmpq_mpoly_ctx.get(tuple(names), "lex")
    poly = fmpq_mpoly(expression.replace("**", "^"), ctx=ctx)
    if not poly:
        return "0", True
    terms = list(poly.terms())
    denominator = 1
    for _, coefficient in terms:
        denominator = math.lcm(denominator, int(coefficient.denominator))
    integral = [(mon, int(coefficient * denominator)) for mon, coefficient in terms]
    common = 0
    for _, coefficient in integral:
        common = math.gcd(common, abs(coefficient))
    common = common or 1
    integral = [(mon, coefficient // common) for mon, coefficient in integral]
    pieces = []
    for mon, coefficient in integral:
        if coefficient == 0:
            continue
        factors = []
        for name, exponent in zip(names, mon):
            if exponent == 1:
                factors.append(name)
            elif exponent > 1:
                factors.append(f"{name}^{exponent}")
        body = "*".join(factors) or "1"
        if abs(coefficient) != 1:
            body = f"{abs(coefficient)}*{body}"
        pieces.append(("+" if coefficient > 0 else "-") + body)
    text = "".join(pieces)
    return (text[1:] if text.startswith("+") else text), False


def child_setup() -> None:
    os.setsid()


def child_rss(pid: int) -> int:
    try:
        status = Path(f"/proc/{pid}/status").read_text()
    except (FileNotFoundError, ProcessLookupError):
        return 0
    match = re.search(r"^VmRSS:\s+(\d+)\s+kB$", status, re.MULTILINE)
    return int(match.group(1)) * 1024 if match else 0


def descendant_pids(pid: int) -> set[int]:
    found = set()
    pending = [pid]
    while pending:
        parent = pending.pop()
        try:
            children = Path(f"/proc/{parent}/task/{parent}/children").read_text().split()
        except (FileNotFoundError, ProcessLookupError):
            continue
        for text in children:
            child = int(text)
            if child not in found:
                found.add(child)
                pending.append(child)
    return found


def run(tag: str) -> dict:
    expected = EXPECTED[tag]
    seconds = int(os.environ.get("T2T3_SINGULAR_SECONDS", DEFAULT_SECONDS))
    total_started = time.monotonic()
    sys.path.insert(0, str(HERE))
    import acyclic_graph_audit_remaining as audit

    build_started = time.monotonic()
    with contextlib.redirect_stdout(io.StringIO()):
        bundle = audit.run(tag, verify_polynomials=False)
    build_seconds = time.monotonic() - build_started
    rows = bundle["rows"]
    graph = bundle["graph"]
    all_names = bundle["all_names"]
    record = bundle["record"]
    spec = bundle["spec"]
    assert record["input_sha256"] == expected["input_sha256"]
    assert len(all_names) == expected["generator_count"]
    assert seqsha(all_names) == expected["generator_order_sha256"]
    assert len(graph) == expected["graph_count"]
    assert len(rows) == expected["row_count"]
    assert seqsha(expression for _, expression, _, _ in rows) == expected["row_expressions_sha256"]
    assert record["T2_face_vector_sha256"] == expected["t2_vector_sha256"]
    assert record["T3_face_vector_sha256"] == expected["t3_vector_sha256"]
    source_residuals = [row for row in rows if row[2] == "source_residual"]
    assert len(source_residuals) == expected["source_residual_rows"]
    if tag == "108-free-mean":
        assert "minor_mean" in all_names
        assert not any(expression in {"minor_mean", "minor_mean-(0)"} for _, expression, _, _ in rows)

    # A one-slot perturbation must not pass the independent target-vector hash.
    t3_vector = [
        math.comb(spec["t3p"], z - spec["t3z"])
        if spec["t3z"] <= z <= spec["D3"] else 0
        for z in range(spec["D3"] + 1)
    ]
    assert seqsha(t3_vector) == expected["t3_vector_sha256"]
    t3_vector[spec["t3z"]] += 1
    assert seqsha(t3_vector) != expected["t3_vector_sha256"]

    # Link every emitted face equation to an independently constructed target
    # vector.  This audits the actual row suffix, not merely its label or DAG
    # leading coordinate.
    t2_vector = [
        math.comb(spec["t2p"], z - spec["t2z"])
        if spec["t2z"] <= z <= spec["D2"] else 0
        for z in range(spec["D2"] + 1)
    ]
    assert seqsha(t2_vector) == expected["t2_vector_sha256"]
    t2_faces = {int(label.rsplit("_", 1)[1]): expression for label, expression, block, _ in rows if block == "T2_face"}
    assert set(t2_faces) == set(range(spec["D2"] + 1))
    for z, coefficient in enumerate(t2_vector):
        target = f"{coefficient}*{spec['lam2']}" if coefficient else "0"
        assert t2_faces[z] == f"xQ_0_{z}-({target})"
    t3_faces = {int(label.rsplit("_", 1)[1]): expression for label, expression, block, _ in rows if block == "T3_face"}
    assert set(range(spec["D3"] + 1)) <= set(t3_faces)
    actual_t3_vector = []
    for z in range(spec["D3"] + 1):
        coefficient = math.comb(spec["t3p"], z - spec["t3z"]) if spec["t3z"] <= z <= spec["D3"] else 0
        target = f"{coefficient}*lambda3" if coefficient else "0"
        assert t3_faces[z].endswith(f"-({target})")
        actual_t3_vector.append(coefficient)
    assert seqsha(actual_t3_vector) == expected["t3_vector_sha256"]
    for z in set(t3_faces) - set(range(spec["D3"] + 1)):
        assert t3_faces[z].endswith("-(0)")

    graph_rows = [row for row in rows if row[3] is not None]
    constraints = [row for row in rows if row[3] is None]
    by_pivot = {row[3]: row for row in graph_rows}
    assert len(by_pivot) == len(graph)
    graph_order = list(reversed(graph))
    base_order = [name for name in all_names if name not in by_pivot]
    ring_names = graph_order + base_order
    assert len(ring_names) == len(set(ring_names)) == expected["generator_count"]
    place = {name: idx for idx, name in enumerate(ring_names)}
    ordered_graph = [by_pivot[name] for name in graph_order]
    for _, expression, _, pivot in ordered_graph:
        dependencies = set(IDENT.findall(expression)) - {pivot}
        assert all(place[pivot] < place[name] for name in dependencies)
    ordered_rows = ordered_graph + constraints

    lam2, zlam2, sep, zsep = [spec[key] for key in ["lam2", "zlam2", "sep", "zsep"]]
    result_path = HERE / f"singular-full-graph-{tag}.result.json"
    state = {
        "reason": None, "peak_child_rss": 0, "peak_parent_rss": 0,
        "peak_aggregate_rss": 0, "output_bytes": 0,
    }
    output_head = []
    output_tail = deque(maxlen=2000)
    lock = threading.Lock()
    started = time.monotonic()
    proc = subprocess.Popen(
        ["Singular", "-q", "--no-rc", "--no-warn", "--no-shell", "--threads=1", "--flint-threads=1"],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, bufsize=1, preexec_fn=child_setup,
    )

    def stop(reason: str) -> None:
        with lock:
            if state["reason"] is not None:
                return
            state["reason"] = reason
        try:
            os.killpg(proc.pid, signal.SIGTERM)
        except ProcessLookupError:
            return
        time.sleep(0.25)
        if proc.poll() is None:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass

    def read_output() -> None:
        assert proc.stdout is not None
        head_chars = 0
        for line in proc.stdout:
            with lock:
                state["output_bytes"] += len(line.encode())
                if head_chars < 131072:
                    output_head.append(line)
                    head_chars += len(line)
                output_tail.append(line)
                overflow = state["output_bytes"] > OUTPUT_CAP
            if overflow:
                stop("OUTPUT_CAP")
                return

    def monitor() -> None:
        while proc.poll() is None:
            parent_rss = child_rss(os.getpid())
            descendants = descendant_pids(os.getpid())
            child_total = sum(child_rss(pid) for pid in descendants)
            aggregate = parent_rss + child_total
            with lock:
                state["peak_child_rss"] = max(state["peak_child_rss"], child_total)
                state["peak_parent_rss"] = max(state["peak_parent_rss"], parent_rss)
                state["peak_aggregate_rss"] = max(state["peak_aggregate_rss"], aggregate)
            if aggregate >= RSS_STOP:
                stop("AGGREGATE_RSS_CAP")
                return
            if time.monotonic() - started > seconds:
                stop("TIME_CAP")
                return
            time.sleep(0.05)

    reader = threading.Thread(target=read_output, daemon=True)
    watcher = threading.Thread(target=monitor, daemon=True)
    reader.start()
    watcher.start()
    streamed_rows = streamed_bytes = canonical_zeros = 0
    write_error = None
    try:
        assert proc.stdin is not None
        header = f"ring R=0,({','.join(ring_names)}),lp;\noption(redSB);\nideal I=\n"
        proc.stdin.write(header)
        streamed_bytes += len(header.encode())
        for idx, (_, expression, _, _) in enumerate(ordered_rows):
            text, zero = primitive_expression(expression)
            canonical_zeros += int(zero)
            chunk = ("" if idx == 0 else ",\n") + text
            proc.stdin.write(chunk)
            streamed_bytes += len(chunk.encode())
            streamed_rows += 1
            if idx % 64 == 0:
                proc.stdin.flush()
        trailer = f''';
print("ALL_ROWS_PARSED");
print("FACE_TARGET_LINK_CHECK"); print(1);
int graphOK=1;
for (int gi=1; gi<={len(graph_order)}; gi++) {{ if (leadmonom(I[gi])!=var(gi)) {{ graphOK=0; }} }}
print("LEADING_TARGET_CHECK"); print(graphOK);
print("BEGIN_GB"); ideal SB=std(I); print("END_GB");
print("BEGIN_RESULT"); print(reduce(1,SB)); print(dim(SB)); print(size(SB)); print("END_RESULT");
ideal n2={lam2},{zlam2}*{lam2}-1; ideal p2={lam2}-1,{zlam2}*{lam2}-1;
ideal n3=lambda3,Z3*lambda3-1; ideal p3=lambda3-1,Z3*lambda3-1;
ideal ns={sep},{zsep}*{sep}-1; ideal ps={sep}-1,{zsep}*{sep}-1;
print("BEGIN_CONTROLS");
print("CTRL_T2_NEG"); print(reduce(1,std(n2))); print("CTRL_T2_POS"); print(reduce(1,std(p2)));
print("CTRL_T3_NEG"); print(reduce(1,std(n3))); print("CTRL_T3_POS"); print(reduce(1,std(p3)));
print("CTRL_SEP_NEG"); print(reduce(1,std(ns))); print("CTRL_SEP_POS"); print(reduce(1,std(ps)));
ring C=0,(b,a,c,d,lam,zlam,r,u,v,w),lp;
ideal coneLead=b+3r,a-2u+3w,c+r^3+r*u-3r*w-2v,d-r^2*u-3r*v-u^2+4u*w-3w^2;
ideal coneNeg=coneLead,lam,zlam*lam-1; ideal conePos=coneLead,lam-1,zlam*lam-1;
print("CTRL_CONE_NEG"); print(reduce(1,std(coneNeg))); print("CTRL_CONE_POS"); print(reduce(1,std(conePos)));
print("END_CONTROLS"); quit;
'''
        proc.stdin.write(trailer)
        proc.stdin.flush()
        proc.stdin.close()
        streamed_bytes += len(trailer.encode())
    except (BrokenPipeError, OSError) as exc:
        write_error = repr(exc)
        try:
            proc.stdin.close()
        except Exception:
            pass
    proc.wait()
    reader.join(timeout=5)
    watcher.join(timeout=1)
    elapsed = time.monotonic() - started
    output = "".join(output_head)
    if state["output_bytes"] > 131072:
        output += "\n[...OUTPUT TRUNCATED IN RESULT...]\n" + "".join(output_tail)
    if state["reason"] is None and proc.returncode == 14 and "no more memory" in output:
        state["reason"] = "SINGULAR_ALLOCATOR_FAILURE_NO_RLIMIT"
    markers = ["ALL_ROWS_PARSED", "FACE_TARGET_LINK_CHECK", "LEADING_TARGET_CHECK", "BEGIN_GB", "END_GB", "BEGIN_RESULT", "END_RESULT", "BEGIN_CONTROLS", "END_CONTROLS"]
    marker_counts = {marker: output.count(marker) for marker in markers}

    def between(begin, end):
        if begin not in output or end not in output:
            return []
        return [line.strip() for line in output.split(begin, 1)[1].split(end, 1)[0].splitlines() if line.strip()]

    result_lines = between("BEGIN_RESULT", "END_RESULT")
    control_lines = between("BEGIN_CONTROLS", "END_CONTROLS")
    expected_controls = ["CTRL_T2_NEG", "0", "CTRL_T2_POS", "1", "CTRL_T3_NEG", "0", "CTRL_T3_POS", "1", "CTRL_SEP_NEG", "0", "CTRL_SEP_POS", "1", "CTRL_CONE_NEG", "0", "CTRL_CONE_POS", "1"]
    controls_ok = control_lines == expected_controls
    face_link_ok = between("FACE_TARGET_LINK_CHECK", "LEADING_TARGET_CHECK") == ["1"]
    leading_ok = between("LEADING_TARGET_CHECK", "BEGIN_GB") == ["1"]
    diagnostic_lines = [
        line for line in output.splitlines()
        if "?" in line or re.search(r"\b(error|warning|halt|diagnostic)\b", line, re.IGNORECASE)
    ]
    strict_markers = proc.returncode == 0 and state["reason"] is None and not diagnostic_lines and all(count == 1 for count in marker_counts.values())
    exact_result_shape = len(result_lines) == 3 and all(re.fullmatch(r"-?\d+", line) for line in result_lines)
    if strict_markers and face_link_ok and leading_ok and controls_ok and exact_result_shape and result_lines[0] == "0":
        decision = "UNIT"
    elif strict_markers and face_link_ok and leading_ok and controls_ok and exact_result_shape and result_lines[0] != "0" and int(result_lines[1]) >= 0:
        decision = "PROPER"
    else:
        decision = "COMPUTE_BOUND_OPEN"
    result = {
        "case": tag, "decision": decision, "field": "Q", "ordering": "lp",
        "generator_count": len(ring_names), "graph_generator_count": len(graph_order),
        "row_count": len(ordered_rows), "source_residual_rows_preserved": len(source_residuals),
        "free_mean_preserved": tag != "108-free-mean" or "minor_mean" in base_order,
        "streamed_row_count": streamed_rows, "streamed_input_bytes": streamed_bytes,
        "canonical_zero_rows_streamed": canonical_zeros,
        "integer_primitive_nonzero_rows": True,
        "reverse_acyclic_order_host_check": True,
        "target_vectors_host_check": True, "emitted_face_rows_target_link_host_check": True,
        "perturbed_target_rejected_host_check": True,
        "child_RLIMIT_AS": None, "rss_monitor_scope": "driver plus all descendants",
        "rss_monitor_cap_bytes": RSS_CAP, "rss_stop_threshold_bytes": RSS_STOP,
        "time_cap_seconds": seconds, "build_seconds": round(build_seconds, 3),
        "singular_wall_seconds": round(elapsed, 3),
        "total_driver_wall_seconds": round(time.monotonic() - total_started, 3),
        "peak_child_tree_RSS_bytes": state["peak_child_rss"],
        "peak_child_tree_RSS_MiB": round(state["peak_child_rss"] / 1024**2, 3),
        "peak_driver_RSS_bytes": state["peak_parent_rss"],
        "peak_driver_RSS_MiB": round(state["peak_parent_rss"] / 1024**2, 3),
        "peak_aggregate_RSS_bytes": state["peak_aggregate_rss"],
        "peak_aggregate_RSS_MiB": round(state["peak_aggregate_rss"] / 1024**2, 3),
        "termination_reason": state["reason"], "returncode": proc.returncode,
        "write_error": write_error, "output_bytes": state["output_bytes"],
        "marker_counts": marker_counts, "result_lines": result_lines,
        "controls_lines": control_lines, "face_target_link_singular_marker": face_link_ok,
        "leading_target_singular_check": leading_ok, "diagnostic_lines": diagnostic_lines,
        "exact_three_result_lines": exact_result_shape,
        "controls_ok": controls_ok,
        "strict_completion": strict_markers and face_link_ok and leading_ok and controls_ok and exact_result_shape,
        "singular_output": output,
        "audit_driver_sha256": hashlib.sha256(Path(audit.__file__).read_bytes()).hexdigest(),
        "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if tag == "108-free-mean":
        result["superseded_harness_attempts"] = [
            {
                "classification": "HARNESS_FAILURE_NOT_BRANCH_VERDICT",
                "returncode": 134,
                "reason": "FLINT allocation failure after RLIMIT_AS was mistakenly applied to the Python audit process; no Singular child was launched",
                "observed_python_RSS_MiB_before_failure": 3577.934,
            },
            {
                "classification": "AS_LIMITED_NOT_RSS_CAPPED_NOT_BRANCH_VERDICT",
                "returncode": 14,
                "reason": "Singular no-more-memory under RLIMIT_AS before ALL_ROWS_PARSED",
                "singular_wall_seconds": 56.901,
                "peak_child_RSS_MiB": 12077.273,
                "streamed_row_count": 3874,
            },
        ]
    result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", required=True, choices=sorted(EXPECTED))
    args = parser.parse_args()
    outcome = run(args.case)
    raise SystemExit(0 if outcome["decision"] in {"UNIT", "PROPER"} else 2)
