#!/usr/bin/env python3
"""Emit Singular jobs for the t=8 one-point lane from charged prefixes.

The charged t=8 .sing files already contain the rank-lane prefix (T-rows,
B_r, C_r, G_r, W_r, I2, evalpoint).  We cut after evalpoint and append a
new payload.  No polynomial is retyped.
"""
from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
CHARGED = Path("/tmp/jc2-lane.8BfZ6v/inputs")


def split_prefix(text: str) -> str:
    marker = "  return(wnz);\n}"
    i = text.find(marker)
    if i < 0:
        raise SystemExit("evalpoint terminator not found")
    return text[: i + len(marker)] + "\n"


def write_job(name: str, body: str, template: Path) -> Path:
    prefix = split_prefix(template.read_text())
    # retarget the banner
    lines = prefix.splitlines()
    if lines and lines[0].startswith('print("K16GALOIS'):
        lines[0] = f'print("K16T8 {name}");'
    prefix = "\n".join(lines) + "\n"
    path = HERE / f"{name}.sing"
    path.write_text(prefix + body)
    print(path, "bytes", path.stat().st_size)
    return path


T8 = CHARGED / "boundary_t8_mod_p32003_b0.sing"
T6 = CHARGED / "verifypoint_t6_mod_p32003_b0.sing"

