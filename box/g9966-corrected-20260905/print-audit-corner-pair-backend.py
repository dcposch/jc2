#!/usr/bin/env python3
"""Rank-two coefficient arithmetic modulo a retained monic quadratic.

A pair(A,B) represents the ONE polynomial A+B*d in the full source ring.
The relation q=d²-a*d*e²+b*e⁴ remains an explicit locus generator. Neither
pair component is imposed separately and neither root is selected.
"""
from collections import defaultdict
from pathlib import Path
import hashlib,time
import sympy as sp


def jacobian_bands(h,C2,C3,outer,cutoff,source,first_band=0,progress=None,quotient=None):
    from flint import fmpq,fmpq_mpoly_ctx
    assert quotient,'this coefficient engine requires an explicitly certified monic quotient'
    d,e=sp.Symbol(quotient['d']),sp.Symbol(quotient['e'])
    qa,qb=sp.Rational(quotient['a']),sp.Rational(quotient['b'])
    assert sp.expand(sp.sympify(quotient['polynomial'])-(d*d-qa*d*e*e+qb*e**4))==0
    polys=[h,C2,C3]+list(outer.values())
    variables=sorted(set().union(*(v.free_symbols for p in polys for v in p.values()))|{e},key=str)
    variables=[v for v in variables if v!=d];w=sp.Symbol('w');assert w not in variables
    variables=[w]+variables;index={v:i for i,v in enumerate(variables)}
    ctx=fmpq_mpoly_ctx.get(tuple(map(str,variables)),'lex');z=ctx.constant(0);one=ctx.constant(1)
    qA_native=fmpq(int(qa.p),int(qa.q));qB_native=fmpq(int(qb.p),int(qb.q))
    e2=ctx.gen(index[e])**2;e4=e2*e2;pairzero=(z,z)
    recurrence=[(fmpq(0),fmpq(1)),(fmpq(1),fmpq(0))]
    def pa(x,y):return (x[0]+y[0],x[1]+y[1])
    def ps(x,n):return (n*x[0],n*x[1])
    def pm(x,y):
        bd=x[1]*y[1]
        return (x[0]*y[0]-qB_native*e4*bd,x[0]*y[1]+x[1]*y[0]+qA_native*e2*bd)
    def pd(x):return (x[0].derivative(0),x[1].derivative(0))
    def pn(x):return not(x[0].is_zero() and x[1].is_zero())
    def encode(poly):
        rows=defaultdict(lambda:({},{}))
        for (r,k),expression in poly.items():
            if r>cutoff:continue
            for monomial,coefficient in expression.as_coefficients_dict().items():
                assert coefficient.is_Rational
                exponent=[0]*len(variables);exponent[0]=k;dpower=0
                for variable,power in monomial.as_powers_dict().items():
                    if variable==1:continue
                    assert power.is_Integer and power>=0
                    if variable==d:dpower+=int(power)
                    else:
                        assert variable in index
                        exponent[index[variable]]+=int(power)
                value=fmpq(int(coefficient.p),int(coefficient.q))
                while len(recurrence)<=dpower:
                    left,right=recurrence[-1];recurrence.append((qA_native*left+right,-qB_native*left))
                if dpower==0:
                    target=tuple(exponent);rows[r][0][target]=rows[r][0].get(target,fmpq(0))+value
                else:
                    left,right=recurrence[dpower]
                    if left:
                        target=list(exponent);target[index[e]]+=2*dpower-2;target=tuple(target)
                        rows[r][1][target]=rows[r][1].get(target,fmpq(0))+value*left
                    if right:
                        target=list(exponent);target[index[e]]+=2*dpower;target=tuple(target)
                        rows[r][0][target]=rows[r][0].get(target,fmpq(0))+value*right
        return {r:p for r,(a,b) in rows.items() if pn(p:=(ctx.from_dict(a),ctx.from_dict(b)))}
    def add(*series):
        out={}
        for poly in series:
            for r,value in poly.items():out[r]=pa(out.get(r,pairzero),value)
        return {r:p for r,p in out.items() if pn(p)}
    def scale(poly,value):return {r:ps(p,value) for r,p in poly.items() if value!=0}
    def mul(a,b):
        out={}
        for r,left in a.items():
            for s,right in b.items():
                if r+s<=cutoff:out[r+s]=pa(out.get(r+s,pairzero),pm(left,right))
        return {r:p for r,p in out.items() if pn(p)}
    def bracket(a,b,D,E):
        out={};da={r:pd(p) for r,p in a.items()};db={r:pd(p) for r,p in b.items()}
        for r,left in a.items():
            for s,right in b.items():
                if r+s<=cutoff:
                    value=pa(ps(pm(left,db[s]),D-r),ps(pm(da[r],right),-(E-s)))
                    out[r+s]=pa(out.get(r+s,pairzero),value)
        return {r:p for r,p in out.items() if pn(p)}
    tick=time.monotonic();hh,c2,c3=map(encode,(h,C2,C3))
    out={name:{r+1:p for r,p in encode(poly).items() if r+1<=cutoff} for name,poly in outer.items()}
    if progress:progress(f'FLINT rank-two quotient encoded {len(variables)} base generators plus retained {d}; {time.monotonic()-tick:.2f}s')
    power={0:(one,z)}
    for _ in range(source['inner_power']):power=mul(power,hh)
    H=add(power,mul(c2,hh),c3);A,B,C,D=(out[n] for n in ('A2','A3','B1','B2'))
    degree=source['k2_degree'];dA=source['n']-degree;dB=source['n'];dC=source['m']-degree;dD=source['m']
    H2=mul(H,H)
    left=mul(add(scale(H2,source['outer_power_F']),A),add(mul(H,bracket(H,C,degree,dC)),bracket(H,D,degree,dD)))
    right=mul(add(scale(H,source['outer_power_G']),C),add(mul(H,bracket(H,A,degree,dA)),bracket(H,B,degree,dB)))
    J=add(left,scale(right,-1),mul(H2,bracket(A,C,dA,dC)),mul(H,bracket(A,D,dA,dD)),mul(H,bracket(B,C,dB,dC)),bracket(B,D,dB,dD))
    result={};termcount=0
    for tp in range(first_band,cutoff+1):
        grouped=defaultdict(list)
        for component,poly in enumerate(J.get(tp,pairzero)):
            termcount+=len(poly.to_dict())
            for exponent,coefficient in poly.to_dict().items():
                term=sp.Rational(int(coefficient.numerator),int(coefficient.denominator))*sp.Mul(*(v**int(n) for v,n in zip(variables[1:],exponent[1:]) if n))
                if component:term*=d
                grouped[exponent[0]].append(term)
        result[tp]={k:sp.Add(*terms) for k,terms in grouped.items()}
    if progress:progress(f'FLINT quotient bands {first_band}..{cutoff}: {termcount} terms; {time.monotonic()-tick:.2f}s')
    return result,{'coefficient_field':'Q','backend':'python-flint rank-two module','base_generators':list(map(str,variables)),
        'retained_ring_variable':str(d),'basis':['1',str(d)],'basis_images':{str(d):['0','1']},
        'quotient':quotient,'emitted_row':'ONE combined polynomial A+B*d; neither component separately',
        'first_band':first_band,'t_cutoff':cutoff,'band_terms':termcount,'elapsed_seconds':time.monotonic()-tick,
        'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def jacobian_band(h,C2,C3,outer,cutoff,source,progress=None,quotient=None):
    result,meta=jacobian_bands(h,C2,C3,outer,cutoff,source,first_band=cutoff,progress=progress,quotient=quotient)
    return result[cutoff],meta
