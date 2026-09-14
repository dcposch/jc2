#!/usr/bin/env python3
"""Regression tests for box/lib guided GB and staged band helpers."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
import time
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "box/sysguidedgb-20260903"
RUNS = OUT / "runs"
LOG = OUT / "test.log"
RECEIPT = ROOT / "xmodel/sys-guided-gb-gpt55-20260903.run.v2"
INPUTS = Path("/tmp/jc2-lane.RZOERU/inputs")

sys.path.insert(0, str(ROOT))

from box.lib.guided_gb import (  # noqa: E402
    HilbertHint,
    PromotionPolicy,
    RunConfig,
    SingularSystem,
    Verdict,
    guided_groebner,
    prelude_from_script,
)
from box.lib.staged_band_emitter import (  # noqa: E402
    emit_order_chart_bands,
    generator_checksum,
    read_order_rows_tsv,
)


def write_log(lines: list[str], message: str) -> None:
    print(message)
    lines.append(message)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def verify_frozen_inputs(lines: list[str]) -> dict[str, Any]:
    fields: dict[int, dict[str, str]] = {}
    for line in RECEIPT.read_text(encoding="utf-8").splitlines():
        match = re.match(r"charged_input_(\d+)_(basename|sha256)=(.*)", line)
        if match:
            fields.setdefault(int(match.group(1)), {})[match.group(2)] = match.group(3)
    manifest_lines = []
    for index in sorted(fields):
        item = fields[index]
        manifest_lines.append(f"{item['sha256']}  {INPUTS / item['basename']}")
    manifest = OUT / "charged_inputs.from_receipt.sha256"
    manifest.write_text("\n".join(manifest_lines) + "\n", encoding="utf-8")
    replay = subprocess.run(
        ["sha256sum", "-c", str(manifest)],
        text=True,
        capture_output=True,
        check=True,
    )
    check_log = OUT / "charged_inputs.sha256sum.log"
    check_log.write_text(replay.stdout, encoding="utf-8")
    write_log(lines, f"INPUTS PASS: {len(manifest_lines)} charged inputs verified via {check_log.relative_to(ROOT)}")
    return {"manifest": str(manifest), "check_log": str(check_log), "count": len(manifest_lines)}


def card_a_system(script: Path, meta: dict[str, Any], name: str) -> SingularSystem:
    return SingularSystem(
        name=name,
        prelude=prelude_from_script(script),
        generators=tuple(f"T{row}" for row in meta["selected_rows"]),
        characteristic=1009,
        variables=tuple(meta["variables"]),
        homogeneous=True,
        positive_weights=tuple(meta["weights"]),
        metadata={
            "source_script": str(script.relative_to(ROOT)),
            "source_sha256": meta["source_sha256"],
            "t": meta["t"],
            "selected_rows": meta["selected_rows"],
        },
    )


def run_card_a_t(lines: list[str], t: int, expected_length: int) -> dict[str, Any]:
    systems = []
    for branch in (0, 1):
        stem = f"t{t}_p1009_b{branch}_tail_guided"
        script = ROOT / f"box/k16stdhilb-20260903/{stem}.sing"
        meta = load_json(script.with_suffix(".json"))
        require(meta["predicted_tail_length"] == expected_length, f"T1 t={t} length metadata mismatch")
        systems.append(card_a_system(script, meta, f"T1_t{t}_b{branch}"))
    hint = HilbertHint.from_sequences(
        load_json(ROOT / f"box/k16stdhilb-20260903/t{t}_p1009_b0_tail_guided.json")["target_hnum"],
        systems[0].positive_weights,
        expected_length,
    )
    started = time.monotonic()
    result = guided_groebner(
        systems,
        hint=hint,
        policy=PromotionPolicy.homogeneous_properness(
            "Card A: homogeneous positive-weight tail ideal; properness promotes modular dim 0 only."
        ),
        config=RunConfig(
            output_dir=RUNS / f"T1_t{t}",
            timeout_seconds=1800,
            total_cores=4,
            max_parallel_jobs=2,
            run_perturbed_control=True,
        ),
    )
    elapsed = time.monotonic() - started
    require(result.verdict == Verdict.DIM0_CHAR0, f"T1 t={t} verdict {result.verdict}")
    require(result.certificate["accepted_run_count"] == 2, f"T1 t={t} did not accept both fibres")
    for run in result.certificate["runs"]:
        main = run["main"]
        perturbed = run["perturbed"]
        require(main["dimension"] == 0, f"T1 t={t} nonzero dim in {run['label']}")
        require(main["lead_vdim"] == expected_length, f"T1 t={t} bad lead length in {run['label']}")
        require(main["accepted"] is True, f"T1 t={t} main control did not accept {run['label']}")
        require(perturbed is not None and perturbed["accepted"] is False, f"T1 t={t} perturb accepted {run['label']}")
    write_log(
        lines,
        f"T1 t={t} PASS: both fibres DIM0_CHAR0, length={expected_length}, perturbed controls failed, wall={elapsed:.2f}s",
    )
    return result.to_json()


def test_card_a(lines: list[str]) -> dict[str, Any]:
    return {
        "t5": run_card_a_t(lines, 5, 3640),
        "t6": run_card_a_t(lines, 6, 23256),
    }


def test_g108_unit(lines: list[str]) -> dict[str, Any]:
    script = ROOT / "box/g108gate-20260903/runs/delta3/stage0/death_replay.sing"
    system = SingularSystem(
        name="T2_g108_delta3_stage0_common_h3",
        prelude=prelude_from_script(script, stop_regex=r"^ideal Raw="),
        generators=(
            "minor_n6_pi0",
            "minor_n7_pi0",
            "minor_n7_pi1",
            "minor_n8_pi0",
            "minor_n8_pi1",
            "L",
        ),
        characteristic=0,
        variables=("jet1", "jet2", "c", "Zc"),
        homogeneous=False,
        metadata={"source_script": str(script.relative_to(ROOT))},
    )
    started = time.monotonic()
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q("D=108 stage-0 replay runs over Q."),
        config=RunConfig(
            output_dir=RUNS / "T2_g108_unit",
            timeout_seconds=1800,
            total_cores=4,
            max_parallel_jobs=1,
            run_perturbed_control=False,
        ),
    )
    elapsed = time.monotonic() - started
    run = result.certificate["runs"][0]
    require(result.verdict == Verdict.UNIT_IDEAL_CHAR0, f"T2 verdict {result.verdict}")
    require(run["main"]["unit"] is True, "T2 did not reduce 1 to 0")
    require(run["main"]["dimension"] == -1, f"T2 unexpected dimension {run['main']['dimension']}")
    write_log(lines, f"T2 PASS: D=108 stage-0 common-h3 exact-Q UNIT_IDEAL_CHAR0, wall={elapsed:.2f}s")
    return result.to_json()


def test_t2_negative(lines: list[str]) -> dict[str, Any]:
    script = ROOT / "box/k16stdhilb-20260903/t2_y1over5_full_negative_guided.sing"
    meta = load_json(script.with_suffix(".json"))
    system = SingularSystem(
        name="T3_t2_y1over5_negative",
        prelude=prelude_from_script(script),
        generators=tuple(f"T{row}" for row in meta["selected_rows"]),
        characteristic=0,
        variables=tuple(meta["variables"]),
        homogeneous=True,
        positive_weights=tuple(meta["weights"]),
        metadata={"source_script": str(script.relative_to(ROOT))},
    )
    started = time.monotonic()
    result = guided_groebner(
        system,
        policy=PromotionPolicy.exact_q("Boundary control is exact over Q."),
        config=RunConfig(
            output_dir=RUNS / "T3_t2_negative",
            timeout_seconds=1800,
            total_cores=4,
            max_parallel_jobs=1,
            run_perturbed_control=False,
        ),
    )
    elapsed = time.monotonic() - started
    run = result.certificate["runs"][0]
    require(result.verdict == Verdict.POSDIM, f"T3 verdict {result.verdict}")
    require(run["main"]["dimension"] == 1, f"T3 expected dim 1, got {run['main']['dimension']}")
    require(run["main"]["unit"] is False, "T3 unexpectedly unit")
    write_log(lines, f"T3 PASS: t=2,y=1/5 exact-Q POSDIM dim=1, wall={elapsed:.2f}s")
    return result.to_json()


def test_staged_emitter(lines: list[str]) -> dict[str, Any]:
    meta = ROOT / "box/orderbasis-20260903/meta/25_15_21_2_k2_part_3_full.json"
    payload = load_json(meta)
    rows_path = ROOT / payload["rows_path"]
    rows = read_order_rows_tsv(rows_path, x_weight=1, y_weight=1, band_column="h_power")
    expected_checksum = generator_checksum(rows, (("localization", f"T*({payload['sat']})-1"),))
    started = time.monotonic()
    manifest = emit_order_chart_bands(
        meta,
        RUNS / "T4_25_15_bands",
        characteristic=0,
        x_weight=1,
        y_weight=1,
        band_column="h_power",
        include_saturation=True,
    )
    elapsed = time.monotonic() - started
    require(manifest["row_count"] == len(rows), "T4 row count mismatch")
    require(manifest["row_count"] == payload["meta"]["equations"], "T4 metadata equation count mismatch")
    require(manifest["band_count"] > 1, "T4 did not split into multiple bands")
    require(manifest["generator_union_checksum"] == expected_checksum, "T4 union checksum mismatch")
    require(manifest["monolithic_generator_checksum"] == expected_checksum, "T4 monolithic checksum mismatch")
    require(manifest["union_equals_monolithic"] is True, "T4 union flag false")
    require(sum(item["rows"] for item in manifest["band_files"]) == len(rows), "T4 band row sum mismatch")
    for item in manifest["band_files"]:
        require(Path(item["path"]).is_file(), f"T4 missing band file {item['path']}")
    require(manifest["global_file"] and Path(manifest["global_file"]["path"]).is_file(), "T4 missing global file")
    write_log(
        lines,
        f"T4 PASS: staged (25,15) emitted {manifest['band_count']} band files, rows={len(rows)}, checksum={expected_checksum}, wall={elapsed:.2f}s",
    )
    return manifest


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    RUNS.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []
    started = time.monotonic()
    write_log(lines, "sysguidedgb regression run started")
    results: dict[str, Any] = {}
    tests = [
        ("inputs", verify_frozen_inputs),
        ("T1_card_a", test_card_a),
        ("T2_g108_unit", test_g108_unit),
        ("T3_t2_negative", test_t2_negative),
        ("T4_staged_emitter", test_staged_emitter),
    ]
    try:
        for name, fn in tests:
            write_log(lines, f"{name} START")
            results[name] = fn(lines)
        total = time.monotonic() - started
        results["summary"] = {"status": "PASS", "wall_seconds": round(total, 3)}
        (OUT / "test-results.json").write_text(
            json.dumps(results, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        write_log(lines, f"ALL TESTS PASS wall={total:.2f}s")
    except Exception as exc:
        total = time.monotonic() - started
        results["summary"] = {"status": "FAIL", "wall_seconds": round(total, 3), "error": repr(exc)}
        (OUT / "test-results.json").write_text(
            json.dumps(results, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        write_log(lines, f"TEST FAILURE after {total:.2f}s: {exc!r}")
        raise


if __name__ == "__main__":
    main()

