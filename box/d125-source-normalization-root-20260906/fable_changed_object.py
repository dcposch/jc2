#!/usr/bin/env python3
"""Fable5 gate: own changed-object controls for the D125 triangular normalization.
stdlib only, exact Fraction arithmetic, self-capped 25 s CPU / 512 MiB."""
from fractions import Fraction as F
from math import comb, factorial
import random, resource, sys
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
random.seed(20260906)
npass = 0
def need(ok, name):
    global npass
    if not ok:
        raise RuntimeError('FAIL ' + name)
    npass += 1
    print('PASS ' + name)
def tidy(p): return {e: c for e, c in p.items() if c}
def add(p, q):
    r = dict(p)
    for e, c in q.items(): r[e] = r.get(e, F(0)) + c
    return tidy(r)
def scale(p, c): return tidy({e: c*v for e, v in p.items()})
def mul(p, q):
    r = {}
    for (i, j), a in p.items():
        for (k, l), b in q.items():
            r[(i+k, j+l)] = r.get((i+k, j+l), F(0)) + a*b
    return tidy(r)
def d(p, ax):
    r = {}
    for e, c in p.items():
        if e[ax]:
            k = list(e); k[ax] -= 1
            r[tuple(k)] = r.get(tuple(k), F(0)) + c*e[ax]
    return tidy(r)
def jac(p, q): return add(mul(d(p,0), d(q,1)), scale(mul(d(p,1), d(q,0)), F(-1)))
def phi(p):
    r = {}
    for (i, j), c in p.items():
        for k in range(j+1):
            e = (5*i-k, j-k); r[e] = r.get(e, F(0)) + c*comb(j, k)
    return tidy(r)
def D(p, sign=1, dropY=False):
    a = mul({(-4,0): F(1,5)}, d(p,0)); b = {} if dropY else mul({(-6,0): F(sign,5)}, d(p,1))
    return add(a, b)
PHIV = {(0,1): F(1), (-1,0): F(1)}
def shift_u(p, s, r):
    out = {}
    for (i, j), c in p.items():
        for a in range(i+1):
            for b in range(i-a+1):
                e = (a, j+b); out[e] = out.get(e, F(0)) + c*comb(i,a)*comb(i-a,b)*(-s)**b*(-r)**(i-a-b)
    return tidy(out)
def shift_v(p, s):   # v -> v - s*u  (the wrong direction)
    out = {}
    for (i, j), c in p.items():
        for k in range(j+1):
            e = (i+k, j-k); out[e] = out.get(e, F(0)) + c*comb(j,k)*(-s)**k
    return tidy(out)
def expo(op, p, coef, maxn=40):
    tot, term, n = {}, dict(p), 0
    while term:
        tot = add(tot, scale(term, coef**n/factorial(n))); n += 1
        if n > maxn: return None, n
        term = op(term)
    return tot, n
W = lambda e: 5*e[0]-17*e[1]
def face(p):
    m = max(W(e) for e in p); return m, {e: c for e, c in p.items() if W(e) == m}
box = lambda Dg, U: [(i, j) for i in range(Dg+1) for j in range(Dg-i+1) if 5*i-j <= U]
PB, QB = box(75, 15), box(125, 25)
need(len(PB) == 706 and len(QB) == 1901, 'box-counts-706-1901')
need(max(i for i, j in PB) == 15 and [(i,j) for i,j in PB if i == 15] == [(15,60)], 'P-top-u-slice-forced')
need(max(i for i, j in QB) == 25 and [(i,j) for i,j in QB if i == 25] == [(25,100)], 'Q-top-u-slice-forced')
# A. random box polynomial: literal finite exponential-lift identity, both shifts and composite
s, r = F(-5, 3), F(11, 4)
R = {e: F(random.randint(-9, 9), random.randint(1, 7)) for e in random.sample(PB, 60)}
R[(15,60)] = F(2); R[(0,75)] = F(3); R[(14,61)] = F(-7); R[(14,60)] = F(5)
lhs_s = phi(shift_u(R, s, F(0)))
rhs_s, n_s = expo(lambda q: mul(PHIV, D(q)), phi(R), -s)
need(rhs_s is not None and lhs_s == rhs_s and n_s == 16, 'exp(-s*Phi(v)D)-equals-Phi(tau_s R)-finite-16-terms')
lhs_r = phi(shift_u(R, F(0), r))
rhs_r, n_r = expo(lambda q: D(q), phi(R), -r)
need(rhs_r is not None and lhs_r == rhs_r and n_r == 16, 'exp(-r*D)-equals-Phi(tau_r R)-finite-16-terms')
both = phi(shift_u(R, s, r))
comp, _ = expo(lambda q: D(q), rhs_s, -r)
need(both == comp, 'composite-shift-equals-product-of-exponentials')
bad, nb = expo(lambda q: mul(PHIV, D(q, sign=-1)), phi(R), -s)
need(bad is None or bad != lhs_s, 'wrong-lift-sign-breaks-identity')
bad2, nb2 = expo(lambda q: mul(PHIV, D(q, dropY=True)), phi(R), -s, maxn=20)
need(bad2 is None or bad2 != lhs_s, 'dropped-dY-term-breaks-identity')
# every non-identity term strictly below the top weight of its input
top = max(W(e) for e in phi(R))
t1 = mul(PHIV, D(phi(R)))
need(max(W(e) for e in t1) <= top - 18, 'one-vD-step-drops-weight-at-least-18')
need(max(W(e) for e in D(phi(R))) <= top - 13, 'one-D-step-drops-weight-at-least-13')
need(face(phi(shift_u(R, s, r))) == face(phi(R)), 'random-box-poly-full-terminal-face-preserved')
# parameter-reading invariances on the random box polynomial
sh = shift_u(R, s, F(0))
need(sh[(14,60)] == R[(14,60)], 'coefficient-(14,60)-shear-invariant')
need(sh[(14,61)] == R[(14,61)] - 15*s*R[(15,60)], 'coefficient-(14,61)-moves-by-minus-15-s-alpha')
tr = shift_u(R, F(0), r)
need(tr[(14,61)] == R[(14,61)] and tr[(14,60)] == R[(14,60)] - 15*r*R[(15,60)], 'translation-moves-(14,60)-only')
need(shift_u(R, s, r)[(15,60)] == R[(15,60)], 'alpha-invariant-under-both')
# B. changed object: wrong-direction shear v -> v - s'*u on root's chart fixture P
def band_fixture(bi, bj, power, off, mult):
    return {(bi+k+off, bj+5*(k+off)): mult*comb(power,k)*(-1)**(power-k) for k in range(power+1)}
