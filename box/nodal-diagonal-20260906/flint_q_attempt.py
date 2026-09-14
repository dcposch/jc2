#!/usr/bin/env python3
"""Exact rational expansion using the host's installed FLINT shared library.

The FFI is independently controlled before any coefficient build. No package
or artifact tree is installed. All polynomial elimination pivots are in Q*.
"""
import ctypes as CT
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json
import resource
import sys
import time
import sympy as S
import expanded_q_attempt as EP
import boundary_maps as BM
import boundary_full_dag as BD


resource.setrlimit(resource.RLIMIT_CORE,(0,0))
LIB=CT.CDLL('/usr/lib/x86_64-linux-gnu/libflint.so.18.0.1');V=CT.c_void_p
DEFS={
 'fmpq_mpoly_ctx_init':(None,[V,CT.c_long,CT.c_int]),
 'fmpq_mpoly_init':(None,[V,V]),'fmpq_mpoly_clear':(None,[V,V]),
 'fmpq_mpoly_set_str_pretty':(CT.c_int,[V,CT.c_char_p,V,V]),
 'fmpq_mpoly_get_str_pretty':(V,[V,V,V]),
 'fmpq_mpoly_add':(None,[V,V,V,V]),'fmpq_mpoly_mul':(None,[V,V,V,V]),
 'fmpq_mpoly_is_fmpq':(CT.c_int,[V,V]),'fmpq_mpoly_length':(CT.c_long,[V,V]),
 'fmpq_mpoly_compose_fmpq_mpoly':(CT.c_int,[V,V,V,V,V]),
 'fmpq_mpoly_gen':(None,[V,CT.c_long,V]),
 'fmpq_mpoly_evaluate_all_fmpq':(CT.c_int,[V,V,V,V]),
 'fmpq_init':(None,[V]),'fmpq_clear':(None,[V]),
 'fmpq_set_si':(None,[V,CT.c_long,CT.c_ulong]),
 'fmpq_get_str':(V,[V,CT.c_int,V]),'flint_free':(None,[V]),
}
for name,(rest,args) in DEFS.items():
    f=getattr(LIB,name);f.restype=rest;f.argtypes=args
N=len(EP.NAMES);CTX=(CT.c_long*512)();LIB.fmpq_mpoly_ctx_init(CTX,N,2)
PRETTY=(CT.c_char_p*N)(*[f'v{i}'.encode() for i in range(N)])
SYMBOLS={f'v{i}':S.Symbol(name) for i,name in enumerate(EP.NAMES)}
CURRENT=None


class FP:
    def __init__(self):
        self.buf=(CT.c_long*128)();LIB.fmpq_mpoly_init(self.buf,CTX)
    def __del__(self):
        try:LIB.fmpq_mpoly_clear(self.buf,CTX)
        except Exception:pass
    @classmethod
    def parse(cls,s):
        p=cls();assert LIB.fmpq_mpoly_set_str_pretty(p.buf,str(s).encode(),PRETTY,CTX)==0
        return p
    def string(self):
        ptr=LIB.fmpq_mpoly_get_str_pretty(self.buf,PRETTY,CTX)
        try:return CT.string_at(ptr).decode()
        finally:LIB.flint_free(ptr)
    def terms(self):return int(LIB.fmpq_mpoly_length(self.buf,CTX))
    def constant(self):return Q(self.string()) if LIB.fmpq_mpoly_is_fmpq(self.buf,CTX) else None
    def add(self,other):
        p=FP();LIB.fmpq_mpoly_add(p.buf,self.buf,other.buf,CTX);return p
    def mul(self,other):
        p=FP();LIB.fmpq_mpoly_mul(p.buf,self.buf,other.buf,CTX);return p
    def substitute(self,index,rhs):
        vv=[rhs if i==index else FLINT_GENS[i] for i in range(N)]
        args=(V*N)(*[CT.addressof(p.buf) for p in vv]);out=FP()
        assert LIB.fmpq_mpoly_compose_fmpq_mpoly(out.buf,self.buf,args,CTX,CTX)==1
        return out
    def sympy(self):return EP.RING.from_expr(S.sympify(self.string(),locals=SYMBOLS))
    @classmethod
    def from_sympy(cls,p):
        terms=[]
        for mon,c in p.items():
            factors=[f'({c})']+[f'v{i}'+(f'^{e}' if e>1 else '') for i,e in enumerate(mon) if e]
            terms.append('*'.join(factors))
        return cls.parse('+'.join(terms) if terms else '0')
    def evaluate(self,vals):
        out=(CT.c_long*2)();LIB.fmpq_init(out)
        arr=(V*N)(*[CT.addressof(v) for v in vals])
        assert LIB.fmpq_mpoly_evaluate_all_fmpq(out,self.buf,arr,CTX)==1
        ptr=LIB.fmpq_get_str(None,10,out)
        try:return Q(CT.string_at(ptr).decode())
        finally:LIB.flint_free(ptr);LIB.fmpq_clear(out)


