#!/usr/bin/env python3
"""Find a small coordinate seed from a fast legacy modular UNIT system.

The result is only a scheduling heuristic.  Promotion must use the same
coordinates in the NEW source-complete rows, together with every exact scalar
pivot used by ``triangular_preprocess.py``.  Since that construction drops
rows but never unknowns, a UNIT result there is safe.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import time

import triangular_preprocess as tp


ROOT = Path(__file__).resolve().parents[3]


def run_test(
    label: str,
    payload: dict,
    rows: list[tp.Row],
    indices: tuple[int, ...],
    characteristic: int,
    branch: str,
    timeout: int,
    directory: Path,
) -> dict:
    key_text = ",".join(map(str, indices))
    key = hashlib.sha256(key_text.encode()).hexdigest()[:16]
    stem = f"{label}_{len(indices):03d}_{key}"
    script = directory / f"{stem}.sing"
    stdout = directory / f"{stem}.out"
    stderr = directory / f"{stem}.err"
    variables = tp.coefficient_first(payload["variables"]) + ["T"]
    generators = [rows[index].expr for index in indices]
    if branch == "q2":
        generators.append("s2^2-s2+1")
    elif branch != "none":
        raise ValueError(branch)
    generators.append(f"T*({payload['sat']})-1")
    text = "\n".join(
        [
            f"ring R={characteristic},({','.join(variables)}),dp;",
            "option(redSB);",
            "ideal I=" + ",\n".join(generators) + ";",
            "timer=1; int T0=timer; ideal G=std(I); int DT=timer-T0;",
            '"CORE_STD_DONE ms="+string(DT)+" size="+string(size(G))+" dim="+string(dim(G));',
            "poly one=reduce(1,G);",
            'if(one==0){"CORE_UNIT 1";}else{"CORE_UNIT 0";}',
            '"SCRIPT_DONE";',
            "",
        ]
    )
    script.write_text(text, encoding="utf-8")
    started = time.monotonic()
    with stdout.open("wb") as out, stderr.open("wb") as err:
        completed = subprocess.run(
            ["timeout", str(timeout), "Singular", "--no-rc", "-q", str(script)],
            cwd=ROOT,
            stdout=out,
            stderr=err,
            check=False,
        )
    elapsed = time.monotonic() - started
    output = stdout.read_text(encoding="utf-8", errors="replace")
    unit = completed.returncode == 0 and "CORE_UNIT 1" in output and "SCRIPT_DONE" in output
    return {
        "indices": list(indices),
        "count": len(indices),
        "unit": unit,
        "returncode": completed.returncode,
        "elapsed_seconds": elapsed,
        "script": str(script.relative_to(ROOT)),
        "stdout": str(stdout.relative_to(ROOT)),
        "stderr": str(stderr.relative_to(ROOT)),
    }


def chunks(values: tuple[int, ...], count: int) -> list[tuple[int, ...]]:
    count = min(count, len(values))
    base, extra = divmod(len(values), count)
    result = []
    start = 0
    for index in range(count):
        width = base + (1 if index < extra else 0)
        result.append(values[start : start + width])
        start += width
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--meta", type=Path, required=True)
    parser.add_argument("--char", type=int, default=32003)
    parser.add_argument("--branch", choices=("none", "q2"), default="none")
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--label", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    meta_path = args.meta.resolve()
    payload = json.loads(meta_path.read_text(encoding="utf-8"))
    rows_path = ROOT / payload["rows_path"]
    rows = tp.read_rows(rows_path)
    directory = args.output.resolve().parent / (args.label + "-tests")
    directory.mkdir(parents=True, exist_ok=True)
    cache: dict[tuple[int, ...], dict] = {}

    def test(indices: tuple[int, ...]) -> bool:
        indices = tuple(sorted(indices))
        if indices not in cache:
            record = run_test(
                args.label,
                payload,
                rows,
                indices,
                args.char,
                args.branch,
                args.timeout,
                directory,
            )
            cache[indices] = record
            print(
                f"test={len(cache)} rows={len(indices)} unit={record['unit']} "
                f"rc={record['returncode']} wall={record['elapsed_seconds']:.3f}",
                flush=True,
            )
        return cache[indices]["unit"]

    current = tuple(range(len(rows)))
    if not test(current):
        raise RuntimeError("full legacy system was not a clean modular UNIT")
    granularity = 2
    while len(current) >= 2:
        reduced = False
        for chunk in chunks(current, granularity):
            removed = set(chunk)
            complement = tuple(index for index in current if index not in removed)
            if complement and test(complement):
                current = complement
                granularity = max(2, granularity - 1)
                reduced = True
                break
        if not reduced:
            if granularity >= len(current):
                break
            granularity = min(len(current), granularity * 2)

    # One final linear deletion pass makes the result inclusion-minimal relative
    # to the completed tests, while the timeout prevents this heuristic from
    # consuming the main campaign budget.
    changed = True
    while changed:
        changed = False
        for index in current:
            trial = tuple(value for value in current if value != index)
            if trial and test(trial):
                current = trial
                changed = True
                break

    coordinates = [
        {
            "source_index": index,
            "h_power": rows[index].h_power,
            "x_power": rows[index].x_power,
            "y_power": rows[index].y_power,
        }
        for index in current
    ]
    result = {
        "schema": "jc2.s56-recert.legacy-coordinate-core/v1",
        "warning": "heuristic coordinates only; never drop source-complete unknowns",
        "meta": str(meta_path.relative_to(ROOT)),
        "rows": str(rows_path.relative_to(ROOT)),
        "rows_sha256": tp.sha256(rows_path),
        "characteristic": args.char,
        "branch": args.branch,
        "full_row_count": len(rows),
        "core_row_count": len(current),
        "core_indices": list(current),
        "core_coordinates": coordinates,
        "test_count": len(cache),
        "tests": list(cache.values()),
    }
    output = args.output.resolve()
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in ("core_row_count", "core_indices", "test_count")}, indent=2))


if __name__ == "__main__":
    main()
