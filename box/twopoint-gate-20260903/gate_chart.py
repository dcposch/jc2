#!/usr/bin/env python3
"""gate_chart.py -- independent re-derivation of the d'=2,e'=3 two-point chart
for the three k=4 rows, WITHOUT the batch's h-adic machinery: J(f,g) - c*x^k is
expanded in k[x,y] and every coefficient is an equation (the h-adic expansion is
unique, so this is the same condition).

Prime marks are labels.  x = Moh's gamma, y = pi.  Top face fixed y^{V2'}(y-x).

h-support variants:
  batch     : lower terms of h pure-y  (shape.py rule  -i + d1*j >= -d1  with d1=0)
  corrected : lower terms with  -i + d1*j >= ord h(sigma1) = V2'*d1 + u'*d2' = -1  => i<=1
beta variants:
  ab   : beta = bp*A + bq*y + br*x + bs  (A = (h - h(y=0))/y), the batch ansatz
  full : all x^i y^j with i<=2 (ord beta(sigma1) >= d'*(-1) = -2), j<K
g variants:
  forced : g = h^3 + 3*beta*h + 3/2*alpha, beta^2 = alpha*h + gamma   (batch A/B forcing)
  thm12  : g = h^3 + g1*h^2 + g2*h + g3, deg_x g_i <= i, deg_y g_i < K  (Theorem 1.2 only)
"""
import sys, os, time, subprocess, hashlib
from math import gcd
import sympy as sp

x, y, c, T = sp.symbols('x y c T')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'indep')

def build(n, m, M2, V2, k, hsup, bmode, gmode):
    K = gcd(n, m); e = n // K; d = m // K; u = K - V2
    assert (d, e, u) == (2, 3, 1)
    R = n - M2 - 1; assert R == k + 1
    params = []
    h = y**K - x*y**(K - 1)                      # y^{V2}(y-x), V2 = K-1
    if hsup == 'batch':
        mons = [(0, j) for j in range(K)]
    elif hsup == 'corrected':
        mons = [(0, j) for j in range(K)] + [(1, j) for j in range(K - 1)]
    else:
        raise ValueError(hsup)
    for (i, j) in mons:
        v = sp.Symbol('h_%d_%d' % (i, j)); params.append(v); h += v * x**i * y**j
    h = sp.expand(h)
    h0 = h.subs(y, 0)
    A = sp.expand(sp.cancel((h - h0) / y))
    if bmode == 'ab':
        bp, bq, br, bs = sp.symbols('bp bq br bs'); params += [bp, bq, br, bs]
        beta = sp.expand(bp * A + bq * y + br * x + bs)
    elif bmode == 'full':
        beta = sp.Integer(0)
        for i in range(3):
            for j in range(K):
                v = sp.Symbol('b_%d_%d' % (i, j)); params.append(v); beta += v * x**i * y**j
    else:
        raise ValueError(bmode)
    f = sp.expand(h**2 + 2 * beta)
    if gmode == 'forced':
        qd, rd = sp.div(sp.Poly(sp.expand(beta**2), y), sp.Poly(h, y), y)
        alpha = sp.expand(qd.as_expr())
        g = sp.expand(h**3 + 3 * beta * h + sp.Rational(3, 2) * alpha)
    elif gmode == 'thm12':
        g = h**3
        for deficit in (1, 2, 3):
            co = sp.Integer(0)
            for i in range(deficit + 1):
                for j in range(K):
                    v = sp.Symbol('g%d_%d_%d' % (deficit, i, j)); params.append(v); co += v * x**i * y**j
            g += co * h**(3 - deficit)
        g = sp.expand(g)
    else:
        raise ValueError(gmode)
    J = sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))
    PJ = sp.Poly(J, x, y)
    degx_J = PJ.degree(x)
    x4y0 = PJ.coeff_monomial(x**k)          # coefficient of x^k y^0 in J
    E = sp.Poly(sp.expand(J - c * x**k), x, y)
    eqs = []
    for mon, co in zip(E.monoms(), E.coeffs()):
        co = sp.expand(co)
        if co != 0:
            eqs.append((mon, co))
    info = dict(K=K, e=e, d=d, u=u, R=R, n_params=len(params), n_eqs=len(eqs),
                degx_f=sp.Poly(f, x, y).degree(x), degx_g=sp.Poly(g, x, y).degree(x),
                degx_J=degx_J, xk_y0_coeff_of_J=str(x4y0))
    return eqs, params, info

def sstr(e):
    return str(sp.expand(e)).replace('**', '^')

