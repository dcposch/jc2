#!/usr/bin/env python3
"""Ladder law test: pivot coefficient of the Jacobian w-band rows.

Claim (derived):  c(p,k) = n*[A*(e+f) - 1 - k] - e*A*p   up to sign,
where A = y-multiplicity of the top form of the approximate root K2,
      e = n/K, f = m/K, K = d_2 = deg K2, p = t-power of the band,
      k = w-power index of the row, and the family starts at k0=(e+1)A-1.
Equivalently in the driver's naming D = n+m-2-p:  c = e*A*D - n*k - r0,
r0 = e*A*(n+m-2) - n*(A*(e+f)-1).
"""
import json, sys
from fractions import Fraction as Fr

n, m, K, A = 99, 66, 33, 9
e, f = n // K, m // K
B = K - A
k0 = (e + 1) * A - 1
tot = n + m - 2

def claw(p, k):
    return n * (A * (e + f) - 1 - k) - e * A * p

r0 = e*A*tot - n*(A*(e+f)-1)
print("datum  n=%d m=%d K=%d A=%d B=%d e=%d f=%d  k0=%d  totdeg=%d" % (n,m,K,A,B,e,f,k0,tot))
print("law    c(p,k) = %d*(%d - k) - %d*p        [= %d*D - %d*k - %d]" %
      (n, A*(e+f)-1, e*A, e*A, n, r0))
print("c(p,k0) = A*n*(f-1) - e*A*p = %d - %d*p" % (A*n*(f-1), e*A))

led = {}
for src in ("stage4.json", "stage7.json"):
    d = json.load(open("/tmp/jc2-lane.boT2Oz/inputs/" + src))
    for pv in d["joint_elimination"]["pivot_ledger"]:
        led[(pv["row"], pv["variable"])] = Fr(pv["coefficient"])
# stage 8 pivots from the charged gate report / stage8-summary
s8 = [("stage8_J_d155_k%d" % k, "B1c_7_%d" % (k - 16), v) for k, v in
      zip(range(35, 42), (675, 576, 477, 378, 279, 180, 81))]
for lab, var, v in s8:
    led[(lab, var)] = Fr(v)

bad = ok = 0
rows = []
for (lab, var), val in sorted(led.items()):
    if "_J_d" not in lab:
        continue
    D = int(lab.split("_J_d")[1].split("_k")[0]); k = int(lab.split("_k")[1])
    p = tot - D
    pred = claw(p, k)
    Q = int(var.split("_")[2])
    sgn = (-1) ** (Q - k)
    match = (abs(val) == abs(pred)) and (val == sgn * pred)
    rows.append((D, k, p, Q, int(val), pred, sgn, match))
    ok += match; bad += (not match)
rows.sort()
print("\n  D    k   p   Q      actual     |law|   sign(-1)^(Q-k)   match")
for D,k,p,Q,val,pred,sgn,match in rows:
    print("  %3d %3d %3d %3d  %10d %9d   %+d              %s" %
          (D,k,p,Q,val,pred,sgn,"OK" if match else "FAIL"))
print("\nJacobian ladder entries matched: %d / %d" % (ok, ok+bad))

# ladder termination: largest k with c(p,k) > 0
print("\nladder termination test  (predicted last k = floor((A*(e+f)-1) - e*A*p/n))")
for p in range(1, 9):
    D = tot - p
    ks = sorted(k for (DD,k,_,_,_,_,_,_) in rows if DD == D)
    if not ks: continue
    kmax_pred = (n*(A*(e+f)-1) - e*A*p) // n
    while claw(p, kmax_pred) <= 0: kmax_pred -= 1
    print("  p=%d D=%d  observed k range %d..%d   predicted last k=%d   %s" %
          (p, D, ks[0], ks[-1], kmax_pred, "OK" if ks[-1]==kmax_pred and ks[0]==k0 else "FAIL"))
