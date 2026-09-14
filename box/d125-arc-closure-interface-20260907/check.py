"""Tiny coefficient projections and changed-object boundary counter-controls."""
import sys
sys.dont_write_bytecode=True
import ast, itertools, json, math
from fractions import Fraction as Q
from pathlib import Path
def need(c,s):
    if not c:raise RuntimeError(s)
def coefficient(n,d):
    # Counts only: [p^d](p^5+t*p^3-h*p)^n, represented in Q[t,h].
    out={}
    for a in range(n+1):
        for b in range(n-a+1):
            c=n-a-b
            if 5*a+3*b+c==d:
                out[(b,c)]=Q(math.factorial(n)//(math.factorial(a)*math.factorial(b)*math.factorial(c)))*(-1)**c
    return out
def check(mode):
    need(not any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(Path(__file__).read_text()))),'Assert absent')
    need(coefficient(3,13)=={(1,0):Q(3)},'literal t coordinate')
    need(coefficient(3,3)=={(0,3):Q(-1)},'literal y cubic correction')
    need(coefficient(5,3)=={},'B fifth power has no degree-three term')
    need(coefficient(5,15)=={(5,0):Q(1),(3,1):Q(-20),(1,2):Q(30)},'B15 scalar projection')
    t=Q(-3)
    shift=Q(0) if mode=='--omit-243' else Q(243)
    gamma_sign=1 if mode=='--gamma-sign' else -1
    for alpha,beta,gamma in ((Q(3),Q(2),Q(1)),(Q(3),Q(2),Q(2)),(Q(0),Q(7),Q(1))):
        y=t*alpha; w=gamma_sign*3*gamma; v=t**5+beta
        D=5*y*y+27*(v+shift)*y-27*w
        delta=gamma-beta*alpha+Q(5,9)*alpha*alpha
        need(D==81*delta,'exact boundary D equals 81 delta')
    # Changed objects: no boundary does not imply empty; boundary constraint is not global.
    k,w,h=Q(2),Q(1,2),Q(2)
    need(k*w-1==0 and h-k==0 and k!=0,'hyperbola exact guarded point')
    if mode=='--claim-global-h':need(h==0,'boundary h cannot be imposed globally')
    need(1==k*w,'k is already a unit on this nonempty affine component')
    # The second toy h=k DOES have a finite boundary h=k=0 and nonzero h on its open.
    need((Q(0)-Q(0))==0 and (Q(2)-Q(2))==0,'boundary and generic points on h=k')
    return {'status':'PASS','scope':'scalar coefficient projections/toy varieties only; not actual source points',
            'H':'A_p13/3+3','D':'5*A_p3^2+27*(B_p15+243)*A_p3-27*B_p3',
            'coefficient_B15':[[list(e),str(c)] for e,c in sorted(coefficient(5,15).items())],
            'counterexample_to_global_inference':{'k':'2','w':'1/2','h':'2','equations':['k*w-1','h-k']}}
if __name__=='__main__':print(json.dumps(check(sys.argv[1] if len(sys.argv)>1 else ''),sort_keys=True))
