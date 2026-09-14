#!/usr/bin/env python3
"""Emit Singular jobs for the weighted resultant of the Lemma SQUARE system
R_r = Res_b3(T_{t,2t-1}, T_{t,2t-1-r}), r=1..t-1, in A_t[b4,q2_0,..,q(t-1)_0], wp(1,2,..,t-1).
Sources: the charged exact resultant files box/k16toptail-20260903/restop_t{3..6}_exact.sing
(RStop[m] = band k=t+m-1, i.e. r=t-m) and, for t=7, the exact rows of box/k16terminal-fable5-20260903/t7_rows.txt.
This script only writes .sing files; run them with `timeout 1800 Singular -q JOB.sing > JOB.out 2> JOB.err`.
"""
import sys, re, pathlib, json
from fractions import Fraction
HERE = pathlib.Path(__file__).resolve().parent
TOP = pathlib.Path("/home/ubuntu/jc2/box/k16toptail-20260903")
TERM = pathlib.Path("/home/ubuntu/jc2/box/k16terminal-fable5-20260903")
sys.path.insert(0, "/tmp/jc2-lane.IDgMGT/inputs")
import emit_hilbert_job as EH   # charged emitter (recurrence_lines, h_text)

def H(t):
    q=2*t+1; return f"{12*q*q}*yy^2{-12*q*(t+1):+d}*yy{(t+1)*(3*t+2):+d}"
def qvars(t): return [f"q{j}_0" for j in range(2,t)]
def header(name, t, mode, p=None, root=None, extra_vars=(), weights_extra=(), with_b4=True):
    vs = (["b4"] if with_b4 else []) + qvars(t) + list(extra_vars)
    ws = ([1] if with_b4 else []) + list(range(2,t)) + list(weights_extra)
    L=[]
    if mode=="exact":
        L.append(f"ring {name}=(0,yy),({','.join(vs)}),wp({','.join(map(str,ws))});")
        L.append(f"minpoly={H(t)};")
    else:
        L.append(f"ring {name}={p},({','.join(vs)}),wp({','.join(map(str,ws))});")
        L.append(f"number yy={root};")
    L.append("option(redSB);")
    return L, vs, ws

PROCS = r'''
proc purepowers(ideal G)
{ // list, per ring variable, the least pure power in lead(G) (0 if none)
  ideal L=lead(G); int i; int v; intvec e; string s=""; int found; int cnt; int k;
  for (v=1; v<=nvars(basering); v++) {
    found=0;
    for (i=1; i<=size(L); i++) { e=leadexp(L[i]); cnt=0; for (k=1;k<=nvars(basering);k++){ if (e[k]>0){cnt++;} }
      if (cnt==1 and e[v]>0) { if (found==0 or e[v]<found) { found=e[v]; } } }
    s=s+string(var(v))+"^"+string(found)+" ";
  }
  return(s);
}
proc onlymono(poly f, poly mon)
{ // coefficient of the monomial mon in f (all other monomials ignored)
  matrix M=coef(f,mon); // not used
  poly g=f; int i; 
  for (i=1;i<=nvars(basering);i++){ if (mon/var(i)==0) { g=subst(g,var(i),0); } }
  return(g);
}
'''

def load_R(t, lines):
    """append lines that load RStop (t<=6 from toptail box; t=7 from our own mod-p build) and set RR[r]."""
    if t<=6:
        lines.append(f'execute(read("{TOP}/restop_t{t}_exact.sing"));')
    else:
        lines.append(f'execute(read("{HERE}/restop_t7_mod_p32059_r4425.sing"));')
    lines += [f"int tt={t}; int m; int r; ideal RR;",
              "for (m=1;m<=tt-1;m++){ r=tt-m; RR[r]=RStop[m]; }",
              "for (r=1;r<=tt-1;r++){ if (homog(RR[r])!=1) { print(\"FAIL inhomogeneous r=\"+string(r)); exit(2); }",
              "  if (deg(RR[r])!=4*tt+4+2*r) { print(\"FAIL weight r=\"+string(r)); exit(2); }",
              "  print(\"R r=\"+string(r)+\" wdeg=\"+string(deg(RR[r]))+\" size=\"+string(size(RR[r]))+\" vars=\"+string(variables(RR[r]))); }"]

