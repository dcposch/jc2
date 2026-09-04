#!/usr/bin/env python3
"""Emit Singular charts for the k=4 two-point ray R_4:
   (n,m) = (3K, 2K),  M2' = 3K-6,  V2' = K-1,  (d2',d1') = (-1,0),  J = c*x^4.
   h monic in y, deg h = K, leading form H = y^(K-1)*(y-x).
   f = h^2 + B    (deg_y B < K            : approximate-root property)
   g = h^3 + a2*h^2 + a1*h + a0   (deg_y a_i < K : h-adic expansion, always valid)
   TOWER variant fixes a2=0, a1=(3/2)B, a0=(3/8)*quo_y(B^2,h).
Usage: gen_k4ray.py K VARIANT BDEG  > out.sing
   VARIANT in {tower, hadic, mohspan}
"""
import sys

def mons(dmax, ymax):
    """monomials x^i y^j with i+j<=dmax and j<=ymax, as (i,j)"""
    return [(i,j) for j in range(0, ymax+1) for i in range(0, dmax-j+1)]

def polystr(name, ml):
    return " + ".join(f"{name}_{i}_{j}*x^{i}*y^{j}" for (i,j) in ml)

def gen(K, variant, Bdeg):
    L = []
    A = L.append
    hm = mons(K-1, K-1)                      # h lower part: total degree <= K-1
    hv = [f"h_{i}_{j}" for (i,j) in hm]
    Bm = mons(Bdeg, K-1)                     # B: deg_y < K, total degree <= Bdeg
    Bv = [f"B_{i}_{j}" for (i,j) in Bm]
    params = hv + Bv
    if variant == "hadic":
        a2m = mons(K-1, K-1); a1m = mons(2*K-1, K-1); a0m = mons(3*K-1, K-1)
        params += [f"p_{i}_{j}" for (i,j) in a2m]
        params += [f"q_{i}_{j}" for (i,j) in a1m]
        params += [f"r_{i}_{j}" for (i,j) in a0m]
    A("option(redSB); short=0;")
    A("// ---- k=4 ray chart, K=%d, variant=%s, Bdeg=%d ----" % (K, variant, Bdeg))
    A("ring R = 0,(x,y,Z,%s),dp;" % ",".join(params))
    A("""proc quoy(poly p, poly hh, int K)
{ poly q = 0; poly ld; matrix cp; int d;
  while (1) { if (p==0) { break; }
    cp = coeffs(p,y); d = nrows(cp)-1;
    if (d < K) { break; }
    ld = cp[d+1,1];
    q = q + ld*y^(d-K); p = p - ld*y^(d-K)*hh; }
  return(q); }""")
    A("poly H = y^%d*(y-x);" % (K-1))
    A("poly h = H + %s;" % polystr("h", hm))
    A("poly B = %s;" % polystr("B", Bm))
    A("poly f = h^2 + B;")
    if variant == "tower":
        A("poly Al = quoy(B^2, h, %d);" % K)
        A("poly g = h^3 + (3/2)*B*h + (3/8)*Al;")
    elif variant == "hadic":
        A("poly a2 = %s;" % polystr("p", a2m))
        A("poly a1 = %s;" % polystr("q", a1m))
        A("poly a0 = %s;" % polystr("r", a0m))
        A("poly g = h^3 + a2*h^2 + a1*h + a0;")
    A("poly J = diff(f,x)*diff(g,y) - diff(f,y)*diff(g,x);")
    A('"MARK_DEG_f"; deg(f); "MARK_DEG_g"; deg(g); "MARK_DEG_J"; deg(J);')
    A("matrix C = coef(J, x*y);")
    A("ideal I; poly cst = 0; int i;")
    A("for (i=1; i<=ncols(C); i++) { if (C[1,i]==x^4) { cst = C[2,i]; } else { I = I+ideal(C[2,i]); } }")
    A("I = simplify(I,2);")
    A('"MARK_NROWS"; size(I);')
    A('"MARK_NPARAMS"; %d;' % len(params))
    A('"MARK_CST"; cst;')
    A("ring S = 0,(Z,%s),dp;" % ",".join(params))
    A("ideal I = imap(R,I); poly cst = imap(R,cst);")
    A("ideal L = I, Z*cst-1;")
    A('"MARK_STD_START";')
    A("ideal G = std(L);")
    A('"MARK_STD_DONE";')
    A('"MARK_DIM"; dim(G);')
    A('"MARK_SIZE"; size(G);')
    A('"MARK_GB1"; G[1];')
    A('"MARK_RED1"; reduce(1,G);')
    A('"MARK_CTRL_RAW_DIM"; dim(std(I));')
    A('"MARK_CTRL_UNIT"; dim(std(ideal(1)));')
    A('"MARK_CTRL_ORIGIN"; dim(std(maxideal(1)));')
    A('"MARK_DONE";')
    A("quit;")
    return "\n".join(L)

if __name__ == "__main__":
    K = int(sys.argv[1]); variant = sys.argv[2]; Bdeg = int(sys.argv[3])
    print(gen(K, variant, Bdeg))
