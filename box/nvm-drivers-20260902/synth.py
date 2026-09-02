"""
Synthetic base-point clusters over L_infty: check the whole boundary ledger
without needing an actual map.  A cluster is a list of points p_1..p_r;
point i carries multiplicity a_i and a parent list (subset of {'L'} u {1..i-1},
of size 1 or 2 = proximity).  Everything else is linear algebra in
Pic = <H, E_1..E_r>.
"""
import sympy as sp
from sympy import Matrix

def analyse_cluster(D, pts, verbose=False):
    """pts = [(a_i, [parents]) ...]  parents in {'L'} u {0..i-1} (0-indexed)."""
    r = len(pts)
    a = [p[0] for p in pts]
    par = [p[1] for p in pts]
    G = sp.diag(1, *([-1]*r))
    def vec(h, es):
        v = [h] + [0]*r
        for j, c in es: v[j] = c
        return Matrix(v)
    comps = [('L', vec(1, [(i+1, -1) for i in range(r) if 'L' in par[i]]))]
    for j in range(r):
        comps.append(('E%d' % (j+1),
                      vec(0, [(j+1, 1)] + [(i+1, -1) for i in range(r) if j in par[i]])))
    Zc = vec(D, [(i+1, -a[i]) for i in range(r)])
    def dot(u, v): return (u.T*G*v)[0, 0]
    N = dot(Zc, Zc)
    m = Matrix.hstack(*[c for _, c in comps]).solve(Zc)
    cv = [dot(Zc, c) for _, c in comps]
    sat = sum(a[i] for i in range(r) if len(par[i]) == 2)
    onto = [(i, m[i], cv[i]) for i in range(len(comps)) if m[i] > 0 and cv[i] > 0]
    dic  = [(i, cv[i]) for i in range(len(comps)) if m[i] == 0 and cv[i] > 0]
    kappa = sum(c for _, _, c in onto); Lam = sum(c for _, c in dic)
    # proximity inequalities  a_i >= sum_{j proximate to i} a_j   (Z . strict transform >= 0)
    prox_ok = all(cv[i] >= 0 for i in range(len(comps)))
    res = dict(D=D, N=N, r=r, suma=sum(a), suma2=sum(v*v for v in a),
               kappa=kappa, Lam=Lam, sat=sat, m=list(m), c=cv,
               ndic=len(dic), dic=[c for _, c in dic],
               ok_mnonneg=all(v >= 0 for v in m),
               ok_I1=(m[0] == D),
               ok_I2=(N == sum(mm*kk for _, mm, kk in onto)),
               ok_BND=(kappa + Lam + sat == D),
               ok_Z2=(N == D*D - sum(v*v for v in a)),
               ok_prox=prox_ok)
    res['ok'] = all(res[k] for k in res if k.startswith('ok_'))
    if verbose:
        for i, (l, _) in enumerate(comps):
            kind = ('dicritical' if m[i] == 0 and cv[i] > 0 else
                    'contracted' if cv[i] == 0 else '->L_inf k=%d' % cv[i])
            print("   %-5s m=%-4s c=%-3s %s" % (l, m[i], cv[i], kind))
    return res
