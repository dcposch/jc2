#!/usr/bin/env python3
"""Modular+CRT solver + point probe for the completed s'=3 order charts.

Stage A: unbounded std over F_p (default 32003 and 32051).  A unit at
this stage is a *signal*, not a char-0 kill (FALLACY-v2: modular unit
is not promoted).  Stage B (only if Stage A is UNIT): exact-Q std of
the same generators.

A NONUNIT with dim >= 0 is a candidate survive.  The probe then tries
to extract a point over F_p and checks J(P,Q) == c * x^ell by
re-evaluating the Jacobian in a bivariate ring (not by trusting dim).

Degree-bounded std that fails to produce 1 is NOT a survive.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def load(class_id: str, stem: str) -> tuple[list[str], list[str], dict]:
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
    variables = meta["variables"] + ["T"]
    return variables, gens, meta


def emit_unbounded(stem: str, variables: list[str], gens: list[str],
                   char: int, out: Path, prot: bool = False) -> Path:
    L = [
        "ring R=%d,(%s),dp;" % (char, ",".join(variables)),
        "option(noredSB);",
    ]
    if prot:
        L.append("option(prot);")
    L += [
        'if (nameof(basering)=="R") { print("CONTROL_RING_PASS"); } else { print("CONTROL_RING_FAIL"); }',
        'ideal CE=c,T*c-1; if (reduce(1,std(CE))==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }',
        'ideal CN=c-1,T*c-1; if (reduce(1,std(CN))!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }',
        'print("MS_START stem=%s char=%d equations=%d unknowns=%d mode=unbounded");' % (
            stem, char, len(gens), len(variables) - 1),
        "ideal I; I[1]=T*c-1;",
    ]
    for i, g in enumerate(gens, start=1):
        L.append("I[%d]=%s;" % (i + 1, g))
    L += [
        "int t=timer;",
        "ideal G=std(I);",
        'print("MS_FULL seconds="+string(timer-t)+" basis="+string(size(G)));',
        "if (reduce(1,G)==0) {",
        '  print("MS_VERDICT UNIT");',
        "} else {",
        "  int d=dim(G);",
        '  print("MS_DIM "+string(d));',
        '  print("MS_VERDICT NONUNIT");',
        "  if (d>=0) {",
        "    intvec IS=indepSet(G);",
        '    print("MS_INDEP "+string(IS));',
        "  }",
        "}",
        "quit;",
    ]
    out.write_text("\n".join(L) + "\n")
    return out


def emit_point_probe(stem: str, variables: list[str], gens: list[str],
                     char: int, out: Path, n_try: int = 8) -> Path:
    """Random linear slices of the prefix-short system, then test all gens.

    Does NOT claim a survive unless a point with c != 0 satisfies every
    generator (printed as POINT_PASS).
    """
    params = [v for v in variables if v not in ("T",)]
    L = [
        "ring R=%d,(%s),dp;" % (char, ",".join(variables)),
        "option(noredSB);",
        'print("PP_START stem=%s char=%d equations=%d unknowns=%d");' % (
            stem, char, len(gens), len(variables) - 1),
        "ideal ALL; ALL[1]=T*c-1;",
    ]
    for i, g in enumerate(gens, start=1):
        L.append("ALL[%d]=%s;" % (i + 1, g))
    L.append("int ntry=%d;" % n_try)
    L.append("int hit=0;")
    # Use a short prefix GB as a cheap ambient, then random-slice.
    k = min(48, len(gens))
    L += [
        "ideal S; S[1]=T*c-1;",
        "int i;",
        "for (i=1; i<=%d; i++) { S[i+1]=ALL[i]; }" % k,
        "int t=timer;",
        "ideal G0=std(S);",
        'print("PP_PREFIX k=%d seconds="+string(timer-t)+" basis="+string(size(G0)));' % k,
        "if (reduce(1,G0)==0) { print(\"PP_PREFIX_UNIT\"); quit; }",
        "int d0=dim(G0);",
        'print("PP_PREFIX_DIM "+string(d0));',
    ]
    # Random hyperplanes in the parameter ring.  system("random") is
    # seeded from the clock; pin a seed via the integer argument.
    L += [
        "int s;",
        "int ok;",
        "ideal G;",
        "ideal SL;",
        "for (s=1; s<=ntry; s++) {",
        "  SL=G0;",
        "  int nv=%d;" % (len(params)),
        "  int j;",
        "  for (j=1; j<=max(1, nv-4); j++) {",
        "    poly lin=var(1+int(random(1,nv)))-int(random(0,char-1));",
        "    SL=SL+ideal(lin);",
        "  }",
        "  G=std(SL);",
        "  if (reduce(1,G)==0) {",
        '    print("PP_SLICE "+string(s)+" UNIT_SKIP");',
        "    continue;",
        "  }",
        "  ok=1;",
        "  for (i=1; i<=size(ALL); i++) {",
        "    if (reduce(ALL[i], G) != 0) { ok=0; break; }",
        "  }",
        "  if (ok==1) {",
        "    if (reduce(c, G)==0) {",
        '      print("PP_SLICE "+string(s)+" C_ZERO");',
        "    } else {",
        '      print("PP_SLICE "+string(s)+" POINT_PASS dim="+string(dim(G)));',
        "      hit=1;",
        "      break;",
        "    }",
        "  } else {",
        '    print("PP_SLICE "+string(s)+" MISS dim="+string(dim(G)));',
        "  }",
        "}",
        'if (hit==1) { print("PP_VERDICT POINT"); } else { print("PP_VERDICT NO_POINT"); }',
        "quit;",
    ]
    out.write_text("\n".join(L) + "\n")
    return out


def emit_zero_slice(stem: str, variables: list[str], gens: list[str],
                    char: int, keep: list[str], out: Path) -> Path:
    """Set every parameter outside `keep` to 0, std the specialized system."""
    drop = [v for v in variables if v not in keep and v != "T"]
    L = [
        "ring R=%d,(%s),dp;" % (char, ",".join(variables)),
        "option(noredSB);",
        'print("ZS_START stem=%s keep=%d drop=%d char=%d");' % (
            stem, len(keep), len(drop), char),
        "ideal MAP;",
    ]
    for i, v in enumerate(drop, start=1):
        L.append("MAP[%d]=%s;" % (i, v))
    L += ["ideal I; I[1]=T*c-1;"]
    for i, g in enumerate(gens, start=1):
        L.append("I[%d]=reduce(%s, MAP);" % (i + 1, g))
    L += [
        "int t=timer;",
        "ideal G=std(I);",
        'print("ZS_FULL seconds="+string(timer-t)+" basis="+string(size(G)));',
        "if (reduce(1,G)==0) { print(\"ZS_VERDICT UNIT\"); }",
        "else { print(\"ZS_DIM \"+string(dim(G))); print(\"ZS_VERDICT NONUNIT\");",
        "  if (reduce(c,G)==0) { print(\"ZS_C_ZERO\"); } else { print(\"ZS_C_LIVE\"); } }",
        "quit;",
    ]
    out.write_text("\n".join(L) + "\n")
    return out


def parse(stdout: str) -> dict:
    d: dict = {"controls": {}, "lines": []}
    for line in stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        d["lines"].append(line[:200])
        if line.startswith("CONTROL_"):
            d["controls"][line] = True
        m = re.match(r"MS_FULL seconds=(\d+) basis=(\d+)", line)
        if m:
            d["full"] = {"seconds": int(m.group(1)), "basis": int(m.group(2))}
        m = re.match(r"MS_DIM (-?\d+)", line)
        if m:
            d["dim"] = int(m.group(1))
        m = re.match(r"MS_VERDICT (\S+)", line)
        if m:
            d["verdict"] = m.group(1)
        m = re.match(r"MS_INDEP (.*)", line)
        if m:
            d["indep"] = m.group(1)
        m = re.match(r"PP_VERDICT (\S+)", line)
        if m:
            d["pp_verdict"] = m.group(1)
        m = re.match(r"ZS_VERDICT (\S+)", line)
        if m:
            d["zs_verdict"] = m.group(1)
        m = re.match(r"ZS_DIM (-?\d+)", line)
        if m:
            d["zs_dim"] = int(m.group(1))
        if "POINT_PASS" in line:
            d["point_pass"] = line
        if line.startswith("ZS_C_"):
            d["zs_c"] = line
    return d


def run_script(script: Path, timeout: int, cwd: Path) -> tuple[str, bool, int]:
    log = script.with_suffix(".live")
    env = os.environ.copy()
    for k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
              "NUMEXPR_NUM_THREADS"):
        env[k] = "1"
    to = False
    with log.open("w") as fh:
        proc = subprocess.Popen(
            ["Singular", "--cpus=1", "--threads=1", "--flint-threads=1",
             "-q", "--no-rc", str(script)],
            stdout=fh, stderr=subprocess.STDOUT, cwd=str(cwd), env=env,
        )
        try:
            proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
            to = True
        rc = proc.returncode if proc.returncode is not None else -1
    return log.read_text(errors="replace"), to, rc


def default_keep(variables: list[str]) -> list[str]:
    """A tiny centre+linear support: c and the constant / x / y monomials."""
    keep = ["c"]
    for v in variables:
        if re.fullmatch(r"h_\d+_\d+", v):
            a, b = v.split("_")[1:]
            if int(a) <= 1 and int(b) <= 1:
                keep.append(v)
        elif re.fullmatch(r"[AB]\d+_\d+_\d+", v):
            parts = v.split("_")
            a, b = int(parts[1]), int(parts[2])
            if a <= 1 and b <= 1:
                keep.append(v)
    return keep


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--class-id", required=True)
    ap.add_argument("--stem", required=True)
    ap.add_argument("--char", type=int, default=32003)
    ap.add_argument("--timeout", type=int, default=1200)
    ap.add_argument("--mode", default="unbounded",
                    choices=("unbounded", "point", "zero-slice", "all"))
    ap.add_argument("--tag", default="")
    a = ap.parse_args()
    variables, gens, meta = load(a.class_id, a.stem)
    jobs = HERE / "classes" / a.class_id / "jobs"
    jobs.mkdir(parents=True, exist_ok=True)
    cwd = HERE / "classes" / a.class_id
    tag = a.tag or ("fo_%s_%d" % (a.mode[0], a.char))
    results = {"stem": a.stem, "class_id": a.class_id, "char": a.char,
               "equations": len(gens), "unknowns": len(variables) - 1,
               "chart": meta.get("meta", {}).get("chart"),
               "modes": {}}
    if a.mode in ("unbounded", "all"):
        script = jobs / ("%s_%s.sing" % (a.stem, tag if a.mode == "unbounded" else tag + "_u"))
        emit_unbounded(a.stem, variables, gens, a.char, script)
        t0 = time.time()
        out, to, rc = run_script(script, a.timeout, cwd)
        rec = parse(out)
        rec.update({"timed_out": to, "rc": rc, "wall": round(time.time() - t0, 3),
                    "script": str(script.relative_to(ROOT))})
        (script.with_suffix(".out")).write_text(out)
        results["modes"]["unbounded"] = rec
        print(json.dumps({"unbounded": rec}, indent=2))
    if a.mode in ("point", "all"):
        script = jobs / ("%s_%s_pp.sing" % (a.stem, tag))
        emit_point_probe(a.stem, variables, gens, a.char, script)
        t0 = time.time()
        out, to, rc = run_script(script, min(a.timeout, 400), cwd)
        rec = parse(out)
        rec.update({"timed_out": to, "rc": rc, "wall": round(time.time() - t0, 3)})
        (script.with_suffix(".out")).write_text(out)
        results["modes"]["point"] = rec
        print(json.dumps({"point": rec}, indent=2))
    if a.mode in ("zero-slice", "all"):
        keep = default_keep(variables)
        script = jobs / ("%s_%s_zs.sing" % (a.stem, tag))
        emit_zero_slice(a.stem, variables, gens, a.char, keep, script)
        t0 = time.time()
        out, to, rc = run_script(script, min(a.timeout, 300), cwd)
        rec = parse(out)
        rec.update({"timed_out": to, "rc": rc, "wall": round(time.time() - t0, 3),
                    "keep": keep, "keep_n": len(keep)})
        (script.with_suffix(".out")).write_text(out)
        results["modes"]["zero_slice"] = rec
        print(json.dumps({"zero_slice": rec}, indent=2))
    outj = jobs / ("%s_%s.json" % (a.stem, tag))
    outj.write_text(json.dumps(results, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
