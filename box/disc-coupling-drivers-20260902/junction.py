#!/usr/bin/env python3
"""DISC-COUPLING -- driver 2: the LEVEL-2 (junction) operator.

Set-up derived here.  At the level-2 disc D_2 (radius delta_2) put
    sigma_2 = w_2(t) + pi_2 t^{delta_2},   F_2 = t^{-lam_f(d2)} f(sigma_2),
                                           G_2 = t^{-lam_g(d2)} g(sigma_2).
The a_2 roots of g in D_2 fall into k sub-discs of a_1 roots each and the b_2 roots
of f into the SAME k sub-discs with b_1 each (Moh Def 5.1(1) at level 1), so the
level-2 leading forms are PURE POWERS of the director polynomial
    Psi(pi_2) = prod_{l=1}^{k} (pi_2 - C_l),        deg Psi = k,
    g_0 = Psi^{a_1},  f_0 = Psi^{b_1}   (a_1 = eV_2, b_1 = dV_2, a_2 = k a_1, b_2 = k b_1).
LOCAL-KELLER at delta_2 reads, order by order in theta (t^{eta}), eps_j = j*eta,
    sum_{i+j=J} [ (lam_f+eps_i) f_i g_j' - (lam_g+eps_i) g_i f_j' ]  =  -c [J = J_*]
with lam = lam(delta_2) and J_* the order of t^{delta_2-1-lam_f-lam_g}.
The order-J unknown pair (f_J,g_J) enters through
    M_eps(f,g) = (lam_f+eps) f g_0' - lam_g g_0 f' + lam_f f_0 g' - (lam_g+eps) g f_0'
              = Psi^{b_1-1} * Mtil_eps(f,g).
This driver computes rank/kernel/cokernel of M_eps exactly and locates its resonances.
FAIL-CLOSED.
"""
import sys, time
from fractions import Fraction as F

FAIL=[]; NCHK=[0]
def check(name, cond, detail=""):
    NCHK[0]+=1
    if not cond: FAIL.append((name,detail)); print("  FAIL %-56s %s"%(name,detail))
    return cond

# ---------------- dense polynomial arithmetic over Q (lists, index = degree)
def pmul(a,b):
    if not a or not b: return []
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): out[i+j]+=x*y
    return out
def padd(a,b):
    n=max(len(a),len(b)); out=[F(0)]*n
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return out
def pscal(c,a): return [c*x for x in a]
def pder(a): return [F(i)*a[i] for i in range(1,len(a))]
def ppow(a,n):
    out=[F(1)]
    for _ in range(n): out=pmul(out,a)
    return out
def ptrim(a):
    while a and a[-1]==0: a=a[:-1]
    return a

def psi_from_roots(roots):
    p=[F(1)]
    for r in roots: p=pmul(p,[F(-r),F(1)])
    return p

# ---------------- the operator
def Mtil_columns(Psi, a1, b1, lam_f, lam_g, eps):
    """columns of Mtil_eps as vectors of coefficients; unknowns f_0..f_{b2}, g_0..g_{a2}.
       Mtil = a1(lam_f+eps) f Psi^{a1-b1} Psi'  - lam_g Psi^{a1-b1+1} f'
              + lam_f Psi g'                    - b1(lam_g+eps) g Psi'          """
    k=len(Psi)-1; a2=k*a1; b2=k*b1
    Pd=pder(Psi)
    Pab=ppow(Psi,a1-b1); Pab1=pmul(Pab,Psi)
    cols=[]
    for i in range(b2+1):                       # f = pi^i
        mono=[F(0)]*i+[F(1)]
        t1=pscal(F(a1)*(lam_f+eps), pmul(mono,pmul(Pab,Pd)))
        t2=pscal(-lam_g, pmul(pder(mono),Pab1))
        cols.append(ptrim(padd(t1,t2)))
    for i in range(a2+1):                       # g = pi^i
        mono=[F(0)]*i+[F(1)]
        t3=pscal(lam_f, pmul(pder(mono),Psi))
        t4=pscal(-F(b1)*(lam_g+eps), pmul(mono,Pd))
        cols.append(ptrim(padd(t3,t4)))
    return cols, a2, b2

