"""MINIMAL-KELLER-SHAPE: independent boundary-tree engine.

Resolves the base cluster at infinity of the net <z^{D-dP}P^h, z^{D-dQ}Q^h, z^D>
by explicit blow-ups in the two standard charts, over QQ, and returns the FULL
dual tree L~ of the boundary with, per component C:
    m_C  = ord_C(Phi^* L_infty)      (target polar multiplicity)
    nu_C = ord_C(sigma^* L_infty)    (source polar multiplicity / degree weight)
    c_C  = Z . C                     (excess)
    C^2, and the adjacency in L~.
Everything is exact integer / rational arithmetic on exponent dictionaries.
"""
import itertools, sys
from fractions import Fraction
import sympy as sp

x, y = sp.symbols('x y')

# ---------- germs are dicts {(i,j): coeff} in local coords (s,t) ----------
def gord(g):
    return min(i+j for (i,j) in g) if g else 10**9

def tangent_cone(g, a):
    """binary form of degree a: dict {(i,j):c} with i+j=a"""
    return {(i,j):c for (i,j),c in g.items() if i+j == a}

def chartA(g, a):
    """(s,t)=(S,S*T), divide by S^a:  s^i t^j -> S^{i+j-a} T^j"""
    out = {}
    for (i,j),c in g.items():
        k = (i+j-a, j)
        out[k] = out.get(k,0) + c
    return {k:v for k,v in out.items() if v != 0}

def chartB(g, a):
    """(s,t)=(S*T,T), divide by T^a: s^i t^j -> S^i T^{i+j-a}"""
    out = {}
    for (i,j),c in g.items():
        k = (i, i+j-a)
        out[k] = out.get(k,0) + c
    return {k:v for k,v in out.items() if v != 0}

def shiftT(g, c):
    """T -> T + c  (second variable)"""
    if c == 0: return dict(g)
    out = {}
    for (i,j),co in g.items():
        for r in range(j+1):
            k = (i, r)
            out[k] = out.get(k,0) + co*sp.binomial(j,r)*c**(j-r)
    return {k:sp.nsimplify(v) for k,v in out.items() if sp.simplify(v) != 0}

class Skip(Exception): pass

def common_roots(germs):
    """common roots in P^1 of the tangent cones of the germs of minimal order.
       returns (list of finite roots c  [direction [1:c]], bool includes [0:1])"""
    a = min(gord(g) for g in germs)
    T = sp.Symbol('T')
    polys = []
    for g in germs:
        if gord(g) != a: continue
        tc = tangent_cone(g, a)
        # binary form sum c_{ij} s^i t^j, i+j=a ; direction [1:c] <-> T=c: value sum c_{ij} c^j
        p = sum(co*T**j for (i,j),co in tc.items())
        polys.append(sp.Poly(sp.expand(p), T))
    G = polys[0]
    for p in polys[1:]:
        G = G.gcd(p)
    # root [0:1] is a common root iff every tangent cone has zero coeff on t^a
    inf_root = all(tc_coeff(g,a) == 0 for g in germs if gord(g)==a)
    finite = []
    if G.degree() > 0:
        fl = sp.factor_list(G.as_expr(), T)
        for f, e in fl[1]:
            pf = sp.Poly(f, T)
            if pf.degree() == 1:
                finite.append(sp.together(-pf.all_coeffs()[1]/pf.all_coeffs()[0]))
            elif pf.degree() > 1:
                raise Skip("irrational cluster point: %s" % f)
    return a, finite, inf_root

def tc_coeff(g, a):
    return g.get((0,a), 0)

