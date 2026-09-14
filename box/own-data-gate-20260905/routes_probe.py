"""[GATE COPY, instrumented] Necessary source-tree compatibility with an actual centre stabilizer.

A positive nonzero centre coefficient at delta enlarges its denominator lattice;
a zero coefficient does not. Every source-major p factor must extend, including
unselected siblings. This is the operative Tree's structural/ODE test with that
state corrected. A witness is combinatorial necessary data, never a source pair.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from math import gcd,lcm

OFF=set()   # names of conditions to disable, set by the driver


class OwnVRouteTree:
    """Reuse one instance across selected first-support positions for one row."""
    def __init__(self, source):
        self.n=int(source.n);self.m=int(source.m);self.s=int(source.s)
        self.M={i:int(source.M[i]) for i in range(1,self.s+1)}
        self.V={i:int(source.V[i]) for i in range(2,self.s+1)}
        self.d={1:self.n}
        for i in range(1,self.s+1):self.d[i+1]=gcd(self.d[i],self.M[i])
        self.ns=self.n//self.d[2];self.ms=self.m//self.d[2]
        self._memo={}
        self._offkey=frozenset(OFF)

    def delta(self,i,high):
        ratio=F(self.n-self.M[i],self.n-self.M[self.s]-1)
        for k,V in zip(range(i+1,self.s+1),high):
            ratio*=F(V*(self.n-self.M[k])-self.d[k],V*(self.n-self.M[k-1])-self.d[k])
        return 1-ratio

    def bottom(self,high,centre_L,danger):
        if danger and 'prop56' not in OFF:return None   # Prop5.6 is a reduced-source rule.
        delta1=self.delta(1,high);A1=(centre_L*delta1).denominator;V2=high[0]
        b12=self.ns*V2%A1==0 and (self.ms*V2-1)%A1==0
        b13=self.ms*V2%A1==0 and (self.ns*V2-1)%A1==0
        if not (b12 or b13) and 'p188' not in OFF:return None
        return dict(V2=V2,delta1=delta1,A1=A1,centre_L=centre_L)

    def ok(self,j,high,centre_L,danger,need=None,first=None):
        key=(j,high,centre_L,danger,need,first,frozenset(OFF))
        if key not in self._memo:self._memo[key]=self._ok(*key[:-1])
        return self._memo[key]

    def _ok(self,j,high,centre_L,danger,need,first):
        delta=self.delta(j,high);A=(centre_L*delta).denominator
        P=high[0]*self.d[j]//self.d[j+1]
        Q=high[0]*(self.n-self.M[j])//self.d[j+1]
        lo=F(self.d[j],self.n-self.M[j])
        removable=delta.denominator==1 and delta<=0
        if need is not None and need[0]<=lo:return None

        def child(v,zero,tail=None,selected=False):
            next_L=centre_L if zero else lcm(centre_L,delta.denominator)
            next_danger=danger and (zero or removable)
            next_high=(v,)+high
            next_first=first if selected and (zero or removable) else None
            if j==2:
                if selected and next_first is not None:return None
                return self.bottom(next_high,next_L,next_danger)
            return self.ok(j-1,next_high,next_L,next_danger,tail,next_first)

        for z in range(P%A,P+1,A):
            if z>0 and P==Q*z and 'resonance' not in OFF:continue
            zmajor=F(z)>lo
            zero_witness=child(z,True) if zmajor else None
            if zmajor and zero_witness is None and 'siblings' not in OFF:continue
            total=(P-z)//A
            cap=(Q-int(z>0))//A
            coins=[];coin_witness={}
            for r in range(1,total+1):
                if P==Q*r and 'resonance' not in OFF:continue
                major=F(r)>lo
                witness=child(r,False) if major else None
                if major and witness is None and 'siblings' not in OFF:continue
                coins.append((r,major));coin_witness[r]=witness
            modes=[('free',())] if need is None else []
            allow_zero=first is None or j>first or removable
            allow_nonzero=first is None or (j==first and (delta>0 or 'deltapos' in OFF))
            if need is not None:
                if allow_zero and z==need[0] and zmajor:modes.append(('zero',()))
                if allow_nonzero and any(r==need[0] for r,_ in coins) and need[0]<=total:
                    modes.append(('nonzero',(need[0],)))
            for mode,pre in modes:
                if mode=='zero':selected=child(z,True,need[1:] or None,True)
                elif mode=='nonzero':selected=child(need[0],False,need[1:] or None,True)
                else:selected=None
                if mode!='free' and selected is None:continue
                remaining=total-sum(pre); slots=cap-len(pre)
                if remaining<0 or slots<0:continue

                @lru_cache(maxsize=None)
                def fill(rem,left,index,major):
                    if rem==0:return () if major else None
                    if left==0:return None
                    for idx in range(index,len(coins)):
                        value,is_major=coins[idx]
                        if value>rem:break
                        rest=fill(rem-value,left-1,idx,major or is_major)
                        if rest is not None:return (value,)+rest
                    return None

                orbit_tail=fill(remaining,slots,0,zmajor or bool(pre))
                if orbit_tail is None:continue
                orbits=pre+orbit_tail
                return dict(j=j,delta=delta,centre_L=centre_L,A=A,P=P,Q=Q,
                            z=z,orbits=orbits,mode=mode,first_requested=first,
                            danger=danger,selected_child=selected,
                            zero_major_child=zero_witness,
                            nonzero_major_children={r:coin_witness[r] for r in set(orbits)
                                                    if coin_witness[r] is not None})
        return None

    def compatible_first_support(self,j):
        if not (2<=j<self.s):raise ValueError('first support is a source split 2..s-1')
        if not self.d[self.s]>self.V[self.s]>F(self.d[self.s],2) and 'majortop' not in OFF:return None
        need=tuple(self.V[i] for i in range(self.s-1,1,-1))
        return self.ok(self.s-1,(self.V[self.s],),1,True,need,j)


def compatible_first_support(source,j):
    return OwnVRouteTree(source).compatible_first_support(j)
