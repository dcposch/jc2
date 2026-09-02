import sympy as sp
from engine import Resolution, x, y
from math import ceil, floor

# ---- (A)  level-1 multiplicity from the Newton polygon:
#      a_{p_j} = D - max(deg_{y_j} P, deg_{y_j} Q, 0),  and T_Linf = D - sum_{level1} a
def lvl1(nm,P,Q):
    r=Resolution(sp.expand(P),sp.expand(Q),nm)
    lev1=[i for i in sorted(r.a) if r.prox[i]==[0]]
    s=sum(r.a[i] for i in lev1)
    return nm,r.D,r.T,r.Tclass,r.T-r.Tclass,r.D-s,[r.a[i] for i in lev1]
print("check  T - T_class  ==  D - sum(level-1 a)   [the L_infty-chain tail]")
for t in [("(x,y+x^2)",x,y+x**2),("(x,y+x^4)",x,y+x**4),("(x,y+x^6)",x,y+x**6),
          ("(x,xy^2)",x,x*y**2),("(x,x^2y^3)",x,x**2*y**3),("(x^2,y^4)",x**2,y**4),
          ("(x^3,y^2)",x**3,y**2),("psi2o(x,xy^2)",x+(x*y**2)**2,x*y**2),
          ("(x,y^4)",x,y**4),("(x,x^3y^2)",x,x**3*y**2)]:
    nm,D,T,Tc,d1,d2,l=lvl1(*t)
    assert d1==d2, (nm,d1,d2)
    print(f"   {nm:18s} D={D:3d} T={T:3d} T_class={Tc:3d} T-T_class={d1:3d} = D-sum(lvl1 a)={d2:3d}  lvl1={l}")
print("   -> identity holds on all rows\n")

# ---- (B)  crossing table
def cell(N,W):
    a=N-W
    if not (ceil(N/2)<=a<=N-2): return None
    return True
print("TABLE C1.  MOH-CROSS price per (N,W).  Smax=floor(W/2) [7.B'], kappa<=N,")
print("           floor n>=P0+1 with P0=ceil((N-1)/(W-S)) [MERIDIAN-FLOOR+, reviewed].")
print("           price(tau) = floor((100 - N - tau)/S) : proving n <= price closes the cell.")
print()
hdr=f"{'N':>3}{'W':>3}{'S':>3}{'P0+1':>6}{'T>0?':>6}" + "".join(f"{'tau='+str(t):>9}" for t in (0,1,10,50))
print(hdr); print("-"*len(hdr))
for N in range(4,17):
    for W in range(2, N//2+1):
        if not cell(N,W): continue
        for S in sorted({1, max(1,W//2)}):
            if 2*S>W: continue
            P0=ceil((N-1)/(W-S)) if W>S else None
            if P0 is None: continue
            floor_n=P0+1
            forced = "yes" if W<=3 else " - "
            row=f"{N:3d}{W:3d}{S:3d}{floor_n:6d}{forced:>6}"
            for tau in (0,1,10,50):
                price=(100-N-tau)//S
                mark="*" if price<floor_n else " "
                row+=f"{price:>8d}{mark}"
            print(row)
print("\n  '*' : the required ceiling on n is BELOW the reviewed floor -> that tau cannot close the cell.")
