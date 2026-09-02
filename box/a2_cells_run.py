#!/usr/bin/env python3
"""Run the charged A2-E1WALL-CELLS window through qqideal/msolveio.

Order is mandatory:

1. Fraction-only self-checks.
2. Item-0 (1,3), mod-p EVIDENCE screen then characteristic-zero-form run.
   Anything except Kind.EMPTY from the latter is ORACLE-P0 and exits 2.
3. Items 1--4, each with the same mod-p-then-Q-form order.

The saturation row is already in every :class:`CellSystem`; this runner never
calls qqideal.saturate() and never passes opens=.  Verdicts have no boolean
truth value and are always inspected through ``verdict.kind``.

Examples:

  python3 box/a2_cells_run.py --self-check
  python3 box/a2_cells_run.py --gate-only --binary /path/to/msolve
  python3 box/a2_cells_run.py --timeout 3600 --threads 8 --binary /path/to/msolve

``--accelerators`` affects only the surviving items 1--4.  The item-0 boundary
is always the exact 37-generator base system, and accelerators are off by
default everywhere.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import traceback
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Tuple


# Support ``python3 box/a2_cells_run.py`` from any working directory.
BOX_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BOX_DIR))

from a2_cells_jobs import (  # noqa: E402
    RUN_CELLS,
    CellSystem,
    build_cell,
    build_qqideal,
    run_self_checks,
)


EXPECTED_PACKAGE_VERSIONS = {"qqideal": "0.2.0", "msolveio": "0.2.1"}  # cut over 2026-09-02 ~08:28Z after a zero-disagreement mini-oracle
# Coordinator 2026-09-02: an explicit env override for the pinned package
# versions, so a candidate stack (e.g. qqideal 0.2.0 + msolveio 0.2.1) can be
# run through the SAME gate/oracle path in a separate venv without editing
# the default pin. Format: A2_CELLS_PACKAGE_VERSIONS="qqideal=0.2.0,msolveio=0.2.1".
# The default pin is unchanged; the override is echoed by the preflight line.
_override = os.environ.get("A2_CELLS_PACKAGE_VERSIONS")
if _override:
    EXPECTED_PACKAGE_VERSIONS = {
        k.strip(): v.strip()
        for k, v in (item.split("=", 1) for item in _override.split(",") if "=" in item)
    }
EXPECTED_MSOLVE_VERSION = "0.10.1"
DEFAULT_PRIME = 65521


@dataclass(frozen=True)
class SolveRecord:
    item: str
    e: int
    U: int
    phase: str
    field: str
    role: str
    verdict: object
    variables: int
    generators: int
    accelerators: bool
    input_sha256: str
    output_sha256: str
    msolve_version: Optional[str]
    wall_seconds: float
    detail: Optional[str]


def _is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value in (2, 3):
        return True
    if value % 2 == 0 or value % 3 == 0:
        return False
    divisor = 5
    step = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += step
        step = 6 - step
    return True


def _resolve_binary(requested: Optional[str]) -> str:
    candidate = requested or os.environ.get("MSOLVE_BINARY") or shutil.which("msolve")
    if not candidate:
        raise RuntimeError(
            "msolve was not found; pass --binary /absolute/path/to/msolve "
            "to pin version 0.10.1"
        )
    found = shutil.which(candidate) if os.sep not in candidate else candidate
    if not found:
        raise RuntimeError(f"msolve binary {candidate!r} was not found")
    path = Path(found).expanduser().resolve()
    if not path.is_file():
        raise RuntimeError(f"msolve binary is not a file: {path}")
    if not os.access(path, os.X_OK):
        raise RuntimeError(f"msolve binary is not executable: {path}")
    completed = subprocess.run(
        (str(path), "--version"),
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=10,
        check=False,
    )
    version = (completed.stdout or completed.stderr).strip().splitlines()[0]
    if completed.returncode != 0 or version != EXPECTED_MSOLVE_VERSION:
        raise RuntimeError(
            f"msolve version gate failed for {path}: rc={completed.returncode}, "
            f"reported={version!r}, required={EXPECTED_MSOLVE_VERSION!r}"
        )
    return str(path)


def _import_stack() -> Dict[str, Any]:
    """Import only after --self-check has had a chance to exit."""
    observed = {
        package: importlib.metadata.version(package)
        for package in EXPECTED_PACKAGE_VERSIONS
    }
    if observed != EXPECTED_PACKAGE_VERSIONS:
        raise RuntimeError(
            f"package version gate failed: observed={observed}, "
            f"required={EXPECTED_PACKAGE_VERSIONS}"
        )
    import msolveio
    from qqideal import Certainty, Kind, Verdict

    return {
        "msolveio": msolveio,
        "Certainty": Certainty,
        "Kind": Kind,
        "Verdict": Verdict,
    }


def _typed_run(
    system: CellSystem,
    *,
    item: str,
    characteristic: int,
    timeout: float,
    threads: int,
    binary: str,
    stack: Dict[str, Any],
) -> SolveRecord:
    """One binary-pinned msolve call, typed with qqideal's Verdict enums."""
    msolveio = stack["msolveio"]
    Certainty = stack["Certainty"]
    Kind = stack["Kind"]
    Verdict = stack["Verdict"]
    is_screen = characteristic != 0
    phase = "mod-p" if is_screen else "char-0"
    field = f"F_{characteristic}" if is_screen else "Q-form"
    role = "EVIDENCE-only" if is_screen else "DECISIVE"
    source = ""
    input_sha256 = ""
    output_sha256 = ""
    detail: Optional[str] = None
    result = None
    started = time.monotonic()

    try:
        ideal = build_qqideal(system, characteristic=characteristic)
        source = ideal.to_msolve()
        input_sha256 = hashlib.sha256(source.encode("utf-8")).hexdigest()
        result = msolveio.run_groebner(
            source,
            gb=1 if is_screen else 2,
            timeout=timeout,
            threads=threads,
            binary=binary,
            allow_unknown_version=False,
        )
        wall_seconds = result.wall_seconds
        # Preserve output custody even if a subsequent envelope/map check fails.
        output_sha256 = result.output_sha256

        # Strong map/parser/version checks. A mismatch is ERROR, never a verdict.
        if result.input_sha256 != input_sha256:
            raise AssertionError(
                f"RunResult input hash {result.input_sha256} != local {input_sha256}"
            )
        if result.msolve_version != EXPECTED_MSOLVE_VERSION:
            raise AssertionError(
                f"msolve version drift: {result.msolve_version!r}"
            )
        output = result.output
        if output.characteristic != characteristic:
            raise AssertionError(
                f"output characteristic {output.characteristic} != input {characteristic}"
            )
        if tuple(output.variables) != system.variables:
            raise AssertionError("msolve echoed a different variable map/order")
        if output.leading_only != is_screen:
            raise AssertionError(
                f"wrong output mode: leading_only={output.leading_only}, screen={is_screen}"
            )
        if output.monomial_order != "graded reverse lexicographical":
            raise AssertionError(f"unexpected monomial order {output.monomial_order!r}")
        # msolveio validates the output envelope.  Re-coerce every basis entry
        # through qqideal as the output-side ring map before trusting NONEMPTY.
        # This rejects undeclared identifiers and malformed lifted polynomials.
        mapped_basis = tuple(ideal.ring(entry) for entry in output.basis)
        if any(poly.ring != ideal.ring for poly in mapped_basis):
            raise AssertionError("msolve basis image escaped the declared qqideal ring")

        if output.unit_ideal:
            verdict = Verdict(
                kind=Kind.EMPTY,
                dim=None,
                degree=None,
                certainty=Certainty.PROVEN if is_screen else Certainty.MODULAR,
                msolve_version=result.msolve_version,
                detail=(
                    f"exact only over F_{characteristic}; EVIDENCE for Q"
                    if is_screen
                    else (
                        "characteristic-zero input, but msolve 0.10.1 returns a "
                        "unit basis after its internal modular computation"
                    )
                ),
            )
        else:
            verdict = Verdict(
                kind=Kind.NONEMPTY,
                dim=None,
                degree=None,
                certainty=Certainty.PROVEN,
                msolve_version=result.msolve_version,
                detail=(
                    f"proper leading ideal over F_{characteristic}; EVIDENCE for Q"
                    if is_screen
                    else "lifted proper Groebner basis over Q"
                ),
            )
        detail = verdict.detail
        version: Optional[str] = result.msolve_version
    except msolveio.MsolveTimeout as exc:
        wall_seconds = time.monotonic() - started
        detail = str(exc)
        verdict = Verdict(
            kind=Kind.TIMEOUT,
            dim=None,
            degree=None,
            certainty=Certainty.MODULAR,
            msolve_version=None,
            detail=detail,
        )
        version = None
    except Exception as exc:  # noqa: BLE001 -- every solver/map failure is typed
        wall_seconds = time.monotonic() - started
        detail = f"{type(exc).__name__}: {exc}"
        version = result.msolve_version if result is not None else None
        verdict = Verdict(
            kind=Kind.ERROR,
            dim=None,
            degree=None,
            certainty=Certainty.MODULAR,
            msolve_version=version,
            detail=detail,
        )
        traceback.print_exc()

    return SolveRecord(
        item=item,
        e=system.e,
        U=system.U,
        phase=phase,
        field=field,
        role=role,
        verdict=verdict,
        variables=system.unknown_count,
        generators=system.generator_count,
        accelerators=system.accelerators,
        input_sha256=input_sha256,
        output_sha256=output_sha256,
        msolve_version=version,
        wall_seconds=wall_seconds,
        detail=detail,
    )


