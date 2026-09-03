#!/usr/bin/env python3
"""Joint-chart design counts for the D=108 row, with the (99,66) chart as CONTROL.

The control targets are the charged design report's block counts
H=77, C2=198, C3=319, A2=1683, A3=2772, B1=594, B2=1683, total 7326.
"""
from fractions import Fraction as F
from math import gcd, lcm
import json, sys
sys.path.insert(0, "box/g108minor-20260903")
from g108_minor_driver import Row, R99, R108, FAIL, ck

OUT = {}

def block(ydeg_bound, totdeg_bound):
    """# monomials x^i y^j with j <= ydeg_bound, i+j <= totdeg_bound"""
    return sum(totdeg_bound - j + 1 for j in range(ydeg_bound+1))

def tower_chart(row):
    """Tschirnhausen approximate-root tower h3 = P (y-deg d_3)
         h2 = P^k2 + C_2 P^{k2-2} + ... + C_{k2}    (k2 = d_2/d_3)
         F  = h2^kF + A2 h2^{kF-2} + ... (kF = n/d_2);  G = h2^kG + B1 h2 + ... (kG = m/d_2)
       Coefficient blocks carry y-degree < (y-degree of the object below them)."""
    d2, d3 = row.d[2], row.d[3]
    k2, kF, kG = d2//d3, row.n//d2, row.m//d2
    blocks = {"H": block(d3-1, d3)}
    for i in range(2, k2+1):                      # h2: powers P^{k2-2}, ..., P^0
        blocks["C%d" % i] = block(d3-1, i*d3)
    for i, nm in ((2, "A2"), (kF, "A3")):
        blocks[nm] = block(d2-1, (kF-i)*d2 + (0 if i == kF else 0) or (kF-i)*d2) \
                     if False else block(d2-1, row.n - (kF-i)*d2 if False else i*d2)
    blocks["A2"] = block(d2-1, (kF-1)*d2)         # slot multiplying h2^{kF-2}: deg <= n-(kF-2)*d2
    blocks["A3"] = block(d2-1, kF*d2)
    blocks["B1"] = block(d2-1, (kG-1)*d2)
    blocks["B2"] = block(d2-1, kG*d2)
    tot = sum(blocks.values())
    monic = (row.n+1)*(row.n+2)//2 + (row.m+1)*(row.m+2)//2 - 2
    return dict(k_h2=k2, k_F=kF, k_G=kG, blocks=blocks, total=tot,
                monic_array=monic, exact=(tot == monic),
                after_fixing_tops=tot-(row.n+row.m))

print("=== CONTROL 4: tower chart block counts vs the charged (99,66) design ===")
T99 = tower_chart(R99); T108 = tower_chart(R108)
print("  (99,66) ", json.dumps(T99))
ck("(99,66) blocks == 77/198/319/1683/2772/594/1683",
   T99["blocks"] == {"H":77,"C2":198,"C3":319,"A2":1683,"A3":2772,"B1":594,"B2":1683},
   str(T99["blocks"]))
ck("(99,66) total 7326 == monic array", T99["total"] == 7326 and T99["exact"])
ck("(99,66) after fixing the two top forms == 7161", T99["after_fixing_tops"] == 7161)
print("  (108,72)", json.dumps(T108))
ck("(108,72) tower chart total == monic array (8694)",
   T108["exact"] and T108["total"] == 8694, str(T108["total"]))
OUT["tower_99"], OUT["tower_108"] = T99, T108

print("\n=== split tree, Im/IM, Thm 3.4 bookkeeping ===")
def tree(row, dl, gpackets):
    """ord g(sigma') = -(major g-roots) + (principal g-roots that separated at dl)*dl
                       + gk*delta';  final at ord g = 0."""
    maj = row.n - row.Kg()*row.us
    tot = row.Kg()*row.us
    out = []
    for gk in gpackets:
        dprime = F(maj - (tot-gk)*dl, gk)
        fk = gk*row.m//row.n
        out.append(dict(g=gk, f=int(fk), final_delta=str(dprime),
                        clears_floor=bool(dprime >= F(row.vs, row.us))))
    Im = 1 + sum(F(o["final_delta"]) - 1 for o in out)
    return out, Im

