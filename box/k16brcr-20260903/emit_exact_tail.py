#!/usr/bin/env python3
"""Emit bounded exact coefficient-extraction jobs from the frozen K16 driver.

This is deliberately not a Groebner-basis driver.  It reuses ``emit`` from the
SHA-256-verified frozen input, then appends coefficient extractions before the
terminal ``quit``.  Generated sources and transcripts live beside this file.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
FROZEN = Path("/tmp/jc2-lane.5ksWeb/inputs/singular_terminal_driver.py")


def load_frozen():
    spec = importlib.util.spec_from_file_location("frozen_terminal", FROZEN)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {FROZEN}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def extraction_block(t: int) -> str:
    low_q = [f"q{j}_0" for j in range(2, t)]
    lines = [f'print("BRCR_BEGIN t={t}");']
    for r in range(t):
        k = 2 * t - 1 - r
        lines += [
            f"poly aa{r}=subst(diff(diff(T{k},b3),b3),b3,0)/2;",
            f"poly bb{r}=subst(diff(T{k},b3),b3,0);",
            f"poly cc{r}=subst(T{k},b3,0);",
            f'print("BRCR_ROW r={r} k={k}"); T{k};',
            f'print("BRCR_A r={r} size="+string(size(aa{r}))); aa{r};',
            f'print("BRCR_b r={r} size="+string(size(bb{r}))); bb{r};',
            f'print("BRCR_c r={r} size="+string(size(cc{r}))); cc{r};',
            f"if (T{k}-aa{r}*b3^2-bb{r}*b3-cc{r}!=0) "
            f'{{ print("FAIL BRCR split r={r}"); exit(2); }}',
        ]
    for r in range(1, t):
        lines += [
            f"poly BB{r}=aa0*bb{r}-aa{r}*bb0;",
            f"poly CC{r}=aa0*cc{r}-aa{r}*cc0;",
            f"poly GG{r}=BB{r}*b3+CC{r};",
            f"poly WW{r}=aa0*CC{r}^2-bb0*BB{r}*CC{r}+cc0*BB{r}^2;",
            f"if (GG{r}-(aa0*T{2*t-1-r}-aa{r}*T{2*t-1})!=0) "
            f'{{ print("FAIL BRCR G r={r}"); exit(2); }}',
            f'print("BRCR_B r={r} size="+string(size(BB{r}))); BB{r};',
            f'print("BRCR_C r={r} size="+string(size(CC{r}))); CC{r};',
            f'print("BRCR_W r={r} size="+string(size(WW{r}))); WW{r};',
        ]
        for name in (f"BB{r}", f"CC{r}"):
            axis = name
            for variable in low_q:
                axis = f"subst({axis},{variable},0)"
            lines += [f'print("BRCR_B4AXIS name={name}"); {axis};']
    lines += ['print("BRCR_DONE");']
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("t", type=int)
    parser.add_argument("--split-branch", type=int, choices=(0, 1))
    args = parser.parse_args()
    mode = "split-exact" if args.split_branch is not None else "exact"
    frozen = load_frozen()
    source, metadata = frozen.emit(
        args.t, mode, None, args.split_branch, "none", "std", None, False, None
    )
    needle = 'print("DRIVER_DONE");\nquit;\n'
    if source.count(needle) != 1:
        raise RuntimeError("unexpected frozen-driver terminator")
    source = source.replace(
        needle, extraction_block(args.t) + 'print("DRIVER_DONE");\nquit;\n'
    )
    suffix = f"split_b{args.split_branch}" if args.split_branch is not None else "exact"
    stem = f"brcr_t{args.t}_{suffix}"
    source_path = HERE / f"{stem}.sing"
    metadata_path = HERE / f"{stem}.json"
    source_path.write_text(source, encoding="utf-8")
    metadata.update(
        purpose="coefficient extraction only; no std/Groebner call",
        algorithm="triangular coefficient recurrence",
        groebner_call=False,
        frozen_emit_algorithm_argument="std (unused by exact/split-exact mode)",
        frozen_driver=str(FROZEN),
        source=str(source_path),
    )
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(source_path)


if __name__ == "__main__":
    main()
