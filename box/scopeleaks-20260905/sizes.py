#!/usr/bin/env python3
"""Price the s'>=3 residual: chart size of every u_s=1 operative receiver,
using the CHARGED compiler's own necessary inventories (B_safe, no sub-slice)."""
from __future__ import annotations
import os, sys, json, collections
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/ubuntu/jc2/box/moh14-charts-20260905")
sys.path.insert(0, HERE)
import sprime3_compiler as SC                                  # noqa: E402
from depth import operative                                    # noqa: E402
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "centre-gate-20260903")))
import moh_skeleton_full_frozen as B                           # noqa: E402


def size(n, m, Ms, V):
    S = B.Skel(n, m, list(Ms), V)
    D = SC.descend_once(S)
    if D is None:
        return None                       # u_s >= 2
    D = SC.drop_p174(D)
    if D["s"] < 2:
        return None
    P = SC.phi_eff(D)
    if P is None:
        return None
    C = SC.closed_form_sprime(D, P)
    if C["u"] < 0:
        return dict(C, unk=None, note="U-NEGATIVE", n1=D["n"], m1=D["m"], sp=D["s"])
    hm = SC.h_inventory_necessary(C)
    al = [len(SC.coeff_inventory_necessary(C, i)) for i in range(1, C["e"] + 1)]
    be = [len(SC.coeff_inventory_necessary(C, i)) for i in range(2, C["q"] + 1)]
    return dict(n1=D["n"], m1=D["m"], sp=D["s"], K=C["K"], e=C["e"], q=C["q"],
                V2=C["V2"], u=C["u"], ell=C["ell"], B=C["B"], delta1=C["delta1"],
                delta_s=C["delta_s"], nh=len(hm), unk=len(hm) + sum(al) + sum(be),
                note="")


def main():
    out = []
    for n in range(16, 201):
        for (m, Ms, V) in B.census(n, Kmin=2, full=True):
            if not operative(n, m, Ms, V):
                continue
            z = size(n, m, Ms, V)
            if z is None:
                continue
            z.update(n=n, m=m, Ms=list(Ms), V={str(k): v for k, v in V.items()})
            out.append(z)
    live = [r for r in out if r["unk"] is not None]
    uneg = [r for r in out if r["note"] == "U-NEGATIVE"]
    print("u_s=1 operative rows priced: %d  (chartable %d, U-NEGATIVE %d)"
          % (len(out), len(live), len(uneg)))
    d3 = [r for r in live if r["sp"] >= 3]
    print("chartable with s'>=3: %d" % len(d3))
    print("unknown-count quantiles (s'>=3):",
          [sorted(r["unk"] for r in d3)[int(x * (len(d3) - 1))] for x in (0, .1, .25, .5, .75, .9, 1)])
    print("\n-- 15 cheapest s'>=3 charts --")
    for r in sorted(d3, key=lambda r: r["unk"])[:15]:
        print("  unk=%-5d (n',m')=(%d,%d) s'=%d K'=%d e'=%d q'=%d V'_2=%d u'=%d ell=%d "
              "d1'=%s ds'=%s B=%s | parent (%d,%d) M=%s V=%s"
              % (r["unk"], r["n1"], r["m1"], r["sp"], r["K"], r["e"], r["q"], r["V2"],
                 r["u"], r["ell"], r["delta1"], r["delta_s"], r["B"],
                 r["n"], r["m"], r["Ms"], r["V"]))
    print("\n-- 6 cheapest s'=2 charts (the covered Appendix-II shape) --")
    for r in sorted([x for x in live if x["sp"] == 2], key=lambda r: r["unk"])[:6]:
        print("  unk=%-5d (n',m')=(%d,%d) K'=%d V'_2=%d u'=%d ell=%d | parent (%d,%d) V=%s"
              % (r["unk"], r["n1"], r["m1"], r["K"], r["V2"], r["u"], r["ell"],
                 r["n"], r["m"], r["V"]))
    json.dump(dict(priced=len(out), chartable=len(live), uneg=len(uneg),
                   rows=[{k: (str(v) if isinstance(v, F) else v) for k, v in r.items()}
                         for r in out]),
              open(os.path.join(HERE, "sizes.json"), "w"), indent=1)
    print("\nwrote sizes.json")


if __name__ == "__main__":
    main()
