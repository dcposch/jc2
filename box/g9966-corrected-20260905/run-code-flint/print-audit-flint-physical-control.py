#!/usr/bin/env python3
"""Independent FLINT control via direct physical x,y differentiation.

No sparse bracket implementation is used to form expected coefficients.
The input coordinate map is explicit: x^i*y^j at normalization D maps to
(r,k)=(D-i-j,j), with exactly the same QQ coefficient polynomial.
"""
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import sympy as sp


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--helper',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    spec=importlib.util.spec_from_file_location('flint_under_test',args.helper.resolve());M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
    begin=time.monotonic();x,y=sp.symbols('x y');a,b,c,d=sp.symbols('a b c d')
    def norm(poly,D):
        out={}
        for (i,j),coef in sp.Poly(sp.expand(poly),x,y).terms():
            assert i+j<=D
            out[D-i-j,j]=sp.expand(coef)
        return out
    def prepare(h,c2,c3,outer,n,m,hdegree):
        H=h**3+c2*h+c3
        F=H**3+outer['A2']*H+outer['A3'];G=H**2+outer['B1']*H+outer['B2']
        # Direct physical derivatives are the independent oracle.
        J=sp.Poly(sp.expand(sp.diff(F,x)*sp.diff(G,y)-sp.diff(F,y)*sp.diff(G,x)),x,y)
        degree=n+m-2
        expected=norm(J.as_expr(),degree)
        normalized=(norm(h,hdegree),norm(c2,2*hdegree),norm(c3,3*hdegree),
                    {name:norm(poly,D) for (name,poly),D in zip(outer.items(),(n-3*hdegree-1,n-1,m-3*hdegree-1,m-1))})
        source={'n':n,'m':m,'h3_degree':hdegree,'k2_degree':3*hdegree,'inner_power':3,'outer_power_F':3,'outer_power_G':2}
        return normalized,source,expected,J.as_expr()
    h=sp.Rational(1,61)+a*x/2+b*y*y/3+x*y/5
    c2=c*x*x/7-y/11+a*b/13;c3=d*x**3/17+y*y/19+b*c/23
    outer={'A2':x**11/17+a*y**3/19+c/23,
           'A3':x**17/29+d*y**5/31,
           'B1':x**5/37+b*y/41+sp.Rational(1,43),
           'B2':x**11/47+a*b*y*y/53+d/59}
    blocks,source,expected,J=prepare(h,c2,c3,outer,18,12,2)
    print('DIRECT_TOY_DERIVATIVE_READY',time.monotonic()-begin,flush=True)
    records=[]
    wanted_generators=['w']+sorted(map(str,set().union(*(v.free_symbols for p in blocks[:3] for v in p.values()),*(v.free_symbols for p in blocks[3].values() for v in p.values()))))
    got_all={}
    for cutoff in range(29):
        got,meta=M.jacobian_band(*blocks,cutoff,source)
        want={k:v for (r,k),v in expected.items() if r==cutoff}
        for k in set(got)|set(want):assert sp.expand(got.get(k,0)-want.get(k,0))==0,(cutoff,k)
        assert all(0<=k<=28-cutoff for k in got)
        assert meta['active_computation_generators']==wanted_generators
        assert meta['coefficient_field']=='Q' and meta['full_chart_coordinates_removed'] is False
        got_all.update({(cutoff,k):v for k,v in got.items()})
        records.append({'cutoff':cutoff,'w_slots':len(got),'active_generators':meta['active_computation_generators'],'band_terms':meta['band_terms']})
    assert set(got_all)==set(expected)
    assert expected[28,0]!=0
    # A rename which changes sorted generator positions must transport the
    # actual polynomial images, not preserve old coefficient indices.
    fresh_z,fresh_A=sp.symbols('zz_late A_early');rename={a:fresh_z,d:fresh_A}
    renamed=tuple({k:sp.expand(v.xreplace(rename)) for k,v in p.items()} for p in blocks[:3])+( {name:{k:sp.expand(v.xreplace(rename)) for k,v in p.items()} for name,p in blocks[3].items()}, )
    rename_checks=[]
    for cutoff in (1,7,14,28):
        got,meta=M.jacobian_band(*renamed,cutoff,source)
        want={k:sp.expand(v.xreplace(rename)) for (r,k),v in expected.items() if r==cutoff}
        assert all(sp.expand(got.get(k,0)-want.get(k,0))==0 for k in set(got)|set(want))
        assert meta['active_computation_generators']==['w','A_early','b','c','zz_late']
        rename_checks.append(cutoff)
    assert sp.expand(expected[28,0].xreplace(rename)-expected[28,0])!=0
    # Every new source generator is automatically retained in the explicit
    # coefficient ring; there is no caller-supplied list that can omit it.
    hidden=sp.Symbol('Zface_hidden');extra=[dict(p) for p in blocks[:3]]+[dict(blocks[3])]
    extra[3]={name:dict(p) for name,p in blocks[3].items()}
    extra[3]['A3'][17,0]=extra[3]['A3'].get((17,0),0)+hidden
    got,meta=M.jacobian_band(*extra,28,source)
    assert 'Zface_hidden' in meta['active_computation_generators']
    # Constant A3 does not change J, but must still be a declared ring image.
    assert all(sp.expand(got.get(k,0)-got_all.get((28,k),0))==0 for k in set(got)|{0})
    negatives=[]
    for label,coefficient in [('nonrational_coefficient',sp.sqrt(2)),('negative_parameter_exponent',a**-1),('fractional_parameter_exponent',a**sp.Rational(1,2)),('reserved_w_collision',sp.Symbol('w'))]:
        bad=[dict(p) for p in blocks[:3]]+[blocks[3]];bad[0][2,0]=coefficient
        try:M.jacobian_band(*bad,28,source)
        except (AssertionError,ValueError,TypeError):negatives.append(label)
        else:raise AssertionError('invalid coefficient accepted: '+label)
    # Full (99,66) normalization, actual physical degree-corner test.
    hh=1+x+2*y;cc2=a+x*y;cc3=b+3*x-y
    oo={'A2':c+x,'A3':d+2*y,'B1':a-y,'B2':x+4*y}
    full,fullsource,fullexpected,fullJ=prepare(hh,cc2,cc3,oo,99,66,11)
    for cutoff in (0,149,150,157,162,163):
        got,meta=M.jacobian_band(*full,cutoff,fullsource)
        want={k:v for (r,k),v in fullexpected.items() if r==cutoff}
        assert all(sp.expand(got.get(k,0)-want.get(k,0))==0 for k in set(got)|set(want))
        assert all(0<=k<=163-cutoff for k in got)
    corner=sp.expand(fullJ.subs({x:0,y:0}));assert corner==fullexpected[163,0] and corner!=0
    result={'status':'PASS','oracle':'Direct physical x,y differentiation and explicit monomial normalization; no shared sparse bracket oracle',
        'coefficient_field':'Q','toy_degrees':[18,12],'toy_all_cutoffs':records,'toy_constant_coefficient':str(expected[28,0]),
        'source_ring_map':'x^i*y^j -> coefficient at (normalization_degree-i-j,j); active generator images preserved in sorted FLINT QQ context',
        'generator_reordering_checks':rename_checks,'wrong_generator_image_negative_control':True,'new_symbol_automatically_retained':True,
        'invalid_inputs_rejected':negatives,'full_degrees':[99,66],'full_checked_cutoffs':[0,149,150,157,162,163],
        'full_constant_coefficient':str(corner),'w_degree_bound_at_every_cutoff_verified':True,
        'helper_sha256':hashlib.sha256(args.helper.read_bytes()).hexdigest(),'control_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'expected_all_coefficient_hash':hashlib.sha256('\n'.join(f'{p}:{sp.srepr(v)}' for p,v in sorted(expected.items())).encode()).hexdigest(),
        'elapsed_seconds':time.monotonic()-begin}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','toy_cutoffs':29,'renamed_cutoffs':4,'full_normalization_cutoffs':6,'negative_controls':len(negatives),'elapsed_seconds':time.monotonic()-begin}),flush=True)

if __name__=='__main__':main()