FLINT_GENS=[]
for i in range(N):
    p=FP();LIB.fmpq_mpoly_gen(p.buf,i,CTX);FLINT_GENS.append(p)


class FV:
    def __init__(self,C,p):
        self.C=C;self.p=p;self.version=len(C.maps);self.cached_constant='unset'
    @property
    def poly(self):
        for index,rhs,_ in self.C.maps[self.version:]:
            self.p=self.p.substitute(index,rhs);self.cached_constant='unset'
        self.version=len(self.C.maps);return self.p
    @property
    def constant(self):
        p=self.poly
        if self.cached_constant=='unset':self.cached_constant=p.constant()
        return self.cached_constant
    @property
    def digest(self):return sha256(self.poly.string().encode()).digest()
    @property
    def values(self):return tuple(self.poly.evaluate(v) for v in self.C.values)


class FC:
    def __init__(self):
        global CURRENT
        CURRENT=self;self.nodes=0;self.constants={};self.free_names=[];self.maps=[]
        self.residuals=[];self.pivot_receipts=[];self.blocks=[];self.first_unit=None;self.max_terms=0
        self.values=[]
        for _ in range(2):
            point=[]
            for _ in range(N):
                v=(CT.c_long*2)();LIB.fmpq_init(v);point.append(v)
            self.values.append(point)
    def checked(self,p):
        self.nodes+=1;self.max_terms=max(self.max_terms,p.terms());return FV(self,p)
    def const(self,v):
        v=Q(v)
        if v not in self.constants:self.constants[v]=self.checked(FP.parse(v))
        return self.constants[v]
    def var(self,name,values,free=False):
        if name=='lambda':name='lambda_placeholder'
        if free and name not in self.free_names:self.free_names.append(name)
        i=EP.NAMES.index(name)
        for point,val in zip(self.values,values):
            v=Q(val);LIB.fmpq_set_si(point[i],v.numerator,v.denominator)
        return self.checked(FLINT_GENS[i])
    def add(self,terms):
        out=FP()
        for scalar,value in terms:
            scalar=Q(scalar)
            if not scalar:continue
            p=value.poly if scalar==1 else self.const(scalar).poly.mul(value.poly)
            LIB.fmpq_mpoly_add(out.buf,out.buf,p.buf,CTX)
        c=out.constant()
        return self.const(c) if c is not None else self.checked(out)
    def mul(self,a,b):
        if a.constant==0 or b.constant==0:return self.const(0)
        return self.checked(a.poly.mul(b.poly))
    def power(self,p,n):
        out=[self.const(1)]
        for _ in range(n):out.append(self.mul(out[-1],p))
        return out
    def reduced_sympy(self,p):
        for index,_,rhs in self.maps:p=p.compose(EP.GENS[index],rhs)
        return p
    def absorb(self,name,values):
        new=[v.poly.sympy() for v in values if v.constant!=0]
        self.residuals.extend(new);changed=True
        while changed:
            changed=False;keep=[]
            for p in self.residuals:
                p=self.reduced_sympy(p)
                if not p:continue
                if p.is_ground:
                    self.first_unit={'block':name,'constant':str(p),'pivot_count':len(self.maps)}
                    raise BD.CpuBound('EXACT_Q_UNIT_CANDIDATE_REQUIRES_INDEPENDENT_REPLAY')
                candidates=[]
                for mon,c in p.items():
                    if sum(mon)==1:
                        i=mon.index(1)
                        if sum(1 for mm in p if mm[i])==1:candidates.append((i,c))
                if candidates:
                    i,c=max(candidates);rhs=-(p-c*EP.GENS[i])/c
                    assert p-c*(EP.GENS[i]-rhs)==EP.RING.zero
                    self.maps.append((i,FP.from_sympy(rhs),rhs));changed=True
                    self.pivot_receipts.append({'row_block':name,'variable':EP.NAMES[i],
                        'coefficient':str(c),'rhs_terms':len(rhs),
                        'row_sha256':sha256(repr(sorted(p.items())).encode()).hexdigest(),
                        'rhs_sha256':sha256(repr(sorted(rhs.items())).encode()).hexdigest()})
                else:keep.append(p)
            self.residuals=keep
        self.blocks.append({'name':name,'incoming_nonzero':len(new),'pivots':len(self.maps),
                            'remaining_residuals':len(self.residuals),
                            'residual_terms':sum(map(len,self.residuals))})


