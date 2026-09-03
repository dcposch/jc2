import sys, json
from fractions import Fraction
sys.path.insert(0,'.')
import full_tree_partition as FT
import repro.moh_skeleton_full as M

FIRED=[]
_cg=FT.TreePartition.child_global; _ce=FT.TreePartition.child_embed
def wrap(orig,tag):
    def f(self,j,path,value,is_zero,dangerous,*a):
        dj=self.radius(j,path)
        if self.polynomial_recenter and dj.denominator==1 and dj<=0 and not is_zero and dangerous:
            FIRED.append((tag,j,str(dj),value))
        return orig(self,j,path,value,is_zero,dangerous,*a)
    return f
FT.TreePartition.child_global=wrap(_cg,'g'); FT.TreePartition.child_embed=wrap(_ce,'e')

print("=== K=16 ray (n=48t+16, m=32t+16, M=(n-12,n-2), V2=V3=3) ===")
for t in range(1,13):
    n=48*t+16; m=32*t+16; Ms=[n-12,n-2]; V={2:3,3:3}
    S=M.Skel(n,m,Ms,V)
    FIRED.clear()
    ode=FT.full_tree_ode_ok(S); poly=FT.full_tree_polynomial_ode_ok(S)
    E=FT.evaluator(S,polynomial_recenter=True,ode_nondegenerate=True)
    d2=E.radius(2,E.initial_path()); d3=E.radius(3,E.initial_path())
    w=FT.evaluator(S,ode_nondegenerate=True).embeds(S)[1]
    print(f" t={t:2d} (n,m)=({n},{m}) s={S.s} delta2={d2} ODE={ode} POLY+ODE={poly} "
          f"selected_mode@j=2={w.get('selected_mode')} rule_fired={len(FIRED)}")

print()
print("=== Moh's six printed rows ===")
for row in M.MOH_TABLE:
    n,m,Ms,Vs=row[0],row[1],row[2],row[3]
    S=M.Skel(n,m,list(Ms),dict(Vs))
    FIRED.clear()
    ode=FT.full_tree_ode_ok(S); poly=FT.full_tree_polynomial_ode_ok(S)
    E=FT.evaluator(S,ode_nondegenerate=True)
    w=E.embeds(S)[1]; ch=[]
    ww=w
    while isinstance(ww,dict) and 'j' in ww:
        ch.append((ww['j'],ww['delta'],ww.get('selected_mode'))); ww=ww.get('selected_child')
    print(f" ({n},{m}) M={tuple(Ms)} V={dict(Vs)} s={S.s} ODE={ode} POLY+ODE={poly} chain={ch} rule_fired={len(FIRED)}")
