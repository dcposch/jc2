"""Same search as sibling_tower2 but records the witness tree."""
import sys, json, itertools
from fractions import Fraction as Q
from math import gcd
sys.path.insert(0, 'box/exact-contact-20260906')
from sibling_tower2 import split_shapes, lcm

def search(n, m, rho, kappa, W0, L, depth, cap_orbits=4):
    unit = m//gcd(n, m)
    out = {}
    key = (Q(n*rho*kappa, (n+m)*rho-m), Q(0))
    out[key] = f"FINAL-MAJOR(rho={rho},kappa={kappa},delta={1-Q((n+m)*kappa,(n+m)*rho-m)})"
    if depth == 0: return out
    step = m//gcd(rho, m); W = ((W0//step)+1)*step
    while W < n+m:
        Qdeg = int(Q(rho*W, m)); delta = 1-Q(W*kappa, W*rho-m)
        A = (L*delta).denominator
        for z, orb, parts in split_shapes(rho, unit, A, cap_orbits):
            if len(parts) > Qdeg: continue
            kj = [Q(kappa*(p*W-m), rho*W-m) for p in parts]
            if any(k == 0 for k in kj) or not any(k > 0 for k in kj): continue
            L2 = lcm(L, delta.denominator); sub = []
            for p, k in zip(parts, kj):
                if k < 0:
                    sub.append({(Q(0), -k/p): f"minor(rho={p},delta={1-k/p})"})
                else:
                    sub.append(search(n, m, p, k, W, L2, depth-1, cap_orbits))
            for combo in itertools.product(*[list(s.items()) for s in sub]):
                kk = (sum(c[0][0] for c in combo), sum(c[0][1] for c in combo))
                if kk not in out:
                    out[kk] = (f"SPLIT@W={W}(delta={delta},A={A},Q={Qdeg},z={z},"
                               f"orbits={orb})[" + " | ".join(c[1] for c in combo) + "]")
        W += step
    return out

for c in json.loads(sys.argv[1]):
    bIM, bIm = Q(c['base_IM']), Q(c['base_Im'])
    T = search(c['n'], c['m'], c['rho'], Q(c['kappa']), c['W0'], c['L'], c['depth'])
    good = sorted([(bIM+a, bIm+b, w) for (a, b), w in T.items()
                   if (bIM+a).denominator == 1 and (bIM+a) >= (bIm+b)])
    print(f"### {c['tag']}: {len(T)} outcomes, {len(good)} survivors")
    for IM, Im, w in good[:6]:
        print(f"  I_M={IM} I_m={Im}\n     {w}")