def full_std(t, label, lines, ws):
    lines += [f"intvec WTS={','.join(map(str,ws))};",
              "int tm=timer; ideal G=std(RR);",
              f'print("{label} dim="+string(dim(G))+" vdim="+string(vdim(G))+" size="+string(size(G))+" time="+string(timer-tm));',
              f'print("{label}_PUREPOWERS "+purepowers(G));',
              f'print("{label}_HILB_BEGIN"); intvec hn=hilb(G,1,WTS); hn; print("{label}_HILB_END");']

def job_full(t, mode, p=None, root=None, tag=""):
    L, vs, ws = header("W", t, mode, p, root)
    L += PROCS.splitlines()
    load_R(t, L)
    full_std(t, "FULL", L, ws)
    L.append(f'print("JOB_DONE full t={t} {tag}");'); L.append("quit;")
    return "\n".join(L)+"\n"

def job_pieces(t, mode, p=None, root=None, tag="", poisson=True, boundary=True):
    L, vs, ws = header("W", t, mode, p, root)
    L += PROCS.splitlines()
    load_R(t, L)
    # facial coefficients: for every variable v and every r, the pure-power coefficient of v in R_r
    L += ["int v; poly g; poly mon; int e;",
          "for (v=1; v<=nvars(basering); v++) { for (r=1;r<=tt-1;r++) { g=RR[r]; int u;",
          "  for (u=1;u<=nvars(basering);u++){ if (u!=v) { g=subst(g,var(u),0); } }",
          "  if (g!=0) { print(\"AXIS var=\"+string(var(v))+\" r=\"+string(r)+\" : \"+string(g)); } else { print(\"AXIS var=\"+string(var(v))+\" r=\"+string(r)+\" : 0\"); } kill u; } }"]
    L += ["ideal RR0=subst(RR,b4,0); ideal RR1=subst(RR,b4,1);"]
    if boundary:
        # boundary ring without b4
        Lb, vsb, wsb = header("WB", t, mode, p, root, with_b4=False)
        L += Lb
        L += ["ideal RB=imap(W,RR0); int tt=%d; int r;" % t,
              "for (r=1;r<=tt-1;r++){ print(\"RB r=\"+string(r)+\" wdeg=\"+string(deg(RB[r]))+\" homog=\"+string(homog(RB[r]))+\" size=\"+string(size(RB[r]))+\" vars=\"+string(variables(RB[r]))); }",
              f"intvec WTSB={','.join(map(str,wsb))};",
              "int tm=timer; ideal GB=std(RB);",
              'print("BOUNDARY dim="+string(dim(GB))+" vdim="+string(vdim(GB))+" size="+string(size(GB))+" time="+string(timer-tm));',
              'print("BOUNDARY_PUREPOWERS "+purepowers(GB));']
        # boundary subsets of size t-2 (square boundary systems): which (t-2)-subsets are already zero-dimensional
        L += ["int s; ideal SB; ideal GS;",
              "for (s=1;s<=tt-1;s++){ SB=0; int c=0; for (r=1;r<=tt-1;r++){ if (r!=s){ c++; SB[c]=RB[r]; } }",
              "  tm=timer; GS=std(SB); print(\"BOUNDARY_MINUS r=\"+string(s)+\" dim=\"+string(dim(GS))+\" vdim=\"+string(vdim(GS))+\" time=\"+string(timer-tm)); kill c; }"]
        L += ["setring W;"]
    if poisson:
        # affine chart b4=1 in q-space: B = A[q]/(R_1..R_{t-2}), Pi = N_B(R_{t-1}); and every other choice of omitted r
        La = []
        vsa = qvars(t)
        if mode=="exact":
            La.append(f"ring WA=(0,yy),({','.join(vsa)}),dp;"); La.append(f"minpoly={H(t)};")
        else:
            La.append(f"ring WA={p},({','.join(vsa)}),dp;"); La.append(f"number yy={root};")
        La.append("option(redSB);")
        L += La
        L += ["ideal RA=imap(W,RR1); int tt=%d; int r; int s; int c; ideal SA; ideal GA; ideal KA; ideal Img; matrix MA; poly dt; int i; int tm;" % t,
              "for (s=tt-1;s>=1;s--){ SA=0; c=0; for (r=1;r<=tt-1;r++){ if (r!=s){ c++; SA[c]=RA[r]; } }",
              "  tm=timer; GA=std(SA); print(\"CHART_MINUS r=\"+string(s)+\" dim=\"+string(dim(GA))+\" vdim=\"+string(vdim(GA))+\" time=\"+string(timer-tm));",
              "  if (dim(GA)==0) { KA=kbase(GA); Img=0; for (i=1;i<=size(KA);i++){ Img[i]=reduce(RA[s]*KA[i],GA); }",
              "    MA=coeffs(Img,KA); tm=timer; dt=det(MA); if (deg(dt)>0) { print(\"FAIL det not constant\"); exit(2); }",
              "    print(\"POISSON_NORM omitted r=\"+string(s)+\" nb=\"+string(size(KA))+\" N_B(R_r|b4=1)=\"+string(dt)+\" time=\"+string(timer-tm)); }",
              "  tm=timer; GA=std(RA); print(\"CHART_ALL unit=\"+string(reduce(1,GA)==0)+\" dim=\"+string(dim(GA))+\" time=\"+string(timer-tm));",
              "}"]
    L.append(f'print("JOB_DONE pieces t={t} {tag}");'); L.append("quit;")
    return "\n".join(L)+"\n"

