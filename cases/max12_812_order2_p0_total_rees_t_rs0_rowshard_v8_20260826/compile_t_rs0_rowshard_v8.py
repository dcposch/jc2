#!/usr/bin/env python3
"""Explicit-normal-form, incrementally truncated T-rs-0 row shards."""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import re
from tempfile import TemporaryDirectory


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V7_COMPILER = ROOT / "cases/max12_812_order2_p0_total_rees_t_rs0_rowshard_v7_20260826/compile_t_rs0_rowshard_v7.py"
V7_COMPILER_SHA256 = "c678d293c2c26462c3ca5cc3776644b181176a2cf657b0beb6b65754c7dcd2d0"
PREREG = HERE / "PREREGISTRATION.md"
CHARACTERISTICS = (0, 32003, 65521, 1000033)
IMPLEMENTATION = "ROW_SHARD_INCREMENTAL_NF_V8"
SOURCE_POLY = re.compile(r"^poly ([TF]_[A-Za-z0-9_]+)=(.*);$")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (
        platform.system() != "Linux"
        or not vendor.is_file()
        or vendor.read_text().strip() != "Amazon EC2"
        or not tag.startswith("max12_812_order2_p0_total_rees_t_rs0_rowshard_v8_")
    ):
        fail("rowshard V8 compiler requires a registered AWS EC2 lane")
    return tag


def load_v7():
    actual = digest(V7_COMPILER)
    if actual != V7_COMPILER_SHA256:
        fail(("V7 compiler hash mismatch", actual, V7_COMPILER_SHA256))
    spec = importlib.util.spec_from_file_location("t_rs0_rowshard_v7_frozen", V7_COMPILER)
    if spec is None or spec.loader is None:
        fail("cannot import frozen V7 compiler")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def formula_data(old, base, tails: dict[str, list[list[object]]], row: int, prefix: str):
    coeffs = {index: f"{prefix}F{index}" for index in range(7)}
    loads = {"k10": f"{prefix}K10", "k6": f"{prefix}K6", "k2": f"{prefix}K2"}
    entries = tails[str(row)]
    # Calling the frozen formatter performs its literal length, load, and
    # weight checks.  Exact text equality guards this successor's schedule.
    tail_text = base.tail_text(entries, row, coeffs, loads).replace("Lambda", "(sigma^2)")
    targets = {1: "0", 2: "mu2", 3: "0", 4: "mu4", 5: "0", 6: "mu6", 7: "J/4"}
    expected = tail_text
    if targets[row] != "0":
        expected += f"-sigma^{2 * (12 + row)}*({targets[row]})"
    legacy = old.phi_text(base, tails, row, prefix)
    if expected != legacy:
        fail(("legacy formula text mismatch", row, prefix, sha256(expected.encode()).hexdigest(), sha256(legacy.encode()).hexdigest()))

    max_powers = [0] * 7
    parsed: list[tuple[list[int], Fraction]] = []
    for raw_monomial, raw_coefficient in entries:
        monomial = [int(value) for value in raw_monomial]
        coefficient = Fraction(str(raw_coefficient))
        parsed.append((monomial, coefficient))
        for index, exponent in enumerate(monomial[:7]):
            max_powers[index] = max(max_powers[index], exponent)
    return parsed, max_powers, targets[row], legacy


def rational_text(base, value: Fraction) -> str:
    return base.rational_text(value)


def build_schedule(old, base, tails, row: int, prefix: str, accumulator: str) -> tuple[list[str], int, str]:
    entries, max_powers, target, legacy = formula_data(old, base, tails, row, prefix)
    lines: list[str] = []
    for index, maximum in enumerate(max_powers):
        if maximum < 2:
            continue
        previous = f"{prefix}F{index}"
        for exponent in range(2, maximum + 1):
            name = f"{prefix}F{index}pow{exponent}"
            lines.append(f"poly {name}=reduce({previous}*{prefix}F{index},PrefixNF);")
            previous = name

    lines.append(f"{accumulator}=0;")
    update_count = 0
    load_names = ("K10", "K6", "K2")
    load_weights = (2, 6, 10)
    for monomial, coefficient in entries:
        lines.append(f"BuildTerm={rational_text(base, coefficient)};")
        lambda_power = sum(exponent * weight for exponent, weight in zip(monomial[7:], load_weights))
        if lambda_power:
            lines.append(f"BuildTerm=reduce(BuildTerm*sigma^{2 * lambda_power},PrefixNF);")
        for index, exponent in enumerate(monomial[:7]):
            if exponent == 0:
                continue
            factor = f"{prefix}F{index}" if exponent == 1 else f"{prefix}F{index}pow{exponent}"
            lines.append(f"BuildTerm=reduce(BuildTerm*{factor},PrefixNF);")
        for offset, exponent in enumerate(monomial[7:]):
            if exponent:
                factor = f"{prefix}{load_names[offset]}"
                lines.append(f"BuildTerm=reduce(BuildTerm*{factor},PrefixNF);")
        lines.append(f"{accumulator}=reduce({accumulator}+BuildTerm,PrefixNF);")
        update_count += 1
    if target != "0":
        lines.append(f"BuildTerm=reduce(-sigma^{2 * (12 + row)}*({target}),PrefixNF);")
        lines.append(f"{accumulator}=reduce({accumulator}+BuildTerm,PrefixNF);")
        update_count += 1
    return lines, update_count, sha256(legacy.encode()).hexdigest()


