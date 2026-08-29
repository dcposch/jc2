#!/usr/bin/env python3
"""Compile and aggregate a disjoint exact-Q(t) shard census for V43G5."""

from __future__ import annotations

import argparse
from hashlib import sha256
import importlib.util
import json
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
V43G5 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_generic_certificate_circuit_v43g5_20260827"
COMPILER = V43G5 / "compile_certificate_circuit_v43g5.py"
COMPILER_SHA256 = "95910e9f93bc007029da9bc89a8a443b18dfcac5165c8a3e79744cd6aa9cde62"
RUNNER_SHA256 = "8e3c995a24bb9d91ae18adfe0cd9fee906112a2e272816cb8225cf7b532249be"
PREREG_SHA256 = "43d466eed8a2feb80057cbc9ca2b37fb9ec35ec9d50c136ee941a3bfe8039745"
LIVE_COMPILER_RESULT_SHA256 = "7b01bd703c3618b65962bcbe73831d4963112d13a47a73400796dcdbe7e14f10"
TAG_PREFIX = "max12_812_order2_p0_total_rees_j2_a1_generic_certificate_circuit_shards_v43g5s_"
SHARDS = 32
MASKS = 2048


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def fail(message: object) -> "None":
    raise RuntimeError(message)


def require_aws() -> str:
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if (platform.system() != "Linux" or not vendor.is_file()
            or vendor.read_text().strip() != "Amazon EC2"
            or not tag.startswith(TAG_PREFIX)):
        fail("registered V43G5S AWS lane required")
    return tag


