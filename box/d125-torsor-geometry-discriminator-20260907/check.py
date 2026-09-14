#!/usr/bin/env python3
"""Tiny exact Laurent identities, not a full receiver or a Keller fixture."""
import json
import sys

# Exponents are (g,w,lambda2,lambda3), coefficients exact integers.
def clean(p):
    return {e: c for e, c in p.items() if c}

def add(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, 0) + c
    return clean(out)

def scale(p, c):
    return clean({e: c*v for e, v in p.items()})

def mul(p, q):
    out = {}
    for e, c in p.items():
        for f, d in q.items():
            a = tuple(x+y for x, y in zip(e, f))
            out[a] = out.get(a, 0) + c*d
    return clean(out)

def deriv(p, i):
    out = {}
    for e, c in p.items():
        if e[i]:
            f = list(e)
            f[i] -= 1
            out[tuple(f)] = c*e[i]
    return clean(out)

def mon(g=0, w=0, l2=0, l3=0, c=1):
    return {(g, w, l2, l3): c}

checks = 0
def require(condition, label):
    global checks
    checks += 1
    if not condition:
        raise ValueError(label)

mode = sys.argv[1] if len(sys.argv) > 1 else 'normal'
u = add(mon(4, 1), mon(2, l2=1), mon(3, l3=1))
v = mon(-1)
if mode == 'mutate-transition':
    u = add(mon(3, 1), mon(2, l2=1), mon(3, l3=1))
j = add(mul(deriv(u, 0), deriv(v, 1)), scale(mul(deriv(u, 1), deriv(v, 0)), -1))
require(j == mon(2), 'actual transition Jacobian must be g^2')
theta_g = mul(v, deriv(u, 0))
theta_w = mul(v, deriv(u, 1))
require(theta_g == add(mon(2, 1, c=4), mon(l2=1, c=2), mon(1, l3=1, c=3)), 'theta dg component')
require(theta_w == mon(3), 'theta dw component')
dtheta = add(deriv(theta_w, 0), scale(deriv(theta_g, 1), -1))
if mode == 'mutate-differential-sign':
    dtheta = scale(dtheta, -1)
require(dtheta == mon(2, c=-1), 'd(v du)=-du wedge dv')
require(all(e[0] >= 0 for p in (theta_g, theta_w) for e in p), 'global primitive is regular')

q = add(mon(2, l2=1), mon(3, l3=1))
def cech(p):
    return {e: c for e, c in p.items() if 1 <= e[0] <= 3}
require(cech(q) == q, 'torsor class is (0,lambda2,lambda3)')
for a in range(6):
    for b in range(6):
        require(cech(add(q, mon(-a, c=2), mon(4+b, c=-3))) == q, 'Cech coboundary invariance')

# The five Wright ring generators, checked by direct substitution.
actual = [u, mul(v, u), mul(mon(-2), u),
          add(mul(mon(-3), u), mon(-1, l2=1, c=-1)),
          add(mul(mon(-4), u), mon(-2, l2=1, c=-1), mon(-1, l3=1, c=-1))]
expected = [u, add(mon(3, 1), mon(1, l2=1), mon(2, l3=1)),
            add(mon(2, 1), mon(l2=1), mon(1, l3=1)),
            add(mon(1, 1), mon(l3=1)), mon(w=1)]
for p, q in zip(actual, expected):
    require(p == q, 'literal global generator')
    require(all(e[0] >= 0 for e in p), 'global generator has no negative g power')

# Adding the missing g class introduces the actual logarithmic pole.
pole_theta = mul(v, deriv(add(u, mon(1)), 0))
require(pole_theta.get((-1, 0, 0, 0)) == 1, 'missing class produces dg/g residue')
require((-1, 0, 0, 0) not in theta_g, 'actual torsor has no residue term')
print(json.dumps({'status': 'PASS', 'checks': checks, 'scope': 'Laurent transition and differential controls only'}, sort_keys=True))
