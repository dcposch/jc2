#!/usr/bin/env python3
"""Exact norms of the facial (axis) coefficients printed by the pieces jobs, and of the t=3 objects."""
import re, sys
sys.path.insert(0,'.')
import norms
def axis_lines(path):
    out=[]
    for line in open(path):
        m=re.match(r"AXIS var=(\S+) r=(\d+) : (\(.*\))\*(\S+)$", line.strip())
        if m: out.append((m.group(1),int(m.group(2)),m.group(3),m.group(4)))
    return out
for t,path in [(4,"t4_pieces_exact.out"),(5,"t5_pieces_exact.out"),(6,"t6_pieces_exact.out")]:
    print(f"===== t={t} axis coefficients (exact) =====")
    for var,r,co,mon in axis_lines(path):
        norms.describe(t,co,f"[{mon}] R_{r}")
print("===== t=3 =====")
txt=open("t3_exact.out").read()
for label,pat in [("c10=[q2^10]R_2",r"C10 q2\^10 coefficient of R2: (\(.*\))\*q2_0\^10"),("tau1=[b4^18]R_1",r"TAU1 b4\^18 coeff: (\(.*\))\*b4\^18"),("tau2=[b4^20]R_2",r"TAU2 b4\^20 coeff: (\(.*\))\*b4\^20"),
                  ("SIGMA_RED",r"SIGMA_RED = Res_\{8,10\}\(f1,f2\) = (\(.*\))"),("PI3",r"PI3 = .* = sred/c10\^8 = (\(.*\))"),("SIGMA3",r"SIGMA3 = .* = c10\*sred = (\(.*\))"),("lc f1=[q2^8 b4^2]R_1",r"lc f1 = (\(.*\))")]:
    m=re.search(pat,txt); norms.describe(3,m.group(1),label)
