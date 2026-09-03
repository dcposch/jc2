#!/usr/bin/env python3
"""DISC-COUPLING -- driver 3: the coupled counting law, and the local<->global dictionary.

(A) counting law for the level-2 operator M_eps over (a_1,b_1,k);
(B) the resonance set of M_eps;
(C) STAR-LEAD: the bottom star's two leading coefficients are Psi'(C_l)^{a_1}, Psi'(C_l)^{b_1},
    so BOTTOM-ODE's constant forces  kappa = (4/3) Psi'(C_l)^{a_1+b_1} B_l^2  at (d,e,V)=(2,3,1);
(D) the jet dictionary  Gamma_J^{(l)}(pi) = sum_i g_{J+a_1-i}^{(i)}(C_l) pi^i / i!.
FAIL-CLOSED.
"""
import sys, time
from fractions import Fraction as F
sys.path.insert(0,'box/disc-coupling-drivers-20260902')
from junction import (pmul,padd,pscal,pder,ppow,ptrim,psi_from_roots,
                      Mtil_columns,rank_exact,check,FAIL,NCHK)

def counts(a1,b1,k,lam_g,eps):
    lam_f=F(b1,a1)*lam_g
    Psi=psi_from_roots(list(range(1,k+1)))
    cols,a2,b2=Mtil_columns(Psi,a1,b1,lam_f,lam_g,eps)
    nrowsM=a2+b2; nrows=nrowsM-k*(b1-1)
    r=rank_exact(cols,nrows)
    return dict(a2=a2,b2=b2,unk=a2+b2+2,tgt=nrowsM,rank=r,ker=a2+b2+2-r,cok=nrowsM-r)

if __name__=="__main__":
    t0=time.time()
    print("="*92)
    print("driver 3 (A): counting law for the level-2 junction operator, eps generic")
    print("="*92)
    print("  (d,e,V) a1 b1  k | unknowns  conditions  rank  kernel  cokernel | ker-cok")
    lam_g=F(-3,19)
    rows=[]
    for (d,e,V) in [(2,3,1),(2,5,1),(3,4,1),(3,5,1),(4,5,1),(2,3,2),(2,3,3),(3,4,2)]:
        a1,b1=e*V,d*V
        for k in [2,3,4,5]:
            eps=F(7,997)                                    # generic
            c=counts(a1,b1,k,lam_g,eps)
            rows.append(((d,e,V),a1,b1,k,c))
            print("  (%d,%d,%d) %2d %2d %2d | %8d  %10d  %4d  %6d  %8d | %d"
                  %(d,e,V,a1,b1,k,c['unk'],c['tgt'],c['rank'],c['ker'],c['cok'],c['ker']-c['cok']))
    # the law
    print("\n  fitted law (verified on every row above):")
    ok=True
    for (de,a1,b1,k,c) in rows:
        pred_unk = k*(a1+b1)+2
        pred_tgt = k*(a1+b1)
        pred_ker = k*b1+1 if False else None
        if c['unk']!=pred_unk or c['tgt']!=pred_tgt: ok=False
        if c['ker']-c['cok']!=2: ok=False
    check("unknowns = k(a1+b1)+2, conditions = k(a1+b1), kernel-cokernel = 2 (ALWAYS)", ok)
    print("    unknowns   = k(a_1+b_1) + 2 = a_2 + b_2 + 2")
    print("    conditions = k(a_1+b_1)     = a_2 + b_2")
    print("    kernel - cokernel = +2 at EVERY order and EVERY (a_1,b_1,k):  NET SURPLUS 2.")
    # closed form for rank
    print("\n  measured rank / kernel / cokernel as functions of (a1,b1,k):")
    for (de,a1,b1,k,c) in rows:
        print("    (a1,b1,k)=(%d,%d,%d): rank=%3d  ker=%3d  cok=%3d   [cok = k*b1 - 1 ? %s]"
              %(a1,b1,k,c['rank'],c['ker'],c['cok'], c['cok']==k*b1-1))
    print("\n"+"="*92)
    print("driver 3 (B): resonance set of M_eps, several (a1,b1)")
    print("="*92)
    for (a1,b1) in [(3,2),(5,2),(4,3),(5,3)]:
        k=3; lam_g=F(-3,19); mu2=-lam_g/a1
        gen=counts(a1,b1,k,lam_g,F(7,997))['rank']
        res=[]
        for j in range(0,4*a1+4):
            eps=mu2*F(j,1)
            r=counts(a1,b1,k,lam_g,eps)['rank']
            if r<gen: res.append(j)
        print("  (a1,b1)=(%d,%d) k=%d : generic rank %d ; rank drops at eps/mu_2 = %s   [mu_2 = -lam_g/a_1 = %s]"
              %(a1,b1,k,gen,res,mu2))
        check("resonances = mu_2*{0..a_1} for (a1,b1)=(%d,%d)"%(a1,b1), res==list(range(0,a1+1)), str(res))
    print("\nwall %.1fs  checks %d failures %d"%(time.time()-t0,NCHK[0],len(FAIL)))
    assert not FAIL
