#!/usr/bin/env python3
"""Bounded EXACT-Q expansion and unit-coefficient graph elimination.

No modular arithmetic. Every nonpivot residual remains in the ideal. This
attempt may stop before a decision; no residual timeout is called proper.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import resource
import sys
import time
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
import boundary_maps as BM
import boundary_full_dag as BD
from boundary_counts import SPECS


START=time.monotonic(); CURRENT=None
CHECK,STATE=BM.build(SPECS[3],{},return_state=True)
NAMES=['minor_u','minor_v','c']+STATE['C'].free_names+['Z_localizer','lambda_placeholder']
del STATE
RING,*GENS=ring(NAMES,QQ)
GMAP=dict(zip(NAMES,GENS));ZEROEXP=(0,)*len(NAMES)


class PValue:
    def __init__(self,C,p):self.C=C;self.p=p;self.version=len(C.maps)
    @property
    def poly(self):
        for index,rhs in self.C.maps[self.version:]:self.p=self.p.compose(GENS[index],rhs)
        self.version=len(self.C.maps)
        return self.p
    @property
    def constant(self):
        p=self.poly
        if p.is_ground:
            v=p.get(ZEROEXP,QQ.zero);return Q(int(v.numerator),int(v.denominator))
        return None
    @property
    def digest(self):
        # Binds the actual reduced polynomial, not an unexpanded syntax tree.
        return sha256(repr(sorted(self.poly.items())).encode()).digest()
    @property
    def values(self):
        ans=[]
        for point in self.C.points:
            value=Q(0)
            for mon,c in self.poly.items():
                v=Q(int(c.numerator),int(c.denominator))
                for i,e in enumerate(mon):
                    if e:v*=point[i]**e
                value+=v
            ans.append(value)
        return tuple(ans)


class Expanded:
    def __init__(self):
        global CURRENT
        CURRENT=self;self.nodes=0;self.constants={};self.free_names=[];self.maps=[]
        self.points=[[Q(0)]*len(NAMES),[Q(0)]*len(NAMES)]
        self.residuals=[];self.pivot_receipts=[];self.first_unit=None
        self.blocks=[];self.max_terms=0;self.names_used=set()
    def checked(self,p):
        self.nodes+=1;self.max_terms=max(self.max_terms,len(p));return PValue(self,p)
    def const(self,v):
        v=Q(v)
        if v not in self.constants:self.constants[v]=self.checked(RING.ground_new(QQ(v.numerator,v.denominator)))
        return self.constants[v]
    def var(self,name,values,free=False):
        if name=='lambda':name='lambda_placeholder'
        if free and name not in self.free_names:self.free_names.append(name)
        self.names_used.add(name);i=NAMES.index(name)
        for point,value in zip(self.points,values):point[i]=Q(value)
        return self.checked(GMAP[name])
    def add(self,terms):
        p=RING.zero
        for scalar,e in terms:
            scalar=Q(scalar)
            if scalar:p+=e.poly*QQ(scalar.numerator,scalar.denominator)
        if p.is_ground:
            v=p.get(ZEROEXP,QQ.zero);return self.const(Q(int(v.numerator),int(v.denominator)))
        return self.checked(p)
    def mul(self,p,q):
        a,b=p.poly,q.poly
        if not a or not b:return self.const(0)
        return self.checked(a*b)
    def power(self,p,n):
        out=[self.const(1)]
        for _ in range(n):out.append(self.mul(out[-1],p))
        return out
    def reduce_poly(self,p):
        for index,rhs in self.maps:p=p.compose(GENS[index],rhs)
        return p
    def absorb(self,name,values):
        fresh=[]
        for value in values:
            p=value.poly
            if p:fresh.append(p)
        self.residuals.extend(fresh)
        changed=True
        while changed:
            changed=False;keep=[]
            for p in self.residuals:
                p=self.reduce_poly(p)
                if not p:continue
                if p.is_ground:
                    self.first_unit={'block':name,'constant':str(p),'pivot_count':len(self.maps)}
                    raise BD.CpuBound('EXACT_Q_LITERAL_UNIT_CANDIDATE_REQUIRES_REPLAY')
                candidates=[]
                for mon,c in p.items():
                    if sum(mon)==1:
                        index=mon.index(1)
                        if sum(1 for mm in p if mm[index])==1:
                            candidates.append((index,c))
                if candidates:
                    index,c=max(candidates)
                    rhs=-(p-c*GENS[index])/c
                    assert not any(mon[index] for mon in rhs)
                    # The identity p=c*(v-rhs) is checked before the graph pivot.
                    assert p-c*(GENS[index]-rhs)==RING.zero
                    self.maps.append((index,rhs))
                    self.pivot_receipts.append({'row_block':name,'variable':NAMES[index],
                        'coefficient':str(c),'rhs_terms':len(rhs),
                        'row_sha256':sha256(repr(sorted(p.items())).encode()).hexdigest(),
                        'rhs_sha256':sha256(repr(sorted(rhs.items())).encode()).hexdigest()})
                    changed=True
                else:keep.append(p)
            self.residuals=keep
        self.blocks.append({'name':name,'incoming_nonzero':len(fresh),
                            'pivots':len(self.maps),'remaining_nonzero_residuals':len(self.residuals),
                            'remaining_residual_terms':sum(map(len,self.residuals))})


class ExpandedEmit(BD.Emit):
    def block(self,name,values):
        # Reduce on every unit-coefficient pivot, retaining all compatibility.
        CURRENT.absorb(name,values)
        return super().block(name,values)


ORIGINAL_BOUNDARY=BD.physical_boundary
def localized_boundary(C,E,name,*args,**kw):
    result=ORIGINAL_BOUNDARY(C,E,name,*args,**kw)
    if '_R_' in name:
        lam=args[-1] if not kw else kw['lam']
        z=C.var('Z_localizer',(1,1));sep=C.var('c',(1,2))
        E.block('actual_separation_lambda_localizer',
                [C.add([(1,C.mul(z,C.mul(sep,lam))),(-1,C.const(1))])])
    return result


def main():
    BM.Circuit=Expanded;BD.Emit=ExpandedEmit;BD.physical_boundary=localized_boundary
    set_limit=resource.setrlimit
    def limit(which,amount):
        if which==resource.RLIMIT_AS:amount=(1400*1024**2,1400*1024**2)
        elif which==resource.RLIMIT_CPU:amount=(600,620)
        return set_limit(which,amount)
    resource.setrlimit=limit
    # Keep the complete circuit receipt separate from this attempt's receipt.
    original_write=Path.write_text
    def redirected(path,data,*args,**kwargs):
        if path.name=='boundary_full_dag_delta52.json':path=path.with_name('expanded_q_internal.json')
        return original_write(path,data,*args,**kwargs)
    Path.write_text=redirected
    sys.argv=[sys.argv[0],'--client','delta52']
    error=None
    try:BD.main()
    except Exception as exc:error=type(exc).__name__+': '+str(exc)
    finally:
        C=CURRENT
        out={'status':'NO_EXACT_IDEAL_DECISION',
             'unit_candidate':C.first_unit if C else None,'unexpected_error':error,
             'coefficient_field':'Q','generator_order':NAMES,
             'pivots':C.pivot_receipts if C else [],'blocks':C.blocks if C else [],
             'remaining_residual_count':len(C.residuals) if C else None,
             'maximum_single_polynomial_terms':C.max_terms if C else None,
             'cpu_seconds':time.process_time(),'elapsed_seconds':time.monotonic()-START,
             'max_rss_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
             'driver_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
             'graph_driver_sha256':sha256(Path(__file__).with_name('boundary_full_dag.py').read_bytes()).hexdigest()}
        # Lists remain compact; no polynomial artifact tree is retained.
        original_write(Path(__file__).with_suffix('.json'),json.dumps(out,separators=(',',':'))+'\n')
        print(json.dumps({k:out[k] for k in ['status','unit_candidate','unexpected_error',
                   'remaining_residual_count','maximum_single_polynomial_terms','cpu_seconds','max_rss_KiB']}),flush=True)


if __name__=='__main__':main()
