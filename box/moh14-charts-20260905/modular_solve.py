#!/usr/bin/env python3
"""modular_solve.py -- fast verdicts for the s'=3 class charts.

The exact-Q `std` emitted by sprime3_compiler.emit_guided did not finish in
53+ min on the 176-/514-equation stems, so this driver replaces it with

  Stage A (signal, char p):  prefix-doubling std over F_p.  The generators are
      sorted by printed length; we std the smallest k of them together with the
      saturation generator T*c-1 for k = 4, 8, 16, ... and stop at the first
      prefix whose std contains 1.  A unit at a small prefix is both the
      verdict signal and a *certificate subset*.

  Stage B (promotion, char 0):  re-run std over Q on exactly that subset.
      1 in std(S) over Q with S a subset of the chart ideal is a complete
      char-0 proof that the chart is empty -- no modular promotion policy is
      needed (FALLACY-v2: a modular unit is never promoted on its own).

If no prefix is a unit the driver reports the dimension of the full modular
std, which is a *candidate* survive and must then be checked exactly.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def load(stem: str, class_id: str) -> tuple[list[str], list[str]]:
    meta = json.loads((HERE / "classes" / class_id / "meta" / (stem + ".json")).read_text())
    rows_path = HERE / "classes" / class_id / "rows" / (stem + "_rows.tsv")
    gens = []
    with rows_path.open() as fh:
        head = fh.readline()
        assert head.startswith("source_index|"), head
        for line in fh:
            line = line.rstrip("\n")
            if not line:
                continue
            expr = line.split("|", 4)[4].strip()
            if expr and expr not in ("0", "(0)"):
                gens.append(expr)
    gens.sort(key=len)
    return meta["variables"] + ["T"], gens


def emit(stem: str, variables: list[str], gens: list[str], char: int,
         prefixes: list[int], out: Path, degbound: int = 0) -> Path:
    # A degree-bounded std returns a PARTIAL basis whose elements still lie in
    # the ideal, so `reduce(1,G)==0` remains a complete certificate for 1 in I.
    # It is not a certificate for NONUNIT, which is why a degree-bounded run
    # never reports a dimension.
    L = ["ring R=%d,(%s),dp;" % (char, ",".join(variables)),
         "option(noredSB);",
         'if (nameof(basering)=="R") { print("CONTROL_RING_PASS"); } else { print("CONTROL_RING_FAIL"); }',
         "ideal CE=c,T*c-1; if (reduce(1,std(CE))==0) { print(\"CONTROL_EMPTY_PASS\"); } else { print(\"CONTROL_EMPTY_FAIL\"); }",
         "ideal CN=c-1,T*c-1; if (reduce(1,std(CN))!=0) { print(\"CONTROL_NONEMPTY_PASS\"); } else { print(\"CONTROL_NONEMPTY_FAIL\"); }",
         'print("MS_START stem=%s char=%d equations=%d unknowns=%d");' % (
             stem, char, len(gens), len(variables) - 1),
         "ideal ALL;"]
    if degbound:
        L.insert(1, "degBound=%d;" % degbound)
    for i, g in enumerate(gens, start=1):
        L.append("ALL[%d]=%s;" % (i, g))
    L.append("ideal S; S[1]=T*c-1;")
    L.append("int i; int t; ideal G; int u; int done=0;")
    steps = sorted({min(k, len(gens)) for k in prefixes} | {len(gens)})
    for k in steps:
        L += [
            "if (done==0) {",
            "  for (i=size(S); i<=%d; i++) { S[i+1]=ALL[i]; }" % k,
            "  t=timer;",
            "  G=std(S);",
            '  print("MS_PREFIX %d seconds="+string(timer-t)+" basis="+string(size(G)));' % k,
            "  if (reduce(1,G)==0) {",
            '    print("MS_UNIT_AT %d"); print("MS_VERDICT UNIT"); done=1;' % k,
            "  }",
            "}",
        ]
    L += [
        ('if (done==0) { print("MS_VERDICT DEGBOUND_NO_UNIT"); }' if degbound
         else 'if (done==0) { print("MS_DIM "+string(dim(G))); print("MS_VERDICT NONUNIT"); }'),
        "quit;",
    ]
    out.write_text("\n".join(L) + "\n")
    return out


def emit_subset(stem: str, variables: list[str], gens: list[str], char: int,
                k: int, out: Path) -> Path:
    L = ["ring R=%d,(%s),dp;" % (char, ",".join(variables)),
         "option(noredSB);",
         'print("MS_START stem=%s char=%d subset=%d unknowns=%d");' % (
             stem, char, k, len(variables) - 1),
         "ideal S=T*c-1;"]
    for i, g in enumerate(gens[:k], start=1):
        L.append("S[%d]=%s;" % (i + 1, g))
    L += ["int t=timer;", "ideal G=std(S);",
          'print("MS_SUBSET seconds="+string(timer-t)+" basis="+string(size(G)));',
          'if (reduce(1,G)==0) { print("MS_VERDICT UNIT"); }'
          ' else { print("MS_DIM "+string(dim(G))); print("MS_VERDICT NONUNIT"); }',
          "quit;"]
    out.write_text("\n".join(L) + "\n")
    return out


def parse(stdout: str) -> dict:
    d: dict = {"controls": {}, "prefixes": []}
    for line in stdout.splitlines():
        line = line.strip()
        if line.startswith("CONTROL_"):
            d["controls"][line] = True
        m = re.match(r"MS_PREFIX (\d+) seconds=(\d+) basis=(\d+)", line)
        if m:
            d["prefixes"].append({"k": int(m.group(1)), "seconds": int(m.group(2)),
                                  "basis": int(m.group(3))})
        m = re.match(r"MS_FULL seconds=(\d+) basis=(\d+)", line)
        if m:
            d["full"] = {"seconds": int(m.group(1)), "basis": int(m.group(2))}
        m = re.match(r"MS_UNIT_AT (\S+)", line)
        if m:
            d["unit_at"] = m.group(1)
        m = re.match(r"MS_SUBSET seconds=(\d+) basis=(\d+)", line)
        if m:
            d["subset"] = {"seconds": int(m.group(1)), "basis": int(m.group(2))}
        m = re.match(r"MS_DIM (-?\d+)", line)
        if m:
            d["dim"] = int(m.group(1))
        m = re.match(r"MS_VERDICT (\S+)", line)
        if m:
            d["verdict"] = m.group(1)
    return d


def run(script: Path, timeout: int) -> tuple[str, str, bool]:
    t0 = time.time()
    log = script.with_suffix(".live")
    to = False
    with log.open("w") as fh:
        proc = subprocess.Popen(["Singular", "--cpus=1", "-q", "--no-rc", str(script)],
                                stdout=fh, stderr=subprocess.STDOUT,
                                cwd=str(script.parent))
        try:
            proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            proc.kill(); proc.wait(); to = True
    return log.read_text(), ("TIMEOUT after %.0fs" % (time.time() - t0)) if to else "", to


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--class-id", required=True)
    ap.add_argument("--stem", required=True)
    ap.add_argument("--char", type=int, default=32003)
    ap.add_argument("--timeout", type=int, default=3600)
    ap.add_argument("--prefixes", default="4,8,16,32,64,128,256")
    ap.add_argument("--subset", type=int, default=0,
                    help="if >0, only std the smallest N generators (+ saturation)")
    ap.add_argument("--degbound", type=int, default=0)
    ap.add_argument("--tag", default="")
    a = ap.parse_args()
    variables, gens = load(a.stem, a.class_id)
    jobs = HERE / "classes" / a.class_id / "jobs"
    jobs.mkdir(parents=True, exist_ok=True)
    tag = a.tag or ("p%d" % a.char if a.char else "Q")
    script = jobs / ("%s_ms_%s.sing" % (a.stem, tag))
    if a.subset:
        emit_subset(a.stem, variables, gens, a.char, a.subset, script)
    else:
        emit(a.stem, variables, gens, a.char,
             [int(x) for x in a.prefixes.split(",")], script, a.degbound)
    out, err, to = run(script, a.timeout)
    res = parse(out)
    res.update({"degbound": a.degbound, "stem": a.stem, "class_id": a.class_id, "char": a.char,
                "equations": len(gens), "unknowns": len(variables) - 1,
                "timed_out": to, "script": str(script.relative_to(ROOT)),
                "stderr_tail": err[-400:]})
    log = jobs / ("%s_ms_%s.out" % (a.stem, tag))
    log.write_text(out)
    print(json.dumps(res, indent=2))
    (jobs / ("%s_ms_%s.json" % (a.stem, tag))).write_text(json.dumps(res, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
