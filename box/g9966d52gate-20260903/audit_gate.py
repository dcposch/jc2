#!/usr/bin/env python3
"""Custody, acceptance, and certificate checks for the g9966 delta=5/2 gate."""

from __future__ import annotations

import argparse
from decimal import Decimal
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

import sympy as sp


ROOT = Path("/home/ubuntu/jc2")
BASE = ROOT / "box/g9966d52gate-20260903"
CURRENT_RECEIPT = ROOT / "xmodel/g9966-delta52-kill-gate-gpt55-20260903.run.v2"
CURRENT_FROZEN = Path("/tmp/jc2-lane.MvSYEH/inputs")
GLOBAL_RECEIPT = ROOT / "xmodel/g9966-global-band-sol56-20260903.run.v2"
ENGINE = ROOT / "box/g9966band-20260903/band_engine.py"
VALIDATOR = ROOT / "box/g9966band-20260903/validate_run_ledger.py"
MANIFEST_HELPER = ROOT / "box/g9966band-20260903/next_system_manifest.py"
SOURCE_RUN52 = ROOT / "box/g9966band-20260903/runs/delta52"
SOURCE_RUN2 = ROOT / "box/g9966band-20260903/runs/delta2"
RUN52 = BASE / "runs/delta52"
ATTEMPT8 = BASE / "attempts/stage8"
PINNED_ENGINE_SHA256 = "3bd2937d75d59d59edeca1b89eba286fd2711f2d608109e7fd8971b64e059ac9"


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in out, f"duplicate JSON key: {key}")
        out[key] = value
    return out


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_bytes(), object_pairs_hook=reject_duplicates)


