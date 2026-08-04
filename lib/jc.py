"""Core library for the (72,108) Jacobian Conjecture case campaign.

Objects: bivariate polynomials in (x,y) whose coefficients are themselves
sparse integer polynomials in a set of scalar unknowns (a0..aN, b0..bM, t...).

Representation:
  BiPoly  = dict { (i,j): Coef }          # exponent of x^i y^j -> coefficient
  Coef    = dict { Mon: int }             # sparse poly in unknowns
  Mon     = tuple of var indices, sorted, with multiplicity  (e.g. (3,3,7) = v3^2*v7)
  ()      = the constant monomial

All arithmetic is exact over Z. Everything is stdlib-only.
"""

from math import gcd
from itertools import product

# ---------------------------------------------------------------- coefficients

def cadd(c1, c2):
    r = dict(c1)
    for m, v in c2.items():
        w = r.get(m, 0) + v
        if w:
            r[m] = w
        else:
            r.pop(m, None)
    return r

def cneg(c):
    return {m: -v for m, v in c.items()}

def cscale(c, k):
    if k == 0:
        return {}
    return {m: k * v for m, v in c.items()}

def cmul(c1, c2):
    r = {}
    for m1, v1 in c1.items():
        for m2, v2 in c2.items():
            m = tuple(sorted(m1 + m2))
            w = r.get(m, 0) + v1 * v2
            if w:
                r[m] = w
            else:
                r.pop(m, None)
    return r

# ---------------------------------------------------------------- bivariate polys

def padd(p1, p2):
    r = {k: dict(v) for k, v in p1.items()}
    for k, c in p2.items():
        rc = cadd(r.get(k, {}), c)
        if rc:
            r[k] = rc
        else:
            r.pop(k, None)
    return r

def pneg(p):
    return {k: cneg(c) for k, c in p.items()}

def pmul(p1, p2):
    r = {}
    for (i1, j1), c1 in p1.items():
        for (i2, j2), c2 in p2.items():
            k = (i1 + i2, j1 + j2)
            c = cmul(c1, c2)
            rc = cadd(r.get(k, {}), c)
            if rc:
                r[k] = rc
            else:
                r.pop(k, None)
    return r

def dx(p):
    r = {}
    for (i, j), c in p.items():
        if i > 0:
            r[(i - 1, j)] = cscale(c, i)
    return r

def dy(p):
    r = {}
    for (i, j), c in p.items():
        if j > 0:
            r[(i, j - 1)] = cscale(c, j)
    return r

def bracket(p, q):
    """[P,Q] = P_x Q_y - P_y Q_x."""
    return padd(pmul(dx(p), dy(q)), pneg(pmul(dy(p), dx(q))))

# ---------------------------------------------------------------- polygons

def ccw_order(corners):
    """Order corner list counterclockwise; assert strict convexity."""
    cx = sum(p[0] for p in corners) / len(corners)
    cy = sum(p[1] for p in corners) / len(corners)
    from math import atan2
    pts = sorted(corners, key=lambda p: atan2(p[1] - cy, p[0] - cx))
    n = len(pts)
    for k in range(n):
        ax, ay = pts[k]
        bx, by = pts[(k + 1) % n]
        cx2, cy2 = pts[(k + 2) % n]
        cross = (bx - ax) * (cy2 - ay) - (by - ay) * (cx2 - ax)
        assert cross > 0, f"corners not strictly convex/CCW at {pts[k]}->{pts[(k+1)%n]}->{pts[(k+2)%n]}"
    return pts

