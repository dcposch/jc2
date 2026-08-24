#!/usr/bin/env python3
"""Exact adaptive b2 probe over the six-point TD6 residue field."""

from fractions import Fraction as Q
from hashlib import sha256
import importlib.util
from pathlib import Path


HERE = Path(__file__).resolve().parent


def load(name, path, expected):
    assert sha256(path.read_bytes()).hexdigest() == expected
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


base = load("q2_base", HERE / "replay.py", "0ba184470dc051fad50640647c4b78ea869b8a4153219026b23abdcf0652d357")
uniform = load(
    "uniform_third",
    HERE.parent / "td6_moduli_uniform_third_band_20260824" / "replay.py",
    "7a21f9495d1e8784a9b253253430846ce882e2ce26f91815b31b6e061022cba8",
)
nr, fb, E, K = base.nr, base.fb, uniform.E, uniform.K
S, D, L, A = E(uniform.S_FIELD), E(uniform.D_FIELD), E(uniform.L_FIELD), uniform.A_FIELD

RHO_ZERO = E([
    K([
        Q(2495634,3625), Q(-4154976,3625), Q(4405068,3625),
        Q(-2488119,3625), Q(761922,3625), Q(-105084,3625),
    ]),
    K(Q(136875,29)),
])
DELTA = E(Q(14012,145))
B = RHO_ZERO / DELTA
Q_PRIME = {0:E(1), 1:2*B, 24:E(25)}


def multiply(left,right):
    out=[E(0)]*(len(left)+len(right)-1)
    for i,a in enumerate(left):
        for j,b in enumerate(right): out[i+j]+=a*b
    return out


def power(poly,n):
    out=[E(1)]
    for _ in range(n): out=multiply(out,poly)
    return out


R=multiply(multiply([E(-1),E(1)],[E(-1),E(1)]),[D,-S,E(1)])
R3,R5=power(R,3),power(R,5)
POLE_F={1:-(L**3)*A,6:L**3}
POLE_G={0:Q(5,9)*L**5*A**2,5:-Q(5,3)*L**5*A,10:L**5}