LISTBOUNDARY = r'''
string MFILE="minpoly_listboundary_t8";
print("LISTBOUNDARY begin stratum j=3 (b4=q2=0, q3=1)");
ideal Bd3=I2+ideal(b4,q2_0,q3_0-1);
int tm=timer; ideal gBd3=std(Bd3);
print("LISTBOUNDARY stratum j=3: vdim="+string(vdim(gBd3))+" dim="+string(dim(gBd3))+" gbsize="+string(size(gBd3))+" time="+string(timer-tm));
ideal BW3=Bd3+Ws; tm=timer; ideal gBW3=std(BW3);
print("LISTBOUNDARY stratum j=3 + (W): vdim="+string(vdim(gBW3))+" dim="+string(dim(gBW3))+" time="+string(timer-tm));
tm=timer; ideal U3=finduni(gBd3);
print("LISTBOUNDARY finduni time="+string(timer-tm));
int k; poly m; list FL; string s; int i;
for (k=4; k<=7; k++) {
  m=U3[k]; FL=factorize(m); s="";
  for (i=1;i<=size(FL[1]);i++) {
    if (deg(FL[1][i])>0) {
      s=s+" "+string(deg(FL[1][i]) div k)+"^"+string(FL[2][i]);
    }
  }
  print("LISTBOUNDARY minpoly "+string(var(k))+" ordinary_degree="+string(deg(m) div k)+" squarefree="+string(deg(gcd(m,diff(m,var(k))))==0)+" FACTOR_PATTERN:"+s);
  write(":w "+MFILE+"_q"+string(k)+".txt", string(m));
}
/* enumerate F_p-points: take linear factors of the q4-minpoly (weight 4),
   fibre, and recurse on remaining finduni.  vdim=6 is small. */
proc roots_linear(poly f, int w)
{
  list FL=factorize(f); list R; int n=0; int i; number v;
  for (i=1;i<=size(FL[1]);i++)
  {
    if ((deg(FL[1][i]) div w)==1)
    {
      v=-leadcoef(subst(FL[1][i],var(w),0))/leadcoef(FL[1][i]);
      n++;
      R[n]=v;
    }
  }
  return(R);
}
list rq4=roots_linear(U3[4],4);
print("LISTBOUNDARY n_rational_q4="+string(size(rq4)));
int iq4; int iq5; int iq6; int iq7; int npt=0;
int nsimple=0; int nwnz=0;
for (iq4=1; iq4<=size(rq4); iq4++)
{
  ideal F4=gBd3+ideal(q4_0-rq4[iq4]); ideal gF4=std(F4);
  print("LISTBOUNDARY fibre q4="+string(rq4[iq4])+" vdim="+string(vdim(gF4)));
  if (vdim(gF4)>0)
  {
    ideal U4=finduni(gF4);
    list rq5=roots_linear(U4[5],5);
    if (size(rq5)==0)
    {
      FL=factorize(U4[5]); s="";
      for (i=1;i<=size(FL[1]);i++) { if (deg(FL[1][i])>0) { s=s+" "+string(deg(FL[1][i]) div 5)+"^"+string(FL[2][i]); } }
      print("LISTBOUNDARY q5 PATTERN"+s+" (no F_p root)");
    }
    for (iq5=1; iq5<=size(rq5); iq5++)
    {
      ideal F5=gF4+ideal(q5_0-rq5[iq5]); ideal gF5=std(F5);
      if (vdim(gF5)>0)
      {
        ideal U5=finduni(gF5);
        list rq6=roots_linear(U5[6],6);
        if (size(rq6)==0)
        {
          FL=factorize(U5[6]); s="";
          for (i=1;i<=size(FL[1]);i++) { if (deg(FL[1][i])>0) { s=s+" "+string(deg(FL[1][i]) div 6)+"^"+string(FL[2][i]); } }
          print("LISTBOUNDARY q6 PATTERN"+s+" (no F_p root)");
        }
        for (iq6=1; iq6<=size(rq6); iq6++)
        {
          ideal F6=gF5+ideal(q6_0-rq6[iq6]); ideal gF6=std(F6);
          if (vdim(gF6)>0)
          {
            ideal U6=finduni(gF6);
            list rq7=roots_linear(U6[7],7);
            if (size(rq7)==0)
            {
              poly rr=reduce(q7_0,gF6);
              if (deg(rr)==0)
              {
                rq7[1]=leadcoef(rr);
              }
              else
              {
                FL=factorize(U6[7]); s="";
                for (i=1;i<=size(FL[1]);i++) { if (deg(FL[1][i])>0) { s=s+" "+string(deg(FL[1][i]) div 7)+"^"+string(FL[2][i]); } }
                print("LISTBOUNDARY q7 PATTERN"+s+" (no F_p root)");
              }
            }
            for (iq7=1; iq7<=size(rq7); iq7++)
            {
              npt++;
              list pt;
              pt[1]=number(0); pt[2]=number(0); pt[3]=number(1);
              pt[4]=rq4[iq4]; pt[5]=rq5[iq5]; pt[6]=rq6[iq6]; pt[7]=rq7[iq7];
              PT=pt; PTOK=1;
              ideal Floc=Bd3+ideal(q4_0-pt[4], q5_0-pt[5], q6_0-pt[6], q7_0-pt[7]);
              ideal gFloc=std(Floc);
              int locvd=vdim(gFloc);
              print("LISTBOUNDARY POINT#"+string(npt)+" local_vdim="+string(locvd)+" (1 <=> simple in the j=3 chart)");
              int w=evalpoint(intvec(4,5,6,7),"BDRY3P"+string(npt));
              if (locvd==1) { nsimple++; }
              if (w==1) { nwnz++; }
            }
          }
        }
      }
    }
  }
}
print("LISTBOUNDARY n_Fp_points="+string(npt)+" n_simple="+string(nsimple)+" n_Wnonzero="+string(nwnz));
print("LISTBOUNDARY_DONE");
print("JOB_DONE");
quit;
'''

CONEW = r'''
print("CONEW begin I2+(W) in P (homogeneous cone statement of Prop 7.1)");
int tm=timer;
ideal IW=I2+Ws;
print("CONEW ngens(I2)="+string(size(I2))+" ngens(W)="+string(size(Ws))+" ngens(IW)="+string(size(IW)));
ideal gIW=std(IW);
print("CONEW I2+(W): dim="+string(dim(gIW))+" vdim="+string(vdim(gIW))+" gbsize="+string(size(gIW))+" time="+string(timer-tm));
tm=timer;
ideal IWa=I2+Ws+ideal(b4-1);
ideal gIWa=std(IWa);
print("CONEW I2+(W)+(b4-1) affine W-locus: dim="+string(dim(gIWa))+" vdim="+string(vdim(gIWa))+" gbsize="+string(size(gIWa))+" time="+string(timer-tm));
print("CONEW_DONE");
print("JOB_DONE");
quit;
'''

CONE = r'''
print("CONE begin std(I2) for Lemma 3.3");
int tm=timer;
ideal gI2=std(I2);
print("CONE I2: dim="+string(dim(gI2))+" mult="+string(mult(gI2))+" gbsize="+string(size(gI2))+" time="+string(timer-tm));
print("CONE_DONE");
print("JOB_DONE");
quit;
'''

