#!/usr/bin/env python3
"""s'>=3 DEPTH residual: enumerate by height, and decide whether Phi_eff ITERATES.

Phi_eff (banked 17(dd)/(y), validated 5/5 on Moh p.207):
    delta'_i = (ell+1) * Def5.1(3)(n', M', d', V', s', i).
At i = s' this collapses:  Def5.1(3)(...,s') = -1/(n'-M'_{s'}-1), so
    delta'_{s'} = -(ell+1)/(n' - M'_{s'} - 1).
Prop 6.3 (p.197) requires delta_s = -1 on its INPUT.  So a SECOND descent of the
child is licensed only if delta'_{s'} = -1, i.e.  M'_{s'} = n' - ell - 2, and
(ell = 0 gives Moh's own Cor 6.1, p.199: M'_{s'} = n'-2, a genuine smaller pair).
"""
from __future__ import annotations
import os, sys, json, collections
from fractions import Fraction as F
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "centre-gate-20260903")))
import moh_skeleton_full_frozen as B
from opus5_probe import Tree


def def51(n, M, d, V, s, i):
    num = F(n - M[i]); den = F(n - M[s] - 1)
    for j in range(i + 1, s + 1):
        num *= (V[j] * (n - M[j]) - d[j]); den *= (V[j] * (n - M[j - 1]) - d[j])
    return 1 - num / den


def operative(n, m, Ms, V):
    T = Tree(n, m, Ms, gate=False, ode=True, capacity=False, passport=False)
    T.recenter = True; T._memo = {}; T.why = []
    if not (T.d[T.s] > V[T.s] > F(T.d[T.s], 2)):
        return False
    return T.ok(T.s - 1, (V[T.s],), True, tuple(V[i] for i in range(T.s - 1, 1, -1))) is not None


def child(n, m, Ms, V):
    sk = B.Skel(n, m, list(Ms), V)
    s = sk.s; ds = sk.d[s]; vs = V[s]; us = ds - vs; ell = vs - us - 1
    sp = s - 1
    n1 = n * us // ds
    Mp = {i: F(sk.M[i] * us, ds) for i in range(1, s)}          # M'_1..M'_{s'}
    dp = {i: F(sk.d[i] * us, ds) for i in range(1, s)}
    dp[sp + 1] = F(us)                                          # gcd(d'_{s'},M'_{s'}) = u_s
    Vp = {i: V[i] for i in range(2, s)}; Vp[sp + 1] = dp[sp + 1]
    m1 = -Mp[1]
    # p.174 drop of a terminal M'_h = n'-1 (Phi_eff, 17(dd)/(y)); iterate.
    drops = 0
    while sp >= 2 and Mp[sp] == n1 - 1:
        del Mp[sp], Vp[sp + 1]
        sp -= 1; drops += 1
        Vp[sp + 1] = dp[sp + 1]
    if sp < 2:
        return dict(s=s, sp=sp, u_s=us, v_s=vs, ell=ell, n1=n1, m1=m1, Mp=Mp, dp=dp,
                    Vp=Vp, dlp={}, d2p=dp[2], V2p=V[2], up=dp[2] - V[2],
                    Mtop=None, dtop=None, second_ok=False, drops=drops, degenerate=True)
    dl = {i: (ell + 1) * def51(n1, Mp, dp, Vp, sp, i) for i in range(1, sp + 1)}
    return dict(s=s, sp=sp, u_s=us, v_s=vs, ell=ell, n1=n1, m1=m1,
                Mp=Mp, dp=dp, Vp=Vp, dlp=dl,
                d2p=dp[2], V2p=V[2], up=dp[2] - V[2],
                Mtop=Mp[sp], dtop=dl[sp],
                second_ok=(dl[sp] == -1), drops=drops, degenerate=False)


