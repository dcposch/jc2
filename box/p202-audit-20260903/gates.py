#!/usr/bin/env python3
"""Reproduce the four MEASURED candidate gates on Moh's n<=100 (1)-(13) census.
Fail-closed: 6/6 printed rows kept; (75,50) residue printed. Desk-scale."""
import sys, os, time
from fractions import Fraction as F
from collections import defaultdict

sys.path.insert(0, "/home/ubuntu/jc2/box")
import moh_skeleton_full as M
from moh_skeleton_full import Skel, census, uni_hits, MOH_TABLE

t0 = time.time()
rows = []
for n in range(4, 101):
    for (m, Ms, V) in census(n, Kmin=2, full=True):
        S = Skel(n, m, list(Ms), V)
        rows.append(S)
print("BASE (1)-(13) n<=100: %d rows / %d classes  [%.1fs]"
      % (len(rows), len(set((S.n, S.m) for S in rows)), time.time()-t0))

PRINTED = [(n, m, tuple(Ms), tuple(sorted(Vs.items())))
           for (n, m, Ms, Vs, *_) in MOH_TABLE]

def key(S):
    return (S.n, S.m, tuple(S.M[i] for i in range(2, S.s+1)),
            tuple(sorted((i, S.V[i]) for i in range(2, S.s+1))))

def cls(ss):
    return len(set((S.n, S.m) for S in ss))

def kept(ss):
    got = set(key(S) for S in ss)
    return sum(1 for p in PRINTED if p in got), [p for p in PRINTED if p not in got]

def force10(S):
    """printed nonzero branch (10) chosen at EVERY level j in {2..s-1}."""
    if S.s < 3:
        return False
    return all(S.cond1011(j)[1] for j in range(S.s-1, 1, -1))

def any10(S):
    return S.any10()

def incr(S):
    return all(S.A(j) >= 2 for j in range(1, S.s))

def major(S):
    return all(S.V[j] >= 2 for j in range(2, S.s+1))

def M2_gt_n_d2(S):
    return S.M[2] > S.n - S.d[2]

def M2_gt_m(S):
    return S.M[2] > S.m

def A_s1_div_nm(S):
    return (S.n - S.m) % S.A(S.s-1) == 0

def has_int_N(S, Nlo=6):
    items = [(S.V[2], S.q(), S.u)]
    return bool(uni_hits(items, Nlo, None))

def dump(name, pred):
    ss = [S for S in rows if pred(S)]
    k, miss = kept(ss)
    r50 = [S for S in ss if (S.n, S.m) == (75, 50)]
    print("\n== %s ==" % name)
    print("   rows %d / classes %d ; printed kept %d/6 missing %s"
          % (len(ss), cls(ss), k, miss if miss else "NONE"))
    print("   (75,50) residue: %d rows  %s"
          % (len(r50), [(S.M[2], S.V[2], S.V[3]) for S in r50]))
    return ss

s_m2 = dump("SOL M2 > n-d2", M2_gt_n_d2)
s_f10 = dump("SOL forced-(10) every j", force10)
s_both = dump("SOL M2>n-d2 AND forced-(10)", lambda S: M2_gt_n_d2(S) and force10(S))
f_m2m = dump("FABLE M2 > m", M2_gt_m)
f_m2mN = dump("FABLE M2 > m AND integral N>=6 (UNI)", lambda S: M2_gt_m(S) and has_int_N(S))
o_inc = dump("OPUS INCREMENT A_j>=2 all j", incr)
o_na11 = dump("OPUS NOT-ALL-(11) = any10", any10)
o_maj = dump("OPUS MAJOR-MULT V_j>=2 all j", major)
o_3 = dump("OPUS INCREMENT AND NOT-ALL-(11) AND MAJOR-MULT",
           lambda S: incr(S) and any10(S) and major(S))
a_div = dump("SOL unlicensed A_{s-1} | (n-m)", A_s1_div_nm)

print("\n== 2x2 of Sol's two clauses ==")
A = M2_gt_n_d2; B = force10
for a in (True, False):
    for b in (True, False):
        ss = [S for S in rows if A(S)==a and B(S)==b]
        k,_ = kept(ss)
        print("   M2>n-d2=%s  forced10=%s : %d rows / %d cls  printed %d/6"
              % (a, b, len(ss), cls(ss), k))

