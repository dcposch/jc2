#!/usr/bin/env python3
"""Direct F/G differentiation in an explicitly proved monic quadratic quotient.

Every coefficient is the COMBINED class A+B*d. No coefficient of that class
is separately set to zero, and neither conjugate of d is selected.
"""
from collections import defaultdict
from math import comb
from pathlib import Path
import hashlib,time
import flint
from flint import fmpq,fmpq_mpoly_ctx
import sympy as sp
OWN_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def band(h,c2,c3,outer,cap,source,relation,generator):
    start=time.monotonic();d=sp.Symbol(str(generator));q=sp.expand(relation)
    qpoly=sp.Poly(q,d);assert qpoly.degree()==2 and qpoly.LC()==1
    qa,qb=qpoly.nth(1),qpoly.nth(0)
    assert d not in qa.free_symbols|qb.free_symbols
    source_symbols=set().union(*(sp.sympify(value).free_symbols for poly in [h,c2,c3,*outer.values()] for value in poly.values()))|q.free_symbols
    all_symbols=sorted(source_symbols,key=str);base_symbols=sorted(source_symbols-{d},key=str)
    assert d in all_symbols
    z=sp.Symbol('verification_z');assert z not in source_symbols
    names=tuple(map(str,[z,*base_symbols]));ctx=fmpq_mpoly_ctx.get(names,'lex')
    for i in range(len(names)):
        exponent=tuple(int(i==j) for j in range(len(names)))
        assert ctx.from_dict({exponent:fmpq(1)}).to_dict()=={exponent:fmpq(1)}
    zero=ctx.constant(0);one=ctx.constant(1);PZERO=(zero,zero);PONE=(one,zero);DELTA=(zero,one)
    positions={symbol:i for i,symbol in enumerate(all_symbols)}
    def native_scalar(expr,zpower=0):
        terms=sp.Poly(expr,*base_symbols,domain=sp.QQ).terms() if base_symbols else [((),sp.Rational(expr))]
        return ctx.from_dict({(zpower,*exponents):fmpq(int(value.p),int(value.q)) for exponents,value in terms})
    na,nb=native_scalar(qa),native_scalar(qb)
    assert na.derivative(0).is_zero() and nb.derivative(0).is_zero(),'quadratic relation depends on the source coordinate'
    def addpair(a,b):return a[0]+b[0],a[1]+b[1]
    def scalepair(a,c):return c*a[0],c*a[1]
    def mulpair(a,b):
        cross=a[1]*b[1]
        return a[0]*b[0]-nb*cross,a[0]*b[1]+a[1]*b[0]-na*cross
    def zeropair(a):return a[0].is_zero() and a[1].is_zero()
    def derivative(a):return a[0].derivative(0),a[1].derivative(0)
    assert zeropair(addpair(addpair(mulpair(DELTA,DELTA),mulpair((na,zero),DELTA)),(nb,zero)))
    assert not zeropair(DELTA),'quadratic generator was silently removed'
    dpowers=[PONE,DELTA]
    def dpower(n):
        while len(dpowers)<=n:dpowers.append(mulpair(dpowers[-1],DELTA))
        return dpowers[n]
    def encode(poly):
        out={}
        for (r,k),value in poly.items():
            if r>cap:continue
            for monomial,coefficient in sp.Poly(sp.expand(value),*all_symbols,domain=sp.QQ).terms():
                exponent=(k,*[monomial[positions[symbol]] for symbol in base_symbols])
                scalar=ctx.from_dict({exponent:fmpq(int(coefficient.p),int(coefficient.q))})
                power=dpower(monomial[positions[d]])
                term=scalar*power[0],scalar*power[1]
                out[r]=addpair(out.get(r,PZERO),term)
        return {r:value for r,value in out.items() if not zeropair(value)}
    def add(*series):
        out={}
        for poly in series:
            for r,value in poly.items():out[r]=addpair(out.get(r,PZERO),value)
        return {r:value for r,value in out.items() if not zeropair(value)}
    def mul(a,b):
        out={}
        for r,left in a.items():
            for s,right in b.items():
                if r+s<=cap:out[r+s]=addpair(out.get(r+s,PZERO),mulpair(left,right))
        return {r:value for r,value in out.items() if not zeropair(value)}
    def power(poly,n):
        result={0:PONE}
        for _ in range(n):result=mul(result,poly)
        return result
    hh,c2,c3=map(encode,(h,c2,c3))
    outer={name:{r+1:value for r,value in encode(poly).items() if r+1<=cap} for name,poly in outer.items()}
    H=add(power(hh,source['inner_power']),mul(c2,hh),c3)
    F=add(power(H,source['outer_power_F']),mul(outer['A2'],H),outer['A3'])
    G=add(power(H,source['outer_power_G']),mul(outer['B1'],H),outer['B2'])
    J=PZERO
    for r,left in F.items():
        if cap-r in G:
            s=cap-r;right=G[s]
            J=addpair(J,addpair(scalepair(mulpair(left,derivative(right)),source['n']-r),
                               scalepair(mulpair(derivative(left),right),-(source['m']-s))))
    terms=defaultdict(list)
    for dpower_index,poly in enumerate(J):
        for exponent,coefficient in poly.to_dict().items():
            value=sp.Rational(int(coefficient.numerator),int(coefficient.denominator))*d**dpower_index
            value*=sp.Mul(*(symbol**n for symbol,n in zip(base_symbols,exponent[1:]) if n))
            for k in range(exponent[0]+1):terms[k].append(value*comb(exponent[0],k)*(-1)**(exponent[0]-k))
    output={k:value for k,pieces in terms.items() if (value:=sp.Add(*pieces))!=0}
    assert all(sp.degree(value,d)<=1 for value in output.values())
    meta={'method':'full normalized F/G construction and direct derivatives in the declared monic quotient; z=w-1 after the band',
          'coefficient_field':'Q','python_flint_version':flint.__version__,
          'base_generator_order':list(names),'retained_quotient_generator':str(d),'relation':str(q),
          'generator_images':[{'source':str(symbol),'native_index':i+1,'pair':[str(symbol),'0']} for i,symbol in enumerate(base_symbols)]+[{'source':str(d),'pair':['0','1']}],
          'native_generator_images_checked':True,
          'quotient_basis':['1',str(d)],'combined_A_plus_B_delta_rows':True,
          'conjugate_selected':False,'monic_relation_identity_checked':True,
          'source_derivatives_commute_with_relation':True,'requested_t_power':cap,
          'helper_sha256_at_import':OWN_SHA256,'elapsed_seconds':time.monotonic()-start}
    return output,meta


