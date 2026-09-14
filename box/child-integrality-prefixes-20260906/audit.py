#!/usr/bin/env python3
"""Exact, finite major-partition audit of the 20 frozen prefix rows.

No terminal child datum is invented. Minor refinement remains unasserted.
Run from the repository root. The only uncharged dependency is the pinned
mechanical route checker required by the frozen descend_own module.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import types
from collections import Counter
from fractions import Fraction as Q
from math import gcd
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
INPUT = Path('/tmp/jc2-lane.ZUsUCw/inputs')
DEPENDENCY = ROOT / 'box/lib/own_v_routes.py'
DEP_HASH = 'f07dd9b0e38118132ed2ec2e5e7e972f98ba8f223213062fed356a30188b3bf3'
assert hashlib.sha256(DEPENDENCY.read_bytes()).hexdigest() == DEP_HASH

# Execute the actual frozen instrument, including its own correlated route
# check. Never replace its V vector by a copied source vector.
pkg = types.ModuleType('prefix_frozen')
pkg.__path__ = []
sys.modules[pkg.__name__] = pkg
for name, path in [('own_v_routes', DEPENDENCY), ('descend_own', INPUT/'descend_own.py')]:
    spec = importlib.util.spec_from_file_location(f'prefix_frozen.{name}', path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
OWN = sys.modules['prefix_frozen.descend_own']


def partitions(total, smallest=1):
    if not total:
        yield ()
    for r in range(smallest, total + 1):
        for tail in partitions(total-r, r):
            yield (r,) + tail


def integer(x):
    x = Q(x)
    assert x.denominator == 1, x
    return x.numerator


def minor_group(source, own, multiplicity, epsilon, index=2):
    """Simple detector degree one cannot split before zero order (M6.1(2))."""
    d = OWN.prefix_gcds(source.n, source.M)
    lo = Q(d[index], source.n-source.M[index])
    item = dict(multiplicity=multiplicity, count=epsilon.numerator,
                rho_f=Q(source.m*multiplicity,d[index]),
                rho_g=Q(source.n*multiplicity,d[index]),
                lambda_f=Q(0),lambda_g=Q(0))
    if multiplicity==1:
        final_parent=epsilon+lo*(1-epsilon)
        item.update(status='DETERMINED_SIMPLE_FINAL_MINOR_PACKETS',
            parent_delta=final_parent,
            delta=own['ell']+1+Q(own['us'],1)/epsilon*(final_parent-1))
        assert item['delta']>own['ell']+1
    else:
        item.update(status='MINOR_GROUP_FINAL_SUBDIVISION_UNDETERMINED',
            missing='First split support and leading detector polynomial of multiplicity-two group')
    return item


def zero_minor_options(source, own, epsilon, z, zero_roots):
    if z==0:
        return [dict(type='FINITE_PARENT_LINE',count=1,rho_f=zero_roots,
                     delta=Q(own['vs']),lambda_f=Q(0),lambda_g=Q(0))]
    assert z==1
    d=OWN.prefix_gcds(source.n,source.M)
    rho=Q(source.m,d[2])
    end=epsilon+Q(d[2],source.n-source.M[2])*(1-epsilon)
    end_int=integer(end)
    assert rho*end==zero_roots
    options=[]
    for k in range(1,end_int):
        options.append(dict(type='FIRST_SUPPORT_BEFORE_ENDPOINT',first_support=k,
            count=k,rho_f=rho,
            delta=own['ell']+1+Q(own['us'],k)*(end-1),
            finite_line_rho_f=zero_roots-k*rho,finite_line_delta=Q(own['vs']),
            lambda_f=Q(0),lambda_g=Q(0)))
    options.append(dict(type='ALL_EARLIER_COMMON_COEFFICIENTS_ZERO',first_support=end,
        count=1,rho_f=zero_roots,delta=own['vs']-Q(own['us'],1)/end,
        finite_line_rho_f=Q(0),lambda_f=Q(0),lambda_g=Q(0)))
    return options


def packet(source, own, multiplicity, epsilon, count, higher=None):
    """A D2 above-average factor continues to final D1 (Moh Prop5.3)."""
    n, m = source.n, source.m
    vv = source.V | (higher or {}) | {2: multiplicity}
    dd = OWN.prefix_gcds(n, source.M)
    delta = OWN.def51_radii(n, source.M, dd, vv)[1]
    rho_f, rho_g = Q(m*multiplicity, dd[2]), Q(n*multiplicity, dd[2])
    lf, lg = Q(m, n+m)*(delta-1), Q(n, n+m)*(delta-1)
    A = (count*delta).denominator
    final_galois = ((rho_g % A == 0 and (rho_f-1) % A == 0) or
                    (rho_f % A == 0 and (rho_g-1) % A == 0))
    pp = dict(count=count, rho_f=rho_f, rho_g=rho_g,
              epsilon=epsilon, delta=delta, lambda_f=lf, lambda_g=lg,
              final_A=A, final_galois=final_galois,
              contribution=-count*rho_f*lg)
    assert 0 < epsilon < delta < 1
    u, H = own['us'], own['ell']+1
    cc = dict(count=integer(epsilon*count), rho_f=rho_f, rho_g=rho_g,
              delta=H+Q(u,1)/epsilon*(delta-1),
              lambda_f=Q(u,1)/epsilon*lf,
              lambda_g=Q(u,1)/epsilon*lg)
    cc['contribution'] = -cc['count']*rho_f*cc['lambda_g']
    cc['shifted_sum'] = Q(own['n'], own['n']+own['m'])*cc['count']*rho_f*(H-cc['delta'])
    assert cc['contribution'] == cc['shifted_sum'] == u*pp['contribution']
    assert cc['delta'] < H
    return dict(multiplicity=multiplicity, parent=pp, child=cc)


def enumerate_s3(source, own):
    n, m, s = source.n, source.m, source.s
    assert s == 3
    d = OWN.prefix_gcds(n, source.M)
    e = OWN.def51_radii(n, source.M, d, source.V)[2]
    a, b = e.numerator, e.denominator
    P = integer(Q(source.V[3]*d[2], d[3]))
    qdegree = integer(Q(source.V[3]*(n-source.M[2]), d[3]))
    lo = Q(d[2], n-source.M[2])
    accepted, rejected = [], []
    for z in range(P % b, P+1, b):
        for orbits in partitions((P-z)//b):
            if source.V[2] not in orbits:
                continue
            if int(z > 0)+b*len(orbits) > qdegree:
                continue
            # Prop5.6 excludes only the entirely zero major route. It does
            # not prohibit an intermediate zero before a later first support.
            if z > lo:
                rejected.append(dict(z=z, orbits=orbits, reason='REDUCED_ALL_ZERO_MAJOR'))
                continue
            if (z and z == lo) or lo in orbits:
                rejected.append(dict(z=z, orbits=orbits, reason='ODE_RESONANT_FACTOR'))
                continue
            majors = [packet(source, own, r, e, b) for r in orbits if r > lo]
            parent_sum = sum((p['parent']['contribution'] for p in majors), Q(0))
            child_sum = sum((p['child']['contribution'] for p in majors), Q(0))
            W0 = Q(own['us']*d[2], d[3])-a*sum(orbits)
            major_roots = sum(p['child']['count']*p['child']['rho_f'] for p in majors)
            minor_groups = [minor_group(source,own,r,e)
                            for r in orbits if r < lo]
            residual_roots = own['m']-major_roots
            zero_roots = Q(m,d[2])*W0
            assert zero_roots+sum(g['count']*g['rho_f'] for g in minor_groups)==residual_roots
            inv = OWN.inverse_top(n,d[3],d[2],own['us'],source.V[3],e,z,orbits)
            assert inv['inverse_groups'][0]['V']==W0
            assert sum(g['roots'] for g in inv['inverse_groups'])==own['n']
            rec = dict(z=z, orbits=orbits, epsilon=e, threshold=lo,
                       p_degree=P,q_degree=qdegree,majors=majors,
                       parent_sum=parent_sum,child_sum=child_sum,
                       child_major_roots=major_roots,
                       child_minor_roots=residual_roots,
            inverse_minor_groups=minor_groups,
                       inverse_zero_V=W0,inverse_zero_f_roots=zero_roots,
                       zero_remainder_type=('FINITE_PARENT_LINE_PACKET' if z==0 else
                           'ZERO_MINOR_ENDPOINT_PLUS_FINITE_LINE_UNRESOLVED'),
                       finite_line_radius=(Q(own['vs']) if z==0 else None),
                       zero_minor_options=zero_minor_options(source,own,e,z,zero_roots))
            if any(not p['parent']['final_galois'] for p in majors):
                rec['reason']='PARENT_FINAL_MAJOR_GALOIS'
                rejected.append(rec)
            elif W0 < 0:
                rec['reason']='CONDITIONAL_INVERSE_NEGATIVE_REMAINDER'
                rejected.append(rec)
            else:
                accepted.append(rec)
    return accepted,rejected


def enumerate_r066(source, own):
    # Exhaustive top: P3=14,Q3=7,A3=6 and selected V3=8.
    # A nonzero selected orbit would cost 48>14, so z=8 and r=(1).
    # The single zero major continues to D2; P2=24,Q2=16,A2=3,V2=8
    # then forces z=0,r=(8). The other D3 orbit is strictly minor (1<2).
    assert (source.n,source.m,source.M,source.V)==(
        162,108,{1:-108,2:126,3:153,4:160},{2:8,3:8,4:7})
    top = [(z,rr) for z in range(2,15,6) for rr in partitions((14-z)//6)
           if z==8 and int(z>0)+6*len(rr)<=7]
    bottom = [(z,rr) for z in range(0,25,3) for rr in partitions((24-z)//3)
              if 8 in rr and int(z>0)+3*len(rr)<=16]
    assert top==[(8,(1,))] and bottom==[(0,(8,))]
    p = packet(source,own,8,Q(1,3),3)
    assert p['parent']['final_galois']
    assert (p['parent']['contribution'],p['child']['contribution'])==(16,32)
    assert OWN.inverse_top(162,9,18,2,7,Q(1,6),8,(1,))['inverse_groups'][0]['V']==3
    return [dict(z=8,orbits=(1,),epsilon=Q(1,6),threshold=Q(2),
                 p_degree=14,q_degree=7,
                 lower_pattern=dict(z=0,orbits=(8,),epsilon=Q(1,3),p_degree=24,q_degree=16),
                 majors=[p],parent_sum=Q(16),child_sum=Q(32),
                 child_major_roots=Q(16),child_minor_roots=Q(8),
                 inverse_minor_groups=[minor_group(source,own,1,Q(1,6),3)],
                 inverse_zero_V=Q(3),inverse_zero_f_roots=Q(18),
                 lower_zero_remainder_f_roots=Q(2),
                 zero_remainder_type='FINITE_PARENT_LINE_PACKET',
                 finite_line_radius=Q(7),
                 zero_minor_options=[dict(type='FINITE_PARENT_LINE',count=1,rho_f=Q(2),
                     delta=Q(7),lambda_f=Q(0),lambda_g=Q(0))])],[]


def encode(obj):
    if isinstance(obj,Q):
        return str(obj)
    raise TypeError(type(obj))


def main():
    rows=[]
    for line in (INPUT/'roster.jsonl').read_text().splitlines():
        r=json.loads(line)
        if r['source']['u_s']<2:
            continue
        src=r['source']
        source=SimpleNamespace(n=src['n'],m=src['m'],s=src['s'],
            M=dict(enumerate(src['M'],1)),V=dict(enumerate(src['V'],2)))
        own=OWN.descend_own(source)  # radius_licensed stays False.
        assert own['descent_license']=='CONDITIONAL_PROP6.3_RADIUS'
        assert own['characteristic_scope']=='retained prefix only'
        assert own['d'][own['s']+1]==own['us']>1
        assert len(own['V_vectors'])==len(own['routes'])==1
        assert own['V_vectors'][0]==tuple(map(Q,r['own_child']['V_prime']))
        assert list(own['M'].values())==r['own_child']['M_prime']
        assert list(own['child_radii'][0]['delta'].values())==list(map(Q,r['own_child']['delta_prime']))
        accepted,rejected=(enumerate_s3(source,own) if source.s==3 else enumerate_r066(source,own))
        sums=sorted({c['child_sum'] for c in accepted})
        psums=sorted({c['parent_sum'] for c in accepted})
        assert accepted and all(x.denominator==1 for x in psums)
        assert sums==sorted(own['us']*x for x in psums)
        row=dict(row_id=r['row_id'],source=src,
            own={key:own[key] for key in ['n','m','s','M','d','ell','us','vs','ds',
                 'V_vectors','characteristic_scope','descent_license','top_license','child_radii']},
            parent_partition_status='COMPLETE_MAJOR_LIST_BY_PRINTED_FIXED_LIST; MINOR_REFINEMENT_OPEN',
            status='SURVIVES',status_scope='INTEGRAL_NECESSARY_ALTERNATIVE; NOT_REALIZATION',
            radius_condition='OPEN[PROP6.3-RADIUS-US>1]: delta_star_(s-1) >= v_s/u_s',
            parent_sums=psums,child_sums=sums,accepted_patterns=accepted,rejected_patterns=rejected,
            minor_roots=sorted({c['child_minor_roots'] for c in accepted}),
            rejected_parent_fractional_sums=sorted({c['parent_sum'] for c in rejected
                if 'parent_sum' in c and c['parent_sum'].denominator!=1}),
            split_window_es_leaves=r['split_window']['leaf_count'])
        rows.append(row)
    assert len(rows)==20
    assert Counter(r['own']['us'] for r in rows)=={2:11,3:6,4:2,5:1}
    all_accepted=[c for r in rows for c in r['accepted_patterns']]
    final_rejected=[c for r in rows for c in r['rejected_patterns']
                    if c['reason']=='PARENT_FINAL_MAJOR_GALOIS']
    assert len(all_accepted)==35 and len(final_rejected)==40
    assert sum(r['split_window_es_leaves'] for r in rows)==36
    # Independent hand values and controls against the two common map errors.
    r12=rows[0]; p12=r12['accepted_patterns'][0]['majors'][0]
    assert (p12['child']['count'],p12['child']['rho_f'],p12['child']['lambda_g'])==(1,14,-3)
    wrong_count_sum=-r12['own']['us']*p12['child']['count']*p12['child']['rho_f']*p12['child']['lambda_g']
    wrong_unshifted=Q(24,40)*14*(1-p12['child']['delta'])
    assert wrong_count_sum==84 and wrong_count_sum!=42
    assert wrong_unshifted==Q(42,5) and wrong_unshifted!=42
    result=dict(schema='jc2.child-integrality-prefixes/v1',
        frozen_input_dir=str(INPUT),mechanical_dependency=dict(path=str(DEPENDENCY),sha256=DEP_HASH),
        semantics='Exact finite necessary major configurations; no polynomial witness; no full minor partition',
        controls=dict(R012_expected_child=42,wrong_u_in_disc_count=wrong_count_sum,
                      wrong_unshifted_sum=wrong_unshifted,
                      R066_expected_parent=16,R066_expected_child=32,
                      actual_stabilizer_zero_adds_no_denominator=True),
        rows=rows,
        summary=dict(rows=len(rows),survives=20,conditional_dead=0,undetermined_major_sum=0,
            accepted_patterns=sum(len(r['accepted_patterns']) for r in rows),
            reduced_top_patterns=len(all_accepted)+len(final_rejected),
            rejected_by_final_major_galois=len(final_rejected),
            frozen_roster_es_leaves=36,
            all_parent_sums_integral=True,all_child_sums_us_times_parent=True,
            own_vectors_singleton=20,radius_unlicensed=20))
    (HERE/'audit.json').write_text(json.dumps(result,default=encode,indent=2)+'\n')
    for r in rows:
        print(r['row_id'], 'patterns',len(r['accepted_patterns']),
            'parent',','.join(map(str,r['parent_sums'])),
            'child',','.join(map(str,r['child_sums'])),
            'minor',','.join(map(str,r['minor_roots'])),
            'rejected_frac',','.join(map(str,r['rejected_parent_fractional_sums'])))
    print(json.dumps(result['summary']))


if __name__=='__main__':
    main()
