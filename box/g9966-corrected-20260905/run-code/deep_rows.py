#!/usr/bin/env python3
"""Exact sparse row helpers for deep continuation of the derived chart.

No chart restriction is made here.  The Jacobian formula is the product rule
applied to F=H^3+A*H+B and G=H^2+C*H+D before coefficient expansion.  Keeping
the cancelling pure powers out of the multiplication saves substantial work.
Degrees are normalization degrees, not claims that a lower block attains its
bound: H=33,A=66,B=99,C=33,D=66, including each outer block's extra t factor.
"""
from __future__ import annotations

from collections import defaultdict
from math import comb
import sympy as sp
from source_data import SOURCE


def plus(*polys):
    terms=defaultdict(list)
    for poly in polys:
        for key,value in poly.items():
            if value!=0:
                terms[key].append(value)
    return {key:sp.Add(*values) for key,values in terms.items() if sp.Add(*values)!=0}


def scale(poly,value):
    return {key:value*coefficient for key,coefficient in poly.items() if value*coefficient!=0}


def times(left,right,cutoff):
    terms=defaultdict(list)
    for (r,q),a in left.items():
        for (s,k),b in right.items():
            if r+s<=cutoff:
                terms[r+s,q+k].append(a*b)
    return {key:sp.Add(*values) for key,values in terms.items() if sp.Add(*values)!=0}


def bracket(left,right,left_degree,right_degree,cutoff):
    """Normalized [P,Q] directly by monomial pair, with exact integer factors."""
    terms=defaultdict(list)
    for (r,q),a in left.items():
        for (s,k),b in right.items():
            coefficient=(left_degree-r)*k-(right_degree-s)*q
            if r+s<=cutoff and coefficient:
                assert q+k>=1
                terms[r+s,q+k-1].append(coefficient*a*b)
    return {key:sp.Add(*values) for key,values in terms.items() if sp.Add(*values)!=0}


def jacobian_factored(k2,outer,cutoff,expand=True):
    """Return all (t,z) Jacobian coefficients through cutoff.

outer uses the engine's unshifted block coordinates.  Every block is shifted
by t exactly once here, as in build_FG.  No leading coefficient is divided.
"""
    effective={name:{(r+1,q):value for (r,q),value in poly.items()
                     if r+1<=cutoff and value!=0} for name,poly in outer.items()}
    H=k2
    A,B,C,D=(effective[name] for name in ("A2","A3","B1","B2"))
    degree=SOURCE["k2_degree"]
    degree_A=SOURCE["n"]-degree
    degree_B=SOURCE["n"]
    degree_C=SOURCE["m"]-degree
    degree_D=SOURCE["m"]
    Fpower=SOURCE["outer_power_F"]
    Gpower=SOURCE["outer_power_G"]
    powers=[{(0,0):sp.Integer(1)},H]
    for _ in range(2,max(Fpower,Gpower)):
        powers.append(times(powers[-1],H,cutoff))
    H2=times(H,H,cutoff)
    left=times(plus(scale(powers[Fpower-1],Fpower),A),
               plus(times(H,bracket(H,C,degree,degree_C,cutoff),cutoff),bracket(H,D,degree,degree_D,cutoff)),cutoff)
    right=times(plus(scale(powers[Gpower-1],Gpower),C),
                plus(times(H,bracket(H,A,degree,degree_A,cutoff),cutoff),bracket(H,B,degree,degree_B,cutoff)),cutoff)
    jac=plus(left,scale(right,-1),
             times(H2,bracket(A,C,degree_A,degree_C,cutoff),cutoff),
             times(H,bracket(A,D,degree_A,degree_D,cutoff),cutoff),
             times(H,bracket(B,C,degree_B,degree_C,cutoff),cutoff),
             bracket(B,D,degree_B,degree_D,cutoff))
    if expand:
        jac={key:sp.expand(value) for key,value in jac.items()}
    return {key:value for key,value in jac.items() if value!=0}


