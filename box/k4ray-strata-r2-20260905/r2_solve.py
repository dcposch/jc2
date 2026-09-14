#!/usr/bin/env python3
"""Round-2 k4ray beta-stratum solver.

Reuses round 1's charts byte-for-byte: strata_prelude / extra_generators are
imported unmodified from box/k4ray-strata-solve-20260905/strata_chart.py.

Round-2 changes are ENGINE-ONLY:
  * ONE Singular formation per chart, over Q, with cleardenom (integral gens).
    Round 1 measured formation cost as char-independent, so a second char-p
    formation is pure waste.  The modular screen is run on the SAME integral
    generator file with only the msolve characteristic header changed to 32003,
    i.e. the screen is literally the reduction mod p of the exact-Q input.
  * msolve runs under /usr/bin/time -v (peak RSS) with -v 2 (F4 degree trace).
  * modular screen first; a modular UNIT immediately triggers the exact-Q run
    on the identical generator body.

FALLACY-v2: a modular unit is a SCREEN.  Only the exact-Q [1] is a certificate.
I_light drops MASTER cutoff ROWS only, never unknowns.
"""
from __future__ import annotations

import argparse, hashlib, json, os, re, subprocess, sys, time
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
R1 = ROOT / "box" / "k4ray-strata-solve-20260905"
HERE = ROOT / "box" / "k4ray-strata-r2-20260905"
sys.path.insert(0, str(R1))
from strata_chart import extra_generators, strata_prelude  # noqa: E402


