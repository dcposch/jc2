from math import gcd, ceil
# ---------- (T-A) admissibility witness: banked constraints vs unbounded k ----------
def witness(N,a,k):
    W=N-a; Dg=2*a-N
    ok={}
    ok['sheet gate ceil(N/2)<=a<=N-2'] = (a>=-(-N//2) and a<=N-2)
    ok['W>=2 (7.B)'] = W>=2
    ok['[P3] N=a+sum s_l mu_l (s=1,mu=W)'] = (N==a+1*W)
    ok["7.B' mu_l>=2"] = W>=2
    Kc=a-1; Kp=0
    ok['sum_p K_p = a-1'] = (Kc+k*Kp == a-1)
    ok['(C2) K_p<=D_gap at multibranch'] = (Kp<=Dg)
    ok['a_p>=0 at cusp']=(a-Kc>=0)
    ok['a_p>=0 at nodes']=(a-1*W-Kp>=0)
    R=0; beta=1
    ok['(C3) #{K_p>0}<=R+beta'] = (1 <= R+beta)
    nu=k
    lhs=(a-Kc)*0+(a-(a-Kc))+k*(a-(a-W-Kp))
    ok["(M') sum(a-a_p)=(a-1)+nu*W"] = (lhs == (a-1)+nu*W)
    ok['(B3) >=1 cusp and >=1 multibranch'] = (k>=1)
    return W,Dg,all(ok.values()),ok
print("=== (T-A)  ledger-admissible (B3) data at fixed N with k unbounded ===")
for N in [5,8,12,16,20]:
    a=N-2
    row=[]
    for k in [1,2,5,50,5000]:
        W,Dg,good,_=witness(N,a,k); row.append(f"k={k}:{'OK' if good else 'FAIL'}")
    print(f" N={N:2d} a={a:2d} W={N-a} D_gap={2*a-N}: "+"  ".join(row))
for N in [10,16]:
    a=-(-N//2)
    row=[]
    for k in [1,3,100,10**4]:
        W,Dg,good,_=witness(N,a,k); row.append(f"k={k}:{'OK' if good else 'FAIL'}")
    print(f" N={N:2d} a={a:2d} W={N-a} D_gap={2*a-N}: "+"  ".join(row))

# ---------- (T-B) MERIDIAN-FLOOR per cell ----------
print()
print("=== (T-B)  MERIDIAN-FLOOR  n_min >= ceil((N-1)/(W-1));  delta_aff >= ceil(that/3) ===")
print("  N |  W=2      W=3      W=4      W=5      W=6      W=7   (entries n_min>= / delta_aff>=)")
for N in range(4,21):
    cells=[]
    for W in range(2,8):
        a=N-W
        if not (a>=-(-N//2) and a<=N-2): cells.append("   --   "); continue
        f=ceil((N-1)/(W-1)); cells.append(f"{f:3d}/{-(-f//3):<3d} ")
    print(f" {N:3d}| "+" ".join(cells))

# ---------- (T-C) consumer thresholds ----------
def Rmax(W): return W//2-1
def beta_min(N):
    for beta in range(0,60):
        for a in range(1,N-1):
            W=N-a; Dg=2*a-N
            if W<2 or Dg<0: continue
            if a-1<=(Rmax(W)+beta)*Dg: return beta
    return None
print()
print("=== (T-C)  what a bound delta_aff <= C buys, per consumer ===")
print(" N   beta_min  (B2) dies iff C<=2*beta_min-1   (B3): k <= C-delta_c   W=2 floor on delta_aff")
for N in range(5,21):
    b=beta_min(N); f=ceil((N-1)/1); fl=-(-f//3)
    s = "already empty" if b==0 else f"C <= {2*b-1}"
    print(f" {N:2d}    {b:2d}       {s:22s}      k <= C - delta_c            {fl}")
# ---------- (T-D) cusp list under HF Prop 3.2 by delta_c ----------
print()
print("=== (T-D)  (B3) cusp types with delta_c <= 12 under HF Prop 3.2 ===")
out=[]
for p in range(2,60):
    for q in range(p+1,120):
        if gcd(p,q)!=1: continue
        if not ((p%2==0 and q%3==0) or (q%2==0 and p%3==0)): continue
        dc=(p-1)*(q-1)//2
        if dc<=12: out.append((dc,p,q))
for dc,p,q in sorted(out): print(f"   (p,q)=({p},{q})  delta_c={dc}   => k <= C-{dc}, admissible only if C>={dc}+1")
