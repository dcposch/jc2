#!/usr/bin/env python3
"""Independently replay exact V18R2 duals and derive V17 local nonmembership."""

from __future__ import annotations

import argparse
import ast
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess


HERE = Path(__file__).resolve().parent
PREREG = HERE / "PREREGISTRATION.md"
PREREG_R1 = HERE / "PREREGISTRATION_R1.md"
EXPECTED_PREREG = "27fb885a1602257c2885e89c194c2d5f5bb2e7a3709f88f366e0c2807a5ad5dc"
EXPECTED_PREREG_R1 = "137fdc18c349a549949e90c3d515b5e08e01d9f69a6be5f8efbbf97b78175d7d"
DIRECTIONS = {"K10": 4, "K6": 3, "K2": 2}
EXPECTED_PAIRING = {
    "K10": Fraction(25, 45056),
    "K6": Fraction(45, 11264),
    "K2": Fraction(-25, 352),
}
NVAR = 6
ZERO = (0,) * NVAR
Key = tuple[int, int, int, int, int, int]
Poly = dict[Key, Fraction]


def fail(message: object) -> "None":
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def require_aws() -> str:
    if platform.system() != "Linux":
        fail("AWS-only V21 verifier refused non-Linux host")
    vendor = Path("/sys/class/dmi/id/sys_vendor")
    if not vendor.is_file() or vendor.read_text().strip() != "Amazon EC2":
        fail("AWS-only V21 verifier refused non-Amazon host")
    tag = os.environ.get("JC2_REGISTERED_AWS_LANE", "")
    if not tag:
        fail("JC2_REGISTERED_AWS_LANE is mandatory")
    return tag


def verify_manifest(input_dir: Path) -> dict[str, str]:
    manifest = input_dir / "INPUT.sha256"
    expected: dict[str, str] = {}
    for line in manifest.read_text().splitlines():
        if not line.strip():
            continue
        parts = line.split(maxsplit=1)
        if len(parts) != 2 or not re.fullmatch(r"[0-9a-f]{64}", parts[0]):
            fail(("malformed input manifest", line))
        name = parts[1].strip()
        if name.startswith("*"):
            name = name[1:]
        if "/" in name or name in expected:
            fail(("unsafe/duplicate input name", name))
        path = input_dir / name
        if not path.is_file() or digest(path) != parts[0]:
            fail(("input custody mismatch", name))
        expected[name] = parts[0]
    required = {
        "prelude_Q.sing", "v17_Q.sing", "syz6.txt", "h.txt",
        *(f"u{i}.txt" for i in range(1, 7)),
    }
    for label, cutoff in DIRECTIONS.items():
        required.update({
            f"load_{label}.txt", f"image_{label}.txt", f"target_{label}.txt",
            f"matrix_{label}_D{cutoff}.tsv", f"rows_{label}_D{cutoff}.json",
            f"columns_{label}_D{cutoff}.json", f"dual_{label}_D{cutoff}.tsv",
        })
    if not required.issubset(expected):
        fail(("missing frozen inputs", sorted(required - set(expected))))
    return expected


def add(left: Poly, right: Poly, scale: Fraction = Fraction(1)) -> Poly:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Fraction(0)) + scale * value
        if out[key] == 0:
            del out[key]
    return out


def multiply(left: Poly, right: Poly) -> Poly:
    out: Poly = {}
    for a, av in left.items():
        for b, bv in right.items():
            key = tuple(x + y for x, y in zip(a, b))
            out[key] = out.get(key, Fraction(0)) + av * bv
    return {key: value for key, value in out.items() if value}


def power(poly: Poly, exponent: int) -> Poly:
    if exponent < 0:
        fail(("negative exponent", exponent))
    result: Poly = {ZERO: Fraction(1)}
    base = poly
    while exponent:
        if exponent & 1:
            result = multiply(result, base)
        exponent >>= 1
        if exponent:
            base = multiply(base, base)
    return result


