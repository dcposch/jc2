#!/usr/bin/env python3
"""Emit a bounded fixed-index homogeneous cone probe; never promote lengths."""
from pathlib import Path
import argparse
ap=argparse.ArgumentParser();ap.add_argument('tag');ap.add_argument('t',type=int)
ap.add_argument('--tail',action='store_true');ap.add_argument('--hint',action='store_true')
a=ap.parse_args();t=a.t;p=Path(__file__).resolve().parent
print(f'< "{p/f"{a.tag}_rows.sing"}";')
print('ideal src='+','.join('T'+str(k) for k in range(t if a.tail else 1,2*t))+';')
vs=['b3','b4']+[f'u{i}' for i in range(2,t)];w=[t+1]+list(range(1,t))
print(f'ring rcone=32003,({",".join(vs)}),wp({",".join(map(str,w))});')
print('ideal I=imap(rres,src);')
print('int i; for(i=1;i<=size(I);i++) { if(!homog(I[i])) { print("FAIL HOMOG"); quit; } }')
print('print("CONE_START");')
if a.hint:
    assert a.tail
    h=[1]
    for deg in range(2*t+2,3*t+2):
        hh=h+[0]*deg
        for j,c in enumerate(h): hh[j+deg]-=c
        h=hh
    print('intvec HH='+','.join(map(str,h))+';')
    print('intvec ww='+','.join(map(str,w))+';')
    print('ideal G=std(I,HH,ww);')
else: print('ideal G=std(I);')
print('print("GB_DONE"); print("CONE_DIM "+string(dim(G))); print("CONE_VDIM "+string(vdim(G)));')
print('print("INPUT_NF_ZERO "+string(size(reduce(I,G))==0));')
print('print("BASIS_SIZE "+string(size(G)));')
print('ideal LM=lead(G); print("LEAD_DIM "+string(dim(std(LM))));')
kind='tailhint' if a.hint else 'tail' if a.tail else 'plus'
print(f'write("{p/f"{a.tag}_{kind}_leaders.txt"}",string(LM));')
print('print("CONE_COMPLETE");quit;')
