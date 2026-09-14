#!/usr/bin/env python3
"""Small exact-Q independent checks for the two direct Abel t=2 fibres."""
from pathlib import Path
import re
import sympy as s

root=Path(__file__).resolve().parent
c,b,x=s.symbols('c1 b x')
aa,bb,cc,dd=s.symbols('aa bb cc dd')
for d in (-1,1):
    raw=(root/f'controls_t2_d{d}_raw.sing').read_text()
    rows=[s.sympify(z.replace('^','**')) for z in re.search(r'ideal rows=(.*);',raw)[1].split(',')]
    target=s.sympify(re.search(r'poly target=(.*);',raw)[1].replace('^','**'))
    mult=[aa*c,bb*c*c,cc*c**3+dd*b]
    eq=s.Poly(s.expand(sum(u*v for u,v in zip(mult,rows))-target),c,b)
    sol=s.solve(eq.coeffs(),[aa,bb,cc,dd],dict=True)[0]
    free=set().union(*(z.free_symbols for z in sol.values()))
    sol={k:v.subs(dict.fromkeys(free,0)) for k,v in sol.items()}
    cert=[v.subs(sol).subs(dict.fromkeys({aa,bb,cc,dd}-set(sol),0)) for v in mult]
    assert s.expand(sum(u*v for u,v in zip(cert,rows))-target)==0
    y=s.Rational(d+3,10); C=x; om=3*(2*d-1)/(4*y*y*9)
    W=om*x**5+(s.Rational(5,2) if d==-1 else -s.Rational(1,4))*b*x*x
    A=3*x**3*C*C/(4*y*y); D=3*b*x*C/(2*y); K=x*x*C-y*b
    rhs=W*W+(-2*A+D)*W+A*(A-D)/3+(b*b*A/2-b*b*W)/x
    residual=s.expand(2*(x*W-b*b/4)*s.diff(W,x)-rhs)
    assert residual==(0 if d==-1 else -2*b*b*x**4)
    print(f'd={d}, y={y}, CERT_MULTIPLIERS={cert}, EXACT_IDENTITY_PASS')
    print(f'C=x FAMILY W={W}, B=eta=0, RESIDUAL={residual}')
print('T2_CERTIFICATES_DONE')