def main(nlo=16, nhi=200):
    rows = []
    for n in range(nlo, nhi + 1):
        for (m, Ms, V) in B.census(n, Kmin=2, full=True):
            if not operative(n, m, Ms, V):
                continue
            c = child(n, m, Ms, V); c.update(n=n, m=m, Ms=tuple(Ms), V=dict(V))
            rows.append(c)
    print("operative rows %d" % len(rows))

    def H(rs, k):
        return dict(sorted(collections.Counter(k(r) for r in rs).items()))

    print("\n-- DEPTH: operative residue by descended height s' --")
    print("  by s'                :", H(rows, lambda r: r["sp"]))
    d3 = [r for r in rows if r["sp"] >= 3]
    print("  s'>=3                : %d rows, %d degree pairs, %d distinct (n',m',ell)"
          % (len(d3), len({(r["n"], r["m"]) for r in d3}),
             len({(r["n1"], r["m1"], r["ell"]) for r in d3})))
    print("  s'>=4                : %d rows" % len([r for r in rows if r["sp"] >= 4]))
    print("  s'>=3 by (s',u_s)    :", H(d3, lambda r: (r["sp"], r["u_s"])))
    print("  s'>=3 by ell         :", H(d3, lambda r: r["ell"]))
    print("  s'>=3 by sign(u')    :", H(d3, lambda r: "u'<0" if r["up"] < 0 else
                                        ("u'=0" if r["up"] == 0 else "u'>0")))

    print("\n-- SECOND DESCENT: is delta'_{s'} = -1 on the child? --")
    print("  delta'_{s'} = -1 count:", H(rows, lambda r: r["second_ok"]))
    print("  ell = 0 count         :", H(rows, lambda r: r["ell"] == 0))
    print("  ell=0 AND M'_{s'}=n'-2:", len([r for r in rows if r["ell"] == 0
                                            and r["Mtop"] == r["n1"] - 2]))
    print("  delta'_{s'} values (top 12):",
          dict(list(H(rows, lambda r: str(r["dtop"])).items())[:12]))
    so = [r for r in rows if r["second_ok"]]
    print("  rows admitting a SECOND Prop 6.3 descent: %d" % len(so))
    for r in so[:20]:
        print("     n=%d m=%d M=%s V=%s s=%d ell=%d (n',m')=(%d,%d) M'_{s'}=%s"
              % (r["n"], r["m"], list(r["Ms"]), r["V"], r["s"], r["ell"],
                 r["n1"], r["m1"], r["Mtop"]))

    print("\n-- delta'_2 = -1 (two-point leading form licensed at level 2 of the child)? --")
    print("  delta'_2 == -1:", H(rows, lambda r: r["dlp"][2] == -1))
    print("  delta'_2 == -1 among s'>=3:", H(d3, lambda r: r["dlp"][2] == -1))

    smallest = sorted(d3, key=lambda r: (r["n1"] + r["m1"], r["n1"], r["m1"], r["ell"]))[:12]
    print("\n-- smallest s'>=3 descended receivers (n',m'; M'; ell; V'_2; u') --")
    for r in smallest:
        print("   (%d,%d) parent (%d,%d) M'=%s ell=%d s'=%d V'_2=%d u'=%s d'_2=%s"
              % (r["n1"], r["m1"], r["n"], r["m"], [str(r["Mp"][i]) for i in range(2, r["sp"] + 1)],
                 r["ell"], r["sp"], r["V2p"], r["up"], r["d2p"]))

    def ser(r):
        return dict(n=r["n"], m=r["m"], Ms=list(r["Ms"]), V={str(k): v for k, v in r["V"].items()},
                    s=r["s"], sp=r["sp"], u_s=r["u_s"], v_s=r["v_s"], ell=r["ell"],
                    n1=r["n1"], m1=str(r["m1"]),
                    Mp=[str(r["Mp"][i]) for i in range(1, r["sp"] + 1)],
                    Vp={str(k): str(v) for k, v in r["Vp"].items()},
                    dlp={str(k): str(v) for k, v in r["dlp"].items()},
                    d2p=str(r["d2p"]), up=str(r["up"]), second_ok=r["second_ok"])
    json.dump(dict(operative=len(rows), by_sp=H(rows, lambda r: r["sp"]),
                   second_descent=len(so), rows=[ser(r) for r in rows]),
              open(os.path.join(HERE, "depth.json"), "w"), indent=1)
    print("\nwrote depth.json")


if __name__ == "__main__":
    a = sys.argv[1:]
    main(int(a[0]) if a else 16, int(a[1]) if len(a) > 1 else 200)
