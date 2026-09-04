#!/usr/bin/env python3
"""Bounded staged guided-GB runner for sparse K=9 alpha/rho charts.

The chart builder is intentionally separate from this solver.  This program
reads its durable staged-band manifest, probes cumulative prefixes at one good
prime, repeats the first killing prefix at three good primes, and performs an
exact-Q replay only after all requested modular fibres are clean unit ideals.
No modular result is promoted on its own: the chart is an inhomogeneous
``mu*mu_inv-1`` localization.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import sys
import time
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "box" / "k4rayk89-20260903"
RUNS = HERE / "driver-audit-artifacts" / "sparse-rho-guided"
sys.path.insert(0, str(ROOT))

from box.lib.guided_gb import (  # noqa: E402
    GuidedGBResult,
    HilbertHint,
    PromotionPolicy,
    RunConfig,
    SingularSystem,
    guided_groebner,
)


GOOD_PRIMES = (32003, 32009, 32027)
MAX_TIMEOUT = 600


def terminate_owned_singulars(tag: str) -> None:
    """Terminate only Singular process groups whose script path is under tag."""

    needle = str((RUNS / tag).resolve()).encode("utf-8")
    process_groups: set[int] = set()
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        try:
            command = (entry / "cmdline").read_bytes()
            pid = int(entry.name)
            if b"Singular\0" in command and needle in command:
                process_groups.add(os.getpgid(pid))
        except (FileNotFoundError, PermissionError, ProcessLookupError):
            continue
    for process_group in process_groups:
        try:
            os.killpg(process_group, signal.SIGTERM)
        except ProcessLookupError:
            pass
    deadline = time.monotonic() + 2.0
    while process_groups and time.monotonic() < deadline:
        remaining: set[int] = set()
        for process_group in process_groups:
            try:
                os.killpg(process_group, 0)
                remaining.add(process_group)
            except ProcessLookupError:
                pass
        process_groups = remaining
        if process_groups:
            time.sleep(0.05)
    for process_group in process_groups:
        try:
            os.killpg(process_group, signal.SIGKILL)
        except ProcessLookupError:
            pass


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(path)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def generator_union_checksum(
    rows: Sequence[tuple[str, str]], globals_: Sequence[tuple[str, str]]
) -> str:
    """Independently reproduce staged_band_emitter.generator_checksum."""

    entries = [f"{label}\0{re.sub(r'\s+', '', expr.strip())}" for label, expr in rows]
    entries.extend(
        f"{label}\0{re.sub(r'\s+', '', expr.strip())}" for label, expr in globals_
    )
    return hashlib.sha256(("\n".join(sorted(entries)) + "\n").encode("utf-8")).hexdigest()


def load_hint(path: Path | None, weights: Sequence[int]) -> HilbertHint | None:
    if path is None:
        return None
    payload = json.loads(path.read_text(encoding="utf-8"))
    hint_weights = tuple(int(value) for value in payload.get("weights", weights))
    if len(hint_weights) != len(weights):
        raise ValueError("Hilbert hint weights do not match the sparse chart ring")
    return HilbertHint(
        tuple(int(value) for value in payload["numerator"]),
        hint_weights,
        None if payload.get("predicted_length") is None else int(payload["predicted_length"]),
    )


def parse_band_file(path: Path) -> list[str]:
    """Read the one-expression-per-line format emitted by staged_band_emitter."""

    expressions: list[str] = []
    inside = False
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not inside:
            if line.startswith("ideal ") and line.endswith("="):
                inside = True
            continue
        if not line:
            continue
        if not (line.startswith("(") and (line.endswith("),") or line.endswith(");"))):
            raise ValueError(f"unexpected staged generator line in {path}: {line[:100]}")
        expressions.append(line[1:-2])
        if line.endswith(");"):
            break
    if not inside:
        raise ValueError(f"no ideal declaration found in {path}")
    return expressions


def stage_rank(item: Mapping[str, Any]) -> tuple[int, int, str]:
    """Force mathematical order even for manifests from the older emitter."""

    band = str(item["band"])
    degree = int(item["degree"])
    upper = band.upper()
    if "REC4" in upper:
        return (0, 0, band)
    if "REC5" in upper:
        return (0, 1, band)
    if "REC6" in upper or "TERMINAL" in upper:
        return (0, 2, band)
    if "ALPHA" in upper:
        return (1, -degree, band)
    if "RHO" in upper:
        # Both the raw quoy chart and sparse alpha chart are triangular from
        # high total degree to low total degree.
        return (2, -degree, band)
    raise ValueError(f"untyped sparse-chart band {band!r}")


def load_chart(metadata_path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    chart_type = metadata.get("type")
    if chart_type not in {
        "K4RAY-K9-RREF-SPARSE-ALPHA-RHO",
        "K4RAY-EXPLICIT-LOWER-BANDS",
        "K9-SPARSE-RHO-DURABLE-PREFIX",
    }:
        raise ValueError(f"unsupported chart type: {chart_type!r}")
    durable_prefix = chart_type == "K9-SPARSE-RHO-DURABLE-PREFIX"
    metadata.setdefault(
        "scope",
        "RAW_EXPLICIT_TERMINAL_RHO_NECESSARY_SUBSYSTEM",
    )
    manifest_key = "manifest" if durable_prefix else "band_manifest"
    manifest_path = Path(metadata[manifest_key])
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("type") != "STAGED-SINGULAR-BAND-FILES":
        raise ValueError("unexpected staged manifest type")
    expected_union = metadata.get("band_union_checksum", metadata.get("generator_union_checksum"))
    if manifest.get("generator_union_checksum") != expected_union:
        raise ValueError("metadata/manifest generator checksum mismatch")
    metadata["band_union_checksum"] = expected_union

    stages: list[dict[str, Any]] = []
    for entry in manifest["band_files"]:
        path = Path(entry["path"])
        if sha256_file(path) != entry["sha256"]:
            raise ValueError(f"staged band hash mismatch: {path}")
        expressions = parse_band_file(path)
        if len(expressions) != int(entry["rows"]):
            raise ValueError(f"staged row count mismatch: {path}")
        stages.append(
            {
                "band": entry["band"],
                "degree": int(entry["degree"]),
                "labels": list(entry["labels"]),
                "expressions": expressions,
                "path": str(path),
                "sha256": entry["sha256"],
            }
        )
    flat_manifest = [
        (label, item["band"], item["degree"], expression)
        for item in stages
        for label, expression in zip(item["labels"], item["expressions"])
    ]
    expected_row_count = int(metadata.get("row_count", manifest["row_count"]))
    if int(manifest["row_count"]) != expected_row_count or len(flat_manifest) != expected_row_count:
        raise ValueError("metadata/manifest total row count mismatch")
    row_key = "solver_rows" if "solver_rows" in metadata else "rows" if "rows" in metadata else None
    if row_key is not None:
        flat_metadata = [
            (row["label"], row["band"], int(row["degree"]), row["expr"])
            for row in metadata[row_key]
        ]
        if sorted(flat_manifest) != sorted(flat_metadata):
            raise ValueError("metadata solver_rows differ from the hashed staged files")

    global_rows: list[tuple[str, str]] = []
    global_entry = manifest.get("global_file")
    if global_entry is not None:
        global_path = Path(global_entry["path"])
        if sha256_file(global_path) != global_entry["sha256"]:
            raise ValueError(f"global generator hash mismatch: {global_path}")
        global_expressions = parse_band_file(global_path)
        global_labels = list(global_entry["labels"])
        if len(global_expressions) != int(global_entry["rows"]) or len(global_labels) != len(
            global_expressions
        ):
            raise ValueError("global generator row/label count mismatch")
        global_rows = list(zip(global_labels, global_expressions))
    canonical_rows = [(label, expression) for label, _band, _degree, expression in flat_manifest]
    recomputed_union = generator_union_checksum(canonical_rows, global_rows)
    if recomputed_union != expected_union:
        raise ValueError("independent generator-union checksum mismatch")

    if durable_prefix:
        # Every staged row has already had its rational content cleared before
        # emission.  Refuse to synthesize denominator_lcm=1 if a rational
        # division token survived; the selected modular primes are then safe.
        if any("/" in expression for _label, expression in [*canonical_rows, *global_rows]):
            raise ValueError("durable prefix contains an uncleared rational division")
        metadata["denominator_lcm"] = 1
        metadata["denominator_policy"] = "all emitted generators integral after row-wise clearing"
        metadata["chart_sha256"] = sha256_file(metadata_path)
        metadata["band_manifest"] = str(manifest_path)
    stages.sort(key=stage_rank)
    return metadata, stages


def ring(
    metadata: Mapping[str, Any], characteristic: int, order: str
) -> tuple[str, list[str], list[int]]:
    names = [str(value) for value in metadata.get("solver_variables", metadata["variables"])]
    weights = [int(value) for value in metadata.get("solver_weights", metadata["weights"])]
    if len(names) != len(weights) or len(set(names)) != len(names):
        raise ValueError("invalid variable/weight declaration")
    if characteristic in (2, 3) or (
        characteristic and int(metadata["denominator_lcm"]) % characteristic == 0
    ):
        raise ValueError(
            f"bad characteristic {characteristic}; denominator lcm={metadata['denominator_lcm']}"
        )
    if order == "metadata-wp":
        order_spec = f"wp({','.join(str(value) for value in weights)})"
    elif order == "h-pivot-block":
        pairs = list(zip(names, weights))
        pivots = [pair for pair in pairs if re.fullmatch(r"h[456]_\d+_\d+", pair[0])]
        rest = [pair for pair in pairs if pair not in pivots]
        if len(pivots) != 15:
            raise ValueError(
                f"h-pivot-block requires the raw 15-variable h4/h5/h6 block; found {len(pivots)}"
            )
        pairs = [*pivots, *rest]
        names = [name for name, _weight in pairs]
        weights = [weight for _name, weight in pairs]
        rest_weights = [weight for _name, weight in rest]
        order_spec = f"(dp(15),wp({','.join(str(value) for value in rest_weights)}))"
    else:
        raise ValueError(f"unknown order {order!r}")
    return (f"ring SS={characteristic},({','.join(names)}),{order_spec};", names, weights)


def summarize(result: GuidedGBResult) -> dict[str, Any]:
    return {
        "verdict": result.verdict.value,
        "promotion_note": result.certificate["promotion_note"],
        "accepted_run_count": result.certificate["accepted_run_count"],
        "runs": [
            {
                "label": run["label"],
                "characteristic": run["characteristic"],
                "returncode": run["returncode"],
                "timed_out": run["timed_out"],
                "elapsed_seconds": run["elapsed_seconds"],
                "unit": run["main"]["unit"],
                "dimension": run["main"]["dimension"],
                "vdim": run["main"]["vdim"],
                "basis_size": run["main"]["basis_size"],
                "nf_all_zero": run["main"]["nf_all_zero"],
                "accepted": run["main"]["accepted"],
                "missing_markers": run["main"]["missing_markers"],
                "script": run["script"],
                "script_sha256": run["script_sha256"],
                "stdout": run["stdout"],
                "stdout_sha256": run["stdout_sha256"],
            }
            for run in result.certificate["runs"]
        ],
    }


def clean_unit(run: Mapping[str, Any]) -> bool:
    return bool(
        run["returncode"] == 0
        and not run["timed_out"]
        and run["unit"]
        and run["nf_all_zero"]
        and run["accepted"]
        and not run["missing_markers"]
    )


def clean_completed(run: Mapping[str, Any]) -> bool:
    """Reject the guided library's known POSDIM-on-error edge case."""

    return bool(
        run["returncode"] == 0
        and not run["timed_out"]
        and run["nf_all_zero"]
        and run["accepted"]
        and not run["missing_markers"]
    )