def eval_ast(node: ast.AST) -> Poly:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return {} if node.value == 0 else {ZERO: Fraction(node.value)}
    if isinstance(node, ast.Name) and re.fullmatch(r"d[0-5]", node.id):
        key = [0] * NVAR
        key[int(node.id[1])] = 1
        return {tuple(key): Fraction(1)}
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = eval_ast(node.operand)
        return value if isinstance(node.op, ast.UAdd) else {key: -x for key, x in value.items()}
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Add):
            return add(eval_ast(node.left), eval_ast(node.right))
        if isinstance(node.op, ast.Sub):
            return add(eval_ast(node.left), eval_ast(node.right), Fraction(-1))
        if isinstance(node.op, ast.Mult):
            return multiply(eval_ast(node.left), eval_ast(node.right))
        if isinstance(node.op, ast.Div):
            numerator, denominator = eval_ast(node.left), eval_ast(node.right)
            if set(denominator) != {ZERO} or denominator[ZERO] == 0:
                fail(("nonconstant denominator", ast.dump(node.right)))
            return {key: value / denominator[ZERO] for key, value in numerator.items()}
        if isinstance(node.op, ast.Pow):
            if not isinstance(node.right, ast.Constant) or not isinstance(node.right.value, int):
                fail(("noninteger exponent", ast.dump(node.right)))
            return power(eval_ast(node.left), node.right.value)
    fail(("unsupported polynomial syntax", ast.dump(node)))


def parse_poly(text: str) -> Poly:
    source = "".join(text.split())
    if not source or any(char in source for char in ';,"'):
        fail(("malformed polynomial", source[:120]))
    try:
        tree = ast.parse(source.replace("^", "**"), mode="eval")
    except SyntaxError as error:
        fail(("polynomial syntax", source[:120], str(error)))
    return eval_ast(tree.body)


def parse_ideal(path: Path) -> list[Poly]:
    text = "".join(path.read_text().split())
    if not text:
        fail(("empty ideal", path.name))
    return [parse_poly(part) for part in text.split(",")]


def parse_rows(prelude: Path) -> list[Poly]:
    text = prelude.read_text()
    rows = []
    for index in range(1, 7):
        match = re.search(rf"(?:^|\n)poly r{index}=(.*?);", text, re.S)
        if match is None:
            fail(("missing row", index))
        rows.append(parse_poly(match.group(1)))
    return rows


@lru_cache(maxsize=None)
def monomials(degree: int, variables: int = NVAR) -> tuple[Key, ...]:
    def build(left: int, count: int, prefix: tuple[int, ...]):
        if count == 1:
            yield prefix + (left,)
            return
        for exponent in range(left + 1):
            yield from build(left - exponent, count - 1, prefix + (exponent,))
    return tuple(build(degree, variables, ()))


def all_monomials(cutoff: int) -> tuple[Key, ...]:
    return tuple(key for degree in range(cutoff + 1) for key in monomials(degree))


def normal_order(poly: Poly) -> int | None:
    return min((sum(key) for key in poly), default=None)


def expected_matrix_bytes(generators: list[Poly], target: Poly, cutoff: int):
    row_keys = all_monomials(cutoff)
    row_index = {key: index for index, key in enumerate(row_keys)}
    columns: list[tuple[int, Key]] = []
    for generator_index, generator in enumerate(generators):
        initial = normal_order(generator)
        if initial is None or initial > cutoff:
            continue
        for degree in range(cutoff - initial + 1):
            for multiplier in monomials(degree):
                columns.append((generator_index, multiplier))
    entries: dict[tuple[int, int], Fraction] = {}
    for column, (generator_index, multiplier) in enumerate(columns):
        for key, value in generators[generator_index].items():
            shifted = tuple(a + b for a, b in zip(key, multiplier))
            if sum(shifted) <= cutoff:
                location = (row_index[shifted], column)
                entries[location] = entries.get(location, Fraction(0)) + value
    target_column = len(columns)
    for key, value in target.items():
        if sum(key) <= cutoff:
            entries[(row_index[key], target_column)] = value
    entries = {key: value for key, value in entries.items() if value}
    lines = [f"{len(row_keys)} {len(columns)} {len(entries)} {cutoff}"]
    for (row, column), value in sorted(entries.items()):
        lines.append(f"{row} {column} {value.numerator} {value.denominator}")
    matrix_bytes = ("\n".join(lines) + "\n").encode()
    row_bytes = (json.dumps([list(key) for key in row_keys], separators=(",", ":")) + "\n").encode()
    column_bytes = (json.dumps([
        {"generator_index": index + 1, "multiplier": list(multiplier)}
        for index, multiplier in columns
    ], separators=(",", ":")) + "\n").encode()
    return matrix_bytes, row_bytes, column_bytes, len(row_keys), len(columns), entries


