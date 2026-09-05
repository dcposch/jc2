#!/usr/bin/env python3
"""U-NEGATIVE: the exact operative list, its licence cross-tabs, and the
u_s>=2 split window (Prop 6.3 radius dichotomy, 17 prop63-radius-dichotomy)."""
from __future__ import annotations
import os, sys, json, collections
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from depth import child, operative, def51                      # noqa: E402
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "centre-gate-20260903")))
import moh_skeleton_full_frozen as B                           # noqa: E402


def window(u_s, v_s):
    """{delta in (1, v_s/u_s) : den(delta) <= u_s}  (Prop 6.3 split window)."""
    hi = F(v_s, u_s); out = []
    for q in range(1, u_s + 1):
        p = q + 1
        while F(p, q) < hi:
            d = F(p, q)
            if d > 1 and d.denominator <= u_s and d not in out:
                out.append(d)
            p += 1
    return sorted(out)


def main(nlo=16, nhi=200):
    rows = []
    for n in range(nlo, nhi + 1):
        for (m, Ms, V) in B.census(n, Kmin=2, full=True):
            if not operative(n, m, Ms, V):
                continue
            c = child(n, m, Ms, V); c.update(n=n, m=m, Ms=tuple(Ms), V=dict(V))
            rows.append(c)
    un = [r for r in rows if r["up"] < 0]
    print("operative %d ; U-NEGATIVE %d" % (len(rows), len(un)))

    def H(rs, k):
        return dict(sorted(collections.Counter(k(r) for r in rs).items(), key=lambda kv: str(kv[0])))
    print("\nU-NEG cross-tabs")
    print("  by u_s                 :", H(un, lambda r: r["u_s"]))
    print("  by s'                  :", H(un, lambda r: r["sp"]))
    print("  by ell                 :", H(un, lambda r: r["ell"]))
    print("  delta'_2 == -1         :", H(un, lambda r: r["dlp"][2] == -1))
    print("  delta'_{s'} == -1      :", H(un, lambda r: r["second_ok"]))
    print("  V'_2 vs d'_2 (V'_2/d'_2 range): %s .. %s"
          % (min(F(r["V2p"], 1) / r["d2p"] for r in un),
             max(F(r["V2p"], 1) / r["d2p"] for r in un)))
    print("  degree pairs           :", sorted({(r["n"], r["m"]) for r in un}))

    print("\n-- the %d U-NEG rows with u_s >= 2: split window (1, v_s/u_s), den <= u_s --"
          % len([r for r in un if r["u_s"] >= 2]))
    for r in [x for x in un if x["u_s"] >= 2]:
        w = window(r["u_s"], r["v_s"])
        print("  n=%d m=%d M=%s V=%s | s=%d d_s=%d u_s=%d v_s=%d | window=%s %s"
              % (r["n"], r["m"], list(r["Ms"]), r["V"], r["s"], r["u_s"] + r["v_s"],
                 r["u_s"], r["v_s"], [str(x) for x in w], "EMPTY -> (R) forced" if not w else ""))

    print("\n-- the U-NEG rows with u_s = 1 (Prop 6.4 discharges (R)) --")
    for r in sorted([x for x in un if x["u_s"] == 1], key=lambda r: (r["n"], r["m"]))[:100]:
        print("  n=%d m=%d M=%s V=%s | s=%d d_s=%d | (n',m')=(%d,%s) K'=%s V'_2=%d u'=%s ell=%d"
              % (r["n"], r["m"], list(r["Ms"]), r["V"], r["s"], r["u_s"] + r["v_s"],
                 r["n1"], r["m1"], r["d2p"], r["V2p"], r["up"], r["ell"]))

    json.dump(dict(operative=len(rows), uneg=len(un),
                   rows=[dict(n=r["n"], m=r["m"], Ms=list(r["Ms"]),
                              V={str(k): v for k, v in r["V"].items()},
                              s=r["s"], sp=r["sp"], u_s=r["u_s"], v_s=r["v_s"], ell=r["ell"],
                              n1=r["n1"], m1=str(r["m1"]), d2p=str(r["d2p"]), V2p=r["V2p"],
                              up=str(r["up"]), delta2p=str(r["dlp"][2]),
                              window=[str(x) for x in window(r["u_s"], r["v_s"])])
                         for r in un]),
              open(os.path.join(HERE, "uneg.json"), "w"), indent=1)
    print("\nwrote uneg.json")


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]) if a else 16, int(a[1]) if len(a) > 1 else 200)
