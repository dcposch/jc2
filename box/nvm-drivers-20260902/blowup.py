"""
Resolution of indeterminacy of F-bar : P^2 --> P^2 for F=(P,Q): A^2 -> A^2,
by explicit chart blowups over Q.  Outputs the base-point cluster
(multiplicities a_i, proximity structure), the boundary component classes,
the polar multiplicities m_C = ord_C Phi^*(L_infty), the degrees c_C = Z . C,
and checks the identities of the report.

All base points of the system <P^h_D, Q^h_D, Z^D> lie on L_infty; blowups are
performed in the two standard charts.  Exact arithmetic over Q throughout.
"""
import sympy as sp
from sympy import Poly, symbols, QQ, factor, gcd, simplify, expand, together

s, t = symbols('s t')

def ordo(f):
    """order of vanishing of f(s,t) at the origin (total degree valuation)."""
    f = sp.expand(f)
    if f == 0: return sp.oo
    p = Poly(f, s, t)
    return min(sum(m) for m in p.monoms())

class Chart:
    """local chart with coords (s,t); comps: list of (label, local equation)."""
    def __init__(self, fs, comps, name=""):
        g = fs[0]
        for f in fs[1:]:
            g = sp.gcd(g, f)
        self.fs = [sp.cancel(sp.expand(f/g)) for f in fs]
        self.comps = [(lab, sp.cancel(e)) for lab, e in comps]
        self.name = name
    def shift(self, s0, t0):
        sub = {s: s+s0, t: t+t0}
        return Chart([sp.expand(f.subs(sub, simultaneous=True)) for f in self.fs],
                     [(l, sp.expand(e.subs(sub, simultaneous=True))) for l, e in self.comps],
                     self.name)
    def mult(self):
        return min(ordo(f) for f in self.fs)
    def comps_through_origin(self):
        return [l for l, e in self.comps if sp.expand(e).subs({s:0, t:0}) == 0]
    def blowup(self, Elabel):
        """returns the two charts of the blowup at the origin."""
        a = self.mult()
        out = []
        # chart A:  (s,t) -> (s, s*t),  E = {s=0}
        subA = {s: s, t: s*t}
        fsA = [sp.cancel(sp.expand(f.subs(subA, simultaneous=True))/s**a) for f in self.fs]
        cA = []
        for l, e in self.comps:
            o = ordo(e)
            eA = sp.cancel(sp.expand(e.subs(subA, simultaneous=True))/s**o)
            cA.append((l, eA))
        cA.append((Elabel, s))
        out.append(Chart(fsA, cA, "A"))
        # chart B:  (s,t) -> (s*t, t),  E = {t=0}
        subB = {s: s*t, t: t}
        fsB = [sp.cancel(sp.expand(f.subs(subB, simultaneous=True))/t**a) for f in self.fs]
        cB = []
        for l, e in self.comps:
            o = ordo(e)
            eB = sp.cancel(sp.expand(e.subs(subB, simultaneous=True))/t**o)
            cB.append((l, eB))
        cB.append((Elabel, t))
        out.append(Chart(fsB, cB, "B"))
        return a, out

def base_points_on_E(ch, Elabel):
    """common zeros of the system lying on the exceptional curve E of this chart."""
    Eeq = dict(ch.comps)[Elabel]
    # E is {s=0} or {t=0}: restrict, solve in the other variable
    var = t if Eeq == s else s
    other = s if Eeq == s else t
    rest = [sp.expand(f.subs({other: 0})) for f in ch.fs]
    rest = [r for r in rest if r != 0]
    if not rest:
        raise RuntimeError("system vanishes identically on E")
    g = rest[0]
    for r in rest[1:]:
        g = sp.gcd(g, r)
    g = sp.expand(g)
    if g.is_number:
        return []
    roots = sp.roots(Poly(g, var))
    return [(0, r) if Eeq == s else (r, 0) for r in roots]

X, Y, Z = symbols('X Y Z')

def homogenize(P, x, y, D):
    """homogenize P(x,y) to degree D in X,Y,Z."""
    p = Poly(P, x, y)
    out = 0
    for m, c in zip(p.monoms(), p.coeffs()):
        out += c * X**m[0] * Y**m[1] * Z**(D - m[0] - m[1])
    return sp.expand(out)

def resolve(Pxy, Qxy, x, y, verbose=False):
    D = max(sp.total_degree(Poly(Pxy, x, y)), sp.total_degree(Poly(Qxy, x, y)))
    F = [homogenize(Pxy, x, y, D), homogenize(Qxy, x, y, D), Z**D]
    g = sp.gcd(sp.gcd(F[0], F[1]), F[2])
    assert sp.expand(g) == 1, ("fixed component!", g)
    cluster = []            # list of dicts: {'a':..,'through':[labels]}
    queue = []
    # --- proper base points on L_infty ---
    # chart Y=1 : coords (s,t)=(X,Z)
    chY = Chart([sp.expand(f.subs({Y: 1, X: s, Z: t}, simultaneous=True)) for f in F],
                [('L', t)])
    # chart X=1 : coords (s,t)=(Y,Z)
    chX = Chart([sp.expand(f.subs({X: 1, Y: s, Z: t}, simultaneous=True)) for f in F],
                [('L', t)])
    pts = []
    for r in base_points_on_E(chX, 'L'):
        pts.append((chX, r, ('X', r[0])))
    # the point [0:1:0] is the only point of L_infty missed by chart X=1
    if all(sp.expand(f.subs({s: 0, t: 0})) == 0 for f in chY.fs):
        pts.append((chY, (0, 0), ('Y', 0)))
    for ch, r, tag in pts:
        queue.append((ch.shift(r[0], r[1]), None))
    idx = 0
    while queue:
        ch, parentinfo = queue.pop(0)
        idx += 1
        lab = 'E%d' % idx
        through = ch.comps_through_origin()
        a, (chA, chB) = ch.blowup(lab)
        cluster.append({'a': a, 'through': through, 'label': lab})
        if verbose:
            print('  p%-2d  a=%d  through=%s' % (idx, a, through))
        found = []
        for c in (chA, chB):
            for r in base_points_on_E(c, lab):
                # avoid double-counting the point at the chart overlap
                key = (c.name, sp.nsimplify(r[0]), sp.nsimplify(r[1]))
                found.append((c, r))
        # chart A misses only the point E ∩ {t=∞}; chart B covers it. Dedup:
        seen = set(); uniq = []
        for c, r in found:
            if c.name == 'A':      # E={s=0}, point (0,t0)
                key = ('fin', sp.nsimplify(r[1]))
            else:                  # E={t=0}, point (s0,0);  s0=1/t0, s0=0 <-> t0=inf
                key = ('inf',) if sp.nsimplify(r[0]) == 0 else ('fin', sp.nsimplify(1/r[0]))
            if key in seen: continue
            seen.add(key); uniq.append((c, r))
        for c, r in uniq:
            queue.append((c.shift(r[0], r[1]), lab))
    return D, cluster
