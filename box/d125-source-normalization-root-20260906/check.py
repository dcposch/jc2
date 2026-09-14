#!/usr/bin/env python3
"""Independent exact source-chart controls; no full Jacobian expansion."""
from fractions import Fraction as F
from math import comb
import resource
import sys

resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2,) * 2)
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))

def need(ok, name):
    if not ok:
        raise RuntimeError('CHECK_FAILED: ' + name)
    print('PASS ' + name)

def tidy(p):
    return {e: c for e, c in p.items() if c}

def plus(p, q):
    r = dict(p)
    for e, c in q.items():
        r[e] = r.get(e, F(0)) + c
    return tidy(r)

def times(p, q):
    r = {}
    for (i, j), c in p.items():
        for (a, b), d in q.items():
            e = (i+a, j+b)
            r[e] = r.get(e, F(0)) + c*d
    return tidy(r)

def scale(p, c):
    return tidy({e: c*d for e, d in p.items()})

def derivative(p, axis):
    r = {}
    for e, c in p.items():
        if e[axis]:
            k = list(e)
            k[axis] -= 1
            r[tuple(k)] = e[axis]*c
    return tidy(r)

def phi(p):
    r = {}
    for (i, j), c in p.items():
        for k in range(j+1):
            e = (5*i-k, j-k)
            r[e] = r.get(e, F(0)) + c*comb(j, k)
    return tidy(r)

def lift_du(p):
    first = times({(-4, 0): F(1, 5)}, derivative(p, 0))
    second = times({(-6, 0): F(1, 5)}, derivative(p, 1))
    if '--mutate' in sys.argv:
        second = {}  # actual omission of the necessary Y derivative
    return plus(first, second)

for i in range(4):
    for j in range(6):
        p = {(i, j): F(1)}
        need(lift_du(phi(p)) == phi(derivative(p, 0)),
             'lifted-du-source-monomial-%d-%d' % (i, j))
need(lift_du(phi({(0, 1): F(1)})) == {}, 'lifted-du-annihilates-v')

# Coefficient monomial times d_X / d_Y: weighted order relative to weight(5,-17).
weight = lambda e: 5*e[0]-17*e[1]
du_orders = [weight((-4, 0))-5, weight((-6, 0))+17]
vdu_orders = [weight((-4, 1))-5, weight((-5, 0))-5,
              weight((-6, 1))+17, weight((-7, 0))+17]
need(du_orders == [-25, -13], 'du-strict-terminal-weight-drops')
need(vdu_orders == [-42, -30, -30, -18], 'vdu-strict-terminal-weight-drops')

def band_fixture(base_i, base_j, power, offset, multiplier):
    # u^base_i v^base_j (uv^5-1)^power (uv^5)^offset
    return {(base_i+k+offset, base_j+5*(k+offset)):
            multiplier*comb(power, k)*(-1)**(power-k)
            for k in range(power+1)}

P = plus(band_fixture(1, 2, 1, 0, F(1, 5)),
         band_fixture(3, 0, 6, 6, F(1, 5**6)))
Q = plus({(1, 4): F(-1)},
         plus(band_fixture(3, 2, 5, 0, F(-3, 5**5)),
              band_fixture(5, 0, 10, 10, F(-9, 5**11))))

def transform_u(p, s, r):
    # Substitute u -> u-s*v-r; finite exact polynomial substitution.
    out = {}
    for (i, j), c in p.items():
        for a in range(i+1):
            for b in range(i-a+1):
                e = (a, j+b)
                val = c*comb(i, a)*comb(i-a, b)*(-s)**b*(-r)**(i-a-b)
                out[e] = out.get(e, F(0)) + val
    return tidy(out)

def coefficient(p, ell, t_exponent):
    order = t_exponent-ell
    return sum((c*comb(j, order) for (i, j), c in p.items()
                if 5*i-j == ell and 0 <= order <= j), F(0))

def source_constraints(p, D, U, h, pins):
    need(all(i >= 0 and j >= 0 and i+j <= D and 5*i-j <= U for i, j in p),
         'ordinary-source-bounds-%d' % D)
    bands = sorted({5*i-j for i, j in p})
    for ell in bands:
        jets = max(0, -((-(5*ell-h)) // 12))
        for order in range(jets):
            need(coefficient(p, ell, ell+order) == 0,
                 'terminal-jet-%d-%d-%d' % (D, ell, order))
    for ell, exponent, value in pins:
        need(coefficient(p, ell, exponent) == value,
             'fixed-terminal-pin-%d-%d-%d' % (D, ell, exponent))

s, r = F(2, 3), F(7, 5)
for name, p, D, U, h, pins, a, b in [
    ('P', P, 75, 15, 3, [(3, 4, F(1)), (15, 21, F(1))], 15, 60),
    ('Q', Q, 125, 25, 5, [(1, 1, F(-1)), (13, 18, F(-3)),
                         (25, 35, F(-9, 5))], 25, 100),
]:
    changed = transform_u(p, s, r)
    source_constraints(p, D, U, h, pins)
    source_constraints(changed, D, U, h, pins)
    alpha = p[a, b]
    need(changed[a, b] == alpha and alpha != 0, name+'-degree-guard-preserved')
    need(changed.get((a-1, b+1), 0)/(a*alpha) == -s,
         name+'-recover-total-shear-parameter')
    need(changed.get((a-1, b), 0)/(a*alpha) == -r,
         name+'-recover-translation-parameter')
    # These fixtures satisfy the linear source contract; NOT the Keller equations.

counts = [sum(1 for i in range(a+1) for j in range(b+1) if 5*i-j <= U)
          for a, b, U in [(15, 60, 15), (25, 100, 25)]]
need(counts == [586, 1576], 'rectangle-source-counts')
need(sum(1 for i in range(40) for j in range(160) if 5*i-j <= 36) == 3792,
     'rectangle-physical-J-row-index-bound')
print('SOURCE_NORMALIZATION_CONTROLS_PASS')