def _run_cell(
    item: str,
    e: int,
    U: int,
    *,
    prime: int,
    screen_timeout: float,
    timeout: float,
    threads: int,
    binary: str,
    accelerators: bool,
    stack: Dict[str, Any],
) -> Tuple[SolveRecord, SolveRecord]:
    # The inhomogeneous gate never receives residual accelerator pins.
    use_accelerators = accelerators and item != "item-0"
    try:
        system = build_cell(e, U, accelerators=use_accelerators)
    except Exception as exc:  # noqa: BLE001 -- a build failure is a typed non-answer
        traceback.print_exc()
        Kind = stack["Kind"]
        Certainty = stack["Certainty"]
        Verdict = stack["Verdict"]
        detail = f"cell construction failed: {type(exc).__name__}: {exc}"

        def build_error_record(*, characteristic: int) -> SolveRecord:
            is_screen = characteristic != 0
            verdict = Verdict(
                kind=Kind.ERROR,
                dim=None,
                degree=None,
                certainty=Certainty.MODULAR,
                msolve_version=None,
                detail=detail,
            )
            return SolveRecord(
                item=item,
                e=e,
                U=U,
                phase="mod-p" if is_screen else "char-0",
                field=f"F_{characteristic}" if is_screen else "Q-form",
                role="EVIDENCE-only" if is_screen else "DECISIVE",
                verdict=verdict,
                variables=0,
                generators=0,
                accelerators=use_accelerators,
                input_sha256="",
                output_sha256="",
                msolve_version=None,
                wall_seconds=0.0,
                detail=detail,
            )

        screen = build_error_record(characteristic=prime)
        decisive = build_error_record(characteristic=0)
        print(
            f"--- {item} cell=({e},{U}) BUILD ERROR "
            f"accelerators={use_accelerators} ---",
            flush=True,
        )
        print(f"  mod-{prime}: ERROR certainty=MODULAR role=EVIDENCE-only", flush=True)
        print("  char-0: ERROR certainty=MODULAR role=DECISIVE", flush=True)
        return screen, decisive

    print(
        f"--- {item} cell=({e},{U}) vars={system.unknown_count} "
        f"gens={system.generator_count} accelerators={system.accelerators} ---",
        flush=True,
    )
    screen = _typed_run(
        system,
        item=item,
        characteristic=prime,
        timeout=screen_timeout,
        threads=threads,
        binary=binary,
        stack=stack,
    )
    print(
        f"  mod-{prime}: {screen.verdict.kind.value.upper()} "
        f"certainty={screen.verdict.certainty.value.upper()} role=EVIDENCE-only "
        f"sha256={screen.input_sha256 or 'UNAVAILABLE'}",
        flush=True,
    )
    # Never short-circuit the Q-form call on any modular outcome.
    decisive = _typed_run(
        system,
        item=item,
        characteristic=0,
        timeout=timeout,
        threads=threads,
        binary=binary,
        stack=stack,
    )
    print(
        f"  char-0: {decisive.verdict.kind.value.upper()} "
        f"certainty={decisive.verdict.certainty.value.upper()} role=DECISIVE "
        f"sha256={decisive.input_sha256 or 'UNAVAILABLE'}",
        flush=True,
    )
    return screen, decisive


