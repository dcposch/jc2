#!/usr/bin/env python3
"""Resume with exact derived-face graph coordinates from a complete saved minor phase.

This uses the entire saved graph map and residual; it never reconstructs an
antecedent by removing solved keys. Only monomial positions that contribute
to the requested D1 equality coefficient or actual origin jet are evaluated.
Unused coefficient coordinates stay in the declared ring and saved locus.
A unit after adding a necessary row is valid independently of later pole
implication checks. Frozen source snapshots are imported without modification.
"""
from __future__ import annotations
import argparse,hashlib,json,sys,time
from pathlib import Path
import sympy as sp
sys.dont_write_bytecode=True


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--code',type=Path,required=True)
    ap.add_argument('--checkpoint',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--phase',choices=['d1','corner','both'],default='both')
    args=ap.parse_args()
    args.code=args.code.resolve();args.checkpoint=args.checkpoint.resolve();args.output=args.output.resolve()
    sys.path.insert(0,str(args.code))
    import deep_gauge_accelerated as G
    import engine as E
    import deep_driver as D
    import deep_rows as R
    import importlib.util
    safe_path=Path(__file__).resolve().with_name('deep_safe_singular.py')
    safe_spec=importlib.util.spec_from_file_location('safe_singular',safe_path)
    safe=importlib.util.module_from_spec(safe_spec);safe_spec.loader.exec_module(safe)
    E.singular_dimension=safe.singular_dimension
    from source_data import SOURCE as S,jsonable
    from d1_jacobian_face import d1_face_jacobian
    begin=time.monotonic()
    log=lambda message:print(message,flush=True)
    saved=json.loads(args.checkpoint.read_text())
    branch=saved['branch']
    assert saved['phase'].startswith('accelerated_FG_targets_local'),saved['phase']
    log(f'{branch}: loading complete checkpoint {args.checkpoint.name}')
    mapping={sp.Symbol(v):sp.sympify(value) for v,value in saved['map_after'].items()}
    free={sp.Symbol(v) for v in saved['free_after']}|set(mapping)
    residual=[(label,sp.sympify(value)) for label,value in saved['residual_after']]
    assert E.rows_hash(residual)==saved['residual_after_hash']
    assert all(not (value.free_symbols & set(mapping)) for value in mapping.values()),'checkpoint graph is not resolved'
    h,C2,C3,inner,meta=E.inner_state(branch)
    outer,outerfree,outermeta=E.outer_state(-1)
    assert free==set(inner)|set(outerfree),'saved ring differs from frozen source ring'
    phaseprefix=args.checkpoint.name.rsplit('_phase',1)[0]
    chain=[path for path in sorted(args.checkpoint.parent.glob(phaseprefix+'_phase*.json')) if path.name<=args.checkpoint.name]
    # Full chain remains linked, including every exact scalar pivot and radical identity.
    records={'branch':branch,'type':'EXACT-Q SOURCE GAUGE LOCUS; COVERAGE REQUIRES T_q ISOMORPHISM AUDIT',
        'checkpoint':str(args.checkpoint),'checkpoint_sha256':hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
        'checkpoint_phase':saved['phase'],'checkpoint_chain':[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in chain],
        'code_directory':str(args.code),'code_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(args.code.glob('*.py'))},
        'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'initial_free':len(free-set(mapping)),'initial_residual_count':len(residual),
        'source_gauge':meta['gauge_slice'],'phases':[],
        'dependency_cut':'Only coefficient extraction dependencies are evaluated; no unknown is dropped from the locus.',
        'proof_scope':'All saved rows are necessary; a unit after a necessary face row does not require uncomputed row implications.'}
    loc=sp.Symbol(saved['localizer'])
    jc,zj=sp.symbols('Jc ZJ')
    free.update({jc,zj})
    def write():
        records['elapsed_seconds']=time.monotonic()-begin
        args.output.write_text(json.dumps(jsonable(records),indent=2,sort_keys=True)+'\n')
    write()
    def coefficient_image(value):
        return E.substitute_map(sp.sympify(value),mapping)
    def mapped_positions(poly,predicate):
        return {pos:image for pos,value in poly.items() if predicate(pos) and (image:=coefficient_image(value))!=0}
    def add(rows,name,derivation,protected=frozenset()):
        nonlocal mapping,residual
        log(f'{branch}: {name}, {len(rows)} equations, operation counts {[int(sp.count_ops(v)) for _,v in rows]}')
        current=[(label,coefficient_image(value)) for label,value in rows]
        certificate={'phase':name,'branch':branch,'field':'Q','localizer':str(loc),
            'free_before':sorted(map(str,free-set(mapping))),'map_before':E.encode_map(mapping),
            'residual_before':D.encoded_rows(residual),'raw_new_rows_before_reduction':D.encoded_rows(current),
            'raw_new_rows_hash':E.rows_hash(current),'pivot_steps':[],'radical_steps':[]}
        pending=residual+current
        while True:
            remaining,new,pivots,zeros=E.qstar_reduce(pending,free-set(mapping)-{loc}-set(protected))
            if new:
                mapping.update(new);mapping=E.resolve_map(mapping)
                certificate['pivot_steps'].extend({'label':p.label,'variable':str(p.variable),
                    'rational_leader':str(p.coefficient),'rhs_at_pivot':str(p.rhs),
                    'selected_equation_at_pivot':str(sp.expand(p.coefficient*(p.variable-p.rhs)))} for p in pivots)
            residual=remaining
            roots,certs=R.pure_power_radical_rows(residual)
            eligible=free-set(mapping)-{loc}-set(protected)
            roots=[(label,row) for label,row in roots if any(sp.diff(row,v).is_Rational and sp.diff(row,v)!=0 for v in row.free_symbols&eligible)]
            if not roots:break
            kept={label for label,_ in roots}
            certificate['radical_steps'].extend(dict(c,source_polynomial=str(dict(residual)[c['source_row']])) for c in certs if c['new_row'] in kept)
            pending=residual+roots
        certificate.update({'map_after':E.encode_map(mapping),'free_after':sorted(map(str,free-set(mapping))),
                            'residual_after':D.encoded_rows(residual),'residual_after_hash':E.rows_hash(residual)})
        phasepath=args.output.with_name(args.output.stem+'_'+name+'_phase.json')
        phasepath.write_text(json.dumps(jsonable(certificate),indent=2,sort_keys=True)+'\n')
        sing=E.singular_dimension(residual,branch,args.output.with_name(args.output.stem+'_'+name+'.sing'))
        dimension=-1 if sing['unit_ideal'] else len(free-set(mapping))-sing['codimension']
        point,pmeta=D.rational_candidate(residual,free,mapping,branch)
        if point is not None:
            assert all(sp.expand(row.xreplace(point))==0 for _,row in current)
            assert all(sp.expand(row.xreplace(point))==0 for _,row in residual)
            pmeta['new_phase_raw_rows_verified']=len(current)
            pmeta['prior_locus']='by complete saved QQ* graph and radical certificates; not remapped through every old raw generator in this harness'
        record={'name':name,'dimension':dimension,'unit_ideal':sing['unit_ideal'],'singular':sing,
                'phase_certificate':str(phasepath),'phase_certificate_sha256':hashlib.sha256(phasepath.read_bytes()).hexdigest(),
                'derivation':derivation,'rational_point':pmeta,'remaining_free':len(free-set(mapping)),
                'residual_count':len(residual),'elapsed_seconds':time.monotonic()-begin}
        records['phases'].append(record);records['unit_ideal']=sing['unit_ideal'];write()
        log(f'{branch}: {name} complete, dimension={dimension}, residual={len(residual)}')
        return sing['unit_ideal']
    if args.phase in ('d1','both'):
        log(f'{branch}: extracting only D1 coefficient dependencies')
        ratio=S['D1_substitution'][0]//S['D2_weight'][0]
        cutoff=S['k2_D1_floor']//ratio
        # h3floor is also fixed by its degree and printed D2 valuation in the source object.
        hfloor=min(E.weight(pos) for pos,value in h.items() if value!=0)
        assert hfloor==S.get('h3_floor',hfloor)
        hs=mapped_positions(h,lambda p:E.weight(p)<=cutoff-2*hfloor)
        cs2=mapped_positions(C2,lambda p:E.weight(p)<=cutoff-hfloor)
        cs3=mapped_positions(C3,lambda p:E.weight(p)<=cutoff)
        cover,base,child=S['D1_substitution'];step=child-base
        def contributes(pos,threshold):
            r,q=pos;gap=threshold-cover*r-base*q
            return gap%step==0 and 0<=gap//step<=q
        os={name:mapped_positions(poly,lambda p,n=name:contributes(p,S['outer_specs'][n][2])) for name,poly in outer.items()}
        log(f'{branch}: dependency positions h/C2/C3={len(hs)}/{len(cs2)}/{len(cs3)}, outer={[len(p) for p in os.values()]}')
        from d1_jacobian_face import extract_face
        low=E.tz_add(E.mul_weight(E.mul_weight(hs,hs,cutoff),hs,cutoff),
                     E.mul_weight(cs2,hs,cutoff),cs3)
        extracted={'H2':extract_face(low,S['k2_D1_floor'])}
        extracted.update({name:extract_face(poly,S['outer_specs'][name][2]) for name,poly in os.items()})
        Pi=sp.Symbol('Pi'); graphfaces={};graphrows=[];graphvars=set()
        for name,poly in extracted.items():
            terms={}
            for (power,),value in sp.Poly(poly,Pi).terms():
                if value.is_Rational:
                    terms[power]=value
                else:
                    variable=sp.Symbol(f'Zface_{name}_{power}')
                    graphvars.add(variable);free.add(variable)
                    graphrows.append((f'derived_D1_graph_{name}_Pi{power}',variable-value))
                    terms[power]=variable
            graphfaces[name]=sum(value*Pi**power for power,value in terms.items())
        graphmeta={'derived_faces':{name:str(poly) for name,poly in extracted.items()},
                   'graph_faces':{name:str(poly) for name,poly in graphfaces.items()},
                   'meaning':'Zface equals the extracted coefficient; every equation is a graph definition, no pin or restriction',
                   'protected_during_graph_elimination':sorted(map(str,graphvars))}
        if add(graphrows,'D1_graph',graphmeta,protected=graphvars):return
        import importlib.util
        compression_path=Path(__file__).resolve().with_name('print-audit-d1-compression.py')
        compression_spec=importlib.util.spec_from_file_location('source_d1_compression',compression_path)
        compression=importlib.util.module_from_spec(compression_spec);compression_spec.loader.exec_module(compression)
        rows,fmeta=compression.coefficient_rows(*(graphfaces[n] for n in ('H2','A2','A3','B1','B2')),jc=jc,expand=True)
        fmeta.update({'compression_helper':str(compression_path),'compression_helper_sha256':hashlib.sha256(compression_path.read_bytes()).hexdigest(),
                      'source':'Moh p179 Def5.1(4), p170 Prop4.6 r=1; exact derived face coefficient graph'})
        fmeta['dependency_cuts']={'h3_max_weight':cutoff-2*hfloor,'C2_max_weight':cutoff-hfloor,'C3_max_weight':cutoff,
            'outer':'exact binomial equality contributors only','h3_minimum_weight_used':hfloor}
        rows.append(('gauge_J_nonzero_wrapper',zj*jc-1))
        if add(rows,'D1_J',fmeta):return
    if args.phase in ('corner','both'):
        def cornerpoly(poly,degree):
            allowed={(degree,0),(degree-1,0),(degree-1,1)}
            return mapped_positions(poly,lambda p:p in allowed)
        hs=cornerpoly(h,S['h3_degree']);cs2=cornerpoly(C2,2*S['h3_degree']);cs3=cornerpoly(C3,S['inner_power']*S['h3_degree'])
        os={name:cornerpoly(poly,S['outer_specs'][name][0]) for name,poly in outer.items()}
        value,jets=G.corner_from_blocks(hs,cs2,cs3,os)
        rows=[('gauge_early_J_constant',value-jc)]
        if args.phase=='corner':rows.append(('gauge_J_nonzero_wrapper',zj*jc-1))
        add(rows,'corner_J',{'constant_polynomial':str(value),'actual_polynomial_jets':jets,
            'coefficient_dependencies':'normalized positions (D,0),(D-1,0),(D-1,1)',
            'direct_derivative_control':G.corner_control()})
    records['final']=True;write()

if __name__=='__main__':main()
