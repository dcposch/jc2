#!/usr/bin/env python3
"""Emit the MASTER-cutoff row labels without recomputing Jacobian rows."""
from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path
import subprocess


HERE = Path(__file__).resolve().parent
STRUCTURE = HERE / "chart_structure_audit.py"
FROZEN_PINNED = Path("/tmp/jc2-lane.qb6I1q/inputs/pinned_chart.py")


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("b", type=int)
    ap.add_argument("pin", type=int)
    ap.add_argument("--timeout", type=int, default=3600)
    args = ap.parse_args()
    assert 9 <= args.b <= 13 and args.pin in (0, 1)

    audit = load("chart_structure", STRUCTURE)
    pinned = load("charged_pinned_for_erows", FROZEN_PINNED)
    full, _names, _weights = audit.independent_prelude(
        pinned, args.b, args.pin, True
    )
    lines = full.splitlines()
    stop = next(i for i, line in enumerate(lines) if line.startswith("ideal I0;"))
    prefix = lines[:stop + 1]
    body = prefix + [
        "poly E64 = 8*B^3 - 48*Rh*h^2 - 72*B*Rh + 9*Al^2;",
        "poly ELAM = E64 - lam*f;",
        'print("DROP__DEG_ELAM "+string(deg(ELAM))+" SIZE_ELAM "+string(size(ELAM)));',
        "matrix CE = coef(ELAM, x*y);",
        "int RAW=0;",
        "for (ii=1; ii<=ncols(CE); ii++)",
        "{",
        "  dde = deg(CE[1,ii]);",
        "  if (dde>13) { if (CE[2,ii] != 0) {",
        '    RAW=RAW+1; print("DROP__ROW "+string(CE[1,ii])+" DEG "+string(dde));',
        "    EROWS=EROWS+ideal(CE[2,ii]);",
        "  } }",
        "}",
        "EROWS=simplify(EROWS,2);",
        'print("PRE__THEOREM_CUTOFF 13");',
        'print("DROP__RAW "+string(RAW));',
        'print("PRE__THEOREM_ROWS "+string(size(EROWS)));',
        'print("DROP__DONE 1");',
        "quit;",
        "",
    ]
    outdir = HERE / "theorem-rows"
    outdir.mkdir(parents=True, exist_ok=True)
    stem = f"K7_B{args.b}_Q{args.pin}_theorem_rows"
    sing = outdir / f"{stem}.sing"
    stdout = outdir / f"{stem}.out"
    stderr = outdir / f"{stem}.err"
    sing.write_text("\n".join(body))
    try:
        proc = subprocess.run(
            ["Singular", "--no-rc", "-q", str(sing)],
            capture_output=True,
            text=True,
            timeout=args.timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        stdout.write_text((exc.stdout or b"").decode() if isinstance(exc.stdout, bytes) else (exc.stdout or ""))
        stderr.write_text((exc.stderr or b"").decode() if isinstance(exc.stderr, bytes) else (exc.stderr or ""))
        raise SystemExit(124)
    stdout.write_text(proc.stdout)
    stderr.write_text(proc.stderr)
    raise SystemExit(proc.returncode)


if __name__ == "__main__":
    main()