def load_v43g5():
    pins = (
        (COMPILER, COMPILER_SHA256),
        (V43G5 / "run_aws.sh", RUNNER_SHA256),
        (V43G5 / "PREREGISTRATION.md", PREREG_SHA256),
    )
    for path, expected in pins:
        if digest(path) != expected:
            fail(("predecessor pin", str(path), digest(path), expected))
    spec = importlib.util.spec_from_file_location("frozen_v43g5", COMPILER)
    if spec is None or spec.loader is None:
        fail("V43G5 import")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compile_shards(output: Path) -> None:
    tag = require_aws()
    output.mkdir(parents=True, exist_ok=False)
    v = load_v43g5()
    _, _, expressions, active = v.frozen_payload()
    if len(expressions) != 11 or len(active) != 30 or v.FULL_MASK != 2047:
        fail(("predecessor census", len(expressions), len(active), v.FULL_MASK))
    declarations = [f"poly R{i}={expression};" for i, expression in enumerate(expressions)]
    scripts = []
    for shard in range(SHARDS):
        start = shard * (MASKS // SHARDS)
        stop = (shard + 1) * (MASKS // SHARDS)
        path = output / f"qfield_shard_{shard:02d}_{start:04d}_{stop - 1:04d}.sing"
        lines = [
            f"ring K=(0,t),({','.join(active)}),dp;",
            "option(redSB);",
            *declarations,
            "ideal JJ; ideal GG; poly nf; int unit;",
        ]
        for mask in range(start, stop):
            if mask == 0:
                lines.append('print("V43G5S_QT_MASK_0=0");')
                continue
            lines += [
                f"JJ={v.ideal_for(mask)};",
                "GG=std(JJ); nf=reduce(1,GG); unit=0; if (nf==0) { unit=1; }",
                f'print("V43G5S_QT_MASK_{mask}="+string(unit));',
            ]
        lines += [
            f'print("V43G5S_RANGE_{start}_{stop - 1}_COUNT={stop - start}");',
            f'print("PASS_A1_GENERIC_CIRCUIT_QT_V43G5S_SHARD_{shard:02d}");',
            "quit;",
        ]
        path.write_text("\n".join(lines) + "\n")
        scripts.append({
            "shard": shard,
            "start": start,
            "stop_exclusive": stop,
            "path": str(path),
            "sha256": digest(path),
        })
    record = {
        "status": "PASS-V43G5S-COMPILER",
        "registered_aws_lane": tag,
        "shards": scripts,
        "shard_count": SHARDS,
        "masks_per_shard": MASKS // SHARDS,
        "mask_count": MASKS,
        "support": v.SUPPORT,
        "active_variables": active,
        "predecessor_compiler_sha256": COMPILER_SHA256,
        "live_predecessor_compiler_result_sha256": LIVE_COMPILER_RESULT_SHA256,
    }
    result = output / "compiler_result.json"
    result.write_text(json.dumps(record, sort_keys=True, indent=2) + "\n")
    print("V43G5S_SHARDS=32")
    print("V43G5S_MASKS_PER_SHARD=64")
    print("PASS-V43G5S-COMPILER")
    print("RESULT_SHA256=" + digest(result))


def aggregate(output: Path, run_dir: Path) -> None:
    require_aws()
    v = load_v43g5()
    compiler = json.loads((output / "compiler_result.json").read_text())
    if compiler.get("status") != "PASS-V43G5S-COMPILER":
        fail("compiler record")
    marker = re.compile(r"V43G5S_QT_MASK_(\d+)=(\d+)$")
    table: dict[int, int] = {}
    shard_hashes = {}
    for item in compiler["shards"]:
        shard = item["shard"]
        path = run_dir / f"shard_{shard:02d}.stdout"
        text = path.read_text()
        terminal = f"PASS_A1_GENERIC_CIRCUIT_QT_V43G5S_SHARD_{shard:02d}"
        if text.count(terminal) != 1:
            fail(("terminal marker", shard, text.count(terminal)))
        expected_range = set(range(item["start"], item["stop_exclusive"]))
        observed = set()
        for line in text.splitlines():
            match = marker.fullmatch(line.strip())
            if not match:
                continue
            mask, value = map(int, match.groups())
            if mask in table or mask in observed:
                fail(("duplicate mask", mask, shard))
            if value not in (0, 1):
                fail(("nonboolean", mask, value))
            observed.add(mask)
            table[mask] = value
        if observed != expected_range:
            fail(("shard range", shard, len(observed), sorted(expected_range - observed)[:8],
                  sorted(observed - expected_range)[:8]))
        shard_hashes[str(shard)] = digest(path)
    if set(table) != set(range(MASKS)) or table[0] != 0 or table[2047] != 1:
        fail(("aggregate census", len(table), table.get(0), table.get(2047)))
    for mask, value in table.items():
        if value:
            for supermask in range(mask, MASKS):
                if (supermask & mask) == mask and table[supermask] != 1:
                    fail(("unit monotonicity", mask, supermask))
    minimal = [
        mask for mask in range(1, MASKS) if table[mask]
        and all(not table[mask ^ (1 << bit)]
                for bit in range(11) if mask & (1 << bit))
    ]
    result = {
        "status": "PASS-V43G5S-EXACT-QT-SUBSET-CENSUS",
        "mask_count": MASKS,
        "unit_count": sum(table.values()),
        "minimal_unit_masks": minimal,
        "minimal_unit_supports": [
            [v.SUPPORT[bit] for bit in range(11) if mask & (1 << bit)]
            for mask in minimal
        ],
        "table": [table[i] for i in range(MASKS)],
        "shard_stdout_sha256": shard_hashes,
        "compiler_result_sha256": digest(output / "compiler_result.json"),
    }
    path = output / "aggregate_result.json"
    path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("V43G5S_MASKS=2048")
    print("V43G5S_UNIT_COUNT=" + str(result["unit_count"]))
    print("V43G5S_MINIMAL_UNIT_COUNT=" + str(len(minimal)))
    print("V43G5S_MINIMAL_UNIT_MASKS=" + ",".join(map(str, minimal)))
    print("PASS-V43G5S-EXACT-QT-SUBSET-CENSUS")
    print("RESULT_SHA256=" + digest(path))


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--phase", choices=("compile", "aggregate"), required=True)
    cli.add_argument("--run-dir", type=Path)
    args = cli.parse_args()
    if args.phase == "compile":
        compile_shards(args.output.resolve())
    else:
        if args.run_dir is None:
            fail("--run-dir required")
        aggregate(args.output.resolve(), args.run_dir.resolve())


if __name__ == "__main__":
    main()
