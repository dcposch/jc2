#!/usr/bin/env python3
"""Compile and validate the exact eleven-row certificate-circuit search."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
G3 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_full_generic_qt_lift_v43g3_20260827"
G3_FREEZE = G3 / "FREEZE.sha256"
G3_FREEZE_SHA256 = "8f60b30576e1712479e09cc01c3244c6ff5c7053c0d3cd08e9d4fbad8745ca45"
G3_RESULT = G3 / "RESULT.md"
G3_RESULT_SHA256 = "6db87ebacaa175c68dca5739dbad35390d36ff62ff914859c82a1d60e79270c4"
G3_AWS = G3 / "aws_r6a_lift_20260827T110250Z/compiled"
G3_JSON = G3_AWS / "compiler_result.json"
G3_JSON_SHA256 = "1c00aef261a3d674cb1b63f4fad18cf0121b9bcb6711a2103e893bab7a83758e"
G3_SCRIPT = G3_AWS / "generic_qt_tracked_lift.sing"
G3_SCRIPT_SHA256 = "0bca5e57db93e620c8f1f9ad52ea50b3f16ab4d01ad0326cab96009bbe803893"
G4 = ROOT / "cases/max12_812_order2_p0_total_rees_j2_a1_generic_rehom_v43g4_20260827"
G4_FREEZE = G4 / "FREEZE.sha256"
G4_FREEZE_SHA256 = "777927795b59509c56c2d971b82db9be05ab7f33a7449b0f1947d28f4a201b91"
G4_RESULT = G4 / "RESULT.md"
G4_RESULT_SHA256 = "ae7beed3e677a46bda82778ae6bbeb1a8aef74dcbf8db35df07f02d183b70015"
G4_JSON = G4 / "aws_r6b_rehom_20260827T111531Z/RESULT.json"
G4_JSON_SHA256 = "e97ebd6a893e73d8e3751692b56300f0df230a75184f20b05d91282ac455e962"
PREREG = HERE / "PREREGISTRATION.md"
TAG_PREFIX = "max12_812_order2_p0_total_rees_j2_a1_generic_certificate_circuit_v43g5_"
SUPPORT = [
    "Tg11_2", "Tg11_7", "Tg12_2", "Tg12_7", "Tg13_5", "Tg13_7",
    "Tg14_5", "Tg14_7", "Tg15_3", "Tg15_5", "Tg15_7",
]
FULL_MASK = (1 << len(SUPPORT)) - 1


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
        or not tag.startswith(TAG_PREFIX)
        or "_exact_circuit_" not in tag
    ):
        fail("registered V43G5 AWS circuit lane required")
    return tag


def verify_freeze(path: Path, expected_hash: str) -> None:
    if digest(path) != expected_hash:
        fail(("freeze manifest hash", str(path), digest(path), expected_hash))
    for line in path.read_text().splitlines():
        expected, relative = line.split(maxsplit=1)
        candidate = ROOT / relative
        if digest(candidate) != expected:
            fail(("frozen dependency", relative, digest(candidate), expected))


def frozen_payload():
    for path, expected in (
        (G3_RESULT, G3_RESULT_SHA256),
        (G3_JSON, G3_JSON_SHA256),
        (G3_SCRIPT, G3_SCRIPT_SHA256),
        (G4_RESULT, G4_RESULT_SHA256),
        (G4_JSON, G4_JSON_SHA256),
    ):
        if digest(path) != expected:
            fail(("custody hash", str(path), digest(path), expected))
    verify_freeze(G3_FREEZE, G3_FREEZE_SHA256)
    verify_freeze(G4_FREEZE, G4_FREEZE_SHA256)
    g3 = json.loads(G3_JSON.read_text())
    g4 = json.loads(G4_JSON.read_text())
    if (
        g3.get("status") != "PASS-A1-GENERIC-QT-LIFT-V43G3-COMPILER"
        or g3.get("g2_ring_and_all_58_entries_byte_equal") is not True
        or g3.get("reduced_row_count") != 58
        or len(g3.get("reduced_variables", [])) != 64
        or g4.get("status") != "PASS-A1-GENERIC-REHOM-V43G4"
        or g4.get("honest_total_identity") != "5*t^6*a1^4=sum H_i*Tg_i"
        or g4.get("used_rows") != SUPPORT
        or g4.get("sigma_projection_dropped_terms") != 0
    ):
        fail("G3/G4 semantic pins")
    lines = G3_SCRIPT.read_text().splitlines()
    if not lines or not lines[0].startswith("ring K=(0,t),"):
        fail("G3 ring declaration")
    start = lines.index("ideal J=") + 1
    entries = lines[start:start + 58]
    if len(entries) != 58 or not entries[-1].endswith(";"):
        fail("G3 ideal payload")
    expressions = [entry[:-1] for entry in entries]
    by_name = dict(zip(g3["reduced_rows"], expressions))
    if set(SUPPORT) - set(by_name):
        fail("support row missing")
    selected = [by_name[name] for name in SUPPORT]
    all_variables = list(g3["reduced_variables"])
    tokens = set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*", "\n".join(selected)))
    if tokens - set(all_variables) - {"t"}:
        fail(("unexpected row tokens", sorted(tokens - set(all_variables) - {"t"})))
    active = [name for name in all_variables if name in tokens]
    if len(active) != 30:
        fail(("active-variable census", len(active), active))
    return g3, g4, selected, active


def row_declarations(expressions: list[str]) -> list[str]:
    return [f"poly R{index}={expression};" for index, expression in enumerate(expressions)]


def ideal_for(mask: int) -> str:
    rows = [f"R{index}" for index in range(len(SUPPORT)) if mask & (1 << index)]
    return ",".join(rows) if rows else "0"


def compile_scripts(output: Path, tag: str) -> None:
    output.mkdir(parents=True, exist_ok=False)
    g3, g4, expressions, active = frozen_payload()
    qfield = output / "qfield_all_subsets.sing"
    qlines = [
        f"ring K=(0,t),({','.join(active)}),dp;",
        "option(redSB);",
        *row_declarations(expressions),
        "ideal JJ; ideal GG; poly nf; int unit;",
        'print("V43G5_QT_MASK_0=0");',
    ]
    for mask in range(1, FULL_MASK + 1):
        qlines += [
            f"JJ={ideal_for(mask)};",
            "GG=std(JJ); nf=reduce(1,GG); unit=0; if (nf==0) { unit=1; }",
            f'print("V43G5_QT_MASK_{mask}="+string(unit));',
        ]
    qlines += [
        f'print("V43G5_QT_SUBSETS={FULL_MASK + 1}");',
        'print("PASS_A1_GENERIC_CIRCUIT_QT_V43G5");',
        "quit;",
    ]
    qfield.write_text("\n".join(qlines) + "\n")

    pole = output / "full_support_pole.sing"
    pole_multiplier_paths = [output / f"full_pole_multiplier_{i + 1:02d}_{name}.poly"
                             for i, name in enumerate(SUPPORT)]
    plines = [
        f"ring P=0,(t,{','.join(active)}),dp;",
        "option(redSB);",
        *row_declarations(expressions),
        f"ideal JJ={ideal_for(FULL_MASK)};",
        "matrix TT; ideal GG=liftstd(JJ,TT);",
        "matrix BR=matrix(JJ)*TT-matrix(GG);",
        'if (BR!=0) { print("FAIL_V43G5_FULL_BASIS_REPLAY"); quit; }',
        "int s; int minpole=-1; poly nf; poly target;",
        "for (s=0;s<=6;s++)",
        "{",
        "  if (s==0) { target=1; } else { target=t^s; }",
        "  nf=reduce(target,GG);",
        '  if (nf==0) { print("V43G5_FULL_POLE_MEMBER_"+string(s)+"=1"); if (minpole<0) { minpole=s; } }',
        '  else { print("V43G5_FULL_POLE_MEMBER_"+string(s)+"=0"); }',
        "}",
        'if (minpole<0) { print("FAIL_V43G5_NO_POLE_LE6"); quit; }',
        "if (minpole==0) { target=1; } else { target=t^minpole; }",
        "matrix HH=lift(GG,ideal(target)); matrix CC=TT*HH;",
        "matrix RR=matrix(JJ)*CC-matrix(ideal(target));",
        'if (RR!=0) { print("FAIL_V43G5_FULL_POLE_REPLAY"); quit; }',
        "int ci; int nonzero=0; int chosen=0;",
        "for (ci=1;ci<=nrows(CC);ci++) { if (CC[ci,1]!=0) { nonzero=nonzero+1; if (chosen==0) { chosen=ci; } } }",
        'if (chosen==0) { print("FAIL_V43G5_EMPTY_CERTIFICATE"); quit; }',
        "matrix MUT=matrix(JJ); MUT[1,chosen]=MUT[1,chosen]+1;",
        "matrix MR=MUT*CC-matrix(ideal(target));",
        'if (MR==0) { print("FAIL_V43G5_ROW_MUTATION_CONTROL"); quit; }',
    ]
    for index, path in enumerate(pole_multiplier_paths, start=1):
        plines.append(f'write("{path}",CC[{index},1]);')
    plines += [
        'print("V43G5_FULL_MIN_POLE="+string(minpole));',
        'print("V43G5_FULL_NONZERO_MULTIPLIERS="+string(nonzero));',
        'print("V43G5_FULL_MUTATED_ROW_INDEX="+string(chosen));',
        'print("PASS_A1_GENERIC_FULL_POLE_V43G5");',
        "quit;",
    ]
    pole.write_text("\n".join(plines) + "\n")
    result = {
        "status": "PASS-A1-GENERIC-CIRCUIT-V43G5-COMPILER",
        "registered_aws_lane": tag,
        "support": SUPPORT,
        "support_size": len(SUPPORT),
        "subset_count": FULL_MASK + 1,
        "active_variables": active,
        "active_variable_count": len(active),
        "row_expressions_sha256": {
            name: sha256(expression.encode()).hexdigest()
            for name, expression in zip(SUPPORT, expressions)
        },
        "qfield_script": str(qfield),
        "qfield_script_sha256": digest(qfield),
        "full_pole_script": str(pole),
        "full_pole_script_sha256": digest(pole),
        "full_pole_multiplier_paths": [str(path) for path in pole_multiplier_paths],
        "g3_freeze_sha256": G3_FREEZE_SHA256,
        "g4_freeze_sha256": G4_FREEZE_SHA256,
        "g3_script_sha256": G3_SCRIPT_SHA256,
        "g4_result_json_sha256": G4_JSON_SHA256,
        "preregistration_sha256": digest(PREREG),
    }
    result_path = output / "compiler_result.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("V43G5_SUPPORT_ROWS=11")
    print("V43G5_ACTIVE_VARIABLES=30")
    print("V43G5_SUBSETS=2048")
    print("PASS-A1-GENERIC-CIRCUIT-V43G5-COMPILER")
    print(f"RESULT_SHA256={digest(result_path)}")


def parse_marker_table(path: Path, prefix: str) -> dict[int, int]:
    table = {}
    pattern = re.compile(re.escape(prefix) + r"(\d+)=(-?\d+)$")
    for line in path.read_text().splitlines():
        match = pattern.fullmatch(line.strip())
        if match:
            key = int(match.group(1))
            if key in table:
                fail(("duplicate marker", prefix, key))
            table[key] = int(match.group(2))
    return table


def analyze(output: Path, qfield_stdout: Path, pole_stdout: Path) -> None:
    _, _, expressions, active = frozen_payload()
    qtext = qfield_stdout.read_text()
    ptext = pole_stdout.read_text()
    if qtext.count("PASS_A1_GENERIC_CIRCUIT_QT_V43G5") != 1:
        fail("qfield terminal marker")
    if ptext.count("PASS_A1_GENERIC_FULL_POLE_V43G5") != 1:
        fail("pole terminal marker")
    units = parse_marker_table(qfield_stdout, "V43G5_QT_MASK_")
    if set(units) != set(range(FULL_MASK + 1)) or units[0] != 0 or units[FULL_MASK] != 1:
        fail(("subset table census", len(units), units.get(0), units.get(FULL_MASK)))
    for mask, value in units.items():
        if value not in (0, 1):
            fail(("nonboolean unit marker", mask, value))
        if value:
            for supermask in range(mask, FULL_MASK + 1):
                if (supermask & mask) == mask and units[supermask] != 1:
                    fail(("unit monotonicity", mask, supermask))
    minimal = [
        mask for mask in range(1, FULL_MASK + 1)
        if units[mask] and all(not units[mask ^ (1 << bit)]
                               for bit in range(len(SUPPORT)) if mask & (1 << bit))
    ]
    if not minimal:
        fail("no minimal unit support")
    pole_table = parse_marker_table(pole_stdout, "V43G5_FULL_POLE_MEMBER_")
    if set(pole_table) != set(range(7)):
        fail(("pole table census", pole_table))
    members = [s for s, value in pole_table.items() if value == 1]
    if not members:
        fail("positive V43G4 pole control missing")
    minpole = min(members)
    marker = re.findall(r"^V43G5_FULL_MIN_POLE=(\d+)$", ptext, re.M)
    if marker != [str(minpole)]:
        fail(("minimum-pole marker", marker, minpole))
    analysis = {
        "status": "PASS-A1-GENERIC-CIRCUIT-V43G5-ANALYSIS",
        "unit_subset_count": sum(units.values()),
        "inclusion_minimal_masks": minimal,
        "inclusion_minimal_supports": [
            [SUPPORT[bit] for bit in range(len(SUPPORT)) if mask & (1 << bit)]
            for mask in minimal
        ],
        "full_support_minimum_t_pole": minpole,
        "full_support_membership_s_0_through_6": pole_table,
        "active_variables": active,
        "row_expression_sha256": [sha256(expression.encode()).hexdigest()
                                  for expression in expressions],
        "qfield_stdout_sha256": digest(qfield_stdout),
        "pole_stdout_sha256": digest(pole_stdout),
    }
    path = output / "analysis.json"
    path.write_text(json.dumps(analysis, sort_keys=True, indent=2) + "\n")
    print(f"V43G5_UNIT_SUBSETS={sum(units.values())}")
    print("V43G5_MINIMAL_MASKS=" + ",".join(map(str, minimal)))
    print(f"V43G5_MINIMUM_T_POLE={minpole}")
    print("PASS-A1-GENERIC-CIRCUIT-V43G5-ANALYSIS")
    print(f"RESULT_SHA256={digest(path)}")


def main() -> None:
    cli = argparse.ArgumentParser()
    cli.add_argument("output", type=Path)
    cli.add_argument("--phase", choices=("compile", "analyze"), required=True)
    cli.add_argument("--qfield-stdout", type=Path)
    cli.add_argument("--pole-stdout", type=Path)
    args = cli.parse_args()
    tag = require_aws()
    if args.phase == "compile":
        if args.qfield_stdout is not None or args.pole_stdout is not None:
            fail("compile phase received stdout paths")
        compile_scripts(args.output.resolve(), tag)
    else:
        if args.qfield_stdout is None or args.pole_stdout is None:
            fail("analyze phase requires both stdout paths")
        analyze(args.output.resolve(), args.qfield_stdout.resolve(), args.pole_stdout.resolve())


if __name__ == "__main__":
    main()
