#!/usr/bin/env python3
"""Independent exact-Q endpoint/certificate verifier for the corrected lane.

A result is never promoted from its final coordinate map alone.  Per-phase
certificates replay the actual QQ* equations and certified radical powers.
The selected terminal phase is regenerated from source polynomials on its
map_before locus, before its new reductions.  Singular is invoked afresh in
an explicitly constructed ring with positive and negative wrapper controls.

Usage: --result RESULT.json --code-dir immutable-code --out VERIFY.json
       --certificate PHASE.json --code-dir CODE --out VERIFY.json
--certificate alone is a phase test, not a full branch verdict.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib
import json
from math import comb
from pathlib import Path
import re
import subprocess
import sys
import time
import sympy as sp


def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

VERIFIER_SHA256_AT_IMPORT=digest(Path(__file__))
PATH_ROOTS=[]

def load_code(directory,gauge=False):
    directory=Path(directory).resolve();sys.path.insert(0,str(directory))
    e=importlib.import_module('engine')
    assert Path(e.__file__).resolve().parent==directory
    if gauge:
        wrapper=importlib.import_module('deep_gauge_accelerated')
        assert Path(wrapper.__file__).resolve().parent==directory
        assert e.inner_state is wrapper.gauge_inner
    return e


class Verifier:
    def __init__(self,e,branch):
        self.e=e;self.branch=branch;self.S=e.S
        self.h,self.c2,self.c3,self.inner,self.major=e.inner_state(branch)
        self.outer,self.outerfree,self.outermeta=e.outer_state(-1)
        self.basefree=set(self.inner)|set(self.outerfree)
        _h,hvars=e.h3_template()
        allsymbols=set(hvars)|set(e.MM.branch_data(branch)['parameters'])|self.basefree|{sp.Symbol('jet0')}
        hd=self.S['h3_degree']
        for name,d in [('C2',2*hd),('C3',3*hd)]:
            allsymbols|={sp.Symbol(f'{name}c_{r}_{q}') for r in range(1,d+1) for q in range(min(hd-1,d-r)+1)}
        allsymbols|=set(map(sp.Symbol,['Jc','ZJ']))
        self.locals={str(v):v for v in allsymbols}
        self.loc=sp.Symbol('rho' if branch=='delta2' else 'c')
        self.cache={};self.symbols_cache={};self.extra_generators=set();self.graph_faces=None;self.weak_map=None;self.weak_residual=None;self.quotient=None;self.quotient_generator=None;self.quotient_parameters=set()

    def symbols(self,value):
        if not hasattr(self,'symbols_cache'):self.symbols_cache={}
        if value not in self.symbols_cache:self.symbols_cache[value]=value.free_symbols
        return self.symbols_cache[value]

    def expr(self,text):
        if not isinstance(text,str):text=str(text)
        if text in self.cache:return self.cache[text]
        names=set(re.findall(r'[A-Za-z_][A-Za-z_0-9]*',text))
        assert names<=set(self.locals),('undeclared generator',names-set(self.locals))
        assert re.fullmatch(r'[A-Za-z_0-9+*/() \-]*',text),('non-polynomial syntax',text[:80])
        value=sp.sympify(text,locals=self.locals)
        assert not value.atoms(sp.Float)
        assert value.free_symbols<=set(self.locals.values())
        for p in value.atoms(sp.Pow):
            assert p.exp.is_Integer and p.exp>=0,('non-polynomial inversion/exponent',p)
        value=sp.expand(value)
        if len(self.cache)>=50000:self.cache.pop(next(iter(self.cache)))
        self.cache[text]=value
        return value

    def rows(self,encoded):
        result=[(label,self.expr(value)) for label,value in encoded]
        assert len({label for label,_ in result})==len(result),'duplicate row labels'
        return result

    def mapping(self,encoded):
        assert set(encoded)<=set(self.locals),'unrecognized source coordinate'
        result={self.locals[name]:self.expr(rhs) for name,rhs in encoded.items()}
        assert self.loc not in result,'branch localizer was eliminated'
        allowed=self.basefree|self.extra_generators|set(map(sp.Symbol,['Jc','ZJ']))
        assert set(result)<=allowed,('map domain outside declared computation ring',set(result)-allowed)
        assert all(self.symbols(rhs)<=allowed for rhs in result.values()),'map image outside declared computation ring'
        domain=set(result)
        assert not any(self.symbols(rhs)&domain for rhs in result.values()),'map not simultaneously resolved'
        return result

    @staticmethod
    def equal_map(a,b):
        return set(a)==set(b) and all(sp.expand(a[v]-b[v])==0 for v in a)

    def check_source(self,result):
        expected=result['initial_inner']
        for key in ['source_raw_rows_hash','source_recheck_hash','inner_dimension_before_residual']:
            assert self.major[key]==expected[key],('source reconstruction',key)
        for key in ['h3_map','source_map']:
            actual={self.locals[k]:self.expr(v) for k,v in self.major[key].items()}
            supplied={self.locals[k]:self.expr(v) for k,v in expected[key].items()}
            assert self.equal_map(actual,supplied),('source map image differs',key)
        assert set(self.basefree)==set(self.inner)|set(self.outerfree)
        expected_outer=result['initial_outer']
        assert self.outermeta['derived_specs']==expected_outer['derived_specs'] or {
            k:list(v) for k,v in self.outermeta['derived_specs'].items()}==expected_outer['derived_specs']
        assert self.outermeta['outer_free_count']==expected_outer['outer_free_count']
        return {'source_maps_rebuilt_and_images_equal':True,
                'source_raw_rows_hash':self.major['source_raw_rows_hash'],
                'base_generator_count':len(self.basefree)}

    def apply(self,poly,mapping,cut=None):
        return {pos:value for pos,expr in poly.items()
                if (cut is None or pos[0]<=cut)
                and (value:=sp.expand(sp.sympify(expr).xreplace(mapping)))!=0}

    def blocks(self,mapping,cut):
        h=self.apply(self.h,mapping,cut);c2=self.apply(self.c2,mapping,cut);c3=self.apply(self.c3,mapping,cut)
        H=self.e.tz_add(self.e.tz_mul(self.e.tz_mul(h,h,cut),h,cut),self.e.tz_mul(c2,h,cut),c3)
        outer={name:self.apply(poly,mapping,cut) for name,poly in self.outer.items()}
        return H,outer

    def independent_local(self,poly,maxpower,exact_only=False):
        """Independent truncated substitution by repeated multiplication."""
        d=self.S['minor'][self.branch]['cover']
        w={(n,k):sp.sympify(value) for n,k,value in self.e.MM.branch_data(self.branch)['w_terms']}
        z=dict(w);z[(0,0)]=sp.Integer(-1)
        powers=[{(0,0):sp.Integer(1)}]
        def mult(a,b):
            terms={}
            for (n,k),x in a.items():
                for (m,l),y in b.items():
                    if n+m<=maxpower:terms[n+m,k+l]=terms.get((n+m,k+l),0)+x*y
            return {key:sp.expand(v) for key,v in terms.items() if v!=0}
        for _ in range(max((q for r,q in poly),default=0)):
            powers.append(mult(powers[-1],z))
        terms={}
        for (r,q),v in poly.items():
            for (n,k),c in powers[q].items():
                if (d*r+n==maxpower if exact_only else d*r+n<=maxpower):terms[d*r+n,k]=terms.get((d*r+n,k),0)+v*c
        return {key:v for key,value in terms.items() if (v:=sp.expand(value))!=0}

    def independent_d1_source_faces(self,mapping):
        """Compose into e,Pi before multiplication; do not use weight faces.

        This deliberately does not call d1_jacobian_face.extract_face or the
        driver's weighted sparse multiplication.  The source substitution is
        t=e^a,z=e^b+Pi*e^c; finite series multiplication derives H2's face.
        """
        Pi=sp.Symbol('Pi');a,b,c=self.S['D1_substitution']
        threshold=self.S['k2_D1_floor']
        def compose(poly,cap):
            out={}
            for (r,q),value in poly.items():
                if a*r+b*q>cap:continue
                value=sp.expand(sp.sympify(value).xreplace(mapping))
                if value==0:continue
                for k in range(q+1):
                    exponent=a*r+b*(q-k)+c*k
                    if exponent<=cap:
                        key=exponent,k
                        out[key]=out.get(key,0)+value*comb(q,k)
            return {key:v for key,value in out.items() if (v:=sp.expand(value))!=0}
        def multiply(x,y,cap):
            out={}
            for (n,k),value in x.items():
                for (m,l),other in y.items():
                    if n+m<=cap:
                        key=n+m,k+l
                        out[key]=out.get(key,0)+value*other
            return {key:v for key,value in out.items() if (v:=sp.expand(value))!=0}
        def coefficient(poly,power):
            return sp.expand(sum(value*Pi**k for (n,k),value in poly.items() if n==power))
        hmin=self.S['h3_floor']*a//self.S['D2_weight'][0]
        h=compose(self.h,threshold-2*hmin)
        c2=compose(self.c2,threshold-hmin)
        c3=compose(self.c3,threshold)
        H=coefficient(multiply(multiply(h,h,threshold),h,threshold),threshold)
        H+=coefficient(multiply(c2,h,threshold),threshold)+coefficient(c3,threshold)
        H=sp.expand(H)
        outer={}
        for name,poly in self.outer.items():
            target=self.S['outer_specs'][name][2]
            # A finite binomial source term reaches this equality exponent
            # iff it lies between its first and last e exponent. Filter
            # dependencies before evaluating large solved coefficient images.
            relevant={pos:value for pos,value in poly.items()
                      if a*pos[0]+b*pos[1]<=target<=a*pos[0]+c*pos[1]
                      and (target-a*pos[0]-b*pos[1])%(c-b)==0}
            outer[name]=coefficient(compose(relevant,target),target)
        return {'H2':H,**outer}

    def independent_d1_face(self,mapping):
        faces=(self.independent_d1_source_faces(mapping) if self.graph_faces is None else
               {name:sp.expand(value.xreplace(mapping)) for name,value in self.graph_faces.items()})
        Pi=sp.Symbol('Pi');a,b,c=self.S['D1_substitution']
        H=faces['H2'];outer=faces
        P=sp.expand(H**self.S['outer_power_F']+outer['A2']*H+outer['A3'])
        Q=sp.expand(H**self.S['outer_power_G']+outer['B1']*H+outer['B2'])
        # Compute the coordinate Jacobian symbolically, instead of entering
        # the specialized 3,-2,9 formula used by the production helper.
        e=sp.Symbol('epsilon');x=e**(-a);y=e**(-a)+e**(b-a)+Pi*e**(c-a)
        f_order=sp.Rational(self.S['g_order_D1'])*a
        g_order=f_order*sp.Rational(self.S['m'],self.S['n'])
        F=e**f_order*P;G=e**g_order*Q
        determinant=sp.diff(x,e)*sp.diff(y,Pi)-sp.diff(x,Pi)*sp.diff(y,e)
        value=sp.cancel((sp.diff(F,e)*sp.diff(G,Pi)-sp.diff(F,Pi)*sp.diff(G,e))/determinant)
        assert e not in value.free_symbols,'D1 Jacobian face was not at physical order zero'
        return sp.expand(value)

    def independent_origin_constant(self,mapping):
        """Rebuild first Taylor polynomials in physical x,y and differentiate."""
        x,y=sp.symbols('physical_x physical_y')
        def taylor(poly,degree):
            positions={(degree,0),(degree-1,0),(degree-1,1)}
            poly=self.apply({pos:value for pos,value in poly.items() if pos in positions},mapping)
            return (poly.get((degree,0),0)
                    +(poly.get((degree-1,0),0)-poly.get((degree-1,1),0))*x
                    +poly.get((degree-1,1),0)*y)
        degree=self.S['h3_degree']
        h=taylor(self.h,degree);c2=taylor(self.c2,2*degree);c3=taylor(self.c3,self.S['inner_power']*degree)
        H=h**self.S['inner_power']+c2*h+c3
        outer={name:taylor(poly,self.S['outer_specs'][name][0]) for name,poly in self.outer.items()}
        F=H**self.S['outer_power_F']+outer['A2']*H+outer['A3']
        G=H**self.S['outer_power_G']+outer['B1']*H+outer['B2']
        # Differentiate factored expressions before expanding; evaluating
        # at the origin discards every higher Taylor term immediately.
        at_origin={x:0,y:0}
        Fx=sp.diff(F,x).xreplace(at_origin);Fy=sp.diff(F,y).xreplace(at_origin)
        Gx=sp.diff(G,x).xreplace(at_origin);Gy=sp.diff(G,y).xreplace(at_origin)
        return sp.expand(Fx*Gy-Fy*Gx)

    def regenerate(self,cert,jacobian_method='direct'):
        before=self.mapping(cert['map_before']);raw=self.rows(cert['raw_new_rows_before_reduction'])
        labels=[label for label,_ in raw];pi=sp.Symbol('pi')
        # Reconstruct each family once.  At the last stage its preceding locus
        # is often small; direct F/G differentiation is independent of the
        # accelerated product-rule Jacobian emitter used by the driver.
        local_requests={};jrequests=[];targets=[];outer_d1=[];wrappers=[];d1_j=[];origin_j=[];graph=[];weak_graph=[];weak_residual=[]
        for label in labels:
            if label.startswith('weak_graph_target_'):
                weak_graph.append((label,label.removeprefix('weak_graph_target_')));continue
            if label.startswith('weak_residual_'):
                weak_residual.append((label,label.removeprefix('weak_residual_')));continue
            m=re.search(r'_J_t(\d+)_d(\d+)_k(\d+)$',label)
            if m:jrequests.append((label,*map(int,m.groups())));continue
            if label.endswith('_nonzero_J_wrapper') or label=='gauge_J_nonzero_wrapper':wrappers.append(label);continue
            m=re.match(r'(?:gauge_)?D1_J_face_Pi(\d+)$',label)
            if m:d1_j.append((label,int(m.group(1))));continue
            m=re.match(r'derived_D1_graph_(H2|A2|A3|B1|B2)_Pi(\d+)$',label)
            if m:graph.append((label,m.group(1),int(m.group(2))));continue
            if label=='gauge_early_J_constant':origin_j.append(label);continue
            m=re.search(r'_(C2|C3|A2|A3|B1|B2|H2|F|G)(?:_minor)?_local(\d+)_coord(\d+)$',label)
            if m:
                name,n,k=m.groups();local_requests[label]=(name,int(n),int(k));continue
            m=re.match(r'(A2|A3|B1|B2)_D1_s(\d+)_k(\d+)$',label)
            if m:outer_d1.append((label,m.group(1),int(m.group(2)),int(m.group(3))));continue
            m=re.match(r'accelerated_(H2|F|G)_minor_target_coord(\d+)$',label)
            if m:targets.append((label,m.group(1),int(m.group(2))));continue
            raise AssertionError(('unknown raw source row family',label))
        full_j_phase=re.fullmatch(r'Jacobian_t(\d+)',cert['phase'])
        if full_j_phase:
            tp=int(full_j_phase.group(1));degree=self.S['n']+self.S['m']-2-tp
            assert degree>=0
            existing={label for label,*_ in jrequests}
            for k in range(degree+1):
                label=f'resumed_J_t{tp}_d{degree}_k{k}'
                if label not in existing:jrequests.append((label,tp,degree,k))
        regenerated={};backend_metadata=[]
        for label,name,offset,k in outer_d1:
            W=self.S['outer_specs'][name][1]+offset
            value=sum(comb(q,k)*v for (r,q),v in self.outer[name].items() if self.e.weight((r,q))==W and q>=k)
            regenerated[label]=sp.expand(sp.sympify(value).xreplace(before))
        maxlocal=max([n for name,n,k in local_requests.values()]+[0])
        if targets:
            maxlocal=max(maxlocal,max(self.S['minor'][self.branch][name+'_local_floor'] for _,name,_ in targets if name in ('F','G')) if any(name in ('F','G') for _,name,_ in targets) else self.S['minor'][self.branch]['h3_local_floor']*self.S['inner_power'])
        d=self.S['minor'][self.branch]['cover']
        local_cache={}
        def get_local(name,limit):
            key=(name,limit)
            if key in local_cache:return local_cache[key]
            if name in ('C2','C3'):poly=self.apply(self.c2 if name=='C2' else self.c3,before,(limit+d-1)//d)
            elif name in self.outer:poly=self.apply(self.outer[name],before,(limit+d-1)//d)
            else:
                H,outer=self.blocks(before,(limit+d-1)//d)
                if name=='H2':poly=H
                else:
                    F,G=self.e.build_FG(H,outer,(limit+d-1)//d)
                    poly=F if name=='F' else G
            # Independent raw composition is intentionally separate from
            # minor_maps.local_rows, whose output the main driver used.
            local_cache[key]=self.independent_local(poly,limit,exact_only=True)
            return local_cache[key]
        P=self.S['minor'][self.branch]['h3_face'].xreplace(before)
        h3floor=self.S['minor'][self.branch]['h3_local_floor'];h2floor=h3floor*self.S['inner_power']
        for label,(name,n,k) in local_requests.items():
            value=get_local(name,n).get((n,k),sp.Integer(0))
            if name in ('H2','F','G'):
                floor=h2floor if name=='H2' else self.S['minor'][self.branch][name+'_local_floor']
                exponent=self.S['inner_power'] if name=='H2' else (self.S['n'] if name=='F' else self.S['m'])//self.S['h3_degree']
                if n==floor:value-=sp.Poly(sp.expand(P**exponent),pi).coeff_monomial(pi**k)
            regenerated[label]=sp.expand(value)
        target_expr={}
        if targets:
            def leader(name,floor):return sp.expand(sum(v*pi**k for (n,k),v in get_local(name,floor).items() if n==floor))
            if any(name=='H2' for _,name,_ in targets):
                target_expr['H2']=sp.expand(leader('C2',2*h3floor)*P+leader('C3',3*h3floor))
            if any(name in ('F','G') for _,name,_ in targets):
                faces={}
                for name in self.outer:
                    deg=self.S['outer_specs'][name][0]+1
                    faces[name]=leader(name,(deg//self.S['k2_degree'])*h2floor-d)
                target_expr['F']=sp.expand(faces['A2']*P**self.S['inner_power']+faces['A3'])
                target_expr['G']=sp.expand(faces['B1']*P**self.S['inner_power']+faces['B2'])
            for label,name,k in targets:regenerated[label]=sp.Poly(target_expr[name],pi).coeff_monomial(pi**k)
        if jrequests:
            cap=max(tp for _,tp,_,_ in jrequests)
            if jacobian_method=='flint-direct':
                helper=importlib.import_module('minor_flint_quotient_direct' if self.quotient is not None else 'minor_flint_direct')
                assert Path(helper.__file__).resolve().parent==Path(__file__).resolve().parent,'independent FLINT helper came from another directory'
                h,c2,c3=[self.apply(poly,before,cap) for poly in (self.h,self.c2,self.c3)]
                outer={name:self.apply(poly,before,cap) for name,poly in self.outer.items()}
                bands={}
                for tp in sorted({tp for _,tp,_,_ in jrequests}):
                    bands[tp],_metadata=(helper.band(h,c2,c3,outer,tp,self.S,self.quotient,self.quotient_generator) if self.quotient is not None else helper.band(h,c2,c3,outer,tp,self.S))
                    backend_metadata.append(_metadata)
            elif jacobian_method=='direct':
                H,outer=self.blocks(before,cap)
                F,G=self.e.build_FG(H,outer,cap)
                bands={tp:self.e.jacobian_band(F,G,tp) for tp in sorted({tp for _,tp,_,_ in jrequests})}
            else:
                H,outer=self.blocks(before,cap)
                helper=importlib.import_module('deep_rows')
                bands=helper.all_w_bands(helper.jacobian_factored(H,outer,cap),cap)
            for _tp,_band in bands.items():
                assert all(0<=_k<=self.S['n']+self.S['m']-2-_tp for _k in _band),'Jacobian coefficient outside total-degree support'
            for label,tp,degree,k in jrequests:
                assert degree==self.S['n']+self.S['m']-2-tp
                value=bands[tp].get(k,sp.Integer(0))
                if degree==0 and k==0:value-=sp.Symbol('Jc').xreplace(before)
                regenerated[label]=sp.expand(value)
            if full_j_phase:
                nf=lambda value:sp.rem(value,self.quotient,self.quotient_generator) if self.quotient is not None else value
                expected={label for label,_tp,_degree,_k in jrequests if nf(regenerated[label])!=0}
                if self.quotient is None:
                    assert expected==set(labels),('complete Jacobian band omits a nonzero coefficient',expected^set(labels))
                else:
                    assert expected<=set(labels)<=set(regenerated),'complete quotient Jacobian band omits a nonzero class or adds an unknown coefficient'
        for label in wrappers:regenerated[label]=sp.expand((sp.Symbol('Jc')*sp.Symbol('ZJ')-1).xreplace(before))
        if d1_j:
            face=sp.Poly(self.independent_d1_face(before)-sp.Symbol('Jc').xreplace(before),sp.Symbol('Pi'))
            for label,k in d1_j:regenerated[label]=face.coeff_monomial(sp.Symbol('Pi')**k)
        if origin_j:
            value=self.independent_origin_constant(before)-sp.Symbol('Jc').xreplace(before)
            for label in origin_j:regenerated[label]=value
        if graph:
            actual=self.independent_d1_source_faces(before)
            assert self.graph_faces is not None,'graph rows lack a declared complete face map'
            Pi=sp.Symbol('Pi');definitions={}
            for label,name,k in graph:
                variable=sp.Symbol(f'Zface_{name}_{k}')
                assert variable in self.extra_generators
                value=sp.Poly(actual[name],Pi).coeff_monomial(Pi**k)
                regenerated[label]=variable-value
                definitions[variable]=value
            for name,value in self.graph_faces.items():
                assert sp.expand(value.xreplace(definitions)-actual[name])==0,('graph face loses or pins a source coefficient',name)
        if weak_graph or weak_residual:
            assert self.weak_map is not None and self.weak_residual is not None,'merge lacks a verified second source graph'
            expected={f'weak_graph_target_{variable}':sp.expand((variable-value).xreplace(before)) for variable,value in self.weak_map.items()}
            expected.update({f'weak_residual_{label}':sp.expand(value.xreplace(before)) for label,value in self.weak_residual})
            expected={label:value for label,value in expected.items() if value!=0}
            assert set(expected)=={label for label,_ in weak_graph+weak_residual},'merge omits a nonzero graph relation or adds an undeclared one'
            regenerated.update(expected)
        got=[(label,sp.expand(regenerated[label])) for label in labels]
        use_quotient=self.quotient is not None and bool(jrequests)
        differences=[(label,sp.expand(a-b)) for (label,a),(_,b) in zip(got,raw)]
        if use_quotient:
            mismatches=[label for label,difference in differences if sp.rem(difference,self.quotient,self.quotient_generator)!=0]
        else:mismatches=[label for label,difference in differences if difference!=0]
        assert not mismatches,('raw source regeneration mismatch',mismatches[:5])
        if not use_quotient:assert self.e.rows_hash(got)==cert['raw_new_rows_hash']
        return {'raw_rows_regenerated_before_reduction':len(got),'all_images_equal':True,
                'row_hash':self.e.rows_hash(got),'recorded_raw_row_hash':cert['raw_new_rows_hash'],
                'equality_in_declared_monic_quotient':str(self.quotient) if use_quotient else None,
                'raw_minus_regenerated_is_multiple_of_imposed_monic_row':use_quotient,
                'jacobian_method':jacobian_method,
                'local_method':'independent repeated polynomial substitution',
                'backend_metadata':backend_metadata,
                'D1_method':'independent e,Pi series multiplication and symbolic physical chain rule' if d1_j else None,
                'origin_method':'independent physical first Taylor polynomials and differentiation' if origin_j else None}

    def replay_phase(self,cert):
        assert cert['field']=='Q' and cert['branch']==self.branch
        assert cert['localizer']==str(self.loc)
        before=self.mapping(cert['map_before']);after=self.mapping(cert['map_after'])
        ambient=set(self.basefree)
        ambient|={v for v in self.extra_generators if any(str(v) in cert[key] for key in ('free_before','map_before','map_after'))}
        if any(name in cert['free_before'] or name in cert['map_before'] or name in cert['map_after'] for name in ('Jc','ZJ')):
            ambient|=set(map(sp.Symbol,['Jc','ZJ']))
        assert set(map(sp.Symbol,cert['free_before']))==ambient-set(before)
        assert set(map(sp.Symbol,cert['free_after']))==ambient-set(after)
        assert set(before)<=set(after)
        raw=self.rows(cert['raw_new_rows_before_reduction'])
        assert self.e.rows_hash(raw)==cert['raw_new_rows_hash']
        pending=[(label,row) for label,row in self.rows(cert['residual_before'])+raw if row!=0]
        assert len({label for label,_ in pending})==len(pending)
        localmap={};used_radicals=set()
        def add_available_radicals():
            available=dict(pending)
            for i,c in enumerate(cert['radical_steps']):
                if i in used_radicals:continue
                src=self.expr(c['source_polynomial']);factor=self.expr(c['factor'])
                unit=sp.Rational(c['rational_unit']);power=int(c['power'])
                assert unit!=0 and power>1 and sp.expand(src-unit*factor**power)==0
                if c['source_row'] in available and sp.expand(available[c['source_row']]-src)==0:
                    pending.append((c['new_row'],factor));used_radicals.add(i)
        for p in cert['pivot_steps']:
            add_available_radicals()
            variable=self.locals[p['variable']]
            assert variable in ambient-set(before)-set(localmap) and variable!=self.loc
            assert variable not in self.quotient_parameters,'protected quotient coordinate was eliminated'
            coefficient=sp.Rational(p['rational_leader']);assert coefficient!=0
            rhs=self.expr(p['rhs_at_pivot']);selected=self.expr(p['selected_equation_at_pivot'])
            candidates=[row for label,row in pending if label==p['label']]
            assert len(candidates)==1,('pivot row missing',p['label'])
            row=candidates[0]
            assert sp.diff(row,variable)==coefficient
            assert variable not in rhs.free_symbols
            assert sp.expand(row-selected)==0 and sp.expand(row-coefficient*(variable-rhs))==0
            localmap[variable]=rhs
            pending=[(label,image) for label,old in pending if label!=p['label']
                     and (image:=sp.expand(old.subs(variable,rhs)))!=0]
        add_available_radicals()
        assert len(used_radicals)==len(cert['radical_steps']),'unverified radical source membership'
        # Reverse the actual triangular pivot order, then apply the resulting
        # simultaneous substitution once to the already resolved preceding
        # graph. This avoids rescanning unchanged high-degree images.
        resolved={}
        for variable,rhs in reversed(list(localmap.items())):
            resolved[variable]=sp.expand(rhs.xreplace(resolved)) if self.symbols(rhs)&set(resolved) else rhs
        combined={variable:(sp.expand(rhs.xreplace(resolved)) if self.symbols(rhs)&set(resolved) else rhs)
                  for variable,rhs in before.items()}
        combined.update(resolved)
        assert self.equal_map(combined,after),'phase map does not follow from certified pivots'
        claimed=self.rows(cert['residual_after'])
        assert self.e.rows_hash(claimed)==cert['residual_after_hash']
        pdict={label:row for label,row in pending};cdict=dict(claimed)
        assert set(pdict)==set(cdict),('residual row set mismatch',set(pdict)^set(cdict))
        assert all(sp.expand(pdict[label]-cdict[label])==0 for label in pdict)
        if self.quotient is not None:
            assert any(sp.expand(row-self.quotient)==0 for _,row in claimed),'explicit imposed monic quotient generator was lost'
            assert not self.quotient_parameters&set(after)
        return {'phase':cert['phase'],'QQstar_pivots_verified':len(cert['pivot_steps']),
                'radical_power_memberships_verified':len(used_radicals),
                'map_images_verified':len(after),'remaining_generators':len(ambient-set(after)),
                'residual_rows_verified':len(claimed)}


def singular_replay(rows,branch,remaining_count,path):
    loc=sp.Symbol('rho' if branch=='delta2' else 'c');wrapper=sp.Symbol('Zrho' if branch=='delta2' else 'Zc')
    active=sorted(set().union(*(v.free_symbols for _,v in rows))|{loc},key=str)
    assert wrapper not in active
    ringvars=active+[wrapper]
    integer_rows=[];scalings=[]
    for label,value in rows:
        polynomial=sp.Poly(value,*active,domain=sp.QQ)
        denominator,integral=polynomial.clear_denoms(convert=True)
        content,primitive=integral.primitive()
        multiplier=sp.Rational(denominator,content) if content else sp.Integer(1)
        integer=primitive.as_expr()
        assert sp.expand(integer-multiplier*value)==0 and multiplier!=0
        encoded=str(integer).replace('**','^')
        assert '/' not in encoded,'rational coefficient leaked into Singular parser'
        integer_rows.append(encoded)
        scalings.append({'row':label,'QQstar_multiplier':str(multiplier),
                         'primitive_integer_polynomial_sha256':hashlib.sha256(sp.srepr(integer).encode()).hexdigest(),
                         'exact_identity_verified':True})
    raw=','.join(integer_rows) or '0'
    script=(f'ring R=0,({",".join(map(str,ringvars))}),dp;\n'
            'print("BEGIN_RING");print(char(R));print(nvars(R));\n'
            'int i;for(i=1;i<=nvars(R);i++){print(var(i));}\nprint("END_RING");\n'
            f'ideal Raw={raw};ideal I=Raw,{wrapper}*{loc}-1;ideal B=std(I);\n'
            'print("BEGIN_DIM");print(dim(B));print(reduce(1,B));print("END_DIM");\n'
            'print("BEGIN_BASIS");print(B);print("END_BASIS");\n'
            f'ideal Empty={loc},{wrapper}*{loc}-1;ideal Point={loc}-1,{wrapper}*{loc}-1;\n'
            'print("BEGIN_CONTROLS");print(reduce(1,std(Empty)));print(reduce(1,std(Point)));print(reduce(1,std(Raw)));print("END_CONTROLS");\nquit;\n')
    path.write_text(script)
    proc=subprocess.run(['Singular','-q'],input=script,text=True,capture_output=True,check=True)
    path.with_suffix('.sing.out').write_text(proc.stdout+proc.stderr)
    assert '?' not in proc.stdout and not proc.stderr.strip(),(proc.stdout[-3000:],proc.stderr)
    def section(name):return proc.stdout.split('BEGIN_'+name+'\n',1)[1].split('\nEND_'+name,1)[0].strip().splitlines()
    ring=section('RING');assert ring[:2]==['0',str(len(ringvars))] and ring[2:]==list(map(str,ringvars))
    dimline=section('DIM');d=int(dimline[0]);unit=dimline[1]=='0';assert unit==(d<0)
    controls=section('CONTROLS');assert controls[:2]==['0','1']
    dimension=-1 if unit else remaining_count-(len(active)-d)
    return {'field':'Q','generator_order':list(map(str,ringvars)),
            'generator_order_sha256':hashlib.sha256(('\n'.join(map(str,ringvars))+'\n').encode()).hexdigest(),
            'ring_characteristic_checked':0,'active_dimension':d,'full_dimension':dimension,'unit_ideal':unit,
            'empty_wrapper_reduces_one_to':controls[0],'nonempty_wrapper_reduces_one_to':controls[1],
            'raw_ideal_reduces_one_to':controls[2],
            'rational_export':'each row scaled by a verified nonzero rational to a primitive integer polynomial before serialization',
            'QQstar_export_scalings':scalings,
            'basis_sha256':hashlib.sha256(('\n'.join(section('BASIS'))+'\n').encode()).hexdigest(),
            'script_sha256':digest(path)}


def local_certificate_path(value,result_path):
    path=Path(value)
    if path.exists():return path.resolve()
    path=result_path.parent/path.name
    if path.exists():return path.resolve()
    matches=sorted({found.resolve() for root in PATH_ROOTS for found in Path(root).rglob(Path(value).name) if found.is_file()})
    assert len(matches)==1,('certificate missing or ambiguous in declared relocation roots',value,[str(x) for x in matches])
    return matches[0]


def main():
    p=argparse.ArgumentParser();p.add_argument('--result',type=Path);p.add_argument('--certificate',type=Path)
    p.add_argument('--resume',type=Path,help='A resume harness result extending an exact complete source checkpoint; requires --result and --chain.')
    p.add_argument('--resume-driver',type=Path,help='Exact resume harness file whose recorded SHA-256 is checked.')
    p.add_argument('--certificate-root',type=Path,action='append',default=[],help='Explicit relocation root; every relocated phase is still checked against its recorded SHA-256.')
    p.add_argument('--code-dir',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--gauge',action='store_true',help='Import the audited jet0=0 wrapper for a phase-only test; final results autodetect it.')
    p.add_argument('--chain',action='store_true',help='Replay every saved phase algebraically; regenerate terminal raw rows independently.')
    p.add_argument('--jacobian-method',choices=['direct','factored','flint-direct'],default='direct');a=p.parse_args()
    PATH_ROOTS.extend(path.resolve() for path in a.certificate_root)
    assert a.result or a.certificate
    started=time.monotonic();result=json.loads(a.result.read_text()) if a.result else None
    resumed=json.loads(a.resume.read_text()) if a.resume else None
    if resumed:assert result and a.chain and not a.certificate,'resumed endpoint needs a source result and full chain replay'
    branch=result['branch'] if result else json.loads(a.certificate.read_text())['branch']
    hashes={name:digest(a.code_dir/name) for name in ['engine.py','source_data.py','deep_rows.py','deep_driver.py','minor_maps.py']}
    if (a.code_dir/'deep_accelerated.py').exists():hashes['deep_accelerated.py']=digest(a.code_dir/'deep_accelerated.py')
    if (a.code_dir/'d1_jacobian_face.py').exists():hashes['d1_jacobian_face.py']=digest(a.code_dir/'d1_jacobian_face.py')
    resume_custody=None
    if resumed:
        assert resumed['branch']==branch
        for name,want in resumed['code_sha256'].items():
            assert (a.code_dir/name).is_file() and digest(a.code_dir/name)==want,('resume code custody mismatch',name)
        driver=a.resume_driver or a.resume.resolve().parent/'deep_resume_faces.py'
        assert digest(driver)==resumed['driver_sha256'],'resume driver custody mismatch'
        resume_custody={'path':str(a.resume.resolve()),'sha256':digest(a.resume),
                        'driver_path':str(driver.resolve()),'driver_sha256':digest(driver),
                        'all_snapshot_code_hashes_checked':True}
    if result:
        for key,name in [('engine_sha256','engine.py'),('source_derivation_sha256','source_data.py'),('helpers_sha256','deep_rows.py'),('driver_sha256','deep_driver.py')]:
            assert result[key]==hashes[name],('code custody mismatch',key)
        if result.get('accelerated_deep_block'):
            assert result['accelerated_deep_block']['accelerated_driver_sha256']==hashes['deep_accelerated.py']
    gauge=a.gauge or bool(result and result.get('initial_inner',{}).get('gauge_slice'))
    gauge_record=None
    if gauge:
        wrapper_path=a.code_dir/'deep_gauge_accelerated.py'
        hashes['deep_gauge_accelerated.py']=digest(wrapper_path)
        if result:
            assert hashes['deep_gauge_accelerated.py']==result['initial_inner']['gauge_slice']['wrapper_sha256']
            if 'gauge_wrapper_sha256' in result:assert hashes['deep_gauge_accelerated.py']==result['gauge_wrapper_sha256']
        gauge_record={'ring_map':{'jet0':'0'},'global_inverse_transport':'T_(-jet0)',
            'full_chart_coverage':'audited polynomial torsor X = X_(jet0=0) x A1',
            'proof_audit':'minor_gauge-final-audit.md','all_other_centres_retained':True}
    e=load_code(a.code_dir,gauge);v=Verifier(e,branch)
    source=v.check_source(result) if result else {'scope':'phase-only test; reconstructed source chart but no final result compared'}
    if resumed:
        if gauge:assert resumed['source_gauge']['wrapper_sha256']==hashes['deep_gauge_accelerated.py']
        graph_records=[phase for phase in resumed['phases'] if phase['name']=='D1_graph']
        assert len(graph_records)<=1
        if graph_records:
            meta=graph_records[0]['derivation'];declared=meta['protected_during_graph_elimination']
            assert len(declared)==len(set(declared))
            assert all(re.fullmatch(r'Zface_(H2|A2|A3|B1|B2)_\d+',name) for name in declared)
            v.extra_generators=set(map(sp.Symbol,declared))
            assert not v.extra_generators&set(v.locals.values())
            v.locals.update({str(x):x for x in v.extra_generators})
            face_locals={**v.locals,'Pi':sp.Symbol('Pi')}
            v.graph_faces={}
            assert set(meta['graph_faces'])=={'H2','A2','A3','B1','B2'}
            for name,encoded in meta['graph_faces'].items():
                assert set(re.findall(r'[A-Za-z_][A-Za-z_0-9]*',encoded))<=set(face_locals)
                value=sp.sympify(encoded,locals=face_locals)
                assert not value.atoms(sp.Float) and all(p.exp.is_Integer and p.exp>=0 for p in value.atoms(sp.Pow))
                assert value.free_symbols<=v.extra_generators|{sp.Symbol('Pi')}
                v.graph_faces[name]=value
    if resumed:
        links=resumed['checkpoint_chain']
        assert links and resumed['phases'],'resume result lacks a completed new phase'
        paths=[]
        for index,link in enumerate(links):
            path=local_certificate_path(link['path'],a.resume.resolve())
            assert digest(path)==link['sha256'],'resume checkpoint chain hash mismatch'
            assert re.search(r'_phase%04d\.json$'%index,path.name),'resume checkpoint chain is not contiguous'
            paths.append(path)
        assert digest(paths[-1])==resumed['checkpoint_sha256'],'resume checkpoint endpoint differs'
        checkpoint=json.loads(paths[-1].read_text())
        assert checkpoint['phase']==resumed['checkpoint_phase'] and checkpoint['phase'].startswith('accelerated_FG_targets_local')
        for phase in resumed['phases']:
            path=local_certificate_path(phase['phase_certificate'],a.resume.resolve())
            assert digest(path)==phase['phase_certificate_sha256'],'resume new-phase custody mismatch'
            paths.append(path)
    elif a.certificate and a.chain:
        assert result,'chain through an explicit checkpoint needs a source-state result'
        endpoint=a.certificate.resolve()
        match=re.fullmatch(r'(.+)_phase(\d+)\.json',endpoint.name)
        assert match,'checkpoint filename lacks a declared phase serial'
        prefix,number=match.group(1),int(match.group(2))
        paths=[endpoint.parent/f'{prefix}_phase{i:04d}.json' for i in range(number+1)]
        assert all(path.exists() for path in paths),'saved checkpoint chain is incomplete'
    elif a.certificate:paths=[a.certificate.resolve()]
    else:
        assert result.get('last_phase_certificate'),'NO_PHASE_PROVENANCE: final map alone does not certify source-locus coverage'
        paths=[local_certificate_path(x,a.result.resolve()) for x in (result['phase_certificate_paths'] if a.chain else [result['last_phase_certificate']])]
    phase_reports=[];previous=None
    for phase_index,path in enumerate(paths):
        cert=json.loads(path.read_text())
        if a.chain and previous is None:
            assert cert['phase']=='source_residue' and not cert['map_before'] and not cert['residual_before'], 'chain does not start at the reconstructed source chart'
        if previous:
            assert v.equal_map(v.mapping(previous['map_after']),v.mapping(cert['map_before'])),'phase map chain broken'
            assert v.rows(previous['residual_after'])==v.rows(cert['residual_before']),'phase residual chain broken'
        phase_report={'path':str(path),'sha256':digest(path),**v.replay_phase(cert)}
        if resumed and cert['phase'] in ('D1_graph','D1_J','corner_J'):
            phase_report['independent_raw_regeneration']=v.regenerate(cert,a.jacobian_method)
        phase_reports.append(phase_report)
        if phase_index%20==0 or phase_index==len(paths)-1:
            print(f'verified phase {phase_index+1}/{len(paths)}: {cert["phase"]}',flush=True)
        previous=cert
    cert=previous
    regenerated=v.regenerate(cert,a.jacobian_method)
    rows=v.rows(cert['residual_after']);remaining=len(cert['free_after'])
    replay=singular_replay(rows,branch,remaining,a.out.with_suffix('.sing'))
    if resumed:
        last=resumed['phases'][-1]
        assert replay['full_dimension']==last['dimension'] and replay['unit_ideal']==last['unit_ideal'],'resumed endpoint dimension/unit mismatch'
    elif result and not a.certificate:
        assert v.equal_map(v.mapping(cert['map_after']),v.mapping(result['cumulative_map']))
        assert v.rows(result['remaining_residual'])==rows
        if result['records']:
            last=result['records'][-1]
            assert replay['full_dimension']==last['dimension'],('dimension differs',replay,last['dimension'])
    output={'type':'INDEPENDENT EXACT-Q SOURCE/PHASE/ENDPOINT VERIFICATION','branch':branch,
            'scope':('full saved source checkpoint chain and necessary-face resume chain plus regenerated endpoint' if resumed else ('full saved reduction chain through explicit checkpoint; original result is source-state custody only' if a.certificate else 'full saved reduction chain plus regenerated endpoint')) if a.chain and result else 'terminal phase plus reconstructed source maps; preceding chain requires saved-phase audit',
            'code_hashes':hashes,'source':source,'gauge_transport':gauge_record,'phase_certificates':phase_reports,'resume_custody':resume_custody,
            'terminal_raw_regeneration':regenerated,'Singular':replay,
            'ambient_source_generator_order':sorted(map(str,v.basefree)),
            'declared_exact_graph_extension_generators':sorted(map(str,v.extra_generators)),
            'ambient_source_generator_order_sha256':hashlib.sha256(('\n'.join(sorted(map(str,v.basefree)))+'\n').encode()).hexdigest(),
            'elapsed_seconds':time.monotonic()-started,'status':'PASS'}
    output['verifier_sha256_at_import']=VERIFIER_SHA256_AT_IMPORT
    if gauge:
        output['gauge_slice_dimension']=replay['full_dimension']
        output['free_centre_dimension_by_audited_transport']=-1 if replay['unit_ideal'] else replay['full_dimension']+1
    a.out.write_text(json.dumps(output,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','branch':branch,'phases_verified':len(paths),'dimension':replay['full_dimension'],'unit':replay['unit_ideal'],'seconds':output['elapsed_seconds']},indent=2))
if __name__=='__main__':main()
