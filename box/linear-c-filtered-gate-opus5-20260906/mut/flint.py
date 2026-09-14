"""Reviewer-local pure-Python stand-in for python-flint (not installed on this host).
verify_filtered.py uses only fmpq() and fmpq_mat().det()/.rank()."""
from fractions import Fraction as _F
def fmpq(a,b=1): return _F(str(a)) if b==1 else _F(a,b)
class fmpq_mat:
    def __init__(self,rows): self.r=[[_F(str(x)) for x in row] for row in rows]
    def _ech(self):
        A=[row[:] for row in self.r]; det=_F(1); rk=0
        n=len(A); m=len(A[0]) if n else 0
        for col in range(m):
            piv=next((i for i in range(rk,n) if A[i][col]),None)
            if piv is None: continue
            if piv!=rk: A[rk],A[piv]=A[piv],A[rk]; det=-det
            det*=A[rk][col]; inv=1/A[rk][col]; A[rk]=[x*inv for x in A[rk]]
            for i in range(rk+1,n):
                if A[i][col]:
                    f=A[i][col]; A[i]=[x-f*y for x,y in zip(A[i],A[rk])]
            rk+=1
        return det,rk
    def det(self):
        d,rk=self._ech(); return d if rk==len(self.r) else _F(0)
    def rank(self): return self._ech()[1]