def source_rhs(key):
    owner,chart,exponent,degree=key
    if chart=="X" and exponent==0:
        if owner=="f": return E(1 if degree==15 else 0)
        return {1:E(1),2:B,25:E(1)}.get(degree,E(0))
    if chart=="F1" and exponent==(-15 if owner=="f" else -25):
        pattern=R3 if owner=="f" else R5
        return pattern[degree//5] if degree%5==0 and degree//5<len(pattern) else E(0)
    if chart=="F0" and exponent==(-3 if owner=="f" else -5):
        return (POLE_F if owner=="f" else POLE_G).get(degree,E(0))
    return E(0)


def build_transport_rows():
    nf,rf=fb.build_transport(15,60,3,{15:Q(1)},fb.F1_F_PATTERN,fb.POLE_F_PATTERN)
    ng,rg=fb.build_transport(25,100,5,{1:Q(1),25:Q(1)},fb.F1_G_PATTERN,fb.POLE_G_PATTERN)
    rows=[(('f',)+key,row,rhs) for key,row,rhs in rf]
    rows += [(('g',)+key,{nf+v:c for v,c in row.items()},rhs) for key,row,rhs in rg]
    return nf,ng,rows


def propagate(records):
    pivot_rhs={};compat=[]
    for key,kind,pivot,lead,factors in records:
        value=source_rhs(key)
        for old,factor in factors:value-=factor*pivot_rhs[old]
        if kind=="pivot":pivot_rhs[pivot]=value/lead
        elif value:compat.append((key,value))
    return pivot_rhs,compat


def rational_direction_parameterization(nvars,pivots,pivot_rhs):
    free=[v for v in range(nvars) if v not in pivots]; pof={v:k for k,v in enumerate(free)}
    forms=[None]*nvars
    for v in range(nvars-1,-1,-1):
        if v in pof:
            forms[v]=(E(0),{pof[v]:Q(1)});continue
        form=(pivot_rhs[v],{})
        for other,c in pivots[v].items():
            if other!=v:form=nr.add_affine(form,forms[other],-c)
        forms[v]=form
    return forms,free


def affine_polys_first(f1,g1):
    rows=[]
    for degree in range(40):
        eq={}
        for i,form in enumerate(f1):
            multiplier=Q_PRIME.get(degree-i,E(0))
            if multiplier:eq=nr.add_polynomial(eq,nr.affine_polynomial(form),multiplier)
        j=degree-14
        if 0<=j<len(g1):eq=nr.add_polynomial(eq,nr.affine_polynomial(g1[j]),E(-15))
        rows.append(eq)
    return rows


def pack(family,polys):
    out=[]
    for degree,poly in enumerate(polys):
        row={};constant=poly.get((),E(0))
        for monomial,c in poly.items():
            if monomial:
                assert len(monomial)==1;row[monomial[0]]=c
        if row or constant:out.append(((family,degree),row,-constant))
    return out


def affine_parameterization(nvars,equations):
    solution,pivots,error=fb.exact_solve(nvars,equations,allow_inconsistent=True)
    if error:return None,None,pivots,error
    free=[v for v in range(nvars) if v not in pivots];pof={v:k for k,v in enumerate(free)}
    forms=[None]*nvars
    for v in range(nvars-1,-1,-1):
        if v in pof:forms[v]=(E(0),{pof[v]:E(1)});continue
        row,rhs=pivots[v];form=(rhs,{})
        for other,c in row.items():
            if other!=v:form=nr.add_affine(form,forms[other],-c)
        forms[v]=form
    return forms,free,pivots,None


def compose(forms,pforms):
    out=[]
    for constant,coefficients in forms:
        value=(constant,{})
        for p,c in coefficients.items():value=nr.add_affine(value,pforms[p],c)
        out.append(value)
    return out


def compile_previous(f1,f2,g1,g2):
    old=base.Q_PRIME;base.Q_PRIME=Q_PRIME
    try:return base.compile_x_previous(f1,f2,g1,g2)
    finally:base.Q_PRIME=old


def compile_current(f1,f2,f3,g1,g2,g3):
    old=base.Q_PRIME;base.Q_PRIME=Q_PRIME
    try:return base.compile_x_current(f1,f2,f3,g1,g2,g3)
    finally:base.Q_PRIME=old


def compile_pole_previous(p1,q1):
    p=[(E(0),{}) for _ in range(7)];q=[(E(0),{}) for _ in range(11)]
    for d,c in POLE_F.items():p[d]=(c,{})
    for d,c in POLE_G.items():q[d]=(c,{})
    rows=[]
    for degree in range(14):
        eq={}
        for i,left in enumerate(p):
            j=degree-i+1
            if 1<=j<len(q1):eq=nr.add_polynomial(eq,nr.multiply_affine(left,nr.scale_affine(q1[j],E(j))),E(-3))
        for i,left in enumerate(p1):
            j=degree-i+1
            if 1<=j<len(q):eq=nr.add_polynomial(eq,nr.multiply_affine(left,nr.scale_affine(q[j],E(j))),E(-2))
        for i in range(1,len(p)):
            j=degree-(i-1)
            if 0<=j<len(q1):eq=nr.add_polynomial(eq,nr.multiply_affine(nr.scale_affine(p[i],E(i)),q1[j]),E(4))
        for i in range(1,len(p1)):
            j=degree-(i-1)
            if 0<=j<len(q):eq=nr.add_polynomial(eq,nr.multiply_affine(nr.scale_affine(p1[i],E(i)),q[j]),E(5))
        rows.append(nr.scale_polynomial(eq,E(Q(-1,25))))
    return rows


def main():
    fb.CENTER=(Q(1),Q(1),Q(1));fb._X_POWER_CACHE.clear()
    nf,ng,transport=build_transport_rows();tpiv,records=uniform.mu.factor_matrix(transport)
    trhs,compat=propagate(records);assert not compat
    forms134,free134=rational_direction_parameterization(nf+ng,tpiv,trhs)
    assert (len(tpiv),len(free134))==(3470,132)
    f1=nr.x_band_forms(15,60,1,forms134,0);g1=nr.x_band_forms(25,100,1,forms134,nf)
    forms94,free94,jpiv,jerr=affine_parameterization(len(free134),pack("X-2",affine_polys_first(f1,g1)))
    assert jerr is None and (len(jpiv),len(free94))==(38,94)
    global94=compose(forms134,forms94)
    f1=nr.x_band_forms(15,60,1,global94,0);f2=nr.x_band_forms(15,60,2,global94,0)
    g1=nr.x_band_forms(25,100,1,global94,nf);g2=nr.x_band_forms(25,100,2,global94,nf)
    previous=compile_previous(f1,f2,g1,g2)
    p1=[nr.combine_global_linear(nr.pole_coefficient(15,60,-2,d),global94,0) for d in range(61)]
    q1=[nr.combine_global_linear(nr.pole_coefficient(25,100,-4,d),global94,nf) for d in range(101)]
    pole=compile_pole_previous(p1,q1)
    forms56,free56,ppiv,perr=affine_parameterization(len(free94),pack("X-1",previous)+pack("P1",pole))
    assert perr is None and (len(ppiv),len(free56))==(38,56)
    global56=compose(global94,forms56)
    bands=[nr.x_band_forms(15,60,e,global56,0) for e in (1,2,3)]
    gbands=[nr.x_band_forms(25,100,e,global56,nf) for e in (1,2,3)]
    current=compile_current(*bands,*gbands)
    sol,cpiv,cerr=fb.exact_solve(len(free56),pack("X0",current),allow_inconsistent=True)
    tangent=nr.exact_rank(nr.tangent_rows(current),len(free56))
    assert sol is None and cerr is not None and cerr[0]==("X0",4)
    assert tangent==25
    residual=cerr[1]
    # The exact residue has nonzero coefficients in each of the independent
    # E/K basis slots 1,A,A^2, so it is certainly nonzero.
    assert all(residual.coefficients)
    b_sha=sha256(repr(B).encode()).hexdigest()
    residual_sha=sha256(repr(residual).encode()).hexdigest()
    print("TD6-BOUNDARY-Q2-ADAPTIVE: PASS")
    print("verdict = ADAPTIVE-B2-CANDIDATE-EMPTY")
    print("boundary = p=t^15; q=t+B*t^2+t^25")
    print("candidate = B=RHO_0/(14012/145) in exact degree-18 source field")
    print("transport = rank 3470 / 3602; dimension 132")
    print("first_J_band = rank 38 / 132; dimension 94")
    print("previous_paired_bands = rank 38 / 94; dimension 56")
    print("current_centered_band = tangent_rank 25 / 56; EMPTY at t^4")
    print("residual_basis_support = 1,A,A^2 (all nonzero)")
    print(f"candidate_B.sha256 = {b_sha}")
    print(f"residual.sha256 = {residual_sha}")
    print("full_b2_family_killed = false")
    print("SP2_killed = false")
    print("JC2_resolved = false")


if __name__=="__main__":main()
