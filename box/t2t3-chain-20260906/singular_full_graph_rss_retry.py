#!/usr/bin/env python3
"""Strict RSS-capped exact-Q retries for the two (99,66) T2+T3 charts.

This runner intentionally sets no address-space limit.  It streams the complete
audited graph presentation to a one-thread local Singular process and monitors
the aggregate resident memory of this Python builder plus the Singular process
tree.  The 12-GiB cap has a small polling safety margin.  Existing audit and run
receipts are never overwritten.
"""
from __future__ import annotations

import argparse
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

from flint import fmpq_mpoly, fmpq_mpoly_ctx


HERE = Path(__file__).resolve().parent
RSS_CAP = 12 * 1024**3
RSS_SAFETY_MARGIN = 128 * 1024**2
RSS_KILL_THRESHOLD = RSS_CAP - RSS_SAFETY_MARGIN
RSS_POLL_SECONDS = 0.05
DEFAULT_SECONDS = 300
OUTPUT_CAP = 512 * 1024
OUTPUT_RETAIN_HEAD = 128 * 1024
OUTPUT_RETAIN_TAIL_LINES = 2000
IDENT = re.compile(r"\b[A-Za-z_]\w*\b")
INTEGER = re.compile(r"^-?\d+$")

CASES = {
    "99-delta2": {
        "audit_module": "acyclic_graph_audit",
        "audit_driver_sha256": "bc83ab1560f418038c7cc26cca003c45fb51ac8745ef2ae4cb5d257438ba6ca4",
        "audit_receipt": "acyclic-graph-delta2.json",
        "input_sha256": "778eda933ee9b2acbad20f6dc862c25db94776cb25ffd5782646427a3b63e1ea",
        "generator_count": 7585,
        "generator_order_sha256": "403154ab65f694c3c4bbc1a5b3051adbc7d9aeae2e556698ec97e350851646a5",
        "graph_count": 7136,
        "row_count": 11606,
        "row_expressions_sha256": "5dadaff4326b065929b6171ce040f95685569ca8c05e100d5fcefba0dd39034e",
        "t2_vector_sha256": "031a1cb74948da83995f6d0d9d561c00fda5e7295e21dbaf88cf0e7d21c9a280",
        "t3_vector_sha256": "2ce824418b57ab57d41704d3f53f45583ca049455040ada2dc588866e2dcbe84",
        "D2": 55,
        "D3": 145,
        "t2z": 40,
        "t2p": 15,
        "t3z": 105,
        "t3p": 40,
        "lam2": "leader55",
        "zlam2": "Z55",
        "sep": "rho",
        "zsep": "Zrho",
    },
    "99-delta52": {
        "audit_module": "acyclic_graph_audit_remaining",
        "audit_driver_sha256": "ef65a942c99a7d37d317438b8d5c3b013095c1c3c1c892d0c64073c4421d52ae",
        "audit_receipt": "acyclic-graph-delta52.json",
        "input_sha256": "3f81dc99770d235099249a818a55b19f0c828d36109e30aa738995177f97dc46",
        "generator_count": 7583,
        "generator_order_sha256": "774d9263cb704a457810942b1e25aed4c42fdbcae2fb6e83fb9cb962f509f859",
        "graph_count": 7136,
        "row_count": 11606,
        "row_expressions_sha256": "7c3743a6512851df24084bb6d64c3589422f5466c64a1510086660f0fdc7fa42",
        "t2_vector_sha256": "031a1cb74948da83995f6d0d9d561c00fda5e7295e21dbaf88cf0e7d21c9a280",
        "t3_vector_sha256": "2ce824418b57ab57d41704d3f53f45583ca049455040ada2dc588866e2dcbe84",
        "D2": 55,
        "D3": 145,
        "t2z": 40,
        "t2p": 15,
        "t3z": 105,
        "t3p": 40,
        "lam2": "leader55",
        "zlam2": "Z55",
        "sep": "c",
        "zsep": "Zc",
    },
}

