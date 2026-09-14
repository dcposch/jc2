#!/usr/bin/env python3
"""Sub-ideal unit probe.

A sub-ideal of the chart ideal that is already the unit ideal kills the chart
outright: (J subset I and J=(1)) implies I=(1).  The top h-adic bands are tiny
compared with the h=0/h=1 bands, so this is the cheapest possible decision.
It is one-sided: a nonunit sub-ideal decides nothing.
"""
from __future__ import annotations
import argparse, hashlib, json, os, subprocess, time
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "g9966n1b3-20260903"
THREAD_ENV = {"OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
              "NUMEXPR_NUM_THREADS": "1", "FLINT_NUM_THREADS": "1"}


def sha256_file(p):
    d = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            d.update(b)
    return d.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True)
    ap.add_argument("--min-h", type=int, default=3)
    ap.add_argument("--char", type=int, default=32003)
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--max-bytes", type=int, default=0)
    a = ap.parse_args()
    payload = json.loads(Path(a.meta).read_text())
    variables = list(payload["variables"])
    variables.sort(key=lambda n: (0 if n.startswith("A1_") else 1 if n.startswith("A2_")
                                  else 2 if n.startswith("A3_") else 3 if n.startswith("B")
                                  else 4 if n.startswith("h_") else 5, n))
    variables.append("T")
    rows = []
    with open(payload["rows_path"]) as f:
        f.readline()
        for line in f:
            s, h, x, y, e = line.rstrip("\n").split("|", 4)
            if int(h) >= a.min_h and (a.max_bytes == 0 or len(e) <= a.max_bytes):
                rows.append(e)
    stem = Path(a.meta).stem
    tag = f"h{a.min_h}_b{a.max_bytes}_" + ("Q" if a.char == 0 else f"p{a.char}")
    d = HERE / "subideal" / stem
    d.mkdir(parents=True, exist_ok=True)
    script = d / f"probe_{tag}.sing"
    lines = [f"ring R={a.char},({','.join(variables)}),dp;", "option(redSB);", "ideal I ="]
    gens = rows + [f"T*({payload['sat']})-1"]
    for i, g in enumerate(gens):
        lines.append(f"  ({g}){';' if i == len(gens)-1 else ','}")
    lines += ['"GENS="+string(size(I));', "ideal G = std(I);",
              '"SIZE="+string(size(G));', '"UNIT="+string(size(reduce(1,G))==0);',
              '"DIM="+string(dim(G));',
              '"NF_ALL_ZERO="+string(size(reduce(I,G))==0);',
              '"PROBE_DONE";', "quit;"]
    script.write_text("\n".join(lines))
    env = os.environ.copy(); env.update(THREAD_ENV)
    log = d / f"probe_{tag}.log"
    t0 = time.monotonic()
    with open(log, "w") as o:
        r = subprocess.run(["timeout", str(a.timeout), "stdbuf", "-oL", "Singular", "--cpus=1",
                            "--threads=1", "--flint-threads=1", "--no-rc", "-q", str(script)],
                           cwd=ROOT, env=env, stdout=o, stderr=subprocess.STDOUT, check=False)
    text = log.read_text(errors="replace")
    get = lambda k: next((ln.split("=", 1)[1] for ln in text.splitlines()
                          if ln.startswith(k + "=")), None)
    rec = {"meta": str(a.meta), "min_h": a.min_h, "max_bytes": a.max_bytes,
           "characteristic": a.char, "generators": len(gens),
           "script": str(script), "script_sha256": sha256_file(script),
           "rows_sha256": sha256_file(payload["rows_path"]),
           "returncode": r.returncode, "timed_out": r.returncode == 124,
           "elapsed_seconds": round(time.monotonic() - t0, 3),
           "done": "PROBE_DONE" in text and "? error" not in text,
           "unit": get("UNIT"), "dim": get("DIM"), "basis_size": get("SIZE"),
           "nf_all_zero": get("NF_ALL_ZERO"), "log": str(log)}
    (d / f"probe_{tag}.json").write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
    print(json.dumps(rec, indent=1))


if __name__ == "__main__":
    main()