def run_systems(
    metadata: Mapping[str, Any],
    generators: Sequence[str],
    characteristics: Sequence[int],
    *,
    stage: str,
    output_dir: Path,
    timeout: int,
    hint_path: Path | None,
    order: str,
) -> GuidedGBResult:
    systems: list[SingularSystem] = []
    hint: HilbertHint | None = None
    for characteristic in characteristics:
        ring_line, names, weights = ring(metadata, characteristic, order)
        if order != "metadata-wp" and hint_path is not None:
            raise ValueError("Hilbert hints are disabled for the h-pivot block order")
        if hint is None:
            hint = load_hint(hint_path, weights)
        systems.append(
            SingularSystem(
                name=f"K9_{metadata['branch']}_{stage}_p{characteristic}",
                prelude="\n".join(
                    ("option(redSB); short=0;", ring_line, 'print("SPARSE_RHO__PRELUDE_DONE 1");')
                ),
                generators=tuple([*generators, "mu*mu_inv-1"]),
                characteristic=characteristic,
                variables=tuple(names),
                homogeneous=False,
                positive_weights=(),
                metadata={
                    "K": 9,
                    "branch": metadata["branch"],
                    "stage": stage,
                    "scope": metadata["scope"],
                    "chart_sha256": metadata["chart_sha256"],
                    "inhomogeneous_localization": True,
                    "modular_unit_requires_exact_Q": True,
                    "monomial_order": order,
                },
            )
        )
    return guided_groebner(
        systems,
        hint=hint,
        policy=PromotionPolicy.exact_q("inhomogeneous sparse-alpha/rho localization"),
        config=RunConfig(
            output_dir=output_dir,
            timeout_seconds=timeout,
            total_cores=1,
            max_parallel_jobs=1,
            run_perturbed_control=False,
            no_rc=True,
        ),
    )


