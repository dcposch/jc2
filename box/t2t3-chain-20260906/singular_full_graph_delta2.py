#!/usr/bin/env python3
"""Stream the full exact-Q 99/delta=2 T2+T3 incidence chart to Singular.

The rows are imported verbatim (as polynomials) from acyclic_graph_audit.py.
No incidence variable is projected out.  Reversing the audited acyclic graph
order before the base variables makes the graph coordinate the lexicographic
leading monomial of every graph row.  Rows are cleared to primitive integer
form while being streamed, so no large .sing input artifact is written.
"""
from __future__ import annotations

import contextlib
import hashlib
import importlib
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


HERE = Path(__file__).resolve().parent
RESULT = HERE / "singular-full-graph-delta2.result.json"
AS_CAP = 12 * 1024**3
DEFAULT_SECONDS = 300
OUTPUT_CAP = 2 * 1024**2
IDENT = re.compile(r"\b[A-Za-z_]\w*\b")

EXPECTED = {
    "input_sha256": "778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea",
    "row_expressions_sha256": "5dadaff4326b065929b6171ce040f95685569ca8c05e100d5fcefba0dd39034e",
    "generator_order_sha256": "403154ab65f694c3c4bbc1a5b3051adbc7d9aeae2e556698ec97e350851646a5",
    "t2_vector_sha256": "031a1cb74948da83995f6d0d9d561c00fda5e7295e21dbaf88cf0e7d21c9a280",
    "t3_vector_sha256": "2ce824418b57ab57d41704d3f53f45583ca049455040ada2dc588866e2dcbe84",
}


def seqsha(items) -> str:
    return hashlib.sha256("".join(str(x) + "\n" for x in items).encode()).hexdigest()


def primitive(poly, local_index) -> str:
    """Serialize an fmpq_mpoly as a primitive polynomial over Z."""
    if poly is None or not poly:
        return "0"
    local_names = [None] * len(local_index)
    for name, idx in local_index.items():
        local_names[idx] = name
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
    # Deterministic local-lex display.  Multiplication by -1 is harmless, but
    # leave the audited graph pivot positive whenever it was positive.
    pieces = []
    for mon, coefficient in integral:
        if not coefficient:
            continue
        factors = []
        for name, exponent in zip(local_names, mon):
            if exponent == 1:
                factors.append(name)
            elif exponent > 1:
                factors.append(f"{name}^{exponent}")
        body = "*".join(factors) or "1"
        magnitude = abs(coefficient)
        if magnitude != 1:
            body = f"{magnitude}*{body}"
        pieces.append(("+" if coefficient > 0 else "-") + body)
    ans = "".join(pieces)
    return ans[1:] if ans.startswith("+") else ans


def set_limits() -> None:
    resource.setrlimit(resource.RLIMIT_AS, (AS_CAP, AS_CAP))
    os.setsid()


def rss_bytes(pid: int) -> int:
    try:
        text = Path(f"/proc/{pid}/status").read_text()
    except (FileNotFoundError, ProcessLookupError):
        return 0
    match = re.search(r"^VmRSS:\s+(\d+)\s+kB$", text, re.MULTILINE)
    return int(match.group(1)) * 1024 if match else 0


