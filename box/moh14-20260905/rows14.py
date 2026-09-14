#!/usr/bin/env python3
"""Step 1+2: enumerate the 14 EXCESS u_s=1 rows at n<=100 and descend them
(Moh Prop 6.3/6.4).  Fail-closed: the 14 are re-derived from the CHARGED
moh_skeleton_full.py census (1)-(13) intersected with the charged operative
POLY+ODE screen artifact; both halves must agree.
"""
import json, ast, os, sys
from fractions import Fraction as F
from math import gcd

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "mohprog-drivers-20260903", "repro"))
import moh_skeleton_full as B     # the CHARGED copy (sha-verified)

AUDIT = os.path.join(os.path.dirname(HERE), "mohprog-drivers-20260903",
                     "full-tree-polynomial-ode-n100-audit.json")

FAIL = []
def ck(name, cond, detail=""):
    print(("  [ok]   " if cond else "  [FAIL] ") + name + ("   " + detail if detail and not cond else ""))
    if not cond: FAIL.append(name)

# ---------- half A: the charged screen artifact --------------------------
d = json.load(open(AUDIT))
surv = [r for r in d["rows"] if r["group_feasible"] and r["selected_path_embeds"]]
ck("screen artifact: survivors == 20", len(surv) == 20, str(len(surv)))
ck("screen artifact header: survivors=20 excess=14 printed_killed=0",
   d["survivors"] == 20 and d["excess_survivors"] == 14 and d["printed_rows_killed"] == 0)
excess = [ast.literal_eval(r["row_key"]) for r in surv if not r["is_printed"]]
ck("screen artifact: excess == 14", len(excess) == 14, str(len(excess)))

# ---------- half B: independent (1)-(13) census from the charged instrument
cens = set()
for n in (90, 96):
    for (m, Ms, V) in B.census(n, Kmin=2, full=True):
        cens.add((n, m, tuple(Ms), tuple(sorted(V.items()))))
norm = set((n, m, tuple(Ms), tuple(sorted(tuple(t) for t in V))) for (n, m, Ms, V) in excess)
ck("all 14 excess rows are (1)-(13)-admissible in the charged census",
   norm <= cens, str(sorted(norm - cens)))

# ---------- the 14 rows, with M, d, V, s, u_s, and the Prop 6.3/6.4 descent
print("\n== the 14 EXCESS rows: skeleton data and Prop 6.3/6.4 descent ==")
hdr = ("%-8s %-20s %-16s %-22s %2s %3s %3s %3s | %-9s %-16s %-12s %2s %s"
       % ("(n,m)", "M_2..M_s", "V_2..V_s", "d_1..d_{s+1}", "s", "d_s", "v_s", "u_s",
          "(n',m')", "M'_2..M'_{s-1}", "V'", "l", "K'"))
print(hdr); print("   " + "-" * (len(hdr) - 3))

DESC = []
for (n, m, Ms, Vt) in sorted(excess):
    V = {i: v for (i, v) in Vt}
    S = B.Skel(n, m, list(Ms), V)
    s = S.s
    ds = S.d[s]; vs = S.V[s]; us = ds - vs
    # Moh Prop 6.3(2): pi-degrees u_s n/d_s and u_s(-mu_1)/d_s = u_s m/d_s
    assert (n * us) % ds == 0 and (m * us) % ds == 0
    np_, mp_ = n * us // ds, m * us // ds
    Mp = []
    ok_int = True
    for i in range(2, s):                       # middles only; M_s = n-2 is consumed
        num = S.M[i] * us
        if num % ds: ok_int = False
        Mp.append(F(num, ds))
    ell = vs - us - 1                           # Prop 6.3(3) exponent (ERRATUM 17(dddddd))
    Vp = {i: S.V[i] for i in range(2, s)}
    Kp = gcd(np_, mp_)
    DESC.append(dict(n=n, m=m, Ms=list(Ms), V={i: S.V[i] for i in range(2, s + 1)},
                     d={i: S.d[i] for i in range(1, s + 2)}, s=s, ds=ds, vs=vs, us=us,
                     np=np_, mp=mp_, Mp=[int(x) for x in Mp], Vp=Vp, ell=ell, Kp=Kp,
                     delta={i: str(S.delta[i]) for i in range(1, s + 1)},
                     ok_int=ok_int))
    print("   %-8s %-20s %-16s %-22s %2d %3d %3d %3d | %-9s %-16s %-12s %2d %d"
          % ("%d,%d" % (n, m), ",".join(map(str, Ms)),
             ",".join(str(S.V[i]) for i in range(2, s + 1)),
             ",".join(str(S.d[i]) for i in range(1, s + 2)), s, ds, vs, us,
             "(%d,%d)" % (np_, mp_), ",".join(str(int(x)) for x in Mp),
             ",".join(str(Vp[i]) for i in sorted(Vp)), ell, Kp))

ck("u_s == 1 on all 14 (Prop 6.4 radius-automatic, 17(gggggg))",
   all(r["us"] == 1 for r in DESC), str(sorted(set(r["us"] for r in DESC))))
ck("all descended M' are integers", all(r["ok_int"] for r in DESC))
ck("class counts (90,60)x4 (96,64)x4 (96,72)x6",
   sorted((r["n"], r["m"]) for r in DESC).count((90, 60)) == 4
   and sorted((r["n"], r["m"]) for r in DESC).count((96, 64)) == 4
   and sorted((r["n"], r["m"]) for r in DESC).count((96, 72)) == 6)
ck("delta_s == -1 on all 14 (Prop 6.3 hypothesis)",
   all(r["delta"][r["s"]] == "-1" for r in DESC))

# ---------- descended classes (Opus (K,ell) lattice, 17(eeeeee)) ---------
print("\n== descended classes: (n', m', M', ell) with the V' fibre ==")
cl = {}
for r in DESC:
    key = (r["np"], r["mp"], tuple(r["Mp"]), r["ell"])
    cl.setdefault(key, []).append(tuple(r["Vp"][i] for i in sorted(r["Vp"])))
for k in sorted(cl):
    print("   (n',m')=(%d,%d)  M'=%-10s  l=%d  K'=%d  e'=%d q'=%d  |  V' fibre %s   [%d rows]"
          % (k[0], k[1], ",".join(map(str, k[2])), k[3], gcd(k[0], k[1]),
             k[0] // gcd(k[0], k[1]), k[1] // gcd(k[0], k[1]), sorted(cl[k]), len(cl[k])))
print("   distinct descended classes: %d  (from 14 rows)" % len(cl))

json.dump(DESC, open(os.path.join(HERE, "rows14.json"), "w"), indent=1)
print("\n" + "=" * 78)
if FAIL:
    print("CONTROLS FAILED (%d): %s" % (len(FAIL), FAIL)); sys.exit(1)
print("ALL ROW-ENUMERATION CONTROLS PASSED.  rows14.json written.")