for row, dl, packs, want in ((R99, F(2), [18,9], None), (R99, F(5,2), [9,9,9], None),
                             (R108, F(3), [12,12], None)):
    t, Im = tree(row, dl, packs)
    print("  %s delta=%-4s packets %s  Im=%s" % (row.label, dl, t, Im))
    OUT["tree_%s_%s" % (row.label, dl)] = dict(packets=t, Im=str(Im))
ck("(99,66) delta=2 tree finals (3,4) and Im=6",
   [o["final_delta"] for o in tree(R99,F(2),[18,9])[0]] == ["3","4"] and tree(R99,F(2),[18,9])[1] == 6)
ck("(99,66) delta=5/2 tree finals (3,3,3) and Im=7",
   [o["final_delta"] for o in tree(R99,F(5,2),[9,9,9])[0]] == ["3","3","3"]
   and tree(R99,F(5,2),[9,9,9])[1] == 7)
t108, Im108 = tree(R108, F(3), [12,12])
ck("(108,72) delta=3 tree finals (4,4), Im=7, floor V_s/u_s=7/2 cleared",
   [o["final_delta"] for o in t108] == ["4","4"] and Im108 == 7
   and all(o["clears_floor"] for o in t108), str((t108, Im108)))

def IM(row):
    """Xu Thm 5.1 all-major evaluation: IM = n/(n+m) * (#major f-roots)*(1-delta_1)."""
    majf = row.m - row.Kf()*row.us
    return F(row.n, row.n+row.m)*majf*(1-row.delta[1])
ck("(99,66) IM = 16 (charged review)", IM(R99) == 16, str(IM(R99)))
print("  (108,72) IM = %s ; Im = %s ; Cor 5.3 (IM>=Im) %s"
      % (IM(R108), Im108, "PASS" if IM(R108) >= Im108 else "FAIL"))
ck("(108,72) Cor 5.3 passes (non-kill)", IM(R108) >= Im108)
OUT["IM_108"], OUT["Im_108"] = str(IM(R108)), str(Im108)

def thm34_gap(row, dl, k):
    """sum n_i(delta_i-1) minus the Thm 3.4 principal term."""
    majf = row.m - row.Kf()*row.us; prf = row.Kf()*row.us
    lhs = majf*k - prf*dl*(k-1) - prf
    rhs = (k-1)*(majf - prf*dl)
    return lhs - rhs
ck("(99,66) Thm 3.4 vs (4.3) gap == 30 for every k, delta",
   all(thm34_gap(R99, F(p,6), k) == 30 for p in range(7,20) for k in (2,3)))
gaps = {thm34_gap(R108, F(p,6), k) for p in range(7,22) for k in (2,)}
ck("(108,72) gap is the constant m(v_s-u_s)/d_s = 40", gaps == {40}, str(gaps))
OUT["thm34_gap_108"] = 40

print("\n=== major-weight rule (Moh (8) A_j/L_j) ===")
for row in (R99, R108):
    A = {j: row.A(j) if hasattr(row, "A") else None for j in (1,2)}
    L1 = 1
    for i in range(2, row.s+1): L1 = lcm(L1, row.delta[i].denominator)
    L2 = 1
    for i in range(3, row.s+1): L2 = lcm(L2, row.delta[i].denominator)
    A2 = (L2*row.delta[2]).denominator; A1 = (L1*row.delta[1]).denominator
    ords = (A2, A2*L1*row.delta[1])
    print("  %s  delta=(%s,%s,%s)  L=(%s,%s)  A=(A1=%s,A2=%s)  t=s^%s, ord_s(w-1)=%s"
          % (row.label, row.delta[1], row.delta[2], row.delta[3], L1, L2, A1, A2,
             ords[0], ords[1]))
    OUT["weights_"+row.label] = dict(A1=A1, A2=A2, t_exp=A2, w_exp=str(ords[1]),
                                     weight="%s*r + %s*q" % (ords[0], ords[1]))
ck("(99,66) weight rule reproduces the charged 3r+4q",
   OUT["weights_(99,66)"]["weight"] == "3*r + 4*q", OUT["weights_(99,66)"]["weight"])

print("\nFAILURES:", FAIL if FAIL else "none")
json.dump(OUT, open("box/g108minor-20260903/design.json","w"), indent=1)
sys.exit(1 if FAIL else 0)
