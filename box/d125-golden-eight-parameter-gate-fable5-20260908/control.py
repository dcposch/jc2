import sys
sys.dont_write_bytecode=True
import resource,json
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
resource.setrlimit(resource.RLIMIT_AS,(512<<20,512<<20))
from fractions import Fraction as Fr
def need(c,m):
    if not c: raise SystemExit('FAIL: '+m)
mode=sys.argv[1] if len(sys.argv)>1 else 'normal'
MODES=('normal','wrong-t','drop-M-square','wrong-59','zero-gp-target','wrong-U-shift','wrong-c')
need(mode in MODES,'mode')
# ---- K=Q(rho), rho^2=3rho-1, elements (a,b)=a+b*rho
def kadd(x,y):return (x[0]+y[0],x[1]+y[1])
def kmul(x,y):return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]+3*x[1]*y[1])
def ksc(a,x):return (a*x[0],a*x[1])
def K(a,b=0):return (Fr(a),Fr(b))
Z=K(0);ONE=K(1)
# ---- bivariate polys in g,p : {(i,j):K}
def padd(A,B):
    C=dict(A)
    for m,c in B.items():C[m]=kadd(C.get(m,Z),c)
    return {m:c for m,c in C.items() if c!=Z}
def pmul(A,B):
    C={}
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            need(i+j+k+l<=5,'actual factor degree cap 5')
            C[(i+k,j+l)]=kadd(C.get((i+k,j+l),Z),kmul(a,b))
    return {m:c for m,c in C.items() if c!=Z}
def psc(s,A):return {m:kmul(s,c) for m,c in A.items() if kmul(s,c)!=Z}
def brk(A,B,t):  # single scalar coefficient of [A,B]=A_g B_p - A_p B_g at g^t0 p^t1
    o=Z
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            if (i+k-1,j+l-1)==t:o=kadd(o,ksc(Fr(i*l-j*k),kmul(a,b)))
    return o
def outer(H,A,B,t): # single scalar coefficient of H*[A,B]
    o=Z
    for (i,j),h in H.items():o=kadd(o,kmul(h,brk(A,B,(t[0]-i,t[1]-j))))
    return o
# ---- free-symbol polys: {exponent tuple: Fr}
NV=10 # R,H,L,D,p,lam,tau,al,de,be  (ga handled via de)
def V(i):
    e=[0]*NV;e[i]=1;return {tuple(e):Fr(1)}
def C(c):return {tuple([0]*NV):Fr(c)} if c!=0 else {}
def madd(A,B):
    X=dict(A)
    for m,c in B.items():X[m]=X.get(m,Fr(0))+c
    return {m:c for m,c in X.items() if c!=0}
def msc(c,A):return {m:c*v for m,v in A.items()} if c!=0 else {}
def mmul(A,B):
    X={}
    for m,a in A.items():
        for n,b in B.items():
            k=tuple(x+y for x,y in zip(m,n));X[k]=X.get(k,Fr(0))+a*b
    return {m:c for m,c in X.items() if c!=0}
def redD(A): # rewrite D^2 -> H*L (indices D=3,H=1,L=2)
    X={}
    for m,c in A.items():
        m=list(m)
        while m[3]>=2:m[3]-=2;m[1]+=1;m[2]+=1
        X[tuple(m)]=X.get(tuple(m),Fr(0))+c
    return {m:c for m,c in X.items() if c!=0}
