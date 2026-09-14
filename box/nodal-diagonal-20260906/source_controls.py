#!/usr/bin/env python3
"""Independent exact-Q replay of source coefficient compiler operations."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import sympy as S
from source_stream import Source


def values(a,point=None):
    point=point or {};out=[]
    for i in range(0,len(a.code),3):
        op,l,r=a.code[i:i+3]
        out.append(a.constants[l] if op==0 else
                   Q(point[a.names[l]]) if op==1 else
                   out[l]+out[r] if op==2 else out[l]*out[r])
    return out


def main():
    x,y,u,z,t,pi=S.symbols('x y u z t pi')
    receipts=[]
    for client in ['99_delta2','99_delta52','108']:
        src=Source(client);a=src.A
        def enc(p):return {ij:a.const(Q(c)) for ij,c in S.Poly(S.expand(p),x,y).terms()}
        def dec(p,v):return S.expand(sum(S.Rational(v[c].numerator,v[c].denominator)*x**i*y**j for (i,j),c in p.items()))
        H=y*y+x*y+x*x+1;AA=x+y;AB=x*y+2
        F=S.expand(H**3+AA*H+AB)
        h=src.monic_root(enc(F),6,2)
        q,r=src.monic_div(src.ppadd(enc(F),src.pppow(h,3),-1),h,2)
        point={'B':2,'Binv':Q(1,2),'j':3}
        v=values(a,point)
        assert dec(h,v)==H and dec(q,v)==AA and dec(r,v)==AB
        rows=[[a.const(2),a.const(3),a.const(1)],[a.const(-1),a.const(4)]]
        phys=src.physical(rows,a.const(5));v=values(a,point)
        assert S.expand(dec(phys,v)-((x+5)**2+3*(x+5)+2+(y-x)*(-1+4*(x+5))))==0
        P=x**3*y**2+2*x*y**3+x-3
        src.up=src.constant_powers(a.const(2),src.n);src.vp=src.constant_powers(a.const(-1),src.n)
        before=len(src.rows);src.minor('minor_control',enc(P),100,[])
        v=values(a,point);actual={key:v[node] for tag,key,node in src.rows[before:]}
        L=2 if client=='99_delta52' else 1
        delta=5 if L==2 else (3 if client=='108' else 2)
        ref=S.expand(P.subs({x:t**(-L),y:2*t**L-t**(2*L)+pi*t**delta}))
        expected={}
        for term in S.Add.make_args(ref):
            powers=term.as_powers_dict();key=(int(powers.get(t,0)),int(powers.get(pi,0)))
            c=term/t**key[0]/pi**key[1]
            expected[key]=expected.get(key,Q(0))+Q(c)
        actual={k:c for k,c in actual.items() if c}
        expected={k:c for k,c in expected.items() if c}
        assert actual==expected,(client,actual,expected)
        # Wrong leading targets must leave a residual, not disappear in pivots.
        before=len(src.rows);src.minor('wrong_target_control',enc(P),100,[a.one])
        v=values(a,point)
        assert any(key==(100,0) and v[node]==-1 for _,key,node in src.rows[before:])
        receipts.append({'client':client,'monic_root_inverse':True,'division_inverse':True,
                         'physical_composition':True,'all_minor_coefficients_Q':True,
                         'wrong_target_detected':True})
    out={'status':'SOURCE_COMPILER_EXACT_Q_CONTROLS_PASS','controls':receipts,
         'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'source_driver_sha256':hashlib.sha256(Path(__file__).with_name('source_stream.py').read_bytes()).hexdigest(),
         'recurrence_driver_sha256':hashlib.sha256(Path(__file__).with_name('recurrence_stream.py').read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out['status'])


if __name__=='__main__':main()