if __name__=='__main__':
    import argparse,json,sys
    ap=argparse.ArgumentParser();ap.add_argument('--code',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    sys.path.insert(0,str(a.code.resolve()));import engine as E
    d,e,b=sp.symbols('test_delta test_e test_b');q=d**2+sp.Rational(2,3)*e*d+sp.Rational(5,7)*b
    h={(0,2):sp.Integer(1),(1,0):d,(2,1):e};c2={(2,0):d**3+b};c3={(3,1):d**4-e}
    outer={name:{(1,0):d+sp.Symbol(name+'_c'),(2,1):e} for name in ('A2','A3','B1','B2')}
    checked=[]
    for cap in range(7):
        H=E.tz_add(E.tz_mul(E.tz_mul(h,h,cap),h,cap),E.tz_mul(c2,h,cap),c3)
        F,G=E.build_FG(H,outer,cap);raw=E.jacobian_band(F,G,cap)
        expected={k:sp.expand(sp.rem(value,q,d)) for k,value in raw.items()}
        actual,meta=band(h,c2,c3,outer,cap,E.S,q,d)
        assert all(sp.expand(actual.get(k,0)-expected.get(k,0))==0 for k in set(actual)|set(expected))
        checked.append(meta)
    a.out.write_text(json.dumps({'status':'PASS','independent_unreduced_SymPy_FG_then_monic_remainder_matches':True,'checks':checked},indent=2,sort_keys=True)+'\n')
    print('Independent direct quotient F/G controls PASS',flush=True)
