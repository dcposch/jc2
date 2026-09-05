"""Regression probe: D=108 delta=3 stage-0 minor incidence with the D2 weight
floor REMOVED from the h3 inventory (all 45 lower coordinates free).

Reproduces box/g108gate-20260903/band_engine.py:291-352 with vmin forced to 0,
so no monomial is dropped by the raw D2 weight 4r+6q >= cutoff.  If the ideal is
still the unit ideal, the 17(ddddd) kill does not rest on that floor.
"""
import sys, json
from collections import defaultdict
from math import comb, factorial
import sympy as sp

def h3_template_free(cutoff):
    result = {(0,7): sp.Integer(1), (0,8): sp.Integer(2), (0,9): sp.Integer(1)}
    variables = []
    for r in range(1,10):
        vmin = 0 if cutoff is None else max(0, -(-(cutoff-4*r)//6))
        vmin = max(0, vmin)
        cap = 9-r
        for degree in range(vmin, cap+1):
            v = sp.Symbol(f"Hc_{r}_{degree}"); variables.append(v)
            for q in range(vmin, degree+1):
                result[(r,q)] = result.get((r,q), sp.Integer(0)) + v*comb(degree-vmin, q-vmin)
    return {k: sp.expand(v) for k,v in result.items()}, variables

def z_to_w(item):
    out = defaultdict(lambda: sp.Integer(0))
    for (r,q),co in item.items():
        for j in range(q+1):
            out[(r,j)] += co*comb(q,j)*(-1)**(q-j)
    return {k: sp.expand(v) for k,v in out.items() if v != 0}

def rows_for(cutoff):
    h3, variables = h3_template_free(cutoff)
    wb = z_to_w(h3)
    jet1, jet2, c = sp.symbols("jet1 jet2 c")
    coll = defaultdict(lambda: sp.Integer(0))
    for (r,j),co in wb.items():
        for a in range(j+1):
            for b in range(j-a+1):
                k = j-a-b
                lp = r + 2*a + 3*b + 4*k
                if lp > 8: continue
                mn = factorial(j)//(factorial(a)*factorial(b)*factorial(k))
                coll[(lp,k)] += co*mn*jet1**a*jet2**b
    coll[(8,0)] -= c
    coll[(8,2)] += 1
    return [(f"minor_n{p}_pi{k}", sp.expand(v)) for (p,k),v in sorted(coll.items())], variables

sys.path.insert(0, "box/g108gate-20260903")
from band_engine import qstar_reduce  # pinned engine, unchanged

for tag, cutoff in (("baseline_cutoff43", 43), ("control_cutoff42", 42), ("UNCAPPED_no_floor", None)):
    rows, hv = rows_for(cutoff)
    resid, subs, piv, zeros = qstar_reduce(rows, hv)
    jet1, jet2, c, zc = sp.symbols("jet1 jet2 c Zc")
    # Groebner over Q[jet1,jet2,c,Zc, remaining h vars] with Rabinowitsch Zc*c-1
    remaining = sorted({s for _l, v in resid for s in v.free_symbols} | set(hv) - set(subs), key=str)
    gens = [v for _l, v in resid] + [zc*c - 1]
    ringvars = sorted({s for g in gens for s in g.free_symbols}, key=str)
    G = sp.groebner(gens, *ringvars, order='grevlex')
    unit = (list(G.exprs) == [sp.Integer(1)])
    print(f"{tag:22s} h3_free_coords={len(hv):3d}  Qstar_pivots={len(piv):2d} "
          f"residual_rows={len(resid)}  GB={list(G.exprs)[:3]}  UNIT={unit}")
