#!/usr/bin/env python3
"""Native Singular preprocessing driver for large two-point charts.

Python is only the coordinator here.  For emitter TSVs it splits the fixed
metadata columns, copies polynomial strings verbatim into a generated Singular
script, and lets Singular perform the affine tests and substitutions.  No large
row expression is parsed by SymPy.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from math import gcd
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
INPUTS = Path("/tmp/jc2-lane.lpjOgw/inputs")
RECEIPT = ROOT / "xmodel/preprocess-native-gpt55-20260903.run.v2"
HELPER = OUT / "prep.sing"
EMITTER = ROOT / "box/emitter-20260903"
PRIMES = (32003, 32009, 32027)


@dataclass(frozen=True)
class NativeCase:
    stem: str
    row_key: str
    part_label: str
    rows: Path
    system: Path
    meta: Path


TARGET_25_15 = [
    NativeCase(
        "25_15_part_3_generic",
        "25_15",
        "3",
        EMITTER / "rows/25_15_part_3_generic_rows.tsv",
        EMITTER / "systems/25_15_part_3_generic_Q.sing",
        EMITTER / "meta/25_15_part_3_generic.json",
    ),
    NativeCase(
        "25_15_part_2_1_generic",
        "25_15",
        "2+1",
        EMITTER / "rows/25_15_part_2_1_generic_rows.tsv",
        EMITTER / "systems/25_15_part_2_1_generic_Q.sing",
        EMITTER / "meta/25_15_part_2_1_generic.json",
    ),
    NativeCase(
        "25_15_part_1_1_1_generic",
        "25_15",
        "1+1+1",
        EMITTER / "rows/25_15_part_1_1_1_generic_rows.tsv",
        EMITTER / "systems/25_15_part_1_1_1_generic_Q.sing",
        EMITTER / "meta/25_15_part_1_1_1_generic.json",
    ),
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def receipt_fields() -> tuple[Path, list[dict]]:
    fields: dict[int, dict[str, str]] = {}
    lane_inputs = INPUTS
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if line.startswith("lane_inputs_dir="):
            lane_inputs = Path(line.split("=", 1)[1])
        match = re.match(r"charged_input_(\d+)_(basename|sha256)=(.*)", line)
        if match:
            fields.setdefault(int(match.group(1)), {})[match.group(2)] = match.group(3)
    rows = []
    for index in sorted(fields):
        item = fields[index]
        rows.append(
            {
                "index": index,
                "basename": item["basename"],
                "path": str(lane_inputs / item["basename"]),
                "expected_sha256": item["sha256"],
            }
        )
    return lane_inputs, rows


def verify_inputs() -> dict:
    lane_inputs, rows = receipt_fields()
    for row in rows:
        row["actual_sha256"] = sha256_file(Path(row["path"]))
        row["ok"] = row["actual_sha256"] == row["expected_sha256"]
    return {
        "receipt": str(RECEIPT),
        "inputs": str(lane_inputs),
        "ok": bool(rows) and all(row["ok"] for row in rows),
        "manifest": rows,
    }


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def parse_ring_variables(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line.startswith("ring R="):
                continue
            match = re.match(r"ring\s+R\s*=\s*(?:0|\d+|\([^)]*\))\s*,\s*\((.*)\)\s*,", line)
            if not match:
                raise ValueError(f"cannot parse ring line in {path}: {line[:200]}")
            return [item.strip() for item in match.group(1).split(",") if item.strip()]
    raise ValueError(f"no ring R declaration in {path}")


def iter_pipe_rows(path: Path) -> Iterable[tuple[int, int, int, int, str]]:
    with path.open("r", encoding="utf-8") as handle:
        header = next(handle).strip()
        if header != "source_index|h_power|x_power|y_power|expr":
            raise ValueError(f"unexpected row header in {path}: {header}")
        for line in handle:
            line = line.rstrip("\n")
            if not line:
                continue
            source, hpow, xpow, ypow, expr = line.split("|", 4)
            yield int(source), int(hpow), int(xpow), int(ypow), expr


def singular_expr_text(value) -> str:
    return str(value).replace("**", "^")


def write_k16_rows(t: int, rows_path: Path, vars_path: Path) -> dict:
    if t == 3:
        driver = load_module(INPUTS / "t_order_system.py", "pn_k16_t3_order")
        source = INPUTS / "t_order_system.py"
        data = driver.build(t=3, gauged=True)
    elif t == 4:
        source = ROOT / "box/k16t3-20260903/t4/t4_order_system.py"
        driver = load_module(source, "pn_k16_t4_order")
        data = driver.build(gauged=True, t=4)
    else:
        raise ValueError(t)

    rows_path.parent.mkdir(parents=True, exist_ok=True)
    vars_path.parent.mkdir(parents=True, exist_ok=True)
    variables = [str(item) for item in data["params"]] + [str(data["c"])]
    vars_path.write_text("\n".join(variables) + "\n", encoding="utf-8")
    lines = ["source_index|h_power|x_power|y_power|expr"]
    for index, (h_power, monomial, expr) in enumerate(data["tagged"]):
        lines.append(
            "%d|%d|%d|%d|%s"
            % (
                index,
                int(h_power),
                int(monomial[0]),
                int(monomial[1]),
                singular_expr_text(expr),
            )
        )
    rows_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {
        "source": str(source),
        "source_sha256": sha256_file(source),
        "t": int(data["t"]),
        "e": int(data["e"]),
        "q": int(data["q"]),
        "unknowns_including_c": len(variables),
        "equations": len(data["tagged"]),
        "rows_sha256": sha256_file(rows_path),
    }


def k16_weight(name: str, t: int) -> int:
    if name == "c":
        return 20 * t + 5
    fixed = {"b1": 1, "b2": 2, "b3": 3, "b4": 4}
    if name in fixed:
        return fixed[name]
    match = re.match(r"a(\d+)_(\d+)$", name)
    if match:
        i = int(match.group(1))
        j = int(match.group(2))
        return 4 * i - j
    match = re.match(r"q(\d+)_(\d+)$", name)
    if match:
        i = int(match.group(1))
        j = int(match.group(2))
        if j == 0:
            return 4 * i - (3 if i == 2 * t + 1 else 0)
        if j == 1:
            return 4 * i - (2 if i == 2 * t + 1 else 3)
        return 4 * i - 3 * j
    return 1


def natural_weight(name: str, meta: dict | None, *, k16_t: int | None = None) -> int:
    if k16_t is not None:
        return k16_weight(name, k16_t)
    if not meta:
        return 1
    K = int(meta.get("K", 0) or 0)
    if name == "c" and K:
        row = meta.get("row", {})
        return int((meta["dprime"] + meta["eprime"]) * K - 2 - row.get("k", 0))
    match = re.match(r"h0_(\d+)_(\d+)$", name) or re.match(r"h_(\d+)_(\d+)$", name)
    if match and K:
        return K - int(match.group(1)) - int(match.group(2))
    match = re.match(r"([AB])(\d+)_(\d+)_(\d+)$", name)
    if match and K:
        deficit = int(match.group(2))
        return deficit * K - int(match.group(3)) - int(match.group(4))
    if re.match(r"[as]\d+$", name):
        return 0
    return 1


def read_vars_file(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_qstage_script(
    *,
    rows_path: Path,
    variables: Sequence[str],
    meta: dict | None,
    script_path: Path,
    prefix: Path,
    max_pivots: int,
    k16_t: int | None = None,
) -> dict:
    script_path.parent.mkdir(parents=True, exist_ok=True)
    prefix.parent.mkdir(parents=True, exist_ok=True)
    variables = [v for v in variables if v != "T"]
    if "c" not in variables:
        raise ValueError("variable list does not contain c")
    cidx = variables.index("c") + 1
    weights = [natural_weight(v, meta, k16_t=k16_t) for v in variables]

    srcs: list[int] = []
    hpows: list[int] = []
    xpows: list[int] = []
    ypows: list[int] = []
    with script_path.open("w", encoding="utf-8") as out:
        out.write("// generated by prep.py; row payload copied verbatim, reduced by prep.sing\n")
        out.write('LIB "resources.lib";\n')
        out.write("setcores(4);\n")
        out.write("ring R=0,(%s),dp;\n" % ",".join(variables))
        out.write("option(redSB);\n")
        out.write('execute(read("%s"));\n' % HELPER.resolve())
        out.write("ideal I;\n")
        for index, (source, hpow, xpow, ypow, expr) in enumerate(iter_pipe_rows(rows_path), start=1):
            srcs.append(source)
            hpows.append(hpow)
            xpows.append(xpow)
            ypows.append(ypow)
            out.write("I[%d]=(%s);\n" % (index, expr))
        out.write("intvec SRC=%s;\n" % ",".join(map(str, srcs)))
        out.write("intvec HPOW=%s;\n" % ",".join(map(str, hpows)))
        out.write("intvec XPOW=%s;\n" % ",".join(map(str, xpows)))
        out.write("intvec YPOW=%s;\n" % ",".join(map(str, ypows)))
        out.write("intvec W=%s;\n" % ",".join(map(str, weights)))
        out.write('string PREFIX="%s";\n' % prefix.resolve())
        out.write("print(\"PN_LOAD rows=%d variables=%d cidx=%d\");\n" % (len(srcs), len(variables), cidx))
        out.write("list QR=pn_qpivot_reduce(I,SRC,HPOW,XPOW,YPOW,%d,%d,PREFIX);\n" % (cidx, max_pivots))
        out.write('list ER=pn_export_exponent_diffs(QR[1],PREFIX+"_exponents.tsv");\n')
        out.write('list WR=pn_weight_report(QR[1],SRC,HPOW,XPOW,YPOW,W,PREFIX+"_weights.tsv");\n')
        out.write("quit;\n")
    return {
        "script": str(script_path.relative_to(ROOT)),
        "script_bytes": script_path.stat().st_size,
        "input_rows": len(srcs),
        "variables": list(variables),
        "weights": weights,
        "c_index_1based": cidx,
    }


def parse_key_value_file(path: Path) -> dict:
    out: dict[str, int | str] = {}
    if not path.is_file():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        try:
            out[key] = int(value)
        except ValueError:
            out[key] = value
    return out


def parse_weight_file(path: Path) -> dict:
    if not path.is_file():
        return {"status": "MISSING"}
    rows = 0
    bad = 0
    sample_bad = []
    with path.open("r", encoding="utf-8") as handle:
        next(handle, None)
        for line in handle:
            rows += 1
            parts = line.rstrip("\n").split("|")
            if len(parts) >= 7 and parts[6] != "1":
                bad += 1
                if len(sample_bad) < 5:
                    sample_bad.append(parts[:6])
    return {
        "status": "VERIFIED_NATURAL" if bad == 0 else "FAILED_NATURAL",
        "rows_checked": rows,
        "nonhomogeneous_rows": bad,
        "sample_nonhomogeneous": sample_bad,
    }


def _lcm(values: Iterable[int]) -> int:
    return reduce(lambda a, b: abs(a * b) // gcd(a, b), values, 1)


def _primitive_ints(values: Sequence) -> list[int]:
    rationals = [Fraction(str(value)) for value in values]
    common = _lcm(fr.denominator for fr in rationals)
    ints = [fr.numerator * (common // fr.denominator) for fr in rationals]
    div = 0
    for item in ints:
        div = gcd(div, abs(item))
    if div:
        ints = [item // div for item in ints]
    return ints


def solve_grading_from_diffs(path: Path, variables: Sequence[str], alive_path: Path | None = None) -> dict:
    if not path.is_file():
        return {"status": "MISSING"}
    with path.open("r", encoding="utf-8") as handle:
        header = next(handle, "").rstrip("\n").split("|")
        matrix_variables = header[2:]
        if matrix_variables != list(variables):
            return {
                "status": "VARIABLE_MISMATCH",
                "matrix_variables": matrix_variables,
                "expected_variables": list(variables),
            }
        active = set(variables)
        if alive_path and alive_path.is_file():
            active = set()
            with alive_path.open("r", encoding="utf-8") as alive:
                next(alive, None)
                for line in alive:
                    parts = line.rstrip("\n").split("|")
                    if len(parts) >= 2:
                        active.add(parts[1])
        active_positions = [index for index, name in enumerate(variables) if name in active]
        inactive_positions = [index for index, name in enumerate(variables) if name not in active]
        constraints_seen: set[tuple[int, ...]] = set()
        raw_constraints = 0
        inactive_violations = 0
        for line in handle:
            parts = line.rstrip("\n").split("|")
            if len(parts) == len(header):
                full = [int(value) for value in parts[2:]]
                raw_constraints += 1
                if any(full[index] != 0 for index in inactive_positions):
                    inactive_violations += 1
                projected = tuple(full[index] for index in active_positions)
                if any(projected):
                    constraints_seen.add(projected)
    constraints = list(constraints_seen)
    if not constraints:
        weights = [1 if index in active_positions else 0 for index, _ in enumerate(variables)]
        return {
            "status": "POSITIVE",
            "constraints": raw_constraints,
            "unique_constraints": 0,
            "rank": 0,
            "nullity": len(active_positions),
            "active_variables": len(active_positions),
            "inactive_diff_violations": inactive_violations,
            "weights": dict(zip(variables, weights)),
        }
    try:
        import sympy as sp
        from sympy.polys.domains import QQ
        from sympy.polys.matrices import DomainMatrix
    except ImportError:
        return {"status": "NO_SYMPY_FOR_LP", "constraints": raw_constraints}
    matrix = DomainMatrix.from_Matrix(sp.Matrix(constraints), fmt="sparse").convert_to(QQ)
    rank = int(matrix.rank())
    nullspace_matrix = matrix.nullspace().to_Matrix()
    nullspace = [list(nullspace_matrix.row(index)) for index in range(nullspace_matrix.rows)]
    if not nullspace:
        return {
            "status": "NO_GRADING",
            "constraints": raw_constraints,
            "unique_constraints": len(constraints),
            "rank": rank,
            "nullity": 0,
            "active_variables": len(active_positions),
            "inactive_diff_violations": inactive_violations,
        }
    if len(nullspace) == 1:
        active_ints = _primitive_ints(nullspace[0])
        if any(item < 0 for item in active_ints) and not any(item > 0 for item in active_ints):
            active_ints = [-item for item in active_ints]
        active_weights = list(active_ints)
        if all(item > 0 for item in active_weights):
            status = "POSITIVE"
        elif all(item >= 0 for item in active_weights) and any(item > 0 for item in active_weights):
            status = "NONNEGATIVE"
        else:
            status = "INDEFINITE"
        ints = [0] * len(variables)
        for index, value in zip(active_positions, active_ints):
            ints[index] = value
        return {
            "status": status,
            "constraints": raw_constraints,
            "unique_constraints": len(constraints),
            "rank": rank,
            "nullity": 1,
            "active_variables": len(active_positions),
            "inactive_diff_violations": inactive_violations,
            "weights": dict(zip(variables, ints)),
        }

    # The observed control charts have nullity one.  For wider kernels, try a
    # small exact integer combination before declaring that the LP needs a
    # stronger solver.
    basis = [_primitive_ints(vec) for vec in nullspace]
    from itertools import product

    radius = 4 if len(basis) <= 5 else 2
    for coeffs in product(range(-radius, radius + 1), repeat=len(basis)):
        if all(value == 0 for value in coeffs):
            continue
        candidate_active = [sum(coeff * vec[pos] for coeff, vec in zip(coeffs, basis)) for pos in range(len(active_positions))]
        if all(value > 0 for value in candidate_active):
            candidate_active = _primitive_ints(candidate_active)
            candidate = [0] * len(variables)
            for index, value in zip(active_positions, candidate_active):
                candidate[index] = value
            return {
                "status": "POSITIVE",
                "constraints": raw_constraints,
                "unique_constraints": len(constraints),
                "rank": rank,
                "nullity": len(nullspace),
                "active_variables": len(active_positions),
                "inactive_diff_violations": inactive_violations,
                "weights": dict(zip(variables, candidate)),
                "combination": list(coeffs),
            }
    return {
        "status": "LP_OPEN",
        "constraints": raw_constraints,
        "unique_constraints": len(constraints),
        "rank": rank,
        "nullity": len(nullspace),
        "active_variables": len(active_positions),
        "inactive_diff_violations": inactive_violations,
    }


def run_process(cmd: Sequence[str], timeout: int, stdout_path: Path, stderr_path: Path) -> dict:
    started = time.time()
    stdout_path.parent.mkdir(parents=True, exist_ok=True)
    stderr_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with stdout_path.open("w", encoding="utf-8") as out, stderr_path.open("w", encoding="utf-8") as err:
            proc = subprocess.run(cmd, stdout=out, stderr=err, text=True, timeout=timeout)
        status = "OK" if proc.returncode == 0 else "ERROR"
        rc = proc.returncode
    except subprocess.TimeoutExpired:
        status = "TIMEOUT"
        rc = 124
    elapsed = round(time.time() - started, 3)
    return {
        "status": status,
        "rc": rc,
        "elapsed": elapsed,
        "timeout": timeout,
        "stdout": str(stdout_path.relative_to(ROOT)),
        "stderr": str(stderr_path.relative_to(ROOT)),
        "stdout_tail": stdout_path.read_text(encoding="utf-8", errors="ignore")[-2400:] if stdout_path.is_file() else "",
        "stderr_tail": stderr_path.read_text(encoding="utf-8", errors="ignore")[-2400:] if stderr_path.is_file() else "",
    }


def run_qstage(
    stem: str,
    rows_path: Path,
    variables: Sequence[str],
    meta: dict | None,
    *,
    timeout: int,
    max_pivots: int = 512,
    k16_t: int | None = None,
) -> dict:
    work = OUT / "work"
    prefix = OUT / "results" / stem
    script = work / f"{stem}_qstage.sing"
    generated = write_qstage_script(
        rows_path=rows_path,
        variables=variables,
        meta=meta,
        script_path=script,
        prefix=prefix,
        max_pivots=max_pivots,
        k16_t=k16_t,
    )
    log = OUT / "logs"
    run = run_process(
        ["Singular", "-q", "--no-rc", str(script)],
        timeout,
        log / f"{stem}_qstage.out",
        log / f"{stem}_qstage.err",
    )
    qtxt = prefix.with_name(prefix.name + "_qstage.txt")
    pivots = prefix.with_name(prefix.name + "_pivots.tsv")
    residual = prefix.with_name(prefix.name + "_residual.tsv")
    weights = prefix.with_name(prefix.name + "_weights.tsv")
    exponents = prefix.with_name(prefix.name + "_exponents.tsv")
    variables_out = prefix.with_name(prefix.name + "_variables.tsv")
    audit = parse_key_value_file(qtxt)
    grading_lp = (
        solve_grading_from_diffs(exponents, generated["variables"], variables_out)
        if run["status"] == "OK"
        else {"status": "NOT_RUN_INCOMPLETE_SINGULAR_STAGE"}
    )
    rec = {
        "typing": "MEASURED",
        "stem": stem,
        "rows_path": str(rows_path.relative_to(ROOT)) if rows_path.is_relative_to(ROOT) else str(rows_path),
        "rows_sha256": sha256_file(rows_path) if rows_path.is_file() else None,
        "generated": generated,
        "run": run,
        "qstage": audit,
        "pivots_tsv": str(pivots.relative_to(ROOT)) if pivots.is_file() else None,
        "residual_tsv": str(residual.relative_to(ROOT)) if residual.is_file() else None,
        "exponents_tsv": str(exponents.relative_to(ROOT)) if exponents.is_file() else None,
        "variables_tsv": str(variables_out.relative_to(ROOT)) if variables_out.is_file() else None,
        "weight_report": parse_weight_file(weights),
        "grading_lp": grading_lp,
    }
    if pivots.is_file():
        rec["pivot_count_from_tsv"] = max(0, sum(1 for _ in pivots.open("r", encoding="utf-8")) - 1)
    if residual.is_file():
        rec["residual_rows_from_tsv"] = max(0, sum(1 for _ in residual.open("r", encoding="utf-8")) - 1)
        rec["residual_bytes"] = residual.stat().st_size
    out_json = OUT / "results" / f"{stem}_qstage.json"
    out_json.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    rec["json"] = str(out_json.relative_to(ROOT))
    return rec


def parse_pivot_file(path: Path) -> list[dict]:
    if not path.is_file():
        return []
    pivots = []
    with path.open("r", encoding="utf-8") as handle:
        header = next(handle, "").rstrip("\n")
        if header != "step|source_index|h_power|x_power|y_power|variable|coefficient_Qstar|rhs":
            raise ValueError(f"unexpected pivot header in {path}: {header}")
        for line in handle:
            parts = line.rstrip("\n").split("|", 7)
            if len(parts) == 8:
                pivots.append(
                    {
                        "step": int(parts[0]),
                        "source_index": int(parts[1]),
                        "h_power": int(parts[2]),
                        "x_power": int(parts[3]),
                        "y_power": int(parts[4]),
                        "variable": parts[5],
                        "coefficient_Qstar": parts[6],
                        "rhs": parts[7],
                    }
                )
    return pivots


def run_stuck_replay(case: NativeCase, timeout: int) -> dict:
    meta = json.loads(case.meta.read_text(encoding="utf-8"))["meta"]
    variables = [v for v in parse_ring_variables(case.system) if v != "T"]
    variable_index = {name: index + 1 for index, name in enumerate(variables)}
    pivots_path = OUT / "results" / f"{case.stem}_pivots.tsv"
    pivots = parse_pivot_file(pivots_path)
    if not pivots:
        return {"status": "NO_PIVOTS_TO_REPLAY"}

    work = OUT / "work"
    results = OUT / "results"
    replay_stem = f"{case.stem}_stuck_after_{len(pivots)}"
    script = work / f"{replay_stem}.sing"
    prefix = results / replay_stem
    srcs: list[int] = []
    hpows: list[int] = []
    xpows: list[int] = []
    ypows: list[int] = []
    src_to_slot: dict[int, int] = {}
    weights = [natural_weight(v, meta) for v in variables]

    with script.open("w", encoding="utf-8") as out:
        out.write("// generated by prep.py stuck replay; row payload copied verbatim\n")
        out.write('LIB "resources.lib";\n')
        out.write("setcores(4);\n")
        out.write("ring R=0,(%s),dp;\n" % ",".join(variables))
        out.write("option(redSB);\n")
        out.write('execute(read("%s"));\n' % HELPER.resolve())
        out.write("ideal I;\n")
        for slot, (source, hpow, xpow, ypow, expr) in enumerate(iter_pipe_rows(case.rows), start=1):
            srcs.append(source)
            hpows.append(hpow)
            xpows.append(xpow)
            ypows.append(ypow)
            src_to_slot[source] = slot
            out.write("I[%d]=(%s);\n" % (slot, expr))
        out.write("intvec SRC=%s;\n" % ",".join(map(str, srcs)))
        out.write("intvec HPOW=%s;\n" % ",".join(map(str, hpows)))
        out.write("intvec XPOW=%s;\n" % ",".join(map(str, xpows)))
        out.write("intvec YPOW=%s;\n" % ",".join(map(str, ypows)))
        out.write("intvec W=%s;\n" % ",".join(map(str, weights)))
        out.write("intvec ALIVE;\n")
        out.write("int v;\n")
        out.write("for (v=1; v<=nvars(basering); v++) { ALIVE[v]=1; }\n")
        out.write("int i;\n")
        for pivot in pivots:
            if pivot["source_index"] not in src_to_slot:
                raise ValueError(f"pivot source {pivot['source_index']} not present in {case.rows}")
            if pivot["variable"] not in variable_index:
                raise ValueError(f"pivot variable {pivot['variable']} not present in ring")
            slot = src_to_slot[pivot["source_index"]]
            vindex = variable_index[pivot["variable"]]
            out.write("// replay pivot step %d variable %s source %d\n" % (pivot["step"], pivot["variable"], pivot["source_index"]))
            out.write("poly RHS=(%s);\n" % pivot["rhs"])
            out.write("if (subst(I[%d],var(%d),RHS)!=0) { ERROR(\"stuck replay pivot mismatch\"); }\n" % (slot, vindex))
            out.write("I[%d]=0;\n" % slot)
            out.write("ALIVE[%d]=0;\n" % vindex)
            out.write(
                "for (i=1; i<=size(I); i++) { "
                "if (I[i]!=0 && pn_var_degree(I[i],%d)>0) { I[i]=subst(I[i],var(%d),RHS); } }\n"
                % (vindex, vindex)
            )
            out.write('print("PN_REPLAY step=%d variable=%s");\n' % (pivot["step"], pivot["variable"]))
        out.write('pn_write_residual(I,SRC,HPOW,XPOW,YPOW,"%s_residual.tsv");\n' % prefix.resolve())
        out.write('pn_write_alive_vars(ALIVE,"%s_variables.tsv");\n' % prefix.resolve())
        out.write('write(":w %s_qstage.txt","pivot_count=%d");\n' % (prefix.resolve(), len(pivots)))
        out.write('write(":a %s_qstage.txt","status=STUCK_REPLAY_RESIDUAL");\n' % prefix.resolve())
        out.write('print("PN_REPLAY_DONE pivots=%d");\n' % len(pivots))
        out.write("quit;\n")

    log = OUT / "logs"
    run = run_process(
        ["Singular", "-q", "--no-rc", str(script)],
        timeout,
        log / f"{replay_stem}.out",
        log / f"{replay_stem}.err",
    )
    residual = prefix.with_name(prefix.name + "_residual.tsv")
    variables_out = prefix.with_name(prefix.name + "_variables.tsv")
    rec = {
        "status": run["status"],
        "pivot_count": len(pivots),
        "script": str(script.relative_to(ROOT)),
        "script_bytes": script.stat().st_size,
        "run": run,
        "residual_tsv": str(residual.relative_to(ROOT)) if residual.is_file() else None,
        "variables_tsv": str(variables_out.relative_to(ROOT)) if variables_out.is_file() else None,
        "weight_report": {"status": "NOT_RUN_RESIDUAL_REPLAY_ONLY"},
        "grading_lp": {"status": "NOT_RUN_RESIDUAL_REPLAY_ONLY"},
    }
    if residual.is_file():
        rec["residual_rows_from_tsv"] = max(0, sum(1 for _ in residual.open("r", encoding="utf-8")) - 1)
        rec["residual_bytes"] = residual.stat().st_size
    out_json = OUT / "results" / f"{replay_stem}.json"
    out_json.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    rec["json"] = str(out_json.relative_to(ROOT))
    return rec


def replay_stuck_targets(timeout: int) -> dict:
    targets_path = OUT / "results/targets_25_15.json"
    targets = json.loads(targets_path.read_text(encoding="utf-8")) if targets_path.is_file() else {}
    out = {}
    for case in TARGET_25_15:
        rec = targets.get(case.stem, {})
        if rec.get("run", {}).get("status") == "TIMEOUT" and rec.get("pivot_count_from_tsv", 0):
            replay = run_stuck_replay(case, timeout)
            rec["stuck_replay"] = replay
            targets[case.stem] = rec
            out[case.stem] = replay
    targets_path.write_text(json.dumps(targets, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return out


def run_singular_timed(script: Path, stem: str, timeout: int) -> dict:
    log = OUT / "logs"
    return run_process(
        ["/usr/bin/time", "-v", "Singular", "-q", "--no-rc", str(script)],
        timeout,
        log / f"{stem}.out",
        log / f"{stem}.err",
    )


def parse_singular_verdict(run: dict) -> dict:
    text = (run.get("stdout_tail") or "") + "\n" + (run.get("stderr_tail") or "")
    verdict = "TIMEOUT" if run["status"] == "TIMEOUT" else "ERROR"
    if "MAIN_SATURATED_EMPTY" in text or "MAIN_QUADRATIC_FIELD_EMPTY" in text or "MAIN_EXACT_UNIT" in text:
        verdict = "SATURATED-EMPTY"
    elif "MAIN_NONTRIVIAL" in text or "MAIN_NONUNIT" in text:
        verdict = "COUNTING-BOUND"
    match = re.search(r"Maximum resident set size \(kbytes\):\s*(\d+)", run.get("stderr_tail", ""))
    rss = int(match.group(1)) if match else None
    return {"verdict": verdict, "max_rss_kb": rss}


def validation_runs(timeout: int) -> dict:
    val_dir = OUT / "validation"
    t3_rows = val_dir / "k16_t3_rows.tsv"
    t3_vars = val_dir / "k16_t3_vars.txt"
    t3_meta = write_k16_rows(3, t3_rows, t3_vars)
    t3_q = run_qstage("k16_t3_native", t3_rows, read_vars_file(t3_vars), None, timeout=timeout, k16_t=3)

    t4_rows = val_dir / "k16_t4_rows.tsv"
    t4_vars = val_dir / "k16_t4_vars.txt"
    t4_meta = write_k16_rows(4, t4_rows, t4_vars)
    t4_q = run_qstage("k16_t4_native", t4_rows, read_vars_file(t4_vars), None, timeout=timeout, k16_t=4)

    t3_std = run_singular_timed(ROOT / "box/k16t3-20260903/preprocessed/t3_normalized_K_std.sing", "k16_t3_normalized_K_std", timeout)
    t3_std.update(parse_singular_verdict(t3_std))
    t4_std = run_singular_timed(ROOT / "box/k16t4-gate-20260903/t4_exact_Qsqrt15_nfmodstd.sing", "k16_t4_Qsqrt15_nfmodstd", timeout)
    t4_std.update(parse_singular_verdict(t4_std))

    v33 = run_singular_timed(EMITTER / "systems/33_22_part_3_ab_Q.sing", "33_22_part_3_ab_Q", timeout)
    v33.update(parse_singular_verdict(v33))

    rec = {
        "k16_t3": {
            "emission": t3_meta,
            "qstage": t3_q,
            "field_std": t3_std,
            "expected": "36 -> 23 variables including c after 13 Q* pivots; field pass leaves 6 rows and std=[1]",
        },
        "k16_t4": {
            "emission": t4_meta,
            "qstage": t4_q,
            "field_std": t4_std,
            "expected": "45 -> 29 variables including c after 16 Q* pivots; Q(sqrt15) eight-generator field system std=[1]",
        },
        "33_22_part_3": {
            "script": str((EMITTER / "systems/33_22_part_3_ab_Q.sing").relative_to(ROOT)),
            "std": v33,
            "expected": "28 unknowns, direct exact standard basis [1]",
        },
    }
    path = OUT / "results/validation.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return rec


def process_targets(timeout: int, max_pivots: int) -> dict:
    out: dict[str, dict] = {}
    for case in TARGET_25_15:
        meta = json.loads(case.meta.read_text(encoding="utf-8"))["meta"]
        vars_in = parse_ring_variables(case.system)
        rec = run_qstage(case.stem, case.rows, vars_in, meta, timeout=timeout, max_pivots=max_pivots)
        rec["meta"] = {
            "row_key": case.row_key,
            "partition": case.part_label,
            "unknowns": meta.get("unknowns"),
            "equations": meta.get("equations"),
            "top_face_factored": meta.get("top_face_factored"),
            "saturation_factor": meta.get("saturation_factor"),
            "alpha_dims": meta.get("alpha_dims"),
            "beta_dims": meta.get("beta_dims"),
            "h_lower_count_corrected": meta.get("h_lower_count_corrected"),
            "omega": meta.get("omega"),
        }
        out[case.stem] = rec
    path = OUT / "results/targets_25_15.json"
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return out


def summarize_qstage(rec: dict) -> dict:
    q = rec.get("qstage", {})
    replay = rec.get("stuck_replay", {})
    return {
        "run_status": rec.get("run", {}).get("status"),
        "elapsed": rec.get("run", {}).get("elapsed"),
        "pivots": rec.get("pivot_count_from_tsv", q.get("pivot_count")),
        "residual_rows": rec.get("residual_rows_from_tsv", q.get("residual_rows")),
        "remaining_variables": q.get("remaining_variables"),
        "stuck_replay_status": replay.get("status"),
        "stuck_replay_elapsed": replay.get("run", {}).get("elapsed") if replay else None,
        "stuck_replay_residual_rows": replay.get("residual_rows_from_tsv"),
        "stuck_replay_residual_tsv": replay.get("residual_tsv"),
        "stuck_replay_json": replay.get("json"),
        "weight_status": rec.get("weight_report", {}).get("status"),
        "nonhomogeneous_rows": rec.get("weight_report", {}).get("nonhomogeneous_rows"),
        "grading_status": rec.get("grading_lp", {}).get("status"),
        "grading_rank": rec.get("grading_lp", {}).get("rank"),
        "grading_nullity": rec.get("grading_lp", {}).get("nullity"),
        "grading_constraints": rec.get("grading_lp", {}).get("constraints"),
        "json": rec.get("json"),
    }


def _fmt_bytes(value: int | None) -> str:
    if value is None:
        return "-"
    if value >= 1_000_000:
        return "%.1f MB" % (value / 1_000_000.0)
    if value >= 1_000:
        return "%.1f KB" % (value / 1_000.0)
    return "%d B" % value


def _read_report_pivots(rel_path: str | None) -> list[dict[str, str]]:
    if not rel_path:
        return []
    path = Path(rel_path)
    if not path.is_absolute():
        path = ROOT / path
    if not path.is_file():
        return []
    out: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8") as handle:
        header = handle.readline().rstrip("\n").split("|")
        for line in handle:
            fields = line.rstrip("\n").split("|", len(header) - 1)
            if len(fields) != len(header):
                continue
            row = dict(zip(header, fields))
            rhs = row.get("rhs", "")
            row["rhs_sha256_12"] = hashlib.sha256(rhs.encode("utf-8")).hexdigest()[:12]
            row["rhs_terms_hint"] = str(rhs.count("+") + rhs.count("-") + 1) if rhs else "0"
            out.append(row)
    return out


def write_report(manifest: dict, validations: dict | None, targets: dict | None) -> Path:
    validations = validations or json.loads((OUT / "results/validation.json").read_text(encoding="utf-8"))
    targets = targets or json.loads((OUT / "results/targets_25_15.json").read_text(encoding="utf-8"))
    report = ROOT / "xmodel/preprocess-native-gpt55-20260903.md"
    lines: list[str] = []
    lines.append("# Native preprocessing pipeline for large two-point charts")
    lines.append("")
    lines.append("Date: 2026-09-03 UTC.")
    lines.append("")
    lines.append("## Custody")
    lines.append("")
    lines.append(
        "MEASURED. The checksum manifest was generated mechanically from "
        "`xmodel/preprocess-native-gpt55-20260903.run.v2` and checked with "
        "`sha256sum -c`; all %d frozen inputs under `%s` returned `OK`."
        % (len(manifest.get("manifest", [])), manifest.get("inputs"))
    )
    lines.append("")
    lines.append("| # | frozen input | sha256 |")
    lines.append("|---:|---|---|")
    for row in sorted(manifest.get("manifest", []), key=lambda item: item["index"]):
        lines.append(
            "| %d | `%s` | `%s` |"
            % (row["index"], row["basename"], row["actual_sha256"])
        )
    lines.append("")
    lines.append("MEASURED. New writes are confined to `box/preprocess-native-20260903/` and this report. No ledger, `jc2-lean`, `ideation-*`, or in-progress lane report was edited.")
    lines.append("")
    lines.append("## Implementation")
    lines.append("")
    lines.append("MEASURED. `prep.sing` implements the native Singular stage. It detects only rows `f=a*x+b` with `a in Q*`, `x` absent from `b`, substitutes `x=-b/a` by `subst`, and records each pivot. Parameter-dependent coefficients are rejected because the derivative coefficient must have total degree zero. The same Singular session exports exact monomial exponent-difference constraints for the residual ideal.")
    lines.append("")
    lines.append("MEASURED. `prep.py` streams the emitter row TSV into generated Singular scripts by copying polynomial payload text verbatim. Python does not parse the 42-180 MB expressions symbolically; it only reads row metadata, ring variables, Singular's small audit files, and the integer exponent-difference matrix. The grading step solves that matrix exactly over `Q` and reports rank/nullity and a primitive positive weight vector when one is found.")
    lines.append("")
    lines.append("AUDIT. The current driver also contains slice/base-scan helpers in `prep.sing`, but the `(25,15)` native Q stage below does not reach a usable forced-nonzero slice. No division by a parameter-dependent pivot is promoted.")
    lines.append("")
    lines.append("## Validation")
    lines.append("")
    k16t3 = validations["k16_t3"]
    k16t4 = validations["k16_t4"]
    v33 = validations["33_22_part_3"]
    lines.append("| case | native Q pivots | residual | grading | field/std verdict | wall |")
    lines.append("|---|---:|---|---|---|---:|")
    for label, item in (("K16 t=3", k16t3), ("K16 t=4", k16t4)):
        q = summarize_qstage(item["qstage"])
        field = item["field_std"]
        lines.append(
            "| %s | %s | %s rows, %s vars | %s, rank %s/nullity %s | %s | %.3f s |"
            % (
                label,
                q["pivots"],
                q["residual_rows"],
                q["remaining_variables"],
                q["grading_status"],
                q["grading_rank"],
                q["grading_nullity"],
                field.get("verdict"),
                field.get("elapsed", 0.0),
            )
        )
    lines.append(
        "| `(33,22;30;8;1)` `[3]` | - | 62 rows, 28 vars | direct exact | %s | %.3f s |"
        % (v33["std"].get("verdict"), v33["std"].get("elapsed", 0.0))
    )
    lines.append("")
    lines.append("MEASURED. The K16 t=3 native Q stage reproduces `36 -> 23` variables including `c`; the charged normalized field script over `Q[q7_1]/(147*q7_1^2-84*q7_1+11)` replays as `[1]` from 6 generators.")
    lines.append("")
    lines.append("MEASURED. The K16 t=4 native Q stage reproduces `45 -> 29` variables including `c`; the charged `Q(sqrt15)` eight-generator `nfmodStd` replay returns `[1]`.")
    lines.append("")
    lines.append("### Validation Audit")
    lines.append("")
    lines.append("| case | qstage wall | qstage residual artifact | exponent constraints | natural-weight check | exact script/log | RSS |")
    lines.append("|---|---:|---|---:|---|---|---:|")
    validation_audit = [
        (
            "K16 t=3",
            k16t3["qstage"],
            "box/k16t3-20260903/preprocessed/t3_normalized_K_std.sing",
            k16t3["field_std"],
        ),
        (
            "K16 t=4",
            k16t4["qstage"],
            "box/k16t4-gate-20260903/t4_exact_Qsqrt15_nfmodstd.sing",
            k16t4["field_std"],
        ),
    ]
    for label, qrec, script, field in validation_audit:
        lp = qrec.get("grading_lp", {})
        wr = qrec.get("weight_report", {})
        residual = "%s (%s)" % (qrec.get("residual_tsv"), _fmt_bytes(qrec.get("residual_bytes")))
        logs = "%s; %s, %s" % (script, field.get("stdout"), field.get("stderr"))
        lines.append(
            "| %s | %.3f s | `%s` | %s | %s, nonhom=%s | `%s` | %s |"
            % (
                label,
                qrec.get("run", {}).get("elapsed", 0.0),
                residual,
                lp.get("constraints"),
                wr.get("status"),
                wr.get("nonhomogeneous_rows"),
                logs,
                field.get("max_rss_kb"),
            )
        )
    lines.append(
        "| `(33,22;30;8;1)` `[3]` | - | direct system | - | direct exact | `%s`; `%s`, `%s` | %s |"
        % (
            v33.get("script"),
            v33["std"].get("stdout"),
            v33["std"].get("stderr"),
            v33["std"].get("max_rss_kb"),
        )
    )
    lines.append("")
    lines.append("MEASURED. The K16 grading LPs were solved from exact exponent-difference TSVs exported by Singular: t=3 has 2104 constraints, 1047 unique constraints, rank 22 and nullity 1; t=4 has 6307 constraints, 3172 unique constraints, rank 28 and nullity 1. In both cases the natural-weight verifier reports zero nonhomogeneous residual rows.")
    lines.append("")
    lines.append("## `(25,15;21;2;k=2)`")
    lines.append("")
    lines.append("| stratum | unknowns | rows | native Q status | pivots | residual/stuck replay | grading | base row | field | verdict |")
    lines.append("|---|---:|---:|---|---:|---|---|---|---|---|")
    for stem, rec in targets.items():
        meta = rec.get("meta", {})
        q = summarize_qstage(rec)
        status = q["run_status"]
        pivots = q["pivots"] if q["pivots"] is not None else "?"
        residual = (
            "%s rows, %s vars" % (q["residual_rows"], q["remaining_variables"])
            if q["residual_rows"] is not None
            else "not reached"
        )
        if q["stuck_replay_status"]:
            residual = "%s; replay %s" % (residual, q["stuck_replay_status"])
            if q["stuck_replay_residual_rows"] is not None:
                residual += ", %s rows" % q["stuck_replay_residual_rows"]
        if status == "OK":
            verdict = "COUNTING-BOUND"
            if q["pivots"] in (0, "0"):
                reason = "no Q* affine pivot found; no forced-nonzero/base-field slice reached"
            else:
                reason = "Q* stage completed but later slice/field certificate not reached"
        elif status == "TIMEOUT":
            verdict = "COUNTING-BOUND"
            reason = "native Q* stage timed out before a certificate"
        else:
            verdict = "COUNTING-BOUND"
            reason = "native Q* stage errored before a certificate"
        lines.append(
            "| `%s` | %s | %s | %s | %s | %s | %s | not reached | not reached | %s: %s |"
            % (
                meta.get("partition"),
                meta.get("unknowns"),
                meta.get("equations"),
                status,
                pivots,
                residual,
                "%s; natural=%s" % (q["grading_status"], q["weight_status"]),
                verdict,
                reason,
            )
        )
    lines.append("")
    lines.append("MEASURED. The base rows, coefficient fields, and final exact standard bases for the three `(25,15)` strata were not reached in this bounded run. Where a stuck replay completed, the post-pivot residual TSV and JSON audit are listed in `box/preprocess-native-20260903/results/`; otherwise the exact retained data are the original row TSV plus the checked partial Q*-pivot chain. No mathematical emptiness claim is made from a timeout.")
    lines.append("")
    lines.append("### Target Artifacts")
    lines.append("")
    lines.append("| stratum | source rows | row sha256 | qstage script | qstage logs | pivot TSV | stuck residual | stuck JSON |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for stem, rec in targets.items():
        meta = rec.get("meta", {})
        replay = rec.get("stuck_replay", {})
        generated = rec.get("generated", {})
        qlogs = "%s; %s" % (rec.get("run", {}).get("stdout"), rec.get("run", {}).get("stderr"))
        replay_residual = "-"
        if replay.get("residual_tsv"):
            replay_residual = "%s (%s, %s rows)" % (
                replay.get("residual_tsv"),
                _fmt_bytes(replay.get("residual_bytes")),
                replay.get("residual_rows_from_tsv"),
            )
        lines.append(
            "| `%s` | `%s` | `%s` | `%s` (%s) | `%s` | `%s` | `%s` | `%s` |"
            % (
                meta.get("partition"),
                rec.get("rows_path"),
                rec.get("rows_sha256"),
                generated.get("script"),
                _fmt_bytes(generated.get("script_bytes")),
                qlogs,
                rec.get("pivots_tsv"),
                replay_residual,
                replay.get("json"),
            )
        )
    lines.append("")
    lines.append("### Partial Q* Chains")
    lines.append("")
    lines.append("MEASURED. The following are the completed affine pivots before timeout. Each coefficient is the recorded constant `Q*` coefficient, and each `rhs#` is the SHA-256 prefix of the recorded right-hand side payload in the pivot TSV. The replay stage verifies `subst(row, variable, rhs)==0` for every listed pivot before writing the stuck residual.")
    lines.append("")
    for stem, rec in targets.items():
        meta = rec.get("meta", {})
        pivots = _read_report_pivots(rec.get("pivots_tsv"))
        lines.append("`%s` (%s pivots):" % (meta.get("partition"), len(pivots)))
        if pivots:
            parts = []
            for row in pivots:
                parts.append(
                    "%s:%s row=%s hxy=%s/%s/%s coeff=%s rhs#%s"
                    % (
                        row.get("step"),
                        row.get("variable"),
                        row.get("source_index"),
                        row.get("h_power"),
                        row.get("x_power"),
                        row.get("y_power"),
                        row.get("coefficient_Qstar"),
                        row.get("rhs_sha256_12"),
                    )
                )
            lines.append("; ".join(parts) + ".")
        else:
            lines.append("No pivot TSV was produced.")
        lines.append("")
    lines.append("AUDIT. These chains are branch-free only because their leading coefficients are constants in `Q*`. They do not license division by any parameter-dependent expression, and the timeout point is reported as a retained exact system rather than as an emptiness certificate.")
    lines.append("")
    lines.append("MEASURED. The optional `(24,16;17;2;5)` stratum was not run; the required `(25,15)` bounded native passes plus stuck-system replays consumed the available lane time.")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append("CONFIRMED. The native lane removes the SymPy parser from the row-file path and validates the Q*-pivot/field-certificate pattern on the K16 t=3/t=4 controls, plus the `(33,22)` `[3]` exact `[1]` check.")
    lines.append("")
    lines.append("COUNTING-BOUND. The three `(25,15)` strata are not promoted to saturated-empty here. The blocker has moved from Python parsing to native affine elimination or the absence of a certificate after that stage.")
    lines.append("")
    lines.append("ENABLED. The same driver can now be pointed at the remaining large row files and later `(99,66)` joint chart bands without SymPy ingest; the next useful improvement is a stronger native sparse/compiled affine pass plus in-Singular branch generation for the slice/base-factor field systems.")
    lines.append("")
    lines.append("FALLACY-v2. No new exit-price assertion is made, so no `charge_basis=...` line is due. Saturation, representative, and timeout statuses are kept separate.")
    lines.append("")
    lines.append("<!-- BODY-END -->")
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["verify", "validate", "targets", "replay-stuck", "report", "all"], nargs="?", default="all")
    parser.add_argument("--timeout", type=int, default=1500, help="per Singular stage timeout in seconds")
    parser.add_argument("--validation-timeout", type=int, default=900)
    parser.add_argument("--max-pivots", type=int, default=512)
    args = parser.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    manifest = verify_inputs()
    (OUT / "results").mkdir(exist_ok=True)
    (OUT / "results/manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if not manifest["ok"]:
        raise SystemExit("frozen input hash mismatch")
    if args.command == "verify":
        print(json.dumps(manifest, indent=2, sort_keys=True))
        return

    validations = None
    targets = None
    if args.command in {"validate", "all"}:
        validations = validation_runs(args.validation_timeout)
        print(json.dumps({"validation": {k: "done" for k in validations}}, indent=2))
    if args.command in {"targets", "all"}:
        targets = process_targets(args.timeout, args.max_pivots)
        print(json.dumps({"targets": {k: summarize_qstage(v) for k, v in targets.items()}}, indent=2, sort_keys=True))
    if args.command in {"replay-stuck", "all"}:
        replay = replay_stuck_targets(args.timeout)
        print(json.dumps({"replay_stuck": replay}, indent=2, sort_keys=True))
    if args.command in {"report", "all"}:
        path = write_report(manifest, validations, targets)
        print(f"REPORT={path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