R,Hs,Ls,Ds,ps,lam,tau,al,de,be=[V(i) for i in range(NV)]
ga=madd(madd(de,mmul(be,al)),msc(Fr(-5,9),mmul(al,al)))   # gamma = delta + beta*alpha - 5alpha^2/9
f59=Fr(5,8) if mode=='wrong-59' else Fr(5,9)
# (I) scalar kernel: chi*phi' - psi' == -delta
chi=madd(madd(msc(Fr(5,3),mmul(R,R)),be),msc(-f59,al))
phip=madd(msc(3,mmul(R,R)),al)
psip=madd(madd(msc(5,mmul(mmul(R,R),mmul(R,R))),msc(3,mmul(be,mmul(R,R)))),ga)
need(madd(mmul(chi,phip),msc(-1,psip))==msc(-1,de),'(I) chi*phi-prime minus psi-prime is -delta')
# (II) T rewrite: -(5/3)R F^2 + mu(3R^2+al)L - de F == displayed (1), using D^2=HL only
mu=msc(Fr(5,9),mmul(lam,lam));F=madd(mmul(lam,Ds),mmul(tau,ps))
lhs=madd(madd(msc(Fr(-5,3),mmul(R,mmul(F,F))),mmul(mu,mmul(madd(msc(3,mmul(R,R)),al),Ls))),msc(-1,mmul(de,F)))
t1=msc(Fr(5,3),mmul(mmul(lam,lam),mmul(R,mmul(madd(R,msc(-1,Hs)),Ls))))
t2=msc(Fr(-10,3),mmul(mmul(lam,tau),mmul(R,mmul(Ds,ps))))
t3=msc(Fr(-5,3),mmul(mmul(tau,tau),mmul(R,mmul(ps,ps))))
t4=mmul(al,mmul(mu,Ls));t5=msc(-1,mmul(de,F))
need(redD(lhs)==redD(madd(madd(madd(madd(t1,t2),t3),t4),t5)),'(II) displayed T identity (1) modulo D^2=HL')
wit=[]
for rho in (K(0,1),K(3,-1)):
    need(kmul(rho,kadd(K(3),ksc(Fr(-1),rho)))==ONE,'rho unit: rho(3-rho)=1')
    t=rho if mode=='wrong-t' else kadd(ONE,ksc(Fr(-1),rho))
    need(kmul(t,t)==rho,'t^2=rho')
    need(kmul(t,kadd(K(2),ksc(Fr(-1),rho)))==ONE,'t unit: t(2-rho)=1')
    need(kmul(kadd(ONE,rho),ksc(Fr(1,5),kadd(K(4),ksc(Fr(-1),rho))))==ONE,'1+rho unit: (1+rho)(4-rho)/5=1')
    p={(0,1):ONE};g={(1,0):ONE};L=padd(p,g);M=padd(p,{(1,0):t})
    H=pmul(pmul(pmul(p,p),L),M if mode=='drop-M-square' else pmul(M,M))
    D=pmul(pmul(p,L),M)
    need(H.get((3,2))==rho,'[g^3p^2]H=rho and it is a unit')
    need(max(i for i,j in H)==3 and max(i for i,j in D)==2,'g-degrees of H,D are 3,2')
    # factor identity behind T_9 and (2): L p^2 M == p D  (degree 4)
    Mx=L if mode=='wrong-U-shift' else M
    need(pmul(pmul(L,pmul(p,p)),Mx)==pmul(p,D),'L p^2 M = p D')
    CU=pmul(pmul(L,pmul(p,p)),g);CV=pmul(pmul(L,pmul(p,p)),p);W=pmul(p,L);pp=pmul(p,p)
    r2=kmul(rho,rho)
    need(outer(H,H,CU,(7,5))==ksc(Fr(2),r2),'row1 g^7p^5: 2 rho^2 U')
    need(outer(H,H,CV,(7,5))==Z,'row1 has no V')
    need(outer(H,H,CV,(6,6))==ksc(Fr(7),r2),'row2 g^6p^6 mod U: 7 rho^2 V')
    need(outer(H,H,W,(6,4))==r2,'row3 g^6p^4: rho^2 w (times 5lam^2/3)')
    need(outer(H,H,pp,(6,4))==Z,'row3 has no tau^2')
    need(brk(p,g,(0,0))==K(-1) and brk(p,L,(0,0))==K(-1),'[p,g]=[p,L]=-1 (constant row -mu(alpha w+tau))')
    need(brk(H,D,(4,2))==ksc(Fr(-1),kmul(rho,t)),'row5 g^4p^2: -rho t (times -delta lam)')
    need(brk(H,L,(3,1))==ksc(Fr(-2),rho),'row6 g^3p: -2 rho (times alpha mu)')
    need(brk(D,L,(2,0))==ksc(Fr(-1),t),'[D,L] g^2 = -t')
    need(brk(D,L,(0,2))==kadd(t,K(-2)),'[D,L] p^2 = t-2')
    gp=K(0) if mode=='zero-gp-target' else K(-2)
    need(brk(D,L,(1,1))==gp,'[D,L] gp = -2 : unit row -2 mu lam')
    # face-forced c: -(5/9)a^3/kappa with a=lam*t, kappa=rho equals -lam*t*mu  (lambda=1 scalar check)
    a=t;kap=rho
    cface=ksc(Fr(-5,9),kmul(kmul(a,kmul(a,a)),kadd(K(2),ksc(Fr(-1),rho))))  # 1/rho = 2-rho? no: rho^-1=3-rho
    cface=ksc(Fr(-5,9),kmul(kmul(a,kmul(a,a)),kadd(K(3),ksc(Fr(-1),rho))))
    cansatz=ksc(Fr(-5,9),t) if mode!='wrong-c' else ksc(Fr(5,9),t)
    need(cface==cansatz,'c=-(5/9)a^3/kappa equals -lam t mu at lam=1')
    wit.append({'rho':[str(x) for x in rho],'2rho2':[str(x) for x in ksc(Fr(2),r2)],'7rho2':[str(x) for x in ksc(Fr(7),r2)],'rho2':[str(x) for x in r2],'rho_t':[str(x) for x in kmul(rho,t)]})
print(json.dumps({'status':'PASS','mode':mode,'scope':'free-symbol identities (I),(II); factor identities deg<=4; single scalar projections; no H powers, no full bracket','w':wit},sort_keys=True))