def resolve(P, Q, maxpts=400, verbose=False):
    dP, dQ = sp.Poly(P,x,y).total_degree(), sp.Poly(Q,x,y).total_degree()
    D = max(dP,dQ)
    z = sp.Symbol('z')
    def homog(R, d):
        R = sp.Poly(R, x, y)
        return sum(c*x**i*y**j*z**(D-i-j) for (i,j),c in R.terms())
    F = [homog(P,dP), homog(Q,dQ), z**D]
    # ---- data structures
    divs = {}   # label -> dict(nu, m, self, adj set)
    divs['E0'] = dict(nu=1, m=D, self=1, adj=set(), a=None)
    cluster = [] # list of dicts: label, a, prox(list of divisor labels), level
    ctr = [0]
    # initial base points on L_infty: common roots of F_i(x,y,0)
    restr = []
    for f in F:
        r = sp.expand(f.subs(z,0))
        if r != 0: restr.append(sp.Poly(r, x, y))
    G = restr[0]
    for p in restr[1:]:
        G = G.gcd(p)
    Tv = sp.Symbol('T')
    Gu = sp.Poly(sp.expand(G.as_expr().subs({x:1,y:Tv})), Tv)
    inf_root = all(sp.Poly(r.as_expr(),x,y).coeff_monomial(y**D) == 0 for r in restr)
    starts = []
    if Gu.degree() > 0:
        for f,e in sp.factor_list(Gu.as_expr(), Tv)[1]:
            pf = sp.Poly(f, Tv)
            if pf.degree() == 1:
                c = sp.together(-pf.all_coeffs()[1]/pf.all_coeffs()[0])
                starts.append(('fin', c))
            else: raise Skip("irrational root at level 1: %s"%f)
    if inf_root: starts.append(('inf', None))
    S, Tl = sp.symbols('s t')
    queue = []
    for kind, c in starts:
        if kind=='fin':
            germs = [dict(sp.Poly(sp.expand(f.subs({x:1,y:S+c,z:Tl})), S, Tl).terms()) for f in F]
        else:
            germs = [dict(sp.Poly(sp.expand(f.subs({x:S,y:1,z:Tl})), S, Tl).terms()) for f in F]
        germs = [{k:v for k,v in g.items() if v!=0} for g in germs]
        queue.append((germs, None, 'E0'))   # (germs, div_s, div_t)
    while queue:
        if len(cluster) > maxpts: raise Skip("cluster too big")
        germs, dsl, dtl = queue.pop(0)
        a, finite, inf_root = common_roots(germs)
        ctr[0] += 1
        lab = 'E%d' % ctr[0]
        prox = [d for d in (dsl, dtl) if d is not None]
        nu = sum(divs[d]['nu'] for d in prox)
        m  = sum(divs[d]['m']  for d in prox) - a
        divs[lab] = dict(nu=nu, m=m, self=-1, adj=set(), a=a)
        for d in prox:
            divs[lab]['adj'].add(d); divs[d]['adj'].add(lab)
            divs[d]['self'] -= 1
        if len(prox)==2:
            divs[prox[0]]['adj'].discard(prox[1]); divs[prox[1]]['adj'].discard(prox[0])
        cluster.append(dict(label=lab, a=a, prox=prox))
        gA = [chartA(g,a) for g in germs]
        gB = [chartB(g,a) for g in germs]
        for c in finite:
            ng = [shiftT(g, c) for g in gA]
            queue.append((ng, lab, dtl if c==0 else None))
        if inf_root:
            queue.append((gB, dsl, lab))
    return dict(D=D, divs=divs, cluster=cluster)

def analyse(P,Q):
    R = resolve(P,Q)
    D, divs, cluster = R['D'], R['divs'], R['cluster']
    sa  = sum(cl['a'] for cl in cluster)
    sa2 = sum(cl['a']**2 for cl in cluster)
    N = D*D - sa2
    # c_C from the tree
    for lab,d in divs.items():
        d['c'] = d['m']*d['self'] + sum(divs[o]['m'] for o in d['adj'])
        d['deg'] = len(d['adj'])
    # cross-check c via proximity excess
    prox_exc = {}
    for cl in cluster:
        prox_exc[cl['label']] = cl['a'] - sum(c2['a'] for c2 in cluster if cl['label'] in c2['prox'])
    prox_exc['E0'] = D - sum(c2['a'] for c2 in cluster if 'E0' in c2['prox'])
    okc = all(divs[l]['c'] == prox_exc[l] for l in divs)
    kappa = sum(d['c'] for d in divs.values() if d['m']>0 and d['c']>0)
    Lam_dic = sum(d['c'] for d in divs.values() if d['m']==0)     # = S n
    ell = sum(1 for d in divs.values() if d['m']==0 and d['c']>0)
    xi  = sum(1 for d in divs.values() if d['m']>0 and d['c']>0)
    T   = D - Lam_dic - kappa
    Tp  = {l for l,d in divs.items() if d['m']>0}
    degT = {l: sum(1 for o in divs[l]['adj'] if o in Tp) for l in Tp}
    Lam = sum(divs[l]['m'] for l in Tp if degT[l]==1) + 2*sum(divs[l]['m'] for l in Tp if degT[l]==0)
    Psi = sum(divs[l]['m']*(degT[l]-2) for l in Tp if degT[l]>=3)
    Theta = sum(d['m']*(d['deg']-2) for d in divs.values())
    ZK1 = sa - 3*D
    ZK2 = sum(d['m']*(-2-d['self']) for d in divs.values())
    Zsq = sum(d['m']*d['c'] for d in divs.values())
    leaves = sum(1 for d in divs.values() if d['deg']==1)
    fork   = sum(d['deg']-2 for d in divs.values() if d['deg']>=3)
    nuE0   = divs['E0']['deg']
    Tclass = sum(cl['a'] for cl in cluster if len(cl['prox'])==2 and 'E0' not in cl['prox'])
    Text   = sum(cl['a'] for cl in cluster if len(cl['prox'])==2)
    return dict(D=D,N=N,sa=sa,sa2=sa2,kappa=kappa,Sn=Lam_dic,ell=ell,xi=xi,T=T,
                Lam=Lam,Psi=Psi,Theta=Theta,ZK1=ZK1,ZK2=ZK2,Zsq=Zsq,leaves=leaves,
                fork=fork,valE0=nuE0,r=len(cluster),okc=okc,Tclass=Tclass,Text=Text,
                numax=max(d['nu'] for d in divs.values()),
                mmax=max(d['m'] for d in divs.values()),
                divs=divs,cluster=cluster)