def parse_dual(path: Path) -> tuple[dict[str, str], dict[int, Fraction]]:
    metadata: dict[str, str] = {}
    dual: dict[int, Fraction] = {}
    for line in path.read_text().splitlines():
        parts = line.split()
        if not parts:
            continue
        if parts[0] == "y":
            if len(parts) != 3 or int(parts[1]) in dual:
                fail(("bad dual entry", line))
            dual[int(parts[1])] = Fraction(parts[2])
        elif parts[0] == "x":
            fail(("incompatible certificate contains lift", line))
        else:
            if len(parts) != 2 or parts[0] in metadata:
                fail(("bad dual metadata", line))
            metadata[parts[0]] = parts[1]
    if not dual:
        fail(("empty exact dual", path.name))
    return metadata, dual


def verify_direction(input_dir: Path, output: Path, label: str, cutoff: int,
                     rows: list[Poly]) -> dict[str, object]:
    image = parse_ideal(input_dir / f"image_{label}.txt")
    target = parse_poly((input_dir / f"target_{label}.txt").read_text())
    if len(image) != 66:
        fail(("image generator count", label, len(image)))
    rebuilt = expected_matrix_bytes(rows + image, target, cutoff)
    matrix_bytes, row_bytes, column_bytes, row_count, column_count, entries = rebuilt
    matrix_path = input_dir / f"matrix_{label}_D{cutoff}.tsv"
    row_path = input_dir / f"rows_{label}_D{cutoff}.json"
    column_path = input_dir / f"columns_{label}_D{cutoff}.json"
    if matrix_bytes != matrix_path.read_bytes():
        fail(("independent matrix byte mismatch", label))
    if row_bytes != row_path.read_bytes() or column_bytes != column_path.read_bytes():
        fail(("independent row/column map mismatch", label))
    emitted = output / f"matrix_{label}_D{cutoff}.replayed.tsv"
    emitted.write_bytes(matrix_bytes)
    metadata, dual = parse_dual(input_dir / f"dual_{label}_D{cutoff}.tsv")
    if (metadata.get("field") != "Q" or int(metadata.get("cutoff", -1)) != cutoff or
            metadata.get("consistent") != "0"):
        fail(("dual branch metadata", label, metadata))
    annihilator = [Fraction(0) for _ in range(column_count)]
    pairing = Fraction(0)
    for (row, column), value in entries.items():
        coefficient = dual.get(row, Fraction(0))
        if column == column_count:
            pairing += coefficient * value
        else:
            annihilator[column] += coefficient * value
    if any(annihilator) or pairing != EXPECTED_PAIRING[label]:
        fail(("exact dual replay", label, pairing))
    if Fraction(metadata.get("certificate_dot", "0")) != pairing:
        fail(("serialized pairing mismatch", label))
    return {
        "cutoff": cutoff,
        "rows": row_count,
        "columns": column_count,
        "image_generators": len(image),
        "matrix_sha256": digest(matrix_path),
        "replayed_matrix_sha256": digest(emitted),
        "row_map_sha256": digest(row_path),
        "column_map_sha256": digest(column_path),
        "dual_sha256": digest(input_dir / f"dual_{label}_D{cutoff}.tsv"),
        "dual_entries": len(dual),
        "target_pairing": str(pairing),
        "truncated_nonmembership": True,
        "local_nonmembership_by_unit_lemma": True,
        "v17_branch": "LOCAL_NONZERO",
    }


def declaration(source: str, name: str) -> str:
    match = re.search(rf"(?:^|\n)poly {re.escape(name)}=(.*?);", source, re.S)
    if match is None:
        fail(("missing frozen declaration", name))
    value = "".join(match.group(1).split())
    if not value or any(char in value for char in ';"'):
        fail(("malformed frozen declaration", name))
    return value


def safe_serialization(path: Path) -> str:
    value = path.read_text().strip()
    if not value or '"' in value or "\r" in value:
        fail(("malformed Singular serialization", path.name))
    return value