HUNT = r'''
print("HUNT affine hyperplane slices of the chart b4=1");
int j; int tm; ideal H; ideal gH;
/* q2=0 in the affine chart: 5 remaining q-variables */
H=I2+ideal(b4-1,q2_0); tm=timer; gH=std(H);
print("HUNT q2=0: dim="+string(dim(gH))+" vdim="+string(vdim(gH))+" gbsize="+string(size(gH))+" time="+string(timer-tm));
if (dim(gH)==0 && vdim(gH)>0) {
  list fx; fx[1]=number(1); fx[2]=number(0);
  int ok=probe(H,3,fx,"HUNT_q2");
  if (ok==1) { evalpoint(2..7,"HUNT_q2"); }
}
H=I2+ideal(b4-1,q3_0); tm=timer; gH=std(H);
print("HUNT q3=0: dim="+string(dim(gH))+" vdim="+string(vdim(gH))+" gbsize="+string(size(gH))+" time="+string(timer-tm));
if (dim(gH)==0 && vdim(gH)>0) {
  list fx3; fx3[1]=number(1); fx3[2]=number(0); fx3[3]=number(0);
  int ok3=probe(H,2,fx3,"HUNT_q3");
  if (ok3==1) { evalpoint(2..7,"HUNT_q3"); }
}
H=I2+ideal(b4-1,q7_0); tm=timer; gH=std(H);
print("HUNT q7=0: dim="+string(dim(gH))+" vdim="+string(vdim(gH))+" gbsize="+string(size(gH))+" time="+string(timer-tm));
if (dim(gH)==0 && vdim(gH)>0) {
  list fx7; fx7[1]=number(1);
  int ok7=probe(H,2,fx7,"HUNT_q7");
  if (ok7==1) { evalpoint(2..7,"HUNT_q7"); }
}
print("HUNT_DONE");
print("JOB_DONE");
quit;
'''

# boundary-chart local-etale hypotheses: CONE dim via SLICE+MAIN is elsewhere;
# here we also record the weighted degree of the stratum and Jacobian expected rank.
# (payload already in LISTBOUNDARY)

AFFINEW = r'''
print("AFFINEW begin I2+(W)+(b4-1) (affine chart of the W-locus)");
int tm=timer;
ideal IWa=I2+Ws+ideal(b4-1);
print("AFFINEW ngens="+string(size(IWa)));
ideal gIWa=std(IWa);
print("AFFINEW I2+(W)+(b4-1): dim="+string(dim(gIWa))+" vdim="+string(vdim(gIWa))+" gbsize="+string(size(gIWa))+" time="+string(timer-tm));
print("AFFINEW_DONE");
print("JOB_DONE");
quit;
'''