def atomic_write(path: Path, payload: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(payload, encoding="utf-8")
    tmp.replace(path)


def form(K, b, pin, timeout, outdir):
    prelude, names, weights, meta = strata_prelude(
        K, b, pin_index=pin, ch=0, theorem_cut=False)
    extras = extra_generators(pin)
    dump = outdir / f"K{K}_B{b}_Q{pin}.dump.sing"
    L = [prelude, "int i;"]
    for e in extras:
        L.append(f"ROWS = ROWS + ideal({e});")
    L.append("ROWS = simplify(ROWS,2);")
    L.append('print("DUMP__N "+string(size(ROWS)));')
    L.append('print("DUMP__VARS "+string(nvars(basering)));')
    L.append('for (i=1; i<=size(ROWS); i++) { print("DUMP__ROW "+string(cleardenom(ROWS[i]))); }')
    L.append('print("DUMP__DONE 1");')
    L.append("quit;")
    atomic_write(dump, "\n".join(L) + "\n")
    t0 = time.time(); to = False
    try:
        pr = subprocess.run(["stdbuf", "-oL", "-eL", "Singular", "--no-rc", "-q", str(dump)],
                            capture_output=True, text=True, timeout=timeout, check=False)
        out, err, rc = pr.stdout, pr.stderr, pr.returncode
    except subprocess.TimeoutExpired as exc:
        out = exc.stdout or b""; err = exc.stderr or b""
        out = out.decode("utf-8", "replace") if isinstance(out, bytes) else out
        err = err.decode("utf-8", "replace") if isinstance(err, bytes) else err
        rc, to = None, True
    atomic_write(dump.with_suffix(".out"), out)
    atomic_write(dump.with_suffix(".err"), err)
    rows, mk = [], {}
    for ln in out.splitlines():
        if ln.startswith("DUMP__ROW "):
            rows.append(ln[len("DUMP__ROW "):].strip())
        elif ln.startswith("PRE__") or ln.startswith("DUMP__"):
            p = ln.split(maxsplit=1); mk[p[0]] = p[1] if len(p) > 1 else ""
    return dict(names=names, weights=weights, meta=meta, rows=rows, extras=extras,
                rc=rc, n=len(rows), form_wall=round(time.time() - t0, 3),
                form_timed_out=to, markers=mk)


def classify(txt):
    length, body = None, []
    for ln in txt.splitlines():
        if ln.startswith("#"):
            m = re.search(r"length of basis:\s*(\d+)", ln)
            if m: length = int(m.group(1))
            continue
        body.append(ln)
    flat = re.sub(r"\s+", "", "".join(body)).rstrip(":")
    if not flat: return ("EMPTY_OUTPUT", length)
    inner = flat[1:-1] if flat.startswith("[") and flat.endswith("]") else flat
    parts = [q for q in inner.split(",") if q]
    if parts == ["1"]: return ("UNIT", length)
    if parts == ["0"] or not parts: return ("ZERO_IDEAL", length)
    return ("NONUNIT", length)


DEG_RE = re.compile(r"[Dd]egree\D{0,12}(\d+)")


def run_msolve(ms: Path, outp: Path, threads, timeout, char):
    t0 = time.time()
    cmd = ["/usr/bin/time", "-v", "msolve", "-g", "2", "-v", "2",
           "-t", str(threads), "-f", str(ms), "-o", str(outp)]
    try:
        pr = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, check=False)
        rc, so, se, to = pr.returncode, pr.stdout, pr.stderr, False
    except subprocess.TimeoutExpired as exc:
        so = (exc.stdout or b""); se = (exc.stderr or b"")
        so = so.decode("utf-8", "replace") if isinstance(so, bytes) else so
        se = se.decode("utf-8", "replace") if isinstance(se, bytes) else se
        rc, to = None, True
    wall = round(time.time() - t0, 3)
    rss = None
    m = re.search(r"Maximum resident set size \(kbytes\): (\d+)", se)
    if m: rss = int(m.group(1))
    degs = [int(d) for d in DEG_RE.findall(so)]
    atomic_write(outp.with_suffix(".log"), so[-40000:] + "\n--STDERR--\n" + se[-8000:])
    txt = outp.read_text() if outp.exists() else ""
    pre = "EXACTQ" if char == 0 else "MODULAR"
    if to: verdict, blen = pre + "_TIMEOUT", None
    elif rc != 0: verdict, blen = f"MSOLVE_RC_{rc}", None
    else:
        cls, blen = classify(txt)
        verdict = f"{pre}_{cls}"
    r = dict(verdict=verdict, rc=rc, wall=wall, peak_rss_kb=rss, timed_out=to,
             basis_length=blen, f4_max_degree=(max(degs) if degs else None),
             msout_bytes=len(txt), msout_head=txt[:300])
    if verdict.endswith("NONUNIT"):
        r["msout_full"] = txt[:200000]
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("K", type=int); ap.add_argument("b", type=int)
    ap.add_argument("--pin-index", type=int, default=0)
    ap.add_argument("--form-timeout", type=int, default=5400)
    ap.add_argument("--msolve-timeout", type=int, default=3000)
    ap.add_argument("--threads", type=int, default=32)
    ap.add_argument("--outdir", default=str(HERE / "msolve"))
    ap.add_argument("--no-run", action="store_true")
    a = ap.parse_args()
    outdir = Path(a.outdir); outdir.mkdir(parents=True, exist_ok=True)
    stem = f"K{a.K}_B{a.b}_Q{a.pin_index}"
    T0 = time.time()
    d = form(a.K, a.b, a.pin_index, a.form_timeout, outdir)
    P = dict(stem=stem, K=a.K, b=a.b, pin_index=a.pin_index, round=2,
             nvars=len(d["names"]), ngens_dumped=d["n"],
             geom=d["meta"]["geometric_parameter_count"],
             gb_vars=d["meta"]["gb_parameter_count"],
             form_wall=d["form_wall"], form_timed_out=d["form_timed_out"],
             form_rc=d["rc"], markers=d["markers"], weights=d["weights"],
             extras=d["extras"], host=os.uname().nodename)
    if d["n"] == 0 or d["form_timed_out"]:
        P["verdict"] = "FORMATION_TIMEOUT" if d["form_timed_out"] else "FORMATION_EMPTY"
        P["total_wall"] = round(time.time() - T0, 3)
        print("R2__RESULT " + json.dumps(P, sort_keys=True, default=str), flush=True)
        atomic_write(outdir / f"{stem}.json", json.dumps(P, indent=2, sort_keys=True, default=str) + "\n")
        return
    raw = list(d["names"])
    alias = {n: f"v{i}" for i, n in enumerate(raw)}
    pat = re.compile("|".join(re.escape(n) for n in sorted(raw, key=len, reverse=True)))
    gens = [pat.sub(lambda m: alias[m.group(0)], g).replace(" ", "")
            for g in d["rows"] if g and g != "0"]
    body = ",\n".join(gens) + "\n"
    head = ",".join(alias[n] for n in raw) + "\n"
    msQ = outdir / f"{stem}_p0.ms"; msP = outdir / f"{stem}_p32003.ms"
    atomic_write(msQ, head + "0\n" + body)
    atomic_write(msP, head + "32003\n" + body)
    P.update(ngens=len(gens), ms_bytes=len(head + "0\n" + body),
             body_sha256=hashlib.sha256(body.encode()).hexdigest(),
             ms_p0_sha256=hashlib.sha256((head + "0\n" + body).encode()).hexdigest(),
             ms_p32003_sha256=hashlib.sha256((head + "32003\n" + body).encode()).hexdigest(),
             alias_sample={n: alias[n] for n in raw[:3] + raw[-3:]})
    print("R2__FORMED " + json.dumps({k: P[k] for k in
          ("stem", "nvars", "ngens", "form_wall", "body_sha256")}), flush=True)
    if not a.no_run:
        P["modular"] = run_msolve(msP, outdir / f"{stem}_p32003.msout",
                                  a.threads, a.msolve_timeout, 32003)
        P["verdict"] = P["modular"]["verdict"]
        atomic_write(outdir / f"{stem}.json", json.dumps(P, indent=2, sort_keys=True, default=str) + "\n")
        if P["modular"]["verdict"] == "MODULAR_UNIT":
            P["exactq"] = run_msolve(msQ, outdir / f"{stem}_p0.msout",
                                     a.threads, a.msolve_timeout, 0)
            P["verdict"] = P["exactq"]["verdict"]
    P["total_wall"] = round(time.time() - T0, 3)
    print("R2__RESULT " + json.dumps(P, sort_keys=True, default=str), flush=True)
    atomic_write(outdir / f"{stem}.json", json.dumps(P, indent=2, sort_keys=True, default=str) + "\n")


if __name__ == "__main__":
    main()
