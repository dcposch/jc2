#!/usr/bin/env python3
"""Tiny exact coordinate/acceptance controls; no CAS, ideal expansion or solve."""
from fractions import Fraction as Q
from math import comb
import json

def clean(p):
    return {e: Q(c) for e, c in p.items() if c}

def add(p, q):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, 0) + c
    return clean(r)

def scale(p, c):
    return clean({e: c*v for e, v in p.items()})

def mul(p, q):
    r = {}
    for (a,b), c in p.items():
        for (d,e), f in q.items():
            v = (a+d, b+e)
            r[v] = r.get(v, 0) + c*f
    return clean(r)

def deriv(p, k):
    r = {}
    for e, c in p.items():
        if e[k]:
            f = list(e)
            f[k] -= 1
            r[tuple(f)] = c*e[k]
    return clean(r)

def jac(p, q):
    return add(mul(deriv(p,0),deriv(q,1)), scale(mul(deriv(p,1),deriv(q,0)),-1))

def source_image(p):
    r = {}
    for (i,j), c in p.items():
        assert i >= 0 and j >= 0
        for k in range(j+1):
            e = (5*i-k, j-k)
            r[e] = r.get(e,0) + c*comb(j,k)
    return clean(r)

def undo_translation(p):
    r = {}
    for (a,b), c in p.items():
        assert b >= 0
        for k in range(b+1):
            e = (a-k,b-k)
            r[e] = r.get(e,0) + c*comb(b,k)*(-1)**k
    return clean(r)

def descend(p):
    r = undo_translation(p)
    if any(a < 0 or a % 5 or b < 0 for a,b in r):
        raise ValueError("outside the translated ordinary polynomial image")
    return {(a//5,b):c for (a,b),c in r.items()}

def xy_to_tz(p):
    return clean({(a,a-b):c for (a,b),c in p.items()})

def band_monomial(i,j):
    ell = 5*i-j
    return {(ell+k,ell):Q(comb(j,k)) for k in range(j+1)}

def expect_equal(p,q):
    if clean(p) != clean(q):
        raise ValueError("polynomial identity mismatch")

def rejected(fn):
    try:
        fn()
    except (ValueError,AssertionError):
        return True
    raise AssertionError("mutation incorrectly accepted")

checks = {}
for i in range(4):
    for j in range(5):
        p = {(i,j):Q(1)}
        expect_equal(descend(source_image(p)),p)
        expect_equal(xy_to_tz(source_image(p)),band_monomial(i,j))
checks['20_basis_forward_inverse_and_band_controls'] = True

h = {(i,j):Q((-1)**(i+j)*(i+1),j+1) for i in range(4) for j in range(5)}
residual = xy_to_tz(mul({(4,0):Q(5)},source_image(h)))
for i in range(4):
    for j in range(5):
        layer = 5*i-j+4
        recovered = sum(Q((-1)**(e-layer-j)*comb(e-layer,j),5)*c
                        for (e,L),c in residual.items() if L==layer and e>=layer+j)
        assert recovered == h[i,j]
checks['explicit_binomial_left_inverse_on_20_term_residual'] = True

p = {(1,0):Q(1), (0,2):Q(1)}
q = {(0,1):Q(1,5)}
pp,qq = source_image(p),source_image(q)
expect_equal(jac(pp,qq), {(4,0):Q(1)})
expect_equal(jac(p,q), {(0,0):Q(1,5)})
checks['positive_polynomial_Keller_control'] = True
checks['wrong_Jacobian_sign_rejected'] = rejected(lambda: expect_equal(jac(pp,qq), {(4,0):Q(-1)}))
checks['wrong_factor_5_rejected'] = rejected(lambda: expect_equal(jac(pp,qq), {(4,0):Q(5)}))
bad_tail = {(a,b):c for (a,b),c in pp.items() if a >= 0}
checks['deleted_negative_tail_rejected'] = rejected(lambda: descend(bad_tail))
fake_p,fake_q = {(1,0):Q(1)},{(4,1):Q(1)}
expect_equal(jac(fake_p,fake_q),{(4,0):Q(1)})
checks['monomial_J_alone_not_descent'] = rejected(lambda: descend(fake_p))

for i,j,k,s in [(1,2,2,1),(0,3,1,0),(3,4,2,3)]:
    ell,m = 5*i-j,5*k-s
    direct = xy_to_tz(jac(source_image({(i,j):Q(1)}),source_image({(k,s):Q(1)})))
    factor = ell*s-m*j
    pred = {(ell+m+r,ell+m):Q(factor*comb(j+s-1,r)) for r in range(j+s)} if factor else {}
    expect_equal(direct,pred)
    checks['reversed_band_bracket_rejected'] = rejected(lambda: expect_equal(direct,scale(pred,-1)))
checks['three_nontrivial_compressed_bracket_controls'] = True

# Modified map X=xi*v^2, Y=xi^-2*v^-7 is a degree-three torus cover.
X,Y = {(1,2):Q(1)},{(-2,-7):Q(1)}
expect_equal(jac(X,Y),{(-2,-6):Q(-3)})
expect_equal(mul(jac(X,Y),{(4,8):Q(1)}),{(2,2):Q(-3)})
checks['modified_cover_Jacobian_and_target'] = True

counts = {}
for name,D,h,upper in [('P',75,3,15),('Q',125,5,25)]:
    raw=jets=0
    for ell in range(-D,upper+1):
        lo=max(0,-((-ell)//5))
        hi=(D+ell)//6
        r=max(0,-((-(5*ell-h))//12))
        assert hi >= lo and r < hi-lo+1
        raw += hi-lo+1
        jets += r
    counts[name]={'bands':D+upper+1,'source_coefficients':raw,'jet_rows':jets,'dimension':raw-jets}
assert counts['P']=={'bands':91,'source_coefficients':706,'jet_rows':53,'dimension':653}
assert counts['Q']=={'bands':151,'source_coefficients':1901,'jet_rows':136,'dimension':1765}
assert 15+60==75 and 25+100==125 and 5*15-60==15 and 5*25-100==25
checks['source_ranges_dimensions_and_degree_guard_indices'] = True
physical_j_row_bound = sum(199-i-max(0,5*i-36) for i in range(40))
assert physical_j_row_bound == 4572
checks['physical_J_row_bound_4572'] = True
assert all(checks.values())
print(json.dumps({'status':'PASS','checks':checks,'counts':counts,'physical_J_row_bound':physical_j_row_bound,'scope':'tiny exact map controls and scalar support counts only; no full ideal or witness'},sort_keys=True,indent=2))