def transform_program(
    source: Path,
    destination: Path,
    staging: Path,
    output: Path,
    old,
    base,
    tails,
    row: int,
) -> tuple[int, str]:
    transformed: list[str] = []
    t_updates = f_updates = -1
    t_hash = f_hash = ""
    for line in source.read_text().splitlines():
        if line == "qring Q=PrefixIdeal;":
            transformed += [
                "ideal PrefixNF=PrefixIdeal;",
                "poly PrefixCanary=reduce(sigma^13*ell1,PrefixNF);",
                "int explicitNF=(PrefixCanary==0);",
                "poly BuildTerm=0;",
            ]
            continue
        if line == 'print("T_RS0_IMPLEMENTATION=ROW_SHARD_DIFFSCAN_V6");':
            transformed += [
                f'print("T_RS0_IMPLEMENTATION={IMPLEMENTATION}");',
                'print("T_RS0_PREFIX_ALGEBRA=PARENT_RING_EXPLICIT_NORMAL_FORM");',
                'print("T_RS0_QRING_DISABLED=1");',
            ]
            continue
        match = SOURCE_POLY.match(line)
        if match:
            name, expression = match.groups()
            transformed.append(f"poly {name}=reduce({expression},PrefixNF);")
            continue
        if line.startswith("TPhi=") and line != "TPhi=0;":
            schedule, t_updates, t_hash = build_schedule(old, base, tails, row, "T_", "TPhi")
            transformed.extend(schedule)
            continue
        if line.startswith("FPhi=") and line != "FPhi=0;":
            schedule, f_updates, f_hash = build_schedule(old, base, tails, row, "F_", "FPhi")
            transformed.extend(schedule)
            continue
        if line.startswith('print("T_RS0_SHARD_ROW='):
            transformed += [
                'print("T_RS0_EXPLICIT_NORMAL_FORM="+string(explicitNF));',
                'print("T_RS0_INCREMENTAL_REDUCTION=1");',
                line,
            ]
            continue
        if line == 'if (prefixMap*deck*extraction*coefficientMap!=1) { print("T_RS0_FAIL=ROW_SOURCE_FIDELITY"); quit(91); }':
            transformed.append('if (prefixMap*deck*extraction*coefficientMap*explicitNF!=1) { print("T_RS0_FAIL=ROW_SOURCE_FIDELITY_OR_NORMAL_FORM"); quit; }')
            continue
        transformed.append(line.replace(str(staging), str(output)))

    if t_updates < 0 or f_updates < 0 or not t_hash or not f_hash:
        fail(("formula assignment not transformed", row, t_updates, f_updates))
    text = "\n".join(transformed) + "\n"
    if "qring " in text or "quit(" in text:
        fail(("forbidden qring or numeric quit survived", row))
    if text.count("PrefixNF") < 10:
        fail(("explicit normal-form census too small", row, text.count("PrefixNF")))
    if text.count("if (diff(TPhi,") != 83:
        fail(("dependency derivative census", row, text.count("if (diff(TPhi,")))
    destination.write_text(text)
    formula_hash = sha256((t_hash + f_hash).encode()).hexdigest()
    return t_updates + f_updates, formula_hash


def compile_rows(output: Path, characteristic: int, tag: str) -> dict[str, object]:
    v7 = load_v7()
    v6 = v7.load_v6()
    stream = v6.load_stream()
    old = stream.load_old()
    base = old.load_base()
    tails = json.loads(old.TAILS.read_text())

    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    label = "q" if characteristic == 0 else f"p{characteristic}"
    row_hashes: dict[str, str] = {}
    formula_hashes: dict[str, str] = {}
    update_counts: dict[str, int] = {}
    with TemporaryDirectory(prefix="t_rs0_v8_") as temporary:
        # TemporaryDirectory creates its root eagerly; the frozen V7 emitter
        # is fail-closed and requires a path that does not yet exist.
        staging = (Path(temporary) / "v7_baseline").resolve()
        baseline = v7.compile_rows(staging, characteristic, tag)
        for row in range(1, 8):
            source = staging / f"t_rs0_row{row}_{label}.sing"
            destination = output / source.name
            updates, formula_hash = transform_program(source, destination, staging, output, old, base, tails, row)
            row_hashes[str(row)] = digest(destination)
            formula_hashes[str(row)] = formula_hash
            update_counts[str(row)] = updates

    keep_files = {
        key: str(output / f"{key}.poly")
        for key in ("KeepT10_2", "KeepF10_2", "KeepT10_3", "KeepF10_3", "KeepT12_6", "KeepF12_6")
    }
    result = {
        **baseline,
        "status": "PASS-T-RS0-ROW-SHARD-V8-COMPILER",
        "implementation": IMPLEMENTATION,
        "compiler_successor": "EXPLICIT_NORMAL_FORM_INCREMENTAL_V8",
        "registered_aws_lane": tag,
        "prefix_algebra": "PARENT_RING_EXPLICIT_NORMAL_FORM_MOD_SIGMA13",
        "qring_used": False,
        "incremental_reduction": True,
        "v7_compiler_sha256": V7_COMPILER_SHA256,
        "preregistration_sha256": digest(PREREG),
        "row_input_sha256": row_hashes,
        "row_formula_pair_sha256": formula_hashes,
        "row_incremental_update_count": update_counts,
        "keep_files": keep_files,
    }
    (output / "result.json").write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--characteristic", type=int, choices=CHARACTERISTICS, required=True)
    args = parser.parse_args()
    tag = require_aws()
    result = compile_rows(args.output, args.characteristic, tag)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
