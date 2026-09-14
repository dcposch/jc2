#!/usr/bin/env python3
"""Inject exact coefficient-coordinate image checks into the fresh recurrence."""
from pathlib import Path
import subprocess,sys
t=int(sys.argv[1]);p=Path(__file__).resolve().parent
src=subprocess.check_output([sys.executable,str(p/'emit_arrays.py'),str(t),'--out',str(p/f't{t}_coordinate_rows.sing')],text=True)
gamma=f'(({108*t**3+126*t*t+8*t+8})*d-{24*t*(t*t-1)})/(({72*t**3+90*t*t+16*t+8})*d-{4*t*(3*t-4)*(t+1)})'
for j in range(1,t):
    target=f'print("PIVOT {j} PASS");'
    if j==1:
        extra=f'must(val==({gamma})*b4,"C1_COORDINATE");'
    else:
        AC=9*j*j*t+18*j*j-54*j*t*t-81*j*t-26*j+72*t**3+144*t*t+88*t+16
        BC=-9*j*j*t-10*j*j+24*j*t*t+33*j*t+10*j-12*t**3-20*t*t-8*t
        pc=f'({3*t*(3*t+1)}*({AC}*d+{BC})/{(t+1)*(3*t+2)**3*(4*t-2*j+1)})'
        pq=f'({(3*t+1)*t*(2*t+1-j)}*(({j-4*t-4})*d-{2*(t+1)})/({(2*t+1)*(4*t-2*j+1)}*(d+{t+1})^2))'
        extra=f'must(diff(val,u{j})==-({pq})/({pc}),"CJ_COORDINATE_{j}");'
    src=src.replace(target,target+extra)
print(src.replace('print("ROWS_COMPLETE");','print("COORDINATE_IMAGES_PASS"); print("ROWS_COMPLETE");'))