DIAGNOSTIC_PATTERNS = [
    re.compile(r"^\s*\?"),
    re.compile(r"//\s*\*{2,}"),
    re.compile(r"\b(?:error occurred|syntax error|parse error|wrong type|not defined)\b", re.I),
    re.compile(r"\b(?:fatal|segmentation fault|no more memory|out of memory|killed|abort(?:ed)?)\b", re.I),
]


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def seqsha(items) -> str:
    return hashlib.sha256("".join(str(item) + "\n" for item in items).encode()).hexdigest()


def rational_text(value) -> str:
    numerator = int(value.numerator)
    denominator = int(value.denominator)
    return str(numerator) if denominator == 1 else f"({numerator}/{denominator})"


def parse_local(expression: str):
    names = sorted(set(IDENT.findall(expression)))
    if not names:
        assert expression in {"0", "0-(0)"}
        return None, None, {}
    ctx = fmpq_mpoly_ctx.get(tuple(names), "lex")
    return fmpq_mpoly(expression.replace("**", "^"), ctx=ctx), ctx, {name: i for i, name in enumerate(names)}


def primitive_poly(poly, local_index) -> tuple[str, bool]:
    """Serialize an exact FLINT polynomial as primitive integral Singular text."""
    if poly is None or not poly:
        return "0", True
    local_names = [None] * len(local_index)
    for name, index in local_index.items():
        local_names[index] = name
    terms = list(poly.terms())
    denominator = 1
    for _, coefficient in terms:
        denominator = math.lcm(denominator, int(coefficient.denominator))
    integral = [(monomial, int(coefficient * denominator)) for monomial, coefficient in terms]
    content = 0
    for _, coefficient in integral:
        content = math.gcd(content, abs(coefficient))
    content = content or 1
    pieces = []
    for monomial, coefficient in integral:
        coefficient //= content
        if coefficient == 0:
            continue
        factors = []
        for name, exponent in zip(local_names, monomial):
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


def primitive_expression(expression: str) -> tuple[str, bool]:
    poly, _, local_index = parse_local(expression)
    return primitive_poly(poly, local_index)


def pure_variable_coefficient(poly, local_index, variable: str):
    """Return coefficient of a variable and reject every non-linear occurrence."""
    if variable not in local_index or poly is None:
        return 0
    position = local_index[variable]
    answer = 0
    for monomial, coefficient in poly.terms():
        if monomial[position] == 0:
            continue
        assert monomial[position] == 1 and sum(monomial) == 1, (variable, monomial)
        answer += coefficient
    return answer


@contextlib.contextmanager
def preserve_receipt(path: Path):
    """Suppress a builder's historical receipt write and prove byte preservation."""
    before = path.read_bytes()
    before_stat = path.stat()
    original = Path.write_text

    def guarded(self, data, *args, **kwargs):
        if self.resolve() == path.resolve():
            return len(data)
        return original(self, data, *args, **kwargs)

    Path.write_text = guarded
    try:
        yield sha_bytes(before)
    finally:
        Path.write_text = original
        assert path.read_bytes() == before
        after_stat = path.stat()
        assert (after_stat.st_mtime_ns, after_stat.st_size) == (before_stat.st_mtime_ns, before_stat.st_size)


def load_case(tag: str):
    spec = CASES[tag]
    audit_path = HERE / f"{spec['audit_module']}.py"
    assert sha_file(audit_path) == spec["audit_driver_sha256"]
    receipt_path = HERE / spec["audit_receipt"]
    with preserve_receipt(receipt_path) as receipt_sha256:
        with contextlib.redirect_stdout(io.StringIO()):
            audit = importlib.import_module(spec["audit_module"])
            if tag == "99-delta2":
                rows = audit.rows
                graph = audit.graph
                all_names = audit.all_names
                input_sha256 = sha_file(audit.INPUT)
                parsed_by_id = {id(row): parsed for row, parsed in zip(rows, audit.parsed)}

                def serializer(row):
                    polynomial, _, local_index = parsed_by_id[id(row)]
                    return primitive_poly(polynomial, local_index)
            else:
                bundle = audit.run(tag, verify_polynomials=False)
                rows = bundle["rows"]
                graph = bundle["graph"]
                all_names = bundle["all_names"]
                input_sha256 = bundle["record"]["input_sha256"]

                def serializer(row):
                    return primitive_expression(row[1])

    assert sha_file(receipt_path) == receipt_sha256
    return audit, rows, graph, all_names, input_sha256, serializer, receipt_sha256