P = add(band_fixture(1,2,1,0,F(1,5)), band_fixture(3,0,6,6,F(1,5**6)))
def chart_ok(p, Dg, U, h, pins):
    if not all(i >= 0 and j >= 0 and i+j <= Dg and 5*i-j <= U for i, j in p): return False
    im = phi(p)
    if not all(5*a-17*b <= h for a, b in im): return False
    return all(im.get(e, 0) == v for e, v in pins.items())
Ppins = {(4,1): F(1), (21,6): F(1)}
need(chart_ok(P, 75, 15, 3, Ppins), 'root-fixture-P-in-chart')
need(chart_ok(shift_u(P, s, r), 75, 15, 3, Ppins), 'u-shift-keeps-fixture-in-chart')
Pv = shift_v(P, F(1, 3))
need(not chart_ok(Pv, 75, 15, 3, Ppins) and max(5*a-17*b for a, b in phi(Pv)) > 3, 'v-direction-shear-breaks-terminal-halfspace')
need(not all(5*i-j <= 15 for i, j in Pv), 'v-direction-shear-breaks-source-weight-box')
# C. same shear parameter for Q is forced: mismatched shear gives a nonzero top bracket
def lin_pow(n, s): return {(n-k, k): F(comb(n,k))*s**k for k in range(n+1)}
Pt = mul(lin_pow(15, s), {(0,60): F(2)})
Qt = mul(lin_pow(25, s), {(0,100): F(3)})
Qt2 = mul(lin_pow(25, s+F(1,2)), {(0,100): F(3)})
need(jac(Pt, Qt) == {} and jac(Pt, Qt2) != {}, 'mismatched-total-shear-rejected-by-top-bracket')
# eigenvalues of [uv/45, u^k v^(75-k)] = (75-2k)/45, unique fixed point k=15
E = {(1,1): F(1,45)}
eig = [jac(E, {(k,75-k): F(1)}) == {(k,75-k): F(75-2*k, 45)} for k in range(16)]
need(all(eig) and [k for k in range(16) if 75-2*k == 45] == [15], 'total-Euler-eigenvalues-unique-k15')
# Q_125 bracket coefficients 75(25-k): k=25 alone survives
for k in range(26):
    b = jac({(15,60): F(1)}, {(k,125-k): F(1)})
    need(b == ({} if k == 25 else {(k+14,184-k): F(75*(25-k))}), 'Q-top-bracket-coefficient-k%d' % k) if k in (0, 13, 24, 25) else None
# vertical ODE leading multipliers 60d-15 nonzero for d>=2, and d=1 gives 45
need(all(60*dd-15 != 0 for dd in range(2, 40)) and 60-15 == 45, 'vertical-ODE-leading-multipliers')
# D. independent recounts
rect = lambda a, b, U: [(i, j) for i in range(a+1) for j in range(b+1) if 5*i-j <= U]
need(len(rect(15,60,15)) == 586 and len(rect(25,100,25)) == 1576, 'rectangle-counts-586-1576')
need(len([e for e in rect(15,60,15) if e[1] < 60 or e[0] == 15]) == 571 and len([e for e in rect(25,100,25) if e[1] < 100 or e[0] == 25]) == 1551, 'pure-top-counts-571-1551')
need(len([(I,J) for I in range(40) for J in range(160) if 5*I-J <= 36]) == 3792, 'physical-J-bound-3792')
need(len([(I,J) for I in range(199) for J in range(199-I) if 5*I-J <= 36]) == 4572, 'unnormalized-bound-4572')
# support of J for rectangle P,Q lies in the 39x159 weight-36 envelope
Pr = {e: F(random.randint(1,5)) for e in random.sample(rect(15,60,15), 40)}
Qr = {e: F(random.randint(1,5)) for e in random.sample(rect(25,100,25), 40)}
Jr = jac(Pr, Qr)
need(all(0 <= I <= 39 and 0 <= J <= 159 and 5*I-J <= 36 for I, J in Jr), 'random-rectangle-J-support-in-envelope')
print('FABLE5_NORMALIZATION_CHANGED_OBJECT_PASS %d' % npass)
