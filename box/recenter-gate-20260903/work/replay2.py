"""Instrument the frozen POLY rule: log every radius at which it fires, over the
whole n<=100 enumeration; and re-derive the audit numbers in-process."""
import sys, json
from collections import Counter
from fractions import Fraction
sys.path.insert(0,'.')
import full_tree_partition as FT
import repro.moh_skeleton_full as M

FIRE=Counter(); ALLNEG=Counter(); ALLDELTA=Counter()
_cg=FT.TreePartition.child_global; _ce=FT.TreePartition.child_embed
def wrap(orig):
    def f(self,j,path,value,is_zero,dangerous,*a):
        dj=self.radius(j,path)
        ALLDELTA[str(dj)]+=1
        if dj<=0: ALLNEG[str(dj)]+=1
        if self.polynomial_recenter and dj.denominator==1 and dj<=0 and not is_zero and dangerous:
            FIRE[str(dj)]+=1
        return orig(self,j,path,value,is_zero,dangerous,*a)
    return f
FT.TreePartition.child_global=wrap(_cg); FT.TreePartition.child_embed=wrap(_ce)

rows=[M.Skel(n,m,list(Ms),V) for n in range(4,101) for m,Ms,V in M.census(n,Kmin=2,full=True)]
printed={(n,m,tuple(Ms),tuple(sorted(Vs.items()))) for n,m,Ms,Vs,*_ in M.MOH_TABLE}
res={}
for tag,pr,od in (("FULL_TREE_ODE",False,True),("FULL_TREE_POLY_ODE",True,True),
                  ("FULL_TREE",False,False),("FULL_TREE_POLY",True,False)):
    surv=set()
    for S in rows:
        E=FT.evaluator(S,polynomial_recenter=pr,ode_nondegenerate=od)
        if E.embeds(S)[0]: surv.add(FT.row_key(S))
    cls={(k[0],k[1]) for k in surv}
    res[tag]=(len(surv),len(cls),len(surv-printed),len(printed-surv))
    print(f"{tag}: rows={len(rows)} survivors={len(surv)} classes={len(cls)} excess={len(surv-printed)} printed_killed={len(printed-surv)}")
print()
print("POLY rule FIRED at radii:",dict(FIRE))
print("all radii <=0 seen at DP levels:",dict(ALLNEG))
print("integral radii seen at DP levels:",{k:v for k,v in ALLDELTA.items() if Fraction(k).denominator==1})
json.dump({"fire":dict(FIRE),"nonpos":dict(ALLNEG),
           "integral_all":{k:v for k,v in ALLDELTA.items() if Fraction(k).denominator==1},
           "screens":res}, open('replay2.json','w'), indent=1)
