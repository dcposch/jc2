#!/usr/bin/env python3
"""k=4 ray charts, v2: weighted-homogeneous (wp) ordering + staged tests.

Grading: the solution set is invariant under (x,y)->(tx,ty) with
   h_ij -> t^(i+j-K) h_ij ,  B_ij -> t^(i+j-2K) B_ij ,  c -> t^(6-5K) c .
So with w(h_ij)=K-i-j>=1, w(B_ij)=2K-i-j>=1 the ideal I of all
non-x^4 Jacobian coefficients is weighted-homogeneous with POSITIVE weights,
and the x^4 coefficient cst is w-homogeneous of weight 5K-6.
Chart empty  <=>  cst in sqrt(I)  <=>  V(I) is a cone inside V(cst).
Usage: gen_k4ray2.py K BDEG CHAR [nohom]
"""
import sys

def mons(dmax, ymax):
    return [(i,j) for j in range(0, ymax+1) for i in range(0, dmax-j+1)]

def gen(K, Bdeg, ch):
    hm = mons(K-1, K-1); Bm = mons(Bdeg, K-1)
    hv = [(f"h_{i}_{j}", K-i-j) for (i,j) in hm]
    Bv = [(f"B_{i}_{j}", 2*K-i-j) for (i,j) in Bm]
    pv = hv + Bv
    names = [n for n,_ in pv]; wts = [w for _,w in pv]
    L=[];A=L.append
    A("option(redSB); short=0;")
    A(f"// k=4 ray, K={K}, Bdeg={Bdeg}, char={ch}; weighted-homogeneous chart")
    A(f"ring R = {ch},(x,y,{','.join(names)}),dp;")
    A("""proc quoy(poly p, poly hh, int K)
{ poly q=0; poly ld; matrix cp; int d;
  while(1){ if(p==0){break;} cp=coeffs(p,y); d=nrows(cp)-1; if(d<K){break;}
    ld=cp[d+1,1]; q=q+ld*y^(d-K); p=p-ld*y^(d-K)*hh; } return(q); }""")
    A(f"poly h = y^{K-1}*(y-x) + " + " + ".join(f"h_{i}_{j}*x^{i}*y^{j}" for (i,j) in hm) + ";")
    A("poly B = " + " + ".join(f"B_{i}_{j}*x^{i}*y^{j}" for (i,j) in Bm) + ";")
    A("poly f = h^2 + B;")
    A(f"poly Al = quoy(B^2, h, {K});")
    A("poly g = h^3 + (3/2)*B*h + (3/8)*Al;")
    A("poly J = diff(f,x)*diff(g,y) - diff(f,y)*diff(g,x);")
    A('"MARK_DEGS"; deg(f); deg(g); deg(J);')
    A("matrix C = coef(J, x*y);")
    A("ideal I; poly cst = 0; int i;")
    A("for (i=1;i<=ncols(C);i++){ if(C[1,i]==x^4){cst=C[2,i];} else {I=I+ideal(C[2,i]);} }")
    A("I = simplify(I,2);")
    A('"MARK_NROWS"; size(I); "MARK_NPARAMS"; ' + str(len(names)) + ";")
    ws = ",".join(str(w) for w in wts)
    A(f"ring S = {ch},({','.join(names)}),wp({ws});")
    A("ideal I = imap(R,I); poly cst = imap(R,cst);")
    A('"MARK_CST_WT"; deg(cst); "MARK_CST_EXPECTED_WT"; ' + str(5*K-6) + ";")
    A('"MARK_HOMOG_I"; homog(I); "MARK_HOMOG_CST"; homog(cst);')
    A('"MARK_STDI_START"; ideal GI = std(I); "MARK_STDI_DONE"; size(GI); dim(GI);')
    A('"MARK_RADMEM";')
    A("int N; poly rr;")
    A("for (N=1; N<=8; N=N*2) { rr = reduce(cst^N, GI); \"N=\",N,\" reduce=\", rr==0; if (rr==0) { break; } }")
    A(f"ring T = {ch},(Z,{','.join(names)}),dp;")
    A("ideal I = imap(S,I); poly cst = imap(S,cst);")
    A("ideal L = I, Z*cst-1;")
    A('"MARK_RAB_START"; ideal G = std(L); "MARK_RAB_DONE";')
    A('"MARK_DIM"; dim(G); "MARK_SIZE"; size(G); "MARK_GB1"; G[1]; "MARK_RED1"; reduce(1,G);')
    A('"MARK_CTRL_RAW_DIM"; dim(std(I));')
    A('"MARK_CTRL_UNIT"; dim(std(ideal(1)));')
    A('"MARK_CTRL_ORIGIN"; dim(std(maxideal(1)));')
    A('"MARK_DONE"; quit;')
    return "\n".join(L)

if __name__=="__main__":
    K=int(sys.argv[1]); Bdeg=int(sys.argv[2]); ch=sys.argv[3]
    print(gen(K,Bdeg,ch))
