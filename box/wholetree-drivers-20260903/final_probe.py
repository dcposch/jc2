import sys; sys.path.insert(0,'.')
from fractions import Fraction as F
import moh_skeleton_full_frozen as B, opus5_probe as OP
rows=[(n,m,Ms,V) for n in range(4,101) for m,Ms,V in B.census(n,Kmin=2,full=True)]
printed={(n,m,tuple(Ms),tuple(sorted(V.items()))) for n,m,Ms,V,*_ in B.MOH_TABLE}
def surv(**kw):
    part = kw.pop('_part', False)
    out=set()
    for n,m,Ms,V in rows:
        T=OP.Tree(n,m,Ms,**kw)
        if part:
            T._memo={}
            if not (T.d[T.s]>V[T.s]>F(T.d[T.s],2)): continue
            need=tuple(V[i] for i in range(T.s-1,1,-1))
            r=T.ok(T.s-1,(V[T.s],),False,need)
        else:
            r=T.embeds(V)
        if r is not None: out.add((n,m,tuple(Ms),tuple(sorted(V.items()))))
    return out
u55 = surv(ode=True,capacity=True,passport=True)
g204 = surv(gate=True,ode=True,capacity=True,passport=True)
p330 = surv(_part=True, ode=True,capacity=True,passport=True)
for lbl, s in (("ungated tree+ODE+passport (charged 55)", u55),
               ("gap-free gated tree+ODE+passport", g204),
               ("partition-only+ODE+passport", p330)):
    cl = sorted({(k[0],k[1]) for k in s})
    print(f"\n{lbl}: {len(s)} rows, {len(cl)} (n,m) classes")
    print("  classes:", cl)
    print("  excess classes (not printed):",
          sorted({(k[0],k[1]) for k in s} - {(k[0],k[1]) for k in printed}))
# D=105 gated survivors and their UNI status
print("\nD=105 survivors under the gap-free gated screen (Kmin=16 census):")
for m,Ms,V in B.census(105,Kmin=16,full=True):
    T=OP.Tree(105,m,Ms,gate=True,ode=True,capacity=True,passport=True)
    if T.embeds(V) is None: continue
    S=B.Skel(105,m,list(Ms),V)
    items=[(S.V[2],S.q(),S.u)]
    print(f"  m={m} M={list(Ms)} V={dict(sorted(V.items()))} q={S.q()} u={S.u} "
          f"UNI alive N>=6: {B.uni_hits(items,6,None)}")
