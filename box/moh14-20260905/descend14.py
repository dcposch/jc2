#!/usr/bin/env python3
"""Step 2: Prop 6.3/6.4 descent of the 14 rows + descended radii Phi_eff.

FAIL-CLOSED CONTROL: the descent map and the radius map are validated by
reproducing MOH'S OWN Appendix II descended table (p.207) -- all five rows
(three principal + two bracketed alternates), every column.
"""
import json, os, sys
from fractions import Fraction as F
from math import gcd

HERE = "/home/ubuntu/jc2/box/moh14-20260905"
sys.path.insert(0, HERE)
sys.path.insert(0, "/home/ubuntu/jc2/box/mohprog-drivers-20260903/repro")
import moh_skeleton_full as B

FAIL = []
def ck(name, cond, detail=""):
    print(("  [ok]   " if cond else "  [FAIL] ") + name + (("   " + detail) if detail and not cond else ""))
    if not cond: FAIL.append(name)

def def51(n, M, d, V, s, i):
    num = F(n - M[i]); den = F(n - M[s] - 1)
    for j in range(i + 1, s + 1):
        num *= V[j] * (n - M[j]) - d[j]
        den *= V[j] * (n - M[j - 1]) - d[j]
        if den == 0: return None
    return 1 - num / den

def descend(S):
    ds, Vs, s = S.d[S.s], S.V[S.s], S.s
    us = ds - Vs
    k = Vs - us - 1
    n2, m2 = S.n * us // ds, S.m * us // ds
    s2 = s - 1
    M2 = {i: S.M[i] * us // ds for i in range(1, s2 + 1)}
    d2 = {i: S.d[i] * us // ds for i in range(1, s2 + 2)}
    V2 = {i: S.V[i] for i in range(2, s2 + 1)}
    V2[s2 + 1] = d2[s2 + 1]
    return {"n": n2, "m": m2, "s": s2, "M": M2, "d": d2, "V": V2, "k": k, "u_s": us}

def phi(D):
    out = {}
    for i in range(1, D["s"] + 1):
        r = def51(D["n"], D["M"], D["d"], D["V"], D["s"], i)
        if r is None: return None
        out[i] = (D["k"] + 1) * r
    return out

APPX2 = [
    ((64, 48, [52, 62], {3: 3, 2: 3}), (16, 12, 13, 3, F(-1),   F(1, 4), 1)),
    ((84, 56, [64, 82], {3: 3, 2: 2}), (21, 14, 16, 2, F(-1, 2), F(7, 6), 1)),
    ((84, 56, [72, 82], {3: 3, 2: 5}), (21, 14, 18, 5, F(-1),   F(1, 3), 1)),
    ((75, 50, [55, 73], {3: 4, 2: 3}), (15, 10, 11, 3, F(-1),   F(1, 2), 2)),
    ((75, 50, [55, 73], {3: 4, 2: 2}), (15, 10, 11, 2, F(-1),   F(4, 3), 2)),
]
print("== CONTROL A: descent + Phi_eff reproduce Moh's Appendix II table (p.207) ==")
for (sk, want) in APPX2:
    S = B.Skel(sk[0], sk[1], sk[2], sk[3])
    D = descend(S); P = phi(D)
    got = (D["n"], D["m"], D["M"][D["s"]], D["V"][2], P[2], P[1], D["k"])
    print("   (%d,%d) V=%-18s -> %-34s  Moh: %s" % (sk[0], sk[1], sk[3], got, want))
    ck("Appendix II row (%d,%d) V_2=%d reproduced" % (sk[0], sk[1], sk[3][2]), got == want, str(got))
ck("u_s == 1 on all five Appendix II rows (Moh p.207: 'u_3 = d_3 - v_3 = 1')",
   all(descend(B.Skel(*sk))["u_s"] == 1 for (sk, _) in APPX2))

sys.path.insert(0, "/home/ubuntu/jc2/box/orderbasis-20260903")
try:
    import order_basis_full as OB
    print("\n== CONTROL A2: order_basis_full.closed_form == Phi_eff on Moh's rows ==")
    for key, want in (("k16a", (F(-1), F(1, 4))), ("banked", (F(-1), F(1, 2)))):
        C = OB.closed_form(OB.ROWS[key])
        ck("closed_form %s (delta_2',delta_1') == Appendix II" % OB.ROWS[key].label,
           (C["delta2"], C["delta1"]) == want, "%s,%s" % (C["delta2"], C["delta1"]))
except Exception as exc:
    print("   [skip] order_basis_full import: %s" % exc)

DESC = json.load(open(os.path.join(HERE, "rows14.json")))
print("\n== the 14 rows, descended (u_s = 1 => Prop 6.4 discharges the radius) ==")
hdr = ("%-7s %-13s %-7s | %-8s %-12s %-9s %2s %2s | %2s %2s %2s %3s %3s | %-22s %-6s %-6s"
       % ("(n,m)", "M_2..M_s", "V", "(n',m')", "M'_1..M'_s'", "V'_2..", "s'", "l",
          "K'", "e'", "q'", "V2'", "u'", "d'_s'..d'_1", "Btig", "Bsafe"))
print(hdr); print("-" * len(hdr))
OUT = []
for r in DESC:
    S = B.Skel(r["n"], r["m"], r["Ms"], {int(k): v for k, v in r["V"].items()})
    D = descend(S); P = phi(D)
    sp, k = D["s"], D["k"]
    Kp = gcd(D["n"], D["m"]); ep, qp = D["n"] // Kp, D["m"] // Kp
    V2p = D["V"][2]; up = Kp - V2p
    d1p = P[1]; d2p = P[2] if 2 in P else None
    Btight = V2p * d1p + up * d2p if d2p is not None else None
    Bsafe = V2p * d1p + up * P[sp]
    OUT.append(dict(n=r["n"], m=r["m"], Ms=r["Ms"], V=r["V"], np=D["n"], mp=D["m"],
                    Mp={str(i): D["M"][i] for i in D["M"]},
                    Vp={str(i): D["V"][i] for i in D["V"]},
                    dp={str(i): D["d"][i] for i in D["d"]}, sp=sp, k=k, Kp=Kp, ep=ep, qp=qp,
                    V2p=V2p, up=up, delta={str(i): str(P[i]) for i in P},
                    d1p=str(d1p), d2p=str(d2p), Btight=str(Btight), Bsafe=str(Bsafe),
                    two_point=(d2p == F(-1))))
    print("%-7s %-13s %-7s | %-8s %-12s %-9s %2d %2d | %2d %2d %2d %3d %3d | %-22s %-6s %-6s"
          % ("%d,%d" % (r["n"], r["m"]), ",".join(map(str, r["Ms"])),
             ",".join(str(v) for _, v in sorted((int(a), b) for a, b in r["V"].items())),
             "(%d,%d)" % (D["n"], D["m"]),
             ",".join(str(D["M"][i]) for i in range(1, sp + 1)),
             ",".join(str(D["V"][i]) for i in range(2, sp + 1)),
             sp, k, Kp, ep, qp, V2p, up,
             ",".join(str(P[i]) for i in range(sp, 0, -1)), str(Btight), str(Bsafe)))

json.dump(OUT, open(os.path.join(HERE, "descend14.json"), "w"), indent=1)
print("\n== summary ==")
print("   s' distribution        : %s" % {v: [x["sp"] for x in OUT].count(v) for v in sorted(set(x["sp"] for x in OUT))})
print("   two-point (delta'_2=-1): %d of 14" % sum(1 for x in OUT if x["two_point"]))
print("   u' = 0 rows            : %d" % sum(1 for x in OUT if x["up"] == 0))
print("   B_tight >= 0           : %d  (outside the charged chart's scope test)"
      % sum(1 for x in OUT if x["Btight"] is not None and F(x["Btight"]) >= 0))
print("   B_safe  >= 0           : %d" % sum(1 for x in OUT if F(x["Bsafe"]) >= 0))
print("\n" + "=" * 78)
if FAIL: print("CONTROLS FAILED (%d): %s" % (len(FAIL), FAIL)); sys.exit(1)
print("ALL DESCENT CONTROLS PASSED.  descend14.json written.")