def run_workflow(
    metadata_path: Path,
    tag: str,
    probe_prime: int,
    primes: Sequence[int],
    timeout: int,
    overall_timeout: int,
    hint_path: Path | None,
    order: str,
    start_index: int,
) -> dict[str, Any]:
    if not 1 <= timeout <= MAX_TIMEOUT:
        raise ValueError(f"timeout must be in [1,{MAX_TIMEOUT}]")
    metadata, stages = load_chart(metadata_path)
    if not stages:
        raise ValueError("sparse chart contains no stages")
    if not 0 <= start_index < len(stages):
        raise ValueError(f"start-index must be in [0,{len(stages) - 1}]")
    base = RUNS / tag / f"K9_{metadata['branch']}"
    prefix: list[str] = []
    progress: list[dict[str, Any]] = []
    killing_index: int | None = None
    started = time.monotonic()

    def bounded_call_timeout() -> int | None:
        remaining = overall_timeout - (time.monotonic() - started)
        # Preserve room for guided_gb's own ten-second TERM->KILL cleanup and
        # atomic summary writes before an external wrapper can fire.
        if remaining <= 15:
            return None
        return max(1, min(timeout, int(remaining - 15)))

    for index, item in enumerate(stages):
        prefix.extend(item["expressions"])
        if index < start_index:
            continue
        call_timeout = bounded_call_timeout()
        if call_timeout is None:
            break
        stage = f"prefix{index:02d}_{item['band']}"
        result = run_systems(
            metadata,
            prefix,
            (probe_prime,),
            stage=stage,
            output_dir=base / "probe" / stage,
            timeout=call_timeout,
            hint_path=hint_path,
            order=order,
        )
        summary = summarize(result)
        record = {
            "stage_index": index,
            "stage": stage,
            "last_band": item["band"],
            "cumulative_row_count": len(prefix),
            **summary,
        }
        progress.append(record)
        atomic_write(base / "probe-progress.json", json.dumps(progress, indent=2, sort_keys=True) + "\n")
        if summary["runs"] and clean_unit(summary["runs"][0]):
            killing_index = index
            break

    confirmation: dict[str, Any] | None = None
    exact: dict[str, Any] | None = None
    if killing_index is not None:
        killing_rows = [
            expression
            for item in stages[: killing_index + 1]
            for expression in item["expressions"]
        ]
        killing_stage = next(
            record["stage"] for record in progress if record["stage_index"] == killing_index
        )
        call_timeout = bounded_call_timeout()
        if call_timeout is not None:
            modular_result = run_systems(
                metadata,
                killing_rows,
                primes,
                stage=f"confirm_{killing_stage}",
                output_dir=base / "confirm-modular" / killing_stage,
                timeout=call_timeout,
                hint_path=hint_path,
                order=order,
            )
            confirmation = {
                "stage_index": killing_index,
                "stage": killing_stage,
                "cumulative_row_count": len(killing_rows),
                **summarize(modular_result),
            }
        else:
            confirmation = None
        modular_runs = [] if confirmation is None else confirmation["runs"]
        if len(modular_runs) == len(primes) and all(clean_unit(run) for run in modular_runs):
            call_timeout = bounded_call_timeout()
            if call_timeout is not None:
                exact_result = run_systems(
                    metadata,
                    killing_rows,
                    (0,),
                    stage=f"exact_{killing_stage}",
                    output_dir=base / "confirm-exact-Q" / killing_stage,
                    timeout=call_timeout,
                    hint_path=hint_path,
                    order=order,
                )
                exact = {
                    "stage_index": killing_index,
                    "stage": killing_stage,
                    "cumulative_row_count": len(killing_rows),
                    **summarize(exact_result),
                }

    if exact is not None and exact["runs"] and all(clean_completed(run) for run in exact["runs"]):
        verdict = exact["verdict"]
    elif exact is not None:
        verdict = "INCONCLUSIVE_EXACT_Q_CONTROLS_FAILED"
    elif killing_index is not None:
        verdict = "MODULAR_ONLY__NO_CHAR0_PROMOTION"
    elif time.monotonic() - started >= overall_timeout - 15:
        verdict = "INCONCLUSIVE_OVERALL_DEADLINE"
    elif any(run["timed_out"] for item in progress for run in item["runs"]):
        verdict = "INCONCLUSIVE_TIMEOUT"
    else:
        verdict = "NO_UNIT_IN_PROBED_PREFIXES__FP_ONLY"
    payload = {
        "type": "K4RAY-K9-SPARSE-RHO-STAGED-GUIDED-GB",
        "tag": tag,
        "K": 9,
        "branch": metadata["branch"],
        "scope": metadata["scope"],
        "metadata_path": str(metadata_path),
        "metadata_sha256": sha256_file(metadata_path),
        "chart_sha256": metadata["chart_sha256"],
        "band_union_checksum": metadata["band_union_checksum"],
        "probe_prime": probe_prime,
        "confirmation_primes": list(primes),
        "per_call_timeout_seconds": timeout,
        "overall_timeout_seconds": overall_timeout,
        "total_cores": 1,
        "monomial_order": order,
        "stage_order": [item["band"] for item in stages],
        "start_index": start_index,
        "seeded_unprobed_bands": [item["band"] for item in stages[:start_index]],
        "progress": progress,
        "first_modular_unit_stage_index": killing_index,
        "confirmation": confirmation,
        "exact": exact,
        "verdict": verdict,
        "fallacy_v2": {
            "modular_unit": "F_p-only until the exact-Q replay is a clean unit",
            "posdim": "necessary subsystem only; not a point or counterexample",
        },
        "elapsed_seconds": round(time.monotonic() - started, 6),
    }
    atomic_write(base / "summary.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    atomic_write(
        RUNS / tag / "aggregate.json",
        json.dumps(
            {
                "tag": tag,
                "K": 9,
                "branch": metadata["branch"],
                "verdict": verdict,
                "summary": str(base / "summary.json"),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
    )
    print(json.dumps({"branch": metadata["branch"], "verdict": verdict, "summary": str(base / "summary.json")}, sort_keys=True))
    return payload


def parse_primes(value: str) -> tuple[int, ...]:
    primes = tuple(int(piece) for piece in value.split(",") if piece)
    if not primes:
        raise ValueError("at least one confirmation prime is required")
    return primes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tag")
    parser.add_argument("metadata", type=Path)
    parser.add_argument("--probe-prime", type=int, default=GOOD_PRIMES[0])
    parser.add_argument("--primes", default=",".join(str(prime) for prime in GOOD_PRIMES))
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--overall-timeout", type=int, default=3600)
    parser.add_argument("--hint-json", type=Path)
    parser.add_argument(
        "--order",
        choices=("metadata-wp", "h-pivot-block"),
        default="metadata-wp",
    )
    parser.add_argument(
        "--start-index",
        type=int,
        default=0,
        help="seed earlier bands without re-probing them; probe from this zero-based stage",
    )
    args = parser.parse_args()

    def stop_handler(signum: int, _frame: Any) -> None:
        terminate_owned_singulars(args.tag)
        raise SystemExit(128 + signum)

    signal.signal(signal.SIGINT, stop_handler)
    signal.signal(signal.SIGTERM, stop_handler)
    try:
        run_workflow(
            args.metadata,
            args.tag,
            args.probe_prime,
            parse_primes(args.primes),
            args.timeout,
            args.overall_timeout,
            args.hint_json,
            args.order,
            args.start_index,
        )
    finally:
        terminate_owned_singulars(args.tag)


if __name__ == "__main__":
    main()