def build_singular_replay(input_dir: Path, output: Path) -> Path:
    prelude = (input_dir / "prelude_Q.sing").read_text().rstrip()
    source = (input_dir / "v17_Q.sing").read_text()
    lines = [prelude, 'print("K00_V21_SOURCE_REPLAY_START");']
    for label in DIRECTIONS:
        for index in range(1, 8):
            name = f"a{label}{index}"
            lines.append(f"poly {name}=({declaration(source, name)});")
    lines.append(f"poly h=({safe_serialization(input_dir / 'h.txt')});")
    for index in range(1, 7):
        lines.append(f"poly u{index}=({safe_serialization(input_dir / f'u{index}.txt')});")
    lines.extend([
        "ideal I=r1,r2,r3,r4,r5,r6;",
        f"module T=({safe_serialization(input_dir / 'syz6.txt')});",
        "int i; int j; poly z; int ok=1;",
        "if (size(T)!=66) { ok=0; }",
        "for (j=1; j<=size(T); j++) { z=0; for (i=1; i<=6; i++) { z=z+T[j][i]*I[i]; } if (z!=0) { ok=0; } }",
        'print("K00_V21_SERIALIZED_SYZ_REPLAY="+string(ok));',
        'if (ok!=1) { print("K00_V21_FAIL=SERIALIZED_SYZ"); quit; }',
        'print("K00_V21_FRESH_SYZ_START");',
        "module Tf=syz(I); module GT=std(T); module GF=std(Tf);",
        "int moduleeq=1; vector vr;",
        "for (j=1; j<=size(T); j++) { vr=reduce(T[j],GF); if (vr!=0) { moduleeq=0; } }",
        "for (j=1; j<=size(Tf); j++) { vr=reduce(Tf[j],GT); if (vr!=0) { moduleeq=0; } }",
        'print("K00_V21_FRESH_SYZ_GENERATORS="+string(size(Tf)));',
        'print("K00_V21_SYZ_MODULE_EQUAL="+string(moduleeq));',
        'if (moduleeq!=1) { print("K00_V21_FAIL=SYZ_COMPLETENESS"); quit; }',
    ])
    for label in DIRECTIONS:
        load = safe_serialization(input_dir / f"load_{label}.txt")
        image = safe_serialization(input_dir / f"image_{label}.txt")
        target = safe_serialization(input_dir / f"target_{label}.txt")
        lines.extend([
            f"ideal LoadSaved{label}=({load});",
            f"ideal ESave{label}=({image});",
            f"poly DSave{label}=({target});",
            f"int loadok{label}=1;",
        ])
        for index in range(1, 8):
            lines.append(f"if (LoadSaved{label}[{index}]-a{label}{index}!=0) {{ loadok{label}=0; }}")
        lines.extend([
            f"ideal ECalc{label}=0;",
            "for (j=1; j<=66; j++)",
            "{",
            "  z=0;",
        ])
        for index in range(1, 7):
            lines.append(f"  z=z+T[j][{index}]*a{label}{index};")
        lines.extend([
            f"  ECalc{label}[j]=z;",
            "}",
            f"int imageok{label}=(size(ESave{label})==66);",
            f"for (j=1; j<=66; j++) {{ if (ECalc{label}[j]-ESave{label}[j]!=0) {{ imageok{label}=0; }} }}",
            f"poly DCalc{label}=h*a{label}7;",
        ])
        for index in range(1, 7):
            lines.append(f"DCalc{label}=DCalc{label}-u{index}*a{label}{index};")
        lines.extend([
            f"int targetok{label}=(DCalc{label}-DSave{label}==0);",
            f"poly DWrong{label}=h*a{label}7;",
        ])
        for index in range(1, 7):
            lines.append(f"DWrong{label}=DWrong{label}+u{index}*a{label}{index};")
        lines.extend([
            f"int mutationok{label}=(DWrong{label}-DSave{label}!=0);",
            f'print("K00_V21_{label}_LOAD_REPLAY="+string(loadok{label}));',
            f'print("K00_V21_{label}_IMAGE_REPLAY="+string(imageok{label}));',
            f'print("K00_V21_{label}_TARGET_REPLAY="+string(targetok{label}));',
            f'print("K00_V21_{label}_SIGN_MUTATION="+string(mutationok{label}));',
            f"if ((loadok{label}!=1)||(imageok{label}!=1)||(targetok{label}!=1)||(mutationok{label}!=1)) {{ print(\"K00_V21_FAIL={label}_SOURCE_REPLAY\"); quit; }}",
        ])
    lines.extend([
        'write("FRESH_SYZ6_MODULE.txt",Tf);',
        'print("K00_V21_SOURCE_REPLAY=PASS");',
        "quit;",
    ])
    script = output / "source_replay_v21.sing"
    script.write_text("\n".join(lines) + "\n")
    return script


