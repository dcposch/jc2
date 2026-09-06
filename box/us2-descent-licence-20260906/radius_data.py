"""Compute (u_s, v_s) data, the Prop 6.3 threshold v_s/u_s, the Prop 6.1 printed
floor 1, and the resulting gap window for the 20 u_s>=2 prefix rows.

Everything here is arithmetic on the FROZEN roster's necessary configuration data.
No value of delta*_{s-1} is asserted: by Moh p.191 it is a min over contact orders
of actual roots, hence not a function of the configuration.
"""
import json
from fractions import Fraction as Q
from math import gcd

IN = "/tmp/jc2-lane.QdmVTB/inputs/roster.jsonl"
rows = [json.loads(l) for l in open(IN)]

def def51_radii(n, M, d, V):
    s = len(M)
    out = {}
    for i in range(1, s+1):
        ratio = Q(n-M[i], n-M[s]-1)
        for j in range(i+1, s+1):
            ratio *= Q(V[j]*(n-M[j]) - d[j], V[j]*(n-M[j-1]) - d[j])
        out[i] = 1 - ratio
    return out

def mus(M, d):
    mu = {1: M[1]}
    for i in range(2, len(M)+1):
        mu[i] = Q(d[i-1], d[i])*mu[i-1] + M[i] - M[i-1]
    return mu

recs = []
for r in rows:
    src = r["source"]
    if src["u_s"] < 2:
        continue
    n, m, s = src["n"], src["m"], src["s"]
    M = {i+1: v for i, v in enumerate(src["M"])}
    d = {i+1: v for i, v in enumerate(src["d"])}
    V = {i+2: v for i, v in enumerate(src["V"])}   # V_2..V_s
    V[s+1] = d[s+1]
    delta = def51_radii(n, M, d, V)
    # roster's own delta (recompute-check)
    rdelta = [Q(x) if isinstance(x, str) else Q(x) for x in src["delta"]]
    assert [delta[i] for i in range(1, s+1)] == rdelta, (r["row_id"], delta, rdelta)
    us, vs = src["u_s"], src["v_s"]
    assert us + vs == d[s], (r["row_id"], us, vs, d[s])
    assert M[s] == n-2 and delta[s] == -1
    thr = Q(vs, us)
    mu = mus(M, d)
    # Prop 6.4 gcd step, evaluated at general u_s:
    degs = [Q(us*n, d[s])] + [Q(us*(-mu[i]), d[s]) for i in range(1, s)]
    assert all(x.denominator == 1 for x in degs), (r["row_id"], degs)
    g = 0
    for x in degs:
        g = gcd(g, int(x))
    # window of split radii allowed by the printed floor and the threshold
    win = []
    for den in range(1, us+1):
        num = den            # rho = num/den, rho > 1
        while Q(num, den) < thr:
            rho = Q(num, den)
            if rho > 1 and rho.denominator <= us:
                win.append(rho)
            num += 1
    win = sorted(set(win))
    sw = r["split_window"]
    recs.append(dict(row=r["row_id"], n=n, m=m, s=s, M=[M[i] for i in range(1, s+1)],
                     d=[d[i] for i in range(1, s+2)], V=[V[i] for i in range(2, s+1)],
                     u_s=us, v_s=vs, d_s=d[s], ell=src.get("ell", 2*vs-d[s]-1),
                     delta=[str(delta[i]) for i in range(1, s+1)],
                     delta_sm1_major=str(delta[s-1]),
                     threshold=str(thr), threshold_float=float(thr),
                     prop61_floor=1,
                     gcd_bound_deg_p=g,
                     leading_degrees=[int(x) for x in degs],
                     window=[str(x) for x in win],
                     roster_orders=sw.get("orders"),
                     roster_raw_pairs=sw.get("raw_pair_count"),
                     roster_killed=sw.get("killed_count"),
                     roster_leaves=sw.get("leaf_count"),
                     roster_leaf_rho=[str(l.get("rho")) for l in sw.get("leaves", [])],
                     np=r["own_child"]["n_prime"], mp=r["own_child"]["m_prime"]))

print(f"{'row':6} {'n,m':9} {'d_s':4} {'u_s':4} {'v_s':4} {'v/u':7} {'d61-1':6} "
      f"{'gcd|p|':6} {'window':34} {'ordrs':6} {'ES':3}")
for c in recs:
    print(f"{c['row']:6} {str(c['n'])+','+str(c['m']):9} {c['d_s']:<4} {c['u_s']:<4} "
          f"{c['v_s']:<4} {c['threshold']:7} {c['delta_sm1_major']:>6} "
          f"{c['gcd_bound_deg_p']:<6} {','.join(c['window']):34} "
          f"{c['roster_raw_pairs']:<6} {c['roster_leaves']}")
json.dump(recs, open("/home/ubuntu/jc2/box/us2-descent-licence-20260906/radius_data.json","w"), indent=1)
print()
print("window == roster orders on every row:",
      all(c['window'] == [str(Q(x)) for x in c['roster_orders']] for c in recs))
print("threshold > 1 on every row:", all(Q(c['threshold']) > 1 for c in recs))
print("gcd bound == u_s on every row:", all(c['gcd_bound_deg_p'] == c['u_s'] for c in recs))