def print_verdict_table(records: Sequence[SolveRecord]) -> None:
    headers = (
        "item/cell",
        "phase(field)",
        "role",
        "kind",
        "certainty",
        "V/E",
        "accel",
        "msolve",
        "wall_s",
        "input_sha256",
        "output_sha256",
    )
    rows: List[List[str]] = [list(headers)]
    for record in records:
        rows.append(
            [
                f"{record.item}({record.e},{record.U})",
                f"{record.phase}({record.field})",
                record.role,
                record.verdict.kind.value.upper(),
                record.verdict.certainty.value.upper(),
                f"{record.variables}/{record.generators}",
                "on" if record.accelerators else "off",
                record.msolve_version or "-",
                f"{record.wall_seconds:.3f}",
                record.input_sha256 or "UNAVAILABLE",
                record.output_sha256 or "UNAVAILABLE",
            ]
        )
    widths = [max(len(row[column]) for row in rows) for column in range(len(headers))]

    def render(row: Sequence[str]) -> str:
        return "  ".join(value.ljust(widths[i]) for i, value in enumerate(row))

    print()
    print("=== A2-E1WALL-CELLS verdict table ===")
    print(render(rows[0]))
    print("  ".join("-" * width for width in widths))
    for row in rows[1:]:
        print(render(row))
    print()
    print(
        "Certainty scope: mod-p rows are exact only for the displayed finite "
        "field and are EVIDENCE for Q. A Q-form EMPTY from msolve 0.10.1 is "
        "MODULAR by qqideal 0.1.0's contract; Q-form NONEMPTY from -g 2 is PROVEN."
    )


