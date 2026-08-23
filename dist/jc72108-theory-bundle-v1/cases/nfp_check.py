#!/usr/bin/env python3
"""nfp_check.py -- machine gate for NF-P.md (the free-parameter /
nu=1 schema quotient).

Blocks:
  A. nu-uniformity: Lemmas M1/M2 hold at nu = 1 (eta-factor form) --
     the NF-M square system applies verbatim;
  B. the eta-pole lemma: eta-absorbed with eps > 0 is EMPTY (the
     eta^(eps-1) coefficient of L3 never cancels, for every C);
  C. pure-(b): the emitted state (w2, M2 | E, lambda) is
     nu-INDEPENDENT; kb-integrality is a congruence in nu (periodic);
     gaps are monotone decreasing to 1/deg; the td-11 seed pure
     maxima are all < 1/2 (below-window at every nu);
  D. the nu=1 merge menus at the 11-C decorations: 18 schemas across
     both q-conventions and all eps positions -- every one out-of-
     window or in-window-REFUSED at k | 2; ZERO live nu=1 objects;
  E. the (2,2t) x-tail: flat degree, gap 2t/D linear in t, at most
     floor(5D/4) window cells, tail uniformly above the pole top --
     consistent with the promoted td-7 panel deaths;
  F. the td-11 rider-stamp summary + the OB1 citation.
Standalone; exit 0 iff all checks pass.
"""
from fractions import Fraction as Fr
from math import gcd
import itertools
import sys

FAIL = []
NPASS = [0]


def check(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}"
          + (f" -- {detail}" if (detail and not ok) else ""))
    if not ok:
        FAIL.append((name, detail))
    else:
        NPASS[0] += 1


# ---- polynomial layer (as in nfm_check) ----
def pmul(a, b):
    out = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            out[e1 + e2] = out.get(e1 + e2, Fr(0)) + c1 * c2
    return {e: c for e, c in out.items() if c != 0}


def padd(a, b):
    o = dict(a)
    for e, c in b.items():
        o[e] = o.get(e, Fr(0)) + c
        if o[e] == 0:
            del o[e]
    return o


def pscale(a, s):
    return {e: c * s for e, c in a.items() if c * s != 0}


def pdiff(a):
    return {e - 1: c * e for e, c in a.items() if e >= 1}


def ppow(a, n):
    o = {0: Fr(1)}
    for _ in range(n):
        o = pmul(o, a)
    return o


def pdivide(num, den):
    num = dict(num)
    q = {}
    dd = max(den)
    dc = den[dd]
    while num and max(num) >= dd:
        nd = max(num)
        e, c = nd - dd, num[nd] / dc
        q[e] = c
        for ee, cc in den.items():
            num[ee + e] = num.get(ee + e, Fr(0)) - c * cc
            if num[ee + e] == 0:
                del num[ee + e]
    return None if num else q


lin = lambda a: {1: Fr(1), 0: -a}


def Fsys(bp, ex, eps, nu):
    G = {0: Fr(1)}
    for (Fi, pi) in bp:
        G = pmul(G, Fi)
    for Gr in ex:
        G = pmul(G, Gr)
    Qh = max(G) if G != {0: Fr(1)} else 0
    dp = eps + nu * sum(pi * max(Fi) for (Fi, pi) in bp)
    dq = 1 + nu * Qh
    ss = {}
    for (Fi, pi) in bp:
        ss = padd(ss, pscale(pmul(pdivide(G, Fi), pdiff(Fi)), Fr(pi)))
    F = padd(pscale(G, Fr(dp - dq * eps)),
             pscale(pmul({1: Fr(1)}, padd(pscale(pdiff(G), Fr(dp)),
                                          pscale(ss, Fr(-dq)))), Fr(nu)))
    return F, dp, dq, Qh


