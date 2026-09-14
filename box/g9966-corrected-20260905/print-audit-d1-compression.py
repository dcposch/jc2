#!/usr/bin/env python3
"""Exact D1 face compression. No coordinate specialization or new equations.

Input is the five already derived Pi faces H,A2,A3,B1,B2. Output is the
coefficient rows of (3 P Q'-2 P' Q)/9 - Jc, with P=H^3+A2 H+A3,
Q=H^2+B1 H+B2. The pure-power cancellation is performed formally before
substitution. This file is an independent audit/helper, not a replacement
of the frozen run's row generator.
"""
from __future__ import annotations
import hashlib,json
from pathlib import Path
import sympy as sp

PI=sp.Symbol('Pi')
X=sp.Symbol('X')

def compress(face,residue):
    result={}
    for (degree,),coefficient in sp.Poly(face,PI).terms():
        if coefficient==0:continue
        assert degree%3==residue,(degree,residue)
        result[(degree-residue)//3]=coefficient
    return result

def add(*polys):
    out={}
    for poly in polys:
        for degree,value in poly.items():out[degree]=out.get(degree,0)+value
    return out

def mul(a,b):
    out={}
    for i,av in a.items():
        for j,bv in b.items():out[i+j]=out.get(i+j,0)+av*bv
    return out

def shift(a,n):return {i+n:v for i,v in a.items()}

def bilinear(a,b):
    """L(a,b)=a*b+3X*a*b'-2X*a'*b, exact coefficient convolution."""
    out={}
    for i,av in a.items():
        for j,bv in b.items():
            factor=1+3*j-2*i
            if factor:out[i+j]=out.get(i+j,0)+factor*av*bv
    return out

def coefficient_rows(H,A2,A3,B1,B2,jc=None,expand=True):
    h,a,b,c,d=(compress(face,residue) for face,residue in
               zip((H,A2,A3,B1,B2),(2,1,0,2,1)))
    assert max(h,default=-1)<=2
    assert max(a,default=-1)<=3 and max(b,default=-1)<=3
    assert max(c,default=-1)<=1 and max(d,default=-1)<=3
    h2=mul(h,h);h3=mul(h2,h)
    p0=shift(h3,2);q0=shift(h2,1)
    u=add(shift(mul(a,h),1),b)
    v=add(shift(mul(c,h),1),d)
    # L(p0,q0)=0 identically, since p0=X^2*h^3, q0=X*h^2.
    numerator=add(bilinear(p0,v),bilinear(u,q0),bilinear(u,v))
    numerator={k:sp.expand(value) if expand else value for k,value in numerator.items()}
    if jc is not None:numerator[0]=numerator.get(0,0)-3*jc
    numerator={k:v for k,v in numerator.items() if v!=0}
    assert max(numerator,default=-1)<=12
    rows=[(f'D1_J_face_Pi{3*k}',sp.expand(value/3) if expand else value/3)
          for k,value in sorted(numerator.items())]
    metadata={'coordinate_substitution':'X=Pi^3','P':'X^2*h(X)^3+X*a(X)*h(X)+b(X)',
       'Q':'Pi*(X*h(X)^2+X*c(X)*h(X)+d(X))',
       'J':'(p*q+3*X*p*q_prime-2*X*p_prime*q)/3',
       'coefficient_rule':'sum_(i+j=k) (1+3*j-2*i)*p_i*q_j / 3',
       'pure_power_bilinear_cancellation':'L(X^2*h^3,X*h^2)=0',
       'face_degrees':dict(zip(('H','A2','A3','B1','B2'),
          [sp.degree(face,PI) for face in (H,A2,A3,B1,B2)])),
       'source_unknowns_retained':True,'no_leading_coefficient_normalization':True,
       'coefficient_count':len(rows),'Pi_degrees':[3*k for k in sorted(numerator)]}
    return rows,metadata

def control():
    symbols={name:sp.symbols(f'{name}0:{degree+1}') for name,degree in
             [('h',2),('a',3),('b',3),('c',1),('d',3)]}
    compressed={name:sum(v*X**i for i,v in enumerate(values)) for name,values in symbols.items()}
    h,a,b,c,d=[compressed[n] for n in ('h','a','b','c','d')]
    p=X**2*h**3+X*a*h+b;q=X*h**2+X*c*h+d
    faces=[PI**r*compressed[n].subs(X,PI**3) for n,r in zip(('h','a','b','c','d'),(2,1,0,2,1))]
    jc=sp.Symbol('Jc');rows,meta=coefficient_rows(*faces,jc=jc)
    got=sum(v*PI**int(label.rsplit('Pi',1)[1]) for label,v in rows)
    P=faces[0]**3+faces[1]*faces[0]+faces[2]
    Q=faces[0]**2+faces[3]*faces[0]+faces[4]
    want=(3*P*sp.diff(Q,PI)-2*sp.diff(P,PI)*Q)/9-jc
    assert sp.expand(got-want)==0
    assert sp.expand((p*q+3*X*p*sp.diff(q,X)-2*X*sp.diff(p,X)*q)/3-jc-got.subs(PI,X**sp.Rational(1,3)))==0
    zero_rows,_=coefficient_rows(faces[0],0,0,0,0,jc=jc)
    assert zero_rows==[('D1_J_face_Pi0',-jc)]
    assert sp.expand(dict(rows)['D1_J_face_Pi0']-(symbols['b'][0]*symbols['d'][0]/3-jc))==0
    meta.update({'generic_direct_derivative_control':True,'all_17_face_parameters_free':True,
                 'pure_power_nonzero_J_negative_control':'-Jc',
                 'constant_coefficient':'b0*d0/3-Jc',
                 'row_terms':[len(sp.Add.make_args(v)) for _,v in rows],
                 'row_hash':hashlib.sha256('\n'.join(f'{label}\t{sp.srepr(v)}' for label,v in rows).encode()).hexdigest(),
                 'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    return meta

if __name__=='__main__':
    result=control()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,default=str,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,default=str,indent=2))
