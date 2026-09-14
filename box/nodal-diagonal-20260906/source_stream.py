#!/usr/bin/env python3
"""Compose the transverse chart with physical source/tower rows over Q.

This reconstructible arithmetic circuit retains all rows and never writes an
artifact tree. A complete build is still not a unit/properness certificate.
"""
from recurrence_stream import Stream
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import argparse
import hashlib
import json
import resource
import time


class Source(Stream):
    def __init__(self,client):
        super().__init__(108,72,4) if client=='108' else super().__init__(99,66,3)
        self.client=client; self.phase='init';self.source_counts={}
    def constant_powers(self,v,N):
        a=self.A;out=[a.one]
        for _ in range(N):out.append(a.mul(out[-1],v))
        return out
    def ppadd(self,p,q,scale=1):
        a=self.A;r=dict(p)
        for ij,v in q.items():r[ij]=a.add(r.get(ij,a.zero),a.scale(v,scale))
        return {ij:v for ij,v in r.items() if v!=a.zero}
    def ppmul(self,p,q):
        a=self.A;r={}
        for (i,j),v in p.items():
            for (k,l),w in q.items():
                ij=(i+k,j+l);r[ij]=a.add(r.get(ij,a.zero),a.mul(v,w))
        return r
    def pppow(self,p,k):
        r={(0,0):self.A.one}
        for _ in range(k):r=self.ppmul(r,p)
        return r
    def physical(self,rows,h):
        a=self.A; out={};hp=self.constant_powers(h,self.n)
        for k,row in enumerate(rows):
            for i,c in enumerate(row):
                if c==a.zero:continue
                for ii in range(i+1):
                    v=a.scale(a.mul(c,hp[i-ii]),comb(i,ii))
                    for j in range(k+1):
                        ij=(ii+k-j,j)
                        term=a.scale(v,comb(k,j)*(-1)**(k-j))
                        out[ij]=a.add(out.get(ij,a.zero),term)
        return out
    def emit_sparse(self,tag,rows):
        before=len(self.rows)
        for key,v in sorted(rows.items()):
            if v!=self.A.zero:self.rows.append((tag,key,v))
        self.source_counts[tag]=len(self.rows)-before
    def major(self,tag,P,floor,target=None):
        a=self.A;out={}
        for (i,j),v in P.items():
            for r in range(j+1):
                ex=-self.d*(i+j)+(self.d+1)*r
                if ex>floor or (ex==floor and target is None):continue
                key=(ex,r)
                out[key]=a.add(out.get(key,a.zero),a.scale(v,comb(j,r)))
        if target is not None:
            for r,v in enumerate(target):
                key=(floor,r);out[key]=a.add(out.get(key,a.zero),a.neg(v))
        self.emit_sparse(tag,out)
    def d1(self,tag,P,floor):
        a=self.A;out={}
        L,v= (9,3) if self.d==3 else (8,2)
        # x=e^-L, y=e^-L+e^v+Pi*e^(v+1).
        for (i,j),c in P.items():
            for b in range(j+1):
                for r in range(j-b+1):
                    ex=-L*(i+j-b-r)+v*b+(v+1)*r
                    if ex>=floor:continue
                    key=(ex,r)
                    val=a.scale(c,comb(j,r)*comb(j-r,b))
                    out[key]=a.add(out.get(key,a.zero),val)
        self.emit_sparse(tag,out)
    def minor(self,tag,P,floor,target=None):
        a=self.A;out={}
        L=2 if self.client=='99_delta52' else 1
        delta=5 if L==2 else (3 if self.client=='108' else 2)
        up=self.up;vp=self.vp
        for (i,j),c in P.items():
            for r in range(j+1):
                for b in range(j-r+1):
                    aa=j-r-b
                    ex=-L*i+L*aa+2*L*b+delta*r
                    if ex>floor or (ex==floor and target is None):continue
                    val=a.mul(c,a.mul(up[aa],vp[b]))
                    val=a.scale(val,comb(j,r)*comb(j-r,b))
                    key=(ex,r);out[key]=a.add(out.get(key,a.zero),val)
        if target is not None:
            for r,v in enumerate(target):
                key=(floor,r);out[key]=a.add(out.get(key,a.zero),a.neg(v))
        self.emit_sparse(tag,out)
    def monic_root(self,P,N,k):
        """Unique degree-k monic (N/k)-th approximate root, over Q[x]."""
        a=self.A;alpha=Q(k,N);f=[]
        for r in range(k+1):
            f.append([P.get((i,N-r),a.zero) for i in range(r+1)])
        hs=[[a.one]]
        for r in range(1,k+1):
            out=self.scaled(f[r],alpha)
            for i in range(1,r):
                out=self.plus(out,self.scaled(self.times(f[i],hs[r-i]),((alpha+1)*i-r)/r))
            hs.append(out)
        return {(i,k-r):v for r,row in enumerate(hs) for i,v in enumerate(row) if v!=a.zero}
    def monic_div(self,P,H,k):
        a=self.A;r=dict(P);quo={}
        top=max((j for i,j in r),default=-1)
        lower={ij:v for ij,v in H.items() if ij!=(0,k)}
        for j in range(top,k-1,-1):
            cs=[(i,r.pop((i,j))) for i,jj in list(r) if jj==j]
            for i,c in cs:
                quo[(i,j-k)]=c
                for (ii,jj),v in lower.items():
                    key=(i+ii,j-k+jj)
                    r[key]=a.add(r.get(key,a.zero),a.neg(a.mul(c,v)))
        return quo,{ij:v for ij,v in r.items() if v!=a.zero}
    def source(self):
        a=self.A
        self.phase='physical composition'
        h=a.var('h'); At=a.var('A_target');bt=a.var('b_target');ct=a.var('c_target')
        X=self.physical(self.X,h);Y=self.physical(self.Y,h)
        G=self.ppadd(X,{(0,0):a.scale(At,Q(-1,3))})
        F={ij:a.scale(v,1 if self.d==3 else -1) for ij,v in Y.items()}
        F=self.ppadd(F,{ij:a.mul(a.scale(bt,Q(1,2)),v) for ij,v in G.items()})
        F=self.ppadd(F,{(0,0):a.scale(ct,Q(1,2))})
        R=self.physical(self.R,h)
        self.phase='physical minor boundaries'
        u=a.var('minor_u');v=a.var('minor_a2' if self.client=='99_delta2' else 'minor_v')
        sep=a.var('rho' if self.client=='99_delta2' else 'c_sep')
        self.up=self.constant_powers(u,self.n);self.vp=self.constant_powers(v,self.n)
        mu=a.var('minor_mean') if self.d==4 else a.zero
        if self.client=='99_delta2': P=[a.zero,a.zero,a.scale(sep,3),a.one]
        elif self.client=='99_delta52':P=[a.zero,a.neg(sep),a.zero,a.one]
        else:P=[a.add(a.mul(mu,mu),a.neg(sep)),a.scale(mu,-2),a.one]
        powers={0:[a.one]}
        for k in range(1,13):powers[k]=self.times(powers[k-1],P)
        if self.d==3:
            fp,gp,rp=(9,6,5);ff,gf,rf=(-18,-12,-10) if self.client=='99_delta2' else (-9,-6,-5)
        else:fp,gp,rp=12,8,7;ff,gf,rf=-12,-8,-7
        self.minor('F_minor',F,ff,powers[fp]);self.minor('G_minor',G,gf,powers[gp])
        self.minor('R_minor',R,rf,[a.mul(a.scale(self.lam,1 if self.d==3 else -1),v) for v in powers[rp]])
        self.d1('F_D1',F,-3);self.d1('G_D1',G,-2)
        self.phase='canonical roots'
        k=self.m//2;kk=11 if self.d==3 else 9;root_index=k//kk
        H=self.monic_root(F,self.n,k); H3=self.monic_root(H,k,kk)
        self.phase='canonical division'
        AA=self.ppadd(F,self.pppow(H,3),-1);A2,A3=self.monic_div(AA,H,k)
        GG=self.ppadd(G,self.pppow(H,2),-1);B1,B2=self.monic_div(GG,H,k)
        inner=self.ppadd(H,self.pppow(H3,root_index),-1); Cs={}
        for i in range(2,root_index+1):
            power=root_index-i
            divisor=self.pppow(H3,power)
            if power:
                Cs[i],inner=self.monic_div(inner,divisor,kk*power)
            else:Cs[i]=inner
        self.phase='source root and remainder bounds'
        for name,poly,D,ycap in [
            ('A2',A2,2*k-1,k),('A3',A3,3*k-1,k),
            ('B1',B1,k-1,k),('B2',B2,2*k-1,k)]:
            self.emit_sparse(name+'_degree_overflow',
                             {ij:v for ij,v in poly.items() if sum(ij)>D or ij[1]>=ycap})
        for i,poly in Cs.items():
            self.emit_sparse('C'+str(i)+'_degree_overflow',
                             {ij:v for ij,v in poly.items() if sum(ij)>i*kk-1 or ij[1]>=kk})
        face=[a.zero]*(self.d*(8 if self.d==3 else 7)+1)
        pp=8 if self.d==3 else 7
        for i in range(pp+1):face[self.d*i]=a.const(comb(pp,i)*(-1)**(pp-i))
        self.major('h2_D2',H,-self.d,face);self.major('h3_D2',H3,-1)
        self.d1('h2_D1',H,-1)
        h3minor=-2 if self.client=='99_delta2' else -1
        h2minor=h3minor*root_index
        self.minor('h3_minor',H3,h3minor,self.scaled(P,-1 if self.d==4 else 1))
        self.minor('h2_minor',H,h2minor,powers[root_index])
        for i,poly in Cs.items():
            self.major('C'+str(i)+'_D2',poly,-i)
            self.minor('C'+str(i)+'_minor',poly,h3minor*i)
        for name,poly,mult in [('A2',A2,2),('A3',A3,3),('B1',B1,1),('B2',B2,2)]:
            self.major(name+'_D2',poly,-self.d*mult)
            self.d1(name+'_D1',poly,-mult)
            self.minor(name+'_minor',poly,h2minor*mult)
        # Localizer is precisely separation*lambda; B inverse was justified by
        # j=unit*lambda and j=-(3B/2)X1(0), not independently assumed on j=0.
        inv=a.var('Z_sep_lambda')
        self.emit('distinguished_localizer',[a.add(a.mul(inv,a.mul(sep,self.lam)),a.const(-1))])
        self.phase='complete source coefficient circuit'


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--client',choices=['99_delta2','99_delta52','108'],required=True)
    args=ap.parse_args();resource.setrlimit(resource.RLIMIT_AS,(1900*1024**2,1900*1024**2))
    start=time.monotonic();s=Source(args.client);status='COMPLETE_CIRCUIT_NO_IDEAL_DECISION'
    try:
        s.phase='transverse recurrence';s.build();s.faces()
        s.phase='characteristic';s.characteristic();s.source()
    except MemoryError:
        status='MEMORY_BOUND_OPEN_INCOMPLETE_CIRCUIT'
    out={'status':status,'phase':s.phase,'client':args.client,
         'arithmetic_nodes':len(s.A.code)//3,'graph_sha256':s.A.digest(),
         'ordered_rows_sha256':hashlib.sha256(repr(s.rows).encode()).hexdigest(),
         'source_row_blocks':s.source_counts,'rows':len(s.rows),'ordered_variables':s.A.names,
         'elapsed_seconds':time.monotonic()-start,'cpu_seconds':time.process_time(),
         'max_rss_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         'driver_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    out['recurrence_driver_sha256']=hashlib.sha256(Path(__file__).with_name('recurrence_stream.py').read_bytes()).hexdigest()
    path=Path(__file__).with_name('source-'+args.client+'.json')
    path.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:out[k] for k in ['status','phase','arithmetic_nodes','rows','elapsed_seconds','cpu_seconds','max_rss_KiB']}),flush=True)


if __name__=='__main__':main()
