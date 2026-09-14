#!/usr/bin/env python3
"""Merge two certified necessary loci and exhaust remaining global J bands.

Both antecedents are preserved as complete checkpoint chains. A weak graph
relation x-map[x]=0 is adjoined only with its exact saved coordinate target;
no coordinate projection or restriction is inferred from a dimension. All
new bands are coefficients of the exact factored bracket after the affine
coordinate substitution z=w-1, which commutes with polynomial operations.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,json,re,subprocess,sys,time
from pathlib import Path
import sympy as sp
sys.dont_write_bytecode=True


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--code',type=Path,required=True)
    ap.add_argument('--weak-code',type=Path,required=True)
    ap.add_argument('--strong',type=Path,required=True)
    ap.add_argument('--strong-summary',type=Path,required=True)
    ap.add_argument('--weak',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--max-t',type=int,default=1000)
    ap.add_argument('--resume-state',type=Path)
    ap.add_argument('--batch-size',type=int,default=4)
    ap.add_argument('--timeout-seconds',type=float)
    args=ap.parse_args()
    for name in ('code','weak_code','strong','strong_summary','weak','output'):setattr(args,name,getattr(args,name).resolve())
    HERE=Path(__file__).resolve().parent
    sys.path.insert(0,str(args.code))
    import deep_gauge_accelerated as G
    import engine as E
    import deep_driver as D
    import deep_rows as R
    flint_spec=importlib.util.spec_from_file_location('exact_flint_jacobian',HERE/'deep_flint_jacobian_pair.py')
    flint_backend=importlib.util.module_from_spec(flint_spec);flint_spec.loader.exec_module(flint_backend)
    from source_data import SOURCE as S,jsonable
    spec=importlib.util.spec_from_file_location('safe_dimension',HERE/'deep_safe_singular.py')
    safe=importlib.util.module_from_spec(spec);spec.loader.exec_module(safe)
    E.singular_dimension=safe.singular_dimension
    begin=time.monotonic();log=lambda message:print(message,flush=True)
    strong=json.loads(args.strong.read_text());weak=json.loads(args.weak.read_text())
    summary=json.loads(args.strong_summary.read_text())
    branch=strong['branch'];assert weak['branch']==branch==summary['branch']
    mapping={sp.Symbol(v):sp.sympify(value) for v,value in strong['map_after'].items()}
    free=set(mapping)|{sp.Symbol(v) for v in strong['free_after']}
    residual=[(label,sp.sympify(value)) for label,value in strong['residual_after']]
    assert E.rows_hash(residual)==strong['residual_after_hash']
    assert all(not(value.free_symbols&set(mapping)) for value in mapping.values())
    loc=sp.Symbol(strong['localizer']);jc,zj=sp.symbols('Jc ZJ')
    assert jc in free and zj in free
    weakmap={sp.Symbol(v):sp.sympify(value) for v,value in weak['map_after'].items()}
    weakfree=set(weakmap)|{sp.Symbol(v) for v in weak['free_after']}
    assert weakfree<=free,'weak source ring is not contained in the strong graph ring'
    assert all(not(value.free_symbols&set(weakmap)) for value in weakmap.values())
    weakresidue=[(label,sp.sympify(value)) for label,value in weak['residual_after']]
    assert E.rows_hash(weakresidue)==weak['residual_after_hash']
    prefix=args.weak.name.rsplit('_phase',1)[0]
    weakchain=[p for p in sorted(args.weak.parent.glob(prefix+'_phase*.json')) if p.name<=args.weak.name]
    jphases=[]
    for path in weakchain:
        phase=json.loads(path.read_text())['phase']
        match=re.fullmatch(r'(?:deep|stage)(\d+)_Jacobian',phase)
        if match:jphases.append(int(match.group(1)))
    completed=max(jphases)
    assert completed>=9 and set(range(completed+1))<=set(jphases),'weak Jacobian prefix is incomplete'
    h,C2,C3,inner,meta=E.inner_state(branch);outer,outerfree,_=E.outer_state(-1)
    assert weakfree==set(inner)|set(outerfree)
    source_images={'h3':h,'C2':C2,'C3':C3,**outer}
    strong_payload={'field':'Q','branch':branch,'ordered_generators':sorted(map(str,set(inner)|set(outerfree))),
        'source_images':{name:[[r,q,str(sp.expand(value))] for (r,q),value in sorted(poly.items())] for name,poly in source_images.items()},
        'initial_residue':[(label,str(sp.expand(value))) for label,value in meta['additional_rows']],
        'outer_specs':jsonable(S['outer_specs']),'gauge':{'jet0':'0'}}
    weak_image_path=args.output.with_name(args.output.stem+'_weak_source_images.json')
    subprocess.run([sys.executable,str(HERE/'deep_source_image_control.py'),'--code',str(args.weak_code),
        '--branch',branch,'--output',str(weak_image_path)],check=True)
    weak_image=json.loads(weak_image_path.read_text())
    assert strong_payload==weak_image['payload'],'same named generators have different source images'
    image_sha=hashlib.sha256(json.dumps(strong_payload,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    assert image_sha==weak_image['payload_sha256']
    ring_transport={'field':'Q','ordered_generator_map':[[v,v] for v in strong_payload['ordered_generators']],
        'all_h3_C2_C3_outer_images_exactly_equal':True,'source_images_sha256':image_sha,
        'weak_image_certificate':str(weak_image_path),'weak_image_certificate_sha256':hashlib.sha256(weak_image_path.read_bytes()).hexdigest()}
    chain=[{'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in weakchain]
    inherited=None
    weak_completed=completed
    if args.resume_state:
        args.resume_state=args.resume_state.resolve()
        inherited=json.loads(args.resume_state.read_text())
        inherited_phase_record=inherited['phase_certificates'][-1]
        inherited_phase_path=Path(inherited_phase_record['path'])
        assert hashlib.sha256(inherited_phase_path.read_bytes()).hexdigest()==inherited_phase_record['sha256']
        inherited_phase=json.loads(inherited_phase_path.read_text())
        completed=inherited['last_completed_t']
        assert inherited_phase['phase']==f'Jacobian_t{completed}'
        assert inherited['branch']==branch==inherited_phase['branch']
        mapping={sp.Symbol(v):sp.sympify(value) for v,value in inherited_phase['map_after'].items()}
        free=set(mapping)|{sp.Symbol(v) for v in inherited_phase['free_after']}
        residual=[(label,sp.sympify(value)) for label,value in inherited_phase['residual_after']]
        assert E.rows_hash(residual)==inherited_phase['residual_after_hash']
        assert all(not(value.free_symbols&set(mapping)) for value in mapping.values())

    state={'branch':branch,'field':'Q','type':'FULL SOURCE GAUGE CHART, TWO CERTIFIED NECESSARY LOCI MERGED',
        'strong_checkpoint':str(args.strong),'strong_checkpoint_sha256':hashlib.sha256(args.strong.read_bytes()).hexdigest(),
        'strong_summary':str(args.strong_summary),'strong_summary_sha256':hashlib.sha256(args.strong_summary.read_bytes()).hexdigest(),
        'strong_antecedent_chain':summary['checkpoint_chain'],
        'strong_added_phases':[{'path':p['phase_certificate'],'sha256':p['phase_certificate_sha256']} for p in summary['phases']],
        'ring_transport':ring_transport,'weak_checkpoint':str(args.weak),'weak_checkpoint_sha256':hashlib.sha256(args.weak.read_bytes()).hexdigest(),
        'weak_chain':chain,'weak_graph_targets':sorted(map(str,weakmap)),
        'weak_complete_free_ring':sorted(map(str,weakfree)),
        'weak_map_after':E.encode_map(weakmap),'weak_residual_after':D.encoded_rows(weakresidue),
        'gauge_coverage_audit_required':True,'source_gauge':meta['gauge_slice'],
        'initial_complete_free_ring':sorted(map(str,free)),
        'code_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(args.code.glob('*.py'))},
        'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'coefficient_backend_sha256':hashlib.sha256((HERE/'deep_flint_jacobian_pair.py').read_bytes()).hexdigest(),
        'quotient_seed_sha256':hashlib.sha256((HERE/'deep_quotient_seed.py').read_bytes()).hexdigest(),
        'safe_exporter_sha256':hashlib.sha256((HERE/'deep_safe_singular.py').read_bytes()).hexdigest(),
        'weak_J_bands_already_proved':list(range(weak_completed+1)),
        'inherited_J_bands_already_proved':list(range(completed+1)),
        'batch_size':args.batch_size,
        'resumed_from':({'state':str(args.resume_state),'state_sha256':hashlib.sha256(args.resume_state.read_bytes()).hexdigest(),
            'terminal_phase':str(inherited_phase_path),'terminal_phase_sha256':inherited_phase_record['sha256'],
            'all_preceding_phase_certificates':inherited['phase_certificates']} if inherited else None),
        'phase_certificates':[],'records':[],'last_completed_t':completed,'final':False}
    allnew=[]
    protected=set()
    def save(reason=None):
        state.update({'elapsed_seconds':time.monotonic()-begin,'cumulative_map':E.encode_map(mapping),
            'free_after':sorted(map(str,free-set(mapping))),'residual_rows':D.encoded_rows(residual),
            'residual_hash':E.rows_hash(residual),'stop_reason':reason})
        args.output.write_text(json.dumps(jsonable(state),indent=2,sort_keys=True)+'\n')
    def add(rows,name):
        nonlocal mapping,residual
        current=[(label,E.substitute_map(sp.sympify(value),mapping)) for label,value in rows]
        current=[(label,row) for label,row in current if row!=0]
        certificate={'phase':name,'branch':branch,'field':'Q','localizer':str(loc),
            'free_before':sorted(map(str,free-set(mapping))),'map_before':E.encode_map(mapping),
            'residual_before':D.encoded_rows(residual),'raw_new_rows_before_reduction':D.encoded_rows(current),
            'raw_new_rows_hash':E.rows_hash(current),'pivot_steps':[],'radical_steps':[]}
        log(f'{branch}: {name} {len(current)} nonzero rows before QQ* reduction')
        allnew.extend(current);pending=residual+current
        while True:
            remaining,new,pivots,zeros=E.qstar_reduce(pending,free-set(mapping)-{loc}-protected)
            if new:
                mapping.update(new);mapping=E.resolve_map(mapping)
                certificate['pivot_steps'].extend({'label':p.label,'variable':str(p.variable),
                    'rational_leader':str(p.coefficient),'rhs_at_pivot':str(p.rhs),
                    'selected_equation_at_pivot':str(sp.expand(p.coefficient*(p.variable-p.rhs)))} for p in pivots)
            residual=remaining
            roots,certificates=R.pure_power_radical_rows(residual)
            eligible=free-set(mapping)-{loc}-protected
            roots=[(label,row) for label,row in roots if any(sp.diff(row,v).is_Rational and sp.diff(row,v)!=0 for v in row.free_symbols&eligible)]
            if not roots:break
            kept={label for label,_ in roots}
            certificate['radical_steps'].extend(dict(c,source_polynomial=str(dict(residual)[c['source_row']])) for c in certificates if c['new_row'] in kept)
            pending=residual+roots
        certificate.update({'map_after':E.encode_map(mapping),'free_after':sorted(map(str,free-set(mapping))),
            'residual_after':D.encoded_rows(residual),'residual_after_hash':E.rows_hash(residual)})
        path=args.output.with_name(args.output.stem+f'_phase{len(state["phase_certificates"]):04d}.json')
        path.write_text(json.dumps(jsonable(certificate),indent=2,sort_keys=True)+'\n')
        state['phase_certificates'].append({'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
        log(f'{branch}: {name} {len(residual)} residual, {len(free-set(mapping))} free; exact Singular')
        sing=E.singular_dimension(residual,branch,args.output.with_name(args.output.stem+'_'+name+'.sing'))
        dimension=-1 if sing['unit_ideal'] else len(free-set(mapping))-sing['codimension']
        record={'phase':name,'dimension':dimension,'unit_ideal':sing['unit_ideal'],'singular':sing,
                'remaining_free':len(free-set(mapping)),'residual_count':len(residual),
                'new_nonzero_rows':len(current),'new_Qstar_pivots':len(certificate['pivot_steps']),
                'rational_point':{'status':'DIMENSION_ONLY_AFTER_NONZERO_D1_FACE','reason':'necessary universal D1 system has no rational points; parent independent certificate'},
                'elapsed_seconds':time.monotonic()-begin}
        state['records'].append(record);save();log(f'{branch}: {name} dimension={dimension}')
        return sing['unit_ideal']
    merge_rows=[(f'weak_graph_target_{v}',v-value) for v,value in sorted(weakmap.items(),key=lambda item:str(item[0]))]
    merge_rows.extend((f'weak_residual_{label}',row) for label,row in weakresidue)
    if not inherited and add(merge_rows,'merge_weak_complete_graph'):
        state['final']=True;save('UNIT_AFTER_MERGING_CERTIFIED_NECESSARY_LOCI');return
    from deep_quotient_seed import derive as derive_quotient
    consequence_rows,quotient_cfg,quotient_proof=derive_quotient(residual,branch,args.output.with_name(args.output.stem+'_quotient-transition.json'),free-set(mapping))
    protected={sp.Symbol(quotient_cfg['d']),sp.Symbol(quotient_cfg['e'])}
    state['coefficient_quotient']=quotient_cfg
    state['quotient_transition']=quotient_proof
    before_dimension=inherited['records'][-1]['dimension'] if inherited else state['records'][-1]['dimension']
    if add(consequence_rows,'certified_quotient_transition'):
        state['final']=True;save('UNIT_AT_CERTIFIED_EQUIVALENT_QUOTIENT_TRANSITION');return
    assert state['records'][-1]['dimension']==before_dimension
    q=sp.sympify(quotient_cfg['polynomial'])
    assert any(sp.expand(row-q)==0 for _,row in residual),'monic relation must remain an explicit ideal generator'
    # z=w-1 is applied to the small source blocks before coefficient products.
    def in_w(poly):
        bands=R.all_w_bands(poly,max(r for r,_ in poly)) if poly else {}
        return {(r,k):value for r,band in bands.items() for k,value in band.items()}
    base_h,base_c2,base_c3=map(in_w,(h,C2,C3))
    base_outer={name:in_w(poly) for name,poly in outer.items()}
    jdegree=S['n']+S['m']-2;terminal=min(jdegree,args.max_t)
    band_cache={};generation_map_hash=None
    save('INHERITED_LOCUS_READY')
    for tp in range(completed+1,terminal+1):
        tick=time.monotonic()
        if args.timeout_seconds and tick-begin>=args.timeout_seconds:
            state['final']=True;save(f'COMPUTE_BOUND_BEFORE_J_T{tp}');return
        if tp not in band_cache:
            high=min(tp+args.batch_size-1,terminal)
            log(f'{branch}: generating exact w Jacobian bands t{tp}..{high}')
            current=lambda poly:{pos:value for pos,expression in poly.items() if pos[0]<=high and (value:=E.substitute_map(expression,mapping))!=0}
            hh,c2,c3=map(current,(base_h,base_c2,base_c3))
            oo={name:current(poly) for name,poly in base_outer.items()}
            band_cache,backend_meta=flint_backend.jacobian_bands(hh,c2,c3,oo,high,S,first_band=tp,progress=log,quotient=quotient_cfg)
            generation_map_hash=hashlib.sha256(json.dumps(E.encode_map(mapping),sort_keys=True).encode()).hexdigest()
            backend_meta['generation_map_sha256']=generation_map_hash
            backend_meta['transport']='Cached polynomial coefficients are substituted through each subsequently proved QQ* graph map before reduction.'
            state['current_backend_metadata']=backend_meta
        band=band_cache.pop(tp)
        assert all(sp.Poly(value,sp.Symbol(quotient_cfg['d'])).degree()<=1 for value in band.values())
        assert all(0<=k<=jdegree-tp for k in band)
        rows=[]
        for k in range(jdegree-tp+1):
            value=band.get(k,sp.Integer(0))
            if tp==jdegree and k==0:value-=E.substitute_map(jc,mapping)
            rows.append((f'resumed_J_t{tp}_d{jdegree-tp}_k{k}',value))
        if add(rows,f'Jacobian_t{tp}'):
            state['last_completed_t']=tp;state['final']=True;save(f'UNIT_CORRECTED_FULL_SOURCE_CHART_AT_J_T{tp}');return
        state['last_completed_t']=tp;state['records'][-1]['elapsed_band_seconds']=time.monotonic()-tick;save()
    state['final']=True
    state['all_J_rows_exhausted']=terminal==jdegree
    save('ALL_JACOBIAN_ROWS_EXHAUSTED' if terminal==jdegree else f'COMPUTE_BOUND_AFTER_J_T{terminal}')

if __name__=='__main__':main()
