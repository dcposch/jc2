#!/usr/bin/env python3
"""Read-only audit of the banked sharpened cohort; no new chart equivalence."""
import collections
import hashlib
import json
import sys
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path('/home/ubuntu/jc2')
OUT = Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)
p = ROOT / 'box/xufloor-20260903/results.json'
upstream = json.loads((ROOT / 'box/h1nonres-20260903/summary.json').read_text())
digest = hashlib.sha256(p.read_bytes()).hexdigest()
assert digest == upstream['provenance']['screen_snapshot']['sha256']
source = json.loads(p.read_text())

def transform(r):
    us, vs = r['u_s'], r['V_s']
    ds = us + vs
    n, m = F(r['n'] * us, ds), F(r['m'] * us, ds)
    ell = vs - us - 1
    assert n.denominator == m.denominator == 1
    M = tuple(F(v * us, ds) for v in [-r['m']] + r['M'][:-1])
    V = tuple(sorted((int(k), int(v)) for k,v in r['V'].items() if int(k) < r['s']))
    h = len(M)
    effective_M = list(M)
    while effective_M and effective_M[-1] == n - 1:
        effective_M.pop()
    heff = len(effective_M)
    return (int(n), int(m), ell, r['V']['2']), (M,V,h,heff), ds

def audit(rows):
    classes=collections.defaultdict(list)
    triples=collections.defaultdict(list)
    decorated=collections.defaultdict(list)
    for r in rows:
        key,dec,ds=transform(r)
        classes[key].append((r,dec))
        triples[key[:3]].append(r)
        decorated[(key,dec)].append(r)
    collisions=[]
    for key,members in classes.items():
        signatures=collections.defaultdict(list)
        for r,dec in members:
            signatures[dec].append(r)
        if len(signatures)>1:
            examples=[]
            for dec,rs in list(signatures.items())[:3]:
                r=rs[0]
                examples.append(dict(parent=[r['n'],r['m'],r['M'],r['V']],
                                     M_prime=list(map(str,dec[0])),V_prime=dec[1],
                                     raw_height=dec[2],effective_height=dec[3]))
            collisions.append(dict(class_key=key,distinct_decorations=len(signatures),examples=examples))
    return dict(rows=len(rows),quadruple_classes=len(classes),triple_classes=len(triples),
        fully_decorated_classes=len(decorated),quadruple_compression=len(rows)/len(classes),
        triple_compression=len(rows)/len(triples),
        quadruple_ell_histogram=dict(sorted(collections.Counter(k[2] for k in classes).items())),
        raw_height_histogram=dict(sorted(collections.Counter(transform(r)[1][2] for r in rows).items())),
        effective_height_histogram=dict(sorted(collections.Counter(transform(r)[1][3] for r in rows).items())),
        ratio_histogram={str(k):v for k,v in sorted(collections.Counter((r['n']//gcd(r['n'],r['m']),r['m']//gcd(r['n'],r['m'])) for r in rows).items())},
        collided_quadruple_classes=len(collisions),collision_examples=collisions[:8],
        original_keys=sorted(r['row_key'] for r in rows),
        quadruple_members=[dict(key=k,original_keys=sorted(r['row_key'] for r,dec in members))
                           for k,members in sorted(classes.items())],
        triple_members=[dict(key=k,original_keys=sorted(r['row_key'] for r in members))
                        for k,members in sorted(triples.items())],
        full_decorations=[dict(key=k[0],M_prime=list(map(str,k[1][0])),V_prime=k[1][1],
                               raw_height=k[1][2],effective_height=k[1][3],
                               original_keys=sorted(r['row_key'] for r in members))
                          for k,members in sorted(decorated.items())])

poly=[r for r in source['rows'] if r['phase']=='us_gt_1']
selected=[r for r in poly if r['xu_ok_candidate']]
assert len(poly)==310 and len(selected)==296
result=dict(source_path=str(p),source_sha256=digest,
            provenance='MEASURED auxiliary sharpened cohort, not a promoted universal census',
            interpretation='Quadruple equality is arithmetic only; transformed radii and height are no-split metadata conditional on licensed descent.',
            selected=audit(selected),poly_ode=audit(poly))
(OUT/'cohort-compression.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({cohort:{key:value for key,value in result[cohort].items()
                        if key not in ('original_keys','quadruple_members','triple_members','full_decorations','collision_examples')}
                  for cohort in ('selected','poly_ode')},indent=2))
