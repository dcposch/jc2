#!/usr/bin/env python3
"""Chart counts, multiplicities, split arithmetic, D_2 thresholds, the inner
h3/h2 support blocks, and the exact outer/major D_1 ranks.  Secs 1.2, 2.1, 3.2,
3.3, 3.5, 7 of xmodel/g9966-chart-necessity-opus5-20260903.md."""
from fractions import Fraction as F
from math import comb

def S(D, r): return r*(D+1) - r*(r-1)//2
def slots(D, r0): return [(r, q) for q in range(r0) for r in range(0, D-q+1)]
def low_slots(D, r0, Dlow):
    return [(r, q) for q in range(r0) for r in range(D-Dlow, D-q+1)
            if r >= 0 and r+q <= D]
def rank(M):
    M = [row[:] for row in M]; R = len(M); C = len(M[0]) if R else 0; r = 0
    for c in range(C):
        p = next((i for i in range(r, R) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]; pv = M[r][c]
        for i in range(r+1, R):
            if M[i][c] != 0:
                f = M[i][c]/pv
                for j in range(c, C): M[i][j] -= f*M[r][j]
        r += 1
        if r == R: break
    return r

print("=== A. chart dimension count (Prop 1.2) ===")
blocks = [("H",10,11),("C2",21,11),("C3",32,11),("A2",65,33),
          ("A3",98,33),("B1",32,33),("B2",65,33)]
tot = sum(S(D,r) for _,D,r in blocks)
print("   blocks %s  total %d" % ([S(D,r) for _,D,r in blocks], tot))
tot0 = sum(S(D+1,r) for _,D,r in blocks)
c99 = sum(1 for i in range(100) for j in range(100) if i+j <= 99 and j < 99)
c66 = sum(1 for i in range(67) for j in range(67) if i+j <= 66 and j < 66)
print("   before fixing the tops %s total %d = %d + %d ; removed %d = 99+66"
      % ([S(D+1,r) for _,D,r in blocks], tot0, c99, c66, tot0-tot))

print("\n=== B. leading forms, multiplicities (Moh p.194, Prop 6.2) ===")
for nm, e in (("h3",1),("h2",3),("F=g_Moh",9),("G=f_Moh",6)):
    print("   in %-8s = P^%-2d deg %3d ; mult y=0 : %2d ; mult y=x : %2d"
          % (nm, e, 11*e, 3*e, 8*e))
print("   Xu 7.3 minor multiplicities  T0:%d T1:%d T2:%d T3:%d"
      % (99*3//11, 66*3//11, 55*3//11, (145-2)*3//11+1))

print("\n=== C. split-order arithmetic (Xu Prop 7.3, Cor 7.5, sec 8) ===")
us, vs, ds, n, m = 3, 8, 11, 99, 66
print("   ord g(sigma) = (n/d_s)(u_s delta - v_s) < 0  <=>  delta < v_s/u_s = %s" % F(vs,us))
cands = sorted({F(a,b) for b in (1,2,3) for a in range(b+1, 3*b+1)
                if 1 < F(a,b) < F(vs,us)})
print("   candidates 1 < delta < %s with den <= %d : %s"
      % (F(vs,us), us, [str(x) for x in cands]))
print("   Cor 7.5 threshold (v_s+1)/(u_s+1) = %s" % F(vs+1, us+1))
for d in cands:
    print("      delta=%-4s ord F = %-6s ord G = %-6s  parts allowed: %s"
          % (d, (n//ds)*(us*d-vs), (m//ds)*(us*d-vs),
             "2 (Cor 7.5)" if d < F(vs+1, us+1) else "2 or 3"))
print("   deg q = 13 u_s + 1 = %d = (-mu_3-2)u_s/d_s + 1 = %d"
      % (13*us+1, (145-2)*us//ds+1))

print("\n=== D. inner major support blocks (sec 3.5) ===")
for nm, D, r0, Dlow, ordb in (("h3",11,11,10,F(-1,3)), ("h2",33,33,32,F(-1))):
    sl = low_slots(D, r0, Dlow); W0 = 3*(D+ordb)
    below = [s for s in sl if 3*s[0]+4*s[1] < W0]
    eq = [s for s in sl if 3*s[0]+4*s[1] == W0]
    above = [s for s in sl if 3*s[0]+4*s[1] > W0]
    print("   %-3s ambient %3d ; boundary %s : below %3d ; face %d %s ; strict %3d"
          % (nm, len(sl), W0, len(below), len(eq), sorted(eq), len(above)))
tot21 = 0
for r in range(1, 12):
    vr = max(0, -((3*r-33)//4)); tot21 += len([d for d in range(vr, 11-r+1)])
print("   free h3 coordinates (r,d), v_r = max(0,ceil((33-3r)/4)) <= d <= 11-r : %d" % tot21)

print("\n=== E. outer D_2 thresholds and support (sec 3.2) ===")
spec = [("A2",65,33,F(-2),F(-2,9)),("A3",98,33,F(-3),F(-1,3)),
        ("B1",32,33,F(-1),F(-1,9)),("B2",65,33,F(-2),F(-2,9))]
ta = td = tr = 0
for nm, D, r0, b2, b1 in spec:
    sl = slots(D, r0); W0 = 3*(D+b2)
    rem = [s for s in sl if 3*s[0]+4*s[1] >= W0]
    ta += len(sl); td += len(sl)-len(rem); tr += len(rem)
    print("   %-3s D=%2d ord>=%-5s W0=%3d : ambient %4d deleted %4d remaining %4d min r %d"
          % (nm, D, b2, W0, len(sl), len(sl)-len(rem), len(rem),
             min(r for r, q in rem)))
print("   TOTAL ambient %d deleted %d remaining %d" % (ta, td, tr))

print("\n=== F. outer D_1 rows and exact Q-ranks (sec 3.3) ===")
TR = TK = 0
for nm, D, r0, b2, b1 in spec:
    W0 = 3*(D+b2); T1 = 9*(D+b1)
    rem = [(r, q) for (r, q) in slots(D, r0) if 3*r+4*q >= W0]
    cols = {s: i for i, s in enumerate(rem)}
    rows = {}
    for (r, q) in rem:
        for j in range(0, q+1):
            E = 9*r+12*q+j
            if E < T1:
                rows.setdefault((E, j), [F(0)]*len(rem))[cols[(r, q)]] += F(comb(q, j))
    M = [rows[k] for k in sorted(rows)]; rk = rank(M) if M else 0
    TR += len(M); TK += rk
    print("   %-3s D_1 threshold %-4s raw rows %3d exact rank %3d window [%d,%d]"
          % (nm, T1, len(M), rk, min(E for E, _ in rows), max(E for E, _ in rows)))
print("   TOTAL raw %d rank %d ; retained 1002 - %d = %d" % (TR, TK, TK, 1002-TK))
D, r0, W0, T1 = 33, 33, 96, 9*(33-F(1,9))
cols = {s: i for i, s in enumerate([s for s in low_slots(33, 33, 32)
                                    if 3*s[0]+4*s[1] >= 97])}
rows = {}
for (r, q) in cols:
    for j in range(0, q+1):
        E = 9*r+12*q+j
        if E < T1:
            rows.setdefault((E, j), [F(0)]*len(cols))[cols[(r, q)]] += F(comb(q, j))
from collections import Counter
M = [rows[k] for k in sorted(rows)]
print("   h2 D_1 threshold %s : raw rows %d at e-powers %s ; exact rank %d"
      % (T1, len(M), dict(sorted(Counter(E for E, _ in rows).items())), rank(M)))
