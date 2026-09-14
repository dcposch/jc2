#!/usr/bin/env python3
"""Exact rational straight-line transverse recurrence, with all terminal rows.

The arena stores arithmetic operations, never floating-point values. Graph
definitions are an acyclic polynomial presentation over Q[B,Binv,j,A_*], with
B*Binv-1. No graph tree is written. An execution receipt is NOT an ideal decision.
"""
from array import array
from fractions import Fraction
import argparse
import gc
import hashlib
import json
from math import comb
from pathlib import Path
import resource
import time


class Arena:
    # Triple opcode,left,right; rational constants indexed in a separate table.
    def __init__(self):
        self.code=array('q'); self.constants=[]; self.cids={}; self.names=[]
        self.zero=self.const(0); self.one=self.const(1)
    def node(self,op,a,b):
        n=len(self.code)//3; self.code.extend((op,a,b)); return n
    def const(self,v):
        v=Fraction(v)
        if v in self.cids: return self.cids[v]
        k=len(self.constants); self.constants.append(v)
        r=self.node(0,k,0); self.cids[v]=r; return r
    def var(self,name):
        k=len(self.names); self.names.append(name); return self.node(1,k,0)
    def add(self,a,b):
        if a==self.zero:return b
        if b==self.zero:return a
        return self.node(2,a,b)
    def mul(self,a,b):
        if a==self.zero or b==self.zero:return self.zero
        if a==self.one:return b
        if b==self.one:return a
        return self.node(3,a,b)
    def scale(self,a,c): return self.mul(a,self.const(c))
    def neg(self,a):return self.scale(a,-1)
    def digest(self):
        h=hashlib.sha256()
        h.update(memoryview(self.code).cast('B'))
        h.update(repr(self.constants).encode()); h.update(repr(self.names).encode())
        return h.hexdigest()