def job_t3_exact():
    t=3
    L, vs, ws = header("W", t, "exact")
    L += PROCS.splitlines()
    load_R(t, L)
    L += [
     "poly R1=RR[1]; poly R2=RR[2];",
     'print("R1="+string(R1)); print("R2="+string(R2));',
     "// facial: q2-axis",
     "poly c10=subst(R2,b4,0); print(\"C10 q2^10 coefficient of R2: \"+string(c10));",
     "poly c9=subst(R1,b4,0); print(\"R1 at b4=0 (expect 0): \"+string(c9));",
     "poly tau1=subst(R1,q2_0,0); poly tau2=subst(R2,q2_0,0); print(\"TAU1 b4^18 coeff: \"+string(tau1)); print(\"TAU2 b4^20 coeff: \"+string(tau2));",
     "// dehomogenise b4=1: univariate in q2_0",
     "ring U=(0,yy),(v,w),dp; minpoly=%s;" % H(3),
     "poly f1=imap(W,R1); poly f2=imap(W,R2);", # note: imap sends b4->0? no: b4 absent in U => imap maps b4 to 0. Avoid: substitute first.
    ]
    # redo properly: substitute in W then imap
    L = L[:-2]
    L += ["ideal DH=subst(R1,b4,1),subst(R2,b4,1); ideal PB=subst(R1,b4,1,q2_0,q2_0^2),subst(R2,b4,1,q2_0,q2_0^2);",
          "ring U=(0,yy),(q2_0),dp; minpoly=%s;" % H(3),
          "ideal DH=imap(W,DH); poly f1=DH[1]; poly f2=DH[2];",
          'print("deg f1="+string(deg(f1))+" deg f2="+string(deg(f2)));',
          "poly sred=resultant(f1,f2,q2_0); print(\"SIGMA_RED = Res_{8,10}(f1,f2) = \"+string(sred));",
          "number c10=leadcoef(f2); print(\"lc f2 = c10 = \"+string(c10));",
          "number lc1=leadcoef(f1); print(\"lc f1 = \"+string(lc1));",
          "poly Pi=sred/(c10^8); print(\"PI3 = N_{A[q2]/(R2|1)}(R1|1) = sred/c10^8 = \"+string(Pi));",
          "poly sig=c10*sred; print(\"SIGMA3 = Res_{9,10}(P1,P2) (formal degrees) = c10*sred = \"+string(sig));",
          "ideal PB=imap(W,PB); poly F1=PB[1]; poly F2=PB[2];",
          'print("deg F1="+string(deg(F1))+" deg F2="+string(deg(F2)));',
          "poly rp=resultant(F1,F2,q2_0); print(\"PULLBACK Res_{16,20}(F1,F2) = \"+string(rp));",
          'print("CHECK pullback == sred^2 : "+string(rp-sred^2==0)+"  or == -sred^2 : "+string(rp+sred^2==0));',
          "// Poisson with R1 as F0: B'=A[q2]/(R2|1), N(R1|1)",
          "ideal G2=std(f2); ideal K2=kbase(G2); ideal Img; int i; for (i=1;i<=size(K2);i++){ Img[i]=reduce(f1*K2[i],G2); } matrix M2=coeffs(Img,K2); poly d2=det(M2);",
          'print("POISSON nb="+string(size(K2))+" det(mult R1|1 on A[q2]/(R2|1)) = "+string(d2)+"  equals PI3: "+string(d2-Pi==0));',
          "setring W;",
          "intvec WTS=1,2; int tm=timer; ideal G=std(RR);",
          'print("FULL dim="+string(dim(G))+" vdim="+string(vdim(G))+" size="+string(size(G))+" time="+string(timer-tm));',
          'print("FULL_PUREPOWERS "+purepowers(G)); print("FULL_HILB_BEGIN"); intvec hn=hilb(G,1,WTS); hn; print("FULL_HILB_END");',
          'print("JOB_DONE t3 exact");', "quit;"]
    return "\n".join(L)+"\n"

