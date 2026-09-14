#!/usr/bin/env python3
"""Independent full-F/G Jacobian coefficient construction over exact QQ.

Unlike the production engine, this builds F and G and differentiates them;
it never uses the factored approximate-root bracket identity. The z->w-1
change is applied after the complete requested Jacobian coefficient.
"""
from collections import defaultdict
from math import comb
from pathlib import Path
import hashlib,json,time
import sympy as sp
import flint
from flint import fmpq,fmpq_mpoly_ctx


def band(h,c2,c3,outer,cap,source):
    start=time.monotonic();polys=[h,c2,c3,*outer.values()]
    symbols=sorted(set().union(*(sp.sympify(x).free_symbols for poly in polys for x in poly.values())),key=str)
    z=sp.Symbol('verification_z');assert z not in symbols
    variables=[z,*symbols];index={x:i for i,x in enumerate(variables)}
    names=tuple(map(str,variables));assert len(names)==len(set(names))
    ctx=fmpq_mpoly_ctx.get(names,'lex');zero=ctx.constant(0)
    for i in range(len(variables)):
        exponent=tuple(int(i==j) for j in range(len(variables)))
        assert ctx.from_dict({exponent:fmpq(1)}).to_dict()=={exponent:fmpq(1)},'native generator image mismatch'
    def encode(poly):
        buckets=defaultdict(dict)
        for (r,k),value in poly.items():
            if r>cap:continue
            value=sp.expand(value)
            if symbols:terms=sp.Poly(value,*symbols,domain=sp.QQ).terms()
            else:terms=[((),sp.Rational(value))]
            for monomial,coefficient in terms:
                exponent=(k,*monomial)
                assert len(exponent)==len(variables) and all(isinstance(x,int) and x>=0 for x in exponent)
                rational=fmpq(int(coefficient.p),int(coefficient.q))
                buckets[r][exponent]=buckets[r].get(exponent,fmpq(0))+rational
        return {r:value for r,terms in buckets.items() if not (value:=ctx.from_dict(terms)).is_zero()}
    def add(*polys):
        out={}
        for poly in polys:
            for r,value in poly.items():out[r]=out.get(r,zero)+value
        return {r:value for r,value in out.items() if not value.is_zero()}
    def mul(left,right):
        out={}
        for r,value in left.items():
            for s,other in right.items():
                if r+s<=cap:out[r+s]=out.get(r+s,zero)+value*other
        return {r:value for r,value in out.items() if not value.is_zero()}
    def power(poly,n):
        value={0:ctx.constant(1)}
        for _ in range(n):value=mul(value,poly)
        return value
    h,c2,c3=map(encode,(h,c2,c3))
    outer={name:{r+1:value for r,value in encode(poly).items() if r+1<=cap} for name,poly in outer.items()}
    H=add(power(h,source['inner_power']),mul(c2,h),c3)
    F=add(power(H,source['outer_power_F']),mul(outer['A2'],H),outer['A3'])
    G=add(power(H,source['outer_power_G']),mul(outer['B1'],H),outer['B2'])
    final=zero
    for r,left in F.items():
        if cap-r in G:
            s=cap-r;right=G[s]
            final+=(source['n']-r)*left*right.derivative(0)-(source['m']-s)*left.derivative(0)*right
    # Perform the affine source-coordinate conversion only after taking the
    # requested coefficient, independently of the production precomposition.
    output=defaultdict(list)
    terms=final.to_dict()
    for exponent,coefficient in terms.items():
        scalar=sp.Rational(int(coefficient.numerator),int(coefficient.denominator))
        monomial=sp.Mul(*(x**power for x,power in zip(symbols,exponent[1:]) if power))
        for k in range(exponent[0]+1):
            output[k].append(scalar*comb(exponent[0],k)*(-1)**(exponent[0]-k)*monomial)
    result={k:value for k,pieces in output.items() if (value:=sp.Add(*pieces))!=0}
    metadata={'method':'full normalized F/G construction, then direct derivatives, then z=w-1',
              'coefficient_field':'Q','generator_order':list(names),
              'python_flint_version':flint.__version__,'native_generator_monomial_images_checked':True,
              'generator_order_sha256':hashlib.sha256(('\n'.join(names)+'\n').encode()).hexdigest(),
              'generator_images':'index0 is normalized z; every remaining index is the declared same SymPy source symbol',
              'F_t_series_slots':len(F),'G_t_series_slots':len(G),'requested_t_power':cap,
              'Jacobian_z_terms':len(terms),'elapsed_seconds':time.monotonic()-start,
              'helper_sha256_at_import':OWN_SHA256}
    return result,metadata


OWN_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


if __name__=='__main__':
    import argparse,sys
    ap=argparse.ArgumentParser();ap.add_argument('--code',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    sys.path.insert(0,str(a.code.resolve()))
    import engine as E
    A,B,C,D=sp.symbols('source_A source_B source_C source_D')
    h={(0,2):sp.Integer(1),(1,0):A,(2,1):sp.Rational(2,3)*B}
    c2={(2,0):C};c3={(3,1):sp.Rational(5,7)*D}
    outer={name:{(1,0):sp.Symbol(name+'_c'),(2,1):sp.Symbol(name+'_l')} for name in ('A2','A3','B1','B2')}
    checks=[]
    for cap in range(7):
        H=E.tz_add(E.tz_mul(E.tz_mul(h,h,cap),h,cap),E.tz_mul(c2,h,cap),c3)
        F,G=E.build_FG(H,outer,cap)
        want=E.jacobian_band(F,G,cap);got,meta=band(h,c2,c3,outer,cap,E.S)
        assert all(sp.expand(got.get(k,0)-want.get(k,0))==0 for k in set(got)|set(want))
        checks.append(meta)
    zero,_=band(h,c2,c3,{name:{} for name in outer},6,E.S);assert not zero
    a.out.write_text(json.dumps({'status':'PASS','full_FG_SymPy_derivative_matches_all_coefficients_t0_through6':True,
                                'pure_power_zero_control':True,'checks':checks},indent=2,sort_keys=True)+'\n')
    print('Independent direct FLINT F/G controls PASS',flush=True)
