import sys, itertools
from fractions import Fraction as F
from math import gcd
sys.path.insert(0,'box')
import moh_skeleton_full as MS

# ---- the (75,50) discriminator, in full -------------------------------------
rows=[]
for (m,Ms,V) in MS.census(75, Kmin=1, full=True):
    S=MS.Skel(75,m,Ms,V)
    rows.append(S)
print("(75,50)-class rows under (1)-(13), Kmin=1, n=75:", len([r for r in rows if r.m==50]))
hdr=f"{'m':>3} {'M*':>12} {'V':>16} {'d':>16} {'A2':>3} {'tri2':>4} {'sq2':>3} {'A1':>3} {'d2':>7} {'d1':>7} {'q':>7} {'u':>5} {'b10':>4} {'b11':>4}"
print(hdr)
for S in rows:
    if S.m!=50: continue
    tri,sq,A,Q=S.div9(2)
    ok,b10,b11=S.cond1011(2)
    print(f"{S.m:>3} {str(list(Ms for Ms in [ [S.M[i] for i in range(2,S.s+1)] ])[0]):>12} "
          f"{str({i:S.V[i] for i in range(2,S.s+2)}):>16} {str({i:S.d[i] for i in range(1,S.s+2)}):>16} "
          f"{A:>3} {tri:>4} {sq:>3} {S.A(1):>3} {str(S.delta[2]):>7} {str(S.delta[1]):>7} {str(S.q()):>7} {str(S.u):>5} {str(b10):>4} {str(b11):>4}")
