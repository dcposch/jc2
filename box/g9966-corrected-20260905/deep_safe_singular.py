#!/usr/bin/env python3
"""Exact QQ polynomial exporter with primitive integer row representatives.

Multiplication by each recorded nonzero rational/integer denominator leaves
the QQ ideal unchanged. Expressions sent to Singular contain integer
coefficients only. Any parser/error output aborts the claim.
"""
from pathlib import Path
import hashlib,json,re,subprocess
import sympy as sp


def encode_polynomial(expression,variables):
    poly=sp.Poly(sp.expand(expression),*variables,domain=sp.QQ)
    multiplier,integer_poly=poly.clear_denoms(convert=True)
    integer_expr=integer_poly.as_expr()
    assert sp.expand(multiplier*expression-integer_expr)==0
    assert all(value.is_Integer for value in integer_poly.coeffs())
    text=str(integer_expr).replace('**','^')
    assert '/' not in text
    return text,str(multiplier)


def singular_dimension(residual,branch,emit_path=None):
    if not residual:
        if emit_path:Path(emit_path).write_text('// zero residual ideal over Q\n')
        return {'unit_ideal':False,'active_variables':0,'dimension':0,'codimension':0,'basis':['0'],'wrapper_control':'not_needed','safe_integer_export':True}
    expressions=[sp.expand(row) for _,row in residual]
    localized=sp.Symbol('rho' if branch=='delta2' else 'c')
    wrapper=sp.Symbol('Zrho' if branch=='delta2' else 'Zc')
    variables=sorted(set().union(*(row.free_symbols for row in expressions))|{localized},key=str)
    assert wrapper not in variables
    encoded=[encode_polynomial(row,variables) for row in expressions]
    entries=[value for value,_ in encoded]
    script=(f'ring R=0,({",".join(map(str,variables+[wrapper]))}),dp;\n'
        f'ideal I={",".join(entries)},{wrapper}*{localized}-1;\n'
        'ideal S=std(I);\n'
        'print("BEGIN_DIM");print(dim(S));print("END_DIM");\n'
        'print("BEGIN_GB");print(S);print("END_GB");\n'
        f'ideal EmptyControl={localized},{wrapper}*{localized}-1;\n'
        f'ideal PointControl={localized}-1,{wrapper}*{localized}-1;\n'
        f'ideal RawControl={",".join(entries)};\n'
        'print("BEGIN_CONTROLS");print(reduce(1,std(EmptyControl)));print(reduce(1,std(PointControl)));print(reduce(1,std(RawControl)));print("END_CONTROLS");\nquit;\n')
    if emit_path:
        emit_path=Path(emit_path);emit_path.write_text(script)
        emit_path.with_suffix('.denominators.json').write_text(json.dumps({'row_QQ_star_multipliers':[(label,factor) for (label,_),(_,factor) in zip(residual,encoded)],'all_integer_coefficient_images_rechecked':True},indent=2)+'\n')
    run=subprocess.run(['Singular','-q'],input=script,text=True,capture_output=True,check=True)
    output=run.stdout+run.stderr
    if emit_path:emit_path.with_suffix('.sing.out').write_text(output)
    assert not re.search(r'(^|\n)\s*\?',output) and 'error' not in output.lower(),output[:5000]
    def section(name):return output.split(f'BEGIN_{name}\n',1)[1].split(f'\nEND_{name}',1)[0].strip()
    dimension=int(section('DIM').splitlines()[-1]);gb=section('GB');controls=section('CONTROLS').splitlines()
    assert controls[-3:-1]==['0','1'],controls
    unit=dimension<0
    return {'unit_ideal':unit,'active_variables':len(variables),'dimension':dimension,
        'codimension':len(variables)-dimension,'basis_line_count':len(gb.splitlines()),
        'basis_sha256':hashlib.sha256((gb+'\n').encode()).hexdigest(),'basis_preview':gb.splitlines()[:20],
        'wrapper':f'{wrapper}*{localized}-1','wrapper_control':'<p,Zp-1> unit; <p-1,Zp-1> nonunit',
        'raw_residue_unit_ideal':controls[-1]=='0','safe_integer_export':True,
        'parser_error_output_rejected':True,'exporter_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def control():
    q=sp.Symbol('q');entry,factor=encode_polynomial(q**9/32768+sp.Rational(1,2),[q])
    assert entry=='q^9 + 16384' and factor=='32768'
    cases=[([('rational_power',q**9/32768+sp.Rational(1,2)),('forceqzero',q)],True),
           ([('rational_power',q**9/32768)],False),([('localized_zero',sp.Symbol('rho')/3)],True)]
    result=[]
    for rows,want in cases:
        got=singular_dimension(rows,'delta2')
        assert got['unit_ideal']==want
        result.append(got)
    return {'status':'PASS','unsafe_shape_integer_representative':entry,'QQ_star_multiplier':factor,'cases':result}

if __name__=='__main__':print(json.dumps(control(),indent=2,sort_keys=True))