def write_sing(path, eqs, params, char, tag, drop_mon=None):
    names = [str(p) for p in params] + ['c', 'T']
    gens = [sstr(co) for (mon, co) in eqs if mon != drop_mon] + ['T*c-1']
    with open(path, 'w') as fh:
        fh.write('// %s\n' % tag)
        fh.write('ring R=%s,(%s),dp;\noption(redSB);\n' % (char, ','.join(names)))
        fh.write('ideal CE=c,T*c-1; ideal GE=std(CE);\n')
        fh.write('if (reduce(1,GE)==0) { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }\n')
        fh.write('ideal CN=c-1,T*c-1; ideal GN=std(CN);\n')
        fh.write('if (reduce(1,GN)!=0) { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }\n')
        fh.write('print("MAIN_START equations=%d unknowns=%d char=%s");\n' % (len(gens) - 1, len(params) + 1, char))
        fh.write('ideal I=%s;\n' % ',\n'.join(gens))
        fh.write('ideal G=std(I);\nprint("MAIN_DONE basis_size="); size(G);\n')
        fh.write('if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); } else { print("MAIN_NONTRIVIAL"); dim(G); }\nquit;\n')

def run_sing(path, timeout):
    t0 = time.time()
    try:
        r = subprocess.run(['Singular', '-q', '--no-rc', path], capture_output=True, text=True, timeout=timeout)
        out = (r.stdout or '') + (r.stderr or '')
        v = 'SATURATED-EMPTY' if 'MAIN_SATURATED_EMPTY' in out else ('SURVIVES' if 'MAIN_NONTRIVIAL' in out else 'ERROR')
    except subprocess.TimeoutExpired:
        out = ''; v = 'TIMEOUT'
    return v, round(time.time() - t0, 2), out

ROWS = [(21, 14, 15, 6, 4), (24, 16, 18, 7, 4), (27, 18, 21, 8, 4)]
VARIANTS = [
    ('R0_batch_ab_forced',        'batch',     'ab',   'forced'),
    ('R1a_corrH_ab_forced',       'corrected', 'ab',   'forced'),
    ('R1b_corrH_fullB_forced',    'corrected', 'full', 'forced'),
    ('R2_corrH_fullB_thm12',      'corrected', 'full', 'thm12'),
]

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    which = sys.argv[1:] or [v[0] for v in VARIANTS]
    rows = ROWS
    if os.environ.get('ROW'):
        rows = [ROWS[int(os.environ['ROW'])]]
    tmo = int(os.environ.get('TMO', '240'))
    for (n, m, M2, V2, k) in rows:
        for (tag, hs, bm, gm) in VARIANTS:
            if tag not in which:
                continue
            t0 = time.time()
            eqs, params, info = build(n, m, M2, V2, k, hs, bm, gm)
            stem = '%s_%d_%d_%d_%d_k%d' % (tag, n, m, M2, V2, k)
            print('== %s build %.1fs %s' % (stem, time.time() - t0, info), flush=True)
            has_minus_c = any(mon == (k, 0) and sp.expand(co + c) == 0 for (mon, co) in eqs)
            print('   x^%d y^0 equation is exactly -c: %s' % (k, has_minus_c), flush=True)
            for char in (32003, 0):
                p = os.path.join(OUT, '%s_%s.sing' % (stem, 'Q' if char == 0 else 'mod%d' % char))
                write_sing(p, eqs, params, char, stem)
                v, dt, out = run_sing(p, tmo)
                open(p + '.out', 'w').write(out)
                print('   char=%-6s %-16s %6.2fs  %s' % (char, v, dt, ' '.join(l for l in out.splitlines() if l.startswith(('CONTROL', 'MAIN_DONE', 'MAIN_SAT', 'MAIN_NON')) or l.strip().isdigit())[:160]), flush=True)
                if v == 'TIMEOUT':
                    break
            if tag.startswith('R0'):
                # diagnostic: drop the x^k y^0 equation -> do the remaining equations kill?
                p = os.path.join(OUT, '%s_dropx%dy0_Q.sing' % (stem, k))
                write_sing(p, eqs, params, 0, stem + ' minus x^k y^0 equation', drop_mon=(k, 0))
                v, dt, out = run_sing(p, tmo)
                open(p + '.out', 'w').write(out)
                print('   DIAG drop x^%d y^0 eq, char=0: %s %.2fs %s' % (k, v, dt, [l for l in out.splitlines() if l.startswith('MAIN') or l.strip().isdigit()]), flush=True)
