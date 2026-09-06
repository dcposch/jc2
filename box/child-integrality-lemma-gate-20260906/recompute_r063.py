from fractions import Fraction as Q
from math import gcd

def prefix_gcds(n, M):
    d = {1: n}
    for i in range(1, len(M)+1):
        d[i+1] = gcd(d[i], M[i])
    return d

def def51(n, M, d, V, mult=1):
    s = len(M)
    ans = {}
    for i in range(1, s+1):
        r = Q(n - M[i], n - M[s] - 1)
        for j in range(i+1, s+1):
            r *= Q(V[j]*(n-M[j]) - d[j], V[j]*(n-M[j-1]) - d[j])
        ans[i] = mult*(1-r)
    return ans

# ---- PARENT R063
n, m = 168, 112
M = {1:-112, 2:140, 3:160, 4:166}
s = len(M)
d = prefix_gcds(n, M)
V = {2:3, 3:21, 4:3}
print("d =", d, " (d[1]=n)")
print("M_s = n-2 ?", M[s] == n-2)
delta = def51(n, M, d, V)
print("parent radii:", {i:str(delta[i]) for i in delta})
ds, vs = d[s], V[s]
us = ds - vs; ell = 2*vs - ds - 1; H = 1+ell
print(f"d_s={ds} V_s={vs} u={us} v={vs} ell={ell} H={H}")
scale = Q(us, ds)
np_, mp_ = n*scale, m*scale
print("n'=",np_," m'=",mp_)
raw_M = {i: M[i]*scale for i in range(1, s)}
print("raw_M' =", {i:str(raw_M[i]) for i in raw_M})
raw_M = {i:int(v) for i,v in raw_M.items()}
raw_d = prefix_gcds(int(np_), raw_M)
print("raw_d' =", raw_d, "  == d*scale?", raw_d == {i:int(d[i]*scale) for i in range(1,s+1)}, " raw_d[s]==u?", raw_d[s]==us)
print("dropped (M'_{s-1}==n'-1)?", raw_M[s-1] == np_-1)

print("\n=== OWN-V ROUTES (outer) ===")
Wzero = {s: Q(us)}
choices = []
for i in range(s-1, 1, -1):
    di = delta[i]; b = di.denominator
    P = Q(V[i+1]*d[i], d[i+1]); assert P.denominator==1; P=int(P)
    zero_ok = (P - V[i]) % b == 0
    nonzero_ok = di > 0 and b*V[i] <= P
    print(f" i={i}: delta={di} b={b} P={P} V_i={V[i]} zero_ok={zero_ok} (P-V_i={P-V[i]} mod {b}) nonzero_ok={nonzero_ok} (b*V_i={b*V[i]}<=P?)")
    if nonzero_ok:
        vec = {k: (Wzero[k] if k>i else Q(V[k])) for k in range(2,s)}
        choices.append((i, vec)); print(f"    -> route first_nonzero={i}, V'={ {k:str(v) for k,v in vec.items()} }")
    if zero_ok:
        Wzero[i] = Q(d[i], d[i+1])*Wzero[i+1] - di*(P - V[i])
        print(f"    W_{i} = {Wzero[i]}")
    else:
        break
print("outer routes:", len(choices))

print("\n=== CHILD RADII ===")
for j, vec in choices:
    e = delta[j]
    metric = {i: (vs - Q(us,1)/delta[i] if i>=j else vs-us-Q(us,1)/e*(1-delta[i])) for i in range(1, s)}
    print(" local inverse map:", {i:str(metric[i]) for i in metric})
    Vp = {k:int(vec[k]) for k in vec}; Vp[s] = raw_d[s]
    f = def51(int(np_), raw_M, raw_d, Vp, ell+1)
    print(" def51(child)*H:  ", {i:str(f[i]) for i in f}, " AGREE:", f==metric)
