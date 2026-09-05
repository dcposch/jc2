#!/usr/bin/env python3
"""Emit an exact Singular cross-engine base probe; never runs CAS itself."""
from pathlib import Path
import sys
t=int(sys.argv[1]); root=Path(__file__).resolve().parent
minors_only=len(sys.argv)>2 and sys.argv[2]=='minors'
pv=['b4']+['u'+str(i) for i in range(2,t)]
decl=(root/f't{t}_rows.sing').read_text()
m=2*t-2
lines=[decl,
f'ideal auditRows='+','.join(f'T{i}' for i in range(1,2*t-1))+';',
f'poly auditTop=T{2*t-1}; poly auditTau=tau;',
'def auditSource=basering;',
f'ring auditLex=(0,d),(b3,{",".join(pv)}),lp;',
f'minpoly=3*d^2-{t+1};',
f'map auditToLex=auditSource,{",".join(pv)},b3;',
'ideal auditRaw=auditToLex(auditRows); poly auditQ=auditToLex(auditTop); poly auditH=auditToLex(auditTau);',
'ideal auditQGB=std(ideal(auditQ));',
'poly auditA=leadcoef(auditQ); poly auditB0=subst(diff(auditQ,b3),b3,0); poly auditC0=subst(auditQ,b3,0);',
'ideal auditU,auditV; int auditI,auditJ; poly auditTmp;',
f'for(auditI=1;auditI<={m};auditI++){{auditTmp=reduce(auditRaw[auditI],auditQGB); auditU[auditI]=subst(diff(auditTmp,b3),b3,0); auditV[auditI]=subst(auditTmp,b3,0); if(auditTmp!=auditV[auditI]+b3*auditU[auditI]){{print("FAIL REMAINDER");quit;}}}}',
'auditH=reduce(auditH,auditQGB); poly auditUT=subst(diff(auditH,b3),b3,0); poly auditVT=subst(auditH,b3,0);',
'if(auditH!=auditVT+b3*auditUT){print("FAIL TARGET_REMAINDER");quit;}',
'def auditLexSource=basering;',
f'ring auditBase=(0,d),({",".join(pv)}),wp({",".join(map(str,range(1,t)))});',
f'minpoly=3*d^2-{t+1};',
f'map auditToBase=auditLexSource,0,{",".join(pv)};',
'proc auditStats(ideal gg,string label){ideal kk=kbase(gg); int aa,jj,ww; int tt=-1; intvec ee; for(aa=1;aa<=size(kk);aa++){ee=leadexp(kk[aa]);ww=0;'+f'for(jj=1;jj<={t-1};jj++)'+'{ww=ww+jj*ee[jj];}if(ww>tt){tt=ww;}}print("STATS "+label+" length="+string(size(kk))+" top="+string(tt));}',
'ideal auditU=auditToBase(auditU); ideal auditV=auditToBase(auditV);',
'poly auditA=auditToBase(auditA); poly auditB0=auditToBase(auditB0); poly auditC0=auditToBase(auditC0); poly auditUT=auditToBase(auditUT); poly auditVT=auditToBase(auditVT);',
'poly auditEll=2*auditA*auditVT-auditB0*auditUT; poly auditNorm=auditA*auditVT^2-auditB0*auditUT*auditVT+auditC0*auditUT^2;',
'ideal auditJ0=auditU,auditV; ideal auditGJ=std(auditJ0);',
'print("J0 dim="+string(dim(auditGJ))+" vdim="+string(vdim(auditGJ))+" ell="+string(reduce(auditEll,auditGJ)==0)+" norm="+string(reduce(auditNorm,auditGJ)==0));',
'auditStats(auditGJ,"J0");',
'ideal auditF=0; ideal auditDs;',
f'for(auditI=1;auditI<={m};auditI++){{auditF=auditF,auditA*auditV[auditI]^2-auditB0*auditU[auditI]*auditV[auditI]+auditC0*auditU[auditI]^2; auditDs[auditI]=auditVT*auditU[auditI]-auditUT*auditV[auditI]; for(auditJ=1;auditJ<auditI;auditJ++){{auditF=auditF,auditV[auditI]*auditU[auditJ]-auditV[auditJ]*auditU[auditI];}}}}',
'print("BUILD F"); ideal auditGF=std(auditF); print("F dim="+string(dim(auditGF))+" vdim="+string(vdim(auditGF)));',
'auditStats(auditGF,"F"); poly auditRem; int auditP1,auditP2;',
f'for(auditI=1;auditI<={m};auditI++){{auditRem=reduce(auditDs[auditI],auditGF); auditP1=(auditRem==0); auditP2=1; if(!auditP1){{auditP2=(reduce(auditRem^2,auditGF)==0);}}print("D "+string(auditI)+" power1="+string(auditP1)+" power2="+string(auditP2));}}',
'ideal auditFF=auditGF;',
f'for(auditI=1;auditI<={m};auditI++){{for(auditJ=1;auditJ<auditI;auditJ++){{auditFF=auditFF,auditA*auditV[auditI]*auditV[auditJ]-auditB0*auditU[auditJ]*auditV[auditI]+auditC0*auditU[auditI]*auditU[auditJ];}}}}',
'print("BUILD FFITT"); ideal auditGFF=std(auditFF); print("FFITT dim="+string(dim(auditGFF))+" vdim="+string(vdim(auditGFF)));',
'auditStats(auditGFF,"FFITT");',
f'for(auditI=1;auditI<={m};auditI++){{auditRem=reduce(auditDs[auditI],auditGFF); auditP1=(auditRem==0); auditP2=1; if(!auditP1){{auditP2=(reduce(auditRem^2,auditGFF)==0);}}print("DFITT "+string(auditI)+" power1="+string(auditP1)+" power2="+string(auditP2));}}',
f'map auditDirect=auditSource,{",".join(pv)},0;',
'ideal auditSlice=auditDirect(auditRows),auditDirect(auditTop); poly auditTau0=auditDirect(auditTau); ideal auditGS=std(auditSlice);',
'print("SLICE dim="+string(dim(auditGS))+" vdim="+string(vdim(auditGS))+" tau="+string(reduce(auditTau0,auditGS)==0));',
'auditStats(auditGS,"SLICE");',
'print("AUDIT_BASE_DONE"); quit;']
if minors_only:
    cutoff=lines.index('ideal auditF=0; ideal auditDs;')
    lines=lines[:cutoff]+[
        'ideal auditMI=0;',
        f'for(auditI=1;auditI<={m};auditI++){{for(auditJ=1;auditJ<auditI;auditJ++){{auditMI=auditMI,auditV[auditI]*auditU[auditJ]-auditV[auditJ]*auditU[auditI];}}}}',
        'print("BUILD MINORS"); ideal auditGMI=std(auditMI); print("MINORS dim="+string(dim(auditGMI))+" vdim="+string(vdim(auditGMI)));',
        'if(dim(auditGMI)==0){auditStats(auditGMI,"MINORS");}',
        'print("AUDIT_MINORS_DONE");quit;']
name=f'audit_minors_t{t}.sing' if minors_only else f'audit_baseprobe_t{t}.sing'
(root/name).write_text('\n'.join(lines)+'\n')
print(root/name)