def job_t2(fibre):
    """t=2 control on a rational fibre: rows by the charged recurrence, formal quadratic resultant and actual resultant."""
    t=2; y=Fraction(fibre)
    rec, srcvars = EH.recurrence_lines(t, "split-exact", None, y)
    L = list(rec)
    L += ["ring S=0,(b4,b3),wp(1,3);", f"number yy=({y.numerator}/{y.denominator});",
          "ideal TT=imap(R,RAW);",
          "poly T3=TT[4]; poly T2=TT[3]; poly T1=TT[2]; poly T0=TT[1];",
          'print("T3="+string(T3)); print("T2="+string(T2)); print("T1="+string(T1)); print("T0="+string(T0));',
          "if (homog(T3)!=1 or deg(T3)!=6 or homog(T2)!=1 or deg(T2)!=7) { print(\"FAIL weights\"); exit(2); }",
          "matrix C0=coeffs(T3,b3); matrix C1=coeffs(T2,b3);",
          "poly a0=0; poly b0=0; poly c0=C0[1,1]; if (nrows(C0)>=2){ b0=C0[2,1]; } if (nrows(C0)>=3){ a0=C0[3,1]; }",
          "poly a1=0; poly b1=0; poly c1=C1[1,1]; if (nrows(C1)>=2){ b1=C1[2,1]; } if (nrows(C1)>=3){ a1=C1[3,1]; }",
          'print("a0="+string(a0)+" b0="+string(b0)+" c0="+string(c0)); print("a1="+string(a1)+" b1="+string(b1)+" c1="+string(c1));',
          "poly Rf=(a0*c1-a1*c0)^2-(a0*b1-a1*b0)*(b0*c1-b1*c0);",
          'print("FORMAL R1 = "+string(Rf)+"   (rho_2 * b4^14)");',
          "poly Ra=resultant(T3,T2,b3);",
          'print("ACTUAL-DEGREE resultant(T3,T2,b3) = "+string(Ra));',
          "poly Rl=b0*c1-b1*c0; print(\"LINEAR-PART b0*c1-b1*c0 = \"+string(Rl));",
          "ideal Gt=std(ideal(T3,T2,T1)); print(\"CONE J+ dim=\"+string(dim(Gt))+\" lead=\"+string(lead(Gt)));",
          f'print("JOB_DONE t2 fibre {fibre}");', "quit;"]
    return "\n".join(L)+"\n"

