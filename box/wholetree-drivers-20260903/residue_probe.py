import sys; sys.path.insert(0,'.')
from fractions import Fraction as F
import moh_skeleton_full_frozen as B, opus5_probe as OP

def surv_at(n, m=None, Kmin=2, **kw):
    out=[]
    for mm, Ms, V in B.census(n, Kmin=Kmin, full=True):
        if m is not None and mm != m: continue
        T = OP.Tree(n, mm, Ms, **kw)
        if kw.pop('_nod', False): pass
        r = T.embeds(V)
        if r is not None: out.append((mm, tuple(Ms), tuple(sorted(V.items()))))
    return out

def partition_only(n, m=None, Kmin=2, **kw):
    out=[]
    for mm, Ms, V in B.census(n, Kmin=Kmin, full=True):
        if m is not None and mm != m: continue
        T = OP.Tree(n, mm, Ms, **kw); T._memo={}
        if not (T.d[T.s] > V[T.s] > F(T.d[T.s],2)): continue
        need = tuple(V[i] for i in range(T.s-1,1,-1))
        if T.ok(T.s-1,(V[T.s],), False, need) is not None:
            out.append((mm, tuple(Ms), tuple(sorted(V.items()))))
    return out

print("== (75,50) residue ==")
for lbl, f, kw in (("baseline", None, {}),
                   ("partition-only", partition_only, {}),
                   ("partition+ODE+passport", partition_only, dict(ode=True,capacity=True,passport=True)),
                   ("GATED tree", surv_at, dict(gate=True)),
                   ("GATED+ODE+passport", surv_at, dict(gate=True,ode=True,capacity=True,passport=True)),
                   ("ungated C_FULL_TREE", surv_at, {}),
                   ("ungated+ODE+passport", surv_at, dict(ode=True,capacity=True,passport=True))):
    if f is None:
        rs = [(m,tuple(Ms),tuple(sorted(V.items()))) for m,Ms,V in B.census(75,Kmin=2,full=True) if m==50]
    else:
        rs = f(75, 50, **kw)
    pairs = sorted({(r[1][0], dict(r[2])[2]) for r in rs})
    print(f"  {lbl:24s} {len(rs):3d} rows  (M2,V2) = {pairs}")

print("\n== D=105 / D=117 (Kmin=16 census, as in the charged D-tables) ==")
for D in (105, 117):
    for lbl, f, kw in (("baseline", None, {}),
                       ("partition-only", partition_only, {}),
                       ("partition+ODE+pass", partition_only, dict(ode=True,capacity=True,passport=True)),
                       ("GATED tree", surv_at, dict(gate=True)),
                       ("GATED+ODE+pass", surv_at, dict(gate=True,ode=True,capacity=True,passport=True)),
                       ("ungated C_FULL_TREE", surv_at, {}),
                       ("ungated+ODE+pass", surv_at, dict(ode=True,capacity=True,passport=True))):
        if f is None:
            rs=[(m,tuple(Ms),tuple(sorted(V.items()))) for m,Ms,V in B.census(D,Kmin=16,full=True)]
        else:
            rs=f(D, None, Kmin=16, **kw)
        grp = {(r[0],r[1],dict(r[2])[max(dict(r[2]))]) for r in rs}
        print(f"  D={D} {lbl:22s} rows={len(rs):3d} groups={len(grp):3d}")
