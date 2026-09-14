#!/usr/bin/env python3
"""Final exact-Q attempt: equivalent differential characteristic recurrence.

For E=F^2-G^3 and T=3G_t F-2G F_t, G E_t-3G_t E=-F T.
Before pG enters, monic coefficient division makes the two prefix ideals equal.
All later characteristic/source/Jacobian rows remain required.
"""
import ctypes as CT
from collections import OrderedDict
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from math import comb
import json
import resource
import signal
import time
import sympy as S
import flint_q_attempt as FQ
import boundary_maps as BM
import boundary_full_dag as BD


FQ.LIB.fmpq_set_str.argtypes=[FQ.V,CT.c_char_p,CT.c_int]
FQ.LIB.fmpq_set_str.restype=CT.c_int
FQ.LIB.fmpq_mpoly_scalar_mul_fmpq.argtypes=[FQ.V,FQ.V,FQ.V,FQ.V]
FQ.LIB.fmpq_mpoly_scalar_mul_fmpq.restype=None
SCALARS=OrderedDict()


def scalar(v):
    v=Q(v)
    if v not in SCALARS:
        z=(CT.c_long*2)();FQ.LIB.fmpq_init(z)
        assert FQ.LIB.fmpq_set_str(z,str(v).encode(),10)==0
        SCALARS[v]=z
        if len(SCALARS)>2048:
            _,old=SCALARS.popitem(last=False);FQ.LIB.fmpq_clear(old)
    return SCALARS[v]


def bounded_const(self,v):
    v=Q(v)
    if v not in self.constants:
        self.constants[v]=self.checked(FQ.FP.parse(v))
        if len(self.constants)>2048:self.constants.pop(next(iter(self.constants)))
    return self.constants[v]


def fast_add(self,terms):
    out=FQ.FP()
    for sc,value in terms:
        sc=Q(sc)
        if not sc:continue
        p=value.poly
        if sc!=1:
            temp=FQ.FP()
            FQ.LIB.fmpq_mpoly_scalar_mul_fmpq(temp.buf,p.buf,scalar(sc),FQ.CTX)
            p=temp
        FQ.LIB.fmpq_mpoly_add(out.buf,out.buf,p.buf,FQ.CTX)
    c=out.constant()
    return self.const(c) if c is not None else self.checked(out)


def controls():
    assert FQ.controls()
    C=FQ.FC();a=C.var('minor_u',(2,-1));b=C.var('minor_v',(3,2))
    ans=C.add([(Q(2,3),a),(-2,b),(Q(4,7),C.const(1))])
    assert ans.poly.sympy()==Q(2,3)*FQ.EP.GENS[0]-2*FQ.EP.GENS[1]+Q(4,7)
    t=S.Symbol('t');f=1+2*t+3*t*t;g=1-t+4*t**3
    E=f*f-g**3;T=3*S.diff(g,t)*f-2*g*S.diff(f,t)
    assert S.expand(g*S.diff(E,t)-3*S.diff(g,t)*E+f*T)==0


