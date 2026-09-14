#!/usr/bin/env python3
"""Fast reduced scan for monomial b2,b1,b0 in the h=z^3 specialization.

The z^14,...,z^5 Jacobian equations integrate explicitly and leave seven
integration constants a1,a2,a3,a4,a5,a7,a8.  The remaining z^4,...,z^0
equations are linear in those constants for fixed b2,b1,b0.  This scanner
uses that exact reduction over GF(p).
"""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


V = {name: i for i, name in enumerate(("a1", "a2", "a3", "a4", "a5", "a7", "a8"))}


def poly_term(exp, coeff, p):
    return {} if coeff % p == 0 else {exp: coeff % p}


def deriv(f, p):
    return {e - 1: e * c % p for e, c in f.items() if e and e * c % p}


def mul(f, g, p):
    out = {}
    for i, a in f.items():
        for j, b in g.items():
            out[i + j] = (out.get(i + j, 0) + a * b) % p
            if not out[i + j]:
                del out[i + j]
    return out


def add_equation(rows, level, unknown, coeff, scale, p, allow_target=False):
    for exp, value in coeff.items():
        value = value * scale % p
        if not value:
            continue
        if allow_target and exp == 8:
            row = rows.setdefault(("target", 8), {})
        else:
            row = rows.setdefault((level, exp), {})
        col = V[unknown] if unknown is not None else -1
        row[col] = (row.get(col, 0) + value) % p
        if not row[col]:
            del row[col]


def sum_poly(*fs, p):
    out = {}
    for f in fs:
        for e, c in f.items():
            out[e] = (out.get(e, 0) + c) % p
            if not out[e]:
                del out[e]
    return out


def scale(f, a, p):
    return {e: a * c % p for e, c in f.items() if a * c % p}


def form_rows(b2, b1, b0, p):
    d2, d1, d0 = deriv(b2, p), deriv(b1, p), deriv(b0, p)
    b2d2 = mul(b2, d2, p)
    b1d2_b2d1 = sum_poly(mul(b1, d2, p), mul(b2, d1, p), p=p)
    b0d2_b1d1_b2d0 = sum_poly(mul(b0, d2, p), mul(b1, d1, p), mul(b2, d0, p), p=p)
    b0d1_b1d0 = sum_poly(mul(b0, d1, p), mul(b1, d0, p), p=p)
    b0d0 = mul(b0, d0, p)
    b2sq_d2 = mul(mul(b2, b2, p), d2, p)
    rows = {}
    def ae(level, u, f, n, target=False):
        add_equation(rows, level, u, f, n, p, target)

    # z^4 numerator
    ae(4,"a3",d2,18); ae(4,"a4",d1,24); ae(4,"a5",d0,30)
    ae(4,"a7",b2d2,7); ae(4,"a8",b1d2_b2d1,16)
    ae(4,None,b0d2_b1d1_b2d0,27)
    # z^3
    ae(3,"a2",d2,12); ae(3,"a3",d1,18); ae(3,"a4",d0,24)
    ae(3,"a7",b1d2_b2d1,7); ae(3,"a8",b0d2_b1d1_b2d0,16)
    ae(3,None,b0d1_b1d0,27)
    # z^2
    ae(2,"a1",d2,24); ae(2,"a2",d1,48); ae(2,"a3",d0,72)
    ae(2,"a5",b2d2,-20); ae(2,"a7",b0d2_b1d1_b2d0,28)
    ae(2,"a8",b0d1_b1d0,64); ae(2,None,b0d0,108); ae(2,None,b2sq_d2,-27)
    # z^1
    ae(1,"a1",d1,72); ae(1,"a2",d0,144); ae(1,"a4",b2d2,-96)
    ae(1,"a5",b1d2_b2d1,-60); ae(1,"a7",b0d1_b1d0,84)
    ae(1,"a8",b0d0,192); ae(1,"a8",b2sq_d2,-64)
    ae(1,None,mul(mul(b1,b2,p),d2,p),-162)
    ae(1,None,mul(mul(b2,b2,p),d1,p),-81)
    # z^0; x^8 is the allowed nonzero target, all other powers vanish.
    ae(0,"a1",d0,72,True); ae(0,"a4",mul(b1,d2,p),-48,True)
    ae(0,"a5",mul(b1,d1,p),-60,True); ae(0,"a5",mul(b2,d0,p),60,True)
    ae(0,"a7",b0d0,84,True)
    ae(0,"a8",mul(mul(b1,b2,p),d2,p),-32,True)
    ae(0,None,mul(mul(b1,b1,p),d2,p),-54,True)
    ae(0,None,mul(mul(b1,b2,p),d1,p),-54,True)
    ae(0,None,mul(mul(b2,b2,p),d0,p),27,True)
    target = rows.pop(("target",8), {})
    return [(k, r) for k, r in rows.items() if r], target