def run_singular(script: Path, output: Path) -> dict[str, object]:
    executable = shutil.which("Singular")
    if executable is None:
        fail("Singular missing on registered AWS host")
    completed = subprocess.run(
        [executable, "-q", str(script)], cwd=output, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1800,
    )
    stdout = output / "source_replay.stdout"
    stderr = output / "source_replay.stderr"
    stdout.write_text(completed.stdout)
    stderr.write_text(completed.stderr)
    required = [
        "K00_V21_SERIALIZED_SYZ_REPLAY=1",
        "K00_V21_SYZ_MODULE_EQUAL=1",
        *(f"K00_V21_{label}_{kind}=1" for label in DIRECTIONS
          for kind in ("LOAD_REPLAY", "IMAGE_REPLAY", "TARGET_REPLAY", "SIGN_MUTATION")),
        "K00_V21_SOURCE_REPLAY=PASS",
    ]
    if completed.returncode != 0 or any(marker not in completed.stdout for marker in required):
        fail(("Singular source replay failed", completed.returncode, completed.stdout[-2000:], completed.stderr[-2000:]))
    lowered = (completed.stdout + completed.stderr).lower()
    if any(token in lowered for token in ("error occurred", "segment fault", "out of memory", "killed")):
        fail("Singular diagnostic token")
    return {
        "returncode": completed.returncode,
        "script_sha256": digest(script),
        "stdout_sha256": digest(stdout),
        "stderr_sha256": digest(stderr),
        "serialized_syzygies": 66,
        "fresh_module_equal": True,
        "source_images_targets_replayed": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    tag = require_aws()
    if EXPECTED_PREREG == "TO_BE_FROZEN" or digest(PREREG) != EXPECTED_PREREG:
        fail(("preregistration freeze mismatch", digest(PREREG), EXPECTED_PREREG))
    if EXPECTED_PREREG_R1 == "TO_BE_FROZEN" or digest(PREREG_R1) != EXPECTED_PREREG_R1:
        fail(("R1 preregistration freeze mismatch", digest(PREREG_R1), EXPECTED_PREREG_R1))
    inputs = verify_manifest(args.input_dir)
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    script = build_singular_replay(args.input_dir, output)
    source_replay = run_singular(script, output)
    rows = parse_rows(args.input_dir / "prelude_Q.sing")
    directions = {
        label: verify_direction(args.input_dir, output, label, cutoff, rows)
        for label, cutoff in DIRECTIONS.items()
    }
    result = {
        "status": "PASS-K00-V21-FILTERED-DUAL-LOCAL-NONMEMBERSHIP-COROLLARY",
        "registered_aws_lane": tag,
        "field": "Q",
        "preregistration_sha256": digest(PREREG),
        "r1_preregistration_sha256": digest(PREREG_R1),
        "input_manifest_sha256": digest(args.input_dir / "INPUT.sha256"),
        "input_sha256": inputs,
        "source_replay": source_replay,
        "directions": directions,
        "lemma": "D_in_J_local_implies_D_in_J_plus_m_power_because_local_denominator_is_unit_mod_m_power",
        "v17_exact_branches": {label: "LOCAL_NONZERO" for label in DIRECTIONS},
        "dependency_repair": "SUPERSEDES_ONLY_V18R2_NO_PROMOTION_BEFORE_MONOLITHIC_V17Q_ORDER",
        "crosscheck": "MONOLITHIC_V17Q_CONTINUES_INDEPENDENTLY",
        "scope": "THREE_SEPARATE_FIRSTORDER_LOAD_CLASSES_AT_NORMALIZED_K00_ONLY",
        "firewall": "NO_COUPLING_NO_LAMBDA19_NO_ARC_NO_CLOSURE_NO_ORDER2_NO_MAX12_NO_JC2",
    }
    result_path = output / "RESULT.json"
    result_path.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print("K00_V21_EXACT_DUAL_REPLAY=PASS")
    for label in DIRECTIONS:
        print(f"K00_V21_{label}_V17_BRANCH=LOCAL_NONZERO")
    print("K00_V21_ENDPOINT=PASS_FILTERED_DUAL_LOCAL_NONMEMBERSHIP")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
