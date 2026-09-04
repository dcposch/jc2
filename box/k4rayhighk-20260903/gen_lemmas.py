#!/usr/bin/env python3
"""Machine verification of the structural lemmas used at high K.

V1  ID6            J(f,g) = 3*(J(beta,alpha) - J(h,rho))            [instrument re-check]
V2  Euler form     J(H,R) = -y^(K-2)*( d*R + K*(y-x)*R_x )          [H=y^(K-1)(y-x), R form of deg d]
V3  INJ            J(H,R)=0, R form, deg R=d>=1, deg_y R<=K-1  ==>  R=0
V4  top band       [J]_{top} = 3*J(beta_b,alpha_top) - 3*J(H,rho_d) and deg(rho)=2b generically
V5  cofactor       P^2 = A*H  ==>  H*J(P,A) = A*J(H,P)
V6  K=9,b=5        P = mu*y^4*(y-x), A = mu^2*(y-x)  ==>  J(P,A) = 4*mu^3*y^3*(y-x)
V7  composite      beta in k ==> alpha=0, J(f,g)=0, f=phi(h), g=psi(h)
"""
import sys

QUOY = """proc quoy(poly p, poly hh, int Kq)
{ poly q=0; poly ld; matrix cp; int d;
  while(1){ if(p==0){break;} cp=coeffs(p,y); d=nrows(cp)-1; if(d<Kq){break;}
    ld=cp[d+1,1]; q=q+ld*y^(d-Kq)*1; p=p-ld*y^(d-Kq)*hh; } return(q); }"""

JAC = "proc jc(poly u, poly v){ return(diff(u,x)*diff(v,y)-diff(u,y)*diff(v,x)); }"


def rnd(seed):
    """deterministic small integers"""
    s = seed
    while True:
        s = (1103515245 * s + 12345) % 2147483648
        yield (s % 19) - 9


def poly_rand(mons, gen):
    terms = []
    for (i, j) in mons:
        c = next(gen)
        if c:
            terms.append(f"({c})*x^{i}*y^{j}")
    return " + ".join(terms) if terms else "0"


def mons(dmax, ymax):
    return [(i, j) for j in range(0, ymax + 1) for i in range(0, dmax - j + 1)]


L = []
A = L.append
A("option(redSB); short=0;")
A("ring RG = 0,(x,y),dp;")
A(QUOY)
A(JAC)

# ---- V1, V4, V7 : concrete instances -------------------------------------
for (K, b, seed) in [(4, 5, 7), (5, 6, 11), (7, 9, 13), (7, 13, 17), (9, 11, 23)]:
    g1 = rnd(seed)
    hlow = poly_rand(mons(K - 1, K - 1), g1)
    bet = poly_rand(mons(b, K - 1), g1)
    A(f"poly Hf_{K}_{b} = y^{K-1}*(y-x);")
    A(f"poly hh_{K}_{b} = Hf_{K}_{b} + {hlow};")
    A(f"poly be_{K}_{b} = {bet};")
    A(f"poly al_{K}_{b} = quoy(be_{K}_{b}^2, hh_{K}_{b}, {K});")
    A(f"poly rh_{K}_{b} = be_{K}_{b}^2 - al_{K}_{b}*hh_{K}_{b};")
    A(f"poly ff_{K}_{b} = hh_{K}_{b}^2 + 2*be_{K}_{b};")
    A(f"poly gg_{K}_{b} = hh_{K}_{b}^3 + 3*be_{K}_{b}*hh_{K}_{b} + (3/2)*al_{K}_{b};")
    A(f"poly JJ_{K}_{b} = jc(ff_{K}_{b},gg_{K}_{b});")
    A(f'print("V1_ID6 K={K} b={b} resid "+string(JJ_{K}_{b} '
      f'- 3*(jc(be_{K}_{b},al_{K}_{b}) - jc(hh_{K}_{b},rh_{K}_{b}))));')
    A(f'print("V4_DEGS K={K} b={b} degbeta "+string(deg(be_{K}_{b}))'
      f'+" degalpha "+string(deg(al_{K}_{b}))+" degrho "+string(deg(rh_{K}_{b}))'
      f'+" 2b "+string(2*deg(be_{K}_{b}))+" degJ "+string(deg(JJ_{K}_{b})));')
    A(f'print("V4_DEGY K={K} b={b} degyrho "+string(deg(rh_{K}_{b},intvec(0,1)))'
      f'+" Kminus1 {K-1}");')
    # top band identity: leading forms
    A(f"poly Pb_{K}_{b} = jet(be_{K}_{b},{b})-jet(be_{K}_{b},{b-1});")
    A(f"int da_{K}_{b} = deg(al_{K}_{b}); int dr_{K}_{b} = deg(rh_{K}_{b});")
    A(f"poly At_{K}_{b} = jet(al_{K}_{b},da_{K}_{b})-jet(al_{K}_{b},da_{K}_{b}-1);")
    A(f"poly Rt_{K}_{b} = jet(rh_{K}_{b},dr_{K}_{b})-jet(rh_{K}_{b},dr_{K}_{b}-1);")
    A(f"int TB_{K}_{b} = {K}+dr_{K}_{b}-2;")
    A(f"poly Jtop_{K}_{b} = jet(JJ_{K}_{b},TB_{K}_{b})-jet(JJ_{K}_{b},TB_{K}_{b}-1);")
    A(f'print("V4_TOPBAND K={K} b={b} resid "+string(Jtop_{K}_{b} '
      f'+ 3*jc(Hf_{K}_{b},Rt_{K}_{b})));')
    A(f'print("V5_COFACTOR K={K} b={b} resid "'
      f'+string(Hf_{K}_{b}*jc(Pb_{K}_{b},At_{K}_{b}) - At_{K}_{b}*jc(Hf_{K}_{b},Pb_{K}_{b}))'
      f'+" P2minusAH "+string(Pb_{K}_{b}^2 - At_{K}_{b}*Hf_{K}_{b}));')
    # V7 composite control on the same h
    A(f"poly bec_{K}_{b} = 5;")
    A(f"poly alc_{K}_{b} = quoy(bec_{K}_{b}^2, hh_{K}_{b}, {K});")
    A(f"poly ffc_{K}_{b} = hh_{K}_{b}^2 + 2*bec_{K}_{b};")
    A(f"poly ggc_{K}_{b} = hh_{K}_{b}^3 + 3*bec_{K}_{b}*hh_{K}_{b} + (3/2)*alc_{K}_{b};")
    A(f'print("V7_COMPOSITE K={K} alpha "+string(alc_{K}_{b})+" J "'
      f'+string(jc(ffc_{K}_{b},ggc_{K}_{b}))+" phi_resid "'
      f'+string(ggc_{K}_{b} - (hh_{K}_{b}^3+3*bec_{K}_{b}*hh_{K}_{b})));')

