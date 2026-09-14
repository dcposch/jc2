#!/usr/bin/env python3
"""The printed r=1 differential face, derived by the D1 coordinate map.

This is a nonvanishing extension of the support/positive-J chart. Neither
F's nor G's D1 face is prescribed: both are computed from all coefficients.
Source: Def5.1(4), p179; Prop4.6 r=1, p170, moh-layout.txt:1648-1651.
"""
from __future__ import annotations
from math import comb
from pathlib import Path
import hashlib,json,sys
import sympy as sp
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import engine as E
from source_data import SOURCE as S
PI=sp.Symbol('Pi')

def extract_face(poly,threshold):
    cover,base,child=S['D1_substitution']
    step=child-base
    out=sp.Integer(0)
    for (r,q),value in poly.items():
        numerator=threshold-cover*r-base*q
        if numerator%step: continue
        k=numerator//step
        if 0<=k<=q: out+=value*comb(q,k)*PI**k
    return sp.expand(out)

def d1_face_jacobian(h,C2,C3,outer):
    """Inputs are actual currently reduced normalized coefficient polynomials."""
    cover=S['D1_substitution'][0]
    ratio=cover//S['D2_weight'][0]
    cutoff=S['k2_D1_floor']//ratio
    low=E.tz_add(E.mul_weight(E.mul_weight(h,h,cutoff),h,cutoff),
                 E.mul_weight(C2,h,cutoff),
                 {p:v for p,v in C3.items() if E.weight(p)<=cutoff})
    H=extract_face(low,S['k2_D1_floor'])
    faces={name:extract_face(poly,S['outer_specs'][name][2]) for name,poly in outer.items()}
    P=sp.expand(H**S['outer_power_F']+faces['A2']*H+faces['A3'])
    Q=sp.expand(H**S['outer_power_G']+faces['B1']*H+faces['B2'])
    F_exp=sp.Rational(str(S['g_order_D1']))*cover
    G_exp=F_exp*sp.Rational(S['m'],S['n'])
    # x=e^-cover, y=e^-cover+e^3+Pi*e^4. Only the generic
    # derivative y_Pi=e^4 enters the Jacobian coordinate determinant.
    y_generic_exp=S['D1_substitution'][2]-cover
    resulting_exp=F_exp+G_exp+cover-y_generic_exp
    assert resulting_exp==0
    face=sp.expand((-F_exp*P*sp.diff(Q,PI)+G_exp*sp.diff(P,PI)*Q)/cover)
    metadata={'source':'Moh p179 Def5.1(4), p170 Prop4.6 r=1; M:1648-1651',
        'computed_H2_face':str(H),'computed_outer_faces':{n:str(v) for n,v in faces.items()},
        'computed_F_face':str(P),'computed_G_face':str(Q),
        'physical_F_e_order':str(F_exp),'physical_G_e_order':str(G_exp),
        'coordinate_determinant':f'-{cover}*e^({-cover-1+y_generic_exp})',
        'resulting_J_e_order':str(resulting_exp),'computed_J_face':str(face),
        'Pi_symbol':str(PI),'no_face_coefficient_was_pinned':True,
        'nonzero_scalar':'Jc, with its own Rabinowitsch inverse; no torus normalization'}
    return face,metadata

def control():
    e,p,a,b,c=sp.symbols('e Pi a b c')
    cover=S['D1_substitution'][0]
    center_exp=S['D1_substitution'][1]-cover
    generic_exp=S['D1_substitution'][2]-cover
    x=e**(-cover);y=e**(-cover)+e**center_exp+p*e**generic_exp
    P=p**3+a*p+b;Q=p**2+c
    F=e**(-3)*P;G=e**(-2)*Q
    actual=sp.cancel((sp.diff(F,e)*sp.diff(G,p)-sp.diff(F,p)*sp.diff(G,e))/(sp.diff(x,e)*sp.diff(y,p)-sp.diff(x,p)*sp.diff(y,e)))
    target=sp.expand((3*P*sp.diff(Q,p)-2*sp.diff(P,p)*Q)/cover)
    assert sp.expand(actual-target)==0
    H=sp.Function('H')(p)
    assert sp.simplify(3*H**3*sp.diff(H**2,p)-2*sp.diff(H**3,p)*H**2)==0
    result={'status':'PASS','physical_coordinate_chain_rule_rechecked':True,
       'Jacobian_face_formula':'(3*P*Qprime-2*Pprime*Q)/9',
       'pure_power_faces_give_zero':True,'generic_test_expression':str(actual),
       'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'d1-jacobian-face-control.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':control()