LINESEARCH = r'''
print("LINESEARCH sparse lines in the affine chart b4=1");
proc line_report(ideal J, string tag)
{
  int tm=timer; ideal g=std(J);
  print(tag+" dim="+string(dim(g))+" vdim="+string(vdim(g))+" gbsize="+string(size(g))+" time="+string(timer-tm));
  if (dim(g)==0 && vdim(g)>0)
  {
    list fx; fx[1]=number(1);
    int ok=probe(J,2,fx,tag);
    if (ok==1) { evalpoint(2..7,tag); }
  }
  return(dim(g));
}
/* evaluate the 21 minors on a parametric line by substitution; gcd of the
   resulting univariates.  Instant. */
proc unigcd_line(list pt, int freei, string tag)
{
  /* pt has constants in all slots; slot freei is ignored and replaced by the variable */
  int i; poly g=0; poly f; int first=1;
  for (i=1;i<=size(I2);i++)
  {
    f=I2[i];
    int j;
    for (j=1;j<=7;j++)
    {
      if (j!=freei) { f=subst(f,var(j),pt[j]); }
    }
    /* f is now a univariate in var(freei) (or a constant) */
    if (first==1) { g=f; first=0; } else { g=gcd(g,f); }
  }
  print(tag+" univariate_gcd_deg="+string(deg(g))+" poly="+string(g));
  if (deg(g)>0)
  {
    list FL=factorize(g); string s=""; int k; int have=0; number v;
    int w=freei;
    for (k=1;k<=size(FL[1]);k++)
    {
      if (deg(FL[1][k])>0)
      {
        s=s+" "+string(deg(FL[1][k]) div w)+"^"+string(FL[2][k]);
        if ((deg(FL[1][k]) div w)==1 && have==0)
        {
          v=-leadcoef(subst(FL[1][k],var(freei),0))/leadcoef(FL[1][k]);
          have=1;
        }
      }
    }
    print(tag+" FACTOR_PATTERN:"+s);
    if (have==1)
    {
      list qt=pt; qt[freei]=v; qt[1]=number(1);
      PT=qt; PTOK=1;
      print(tag+" candidate from linear factor");
      ideal Fp=I2+ideal(b4-1);
      int j;
      for (j=2;j<=7;j++) { Fp=Fp+ideal(var(j)-PT[j]); }
      ideal gFp=std(Fp);
      print(tag+" local_vdim="+string(vdim(gFp)));
      evalpoint(2..7,tag);
    }
  }
  else
  {
    if (g==0) { print(tag+" gcd=0 (line lies in Gamma)"); }
    else { print(tag+" gcd constant nonzero (line misses Gamma)"); }
  }
}

list pt; int i;
for (i=1;i<=7;i++) { pt[i]=number(0); }
pt[1]=number(1);
/* L1: b4=1, q2=q4=q5=q7=0, q3=1, q6 free  -- affine analogue of the known boundary point */
pt[3]=number(1);
unigcd_line(pt, 6, "LINE_q3=1_q6free");
/* L2: b4=1, all q=0 except q2 free */
pt[3]=number(0);
unigcd_line(pt, 2, "LINE_q2free");
/* L3: b4=1, all q=0 except q3 free */
unigcd_line(pt, 3, "LINE_q3free");
/* L4: q6 free, all other q=0, b4=1 */
unigcd_line(pt, 6, "LINE_q6free");
/* L5: q7 free */
unigcd_line(pt, 7, "LINE_q7free");
/* L6: q4 free */
unigcd_line(pt, 4, "LINE_q4free");
/* L7: q5 free */
unigcd_line(pt, 5, "LINE_q5free");
/* L8: b4=1, q3=1, q6=7416 (the boundary q6), q2 free */
pt[3]=number(1); pt[6]=number(7416);
unigcd_line(pt, 2, "LINE_q3=1_q6=7416_q2free");
/* L9: b4=1, q3=1, q6=7416, q4 free */
pt[2]=number(0);
unigcd_line(pt, 4, "LINE_q3=1_q6=7416_q4free");
/* L10: b4=1, q3=1, q6=7416, q5 free */
unigcd_line(pt, 5, "LINE_q3=1_q6=7416_q5free");
/* L11: b4=1, q3=1, q6=7416, q7 free */
unigcd_line(pt, 7, "LINE_q3=1_q6=7416_q7free");
/* L12: b4=1, q3=1, q2=q4=q5=q6=q7=0 (the point itself) */
pt[6]=number(0);
PT=pt; PTOK=1;
int mz=1; for(i=1;i<=size(I2);i++){ if (ev(I2[i],PT)!=0) { mz=0; } }
print("POINT b4=1 q3=1 others 0 MINORS_ZERO="+string(mz));
/* L13: b4=1, copy of boundary point with b4 flipped to 1 */
pt[6]=number(7416);
PT=pt; PTOK=1;
mz=1; for(i=1;i<=size(I2);i++){ if (ev(I2[i],PT)!=0) { mz=0; } }
print("POINT b4=1 q3=1 q6=7416 others 0 MINORS_ZERO="+string(mz));
if (mz==1) { evalpoint(2..7,"AFFINE_FLIP"); }

print("LINESEARCH_DONE");
print("JOB_DONE");
quit;
'''

write_job("listboundary_t8_mod_p32003_b0", LISTBOUNDARY, T8)
write_job("conew_t8_mod_p32003_b0", CONEW, T8)
write_job("cone_t8_mod_p32003_b0", CONE, T8)
write_job("hunt_t8_mod_p32003_b0", HUNT, T8)
write_job("affinew_t8_mod_p32003_b0", AFFINEW, T8)
write_job("linesearch_t8_mod_p32003_b0", LINESEARCH, T8)