def echelon(rows, p):
    pivots = {}
    for _key, original in rows:
        row = dict(original)
        while True:
            cols = [c for c in row if c >= 0]
            if not cols:
                if row.get(-1, 0):
                    return pivots, True
                break
            pivot = min(cols)
            if pivot not in pivots:
                inv = pow(row[pivot], -1, p)
                row = {c: v * inv % p for c, v in row.items() if v * inv % p}
                for old in pivots.values():
                    fac = old.get(pivot, 0)
                    if fac:
                        for c, v in row.items():
                            old[c] = (old.get(c, 0) - fac*v) % p
                            if not old[c]: old.pop(c, None)
                pivots[pivot] = row
                break
            fac = row[pivot]
            for c, v in pivots[pivot].items():
                row[c] = (row.get(c, 0) - fac*v) % p
                if not row[c]: row.pop(c, None)
    return pivots, False


def reduce_target(target, pivots, p):
    row = dict(target)
    for pivot in sorted(pivots):
        fac = row.get(pivot, 0)
        if fac:
            row.pop(pivot, None)
            base = pivots[pivot]
            for c, v in base.items():
                if c == pivot: continue
                if c == -1:
                    # Pivot rows are stored as p_pivot + ... + const = 0.
                    row[-1] = (row.get(-1,0) - fac*v) % p
                else:
                    row[c] = (row.get(c,0) - fac*v) % p
                    if not row[c]: row.pop(c,None)
    return row


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--prime',type=int,default=32003)
    ap.add_argument('--coeff-min',type=int,default=-12)
    ap.add_argument('--coeff-max',type=int,default=12)
    ap.add_argument('--out',type=Path)
    ap.add_argument('--all-field',action='store_true')
    args=ap.parse_args(); p=args.prime
    coeffs=range(1,p) if args.all_field else [i%p for i in range(args.coeff_min,args.coeff_max+1) if i]
    hits=[]; seen=0
    # All three terms present.  Torus scaling leaves one coefficient invariant;
    # normalize b2=b1=1 and scan b0=C.
    for e2,e1,e0 in itertools.product(range(13),range(16),range(19)):
        target_degrees = {
            e0 - 1, e1 + e2 - 1, 2*e1 - 1, e2 + e0 - 1,
            2*e0 - 1, e1 + 2*e2 - 1, 2*e1 + e2 - 1,
            2*e2 + e0 - 1,
        }
        if 8 not in target_degrees:
            continue
        for C in coeffs:
            seen += 1
            rows,target=form_rows(poly_term(e2,1,p),poly_term(e1,1,p),poly_term(e0,C,p),p)
            piv,bad=echelon(rows,p)
            if bad: continue
            tr=reduce_target(target,piv,p)
            if any(v for c,v in tr.items() if c>=0) or tr.get(-1,0):
                hit={'exponents':[e2,e1,e0],'coefficients':[1,1,C],
                     'rank':len(piv),'target_reduced':tr}
                hits.append(hit); print(json.dumps(hit),flush=True)
    payload={'prime':p,'seen':seen,'hits':hits,'hit_count':len(hits)}
    if args.out: args.out.write_text(json.dumps(payload,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:payload[k] for k in ('prime','seen','hit_count')}))


if __name__=='__main__': main()
