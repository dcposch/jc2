"""Necessary source-tree compatibility with an actual centre stabilizer.

A positive nonzero centre coefficient at delta enlarges its denominator lattice;
a zero coefficient does not. Every source-major p factor must extend, including
unselected siblings. This is the operative Tree's structural/ODE test with that
state corrected. A witness is combinatorial necessary data, never a source pair.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from math import gcd,lcm


def _is_q_power_completion(P,Q,distinct_roots,all_multiplicity_w):
    """Production final test for the completed Prop. 4.6(5) pattern."""
    return (Q>0 and P%Q==0 and all_multiplicity_w and distinct_roots==Q)


def is_q_power_pattern(P,Q,A,z,orbits):
    """Expose the exact whole-pattern predicate for regression controls."""
    P=int(P);Q=int(Q);A=int(A);z=int(z);orbits=tuple(map(int,orbits))
    if Q<=0 or P%Q:return False
    w=P//Q
    multiplicities=((z,) if z>0 else ())+orbits
    return _is_q_power_completion(
        P,Q,int(z>0)+A*len(orbits),
        bool(multiplicities) and all(value==w for value in multiplicities)
    )


class OwnVRouteTree:
    """Reuse one instance across selected first-support positions for one row."""
    def __init__(self, source, *, legacy_resonance_filter=False):
        self.n=int(source.n);self.m=int(source.m);self.s=int(source.s)
        self.M={i:int(source.M[i]) for i in range(1,self.s+1)}
        self.V={i:int(source.V[i]) for i in range(2,self.s+1)}
        self.d={1:self.n}
        for i in range(1,self.s+1):self.d[i+1]=gcd(self.d[i],self.M[i])
        self.ns=self.n//self.d[2];self.ms=self.m//self.d[2]
        self.legacy_resonance_filter=bool(legacy_resonance_filter)
        self._memo={}

    def delta(self,i,high):
        ratio=F(self.n-self.M[i],self.n-self.M[self.s]-1)
        for k,V in zip(range(i+1,self.s+1),high):
            ratio*=F(V*(self.n-self.M[k])-self.d[k],V*(self.n-self.M[k-1])-self.d[k])
        return 1-ratio

    def bottom(self,high,centre_L,danger):
        if danger:return None   # Prop5.6 is a reduced-source rule.
        delta1=self.delta(1,high);A1=(centre_L*delta1).denominator;V2=high[0]
        b12=self.ns*V2%A1==0 and (self.ms*V2-1)%A1==0
        b13=self.ms*V2%A1==0 and (self.ns*V2-1)%A1==0
        if not (b12 or b13):return None
        return dict(V2=V2,delta1=delta1,A1=A1,centre_L=centre_L)

    def ok(self,j,high,centre_L,danger,need=None,first=None):
        key=(j,high,centre_L,danger,need,first)
        if key not in self._memo:self._memo[key]=self._ok(*key)
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
            # Historical control only: this per-factor test is strictly
            # stronger than Prop 4.6(5), which excludes p=q^w as a whole.
            if self.legacy_resonance_filter and z>0 and P==Q*z:continue
            zmajor=F(z)>lo
            zero_witness=child(z,True) if zmajor else None
            if zmajor and zero_witness is None:continue
            total=(P-z)//A
            cap=(Q-int(z>0))//A
            coins=[];coin_witness={}
            for r in range(1,total+1):
                if self.legacy_resonance_filter and P==Q*r:continue
                major=F(r)>lo
                witness=child(r,False) if major else None
                if major and witness is None:continue
                coins.append((r,major));coin_witness[r]=witness
            modes=[('free',())] if need is None else []
            allow_zero=first is None or j>first or removable
            allow_nonzero=first is None or (j==first and delta>0)
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

                w=P//Q if P%Q==0 else None
                distinct=int(z>0)+A*len(pre)
                all_w=(w is not None and (z==0 or z==w)
                       and all(value==w for value in pre))

                @lru_cache(maxsize=None)
                def fill(rem,left,index,major,distinct_roots,all_multiplicity_w):
                    if rem==0:
                        if not major:return None
                        # Prop 4.6(5): reject exactly p=q^w, not an
                        # individual factor whose multiplicity happens to w.
                        if (not self.legacy_resonance_filter and
                            _is_q_power_completion(
                                P,Q,distinct_roots,all_multiplicity_w)):return None
                        return ()
                    if left==0:return None
                    for idx in range(index,len(coins)):
                        value,is_major=coins[idx]
                        if value>rem:break
                        rest=fill(rem-value,left-1,idx,major or is_major,
                                  distinct_roots+A,
                                  all_multiplicity_w and value==w)
                        if rest is not None:return (value,)+rest
                    return None

                orbit_tail=fill(remaining,slots,0,zmajor or bool(pre),distinct,all_w)
                if orbit_tail is None:continue
                orbits=pre+orbit_tail
                return dict(j=j,delta=delta,centre_L=centre_L,A=A,P=P,Q=Q,
                            z=z,orbits=orbits,mode=mode,first_requested=first,
                            resonance_filter=("legacy-per-factor" if
                                self.legacy_resonance_filter else "exact-p-not-q-power"),
                            danger=danger,selected_child=selected,
                            zero_major_child=zero_witness,
                            nonzero_major_children={r:coin_witness[r] for r in set(orbits)
                                                    if coin_witness[r] is not None})
        return None

    def compatible_first_support(self,j):
        if not (2<=j<self.s):raise ValueError('first support is a source split 2..s-1')
        if not self.d[self.s]>self.V[self.s]>F(self.d[self.s],2):return None
        need=tuple(self.V[i] for i in range(self.s-1,1,-1))
        return self.ok(self.s-1,(self.V[self.s],),1,True,need,j)


def compatible_first_support(source,j,*,legacy_resonance_filter=False):
    return OwnVRouteTree(
        source,legacy_resonance_filter=legacy_resonance_filter
    ).compatible_first_support(j)
