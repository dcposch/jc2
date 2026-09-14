#!/usr/bin/env python3
"""Export an I_light strata prelude to msolve and run it.

Generators are printed by Singular with string() after imap to the parameter
ring.  msolveio.emit_system is the only emitter.  Characteristic-zero msolve
[1] is recorded as a screen until the same unit is seen from guided_gb exact Q;
the converse (msolve non-unit) is a Q non-unit for a good prime-free input.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "k4ray-beta-strata-20260905"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

from strata_chart import extra_generators, strata_prelude  # noqa: E402


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(payload, encoding="utf-8")
    tmp.replace(path)


def dump_generators(K: int, b: int, pin_index: int, ch: int, timeout: int) -> dict:
    prelude, names, weights, meta = strata_prelude(K, b, pin_index=pin_index, ch=ch, theorem_cut=False)
    extras = extra_generators(pin_index)
    dump = HERE / "msolve" / f"K{K}_B{b}_Q{pin_index}_p{ch}.dump.sing"
    outp = dump.with_suffix(".dump")
    lines = [prelude, "int i;"]
    for extra in extras:
        lines.append(f"ROWS = ROWS + ideal({extra});")
    lines.append("ROWS = simplify(ROWS,2);")
    lines.append(f'print("DUMP__N "+string(size(ROWS)));')
    lines.append('print("DUMP__VARS "+string(nvars(basering)));')
    lines.append("for (i=1; i<=size(ROWS); i++) { print(\"DUMP__ROW \"+string(ROWS[i])); }")
    lines.append("quit;")
    atomic_write(dump, "\n".join(lines) + "\n")
    proc = subprocess.run(
        ["stdbuf", "-oL", "-eL", "Singular", "--no-rc", "-q", str(dump)],
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    atomic_write(outp, proc.stdout)
    rows = []
    cstp = None
    extras_out = []
    for line in proc.stdout.splitlines():
        if line.startswith("DUMP__ROW "):
            rows.append(line[len("DUMP__ROW "):].strip())
        elif line.startswith("DUMP__CSTP "):
            cstp = line[len("DUMP__CSTP "):].strip()
        elif line.startswith("DUMP__EXTRA "):
            extras_out.append(line[len("DUMP__EXTRA "):].strip())
    return {
        "names": names,
        "weights": weights,
        "meta": meta,
        "rows": rows,
        "cstp": cstp,
        "extras": extras,
        "returncode": proc.returncode,
        "n": len(rows),
    }


def to_msolve_poly(expr: str) -> str:
    return expr.replace(" ", "")


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("K", type=int)
    p.add_argument("b", type=int)
    p.add_argument("--pin-index", type=int, default=0)
    p.add_argument("--char", type=int, default=0)
    p.add_argument("--dump-timeout", type=int, default=180)
    p.add_argument("--msolve-timeout", type=int, default=600)
    p.add_argument("--run", action="store_true")
    args = p.parse_args()
    t0 = time.time()
    dumped = dump_generators(args.K, args.b, args.pin_index, args.char, args.dump_timeout)
    raw_names = list(dumped["names"])
    alias = {name: f"v{i}" for i, name in enumerate(raw_names)}
    gens = []
    for g in dumped["rows"]:
        if not g or g == "0":
            continue
        expr = g
        for name in sorted(raw_names, key=len, reverse=True):
            expr = expr.replace(name, alias[name])
        gens.append(to_msolve_poly(expr))
    msolve_vars = [alias[name] for name in raw_names]
    import msolveio
    text = msolveio.emit_system(gens, variables=msolve_vars, characteristic=args.char)
    ms_path = HERE / "msolve" / f"K{args.K}_B{args.b}_Q{args.pin_index}_p{args.char}.ms"
    atomic_write(ms_path, text)
    payload = {
        "K": args.K,
        "b": args.b,
        "pin_index": args.pin_index,
        "char": args.char,
        "nvars": len(dumped["names"]),
        "ngens": len(gens),
        "ms_path": str(ms_path),
        "dump_wall": round(time.time() - t0, 3),
        "geom": dumped["meta"]["geometric_parameter_count"],
    }
    if args.run:
        t1 = time.time()
        result = msolveio.run_groebner(text, timeout=float(args.msolve_timeout), threads=4, gb=2)
        payload["msolve_wall"] = round(time.time() - t1, 3)
        payload["msolve"] = {
            "type": type(result).__name__,
            "repr": repr(result)[:2000],
        }
    print(json.dumps(payload, indent=2, default=str))


if __name__ == "__main__":
    main()