def lattice_points(corners):
    """All integer points in the convex hull of `corners` (inclusive)."""
    cs = sorted(set(tuple(p) for p in corners))
    if len(cs) == 1:
        return cs
    if len(cs) == 2:
        (ax, ay), (bx, by) = cs
        g = gcd(abs(bx - ax), abs(by - ay))
        return sorted((ax + k * (bx - ax) // g, ay + k * (by - ay) // g)
                      for k in range(g + 1))
    pts = ccw_order(corners)
    n = len(pts)
    xmin = min(p[0] for p in pts); xmax = max(p[0] for p in pts)
    ymin = min(p[1] for p in pts); ymax = max(p[1] for p in pts)
    out = []
    for i in range(xmin, xmax + 1):
        for j in range(ymin, ymax + 1):
            inside = True
            for k in range(n):
                ax, ay = pts[k]
                bx, by = pts[(k + 1) % n]
                if (bx - ax) * (j - ay) - (by - ay) * (i - ax) < 0:
                    inside = False
                    break
            if inside:
                out.append((i, j))
    return sorted(out)

# ---------------------------------------------------------------- Generator A

class SystemA:
    """Direct transcription of a reduced case:
    unknown P with support in hull(cornersP), unknown Q with support in
    hull(cornersQ), equations  coeffs([P,Q] - rhs) = 0, plus saturation
    t * prod(corner coefficients) = 1 forcing listed corners to be attained.

    nonvanish: 'all' -> every listed corner constrained nonzero;
               'nonorigin' -> all except (0,0) (conservative w.r.t. the
               convention that (0,0) always belongs to the Newton polygon).
    """

    def __init__(self, name, cornersP, cornersQ, rhs_monomial, nonvanish="nonorigin",
                 fix_ones=()):
        """fix_ones: iterable of ("P"|"Q", (i,j)) corner points whose coefficients
        are normalized to 1 via the torus action (x,y) -> (lx, my), m = l^-(k+1),
        (P,Q) -> (aP, Q/a).  Caller must ensure the 2x2 weight determinant
        w_P + w_Q != 0 (w = i - (k+1)j) so the normalization is lossless for
        emptiness over the algebraic closure."""
        self.name = name
        self.fix = set(fix_ones)
        self.ptsP = lattice_points(cornersP)
        self.ptsQ = lattice_points(cornersQ)
        for kind, pt in self.fix:
            cl = cornersP if kind == "P" else cornersQ
            assert tuple(pt) in {tuple(c) for c in cl}, f"fix_ones point {kind}{pt} is not a listed corner"
        self.varnames = []
        self.varof = {}
        na = 0
        for pt in self.ptsP:
            if ("P", pt) not in self.fix:
                self._newvar(f"a{na}", ("P", pt)); na += 1
        nb = 0
        for pt in self.ptsQ:
            if ("Q", pt) not in self.fix:
                self._newvar(f"b{nb}", ("Q", pt)); nb += 1
        self.tvar = self._newvar("t", ("sat", None))

        def coef(kind, pt):
            if (kind, pt) in self.fix:
                return {(): 1}
            return {(self.varof[(kind, pt)],): 1}
        P = {pt: coef("P", pt) for pt in self.ptsP}
        Q = {pt: coef("Q", pt) for pt in self.ptsQ}
        E = bracket(P, Q)
        E = padd(E, {rhs_monomial: {(): -1}})
        self.equations = [c for _, c in sorted(E.items())]

        corner_vars = []
        for pt in cornersP:
            if (nonvanish == "all" or tuple(pt) != (0, 0)) and ("P", tuple(pt)) not in self.fix:
                corner_vars.append(self.varof[("P", tuple(pt))])
        for pt in cornersQ:
            if (nonvanish == "all" or tuple(pt) != (0, 0)) and ("Q", tuple(pt)) not in self.fix:
                corner_vars.append(self.varof[("Q", tuple(pt))])
        sat = {tuple(sorted([self.tvar] + corner_vars)): 1, (): -1}
        self.equations.append(sat)
        self.corner_vars = corner_vars

    def _newvar(self, name, key):
        idx = len(self.varnames)
        self.varnames.append(name)
        self.varof[key] = idx
        return idx

    # ---------------- emission

    def _mon_str(self, mon):
        if not mon:
            return ""
        parts = []
        k = 0
        while k < len(mon):
            e = 1
            while k + e < len(mon) and mon[k + e] == mon[k]:
                e += 1
            v = self.varnames[mon[k]]
            parts.append(v if e == 1 else f"{v}^{e}")
            k += e
        return "*".join(parts)

    def _poly_str(self, c):
        terms = []
        for m in sorted(c.keys()):
            v = c[m]
            ms = self._mon_str(m)
            if ms == "":
                terms.append(f"{'+' if v > 0 else '-'}{abs(v)}")
            elif abs(v) == 1:
                terms.append(f"{'+' if v > 0 else '-'}{ms}")
            else:
                terms.append(f"{'+' if v > 0 else '-'}{abs(v)}*{ms}")
        s = "".join(terms)
        return s[1:] if s.startswith("+") else s

    def stats(self):
        nbil = sum(1 for c in self.equations if all(len(m) <= 2 for m in c))
        return (f"{self.name}: {len(self.varnames)} vars "
                f"({len(self.ptsP)} P + {len(self.ptsQ)} Q + t), "
                f"{len(self.equations)} equations ({nbil} bilinear-or-lower, "
                f"1 saturation of degree {len(self.corner_vars)+1})")

    def write_msolve(self, path, char):
        with open(path, "w") as f:
            f.write(",".join(self.varnames) + "\n")
            f.write(f"{char}\n")
            f.write(",\n".join(self._poly_str(c) for c in self.equations))
            f.write("\n")

    def write_singular(self, path, char):
        with open(path, "w") as f:
            f.write(f'ring r = {char},({",".join(self.varnames)}),dp;\n')
            f.write("ideal I = " + ",\n".join(self._poly_str(c) for c in self.equations) + ";\n")
            f.write("ideal G = groebner(I);\nG;\nquit;\n")

    # ---------------- checking

    def substitute(self, values):
        """values: dict varname->int. Returns list of evaluated equations."""
        out = []
        for c in self.equations:
            s = 0
            for m, v in c.items():
                t = v
                for idx in m:
                    t *= values[self.varnames[idx]]
                s += t
            out.append(s)
        return out
