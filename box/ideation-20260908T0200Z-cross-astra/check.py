import sys
sys.dont_write_bytecode=True
from fractions import Fraction as Q
import resource,json
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
def need(x,m):
    if not x:raise ValueError(m)
def K(a=0,b=0):return (Q(a),Q(b))
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[0],-x[1])
def mul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]+3*x[1]*y[1])
def smul(a,x):return mul(K(a),x)
def plus(A,B):
    C=dict(A)
    for m,c in B.items():C[m]=add(C.get(m,K()),c)
    return {m:c for m,c in C.items() if c!=K()}
def product(A,B):
    C={}
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            m=(i+k,j+l);need(sum(m)<=5,'only actual factors through degree5')
            C[m]=add(C.get(m,K()),mul(a,b))
    return {m:c for m,c in C.items() if c!=K()}
def bracket_projection(A,B,target):
    # One scalar coefficient; never forms the bracket polynomial.
    out=K()
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            if (i+k-1,j+l-1)==target:out=add(out,smul(i*l-j*k,mul(a,b)))
    return out
def outer_projection(H,A,B,target):
    # One coefficient of H*[A,B], streaming scalar products of degree<=5 factors.
    out=K()
    for (i,j),h in H.items():out=add(out,mul(h,bracket_projection(A,B,(target[0]-i,target[1]-j))))
    return out
mode=sys.argv[1] if len(sys.argv)>1 else 'normal'
need(mode in ('normal','change-cubic-face','change-quadratic-face','change-D','change-target'),'mode')
witness=[]
for rho in (K(0,1),K(3,-1)):
    t=add(K(1),neg(rho));need(mul(t,t)==rho and t not in (K(),K(1)),'both golden embeddings')
    p={(0,1):K(1)};g={(1,0):K(1)}
    L=plus(p,g);M=plus(p,{(1,0):t})
    H=product(product(product(p,p),L),product(M,M))
    D=product(product(p,L),M)
    need(H[(3,2)]==rho,'actual top coefficient')
    C_U=product(product(L,product(p,p)),g)
    C_V=product(product(L,product(p,p)),p)
    if mode=='change-cubic-face':C_U.pop((2,2))
    h2=mul(rho,rho)
    need(outer_projection(H,H,C_U,(7,5))==smul(2,h2),'first degree12 scalar pivot')
    need(outer_projection(H,H,C_V,(7,5))==K(),'no V in first pivot')
    need(outer_projection(H,H,C_V,(6,6))==smul(7,h2),'second degree12 pivot modulo U')
    W=product(p,L)
    if mode=='change-quadratic-face':W.pop((1,1))
    need(outer_projection(H,H,W,(6,4))==h2,'degree10 w pivot')
    need(outer_projection(H,H,product(p,p),(6,4))==K(),'no tau-squared in w pivot')
    if mode=='change-D':D[(1,2)]=t
    need(bracket_projection(H,D,(4,2))==neg(mul(rho,t)),'degree6 delta pivot sign')
    need(bracket_projection(H,L,(3,1))==smul(-2,rho),'degree4 alpha pivot sign')
    need(bracket_projection(D,L,(2,0))==neg(t),'g-squared target face')
    target_gp=K(-2) if mode=='change-target' else K()
    residual=add(bracket_projection(D,L,(1,1)),neg(target_gp))
    need(residual==K(-2),'unavoidable gp row')
    witness.append({'rho':list(map(str,rho)),'pivot_factors_without_external_scalar':{'U':list(map(str,smul(2,h2))),'V':list(map(str,smul(7,h2))),'w':list(map(str,h2)),'delta':list(map(str,mul(rho,t))),'alpha':list(map(str,smul(-2,rho))),'gp':['-2','0']}})
print(json.dumps({'status':'PASS','mode':mode,'scope':'seven scalar coefficient projections from actual factors degree<=5; no full bracket/source or H powers materialized','embeddings':witness},sort_keys=True))