def proportional_factor(original, emitted, local_index):
    """Prove two local polynomials differ by one nonzero rational scalar."""
    assert original is not None and original
    assert emitted is not None and emitted
    original_terms = dict(original.terms())
    emitted_terms = dict(emitted.terms())
    assert set(original_terms) == set(emitted_terms)
    first = next(iter(original_terms))
    factor = emitted_terms[first] / original_terms[first]
    assert factor
    assert all(emitted_terms[monomial] == factor * coefficient for monomial, coefficient in original_terms.items())
    return factor


def audit_attained_target_rows(rows, ordered_rows, serializer, spec: dict):
    """Independently audit complete targets in the exact rows actually streamed."""
    position = {id(row): index for index, row in enumerate(ordered_rows, 1)}
    by_label = {row[0]: row for row in rows}
    assert len(by_label) == len(rows)
    t2_vector = [
        math.comb(spec["t2p"], z - spec["t2z"])
        if spec["t2z"] <= z <= spec["D2"] else 0
        for z in range(spec["D2"] + 1)
    ]
    t3_vector = [
        math.comb(spec["t3p"], z - spec["t3z"])
        if spec["t3z"] <= z <= spec["D3"] else 0
        for z in range(spec["D3"] + 1)
    ]
    assert seqsha(t2_vector) == spec["t2_vector_sha256"]
    assert seqsha(t3_vector) == spec["t3_vector_sha256"]
    perturbed2 = list(t2_vector)
    perturbed3 = list(t3_vector)
    perturbed2[spec["t2z"]] += 1
    perturbed3[spec["t3z"]] += 1
    assert seqsha(perturbed2) != spec["t2_vector_sha256"]
    assert seqsha(perturbed3) != spec["t3_vector_sha256"]

    singular_checks = []
    face_payload = []
    emitted_t2 = []
    emitted_t3 = []
    for family, degree, vector, scalar in [
        ("T2", spec["D2"], t2_vector, spec["lam2"]),
        ("T3", spec["D3"], t3_vector, "lambda3"),
    ]:
        for z in range(degree + 1):
            label = f"{family}_face_{z}"
            row = by_label[label]
            assert row[2] == f"{family}_face" and row[3] is None
            original, _, original_index = parse_local(row[1])
            expected = -vector[z]
            assert pure_variable_coefficient(original, original_index, scalar) == expected
            if family == "T2":
                qname = f"xQ_0_{z}"
                assert pure_variable_coefficient(original, original_index, qname) == 1

            emitted_text, emitted_zero = serializer(row)
            assert not emitted_zero or (not original)
            emitted, _, emitted_index = parse_local(emitted_text)
            if original:
                factor = proportional_factor(original, emitted, original_index)
                emitted_expected = factor * expected
                assert pure_variable_coefficient(emitted, emitted_index, scalar) == emitted_expected
                if family == "T2":
                    assert pure_variable_coefficient(emitted, emitted_index, qname) == factor
            else:
                factor = 1
                emitted_expected = 0
            emitted_vector = emitted_t2 if family == "T2" else emitted_t3
            emitted_vector.append(rational_text(emitted_expected))
            row_number = position[id(row)]
            singular_checks.append(
                f"if (diff(I[{row_number}],{scalar})!={rational_text(emitted_expected)}) {{ targetOK=0; }}"
            )
            if family == "T2":
                singular_checks.append(
                    f"if (diff(I[{row_number}],{qname})!={rational_text(factor)}) {{ targetOK=0; }}"
                )
            face_payload.append(f"{row_number}\t{label}\t{emitted_text}")

    return {
        "T2_slot_count": len(t2_vector),
        "T3_slot_count": len(t3_vector),
        "T2_expected_vector_sha256": seqsha(t2_vector),
        "T3_expected_vector_sha256": seqsha(t3_vector),
        "T2_emitted_target_derivatives_sha256": seqsha(emitted_t2),
        "T3_emitted_target_derivatives_sha256": seqsha(emitted_t3),
        "complete_face_labels_exact": True,
        "raw_row_scalar_coefficients_exact": True,
        "primitive_rows_proportional_exact": True,
        "one_slot_perturbations_rejected": True,
        "streamed_face_payload_sha256": seqsha(face_payload),
        "singular_checks": singular_checks,
    }