def main() -> int:
    seconds = int(os.environ.get("T2T3_SINGULAR_SECONDS", DEFAULT_SECONDS))
    # Bound the Python/FLINT audit build as well as the Singular child.
    resource.setrlimit(resource.RLIMIT_AS, (AS_CAP, AS_CAP))
    build_started = time.monotonic()
    sys.path.insert(0, str(HERE))
    # The audited module prints its record; suppress that duplicate here.
    with contextlib.redirect_stdout(io.StringIO()):
        audit = importlib.import_module("acyclic_graph_audit")
    build_seconds = time.monotonic() - build_started

    assert hashlib.sha256(audit.INPUT.read_bytes()).hexdigest() == EXPECTED["input_sha256"]
    assert seqsha(expression for _, expression, _, _ in audit.rows) == EXPECTED["row_expressions_sha256"]
    assert seqsha(audit.all_names) == EXPECTED["generator_order_sha256"]
    t2 = [math.comb(15, z - 40) if 40 <= z <= 55 else 0 for z in range(56)]
    t3 = [math.comb(40, z - 105) if 105 <= z <= 145 else 0 for z in range(146)]
    assert seqsha(t2) == EXPECTED["t2_vector_sha256"]
    assert seqsha(t3) == EXPECTED["t3_vector_sha256"]
    perturbed = t3.copy()
    perturbed[105] += 1
    assert seqsha(perturbed) != EXPECTED["t3_vector_sha256"]

    graph_rows = [item for item in audit.rows if item[3] is not None]
    constraints = [item for item in audit.rows if item[3] is None]
    assert len(graph_rows) == len(audit.graph) == 7136
    by_pivot = {pivot: item for item in graph_rows for pivot in [item[3]]}
    graph_order = list(reversed(audit.graph))
    base_order = [name for name in audit.all_names if name not in by_pivot]
    ring_names = graph_order + base_order
    assert len(ring_names) == len(set(ring_names)) == 7585
    place = {name: i for i, name in enumerate(ring_names)}
    ordered_graph_rows = [by_pivot[name] for name in graph_order]
    # Mechanical global-lp leading-target audit before invoking Singular.
    for _, expression, _, pivot in ordered_graph_rows:
        dependencies = set(IDENT.findall(expression)) - {pivot}
        assert all(place[pivot] < place[name] for name in dependencies), (pivot, dependencies)

    row_lookup = {id(row): parsed for row, parsed in zip(audit.rows, audit.parsed)}
    ordered = ordered_graph_rows + constraints
    state = {"reason": None, "peak_rss": 0, "output_bytes": 0}
    output_head = []
    output_tail = deque(maxlen=2000)
    lock = threading.Lock()
    run_started = time.monotonic()
    proc = subprocess.Popen(
        ["Singular", "-q", "--no-rc", "--no-warn", "--no-shell", "--threads=1", "--flint-threads=1"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        preexec_fn=set_limits,
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

    def reader() -> None:
        assert proc.stdout is not None
        for line in proc.stdout:
            encoded = len(line.encode())
            with lock:
                state["output_bytes"] += encoded
                if sum(len(x) for x in output_head) < 131072:
                    output_head.append(line)
                output_tail.append(line)
                too_much = state["output_bytes"] > OUTPUT_CAP
            if too_much:
                stop("OUTPUT_CAP")
                return

    def monitor() -> None:
        while proc.poll() is None:
            got = rss_bytes(proc.pid)
            with lock:
                state["peak_rss"] = max(state["peak_rss"], got)
            if got > AS_CAP:
                stop("RSS_CAP")
                return
            if time.monotonic() - run_started > seconds:
                stop("TIME_CAP")
                return
            time.sleep(0.2)

    reader_thread = threading.Thread(target=reader, daemon=True)
    monitor_thread = threading.Thread(target=monitor, daemon=True)
    reader_thread.start()
    monitor_thread.start()
    streamed_rows = 0
    streamed_bytes = 0
    write_error = None
    try:
        assert proc.stdin is not None
        header = f"ring R=0,({','.join(ring_names)}),lp;\noption(redSB);\nideal I=\n"
        proc.stdin.write(header)
        streamed_bytes += len(header.encode())
        for i, row in enumerate(ordered):
            polynomial, _, local_index = row_lookup[id(row)]
            text = primitive(polynomial, local_index)
            chunk = ("" if i == 0 else ",\n") + text
            proc.stdin.write(chunk)
            streamed_bytes += len(chunk.encode())
            streamed_rows += 1
            if i % 64 == 0:
                proc.stdin.flush()
        trailer = f''';
print("ALL_ROWS_PARSED");
int graphOK=1;
for (int gi=1; gi<={len(graph_order)}; gi++) {{ if (leadmonom(I[gi])!=var(gi)) {{ graphOK=0; }} }}
print("LEADING_TARGET_CHECK"); print(graphOK);
print("BEGIN_GB");
ideal SB=std(I);
print("END_GB");
print("BEGIN_RESULT"); print(reduce(1,SB)); print(dim(SB)); print(size(SB)); print("END_RESULT");
ideal n2=leader55,Z55*leader55-1; ideal p2=leader55-1,Z55*leader55-1;
ideal n3=lambda3,Z3*lambda3-1; ideal p3=lambda3-1,Z3*lambda3-1;
ideal ns=rho,Zrho*rho-1; ideal ps=rho-1,Zrho*rho-1;
print("BEGIN_CONTROLS");
print("CTRL_T2_NEG"); print(reduce(1,std(n2))); print("CTRL_T2_POS"); print(reduce(1,std(p2)));
print("CTRL_T3_NEG"); print(reduce(1,std(n3))); print("CTRL_T3_POS"); print(reduce(1,std(p3)));
print("CTRL_SEP_NEG"); print(reduce(1,std(ns))); print("CTRL_SEP_POS"); print(reduce(1,std(ps)));
ring C=0,(b,a,c,d,lam,zlam,r,u,v,w),lp;
ideal coneLead=b+3r,a-2u+3w,c+r^3+r*u-3r*w-2v,d-r^2*u-3r*v-u^2+4u*w-3w^2;
ideal coneNeg=coneLead,lam,zlam*lam-1; ideal conePos=coneLead,lam-1,zlam*lam-1;
print("CTRL_CONE_NEG"); print(reduce(1,std(coneNeg))); print("CTRL_CONE_POS"); print(reduce(1,std(conePos)));
print("END_CONTROLS");
quit;
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
    reader_thread.join(timeout=5)
    monitor_thread.join(timeout=1)
    elapsed = time.monotonic() - run_started
    output = "".join(output_head)
    if state["output_bytes"] > 131072:
        output += "\n[...OUTPUT TRUNCATED IN RESULT...]\n" + "".join(output_tail)
    markers = [
        "ALL_ROWS_PARSED", "LEADING_TARGET_CHECK", "BEGIN_GB", "END_GB",
        "BEGIN_RESULT", "END_RESULT", "BEGIN_CONTROLS", "END_CONTROLS",
    ]
    marker_counts = {marker: output.count(marker) for marker in markers}

    def between(begin, end):
        if begin not in output or end not in output:
            return []
        body = output.split(begin, 1)[1].split(end, 1)[0]
        return [line.strip() for line in body.splitlines() if line.strip()]

    result_lines = between("BEGIN_RESULT", "END_RESULT")
    controls = between("BEGIN_CONTROLS", "END_CONTROLS")
    # RLIMIT_AS is enforced by the kernel; Singular reports its own allocation
    # failure and exits 14 before the polling thread can observe RSS > cap.
    if state["reason"] is None and proc.returncode == 14 and "no more memory" in output:
        state["reason"] = "RLIMIT_AS_MEMORY"
    strict = proc.returncode == 0 and state["reason"] is None and all(value == 1 for value in marker_counts.values())
    leading_ok = between("LEADING_TARGET_CHECK", "BEGIN_GB") == ["1"]
    expected_controls = [
        "CTRL_T2_NEG", "0", "CTRL_T2_POS", "1",
        "CTRL_T3_NEG", "0", "CTRL_T3_POS", "1",
        "CTRL_SEP_NEG", "0", "CTRL_SEP_POS", "1",
        "CTRL_CONE_NEG", "0", "CTRL_CONE_POS", "1",
    ]
    controls_ok = controls == expected_controls
    if strict and leading_ok and controls_ok and len(result_lines) >= 3 and result_lines[0] == "0":
        decision = "UNIT"
    elif strict and leading_ok and controls_ok and len(result_lines) >= 3 and result_lines[0] != "0" and int(result_lines[1]) >= 0:
        decision = "PROPER"
    else:
        decision = "COMPUTE_BOUND_OPEN"
    record = {
        "case": "99-delta2",
        "decision": decision,
        "field": "Q",
        "ordering": "lp",
        "generator_count": len(ring_names),
        "graph_generator_count": len(graph_order),
        "row_count": len(ordered),
        "streamed_row_count": streamed_rows,
        "streamed_input_bytes": streamed_bytes,
        "integer_primitive_nonzero_rows": True,
        "canonical_zero_rows": sum(parsed[0] is None or not parsed[0] for parsed in audit.parsed),
        "reverse_acyclic_order_host_check": True,
        "target_vectors_host_check": True,
        "perturbed_target_rejected_host_check": True,
        "child_RLIMIT_AS_bytes": AS_CAP,
        "rss_monitor_cap_bytes": AS_CAP,
        "time_cap_seconds": seconds,
        "build_seconds": round(build_seconds, 3),
        "singular_wall_seconds": round(elapsed, 3),
        "peak_child_RSS_bytes": state["peak_rss"],
        "peak_child_RSS_MiB": round(state["peak_rss"] / 1024**2, 3),
        "termination_reason": state["reason"],
        "returncode": proc.returncode,
        "write_error": write_error,
        "output_bytes": state["output_bytes"],
        "marker_counts": marker_counts,
        "result_lines": result_lines,
        "controls_lines": controls,
        "leading_target_singular_check": leading_ok,
        "controls_ok": controls_ok,
        "strict_completion": strict and leading_ok and controls_ok,
        "singular_output": output,
        "driver_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps(record, indent=2, sort_keys=True), flush=True)
    return 0 if decision in {"UNIT", "PROPER"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
