#!/usr/bin/env python3
"""Reproducible corrected-descent builders for the (99,66) N1 batch-2 lane.

All generated files stay below ``box/g9966n1b2-20260903``.  The crucial
source correction is that Moh Proposition 6.3(3) gives the descended
Jacobian exponent ``ell = v_s-u_s-1``; it is not ``n'-M2'-2``.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time
from typing import Any, Iterable


ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b2-20260903"
INPUTS = Path("/tmp/jc2-lane.y07qTi/inputs")
RECEIPT = ROOT / "xmodel" / "g9966-n1-batch2-sol56-20260903.run.v2"
ORDER_BASIS = ROOT / "box" / "orderbasis-20260903" / "order_basis_full.py"

THREAD_ENV = {
    "OMP_NUM_THREADS": "1",
    "OPENBLAS_NUM_THREADS": "1",
    "MKL_NUM_THREADS": "1",
    "NUMEXPR_NUM_THREADS": "1",
    "FLINT_NUM_THREADS": "1",
}


def load_module(name: str, path: Path) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ob = load_module("n1b2_order_basis", ORDER_BASIS)
gg = load_module("n1b2_guided_gb", INPUTS / "guided_gb.py")
bands = load_module("n1b2_staged_bands", INPUTS / "staged_band_emitter.py")


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


# Correct Prop. 6.3 target exponents ell=v_s-u_s-1.
ROWS = {
    "S1": ob.Row("S1_n18_m12_Mm4_V1_k6", "S1 corrected", 18, 12, -4, 1, 6),
    "S2": ob.Row("S2_n36_m24_M8_V1_k2", "S2 corrected", 36, 24, 8, 1, 2),
    "S3": ob.Row("S3_n36_m24_M8_V5_k2", "S3 corrected", 36, 24, 8, 5, 2),
    "S4": ob.Row("S4_n27_m18_M6_V1_k4", "S4 corrected", 27, 18, 6, 1, 4),
    "S5": ob.Row("S5_n9_m6_M2_V1_k8", "S5 corrected", 9, 6, 2, 1, 8),
    "S6": ob.Row("S6_n9_m6_M5_V2_k8", "S6 corrected", 9, 6, 5, 2, 8),
    "S7": ob.Row("S7_n36_m24_M28_V8_k2", "S7 corrected", 36, 24, 28, 8, 2),
    "S8": ob.Row("S8_n27_m18_M21_V8_k4", "S8 corrected", 27, 18, 21, 8, 4),
}


def receipt_fields() -> tuple[Path, list[dict[str, Any]]]:
    values: dict[str, str] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            values[key] = value
    input_dir = Path(values["lane_inputs_dir"])
    count = int(values["charged_inputs"])
    records = []
    for index in range(1, count + 1):
        records.append({
            "index": index,
            "basename": values[f"charged_input_{index}_basename"],
            "expected": values[f"charged_input_{index}_sha256"],
        })
    return input_dir, records


def verify_manifest() -> dict[str, Any]:
    input_dir, records = receipt_fields()
    lines = []
    checks = []
    for record in records:
        path = input_dir / record["basename"]
        got = sha256(path)
        lines.append(f"{record['expected']}  {path}")
        checks.append({**record, "path": str(path), "got": got, "ok": got == record["expected"]})
    manifest = HERE / "charged-inputs.sha256"
    atomic_write(manifest, "\n".join(lines) + "\n")
    payload = {
        "receipt": str(RECEIPT.relative_to(ROOT)),
        "input_dir": str(input_dir),
        "checks": checks,
        "ok": bool(checks) and all(row["ok"] for row in checks),
        "manifest": str(manifest.relative_to(ROOT)),
        "manifest_sha256": sha256(manifest),
    }
    atomic_write(HERE / "charged-inputs-check.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    if not payload["ok"]:
        raise RuntimeError("charged-input content mismatch")
    return payload


def frozen_enumeration() -> dict[str, Any]:
    moh = load_module("n1b2_frozen_moh", INPUTS / "moh_skeleton_full.py")
    found = []
    for m, Ms, V in moh.census(99, Kmin=2, full=True):
        if m != 66:
            continue
        skel = moh.Skel(99, m, list(Ms), V)
        found.append(skel)
    found.sort(key=lambda row: (row.M[2], row.V[3], row.V[2]))
    if len(found) != 8:
        raise AssertionError(f"expected eight skeletons, got {len(found)}")
    rows = []
    for index, skel in enumerate(found, 1):
        ds = skel.d[skel.s]
        vs = skel.V[skel.s]
        us = ds - vs
        desc = {
            "n": us * skel.n // ds,
            "m": us * skel.m // ds,
            "M": [us * skel.M[i] // ds for i in range(1, skel.s)],
            "M2": us * skel.M[2] // ds,
            "V2": skel.V[2],
            "K": __import__("math").gcd(us * skel.n // ds, us * skel.m // ds),
            "ell": vs - us - 1,
        }
        desc["u_prime"] = desc["K"] - desc["V2"]
        rows.append({
            "id": f"S{index}",
            "s": skel.s,
            "M": [skel.M[i] for i in range(1, skel.s + 1)],
            "d": [skel.d[i] for i in range(1, skel.s + 2)],
            "V": {str(i): skel.V[i] for i in range(2, skel.s + 1)},
            "u_s": us,
            "v_s": vs,
            "descended": desc,
            "prop63_automatic": us == 1,
        })
    payload = {
        "method": "frozen moh_skeleton_full.census(99,Kmin=2,full=True), m=66, charged ID sort",
        "count": len(rows),
        "rows": rows,
        "source_sha256": sha256(INPUTS / "moh_skeleton_full.py"),
    }
    atomic_write(HERE / "enumeration.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload


def parse_part(text: str) -> tuple[int, ...]:
    part = tuple(int(piece) for piece in text.replace(",", "+").split("+") if piece)
    if not part or tuple(sorted(part, reverse=True)) != part:
        raise ValueError(f"bad partition {text!r}")
    return part


def chart_stem(name: str, part: Iterable[int]) -> str:
    row = ROWS[name]
    return ob.stem_for(row, tuple(part))


def prepare_one(name: str, part: tuple[int, ...]) -> dict[str, Any]:
    row = ROWS[name]
    spec = ob.build_full_spec(row, part)
    stem = chart_stem(name, part)
    rows_path = HERE / "rows" / f"{stem}_rows.tsv"
    builder_path = HERE / "builders" / f"{stem}_builder.sing"
    meta_path = HERE / "meta" / f"{stem}.json"
    rows_path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(builder_path, ob.native_builder_text(spec, rows_path))
    payload = {
        "schema": "jc2.g9966n1b2.corrected-order-chart/v1",
        "source_correction": {
            "target": f"c*x^{row.k}",
            "formula": "ell=v_s-u_s-1",
            "citation": "Moh 1983 Proposition 6.3(3), printed p.197",
        },
        "meta": spec["meta"],
        "variables": [str(symbol) for symbol in spec["params"]],
        "sat": ob.sstr(spec["sat"]),
        "builder": str(builder_path.relative_to(ROOT)),
        "builder_sha256": sha256(builder_path),
        "rows_path": str(rows_path.relative_to(ROOT)),
    }
    atomic_write(meta_path, json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return {"meta": str(meta_path.relative_to(ROOT)), **payload}


def run_call(command: list[str], stdout_path: Path, stderr_path: Path, timeout: int) -> dict[str, Any]:
    env = os.environ.copy()
    env.update(THREAD_ENV)
    wrapped = ["timeout", str(timeout), "stdbuf", "-oL", "-eL", *command]
    started = time.monotonic()
    with stdout_path.open("w", encoding="utf-8") as out, stderr_path.open("w", encoding="utf-8") as err:
        result = subprocess.run(wrapped, cwd=ROOT, env=env, stdout=out, stderr=err, text=True, check=False)
    return {
        "command": wrapped,
        "returncode": result.returncode,
        "timed_out": result.returncode == 124,
        "elapsed_seconds": round(time.monotonic() - started, 6),
        "stdout": str(stdout_path.relative_to(ROOT)),
        "stderr": str(stderr_path.relative_to(ROOT)),
        "stdout_sha256": sha256(stdout_path),
        "stderr_sha256": sha256(stderr_path),
    }


def build_one(meta_path: Path, timeout: int) -> dict[str, Any]:
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    builder = ROOT / payload["builder"]
    out = builder.with_suffix(builder.suffix + ".out")
    err = builder.with_suffix(builder.suffix + ".err")
    run = run_call(
        ["Singular", "--cpus=1", "--threads=1", "--flint-threads=1", "--no-rc", "-q", str(builder)],
        out,
        err,
        timeout,
    )
    text = out.read_text(encoding="utf-8", errors="replace")
    rows_path = ROOT / payload["rows_path"]
    run.update({
        "native_done": "NATIVE_DONE" in text and "? error occurred" not in text,
        "target_gate": "NATIVE_GATE target_xk_level0_nonzero=1" in text,
        "rows_exists": rows_path.exists(),
        "rows_sha256": sha256(rows_path) if rows_path.exists() else None,
        "row_count": max(0, sum(1 for _ in rows_path.open(encoding="utf-8")) - 1) if rows_path.exists() else None,
    })
    record = HERE / "build-runs" / f"{meta_path.stem}.json"
    atomic_write(record, json.dumps(run, indent=2, sort_keys=True) + "\n")
    if run["native_done"] and run["target_gate"]:
        payload["builder_run"] = run
        atomic_write(meta_path, json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return run


def emit_bands(meta_path: Path, characteristic: int) -> dict[str, Any]:
    suffix = "Q" if characteristic == 0 else f"p{characteristic}"
    output_dir = HERE / "bands" / meta_path.stem / suffix
    return bands.emit_order_chart_bands(
        meta_path,
        output_dir,
        characteristic=characteristic,
        band_column="h_power",
        include_saturation=True,
    )


def read_rows(path: Path) -> list[str]:
    expressions = []
    with path.open(encoding="utf-8") as source:
        header = source.readline().rstrip("\n")
        if header != "source_index|h_power|x_power|y_power|expr":
            raise ValueError(f"unexpected row header in {path}")
        for line in source:
            if line.strip():
                expressions.append(line.rstrip("\n").split("|", 4)[4])
    return expressions


def guided_one(
    meta_path: Path,
    characteristic: int,
    timeout: int,
    order: str,
    extra_generators: Iterable[str] = (),
    coefficient_variable: str | None = None,
    minpoly: str | None = None,
    monomial_order: str = "dp",
) -> dict[str, Any]:
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    variables = list(payload["variables"])
    if coefficient_variable is not None:
        if coefficient_variable not in variables or not minpoly:
            raise ValueError("coefficient-variable mode needs an existing variable and --minpoly")
        variables.remove(coefficient_variable)
    if order == "coefficient-first":
        variables.sort(key=lambda name: (
            0 if name.startswith("A1_") else 1 if name.startswith("A2_") else
            2 if name.startswith("A3_") else 3 if name.startswith("B") else
            4 if name.startswith("h_") else 5,
            name,
        ))
    variables.append("T")
    rows_path = ROOT / payload["rows_path"]
    extras = list(extra_generators)
    generators = read_rows(rows_path) + extras + [f"T*({payload['sat']})-1"]
    if coefficient_variable is None:
        prelude = f"ring R={characteristic},({','.join(variables)}),{monomial_order};\noption(redSB);\n"
    else:
        prelude = (
            f"ring R=({characteristic},{coefficient_variable}),({','.join(variables)}),{monomial_order};\n"
            f"minpoly={minpoly};\noption(redSB);\n"
        )
    branch_material = [*extras]
    if coefficient_variable is not None:
        branch_material.append(f"COEFF:{coefficient_variable}:{minpoly}")
    if monomial_order != "dp":
        branch_material.append(f"ORDER:{monomial_order}")
    extra_tag = "" if not branch_material else "_branch_" + hashlib.sha256("\n".join(branch_material).encode()).hexdigest()[:10]
    label = f"{meta_path.stem}_{order}{extra_tag}"
    system = gg.SingularSystem(
        name=label,
        prelude=prelude,
        generators=tuple(generators),
        characteristic=characteristic,
        variables=tuple(variables),
        homogeneous=False,
        metadata={
            "meta": str(meta_path.relative_to(ROOT)),
            "rows_sha256": sha256(rows_path),
            "target": payload["source_correction"]["target"],
            "variable_order": order,
            "extra_generators": extras,
            "coefficient_variable": coefficient_variable,
            "minpoly": minpoly,
            "monomial_order": monomial_order,
        },
    )
    result = gg.guided_groebner(
        system,
        policy=gg.PromotionPolicy.exact_q("inhomogeneous localized chart; exact Q required"),
        config=gg.RunConfig(
            HERE / "guided" / meta_path.stem / (order + extra_tag),
            timeout_seconds=timeout,
            total_cores=1,
            max_parallel_jobs=1,
            run_perturbed_control=False,
        ),
    )
    return result.to_json()


def artifacts_manifest() -> dict[str, Any]:
    manifest = HERE / "artifacts.sha256"
    rows = []
    for path in sorted(HERE.rglob("*")):
        if (
            path.is_file()
            and path != manifest
            and "__pycache__" not in path.parts
            and path.suffix != ".pyc"
            and not path.name.endswith(".tmp")
        ):
            rows.append(f"{sha256(path)}  {path.relative_to(ROOT)}")
    atomic_write(manifest, "\n".join(rows) + "\n")
    return {"files": len(rows), "manifest": str(manifest.relative_to(ROOT)), "sha256": sha256(manifest)}


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("verify")
    sub.add_parser("enumerate")
    prepare = sub.add_parser("prepare")
    prepare.add_argument("--row", choices=sorted(ROWS), required=True)
    prepare.add_argument("--part", required=True)
    build = sub.add_parser("build")
    build.add_argument("--meta", type=Path, required=True)
    build.add_argument("--timeout", type=int, default=300)
    emit = sub.add_parser("bands")
    emit.add_argument("--meta", type=Path, required=True)
    emit.add_argument("--char", type=int, default=0)
    solve = sub.add_parser("solve")
    solve.add_argument("--meta", type=Path, required=True)
    solve.add_argument("--char", type=int, required=True)
    solve.add_argument("--timeout", type=int, default=300)
    solve.add_argument("--order", choices=("metadata", "coefficient-first"), default="coefficient-first")
    solve.add_argument("--extra", action="append", default=[])
    solve.add_argument("--coeff-var")
    solve.add_argument("--minpoly")
    solve.add_argument("--monomial-order", choices=("dp", "lp", "Dp"), default="dp")
    sub.add_parser("manifest")
    args = parser.parse_args()

    if args.cmd == "verify":
        result = verify_manifest()
    elif args.cmd == "enumerate":
        result = frozen_enumeration()
    elif args.cmd == "prepare":
        result = prepare_one(args.row, parse_part(args.part))
    elif args.cmd == "build":
        result = build_one(args.meta.resolve(), args.timeout)
    elif args.cmd == "bands":
        result = emit_bands(args.meta.resolve(), args.char)
    elif args.cmd == "solve":
        result = guided_one(
            args.meta.resolve(), args.char, args.timeout, args.order, args.extra,
            args.coeff_var, args.minpoly, args.monomial_order,
        )
    else:
        result = artifacts_manifest()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