# t=6 perturbed-W negative control: same point, W replaced by W+1 in FITT,
# and a nearby point that must leave Gamma.
t6 = T6.read_text()
# insert after VERIFYPOINT_DONE, before JOB_DONE
perturb_tail = r'''
print("PERTURB begin (negative controls)");
/* (A) FITT identity with W_r+1 must fail */
number Wv; number tt; number Bv;
number beta; int rb=0; number Cv;
Bv=leadcoef(ev(B1,PT)); Cv=leadcoef(ev(C1,PT)); if (Bv!=0 && rb==0) { beta=-Cv/Bv; rb=1; }
Bv=leadcoef(ev(B2,PT)); Cv=leadcoef(ev(C2,PT)); if (Bv!=0 && rb==0) { beta=-Cv/Bv; rb=2; }
Bv=leadcoef(ev(B3,PT)); Cv=leadcoef(ev(C3,PT)); if (Bv!=0 && rb==0) { beta=-Cv/Bv; rb=3; }
Bv=leadcoef(ev(B4,PT)); Cv=leadcoef(ev(C4,PT)); if (Bv!=0 && rb==0) { beta=-Cv/Bv; rb=4; }
Bv=leadcoef(ev(B5,PT)); Cv=leadcoef(ev(C5,PT)); if (Bv!=0 && rb==0) { beta=-Cv/Bv; rb=5; }
tt=leadcoef(a0)*beta^2+leadcoef(ev(b0,PT))*beta+leadcoef(ev(c0,PT));
int pf1; Wv=leadcoef(ev(W1,PT))+1; pf1=(Wv==leadcoef(ev(B1,PT))^2*tt); print("PERTURB W1+1 FITTcheck="+string(pf1)+" (expect 0)");
Wv=leadcoef(ev(W2,PT))+1; print("PERTURB W2+1 FITTcheck="+string(Wv==leadcoef(ev(B2,PT))^2*tt)+" (expect 0)");
Wv=leadcoef(ev(W3,PT))+1; print("PERTURB W3+1 FITTcheck="+string(Wv==leadcoef(ev(B3,PT))^2*tt)+" (expect 0)");
Wv=leadcoef(ev(W4,PT))+1; print("PERTURB W4+1 FITTcheck="+string(Wv==leadcoef(ev(B4,PT))^2*tt)+" (expect 0)");
Wv=leadcoef(ev(W5,PT))+1; print("PERTURB W5+1 FITTcheck="+string(Wv==leadcoef(ev(B5,PT))^2*tt)+" (expect 0)");
int any_pass=pf1;
if (any_pass!=0) { print("PERTURB_FITT_UNEXPECTED_PASS"); } else { print("PERTURB_FITT_FAILS_AS_REQUIRED=1"); }
/* (B) nearby point q2+1 is not on Gamma */
list qt=PT; qt[2]=PT[2]+1; PT=qt;
int mz=1; int i; for(i=1;i<=size(I2);i++){ if (ev(I2[i],PT)!=0) { mz=0; } }
print("PERTURB nearby q2+1 MINORS_ZERO="+string(mz)+" (expect 0)");
ideal Jpert=I2+ideal(b4-1,q2_0-PT[2],q3_0-PT[3],q4_0-PT[4],q5_0-PT[5]);
ideal gJp=std(Jpert);
print("PERTURB nearby local vdim="+string(vdim(gJp))+" (expect 0)");
if (mz==0 && vdim(gJp)==0) { print("PERTURB_NEARBY_FAILS_AS_REQUIRED=1"); } else { print("PERTURB_NEARBY_UNEXPECTED"); }
print("PERTURB_DONE");
print("JOB_DONE");
quit;
'''
# drop original JOB_DONE/quit and append
if "print(\"JOB_DONE\");" not in t6:
    raise SystemExit("t6 JOB_DONE missing")
t6_body = t6.split('print("JOB_DONE");')[0] + perturb_tail
# retarget banner
t6_lines = t6_body.splitlines()
t6_lines[0] = 'print("K16T8 perturb_t6_mod_p32003_b0");'
(HERE / "perturb_t6_mod_p32003_b0.sing").write_text("\n".join(t6_lines) + "\n")
print("wrote perturb_t6", (HERE / "perturb_t6_mod_p32003_b0.sing").stat().st_size)
print("emit_jobs done")