def _p0_banner(record: SolveRecord) -> None:
    print()
    print("=" * 88)
    print("ORACLE-P0  ORACLE-P0  ORACLE-P0")
    print(
        "ORACLE-P0  ITEM-0 (1,3) FAILED THE SECOND-ENGINE PROMOTION GATE: "
        f"Q-form kind={record.verdict.kind.value.upper()} "
        f"certainty={record.verdict.certainty.value.upper()}"
    )
    print(f"ORACLE-P0  detail={record.detail!r}")
    print("ORACLE-P0  refusing to run items 1-4; exit status 2")
    print("=" * 88)


def run_campaign(
    *,
    prime: int,
    screen_timeout: float,
    timeout: float,
    threads: int,
    binary: str,
    accelerators: bool,
    gate_only: bool,
    stack: Dict[str, Any],
) -> int:
    Kind = stack["Kind"]
    records: List[SolveRecord] = []

    gate_item, gate_e, gate_U = RUN_CELLS[0]
    gate_screen, gate_q = _run_cell(
        gate_item,
        gate_e,
        gate_U,
        prime=prime,
        screen_timeout=screen_timeout,
        timeout=timeout,
        threads=threads,
        binary=binary,
        accelerators=False,
        stack=stack,
    )
    records.extend((gate_screen, gate_q))
    if gate_q.verdict.kind is not Kind.EMPTY:
        print_verdict_table(records)
        _p0_banner(gate_q)
        return 2

    print()
    print("=" * 88)
    print(
        "PROMOTION-GATE ENGINE AGREEMENT: item-0 (1,3) EMPTY "
        f"certainty={gate_q.verdict.certainty.value.upper()}"
    )
    print(
        "This is independent msolve/qqideal engine agreement with the charged "
        "Sympy-Q [1] result; it is not relabeled PROVEN when qqideal says MODULAR."
    )
    print("=" * 88)
    if gate_only:
        print_verdict_table(records)
        return 0

    char0_nonanswers = False
    for item, e, U in RUN_CELLS[1:]:
        screen, decisive = _run_cell(
            item,
            e,
            U,
            prime=prime,
            screen_timeout=screen_timeout,
            timeout=timeout,
            threads=threads,
            binary=binary,
            accelerators=accelerators,
            stack=stack,
        )
        records.extend((screen, decisive))
        if decisive.verdict.kind is Kind.TIMEOUT or decisive.verdict.kind is Kind.ERROR:
            char0_nonanswers = True

    print_verdict_table(records)
    if char0_nonanswers:
        print(
            "OPEN[A2-E1WALL-CELLS-NONANSWER]: at least one listed Q-form cell "
            "timed out or errored. Completed answers remain recorded; exit status 1."
        )
        return 1
    print(
        "WINDOW ONLY: even all listed EMPTY answers do not close the unbounded "
        "ray; OPEN[A2-U-BOUND] remains."
    )
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-check",
        "--self-check-only",
        dest="self_check_only",
        action="store_true",
        help="run Fraction-only checks and exit before importing solver packages",
    )
    parser.add_argument(
        "--gate-only",
        action="store_true",
        help="run item-0 promotion gate, print its table, and stop",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=float(os.environ.get("A2_CELLS_TIMEOUT", "3600")),
        help="timeout in seconds for the decisive Q-form call of each cell",
    )
    parser.add_argument(
        "--screen-timeout",
        type=float,
        default=None,
        help="timeout for each mod-p screen (default: --timeout)",
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=int(os.environ.get("A2_CELLS_THREADS", "1")),
        help="positive msolve thread count",
    )
    parser.add_argument(
        "--prime",
        type=int,
        default=int(os.environ.get("A2_CELLS_PRIME", str(DEFAULT_PRIME))),
        help="large-prime evidence screen characteristic (default: 65521)",
    )
    parser.add_argument(
        "--binary",
        default=os.environ.get("MSOLVE_BINARY"),
        help="msolve executable; exact version 0.10.1 is required and passed via binary=",
    )
    parser.add_argument(
        "--accelerators",
        action="store_true",
        help="append the five optional residual pins to items 1-4 (default off)",
    )
    args = parser.parse_args(argv)

    print("A2-E1WALL-CELLS preflight: Fraction-only self-checks", flush=True)
    try:
        self_check_ok, transcript = run_self_checks()
    except Exception as exc:  # noqa: BLE001 -- a preflight crash is a non-answer
        traceback.print_exc()
        self_check_ok = False
        transcript = [f"FAIL self-check exception: {type(exc).__name__}: {exc}"]
    print("\n".join(transcript))
    if not self_check_ok:
        print("self-check failure: refusing every solver call", file=sys.stderr)
        if args.self_check_only:
            return 1
        print()
        print("=" * 88)
        print("ORACLE-P0  item-0 could not start: generator self-check non-answer")
        print("ORACLE-P0  refusing every solver call; exit status 2")
        print("=" * 88)
        return 2
    if args.self_check_only:
        return 0

    if args.timeout <= 0:
        parser.error("--timeout must be positive")
    screen_timeout = args.timeout if args.screen_timeout is None else args.screen_timeout
    if screen_timeout <= 0:
        parser.error("--screen-timeout must be positive")
    if args.threads < 1:
        parser.error("--threads must be positive")
    if args.prime <= 3 or args.prime > 2_147_483_647 or not _is_prime(args.prime):
        parser.error(
            "--prime must be an odd prime > 3 and <= 2147483647 "
            "(so the displayed 2-denominators and 3-coefficients survive)"
        )

    try:
        binary = _resolve_binary(args.binary)
        stack = _import_stack()
    except Exception as exc:  # noqa: BLE001 -- gate cannot answer without this stack
        traceback.print_exc()
        print()
        print("=" * 88)
        print("ORACLE-P0  item-0 could not start: solver stack/binary non-answer")
        print(f"ORACLE-P0  {type(exc).__name__}: {exc}")
        print("=" * 88)
        return 2

    print(
        f"solver preflight: qqideal=0.1.0 msolveio=0.1.0 "
        f"msolve={EXPECTED_MSOLVE_VERSION} binary={binary} prime={args.prime} "
        f"Q-timeout={args.timeout}s screen-timeout={screen_timeout}s "
        f"threads={args.threads} accelerators(items1-4)={args.accelerators}",
        flush=True,
    )
    return run_campaign(
        prime=args.prime,
        screen_timeout=screen_timeout,
        timeout=args.timeout,
        threads=args.threads,
        binary=binary,
        accelerators=args.accelerators,
        gate_only=args.gate_only,
        stack=stack,
    )


if __name__ == "__main__":
    raise SystemExit(main())
