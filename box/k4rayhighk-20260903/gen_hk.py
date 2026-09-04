#!/usr/bin/env python3
"""k=4 ray chart generator, high-K edition.

Ray R_4 = { (n,m;M2',V2';k) = (3K,2K;3K-6;K-1;4) }, tower
    h  monic in y, deg_y h = K, leading form H = y^(K-1)*(y-x)
    f  = h^2 + B          (B = 2*beta, deg_y B < K, deg B <= Bdeg)
    Al = quo_y(B^2,h)     (= 4*alpha)
    Rh = rem_y(B^2,h)     (= 4*rho)
    g  = h^3 + (3/2)*B*h + (3/8)*Al
    J  = f_x g_y - f_y g_x ,  target  J = c*x^tk  (tk = 4 on the ray)

Two emitters:

  direct : one ring, unknowns = h_ij, B_ij; J built by the Singular expression.
           Generator degree in the unknowns is high (up to ~K+3).
  quad   : unknowns = h_ij, B_ij, A_ij (for Al), R_ij (for Rh); generators are
           (a) the coefficients of  B^2 - Al*h - Rh   and
           (b) the coefficients of  J/3 = J(B/2,Al/4) - J(h,Rh/4)  scaled,
           every one of them QUADRATIC in the unknowns.

Both emit a guided_gb-ready prelude ending in the weighted parameter ring, with
the rows in an ideal named ROWS and the target coefficient in a poly named CSTP.
The weighting is the proved chart grading  w(h_ij)=K-i-j, w(B_ij)=2K-i-j,
w(A_ij)=2*Bdeg-K-i-j, w(R_ij)=2*Bdeg-i-j, and CSTP is w-homogeneous of weight
5K-6 in the direct chart.
"""
import sys


def mons(dmax, ymax):
    """monomials x^i y^j with j<=ymax and i+j<=dmax, in a stable order."""
    return [(i, j) for j in range(0, ymax + 1) for i in range(0, dmax - j + 1)]


QUOY = """proc quoy(poly p, poly hh, int K)
{ poly q=0; poly ld; matrix cp; int d;
  while(1){ if(p==0){break;} cp=coeffs(p,y); d=nrows(cp)-1; if(d<K){break;}
    ld=cp[d+1,1]; q=q+ld*y^(d-K); p=p-ld*y^(d-K)*hh; } return(q); }"""


def hpoly(K, drop_top):
    hm = mons(K - 1, K - 1)
    if drop_top:
        hm = [ij for ij in hm if ij != (0, K - 1)]
    return hm


