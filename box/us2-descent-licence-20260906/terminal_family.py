"""Enumerate the child's possible TERMINAL characteristic completions at u_s>=2.

Printed inputs only:
 * Moh p.150: the characteristic sequence M_1<M_2<... is strictly increasing and
   each entry strictly drops the running gcd d_{i+1}=gcd(d_i,M_i); the sequence
   stops when the gcd reaches 1 or when the defining set is empty (M=infinity).
 * Moh Prop 6.3(2), p.197: the child's degrees are n'=u_s n/d_s, m'=u_s m/d_s and
   the retained prefix is M'_i = M_i u_s/d_s for i=1..s-1, so d'_s = u_s.
 * Moh p.174 / p.150: a characteristic exponent is < n' (the p.174 drop value is
   n'-1); M'_j <= n'-1.
No value of any V' or radius is asserted here: this is the M'-support family.
"""
import json
from fractions import Fraction as Q
from math import gcd

rows = [json.loads(l) for l in open("/tmp/jc2-lane.QdmVTB/inputs/roster.jsonl")]

def Omega(k):
    c, p = 0, 2
    while p*p <= k:
        while k % p == 0:
            k //= p; c += 1
        p += 1
    return c + (1 if k > 1 else 0)

def completions(dcur, lo, hi):
    """All strictly increasing gcd-dropping tails in (lo,hi], plus the INFINITY tail."""
    out = [("INF",)]
    if dcur == 1:
        return [()]                      # chain already complete
    for M in range(lo+1, hi+1):
        g = gcd(dcur, M)
        if g == dcur:                    # does not drop the gcd: not a char. exponent
            continue
        for tail in completions(g, M, hi):
            out.append((M,) + tail)
    return out

recs = []
for r in rows:
    src = r["source"]
    if src["u_s"] < 2:
        continue
    oc = r["own_child"]
    us = src["u_s"]
    npr, mpr = oc["n_prime"], oc["m_prime"]
    Mp = oc["M_prime"]
    dpr = oc["d_prime"]
    assert dpr[-1] == us, (r["row_id"], dpr, us)
    fam = completions(us, Mp[-1], npr-1)
    # split by shape
    inf_only = [f for f in fam if f == ("INF",)]
    finite  = [f for f in fam if f != ("INF",) and "INF" not in f]
    mixed   = [f for f in fam if f != ("INF",) and "INF" in f]
    depth   = max((len([x for x in f if x != "INF"]) for f in fam), default=0)
    # would the child be a campaign-normalised source (M'_last = n'-2)?
    norm = [f for f in fam if f and f[0] != "INF" and f[-2 if f[-1]=="INF" else -1] == npr-2]
    recs.append(dict(row=r["row_id"], u_s=us, n_prime=npr, m_prime=mpr,
                     prefix=Mp, d_prime=dpr, Omega_us=Omega(us),
                     max_extra_levels=depth, family_size=len(fam),
                     n_finite=len(finite), n_mixed=len(mixed),
                     family=[",".join(str(x) for x in f) if f else "(complete)" for f in fam],
                     admits_M_last_eq_nprime_minus_2=len(norm)))

w = "%-6s %-3s %-3s %-9s %-14s %-14s %-6s %-5s  family" % ("row","u_s","Om","np,mp","prefix Mp","dp","maxlev","|fam|")
print(w)
for c in recs:
    print(f"{c['row']:6} {c['u_s']:<3} {c['Omega_us']:<3} "
          f"{str(c['n_prime'])+','+str(c['m_prime']):9} {str(c['prefix']):14} "
          f"{str(c['d_prime']):14} {c['max_extra_levels']:<6} {c['family_size']:<5}  "
          f"{'; '.join(c['family'])}")
json.dump(recs, open("/home/ubuntu/jc2/box/us2-descent-licence-20260906/terminal_family.json","w"), indent=1)
print()
print("max family size:", max(c['family_size'] for c in recs))
print("max extra levels:", max(c['max_extra_levels'] for c in recs))
print("rows admitting M'_last = n'-2:", [c['row'] for c in recs if c['admits_M_last_eq_nprime_minus_2']])
print("total alternatives over 20 rows:", sum(c['family_size'] for c in recs))