def all_w_bands(poly,cutoff,expand=True):
    terms=defaultdict(list)
    for (r,q),coefficient in poly.items():
        if r<=cutoff:
            for k in range(q+1):
                terms[r,k].append(coefficient*comb(q,k)*(-1)**(q-k))
    result={r:{} for r in range(cutoff+1)}
    for (r,k),values in terms.items():
        coefficient=sp.Add(*values)
        if expand:
            coefficient=sp.expand(coefficient)
        if coefficient!=0:
            result[r][k]=coefficient
    return result


def local_FG(engine,k2,outer,branch,cutoff):
    """Compose the small blocks before products, retaining every local term.

Polynomial substitution is a ring homomorphism, so this emits exactly the
same rows as local_rows(build_FG(...)), with much less intermediate expansion.
The caller may substitute only a previously certified surviving locus.
"""
    H=engine.local_rows(k2,branch,cutoff)
    effective={name:{(r+1,q):value for (r,q),value in poly.items() if value!=0}
               for name,poly in outer.items()}
    local={name:engine.local_rows(poly,branch,cutoff) for name,poly in effective.items()}
    Fpower=SOURCE["outer_power_F"]
    Gpower=SOURCE["outer_power_G"]
    powers=[{(0,0):sp.Integer(1)},H]
    for _ in range(2,max(Fpower,Gpower)+1):
        powers.append(times(powers[-1],H,cutoff))
    F=plus(powers[Fpower],times(local["A2"],H,cutoff),local["A3"])
    G=plus(powers[Gpower],times(local["B1"],H,cutoff),local["B2"])
    result=[]
    for poly in (F,G):
        expanded={key:sp.expand(value) for key,value in poly.items()}
        result.append({key:value for key,value in expanded.items() if value!=0})
    return tuple(result)


def point_controls(rows,free,localizer,linear_map=None):
    """Gate point and a rational trial after reversible linear elimination.

The gate point is never silently replaced by the resolved-point candidate.
Both are returned separately and tested against the raw emitted rows.
"""
    base=dict.fromkeys(free,sp.Integer(0))
    base[sp.Symbol("jet0")]=base[sp.Symbol(localizer)]=sp.Integer(1)
    def failures(point):
        bad=[]
        for label,row in rows:
            value=sp.expand(sp.sympify(row).xreplace(point))
            if value!=0:
                bad.append((label,str(value)))
        return bad
    original=failures(base)
    candidate=dict(base)
    for variable,rhs in (linear_map or {}).items():
        value=sp.expand(rhs.xreplace(candidate))
        if value.free_symbols:
            raise AssertionError("linear map must already be fully resolved")
        candidate[variable]=value
    rational=failures(candidate)
    return {"gate_point_satisfies_raw_rows":not original,
            "gate_point_failures":original[:12],"gate_point_failure_count":len(original),
            "resolved_rational_candidate_satisfies_raw_rows":not rational,
            "resolved_rational_candidate_failures":rational[:12],
            "resolved_rational_candidate_nonzero":{str(v):str(value) for v,value in candidate.items() if value!=0}}


def pure_power_radical_rows(residual):
    """Add only sound set-equivalent roots of rows a*f^n, a in Q*, n>1.

A product of distinct factors never licenses choosing one component.  The
returned rows can be adjoined because each has a certified power in the ideal.
No radical equality for an arbitrary residual ideal is claimed.
"""
    rows=[]
    certificates=[]
    for label,row in residual:
        constant,factors=sp.factor_list(row)
        if constant.is_Rational and constant!=0 and len(factors)==1 and factors[0][1]>1:
            factor,power=factors[0]
            assert sp.expand(row-constant*factor**power)==0
            root_label=f"radical_of_{label}"
            rows.append((root_label,factor))
            certificates.append({"source_row":label,"new_row":root_label,
                                 "factor":str(factor),"power":int(power),"rational_unit":str(constant),
                                 "identity_verified":True})
    return rows,certificates
