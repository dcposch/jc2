#!/usr/bin/env python3
"""Jet0=0 gauge computation; full-chart promotion requires the root's T_q audit.

All other centres remain free, including the delta2 at-level minor_a2, and
Hc_11_0 remains in the source ring unless an actual row later solves it.  The
generic source state is derived first, then specialized by the explicit ring
map jet0->0. The minor emitter uses that same map before any expansion.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys

import sympy as sp

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import engine as E
import minor_maps as MM
import deep_driver as DRIVER
from deep_accelerated import accelerate
from source_data import SOURCE as S,jsonable

JET0=sp.Symbol('jet0')
GAUGE={JET0:sp.Integer(0)}
ORIGINAL_INNER=E.inner_state
ORIGINAL_BRANCH_DATA=MM.branch_data
DERIVING_GENERIC=False
OWN_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def polynomial_jet(poly,degree):
    """Actual value,x derivative,y derivative at (0,0), from normalized slots."""
    assert all(r+q<=degree for r,q in poly)
    return (poly.get((degree,0),sp.Integer(0)),
            poly.get((degree-1,0),sp.Integer(0))-poly.get((degree-1,1),sp.Integer(0)),
            poly.get((degree-1,1),sp.Integer(0)))


def jet_add(*jets):
    return tuple(sum(j[i] for j in jets) for i in range(3))


def jet_mul(a,b):
    return (a[0]*b[0],a[1]*b[0]+a[0]*b[1],a[2]*b[0]+a[0]*b[2])


def jet_power(a,n):
    value=(sp.Integer(1),sp.Integer(0),sp.Integer(0))
    for _ in range(n):
        value=jet_mul(value,a)
    return value


def corner_from_blocks(h,C2,C3,outer):
    hjet=polynomial_jet(h,S['h3_degree'])
    c2jet=polynomial_jet(C2,2*S['h3_degree'])
    c3jet=polynomial_jet(C3,S['inner_power']*S['h3_degree'])
    H=jet_add(jet_power(hjet,S['inner_power']),jet_mul(c2jet,hjet),c3jet)
    A,B,C,D=(polynomial_jet(outer[name],S['outer_specs'][name][0])
             for name in ('A2','A3','B1','B2'))
    bracket=lambda a,b:a[1]*b[2]-a[2]*b[1]
    fp,gp=S['outer_power_F'],S['outer_power_G']
    value=((fp*H[0]**(fp-1)+A[0])*(H[0]*bracket(H,C)+bracket(H,D))
           -(gp*H[0]**(gp-1)+C[0])*(H[0]*bracket(H,A)+bracket(H,B))
           +H[0]**2*bracket(A,C)+H[0]*bracket(A,D)+H[0]*bracket(B,C)+bracket(B,D))
    return sp.expand(value),{'H2':H,'A2':A,'A3':B,'B1':C,'B2':D}


def corner_control():
    """Compare with independent differentiation in actual x,y coordinates."""
    from math import comb
    x,y,a,b,c,d,e,f=sp.symbols('x y a b c d e f')
    def normalized(poly,degree):
        out={}
        for (i,j),coefficient in sp.Poly(poly,x,y).terms():
            r=degree-i-j
            for q in range(j+1):
                out[r,q]=out.get((r,q),0)+coefficient*comb(j,q)
        return out
    hp=a+x+2*y
    c2p=b+x*y
    c3p=c+3*x-y
    ops={'A2':d+x,'A3':e+2*y,'B1':f-y,'B2':x+4*y}
    got,_=corner_from_blocks(normalized(hp,S['h3_degree']),
        normalized(c2p,2*S['h3_degree']),normalized(c3p,S['inner_power']*S['h3_degree']),
        {name:normalized(poly,S['outer_specs'][name][0]) for name,poly in ops.items()})
    H=hp**S['inner_power']+c2p*hp+c3p
    F=H**S['outer_power_F']+ops['A2']*H+ops['A3']
    G=H**S['outer_power_G']+ops['B1']*H+ops['B2']
    want=(sp.diff(F,x)*sp.diff(G,y)-sp.diff(F,y)*sp.diff(G,x)).subs({x:0,y:0})
    assert sp.expand(got-want)==0
    return {'status':'PASS','exact_actual_xy_differentiation_match':True,
            'zero_outer_implies_zero':corner_from_blocks(
                normalized(hp,S['h3_degree']),normalized(c2p,2*S['h3_degree']),
                normalized(c3p,S['inner_power']*S['h3_degree']),{name:{} for name in ops})[0]==0,
            'expression_sha256':hashlib.sha256(sp.srepr(got).encode()).hexdigest()}


def gauge_accelerate(context):
    result=accelerate(context)
    if result.get('unit_ideal'):
        return result
    free,mapping,residual,_allraw=context['state']()
    current=lambda poly:DRIVER.apply_poly(poly,mapping)
    from d1_jacobian_face import d1_face_jacobian
    face,face_meta=d1_face_jacobian(current(context['h']),current(context['C2']),
        current(context['C3']),{name:current(poly) for name,poly in context['outer'].items()})
    jc,zj=sp.symbols('Jc ZJ')
    free.update({jc,zj})
    Pi=sp.Symbol('Pi')
    facepoly=sp.Poly(sp.expand(face-jc),Pi)
    facerows=[(f'gauge_D1_J_face_Pi{k[0]}',value) for k,value in facepoly.terms() if value!=0]
    facerows.append(('gauge_J_nonzero_wrapper',zj*jc-1))
    context['reduce_new'](facerows,'gauge_D1_J_face')
    free,mapping,residual,allraw=context['state']()
    facesing=E.singular_dimension(residual,context['branch'],context['output'].with_name(context['output'].stem+'_D1_J.sing'))
    facepoint,facepointmeta=context['rational_candidate'](residual,free,mapping,context['branch'])
    if facepoint is not None:
        assert all(sp.expand(sp.sympify(row).xreplace(facepoint))==0 for _,row in allraw)
        facepointmeta.update({'all_accumulated_raw_rows_verified':len(allraw),'raw_images_all_zero':True})
    facerecord={'scope':'derived D1 Jacobian leading face at physical order0 equals the free nonzero Keller constant',
        'face_polynomial':str(face),'face_derivation':face_meta,'raw_rows':DRIVER.encoded_rows(facerows),
        'singular':facesing,'rational_point':facepointmeta,'gauge_coverage_audit_required':True}
    context['output'].with_name(context['output'].stem+'_D1_J.json').write_text(
        json.dumps(jsonable(facerecord),indent=2,sort_keys=True)+'\n')
    result['D1_J_face']=facerecord
    if facesing['unit_ideal']:
        result['unit_ideal']=True
        return result
    constant,jets=corner_from_blocks(current(context['h']),current(context['C2']),
        current(context['C3']),{name:current(poly) for name,poly in context['outer'].items()})
    rows=[('gauge_early_J_constant',constant-jc)]
    context['reduce_new'](rows,'gauge_early_J_constant')
    free,mapping,residual,allraw=context['state']()
    path=context['output'].with_name(context['output'].stem+'_early_J.sing')
    singular=E.singular_dimension(residual,context['branch'],path)
    point,pmeta=context['rational_candidate'](residual,free,mapping,context['branch'])
    if point is not None:
        assert all(sp.expand(sp.sympify(row).xreplace(point))==0 for _,row in allraw)
        pmeta.update({'all_accumulated_raw_rows_verified':len(allraw),'raw_images_all_zero':True})
    record={'scope':'constant coefficient required by the full Jacobian equation, imposed early',
            'corner_formula':'K[D,0], K[D-1,0]-K[D-1,1], K[D-1,1]',
            'constant_polynomial':str(constant),'actual_polynomial_jets':jets,
            'direct_derivative_control':corner_control(),'singular':singular,'rational_point':pmeta,
            'nonzero_constant_is_free':'Jc with inverseZJ; no numerical normalization or torus spend',
            'gauge_coverage_audit_required':True}
    context['output'].with_name(context['output'].stem+'_early_J.json').write_text(
        json.dumps(jsonable(record),indent=2,sort_keys=True)+'\n')
    result['early_J_constant']=record
    result['unit_ideal']=singular['unit_ideal']
    return result


def gauge_branch_data(branch,mode='corrected'):
    data=ORIGINAL_BRANCH_DATA(branch,mode)
    if DERIVING_GENERIC or mode!='corrected':
        return data
    data=dict(data)
    data['parameters']=[v for v in data['parameters'] if v!=JET0]
    data['w_terms']=[(n,k,value) for n,k,coefficient in data['w_terms']
                     if (value:=sp.sympify(coefficient).xreplace(GAUGE))!=0]
    return data


def gauge_inner(branch):
    global DERIVING_GENERIC
    DERIVING_GENERIC=True
    MM._w_power.cache_clear()
    try:
        h,C2,C3,free,metadata=ORIGINAL_INNER(branch)
    finally:
        DERIVING_GENERIC=False
        MM._w_power.cache_clear()
    had_jet0=JET0 in free
    assert had_jet0,'generic source chart lost the declared translation orbit coordinate'
    def specialize(poly):
        return {key:value for key,expression in poly.items()
                if (value:=sp.expand(sp.sympify(expression).xreplace(GAUGE)))!=0}
    h,C2,C3=map(specialize,(h,C2,C3))
    metadata=dict(metadata)
    metadata['additional_rows']=[(label,sp.expand(row.xreplace(GAUGE)))
                                 for label,row in metadata['additional_rows']]
    metadata['generic_inner_dimension_before_gauge']=metadata['inner_dimension_before_residual']
    metadata['inner_dimension_before_residual']-=1
    metadata['h3_free']=[name for name in metadata['h3_free'] if name!='jet0']
    metadata['gauge_slice']={
        'ring_map':{'jet0':'0'},'wrapper_sha256':OWN_SHA256,
        'source_parameter_spent':'second source translation, residual diagonal (x,y)->(x+q,y+q)',
        'first_source_translation':'major centre combination B-A already spent by generic engine',
        'full_chart_transport':'T_q K = sum c_(r,p) t^r z^p (1+q*t)^(D-r-p)',
        'inverse':'T_(-q)',
        'centre_transport':{'jet0':'jet0-q','u':'u','minor_a2_or_v':'minor_a2_or_v-q*u',
                            'rho_or_c':'unchanged','Hc_11_0':'unchanged'},
        'retained_centres':'minor_a2 on delta2; u,v on delta52; localizer rho/c',
        'full_chart_verdict_status':'GAUGE_ISOMORPHISM_AUDIT_REQUIRED; this run directly decides the displayed slice',
        'generic_state_derived_before_specialization':True,
        'local_series_specialized_before_expansion':True,
        'no_other_equation_or_coordinate_pin':True}
    resultfree=set(free)-{JET0}
    assert not any(JET0 in sp.sympify(v).free_symbols for p in (h,C2,C3) for v in p.values())
    return h,C2,C3,resultfree,metadata


MM.branch_data=gauge_branch_data
E.inner_state=gauge_inner


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--branch',required=True,choices=['delta2','delta52'])
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--max-stage',type=int,default=1000)
    parser.add_argument('--timeout-seconds',type=float)
    args=parser.parse_args()
    DRIVER.run(args.branch,args.output.resolve(),args.max_stage,8,args.timeout_seconds,deep_hook=gauge_accelerate)
    data=json.loads(args.output.read_text())
    data['gauge_wrapper_sha256']=OWN_SHA256
    data['type']='EXACT-Q GAUGE SLICE; FULL-CHART PROMOTION REQUIRES THE T_q ISOMORPHISM AUDIT'
    args.output.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
