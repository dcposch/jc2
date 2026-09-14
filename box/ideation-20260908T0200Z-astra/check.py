import sys
sys.dont_write_bytecode=True
import resource,json
from fractions import Fraction as Q
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(536870912,536870912))
def need(x,n):
    if not x:raise ValueError(n)
# Tiny formal ring Q[epsilon,p,Z]/epsilon^e. No actual H/R/source powers.
def add(A,B):
    C=dict(A)
    for m,c in B.items():C[m]=C.get(m,Q(0))+c
    return {m:c for m,c in C.items() if c}
def scale(A,c):return {m:c*v for m,v in A.items() if c*v}
def mul(A,B,cap):
    C={}
    for m,c in A.items():
        for n,d in B.items():
            t=tuple(x+y for x,y in zip(m,n))
            if t[0]<cap:C[t]=C.get(t,Q(0))+c*d
    return {m:c for m,c in C.items() if c}
def diff(A,k):
    C={}
    for m,c in A.items():
        if m[k]:
            t=list(m);t[k]-=1;C[tuple(t)]=c*m[k]
    return C
def bracket(A,B,cap):return add(mul(diff(A,2),diff(B,1),cap),scale(mul(diff(A,1),diff(B,2),cap),-1))
mode=sys.argv[1] if len(sys.argv)>1 else 'normal'
need(mode in ('normal','change-ribbon','thicken-ribbon','change-golden-pivot'),'mode')
c=Q(4,3) if mode=='change-ribbon' else Q(5,3)
P={(0,0,3):Q(1),(1,2,1):Q(1)}
T={(0,0,5):Q(1),(1,2,3):c}
cap=3 if mode=='thicken-ribbon' else 2
need(not bracket(P,T,cap),'nonconstant nilpotent monic commuting control')
need(bracket(P,T,3)=={(2,3,3):Q(-20,3)},'actual order-two obstruction before quotient')
mu=Q(4,9) if mode=='change-golden-pivot' else Q(5,9)
need(3*mu-Q(5,3)==0,'golden highest formal T coefficient')
# The family inequalities below are finite controls of the written universal algebra.
count=0
for e in range(3,52,2):
    for q in range(e-1):
        M=8*e-2-q
        need(2*(3*e-1)<M,'all tentative second contacts precede target')
        for j in range(2,3*e,2):
            degree=7*e-2*j
            if degree%e==0:need(degree//e>=2,'scalar kernel divisible by H^2')
        need(7*(e-1)<M,'final global initial precedes target')
        count+=1
need(5+1>5 and 5>2,'normal/repeated-p thresholds')
print(json.dumps({'status':'PASS','mode':mode,'ribbon':'epsilon^2=0; u=epsilon*p^2 is nonzero','prequotient_bracket':'-20*epsilon^2*p^3*Z^3/3','golden_mu_over_lambda_squared':'5/9','finite_inequality_controls':count,'universal_claim_from_samples':False},sort_keys=True))
