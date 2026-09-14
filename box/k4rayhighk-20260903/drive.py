#!/usr/bin/env python3
"""guided_gb driver for the k=4 ray high-K charts."""
import json, subprocess, sys, time
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "box" / "k4rayhighk-20260903"))

from box.lib.guided_gb import (  # noqa: E402
    HilbertHint, PromotionPolicy, RunConfig, SingularSystem, guided_groebner,
)
import gen_hk  # noqa: E402

RUNS = ROOT / "box" / "k4rayhighk-20260903" / "runs"


def prelude_rowcount(prelude, tag, timeout=900):
    """Run the prelude standalone to learn size(ROWS)."""
    cache = RUNS / f"{tag}.rowcount.json"
    if cache.exists():
        return json.loads(cache.read_text())
    RUNS.mkdir(parents=True, exist_ok=True)
    script = RUNS / f"{tag}.count.sing"
    script.write_text(prelude + '\nprint("PRE__ROWS_FINAL "+string(size(ROWS)));\nquit;\n')
    t0 = time.time()
    try:
        proc = subprocess.run(
            ["stdbuf", "-oL", "Singular", "--no-rc", "-q", str(script)],
            capture_output=True, text=True, timeout=timeout)
        out = proc.stdout
    except subprocess.TimeoutExpired as exc:
        out = (exc.stdout or b"").decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
    (RUNS / f"{tag}.count.out").write_text(out)
    info = {"wall": round(time.time() - t0, 2), "n": None, "markers": {}}
    for line in out.splitlines():
        if line.startswith("PRE__"):
            parts = line.split()
            info["markers"][parts[0]] = parts[1] if len(parts) > 1 else ""
    if "PRE__ROWS_FINAL" in info["markers"]:
        info["n"] = int(info["markers"]["PRE__ROWS_FINAL"])
    cache.write_text(json.dumps(info, indent=2))
    return info


def build(mode, K, Bdeg, ch, tk, tag, dehom=True, rhodeg=None, drop_top=True, extra="", rhocut=None, tbcut=False):
    if mode in ("direct", "idsix"):
        prelude, names, wts = gen_hk.direct(K, Bdeg, ch, tk, drop_top=drop_top, extra=extra, rhocut=rhocut, idsix=(mode=="idsix"), tbcut=tbcut)
    else:
        prelude, names, wts = gen_hk.quad(K, Bdeg, ch, tk, drop_top=drop_top, rhodeg=rhodeg)
    info = prelude_rowcount(prelude, tag)
    if info["n"] is None:
        return None, info, names, wts
    gens = [f"ROWS[{i}]" for i in range(1, info["n"] + 1)]
    if dehom:
        gens.append("CSTP-1")
    return prelude, info, names, wts, gens


def run(tag, mode, K, Bdeg, tk=4, chars=(0,), timeout=1500, dehom=True,
        rhodeg=None, drop_top=True, extra="", cores=4, rhocut=None, tbcut=False):
    built = build(mode, K, Bdeg, chars[0], tk, tag, dehom, rhodeg, drop_top, extra, rhocut, tbcut)
    if len(built) == 4:
        return {"tag": tag, "verdict": "PRELUDE_FAILED", "info": built[1]}
    prelude, info, names, wts, gens = built
    systems = []
    for ch in chars:
        pre = (prelude if ch == 0 else
               (gen_hk.direct(K, Bdeg, ch, tk, drop_top=drop_top, extra=extra, rhocut=rhocut, idsix=(mode=="idsix"), tbcut=tbcut)[0]
                if mode in ("direct","idsix") else
                gen_hk.quad(K, Bdeg, ch, tk, drop_top=drop_top, rhodeg=rhodeg)[0]))
        systems.append(SingularSystem(
            name=f"{tag}_p{ch}", prelude=pre, generators=tuple(gens),
            characteristic=ch, variables=tuple(names),
            homogeneous=False, positive_weights=(),
            metadata={"K": K, "Bdeg": Bdeg, "mode": mode, "dehom": dehom}))
    cfg = RunConfig(output_dir=RUNS / tag, timeout_seconds=timeout,
                    total_cores=cores, run_perturbed_control=False)
    t0 = time.time()
    res = guided_groebner(systems, hint=None,
                          policy=PromotionPolicy.exact_q("k4ray high-K dehomogenised kill test"),
                          config=cfg)
    wall = round(time.time() - t0, 2)
    summary = {"tag": tag, "K": K, "Bdeg": Bdeg, "mode": mode, "dehom": dehom,
               "nrows": info["n"], "nparams": len(names), "wall": wall, "rhocut": rhocut, "tbcut": tbcut,
               "verdict": res.verdict.value,
               "prelude_wall": info["wall"],
               "runs": [{"label": r["label"], "char": r["characteristic"],
                         "unit": r["main"]["unit"], "dim": r["main"]["dimension"],
                         "nf_all_zero": r["main"]["nf_all_zero"],
                         "timed_out": r["timed_out"], "secs": round(r["elapsed_seconds"], 2)}
                        for r in res.certificate["runs"]]}
    (RUNS / tag / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary))
    return summary


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("tag"); ap.add_argument("mode")
    ap.add_argument("K", type=int); ap.add_argument("Bdeg", type=int)
    ap.add_argument("--tk", type=int, default=4)
    ap.add_argument("--chars", default="0")
    ap.add_argument("--timeout", type=int, default=1500)
    ap.add_argument("--nodehom", action="store_true")
    ap.add_argument("--rhodeg", type=int, default=None)
    ap.add_argument("--keeptop", action="store_true")
    ap.add_argument("--cores", type=int, default=4)
    ap.add_argument("--rhocut", type=int, default=None)
    ap.add_argument("--tbcut", action="store_true")
    a = ap.parse_args()
    run(a.tag, a.mode, a.K, a.Bdeg, a.tk, tuple(int(c) for c in a.chars.split(",")),
        a.timeout, not a.nodehom, a.rhodeg, not a.keeptop, cores=a.cores, rhocut=a.rhocut, tbcut=a.tbcut)
