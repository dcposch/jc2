"""Gate every Prop 5.6 kill on the branch's free set being empty (the 7.3
repair), with and without the delta=0 recentring, and count at n<=100."""
import sys
from fractions import Fraction as F
from math import lcm
sys.path.insert(0,'.')
import full_tree_partition as FT
import repro.moh_skeleton_full as M

def free_empty(self, path):
    delta={i:self.radius(i,path) for i in range(1,self.s+1)}
    L=1
    for i in range(self.s-1,0,-1):
        L=lcm(L, delta[i+1].denominator)
        lo,hi=delta[i+1],delta[i]
        k=lo.numerator*L//lo.denominator; e=F(k,L)
        while e<=lo: k+=1; e=F(k,L)
        while e<hi:
            if e.denominator!=1: return False
            k+=1; e=F(k,L)
    return True

GATE=[False]
_cg=FT.TreePartition.child_global; _ce=FT.TreePartition.child_embed
def wrap(orig, msg):
    def f(self,j,path,value,is_zero,dangerous,*a):
        if GATE[0] and j==2:
            newpath=self.extend(path,2,value)
            dj=self.radius(2,path)
            rem=self.polynomial_recenter and dj.denominator==1 and dj<=0
            if dangerous and (is_zero or rem) and not free_empty(self,newpath):
                # Prop 5.6 not available on this branch: it survives
                return self.bottom(newpath)
        return orig(self,j,path,value,is_zero,dangerous,*a)
    return f
FT.TreePartition.child_global=wrap(_cg,'g'); FT.TreePartition.child_embed=wrap(_ce,'e')

rows=[M.Skel(n,m,list(Ms),V) for n in range(4,101) for m,Ms,V in M.census(n,Kmin=2,full=True)]
printed={(n,m,tuple(Ms),tuple(sorted(Vs.items()))) for n,m,Ms,Vs,*_ in M.MOH_TABLE}
def run(tag,pr,od,gate):
    GATE[0]=gate; FT._EVALUATORS.clear()
    surv=set()
    for S in rows:
        if FT.evaluator(S,polynomial_recenter=pr,ode_nondegenerate=od).embeds(S)[0]:
            surv.add(FT.row_key(S))
    cls={(k[0],k[1]) for k in surv}
    print(f"{tag:34s} rows={len(surv):4d} classes={len(cls):3d} excess={len(surv-printed):4d} printed_killed={len(printed-surv)}")
    return surv
a=run("C_FULL_TREE_ODE (charged)",False,True,False)
b=run("C_FULL_TREE_POLY_ODE (charged)",True,True,False)
c=run("gated ODE (7.4 repair)",False,True,True)
d=run("gated POLY+ODE (repair + delta=0)",True,True,True)
print()
print("gap-free increment of the delta=0 recentring:", len(c)-len(d), "rows,",
      len({(k[0],k[1]) for k in c})-len({(k[0],k[1]) for k in d}), "classes")
print("charged (gapped) increment:", len(a)-len(b), "rows")

diff = sorted(c - d)
print()
print(f"the {len(diff)} rows killed GAP-FREE by the delta=0 recentring (gated ODE -> gated POLY+ODE):")
from collections import Counter
print("  by (n,m):", dict(Counter((k[0],k[1]) for k in diff)))
for k in diff[:6]: print("   ", k)
sel = sorted(a - b)
print(f"\nrows killed by the CHARGED (ungated) recentring: {len(sel)}; by (n,m):",
      dict(Counter((k[0],k[1]) for k in sel)))
print("survivors of gated POLY+ODE by (n,m):", dict(Counter((k[0],k[1]) for k in sorted(d))))