class FE(BD.Emit):
    def block(self,name,values):
        CURRENT.absorb(name,values)
        return super().block(name,values)


def controls():
    a=FP.parse('v0^2+1/2*v0*v1+3');b=FP.parse('v1-2')
    assert a.sympy()==EP.GENS[0]**2+EP.GENS[0]*EP.GENS[1]/2+3
    assert a.add(b).sympy()==a.sympy()+b.sympy()
    assert a.mul(b).sympy()==a.sympy()*b.sympy()
    assert a.substitute(0,b).sympy()==a.sympy().compose(EP.GENS[0],b.sympy())
    C=FC();v=C.var('minor_u',(2,-1));w=C.var('minor_v',(3,2))
    assert a.evaluate(C.values[0])==10 and a.evaluate(C.values[1])==3
    assert FP.from_sympy(a.sympy()).string()==a.string()
    return True


def main():
    start=time.monotonic();assert controls()
    BM.Circuit=FC;BD.Emit=FE;BD.physical_boundary=EP.localized_boundary
    set_limit=resource.setrlimit
    def limit(which,amount):
        if which==resource.RLIMIT_AS:amount=(1500*1024**2,1500*1024**2)
        elif which==resource.RLIMIT_CPU:amount=(600,620)
        return set_limit(which,amount)
    resource.setrlimit=limit
    write=Path.write_text
    def redirected(path,data,*args,**kw):
        if path.name=='boundary_full_dag_delta52.json':path=path.with_name('flint_q_internal.json')
        return write(path,data,*args,**kw)
    Path.write_text=redirected;sys.argv=[sys.argv[0],'--client','delta52'];error=None
    try:BD.main()
    except Exception as exc:error=type(exc).__name__+': '+str(exc)
    finally:
        C=CURRENT
        out={'status':'NO_EXACT_IDEAL_DECISION','unit_candidate':C.first_unit,'unexpected_error':error,
             'ffi_exact_Q_controls_passed':True,'coefficient_field':'Q',
             'library':'/usr/lib/x86_64-linux-gnu/libflint.so.18.0.1',
             'generator_order':EP.NAMES,'pivots':C.pivot_receipts,'blocks':C.blocks,
             'remaining_residual_count':len(C.residuals),'maximum_single_polynomial_terms':C.max_terms,
             'cpu_seconds':time.process_time(),'elapsed_seconds':time.monotonic()-start,
             'max_rss_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
             'driver_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
             'expanded_driver_sha256':sha256(Path(__file__).with_name('expanded_q_attempt.py').read_bytes()).hexdigest(),
             'graph_driver_sha256':sha256(Path(__file__).with_name('boundary_full_dag.py').read_bytes()).hexdigest()}
        write(Path(__file__).with_suffix('.json'),json.dumps(out,separators=(',',':'))+'\n')
        print(json.dumps({k:out[k] for k in ['status','unit_candidate','unexpected_error','remaining_residual_count',
                   'maximum_single_polynomial_terms','cpu_seconds','max_rss_KiB']}),flush=True)


if __name__=='__main__':main()
