"""Sensitivity of the whole-tree screen to the top-edge normalisation."""
import sys
sys.path.insert(0,'.')
from fractions import Fraction as F
import moh_skeleton_full_frozen as B
import opus5_probe as OP

# monkeypatch: allow the initial danger flag to be chosen
def embeds_with(self, V, danger0):
    self._memo = {}
    if not (self.d[self.s] > V[self.s] > F(self.d[self.s], 2)):
        return None
    need = tuple(V[i] for i in range(self.s-1, 1, -1))
    return self.ok(self.s-1, (V[self.s],), danger0, need)
OP.Tree.embeds_with = embeds_with

rows = [(n,m,Ms,V) for n in range(4,101) for m,Ms,V in B.census(n,Kmin=2,full=True)]
printed = {(n,m,tuple(Ms),tuple(sorted(V.items()))) for n,m,Ms,V,*_ in B.MOH_TABLE}
for d0 in (True, False):
    for name, kw in (("TREE",{}), ("TREE_ODE",dict(ode=True)),
                     ("TREE_ODE_PASS",dict(ode=True,capacity=True,passport=True))):
        surv = set()
        for n,m,Ms,V in rows:
            if OP.Tree(n,m,Ms,**kw).embeds_with(V, d0) is not None:
                surv.add((n,m,tuple(Ms),tuple(sorted(V.items()))))
        print(f"danger0={d0!s:5s} {name:14s} rows={len(surv):4d} "
              f"classes={len({(k[0],k[1]) for k in surv}):3d} printed={len(surv&printed)}/6")
