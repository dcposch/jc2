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

JET0=sp.Symbol('jet0')
GAUGE={JET0:sp.Integer(0)}
ORIGINAL_INNER=E.inner_state
ORIGINAL_BRANCH_DATA=MM.branch_data
DERIVING_GENERIC=False
OWN_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


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
    DRIVER.run(args.branch,args.output.resolve(),args.max_stage,8,args.timeout_seconds,deep_hook=accelerate)
    data=json.loads(args.output.read_text())
    data['gauge_wrapper_sha256']=OWN_SHA256
    data['type']='EXACT-Q GAUGE SLICE; FULL-CHART PROMOTION REQUIRES THE T_q ISOMORPHISM AUDIT'
    args.output.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