print("\n== 2x2x2 : Sol-conj  x  Fable M2>m  x  Opus MAJOR-MULT ==")
C = lambda S: M2_gt_n_d2(S) and force10(S)
D = M2_gt_m
E = major
for c in (True, False):
    for d in (True, False):
        for e in (True, False):
            ss = [S for S in rows if C(S)==c and D(S)==d and E(S)==e]
            k,_ = kept(ss)
            print("   Sol10=%s FableM2m=%s Major=%s : %4d rows / %2d cls  printed %d/6"
                  % (c, d, e, len(ss), cls(ss), k))

print("\n== 2x2x2 of Sol two clauses x Fable M2>m ==")
for a in (True, False):
    for b in (True, False):
        for d in (True, False):
            ss = [S for S in rows if A(S)==a and B(S)==b and D(S)==d]
            k,_ = kept(ss)
            print("   M2n-d2=%s f10=%s M2>m=%s : %4d / %2d  printed %d/6"
                  % (a, b, d, len(ss), cls(ss), k))

print("\n== 2x2x2 of Sol two clauses x Opus MAJOR-MULT ==")
for a in (True, False):
    for b in (True, False):
        for e in (True, False):
            ss = [S for S in rows if A(S)==a and B(S)==b and E(S)==e]
            k,_ = kept(ss)
            print("   M2n-d2=%s f10=%s Major=%s : %4d / %2d  printed %d/6"
                  % (a, b, e, len(ss), cls(ss), k))

print("\n== implications (predicate P => Q on the 658) ==")
preds = [
    ("M2>n-d2", M2_gt_n_d2),
    ("forced10", force10),
    ("Sol-conj", C),
    ("M2>m", M2_gt_m),
    ("M2>m+N>=6", lambda S: M2_gt_m(S) and has_int_N(S)),
    ("INCREMENT", incr),
    ("NOT-ALL-11", any10),
    ("MAJOR-MULT", major),
    ("Opus-3", lambda S: incr(S) and any10(S) and major(S)),
    ("A_s1|(n-m)", A_s1_div_nm),
]
sets = {name: [S for S in rows if p(S)] for name, p in preds}
for n1, _ in preds:
    for n2, _ in preds:
        if n1 == n2: continue
        s1, s2 = sets[n1], sets[n2]
        k1 = set(id(S) for S in s1); k2 = set(id(S) for S in s2)
        if k1 <= k2:
            print("   %s  =>  %s   (%d => %d)" % (n1, n2, len(s1), len(s2)))

print("\n== Sol's TEN rows (full data) ==")
def show(S, tag=""):
    d2 = S.d[2]
    print("   %s n=%d m=%d M=%s V=%s  d=%s  delta=%s  A=%s"
          % (tag, S.n, S.m,
             [S.M[i] for i in range(1, S.s+1)],
             {i: S.V[i] for i in range(2, S.s+1)},
             {i: S.d[i] for i in range(1, S.s+2)},
             {i: str(S.delta[i]) for i in range(1, S.s+1)},
             {j: S.A(j) for j in range(1, S.s)}))
    print("      e=%d d*=%d  M2=%s  n-d2=%s (n=%s d2=%s) M2>n-d2=%s ; M2>m=%s (m=%s)"
          % (S.e, S.dd, S.M[2], S.n-d2, S.n, d2, S.M[2] > S.n-d2, S.M[2] > S.m, S.m))
    print("      force10=%s any10=%s incr=%s major=%s As-1|(n-m)=%s N>=6=%s q=%s u=%s"
          % (force10(S), any10(S), incr(S), major(S), A_s1_div_nm(S),
             has_int_N(S), S.q(), S.u))
    for j in range(S.s-1, 1, -1):
        ok, b10, b11 = S.cond1011(j)
        tri, sq, Aj, Q = S.div9(j)
        print("      j=%d (10)=%s (11)=%s TRI=%s SQ=%s A=%s Q=%s V=%s"
              % (j, b10, b11, tri, sq, Aj, Q, S.V[j]))
    ok, b12, b13 = S.cond1213()
    print("      (12)=%s (13)=%s A1=%s  u_s=%s"
          % (b12, b13, S.A(1), S.d[S.s]-S.V[S.s]))

