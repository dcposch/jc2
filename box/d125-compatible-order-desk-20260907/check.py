#!/usr/bin/env python3
"""Tiny A-Hermite order refinement only; no source-row expansion or CAS."""
import ast
from collections import Counter
import hashlib
import importlib.util
from itertools import permutations
import json
from math import comb
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT/'box/d125-small-source-exporter-prep-20260906/baseline.py'
WIT = ROOT/'box/d125-defect-order-discriminator-20260907/witnesses.json'
def need(ok, why):
    if not ok:
        raise ValueError(why)
def sha(data):
    return hashlib.sha256(data).hexdigest()
need(sha(BASE.read_bytes()) == 'ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53', 'baseline pin')
need(sha(WIT.read_bytes()) == '6e8c0102089ca6d046f4e1834ce30917a1dff6b2ad7d8ab29de95e7fc7eb83a1', 'three-row witness pin')
need(not any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(BASE.read_bytes()))), 'imported asserts')
spec = importlib.util.spec_from_file_location('baseline', BASE)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
contract = base.make_contract('unequal', 'rational')
old = json.loads(WIT.read_bytes())['order']
names = old['variables']
need(names == contract['variables']+['lambda2','lambda3'], 'names')
weights = [row[:] for row in old['weight_rows']]
w4, w5 = [0]*269, [0]*269
by_degree = {}
for row in contract['coefficient_maps'][0]:
    if 'variable' in row:
        i,j = row['point']
        ix = row['variable']
        w4[ix] = 15-i-j
        w5[ix] = -i
        by_degree.setdefault(i+j, []).append(i)
mode = sys.argv[1] if len(sys.argv)>1 else 'normal'
need(mode in ('normal', 'no-w4', 'reverse-w5'), 'mode')
if mode == 'no-w4':
    w4 = [0]*269
if mode == 'reverse-w5':
    w5 = [-x for x in w5]
weights += [w4,w5]
ids = {name:i for i,name in enumerate(names)}
def key(m):
    c = Counter(m)
    return tuple(sum(row[i] for i in m) for row in weights)+(len(m),)+tuple(-c[i] for i in range(268,-1,-1))
need(key((ids['A_g0_p1'],)) > key((ids['A_g0_p3'], ids['lambda3'])), 'actual higher-degree lambda forcing')
need(key((ids['A_g0_p2'],)) > key((ids['A_g1_p1'],)), 'actual same-degree nonpivot')
blocks = []
degree_cases = 0
for s in range(1,15):
    r = (s+4)//5
    need(all(i in by_degree[s] for i in range(r)), 'actual selected A slots')
    mat = [[(-1)**(s-i-t)*comb(s-i,t) for i in range(r)] for t in range(r)]
    determinant = 0
    for perm in permutations(range(r)):
        inversions = sum(perm[i]>perm[j] for i in range(r) for j in range(i+1,r))
        term = (-1)**inversions
        for t,i in enumerate(perm):
            term *= mat[t][i]
        determinant += term
    need(abs(determinant)==1, 'unit Hermite minor')
    for i in range(r):
        for h in by_degree[s]:
            if h>=r:
                need(key((ids[f'A_g{i}_p{s-i}'],)) > key((ids[f'A_g{h}_p{s-h}'],)), 'same-layer direction')
    for b in range(8):
        for d in range(8):
            k = s+3*b+2*d
            if b+d and k<=15:
                need(15-k+3*b+2*d == 15-s, 'W1 row homogeneity')
                need(15-k < 15-s, 'W4 strict forcing')
                degree_cases += 1
    blocks.append({'degree':s, 'pivot_g_exponents':list(range(r)), 'determinant':determinant})
need(sum(len(b['pivot_g_exponents']) for b in blocks)==27, '27 A pivots')
need(all(v>0 for v in weights[0]), 'global first weight')
descriptor = {'schema':'jc2.d125-compatible-defect-order/v1', 'field':'Q',
              'variables':names, 'weight_rows':weights, 'tie_break':'dp',
              'comparison':'lexicographically larger (W1,W2,W3,W4,W5,total,-last,...,-first)'}
wire = (json.dumps(descriptor,sort_keys=True,separators=(',',':'))+'\n').encode()
print(json.dumps({'status':'PASS_A_REFINEMENT_ONLY', 'A_leaders':27,
                  'B_leaders_inherited_conditionally':192, 'remaining_names':50,
                  'blocks':blocks, 'degree_cases':degree_cases, 'order':descriptor,
                  'order_sha256':sha(wire)},sort_keys=True))
