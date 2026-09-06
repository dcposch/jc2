"""Full child terminal family: M'-tail  x  Def 5.1(2)-admissible V' at the new levels.

Printed conditions used, and nothing else:
  (T1) p.150 : M' strictly increasing, each entry strictly drops the running gcd,
       chain stops at gcd 1 or at M'=infinity; M' <= n'-1.
  (T2) Prop 6.3(2) p.197 : n',m' and the prefix M'_1..M'_{s-1}, so d'_s = u_s.
  (T3) Def 5.1(2) p.179 : V'_{i+1} d'_i/d'_{i+1} >= V'_i > d'_i/(n'-M'_i), V' a
       positive integer, with the truncation convention V'_{s'+1} = d'_{s'+1}.
The retained prefix multiplicities V'_2..V'_{s'} are the frozen roster's own_child.
"""
import json
from fractions import Fraction as Q
from math import gcd

rows = [json.loads(l) for l in open("/tmp/jc2-lane.QdmVTB/inputs/roster.jsonl")]

def tails(dcur, lo, hi):
    out = [("INF",)]
    if dcur == 1:
        return [()]
    for M in range(lo+1, hi+1):
        g = gcd(dcur, M)
        if g == dcur:
            continue
        for t in tails(g, M, hi):
            out.append((M,) + t)
    return out

recs = []
for r in rows:
    src = r["source"]
    if src["u_s"] < 2:
        continue
    oc = r["own_child"]
    us, npr = src["u_s"], oc["n_prime"]
    Mpref = list(oc["M_prime"])                  # M'_1 .. M'_{s'}
    Vpref = list(oc["V_prime"])                  # V'_2 .. V'_{s'}
    sols = []
    for t in tails(us, Mpref[-1], npr-1):
        tail = [x for x in t if x != "INF"]
        M = {i+1: v for i, v in enumerate(Mpref + tail)}
        S = len(M)
        d = {1: npr}
        for i in range(1, S+1):
            d[i+1] = gcd(d[i], abs(M[i]))
        # V'_2..V'_{s'} fixed by the prefix; new levels free, V'_{S+1}=d_{S+1}
        base = {i+2: v for i, v in enumerate(Vpref)}
        free = [i for i in range(2, S+1) if i not in base]
        def rec(j, V):
            if j < 2:
                sols.append((t, tuple(V[i] for i in range(2, S+1))))
                return
            lo = Q(d[j], npr - M[j])             # strict lower bound
            hi = Q(V[j+1]*d[j], d[j+1])          # inclusive upper bound
            cand = [base[j]] if j in base else list(range(1, int(hi)+1))
            for v in cand:
                if Q(v) > lo and Q(v) <= hi:
                    V[j] = v
                    rec(j-1, V)
                    del V[j]
        rec(S, {S+1: d[S+1]})
    recs.append(dict(row=r["row_id"], u_s=us, n_prime=npr, m_prime=oc["m_prime"],
                     prefix_M=Mpref, prefix_V=Vpref,
                     n_M_tails=len(tails(us, Mpref[-1], npr-1)),
                     n_full=len(sols),
                     full=[",".join(str(x) for x in t) + " | V'=" + ",".join(map(str,v))
                           for t, v in sols]))

print("%-6s %-3s %-9s %-7s %-7s  full family (M'-tail | V' at levels 2..s')" %
      ("row","u_s","np,mp","#tails","#full"))
for c in recs:
    print("%-6s %-3s %-9s %-7s %-7s  %s" % (c['row'], c['u_s'],
          f"{c['n_prime']},{c['m_prime']}", c['n_M_tails'], c['n_full'],
          "; ".join(c['full'])))
json.dump(recs, open("/home/ubuntu/jc2/box/us2-descent-licence-20260906/terminal_full.json","w"), indent=1)
print()
print("total full alternatives:", sum(c['n_full'] for c in recs))
print("max per row:", max(c['n_full'] for c in recs))
print("rows with zero admissible completion:", [c['row'] for c in recs if c['n_full']==0])
