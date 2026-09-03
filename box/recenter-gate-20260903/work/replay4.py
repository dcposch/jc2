"""Free set on the selected chain (replicating whole-tree-review-opus5 7.3):
for each level i, window (delta_{i+1}, delta_i), lattice (1/L_i)Z with
L_i = lcm(den delta_s .. den delta_{i+1}); free = lattice pts strictly inside,
minus the integral ones (removable by Moh p.190 y -> y - ax - b)."""
import sys, json, ast
from fractions import Fraction as F
from math import lcm
sys.path.insert(0,'.')
import full_tree_partition as FT
import repro.moh_skeleton_full as M

IN='/tmp/jc2-lane.4VL5oJ/inputs/'
d52=json.load(open(IN+'full-tree-ode-excess-witnesses.json'))
d14=json.load(open(IN+'full-tree-polynomial-ode-excess-witnesses.json'))

def chain_path(key, w):
    n,m,Ms,Vs=ast.literal_eval(key)
    S=M.Skel(n,m,list(Ms),dict(Vs))
    E=FT.evaluator(S, ode_nondegenerate=True)
    path=list(E.initial_path())
    ww=w
    while isinstance(ww,dict) and 'j' in ww:
        path[ww['j']]=ww['selected_V']; ww=ww.get('selected_child')
    path=tuple(path)
    delta={i:E.radius(i,path) for i in range(1,S.s+1)}
    return S,delta

def free_set(S,delta):
    out=[]
    L=1
    for i in range(S.s-1,0,-1):
        L=lcm(L, delta[i+1].denominator)
        lo,hi=delta[i+1],delta[i]
        k=lo.numerator*L//lo.denominator
        e=F(k,L)
        while e<=lo: k+=1; e=F(k,L)
        while e<hi:
            if e.denominator!=1: out.append((i,e))
            k+=1; e=F(k,L)
    return out

def report(d,label):
    empty=0; rows=[]
    for k,w in d.items():
        S,delta=chain_path(k,w)
        fs=free_set(S,delta)
        if not fs: empty+=1
        rows.append((k,[str(delta[i]) for i in range(S.s,0,-1)],[f"{i}:{e}" for i,e in fs]))
    print(f"{label}: {len(d)} rows, free-set EMPTY on {empty}, NON-EMPTY on {len(d)-empty}")
    return rows,empty

killed={k:w for k,w in d52.items() if k not in d14}
r1,e1=report(killed,"38 POLY-killed rows        ")
r2,e2=report(d14,   "14 POLY+ODE survivors      ")
print()
print("sample of the 38 (row, radii top->bottom, free set):")
for row in r1[:6]: print("  ",row[0]); print("      delta=",row[1]," free=",row[2])
print()
print("=== Moh's six (control, reproduces charged 7.3 table) ===")
dp=json.load(open('/home/ubuntu/jc2/box/mohprog-drivers-20260903/full-tree-ode-printed-witnesses.json'))
for k,w in dp.items():
    S,delta=chain_path(k,w); fs=free_set(S,delta)
    print(f"  {k}  delta={[str(delta[i]) for i in range(S.s,0,-1)]} free={[str(e) for _,e in fs] or 'EMPTY'}")
