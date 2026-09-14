#!/usr/bin/env python3
"""Dump an I_light strata chart to msolve input and run the modular screen.

Self-contained emitter (no msolveio version gate).  msolve input format:

    v0,v1,...,vn
    p
    g1,
    g2,
    ...
    gk

Variable names are aliased h_i_j / B_i_j / q0 / q0_inv -> v0,v1,... because
msolve rejects underscores.  The alias map is recorded in the JSON payload so
any msolve point can be pulled back to the chart coordinates.

A modular UNIT is a SCREEN only; exact Q is the only promotion path.
A modular NONUNIT at a single prime is evidence, not a proof, that the chart
survives over Q (the prime could divide the denominator of a Q certificate).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
HERE = ROOT / "box" / "k4ray-strata-solve-20260905"
sys.path.insert(0, str(HERE))

from strata_chart import extra_generators, strata_prelude  # noqa: E402


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(payload, encoding="utf-8")
    tmp.replace(path)


def dump_generators(K, b, pin_index, ch, timeout, outdir, extras_mode="all"):
    prelude, names, weights, meta = strata_prelude(
        K, b, pin_index=pin_index, ch=ch, theorem_cut=False
    )
    extras = extra_generators(pin_index)
    if extras_mode == "localizer":
        extras = [g for g in extras if g != "CSTP-1"]
    elif extras_mode == "none":
        extras = []
    dump = outdir / f"K{K}_B{b}_Q{pin_index}_p{ch}_{extras_mode}.dump.sing"
    lines = [prelude, "int i;"]
    for extra in extras:
        lines.append(f"ROWS = ROWS + ideal({extra});")
    lines.append("ROWS = simplify(ROWS,2);")
    lines.append('print("DUMP__N "+string(size(ROWS)));')
    lines.append('print("DUMP__VARS "+string(nvars(basering)));')
    if ch == 0:
        lines.append('for (i=1; i<=size(ROWS); i++) { print("DUMP__ROW "+string(cleardenom(ROWS[i]))); }')
    else:
        lines.append('for (i=1; i<=size(ROWS); i++) { print("DUMP__ROW "+string(ROWS[i])); }')
    lines.append('print("DUMP__DONE 1");')
    lines.append("quit;")
    atomic_write(dump, "\n".join(lines) + "\n")
    t0 = time.time()
    timed_out = False
    try:
        proc = subprocess.run(
            ["stdbuf", "-oL", "-eL", "Singular", "--no-rc", "-q", str(dump)],
            capture_output=True, text=True, timeout=timeout, check=False,
        )
        out, err, rc = proc.stdout, proc.stderr, proc.returncode
    except subprocess.TimeoutExpired as exc:
        out = (exc.stdout or b"")
        err = (exc.stderr or b"")
        out = out.decode("utf-8", "replace") if isinstance(out, bytes) else out
        err = err.decode("utf-8", "replace") if isinstance(err, bytes) else err
        rc = None
        timed_out = True
    atomic_write(dump.with_suffix(".out"), out)
    atomic_write(dump.with_suffix(".err"), err)
    rows, markers = [], {}
    for line in out.splitlines():
        if line.startswith("DUMP__ROW "):
            rows.append(line[len("DUMP__ROW "):].strip())
        elif line.startswith("PRE__") or line.startswith("DUMP__"):
            parts = line.split(maxsplit=1)
            markers[parts[0]] = parts[1] if len(parts) > 1 else ""
    return {
        "names": names, "weights": weights, "meta": meta, "rows": rows,
        "extras": extras, "returncode": rc, "n": len(rows),
        "form_wall": round(time.time() - t0, 3), "form_timed_out": timed_out,
        "markers": markers,
    }


def emit(gens, msolve_vars, ch):
    head = ",".join(msolve_vars) + "\n" + str(ch) + "\n"
    return head + ",\n".join(gens) + "\n"


def classify(out_text):
    """msolve -g 2 output: comment header (#...) then the reduced GB as [g1,...]:.

    The unit ideal prints as ``[1]:`` with ``#length of basis: 1 element``.
    """
    lines = out_text.splitlines()
    length = None
    body = []
    for line in lines:
        if line.startswith("#"):
            m = re.search(r"length of basis:\s*(\d+)", line)
            if m:
                length = int(m.group(1))
            continue
        body.append(line)
    flat = re.sub(r"\s+", "", "".join(body))
    flat = flat.rstrip(":")
    if not flat:
        return ("EMPTY_OUTPUT", length)
    inner = flat
    if inner.startswith("[") and inner.endswith("]"):
        inner = inner[1:-1]
    parts = [q for q in inner.split(",") if q]
    if parts == ["1"]:
        return ("UNIT", length)
    if parts == ["0"] or parts == []:
        return ("ZERO_IDEAL", length)
    return ("NONUNIT", length)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("K", type=int)
    p.add_argument("b", type=int)
    p.add_argument("--pin-index", type=int, default=0)
    p.add_argument("--char", type=int, default=32003)
    p.add_argument("--dump-timeout", type=int, default=3600)
    p.add_argument("--msolve-timeout", type=int, default=5400)
    p.add_argument("--threads", type=int, default=2)
    p.add_argument("--outdir", default=str(HERE / "msolve"))
    p.add_argument("--run", action="store_true")
    p.add_argument("--extras", default="all", choices=["all", "localizer", "none"])
    a = p.parse_args()
    outdir = Path(a.outdir)
    stem = f"K{a.K}_B{a.b}_Q{a.pin_index}_p{a.char}"
    if a.extras != "all":
        stem += f"_{a.extras}"
    t0 = time.time()
    d = dump_generators(a.K, a.b, a.pin_index, a.char, a.dump_timeout, outdir, a.extras)
    payload = {
        "stem": stem, "K": a.K, "b": a.b, "pin_index": a.pin_index, "char": a.char,
        "nvars": len(d["names"]), "ngens_dumped": d["n"],
        "geom": d["meta"]["geometric_parameter_count"],
        "gb_vars": d["meta"]["gb_parameter_count"],
        "form_wall": d["form_wall"], "form_timed_out": d["form_timed_out"],
        "markers": d["markers"], "weights": d["weights"], "extras_mode": a.extras,
        "extras": d["extras"],
    }
    if d["n"] == 0 or d["form_timed_out"]:
        payload["verdict"] = "FORMATION_TIMEOUT" if d["form_timed_out"] else "FORMATION_EMPTY"
        print("MSJOB__RESULT " + json.dumps(payload, sort_keys=True, default=str))
        atomic_write(outdir / f"{stem}.json", json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n")
        return
    raw = list(d["names"])
    alias = {n: f"v{i}" for i, n in enumerate(raw)}
    order = sorted(raw, key=len, reverse=True)
    pat = re.compile("|".join(re.escape(n) for n in order))
    gens = []
    for g in d["rows"]:
        if not g or g == "0":
            continue
        gens.append(pat.sub(lambda m: alias[m.group(0)], g).replace(" ", ""))
    text = emit(gens, [alias[n] for n in raw], a.char)
    ms = outdir / f"{stem}.ms"
    atomic_write(ms, text)
    payload["ms_path"] = str(ms)
    payload["ms_bytes"] = len(text)
    payload["ms_sha256"] = hashlib.sha256(text.encode()).hexdigest()
    payload["ngens"] = len(gens)
    payload["alias_sample"] = {n: alias[n] for n in raw[:3] + raw[-3:]}
    if a.run:
        t1 = time.time()
        outp = outdir / f"{stem}.msout"
        cmd = ["msolve", "-g", "2", "-t", str(a.threads), "-f", str(ms), "-o", str(outp)]
        try:
            pr = subprocess.run(cmd, capture_output=True, text=True,
                                timeout=a.msolve_timeout, check=False)
            rc, mo, me, to = pr.returncode, pr.stdout, pr.stderr, False
        except subprocess.TimeoutExpired:
            rc, mo, me, to = None, "", "", True
        payload["msolve_wall"] = round(time.time() - t1, 3)
        payload["msolve_rc"] = rc
        payload["msolve_timed_out"] = to
        payload["msolve_stderr"] = me[-1500:]
        txt = outp.read_text() if outp.exists() else ""
        payload["msout_bytes"] = len(txt)
        payload["msout_head"] = txt[:400]
        if to:
            payload["verdict"] = ("EXACTQ" if a.char == 0 else "MODULAR") + "_TIMEOUT"
        elif rc not in (0,):
            payload["verdict"] = f"MSOLVE_RC_{rc}"
        else:
            cls, blen = classify(txt)
            payload["msolve_basis_length"] = blen
            pre = "EXACTQ" if a.char == 0 else "MODULAR"
            payload["verdict"] = f"{pre}_UNIT" if cls == "UNIT" else (
                f"{pre}_NONUNIT" if cls == "NONUNIT" else pre + "_" + cls)
            if cls == "NONUNIT":
                payload["msout_tail"] = txt[-600:]
    payload["total_wall"] = round(time.time() - t0, 3)
    print("MSJOB__RESULT " + json.dumps(payload, sort_keys=True, default=str))
    atomic_write(outdir / f"{stem}.json", json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n")


if __name__ == "__main__":
    main()
