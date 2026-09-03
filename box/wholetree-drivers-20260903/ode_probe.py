import sys; sys.path.insert(0,'.')
from fractions import Fraction as F
from math import gcd
import moh_skeleton_full_frozen as B, opus5_probe as OP
rows=[(n,m,Ms,V) for n in range(4,101) for m,Ms,V in B.census(n,Kmin=2,full=True)]
def S(kw):
    return {(n,m,tuple(Ms),tuple(sorted(V.items()))) for n,m,Ms,V in rows
            if OP.Tree(n,m,Ms,**kw).embeds(V) is not None}
t   = S({}); to = S(dict(ode=True)); tp = S(dict(ode=True,capacity=True,passport=True))
print("bare tree",len(t)," +ODE",len(to)," +passport",len(tp))
print("\nrows killed by the ODE step (3.7):")
for k in sorted(t-to):
    n,m,Ms,V = k[0],k[1],k[2],dict(k[3])
    T=OP.Tree(n,m,Ms)
    hi=(V[T.s],)
    for j in range(T.s-1,1,-1):
        dl,L,A,P,Q,lo=T.node(j,hi)
        exact = F(P,Q)
        print(f"  {k[:3]} V={V}:  D_{j}: P={P} Q={Q} P/Q={exact} threshold={lo} "
              f"integral-P/Q={exact.denominator==1} selectedV={V[j]}")
        hi=(V[j],)+hi
print("\nrows killed by the passport step (3.8):")
for k in sorted(to-tp):
    n,m,Ms,V=k[0],k[1],k[2],dict(k[3])
    T=OP.Tree(n,m,Ms,ode=True)
    w=T.embeds(V); print(f"  {k[:3]} V={V}  bare/ODE witness b={w['b']} orbits={w['orbits']} "
                         f"A={w['A']} P={w['P']} Q={w['Q']} S={(w['Q']-1)//w['A']}")
    b,orb,A,P,Q=w['b'],w['orbits'],w['A'],w['P'],w['Q']; Ss=(Q-1)//A
    W=[(P-Q*b)//A]+[P-Q*u for u in orb]+[P]*(Ss-len(orb)); g=0
    for x in W: g=gcd(g,abs(x))
    print(f"        W={W} g={g} d_+={sum(x for x in W if x>0)} d_+/g={sum(x for x in W if x>0)//g} vs S={Ss}")
