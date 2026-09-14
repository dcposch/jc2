#!/usr/bin/env python3
"""Emit exact controls, nilpotence and annihilator probes for fresh rows."""
from pathlib import Path
import argparse
ap=argparse.ArgumentParser()
ap.add_argument('tag')
ap.add_argument('t',type=int)
a=ap.parse_args()
p=Path(__file__).resolve().parent
t=a.t
rows=p/f'{a.tag}_rows.sing'
print(f'< "{rows}";')
print('option(redSB);')
print('proc must(int ok,string label) { if(!ok) { print("FAIL "+label); quit; } }')
print('ideal Iplus='+','.join('T'+str(i) for i in range(1,2*t))+';')
print('ideal Jtail='+','.join('T'+str(i) for i in range(t,2*t))+';')
print('ideal GI=std(Iplus);')
print('must(size(reduce(Iplus,GI))==0,"PLUS_GENERATORS");')
print('print("IPLUS_DIM "+string(dim(GI))); print("IPLUS_LENGTH "+string(vdim(GI)));')
print('poly remtau=reduce(tau,GI);')
print('print("TAU_NF_TERMS "+string(size(remtau))); print("TAU_NF "+string(remtau));')
print('print("FULL_T0_NONZERO "+string(reduce(T0,GI)!=0));')
print('int i; for(i=1;i<=4;i++) {print("TAU_POWER "+string(i)+" ZERO "+string(reduce(tau^i,GI)==0));}')
print('poly probe; for(i=1;i<=nvars(basering);i++) { probe=reduce(tau*var(i),GI); print("TAU_TIMES "+string(var(i))+" ZERO "+string(probe==0)); }')
print(f'write("{p/(a.tag+"_plus_basis.txt")}",string(GI));')
print('print("IPLUS_COMPLETE");')
print('ideal GJ=std(Jtail);')
print('must(size(reduce(Jtail,GJ))==0,"TAIL_GENERATORS");')
print('print("TAIL_DIM "+string(dim(GJ))); print("TAIL_LENGTH "+string(vdim(GJ)));')
print('for(i=1;i<=4;i++) {print("TAIL_TAU_POWER "+string(i)+" ZERO "+string(reduce(tau^i,GJ)==0));}')
print('print("TAIL_COMPLETE"); print("CHECKS_COMPLETE"); quit;')
