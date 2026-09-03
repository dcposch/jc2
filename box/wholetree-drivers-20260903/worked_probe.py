import sys; sys.path.insert(0,'.')
from fractions import Fraction as F
from math import gcd
import moh_skeleton_full_frozen as B, opus5_probe as OP

print("=== worked example 1: Moh's printed (99,66; M2=77,M3=97; V2=8,V3=8) ===")
n,m,Ms,V = 99,66,(77,97),{2:8,3:8}
T = OP.Tree(n,m,Ms, ode=True, capacity=True, passport=True)
S = B.Skel(n,m,list(Ms),V)
print(" d =", {k:S.d[k] for k in sorted(S.d)}, " deltas =", {k:str(S.delta[k]) for k in sorted(S.delta)})
dl,L,A,P,Q,lo = T.node(2,(V[3],))
print(f" D_2: delta_2={dl} L_2={L} A_2={A} P_2={P} Q_2={Q} threshold={lo}")
print(f"      (9): P_2 = {P} = {P//A}*{A} + {P%A}   so TRI={P//A}, SQ={P%A}")
print(f"      (10) V_2={V[2]} <= TRI={P//A}? {V[2] <= P//A};  (11) V_2 == SQ mod A? {(V[2]-P%A)%A==0}")
print(f"      A_2 | Q_2 - 1 ? {(Q-1)%A==0}   S=(Q-1)/A={(Q-1)//A}")
w = T.embeds(V)
print(" witness:", {k:w[k] for k in ('j','A','P','Q','b','mode','orbits','zero_major')})
b, orbits = w['b'], w['orbits']
Sslots = (Q-1)//A
W = [(P-Q*b)//A] + [P-Q*u for u in orbits] + [P]*(Sslots-len(orbits))
g = 0
for x in W: g = gcd(g, abs(x))
print(f" passport: S={Sslots}  W={W}  sum={sum(W)}  g={g}  d_+={sum(x for x in W if x>0)}"
      f"  d_+/g={sum(x for x in W if x>0)//g} >= S ? {sum(x for x in W if x>0)//g >= Sslots}")
print(" child (bottom):", w['child'])

print("\n=== worked example 2: excess rows killed WITHOUT Prop.5.6 (partition-only) ===")
found = 0
for n in range(4,101):
    if found >= 3: break
    for m, Ms, V in B.census(n, Kmin=2, full=True):
        T2 = OP.Tree(n,m,Ms); T2._memo={}
        if not (T2.d[T2.s] > V[T2.s] > F(T2.d[T2.s],2)): continue
        need = tuple(V[i] for i in range(T2.s-1,1,-1))
        if T2.ok(T2.s-1,(V[T2.s],), False, need) is not None: continue
        # locate the killing node/sibling
        if T2.s != 3: continue
        dl,L,A,P,Q,lo = T2.node(2,(V[T2.s],))
        bs = [b for b in range(P%A, P+1, A)]
        reasons=[]
        for b in bs:
            if not (F(b) > lo):
                reasons.append((b,'minor')); continue
            good,A1,c12,c13 = T2.bottom((b,V[3]))
            reasons.append((b, f"major zero sibling -> V_2={b}: A_1={A1} (12)={c12} (13)={c13}"
                            + ("" if good else "  FAILS")))
        if all('FAILS' in str(r[1]) for r in reasons):
            print(f"\n  (n,m)=({n},{m}) M={list(Ms)} V={dict(sorted(V.items()))}")
            print(f"    D_2: delta_2={dl} A_2={A} P_2={P} Q_2={Q} thr={lo}; "
                  f"selected V_2={V[2]} would embed, but")
            for b, r in reasons: print(f"      b={b}: {r}")
            found += 1
            if found >= 3: break