def job_t7_build():
    """Build the t=7 resultants modulo 32059 at y=4425 from the exact rows (terminal box)."""
    rows={}
    for line in open(TERM/"t7_rows.txt"):
        m=re.match(r"T(\d+) = (.*);$", line.strip())
        if m: rows[int(m.group(1))]=m.group(2)
    assert sorted(rows)==list(range(14)), sorted(rows)
    L=["ring R7=32059,(b3,b4,q(2),q(3),q(4),q(5),q(6)),wp(8,1,2,3,4,5,6);","number y=4425;","option(redSB);",
       "if (12*15^2*y^2-12*15*8*y+8*23!=0) { print(\"FAIL root\"); exit(2); }"]
    for k in range(7,14):
        L.append(f"poly T{k} = {rows[k]};")
        L.append(f'if (homog(T{k})!=1 or deg(T{k})!={29-k}) {{ print("FAIL row weight {k}"); exit(2); }}')
    L += ["int tt=7; int k; int r; matrix CM; list AC; list BC; list CC;",
          "for (k=7;k<=13;k++){ r=13-k; CM=coeffs(T13,b3); }"]
    # explicit per-row coefficient extraction
    for k in range(7,14):
        L += [f"CM=coeffs(T{k},b3); if (nrows(CM)!=3) {{ print(\"FAIL deg_b3 row {k}\"); exit(2); }}",
              f"AC[{k}]=CM[3,1]; BC[{k}]=CM[2,1]; CC[{k}]=CM[1,1];",
              f'print("TOP band={k} r={13-k} wt(a,b,c)="+string(deg(CM[3,1]))+","+string(deg(CM[2,1]))+","+string(deg(CM[1,1])));']
    L += ["poly a0=AC[13]; poly b0=BC[13]; poly c0=CC[13];",
          'print("ALPHA7 mod p = "+string(a0));',
          "ideal RStop; int mm=0; poly rk;",
          "for (k=7;k<=12;k++){ rk=(a0*CC[k]-AC[k]*c0)^2-(a0*BC[k]-AC[k]*b0)*(b0*CC[k]-BC[k]*c0); mm++; RStop[mm]=rk;",
          '  print("RES band="+string(k)+" r="+string(13-k)+" wdeg="+string(deg(rk))+" expected="+string(58-2*k)+" homog="+string(homog(rk))+" size="+string(size(rk))); }',
          "// rename to the toptail convention q2_0.. and drop b3",
          "ring W=32059,(b4,q2_0,q3_0,q4_0,q5_0,q6_0),wp(1,2,3,4,5,6); number yy=4425;",
          "ideal RStop=fetch(R7,RStop); // fetch maps by position? no: use imap with renamed ring below",
          "quit;"]
    return "\n".join(L)+"\n"

if __name__=="__main__":
    out = {}
    out["t2_f15.sing"]=job_t2("1/5"); out["t2_f25.sing"]=job_t2("2/5")
    out["t3_exact.sing"]=job_t3_exact()
    out["t4_exact_std.sing"]=job_full(4,"exact",tag="exact")
    out["t4_mod_p32029_r25378.sing"]=job_full(4,"mod",32029,25378,"mod p=32029 r=25378")
    out["t4_mod_p32029_r31563.sing"]=job_full(4,"mod",32029,31563,"mod p=32029 r=31563")
    out["t4_pieces_exact.sing"]=job_pieces(4,"exact",tag="exact")
    out["t4_pieces_mod_p32029_r25378.sing"]=job_pieces(4,"mod",32029,25378,"mod")
    out["t5_exact_std.sing"]=job_full(5,"exact",tag="exact")
    out["t5_mod_p32009_r1821.sing"]=job_full(5,"mod",32009,1821,"mod p=32009 r=1821")
    out["t5_mod_p32009_r15639.sing"]=job_full(5,"mod",32009,15639,"mod p=32009 r=15639")
    out["t5_pieces_exact.sing"]=job_pieces(5,"exact",tag="exact",poisson=False)
    out["t5_pieces_mod_p32009_r1821.sing"]=job_pieces(5,"mod",32009,1821,"mod")
    out["t6_mod_p32003_r27617.sing"]=job_full(6,"mod",32003,27617,"mod p=32003 r=27617")
    out["t6_pieces_exact.sing"]=job_pieces(6,"exact",tag="exact",poisson=False,boundary=False)
    out["t6_pieces_mod_p32003_r27617.sing"]=job_pieces(6,"mod",32003,27617,"mod",poisson=False)
    for name, src in out.items():
        (HERE/name).write_text(src)
        print("wrote", name, len(src))
