#!/usr/bin/env python3
"""Alternative full-chart row order with a complete minor block after stage8.

The finite stages are unchanged.  The accelerated block derives every inner
and outer strict minor valuation row from the represented polynomials, reduces
them in local-power order, and imposes the derived F/G leading targets.  These
conditions imply all F/G pole rows by polynomial multiplication.  Only QQ*
pivots or certified powers restrict the subsequent global Jacobian products.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import sys
import time
import subprocess

import sympy as sp

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import deep_driver as DRIVER
import engine as E
from source_data import SOURCE as S,jsonable

OWN_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def verify_quotient_images(images,residual,branch,path):
    nonzero=[sp.expand(value) for value in images if value!=0]
    if not nonzero:
        return {'mode':'literal polynomial zero','nonzero_before_normal_form':0,'all_zero':True}
    assert residual,'nonzero raw image after eliminating an empty residual'
    loc=sp.Symbol('rho' if branch=='delta2' else 'c')
    wrapper=sp.Symbol('Zrho' if branch=='delta2' else 'Zc')
    expressions=[row for _,row in residual]
    variables=sorted(set().union(*(v.free_symbols for v in nonzero+expressions))|{loc},key=str)
    enc=lambda value:str(value).replace('**','^')
    script=(f'ring R=0,({",".join(map(str,variables+[wrapper]))}),dp;\n'
            f'ideal I={",".join(map(enc,expressions))},{wrapper}*{loc}-1;\n'
            'ideal S=std(I);\n'
            f'ideal Images={",".join(map(enc,nonzero))};\n'
            'ideal N=reduce(Images,S);\nprint("BEGIN_CHECK");print(size(N));print(N);print("END_CHECK");\nquit;\n')
    path.write_text(script)
    run=subprocess.run(['Singular','-q'],input=script,text=True,capture_output=True,check=True)
    path.with_suffix('.sing.out').write_text(run.stdout+run.stderr)
    size=int(run.stdout.split('BEGIN_CHECK\n',1)[1].splitlines()[0])
    assert size==0,run.stdout
    return {'mode':'exact-Q normal form in localized maintained residual ideal',
            'nonzero_before_normal_form':len(nonzero),'all_zero':True,'script':str(path)}


def accelerate(context):
    start=time.monotonic()
    branch=context['branch']
    output=context['output']
    tracepath=output.with_name(output.stem+'_minor_block.json')
    cover=S['minor'][branch]['cover']
    h3floor=S['minor'][branch]['h3_local_floor']
    h2floor=h3floor*S['inner_power']
    pi=sp.Symbol('pi')
    P=S['minor'][branch]['h3_face']
    trace=[]
    targets=[]

    def snapshot(final=False,unit=False,proof=None):
        free,mapping,residual,allraw=context['state']()
        record={'type':'DERIVED COMPLETE MINOR BLOCK, LOCAL POWER ORDER',
            'branch':branch,'accelerated_driver_sha256':OWN_SHA256,
            'trace':trace,'target_equations':targets,'unit_ideal':unit,
            'final':final,'residual_rows':DRIVER.encoded_rows(residual),
            'remaining_free':len(free-set(mapping)),
            'elapsed_seconds':round(time.monotonic()-start,3),
            'pole_implication_certificate':proof}
        tracepath.write_text(json.dumps(jsonable(record),indent=2,sort_keys=True)+'\n')
        return record

    def consume_groups(groups,kind):
        for power,rows in sorted(groups.items()):
            t0=time.monotonic()
            _free,before,_residual,_allraw=context['state']()
            before_count=len(before)
            context['reduce_new'](rows,f'accelerated_{kind}_local{power}')
            free,mapping,residual,allraw=context['state']()
            sing=E.singular_dimension(residual,branch,output.with_name(
                f'{output.stem}_{kind}_local{power}.sing'))
            dim=-1 if sing['unit_ideal'] else len(free-set(mapping))-sing['codimension']
            point,pmeta=context['rational_candidate'](residual,free,mapping,branch)
            if point is not None:
                bad=[(label,str(value)) for label,row in allraw
                     if (value:=sp.expand(sp.sympify(row).xreplace(point)))!=0]
                assert not bad,bad[:3]
                pmeta.update({'all_accumulated_raw_rows_verified':len(allraw),
                              'raw_images_all_zero':True})
            trace.append({'kind':kind,'local_power':power,'new_rows':len(rows),
                'new_Qstar_pivots':len(mapping)-before_count,
                'remaining_free':len(free-set(mapping)),'residual_count':len(residual),
                'dimension':dim,'singular':sing,'rational_point':pmeta,
                'seconds':round(time.monotonic()-t0,3)})
            DRIVER.log(f'[{branch} accelerated {kind} local{power}] rows={len(rows)} '
                       f'QQ*={len(mapping)-before_count} dim={dim} point={pmeta["status"]}')
            snapshot(False,sing['unit_ideal'])
            if sing['unit_ideal']:
                return False
        return True

    def current(poly):
        _free,mapping,_residual,_allraw=context['state']()
        return DRIVER.apply_poly(poly,mapping)

    def leading(table,power):
        _free,mapping,_residual,_allraw=context['state']()
        return sp.expand(sum(E.substitute_map(value,mapping)*pi**k
                             for (n,k),value in table.items() if n==power))

    def coefficient_rows(expression,prefix):
        return [(f'{prefix}_coord{k[0]}',coefficient)
                for k,coefficient in sp.Poly(sp.expand(expression),pi).terms() if coefficient!=0]

    # Every strict scalar row is emitted; neither equality is zeroed.
    innerlocal={}
    innerfloors={'C2':2*h3floor,'C3':S['inner_power']*h3floor}
    groups=defaultdict(list)
    for name,floor in innerfloors.items():
        DRIVER.log(f'[{branch} accelerated] composing {name} through local{floor}')
        table=E.local_rows(current(context[name]),branch,floor)
        innerlocal[name]=table
        for (power,k),value in table.items():
            if power<floor:
                groups[power].append((f'accelerated_{name}_minor_local{power}_coord{k}',value))
    if not consume_groups(groups,'inner_strict'):
        return snapshot(True,True)
    # h3 already has the derived exact P leader. Hence h2=P^3 precisely when
    # the canonical remainder equality C2_face*P+C3_face is zero.
    innerface=leading(innerlocal['C2'],innerfloors['C2'])*P+leading(innerlocal['C3'],innerfloors['C3'])
    innerrows=coefficient_rows(innerface,'accelerated_H2_minor_target')
    targets.extend(DRIVER.encoded_rows(innerrows))
    if not consume_groups({h2floor:innerrows},'inner_target'):
        return snapshot(True,True)

    outerlocal={}
    outerfloors={}
    groups=defaultdict(list)
    for name,poly in context['outer'].items():
        degree=S['outer_specs'][name][0]+1
        floor=(degree//S['k2_degree'])*h2floor-cover
        outerfloors[name]=floor
        DRIVER.log(f'[{branch} accelerated] composing {name} through local{floor}')
        table=E.local_rows(current(poly),branch,floor)
        outerlocal[name]=table
        for (power,k),value in table.items():
            if power<floor:
                groups[power].append((f'accelerated_{name}_minor_local{power}_coord{k}',value))
    if not consume_groups(groups,'outer_strict'):
        return snapshot(True,True)
    H2face=sp.expand(P**S['inner_power'])
    outerfaces={name:leading(table,outerfloors[name]) for name,table in outerlocal.items()}
    Fdifference=sp.expand(outerfaces['A2']*H2face+outerfaces['A3'])
    Gdifference=sp.expand(outerfaces['B1']*H2face+outerfaces['B2'])
    fgrows=coefficient_rows(Fdifference,'accelerated_F_minor_target')+coefficient_rows(Gdifference,'accelerated_G_minor_target')
    targets.extend(DRIVER.encoded_rows(fgrows))
    if not consume_groups({max(S['minor'][branch]['F_local_floor'],S['minor'][branch]['G_local_floor']):fgrows},'FG_targets'):
        return snapshot(True,True)

    # Recheck all omitted pole implications in the declared polynomial ring.
    _free,mapping,residual,_allraw=context['state']()
    images=[]
    for name,table in innerlocal.items():
        images.extend(E.substitute_map(value,mapping) for (n,_),value in table.items() if n<innerfloors[name])
    for name,table in outerlocal.items():
        images.extend(E.substitute_map(value,mapping) for (n,_),value in table.items() if n<outerfloors[name])
    for expression in (innerface,Fdifference,Gdifference):
        images.extend(E.substitute_map(value,mapping) for _label,value in coefficient_rows(expression,'check'))
    recheck=verify_quotient_images(images,residual,branch,output.with_name(output.stem+'_pole_implications.sing'))
    alltags={name:sum(map(len,E.raw_minor_support(branch,name).values())) for name in ('F','G')}
    proof={'all_scalar_strict_floor_rows_rechecked':True,
        'inner_target_rechecked':True,'FG_target_differences_rechecked':True,
        'normal_form_recheck':recheck,
        'h3_local_floor':h3floor,'h2_local_floor':h2floor,
        'inner_remainder_floors':innerfloors,'unshifted_outer_remainder_floors':outerfloors,
        'implied_raw_pole_rows':alltags,
        'identity':'F=H2^3+A2_effective*H2+A3_effective; G=H2^2+B1_effective*H2+B2_effective',
        'reason':'Every product has order at least its derived F/G floor. The leading differences were emitted and rechecked exactly. Polynomial multiplication implies every strict lower coefficient is zero.'}
    return snapshot(True,False,proof)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--branch',required=True,choices=['delta2','delta52'])
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--max-stage',type=int,default=1000)
    parser.add_argument('--timeout-seconds',type=float)
    args=parser.parse_args()
    DRIVER.run(args.branch,args.output.resolve(),args.max_stage,8,args.timeout_seconds,deep_hook=accelerate)