def direct(K, Bdeg, ch, tk, drop_top=True, extra="", rhocut=None, idsix=False, tbcut=False):
    hm = hpoly(K, drop_top)
    Bm = mons(Bdeg, K - 1)
    pv = [(f"h_{i}_{j}", K - i - j) for (i, j) in hm]
    pv += [(f"B_{i}_{j}", 2 * K - i - j) for (i, j) in Bm]
    names = [n for n, _ in pv]
    wts = [w for _, w in pv]
    L = []
    A = L.append
    A("option(redSB); short=0;")
    A(f"// k4ray direct chart K={K} Bdeg={Bdeg} char={ch} target=x^{tk} nparam={len(names)}")
    A(f"ring RR = {ch},(x,y,{','.join(names)}),dp;")
    A(QUOY)
    hs = " + ".join(f"h_{i}_{j}*x^{i}*y^{j}" for (i, j) in hm)
    A(f"poly h = y^{K-1}*(y-x)" + (" + " + hs if hs else "") + ";")
    A("poly B = " + " + ".join(f"B_{i}_{j}*x^{i}*y^{j}" for (i, j) in Bm) + ";")
    A(extra)
    A("poly f = h^2 + B;")
    A(f"poly Al = quoy(B^2, h, {K});")
    A("poly Rh = B^2 - Al*h;")
    A('print("PRE__SIZE_AL "+string(size(Al))+" SIZE_RH "+string(size(Rh)));')
    A("ideal RCUT;")
    if rhocut is not None:
        A(f"poly Rtail = Rh - jet(Rh,{max(rhocut,-1)});")
        A('print("PRE__RHOTAIL_SIZE "+string(size(Rtail)));')
        A("matrix CRt = coef(Rtail, x*y); int ir;")
        A("for (ir=1;ir<=ncols(CRt);ir++){ RCUT=RCUT+ideal(CRt[2,ir]); }")
        A("RCUT = simplify(RCUT,2);")
        A('print("PRE__RHOCUT_ROWS "+string(size(RCUT)));')
    if idsix:
        # ID6 (machine-verified): J(f,g) = 3*(J(beta,alpha) - J(h,rho))
        #                               = (3/8)*J(B,Al) - (3/4)*J(h,Rh)
        A("poly JJ = (3/8)*(diff(B,x)*diff(Al,y)-diff(B,y)*diff(Al,x))"
          " - (3/4)*(diff(h,x)*diff(Rh,y)-diff(h,y)*diff(Rh,x));")
    else:
        A("poly g = h^3 + (3/2)*B*h + (3/8)*Al;")
        A("poly JJ = diff(f,x)*diff(g,y) - diff(f,y)*diff(g,x);")
    A('print("PRE__DEG_J "+string(deg(JJ)));')
    A('print("PRE__SIZE_J "+string(size(JJ)));')
    A("matrix CC = coef(JJ, x*y);")
    A("ideal I0; poly CST = 0; int ii;")
    A("for (ii=1;ii<=ncols(CC);ii++){ if(CC[1,ii]==x^" + str(tk) +
      "){CST=CC[2,ii];} else {I0=I0+ideal(CC[2,ii]);} }")
    if tbcut:
        # charged TOP-BAND LEMMA: beta not in k  ==>  y^ceil((K-1)/2)*(y-x) | beta_b.
        # Both halves are LINEAR in the top-band unknowns B_ij (i+j = Bdeg):
        #   y^e | beta_b   <=>  B_ij = 0 for j < e ;   (y-x) | beta_b  <=>  sum_ij B_ij = 0.
        e = -(-(K - 1) // 2)
        top = [(i, j) for (i, j) in Bm if i + j == Bdeg]
        tb = [f"B_{i}_{j}" for (i, j) in top if j < e]
        tb.append(" + ".join(f"B_{i}_{j}" for (i, j) in top) or "0")
        A("ideal TBCUT = " + ",".join(tb) + ";")
        A('print("PRE__TBCUT_ROWS "+string(size(TBCUT))+" e ' + str(e) + '");')
        A("I0 = I0 + TBCUT;")
    A("I0 = I0 + RCUT;")
    A("I0 = simplify(I0,2);")
    A('print("PRE__NROWS "+string(size(I0)));')
    A('print("PRE__NPARAMS ' + str(len(names)) + '");')
    A(f"ring SS = {ch},({','.join(names)}),wp({','.join(str(w) for w in wts)});")
    A("ideal ROWS = imap(RR,I0); poly CSTP = imap(RR,CST);")
    A('print("PRE__CST_ZERO "+string(CSTP==0));')
    A('print("PRE__CST_WT "+string(deg(CSTP)));')
    A('print("PRE__HOMOG_I "+string(homog(ROWS)));')
    A('print("PRE__HOMOG_CST "+string(homog(CSTP)));')
    A('print("PRE__PRELUDE_DONE 1");')
    return "\n".join(L), names, wts


def quad(K, Bdeg, ch, tk, drop_top=True, rhodeg=None):
    """low-degree formulation: Al and Rh carry their own unknowns."""
    Adeg = 2 * Bdeg - K
    Rdeg = 2 * Bdeg if rhodeg is None else rhodeg
    hm = hpoly(K, drop_top)
    Bm = mons(Bdeg, K - 1)
    Am = mons(Adeg, K - 2) if Adeg >= 0 else []
    Rm = mons(Rdeg, K - 1) if Rdeg >= 0 else []
    pv = [(f"h_{i}_{j}", K - i - j) for (i, j) in hm]
    pv += [(f"B_{i}_{j}", 2 * K - i - j) for (i, j) in Bm]
    pv += [(f"A_{i}_{j}", 2 * (2 * K) - K - i - j) for (i, j) in Am]
    pv += [(f"R_{i}_{j}", 2 * (2 * K) - i - j) for (i, j) in Rm]
    names = [n for n, _ in pv]
    wts = [w for _, w in pv]
    L = []
    A = L.append
    A("option(redSB); short=0;")
    A(f"// k4ray quad chart K={K} Bdeg={Bdeg} char={ch} target=x^{tk} nparam={len(names)}")
    A(f"ring RR = {ch},(x,y,{','.join(names)}),dp;")
    hs = " + ".join(f"h_{i}_{j}*x^{i}*y^{j}" for (i, j) in hm)
    A(f"poly h = y^{K-1}*(y-x)" + (" + " + hs if hs else "") + ";")
    A("poly B = " + " + ".join(f"B_{i}_{j}*x^{i}*y^{j}" for (i, j) in Bm) + ";")
    A("poly Al = " + (" + ".join(f"A_{i}_{j}*x^{i}*y^{j}" for (i, j) in Am) or "0") + ";")
    A("poly Rh = " + (" + ".join(f"R_{i}_{j}*x^{i}*y^{j}" for (i, j) in Rm) or "0") + ";")
    A("poly DIV = B^2 - Al*h - Rh;")
    A("poly JJ = 2*(diff(B,x)*diff(Al,y)-diff(B,y)*diff(Al,x))"
      " - 2*(diff(h,x)*diff(Rh,y)-diff(h,y)*diff(Rh,x));")
    A('print("PRE__DEG_J "+string(deg(JJ)));')
    A("matrix CD = coef(DIV, x*y); matrix CC = coef(JJ, x*y);")
    A("ideal I0; poly CST = 0; int ii;")
    A("for (ii=1;ii<=ncols(CD);ii++){ I0=I0+ideal(CD[2,ii]); }")
    A("for (ii=1;ii<=ncols(CC);ii++){ if(CC[1,ii]==x^" + str(tk) +
      "){CST=CC[2,ii];} else {I0=I0+ideal(CC[2,ii]);} }")
    if tbcut:
        # charged TOP-BAND LEMMA: beta not in k  ==>  y^ceil((K-1)/2)*(y-x) | beta_b.
        # Both halves are LINEAR in the top-band unknowns B_ij (i+j = Bdeg):
        #   y^e | beta_b   <=>  B_ij = 0 for j < e ;   (y-x) | beta_b  <=>  sum_ij B_ij = 0.
        e = -(-(K - 1) // 2)
        top = [(i, j) for (i, j) in Bm if i + j == Bdeg]
        tb = [f"B_{i}_{j}" for (i, j) in top if j < e]
        tb.append(" + ".join(f"B_{i}_{j}" for (i, j) in top) or "0")
        A("ideal TBCUT = " + ",".join(tb) + ";")
        A('print("PRE__TBCUT_ROWS "+string(size(TBCUT))+" e ' + str(e) + '");')
        A("I0 = I0 + TBCUT;")
    A("I0 = I0 + RCUT;")
    A("I0 = simplify(I0,2);")
    A('print("PRE__NROWS "+string(size(I0)));')
    A('print("PRE__NPARAMS ' + str(len(names)) + '");')
    A(f"ring SS = {ch},({','.join(names)}),wp({','.join(str(w) for w in wts)});")
    A("ideal ROWS = imap(RR,I0); poly CSTP = imap(RR,CST);")
    A('print("PRE__CST_ZERO "+string(CSTP==0));')
    A('print("PRE__PRELUDE_DONE 1");')
    return "\n".join(L), names, wts


if __name__ == "__main__":
    mode = sys.argv[1]
    K = int(sys.argv[2])
    Bdeg = int(sys.argv[3])
    ch = sys.argv[4]
    tk = int(sys.argv[5])
    if mode == "direct":
        txt, _, _ = direct(K, Bdeg, ch, tk)
    else:
        txt, _, _ = quad(K, Bdeg, ch, tk)
    print(txt)
    print('print("PRE__STANDALONE 1"); quit;')