def proc_snapshot():
    """Return {pid: (ppid, resident bytes)} for readable Linux processes."""
    result = {}
    for status_path in Path("/proc").glob("[0-9]*/status"):
        try:
            text = status_path.read_text()
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            continue
        ppid_match = re.search(r"^PPid:\s+(\d+)$", text, re.MULTILINE)
        rss_match = re.search(r"^VmRSS:\s+(\d+)\s+kB$", text, re.MULTILINE)
        if ppid_match:
            result[int(status_path.parent.name)] = (
                int(ppid_match.group(1)),
                int(rss_match.group(1)) * 1024 if rss_match else 0,
            )
    return result


def descendant_pids(root: int, snapshot) -> set[int]:
    children = {}
    for pid, (ppid, _) in snapshot.items():
        children.setdefault(ppid, []).append(pid)
    found = set()
    pending = [root]
    while pending:
        pid = pending.pop()
        if pid in found:
            continue
        found.add(pid)
        pending.extend(children.get(pid, []))
    return found


def diagnostic_lines(output: str) -> list[str]:
    found = []
    for line in output.splitlines():
        if any(pattern.search(line) for pattern in DIAGNOSTIC_PATTERNS):
            found.append(line.strip())
    return found


def child_session() -> None:
    # Deliberately no setrlimit call: the retry is governed by aggregate RSS.
    os.setsid()


