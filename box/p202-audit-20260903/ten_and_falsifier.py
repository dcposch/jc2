#!/usr/bin/env python3
"""Ten-row table extras + Lemma 6.1 numbers + falsifier identities (sympy)."""
import sys
from fractions import Fraction as F
sys.path.insert(0, "/home/ubuntu/jc2/box")
from moh_skeleton_full import Skel, census, uni_hits, MOH_TABLE

rows = []
for n in range(4, 101):
    for (m, Ms, V) in census(n, Kmin=2, full=True):
        rows.append(Skel(n, m, list(Ms), V))

def force10(S):
    return S.s >= 3 and all(S.cond1011(j)[1] for j in range(S.s-1, 1, -1))

sol10 = [S for S in rows if S.M[2] > S.n - S.d[2] and force10(S)]
printed = set((n,m,tuple(Ms),tuple(sorted(Vs.items()))) for (n,m,Ms,Vs, *_) in MOH_TABLE)

def k(S):
    return (S.n,S.m,tuple(S.M[i] for i in range(2,S.s+1)),
            tuple(sorted((i,S.V[i]) for i in range(2,S.s+1))))

print("TEN-ROW FACTOR DATA")
print("%-8s %-4s %-4s %-14s %-12s %4s %4s %6s %6s %4s %4s %5s %5s %4s %5s %6s %s" %
      ("tag","n","m","M","V","d2","ds","n-d2","n-m","A2","TRI","SQ","(10)","(11)",
       "us","Lem61","desc"))
for S in sol10:
    tag = "P" if k(S) in printed else "E"
    tri, sq, A2, Q = S.div9(2)
    ok, b10, b11 = S.cond1011(2)
    us = S.d[S.s] - S.V[S.s]
    # Lemma 6.1: u_s(n-M_{s-1}) - d_s >= 0
    lem = us*(S.n - S.M[S.s-1]) - S.d[S.s]
    ds = S.d[S.s]
    desc = "(%g,%g,M2=%g,V2=%s,J=X^%s)" % (
        S.n/ds, S.m/ds, S.M[2]/ds, S.V[2], S.V[S.s]-2)
    print("%-8s %-4d %-4d %-14s %-12s %4d %4d %6d %6d %4d %4d %5d %5s %4s %5d %6s %s" %
          (tag, S.n, S.m, str([S.M[i] for i in range(2,S.s+1)]),
           str({i:S.V[i] for i in range(2,S.s+1)}),
           S.d[2], ds, S.n-S.d[2], S.n-S.m, A2, tri, sq, b10, b11, us, lem, desc))
    print("         delta=%s A=%s e,d*=%s,%s  Q=%s  (12/13)=%s/%s  As1|(n-m)=%s  lo2=%s"
          % ({i:str(S.delta[i]) for i in range(1,S.s+1)},
             {j:S.A(j) for j in range(1,S.s)}, S.e, S.dd, Q,
             S.cond1213()[1], S.cond1213()[2],
             (S.n-S.m) % S.A(S.s-1) == 0,
             str(F(S.d[2], S.n-S.M[2]))))

print("\nFABLE33 keys vs SOL10")
f33 = [S for S in rows if S.M[2] > S.m and uni_hits([(S.V[2],S.q(),S.u)],6,None)]
sk, fk = set(id(S) for S in sol10), set(id(S) for S in f33)
print("symdiff sizes: Sol\\F=%d F\\Sol=%d inter=%d" %
      (len(sk-fk), len(fk-sk), len(sk&fk)))

print("\n== sympy falsifier identities ==")
import sympy as sp
b, pi = sp.symbols('b pi', complex=True)
p = pi**3 + (sp.Rational(3,2)*b)*pi
q = pi**2 + b
# D(a,b,p,q) = a p q' - b q p'   with a=3, b=2  (Moh Def 4.1)
Dp = sp.diff(p, pi); Dq = sp.diff(q, pi)
D = sp.simplify(3*p*Dq - 2*q*Dp)
Res = sp.simplify(sp.resultant(p, q, pi))
disc_p = sp.simplify(sp.discriminant(p, pi))
disc_q = sp.simplify(sp.discriminant(q, pi))
print("D(3,2,p,q) =", D)
print("Res(p,q)   =", Res)
print("disc(p)    =", disc_p)
print("disc(q)    =", disc_q)
# squarefree/coprime for b!=0
print("D is -3b^2:", sp.simplify(D + 3*b**2)==0)
print("Res is b^3/4:", sp.simplify(Res - b**3/4)==0)
# C2: p(-pi) = -p(pi) odd; q even
print("p odd:", sp.expand(p.subs(pi, -pi) + p)==0)
print("q even:", sp.expand(q.subs(pi, -pi) - q)==0)

# r=2 numerical hypotheses for (75,50,40,1)
S = [T for T in rows if T.n==75 and T.m==50 and T.M[2]==40 and T.V[2]==1][0]
print("\nFALSIFIER r=2 Prop 5.3 numbers")
print("V3=%s d2=%s d3=%s  deg p_D2 = V3*d2/d3 = %s" %
      (S.V[3], S.d[2], S.d[3], S.V[3]*S.d[2]//S.d[3]))
print("deg p_D1 (g) = V2*n/d2 =", S.V[2]*S.n//S.d[2])
print("deg q_star  = V2*m/d2 =", S.V[2]*S.m//S.d[2])
print("delta2=%s delta1=%s  delta1-delta2=%s" %
      (S.delta[2], S.delta[1], S.delta[1]-S.delta[2]))
tri, sq, A2, Q = S.div9(2)
print("A2=%s TRI=%s SQ=%s Q=%s  orbit A2*V2=%s  remainder Q-A2*V2=%s"
      % (A2, tri, sq, Q, A2*S.V[2], Q-A2*S.V[2]))
print("window lo V2 >", F(S.d[2], S.n-S.M[2]), "actual V2", S.V[2])
print("Lemma6.1 u_s(n-M2)-d_s =", (S.d[S.s]-S.V[S.s])*(S.n-S.M[2]) - S.d[S.s],
      "delta2>=0", S.delta[2]>=0)
print("descended (n,m,M2) =", (S.n/S.d[3], S.m/S.d[3], S.M[2]/S.d[3]),
      "n'-d2'=", S.n/S.d[3] - S.d[2]/S.d[3])

# Prop 5.3 claim deg q at construction D1 from D2
print("Prop5.3 deg q = V2*(n-M1)/d2 =", S.V[2]*(S.n - S.M[1])//S.d[2])

print("\nOpus-3 contains Sol10?",
      all((all(T.A(j)>=2 for j in range(1,T.s)) and T.any10()
           and all(T.V[j]>=2 for j in range(2,T.s+1))) for T in sol10))
print("A_s-1|(n-m) on Sol10 extras:")
for S in sol10:
    if k(S) not in printed:
        print(" ", S.n, S.m, S.M[2], S.A(S.s-1), S.n-S.m,
              (S.n-S.m)%S.A(S.s-1)==0)
