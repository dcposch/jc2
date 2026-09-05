#!/usr/bin/env python3
"""Independent replay gate for a published pivot reduction.

The reducer publishes (a) a substitution map SUBV -> SUBE and (b) a residual
file.  This gate rebuilds the map from the published SUBST lines in a fresh
Singular session, applies it to the ORIGINAL rows the reduction consumed, and
checks two things:

  RESOLVED   every published image is free of every pivoted variable, i.e. the
             map is fully resolved and the elimination is triangular;
  REPLAY     the multiset of nonzero images of the consumed rows equals the
             published residual, so nothing was silently dropped and nothing
             was added.

Passing both means the published residual really is the image of the consumed
part of the chart ideal under a triangular ring automorphism.
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
    ap.add_argument("--timeout", type=int, default=900)
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
    cap = rec["cap_bytes"]
    rows = []
    with open(meta["rows_path"]) as f:
        f.readline()
        for line in f:
            s, h, x, y, e = line.rstrip("\n").split("|", 4)
            rows.append((len(e), e))
    rows.sort()
    used = [e for L, e in rows if not cap or L <= cap]
    sat = f"T*({meta['sat']})-1"
    d = Path(rec["residual_file"]).parent
    out_txt = d / f"replay_{Path(a.reduce_json).stem}.txt"
    S = [f"ring R={rec['characteristic']},({','.join(variables)}),dp;", "option(redSB);",
         "ideal IMG = " + ",".join(img[v] for v in variables) + ";",
         "map PHI = R, IMG;",
         # RESOLVED: no image may still involve a pivoted variable
         "ideal PIVV = " + (",".join(v for v, _ in subs) if subs else "0") + ";",
         "int bad = 0; int i; int j; poly im;",
         "for (i = 1; i <= size(IMG); i++) {",
         "  for (j = 1; j <= size(PIVV); j++) {",
         "    if (diff(IMG[i], PIVV[j]) != 0) { bad = bad + 1; }",
         "  }",
         "}",
         '"RESOLVED="+string(bad==0);',
         "poly g; ideal OUT; int n = 0;"]
    for e in [sat] + used:
        S.append(f"g = {e}; g = PHI(g); if (g != 0) {{ n = n+1; OUT[n] = g; }}")
    S += ['"REPLAY_ROWS="+string(n);',
          f'link LL = ":w {out_txt}"; write(LL, "");',
          f'int z; for (z=1; z<=n; z++) {{ write(":a {out_txt}", string(OUT[z])); }}',
          '"GATE_DONE";', "quit;"]
    script = d / f"replay_{Path(a.reduce_json).stem}.sing"
    script.write_text("\n".join(S))
    env = os.environ.copy(); env.update(THREAD_ENV)
    log = d / f"replay_{Path(a.reduce_json).stem}.log"
    t0 = time.monotonic()
    with open(log, "w") as o:
        r = subprocess.run(["timeout", str(a.timeout), "stdbuf", "-oL", "Singular", "--cpus=1",
                            "--threads=1", "--flint-threads=1", "--no-rc", "-q", str(script)],
                           cwd=ROOT, env=env, stdout=o, stderr=subprocess.STDOUT, check=False)
    text = log.read_text(errors="replace")
    get = lambda k: next((ln.split("=", 1)[1] for ln in text.splitlines()
                          if ln.startswith(k + "=")), None)
    norm = lambda p: sorted(ln.strip().rstrip(";") for ln in Path(p).read_text().splitlines()
                            if ln.strip())
    replay = norm(out_txt) if out_txt.exists() else []
    published = norm(rec["residual_file"])
    res = {"reduce_json": str(a.reduce_json), "characteristic": rec["characteristic"],
           "pivots": len(subs), "rows_consumed": len(used) + 1,
           "resolved": get("RESOLVED"), "replay_rows": get("REPLAY_ROWS"),
           "published_residual_rows": len(published),
           "multisets_equal": replay == published,
           "replay_sha256": hashlib.sha256("\n".join(replay).encode()).hexdigest(),
           "published_sha256": hashlib.sha256("\n".join(published).encode()).hexdigest(),
           "elapsed_seconds": round(time.monotonic() - t0, 3),
           "done": "GATE_DONE" in text, "errors": text.count("? error"),
           "script": str(script), "log": str(log)}
    res["status"] = "PASS" if (res["resolved"] == "1" and res["multisets_equal"]
                               and res["done"] and res["errors"] == 0) else "FAIL"
    (d / f"replay_{Path(a.reduce_json).stem}.json").write_text(
        json.dumps(res, indent=2, sort_keys=True) + "\n")
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