class Stream:
    def __init__(self,n,m,d):
        self.n=n;self.m=m;self.d=d;self.A=Arena(); self.rows=[];self.blocks={}
        a=self.A
        self.B=a.var('B');self.Bi=a.var('Binv');self.j=a.var('j')
        self.emit('B_inverse',[a.add(a.mul(self.B,self.Bi),a.const(-1))])
        self.X=[[self.B,a.zero,a.one]]
        self.Y=[[a.zero,a.scale(self.B,Fraction(3,2)),a.zero,a.one]]
    def trim(self,p):
        while p and p[-1]==self.A.zero:p.pop()
        return p
    def plus(self,p,q,scale=1):
        a=self.A;r=list(p)+[a.zero]*max(0,len(q)-len(p))
        for i,v in enumerate(q):r[i]=a.add(r[i],a.scale(v,scale))
        return self.trim(r)
    def times(self,p,q):
        if not p or not q:return []
        a=self.A;r=[a.zero]*(len(p)+len(q)-1)
        for i,x in enumerate(p):
            if x==a.zero:continue
            for k,y in enumerate(q):
                if y!=a.zero:r[i+k]=a.add(r[i+k],a.mul(x,y))
        return self.trim(r)
    def deriv(self,p):return [self.A.scale(v,i) for i,v in enumerate(p)][1:]
    def scaled(self,p,c):return self.trim([self.A.scale(v,c) for v in p])
    def emit(self,tag,p):
        count=0
        for i,v in enumerate(p):
            if v!=self.A.zero:self.rows.append((tag,i,v));count+=1
        self.blocks[tag]=self.blocks.get(tag,0)+count
    def residual(self,k):
        S=[]
        for i in range(max(1,k-len(self.Y)+1),min(k,len(self.X))):
            b=k-i
            if b<1 or b>=len(self.Y):continue
            term=self.plus(self.scaled(self.times(self.deriv(self.X[i]),self.Y[b]),b),
                           self.scaled(self.times(self.X[i],self.deriv(self.Y[b])),-i))
            S=self.plus(S,term)
        if k==1:S=self.plus(S,[self.j],-1)
        return self.scaled(S,Fraction(-1,k))
    def build(self):
        a=self.A; D=[a.scale(self.B,Fraction(3,2)),a.zero,a.const(3)]
        counts=[]
        for k in range(1,self.n+1):
            H=self.residual(k);H0=H[0] if H else a.zero
            dx=min(self.m-k,2+k//self.d)
            dy=min(self.n-k,3+k//self.d)
            av=a.scale(a.mul(H0,self.Bi),Fraction(-2,3))
            if dx<0:
                self.emit('X_termination_constant',[H0]); X=[]
                numerator=H
            else:
                X=[av]
                numerator=self.plus(H,[a.mul(v,av) for v in D])
            # Constant coefficient cancels algebraically using B*Binv=1.
            # With X absent, H0=0 is separately retained above.
            Y=self.scaled(numerator[1:],Fraction(1,2))
            count=max(0,min(dx-1,dy-2)+1)
            counts.append(count)
            if count:
                Ap=[a.var(f'A_{k-1}_{i}') for i in range(count)]
                X=self.plus(X,[a.zero]+self.scaled(Ap,2))
                Y=self.plus(Y,self.times(D,Ap))
            self.emit('Y_support_overflow',Y[dy+1:])
            Y=Y[:dy+1]
            self.X.append(self.trim(X));self.Y.append(self.trim(Y))
        # X/Y are now finite physical polynomials. Every remaining coefficient
        # of J-j is imposed, including those after the final nonzero strip.
        for k in range(self.n+1,self.n+self.m):
            self.emit('Jacobian_terminal',self.residual(k))
        self.A_counts=counts
    def faces(self):
        """Whole F/G top and actual major faces in translated (u,z)."""
        a=self.A
        for name,rows,D,power,minor,major,sign in [
            ('X',self.X,self.m,16 if self.d==3 else 14,
             18 if self.d==3 else 16,48 if self.d==3 else 56,1),
            ('Y',self.Y,self.n,24 if self.d==3 else 21,
             27 if self.d==3 else 24,72 if self.d==3 else 84,
             1 if self.d==3 else -1)]:
            lead=2 if name=='X' else 3
            for k in range(D+1):
                v=rows[k]
                i=D-k
                target=sign*comb(minor,k-major) if major<=k<=major+minor else 0
                old=v[i] if i<len(v) else a.zero
                self.emit(name+'_whole_top',[a.add(old,a.const(-target))])
                if k%self.d==0:
                    i=lead+k//self.d
                    if i+k>D:continue
                    target=(-1)**(k//self.d)*comb(power,k//self.d)
                    old=v[i] if i<len(v) else a.zero
                    self.emit(name+'_major_face',[a.add(old,a.const(-target))])
    def characteristic(self):
        a=self.A; p=a.scale(a.mul(self.B,self.B),Fraction(-3,4)); q=a.var('q')
        lam=a.var('lambda'); self.lam=lam
        l_over_j=Fraction(243,455) if self.d==3 else Fraction(-2048,3315)
        self.emit('lambda_transport',[a.add(lam,a.scale(self.j,-l_over_j))])
        # Stream R_k and its major/total support rows. The X^2 cache is bounded
        # by 2m strips; R is never expanded in the chart variables.
        XX=[]
        for k in range(2*self.m+1):
            v=[]
            for i in range(max(0,k-self.m),min(self.m,k)+1):
                v=self.plus(v,self.times(self.X[i],self.X[k-i]))
            XX.append(v)
        D2=55 if self.d==3 else 63
        self.R=[]
        for k in range(3*self.m+1):
            v=[]
            for i in range(max(0,k-2*self.m),min(self.m,k)+1):
                v=self.plus(v,self.times(self.X[i],XX[k-i]))
            for i in range(max(0,k-self.n),min(self.n,k)+1):
                v=self.plus(v,self.times(self.Y[i],self.Y[k-i]),-1)
            if k<=self.m:v=self.plus(v,[a.mul(p,x) for x in self.X[k]])
            if k==0:v=self.plus(v,[q])
            cap=min(D2-k,(k+2*self.d-1)//self.d)
            self.emit('R_support_overflow',v[max(0,cap+1):])
            self.R.append(v[:max(0,cap+1)])
        del XX
        # Degree-D2 target is a WHOLE homogeneous polynomial, not just y^D2.
        minor,major=(15,40) if self.d==3 else (14,49)
        for k in range(D2+1):
            i=D2-k;v=self.R[k]
            old=v[i] if i<len(v) else a.zero
            target=comb(minor,k-major) if major<=k<=major+minor else 0
            self.emit('R_whole_top',[a.add(old,a.scale(lam,-target))])
        # Complete actual R major face; q/C is stored as exact rational data.
        qs=([Fraction(1),Fraction(-4),Fraction(48,7),Fraction(-216,35),
             Fraction(1296,455),Fraction(-243,455)] if self.d==3 else
            [Fraction(1),Fraction(-21,5),Fraction(112,15),Fraction(-448,65),
             Fraction(3584,1105),Fraction(-2048,3315)])
        power=8 if self.d==3 else 7; face={}
        for r in range(power+1):
            for s,qc in enumerate(qs):
                k=self.d*(r+s)+1
                face[k]=face.get(k,Fraction(0))+comb(power,r)*(-1)**(power-r)*qc
        C_over_j=-1 if self.d==3 else 1
        for k,v in enumerate(self.R):
            if (k+2*self.d-1)%self.d:continue
            i=(k+2*self.d-1)//self.d
            if i+k>D2:continue
            old=v[i] if i<len(v) else a.zero
            self.emit('R_major_face',[a.add(old,a.scale(self.j,-C_over_j*face.get(k,0)))])
    def receipt(self,elapsed):
        rowhash=hashlib.sha256(repr(self.rows).encode()).hexdigest()
        return {'status':'EXACT_CIRCUIT_BUILT_NOT_IDEAL_DECIDED',
                'n':self.n,'m':self.m,'cover_d':self.d,
                'A_coefficients_before_minor_and_face_rows':sum(self.A_counts),
                'max_strip_A_coefficients':max(self.A_counts),
                'ordered_variables':self.A.names,
                'arithmetic_nodes':len(self.A.code)//3,
                'arena_bytes':len(self.A.code)*self.A.code.itemsize,
                'nonzero_syntax_rows':len(self.rows),'row_blocks':self.blocks,
                'graph_sha256':self.A.digest(),'ordered_rows_sha256':rowhash,
                'rows_are_circuits_over_Q':True,
                'last_J_transverse_power':self.n+self.m-2,
                'all_J_termination_rows_generated':True,
                'complete_major_faces_and_whole_top_rows_generated':True,
                'minor_boundary_and_tower_rows_not_in_this_driver':True,
                'elapsed_seconds':elapsed,
                'cpu_seconds':time.process_time(),
                'max_rss_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--d',type=int,choices=[3,4],required=True)
    ap.add_argument('--characteristic',action='store_true');args=ap.parse_args()
    # This lane's memory ceiling includes graph construction.
    resource.setrlimit(resource.RLIMIT_AS,(1900*1024**2,1900*1024**2))
    start=time.monotonic()
    s=Stream(99,66,3) if args.d==3 else Stream(108,72,4)
    s.build()
    s.faces()
    if args.characteristic:s.characteristic()
    out=s.receipt(time.monotonic()-start)
    out['driver_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    path=Path(__file__).with_name(f'recurrence-d{args.d}.json')
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:out[k] for k in ['status','arithmetic_nodes','nonzero_syntax_rows',
                                       'elapsed_seconds','cpu_seconds','max_rss_KiB']}),flush=True)


if __name__=='__main__':main()
