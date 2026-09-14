#!/usr/bin/env python3
"""Emit a Singular driver for the two-step K16 radical certificate at index t.

Replays the charged UF top-down reconstruction (same as custody_tacnode.py),
audits the unit Toeplitz L-tail block on the unreduced high rows, imports the
frozen controls_t{t}_raw.sing under the identity map on (c_i,b), verifies
u^2+4 T2 in J_t, then computes min exponents e1,e2 and lift cofactor weights.
Usage: emit_radical.py t [--prime p --droot r]
"""
from __future__ import annotations

import argparse
from pathlib import Path

HERE = Path(__file__).resolve().parent
FROZEN = Path("/home/ubuntu/jc2/box/k16xempty-20260905")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("t", type=int)
    ap.add_argument("--prime", type=int, default=0)
    ap.add_argument("--droot", type=int, default=0)
    a = ap.parse_args()
    t = a.t
    N = t + 1
    q = 2 * t + 1
    cs = [f"c{i}" for i in range(1, t)]
    ws = [f"w{i}" for i in range(1, q)]
    if a.prime:
        co = str(a.prime)
        rel = f"number d={a.droot};"
        assert (3 * a.droot * a.droot - N) % a.prime == 0
    else:
        co = "(0,d)"
        rel = f"minpoly=3*d^2-{N};"
    wts = list(range(1, t)) + [N]
    n_extra = len(cs) + len(ws) + 3  # b,B,eta plus c's and w's; x,Y already counted
    # deg(D,intvec) in the big ring: vars (x,Y,cs,b,B,eta,ws) so weight on x only
    xwt = "intvec(1,0" + ",0" * (len(cs) + len(ws) + 3) + ")"

    s: list[str] = [
        f"ring r={co},(x,Y,{','.join(cs)},b,B,eta,{','.join(ws)}),dp;",
        rel,
        "option(redSB);",
        'proc must(int ok,string msg){ if(!ok){print("FAIL "+msg);quit;} }',
        "proc xc(poly f,int k){matrix m=coef(f,x);int i;for(i=1;i<=ncols(m);i++){if(deg(m[1,i])==k){return(m[2,i]);}}return(poly(0));}",
        f"number y=(d+{N})/{2 * q}; number om=1/(4*y^2*(2*d+1));",
        f"poly C=x^{t - 1}" + "".join(f"+c{i}*x^{t - 1 - i}" for i in range(1, t)) + ";",
        f"poly W=om*x^{q}-B" + "".join(f"+w{i}*x^{i}" for i in range(1, q)) + ";",
        "poly L=x^2*C/y-b; poly P=x*W-(b^2)/4;",
        "poly Hdiff=2*x*diff(P,x)-3*P-B*x+(3/2)*L*(L+b);",
        "poly Rfree=(3/16)*(L^2)*(L*(L+2*b)-4*B*x)-eta*x^2*(b*L/2+B*x);",
        "poly UF=P*Hdiff-Rfree;",
        "UF=subst(UF,eta,w1); W=subst(W,eta,w1);",
        f'must(xc(UF,{4 * N})==0,"top");',
        "// ---- Toeplitz L-tail block on UNREDUCED high rows (P-jets still free) ----",
        "poly PTD0=x*W-(b^2)/4;",
        "poly RY0=(3/16)*Y^2*(Y*(Y+2*b)-4*B*x)-w1*x^2*(b*Y/2+B*x);",
        "poly GY0=(3/2)*Y*(Y+b)-B*x;",
        "poly QP0=RY0-GY0*PTD0-(x*diff(PTD0^2,x)-3*PTD0^2);",
        "poly D0=subst(diff(QP0,Y),Y,L);",
        f"poly d3N=xc(D0,{3 * N});",
        'print("TOEPLITZ_d3N_field="+string(deg(d3N)==0 && d3N!=0));',
        'print("TOEPLITZ_d3N_formula="+string(d3N-(3/(4*y^3))*(1-4*om*y^2)==0));',
        "int tok=1; int k; int m; int j; int kk; int mm; poly band; poly got; poly expect; poly ddiag; poly off;",
    ]
    # Jacobian identity d F_k / d l_m = -[x^{k-m}] D,  l_m = c_{N-m}/y
    # so y * diff(F_k, c_{N-m}) == -[x^{k-m}] D
    s += [
        f"for(k={3 * N + 2};k<={4 * N - 1};k++){{",
        "  band=xc(UF,k);",
        f"  for(m=2;m<={N - 1};m++){{",
        "    got=0;",
    ]
    # c-index N-m: need a switch on m because Singular has no computed var names easily
    # generate an explicit if-chain
    ifs = []
    for m in range(2, N):
        cname = f"c{N - m}"
        ifs.append(
            f"    if(m=={m}){{got=y*diff(band,{cname});}}"
        )
    s += ifs
    s += [
        "    expect=-xc(D0,k-m);",
        '    if(got-expect!=0){tok=0; print("TOEPLITZ_MISMATCH k="+string(k)+" m="+string(m));}',
        "  }",
        "}",
        'print("TOEPLITZ_JACOBIAN_OK="+string(tok));',
        # triangular from the tail: row F_{4N-1-j} vs l_{N-1-i}; above-diagonal (i<j wait)
        # For row k=4N-1, only l_{N-1} can appear (k-m<=3N => m>=N-1).
        "int tri=1; poly diagprod=1;",
    ]
    # For j=0..N-3: row k=4N-1-j, column l_{N-1-j} is diagonal = -d3N
    # columns with higher m (m > N-1-j) should have k-m > 3N, hence 0
    s += [
        f"for(j=0;j<={N - 3};j++){{",
        f"  kk={4 * N - 1}-j;",
        "  band=xc(UF,kk);",
        f"  mm={N - 1}-j;",  # diagonal column
        "  ddiag=0;",
    ]
    for m in range(2, N):
        cname = f"c{N - m}"
        s.append(f"  if(mm=={m}){{ddiag=y*diff(band,{cname});}}")
    s += [
        '  if(ddiag+d3N!=0){tri=0; print("TOEPLITZ_DIAG_FAIL j="+string(j));}',
        "  diagprod=diagprod*(-d3N);",
        "  for(m=2;m<mm;m++){",  # smaller l-index: later columns in tail order, must vanish
        "    off=0;",
    ]
    for m in range(2, N):
        cname = f"c{N - m}"
        s.append(f"    if(m=={m}){{off=y*diff(band,{cname});}}")
    s += [
        '    if(off!=0){tri=0; print("TOEPLITZ_UPPER_FAIL k="+string(kk)+" m="+string(m));}',
        "  }",
        "}",
        'print("TOEPLITZ_TRIANGULAR="+string(tri));',
        f'print("TOEPLITZ_DET_FORMULA="+string(diagprod-((-d3N)^{N - 2})==0));',
        f'print("TOEPLITZ_Nminus2={N - 2}");',
        "// ---- Theorem H: eliminate P-jets (W,B) from high rows ----",
        "poly band2,piv,val; poly solB;",
    ]
    for v, k in zip(list(reversed(ws)) + ["B"], range(4 * N - 1, 2 * N, -1)):
        s += [
            f"band2=xc(UF,{k}); piv=diff(band2,{v});",
            f'must(deg(piv)==0 && piv!=0,"pivot_{v}");',
            f"val=-subst(band2,{v},0)/piv; UF=subst(UF,{v},val); W=subst(W,{v},val);",
        ]
        if v == "B":
            s += ["solB=val;"]
    s += [
        'must(xc(UF,0)==0 && xc(UF,1)==0 && xc(UF,2)==0 && xc(UF,3)==0,"low_four");',
        f"for(k={2 * N + 1};k<={4 * N};k++){{must(xc(UF,k)==0,\"high\");}}",
        "poly etasol=xc(W,1); poly w2sol=xc(W,2); poly w3sol=xc(W,3);",
        "poly target=solB*etasol; ideal rows;",
        f"for(k=2;k<={2 * t};k++){{rows[k-1]=xc(UF,k+2);}}",
        "poly PTD=x*W-(b^2)/4;",
        "PTD=subst(PTD,B,solB);",
        "poly RY=(3/16)*Y^2*(Y*(Y+2*b)-4*solB*x)-etasol*x^2*(b*Y/2+solB*x);",
        "poly GY=(3/2)*Y*(Y+b)-solB*x;",
        "poly QP=RY-GY*PTD-(x*diff(PTD^2,x)-3*PTD^2);",
        'must(subst(QP,Y,L)+UF==0,"Q_P(x,L)=-UF");',
        f"number yv=y; poly l2=c{t - 1}/yv;",
        "poly u=4*etasol+3*b*l2;",  # Lpivot
        "poly T2=3*b^2*w3sol+18*solB*w2sol-10*etasol^2;",
        "poly rr=target;",  # B*eta; never named r (the big ring is r)
        f"ring rsmall={co},({','.join(cs)},b),wp({','.join(map(str, wts))});",
        rel,
        "option(redSB);",
        "ideal rows=imap(r,rows); poly target=imap(r,target); poly Bsol=imap(r,solB); poly eta=imap(r,etasol);",
        "poly u=imap(r,u); poly T2=imap(r,T2); poly rr=imap(r,rr); poly w2=imap(r,w2sol); poly w3=imap(r,w3sol);",
        f'print("ROWS_BUILT nrows="+string(size(rows))+" t={t} N={N}");',
        'print("u_wt="+string(deg(u))+" rr_wt="+string(deg(rr))+" T2_wt="+string(deg(T2)));',
        'print("u_homog="+string(homog(u))+" rr_homog="+string(homog(rr))+" T2_homog="+string(homog(T2)));',
        'print("IDENTITY_u2_plus_4T2_plus_24E2="+string(u^2+4*T2+24*rows[1]==0));',
        'print("E2_wt="+string(deg(rows[1]))+" E2_terms="+string(size(rows[1])));',
    ]
    if not a.prime and (FROZEN / f"controls_t{t}_raw.sing").is_file():
        frz = (FROZEN / f"controls_t{t}_raw.sing").read_text()
        frz = (
            frz.replace("ring rsmall=", "ring rfro=")
            .replace("ideal rows=", "ideal rows_fro=")
            .replace("poly Bsol=", "poly B_fro=")
            .replace("poly eta=", "poly eta_fro=")
            .replace("poly target=", "poly T_fro=")
        )
        s += ["// ---- frozen custody: identity map on (c_i,b) ----"]
        s += frz.splitlines()
        s += [
            "setring rsmall;",
            "ideal rows_f=imap(rfro,rows_fro); poly B_f=imap(rfro,B_fro); poly eta_f=imap(rfro,eta_fro); poly T_f=imap(rfro,T_fro);",
            "int same=1; int ii; for(ii=1;ii<=size(rows);ii++){ if(rows[ii]-rows_f[ii]!=0){same=0; print(\"ROW_MISMATCH \"+string(ii));} }",
            'print("CUSTODY rows_equal="+string(same)+" B_equal="+string(Bsol-B_f==0)+" eta_equal="+string(eta-eta_f==0)+" target_equal="+string(target-T_f==0));',
        ]
    else:
        s += ['print("CUSTODY skipped (modular or no frozen t-file)");']

    s += [
        "// ---- std of J_t ----",
        "int tt=timer;",
        "ideal gg=std(rows);",
        'print("STD_J dim="+string(dim(gg))+" vdim="+string(vdim(gg))+" time="+string(timer-tt));',
        "ideal kb=kbase(gg); int soc=0; int hi; for(hi=1;hi<=size(kb);hi++){ if(deg(kb[hi])>soc){soc=deg(kb[hi]);} }",
        'print("SOCLE="+string(soc)+" kbase="+string(size(kb)));',
        "poly u2p4T=u^2+4*T2;",
        'print("(1)_u2+4T2_in_J="+string(reduce(u2p4T,gg)==0)+" terms="+string(size(u2p4T))+" wt="+string(deg(u2p4T)));',
        'print("T2_in_J="+string(reduce(T2,gg)==0)+" u_in_J="+string(reduce(u,gg)==0)+" rr_in_J="+string(reduce(rr,gg)==0));',
        'print("u2_in_J="+string(reduce(u^2,gg)==0)+" T2_minpow_search:");',
        "int m=1; while(reduce(T2^m,gg)!=0 && m<=8){m++;} print(\"T2_minpow=\"+string(m)+\" wt=\"+string(deg(T2)*m)+\" vacuous=\"+string(deg(T2)*m>soc));",
        "m=1; while(reduce(u^m,gg)!=0 && m<=8){m++;} print(\"u_in_J_minpow=\"+string(m)+\" wt=\"+string(deg(u)*m)+\" vacuous=\"+string(deg(u)*m>soc));",
        "// ---- J+(rr) and J+(u) ----",
        "tt=timer; ideal gr=std(rows+rr);",
        'print("STD_J+rr dim="+string(dim(gr))+" vdim="+string(vdim(gr))+" time="+string(timer-tt));',
        "tt=timer; ideal gu=std(rows+u);",
        'print("STD_J+u dim="+string(dim(gu))+" vdim="+string(vdim(gu))+" time="+string(timer-tt));',
        "int e1=1; while(reduce(u^e1,gr)!=0 && e1<=8){e1++;}",
        "int e2=1; while(reduce(rr^e2,gu)!=0 && e2<=8){e2++;}",
        'print("e1_u^e_in_J+(rr)="+string(e1)+" wt="+string(deg(u)*e1)+" vacuous="+string(deg(u)*e1>soc));',
        'print("e2_rr^e_in_J+(u)="+string(e2)+" wt="+string(deg(rr)*e2)+" vacuous="+string(deg(rr)*e2>soc));',
        'if(e1>1){print("NEG_u^(e1-1)_notin_J+(rr)="+string(reduce(u^(e1-1),gr)!=0));}',
        'if(e2>1){print("NEG_rr^(e2-1)_notin_J+(u)="+string(reduce(rr^(e2-1),gu)!=0));}',
        'print("POS_u^e1_in_J+(rr)="+string(reduce(u^e1,gr)==0));',
        'print("POS_rr^e2_in_J+(u)="+string(reduce(rr^e2,gu)==0));',
        "// ---- lift cofactors against original generators (not the GB) ----",
        "ideal Ir=rows+rr;  // last gen is rr = B*eta",
        "ideal Iu=rows+u;  // last gen is u",
        "poly f1=u^e1; poly f2=rr^e2;",
        "tt=timer; matrix M1=lift(Ir,f1);",
        'print("LIFT_e1_time="+string(timer-tt)+" nrows="+string(nrows(M1)));',
        "poly recon1=0; int i; int di; int si; int gwt; int maxd1=-1; int maxt1=0; int rcof_deg=-1; int rcof_sz=0;",
        "for(i=1;i<=nrows(M1);i++){",
        "  di=-1; si=0; gwt=-1;",
        "  if(M1[i,1]!=0){di=deg(M1[i,1]); si=size(M1[i,1]); if(di>maxd1){maxd1=di;} if(si>maxt1){maxt1=si;}}",
        "  if(Ir[i]!=0){gwt=deg(Ir[i]);}",
        '  print("COF1 i="+string(i)+" deg="+string(di)+" terms="+string(si)+" gen_wt="+string(gwt));',
        "  recon1=recon1+Ir[i]*M1[i,1];",
        "}",
        "if(M1[nrows(M1),1]!=0){rcof_deg=deg(M1[nrows(M1),1]); rcof_sz=size(M1[nrows(M1),1]);}",
        'print("COF1_rr_cofactor_deg="+string(rcof_deg)+" terms="+string(rcof_sz)+" expected_wt="+string(deg(f1)-deg(rr)));',
        'print("COF1_maxdeg="+string(maxd1)+" maxterms="+string(maxt1)+" LIFT_OK="+string(recon1==f1));',
        "tt=timer; matrix M2=lift(Iu,f2);",
        'print("LIFT_e2_time="+string(timer-tt)+" nrows="+string(nrows(M2)));',
        "poly recon2=0; int maxd2=-1; int maxt2=0; int ucof_deg=-1; int ucof_sz=0;",
        "for(i=1;i<=nrows(M2);i++){",
        "  di=-1; si=0; gwt=-1;",
        "  if(M2[i,1]!=0){di=deg(M2[i,1]); si=size(M2[i,1]); if(di>maxd2){maxd2=di;} if(si>maxt2){maxt2=si;}}",
        "  if(Iu[i]!=0){gwt=deg(Iu[i]);}",
        '  print("COF2 i="+string(i)+" deg="+string(di)+" terms="+string(si)+" gen_wt="+string(gwt));',
        "  recon2=recon2+Iu[i]*M2[i,1];",
        "}",
        "if(M2[nrows(M2),1]!=0){ucof_deg=deg(M2[nrows(M2),1]); ucof_sz=size(M2[nrows(M2),1]);}",
        'print("COF2_u_cofactor_deg="+string(ucof_deg)+" terms="+string(ucof_sz)+" expected_wt="+string(deg(f2)-deg(u)));',
        'print("COF2_maxdeg="+string(maxd2)+" maxterms="+string(maxt2)+" LIFT_OK="+string(recon2==f2));',
        "// identity cofactors for (1): u^2+4 T2 + 24 E2 = 0, so u^2+4T2 = -24 * rows[1]",
        'print("ID_COFACTOR_of_E2=-24 (weight 0, constant)");',
        "// also lift u^2+4T2 against rows alone",
        "poly f0=u^2+4*T2; matrix M0=lift(rows,f0);",
        "poly recon0=0; for(i=1;i<=nrows(M0);i++){",
        "  di=-1; si=0; gwt=-1; if(M0[i,1]!=0){di=deg(M0[i,1]); si=size(M0[i,1]);}",
        "  if(rows[i]!=0){gwt=deg(rows[i]);}",
        '  print("COF0 i="+string(i)+" deg="+string(di)+" terms="+string(si)+" gen_wt="+string(gwt));',
        "  recon0=recon0+rows[i]*M0[i,1];",
        "}",
        'print("COF0_LIFT_OK="+string(recon0==f0)+" M0_1_equals_-24="+string(M0[1,1]+24==0));',
        'print("RADICAL_STEPS_DONE");',
        "quit;",
    ]

    lab = f"t{t}" + (f"_p{a.prime}_d{a.droot}" if a.prime else "")
    out = HERE / f"radical_{lab}.sing"
    out.write_text("\n".join(s) + "\n")
    print(out)


if __name__ == "__main__":
    main()
