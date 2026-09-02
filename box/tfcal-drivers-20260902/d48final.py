#!/usr/bin/env python3
"""Where every D=48 skeleton dies, filter by filter; plus the machine check that
   Moh's six published rows survive (10) and (10)_1."""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moh_skeleton_N import Skel, census, MOH_SURVIVORS
from d1floor import qval
from mohcond import moh10, star_congruence, Delta

print("== A. Moh's six published rows against (10) and (10)_1 (fail-closed) ==")
print("   %-22s %-10s %-6s %-6s %-6s %-8s %-8s" % ("row","delta_1","L_1","Delta_1","a_1","a_1 mod","verdict"))
bad=0
for (n,m,Ms,Vs,lab,_) in MOH_SURVIVORS:
    S=Skel(n,m,list(Ms),Vs); D1=Delta(S,1); a1=S.e*S.V[2]
    ok = moh10(S) and star_congruence(S)
    if not ok: bad+=1
    from math import lcm
    L=1
    for i in range(2,S.s+1): L=lcm(L,S.delta[i].denominator)
    print("   %-22s %-10s %-6d %-6d %-6d %-8d %-8s" % (lab,S.delta[1],L,D1,a1,a1%D1,"PASS" if ok else "FAIL"))
print("   -> %d of 6 fail" % bad)
assert bad==0, "reconstruction contradicts Moh's own table"

print("\n== B. D=48: the funnel ==")
D=48; Nlo,Nhi=6,16
stage={ 'census':0,'windows':0,'(10)':0,'(10)_1':0 }
g_all={}; g10={}; g11={}
for (m,Ms,V) in census(D):
    S=Skel(D,m,list(Ms),V)
    stage['census']+=1
    if not S.windows_ok(): continue
    stage['windows']+=1
    key=(m,Ms,S.V[S.s]); g_all.setdefault(key,[]).append(S)
    if moh10(S):
        stage['(10)']+=1; g10.setdefault(key,[]).append(S)
        if star_congruence(S):
            stage['(10)_1']+=1; g11.setdefault(key,[]).append(S)
print("   V-assignments: census %d, Def 5.1(2) windows %d, Moh (10) %d, +(10)_1 %d"
      % (stage['census'],stage['windows'],stage['(10)'],stage['(10)_1']))
print("   groups: %d -> (10) %d -> (10)_1 %d" % (len(g_all),len(g10),len(g11)))
print("\n   the %d V-assignments that pass Moh (10), and why each fails (10)_1:" % stage['(10)'])
print("   %-16s %-4s %-12s %-9s %-9s %-6s %-6s %-6s %-4s %s" %
      ("M_2..M_s","V_s","V_2..V_s","delta_1","delta_2","L_1","Delta_1","a_1","mod","(10)_1"))
from math import lcm
seen=set()
for key in sorted(g10):
    for S in g10[key]:
        L=1
        for i in range(2,S.s+1): L=lcm(L,S.delta[i].denominator)
        D1=Delta(S,1); a1=S.e*S.V[2]
        print("   %-16s %-4d %-12s %-9s %-9s %-6d %-6d %-6d %-4d %s" %
              (str(list(key[1])),key[2],str([S.V[i] for i in range(2,S.s+1)]),
               S.delta[1],S.delta[2],L,D1,a1,a1%D1,"PASS" if star_congruence(S) else "FAIL"))
print("\n   => D = 48 is EMPTY after (10)+(10)_1 (before any N-filter).")