def main():
    start=time.monotonic();FQ.FC.const=bounded_const;FQ.FC.add=fast_add;controls()
    resource.setrlimit(resource.RLIMIT_AS,(1900*1024**2,1900*1024**2))
    resource.setrlimit(resource.RLIMIT_CPU,(600,620))
    signal.signal(signal.SIGXCPU,lambda s,f: (_ for _ in ()).throw(BD.CpuBound('600 CPU seconds')))
    BM.Circuit=FQ.FC;E=FQ.FE();receipt={'status':'RUNNING','coefficient_field':'Q'};phase='G boundary'
    C=None
    try:
        gcheck,state=BM.build(BM.SPECS[3],{},return_state=True);C=state['C']
        n,m=99,66;zero=C.const(0)
        up=C.power(state['u'],n//2);vp=C.power(state['v'],n//3)
        state['centre_products']={(a,b):C.mul(up[a],vp[b])
            for a in range(n//2+1) for b in range((n-2*a)//3+1)}
        G=[state['coeff_y'][m-r] for r in range(m+1)]
        gtop=[v.constant for v in G[0]];assert all(v is not None for v in gtop)
        ftop=[Q(0)]*(n+1)
        for i in range(73):ftop[27+i]=Q(comb(72,i)*(-1)**(72-i))
        F=[[C.const(v) for v in ftop]]
        phase='differential characteristic prefix'
        for r in range(1,n+1):
            pieces=[]
            for i in range(1,min(r,m)+1):
                sc=5*i-2*r
                if sc:pieces.append((sc,BD.multiply(C,G[i],F[r-i])))
            num=BD.add_poly(C,pieces,size=n+m-r+1)
            quot,rem=BD.monic_division(C,num,gtop)
            F.append(BD.add_poly(C,[(Q(1,2*r),quot)],size=n-r+1))
            E.block('differential_characteristic_depth_'+str(r),rem)
            if r%10==0:print(json.dumps({'phase':phase,'depth':r,'cpu_seconds':round(time.process_time(),2),
                'pivots':len(C.maps),'residuals':len(C.residuals),'max_terms':C.max_terms,
                'rss_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
        phase='complete characteristic suffix';G2={};Rphys={};parameter=None
        for r in range(n+1-m,2*m+1):
            pieces=[]
            for i in range(max(0,r-m),min(m,r)+1):
                j=r-i
                if i<=j:pieces.append((1 if i==j else 2,BD.multiply(C,G[i],G[j])))
            G2[r]=BD.add_poly(C,pieces,size=2*m-r+1)
        for r in range(n+1,2*n+1):
            pieces=[]
            for i in range(max(0,r-2*m),min(m,r)+1):
                pieces.append((1,BD.multiply(C,G[i],G2[r-i])))
            for i in range(max(0,r-n),min(n,r)+1):
                j=r-i
                if i<=j:pieces.append((-1 if i==j else -2,BD.multiply(C,F[i],F[j])))
            num=BD.add_poly(C,pieces,size=2*n-r+1)
            if r==132:parameter=C.add([(-1,num[-1])])
            if parameter is not None:
                gi=r-132
                if gi<=m:num=BD.add_poly(C,[(1,num),(1,[C.mul(parameter,v) for v in G[gi]])],size=2*n-r+1)
            if r<143:E.block('characteristic_upper_depth_'+str(r),num)
            else:Rphys[2*n-r]=num
        lam=Rphys[55][-1];jc=C.add([(Q(-455,243),lam)])
        phase='all boundary and Jacobian rows'
        BD.physical_boundary(C,E,'99_delta52_F',{n-r:v for r,v in enumerate(F)},n,3,9,Q(9,2),Q(7,2),state,C.const(1))
        BD.physical_boundary(C,E,'99_delta52_R_conditional',Rphys,55,3,5,Q(5,2),Q(7,2),state,lam)
        inv=C.var('Z_localizer',(1,1));sep=C.var('c',(1,2))
        E.block('separation_lambda_localizer',[C.add([(1,C.mul(inv,C.mul(sep,lam))),(-1,C.const(1))])])
        for r in range(n+m-1):
            pieces=[]
            for i in range(max(0,r-m),min(n,r)+1):
                j=r-i
                if j<=m:pieces.append((1,BD.bracket(C,F[i],G[j],n-i,m-j)))
            vals=BD.add_poly(C,pieces,size=n+m-1-r)
            if r==n+m-2:vals[0]=C.add([(1,vals[0]),(-1,jc)])
            E.block('jacobian_depth_'+str(r),vals)
        receipt['status']='COMPLETE_POLYNOMIAL_RESIDUAL_IDEAL_UNDECIDED'
    except (BD.CpuBound,MemoryError) as exc:
        receipt.update(status='BOUNDED_EXACT_Q_OPEN',bound_reason=type(exc).__name__+': '+str(exc))
    except Exception as exc:
        receipt.update(status='CONSTRUCTION_ERROR_OPEN',bound_reason=type(exc).__name__+': '+str(exc))
    finally:
        C=C or FQ.CURRENT
        receipt.update(last_phase=phase,unit_candidate=C.first_unit,pivots=C.pivot_receipts,
            blocks=C.blocks,remaining_residual_count=len(C.residuals),maximum_single_polynomial_terms=C.max_terms,
            formal_identity_and_ffi_controls_passed=True,cpu_seconds=time.process_time(),
            elapsed_seconds=time.monotonic()-start,max_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            driver_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
            flint_driver_sha256=sha256(Path(__file__).with_name('flint_q_attempt.py').read_bytes()).hexdigest())
        Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,separators=(',',':'))+'\n')
        print(json.dumps({k:receipt[k] for k in ['status','last_phase','unit_candidate','remaining_residual_count',
                 'maximum_single_polynomial_terms','cpu_seconds','max_rss_KiB']}),flush=True)


if __name__=='__main__':main()
