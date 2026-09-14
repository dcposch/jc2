#!/usr/bin/env python3
"""Bounded search for a single expression R(datum) reproducing BOTH numeric
engine residues.  Grammar: R = s * prod_j  atom_j ^ e_j,  e_j in -2..3,
atoms drawn from the split datum of each branch.  Reports how many distinct
formulas in the grammar hit (6264, 64) -- a large count means a 2-point fit
carries no information."""
from itertools import product
from fractions import Fraction as Fr

# split datum per branch (Moh/Xu invariants + the band index the kill occurred at)
D = {
 "d2":   dict(n=99, m=66, K=33, A=9, B=24, e=3, f=2, d2=33, d3=11, V2=8, V3=8,
              us=3, vs=8, dnum=2, dden=1, npart=2, p=4,  ell=8,  degp=3),
 "d52":  dict(n=99, m=66, K=33, A=9, B=24, e=3, f=2, d2=33, d3=11, V2=8, V3=8,
              us=3, vs=8, dnum=5, dden=2, npart=3, p=8,  ell=16, degp=3),
}
TARGET = {"d2": 6264, "d52": 64}

# derived atoms
for k, v in D.items():
    v["Kmp"]   = v["K"] - v["p"]
    v["eA"]    = v["e"]*v["A"]
    v["cJ"]    = v["e"]*v["A"]*(v["K"]-v["p"])       # derived ladder value at k0
    v["k0"]    = v["A"]*(v["e"]+v["f"]-1)-1
    v["vsmus"] = v["vs"]-v["us"]

ATOMS = ["n","m","K","A","B","e","f","d3","V2","us","vs","dnum","dden","npart",
         "p","ell","degp","Kmp","eA","cJ","k0","vsmus"]

hits = []
# single-atom-power families with a 2,3-smooth prefactor
for a in ATOMS:
    for ea in range(-2, 4):
        for b in ATOMS:
            for eb in range(-2, 4):
                for two in range(-3, 7):
                    for three in range(-3, 5):
                        ok = True
                        for br, tgt in TARGET.items():
                            d = D[br]
                            try:
                                val = Fr(2)**two * Fr(3)**three * Fr(d[a])**ea * Fr(d[b])**eb
                            except ZeroDivisionError:
                                ok = False; break
                            if val != tgt: ok = False; break
                        if ok:
                            hits.append((two, three, a, ea, b, eb))
print("grammar: R = 2^i * 3^j * X^a * Y^b,  i in -3..6, j in -3..4, a,b in -2..3,")
print("         X,Y among %d datum atoms" % len(ATOMS))
print("formulas in the grammar hitting BOTH 6264 and 64: %d" % len(hits))
seen = set()
for h in hits[:400]:
    two, three, a, ea, b, eb = h
    key = tuple(sorted([(a, ea), (b, eb)])) + (two, three)
    if key in seen: continue
    seen.add(key)
print("distinct (up to factor order): %d" % len(seen))
for k in sorted(seen)[:25]:
    (a, ea), (b, eb), two, three = k
    print("   R = 2^%d*3^%d * %s^%d * %s^%d" % (two, three, a, ea, b, eb))

# the derived decomposition
print()
for br, tgt in TARGET.items():
    d = D[br]
    print("%-4s  target %-6d   derived c_J(p,k0)=e*A*(K-p)=%d   target/c_J = %s"
          % (br, tgt, d["cJ"], Fr(tgt, d["cJ"])))