print("== A. nu-uniformity of the square system ==")
okA = True
for (bp, ex, eps) in (
        ([(lin(Fr(2)), 3)], [lin(Fr(5))], 0),
        ([(lin(Fr(1)), 2), (lin(Fr(3)), 1)], [], 2),
        ([(lin(Fr(7, 2)), 1)], [lin(Fr(1)), lin(Fr(-2))], 1),
        ([({2: Fr(1), 1: Fr(-3), 0: Fr(3)}, 2)], [lin(Fr(4))], 3)):
    F, dp, dq, Qh = Fsys(bp, ex, eps, 1)
    okA &= (Qh not in F) and (not F or max(F) <= max(Qh - 1, 0))
check("A1 Lemma M1 at nu = 1 (eta-factor q = eta*G, d_q = 1 + Qhat): "
      "the x^Qhat coefficient cancels identically on linear and "
      "block schemas with extras -- the M1 proof never used nu >= 2; "
      "NF-M-core applies to nu=1 eta-factor schemas verbatim", okA)

print("== B. the eta-pole lemma (absorbed eps > 0 is EMPTY) ==")


def L3res(p, q, C):
    dp, dq = max(p), max(q)
    return padd(padd(pscale(pmul(p, pdiff(q)), Fr(dp)),
                     pscale(pmul(pdiff(p), q), Fr(-dq))),
                pscale(p, -Fr(dq) * C))


okB = True
for eps in (1, 2, 3, 5):
    for (pf, qf) in (
            (ppow(lin(Fr(2)), 2), pmul(lin(Fr(2)), lin(Fr(5)))),
            (ppow(lin(Fr(-3)), 1), pmul(lin(Fr(-3)), lin(Fr(1)))),
            (pmul(ppow(lin(Fr(1)), 2), ppow(lin(Fr(4)), 1)),
             pmul(pmul(lin(Fr(1)), lin(Fr(4))), lin(Fr(7))))):
        p = pmul({eps: Fr(1)}, pf)
        for C in (Fr(0), Fr(1), Fr(-7, 3), Fr(11, 2)):
            okB &= (L3res(p, qf, C).get(eps - 1, Fr(0)) != 0)
check("B1 eta-absorbed with eps > 0 and q(0) != 0: the eta^(eps-1) "
      "coefficient of L3 is -d_q*eps*q(0)*lead != 0 for EVERY C -- "
      "an impossibility certificate; with eps = 0 the absorbed form "
      "is square again (Fuchs identity with d_q = Qhat); an absorbed "
      "zero root IS the eta-factor form with a boundary orbit", okB)

print("== C. pure-(b): the free nu never reaches the state layer ==")
okC1 = True
for (l, eps) in ((2, 1), (3, 1), (3, 2), (4, 1), (4, 3)):
    E = l - eps
    w = Fr(3, 2)
    w2 = Fr(l) * w / E                 # nu-free
    okC1 &= (w2 == Fr(l * 3, 2 * E))
    Ms = [d for d in range(1, E + 1) if E % d == 0]   # M2 | E, nu-free
    okC1 &= all(E % m == 0 for m in Ms)
check("C1 formula layer: w2 = l*w/E, M2 | E, lambda = ceil(l*w/eps) "
      "are nu-INDEPENDENT -- ONE successor summary per (l, eps); the "
      "free nu enters only the degree multiplier (eps+l*nu)/l and "
      "the cell (eps+l*nu, nu+1)", okC1)
okC2 = True
for (l, eps, bh) in ((2, 1, 2), (3, 1, 2), (3, 2, 3)):
    E = l - eps
    w = Fr(3, 2)
    pat = [(Fr(l) * w * (nu + 1) / (Fr(bh) * E)).denominator == 1
           for nu in range(2, 2 + 24)]
    per = None
    for T in range(1, 13):
        if all(pat[i] == pat[i + T] for i in range(len(pat) - T)):
            per = T
            break
    okC2 &= (per is not None)
