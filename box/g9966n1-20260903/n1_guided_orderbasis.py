#!/usr/bin/env python3
"""Guided-GB replay for selected N1 order-basis row files."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
HERE = ROOT / "box" / "g9966n1-20260903"
sys.path.insert(0, str(ROOT))

from box.lib.guided_gb import PromotionPolicy, RunConfig, SingularSystem, guided_groebner  # noqa: E402


def read_rows(path: Path) -> list[str]:
    rows: list[str] = []
    with path.open(encoding="utf-8") as handle:
        next(handle)
        for line in handle:
            line = line.rstrip("\n")
            if line:
                rows.append(line.split("|", 4)[4])
    return rows


def run(meta_path: Path, chars: list[int], timeout: int, output: Path) -> dict:
    meta_payload = json.loads(meta_path.read_text(encoding="utf-8"))
    variables = tuple(meta_payload["variables"] + ["T"])
    sat = meta_payload["sat"]
    row_file = ROOT / meta_payload["rows_path"]
    generators = tuple(read_rows(row_file) + [f"T*({sat})-1"])
    runs = []
    for char in chars:
        system = SingularSystem(
            name=f"{Path(meta_payload['rows_path']).stem.replace('_rows', '')}_{'Q' if char == 0 else 'p' + str(char)}",
            prelude=f"ring R={char},({','.join(variables)}),dp;\noption(redSB);\n",
            generators=generators,
            characteristic=char,
            variables=variables,
            metadata={
                "meta": str(meta_path.relative_to(ROOT)),
                "rows_path": meta_payload["rows_path"],
                "row_count": len(generators) - 1,
                "localizer": generators[-1],
            },
        )
        result = guided_groebner(
            system,
            policy=PromotionPolicy.exact_q("N1 order-basis exact guided replay"),
            config=RunConfig(
                output_dir=output / ("Q" if char == 0 else f"p{char}"),
                timeout_seconds=timeout,
                total_cores=1,
                max_parallel_jobs=1,
                run_perturbed_control=False,
            ),
        )
        runs.append(result.to_json())
    payload = {
        "meta": str(meta_path.relative_to(ROOT)),
        "chars": chars,
        "timeout_seconds": timeout,
        "row_count_without_localizer": len(generators) - 1,
        "runs": runs,
    }
    out_path = output / "guided-summary.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    payload["summary_path"] = str(out_path.relative_to(ROOT))
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--meta", required=True)
    parser.add_argument("--chars", default="32003,32009,32027,0")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--output", default="box/g9966n1-20260903/guided")
    args = parser.parse_args()
    chars = [int(piece) for piece in args.chars.split(",") if piece]
    result = run(ROOT / args.meta, chars, args.timeout, ROOT / args.output)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
