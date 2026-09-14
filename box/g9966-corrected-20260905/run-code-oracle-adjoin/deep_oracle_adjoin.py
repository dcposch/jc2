#!/usr/bin/env python3
"""Adjoin one independently reconstructed necessary J band to an exact checkpoint.
No source parameters are specialized. The oracle's literal complete map must
match the predecessor. Its coefficients are combined classes modulo the same
explicit monic relation, which remains a generator throughout QQ* reduction.
"""
import argparse,copy,hashlib,importlib.util,json,sys,time
from pathlib import Path
import sympy as sp

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--code',type=Path,required=True);ap.add_argument('--state',type=Path,required=True);ap.add_argument('--oracle',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    for k in ('code','state','oracle','output'):setattr(args,k,getattr(args,k).resolve())
    sys.path.insert(0,str(args.code));import engine as E;import deep_rows as R
    spec=importlib.util.spec_from_file_location('safe',Path(__file__).with_name('deep_safe_singular.py'));safe=importlib.util.module_from_spec(spec);spec.loader.exec_module(safe)
    E.singular_dimension=safe.singular_dimension
    begin=time.monotonic();old=json.loads(args.state.read_text());oracle=json.loads(args.oracle.read_text());tp=int(oracle['tp']);branch=old['branch']
    assert oracle['status']=='REGENERATED' and oracle['branch']==branch
    assert tp==old['last_completed_t']+1
    assert oracle['map_before']==old['cumulative_map']
    assert oracle['metadata']['combined_A_plus_B_delta_rows'] is True and oracle['metadata']['conjugate_selected'] is False
    cfg=old['coefficient_quotient'];q=sp.sympify(cfg['polynomial']);d,e=map(sp.Symbol,(cfg['d'],cfg['e']))
    assert sp.expand(sp.sympify(oracle['metadata']['relation'])-q)==0
    free={sp.Symbol(v) for v in old['free_after']};loc=sp.Symbol('rho' if branch=='delta2' else 'c')
    residual=[(label,sp.sympify(value)) for label,value in old['residual_rows']]
    assert E.rows_hash(residual)==old['residual_hash'] and any(sp.expand(value-q)==0 for _,value in residual)
    raw=[(f'resumed_J_t{tp}_d{163-tp}_k{int(k)}',sp.sympify(v)) for k,v in sorted(oracle['rows'].items(),key=lambda kv:int(kv[0]))]
    assert all(0<=int(k)<=163-tp for k in oracle['rows'])
    assert all(row.free_symbols<=free and sp.Poly(row,d).degree()<=1 for _,row in raw)
    phase={'phase':f'Jacobian_t{tp}','branch':branch,'field':'Q','localizer':str(loc),'free_before':old['free_after'],'map_before':old['cumulative_map'],'residual_before':old['residual_rows'],'raw_new_rows_before_reduction':[(a,str(sp.expand(b))) for a,b in raw],'raw_new_rows_hash':E.rows_hash(raw),'pivot_steps':[],'radical_steps':[],
        'necessary_row_oracle':{'path':str(args.oracle),'sha256':sha(args.oracle),'driver_sha256':oracle['driver_sha256_at_start'],'core_sha256':oracle['core_sha256_at_import'],'metadata':oracle['metadata'],'map_before_literal_equality':True,'quotient_relation_exact_equality':True,'missing_coefficient_classes_are_zero':True}}
    mapping={};pending=residual+raw
    print(f'{branch}: oracle t{tp} {len(raw)} combined nonzero rows, exact QQ* reduction',flush=True)
    while True:
        residual,new,pivots,zeros=E.qstar_reduce(pending,free-set(mapping)-{loc,d,e})
        if new:
            mapping.update(new);mapping=E.resolve_map(mapping)
            phase['pivot_steps'].extend({'label':p.label,'variable':str(p.variable),'rational_leader':str(p.coefficient),'rhs_at_pivot':str(p.rhs),'selected_equation_at_pivot':str(sp.expand(p.coefficient*(p.variable-p.rhs)))} for p in pivots)
        roots,certs=R.pure_power_radical_rows(residual);eligible=free-set(mapping)-{loc,d,e}
        roots=[(label,row) for label,row in roots if any(sp.diff(row,v).is_Rational and sp.diff(row,v)!=0 for v in row.free_symbols&eligible)]
        if not roots:break
        kept={label for label,_ in roots};phase['radical_steps'].extend(dict(c,source_polynomial=str(dict(residual)[c['source_row']])) for c in certs if c['new_row'] in kept);pending=residual+roots
    print(f'{branch}: {len(mapping)} QQ* graph targets; {len(residual)} residual; transporting complete map',flush=True)
    oldmap={sp.Symbol(v):sp.sympify(expr) for v,expr in old['cumulative_map'].items()}
    oldmap={v:E.substitute_map(expr,mapping) for v,expr in oldmap.items()};oldmap.update(mapping)
    assert all(not(expr.free_symbols&set(oldmap)) for expr in oldmap.values())
    assert any(sp.expand(value-q)==0 for _,value in residual)
    encmap=E.encode_map(oldmap);encrows=[(label,str(sp.expand(row))) for label,row in residual]
    phase.update({'map_after':encmap,'free_after':sorted(map(str,free-set(mapping))),'residual_after':encrows,'residual_after_hash':E.rows_hash(residual)})
    phasepath=args.output.with_name(args.output.stem+'_phase0000.json');phasepath.write_text(json.dumps(phase,indent=2,sort_keys=True)+'\n')
    state=copy.deepcopy(old);prior=old['phase_certificates'][-1] if old['phase_certificates'] else {'path':old['resumed_from']['terminal_phase'],'sha256':old['resumed_from']['terminal_phase_sha256']}
    state.update({'driver_sha256':sha(__file__),'oracle_producer':phase['necessary_row_oracle'],'resumed_from':{'state':str(args.state),'state_sha256':sha(args.state),'terminal_phase':prior['path'],'terminal_phase_sha256':prior['sha256'],'all_preceding_phase_certificates':old['phase_certificates']},'phase_certificates':[{'path':str(phasepath),'sha256':sha(phasepath)}],'records':[],'last_completed_t':tp,'cumulative_map':encmap,'free_after':phase['free_after'],'residual_rows':encrows,'residual_hash':phase['residual_after_hash'],'final':False,'stop_reason':'ORACLE_BAND_ROWS_REDUCED_DIMENSION_PENDING'})
    args.output.write_text(json.dumps(state,indent=2,sort_keys=True)+'\n')
    print(f'{branch}: exact Singular on {len(residual)} residual rows',flush=True)
    sing=E.singular_dimension(residual,branch,args.output.with_suffix('.sing'));dimension=-1 if sing['unit_ideal'] else len(free-set(mapping))-sing['codimension']
    state['records'].append({'phase':f'Jacobian_t{tp}','dimension':dimension,'unit_ideal':sing['unit_ideal'],'singular':sing,'remaining_free':len(free-set(mapping)),'residual_count':len(residual),'new_nonzero_rows':len(raw),'new_Qstar_pivots':len(phase['pivot_steps']),'elapsed_seconds':time.monotonic()-begin,'rational_point':{'status':'DIMENSION_ONLY_AFTER_NONZERO_D1_FACE'}})
    state['final']=True;state['stop_reason']='UNIT_CORRECTED_FULL_SOURCE_CHART' if sing['unit_ideal'] else f'ORACLE_BAND_COMPLETED_T{tp}'
    args.output.write_text(json.dumps(state,indent=2,sort_keys=True)+'\n');print(f'{branch}: J{tp} dimension={dimension}',flush=True)
if __name__=='__main__':main()