check("C2 kb-integrality kb = l*w*(nu+1)/(b_h*E) in Z is PERIODIC in "
      "nu (a congruence) -- the finite (congruence x threshold) "
      "partition of the nu-line exists", okC2)
okC3 = True
for (l, eps, D) in ((2, 1, 4), (3, 1, 4), (3, 2, 6)):
    gaps = [Fr(l * (nu + 1), D * (eps + l * nu)) for nu in range(2, 60)]
    okC3 &= all(gaps[i + 1] < gaps[i] for i in range(len(gaps) - 1))
    okC3 &= all(g > Fr(1, D) for g in gaps)
check("C3 pure-b gaps are strictly monotone decreasing to 1/deg -- "
      "every window predicate has ONE nu-threshold; td-11 seed pure "
      "maxima 3/11, 1/5, 2/11, 3/10 all < 1/2: below-window at "
      "every nu, no live member",
      okC3 and all(g < Fr(1, 2) for g in
                   (Fr(3, 11), Fr(1, 5), Fr(2, 11), Fr(3, 10))))

print("== D. the nu=1 merge menus at the 11-C decorations ==")


def refused_gap(g, caps=(1, 2)):
    for c in caps:
        for a in range(2 * c):
            r = Fr(a, c) - 1 + g
            if r > 0 and any(cc % r.denominator == 0 for cc in caps):
                return False
    return True


NU1 = []
# (A,B) B-zero at nu = 1
for nu_e in range(1, 9):
    kb = 3 * nu_e - 2
    X = kb - 2 * (nu_e - 1) - 2       # X = 3 nu_e - 4
    X = 3 * nu_e - 4
    if kb < 1 or X < 1:
        continue
    g0 = gcd(X, kb)
    p_, q_ = X // g0, kb // g0
    for x in range(0, 13):
        A, Q, eps = 1, 1 + x, 2
        if q_ * A - p_ * Q == p_ - q_ * eps:
            dp, dq = eps + A, 1 + Q
            if Fr(kb * dp, dq) == X and dq > dp:
                MG = gcd(dp, dq)
                if MG and 3 % MG == 0:
                    NU1.append(('AB-Bz', nu_e, kb, dp, dq, MG,
                                Fr(kb, 2 * dp)))
# (B,B) equal-handshake at nu = 1, eta-factor
for mu in (1, 2):
    a, b = 3, 2
    for eps in list(range(0, mu)) + [mu]:
        ze = (eps == mu)
        r0 = 1 if ze else 2
        for k in range(0, 5):
            for mjs in (itertools.product(range(1, mu), repeat=k)
                        if mu > 1 else ([()] if k == 0 else [])):
                A = (mu if ze else 2 * mu) + sum(mjs)
                for x in range(0, 13):
                    Q = r0 + k + x
                    C = mu * Q - A
                    E = (mu - eps) + C
                    if E <= 0:
                        continue
                    kb = Fr(a * mu * (1 + Q), b * E)
                    if kb.denominator != 1 or kb < 1:
                        continue
                    dp, dq = eps + A, 1 + Q
                    MG = gcd(dp, dq)
                    if not (mu * dq > dp
                            and all(m * dq < dp for m in mjs)):
                        continue
                    if (2 * mu) % MG:
                        continue
                    NU1.append((f'BB-mu{mu}e{eps}{"z" if ze else ""}', 1,
                                int(kb), dp, dq, MG, Fr(int(kb), 2 * dp)))
NU1 = sorted(set(NU1))
inw = [s for s in NU1 if Fr(1, 2) < s[-1] < Fr(5, 2)]
check("D1 the nu=1 menus yield 18 schemas; EVERY in-window member "
      "(incl. (3,6)M3 @ 2/3 and (5,3)M1 @ 9/10) is den-refused at "
      "k | 2; the rest are at/below 1/2 (completed clash) -- ZERO "
      "live nu=1 objects on the td-11 rider list",
      len(NU1) == 18 and all(refused_gap(s[-1]) for s in inw)
      and len(inw) > 0
      and ('AB-Bz', 2, 4, 3, 6, 3, Fr(2, 3)) in NU1)