def fields(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if "=" in line:
            key, value = line.split("=", 1)
            out[key] = value
    return out


def write_same_or_new(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        require(path.read_bytes() == payload, f"refusing to change existing file: {path}")
    else:
        path.write_bytes(payload)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    write_same_or_new(path, (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode())


def run_capture(argv: list[str], **kwargs: Any) -> subprocess.CompletedProcess:
    return subprocess.run(argv, check=True, capture_output=True, timeout=3000, **kwargs)


def parse_elapsed(value: str) -> float:
    parts = [Decimal(part) for part in value.strip().split(":")]
    require(len(parts) in (2, 3), f"bad elapsed value: {value}")
    if len(parts) == 2:
        return float(parts[0] * 60 + parts[1])
    return float(parts[0] * 3600 + parts[1] * 60 + parts[2])


def parse_time(path: Path) -> dict[str, int | float]:
    text = path.read_text(encoding="utf-8")
    elapsed = re.findall(r"Elapsed \(wall clock\) time \(h:mm:ss or m:ss\):\s*(\S+)", text)
    rss = re.findall(r"Maximum resident set size \(kbytes\):\s*(\d+)", text)
    status = re.findall(r"Exit status:\s*(\d+)", text)
    require(len(elapsed) == len(rss) == len(status) == 1, f"bad GNU time record: {path}")
    require(status[0] == "0", f"nonzero time status: {path}")
    return {"wall_seconds": parse_elapsed(elapsed[0]), "max_rss_kib": int(rss[0])}


def load_engine():
    require(sha256_file(ENGINE) == PINNED_ENGINE_SHA256, "pinned engine digest mismatch")
    name = "g9966_gate_pinned_engine"
    spec = importlib.util.spec_from_file_location(name, ENGINE)
    require(spec is not None and spec.loader is not None, "cannot load engine")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def current_input_manifest() -> dict[str, Any]:
    receipt = fields(CURRENT_RECEIPT)
    require(Path(receipt["lane_inputs_dir"]) == CURRENT_FROZEN, "current lane input dir mismatch")
    count = int(receipt["charged_inputs"])
    lines: list[str] = []
    check_lines: list[str] = []
    for index in range(1, count + 1):
        basename = receipt[f"charged_input_{index}_basename"]
        expected = receipt[f"charged_input_{index}_sha256"]
        path = CURRENT_FROZEN / basename
        actual = sha256_file(path)
        require(actual == expected, f"charged input mismatch: {basename}")
        lines.append(f"{expected}  {path}\n")
        check_lines.append(f"{path}: OK\n")
    manifest = "".join(lines).encode()
    check = "".join(check_lines).encode()
    write_same_or_new(BASE / "charged-inputs.sha256", manifest)
    write_same_or_new(BASE / "charged-inputs.check", check)
    return {
        "receipt": str(CURRENT_RECEIPT),
        "lane_inputs_dir": str(CURRENT_FROZEN),
        "charged_inputs": count,
        "all_hashes_match": True,
        "manifest_sha256": sha256_bytes(manifest),
        "check_sha256": sha256_bytes(check),
    }


def safe_link(source: Path, destination: Path, expected: str | None = None) -> str:
    require(source.is_file(), f"missing source: {source}")
    if expected is None:
        expected = sha256_file(source)
    require(sha256_file(source) == expected, f"source digest mismatch: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        require(destination.is_file(), f"destination is not a file: {destination}")
        require(sha256_file(destination) == expected, f"destination digest mismatch: {destination}")
        return "existing"
    if destination.is_symlink():
        raise RuntimeError(f"dangling destination symlink: {destination}")
    destination.symlink_to(source)
    require(sha256_file(destination) == expected, f"linked digest mismatch: {destination}")
    return "linked"


def prepare_workspace() -> dict[str, Any]:
    require(sha256_file(ENGINE) == PINNED_ENGINE_SHA256, "engine digest mismatch")
    receipt = fields(GLOBAL_RECEIPT)
    count = int(receipt["charged_inputs"])
    require(count == 20, "unexpected global charged-input count")
    text = ENGINE.read_text(encoding="utf-8")
    match = re.search(r'^FROZEN = Path\("([^"]+)"\)$', text, re.MULTILINE)
    require(match is not None, "cannot recover engine FROZEN path")
    frozen = Path(match.group(1))
    require(str(frozen).startswith("/tmp/jc2-lane."), f"unsafe frozen target: {frozen}")
    frozen.mkdir(parents=True, exist_ok=True)

    linked = []
    for index in range(1, count + 1):
        rel = receipt[f"charged_input_{index}"]
        basename = receipt[f"charged_input_{index}_basename"]
        expected = receipt[f"charged_input_{index}_sha256"]
        require(Path(rel).name == basename, f"global basename mismatch at {index}")
        source = ROOT / rel
        action = safe_link(source, frozen / basename, expected)
        linked.append({"index": index, "basename": basename, "sha256": expected, "action": action})

    seeded = []
    for stage in range(8):
        for suffix in ("json", "time", "sing", "err"):
            source = SOURCE_RUN52 / f"stage{stage}.{suffix}"
            action = safe_link(source, RUN52 / source.name)
            seeded.append({"file": source.name, "sha256": sha256_file(source), "action": action})

    out = {
        "status": "READY",
        "current_inputs": current_input_manifest(),
        "engine": {"path": str(ENGINE), "sha256": PINNED_ENGINE_SHA256},
        "legacy_receipt": str(GLOBAL_RECEIPT),
        "engine_frozen_directory": str(frozen),
        "engine_inputs": linked,
        "run_directory": str(RUN52),
        "seeded_prefix_artifacts": seeded,
    }
    write_json(BASE / "prepare-workspace.json", out)
    return out


def custody_stage7() -> dict[str, Any]:
    engine = load_engine()
    frozen_stage7 = CURRENT_FROZEN / "stage7.json"
    live_stage7 = SOURCE_RUN52 / "stage7.json"
    require(sha256_file(frozen_stage7) == sha256_file(live_stage7), "frozen/live stage7 mismatch")
    stage7 = load_json(live_stage7)
    require(stage7["branch"] == "delta52", "stage7 branch mismatch")
    require(stage7["stage_spec"] == engine.stage_spec("delta52", 7), "stage7 spec mismatch")
    require(stage7["driver_sha256"] == PINNED_ENGINE_SHA256, "stage7 driver mismatch")
    require(stage7["joint_elimination"]["Qstar_pivots"] == 59, "stage7 joint rank mismatch")
    require(stage7["joint_elimination"]["residual_count"] == 0, "stage7 residue mismatch")
    require(stage7["outer_major"]["preblock"]["Qstar_pivots"] == 5598, "outer D2 rank mismatch")
    require(stage7["outer_major"]["D1_cumulative_pivots"] == 176, "outer D1 rank mismatch")
    require(stage7["counts"]["exact_Krull_dimension_localized"] == 869, "stage7 dimension mismatch")
    require(6702 - 5598 - 176 - 59 == 869, "stage7 dimension formula mismatch")

    manifest_bytes = run_capture([
        "python3", str(MANIFEST_HELPER), "--branch", "delta52",
        "--completed-stage", "7", "--result-json", str(live_stage7)
    ]).stdout
    source_manifest = SOURCE_RUN52 / "next-stage8-system.json"
    require(manifest_bytes == source_manifest.read_bytes(), "stage8 manifest is not byte-identical")
    write_same_or_new(BASE / "next-stage8-system.json", manifest_bytes)
    manifest = json.loads(manifest_bytes, object_pairs_hook=reject_duplicates)

    free_names = "".join(name + "\n" for name in manifest["unresolved_quotient_generators"]).encode()
    source_free = SOURCE_RUN52 / "stage7-free-coefficients.txt"
    require(source_free.read_bytes() == free_names, "stage7 free list mismatch")
    write_same_or_new(BASE / "stage7-free-coefficients.txt", free_names)
    require(len(manifest["unresolved_quotient_generators"]) == 869, "free count mismatch")

    ledger_bytes = run_capture([
        "python3", str(VALIDATOR), "--branch", "delta52", "--run-dir", str(SOURCE_RUN52)
    ]).stdout
    require(ledger_bytes == (SOURCE_RUN52 / "validated-ledger.json").read_bytes(),
            "stage7 ledger is not byte-identical")
    ledger = json.loads(ledger_bytes, object_pairs_hook=reject_duplicates)
    require(ledger["status"] == "VALIDATED", "stage7 ledger validation failed")

    out = {
        "status": "CUSTODY-REPLAY-PASS",
        "stage7": {
            "path": str(live_stage7),
            "bytes": live_stage7.stat().st_size,
            "sha256": sha256_file(live_stage7),
            "dimension": 869,
            "outer_D2_rank": 5598,
            "outer_D1_rank": 176,
            "joint_Qstar_rank": 59,
            "residue_count": 0,
        },
        "manifest": {
            "path": str(BASE / "next-stage8-system.json"),
            "sha256": sha256_bytes(manifest_bytes),
            "byte_identical_replay": True,
            "next_stage_spec": manifest["next_stage_spec"],
        },
        "free_coordinates": {
            "path": str(BASE / "stage7-free-coefficients.txt"),
            "count": 869,
            "sha256": sha256_bytes(free_names),
            "byte_identical": True,
        },
        "ledger": {
            "path": str(SOURCE_RUN52 / "validated-ledger.json"),
            "sha256": sha256_bytes(ledger_bytes),
            "byte_identical_replay": True,
            "completed_through_stage": ledger["completed_through_stage"],
        },
    }
    write_json(BASE / "custody-stage7.json", out)
    return out


def promote_stage8() -> dict[str, Any]:
    require(sha256_file(ENGINE) == PINNED_ENGINE_SHA256, "engine digest mismatch")
    sources = {suffix: ATTEMPT8 / f"stage8.{suffix}" for suffix in ("json", "time", "sing", "err")}
    require(all(path.is_file() for path in sources.values()), "stage8 attempt artifact set incomplete")
    require(sources["json"].stat().st_size > 0, "stage8 JSON is empty")
    require(sources["err"].read_bytes() == b"", "stage8 stderr is nonempty")
    stage8 = load_json(sources["json"])
    require(stage8["branch"] == "delta52", "stage8 branch mismatch")
    require(stage8["stage_spec"]["stage"] == 8, "stage8 stage mismatch")
    require(stage8["driver_sha256"] == PINNED_ENGINE_SHA256, "stage8 driver mismatch")

    promoted = []
    for suffix, source in sources.items():
        destination = RUN52 / f"stage8.{suffix}"
        if destination.exists():
            require(sha256_file(destination) == sha256_file(source),
                    f"existing stage8 {suffix} does not match attempt")
            action = "existing"
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            os.link(source, destination)
            action = "linked"
        promoted.append({"file": destination.name, "sha256": sha256_file(destination), "action": action})

    ledger_bytes = run_capture([
        "python3", str(VALIDATOR), "--branch", "delta52", "--run-dir", str(RUN52)
    ]).stdout
    ledger = json.loads(ledger_bytes, object_pairs_hook=reject_duplicates)
    require(ledger["status"] == "VALIDATED", "stage8 ledger validation failed")
    require(ledger["completed_through_stage"] == 8, "stage8 ledger endpoint mismatch")
    write_same_or_new(BASE / "validated-through-stage8.json", ledger_bytes)

    previous = load_json(RUN52 / "stage7.json")
    prior_pairs = {(p["row"], p["variable"]) for p in previous["joint_elimination"]["pivot_ledger"]}
    introduced = [
        p for p in stage8["joint_elimination"]["pivot_ledger"]
        if (p["row"], p["variable"]) not in prior_pairs
    ]
    require(len(introduced) == 7, "stage8 introduced-pivot count mismatch")
    constants = []
    for row in stage8["joint_elimination"]["residual_rows"]:
        value = sp.sympify(row["expression"])
        if not value.free_symbols and value != 0:
            constants.append({"label": row["label"], "expression": str(value)})
    terminal = ledger["stages"][-1]
    summary = {
        "status": "ACCEPTED",
        "stage": 8,
        "stage_json_sha256": sha256_file(RUN52 / "stage8.json"),
        "stage_json_bytes": (RUN52 / "stage8.json").stat().st_size,
        "band": terminal["band"],
        "new_rows": terminal["new_row_labels"],
        "new_outer_D1": terminal["new_outer_D1"],
        "joint_Qstar_pivots": {
            **terminal["joint_Qstar_pivots"],
            "introduced_with_coefficients": introduced,
        },
        "constant_residue_rows": constants,
        "residue": terminal["residue"],
        "dimension": terminal["dimension"],
        "dimension_decrement": terminal["dimension_decrement_from_previous_stage"],
        "external_resources": terminal["external_resources"],
        "attempt_resources": parse_time(sources["time"]),
        "dimension_history": [stage["dimension"] for stage in ledger["stages"]],
        "free_coordinate_list_is_valid": stage8["free_coordinate_list_is_valid"],
        "promoted_artifacts": promoted,
        "ledger": {"path": str(BASE / "validated-through-stage8.json"), "sha256": sha256_bytes(ledger_bytes)},
        "next_system": None,
    }
    require(constants == [{"label": "stage8_G_local16_coord0", "expression": "64"}],
            "stage8 constant residue mismatch")
    write_json(BASE / "stage8-summary.json", summary)
    return summary


def singular_sections(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    def section(name: str) -> str:
        match = re.search(rf"BEGIN_{name}\n(.*?)\nEND_{name}", text, re.DOTALL)
        require(match is not None, f"missing Singular section {name}: {path}")
        return match.group(1).strip()
    controls = section("CONTROLS").splitlines()
    out = {
        "dimension": int(section("DIM")),
        "basis": section("GB"),
        "controls": controls,
        "output_sha256": sha256_file(path),
    }
    require(out["dimension"] == -1, "Singular dimension mismatch")
    require(out["basis"] == "1", "Singular basis mismatch")
    require(controls == ["0", "1", "0"], "Singular controls mismatch")
    return out


def expected_singular_input(stage: dict[str, Any]) -> str:
    expressions = [sp.expand(sp.sympify(row["expression"]))
                   for row in stage["joint_elimination"]["residual_rows"]]
    variables = sorted(set().union(*(expr.free_symbols for expr in expressions)), key=str)
    localized = sp.Symbol("rho" if stage["branch"] == "delta2" else "c")
    wrapper = sp.Symbol("Zrho" if stage["branch"] == "delta2" else "Zc")
    if localized not in variables:
        variables.append(localized)
        variables.sort(key=str)
    ringvars = variables + [wrapper]
    def singular_expr(expr: sp.Expr) -> str:
        return str(expr).replace("**", "^")
    ideal_entries = [singular_expr(expr) for expr in expressions] + [f"{wrapper}*{localized}-1"]
    return (
        f"ring R=0,({','.join(map(str, ringvars))}),dp;\n"
        f"ideal I={','.join(ideal_entries)};\n"
        "ideal S=std(I);\n"
        'print("BEGIN_DIM"); print(dim(S)); print("END_DIM");\n'
        'print("BEGIN_GB"); print(S); print("END_GB");\n'
        f"ideal EmptyControl={localized},{wrapper}*{localized}-1;\n"
        f"ideal PointControl={localized}-1,{wrapper}*{localized}-1;\n"
        f"ideal RawControl={','.join(singular_expr(expr) for expr in expressions)};\n"
        'print("BEGIN_CONTROLS"); print(reduce(1,std(EmptyControl))); '
        'print(reduce(1,std(PointControl))); print(reduce(1,std(RawControl))); '
        'print("END_CONTROLS");\n'
        "quit;\n"
    )


def certificate_for(stage_path: Path, singular_input: Path, singular_output: Path,
                    branch: str, stage_number: int, label: str, constant: int) -> dict[str, Any]:
    stage = load_json(stage_path)
    require(stage["branch"] == branch, "certificate branch mismatch")
    require(stage["stage_spec"]["stage"] == stage_number, "certificate stage mismatch")
    require(stage["driver_sha256"] == PINNED_ENGINE_SHA256, "certificate driver mismatch")
    rows = [row for row in stage["joint_elimination"]["residual_rows"] if row["label"] == label]
    require(len(rows) == 1, f"missing residue row: {label}")
    value = sp.sympify(rows[0]["expression"])
    require(not value.free_symbols and value == constant, "residue constant mismatch")
    inverse = sp.Rational(1, constant)
    require(sp.cancel(inverse * value) == 1, "membership witness mismatch")
    localized = "rho" if branch == "delta2" else "c"
    for pivot in stage["joint_elimination"]["pivot_ledger"]:
        coeff = sp.Rational(pivot["coefficient"])
        require(coeff != 0, f"zero pivot coefficient: {pivot['row']}")
        require(pivot["variable"] != localized, "localized parameter used as pivot")
    singular = stage["joint_elimination"]["singular"]
    require(singular["unit_ideal"] is True and singular["dimension"] == -1, "embedded Singular mismatch")
    require(singular["basis_preview"] == ["1"], "embedded basis mismatch")
    require(singular["raw_residue_unit_ideal"] is True, "raw residue not unit")
    if singular_input.exists():
        require(singular_input.read_text(encoding="utf-8") == expected_singular_input(stage),
                "Singular input reconstruction mismatch")
    replay = singular_sections(singular_output)
    return {
        "branch": branch,
        "stage": stage_number,
        "stage_json": {"path": str(stage_path), "sha256": sha256_file(stage_path)},
        "reduced_row": label,
        "constant": str(value),
        "membership_witness_over_Q": f"1 = ({inverse})*{label}",
        "Qstar_pivot_count": len(stage["joint_elimination"]["pivot_ledger"]),
        "Qstar_pivots_checked_nonzero_rational": True,
        "localization_parameter_excluded_from_pivots": True,
        "emitted_singular_input": {"path": str(singular_input), "sha256": sha256_file(singular_input)}
        if singular_input.exists() else None,
        "independent_singular_replay": replay,
        "raw_residue_unit_ideal": True,
        "localized_unit_ideal": True,
        "verdict": stage["verdict"],
    }


def death_certificate() -> dict[str, Any]:
    out = {
        "schema": "g9966-delta52-kill-gate-certificate-v1",
        "coefficient_field": "Q",
        "engine": {"path": str(ENGINE), "sha256": sha256_file(ENGINE)},
        "certificates": [
            certificate_for(
                SOURCE_RUN2 / "stage4.json",
                SOURCE_RUN2 / "stage4.sing",
                BASE / "delta2-stage4-singular-replay.out",
                "delta2", 4, "stage4_J_d159_k35", 6264,
            ),
            certificate_for(
                RUN52 / "stage8.json",
                RUN52 / "stage8.sing",
                BASE / "stage8-singular-replay.out",
                "delta52", 8, "stage8_G_local16_coord0", 64,
            ),
        ],
        "all_declared_branches_dead": True,
        "typed_chart_verdict": "NO-SURVIVING-BRANCH[DECLARED-(99,66)-JOINT-CHART]",
    }
    write_json(BASE / "death-certificate.json", out)
    return out


def controls_summary() -> dict[str, Any]:
    controls = ROOT / "box/g9966outer-20260903/controls.py"
    run = run_capture(["python3", str(controls)])
    payload = run.stdout
    parsed = json.loads(payload, object_pairs_hook=reject_duplicates)
    require(parsed["controls_pass"] is True, "controls did not pass")
    write_same_or_new(BASE / "controls-replay.json", payload)
    return parsed


def artifact_manifest() -> dict[str, Any]:
    rows = []
    for path in sorted(BASE.rglob("*")):
        if not path.is_file() or path.name in {"artifact-manifest.sha256", "artifact-manifest.check"}:
            continue
        rel = path.relative_to(BASE)
        rows.append(f"{sha256_file(path)}  ./{rel}\n")
    payload = "".join(rows).encode()
    write_same_or_new(BASE / "artifact-manifest.sha256", payload)
    check = subprocess.run(
        ["sha256sum", "-c", "artifact-manifest.sha256"],
        cwd=BASE,
        check=True,
        capture_output=True,
        timeout=3000,
    ).stdout
    write_same_or_new(BASE / "artifact-manifest.check", check)
    return {
        "path": str(BASE / "artifact-manifest.sha256"),
        "sha256": sha256_bytes(payload),
        "check_sha256": sha256_bytes(check),
        "entries": len(rows),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=[
        "prepare", "custody", "accept-stage8", "death-certificate",
        "controls", "manifest"
    ])
    args = parser.parse_args()
    if args.command == "prepare":
        out = prepare_workspace()
    elif args.command == "custody":
        out = custody_stage7()
    elif args.command == "accept-stage8":
        out = promote_stage8()
    elif args.command == "death-certificate":
        out = death_certificate()
    elif args.command == "controls":
        out = controls_summary()
    else:
        out = artifact_manifest()
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
