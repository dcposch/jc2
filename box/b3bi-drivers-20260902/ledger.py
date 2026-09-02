"""Boundary ledger produced by substituting the campaign affine data into the
degree-free DO package.  Inputs: N, a, dicriticals [(s,mu)], singular points
[(r_p,K_p)].  a_p = N - r_p*W - K_p."""
def ledger(N,a,dic,pts,label=""):
    W=N-a; out={}
    assert sum(s*mu for s,mu in dic)==W, "W mismatch"
    assert sum(K for r,K in pts)==a-1, "(K) mismatch"
    ap={i:N-r*W-K for i,(r,K) in enumerate(pts)}
    assert all(v>=0 for v in ap.values()), "a_p<0"
    R=sum(r for r,K in pts)
    # E-side
    # places of E at infty over branch puncture of p : total degree a-a_p, per branch
    inf_deg_branch={i:(a-ap[i]) for i,(r,K) in enumerate(pts)}
    # boundary marks over p_infty = the unique place of A_F at infinity
    marks_total=a
    # E-branch degree carried at the affine points t over p (all r_p punctures)
    tload={i:r*(a-ap[i]) for i,(r,K) in enumerate(pts)}
    same={i:K for i,(r,K) in enumerate(pts)}          # <= K_p, = K_p at r=1
    # covering genus cap (B3-E-GENUS)
    cap=1-a+sum(r*max(0,(r-1)*W+K-1) for r,K in pts)
    print("--- %s  N=%d a=%d W=%d  dicriticals=%s"%(label,N,a,W,dic))
    print("    Deg over g = %s (dicriticals) + %s (E-components) = %d"%(
          [s*mu for s,mu in dic], a, sum(s*mu for s,mu in dic)+a))
    print("    fibre-at-p local degrees: %s (attaching pts) + marks summing to %d ; total %d = N"%(
          [s*mu for s,mu in dic], marks_total, W+marks_total))
    print("    spine-depth cap (#forks from a dicritical) <= N - s*mu :",[N-s*mu for s,mu in dic])
    for i,(r,K) in enumerate(pts):
        print("      p_%d: r=%d K=%d a_p=%d | E-places at infty per branch puncture: deg %d"
              " | Ebar_X-branch degree at the t's over p: %d, same-branch <= %d, exchanged >= %d"
              %(i,r,K,ap[i],inf_deg_branch[i],tload[i],same[i],tload[i]-same[i]))
    print("    R=sum r_p=%d ; chi_c(E)=a(1-R)+sum a_p = %d ; 2g(E) <= %d"%(
          R, a*(1-R)+sum(ap.values()), cap))
    return dict(a=a,W=W,R=R,chi=a*(1-R)+sum(ap.values()),cap=cap)

print("### CONTROL 2 : Gamma  y^2=x^3(x-1)^2  as A_F at N=4, k=k_odd=1")
r=ledger(4,2,[(1,2)],[(1,1),(2,0)],"Gamma / N4-PIN k=1")
print("    B3-N4 predicts g=k_odd-1=0, n_infty=3+4k-2k_odd=5, chi_c=1-4k=-3")
print("    instrument: chi_c =",r['chi'],"; n_infty = (R-1)a+2-2g-sum a_p r_p =",(r['R']-1)*2+2-0-(1*1+0*2))
print()
print("### N=5 (B3)")
for pts,lab in ((((1,2),(2,0)),"5a one cusp K=2 + node"),
                (((1,1),(1,1),(2,0)),"5b two cusps K=1 + node"),
                (((1,1),(2,1),(2,0)),"5c cusp K=1 + charged double point K=1 + node")):
    ledger(5,3,[(1,2)],list(pts),lab)
print()
print("### N=6 (B3)")
for a,dic,pts,lab in ((3,[(1,3)],[(1,2),(2,0)],"6a a=3 W=3 one cusp K=2 + node"),
                      (3,[(1,3)],[(1,1),(1,1),(2,0)],"6b a=3 W=3 two cusps + node"),
                      (4,[(1,2)],[(1,3),(2,0)],"6c a=4 W=2 one cusp K=3 + node"),
                      (4,[(1,2)],[(1,1),(1,2),(2,0)],"6d a=4 two cusps K=1,2 + node"),
                      (4,[(1,2)],[(1,1),(2,2),(2,0)],"6e a=4 cusp K=1 + charged dp K=2 + node"),
                      (4,[(1,2)],[(1,1),(1,1),(1,1),(2,0)],"6f a=4 three cusps + node")):
    ledger(6,a,dic,pts,lab)