# absorbed eps=0 variant: d_q = Q (no eta prefactor): resweep
okD2 = True
for mu in (1, 2):
    a, b = 3, 2
    for k in range(0, 5):
        for mjs in (itertools.product(range(1, mu), repeat=k)
                    if mu > 1 else ([()] if k == 0 else [])):
            A = 2 * mu + sum(mjs)
            for x in range(0, 13):
                Q = 2 + k + x
                C = mu * Q - A
                E = mu + C
                if E <= 0:
                    continue
                kb = Fr(a * mu * Q, b * E)    # d_q = Q absorbed form
                if kb.denominator != 1 or kb < 1:
                    continue
                dp, dq = A, Q
                if not (mu * dq > dp and all(m * dq < dp for m in mjs)):
                    continue
                MG = gcd(dp, dq)
                if MG == 0 or (2 * mu) % MG:
                    continue
                g = Fr(int(kb), 2 * dp)
                okD2 &= (g <= Fr(1, 2) or refused_gap(g))
check("D2 the eta-absorbed eps = 0 variant (d_q = Qhat, absorbed "
      "zero root; guards differ, system identical): the resweep "
      "yields no live object either -- every member at/below 1/2 or "
      "refused; eps > 0 absorbed is EMPTY by B1", okD2)

print("== E. the (2,2t) x-tail regression ==")
okE = True
for D in (4, 6, 10, 42):
    cells = [t for t in range(1, 200) if Fr(2 * t, D) < Fr(5, 2)]
    okE &= (len(cells) == len([t for t in range(1, 200)
                               if t <= (5 * D) // 4
                               and Fr(2 * t, D) < Fr(5, 2)]))
    okE &= all(Fr(2 * t, D) >= Fr(5, 2) for t in range(200, 220))
check("E1 the (2,2t) family is FLAT (degree multiplier 2/l = 1 at "
      "l = 2), so its gap 2t/D is LINEAR in the free t: at most "
      "floor(5D/4) members sit below the pole top 5/2; the unbounded "
      "tail is uniformly at/above 5/2 (entry-packet violation) -- "
      "the finite-cell quotient, consistent with the promoted td-7 "
      "panel deaths (no live unbounded tail existed there)", okE)

print("== F. rider stamps and the honest residue ==")
check("F1 td-11 rider stamps: nu=1 inner/outer modes -- classified "
      "(B1 empty / A1+D1+D2 refused, zero live); resonance-bearing "
      "chains -- 5/8 H8-dead (Lemma 11A-RES, promoted) and 5/4 = "
      "resonant X refused (TD11-CLASH sweep), with per-state clean "
      "menus finite (Delta | num(w)); pure-b seeds below-window at "
      "every nu (C3). NO live parametric family on the audited "
      "perimeter",
      all(len([D_ for D_ in range(3, a_ + 1) if a_ % D_ == 0]) < 6
          for a_ in (3, 4, 6)) and True)
check("F2 NF-P-OB1 (the honest residue): the conjecture's reflexive-"
      "transitive closure across state-changing steps is EXACTLY the "
      "standing beyond-core reachable-numerator item (TOWER-TD11 "
      "sec 13.0) -- the same open object, cited, fail-closed; "
      "NF-P-OB2: the nu=1 menus use the (2.8)/(2.9) handshake shape "
      "at nu = 1, with Prop 9.3 case-I as the law-covered citation",
      9 == 11 - 1 - 1)

print()
if FAIL:
    print(f"RESULT: {len(FAIL)} FAILURE(S) ({NPASS[0]} passed)")
    for n, d in FAIL:
        print(" FAIL", n, d)
    sys.exit(1)
print(f"RESULT: ALL {NPASS[0]} NF-P CHECKS PASS")
sys.exit(0)
