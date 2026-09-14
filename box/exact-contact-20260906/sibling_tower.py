"""Bounded search over sibling MAJOR sub-towers.

A major packet is (rho, kappa) born at tower parameter W0 = n - M(disc).
Along a packet with rho fixed, |lam^f(W)| = m*kappa/(W*rho - m) and
1 - delta(W) = W*kappa/(W*rho - m); the packet goes final major at W = n+m.
A split at W sends rho -> {rho_j} with kappa_j = kappa*(rho_j*W - m)/(rho*W - m);
kappa_j < 0 is a final MINOR leaf at delta = 1 - kappa_j/rho_j.

Constraints imposed (all printed):
  Prop 4.6(2)  deg q = Q = rho*W/m must be a positive integer
  Prop 4.6(3),(4)  #distinct roots of p = #parts <= Q
  Prop 4.6/A.3  no multiplicity == P/Q  (kappa_j != 0); some multiplicity > P/Q
  Lemma 2.1(ii)  rho_j : rho_g,j = m : n, so rho_j in (m/gcd(n,m))Z
NOT imposed (so the search OVER-counts survivors): the Galois orbit-size law
p in pi^z k[pi^A], and any second-generation condition on the sibling tower.
"""
from fractions import Fraction as Q
from math import gcd
import sys, itertools

def parts_even(total, unit, maxpart=None):
    """partitions of total into parts that are positive multiples of unit"""
    if maxpart is None: maxpart = total
    if total == 0:
        yield ()
        return
    k = min(total, maxpart)
    k -= k % unit
    while k >= unit:
        for rest in parts_even(total-k, unit, k):
            yield (k,)+rest
        k -= unit

def search(n, m, rho, kappa, W0, depth, cap_parts, memo=None, seen=None):
    """returns set of (dIM, dIm) reachable from this major packet"""
    unit = m//gcd(n, m)
    res = set()
    # (a) terminate as a final major disc
    res.add((Q(n*rho*kappa, (n+m)*rho - m), Q(0)))
    if depth == 0:
        return res
    # (b) split at W
    step = m//gcd(rho, m)            # rho*W/m integral  <=>  W multiple of step
    W = ((W0//step)+1)*step
    while W < n+m:
        Qdeg = Q(rho*W, m)
        assert Qdeg.denominator == 1
        Qdeg = int(Qdeg)
        for pt in parts_even(rho, unit):
            if len(pt) < 2 or len(pt) > min(Qdeg, cap_parts): continue
            kj = [Q(kappa*(p*W - m), rho*W - m) for p in pt]
            if any(k == 0 for k in kj): continue
            if not any(k > 0 for k in kj): continue
            sub = []
            for p, k in zip(pt, kj):
                if k < 0:
                    sub.append({(Q(0), -k/p)})
                else:
                    sub.append(search(n, m, p, k, W, depth-1, cap_parts))
            for combo in itertools.product(*sub):
                res.add((sum(c[0] for c in combo), sum(c[1] for c in combo)))
        W += step
    return res

if __name__ == '__main__':
    # R009 pattern z=16: sibling zero-disc rho=32 kappa=20 born at W0=44
    # R050 pattern z=5 : sibling zero-disc rho=10 kappa=?? born at W0=12
    # R001 pattern z=7 : sibling zero-disc rho=14 kappa=?? born at W0=12
    import json
    cases = json.loads(sys.argv[1])
    for c in cases:
        n, m, rho, kappa, W0, base_IM, base_Im, tag = (
            c['n'], c['m'], c['rho'], Q(c['kappa']), c['W0'],
            Q(c['base_IM']), Q(c['base_Im']), c['tag'])
        for depth in c.get('depths', [0, 1, 2]):
            R = search(n, m, rho, kappa, W0, depth, c.get('cap_parts', 6))
            good = [(base_IM+a, base_Im+b) for a, b in R
                    if (base_IM+a).denominator == 1 and (base_IM+a) >= (base_Im+b)]
            print(f"{tag} depth={depth}: {len(R)} outcomes, "
                  f"{len(good)} with I_M integral AND I_M>=I_m")
            for g in sorted(set(good))[:10]:
                print("     SURVIVOR I_M=%s I_m=%s" % g)
