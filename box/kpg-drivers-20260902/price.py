#!/usr/bin/env python3
"""KELLER-PENCIL-GENUS: price the chain-ceiling against the promoted MF-SHARP floor Phi.

Inputs (consumed, not re-derived):
  Phi(N,W)  -- MFS price table, reviewer-CONFIRMED at declared strength (a FLOOR on n_min).
Derived here:
  CH1 (chain, Psi=0):                     n (W-S) <= 2N - 2
  CH2 (chain + E_0 an end of T_+ + DEG-SPLIT D >= nS+kappa+T, kappa>=1):  n W <= 2N - 2
Kill test: a cell dies if the ceiling is < the floor for EVERY admissible profile.
Profiles: dicritical multisets {(s_l,mu_l)}, mu_l >= 2, sum s_l mu_l = W.  S = sum s_l.
"""
import re, math, itertools, sys

rows = {}
for line in open('/tmp/kpg/table.txt'):
    if line.startswith(' N ') or '```' in line: continue
    # two cells per line, fixed columns; split on '|' groups
    parts = [p for p in re.split(r'\s{2,}', line.rstrip('\n').strip()) if p]
    # simpler: regex each cell
    for m in re.finditer(r'(\d+)\s+(\d+)\|\s*(\d+)\s+(\S+)\s+(\S+)\s+(\S+)\|\s*(\d+)\s+(\d+)\s+(\d+)\|', line):
        N,W,MFb,B1,B2,B3,Phi,gain,C = m.groups()
        rows[(int(N),int(W))] = dict(MFb=int(MFb),B1=B1,B2=B2,B3=B3,Phi=int(Phi))
print("cells parsed:", len(rows))

def profiles(W):
    """all multisets {(s_l,mu_l)}: mu_l>=2, sum s_l*mu_l = W. return set of S values."""
    out=set()
    def rec(rem, minmu, S):
        if rem==0: out.add(S); return
        for mu in range(minmu, rem+1):
            for s in range(1, rem//mu+1):
                rec(rem-s*mu, mu+1, S+s)
    rec(W,2,0)
    return sorted(out)

print()
print(" N  W | Phi | S-values | CH1 max n | CH2 max n | CH1 kill | CH2 kill")
kills1=[]; kills2=[]
for (N,W) in sorted(rows):
    Phi = rows[(N,W)]['Phi']
    Ss = profiles(W)
    # CH1: n <= (2N-2)/(W-S)  ; worst (largest) over admissible S
    c1 = max((2*N-2)//(W-S) for S in Ss)
    c2 = (2*N-2)//W
    k1 = c1 < Phi
    k2 = c2 < Phi
    if k1: kills1.append((N,W))
    if k2: kills2.append((N,W))
    print(f"{N:3d} {W:2d} | {Phi:3d} | {str(Ss):10s} | {c1:6d}    | {c2:6d}    | {str(k1):5s}    | {k2}")
print()
print("CH1 (chain only) kills:", kills1)
print("CH2 (chain + E0 end)  kills:", kills2)

print()
print("=== delta_aff ceiling induced by CH1 (chain):  delta_aff <= p_a(n_max) ===")
print(" N | max over W of  n_max(CH1) | p_a  || (B2) death thr | reached?")
for N in sorted(set(n for n,_ in rows)):
    best=0; bw=None
    for (NN,W) in rows:
        if NN!=N: continue
        Ss=profiles(W)
        c1=max((2*N-2)//(W-S) for S in Ss)
        if c1>best: best,bw=c1,W
    pa=(best-1)*(best-2)//2
    thr = 3 if N<=10 else 1
    print(f"{N:3d} | n<= {best:3d} (at W={bw})        | {pa:4d} || {thr:2d}            | {'YES' if pa<=thr else 'no'}")
