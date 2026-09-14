#!/usr/bin/env python3
"""Read-only exact source/chain arithmetic controls; stdlib only, no CAS/solve.

This does not verify an imported theorem or assert that the source has a point.
"""
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from math import comb, gcd
from pathlib import Path
import json
import re

BOX = Path(__file__).resolve().parent
REPO = BOX.parents[1]
SOURCE = REPO / 'box/char-degree-20260905/d108/selected/meanfree_stage8_slimgb/d108_meanfree_stage8_strongfront.input.json'
SOURCE_SHA = '1c927d83aa4684ae91bfffc8d03500fbabb73a500faa222fa349a6d129a10814'

def require(test, name):
    if not test:
        raise ValueError(name)

def split_top(s):
    parts = []
    depth = start = 0
    for i, ch in enumerate(s):
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        elif ch == '+' and depth == 0:
            parts.append(s[start:i]); start = i + 1
        require(depth >= 0, 'balanced source')
    require(depth == 0, 'balanced source')
    return parts + [s[start:]]

def parse(s, normalizer):
    rows = []
    for part in split_top(s):
        match = re.fullmatch(r'\((.*)\)\*tt\^(\d+)\*zz\^(\d+)', part)
        require(match is not None, 'literal source grammar')
        c, r, w = match.groups()
        r, w = int(r), int(w)
        rows.append((normalizer - r - w, w, c))
    return rows

def check_source(rows):
    for key, values in rows.items():
        require(all(x >= 0 and w >= 0 for x, w, c in values), 'physical polynomiality')
        require(max(x for x, w, c in values) == 8, 'source x bound')
        require(max(4*x-w for x, w, c in values) == 4, 'source weight bound')
    require([max(x+w for x,w,c in rows[k]) for k in ('h','D','C')] == [36,37,38], 'degree bounds')
    require([(x,w,Q(c)) for x,w,c in rows['h'] if x == 8] == [(8,28,Q(1))], 'highest x slot')
    face = {(x,w):Q(c) for x,w,c in rows['h'] if 4*x-w == 4}
    expected = {(1+k,4*k):Q(comb(7,k)*(-1)**(7-k)) for k in range(8)}
    require(face == expected, 'complete fixed edge')

