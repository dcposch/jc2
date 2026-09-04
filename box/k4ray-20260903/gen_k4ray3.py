#!/usr/bin/env python3
"""k=4 ray charts, v3.  Primary kill test: cst in I  (STRONGER than Rabinowitsch:
it is an exact cofactor identity cst = sum q_i*I_i, verified by lift()).
Chart empty <=> no point of V(I) has cst != 0;  cst in I  ==>  that, over any field.
Usage: gen_k4ray3.py K BDEG CHAR TARGETK [rab]
"""
import sys
def mons(dmax, ymax):
    return [(i,j) for j in range(0,ymax+1) for i in range(0,dmax-j+1)]
def gen(K,Bdeg,ch,tk,rab):
    hm=mons(K-1,K-1); Bm=mons(Bdeg,K-1)
    pv=[(f"h_{i}_{j}",K-i-j) for (i,j) in hm]+[(f"B_{i}_{j}",2*K-i-j) for (i,j) in Bm]
    names=[n for n,_ in pv]; wts=[w for _,w in pv]
    L=[];A=L.append
    A("option(redSB); short=0;")
    A(f"// k-ray chart K={K} Bdeg={Bdeg} char={ch} target=x^{tk}")
    A(f"ring R = {ch},(x,y,{','.join(names)}),dp;")
    A("""proc quoy(poly p, poly hh, int K)
{ poly q=0; poly ld; matrix cp; int d;
  while(1){ if(p==0){break;} cp=coeffs(p,y); d=nrows(cp)-1; if(d<K){break;}
    ld=cp[d+1,1]; q=q+ld*y^(d-K); p=p-ld*y^(d-K)*hh; } return(q); }""")
    hs = " + ".join(f"h_{i}_{j}*x^{i}*y^{j}" for (i,j) in hm)
    A(f"poly h = y^{K-1}*(y-x)" + (" + "+hs if hs else "") + ";")
    A("poly B = " + " + ".join(f"B_{i}_{j}*x^{i}*y^{j}" for (i,j) in Bm) + ";")
    A("poly f = h^2 + B;")
    A(f"poly Al = quoy(B^2, h, {K});")
    A("poly g = h^3 + (3/2)*B*h + (3/8)*Al;")
    A("poly J = diff(f,x)*diff(g,y) - diff(f,y)*diff(g,x);")
    A('"MARK_DEGS"; deg(f); deg(g); deg(J);')
    A("matrix C = coef(J, x*y);")
    A("ideal I; poly cst = 0; int i;")
    A(f"for (i=1;i<=ncols(C);i++)"+"{ if(C[1,i]==x^"+str(tk)+"){cst=C[2,i];} else {I=I+ideal(C[2,i]);} }")
    A("I = simplify(I,2);")
    A('"MARK_NROWS"; size(I); "MARK_NPARAMS"; '+str(len(names))+";")
    ws=",".join(str(w) for w in wts)
    A(f"ring S = {ch},({','.join(names)}),wp({ws});")
    A("ideal I = imap(R,I); poly cst = imap(R,cst);")
    A('"MARK_CST_ZERO"; cst==0;')
    A('"MARK_CST_WT"; deg(cst); "MARK_HOMOG_I"; homog(I); "MARK_HOMOG_CST"; homog(cst);')
    A('"MARK_STDI_START"; ideal GI = std(I); "MARK_STDI_DONE"; "MARK_STDI_SIZE"; size(GI);')
    A('"MARK_CTRL_RAW_DIM"; dim(GI);')
    A('"MARK_REDUCE_CST"; poly rr = reduce(cst,GI); "MARK_CST_IN_I"; rr==0;')
    A('if (rr==0) { matrix Q = lift(I,cst); poly chk = cst - (matrix(I)*Q)[1,1];')
    A('  "MARK_LIFT_VERIFY"; chk==0; "MARK_LIFT_NCOF"; size(ideal(Q));')
    A('  int nz=0; for(i=1;i<=nrows(Q);i++){ if(Q[i,1]!=0){nz++;} } "MARK_LIFT_SUPPORT"; nz; }')
    A('"MARK_CTRL_UNIT"; dim(std(ideal(1)));')
    A('"MARK_CTRL_ORIGIN"; dim(std(maxideal(1)));')
    if rab:
        A(f"ring T = {ch},(Z,{','.join(names)}),dp;")
        A("ideal I=imap(S,I); poly cst=imap(S,cst); ideal L=I,Z*cst-1;")
        A('"MARK_RAB_START"; ideal G=std(L); "MARK_RAB_DONE"; "MARK_DIM"; dim(G); "MARK_GB1"; G[1]; "MARK_RED1"; reduce(1,G);')
    A('"MARK_DONE"; quit;')
    return "\n".join(L)
if __name__=="__main__":
    K=int(sys.argv[1]);Bdeg=int(sys.argv[2]);ch=sys.argv[3];tk=int(sys.argv[4])
    rab = len(sys.argv)>5 and sys.argv[5]=="rab"
    print(gen(K,Bdeg,ch,tk,rab))
