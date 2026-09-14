#!/usr/bin/env python3
"""Derive and certify actual D1 Groebner consequences before quotient use."""
from pathlib import Path
import hashlib,json,re,subprocess
import sympy as sp
import engine as E
import deep_safe_singular as SAFE


def derive(residual,branch,path,free):
    path=Path(path)
    dim=SAFE.singular_dimension(residual,branch,path.with_suffix('.seed-GB.sing'))
    assert not dim['unit_ideal']
    output=path.with_suffix('.seed-GB.sing.out').read_text()
    section=output.split('BEGIN_GB\n',1)[1].split('\nEND_GB',1)[0]
    gb=[(f'actual_D1_GB_{i}',sp.sympify(value.replace('^','**').replace('\n',''))) for i,value in enumerate(section.split(',')) if value.strip()]
    faces=sorted((v for v in set(free) if str(v).startswith('Zface_H2_')),key=lambda v:int(str(v).rsplit('_',1)[1]))
    assert len(faces)==2,faces
    d,e=faces
    eligible={v for _,row in residual for v in row.free_symbols if str(v).startswith('Zface_B2_')}
    remain,mapping,pivots,_=E.qstar_reduce(gb,set(eligible))
    assert len(mapping)==len(eligible)==3,(mapping,eligible)
    candidates=[]
    for label,row in remain:
        if row.free_symbols<={d,e} and row!=0:
            poly=sp.Poly(row,d)
            if poly.degree()==2 and poly.LC().is_Rational and poly.LC()!=0:
                candidates.append((label,sp.expand(poly.monic().as_expr()),str(row)))
    assert candidates,'GB has no constant-leader quadratic in retained source face coordinate'
    label,q,source=candidates[0]
    assert all(sp.expand(other-q)==0 for _,other,_ in candidates)
    poly=sp.Poly(q,d,e,domain=sp.QQ)
    assert set(poly.monoms())=={(2,0),(1,2),(0,4)} and poly.coeff_monomial(d*d)==1
    qa=-poly.coeff_monomial(d*e*e);qb=poly.coeff_monomial(e**4)
    cfg={'d':str(d),'e':str(e),'a':str(qa),'b':str(qb),'polynomial':str(q),
        'explicit_generator_label':'retained_monic_D1_relation','coefficient_leader':'1',
        'both_components_retained':True}
    rows=[(f'GB_consequence_graph_{v}',sp.expand(v-rhs)) for v,rhs in sorted(mapping.items(),key=lambda pair:str(pair[0]))]
    rows.append(('retained_monic_D1_relation',q))
    loc=sp.Symbol('rho' if branch=='delta2' else 'c');inv=sp.Symbol('Zrho' if branch=='delta2' else 'Zc')
    variables=sorted(set().union(*(value.free_symbols for _,value in residual+rows))|{loc},key=str)
    encode=lambda row:SAFE.encode_polynomial(row,variables)[0]
    script=(f'ring R=0,({",".join(map(str,variables+[inv]))}),dp;\n'
        f'ideal I={",".join(encode(v) for _,v in residual)},{inv}*{loc}-1;\n'
        f'ideal K={",".join(encode(v) for _,v in rows)};\n'
        'ideal G=std(I);ideal H=std(I+K);\n'
        'print("BEGIN_INCLUSIONS");print(size(reduce(K,G)));print(size(reduce(G,H)));print(size(reduce(H,G)));print("END_INCLUSIONS");\n'
        f'ideal Empty={loc},{inv}*{loc}-1;ideal Point={loc}-1,{inv}*{loc}-1;\n'
        'print("BEGIN_CONTROLS");print(reduce(1,std(Empty)));print(reduce(1,std(Point)));print("END_CONTROLS");quit;\n')
    singpath=path.with_suffix('.membership.sing');singpath.write_text(script)
    run=subprocess.run(['Singular','-q'],input=script,text=True,capture_output=True,check=True);text=run.stdout+run.stderr
    singpath.with_suffix('.sing.out').write_text(text)
    assert not re.search(r'(^|\n)\s*\?',text) and 'error' not in text.lower(),text[:2000]
    checks=text.split('BEGIN_INCLUSIONS\n',1)[1].split('\nEND_INCLUSIONS',1)[0].splitlines();assert checks==['0','0','0'],checks
    controls=text.split('BEGIN_CONTROLS\n',1)[1].split('\nEND_CONTROLS',1)[0].splitlines();assert controls==['0','1']
    record={'status':'PASS','field':'Q','branch':branch,'ring_variables':list(map(str,variables+[inv])),
        'localized_ideal_wrapper':f'{inv}*{loc}-1','input_residual':[(l,str(v)) for l,v in residual],
        'input_residual_hash':E.rows_hash(residual),'actual_GB_rows':[(l,str(v)) for l,v in gb],
        'source_GB_sha256':hashlib.sha256(output.encode()).hexdigest(),
        'derived_graph_map':E.encode_map(mapping),'graph_pivots':[{'label':p.label,'variable':str(p.variable),'rational_leader':str(p.coefficient),'rhs':str(p.rhs)} for p in pivots],
        'quadratic_source_row':{'label':label,'polynomial':source},'quotient':cfg,
        'adjoined_consequences':[(l,str(v)) for l,v in rows],
        'exact_ideal_checks':{'K_subset_I':True,'I_plus_K_equals_I_both_inclusions':True},
        'membership_script':str(singpath),'membership_script_sha256':hashlib.sha256(script.encode()).hexdigest(),
        'original_residual_generators_retained':True,'no_generator_deleted':True,
        'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    return rows,cfg,record
