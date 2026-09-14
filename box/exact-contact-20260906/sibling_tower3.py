"""sibling_tower2 + CROSS-TOWER CONSISTENCY.

Moh d_i = gcd(n, M_1,...,M_{i-1}) is the gcd of n with the exponents STRICTLY
DEEPER than D_i, and Prop 4.6(1)/Def 5.1(4) fix the pattern at D_i by
g_sigma = p^{n/d_i}, deg p = V_{i+1} d_i/d_{i+1}.  A sibling sub-tower that
inserts a new exponent M below an ancestor disc D changes that ancestor's
d to gcd(d_D, M).  The ancestor's pattern degree is already fixed by the row,
so consistency forces  d_D | M  for every ancestor D.  With W = n - M this is
W == n (mod d_D).  Additionally the split multiplicities r_j = rho_j/(m/d)
must be coprime as a set (else d was not the true reduction divisor).
"""
from fractions import Fraction as Q
from math import gcd
from functools import reduce
import sys, itertools, json
sys.path.insert(0, 'box/exact-contact-20260906')
from sibling_tower2 import orbit_parts, lcm

def shapes(rho, unit, A, cap):
    out = []
    for z in range(0, rho+1, unit):
        rest = rho-z
        if rest % A: continue
        per = rest//A
        if per == 0: continue
        for orb in orbit_parts(per, unit, cap):
            parts = ([z] if z > 0 else [])+[r for r in orb for _ in range(A)]
            if len(parts) < 2: continue
            rs = [p//unit for p in parts]
            if reduce(gcd, rs) != 1: continue       # d is the true divisor
            out.append((z, tuple(orb), tuple(parts)))
    return out

def search(n, m, rho, kappa, W0, L, dcur, depth, cap=4, trace=False):
    unit = m//dcur
    res = {}
    dfin = 1-Q((n+m)*kappa, (n+m)*rho-m)
    Afin = (L*dfin).denominator
    rgo = Q(n*rho, m)
    if rho % Afin in (0, 1) and rgo.denominator == 1 and int(rgo) % Afin in (0, 1):
        res[(Q(n*rho*kappa, (n+m)*rho-m), Q(0))] = f"FINAL(rho={rho},delta={dfin},A={Afin})"
    if depth == 0: return res
    step = m//gcd(rho, m)
    lcmstep = step*dcur//gcd(step, dcur)
    W = W0+1
    while W < n+m:
        if (n-W) % dcur or Q(rho*W, m).denominator != 1:
            W += 1; continue
        Qd = int(Q(rho*W, m)); delta = 1-Q(W*kappa, W*rho-m)
        A = (L*delta).denominator
        for z, orb, parts in shapes(rho, unit, A, cap):
            if len(parts) > Qd: continue
            kj = [Q(kappa*(p*W-m), rho*W-m) for p in parts]
            if any(k == 0 for k in kj) or not any(k > 0 for k in kj): continue
            L2 = lcm(L, delta.denominator); sub = []
            for p, k in zip(parts, kj):
                sub.append({(Q(0), -k/p): f"minor(rho={p},d={1-k/p})"} if k < 0
                           else search(n, m, p, k, W, L2, dcur, depth-1, cap, trace))
            if any(not s for s in sub): continue
            for combo in itertools.product(*[list(s.items()) for s in sub]):
                key = (sum(c[0][0] for c in combo), sum(c[0][1] for c in combo))
                res.setdefault(key, f"SPLIT@W={W}(M={n-W},delta={delta},A={A},z={z},"
                               f"orb={orb})[" + " | ".join(c[1] for c in combo) + "]")
        W += 1
    return res

if __name__ == '__main__':
  for c in json.loads(sys.argv[1]):
      bIM, bIm = Q(c['base_IM']), Q(c['base_Im'])
      for depth in c['depths']:
          T = search(c['n'], c['m'], c['rho'], Q(c['kappa']), c['W0'], c['L'],
                     c['dcur'], depth, c.get('cap', 4))
          good = sorted([(bIM+a, bIm+b, w) for (a, b), w in T.items()
                         if (bIM+a).denominator == 1 and (bIM+a) >= (bIm+b)])
          print(f"{c['tag']} depth={depth}: {len(T)} outcomes, {len(good)} survivors")
          for IM, Im, w in good[:5]: print(f"   I_M={IM} I_m={Im}  {w[:200]}")
          sys.stdout.flush()
  