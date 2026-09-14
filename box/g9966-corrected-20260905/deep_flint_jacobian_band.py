#!/usr/bin/env python3
"""Exact t-series arithmetic with FLINT QQ multivariate coefficients.

The coefficient ring includes w and every active original/graph coordinate.
The full chart ring is maintained by the caller. A t cutoff retains all
coefficient dependencies for the requested band; no coordinate or component
is removed. All bracket identities are controlled against sparse SymPy rows.
"""
from collections import defaultdict
from pathlib import Path
import hashlib,json,sys,time
import sympy as sp


def jacobian_band(h,C2,C3,outer,cutoff,source,progress=None):
    from flint import fmpq,fmpq_mpoly_ctx
    polys=[h,C2,C3]+list(outer.values())
    variables=sorted(set().union(*(value.free_symbols for poly in polys for value in poly.values())),key=str)
    w=sp.Symbol('w');assert w not in variables
    variables=[w]+variables
    index={v:i for i,v in enumerate(variables)}
    ctx=fmpq_mpoly_ctx.get(tuple(map(str,variables)),'lex')
    zero=ctx.constant(0)
    def encode(poly):
        rows=defaultdict(dict)
        for (r,k),expression in poly.items():
            if r>cutoff:continue
            for monomial,coefficient in expression.as_coefficients_dict().items():
                assert coefficient.is_Rational
                exponent=[0]*len(variables);exponent[0]=k
                for variable,power in monomial.as_powers_dict().items():
                    if variable==1:continue
                    assert variable in index and power.is_Integer and power>=0,(variable,power)
                    exponent[index[variable]]+=int(power)
                key=tuple(exponent);value=fmpq(int(coefficient.p),int(coefficient.q))
                rows[r][key]=rows[r].get(key,fmpq(0))+value
        return {r:p for r,row in rows.items() if not (p:=ctx.from_dict(row)).is_zero()}
    def add(*series):
        out={}
        for poly in series:
            for r,value in poly.items():out[r]=out.get(r,zero)+value
        return {r:p for r,p in out.items() if not p.is_zero()}
    def scale(poly,value):return {r:value*p for r,p in poly.items() if value!=0}
    def mul(a,b):
        out={}
        for r,left in a.items():
            for s,right in b.items():
                if r+s<=cutoff:out[r+s]=out.get(r+s,zero)+left*right
        return {r:p for r,p in out.items() if not p.is_zero()}
    def mul_band(a,b):
        out=zero
        for r,left in a.items():
            if cutoff-r in b:out=out+left*b[cutoff-r]
        return out
    def bracket(a,b,D,E):
        out={};da={r:p.derivative(0) for r,p in a.items()};db={r:p.derivative(0) for r,p in b.items()}
        for r,left in a.items():
            for s,right in b.items():
                if r+s<=cutoff:
                    value=(D-r)*left*db[s]-(E-s)*da[r]*right
                    out[r+s]=out.get(r+s,zero)+value
        return {r:p for r,p in out.items() if not p.is_zero()}
    tick=time.monotonic()
    hh,c2,c3=map(encode,(h,C2,C3))
    out={name:{r+1:p for r,p in encode(poly).items() if r+1<=cutoff} for name,poly in outer.items()}
    if progress:progress(f'FLINT encoded {len(variables)} active coefficient variables; {time.monotonic()-tick:.2f}s')
    inner_power={0:ctx.constant(1)}
    for _ in range(source['inner_power']):inner_power=mul(inner_power,hh)
    H=add(inner_power,mul(c2,hh),c3)
    A,B,C,D=(out[n] for n in ('A2','A3','B1','B2'))
    degree=source['k2_degree'];dA=source['n']-degree;dB=source['n'];dC=source['m']-degree;dD=source['m']
    H2=mul(H,H)
    left=mul_band(add(scale(H2,source['outer_power_F']),A),add(mul(H,bracket(H,C,degree,dC)),bracket(H,D,degree,dD)))
    right=mul_band(add(scale(H,source['outer_power_G']),C),add(mul(H,bracket(H,A,degree,dA)),bracket(H,B,degree,dB)))
    final=left-right+mul_band(H2,bracket(A,C,dA,dC))+mul_band(H,bracket(A,D,dA,dD))+mul_band(H,bracket(B,C,dB,dC))+bracket(B,D,dB,dD).get(cutoff,zero)
    if progress:progress(f'FLINT exact products complete; band has {len(final.to_dict())} terms; {time.monotonic()-tick:.2f}s')
    grouped=defaultdict(list)
    for exponent,coefficient in final.to_dict().items():
        monomial=sp.Mul(*(variable**power for variable,power in zip(variables[1:],exponent[1:]) if power))
        grouped[exponent[0]].append(sp.Rational(int(coefficient.numerator),int(coefficient.denominator))*monomial)
    band={k:sp.Add(*terms) for k,terms in grouped.items()}
    return band,{'coefficient_field':'Q','backend':'python-flint fmpq_mpoly',
        'active_computation_generators':list(map(str,variables)),'band_terms':len(final.to_dict()),
        't_cutoff':cutoff,'full_chart_coordinates_removed':False,'elapsed_seconds':time.monotonic()-tick,
        'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def control(code):
    sys.path.insert(0,str(code))
    import deep_rows as R
    from source_data import SOURCE as S
    a,b,c,d=sp.symbols('a b c d')
    h={(0,1):sp.Integer(1),(1,0):a,(2,1):sp.Rational(2,3)*b}
    c2={(1,0):c};c3={(2,1):sp.Rational(3,7)*d}
    outer={name:{(1,0):sp.Symbol(name+'0'),(2,1):sp.Symbol(name+'1')} for name in ['A2','A3','B1','B2']}
    checked=[]
    for cutoff in range(7):
        H=R.plus(R.times(R.times(h,h,cutoff),h,cutoff),R.times(c2,h,cutoff),c3)
        expected={k:value for (r,k),value in R.jacobian_factored(H,outer,cutoff).items() if r==cutoff}
        got,meta=jacobian_band(h,c2,c3,outer,cutoff,S)
        assert all(sp.expand(got.get(k,0)-expected.get(k,0))==0 for k in set(got)|set(expected))
        checked.append({'t':cutoff,'coefficient_slots':len(set(got)|set(expected)),**meta})
    zero,_=jacobian_band(h,c2,c3,{name:{} for name in outer},6,S)
    assert not zero
    return {'status':'PASS','all_rows_equal_to_independent_SymPy_sparse_formula':True,'zero_outer_zero_J':True,'checks':checked}

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser();ap.add_argument('--code',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    result=control(args.code.resolve());args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print('FLINT exact coefficient controls PASS',flush=True)
