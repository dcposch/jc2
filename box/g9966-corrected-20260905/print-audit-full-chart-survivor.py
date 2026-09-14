#!/usr/bin/env python3
"""Complete rational certificates for the positive-Jacobian necessary chart.

All coefficient unknowns belong to full canonical remainder boxes. At each
certified inner point set ALL outer coefficients to zero. Explicit rational
polynomials reconstruct F=h2^3,G=h2^2; every positive-degree Jacobian row is
then identically zero by the polynomial product rule. The constant is recorded
as zero. Nonvanishing of that constant is a SEPARATE stronger instrument.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from pathlib import Path
from math import comb
from fractions import Fraction as Q
from collections import defaultdict
import sympy as sp
import engine as E
import minor_maps as MM
import deep_point_scan as D
from source_data import SOURCE as S,jsonable

HERE=Path(__file__).resolve().parent

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def allbox(degree,qcap=None,start=0):
    if qcap is None:qcap=degree
    return [(r,q) for r in range(start,degree+1) for q in range(min(qcap,degree-r)+1)]
def row_hash(rows):return hashlib.sha256(''.join(f'{l}\t{v}\n' for l,v in rows).encode()).hexdigest()
def poly_hash(poly):return row_hash([(f'{r},{q}',v) for (r,q),v in sorted(poly.items())])
def powered(poly,power,cut):
    out={(0,0):Q(1)}
    for _ in range(power):out=D.mul(out,poly,cut)
    return out

def pull_d1(poly,positions,threshold):
    cover,base,child=S['D1_substitution'];tags=set();images=defaultdict(Q)
    for r,q in positions:
        for k in range(q+1):
            e=cover*r+base*q+(child-base)*k
            if e<threshold:tags.add((e,k))
    for (r,q),v in poly.items():
        for k in range(q+1):
            e=cover*r+base*q+(child-base)*k
            if e<threshold:images[e,k]+=v*comb(q,k)
    assert set(images)<=tags
    return {key:images[key] for key in sorted(tags)}

def pole_tags(branch,floor,qcap):
    data=S['minor'][branch];L=data['cover'];g=int(L*data['radius_z'])
    return [(n,k) for n in range(1,floor+1)
            for k in range(min(qcap,(n-L)//g)+1) if (n-g*k)%L==0]

def run(branch):
    started=time.monotonic();prefix=HERE/f'print-audit-full-chart-survivor-{branch}'
    custody={p.name:sha(p) for p in [Path(__file__),HERE/'engine.py',HERE/'source_data.py',HERE/'minor_maps.py',HERE/'deep_point_scan.py',HERE/'frozen/band_engine.py']}
    point_file=HERE/f'print-audit-inner-minor-{branch}.json';point_data=json.loads(point_file.read_text())
    h,c2,c3,free,meta=E.inner_state(branch)
    assignment={v:sp.Integer(0) for v in free}
    assignment.update({sp.Symbol(v):sp.Rational(x) for v,x in point_data['native_trial_nonzero'].items()})
    assert set(assignment)==set(free)
    h,c2,c3=map(lambda p:D.specialize(p,assignment),(h,c2,c3))
    for name,poly,degree,start,qcap in [('h3',h,S['h3_degree'],0,S['h3_degree']),('C2',c2,S['inner_normalization_degrees']['C2'],1,S['inner_qcap']),('C3',c3,S['inner_normalization_degrees']['C3'],1,S['inner_qcap'])]:
        assert set(poly)<=set(allbox(degree,qcap,start)),(name,'outside canonical box')
    hcube=powered(h,S['inner_power'],S['k2_degree'])
    k2=D.add(hcube,D.mul(c2,h,S['k2_degree']),c3)
    assert set(k2)<=set(allbox(S['k2_degree']))
    quotient,remainder=D.monic_z_division(D.add(k2,D.scale(hcube,Q(-1))),h)
    assert quotient==c2 and remainder==c3
    # Entire global polynomials, without truncating their degree boxes.
    F=powered(k2,S['outer_power_F'],S['n']);G=powered(k2,S['outer_power_G'],S['m'])
    assert set(F)<=set(allbox(S['n'])) and set(G)<=set(allbox(S['m']))
    print('POLYNOMIALS',branch,len(F),len(G),round(time.monotonic()-started,2),flush=True)
    rows=[];groups={}
    def group(name,items):
        items=[(label,Q(value)) for label,value in items]
        bad=[(label,str(value)) for label,value in items if value]
        assert not bad,(branch,name,bad[:4])
        groups[name]={'row_count':len(items),'all_zero':True,'row_images_sha256':row_hash(items)}
        rows.extend(items)
    wt,wq=S['D2_weight']
    # Full top polynomials; every represented coefficient is checked.
    htop={p:Q(int(v),1) for p,v in S['h3_top'].items()}
    group('h3_top',[(f'h3_top_q{q}',h.get((0,q),0)-htop.get((0,q),0)) for q in range(S['h3_degree']+1)])
    for name,poly,powr,degree in [('K2',k2,S['inner_power'],S['k2_degree']),('F',F,S['n']//S['h3_degree'],S['n']),('G',G,S['m']//S['h3_degree'],S['m'])]:
        top=powered(htop,powr,0)
        group(name+'_top',[(f'{name}_top_q{q}',poly.get((0,q),0)-top.get((0,q),0)) for q in range(degree+1)])
    for name,poly,degree,qcap,start,floor in [('h3',h,S['h3_degree'],S['h3_degree'],1,S['h3_floor']),('C2',c2,S['inner_normalization_degrees']['C2'],S['inner_qcap'],1,S['C2_floor']),('C3',c3,S['inner_normalization_degrees']['C3'],S['inner_qcap'],1,S['C3_floor']),('K2',k2,S['k2_degree'],S['k2_degree'],0,S['k2_floor'])]:
        group(name+'_D2_strict',[(f'{name}_D2_below_r{r}_q{q}',poly.get((r,q),0)) for r,q in allbox(degree,qcap,start) if wt*r+wq*q<floor])
    beta,ell=sp.symbols('beta ell');source_point={beta:sp.Integer(1),ell:assignment[sp.Symbol('E82')]}
    for name,poly,face,floor,degree in [('h3',h,S['h3_face'],S['h3_floor'],S['h3_degree']),('K2',k2,S['k2_face'],S['k2_floor'],S['k2_degree'])]:
        face=sp.Poly(sp.expand(face.xreplace(source_point)),sp.Symbol('pi'))
        images=defaultdict(Q)
        for (r,q),v in poly.items():
            if wt*r+wq*q==floor:images[q]+=v
        group(name+'_D2_face',[(f'{name}_D2_face_q{q}',images[q]-Q(str(face.coeff_monomial(sp.Symbol('pi')**q)))) for q in range(degree+1)])
    d1=pull_d1(k2,allbox(S['k2_degree']),S['k2_D1_floor'])
    group('K2_D1',[(f'K2_D1_e{e}_k{k}',v) for (e,k),v in d1.items()])
    # All outer ambient coefficients are explicitly assigned zero, including
    # the coordinates later removed by source equations or rational pivots.
    outer_counts={};outer_offset_rows=defaultdict(list)
    for name,(degree,floor,threshold) in S['outer_specs'].items():
        positions=allbox(degree,S['outer_qcap']);outer_counts[name]=len(positions)
        group(name+'_D2_strict',[(f'{name}_D2_below_r{r}_q{q}',0) for r,q in positions if wt*r+wq*q<floor])
        images=pull_d1({},positions,threshold)
        group(name+'_D1',[(f'{name}_D1_e{e}_k{k}',v) for (e,k),v in images.items()])
        for offset in range(8):
            W=floor+offset
            for k in range(max(0,threshold-3*W)):
                outer_offset_rows[offset].append((f'{name}_D1_s{offset}_k{k}',Q(0)))
    # Pull back ALL source-polynomial coefficients before multiplying local
    # images. Composition is a ring homomorphism; no omitted higher H term
    # can enter the F/G ceilings once its verified local minimum is known.
    L,wseries=D.local_series(branch,assignment)
    hfloor=S['minor'][branch]['h3_local_floor'];kfloor=S['inner_power']*hfloor
    P,_=MM.derive_minor_face(branch);P=sp.Poly(sp.expand(P.xreplace(assignment)),sp.Symbol('zeta'))
    htarget={(hfloor,k[0]):Q(str(v)) for k,v in P.terms()}
    lh=D.compose_local(h,L,wseries,hfloor)
    group('h3_minor',[(f'h3_minor_n{n}_k{k}',lh.get((n,k),0)-htarget.get((n,k),0)) for n in range(hfloor+1) for k in range(S['h3_degree']+1)])
    for name,poly,mult in [('C2',c2,2),('C3',c3,S['inner_power'])]:
        floor=mult*hfloor;local=D.compose_local(poly,L,wseries,floor-1)
        tags=pole_tags(branch,floor-1,S['inner_qcap'])
        assert set(local)<=set(tags)
        group(name+'_minor',[(f'{name}_minor_n{n}_k{k}',local.get((n,k),0)) for n,k in tags])
    lk2=D.compose_local(k2,L,wseries,kfloor)
    ktarget=powered(htarget,S['inner_power'],kfloor)
    assert lk2==ktarget
    ktags=sorted(set(pole_tags(branch,kfloor,S['k2_degree']-1))|set(lk2)|set(ktarget))
    group('K2_minor',[(f'K2_minor_n{n}_k{k}',lk2.get((n,k),0)-ktarget.get((n,k),0)) for n,k in ktags])
    for name,mult in [('A2',2),('A3',S['outer_power_F']),('B1',1),('B2',S['outer_power_G'])]:
        effective_floor=mult*kfloor;unshifted_floor=effective_floor-L
        tags=pole_tags(branch,unshifted_floor-1,S['outer_qcap'])
        group(name+'_minor',[(f'{name}_minor_n{n}_k{k}',0) for n,k in tags])
    full_pole_images={};pole_records=[];raw_pole_counts={};extra_top_face_counts={}
    for name,power,degree in [('F',S['outer_power_F'],S['n']),('G',S['outer_power_G'],S['m'])]:
        floor=S['minor'][branch][name+'_local_floor']
        # Exact power of the full-degree h2 local image truncated ONLY after
        # proving h2's strict pole rows. This equals full F/G pullback to floor.
        image=powered(lk2,power,floor)
        target=powered(htarget,degree//S['h3_degree'],floor)
        rawtags=pole_tags(branch,floor,degree-1)
        tags=sorted(set(rawtags)|set(image)|set(target))
        raw_pole_counts[name]=len(rawtags)
        extra_top_face_counts[name]=len(tags)-len(rawtags)
        # The fixed top contributes the maximum generic-power leader, which
        # has no lower-coefficient raw tag. Check it explicitly as well.
        actual=[(f'{name}_local{n}_coord{k}',image.get((n,k),0)-target.get((n,k),0)) for n,k in tags]
        group(name+'_minor_full_poles',actual)
        for (n,k),(_,v) in zip(tags,actual):full_pole_images[name,n,k]=v
        for n in range(1,floor+1):
            band=[(l,v) for (nn,k),(l,v) in zip(tags,actual) if nn==n]
            if band:pole_records.append({'name':name,'local_power':n,'rows':len(band),'all_zero':True,'row_images_sha256':row_hash(band)})
    # Exact symbolic product-rule identity, independent of sparse J emitter.
    H,Hx,Hy=sp.symbols('H Hx Hy')
    Jidentity=sp.expand((3*H**2*Hx)*(2*H*Hy)-(3*H**2*Hy)*(2*H*Hx))
    assert Jidentity==0
    maxJ=S['n']+S['m']-2
    jacrows=[(f'J_t{r}_degree{maxJ-r}_w{k}',0) for r in range(maxJ) for k in range(maxJ-r+1)]
    group('all_positive_degree_J',jacrows)
    loc='rho' if branch=='delta2' else 'c';locvalue=Q(str(assignment[sp.Symbol(loc)]));inverse=1/locvalue
    group('branch_localization',[(f'Z{loc}*{loc}-1',inverse*locvalue-1)])
    # Every historical stage is explicitly re-evaluated from the complete
    # independent pole coefficient table and product-rule J identity.
    stages=[];prior=[1,2,3] if L==1 else [2,4,6]
    cumulative=[]
    for name in ('F','G'):
        for n in prior:
            for k in E.raw_minor_tags(branch,name,n):cumulative.append((f'prior_{name}_local{n}_coord{k}',full_pole_images[name,n,k]))
    cumulative += [(f'prior_J_d162_k{k}',Q(0)) for k in range(17,27)]
    for stage in range(9):
        spec=E.stage_spec(branch,stage);n=spec['pole_local_power'];new=[]
        for name in ('F','G'):
            for k in E.raw_minor_tags(branch,name,n):new.append((f'stage{stage}_{name}_local{n}_coord{k}',full_pole_images[name,n,k]))
        js=spec['jacobian'];new += [(f"stage{stage}_J_d{js['degree']}_k{k}",Q(0)) for k in js['w_powers']]
        cumulative+=new
        assert all(v==0 for _,v in cumulative)
        stages.append({'stage':stage,'new_schedule_rows':len(new),'cumulative_schedule_rows':len(cumulative),'D1_offset':spec['D1_offset'],'D1_rows_at_offset':len(outer_offset_rows.get(stage,[])),'all_rows_satisfied':True,'new_images_sha256':row_hash(new),'cumulative_images_sha256':row_hash(cumulative)})
    # Independent negative global-J control: B1(0,32)=1 means deltaG=L^32 H.
    # For Htop=y^9 L^24, product differentiation gives 864*y^35*L^127.
    a=S['inner_power']*S['h3_minor'];b=S['inner_power']*S['h3_major'];qcap=S['outer_qcap'];fp=S['outer_power_F']
    factor=fp*a*qcap;yexp=(fp+1)*a-1;lexp=(fp+1)*b+qcap-1
    negative_value=factor*((-1)**lexp)
    assert negative_value==-864 and yexp==35
    sk2={p:sp.Rational(v.numerator,v.denominator) for p,v in k2.items() if p[0]<=1}
    perturbed_outer={name:{} for name in S['outer_specs']};perturbed_outer['B1']={(0,qcap):sp.Integer(1)}
    f1,g1=E.build_FG(sk2,perturbed_outer,1)
    direct_negative=E.jacobian_band(f1,g1,1)[yexp]
    assert direct_negative==negative_value
    # Custody of the old gate point controls: original source-inverse failure
    # and later diagnostic pole failure are preserved, never renamed as the
    # new rational point. Their stored exact drivers remain independently runnable.
    gate_path=HERE/f'deep_diagnostic_point_{branch}.json';gate=json.loads(gate_path.read_text())
    gate_control={'artifact':str(gate_path),'sha256':sha(gate_path),'original_assignment':gate['nonzero_assignment'],'first_source_failure':gate['inverse_K2_output_to_C2_C3'],'later_diagnostic_pole_failure':gate['first_pole_failure'],'independent_gate_depth_control':gate['independent_local_emitter_control']}
    raw_text=''.join(f'{l}\t{v}\n' for l,v in rows)
    prefix.with_suffix('.rows.tsv').write_text(raw_text)
    point_payload=''.join(f'{v}={assignment[v]}\n' for v in sorted(assignment,key=str))
    certificate={'branch':branch,'verdict':'SURVIVOR_OF_FULL_POSITIVE_JACOBIAN_NECESSARY_CHART',
        'scope':'All canonical source/D2/D1/minor/remainder rows and EVERY positive-degree global Jacobian coefficient; the Jacobian constant is recorded0 and is not localized in this certificate.',
        'coefficient_field':'QQ','canonical_polynomial_maps':{'K2':'K3^3+C2_normalized*K3+C3_normalized','KF':'K2^3','KG':'K2^2','all_outer_coefficients':'0'},
        'source_inner_coordinate_count':len(free),'all_outer_ambient_coordinate_count':sum(outer_counts.values()),'outer_ambient_counts':outer_counts,
        'inner_nonzero_assignment':{str(v):str(x) for v,x in assignment.items() if x!=0},'every_other_inner_coordinate':'0','point_generator_sha256':hashlib.sha256(point_payload.encode()).hexdigest(),
        'point_input_artifact':str(point_file),'point_input_sha256':sha(point_file),'source_engine_inner_dimension':meta['inner_dimension_before_residual'],
        'polynomials':{'K3':D.polynomial_record(h),'C2_normalized':D.polynomial_record(c2),'C3_normalized':D.polynomial_record(c3),'K2':D.polynomial_record(k2)},
        'full_global_polynomial_coefficients':{'KF':len(F),'KG':len(G)},'full_global_polynomial_sha256':{'KF':poly_hash(F),'KG':poly_hash(G)},
        'every_polynomial_total_degree_box_verified':True,'exact_monic_C2_C3_inverse_verified':True,
        'source_and_row_groups':groups,'all_row_count':len(rows),'all_rows_satisfied':True,'all_row_images_sha256':row_hash(rows),'row_images_file':str(prefix.with_suffix('.rows.tsv')),
        'finite_stages':stages,'raw_lower_pole_support_counts':raw_pole_counts,'additional_fixed_top_face_checks':extra_top_face_counts,'deep_pole_powers':pole_records,'positive_J_bands':[{'t_power':r,'global_degree':maxJ-r,'coefficient_count':maxJ-r+1,'all_zero':True} for r in range(maxJ)],
        'Jacobian_constant':{'normalized_t_power':maxJ,'global_degree':0,'value':'0','coefficient_computed_by_exact_product_rule':True,'nonzero_constant_instrument_is_separate':True},
        'product_rule_certificate':{'identity':str(Jidentity),'F':'H^3','G':'H^2','differentiation':'Fx=3H^2Hx,Fy=3H^2Hy,Gx=2HHx,Gy=2HHy','all_positive_coefficient_count':len(jacrows)},
        'negative_controls':{'B1_0_32_perturbation':{'global_J_t1_w35':str(direct_negative),'independent_top_derivative':f'{factor}*y^{yexp}*(y-x)^{lexp}','both_methods_agree':True},'branch_localizer_zero':{'localizer':loc,'Zvalue':'1','equation_value':'-1'},'nonzero_J_extension':{'Jc':'1','ZJ':'1','constant_equation_value':'-1','wrapper_equation_value':'0'}},
        'gate_point_controls':gate_control,'custody':custody,
        'inference_limits':['Point satisfies the entire declared positive-Jacobian necessary chart.','Point has J=0; it is not a Keller pair.','No dimension of the entire full-chart locus is inferred from this point.','No unit on a point restriction or pure-power locus is promoted to a branch kill.'],
        'elapsed_seconds':round(time.monotonic()-started,3)}
    prefix.with_suffix('.json').write_text(json.dumps(jsonable(certificate),indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:certificate[k] for k in ('branch','verdict','all_row_count','all_rows_satisfied','full_global_polynomial_coefficients','elapsed_seconds')},indent=2),flush=True)
    return certificate

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--branch',required=True,choices=['delta2','delta52']);a=ap.parse_args();run(a.branch)