# Tiny multiplication in Q[lambda,V]/(lambda^4-root_value), with integer input.
def mul(p, q, root_value):
    result = {}
    for (v,l), a in p.items():
        for (w,k), b in q.items():
            key = (v+w,(l+k)%4)
            result[key] = result.get(key,0) + a*b*root_value**((l+k)//4)
    return {k:v for k,v in result.items() if v}

def shifted(power=7, root_value=1):
    # ((V+lambda)^4-1)^power, retaining the quotient-ring arithmetic.
    base = {(k,(4-k)%4):comb(4,k)*root_value**((4-k)//4) for k in range(5)}
    base[(0,0)] -= 1
    base = {k:v for k,v in base.items() if v}
    result = {(0,0):1}
    for _ in range(power):
        result = mul(result,base,root_value)
    return result

def check_cut(power=7, root_value=1, denominator=4, expected_corner=(Q(11,4),Q(7))):
    p = shifted(power,root_value)
    order = min(v for v,l in p)
    require(order == 7, 'root multiplicity seven')
    require({l:c for (v,l),c in p.items() if v == 7} == {1:4**7}, 'nonzero leading coefficient 4^7 lambda')
    actual_corner = (1+Q(order,denominator),Q(order))
    require(actual_corner == expected_corner, 'actual normalized successor')
    return p

def check_split(a=7,l=1,claimed=(3,)):
    allowed = tuple(d for d in range(l+1,(a+1)//2) if (d-l) % (a-2*d) == 0)
    require(allowed == claimed, 'published split-root divisor test')
    return allowed

def rejected(name, operation):
    try:
        operation()
    except ValueError:
        return name
    raise AssertionError('mutation not rejected: '+name)

def run():
    raw = SOURCE.read_bytes()
    require(sha256(raw).hexdigest() == SOURCE_SHA,'frozen source hash')
    data = json.loads(raw)
    rows = {k:parse(data[k+'_expr'],N) for k,N in [('h',36),('D',71),('C',107)]}
    check_source(rows)
    p = check_cut()
    require(gcd(11,7) == 1 and Q(4)-Q(11,7) > 1,'final-corner numerical criteria')
    require(Q(108,72) == Q(24,16) == Q(3,2),'standard degree ratios')
    require(24-84 == -60 and 16-56 == -40,'standard endpoint signs')
    require((3*36,2*36) == (108,72),'published degree row')
    require(3*(Q(11,4),)[0] == Q(33,4),'F successor scaling')
    split = check_split()
    single = tuple(s for s in range(-5,-1) if 7+2*s > 0)
    require(single == (-3,-2),'single-root direction alternatives')
    # Exact positivity cone: d = alpha*(1,-1)+beta*(-1,4), alpha,beta>=0.
    corner = (84,24)
    cone_values = (corner[0]-corner[1],-corner[0]+4*corner[1])
    require(cone_values == (60,12),'positive cone endpoint values')
    # A meaningful non-Keller control retaining the two numerical degrees/edge.
    # P=[y(y*x^4-1)^7]^3+1 has predecessor (2,-7), valuation exactly zero.
    support = [(0,0)]+[(4*k,3+k) for k in range(22)]
    values = [2*x-7*y for x,y in support]
    require(max(values) == 0,'zero predecessor control')
    require([v for v,t in zip(support,values) if t == 0] == [(0,0),(84,24)],'zero edge endpoints')
    require(all(-x+4*y == 12 for x,y in support[1:]),'fixed-edge control')
    bad = deepcopy(rows)
    bad['h'] = [(x,w,'2' if (x,w)==(8,28) else c) for x,w,c in bad['h']]
    mutations = [
      rejected('source highest-face coefficient 1 -> 2',lambda:check_source(bad)),
      rejected('root power 7 -> 6',lambda:check_cut(power=6)),
      rejected('root equation lambda^4=1 -> lambda^4=2',lambda:check_cut(root_value=2)),
      rejected('ramification denominator 4 -> 3',lambda:check_cut(denominator=3)),
      rejected('successor 11/4 -> 7/4',lambda:check_cut(expected_corner=(Q(7,4),Q(7)))),
      rejected('incorrectly permit split direction (1,-2)',lambda:check_split(claimed=(2,3)))
    ]
    return {
      'status':'D108_PUBLISHED_CASE_SMALL_CONTROLS_PASS',
      'source_sha256':SOURCE_SHA,
      'source_slots':{k:len(v) for k,v in rows.items()},
      'standard_pair_requires_actual_Keller_equation':True,
      'starting_chain':{'A0':['8','28'],'A0_prime':['1','0'],'direction':[4,-1],
                        'A1':['11/4','7'],'l1':4,'m_n':[3,2],'degrees':[108,72]},
      'root_control':{'relation':'lambda^4=1','gcd_identity':'(z/4)*(4*z^3)-(z^4-1)=1',
                      'shifted_power':7,'V_order':7,'V7_coefficient':'16384*lambda',
                      'expanded_quotient_ring_terms':len(p)},
      'split_delta_allowed':list(split),
      'single_root_sigma_allowed':list(single),
      'positivity_proved_cone':[[1,-1],[-1,4]],
      'positivity_cone_corner_values':list(cone_values),
      'non_Keller_control':{'P':'[y(y*x^4-1)^7]^3+1','Q':'[y(y*x^4-1)^7]^2+1',
                           'Jacobian':'0 by chain rule','predecessor':[2,-7],'valuation':0,
                           'purpose':'Numerical/fixed-edge data alone do not extend the positivity interval.'},
      'genuine_mutations_rejected':mutations,
      'claims_not_tested':['published theorem proofs','case-table enumeration','source properness',
                           'Keller point existence','coefficientwise full transport','external exclusion certificates']}

if __name__ == '__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
