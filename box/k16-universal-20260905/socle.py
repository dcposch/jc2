#!/usr/bin/env python3
"""Socle degree of J=(E_2..E_2t) (weights wt c_j=j, wt b=t+1) from the frozen rows: max weight of a kbase monomial.
Used to decide which bottom-up memberships are non-vacuous:  wt(N_k) = 2N-k + 2N(k-3) = (2N-1)k - 4N.  Usage: socle.py t [p droot]"""
import sys
from pathlib import Path
t=int(sys.argv[1]); N=t+1
p = int(sys.argv[2]) if len(sys.argv)>2 else 0; dr = int(sys.argv[3]) if len(sys.argv)>3 else 0
frz=(Path('/home/ubuntu/jc2/box/k16xempty-20260905')/f'controls_t{t}_raw.sing').read_text()
cs=','.join(f'c{i}' for i in range(1,t)); wts=','.join(map(str,list(range(1,t))+[t+1]))
if p:
    frz = frz.replace('ring rsmall=(0,d),', f'ring rsmall={p},').replace('minpoly=3*d^2-'+str(N)+';', f'number d={dr};')
s=[frz, 'option(redSB); ideal gg=std(rows); int mx=0; int i; ideal kb=kbase(gg);',
   'for(i=1;i<=size(kb);i++){ if(deg(kb[i])>mx){mx=deg(kb[i]);} }',
   f'print("SOCLE t={t} vdim="+string(vdim(gg))+" socle_degree="+string(mx));',
   f'int k; for(k=4;k<={4*N};k++){{ print("WT_N_k k="+string(k)+" wt="+string((2*N-1)*k-4*N)+" nonvacuous="+string(((2*N-1)*k-4*N)<=mx)); }}',
   'quit;']
out=Path(f'{Path(__file__).parent}/socle_t{t}'+(f'_p{p}' if p else '')+'.sing'); out.write_text('\n'.join(s)+'\n'); print(out)
