#!/usr/bin/env python3
"""Exact monomial map and leader target-subtraction controls for the instrument."""
import hashlib
import json
from math import comb
from pathlib import Path

HERE=Path(__file__).resolve().parent

def xy_to_tz(xy,B):
    out={}
    for (p,q),v in xy.items():
        assert p>=0 and q>=0 and p+q<=B
        for j in range(q+1):
            key=(B-p-q,j)
            out[key]=out.get(key,0)+v*comb(q,j)
    return {key:v for key,v in out.items() if v}

def tz_to_tw(tz):
    out={}
    for (r,j),v in tz.items():
        for q in range(j+1):
            key=(r,q)
            out[key]=out.get(key,0)+v*comb(j,q)*(-1)**(j-q)
    return {key:v for key,v in out.items() if v}

def row_images(tw,B,target,leader,inv):
    L=B-target
    rows=[]
    for r in range(L+1):
        for q in range(target,B-r+1):
            value=tw.get((r,q),0)
            if (r,q)==(L,target): value-=leader
            rows.append((f't{r}_w{q}',value))
    rows.append(('localizer',leader*inv-1))
    return rows

records=[]
for B,d,wt,expected in [(198,55,(3,4),10441),(216,63,(4,5),11936)]:
    L=B-d
    # A scalar unit leader with substantial allowed total degree: this must
    # pass. It would fail an unjustified total-degree <= d implementation.
    good={(0,d):1,(B-1,1):17,(0,0):5}
    direct={(B-p-q,q):v for (p,q),v in good.items()}
    tw=tz_to_tw(xy_to_tz(good,B))
    assert tw==direct
    goodrows=row_images(tw,B,d,1,1)
    assert len(goodrows)==expected and all(v==0 for _,v in goodrows)
    # An upper degree violation and a nonconstant leader violate exactly
    # their intended scalar coefficient rows.
    bad={**good,(2,d+1):3,(1,d):7}
    badtw=tz_to_tw(xy_to_tz(bad,B))
    violations=[(l,v) for l,v in row_images(badtw,B,d,1,1) if v]
    assert violations==[(f't{L-3}_w{d+1}',3),(f't{L-1}_w{d}',7)]
    # The valid point has coefficient 1 at the leading row: zeroing that
    # coefficient instead of subtracting the unit target would reject it.
    assert tw[L,d]==1
    records.append(dict(B=B,target=d,defect=L,formal_scalar_row_count=expected,
                        leader_site=[L,d],D2_leader_weight=wt[0]*L+wt[1]*d,
                        allowed_high_total_degree_control={'xy_terms':[[p,q,v] for (p,q),v in good.items()],
                                                          'violations':0},
                        wrong_above_or_lc_rows=violations,
                        forbidden_zero_leader_residual=1,
                        target_subtracted_leader_residual=0,
                        coefficient_map='[t^r w^q] KQ = [x^(B-r-q)y^q]Q; w=1+z'))

record={'coefficient_field':'Q','cases':records,
        'self_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(HERE/'row_index_control.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
print(json.dumps(record,indent=2,sort_keys=True))
