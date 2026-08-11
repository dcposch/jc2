"""Cascade2: level-ordered elimination with unit-monomial pivots.

Differences from reduce.Cascade:
  * corner inverse variables are introduced UP FRONT (ic*c = 1), so any pivot
    of the form  q * v * (monomial in corners/inverses)  is invertible on the
    saturated locus and v can be eliminated staying polynomial;
  * elimination order follows a level function L(i,j) = rho*i + sigma*j on the
    source points, processed from the fixed corners inward (highest level
    first) — GGV's boundary-to-interior valuation order — which keeps
    substitutes short instead of densifying.

All moves preserve the corner-saturated variety over Q.
"""
from fractions import Fraction
from jc import cadd, cmul, cscale
from reduce import _subst, _kill_var

MAXTERMS = 400
MAXPASSES = 20000

class Cascade2:
    def __init__(self, system, level_dir=(2, 1)):
        S = self.S = system
        self.eqs = [dict((m, Fraction(k)) for m, k in c.items())
                    for c in S.equations[:-1]]
        self.varnames = list(S.varnames)
        self.units = set(S.corner_vars)
        self.invof = {}
        for c in sorted(S.corner_vars):
            iv = len(self.varnames)
            self.varnames.append("i" + S.varnames[c])
            self.invof[c] = iv
            self.invof[iv] = c
            self.units.add(iv)
            self.eqs.append({(min(c, iv), max(c, iv)): Fraction(1), (): Fraction(-1)})
        rho, sig = level_dir
        self.level = {}
        for (kind, pt), idx in S.varof.items():
            if kind in ("P", "Q"):
                self.level[idx] = rho * pt[0] + sig * pt[1]
        self.alive = set(range(len(self.varnames))) - {S.tvar}
        self.zeroed, self.elim = [], []
        self.status = "reduced"

    def _try_m1_m2(self):
        neweqs, force = [], set()
        for c in self.eqs:
            if not c:
                continue
            if len(c) == 1:
                (m, k), = c.items()
                if m == ():
                    self.status = "EMPTY"
                    return None
                nonunits = [v for v in set(m) if v not in self.units]
                if not nonunits:
                    self.status = "EMPTY"
                    return None
                if len(nonunits) == 1:
                    force.add(nonunits[0])
                    continue
            neweqs.append(c)
        self.eqs = neweqs
        if force:
            for v in sorted(force):
                self.eqs = [_kill_var(c, v) for c in self.eqs]
                self.zeroed.append(v)
                self.alive.discard(v)
            self.eqs = [c for c in self.eqs if c]
            return True
        return False

    def _try_m3(self):
        best = None
        for ei, c in enumerate(self.eqs):
            # variable occurrence census for this equation
            occ = {}
            for m in c:
                for v in set(m):
                    occ.setdefault(v, []).append(m)
            for v, ms in occ.items():
                if v in self.units or v not in self.level:
                    continue
                if len(ms) != 1:
                    continue
                m0 = ms[0]
                if sum(1 for i in m0 if i == v) != 1:
                    continue
                if any(i != v and i not in self.units for i in m0):
                    continue
                if len(c) - 1 > MAXTERMS:
                    continue
                key = (self.level[v], -len(c))
                if best is None or key > best[0]:
                    best = (key, ei, v, m0)
        if best is None:
            return False
        _, ei, v, m0 = best
        c = self.eqs.pop(ei)
        q = c[m0]
        rest = {m: k for m, k in c.items() if m != m0}
        # v = -(rest) * inv(u) / q  where u = m0 minus v
        invmon = tuple(sorted(self.invof[i] for i in m0 if i != v))
        g = {}
        for m, k in rest.items():
            g = cadd(g, cmul({m: -k / q}, {invmon: Fraction(1)}))
        self.eqs = [_subst(cc, v, g) for cc in self.eqs]
        self.eqs = [self._inv_reduce(cc) for cc in self.eqs]
        self.eqs = [cc for cc in self.eqs if cc]
        self.elim.append((v, g))
        self.alive.discard(v)
        return True

    def _inv_reduce(self, c):
        """cancel c * ic pairs inside monomials (they equal 1 on the locus)"""
        out = {}
        for m, k in c.items():
            mm = list(m)
            changed = True
            while changed:
                changed = False
                for i in list(mm):
                    j = self.invof.get(i)
                    if j is not None and j in mm and i in mm:
                        mm.remove(i); mm.remove(j)
                        changed = True
                        break
            out = cadd(out, {tuple(sorted(mm)): k})
        return out

    def run(self):
        for _ in range(MAXPASSES):
            r = self._try_m1_m2()
            if r is None:
                return self.status
            if r:
                continue
            if not self._try_m3():
                break
        return self.status

    def stats(self):
        pa = sum(1 for v in self.alive if v in self.level and self.S.varnames[v].startswith("a"))
        pb = sum(1 for v in self.alive if v in self.level and self.S.varnames[v].startswith("b"))
        terms = sorted(len(c) for c in self.eqs) or [0]
        return (f"core: {len(self.alive)} vars ({pa} a, {pb} b, "
                f"{len(self.alive)-pa-pb} units/inv), {len(self.eqs)} eqs; "
                f"zeroed {len(self.zeroed)}, elim {len(self.elim)}; "
                f"terms min/med/max {terms[0]}/{terms[len(terms)//2]}/{terms[-1]}")

    def write_msolve(self, path, char):
        import math
        alive_sorted = sorted(self.alive)
        names = {v: self.varnames[v] for v in alive_sorted}
        polys = []
        for c in self.eqs:
            den = 1
            for k in c.values():
                den = den * k.denominator // math.gcd(den, k.denominator)
            cc = {m: int(k * den) for m, k in c.items()}
            if char:
                assert all(val % char for val in cc.values()), "coeff vanished mod p"
            polys.append(cc)
        strs = []
        for cc in polys:
            terms = []
            for m in sorted(cc):
                k = cc[m]
                parts = []
                i = 0
                while i < len(m):
                    e = 1
                    while i + e < len(m) and m[i + e] == m[i]:
                        e += 1
                    parts.append(names[m[i]] if e == 1 else f"{names[m[i]]}^{e}")
                    i += e
                ms = "*".join(parts)
                if ms == "":
                    terms.append(f"{'+' if k>0 else '-'}{abs(k)}")
                elif abs(k) == 1:
                    terms.append(f"{'+' if k>0 else '-'}{ms}")
                else:
                    terms.append(f"{'+' if k>0 else '-'}{abs(k)}*{ms}")
            s = "".join(terms)
            strs.append(s[1:] if s.startswith("+") else s)
        with open(path, "w") as f:
            f.write(",".join(names[v] for v in alive_sorted) + "\n")
            f.write(f"{char}\n")
            f.write(",\n".join(strs) + "\n")
        return len(alive_sorted), len(strs)
