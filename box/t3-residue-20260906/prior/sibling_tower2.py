"""Sibling MAJOR sub-tower search WITH the Galois orbit-size law.

State of a major packet: (rho, kappa, W0, L) where
  rho    = #roots of the deg-m polynomial in it,
  kappa  = rho*(1-delta_zero)  (invariant while the packet does not split),
  W0     = the tower parameter n-M at which the packet was born,
  L      = lcm of the reduced denominators of the radii of ALL ancestor discs
           (Moh p.201(8): "let the l.c.m. of the reduced denominators of
            delta_s,...,delta_r be L; A_{r-1} is the reduced denominator of
            L*delta_{r-1}").  L is a function of the path already travelled.

At tower parameter W: |lam^f| = m*kappa/(W*rho-m), delta(W) = 1 - W*kappa/(W*rho-m).
Final major disc  <=> W = n+m (Xu Lemma 4.4(i): delta = lam^f+lam^g+1).
Split at W: A = den(L*delta(W)); the pattern is p = pi^z prod(pi^A - c_nu)^{r_nu},
so the sub-packet multiset is (optional one singleton part) + orbits of A EQUAL parts.
Constraints: Q = rho*W/m in Z; #parts <= Q; every kappa_j != 0; some kappa_j > 0.
"""
from fractions import Fraction as Q
from math import gcd
import sys, itertools, json

def lcm(a, b): return a*b//gcd(a, b)

def split_shapes(rho, unit, A, cap_orbits):
    """multisets of parts = [z] (optional) + A copies each of r_1..r_k"""
    out = []
    for z in range(0, rho+1, unit):
        rest = rho - z
        if rest % A: continue
        per = rest // A                      # sum of the orbit part-sizes
        if per == 0: continue
        for orb in orbit_parts(per, unit, cap_orbits):
            parts = ([z] if z > 0 else []) + [r for r in orb for _ in range(A)]
            if len(parts) < 2: continue
            out.append((z, tuple(orb), tuple(parts)))
    return out

def orbit_parts(total, unit, cap, maxpart=None):
    if maxpart is None: maxpart = total
    if total == 0:
        yield ()
        return
    if cap == 0: return
    k = min(total, maxpart); k -= k % unit
    while k >= unit:
        for rest in orbit_parts(total-k, unit, cap-1, k):
            yield (k,)+rest
        k -= unit

def search(n, m, rho, kappa, W0, L, depth, cap_orbits=4, cap_W=None):
    unit = m//gcd(n, m)
    res = set()
    # (a) terminate as a final major disc: pattern squarefree, in pi^z k[pi^A]
    #     with z<=1 and A = den(L*delta_final)  (Moh p.201(8); calibrated on the
    #     four printed Xu displays 6.1(i),(ii) and 6.2(i),(ii))
    dfin = 1 - Q((n+m)*kappa, (n+m)*rho - m)
    Afin = (L*dfin).denominator
    rgo = Q(n*rho, m)
    if rho % Afin in (0, 1) and rgo.denominator == 1 and int(rgo) % Afin in (0, 1):
        res.add((Q(n*rho*kappa, (n+m)*rho - m), Q(0)))
    if depth == 0: return res
    step = m//gcd(rho, m)
    W = ((W0//step)+1)*step
    while W < n+m:
        if cap_W and W > cap_W: break
        Qdeg = int(Q(rho*W, m))
        delta = 1 - Q(W*kappa, W*rho - m)
        A = (L*delta).denominator
        for z, orb, parts in split_shapes(rho, unit, A, cap_orbits):
            if len(parts) > Qdeg: continue
            kj = [Q(kappa*(p*W - m), rho*W - m) for p in parts]
            if any(k == 0 for k in kj): continue
            if not any(k > 0 for k in kj): continue
            L2 = lcm(L, delta.denominator)
            sub = []
            for p, k in zip(parts, kj):
                sub.append({(Q(0), -k/p)} if k < 0 else
                           search(n, m, p, k, W, L2, depth-1, cap_orbits, cap_W))
            for combo in itertools.product(*sub):
                res.add((sum(c[0] for c in combo), sum(c[1] for c in combo)))
        W += step
    return res

if __name__ == '__main__':
    for c in json.loads(sys.argv[1]):
        base_IM, base_Im = Q(c['base_IM']), Q(c['base_Im'])
        for depth in c['depths']:
            R = search(c['n'], c['m'], c['rho'], Q(c['kappa']), c['W0'], c['L'],
                       depth, c.get('cap_orbits', 4))
            good = sorted({(base_IM+a, base_Im+b) for a, b in R
                           if (base_IM+a).denominator == 1 and (base_IM+a) >= (base_Im+b)})
            print(f"{c['tag']} depth={depth}: {len(R)} outcomes, {len(good)} survivors")
            for g in good[:12]: print("     SURVIVOR I_M=%s I_m=%s" % g)
            sys.stdout.flush()
