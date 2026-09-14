#!/usr/bin/env python3
"""Incremental exact-Q full schedule on the derived (99,66) coefficient chart.

Only QQ* pivots and certified pure-power radical rows restrict later builds.
All outer D2 coordinates remain in the declared ring; D1 offsets enter at
their scheduled stage. The first nine finite stages are followed by the same
independent local-power/Jacobian filtration until every row is exhausted.
The final constant Jacobian is free nonzero Jc, not an extra torus spend.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from math import comb
from pathlib import Path
import sys
import time

import sympy as sp

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import engine as E
import deep_rows as D
from source_data import SOURCE as S, jsonable
ENGINE_SHA256=hashlib.sha256((HERE/'engine.py').read_bytes()).hexdigest()
DRIVER_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
HELPERS_SHA256=hashlib.sha256((HERE/'deep_rows.py').read_bytes()).hexdigest()
SOURCE_SHA256=hashlib.sha256((HERE/'source_data.py').read_bytes()).hexdigest()


def log(message):
    print(message,flush=True)


def encoded_rows(rows):
    return [(label,str(row)) for label,row in rows]


def apply_poly(poly,mapping,cutoff=None):
    return {pos:value for pos,expression in poly.items()
            if (cutoff is None or pos[0]<=cutoff)
            and (value:=E.substitute_map(sp.sympify(expression),mapping))!=0}


def outer_D1_rows(outer,offset):
    cover,base,child=S['D1_substitution']
    multiplier=cover//S['D2_weight'][0]
    rows=[]
    for name,(_degree,floor,threshold) in S['outer_specs'].items():
        W=floor+offset
        for k in range(max(0,(threshold-multiplier*W+child-base-1)//(child-base))):
            expression=sum(comb(q,k)*v for (r,q),v in outer[name].items()
                           if E.weight((r,q))==W and q>=k)
            rows.append((f'{name}_D1_s{offset}_k{k}',sp.expand(expression)))
    return rows


def targets(branch):
    data=S['minor'][branch]
    pi=sp.Symbol('pi')
    result={}
    for name in ('F','G'):
        result[name]={(data[name+'_local_floor'],q[0]):v
                      for q,v in sp.Poly(data[name+'_face'],pi).terms()}
    floor=data['h3_local_floor']*S['inner_power']
    result['H2']={(floor,q[0]):v for q,v in sp.Poly(
        sp.expand(data['h3_face']**S['inner_power']),pi).terms()}
    return result


def rational_candidate(rows,free,mapping,branch):
    """Find a small rational point of the current residual; no branch restriction."""
    localizer=sp.Symbol('rho' if branch=='delta2' else 'c')
    for jet in (1,0,-1):
        point=dict.fromkeys(free-set(mapping),sp.Integer(0))
        point[localizer]=sp.Integer(1)
        if sp.Symbol('jet0') in point:
            point[sp.Symbol('jet0')]=sp.Integer(jet)
        if sp.Symbol('Jc') in point:
            point[sp.Symbol('Jc')]=point[sp.Symbol('ZJ')]=sp.Integer(1)
        bad=[]
        for label,row in rows:
            value=sp.expand(row.xreplace(point))
            if value!=0:
                bad.append((label,str(value)))
        if not bad:
            full=dict(point)
            for variable,rhs in mapping.items():
                value=sp.expand(rhs.xreplace(point))
                assert not value.free_symbols and value.is_Rational
                full[variable]=value
            return full,{'status':'FOUND_EXACT_Q','free_trial':{'jet0':jet,str(localizer):1},
                         'nonzero_assignment':{str(v):str(value) for v,value in full.items() if value!=0}}
    return None,{'status':'NO_SMALL_RATIONAL_POINT_FOUND_DIMENSION_ONLY',
                 'last_trial_first_failures':bad[:5]}


def run(branch,output,max_stage,finite_through=8,timeout_seconds=None):
    start=time.monotonic()
    outdir=output.parent
    outdir.mkdir(parents=True,exist_ok=True)
    h,C2,C3,inner,major=E.inner_state(branch)
    baseouter,outerfree,outermeta=E.outer_state(-1)
    baseouter={name:dict(poly) for name,poly in baseouter.items()}
    free=set(inner)|set(outerfree)
    localizer=sp.Symbol('rho' if branch=='delta2' else 'c')
    mapping={}
    residual=list(major['additional_rows'])
    all_raw=[]
    pivot_certificates=[]
    radical_certificates=[]
    records=[]
    trgt=targets(branch)
    support={name:E.raw_minor_support(branch,name) for name in ('F','G')}
    pole_max=max(S['minor'][branch]['F_local_floor'],S['minor'][branch]['G_local_floor'])
    jdegree=S['n']+S['m']-2
    firstpole=E.stage_spec(branch,0)['pole_local_power']
    terminal=max(jdegree,pole_max-firstpole)
    requested=min(max_stage,terminal)
    pole_done=0
    h2_done=0
    inner_remainder_done={'C2':0,'C3':0}
    outer_remainder_done={name:0 for name in baseouter}
    jdone=set()
    totalzero=0
    priorstart=S['m']*S['h3_minor']//S['h3_degree']-1
    priorwidth=S['h3_degree']-1
    firstnamed=priorstart+priorwidth
    d1_multiplier=S['D1_substitution'][0]//S['D2_weight'][0]
    outer_last=max((threshold-d1_multiplier*floor-1)//d1_multiplier
                   for _degree,floor,threshold in S['outer_specs'].values())
    source_status={
        'original_gate_point':'FAILS_INITIAL_SOURCE_C2_C3_FLOOR_ROWS',
        'certificate':f'deep_diagnostic_point_{branch}.json',
        'C2_minimum_weight':15,'required_C2_floor':S['C2_floor'],
        'C3_minimum_weight':47,'required_C3_floor':S['C3_floor'],
        'full_chart_point_claim':False}

    def save(final=False,reason=None):
        safe_major={key:value for key,value in major.items() if key!='additional_rows'}
        data={'type':'EXACT-Q FULL DERIVED CHART; INCREMENTAL SOUND LOCUS',
              'branch':branch,'engine_sha256':ENGINE_SHA256,
              'driver_sha256':DRIVER_SHA256,'helpers_sha256':HELPERS_SHA256,'source_derivation_sha256':SOURCE_SHA256,
              'finite_schedule_through':finite_through,'requested_max_stage':max_stage,
              'full_terminal_stage':terminal,'last_completed_stage':records[-1]['stage'] if records else None,
              'initial_inner':safe_major,'initial_outer':outermeta,
              'gate_point_control':source_status,'records':records,
              'cumulative_map':E.encode_map(mapping),'pivot_certificates':pivot_certificates,
              'radical_certificates':radical_certificates,
              'remaining_residual':encoded_rows(residual),
              'elapsed_seconds':round(time.monotonic()-start,3),
              'final':final,'stop_reason':reason,
              'all_rows_exhausted':bool(records and records[-1]['stage']==terminal)}
        output.write_text(json.dumps(jsonable(data),indent=2,sort_keys=True)+'\n')

    def reduce_new(rows,phase):
        nonlocal mapping,residual,totalzero
        current=[(label,E.substitute_map(sp.sympify(row),mapping)) for label,row in rows]
        all_raw.extend(current)
        pending=residual+current
        rounds=0
        while True:
            remain,new,pivots,zeros=E.qstar_reduce(pending,free-set(mapping)-{localizer})
            totalzero+=zeros
            if new:
                mapping.update(new)
                mapping=E.resolve_map(mapping)
                for pivot in pivots:
                    pivot_certificates.append({'phase':phase,'label':pivot.label,
                        'variable':str(pivot.variable),'rational_leader':str(pivot.coefficient)})
            residual=remain
            roots,certificates=D.pure_power_radical_rows(residual)
            if not roots:
                break
            # A non-affine pure-power root cannot create a QQ* pivot. Keep it
            # as a certified radical generator once, then stop if no progress.
            eligible=free-set(mapping)-{localizer}
            roots=[(label,row) for label,row in roots if any(
                sp.diff(row,v).is_Rational and sp.diff(row,v)!=0 for v in row.free_symbols & eligible)]
            if not roots:
                break
            kept={label for label,_ in roots}
            radical_certificates.extend(dict(c,phase=phase) for c in certificates if c['new_row'] in kept)
            pending=residual+roots
            rounds+=1
            assert rounds<=len(free),'radical pivot did not decrease variables'

    reduce_new([], 'source_residue')
    save(False,'INITIAL_STATE_READY')
    for stage in range(requested+1):
        tick=time.monotonic()
        if timeout_seconds is not None and tick-start>=timeout_seconds:
            save(True,f'COMPUTE_BOUND_BEFORE_STAGE_{stage}')
            return
        phase='stage' if stage<=finite_through else 'deep'
        log(f'[{branch} {phase}{stage}] remaining={len(free-set(mapping))} residual={len(residual)}')
        if stage<=outer_last:
            reduce_new(outer_D1_rows(baseouter,stage),f'{phase}{stage}_outer_D1')
        spec=E.stage_spec(branch,stage)
        localcap=min(spec['pole_local_power'],pole_max)
        jcap=min(max(1,stage),jdegree)
        cover=S['minor'][branch]['cover']
        tcap=max((localcap+cover-1)//cover,jcap)
        hh=apply_poly(h,mapping,tcap)
        c2=apply_poly(C2,mapping,tcap)
        c3=apply_poly(C3,mapping,tcap)
        k2=E.tz_add(E.tz_mul(E.tz_mul(hh,hh,tcap),hh,tcap),E.tz_mul(c2,hh,tcap),c3)
        outer={name:apply_poly(poly,mapping,tcap) for name,poly in baseouter.items()}
        log(f'[{branch} {phase}{stage}] k2={len(k2)}, localcap={localcap}, Jcap={jcap}; emitting small-block local rows')
        local_F,local_G=D.local_FG(E,k2,outer,branch,localcap)
        rows=[]
        counts={'F':0,'G':0,'H2':0,'C2_minor':0,'C3_minor':0,'outer_minor':0,'J':0}
        for name,table in (('F',local_F),('G',local_G)):
            for n in range(pole_done+1,localcap+1):
                if n>S['minor'][branch][name+'_local_floor']:
                    continue
                tags=set(support[name].get(n,()))|{k for p,k in trgt[name] if p==n}
                for k in sorted(tags):
                    row=table.get((n,k),sp.Integer(0))-trgt[name].get((n,k),sp.Integer(0))
                    rows.append((f'{phase}{stage}_{name}_local{n}_coord{k}',sp.expand(row)))
                    counts[name]+=1
        pole_done=localcap
        if stage>finite_through:
            # Thm1.2 at the same completed minor system gives only floors
            # for these remainders. Equality is retained with no typed face.
            for name,poly,power in (('C2',c2,2),('C3',c3,S['inner_power'])):
                remainder_floor=S['minor'][branch]['h3_local_floor']*power
                remainder_cap=min(localcap,remainder_floor-1)
                remainder_local=E.local_rows(poly,branch,remainder_cap)
                for (n,k),value in sorted(remainder_local.items()):
                    if inner_remainder_done[name]<n<=remainder_cap:
                        rows.append((f'{phase}{stage}_{name}_minor_local{n}_coord{k}',value))
                        counts[name+'_minor']+=1
                inner_remainder_done[name]=remainder_cap
            # The quasi/approximate-root theorem gives the same strict
            # endpoint bounds for every outer remainder actually used.
            # Each unshifted block has one fewer t power than its effective
            # normalized contribution, hence the subtraction of the cover.
            h2_minor_floor=S['minor'][branch]['h3_local_floor']*S['inner_power']
            for name,poly in outer.items():
                normalization_degree=S['outer_specs'][name][0]+1
                remainder_power=normalization_degree//S['k2_degree']
                remainder_floor=remainder_power*h2_minor_floor-cover
                remainder_cap=min(localcap,remainder_floor-1)
                remainder_local=E.local_rows(poly,branch,remainder_cap)
                for (n,k),value in sorted(remainder_local.items()):
                    if outer_remainder_done[name]<n<=remainder_cap:
                        rows.append((f'{phase}{stage}_{name}_minor_local{n}_coord{k}',value))
                        counts['outer_minor']+=1
                outer_remainder_done[name]=remainder_cap
            h2floor=max(n for n,_ in trgt['H2'])
            h2cap=min(localcap,h2floor)
            h2local=E.local_rows(k2,branch,h2cap)
            tags=set(h2local)|set(trgt['H2'])
            for n,k in sorted(tags):
                if h2_done<n<=h2cap:
                    rows.append((f'{phase}{stage}_H2_local{n}_coord{k}',sp.expand(
                        h2local.get((n,k),0)-trgt['H2'].get((n,k),0))))
                    counts['H2']+=1
            h2_done=h2cap
        reduce_new(rows,f'{phase}{stage}_pole')
        # Pole pivots are propagated before expensive Jacobian products.
        k2=apply_poly(k2,mapping,jcap)
        outer={name:apply_poly(poly,mapping,jcap) for name,poly in outer.items()}
        if stage==0:
            slots={(1,k) for k in range(priorstart,firstnamed+1)}
        elif stage==1:
            slots={(1,k) for k in range(firstnamed+1,jdegree)}
        elif stage<=jdegree:
            slots={(stage,k) for k in range(jdegree-stage+1)}
        else:
            slots=set()
        if stage==finite_through+1:
            # Exhaust the top/low positive-degree slots absent from the old
            # named prefix. No cancellation is assumed without an emitted row.
            slots |= {(0,k) for k in range(jdegree+1)}
            slots |= {(1,k) for k in range(priorstart)}
        slots -= jdone
        if slots:
            log(f'[{branch} {phase}{stage}] factored Jacobian, {len(slots)} new scalar slots')
            J=D.all_w_bands(D.jacobian_factored(k2,outer,jcap),jcap)
            jrows=[]
            for tp,k in sorted(slots):
                value=J[tp].get(k,sp.Integer(0))
                if tp==jdegree and k==0:
                    jc,zj=sp.symbols('Jc ZJ')
                    free|={jc,zj}
                    value-=jc
                    jrows.append((f'{phase}{stage}_nonzero_J_wrapper',zj*jc-1))
                jrows.append((f'{phase}{stage}_J_t{tp}_d{jdegree-tp}_k{k}',value))
            counts['J']=len(jrows)
            reduce_new(jrows,f'{phase}{stage}_Jacobian')
            jdone |= slots
        log(f'[{branch} {phase}{stage}] QQ*={len(mapping)}, residual={len(residual)}; Singular exact Q')
        singpath=outdir/f'{output.stem}_{phase}{stage}.sing'
        singular=E.singular_dimension(residual,branch,singpath)
        dimension=-1 if singular['unit_ideal'] else len(free-set(mapping))-singular['codimension']
        point,pmeta=rational_candidate(residual,free,mapping,branch)
        if point is not None:
            failures=[]
            for label,row in all_raw:
                value=sp.expand(sp.sympify(row).xreplace(point))
                if value!=0:
                    failures.append((label,str(value)))
            assert not failures,failures[:3]
            pmeta.update({'all_accumulated_emitted_raw_rows_verified':len(all_raw),
                          'raw_row_images_all_zero':True,
                          'source_residue_verified':all(sp.expand(row.xreplace(point))==0 for _,row in major['additional_rows'])})
        rec={'stage':stage,'phase':phase,'local_power':localcap,'J_depth':jcap,
             'new_row_counts':counts,'cumulative_emitted_raw_rows':len(all_raw),
             'cumulative_Qstar_pivots':len(mapping),'free_after':len(free-set(mapping)),
             'residual_count':len(residual),'residual_hash':E.rows_hash(residual),
             'residual_rows':encoded_rows(residual),'dimension':dimension,'singular':singular,
             'original_gate_control':source_status,'rational_point':pmeta,
             'elapsed_stage_seconds':round(time.monotonic()-tick,3)}
        records.append(rec)
        log(f'[{branch} {phase}{stage}] dimension={dimension}; point={pmeta["status"]}; {time.monotonic()-tick:.2f}s')
        save(False,None)
        if singular['unit_ideal']:
            save(True,f'UNIT_CORRECTED_DERIVED_CHART_AT_{phase.upper()}_{stage}')
            return
    save(True,'ROWS_EXHAUSTED' if requested==terminal else f'COMPUTE_BOUND_AFTER_STAGE_{requested}')


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--branch',required=True,choices=['delta2','delta52'])
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--max-stage',type=int,default=1000)
    parser.add_argument('--finite-through',type=int,default=8)
    parser.add_argument('--timeout-seconds',type=float)
    args=parser.parse_args()
    run(args.branch,args.output.resolve(),args.max_stage,args.finite_through,args.timeout_seconds)
