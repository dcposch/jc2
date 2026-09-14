#!/usr/bin/env python3
"""Executable (99,66) source arithmetic; formulas, not a table of faces.

Source: frozen Moh (JRAM 340, 1983).  Printed p179 Def5.1(1),(3),(4)
(lines2120-2138 of moh-layout.txt); p170 Prop4.6(1), lines1632-1635;
p147 Prop1.2, lines373-390; p149 Thms1.1,1.2, lines478-507.
The complete-system hypotheses and Galois centre argument are supplied in
print-audit-derivations.md.  Branch radii and partitions are input branch data.
"""
from __future__ import annotations
from fractions import Fraction as Q
from functools import reduce
from math import gcd, lcm
import json
import sympy as sp


def derive_source() -> dict:
    n, m = 99, 66
    M = {1: -m, 2: 77, 3: 97}
    # Characteristic gcds, rather than a second independently typed degree list.
    d = {1: n}
    for j in range(1, len(M)+1):
        d[j+1] = gcd(d[j], abs(M[j]))
    V = {2: 8, 3: 8, 4: d[4]}
    last = len(M)
    radius_y = {}
    for i in range(1, last+1):
        numerator = Q(n-M[i])
        denominator = Q(n-M[last]-1)
        for j in range(i+1, last+1):
            numerator *= V[j]*(n-M[j])-d[j]
            denominator *= V[j]*(n-M[j-1])-d[j]
        radius_y[i] = 1 - numerator/denominator
    radius_z = {i: 1+r for i,r in radius_y.items()}
    h3_degree, k2_degree = d[3], d[2]
    h3_major = V[3]
    h3_minor = h3_degree-h3_major
    outer_power_F, outer_power_G = n//k2_degree, m//k2_degree
    inner_power = k2_degree//h3_degree
    g_D2_count = Q(n,d[3])*V[3]
    g_D1_count = Q(n,d[2])*V[2]
    g_order_D2 = g_D2_count*radius_y[2]+(n-g_D2_count)*radius_y[3]
    g_order_D1 = (g_D1_count*radius_y[1]
                 +(g_D2_count-g_D1_count)*radius_y[2]
                 +(n-g_D2_count)*radius_y[3])
    k2_order_D2 = g_order_D2/outer_power_F
    h3_order_D2 = k2_order_D2/inner_power
    k2_order_D1 = g_order_D1/outer_power_F
    cover_D2 = radius_z[2].denominator
    weight_D2 = (cover_D2, int(cover_D2*radius_z[2]))
    h3_floor = int(cover_D2*(h3_degree+h3_order_D2))
    k2_floor = int(cover_D2*(k2_degree+k2_order_D2))
    cover_D1 = lcm(radius_z[1].denominator,radius_z[2].denominator)
    D1_substitution = (cover_D1,int(cover_D1*radius_z[2]),int(cover_D1*radius_z[1]))
    k2_D1_floor = int(cover_D1*(k2_degree+k2_order_D1))
    outer = {}
    for name,j in (("A2",2),("A3",outer_power_F),("B1",1),("B2",outer_power_G)):
        degree=j*k2_degree-1
        outer[name] = (degree,int(cover_D2*(degree+j*k2_order_D2)),
                       int(cover_D1*(degree+j*k2_order_D1)))
    pi, alpha, beta, ell = sp.symbols("pi alpha beta ell")
    orbit = sp.resultant(alpha**cover_D2-beta, pi-alpha, alpha)
    child_multiplicity = int(g_D1_count/outer_power_F)
    k2_face = sp.expand(orbit**child_multiplicity)
    k2_equality = {}
    for (q,),coefficient in sp.Poly(k2_face,pi).terms():
        r=Q(k2_floor-weight_D2[1]*q,weight_D2[0])
        assert r.denominator==1 and r>=0 and int(r)+q<=k2_degree
        k2_equality[(int(r),q)] = coefficient
    h3_equality_slots = [(r,q) for r in range(1,h3_degree+1)
                         for q in range(h3_degree-r+1)
                         if weight_D2[0]*r+weight_D2[1]*q==h3_floor]
    h3_equality_slots.sort()
    unknowns=sp.symbols(' '.join(f"eq_{r}_{q}" for r,q in h3_equality_slots),seq=True)
    h3_face_raw=pi**h3_major+sum(c*pi**q for c,(_,q) in zip(unknowns,h3_equality_slots))
    # C2 floor 2*ord(h3); its y-degree is <deg(h3).  At equality
    # max pi degree is determined by the lattice, so coefficients above
    # maxdeg(UH,V) are forced solely by H^3.
    C2_degree=2*h3_degree
    C3_degree=3*h3_degree
    C2_floor=int(cover_D2*(C2_degree+2*h3_order_D2))
    C3_floor=int(cover_D2*(C3_degree+3*h3_order_D2))
    Uslots=[(r,q) for r in range(1,C2_degree+1) for q in range(min(h3_degree-1,C2_degree-r)+1)
            if weight_D2[0]*r+weight_D2[1]*q==C2_floor]
    Vslots=[(r,q) for r in range(1,C3_degree+1) for q in range(min(h3_degree-1,C3_degree-r)+1)
            if weight_D2[0]*r+weight_D2[1]*q==C3_floor]
    uh_degree=max(q for r,q in Uslots)+h3_major
    v_degree=max(q for r,q in Vslots)
    residual=sp.Poly(sp.expand(k2_face-h3_face_raw**inner_power),pi)
    forced_rows=[residual.coeff_monomial(pi**q) for q in range(max(uh_degree,v_degree)+1,residual.degree()+1)
                 if residual.coeff_monomial(pi**q)!=0]
    forced=sp.solve(forced_rows,unknowns,dict=True)
    assert len(forced)==1
    h3_face=sp.expand(h3_face_raw.subs(forced[0]))
    remaining=sorted(h3_face.free_symbols-{pi,beta},key=str)
    assert len(remaining)==1
    h3_face=h3_face.subs(remaining[0],ell)
    h3_equality={slot:sp.expand(h3_face).coeff(pi,slot[1]) for slot in h3_equality_slots}
    h3_top={(0,h3_major+j):sp.binomial(h3_minor,j) for j in range(h3_minor+1)}
    minor={}
    rho, c = sp.symbols('rho c')
    for branch,radius,partition in (("delta2",Q(2),(2,1)),("delta52",Q(5,2),(1,1,1))):
        cover=radius.denominator
        h3_order=h3_minor*radius+h3_major*radius_y[3]
        F_order=Q(n,h3_degree)*h3_order
        G_order=Q(m,h3_degree)*h3_order
        if branch=='delta2':
            # At-level centre a2 is the double root; rho is the other
            # root's separation divided by total minor multiplicity.
            root_positions=(sp.Integer(0),-h3_minor*rho)
            face=sp.prod((pi-root)**mult for root,mult in zip(root_positions,partition))
        else:
            # Deck involution of the first denominator-two splitting
            # fixes one residue and exchanges the other two.
            face=pi*sp.resultant(alpha**cover-c,pi-alpha,alpha)
        minor[branch]={
            'h3_face':sp.expand(face),'F_face':sp.expand(face**(n//h3_degree)),
            'G_face':sp.expand(face**(m//h3_degree)),
            'radius_y':radius,'radius_z':1+radius,'cover':cover,'partition':partition,
            'h3_order':h3_order,'F_order':F_order,'G_order':G_order,
            'h3_local_floor':int(cover*(h3_degree+h3_order)),
            'F_local_floor':int(cover*(n+F_order)),
            'G_local_floor':int(cover*(m+G_order)),
            'F_pole':int(-cover*F_order),'G_pole':int(-cover*G_order),
            'strict_zero_rule':'n < local_floor; equality is the nonzero face',
        }
    return {
      'n':n,'m':m,'M':M,'d':d,'V':V,'radius_y':radius_y,'radius_z':radius_z,
      'h3_degree':h3_degree,'k2_degree':k2_degree,'h3_major':h3_major,'h3_minor':h3_minor,
      'inner_power':inner_power,'outer_power_F':outer_power_F,'outer_power_G':outer_power_G,
      'g_D2_count':g_D2_count,'g_D1_count':g_D1_count,
      'g_order_D2':g_order_D2,'g_order_D1':g_order_D1,
      'k2_order_D2':k2_order_D2,'h3_order_D2':h3_order_D2,'k2_order_D1':k2_order_D1,
      'D2_weight':weight_D2,'h3_floor':h3_floor,'k2_floor':k2_floor,
      'D1_substitution':D1_substitution,'k2_D1_floor':k2_D1_floor,
      'outer_specs':outer,'outer_qcap':k2_degree-1,
      'C2_floor':C2_floor,'C3_floor':C3_floor,'Uslots':Uslots,'Vslots':Vslots,
      'inner_normalization_degrees':{'C2':C2_degree,'C3':C3_degree},
      'inner_total_degrees':{'C2':C2_degree-1,'C3':C3_degree-1},
      'inner_qcap':h3_degree-1,
      'orbit_polynomial':orbit,'k2_face':k2_face,'k2_equality':k2_equality,
      'h3_equality_slots':h3_equality_slots,'h3_face':h3_face,'h3_equality':h3_equality,
      'h3_top':h3_top,'minor':minor,
      'source':{'radii':'Moh p179 Def5.1(3), moh-layout.txt:2131-2138',
                'multiplicities':'Moh p179 Def5.1(1), moh-layout.txt:2120-2124',
                'conjugate_face':'Moh p170 Prop4.6(1), moh-layout.txt:1632-1635; p149 Thm1.1:478-483',
                'remainder_floors':'Moh p149 Thm1.2, moh-layout.txt:495-507',
                'minor_distribution':'Moh p191 Prop6.1(2), moh-layout.txt:2754-2762'}}

SOURCE=derive_source()


def jsonable(value):
    if isinstance(value,dict): return {str(k):jsonable(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)): return [jsonable(v) for v in value]
    if isinstance(value,(Q,sp.Basic)): return str(value)
    return value

if __name__=='__main__':
    print(json.dumps(jsonable(SOURCE),indent=2,sort_keys=True))