# ---- V2 : Euler form of J(H,R) -------------------------------------------
for K in [4, 5, 7, 8, 9]:
    for d in [1, 3, K - 1, K, 2 * K - 1]:
        g2 = rnd(1000 + 7 * K + d)
        rr = poly_rand([(d - j, j) for j in range(0, min(d, K - 1) + 1)], g2)
        A(f"poly Hv = y^{K-1}*(y-x); poly Rv = {rr};")
        A(f'print("V2_EULER K={K} d={d} resid "+string(jc(Hv,Rv)'
          f' + y^{K-2}*({d}*Rv + {K}*(y-x)*diff(Rv,x))));')

# ---- V3 : injectivity of R |-> J(H,R) on forms with deg_y <= K-1 ---------
A('print("V3_INJ_BEGIN 1");')
for K in [4, 5, 6, 7, 8, 9]:
    for d in range(1, 4 * K + 1):
        idx = list(range(0, min(d, K - 1) + 1))
        names = ",".join(f"r{j}" for j in idx)
        A(f"ring Rv_{K}_{d} = 0,(x,y,{names}),dp;")
        A(f"poly Hw = y^{K-1}*(y-x);")
        A("poly Rw = " + " + ".join(f"r{j}*x^{d-j}*y^{j}" for j in idx) + ";")
        A("poly Jw = diff(Hw,x)*diff(Rw,y)-diff(Hw,y)*diff(Rw,x);")
        A("matrix Cw = coef(Jw,x*y); ideal Iw; int iw;")
        A("for(iw=1;iw<=ncols(Cw);iw++){ Iw=Iw+ideal(Cw[2,iw]); }")
        A("ideal Gw = std(Iw); int okw = 1;")
        for j in idx:
            A(f"if (reduce(r{j},Gw)!=0) {{ okw = 0; }}")
        A(f'print("V3_INJ K={K} d={d} nvars {len(idx)} only_trivial "+string(okw));')
        A(f"kill Rv_{K}_{d};")

# ---- V6 : the K=9,b=5 corner ---------------------------------------------
A("ring R6 = 0,(x,y,mu),dp;")
A("poly P6 = mu*y^4*(y-x); poly A6 = mu^2*(y-x); poly H6 = y^8*(y-x);")
A("poly chk6 = P6^2 - A6*H6;")
A("poly J6 = diff(P6,x)*diff(A6,y)-diff(P6,y)*diff(A6,x);")
A('print("V6_K9B5 P2minusAH "+string(chk6)+" JPA "+string(J6)'
  '+" resid "+string(J6 - 4*mu^3*y^3*(y-x)));')
A('print("LEMMAS_DONE 1"); quit;')
print("\n".join(L))
