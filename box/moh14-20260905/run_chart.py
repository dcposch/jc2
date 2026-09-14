#!/usr/bin/env python3
"""Step 3b: build + run one descended order chart for a row of the 14.

Chart logic = the charged order_basis_full.py verbatim; only `closed_form` is
replaced by the multi-level Phi_eff map validated against Moh Appendix II, with
the SAFE (over-approximating) threshold B_safe.  Artifacts land in this lane's
own directory (OB.HERE is repointed), never in the charged instrument's dir.
"""
import argparse, json, sys, time
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0, "/home/ubuntu/jc2/box/orderbasis-20260903")
import order_basis_full as OB

LANE = Path("/home/ubuntu/jc2/box/moh14-20260905")
OB.HERE = LANE / "charts"
(LANE / "charts").mkdir(exist_ok=True)
OB.ROOT = Path("/home/ubuntu/jc2")

ROWSJ = json.load(open(LANE / "descend14.json"))

def label(r):
    return "%d,%d|%s|V=%s" % (r["n"], r["m"], ",".join(map(str, r["Ms"])),
                              ",".join(str(v) for _, v in sorted((int(a), b) for a, b in r["V"].items())))

def pick(idx):
    return ROWSJ[idx]

def install(r, mode):
    d = {int(k): F(v) for k, v in r["delta"].items()}
    B = F(r["Bsafe"]) if mode == "safe" else F(r["Btight"])
    C = {"K": r["Kp"], "e": r["ep"], "q": r["qp"], "u": r["up"],
         "R": r["np"] - int(r["Mp"][str(r["sp"])]) - 1, "Pi": r["ep"] + r["qp"],
         "delta1": d[1], "delta2": d[2], "B": B,
         "lambda_P": r["ep"] * B, "lambda_Q": r["qp"] * B, "d3prime": 0}
    OB.closed_form = lambda row, _C=C: _C
    OB.manifest_check = lambda: {"ok": "LANE_REPOINTED"}
    key = ("r%d_%d_%d_M%s_V%s" % (r["n"], r["m"], r["np"],
           "_".join(str(r["Mp"][str(i)]) for i in range(2, r["sp"] + 1)).replace("-", "m"),
           "_".join(str(r["Vp"][str(i)]) for i in range(2, r["sp"] + 1))))
    return C, OB.Row(key=key, label=label(r), n=r["np"], m=r["mp"],
                     M2=int(r["Mp"][str(r["sp"])]), V2=r["V2p"], k=r["k"])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--idx", type=int, required=True)
    ap.add_argument("--partition", type=str, required=True)   # e.g. "3" or "2+1" or "" for empty
    ap.add_argument("--mode", default="safe")
    ap.add_argument("--char", type=int, default=0)
    ap.add_argument("--algorithm", default="std")
    ap.add_argument("--build-timeout", type=int, default=900)
    ap.add_argument("--solve-timeout", type=int, default=1500)
    ap.add_argument("--build-only", action="store_true")
    a = ap.parse_args()

    r = pick(a.idx)
    C, Row = install(r, a.mode)
    part = tuple(int(v) for v in a.partition.split("+")) if a.partition else ()
    print("ROW  %s  (n',m')=(%d,%d) K'=%d e'=%d q'=%d V2'=%d u'=%d l=%d B=%s part=%s"
          % (label(r), r["np"], r["mp"], C["K"], C["e"], C["q"], Row.V2, C["u"], r["k"],
             C["B"], part), flush=True)
    if sum(part) != C["u"]:
        print("PARTITION-MISMATCH sum(part)=%d u'=%d" % (sum(part), C["u"])); sys.exit(2)

    t0 = time.time()
    info = OB.write_native_builder(Row, part)
    print("BUILDER %s  unknowns=%d  [%.1fs]" % (info["builder"], len(info["variables"]), time.time() - t0), flush=True)
    br = OB.run_singular(OB.ROOT / info["builder"], timeout=a.build_timeout)
    print("BUILD rc=%s wall=%.1fs" % (br.get("returncode"), br.get("seconds", -1)), flush=True)
    for ln in (br.get("stdout") or "").splitlines():
        if "NATIVE_" in ln: print("   " + ln)
    rowsp = OB.ROOT / info["rows_path"]
    if not rowsp.exists():
        print("VERDICT BUILD-FAILED (no rows file)"); sys.exit(3)
    print("ROWS %s  bytes=%d" % (info["rows_path"], rowsp.stat().st_size), flush=True)
    if a.build_only: return

    meta_path = OB.ROOT / info["meta_path"] if "meta_path" in info else None
    mp = Path("/home/ubuntu/jc2") / info["meta_path"]
    sysinfo = OB.write_system_from_rows(mp, a.char, a.algorithm)
    print("SYSTEM %s equations=%d unknowns=%d"
          % (sysinfo["system"], sysinfo["equations"], sysinfo["unknowns"]), flush=True)
    sr = OB.run_singular(OB.ROOT / sysinfo["system"], timeout=a.solve_timeout)
    out = sr.get("stdout") or ""
    print("SOLVE rc=%s wall=%.1fs" % (sr.get("returncode"), sr.get("seconds", -1)), flush=True)
    for ln in out.splitlines():
        if any(t in ln for t in ("CONTROL_", "MAIN_", "dim=", "?")): print("   " + ln)
    if "MAIN_SATURATED_EMPTY" in out:   v = "SATURATED-EMPTY (row dead)"
    elif "MAIN_NONTRIVIAL" in out:      v = "NONTRIVIAL"
    elif sr.get("returncode") == 124:   v = "TIMEOUT"
    else:                               v = "UNKNOWN"
    print("VERDICT %s" % v, flush=True)

main()
