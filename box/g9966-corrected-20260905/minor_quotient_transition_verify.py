#!/usr/bin/env python3
"""Independent ideal-membership gate for activating a monic coefficient quotient."""
from pathlib import Path
import hashlib,re,subprocess
import sympy as sp
OWN_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

def verify(verifier,certificate,proof,config,path):
    v=verifier;path=Path(path)
    assert certificate['phase']=='certified_quotient_transition'
    before=v.rows(certificate['residual_before']);raw=v.rows(certificate['raw_new_rows_before_reduction'])
    assert before==v.rows(proof['input_residual'])
    assert v.e.rows_hash(before)==proof['input_residual_hash']
    assert raw==v.rows(proof['adjoined_consequences'])
    assert config==proof['quotient'] and proof['status']=='PASS' and proof['branch']==v.branch and proof['field']=='Q'
    d=v.locals[config['d']];e=v.locals[config['e']];q=v.expr(config['polynomial'])
    assert d!=e and {d,e}<=set(map(sp.Symbol,certificate['free_before']))
    p=sp.Poly(q,d);assert p.degree()==2 and p.LC()==1
    assert sp.expand(q-(d**2-sp.Rational(config['a'])*d*e**2+sp.Rational(config['b'])*e**4))==0
    assert q.free_symbols=={d,e} and config['coefficient_leader']=='1' and config['both_components_retained']
    assert dict(raw)[config['explicit_generator_label']]==q
    graphs={label.removeprefix('GB_consequence_graph_'):row for label,row in raw if label.startswith('GB_consequence_graph_')}
    assert set(graphs)==set(proof['derived_graph_map']) and len(graphs)==3
    for name,row in graphs.items():assert sp.expand(row-(v.locals[name]-v.expr(proof['derived_graph_map'][name])))==0
    assert len(raw)==4
    loc=v.loc;inv=sp.Symbol('Zrho' if v.branch=='delta2' else 'Zc')
    symbols=sorted(set().union(*(value.free_symbols for _,value in before+raw))|{loc},key=str)
    assert inv not in symbols
    multipliers=[]
    def encode(label,value):
        p=sp.Poly(value,*symbols,domain=sp.QQ);denom,integer=p.clear_denoms(convert=True);content,primitive=integer.primitive()
        factor=sp.Rational(denom,content) if content else sp.Integer(1)
        assert factor!=0 and sp.expand(factor*value-primitive.as_expr())==0
        text=str(primitive.as_expr()).replace('**','^');assert '/' not in text
        multipliers.append([label,str(factor)])
        return text
    lhs=','.join(encode('old:'+l,x) for l,x in before) or '0'
    rhs=','.join(encode('new:'+l,x) for l,x in raw) or '0'
    order=symbols+[inv]
    script=(f'ring R=0,({",".join(map(str,order))}),dp;\n'
      'print("BEGIN_RING");print(char(R));print(nvars(R));int i;for(i=1;i<=nvars(R);i++){print(var(i));}print("END_RING");\n'
      f'ideal I={lhs},{inv}*{loc}-1;ideal K={rhs};ideal G=std(I);ideal H=std(I+K);\n'
      'print("BEGIN_INCLUSIONS");print(size(reduce(K,G)));print(size(reduce(G,H)));print(size(reduce(H,G)));print(dim(G));print(dim(H));print("END_INCLUSIONS");\n'
      f'ideal Empty={loc},{inv}*{loc}-1;ideal Point={loc}-1,{inv}*{loc}-1;\n'
      'print("BEGIN_CONTROLS");print(reduce(1,std(Empty)));print(reduce(1,std(Point)));print("END_CONTROLS");quit;\n')
    path.write_text(script);run=subprocess.run(['Singular','-q'],input=script,text=True,capture_output=True,check=True)
    path.with_suffix('.sing.out').write_text(run.stdout+run.stderr)
    assert '?' not in run.stdout and not run.stderr.strip() and 'error' not in run.stdout.lower()
    def section(name):return run.stdout.split('BEGIN_'+name+'\n',1)[1].split('\nEND_'+name,1)[0].strip().splitlines()
    ring=section('RING');assert ring==['0',str(len(order)),*map(str,order)]
    inclusion=section('INCLUSIONS');assert inclusion[:3]==['0']*3 and inclusion[3]==inclusion[4] and int(inclusion[3])>=0
    assert section('CONTROLS')==['0','1']
    v.quotient=q;v.quotient_generator=d;v.quotient_parameters={d,e}
    return {'status':'PASS','current_residual_membership_recomputed':True,
      'consequences_subset_current_ideal':True,'I_plus_K_equals_I_both_inclusions':True,
      'field':'Q','ordered_ring_generators':list(map(str,order)),
      'all_generators_have_checked_polynomial_images':True,
      'QQstar_export_multipliers':multipliers,'monic_relation':str(q),'protected_coordinates':[str(d),str(e)],
      'script_sha256':hashlib.sha256(script.encode()).hexdigest(),
      'output_sha256':hashlib.sha256((run.stdout+run.stderr).encode()).hexdigest(),
      'verifier_sha256_at_import':OWN_SHA256,'dimension_before_and_after':int(inclusion[3]),
      'empty_and_nonempty_localizer_controls':['0','1']}
