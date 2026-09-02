import sympy as sp
from engine import Resolution, x, y
import itertools
S=set(); rows=[]
def add(P,Q):
    S.add((sp.srepr(sp.expand(P)), sp.srepr(sp.expand(Q))))
def psi(k,P,Q): return (P+Q**k, Q)
for k in range(2,7): add(x, y+x**k)
for k in range(2,5): add(x+y**k, y)
add(x+(y+x**2)**3, y+x**2); add(x+y**2+y**3,y); add(y,x+y**3)
for N in [1,2,3,4]:
    for c in [0,1,2,3]:
        if c==0 and N==1: continue
        add(x, x**c*y**N)
for N in [1,2,3]:
    for k in [2,3,4]:
        P,Q=psi(k,x,x*y**N); add(P,Q)
for P,Q in [(x**2,y**4),(x,x*y**2+y),(x+y**2,y+x**2),(x**2*y,y),(x,y**3),(x**3,y**2),
            (x+y**3,x),(y,x+y**2),(x*y,y),(x**2+y,x),(x,y+x**2+x**3),(x+y**2,y**3),
            (x,x*y**5),(x,x**3*y**4),(x,x**4*y**3),(x,x**3*y**2),(x*y,x+y),(x**2*y**2,y),
            (x*y**2,x*y),(x**2-y**2,x*y),(x*(x+y),y),(x**2*y,x*y),(x,x*(x+1)*y**2),
            (x,(x**2-1)*y**2),(x,(x**2-1)*y**3),(x,x*(x-1)*(x-2)*y**2),(x,y+x**5),(x,y+x**6),
            (x,x*(y+x**2)**2),(x,x*(y+x**3)**3),(x+y**2,(x+y**2)**2*y**3)]:
    add(P,Q)
chis=[(x,y+x**2),(x,y+x**3),(x+y**2,y),(x+y**2,y+(x+y**2)**2)]
for BP,BQ in [(x,x*y**2),(x,x**2*y**3),(x,y**3),(x,x*y**3),(x,y+x**2)]:
    for c1,c2 in chis:
        add(sp.expand(BP.subs({x:c1,y:c2},simultaneous=True)), sp.expand(BQ.subs({x:c1,y:c2},simultaneous=True)))
ok=0; skip=0; fail=0
for a,b in S:
    P,Q=sp.sympify(a),sp.sympify(b)
    try: r=Resolution(P,Q,"")
    except AssertionError: skip+=1; continue
    if all(r.checks.values()):
        assert r.D==sum(r.nu[i]*r.rho[i] for i in [0]+sorted(r.a))
        assert r.T==sum((r.nu[i]-1)*r.rho[i] for i in [0]+sorted(r.a))
        assert r.N==sum((r.m[i] or 0)*r.rho[i] for i in [0]+sorted(r.a))
        assert r.D-r.T==sum(r.rho[i] for i in [0]+sorted(r.a))
        assert r.D==r.kappa+r.Lam+r.T
        ok+=1
    else: fail+=1
print("distinct maps attempted:",len(S)," resolved+all identities OK:",ok," skipped(irrational cluster):",skip," failures:",fail)
