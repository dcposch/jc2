#!/usr/bin/env python3
"""G2 without (c): honest 14+27 order support, tail (3) only, then optional J."""
from __future__ import annotations
import json, time, sys, os
import sympy as sp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from appii_reduce import (
    datum, supports, build_h, build_beta_generic, tail_m2n3, groebner_sat, jac_eqs,
)

x, y = sp.symbols("x y")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")
os.makedirs(OUT, exist_ok=True)


def conv(o):
    if isinstance(o, dict):
        return {str(k): conv(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [conv(v) for v in o]
    if isinstance(o, sp.Basic):
        return str(o)
    if isinstance(o, (int, float, str, bool)) or o is None:
        return o
    return str(o)


def main():
    t0 = time.time()
    C = datum(15, 10, 4, 1, 4)
    S = supports(C, use_c=False)
    print("n_h", S["n_h"], "n_beta", S["n_beta"], "n_ord", S["n_ord"])
    h, hfrees, hnames = build_h(C, S, x, y, use_c=False)
    beta, bfrees, bnames = build_beta_generic(S, x, y)
    print("building tail (3) on 14+27 ...")
    t1 = time.time()
    T = tail_m2n3(h, beta, x, y, C["d2"])
    t_build = time.time() - t1
    print("built in %.2fs  deg_gamma=%s  #eqs7=%d #eqs3=%d #eqs_rem=%d #eqs=%d"
          % (t_build, T["deg_gamma"], len(T["eqs7"]), len(T["eqs3"]),
             len(T["eqs_rem"]), len(T["eqs"])))
    names = hnames + bnames
    n_unk, n_eq = len(names), len(T["eqs"])
    print("COUNT %d unk, %d eqs" % (n_unk, n_eq))
    # try eqs7 only first (cheaper)
    print("GB eqs7 only, sat first beta coeff ...")
    sat = names[len(hnames)]  # first beta
    m7 = groebner_sat(T["eqs7"], names, sat, order="grevlex", timeout=60, engine="singular")
    print("eqs7", m7.get("verdict"), "size", m7.get("basis_size"), "time", m7.get("elapsed"))
    print((m7.get("stdout_tail") or "")[-400:])
    m3 = None
    if m7.get("verdict") != "SATURATED-EMPTY":
        print("GB full tail (3), timeout 75s ...")
        m3 = groebner_sat(T["eqs"], names, sat, order="grevlex", timeout=75, engine="singular")
        print("full", m3.get("verdict"), "size", m3.get("basis_size"), "time", m3.get("elapsed"))
        print((m3.get("stdout_tail") or "")[-400:])
    verdict = "SATURATED-EMPTY" if (
        m7.get("verdict") == "SATURATED-EMPTY"
        or (m3 and m3.get("verdict") == "SATURATED-EMPTY")
    ) else ("COUNTING-BOUND" if (m3 and m3.get("verdict") == "TIMEOUT")
            or m7.get("verdict") == "TIMEOUT"
            else (m3 or m7).get("verdict"))
    out = dict(
        verdict=verdict, n_unknowns=n_unk, n_eqs=n_eq,
        n_eqs7=len(T["eqs7"]), n_eqs3=len(T["eqs3"]), t_build=t_build,
        eqs7=m7, full=m3, elapsed=time.time() - t0,
        note="honest (a) support 14+27; (c) off; tail only, no Jacobian in this job",
    )
    with open(os.path.join(OUT, "g2_generic.json"), "w") as f:
        json.dump(conv(out), f, indent=2)
    print("WROTE g2_generic.json", verdict, "elapsed", out["elapsed"])


if __name__ == "__main__":
    main()
