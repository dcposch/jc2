#!/usr/bin/env python3
"""Hash-only replay of the normalized coefficient map, then canonical rows.

The old characteristic/boundary circuit hashes must match before this receipt
can be composed with the already completed full Jacobian receipt. Hash-only
values are not arithmetic evaluations. Every arithmetic node remains a formal
Q circuit, and all canonical residuals are retained in reproducible order.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import resource
import signal
import time

import boundary_maps as BM
from boundary_maps import E, Circuit
from boundary_counts import SPECS
from boundary_full_dag import add_poly,multiply,monic_division,physical_boundary,CpuBound,cpu_alarm
from source_stream import Source


class HashCircuit(Circuit):
    def const(self,value):
        value=Q(value)
        if value not in self.constants:
            self.nodes+=1
            digest=sha256(f"Q:{value.numerator}/{value.denominator}".encode()).digest()
            self.constants[value]=E(digest,(Q(0),Q(0)),value)
        return self.constants[value]
    def var(self,name,values=(0,0),free=False):
        self.nodes+=1
        if free:self.free_names.append(name)
        return E(sha256(("variable:"+name).encode()).digest(),(Q(0),Q(0)))
    def add(self,terms):
        by_hash={};constants=Q(0)
        for scalar,expr in terms:
            scalar=Q(scalar)
            if not scalar:continue
            if expr.constant is not None:constants+=scalar*expr.constant
            else:
                if expr.digest not in by_hash:by_hash[expr.digest]=[Q(0),expr]
                by_hash[expr.digest][0]+=scalar
        if constants:
            expr=self.const(constants);by_hash[expr.digest]=[Q(1),expr]
        rows=sorted((digest,scalar,expr) for digest,(scalar,expr) in by_hash.items() if scalar)
        if not rows:return self.const(0)
        if len(rows)==1 and rows[0][1]==1:return rows[0][2]
        digest=sha256(b"linear-combination:")
        for child,scalar,expr in rows:
            digest.update(f"{scalar.numerator}/{scalar.denominator}:".encode());digest.update(child)
        self.nodes+=1
        return E(digest.digest(),(Q(0),Q(0)))
    def mul(self,left,right):
        if left.constant is not None:return self.add([(left.constant,right)])
        if right.constant is not None:return self.add([(right.constant,left)])
        self.nodes+=1
        return E(sha256(b"product:"+b"".join(sorted([left.digest,right.digest]))).digest(),(Q(0),Q(0)))


class HashEmit:
    def __init__(self):self.groups=[]
    def block(self,name,values):
        digest=sha256();count=zero=0;nonzero=[]
        for value in values:
            digest.update(f"{count}:".encode()+value.digest)
            if value.constant==0:zero+=1
            elif value.constant is not None:nonzero.append([count,str(value.constant)])
            count+=1
        self.groups.append(dict(name=name,coefficients=count,literal_zero_constants=zero,
                                literal_nonzero_constants=nonzero,
                                coefficient_circuits_sha256=digest.hexdigest()))


class Adapter:
    def __init__(self,C):self.C=C;self.zero=C.const(0);self.one=C.const(1)
    def const(self,x):return self.C.const(x)
    def add(self,*args):return self.C.add([(1,x) for x in args])
    def neg(self,x):return self.C.add([(-1,x)])
    def scale(self,x,s):return self.C.add([(s,x)])
    def mul(self,x,y):return self.C.mul(x,y)
    def var(self,name):return self.C.var(name)


class Canonical(Source):
    def __init__(self,C,emit):
        self.n=99;self.m=66;self.d=3;self.client='99_delta52'
        self.A=Adapter(C);self.collector=emit;self.source_counts={};self.phase='init'
    def emit_sparse(self,tag,rows):
        values=[v for key,v in sorted(rows.items()) if v!=self.A.zero]
        self.collector.block(tag,values);self.source_counts[tag]=len(values)
    def emit(self,tag,rows):self.collector.block(tag,rows)
    def compose(self,F,G,R,lam,u,v):
        a=self.A;self.lam=lam
        self.up=self.constant_powers(u,self.n);self.vp=self.constant_powers(v,self.n)
        sep=a.var('c');P=[a.zero,a.neg(sep),a.zero,a.one]
        powers={0:[a.one]}
        for k in range(1,13):powers[k]=self.times(powers[k-1],P)
        self.phase='F/G D1'
        self.d1('F_D1',F,-3);self.d1('G_D1',G,-2)
        self.phase='canonical roots'
        k=33;kk=11;root_index=3
        H=self.monic_root(F,self.n,k);H3=self.monic_root(H,k,kk)
        self.phase='canonical divisions'
        AA=self.ppadd(F,self.pppow(H,3),-1);A2,A3=self.monic_div(AA,H,k)
        GG=self.ppadd(G,self.pppow(H,2),-1);B1,B2=self.monic_div(GG,H,k)
        inner=self.ppadd(H,self.pppow(H3,root_index),-1);Cs={}
        for i in range(2,root_index+1):
            power=root_index-i;divisor=self.pppow(H3,power)
            if power:Cs[i],inner=self.monic_div(inner,divisor,kk*power)
            else:Cs[i]=inner
        self.phase='canonical degree overflows'
        for name,poly,D,ycap in [('A2',A2,65,k),('A3',A3,98,k),('B1',B1,32,k),('B2',B2,65,k)]:
            self.emit_sparse(name+'_degree_overflow',{ij:v for ij,v in poly.items() if sum(ij)>D or ij[1]>=ycap})
        for i,poly in Cs.items():
            self.emit_sparse('C'+str(i)+'_degree_overflow',{ij:v for ij,v in poly.items() if sum(ij)>i*kk-1 or ij[1]>=kk})
        self.phase='canonical major/D1/minor rows'
        face=[a.zero]*25
        for i in range(9):face[3*i]=a.const(comb(8,i)*(-1)**(8-i))
        self.major('h2_D2',H,-3,face);self.major('h3_D2',H3,-1)
        self.d1('h2_D1',H,-1)
        self.minor('h3_minor',H3,-1,P);self.minor('h2_minor',H,-3,powers[3])
        for i,poly in Cs.items():
            self.major('C'+str(i)+'_D2',poly,-i);self.minor('C'+str(i)+'_minor',poly,-i)
        for name,poly,mult in [('A2',A2,2),('A3',A3,3),('B1',B1,1),('B2',B2,2)]:
            self.major(name+'_D2',poly,-3*mult);self.d1(name+'_D1',poly,-mult)
            self.minor(name+'_minor',poly,-3*mult)
        self.emit('distinguished_localizer',[a.add(a.mul(a.var('Z_sep_lambda'),a.mul(sep,lam)),a.const(-1))])
        self.phase='complete canonical source rows'


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(390,400))
    resource.setrlimit(resource.RLIMIT_AS,(295*1024**2,295*1024**2))
    signal.signal(signal.SIGXCPU,cpu_alarm)
    start=time.monotonic();cpu=time.process_time()
    root=Path(__file__).parent;old=json.loads((root/'boundary_full_dag_delta52.json').read_text())
    assert old['status']=='COMPLETE_DAG_RESIDUAL_IDEAL_UNDECIDED'
    old_groups={g['name']:g for g in old['residual_blocks']}
    BM.Circuit=HashCircuit
    Emitter=HashEmit();phase='G boundary replay';source=None
    result=dict(status='RUNNING',evaluations_enabled=False,client='99_delta52',
                prior_full_jacobian_receipt_sha256=sha256((root/'boundary_full_dag_delta52.json').read_bytes()).hexdigest())
    try:
        gcheck,state=BM.build(SPECS[3],{},return_state=True)
        C=state['C'];n=99;m=66
        assert gcheck['forward_coefficient_circuit_sha256']==old['G_boundary_receipt']['forward_coefficient_circuit_sha256']
        up=C.power(state['u'],n//2);vp=C.power(state['v'],n//3)
        state['centre_products']={(a,b):C.mul(up[a],vp[b]) for a in range(n//2+1) for b in range((n-2*a)//3+1)}
        G=[state['coeff_y'][m-r] for r in range(m+1)]
        ftop=[Q(0)]*100
        for i in range(73):ftop[27+i]=Q(comb(72,i)*(-1)**(72-i))
        F=[[C.const(x) for x in ftop]];G2={};Rphysical={};p=None
        phase='hash-only characteristic replay'
        for r in range(199):
            if r<=132:
                pieces=[]
                for i in range(max(0,r-m),min(m,r)+1):
                    j=r-i
                    if i<=j:pieces.append((1 if i==j else 2,multiply(C,G[i],G[j])))
                G2[r]=add_poly(C,pieces,size=133-r)
            cube=[(1,multiply(C,G[i],G2[r-i])) for i in range(max(0,r-132),min(m,r)+1)]
            g3=add_poly(C,cube,size=199-r)
            if r==0:continue
            square=[]
            for i in range(max(1 if r<=n else 0,r-n),min(n,r-1 if r<=n else r)+1):
                j=r-i
                if i<=j and i<len(F) and j<len(F):square.append((1 if i==j else 2,multiply(C,F[i],F[j])))
            num=add_poly(C,[(1,g3)]+[(-s,v) for s,v in square],size=199-r)
            if r<=99:
                quotient,remainder=monic_division(C,num,ftop)
                F.append(add_poly(C,[(Q(1,2),quotient)],size=100-r))
                Emitter.block('characteristic_upper_depth_'+str(r),remainder)
            else:
                if r==132:p=C.add([(-1,num[-1])])
                if p is not None:
                    gi=r-132
                    if 0<=gi<=66:num=add_poly(C,[(1,num),(1,[C.mul(p,v) for v in G[gi]])],size=199-r)
                if 198-r>55:Emitter.block('characteristic_upper_depth_'+str(r),num)
                else:Rphysical[198-r]=num
            if r%20==0:print(json.dumps(dict(phase=phase,depth=r,cpu_seconds=round(time.process_time()-cpu,1))),flush=True)
        lam=Rphysical[55][-1]
        assert lam.digest.hex()==old['lambda_circuit_sha256'] and p.digest.hex()==old['p_circuit_sha256']
        Fphysical={99-r:f for r,f in enumerate(F)}
        physical_boundary(C,Emitter,'99_delta52_F',Fphysical,99,3,9,Q(9,2),Q(7,2),state,C.const(1))
        physical_boundary(C,Emitter,'99_delta52_R_conditional',Rphysical,55,3,5,Q(5,2),Q(7,2),state,lam)
        for group in Emitter.groups:
            previous=old_groups[group['name']]
            assert group['coefficients']==previous['coefficients']
            assert group['coefficient_circuits_sha256']==previous['coefficient_circuits_sha256']
        result['matched_replay_blocks']=len(Emitter.groups)
        result['matched_replay_coefficients']=sum(g['coefficients'] for g in Emitter.groups)
        phase='canonical source composition';source=Canonical(C,Emitter)
        physical=lambda rows:{(N-j,j):v for N,row in rows.items() for j,v in enumerate(row) if v.constant!=0}
        source.compose(physical(Fphysical),physical(state['coeff_y']),physical(Rphysical),lam,state['u'],state['v'])
        result['status']='COMPLETE_69_VARIABLE_SOURCE_CIRCUIT_IDEAL_UNDECIDED'
        result['canonical_source_row_blocks']=source.source_counts
        result['generators_before_Rabinowitsch']=69
    except (CpuBound,MemoryError) as exc:
        result['status']='BOUNDED_CANONICAL_ADDON_INCOMPLETE';result['bound_reason']=type(exc).__name__
    finally:
        result.update(phase=source.phase if source is not None else phase,
                      elapsed_seconds=round(time.monotonic()-start,3),cpu_seconds=round(time.process_time()-cpu,3),
                      maximum_resident_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                      blocks=Emitter.groups,driver_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                      source_stream_sha256=sha256((root/'source_stream.py').read_bytes()).hexdigest())
        if 'C' in locals():result['circuit_nodes_constructed']=C.nodes
        (root/'boundary_canonical_addon_delta52.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
        print(json.dumps({k:v for k,v in result.items() if k not in ('blocks','canonical_source_row_blocks')}),flush=True)


if __name__=='__main__':main()
