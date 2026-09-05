#!/usr/bin/env python3
"""Controls for the U-NEGATIVE reading + the exact residual partition."""
from __future__ import annotations
import os, sys, collections
from fractions import Fraction as F
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/ubuntu/jc2/box/moh14-charts-20260905")
sys.path.insert(0, HERE)
import sprime3_compiler as SC
from depth import operative, child
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "centre-gate-20260903")))
import moh_skeleton_full_frozen as B

FAIL = []
def ck(name, cond, detail=""):
    print(("  [ok]   " if cond else "  [FAIL] ") + name + (("   " + detail) if detail else ""))
    if not cond: FAIL.append(name)

print("== CONTROL P: no false kill on Moh's own printed rows (p.202 -> p.207) ==")
for (n, m, Ms, V, lab, _p2, _p1, _e) in B.MOH_TABLE:
    S = B.Skel(n, m, list(Ms), V)
    D = SC.descend_once(S)
    if D is None:
        print("   %-24s u_s=%d != 1, Prop 6.4 not applicable (Moh skips it)"
              % (lab, S.d[S.s] - S.V[S.s])); continue
    K = gcd(D["n"], D["m"]); u = K - D["V"][2]
    ck("%-24s (n',m')=(%d,%d) K'=%d V'_2=%d u'=%d >= 0"
       % (lab, D["n"], D["m"], K, D["V"][2], u), u >= 0)

print("\n== CONTROL Q: the 12 charged n<=100 receiver rows have u' >= 0 ==")
cnt = collections.Counter()
for n in range(16, 101):
    for (m, Ms, V) in B.census(n, Kmin=2, full=True):
        if not operative(n, m, Ms, V): continue
        S = B.Skel(n, m, list(Ms), V); D = SC.descend_once(S)
        if D is None: cnt["u_s>=2"] += 1; continue
        D = SC.drop_p174(D); K = gcd(D["n"], D["m"])
        cnt["u'<0" if K - D["V"][2] < 0 else ("u'=0" if K == D["V"][2] else "u'>0")] += 1
ck("n<=100 operative rows: no u'<0", cnt["u'<0"] == 0, str(dict(cnt)))

print("\n== the exact residual partition of the 1420 operative rows (16<=n<=200) ==")
part = collections.Counter(); rows = []
for n in range(16, 201):
    for (m, Ms, V) in B.census(n, Kmin=2, full=True):
        if not operative(n, m, Ms, V): continue
        S = B.Skel(n, m, list(Ms), V); us = S.d[S.s] - S.V[S.s]
        c = child(n, m, Ms, V); up = c["up"]
        if us == 1:
            key = ("A U-NEG u_s=1 (descent forced, datum degenerate)" if up < 0 else
                   ("D s'=2 Appendix II covered" if c["sp"] == 2 else
                    "C s'>=3 Phi_eff receiver (compute-bound)"))
        else:
            key = ("B U-NEG u_s>=2 (radius dichotomy)" if up < 0 else
                   "E u_s>=2 non-U-NEG (radius dichotomy first)")
        part[key] += 1; rows.append((key, n, m, us, c["sp"], up))
tot = 0
for k in sorted(part):
    print("   %-52s %5d" % (k, part[k])); tot += part[k]
ck("partition totals 1420", tot == 1420, str(tot))

print("\n== B-family split windows ==")
def window(u_s, v_s):
    hi = F(v_s, u_s); out = set()
    for q in range(1, u_s + 1):
        p = q + 1
        while F(p, q) < hi:
            d = F(p, q)
            if d > 1 and d.denominator <= u_s: out.add(d)
            p += 1
    return sorted(out)
emptyw = 0; nonempty = []
for (k, n, m, us, sp, up) in rows:
    if not k.startswith("B"): continue
    for (mm, Ms, V) in B.census(n, Kmin=2, full=True):
        if mm != m: continue
        S = B.Skel(n, m, list(Ms), V)
        if S.d[S.s] - S.V[S.s] != us or child(n, m, Ms, V)["up"] != up: continue
        w = window(us, S.V[S.s])
        if not w: emptyw += 1
        else: nonempty.append((n, m, list(Ms), dict(V), [str(x) for x in w]))
        break
print("   B rows with EMPTY split window (=> (R) forced, descent unconditional):", emptyw)
print("   B rows with a non-empty window:", len(nonempty))
for r in nonempty: print("     ", r)

print("\nFAILURES:", FAIL if FAIL else "none")
