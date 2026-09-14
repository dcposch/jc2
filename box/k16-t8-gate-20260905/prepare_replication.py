#!/usr/bin/env python3
"""Rebuild t8 second-prime inputs from charged exact rational expressions.
No finite-field coefficient is relabelled. All changes to source driver are asserted.
Run Singular -q affinew_p32027.sing, then this script --convert.
"""
from pathlib import Path
import hashlib,json,re,sys
D=Path(__file__).resolve().parent
S=D.parent/'k16t8-20260905'
p=32027
if '--convert' in sys.argv:
 raw=(D/f'affinew_p{p}_raw.txt').read_text().splitlines()
 assert raw.pop(0)=='BEGIN' and len(raw)==28
 polys=[re.sub(r'\bq([2-7])_0\b',r'q\1',s) for s in raw]
 assert all(re.fullmatch(r'[0-9q+*^\- ]+',s) for s in polys)
 assert set(re.findall(r'[A-Za-z_]\w*','\n'.join(polys)))=={f'q{j}' for j in range(2,8)}
 ms='q2,q3,q4,q5,q6,q7\n'+str(p)+'\n'+',\n'.join(polys)+'\n'
 (D/f'affinew_p{p}.ms').write_text(ms)
 print('EXPORT PASS',len(polys),len(ms),hashlib.sha256(ms.encode()).hexdigest())
else:
 src=S/'affinewms2_t8_mod_p32003_b0.sing'
 x=src.read_text()
 assert hashlib.sha256(x.encode()).hexdigest()=='4c8684cda0e18f0fa8cf5e97af0b460fe443b265961092667de2bbe1307cacf3'
 roots=[r for r in range(p) if (3468*r*r-1836*r+234)%p==0]
 assert roots==[23825,25158]
 den=list(map(int,re.findall(r'/([0-9]+)',x)))
 assert len(den)==9584 and not any(d%p==0 for d in den)
 y=x.replace('ring S=(32003)',f'ring S=({p})').replace('ring P=(32003)',f'ring P=({p})').replace('number yy=11288;',f'number yy={roots[0]};')
 assert y.count(f'number yy={roots[0]};')==2
 assert y.count(f'ring S=({p})')==1 and y.count(f'ring P=({p})')==1
 y=y.replace('prime=32003',f'prime={p}').replace('p32003',f'p{p}').replace(str(S/'affinew_raw.txt'),str(D/f'affinew_p{p}_raw.txt'))
 (D/f'affinew_p{p}.sing').write_text(y)
 print('DRIVER PASS',hashlib.sha256(y.encode()).hexdigest())
