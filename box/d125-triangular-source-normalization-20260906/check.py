#!/usr/bin/env python3
"""Tiny exact controls only: no full ideal, CAS, solver, or Keller witness."""
from fractions import Fraction as F
from math import comb
import json

def require(test, msg):
    if not test:
        raise ValueError(msg)

def clean(p):
    return {e:F(c) for e,c in p.items() if c}

def add(*ps):
    r={}
    for p in ps:
        for e,c in p.items():
            r[e]=r.get(e,0)+c
    return clean(r)

def scale(p,c):
    return clean({e:c*v for e,v in p.items()})

def mul(p,q):
    r={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            e=(i+k,j+l)
            r[e]=r.get(e,0)+a*b
    return clean(r)

def diff(p,axis):
    r={}
    for e,c in p.items():
        if e[axis]:
            k=list(e); k[axis]-=1
            r[tuple(k)]=c*e[axis]
    return clean(r)

def jac(p,q):
    return add(mul(diff(p,0),diff(q,1)),scale(mul(diff(p,1),diff(q,0)),-1))

def equal(p,q,label):
    require(clean(p)==clean(q),label)

def reject(fn,label):
    try:
        fn()
    except ValueError:
        return True
    raise ValueError('mutation accepted: '+label)

def power_linear(n,s):
    return {(n-k,k):F(comb(n,k))*s**k for k in range(n+1)}

def shifted_power(n,r):
    return {(n-k,0):F(comb(n,k))*r**k for k in range(n+1)}

def shift(p,s=F(0),r=F(0)):
    # u -> u-s*v-r, v -> v. All source exponents are nonnegative.
    out={}
    for (i,j),a in p.items():
        for k in range(i+1):
            for l in range(i-k+1):
                e=(i-k-l,j+k)
                c=a*comb(i,k)*comb(i-k,l)*(-s)**k*(-r)**l
                out[e]=out.get(e,0)+c
    return clean(out)

def image(p):
    out={}
    for (i,j),a in p.items():
        for k in range(j+1):
            e=(5*i-k,j-k)
            out[e]=out.get(e,0)+a*comb(j,k)
    return clean(out)

def D(p,wrong=False):
    return scale(add(mul({(-4,0):F(1)},diff(p,0)),
                     mul({(-6,0):F(-1 if wrong else 1)},diff(p,1))),F(1,5))

def face(p,weights):
    m=max(weights[0]*i+weights[1]*j for i,j in p)
    return {e:c for e,c in p.items() if weights[0]*e[0]+weights[1]*e[1]==m}

def w_minus_one_power(n):
    return {(k,5*k):F(comb(n,k)*(-1)**(n-k)) for k in range(n+1)}

def band_seed(ell,r,value=F(1),extra_w=0):
    i=max(0,-((-ell)//5)); j=5*i-ell
    return scale(mul({(i+extra_w,j+5*extra_w):F(1)},w_minus_one_power(r)),value/F(5)**r)

Ppins={(4,1):F(1),(21,6):F(1)}
Qpins={(1,0):F(-1),(18,5):F(-3),(35,10):F(-9,5)}

def verify_chart(p,q):
    for poly,Dg,U,h,pins,guard in [(p,75,15,3,Ppins,(15,60)),(q,125,25,5,Qpins,(25,100))]:
        require(all(i>=0 and j>=0 and i+j<=Dg and 5*i-j<=U for i,j in poly),'source support')
        require(poly.get(guard,0)!=0,'degree guard')
        trans=image(poly)
        require(all(5*a-17*b<=h for a,b in trans),'terminal halfspace')
        require(all(trans.get(e,0)==v for e,v in pins.items()),'terminal pins')
    return True

checks={}
alpha,beta,s,r=F(2),F(3),F(2,3),F(-4,7)
Ptop=scale(mul(power_linear(15,s),{(0,60):F(1)}),alpha)
Qtop=scale(mul(power_linear(25,s),{(0,100):F(1)}),beta)
E={(1,1):F(1,45),(0,2):s/F(45)}
equal(jac(E,Ptop),Ptop,'total Euler equation')
equal(jac(Ptop,Qtop),{},'common homogeneous top')
equal(shift(Ptop,s=s),{(15,60):alpha},'shear normalization sign P')
equal(shift(Qtop,s=s),{(25,100):beta},'shear normalization sign Q')
checks['total_Euler_and_shared_shear']=True
checks['wrong_Euler_coefficient_rejected']=reject(lambda:equal(jac(scale(E,F(45,44)),Ptop),Ptop,'bad b'),'b')
checks['u_squared_Euler_term_rejected']=reject(lambda:equal(jac(add(E,{(2,0):F(1)}),Ptop),Ptop,'bad a'),'a')
checks['wrong_shear_sign_rejected']=reject(lambda:equal(shift(Ptop,s=-s),{(15,60):alpha},'bad sign'),'sign')
Pt=scale(mul(shifted_power(15,r),{(0,60):F(1)}),alpha)
Qt=scale(mul(shifted_power(25,r),{(0,100):F(1)}),beta)
Et={(1,1):F(1,45),(0,1):r/F(45)}
equal(jac(Et,Pt),Pt,'vertical Euler equation')
equal(jac(Pt,Qt),{},'shared vertical root')
equal(shift(Pt,r=r),{(15,60):alpha},'translation sign P')
equal(shift(Qt,r=r),{(25,100):beta},'translation sign Q')
badQt=scale(mul(shifted_power(25,r+1),{(0,100):F(1)}),beta)
checks['different_vertical_Q_root_rejected']=reject(lambda:equal(jac(Pt,badQt),{},'different root'),'root')
checks['vertical_Euler_and_shared_translation']=True

equal(D(image({(1,0):F(1)})),{(0,0):F(1)},'D Phi(u)')
equal(D(image({(0,1):F(1)})),{},'D Phi(v)')
checks['wrong_lift_Y_sign_rejected']=reject(lambda:equal(D(image({(0,1):F(1)}),wrong=True),{},'bad lift'),'lift')
seed={(2,3):F(1)}
equal(D(image(seed)),image(diff(seed,0)),'lift conjugation')
nil=image(seed)
for _ in range(3): nil=D(nil)
equal(nil,{},'source nilpotence')
ambient={(1,0):F(1)}
for _ in range(4): ambient=D(ambient)
require(bool(ambient),'ambient derivation unexpectedly nilpotent')
checks['lift_and_source_only_nilpotence']=True
require([-4*5-5,-6*5+17]==[-25,-13],'D weight shifts')
require([-25-17,-13-17,-25-5,-13-5]==[-42,-30,-30,-18],'vD weight shifts')
checks['all_terminal_operator_shifts_strictly_negative']=True
require([5*a-17*b for a,b in Ppins]==[3,3] and [5*a-17*b for a,b in Qpins]==[5,5,5],'pin weights')

# Non-Keller fixture in the full linear source chart, with both degree guards.
p=add(band_seed(3,1),band_seed(15,6),band_seed(15,7,F(5)**7,5),{(0,75):F(1)})
q=add(band_seed(1,0,F(-1)),band_seed(13,5,F(-3)),band_seed(25,10,F(-9,5)),band_seed(25,11,F(5)**11,9))
verify_chart(p,q)
unguarded=dict(p)
unguarded.pop((15,60))
checks['zero_alpha_boundary_rejected_by_actual_chart_checker']=reject(lambda:verify_chart(unguarded,q),'degree guard')
require(any(i+j>0 for i,j in jac(p,q)),'fixture unexpectedly Keller')
newp,newq=shift(p,s,r),shift(q,s,r)
verify_chart(newp,newq)
equal(face(image(newp),(5,-17)),face(image(p),(5,-17)),'P entire terminal face')
equal(face(image(newq),(5,-17)),face(image(q),(5,-17)),'Q entire terminal face')
equal(shift(newp,-s,-r),p,'inverse shift P')
equal(shift(newq,-s,-r),q,'inverse shift Q')
require(newp[15,60]==p[15,60] and newq[25,100]==q[25,100],'top guard invariance')
checks['non_Keller_chart_fixture_all_jets_pins_guards_preserved']=True
checks['inverse_source_shift_on_actual_degree_75_125_fixture']=True

counts={}
for name,Dg,U,a,b in [('P',75,15,15,60),('Q',125,25,25,100)]:
    source=[(i,j) for i in range(Dg+1) for j in range(Dg-i+1) if 5*i-j<=U]
    rect=[(i,j) for i,j in source if i<=a and j<=b]
    pure=[(i,j) for i,j in rect if j<b or i==a]
    require(max(i for i,j in source)==a,'pre-existing horizontal bound')
    require([(i,j) for i,j in source if i==a]==[(a,b)],'highest-u slice')
    counts[name]={'original_raw':len(source),'rectangle_raw':len(rect),'pure_vertical_top_raw':len(pure)}
require(counts=={'P':{'original_raw':706,'rectangle_raw':586,'pure_vertical_top_raw':571},'Q':{'original_raw':1901,'rectangle_raw':1576,'pure_vertical_top_raw':1551}},'counts')
physical_bound=sum(160-max(0,5*i-36) for i in range(40))
require(physical_bound==3792,'physical bound')
checks['exact_support_counts_and_3792_bound']=True
print(json.dumps({'status':'PASS','checks':checks,'counts':counts,'physical_J_index_upper_bound':physical_bound,'scope':'tiny exact controls; fixture is non-Keller; no full-ideal construction'},sort_keys=True,indent=2))
