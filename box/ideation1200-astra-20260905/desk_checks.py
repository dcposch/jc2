#!/usr/bin/env python3
"""Desk arithmetic from SEALED fullorder/socle tables; no CAS or live-lane reads.
Ordinary Python only; no claim about optimized interpreter modes.
"""
from fractions import Fraction as Q
from math import floor
import json

# name, K, V2, delta1, Bsafe, banked fullorder parameter count.
FIBRES = [
    ('M6_13/V1_1',4,1,'9/4','-15/4',333),
    ('M6_13/V1_3',4,1,'1/2','-11/2',378),
    ('M6_13/V4_3',4,4,'-2/3','-8/3',155),
    ('M2_9/V1_8',6,1,'19/48','-71/48',120),
    ('M2_9/V3_8',6,3,'-1/8','-3/2',88),
    ('Mm12_m2_5/V1_1_6',8,1,'1/18','-13/18',77),
    ('M12_17/V2_1',8,2,'8/9','-2/9',153),
    ('M12_17/V1_2',8,1,'7/6','-7/6',251),
    ('M12_17/V3_2',8,3,'1/3','-2/3',118),
    ('Mm15_14/V1_9',6,1,'-5/36','-5/4',126),
    ('M9_20/V1_9',6,1,'1/4','-37/12',341),
    ('M9_20/V4_9',6,4,'-1/3','-8/3',248),
]
out=[]
for name,K,V2,delta,B,n in FIBRES:
    d1,B=Q(delta),Q(B)
    raw={(r,s) for s in range(K) for r in range(max(0,floor(d1*s-B)+1))}
    old={(r,s) for r,s in raw if r<=max(K-V2,0) and r+s<=K}
    missing=sorted(raw-old)
    out.append(dict(fibre=name,K=K,V2=V2,delta1=str(d1),B_safe=str(B),
                    old_h_count=len(old),raw_h_count=len(raw),h_coker=len(missing),
                    old_parameters=n,expanded_parameters=n+len(missing),
                    missing_monomials=missing))

def homogeneous_count(weights,cap):
    counts=[0]*(cap+1);counts[0]=1
    for w in weights:
        for d in range(w,cap+1):counts[d]+=counts[d-w]
    return counts

squares=[]
for t in range(8,12):
    target=8*t+2
    counts=homogeneous_count(list(range(1,t))+[t+1],target)
    generator_weights=[4*t+1-k for k in range(1,2*t)]
    rows=sum(counts[target-d] for d in generator_weights if d<=target)
    squares.append(dict(t=t,weights=list(range(1,t))+[t+1],square_weight=target,
                        ambient_columns=counts[target],raw_macaulay_rows=rows))

# Logical control: same graded algebra, equal-degree marked elements,
# different square behaviour. A=Q[X,Y]/(X^2,Y^4), deg X=deg Y=1.
# Its standard monomials are X^a Y^b with 0<=a<2, 0<=b<4.
std={(a,b) for a in range(2) for b in range(4)}
if (2,0) in std or (0,2) not in std:
    raise RuntimeError('socle logical control failed')

# Legacy cap really deletes a D1-allowed monomial in both big fibres.
for row in out[:2]:
    if [2,3] not in [list(m) for m in row['missing_monomials']]:
        raise RuntimeError('h support negative control failed')
print(json.dumps(dict(scope='EXACT_INTEGER_ARITHMETIC; no source-necessity or emptiness verdict',
                      h_inventory=out,square_matrix_sizes=squares,
                      socle_control='same ring and Hilbert series; X^2=0 but Y^2!=0',
                      h_control='x^2*y^3 omitted on both big fibres despite D1 inequality'),indent=2))
