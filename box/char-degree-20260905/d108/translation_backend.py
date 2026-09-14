#!/usr/bin/env python3
"""An invertible coefficient-ring change, never a jet0 gauge slice."""
from collections import defaultdict
import hashlib,re
import sympy as sp
from char_degree_driver import clean,rows_hash

def translate(table,degree,shift):
    out=defaultdict(lambda:sp.Integer(0))
    for (r,q),value in table.items():
        rem=degree-r-q;assert rem>=0,(degree,r,q)
        for ell in range(rem+1):
            out[r+ell,q]+=value*sp.binomial(rem,ell)*shift**ell
    return {key:value for key,expr in out.items() if (value:=sp.expand(expr))!=0}

def audit_and_translate(maps):
    s=sp.Symbol('jet0');images={};inverse={};checks={}
    hnew=translate(maps['h2'],36,s)
    assert translate(hnew,36,-s)==maps['h2']
    assert not any(r==1 and value!=0 for (r,q),value in hnew.items())
    for block,degree in [('B2',71),('A3',107)]:
        table=maps[block];forward=translate(table,degree,s);backward=translate(table,degree,-s)
        variables=sorted({v for expr in table.values() for v in expr.free_symbols
                          if re.fullmatch(r'(B2|A3)c_\d+_\d+',str(v))},key=str)
        for v in variables:
            block0,r,q=re.fullmatch(r'(B2|A3)c_(\d+)_(\d+)',str(v)).groups()
            if block0!=block:continue
            pos=(int(r),int(q));assert table.get(pos)==v,(v,table.get(pos))
            images[v]=forward.get(pos,sp.Integer(0));inverse[v]=backward.get(pos,sp.Integer(0))
    for block,degree in [('B2',71),('A3',107)]:
        table=maps[block];forward=translate(table,degree,s);backward=translate(table,degree,-s)
        assert clean(table,images)==forward,(block,'forward image mismatch')
        assert clean(table,inverse)==backward,(block,'inverse image mismatch')
        assert translate(forward,degree,-s)==table,(block,'roundtrip mismatch')
        checks[block]={'forward_image':True,'inverse_image':True,'roundtrip':True}
    for v,image in images.items():
        assert sp.expand(image.subs(inverse,simultaneous=True)-v)==0,(v,'basis roundtrip')
    record={'operation':'P(x,y)->P(x+jet0,y+jet0), computational characteristic coefficient map only',
       'jet0_remains_free':True,'old_h_and_minor_parameters_fixed':True,
       'old_source_pole_and_J_rows_retained':True,'target_constants_and_leader_fixed':True,
       'source_outer_inverse':'old D=T_-jet0(new D), old C=T_-jet0(new C)',
       'forward_generator_images':{str(v):str(x) for v,x in images.items()},
       'old_generator_images_in_new_ring':{str(v):str(x) for v,x in inverse.items()},
       'full_polynomial_image_checks':checks,'all_basis_roundtrips':True,
       'h_roundtrip':True,'h_t1_removed':True,
       'h_before_sha256':rows_hash([(f'{r}_{q}',v) for (r,q),v in sorted(maps['h2'].items())]),
       'h_after_sha256':rows_hash([(f'{r}_{q}',v) for (r,q),v in sorted(hnew.items())])}
    all_symbols=set(sp.symbols('target_a target_b target_c target_d target_e leader63 Z63 c Zc'))
    for table in maps.values():
        for expression in table.values():all_symbols|=expression.free_symbols
    record['coefficient_field']='QQ'
    record['coefficient_generator_order']=sorted(map(str,all_symbols))
    record['fixed_generators']=sorted(map(str,all_symbols-set(images)))
    return {'h2':hnew,'B2':maps['B2'],'A3':maps['A3']},record
