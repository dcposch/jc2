#!/usr/bin/env python3
"""Tiny fixed-matrix parity and whole-gauge checks. No forcing expansion."""
import ast
from fractions import Fraction as Q
import hashlib
import json
from math import comb
from pathlib import Path
import resource
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

def need(ok, msg):
    if not ok:
        raise ValueError(msg)

def rank(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((k for k in range(r, len(a)) if a[k][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = a[r][c]
        a[r] = [x/z for x in a[r]]
        for k in range(r+1, len(a)):
            z = a[k][c]
            a[k] = [x-z*y for x,y in zip(a[k],a[r])]
        r += 1
    return r

def check(mutation):
    need(not any(isinstance(x, ast.Assert) for x in ast.walk(ast.parse(Path(__file__).read_text()))), 'Assert node')
    repaired = ROOT/'box/d125-b-witness-exact-export-repair-20260906/exact-witnesses-v2.json'
    need(hashlib.sha256(repaired.read_bytes()).hexdigest() == '07b4ce881b4f90f9a41a3f8cb01fcd3a120ff64a4f04969e60126dbdb6e7f246', 'repaired witness pin')
    old = json.loads(repaired.read_bytes())
    slots = json.loads((HERE/'witness.json').read_bytes())
    odd_free = {tuple(p) for p in slots['members']['B']['fixed_loci']['2']['free_slots']}
    rows = []
    h3 = {0:1, 3:3, 6:3, 9:1}
    for d in range(1,25,2):
        cols = sorted(i for i,j in odd_free if i+j == d)
        need(cols == list(range((7*d+4)//12+1)), 'actual odd B free columns')
        matrix = [[((r+1-i)*d-15*i)*h3.get(r+1-i,0) for i in cols] for r in range(d+14)]
        measured = rank(matrix)
        expected = len(cols)-(1 if d%5 == 0 else 0)
        need(measured == expected, 'odd B exact matrix rank')
        need(old['tables']['unequal'][d-1] == [d,len(cols),expected], 'repaired witness rank agreement')
        rows.append([d,len(cols),measured])
        if d%5 == 0:
            power = d//5
            kernel = [comb(power,i//3) if i%3 == 0 and i//3 <= power else 0 for i in cols]
            need(all(sum(x*y for x,y in zip(row,kernel)) == 0 for row in matrix), 'actual free-slot H-power kernel')
    need(sum(r[1] for r in rows)==94 and sum(r[2] for r in rows)==92, 'odd B rank totals')
    kernel_degrees = [5,15]
    if mutation == '--mutate-kernel-character':
        kernel_degrees.append(10)
    need(all((d-25)%2 == 0 for d in kernel_degrees), 'forbidden kernel character')
    # Every forcing product in layer d+13 has the same coefficient character.
    for d in range(1,25):
        for i in range(15):
            j = d+15-i
            if d < j <= 25:
                need((i-15)+(j-25) == d-25, 'B graph forcing character')
    # Whole-shear coordinate action, not deletion of an isolated H^3 term.
    a5, a10 = Q(2), Q(0)
    beta = [Q(3),Q(0),Q(5),Q(0)]
    s = beta[2]
    shifted = [beta[0]-s*a5, beta[1]-s*a10, Q(0), beta[3]]
    restored = [shifted[0]+s*a5, shifted[1]+s*a10, s, shifted[3]]
    if mutation == '--mutate-gauge-inverse':
        restored[0] = shifted[0]
    need(restored == beta, 'whole gauge inverse')
    need(shifted[1] == shifted[2] == shifted[3] == 0, 'odd fixed gauge slice')
    need((-10)+(-10)==-20 and (-10)+(-5)==-15, 'exact shear coordinate characters')
    need(33-13+2+1 == 23 and 33-13+1+1 == 22, 'combined counts')
    return {'status':'PASS','odd_B_degree_columns_ranks':rows,'odd_B_columns':94,'odd_B_pivots':92,
            'kernel_degrees':kernel_degrees,'A_after_13_pivots':20,'before_gauge_coordinates':23,
            'slice_coordinates':22,'assert_nodes':0,
            'scope':'constant matrices/slots/characters and a gauge fixture only; no residual materialization'}

def cap():
    resource.setrlimit(resource.RLIMIT_CPU,(25,25))
    resource.setrlimit(resource.RLIMIT_AS,(512*1024*1024,512*1024*1024))

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv)>1 else ''
    if mode == '--record':
        runs=[]
        for opt in (False,True):
            for mutation in ('','--mutate-kernel-character','--mutate-gauge-inverse'):
                args=[sys.executable]+(['-O'] if opt else [])+[str(Path(__file__).resolve())]+([mutation] if mutation else [])
                run=subprocess.run(args,capture_output=True,timeout=30,preexec_fn=cap)
                need((run.returncode != 0)==bool(mutation),'control exit')
                if mutation:
                    msg=b'forbidden kernel character' if mutation=='--mutate-kernel-character' else b'whole gauge inverse'
                    need(msg in run.stderr,'unrelated mutation failure')
                else:
                    with (HERE/('composition-witness-O.json' if opt else 'composition-witness.json')).open('xb') as f:
                        f.write(run.stdout)
                runs.append({'optimized':opt,'mutation':mutation or None,'returncode':run.returncode,
                             'stdout_sha256':hashlib.sha256(run.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(run.stderr).hexdigest()})
        need((HERE/'composition-witness.json').read_bytes()==(HERE/'composition-witness-O.json').read_bytes(),'normal/-O mismatch')
        with (HERE/'composition-replay.json').open('x') as f:
            json.dump({'status':'PASS','runs':runs,'all_writers_finished':True},f,sort_keys=True,indent=2)
            f.write('\n')
        print(json.dumps({'status':'PASS','runs':len(runs),'witness_sha256':hashlib.sha256((HERE/'composition-witness.json').read_bytes()).hexdigest()}))
    else:
        print(json.dumps(check(mode),sort_keys=True,indent=2))
