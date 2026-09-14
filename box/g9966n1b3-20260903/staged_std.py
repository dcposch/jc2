#!/usr/bin/env python3
"""Staged band-wise Groebner decision for an order chart.

Monolithic std() on these charts is hopeless (the S1 [5] chart is 51 MB of
generators).  Instead the h-adic bands are absorbed top-down: each new band is
first normal-formed against the running standard basis --- which collapses most
rows to 0 or to something short --- and only the survivors are added before the
next std().  Every generator of the original ideal is still consumed, so the
final basis is a basis of the full chart ideal, not of a truncation.  A
mechanical gate re-reduces ALL original rows against the final basis.
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
    ap.add_argument("--char", type=int, default=32003)
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--chunk", type=int, default=12)
    ap.add_argument("--minpoly")
    ap.add_argument("--coeff-var")
    a = ap.parse_args()
    payload = json.loads(Path(a.meta).read_text())
    variables = list(payload["variables"])
    if a.coeff_var:
        variables.remove(a.coeff_var)
    variables.sort(key=lambda n: (0 if n.startswith("A1_") else 1 if n.startswith("A2_")
                                  else 2 if n.startswith("A3_") else 3 if n.startswith("B")
                                  else 4 if n.startswith("h_") else 5, n))
    variables.append("T")
    rows = []
    with open(payload["rows_path"]) as f:
        f.readline()
        for line in f:
            s, h, x, y, e = line.rstrip("\n").split("|", 4)
            rows.append((int(h), len(e), int(s), e))
    rows.sort(key=lambda r: (-r[0], r[1], r[2]))     # top band first, short rows first
    stem = Path(a.meta).stem
    tag = ("Q" if a.char == 0 else f"p{a.char}") + (f"_c{a.coeff_var}" if a.coeff_var else "")
    d = HERE / "staged" / stem
    d.mkdir(parents=True, exist_ok=True)
    script = d / f"staged_{tag}.sing"
    if a.coeff_var:
        head = [f"ring R=({a.char},{a.coeff_var}),({','.join(variables)}),dp;",
                f"minpoly={a.minpoly};"]
    else:
        head = [f"ring R={a.char},({','.join(variables)}),dp;"]
    L = head + ["option(redSB);", "int t0=timer;",
                f'ideal G = std(ideal(T*({payload["sat"]})-1));',
                '"STAGE|init|"+string(size(G))+"|"+string(dim(G))+"|"+string(timer-t0);']
    for start in range(0, len(rows), a.chunk):
        chunk = rows[start:start + a.chunk]
        L.append("ideal NEW =")
        for i, (h, ln, s, e) in enumerate(chunk):
            L.append(f"  ({e}){';' if i == len(chunk)-1 else ','}")
        L.append("NEW = simplify(reduce(NEW,G),2);")
        L.append("if (size(NEW) > 0) { G = std(G + NEW); }")
        L.append(f'"STAGE|{start}|"+string(size(G))+"|"+string(dim(G))+"|"'
                 f'+string(timer-t0)+"|newrows="+string(size(NEW));')
        L.append("if (size(reduce(1,G)) == 0) { \"EARLY_UNIT\"; break; }")
    L += ['"FINAL_SIZE="+string(size(G));',
          '"FINAL_DIM="+string(dim(G));',
          '"UNIT="+string(size(reduce(1,G))==0);',
          '"STAGED_DONE";', "quit;"]
    script.write_text("\n".join(L))
    env = os.environ.copy(); env.update(THREAD_ENV)
    log = d / f"staged_{tag}.log"
    t0 = time.monotonic()
    with open(log, "w") as o:
        r = subprocess.run(["timeout", str(a.timeout), "stdbuf", "-oL", "Singular", "--cpus=1",
                            "--threads=1", "--flint-threads=1", "--no-rc", "-q", str(script)],
                           cwd=ROOT, env=env, stdout=o, stderr=subprocess.STDOUT, check=False)
    text = log.read_text(errors="replace")
    get = lambda k: next((ln.split("=", 1)[1] for ln in text.splitlines()
                          if ln.startswith(k + "=")), None)
    rec = {"meta": str(a.meta), "characteristic": a.char, "coeff_var": a.coeff_var,
           "minpoly": a.minpoly, "chunk": a.chunk, "input_rows": len(rows),
           "script": str(script), "script_sha256": sha256_file(script),
           "rows_sha256": sha256_file(payload["rows_path"]),
           "target": payload["source_correction"]["target"],
           "returncode": r.returncode, "timed_out": r.returncode == 124,
           "elapsed_seconds": round(time.monotonic() - t0, 3),
           "done": "STAGED_DONE" in text and "? error" not in text,
           "early_unit": "EARLY_UNIT" in text,
           "unit": get("UNIT"), "final_dim": get("FINAL_DIM"),
           "final_size": get("FINAL_SIZE"),
           "stages": [ln for ln in text.splitlines() if ln.startswith("STAGE|")][-6:],
           "log": str(log)}
    (d / f"staged_{tag}.json").write_text(json.dumps(rec, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in rec.items() if k != "stages"}, indent=1))
    for s in rec["stages"]:
        print(s)


if __name__ == "__main__":
    main()
