"""ell-shifted sibling-tower closure for a LICENSED Prop 6.3 CHILD.

Identical to box/exact-contact-20260906/sibling_tower3.py except that every
radius carries the ell-shift derived in the report:
    delta(W)  = (1+l) - W*kappa/(W*rho - m)          [Prop 4.6(3)* + Lem 4.4(i)^l]
    delta_fin = (1+l) - (n+m)*kappa/((n+m)*rho - m)  [final major at W = n+m]
The split law kappa_j = kappa*(p*W-m)/(rho*W-m) is ell-FREE (report sec. 2.7),
as are Q = rho*W/m in Z, #parts <= Q, the orbit law A = den(L*delta), the
final Galois law rho_f, rho_g = 0 or 1 mod A, Lemma A (setwise-coprime parts)
and Lemma B (d_D | M, i.e. W == n mod d_D).
A minor leaf contributes delta - (1+l) = -kappa_j/rho_j to I_m^l, unchanged.
"""
from fractions import Fraction as Q
from math import gcd
from functools import reduce
import itertools, sys

sys.path.insert(0, '/home/ubuntu/jc2/box/exact-contact-20260906')
from sibling_tower2 import orbit_parts, lcm


def shapes(rho, unit, A, cap):
    out = []
    for z in range(0, rho + 1, unit):
        rest = rho - z
        if rest % A:
            continue
        per = rest // A
        if per == 0:
            continue
        for orb in orbit_parts(per, unit, cap):
            parts = ([z] if z > 0 else []) + [r for r in orb for _ in range(A)]
            if len(parts) < 2:
                continue
            rs = [p // unit for p in parts]
            if reduce(gcd, rs) != 1:
                continue
            out.append((z, tuple(orb), tuple(parts)))
    return out


def search(n, m, rho, kappa, W0, L, dcur, depth, ell, cap=4):
    """Return {(I_M-contribution, I_m-contribution): witness} for one packet."""
    unit = m // dcur
    res = {}
    dfin = (1 + ell) - Q((n + m) * kappa, (n + m) * rho - m)
    Afin = (L * dfin).denominator
    rgo = Q(n * rho, m)
    if rho % Afin in (0, 1) and rgo.denominator == 1 and int(rgo) % Afin in (0, 1):
        res[(Q(n * rho * kappa, (n + m) * rho - m), Q(0))] = \
            f"FINAL(rho={rho},delta={dfin},A={Afin})"
    if depth == 0:
        return res
    W = W0 + 1
    while W < n + m:
        if (n - W) % dcur or Q(rho * W, m).denominator != 1:
            W += 1
            continue
        Qd = int(Q(rho * W, m))
        delta = (1 + ell) - Q(W * kappa, W * rho - m)
        A = (L * delta).denominator
        for z, orb, parts in shapes(rho, unit, A, cap):
            if len(parts) > Qd:
                continue
            kj = [Q(kappa * (p * W - m), rho * W - m) for p in parts]
            if any(k == 0 for k in kj) or not any(k > 0 for k in kj):
                continue
            L2 = lcm(L, delta.denominator)
            sub = []
            for p, k in zip(parts, kj):
                sub.append({(Q(0), -k / p): f"minor(rho={p},delta={(1+ell)-k/p})"}
                           if k < 0 else
                           search(n, m, p, k, W, L2, dcur, depth - 1, ell, cap))
            if any(not s for s in sub):
                continue
            for combo in itertools.product(*[list(s.items()) for s in sub]):
                key = (sum(c[0][0] for c in combo), sum(c[0][1] for c in combo))
                res.setdefault(key,
                               f"SPLIT@W={W}(M={n-W},delta={delta},A={A},z={z},"
                               f"orb={orb})[" + " | ".join(c[1] for c in combo) + "]")
        W += 1
    return res
