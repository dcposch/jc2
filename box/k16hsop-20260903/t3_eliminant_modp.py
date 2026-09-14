#!/usr/bin/env python3
"""Decisive modular re-check at t=3 of the two comparisons that expression swell
left inconclusive in the exact run: W_r == Res_b3(Q_0,G_r), and W_r in J^tail."""
import json, itertools, sympy as sp
y,b4,u2,b3 = sp.symbols('y b4 u2 b3'); t=3; q=2*t+1; p=1009
H = 12*q**2*y**2-12*q*(t+1)*y+(t+1)*(3*t+2)
roots=[r for r in range(p) if int(sp.Poly(H,y).eval(r))%p==0]
D=json.load(open('/home/ubuntu/jc2/box/k16hsop-20260903/tail_t3_rows.json'))
T={int(k):sp.sympify(v) for k,v in D['rows'].items()}
a={int(k):sp.sympify(v) for k,v in D['a'].items()}
B={int(k):sp.sympify(v) for k,v in D['B'].items()}
Cc={int(k):sp.sympify(v) for k,v in D['C'].items()}
a0=sp.sympify(D['a0'])
def modp(e,yv):
    e=sp.together(sp.expand(e)); n,dd=sp.fraction(e)
    n=sp.Poly(sp.expand(n),b4,u2,b3,y); dd=sp.expand(dd)
    dn=int(sp.Poly(dd,y).eval(yv))%p if dd.has(y) else int(dd)%p
    inv=pow(dn,p-2,p); out=0
    for mo,co in zip(n.monoms(),n.coeffs()):
        co=sp.Rational(co); cc=int(co.p)%p*pow(int(co.q)%p,p-2,p)%p
        cc=cc*pow(yv,mo[3],p)%p
        out+=cc*b4**mo[0]*u2**mo[1]*b3**mo[2]
    return sp.expand(out*inv)
for yv in roots:
    Q0=modp(T[5],yv); A0=modp(a0,yv)
    b0=sp.Poly(Q0,b3).nth(1); c0=sp.Poly(Q0,b3).nth(0)
    G=sp.groebner([modp(T[k],yv) for k in (3,4,5)],b4,u2,b3,order='grevlex',modulus=p)
    for r in (1,2):
        Br=modp(B[r],yv); Cr=modp(Cc[r],yv)
        W=sp.expand(A0*Cr**2-b0*Br*Cr+c0*Br**2)
        Gr=sp.expand(modp(a0,yv)*modp(T[5-r],yv)-modp(a[r],yv)*Q0)
        # cross-check W against the definition via the linearised row Gr:
        chk=sp.expand(sp.Poly(Br**2*Q0-Gr*(A0*Gr-2*A0*Cr+b0*Br)-W, b4,u2,b3, modulus=p).as_expr())
        red=G.reduce(W)[1]
        print(f"  y={yv} r={r}: certificate identity holds mod p : {chk==0} ;"
              f"  NF(W_r, GB(J)) == 0 : {red==0} ;  W_r nonzero : {sp.Poly(W,b4,u2,modulus=p).as_expr()!=0}")
