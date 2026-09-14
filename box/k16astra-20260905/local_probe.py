#!/usr/bin/env python3
from pathlib import Path
import sys
t=int(sys.argv[1]); p=Path(__file__).resolve().parent
print(f'< "{p/f"t{t}_local_rows.sing"}";')
print('poly db=diff(spineB2,b4); number rr=leadcoef(rootR)/leadcoef(db);')
print('print("ROOT_DERIVATIVE_PROPORTIONAL "+string(rootR==rr*db));')
print('print("ROOT_DERIVATIVE_RATIO "+string(rr));')
print('ideal gradient; int i; for(i=1;i<=nvars(basering);i++){gradient[i]=diff(spineB2,var(i));}')
print('ideal GG=std(gradient);')
print('print("ROOT_IN_GRADIENT "+string(reduce(rootR,GG)==0));')
print('print("LOCAL_PROBE_COMPLETE");quit;')
