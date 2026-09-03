#!/usr/bin/env python3
"""t=1 Horner-cap gate; t=2 slice dim+point+J check; TIMEOUT rows via Singular."""
from __future__ import annotations

import json
import os
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
BOX = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, BOX)
OUT = os.path.join(HERE, "out")

import sympy as sp
from solve_twopoint import (
    solve_horner_cap, build_horner_cap, hadic_jac_eqs, write_singular,
    run_singular, jac,
)
from solve import jac_eqs, Alarm, Timeout
from solve_twopoint import solve_d2e3_d1


def conv(o):
    if isinstance(o, dict):
        return {str(k): conv(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [conv(x) for x in o]
    if isinstance(o, (int, float, str, bool)) or o is None:
        return o
    return str(o)


def dump(name, obj):
    path = os.path.join(OUT, name)
    with open(path, "w") as f:
        json.dump(conv(obj), f, indent=2, sort_keys=True)
    print("  wrote", path, flush=True)


def main():
    print("== GATE t=1 horner_cap (expanded jac, must SATURATED-EMPTY) ==", flush=True)
    r = solve_horner_cap(16, 12, 13, 3, 1, timeout=180, drop_high=0,
                         backend="singular", char=0, order="dp")
    print("  t1 horner Q-sing", r.get("verdict"), "empty", r.get("empty"),
          "nunk", r.get("n_unknowns"), "neqs", r.get("n_eqs"),
          "unsat_empty", r.get("unsaturated_empty"), "neg", r.get("negative_nontrivial"),
          "elapsed", r.get("elapsed"), "tail", (r.get("stdout_tail") or "")[-400:],
          flush=True)
    dump("gate_t1_horner.json", r)

    print("\n== GATE t=1 hadic vs expanded eq counts ==", flush=True)
    B = build_horner_cap(16, 12, 13, 3, 1, drop_high=0)
    eqs_exp, _ = jac_eqs(B["f"], B["g"], B["c"], 1, B["x"], B["y"])
    eqs_h, bp = hadic_jac_eqs(B["h"], B["f_terms"], B["g_terms"], B["c"], 1, B["x"], B["y"])
    print("  expanded", len(eqs_exp), "hadic", len(eqs_h), "hpows", len(bp), flush=True)
    dump("gate_t1_eqcounts.json", dict(n_exp=len(eqs_exp), n_hadic=len(eqs_h),
                                       nunk=B["n_unknowns"]))

    print("\n== t=2 slice19: dim + c=1 slice + try b_i=0 ==", flush=True)
    B = build_horner_cap(28, 20, 25, 3, 1, drop_high=5)
    eqs, bp = hadic_jac_eqs(B["h"], B["f_terms"], B["g_terms"], B["c"], 1, B["x"], B["y"])
    T = sp.Symbol("T")
    gens = B["params"] + [B["c"], T]
    td = tempfile.mkdtemp(prefix="a2k16w-")
    spath = os.path.join(td, "t2s.sing")
    names = write_singular(spath, eqs, gens, ["T*c-1"], char=0, order="dp")
    # append dim
    with open(spath) as f:
        txt = f.read()
    txt = txt.replace("quit;",
                      'print("DIM="); dim(G);\n'
                      'print("DIM_UNSAT="); dim(G0);\n'
                      'ideal Gc=subst(G,c,1);\n'
                      'ideal Gc2=std(Gc);\n'
                      'print("C1_SIZE="); size(Gc2);\n'
                      'if (reduce(1,Gc2)==0) { print("C1_EMPTY"); } else { print("C1_NONTRIVIAL"); }\n'
                      'print("C1_DIM="); dim(Gc2);\n'
                      "quit;\n")
    with open(spath, "w") as f:
        f.write(txt)
    t0 = time.time()
    import subprocess
    rr = subprocess.run(["Singular", "-q", "--no-rc", spath],
                        capture_output=True, text=True, timeout=60)
    out = (rr.stdout or "") + (rr.stderr or "")
    print("  dim-run elapsed", time.time() - t0, flush=True)
    print(out[-1500:], flush=True)
    dump("t2_slice19_dim.json", dict(stdout=out[-3000:], n_eqs=len(eqs),
                                     nunk=B["n_unknowns"], names=names))

    # b_i=0 specialization: h = y^3(y-x)
    print("\n== t=2 slice, set b1=b2=b3=b4=0, groebner the rest ==", flush=True)
    subs0 = {sp.Symbol(s): 0 for s in ("b1", "b2", "b3", "b4")}
    eqs0 = [sp.expand(e.subs(subs0)) for e in eqs]
    eqs0 = [e for e in eqs0 if e != 0]
    rest = [p for p in B["params"] if str(p) not in ("b1", "b2", "b3", "b4")]
    print("  eqs after b=0:", len(eqs0), "rest unk", len(rest) + 1, flush=True)
    gens0 = rest + [B["c"], T]
    spath0 = os.path.join(td, "t2s_b0.sing")
    write_singular(spath0, eqs0, gens0, ["T*c-1"], char=0, order="dp")
    with open(spath0) as f:
        txt = f.read()
    txt = txt.replace("quit;", 'print("DIM="); dim(G);\nquit;\n')
    with open(spath0, "w") as f:
        f.write(txt)
    r0 = subprocess.run(["Singular", "-q", "--no-rc", spath0],
                        capture_output=True, text=True, timeout=30)
    out0 = (r0.stdout or "") + (r0.stderr or "")
    print(out0[-800:], flush=True)
    dump("t2_slice19_b0.json", dict(stdout=out0[-2000:], n_eqs=len(eqs0)))

    # try to build expanded f,g at a numeric trial: all free=0 except c=1
    print("\n== direct J check at leading-form + zero remainders, c=1 ==", flush=True)
    x, y = B["x"], B["y"]
    h0 = B["h"].subs({sp.Symbol("b1"): 0, sp.Symbol("b2"): 0,
                      sp.Symbol("b3"): 0, sp.Symbol("b4"): 0})
    # remainders 0 => f=h^5, g=h^7, J=0
    f0 = sp.expand(h0 ** 5)
    g0 = sp.expand(h0 ** 7)
    J0 = sp.expand(jac(f0, g0, x, y))
    print("  pure powers J==0?", J0 == 0, "h0", h0, flush=True)

    print("\n== TIMEOUT d2e3_d1 via Singular: skip (no sing path in d2e3_d1). sympy already TIMEOUT. ==", flush=True)
    # Newton-tight of those two: not this script.

    print("GATE+WITNESS DONE", flush=True)


if __name__ == "__main__":
    main()
