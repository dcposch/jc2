#!/usr/bin/env python3
"""M2-DESCENT (1c-bis): wider automorphism scan + one fully printed witness."""
import sys, os, random
from fractions import Fraction as F
from math import gcd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from etaexp import char_data
from autoscan import (add, scal, mul, dx, dy, jac, deg, degy, subst,
                      normalize_monic_y, build, gauge, X, Y)

def pstr(P):
    ts=[]
    for (i,j) in sorted(P, key=lambda t:(-(t[0]+t[1]),-t[1])):
        c=P[(i,j)]; s=("%s"%c) if (i or j) else "%s"%c
        mon = ("x^%d"%i if i>1 else ("x" if i==1 else "")) + ("y^%d"%j if j>1 else ("y" if j==1 else ""))
        ts.append(("%s"%c if (c!=1 or not mon) else "") + ("*" if (c!=1 and mon) else "") + mon)
    return " + ".join(ts).replace("+ -","- ")

rnd=random.Random(7717)
seqs=[[2],[3],[4],[5],[6],[7],[2,2],[3,2],[2,3],[4,2],[2,4],[3,3],[5,2],[2,5],[4,3],[3,4],
      [2,2,2],[3,2,2],[2,3,2],[2,2,3],[3,3,2],[2,2,2,2],[4,2,2],[2,4,2],[2,2,4],[5,3],[3,5],
      [2,2,2,2,2],[3,2,3],[4,4],[2,6],[6,2]]
rows=[]; seen=set()
for L in seqs:
    for rep in range(6):
        Ff,Gg=build(L,rnd)
        f2,g2=gauge(Ff,Gg,rnd)
        if f2 is None: continue
        J=jac(f2,g2)
        if len(J)!=1 or (0,0) not in J: continue
        m,n=degy(f2),degy(g2)
        if not (1<n<=30 and 0<m<n): continue
        Ms,ds,fj=char_data(f2,m,g2,n)
        if len(Ms)<2: continue
        key=(n,m,tuple(Ms))
        if key in seen: continue
        seen.add(key)
        s=len(Ms); dsl=ds[:]
        rows.append((L,n,m,Ms,ds,fj,f2,g2))
print("  %-16s %4s %4s %-24s %-20s %6s %5s %5s" % ("build","n","m","M_1..M_s","d_1..","M_2>m","s","d_s"))
w=[]
for (L,n,m,Ms,ds,fj,f2,g2) in sorted(rows,key=lambda r:(r[1],r[2])):
    M2=Ms[1]; s=len(Ms); d_s=ds[s-1]
    print("  %-16s %4d %4d %-24s %-20s %6s %5d %5d" % (str(L),n,m,str(Ms),str(ds),str(M2>m),s,d_s))
    if M2<=m: w.append((n,m,Ms,ds,fj,f2,g2))
print("\n  total pairs %d ; M_2 > m : %d ; M_2 <= m : %d"
      % (len(rows), sum(1 for r in rows if r[3][1]>r[2]), len(w)))
print("  witnesses with M_2 <= m and d_s >= 4 :",
      [(n,m,Ms,ds) for (n,m,Ms,ds,_,_,_) in w if ds[len(Ms)-1]>=4])

if w:
    n,m,Ms,ds,fj,f2,g2 = sorted(w)[0]
    print("\n== SMALLEST WITNESS, printed in full (M_2 <= m) ==")
    print("   n = deg g = deg_y g = %d ,  m = deg f = deg_y f = %d ,  K = gcd = %d" % (n,m,gcd(n,m)))
    print("   g =", pstr(g2))
    print("   f =", pstr(f2))
    print("   J(f,g) =", jac(f2,g2))
    print("   deg g = %d, deg_y g = %d ; deg f = %d, deg_y f = %d" % (deg(g2),degy(g2),deg(f2),degy(f2)))
    print("   eta-expansion  f = eta^{-m} + sum f_j(x) eta^j :")
    for j in sorted(fj):
        p=fj[j]
        print("      f_%-4d = %s" % (j, " + ".join("%s*x^%d"%(c,d) for d,c in sorted(p.items()))))
    print("   characteristic data  M =", Ms, "  d =", ds)
    print("   M_2 = %d  vs  m = %d   ->  M_2 > m is FALSE" % (Ms[1], m))
