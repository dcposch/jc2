#!/usr/bin/env python3
"""(99,66) necessary chart built from printed root and remainder formulae.

The only inherited code is sparse arithmetic, QQ* elimination, stage labels,
and the exact-Q Singular wrapper. Mathematical state is rebuilt here.
Every ambient coefficient exists before its explicit valuation equation is
solved. Equality slots are retained, then solved only by coefficient rows.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, sys, time
from functools import lru_cache
from math import comb
from pathlib import Path
import sympy as sp

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from source_data import SOURCE as S, jsonable
import minor_maps as MM
spec=importlib.util.spec_from_file_location('frozen_arithmetic',HERE/'frozen/band_engine.py')
E=importlib.util.module_from_spec(spec);sys.modules[spec.name]=E;spec.loader.exec_module(E)
for name in ('symbol','expr_text','tz_add','tz_scale','tz_mul','tz_dt','tz_dz',
             'tz_times_t','z_band_to_w','substitute_map','resolve_map','qstar_reduce',
             'rows_hash','singular_dimension','jacobian_band',
             'jacobian_normalization_control'):
    globals()[name]=getattr(E,name)
TZ=dict
WT=S['D2_weight']
def weight(pos): return WT[0]*pos[0]+WT[1]*pos[1]
def log(message): print(message,file=sys.stderr,flush=True)
def encode_map(mapping): return {str(k):str(v) for k,v in mapping.items()}

def substitute_map(expr,substitutions):
    """Exact simultaneous symbol replacement, iterated for triangular maps."""
    current=sp.sympify(expr)
    if not substitutions: return current
    for _ in range(len(substitutions)+2):
        if not current.free_symbols.intersection(substitutions): return sp.expand(current)
        image=sp.expand(current.xreplace(substitutions))
        if image==current: return image
        current=image
    raise AssertionError('nonterminating substitution map')
E.substitute_map=substitute_map

def h3_template():
    """Full degree-11 ambient box, explicit below-face rows, triangular basis.

    At fixed r the surviving strict coefficients are expressed in
    z^v(1+z)^j; this has diagonal one. Equality uses separate raw monomials.
    Hc_11_0 therefore keeps the gate's exact meaning.
    """
    degree=S['h3_degree'];floor=S['h3_floor']
    ambient={(r,q):symbol(f'Hraw_{r}_{q}') for r in range(1,degree+1)
             for q in range(degree-r+1)}
    below=[(f'h3_D2_below_{r}_{q}',v) for (r,q),v in ambient.items() if weight((r,q))<floor]
    zero_map={row:sp.Integer(0) for _,row in below}
    assert all(substitute_map(row,zero_map)==0 for _,row in below)
    out=dict(S['h3_top']);variables=[]
    for r in range(1,degree+1):
        strict=[q for q in range(degree-r+1) if weight((r,q))>floor]
        if not strict: continue
        vmin=min(strict)
        for q in strict:
            v=symbol(f'Hc_{r}_{q}');variables.append(v)
            for j in range(q-vmin+1):
                out[(r,vmin+j)]=out.get((r,vmin+j),0)+v*comb(q-vmin,j)
    beta,ell=sp.symbols('beta ell')
    for pos,value in S['h3_equality'].items():
        image=value.subs({beta:1,ell:symbol('E82')})
        out[pos]=out.get(pos,0)+image
        variables.extend(sorted(image.free_symbols-set(variables),key=str))
    assert len(set(ambient.values())-set(zero_map))==len(variables)+1
    return {p:sp.expand(v) for p,v in out.items()},variables

def coefficient_box(name,degree,qcap,floor,start=1):
    """Emit all ambient coordinates and solve the strict-below scalar rows.

    At t=s^3,z=pi*s^4, distinct q label distinct powers of generic pi;
    coefficients cannot cancel. These are actual equations with leader 1.
    """
    allcoords={(r,q):symbol(f'{name}c_{r}_{q}') for r in range(start,degree+1)
               for q in range(min(qcap,degree-r)+1)}
    rows=[(f'{name}_D2_below_{r}_{q}',v) for (r,q),v in allcoords.items() if weight((r,q))<floor]
    solved={v:sp.Integer(0) for _,v in rows}
    images={p:v.xreplace(solved) for p,v in allcoords.items()}
    assert all(row.xreplace(solved)==0 for _,row in rows)
    kept={p:v for p,v in images.items() if v!=0}
    meta={'ambient_count':len(allcoords),'equation_count':len(rows),
          'equations_sha256':rows_hash(rows),'pivot_coefficient':'1',
          'solved_coordinates':sorted(map(str,solved)),
          'kept_count':len(kept),'floor':floor,'all_equations_rechecked':True}
    return kept,set(kept.values()),meta

def mul_weight(a,b,cut):
    out={}
    for (r,q),x in a.items():
        for (r1,q1),y in b.items():
            pos=(r+r1,q+q1)
            if weight(pos)<=cut: out[pos]=out.get(pos,0)+x*y
    return {p:sp.expand(v) for p,v in out.items() if v!=0}

@lru_cache(maxsize=None)
def inner_state(branch):
    start=time.monotonic()
    h,hvars=h3_template()
    hm,hfree,minor=MM.derive_minor_map(branch,h,hvars)
    # Keep the allowed equality coordinate itself free. The minor solver's
    # lexical pivot happens to choose E82; exchange it with Hc_8_3 by its
    # rational unit coefficient, without selecting a locus or spending a gauge.
    ell,exchange=symbol('E82'),symbol('Hc_8_3')
    old_rhs=hm[ell];leader=sp.diff(old_rhs,exchange)
    assert leader.is_Rational and leader!=0
    new_rhs=sp.expand((ell-(old_rhs-leader*exchange))/leader)
    hm={v:sp.expand(rhs.xreplace({exchange:new_rhs})) for v,rhs in hm.items() if v!=ell}
    hm[exchange]=new_rhs
    hm=resolve_map(hm)
    hfree=[v for v in hfree if v!=exchange]+[ell]
    minor=dict(minor,equality_coordinate_exchange={
        'kept_free':str(ell),'eliminated':str(exchange),'leader':str(leader),
        'rhs':str(new_rhs),'type':'invertible rational triangular coordinate change'})
    log(f'{branch} inner minor solved in {time.monotonic()-start:.2f}s')
    h={p:substitute_map(v,hm) for p,v in h.items()}
    h={p:v for p,v in h.items() if v!=0}
    C2,c2vars,c2meta=coefficient_box('C2',2*S['h3_degree'],S['h3_degree']-1,S['C2_floor'])
    C3,c3vars,c3meta=coefficient_box('C3',3*S['h3_degree'],S['h3_degree']-1,S['C3_floor'])
    cover,base,child=S['D1_substitution']
    multiplier=cover//WT[0]
    cutoff=(S['k2_D1_floor']-1)//multiplier
    low=tz_add(mul_weight(mul_weight(h,h,cutoff),h,cutoff),
               mul_weight(C2,h,cutoff),{p:v for p,v in C3.items() if weight(p)<=cutoff})
    log(f'{branch} inner low-weight product: {len(low)} slots, {time.monotonic()-start:.2f}s')
    beta=sp.Symbol('beta')
    equality={p:v.subs(beta,1) for p,v in S['k2_equality'].items()}
    positions=set(p for p in low if weight(p)<=S['k2_floor'])|set(equality)
    rows=[(f'K2_D2_{r}_{q}',sp.expand(low.get((r,q),0)-equality.get((r,q),0)))
          for r,q in sorted(positions)]
    # Def5.1 radius at the selected child: t=e^9,z=e^12(1+Pi*e).
    d1={}
    for (r,q),value in low.items():
        for k in range(q+1):
            exponent=cover*r+base*q+(child-base)*k
            if exponent<S['k2_D1_floor']:
                tag=(exponent,k)
                d1[tag]=d1.get(tag,0)+value*comb(q,k)
    rows += [(f'K2_D1_e{e}_k{k}',sp.expand(v)) for (e,k),v in sorted(d1.items())]
    allfree=set(hfree)|c2vars|c3vars
    localizer=symbol('rho' if branch=='delta2' else 'c')
    residue,mapping,pivots,zero=qstar_reduce(rows,allfree-{localizer})
    log(f'{branch} inner incidence reduced: {len(pivots)} pivots, {time.monotonic()-start:.2f}s')
    mapping=resolve_map(mapping)
    # C2/C3 and h3 remain explicit canonical polynomials, not output projections.
    def apply(tz): return {p:image for p,v in tz.items() if (image:=substitute_map(v,mapping))!=0}
    h,C2,C3=map(apply,(h,C2,C3))
    rechecked=[substitute_map(v,mapping) for _,v in rows]
    metadata={
        'h3_control':minor,'centre':minor,'h3_free':list(map(str,hfree)),
        'h3_map':encode_map(hm),'source_C2':c2meta,'source_C3':c3meta,
        'source_rows':len(rows),'source_raw_rows_hash':rows_hash(rows),
        'source_Qstar_pivots':[{'label':p.label,'variable':str(p.variable),'coefficient':str(p.coefficient),'rhs':str(mapping[p.variable])} for p in pivots],
        'source_map':encode_map(mapping),'source_residual_count':len(residue),
        'additional_rows':residue,'inner_dimension_before_residual':len(allfree-set(mapping)),
        'source_recheck_hash':rows_hash(list(zip((l for l,_ in rows),rechecked))),
        'basis':'explicit canonical C2,C3; h2=h3^3+C2*h3+C3',
        'build_seconds':time.monotonic()-start}
    log(f'{branch} inner: {len(allfree)} preincidence, {len(pivots)} QQ* pivots, {len(residue)} residual, {time.monotonic()-start:.2f}s')
    return h,C2,C3,allfree-set(mapping),metadata

def build_major_h2(branch,max_t):
    h,C2,C3,free,metadata=inner_state(branch)
    k2=tz_add(tz_mul(tz_mul(h,h,max_t),h,max_t),tz_mul(C2,h,max_t),
              {p:v for p,v in C3.items() if p[0]<=max_t})
    return k2,set(free),dict(metadata)

@lru_cache(maxsize=None)
def outer_state(max_offset):
    blocks={};allfree=set();pre={}
    for name,(degree,floor,threshold) in S['outer_specs'].items():
        coords,free,meta=coefficient_box(name,degree,S['outer_qcap'],floor,start=0)
        blocks[name]=coords;allfree |= free;pre[name]=meta
    cover,base,child=S['D1_substitution'];multiplier=cover//WT[0]
    mapping={};ledger=[]
    for offset in range(max_offset+1):
        rows=[]
        for name,(degree,floor,threshold) in S['outer_specs'].items():
            W=floor+offset
            for k in range(max(0,(threshold-multiplier*W+child-base-1)//(child-base))):
                row=sum(comb(q,k)*v for (r,q),v in blocks[name].items() if weight((r,q))==W and q>=k)
                rows.append((f'{name}_D1_s{offset}_k{k}',substitute_map(sp.expand(row),mapping)))
        residue,new,pivots,zero=qstar_reduce(rows,allfree-set(mapping))
        assert not residue
        mapping.update(new);mapping=resolve_map(mapping)
        ledger.append({'offset':offset,'rows':len(rows),'Qstar_pivots':len(pivots),
                       'row_hash':rows_hash(rows),'pivot_variables':[str(p.variable) for p in pivots]})
    blocks={name:{p:substitute_map(v,mapping) for p,v in block.items()} for name,block in blocks.items()}
    return blocks,allfree-set(mapping),{'preblocks':pre,'D1_offsets':ledger,
             'D1_cumulative_pivots':len(mapping),'outer_free_count':len(allfree-set(mapping)),
             'map':encode_map(mapping),'derived_specs':S['outer_specs']}

def outer_effective_tz(outer,name,max_t):
    return {(r+1,q):v for (r,q),v in outer[name].items() if r+1<=max_t and v!=0}

def build_FG(k2,outer,max_t):
    sq=tz_mul(k2,k2,max_t)
    F=tz_add(tz_mul(sq,k2,max_t),tz_mul(outer_effective_tz(outer,'A2',max_t),k2,max_t),outer_effective_tz(outer,'A3',max_t))
    G=tz_add(sq,tz_mul(outer_effective_tz(outer,'B1',max_t),k2,max_t),outer_effective_tz(outer,'B2',max_t))
    return F,G

def local_rows(item,branch,max_power,exact_only=True): return MM.local_rows(item,branch,max_power,exact_only)
def minor_series(branch): return MM.branch_data(branch)['w_terms']
def minor_pole_targets(branch):
    P,proof=MM.derive_minor_face(branch);zeta=symbol('zeta')
    return {name:(S['minor'][branch][name+'_local_floor'],{q[0]:v for q,v in sp.Poly(sp.expand(P**(degree//S['h3_degree'])),zeta).terms()})
            for name,degree in (('F',S['n']),('G',S['m']))}

@lru_cache(maxsize=None)
def raw_minor_support(branch,name):
    """All nonzero scalar labels from the full total-degree box and centres.

    Retain equality labels for target subtraction; equality is never zeroed.
    Constant-centre selections introduce labels already present lower in the
    triangular total-degree box. The direct emitter also checks every image.
    """
    data=S['minor'][branch]
    cover=data['cover'];generic=int(cover*data['radius_z'])
    floor=data[name+'_local_floor']
    return {n:tuple(k for k in range((n-cover)//generic+1) if (n-generic*k)%cover==0)
            for n in range(1,floor+1)
            if any((n-generic*k)%cover==0 for k in range((n-cover)//generic+1))}
def raw_minor_tags(branch,name,power): return raw_minor_support(branch,name).get(power,())

def stage_spec(branch,stage):
    """Historical synchronization convention, with all powers source-derived."""
    cover=S['minor'][branch]['cover']
    local_power=4*cover+stage
    top_J_degree=S['n']+S['m']-2
    first_k=S['outer_power_F']*S['inner_power']*S['h3_minor']
    if stage==0:
        jac={'t_power':1,'degree':top_J_degree-1,'w_powers':[first_k]}
    elif stage==1:
        jac={'t_power':1,'degree':top_J_degree-1,'w_powers':list(range(first_k+1,top_J_degree))}
    else:
        jac={'t_power':stage,'degree':top_J_degree-stage,'w_powers':list(range(top_J_degree-stage+1))}
    return {'stage':stage,'D1_offset':stage if stage<=7 else None,
            'pole_local_power':local_power,
            'pole_exponents':{name:local_power-S['minor'][branch][name+'_local_floor'] for name in ('F','G')},
            'jacobian':jac}

def cumulative_rows(branch,stage,KF,KG):
    # The historical finite schedule lies strictly below the nonzero faces.
    # Patch only dependency calls, so arithmetic labels remain comparable.
    previous=(E.local_rows,E.stage_spec,E.raw_minor_tags)
    try:
        E.local_rows=local_rows
        E.stage_spec=stage_spec;E.raw_minor_tags=raw_minor_tags
        return E.cumulative_rows(branch,stage,KF,KG)
    finally: E.local_rows,E.stage_spec,E.raw_minor_tags=previous

def run(branch,stage,out=None):
    """Finite compatibility schedule only; deep drivers subtract endpoint faces."""
    if not isinstance(stage,int) or not 0 <= stage <= 8:
        raise ValueError('engine.run supports the finite schedule 0..8 only; '
                         'use the deep drivers for later rows and nonzero endpoint targets')
    start=time.monotonic()
    st=stage_spec(branch,stage)
    cap=max(stage if stage>=2 else 1,(st['pole_local_power']+MM.branch_data(branch)['denominator']-1)//MM.branch_data(branch)['denominator'],4)
    k2,inner,major=build_major_h2(branch,cap)
    outer,ofree,ometa=outer_state(min(stage,7))
    log(f'{branch} stage{stage}: building F/G at t<={cap}')
    F,G=build_FG(k2,outer,cap)
    log(f'{branch} stage{stage}: F/G {len(F)}/{len(G)}; emitting rows')
    rows,counts=cumulative_rows(branch,stage,F,G)
    rows=list(major['additional_rows'])+rows
    log(f'{branch} stage{stage}: reducing {len(rows)} rows')
    free=inner|ofree;loc=symbol('rho' if branch=='delta2' else 'c')
    residual,mapping,pivots,zero=qstar_reduce(rows,free-{loc})
    if out is not None: out=Path(out)
    singular=singular_dimension(residual,branch,out.with_suffix('.sing') if out else None)
    dim=-1 if singular['unit_ideal'] else len(free-set(mapping))-singular['codimension']
    major=dict(major);major['additional_rows']=[(l,str(v)) for l,v in major['additional_rows']]
    result={'branch':branch,'stage':stage,'cap':cap,'engine_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'source':jsonable(S),'major':major,'outer':ometa,'row_accounting':counts,
        'row_count':len(rows),'raw_row_hash':rows_hash(rows),'Qstar_pivots':len(pivots),
        'joint_map':encode_map(mapping),'pivot_ledger':[{'label':p.label,'variable':str(p.variable),'coefficient':str(p.coefficient)} for p in pivots],
        'residual_count':len(residual),'residual_rows':[(l,str(v)) for l,v in residual],
        'residual_hash':rows_hash(residual),'singular':singular,'dimension':dim,
        'free_before':sorted(map(str,free)),'free_after':sorted(map(str,free-set(mapping))),
        'elapsed_seconds':time.monotonic()-start,
        'verdict':'DEAD-CANDIDATE' if dim==-1 else 'FINITE-CHART-NONUNIT'}
    if out: out.write_text(json.dumps(jsonable(result),indent=2,sort_keys=True)+'\n')
    return result

# Output serialization repair: exact integer representatives preserve every
# rational polynomial ideal; reject parser errors before reading dimensions.
# This affects Singular I/O only, not any source coefficient or equation.
from deep_safe_singular import singular_dimension as singular_dimension

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--branch',required=True,choices=['delta2','delta52']);p.add_argument('--stage',type=int,default=0);p.add_argument('--out',type=Path);a=p.parse_args()
    r=run(a.branch,a.stage,a.out);print(json.dumps({k:r[k] for k in ('branch','stage','dimension','Qstar_pivots','residual_count','elapsed_seconds','verdict')},indent=2))
