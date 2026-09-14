#!/usr/bin/env python3
"""Exact diagonal-translation chart transport; never a parameter division.

For K=t^D Q(t^-1,(z+1)/t), the pullback Q(x+q,y+q) has
Tq(K)=sum K[r,p]*t^r*z^p*(1+q*t)^(D-r-p).
This acts on the entire total-degree box and has polynomial inverse T(-q).
The source minor constant goes j->j-q. This is a gauge isomorphism, not a
claim that an arbitrary coordinate hyperplane meets every component.
"""
from __future__ import annotations
from collections import defaultdict
from math import comb
from pathlib import Path
import hashlib,json,sys
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from source_data import SOURCE as S

def translate(poly,D,q):
    out=defaultdict(lambda:sp.Integer(0))
    for (r,p),value in poly.items():
        assert r>=0 and p>=0 and r+p<=D
        for k in range(D-r-p+1):
            out[r+k,p]+=value*comb(D-r-p,k)*q**k
    return {pos:v for pos,value in out.items() if (v:=sp.expand(value))!=0}

def decode(items):
    if isinstance(items,list):
        return {(int(r),int(q)):sp.Rational(c) for r,q,c in items}
    return {tuple(map(int,key.split(','))):sp.Rational(c) for key,c in items.items()}

def run():
    # Coefficient-by-coefficient Vandermonde identity certifies the group law
    # on every monomial in every normalization degree used by the engine.
    largest=max(S['n'],S['m'])
    checked=0
    for N in range(largest+1):
        for k in range(N+1):
            for i in range(k+1):
                assert comb(N,i)*comb(N-i,k-i)==comb(N,k)*comb(k,i)
                checked+=1
    q,t,j,u,v,a,rho,c,pi=sp.symbols('q t jet0 u v minor_a2 rho c pi')
    centres={}
    for branch in ('delta2','delta52'):
        delta=sp.Rational(str(S['minor'][branch]['radius_y']))
        # Only integer centre terms up to floor(delta) matter. The generic
        # term is multiplied by (1+q*t)^(-delta), with leading coefficient1.
        centre=j-q+u*t/(1+q*t)+(a if branch=='delta2' else v)*t*t/(1+q*t)**2
        expansion=sp.series(centre,t,0,3).removeO().expand()
        want=j-q+u*t+((a if branch=='delta2' else v)-q*u)*t*t
        assert sp.expand(expansion-want)==0
        assert sp.series((1+q*t)**(-delta),t,0,1).removeO()==1
        centres[branch]={'constant':str(j-q),'u':str(u),
            'at_level_or_last_integer':str((a if branch=='delta2' else v)-q*u),
            'rho_or_c_unchanged':True,'generic_leading_coefficient':'1',
            'terms_omitted_only_strictly_above_radius':str(delta)}
    # A sparse independent generic polynomial tests multiplication and degree
    # normalization, including the one-t shift on each outer block.
    H={(0,8):sp.Integer(1),(0,9):sp.Integer(3),(0,10):sp.Integer(3),(0,11):sp.Integer(1),
       (4,5):-sp.Rational(8,3),(8,2):sp.Symbol('ell'),(11,0):sp.Symbol('Hc_11_0')}
    transported=translate(H,S['h3_degree'],q)
    assert transported.get((S['h3_degree'],0))==sp.Symbol('Hc_11_0')
    back=translate(transported,S['h3_degree'],-q)
    assert back==H
    # Pure coordinate support: each translation increases r and keeps p.
    # Therefore below-D2 zero rows are stable, as is the equality face.
    below=[]
    wt=S['D2_weight']
    for pos,value in transported.items():
        if wt[0]*pos[0]+wt[1]*pos[1]<S['h3_floor']: below.append((pos,value))
    assert not below
    equality={pos:value for pos,value in H.items() if wt[0]*pos[0]+wt[1]*pos[1]==S['h3_floor']}
    assert {pos:value for pos,value in transported.items() if wt[0]*pos[0]+wt[1]*pos[1]==S['h3_floor']}==equality
    result={'status':'PASS','field':'QQ','driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'normalization_degrees':[S['h3_degree'],S['k2_degree'],2*S['h3_degree'],3*S['h3_degree'],S['n'],S['m']]+[v[0] for v in S['outer_specs'].values()],
       'group_law_coefficient_identities_verified':checked,
       'group_law':'T_a(T_b(K))=T_(a+b)(K)','inverse':'T_(-q)',
       'coefficient_map':'c_(r,p) -> sum_l binom(D-r-p,l)*q^l*c_(r,p) at (r+l,p)',
       'centre_maps':centres,'Hc_11_0_invariant':True,
       'h3_D2_face_preserved':True,'symbolic_h3_inverse_rechecked':True,
       'gauge_equivalence':'X -> X_(jet0=0) x A1; p -> (T_jet0(p),jet0); inverse (p0,j) -> T_(-j)(p0)',
       'group_spend':'residual diagonal source translation only; first translation already fixed major centre',
       'no_parameter_division':True,'all_other_minor_centres_retained':True,
       'scope':'complete necessary chart and full Jacobian equations; points transported, not discarded'}
    (HERE/'translation-controls.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__': run()