def rank_exact(cols, nrows):
    """exact rank over Q of the matrix whose COLUMNS are cols (padded to nrows)."""
    M=[[F(0)]*len(cols) for _ in range(nrows)]
    for j,c in enumerate(cols):
        for i,v in enumerate(c):
            if i>=nrows: raise RuntimeError("degree overflow row %d"%i)
            M[i][j]=v
    r=0
    for c in range(len(cols)):
        piv=None
        for i in range(r,nrows):
            if M[i][c]!=0: piv=i; break
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]
        pv=M[r][c]
        M[r]=[x/pv for x in M[r]]
        for i in range(nrows):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[x-f*y for x,y in zip(M[i],M[r])]
        r+=1
        if r==nrows: break
    return r

def report(k, a1, b1, lam_g, eps_list, label=""):
    lam_f=F(b1,a1)*lam_g                       # lam_f/lam_g = m/n = d/e = b_1/a_1
    Psi=psi_from_roots(list(range(1,k+1)))
    a2,b2=k*a1,k*b1
    nrowsM = a2+b2                              # deg <= a2+b2-1  (target of M_eps)
    nrows  = nrowsM - k*(b1-1)                  # deg <= that, after dividing by Psi^{b1-1}
    nunk   = (a2+1)+(b2+1)
    print("  k=%-3d (d,e,V)->(a1,b1)=(%d,%d)  a2=%-3d b2=%-3d unknowns=%-4d target(M)=%-4d target(Mtil)=%-3d %s"
          %(k,a1,b1,a2,b2,nunk,nrowsM,nrows,label))
    out=[]
    for eps in eps_list:
        cols,_,_=Mtil_columns(Psi,a1,b1,lam_f,lam_g,eps)
        r=rank_exact(cols,nrows)
        out.append((eps,r,nunk-r,nrowsM-r))
    return out,nunk,nrowsM,nrows

if __name__=="__main__":
    t0=time.time()
    print("="*90)
    print("driver 2: the level-2 junction operator  M_eps = Psi^{b1-1} * Mtil_eps")
    print("="*90)
    # ---- structural check 1: order 0 of the level-2 equation is IDENTICALLY zero
    print("\n-- CHECK A: level-2 order 0  lam_f f_0 g_0' - lam_g g_0 f_0' == 0 (pure powers) --")
    for (a1,b1,k) in [(3,2,20),(3,2,5),(5,2,4),(4,3,7),(5,3,3),(7,4,2)]:
        lam_g=F(-3,19); lam_f=F(b1,a1)*lam_g
        Psi=psi_from_roots(list(range(1,k+1)))
        g0=ppow(Psi,a1); f0=ppow(Psi,b1)
        z=ptrim(padd(pscal(lam_f,pmul(f0,pder(g0))), pscal(-lam_g,pmul(g0,pder(f0)))))
        check("order-0 vanishes (a1,b1,k)=(%d,%d,%d)"%(a1,b1,k), z==[], "deg %d"%(len(z)-1))
    print("   -> JUNCTION-DEGENERACY: the level-i>=2 leading pair is ABC-DEGENERATE (kappa == 0).")

    # ---- resonance scan at small k, (a1,b1)=(3,2), lam_g = -3/19 (the selected skeleton)
    print("\n-- CHECK B: rank of Mtil_eps versus eps  (a1,b1)=(3,2), lam_g=-3/19, eps=j/380 --")
    lam_g=F(-3,19)
    for k in [2,3,4]:
        eps_list=[F(j,380) for j in range(0,90)]
        res,nunk,nrowsM,nrows=report(k,3,2,lam_g,eps_list)
        drops=[(e,r,ker,cok) for (e,r,ker,cok) in res if r<nrows]
        print("     rank<%d at eps = %s"%(nrows,[str(e) for e,_,_,_ in drops]))
        for e,r,ker,cok in drops:
            print("        eps=%-8s j=%-4s rank %-3d kernel %-3d cokernel(in M) %-3d"%(e,e*380,r,ker,cok))
        gen=[x for x in res if x[0]==F(7,380)][0]
        print("        generic eps=7/380 : rank %d  kernel %d  cokernel(in M) %d"%(gen[1],gen[2],gen[3]))
    print("\nwall %.1fs  checks %d failures %d"%(time.time()-t0,NCHK[0],len(FAIL)))
    assert not FAIL
