"""SAT-MASS resolution engine.

Resolves the rational map  Fbar : P^2 --> P^2,  [x:y:z] |-> [P^h_D : Q^h_D : z^D]
attached to a dominant polynomial map F = (P,Q) : A^2 -> A^2, by explicit
two-chart blow-ups over Q.  Returns the base cluster with its FULL proximity
structure (including proximity to L_infty itself), the polar multiplicities
m_C = ord_C(Phi^* L_infty), the excesses rho_i = Z.E_i^strict, and the
path-weights nu_i.

Conventions
-----------
component id 0  = strict transform of L_infty          (E_0)
component id i  = exceptional divisor of the i-th blown-up point   (E_i)
prox[i]         = ids of the boundary components through p_i
                  ("p_i is proximate to those"), |prox[i]| in {1,2} by SNC.
a[i]            = multiplicity of the net at p_i
rho[i]          = a[i] - sum_{j -> i} a[j]   (rho[0] = D - sum_{j -> 0} a[j])
nu[i]           = # proximity paths from p_i down to L_infty ; nu[0] = 1
m[i]            = ord_{E_i}(Phi^* L_infty)   ; m[0] = D
"""
import sympy as sp
from sympy import Rational as R

U, V = sp.symbols('U V')
x, y, z = sp.symbols('x y z')


def ord0(f):
    """order of vanishing at the origin of a polynomial in U,V (oo if f==0)."""
    f = sp.expand(f)
    if f == 0:
        return sp.oo
    p = sp.Poly(f, U, V)
    return min(sum(mon) for mon in p.monoms())


def divexact(f, g):
    q, r = sp.div(sp.expand(f), sp.expand(g), U, V)
    assert sp.expand(r) == 0, ("inexact division", f, g)
    return sp.expand(q)


