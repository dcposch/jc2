"""Boundary class bookkeeping and the identity checks."""
import sympy as sp
from sympy import symbols, Rational, Matrix
import sys
sys.path.insert(0,'/tmp/nvm')
from blowup import resolve
x, y = symbols('x y')

def analyse(name, P, Q, verbose=False):
    D, cl = resolve(P, Q, x, y)
    r = len(cl)
    a = [c['a'] for c in cl]
    lab = [c['label'] for c in cl]
    thr = [c['through'] for c in cl]
    # class vectors in basis (H, E_1..E_r)
    def vec(h, es):
        v = [h] + [0]*r
        for j, c in es: v[j] = c
        return Matrix(v)
    idx = {l: i+1 for i, l in enumerate(lab)}
    comps = []   # (label, class-vector)
    # E_0 = strict transform of L_infty
    comps.append(('L', vec(1, [(i+1, -1) for i in range(r) if 'L' in thr[i]])))
    for j in range(r):
        comps.append((lab[j], vec(0, [(j+1, 1)] +
                     [(i+1, -1) for i in range(r) if lab[j] in thr[i]])))
    Zc = vec(D, [(i+1, -a[i]) for i in range(r)])
    # intersection form:  H^2=1, E_i^2=-1, all others 0
    G = sp.diag(1, *([-1]*r))
    def dot(u, v): return (u.T*G*v)[0,0]
    N = dot(Zc, Zc)
    # solve Z = sum m_C C
    Mx = Matrix.hstack(*[c for _, c in comps])
    m = Mx.solve(Zc)
    cvals = [dot(Zc, c) for _, c in comps]
    prox = [len(thr[i]) for i in range(r)]
    sat = sum(a[i] for i in range(r) if prox[i] == 2)
    # classification
    onto = [(comps[i][0], m[i], cvals[i]) for i in range(len(comps)) if m[i] > 0 and cvals[i] > 0]
    dic  = [(comps[i][0], cvals[i]) for i in range(len(comps)) if m[i] == 0 and cvals[i] > 0]
    contr= [comps[i][0] for i in range(len(comps)) if cvals[i] == 0]
    kappa = sum(c for _, _, c in onto)
    lam   = sum(c for _, c in dic)
    checks = {
        "I1 m_{E0} = D":           (m[0] == D),
        "N = D^2-sum a^2":         (N == D*D - sum(v*v for v in a)),
        "I2 N = sum_onto m_C k_C": (N == sum(mm*kk for _, mm, kk in onto)),
        "BND sum_C c_C + sat = D": (kappa + lam + sat == D),
        "m_C >= 0":                all(v >= 0 for v in m),
        "dicritical has m=0":      all(c > 0 for _, c in dic),
        "c_C >= 0 everywhere":     all(c >= 0 for c in cvals),
    }
    print("%-16s D=%2d N=%2d r=%2d | kappa=%2d  sum_l s_l*n_c=%2d  sat=%2d | %s"
          % (name, D, N, r, kappa, lam, sat,
             "OK" if all(checks.values()) else "FAIL "+str([k for k,v in checks.items() if not v])))
    if verbose:
        for i,(l,_) in enumerate(comps):
            kind = 'dicritical' if m[i]==0 else ('->L_inf k=%d'%cvals[i] if cvals[i]>0 else 'contracted')
            print("      %-4s m=%-3d c=%-3d  %s" % (l, m[i], cvals[i], kind))
    return dict(D=D, N=N, r=r, kappa=kappa, lam=lam, sat=sat, ok=all(checks.values()))

if __name__ == "__main__":
    tests = [
        ("(x, xy)",      x,       x*y),
        ("(x, y^2)",     x,       y**2),
        ("(x, xy^2)",    x,       x*y**2),
        ("(x, xy^3)",    x,       x*y**3),
        ("(x, y+x^2)",   x,       y+x**2),
        ("(x, y+x^3)",   x,       y+x**3),
        ("(x, y+x^4)",   x,       y+x**4),
        ("(x, x^2 y)",   x,       x**2*y),
        ("(x, x^3 y)",   x,       x**3*y),
        ("(x, x^2 y^2)", x,       x**2*y**2),
        ("(x+y^2, y)",   x+y**2,  y),
        ("(x, x y + y^2)", x,     x*y+y**2),
        ("(x^2, y)",     x**2,    y),
        ("(x^2 y, y)",   x**2*y,  y),
        ("(x, x^2 y^3)", x,       x**2*y**3),
    ]
    for n, P, Q in tests:
        analyse(n, P, Q)
