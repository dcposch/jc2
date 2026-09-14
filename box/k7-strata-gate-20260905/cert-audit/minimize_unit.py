#!/usr/bin/env python3
"""Find a smaller exact-Q unit subset of an msolve generator list.

Uses deterministic delta debugging with an exact-Q msolve unit test.  The last
two chart generators are kept until the final one-at-a-time pass because they
are CSTP-1 and the Rabinowitsch localizer.  Original 1-based generator indices
are retained in the JSON receipt and in the subset filename companion.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time


def parse_ms(path: Path) -> tuple[str, str, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    header = lines[0]
    characteristic = lines[1]
    body = "\n".join(lines[2:]).strip()
    if body.endswith(","):
        body = body[:-1]
    return header, characteristic, [x.strip() for x in body.split(",\n") if x.strip()]


def emit(header: str, characteristic: str, generators: list[str]) -> str:
    return f"{header}\n{characteristic}\n" + ",\n".join(generators) + "\n"


def is_unit(msolve: str, libdir: str | None, text: str, work: Path, label: str,
            timeout: int, threads: int) -> tuple[bool, float, int | None]:
    inp = work / f"{label}.ms"
    out = work / f"{label}.out"
    inp.write_text(text, encoding="utf-8")
    env = os.environ.copy()
    if libdir:
        env["LD_LIBRARY_PATH"] = libdir
    t0 = time.time()
    try:
        p = subprocess.run(
            [msolve, "-g", "2", "-t", str(threads), "-f", str(inp), "-o", str(out)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
            env=env,
        )
        rc = p.returncode
    except subprocess.TimeoutExpired:
        return False, time.time() - t0, None
    payload = out.read_text(encoding="utf-8") if out.exists() else ""
    flat = re.sub(r"\s+", "", "".join(x for x in payload.splitlines() if not x.startswith("#"))).rstrip(":")
    return flat == "[1]", time.time() - t0, rc


def chunks(seq: list[int], n: int) -> list[list[int]]:
    return [seq[i * len(seq) // n:(i + 1) * len(seq) // n] for i in range(n)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--msolve", required=True)
    ap.add_argument("--libdir")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--threads", type=int, default=4)
    ap.add_argument("--max-calls", type=int, default=80)
    ap.add_argument("--stop-size", type=int, default=0)
    ap.add_argument("--trial-char", default="0",
                    help="field characteristic for shrink trials; final check is always Q")
    ap.add_argument("--initial-granularity", type=int, default=2)
    args = ap.parse_args()

    header, characteristic, generators = parse_ms(args.source)
    if characteristic.strip() != "0":
        raise SystemExit("only exact-Q inputs are accepted")
    current = list(range(len(generators)))
    successful: list[list[int]] = [current.copy()]
    calls: list[dict[str, object]] = []
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="min-unit-", dir=args.output.parent) as td:
        work = Path(td)

        def check(indices: list[int]) -> bool:
            call = len(calls) + 1
            text = emit(header, args.trial_char, [generators[i] for i in indices])
            unit, wall, rc = is_unit(args.msolve, args.libdir, text, work,
                                     f"trial-{call:04d}",
                                     args.timeout, args.threads)
            calls.append({"phase": "shrink", "call": call,
                          "characteristic": args.trial_char,
                          "size": len(indices), "unit": unit,
                          "wall": round(wall, 3), "returncode": rc})
            print(json.dumps(calls[-1], sort_keys=True), flush=True)
            return unit

        if not check(current):
            raise SystemExit("full source was not certified unit")

        # Preserve the final two extras while coarse-shrinking the coefficient rows.
        fixed = current[-2:]
        active = current[:-2]
        granularity = max(2, min(args.initial_granularity, len(active)))
        while len(calls) < args.max_calls and len(active) >= 2:
            parts = chunks(active, min(granularity, len(active)))
            reduced = False
            for part in parts:
                if len(calls) >= args.max_calls:
                    break
                drop = set(part)
                candidate_active = [i for i in active if i not in drop]
                if check(candidate_active + fixed):
                    active = candidate_active
                    successful.append((active + fixed).copy())
                    granularity = max(2, granularity - 1)
                    reduced = True
                    break
            if args.stop_size and len(active) + len(fixed) <= args.stop_size:
                break
            if not reduced:
                if granularity >= len(active):
                    break
                granularity = min(len(active), granularity * 2)

        current = active + fixed
        # A bounded deterministic one-at-a-time cleanup.
        for idx in list(current):
            if len(calls) >= args.max_calls:
                break
            candidate = [i for i in current if i != idx]
            if check(candidate):
                current = candidate
                successful.append(current.copy())

        # A modular unit was used only as a shrink heuristic.  Verify candidate
        # subsets over Q, smallest first, falling back through known supersets.
        exact_current: list[int] | None = None
        for attempt, candidate in enumerate(reversed(successful), 1):
            text = emit(header, characteristic, [generators[i] for i in candidate])
            unit, wall, rc = is_unit(args.msolve, args.libdir, text, work,
                                     f"exact-{attempt:04d}",
                                     args.timeout, args.threads)
            item = {"phase": "exact-final", "attempt": attempt,
                    "characteristic": "0", "size": len(candidate),
                    "unit": unit, "wall": round(wall, 3), "returncode": rc}
            calls.append(item)
            print(json.dumps(item, sort_keys=True), flush=True)
            if unit:
                exact_current = candidate
                break
        if exact_current is None:
            raise SystemExit("no exact-Q unit subset survived final verification")
        current = exact_current

    subset_text = emit(header, characteristic, [generators[i] for i in current])
    args.output.write_text(subset_text, encoding="utf-8")
    receipt = {
        "source": str(args.source.resolve()),
        "source_sha256": hashlib.sha256(args.source.read_bytes()).hexdigest(),
        "source_generator_count": len(generators),
        "subset_generator_count": len(current),
        "original_indices_1based": [i + 1 for i in current],
        "subset_sha256": hashlib.sha256(subset_text.encode()).hexdigest(),
        "msolve": str(Path(args.msolve).resolve()),
        "msolve_sha256": hashlib.sha256(Path(args.msolve).read_bytes()).hexdigest(),
        "calls": calls,
    }
    args.output.with_suffix(args.output.suffix + ".json").write_text(
        json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