def run(tag: str) -> dict:
    spec = CASES[tag]
    requested_seconds = int(os.environ.get("T2T3_SINGULAR_SECONDS", DEFAULT_SECONDS))
    seconds = min(max(requested_seconds, 1), DEFAULT_SECONDS)
    total_started = time.monotonic()
    parent_pid = os.getpid()
    parent_as_limits = resource.getrlimit(resource.RLIMIT_AS)
    assert parent_as_limits == (resource.RLIM_INFINITY, resource.RLIM_INFINITY)
    receipt_path = HERE / spec["audit_receipt"]
    build_started = time.monotonic()
    audit, rows, graph, all_names, input_sha256, serializer, audit_receipt_sha = load_case(tag)
    build_seconds = time.monotonic() - build_started

    assert input_sha256 == spec["input_sha256"]
    assert len(all_names) == spec["generator_count"]
    assert seqsha(all_names) == spec["generator_order_sha256"]
    assert len(graph) == spec["graph_count"]
    assert len(rows) == spec["row_count"]
    assert seqsha(expression for _, expression, _, _ in rows) == spec["row_expressions_sha256"]

    graph_rows = [row for row in rows if row[3] is not None]
    constraints = [row for row in rows if row[3] is None]
    by_pivot = {row[3]: row for row in graph_rows}
    assert len(by_pivot) == len(graph)
    graph_order = list(reversed(graph))
    base_order = [name for name in all_names if name not in by_pivot]
    ring_names = graph_order + base_order
    assert len(ring_names) == len(set(ring_names)) == spec["generator_count"]
    place = {name: index for index, name in enumerate(ring_names)}
    ordered_graph = [by_pivot[name] for name in graph_order]
    for _, expression, _, pivot in ordered_graph:
        dependencies = set(IDENT.findall(expression)) - {pivot}
        assert all(place[pivot] < place[name] for name in dependencies)
    ordered_rows = ordered_graph + constraints
    target_audit = audit_attained_target_rows(rows, ordered_rows, serializer, spec)

    result_path = HERE / f"singular-full-graph-{tag}.rss-retry.result.json"
    state = {
        "reason": None,
        "output_bytes": 0,
        "peak_parent_rss": 0,
        "peak_singular_root_rss": 0,
        "peak_singular_tree_rss": 0,
        "peak_aggregate_rss": 0,
        "rss_samples": 0,
        "cap_trigger_aggregate_rss": None,
    }
    output_head = []
    output_head_bytes = 0
    output_tail = deque(maxlen=OUTPUT_RETAIN_TAIL_LINES)
    lock = threading.Lock()
    started = time.monotonic()
    proc = subprocess.Popen(
        ["Singular", "-q", "--no-rc", "--no-warn", "--no-shell", "--threads=1", "--flint-threads=1"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
        preexec_fn=child_session,
    )

    def stop(reason: str, trigger_rss=None) -> None:
        with lock:
            if state["reason"] is not None:
                return
            state["reason"] = reason
            if trigger_rss is not None:
                state["cap_trigger_aggregate_rss"] = trigger_rss
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
        nonlocal output_head_bytes
        assert proc.stdout is not None
        for line in proc.stdout:
            encoded_size = len(line.encode())
            with lock:
                state["output_bytes"] += encoded_size
                if output_head_bytes < OUTPUT_RETAIN_HEAD:
                    output_head.append(line)
                    output_head_bytes += encoded_size
                output_tail.append(line)
                overflow = state["output_bytes"] > OUTPUT_CAP
            if overflow:
                stop("OUTPUT_CAP")
                return

    def monitor() -> None:
        while proc.poll() is None:
            snapshot = proc_snapshot()
            parent_rss = snapshot.get(parent_pid, (0, 0))[1]
            tree = descendant_pids(proc.pid, snapshot)
            root_rss = snapshot.get(proc.pid, (0, 0))[1]
            tree_rss = sum(snapshot.get(pid, (0, 0))[1] for pid in tree)
            aggregate = parent_rss + tree_rss
            with lock:
                state["rss_samples"] += 1
                state["peak_parent_rss"] = max(state["peak_parent_rss"], parent_rss)
                state["peak_singular_root_rss"] = max(state["peak_singular_root_rss"], root_rss)
                state["peak_singular_tree_rss"] = max(state["peak_singular_tree_rss"], tree_rss)
                state["peak_aggregate_rss"] = max(state["peak_aggregate_rss"], aggregate)
            if aggregate >= RSS_KILL_THRESHOLD:
                stop("AGGREGATE_RSS_CAP", aggregate)
                return
            if time.monotonic() - started >= seconds:
                stop("TIME_CAP")
                return
            time.sleep(RSS_POLL_SECONDS)

    reader = threading.Thread(target=read_output, daemon=True)
    watcher = threading.Thread(target=monitor, daemon=True)
    reader.start()
    watcher.start()
    streamed_rows = streamed_bytes = canonical_zeros = 0
    write_error = None
    serialized_cache = {}
    try:
        assert proc.stdin is not None
        header = f"ring R=0,({','.join(ring_names)}),lp;\noption(redSB);\nideal I=\n"
        proc.stdin.write(header)
        streamed_bytes += len(header.encode())
        for index, row in enumerate(ordered_rows):
            key = id(row)
            if key not in serialized_cache:
                serialized_cache[key] = serializer(row)
            text, zero = serialized_cache[key]
            canonical_zeros += int(zero)
            chunk = ("" if index == 0 else ",\n") + text
            proc.stdin.write(chunk)
            streamed_bytes += len(chunk.encode())
            streamed_rows += 1
            if index % 64 == 0:
                proc.stdin.flush()
        checks = "\n".join(target_audit["singular_checks"])
        trailer = f''';
print("ALL_ROWS_PARSED");
int graphOK=1;
for (int gi=1; gi<={len(graph_order)}; gi++) {{ if (leadmonom(I[gi])!=var(gi)) {{ graphOK=0; }} }}
print("GRAPH_LEADER_CHECK"); print(graphOK);
int targetOK=1;
{checks}
print("ATTAINED_TARGET_ROW_CHECK"); print(targetOK);
print("BEGIN_GB"); ideal SB=std(I); print("END_GB");
print("BEGIN_RESULT"); print(reduce(1,SB)); print(dim(SB)); print(size(SB)); print("END_RESULT");
ideal n2={spec['lam2']},{spec['zlam2']}*{spec['lam2']}-1; ideal p2={spec['lam2']}-1,{spec['zlam2']}*{spec['lam2']}-1;
ideal n3=lambda3,Z3*lambda3-1; ideal p3=lambda3-1,Z3*lambda3-1;
ideal ns={spec['sep']},{spec['zsep']}*{spec['sep']}-1; ideal ps={spec['sep']}-1,{spec['zsep']}*{spec['sep']}-1;
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
    except (BrokenPipeError, OSError) as error:
        write_error = repr(error)
        try:
            proc.stdin.close()
        except Exception:
            pass

    proc.wait()
    reader.join(timeout=5)
    watcher.join(timeout=1)
    elapsed = time.monotonic() - started
    output = "".join(output_head)
    if state["output_bytes"] > output_head_bytes:
        output += "\n[...OUTPUT MIDDLE OMITTED FROM RECEIPT...]\n" + "".join(output_tail)

    markers = [
        "ALL_ROWS_PARSED",
        "GRAPH_LEADER_CHECK",
        "ATTAINED_TARGET_ROW_CHECK",
        "BEGIN_GB",
        "END_GB",
        "BEGIN_RESULT",
        "END_RESULT",
        "BEGIN_CONTROLS",
        "END_CONTROLS",
    ]
    marker_counts = {marker: output.count(marker) for marker in markers}
    cursor = -1
    markers_in_order = True
    for marker in markers:
        found = output.find(marker, cursor + 1)
        if found < 0:
            markers_in_order = False
            break
        cursor = found

    def between(begin: str, end: str) -> list[str]:
        if output.count(begin) != 1 or output.count(end) != 1:
            return []
        body = output.split(begin, 1)[1].split(end, 1)[0]
        return [line.strip() for line in body.splitlines() if line.strip()]

    result_lines = between("BEGIN_RESULT", "END_RESULT")
    control_lines = between("BEGIN_CONTROLS", "END_CONTROLS")
    graph_lines = between("GRAPH_LEADER_CHECK", "ATTAINED_TARGET_ROW_CHECK")
    target_lines = between("ATTAINED_TARGET_ROW_CHECK", "BEGIN_GB")
    expected_controls = [
        "CTRL_T2_NEG", "0", "CTRL_T2_POS", "1",
        "CTRL_T3_NEG", "0", "CTRL_T3_POS", "1",
        "CTRL_SEP_NEG", "0", "CTRL_SEP_POS", "1",
        "CTRL_CONE_NEG", "0", "CTRL_CONE_POS", "1",
    ]
    diagnostics = diagnostic_lines(output)
    exact_result_fields = (
        len(result_lines) == 3
        and result_lines[0] in {"0", "1"}
        and bool(INTEGER.fullmatch(result_lines[1]))
        and bool(INTEGER.fullmatch(result_lines[2]))
    )
    strict_completion = (
        proc.returncode == 0
        and state["reason"] is None
        and write_error is None
        and streamed_rows == len(ordered_rows)
        and all(count == 1 for count in marker_counts.values())
        and markers_in_order
        and graph_lines == ["1"]
        and target_lines == ["1"]
        and control_lines == expected_controls
        and not diagnostics
        and exact_result_fields
    )
    if strict_completion and result_lines[0] == "0":
        decision = "UNIT"
    elif strict_completion and result_lines[0] == "1" and int(result_lines[1]) >= 0:
        decision = "PROPER"
    elif state["reason"] in {"AGGREGATE_RSS_CAP", "TIME_CAP", "OUTPUT_CAP"}:
        decision = "COMPUTE_BOUND_OPEN"
    else:
        decision = "OPEN_HARNESS_OR_CAS_FAILURE"

    target_receipt = dict(target_audit)
    target_receipt.pop("singular_checks")
    record = {
        "case": tag,
        "decision": decision,
        "field": "Q",
        "ordering": "lp",
        "generator_count": len(ring_names),
        "graph_generator_count": len(graph_order),
        "row_count": len(ordered_rows),
        "streamed_row_count": streamed_rows,
        "streamed_input_bytes": streamed_bytes,
        "canonical_zero_rows_streamed": canonical_zeros,
        "integer_primitive_nonzero_rows": True,
        "reverse_acyclic_order_host_check": True,
        "attained_target_row_audit": target_receipt,
        "audit_receipt_path": str(receipt_path.relative_to(HERE.parent.parent)),
        "audit_receipt_sha256_before_and_after": audit_receipt_sha,
        "audit_driver_sha256": sha_file(Path(audit.__file__)),
        "input_sha256": input_sha256,
        "address_space_limit_set_by_retry": False,
        "parent_RLIMIT_AS_soft": parent_as_limits[0],
        "parent_RLIMIT_AS_hard": parent_as_limits[1],
        "rss_cap_bytes": RSS_CAP,
        "rss_kill_threshold_bytes": RSS_KILL_THRESHOLD,
        "rss_safety_margin_bytes": RSS_SAFETY_MARGIN,
        "rss_poll_seconds": RSS_POLL_SECONDS,
        "rss_scope": "Python builder parent plus complete Singular descendant process tree",
        "rss_samples": state["rss_samples"],
        "peak_parent_RSS_bytes": state["peak_parent_rss"],
        "peak_parent_RSS_MiB": round(state["peak_parent_rss"] / 1024**2, 3),
        "peak_singular_root_RSS_bytes": state["peak_singular_root_rss"],
        "peak_singular_root_RSS_MiB": round(state["peak_singular_root_rss"] / 1024**2, 3),
        "peak_singular_tree_RSS_bytes": state["peak_singular_tree_rss"],
        "peak_singular_tree_RSS_MiB": round(state["peak_singular_tree_rss"] / 1024**2, 3),
        "peak_aggregate_RSS_bytes": state["peak_aggregate_rss"],
        "peak_aggregate_RSS_MiB": round(state["peak_aggregate_rss"] / 1024**2, 3),
        "cap_trigger_aggregate_RSS_bytes": state["cap_trigger_aggregate_rss"],
        "time_cap_seconds": seconds,
        "requested_time_cap_seconds": requested_seconds,
        "build_seconds": round(build_seconds, 3),
        "singular_wall_seconds": round(elapsed, 3),
        "total_driver_wall_seconds": round(time.monotonic() - total_started, 3),
        "termination_reason": state["reason"],
        "returncode": proc.returncode,
        "write_error": write_error,
        "output_bytes": state["output_bytes"],
        "marker_counts": marker_counts,
        "markers_in_required_order": markers_in_order,
        "result_lines": result_lines,
        "exact_result_field_count_and_types": exact_result_fields,
        "controls_lines": control_lines,
        "controls_ok": control_lines == expected_controls,
        "graph_leader_singular_check": graph_lines == ["1"],
        "attained_target_rows_singular_check": target_lines == ["1"],
        "diagnostic_count": len(diagnostics),
        "diagnostic_lines": diagnostics[:100],
        "strict_completion": strict_completion,
        "singular_output": output,
        "driver_sha256": sha_file(Path(__file__)),
    }
    result_path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")
    print(json.dumps(record, indent=2, sort_keys=True), flush=True)
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", required=True, choices=sorted(CASES))
    args = parser.parse_args()
    try:
        result = run(args.case)
    except Exception as error:
        path = HERE / f"singular-full-graph-{args.case}.rss-retry.result.json"
        result = {
            "case": args.case,
            "decision": "OPEN_HARNESS_FAILURE",
            "termination_reason": "HARNESS_EXCEPTION",
            "exception_type": type(error).__name__,
            "exception": repr(error),
            "address_space_limit_set_by_retry": False,
            "driver_sha256": sha_file(Path(__file__)),
        }
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    return 0 if result["decision"] in {"UNIT", "PROPER"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
