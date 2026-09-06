#!/usr/bin/env python3
"""Reconstruct exact roster Jacobian rows in disposable shared memory.

The production support/compiler/fix path is hash pinned by chart_counts.
Its emitted setup and coordinate inventory are compared with the frozen roster.
The already audited sparse extractor supplies exact Z-polynomial arithmetic.
No production receiver, coefficient coordinate, or gauge is altered.
"""
import hashlib, importlib.util, json, re, resource, sys, time
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]

def imp(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod
    spec.loader.exec_module(mod);return mod

cc=imp('lambda_roster_counts',ROOT/'box/residual66-20260905/chart_counts.py')
sp=imp('lambda_sparse_rows',ROOT/'box/gi-only-20260905/experiments/fast-extract/sparse_hadic_extract.py')
assert sp.sha256(Path(sp.__file__))=='a1c24fc7b7b4732ec3a78efe968763abe9846418bab80fff8e7128a224386516'

def build(row):
    start=time.monotonic(); child=row['own_child']; rc=row['receiver_chart']
    K,e,q,ell=rc['K'],rc['e'],rc['q'],child['ell'];d=F(rc['d'])
    compiler,emitter,fix,custody=cc.production_emitter_runtime()
    C=dict(K=K,e=e,q=q,u=0,R=0,Pi=0,d3prime=1,delta1=F(0),delta2=F(0),
           delta_s=-d,B=F(-1),B_safe=F(-1),B_tight=F(-1),lambda_P=F(0),
           lambda_Q=F(0),s=2,ell=ell,two_point=False,
           support_basis='proved_outer_disc_G_only_H1_H2_H3_v1')
    inv=emitter.supports(compiler,C)
    key=(child['n_prime'],child['m_prime'],child['M_prime'][-1],ell)
    name=cc.receiver_key_string(key)
    rr=compiler.OB.Row(key=name,label=f'residual66 dry production {name}',
        n=key[0],m=key[1],M2=key[2],V2=0,k=ell)
    spec=compiler.build_spec(C,inv['h'],inv['alpha_pre'],inv['beta_pre'],rr,
                           'proved_G_only_class_uniform_count_only')
    spec['low_terms'],spec['high_terms']=list(spec['high_terms']),list(spec['low_terms'])
    raw=compiler.OB.native_builder_text(spec,Path('/tmp/residual66-production-count-only-rows.tsv'))
    program,fixinfo=fix.fix_text(raw)
    digest=hashlib.sha256(program.encode()).hexdigest()
    expected=rc['production_emitter_dry_run']
    assert digest==expected['emitted_program_sha256'],(digest,expected['emitted_program_sha256'])
    model=cc.parse_emitted_row_program(program,e=e,q=q,expected_program_sha256=digest)
    variables=model['parameters'];assert len(variables)==rc['unknowns_without_T']
    assert variables==[str(p) for p in spec['params']]
    nums={v:i for i,v in enumerate(variables)}
    setup=dict(re.findall(r'^poly (h|AA\d+|BB\d+) = (.*);$',program,re.M))
    base={k:sp.parse_base_polynomial(v,nums) for k,v in setup.items()}
    one={(0,0):{():1}}
    P=[(one,e)]+[(base[f'AA{i}'],e-i) for i in range(1,e+1)]
    Q=[(one,q)]+[(base[f'BB{i}'],q-i) for i in range(2,q+1)]
    levels=defaultdict(dict)
    for left,r in P:
        for right,s in Q:
            sp.bp_addto(levels[r+s],sp.bp_jac(left,right))
            if r+s:
                lower={}
                if s:sp.bp_addto(lower,sp.bp_scaled_product(right,sp.bp_jac(left,base['h']),s))
                if r:sp.bp_addto(lower,sp.bp_scaled_product(left,sp.bp_jac(base['h'],right),r))
                sp.bp_addto(levels[r+s-1],lower)
    out=Path('/dev/shm')/f'lambda-lowweight-{row["row_id"]}-rows.tsv'
    coords=[];total_terms=0;level=0;last=max(levels)
    with out.open('w') as f:
        f.write('source_index|h_power|x_power|y_power|expr\n')
        while level<=last or levels.get(level):
            before=levels.pop(level,{})
            quotient,remainder=sp.monic_y_division(before,base['h'],K)
            if quotient:sp.bp_addto(levels[level+1],quotient)
            if level==0:sp.pp_addto(remainder.setdefault((ell,0),{}),{(nums['c'],):1},-1)
            for (x,y),poly in sorted(remainder.items()):
                if not poly:continue
                f.write(f'{len(coords)}|{level}|{x}|{y}|{sp.pp_text(poly,variables)}\n')
                coords.append((level,x,y));total_terms+=len(poly)
            level+=1
    assert len(coords)==rc['coefficient_generators']
    assert cc.coordinate_digest(coords)==rc['coefficient_coordinate_sha256']
    result=dict(id=row['row_id'],n=key[0],m=key[1],K=K,ell=ell,
        W=key[1]+child['M_prime'][1],variables=variables,rows_path=str(out),
        rows_sha256=sp.sha256(out),rows_bytes=out.stat().st_size,
        coefficient_rows=len(coords),coefficient_coordinate_sha256=cc.coordinate_digest(coords),
        production_builder_sha256=digest,production_custody=custody,
        total_terms=total_terms,wall_seconds=round(time.monotonic()-start,3),
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        status='EXACT_Z_ROWS_FROM_HASH_MATCHED_PRODUCTION_SETUP')
    (HERE/f'{row["row_id"]}.rows.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['variables','production_custody']}),flush=True)
    return result

if __name__=='__main__':
    rows=[json.loads(s) for s in Path('/tmp/jc2-lane.IZAvbL/inputs/roster.jsonl').read_text().splitlines()[:4]]
    for row in rows:
        if row['row_id']=='R003':
            previous=json.loads((HERE/'R002.rows.json').read_text());previous['id']='R003'
            (HERE/'R003.rows.json').write_text(json.dumps(previous,indent=2)+'\n')
            continue
        if len(sys.argv)>1 and row['row_id'] not in sys.argv[1:]:continue
        build(row)