class Resolution:
    def __init__(self, P, Q, name="", verbose=False):
        self.name = name
        self.P, self.Q = sp.expand(P), sp.expand(Q)
        self.dP = sp.Poly(self.P, x, y).total_degree() if self.P != 0 else 0
        self.dQ = sp.Poly(self.Q, x, y).total_degree() if self.Q != 0 else 0
        self.D = max(self.dP, self.dQ)
        D = self.D
        Ph = sp.expand(z**D * self.P.subs({x: x/z, y: y/z}))
        Qh = sp.expand(z**D * self.Q.subs({x: x/z, y: y/z}))
        self.Ph, self.Qh = sp.simplify(Ph), sp.simplify(Qh)
        self.verbose = verbose
        # cluster data
        self.a = {}      # id -> multiplicity
        self.prox = {}   # id -> list of ids
        self.m = {0: D}  # polar multiplicity
        self.res = {}    # id -> reduced restriction (3 polys in V) of Phi|_E
        self.run()

    # ---------- level-1 base points on L_infty ----------
    def level1(self):
        A = sp.expand(self.Ph.subs(z, 0))
        B = sp.expand(self.Qh.subs(z, 0))
        forms = [f for f in (A, B) if f != 0]
        assert forms, "both leading forms vanish: not a common-degree map"
        g = forms[0]
        for f in forms[1:]:
            g = sp.gcd(g, f)
        g = sp.expand(g)
        if g.is_number:
            return []
        pts = []
        fl = sp.factor_list(sp.Poly(g, x, y))
        for fac, _mult in fl[1]:
            fac = fac.as_expr()
            pf = sp.Poly(fac, x, y)
            assert pf.total_degree() == 1, ("non-rational base point on L_infty", fac)
            cx = pf.coeff_monomial(x)
            cy = pf.coeff_monomial(y)
            assert pf.coeff_monomial(1) == 0
            # zero locus  cx*x + cy*y = 0  ->  [x:y] = [-cy : cx]
            pts.append((-cy, cx))
        return pts

    def run(self):
        D = self.D
        queue = []
        for (ax, ay) in self.level1():
            if ay != 0:                       # chart y = 1 : (U,V) = (x/y - ax/ay, z/y)
                x0 = sp.nsimplify(R(sp.Integer(ax), sp.Integer(ay))) if not isinstance(ax, sp.Expr) else sp.simplify(ax/ay)
                sub = {x: (U + x0), y: 1, z: V}
            else:                             # chart x = 1 : (U,V) = (y/x, z/x), point U=0
                sub = {x: 1, y: U, z: V}
            F = tuple(sp.expand(sp.together(f.subs(sub))) for f in (self.Ph, self.Qh, z**D))
            F = tuple(sp.expand(f) for f in F)
            queue.append({'F': F, 'bnd': {0: 'V'}})
        self.nid = 0
        while queue:
            nxt = []
            for pt in queue:
                nxt.extend(self.blowup(pt))
            queue = nxt
        self.finish()

    def blowup(self, pt):
        F, bnd = pt['F'], pt['bnd']
        a = min(ord0(f) for f in F)
        assert a >= 1, ("not a base point", F)
        self.nid += 1
        i = self.nid
        self.a[i] = int(a)
        self.prox[i] = sorted(bnd.keys())
        assert len(bnd) <= 2, ("non-SNC configuration", bnd)
        # ---- chart A : (u,v) = (U, U*V),  E = {U=0} ----
        FA = tuple(divexact(sp.expand(f.subs({U: U, V: U*V}, simultaneous=True)), U**a) for f in F)
        # ---- chart B : (u,v) = (U*V, V),  E = {V=0} ----
        FB = tuple(divexact(sp.expand(f.subs({U: U*V, V: V}, simultaneous=True)), V**a) for f in F)
        # polar multiplicity of E : ord_p(f_2) - a
        self.m[i] = int(ord0(F[2]) - a) if F[2] != 0 else None
        # restriction of Phi to E, in chart A coordinate V
        resA = [sp.expand(f.subs(U, 0)) for f in FA]
        self.res[i] = (resA, [sp.expand(f.subs(V, 0)) for f in FB])
        # ---- new base points on E ----
        out = []
        nz = [f for f in resA if f != 0]
        if nz:
            g = nz[0]
            for f in nz[1:]:
                g = sp.gcd(g, f)
            g = sp.expand(g)
        else:
            g = sp.Integer(0)     # E is entirely in the base locus: impossible after division
        assert g != 0, "whole exceptional divisor in the base locus"
        if not g.is_number:
            fl = sp.factor_list(sp.Poly(g, V))
            for fac, _mm in fl[1]:
                pf = sp.Poly(fac, V)
                assert pf.total_degree() == 1, ("non-rational infinitely near point", fac)
                v0 = sp.simplify(-pf.coeff_monomial(1)/pf.coeff_monomial(V))
                nb = {i: 'U'}
                if v0 == 0:
                    for cid, eq in bnd.items():
                        if eq == 'V':
                            nb[cid] = 'V'
                FF = tuple(sp.expand(f.subs(V, V + v0)) for f in FA)
                out.append({'F': FF, 'bnd': nb})
        # chart-B origin (the point of E missed by chart A)
        if all(ord0(f) >= 1 for f in FB):
            nb = {i: 'V'}
            for cid, eq in bnd.items():
                if eq == 'U':
                    nb[cid] = 'U'
            out.append({'F': FB, 'bnd': nb})
        return out

    # ---------- derived quantities ----------
    def finish(self):
        D, a, prox = self.D, self.a, self.prox
        ids = sorted(a.keys())
        self.r = len(ids)
        # proximity: children of each component id (0 included)
        self.children = {0: []}
        for i in ids:
            self.children.setdefault(i, [])
        for j in ids:
            for i in prox[j]:
                self.children[i].append(j)
        # excesses
        self.rho = {0: D - sum(a[j] for j in self.children[0])}
        for i in ids:
            self.rho[i] = a[i] - sum(a[j] for j in self.children[i])
        # path weights
        self.nu = {0: 1}
        for i in ids:
            self.nu[i] = sum(self.nu[k] for k in prox[i])
        # invariants
        self.suma = sum(a.values())
        self.suma2 = sum(v*v for v in a.values())
        self.N = D*D - self.suma2
        self.T = sum(a[i] for i in ids if len(prox[i]) == 2)
        self.Tclass = sum(a[i] for i in ids if len([k for k in prox[i] if k != 0]) == 2)
        self.Tzero = sum(a[i] for i in ids if 0 in prox[i] and len(prox[i]) == 2)
        self.ZK = self.suma - 3*D
        # classify components
        self.kind = {}
        for i in [0] + ids:
            c = self.rho[i]
            mm = self.m[i]
            if mm is None:
                mm = 0
            if mm > 0 and c == 0:
                self.kind[i] = 'contr-inf'
            elif mm > 0 and c > 0:
                self.kind[i] = 'onto-Linf'
            elif mm == 0 and c > 0:
                self.kind[i] = 'dicritical'
            else:
                self.kind[i] = 'contr-aff'
        self.kappa = sum(self.rho[i] for i in self.kind if self.kind[i] == 'onto-Linf')
        self.Lam = sum(self.rho[i] for i in self.kind if self.kind[i] == 'dicritical')
        self.checks = self.verify()

    def verify(self):
        D, N = self.D, self.N
        ids = [0] + sorted(self.a.keys())
        c = {}
        c['DEG-SPLIT   D = Lam+kap+T'] = (D == self.Lam + self.kappa + self.T)
        c['SAT-WEIGHT  D = sum nu*rho'] = (D == sum(self.nu[i]*self.rho[i] for i in ids))
        c['SAT-WEIGHT  T = sum(nu-1)rho'] = (self.T == sum((self.nu[i]-1)*self.rho[i] for i in ids))
        c['EXCESS      D-T = sum rho'] = (D - self.T == sum(self.rho[i] for i in ids))
        c['POLAR       N = sum m*rho'] = (N == sum((self.m[i] or 0)*self.rho[i] for i in ids))
        c['rho >= 0'] = all(self.rho[i] >= 0 for i in ids)
        c['proximity ineq'] = all(self.rho[i] >= 0 for i in ids)
        c['m >= 0'] = all((self.m[i] or 0) >= 0 for i in ids)
        c['N >= 1'] = (N >= 1)
        c['rho0 = 0 iff E0 contracted'] = ((self.rho[0] == 0) == (self.kind[0].startswith('contr')))
        return c

    def summary(self):
        ids = sorted(self.a.keys())
        return dict(name=self.name, D=self.D, N=self.N, degs=(self.dP, self.dQ),
                    r=self.r, kappa=self.kappa, Lam=self.Lam, T=self.T,
                    Tclass=self.Tclass, Tzero=self.Tzero,
                    suma=self.suma, suma2=self.suma2, ZK=self.ZK,
                    numax=max(self.nu[i] for i in [0]+ids),
                    ok=all(self.checks.values()))

    def table(self):
        ids = [0] + sorted(self.a.keys())
        rows = []
        for i in ids:
            rows.append((i, self.a.get(i, self.D), self.prox.get(i, []), self.rho[i],
                         self.m[i], self.nu[i], self.kind[i]))
        return rows