printed_keys = set(PRINTED)
print("-- printed six --")
for S in s_both:
    if key(S) in printed_keys:
        show(S, "PRINTED")
print("-- four extras --")
extras = []
for S in s_both:
    if key(S) not in printed_keys:
        show(S, "EXTRA")
        extras.append(S)

print("\n== Fable 33 (M2>m + N>=6 UNI) minus printed, and vs Sol ten ==")
f33 = [S for S in rows if M2_gt_m(S) and has_int_N(S)]
sol10 = s_both
sk = set(id(S) for S in sol10)
fk = set(id(S) for S in f33)
print("   |Sol10|=%d |Fable33|=%d  intersection=%d"
      % (len(sol10), len(f33), len(sk & fk)))
print("   Sol10 \\ Fable33:")
for S in sol10:
    if id(S) not in fk:
        print("      n=%d m=%d M=%s V=%s  N-hits=%s  M2>m=%s"
              % (S.n, S.m, [S.M[i] for i in range(2,S.s+1)],
                 {i:S.V[i] for i in range(2,S.s+1)},
                 sorted(uni_hits([(S.V[2], S.q(), S.u)], 6, None)),
                 M2_gt_m(S)))
print("   Fable33 \\ Sol10:")
for S in f33:
    if id(S) not in sk:
        pk = "P" if key(S) in printed_keys else " "
        print("      %s n=%d m=%d M=%s V=%s  force10=%s M2>n-d2=%s N=%s"
              % (pk, S.n, S.m, [S.M[i] for i in range(2,S.s+1)],
                 {i:S.V[i] for i in range(2,S.s+1)},
                 force10(S), M2_gt_n_d2(S),
                 sorted(uni_hits([(S.V[2], S.q(), S.u)], 6, None))))

print("\n== (75,50) ALL 9 rows through every gate ==")
r75 = [S for S in rows if (S.n, S.m)==(75,50)]
print("   %-8s %-8s %-6s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s"
      % ("M2","V2","V3","n-d2","M2>n-d2","f10","M2>m","incr","any10","major","As1|nm","N>=6"))
for S in sorted(r75, key=lambda S: (S.M[2], S.V[2])):
    print("   %-8s %-8s %-6s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s"
          % (S.M[2], S.V[2], S.V[3], S.n-S.d[2],
             M2_gt_n_d2(S), force10(S), M2_gt_m(S), incr(S), any10(S),
             major(S), A_s1_div_nm(S), has_int_N(S)))
    show(S, "75-50")

print("\n== falsifier (75,50,M2=40,V2=1) detail ==")
for S in r75:
    if S.M[2]==40 and S.V[2]==1:
        show(S, "FALSIFIER")
        print("      d2=%s  n-d2=%s  M2=%s  so M2>n-d2 is %s"
              % (S.d[2], S.n-S.d[2], S.M[2], S.M[2] > S.n-S.d[2]))
        print("      d3=%s d4=%s s=%s K=%s"
              % (S.d[3], S.d.get(4), S.s, S.K))

print("\n== Prop 5.3 / descent data for ten rows ==")
for S in list(s_both):
    ds = S.d[S.s]; us = S.d[S.s]-S.V[S.s]
    tag = "P" if key(S) in printed_keys else "E"
    print("   %s (n,m)=(%d,%d) M=%s V=%s  d_s=%s V_s=%s u_s=%s  n/ds=%s m/ds=%s M/ds=%s"
          % (tag, S.n, S.m, [S.M[i] for i in range(2,S.s+1)],
             {i:S.V[i] for i in range(2,S.s+1)},
             ds, S.V[S.s], us,
             S.n/ds if ds else None, S.m/ds if ds else None,
             [S.M[i]/ds for i in range(2,S.s+1)] if ds else None))
    # Lemma 6.1 style: delta_{s-1} >= 0 ?
    print("      delta_s=%s delta_{s-1}=%s  (>=0? %s)  M_{s-1}=%s  n-d_{s-1}=%s"
          % (S.delta[S.s], S.delta[S.s-1], S.delta[S.s-1] >= 0,
             S.M[S.s-1], S.n - S.d[S.s-1]))

print("\nDONE in %.1fs" % (time.time()-t0))
