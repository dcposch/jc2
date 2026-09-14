#!/usr/bin/env python3
"""Apply a published phase-1 substitution to the remaining large rows.

No pivoting, no re-mapping of an accumulator: one Singular ``map`` evaluation
per row, appended straight to disk.  Together with the phase-1 residual this is
the image of the FULL chart ideal in the surviving variables.
"""
from __future__ import annotations
import argparse, hashlib, json, os, subprocess, time
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
THREAD_ENV = {"OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1",
              "NUMEXPR_NUM_THREADS": "1", "FLINT_NUM_THREADS": "1"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--reduce-json", required=True)
    ap.add_argument("--char", type=int, default=32003)
    ap.add_argument("--timeout", type=int, default=1200)
    a = ap.parse_args()
    rec = json.loads(Path(a.reduce_json).read_text())
    meta = json.loads(Path(rec["meta"]).read_text())
    subs = [ln.split("|", 2)[1:] for ln in Path(rec["log"]).read_text().splitlines()
            if ln.startswith("SUBST|")]
    variables = list(meta["variables"])
    variables.sort(key=lambda n: (0 if n.startswith("A1_") else 1 if n.startswith("A2_")
                                  else 2 if n.startswith("A3_") else 3 if n.startswith("B")
                                  else 4 if n.startswith("h_") else 5, n))
    variables.append("T")
    img = {v: v for v in variables}
    for v, e in subs:
        img[v] = "(" + e + ")"
    rows = []
    with open(meta["rows_path"]) as f:
        f.readline()
        for line in f:
            s, h, x, y, e = line.rstrip("\n").split("|", 4)
            rows.append((len(e), e))
    rows.sort()
    big = [e for L, e in rows if L > rec["cap_bytes"]]
    base = Path(rec["residual_file"]).parent
    out = base / f"residual_full_{'Q' if a.char == 0 else 'p' + str(a.char)}.txt"
    S = [f"ring R={a.char},({','.join(variables)}),dp;", "option(redSB);", "int t0=timer;",
         "ideal IMG = " + ",".join(img[v] for v in variables) + ";",
         "map PHI = R, IMG;", "poly g;",
         f'link LL=":w {out}"; write(LL, "");']
    for i, e in enumerate(big):
        S.append(f"g = ({e}); g = PHI(g);")
        S.append(f'if (g != 0) {{ write(":a {out}", string(g)); }}')
        S.append(f'"FR|{i}|"+string(timer-t0);')
    S += [f'"BIG_MAPPED={len(big)}";', '"FULLMAP_DONE";', "quit;"]
    script = base / f"full_map_{'Q' if a.char == 0 else 'p' + str(a.char)}.sing"
    script.write_text("\n".join(S))
    env = os.environ.copy(); env.update(THREAD_ENV)
    log = base / f"full_map_{'Q' if a.char == 0 else 'p' + str(a.char)}.log"
    t0 = time.monotonic()
    with open(log, "w") as o:
        r = subprocess.run(["timeout", str(a.timeout), "stdbuf", "-oL", "Singular", "--cpus=1",
                            "--threads=1", "--flint-threads=1", "--no-rc", "-q", str(script)],
                           cwd=ROOT, env=env, stdout=o, stderr=subprocess.STDOUT, check=False)
    text = log.read_text(errors="replace")
    nrows = sum(1 for _ in open(out)) if out.exists() else 0
    prior = sum(1 for ln in open(rec["residual_file"]) if ln.strip())
    res = {"reduce_json": str(a.reduce_json), "characteristic": a.char,
           "big_rows": len(big), "mapped_nonzero": nrows, "phase1_residual_rows": prior,
           "total_reduced_rows": nrows + prior,
           "surviving_variables": rec["surviving_variables"],
           "surviving_variable_count": rec["surviving_variable_count"],
           "residual_full_file": str(out),
           "residual_full_sha256": (hashlib.sha256(out.read_bytes()).hexdigest()
                                    if out.exists() else None),
           "script": str(script), "returncode": r.returncode,
           "timed_out": r.returncode == 124,
           "elapsed_seconds": round(time.monotonic() - t0, 3),
           "done": "FULLMAP_DONE" in text, "errors": text.count("? error"), "log": str(log)}
    (base / f"full_map_{'Q' if a.char == 0 else 'p' + str(a.char)}.json").write_text(
        json.dumps(res, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in res.items() if k != "surviving_variables"}, indent=1))


if __name__ == "__main__":
    main()
