#!/usr/bin/env python3
"""Second pass: (a) widen the grammar to 3 atoms + free 2,3,5,7-smooth constant
and count solutions -- if many, the 2-point fit carries no information;
(b) verify the D=108 residue is exactly disc p, from the frozen incidence rows."""
from itertools import combinations, product
from fractions import Fraction as Fr
import sympy as sp, json

D = {
 "d2":  dict(n=99,m=66,K=33,A=9,B=24,e=3,f=2,d3=11,V2=8,us=3,vs=8,dnum=2,dden=1,
             npart=2,p=4,ell=8,degp=3),
 "d52": dict(n=99,m=66,K=33,A=9,B=24,e=3,f=2,d3=11,V2=8,us=3,vs=8,dnum=5,dden=2,
             npart=3,p=8,ell=16,degp=3)}
for v in D.values():
    v["Kmp"]=v["K"]-v["p"]; v["cJ"]=v["e"]*v["A"]*(v["K"]-v["p"])
T = {"d2":6264,"d52":64}
ATOMS=[a for a in D["d2"]]
# only atoms that actually differ between the branches can shape the ratio
varying=[a for a in ATOMS if D["d2"][a]!=D["d52"][a]]
print("atoms differing between the two branches:", varying)
print("branch ratios:", {a: str(Fr(D['d2'][a],D['d52'][a])) for a in varying})
print("required ratio R(d2)/R(d52) = 6264/64 =", Fr(6264,64))

sols=0; examples=[]
for trio in combinations(ATOMS,3):
    for exps in product(range(-3,4),repeat=3):
        r=Fr(1)
        for a,e in zip(trio,exps): r*= Fr(D["d2"][a],D["d52"][a])**e
        if r!=Fr(6264,64): continue
        base=Fr(1)
        for a,e in zip(trio,exps): base*=Fr(D["d2"][a])**e
        C=Fr(6264)/base
        # accept if the leftover constant is {2,3,5,7}-smooth
        num,den=C.numerator,C.denominator; ok=True
        for x in (num,den):
            x=abs(x)
            for pr in (2,3,5,7):
                while x%pr==0: x//=pr
            if x!=1: ok=False
        if ok:
            sols+=1
            if len(examples)<6: examples.append((C,trio,exps))
print("\n3-atom formulas with a {2,3,5,7}-smooth constant fitting BOTH points: %d" % sols)
for C,trio,exps in examples:
    print("   R = %s * %s" % (C, " * ".join("%s^%d"%(a,e) for a,e in zip(trio,exps) if e)))

print("\n--- D=108: is the residue exactly disc p ? (frozen incidence-variants.json) ---")
iv=json.load(open("/tmp/jc2-lane.boT2Oz/inputs/incidence-variants.json"))
b,c,j1,j2=sp.symbols("b c jet1 jet2")
for var in iv["variants"]:
    rows=[sp.sympify(v) for v in var["residual"].values()]
    G=sp.groebner(rows,b,c,j1,j2,order="lex")
    disc=b**2+4*c                       # disc(pi^2+b*pi-c)
    red=G.reduce(disc)[1]
    print("  %-28s  h3 coords=%d  rows=%d   reduce(disc p, I_inc) = %s"
          % (var["variant"], var["h3_coordinates"], len(rows), red))
    print("      solved locus: %s" % sp.solve(rows,[b,c,j1,j2],dict=True))
