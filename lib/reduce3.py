"""Cascade3: b-only sparse linear elimination over Q[a, corner-inverses].

The Generator-A system is bilinear: every monomial contains at most one
a-variable and at most one b-variable, each to the first power.  Eliminating
ONLY b-variables preserves this b-linearity forever: substitutes are never
raised to powers, and the process terminates after at most #b steps.

Pivots are restricted to unit monomials (integer * product of corner vars /
inverse vars * at most one... none of b), i.e. coefficients invertible on the
corner-saturated locus, so everything stays polynomial after multiplying by
inverse variables.  M1/M2 (contradiction, monomial zero-forcing) run between
eliminations.  When no unit-pivot b remains, stop and report the mixed core.
"""
from fractions import Fraction
from jc import cadd, cmul
from reduce import _kill_var

MAXTERMS_EQ = 20000     # abort threshold on any equation size

class Cascade3:
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
        self.avars, self.bvars = set(), set()
        rho, sig = level_dir
        self.level = {}
        for (kind, pt), idx in S.varof.items():
            if kind == "P":
                self.avars.add(idx)
            elif kind == "Q":
                self.bvars.add(idx)
            if kind in ("P", "Q"):
                self.level[idx] = rho * pt[0] + sig * pt[1]
        self.alive = set(range(len(self.varnames))) - {S.tvar}
        self.zeroed, self.elim = [], []
        self.status = "reduced"
        self.log = []

    def _m1_m2(self):
        acted = False
        while True:
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
            if not force:
                return acted
            for v in sorted(force):
                self.eqs = [_kill_var(c, v) for c in self.eqs]
                self.zeroed.append(v)
                self.alive.discard(v)
                self.bvars.discard(v); self.avars.discard(v)
            self.eqs = [c for c in self.eqs if c]
            acted = True

    def _subst_linear(self, c, v, g):
        """substitute b-var v := g into c, where v occurs with exponent <= 1"""
        out = {}
        for m, k in c.items():
            if v in m:
                m2 = tuple(i for i in m if i != v)
                out = cadd(out, cmul({m2: k}, g))
            else:
                out = cadd(out, {m: k})
        return self._inv_reduce(out)

    def _inv_reduce(self, c):
        out = {}
        for m, k in c.items():
            cnt = {}
            for i in m:
                cnt[i] = cnt.get(i, 0) + 1
            for i in list(cnt):
                j = self.invof.get(i)
                if j is not None and j in cnt and j > i:
                    d = min(cnt[i], cnt[j])
                    cnt[i] -= d; cnt[j] -= d
            mm = tuple(sorted(i for i, e in cnt.items() for _ in range(e)))
            out = cadd(out, {mm: k})
        return out

    def _pick_pivot(self):
        best = None
        for ei, c in enumerate(self.eqs):
            occ = {}
            for m in c:
                for v in set(m):
                    if v in self.bvars and v not in self.units:
                        occ.setdefault(v, []).append(m)
            for v, ms in occ.items():
                if len(ms) != 1:
                    continue
                m0 = ms[0]
                if sum(1 for i in m0 if i == v) != 1:
                    continue
                if any(i != v and i not in self.units for i in m0):
                    continue          # pivot coefficient must be a unit monomial
                key = (self.level[v], -len(c))
                if best is None or key > best[0]:
                    best = (key, ei, v, m0)
        return best

    def run(self, verbose=False):
        if self._m1_m2() is None:
            return self.status
        while True:
            pick = self._pick_pivot()
            if pick is None:
                break
            _, ei, v, m0 = pick
            c = self.eqs.pop(ei)
            q = c[m0]
            invmon = tuple(sorted(self.invof[i] for i in m0 if i != v))
            g = {}
            for m, k in c.items():
                if m == m0:
                    continue
                g = cadd(g, cmul({m: -k / q}, {invmon: Fraction(1)}))
            g = self._inv_reduce(g)
            self.eqs = [self._subst_linear(cc, v, g) if any(v in m for m in cc) else cc
                        for cc in self.eqs]
            self.eqs = [cc for cc in self.eqs if cc]
            self.elim.append((v, g))
            self.alive.discard(v)
            self.bvars.discard(v)
            biggest = max((len(cc) for cc in self.eqs), default=0)
            self.log.append((self.varnames[v], len(g), biggest))
            if verbose:
                print(f"  elim {self.varnames[v]} (|g|={len(g)}), biggest eq {biggest}")
            if biggest > MAXTERMS_EQ:
                self.status = "aborted-swell"
                break
            if self._m1_m2() is None:
                return self.status
        return self.status

    def stats(self):
        terms = sorted(len(c) for c in self.eqs) or [0]
        return (f"core: {len(self.alive)} vars ({len(self.avars)} a, "
                f"{len(self.bvars)} b, {len(self.alive)-len(self.avars)-len(self.bvars)} unit/inv), "
                f"{len(self.eqs)} eqs; zeroed {len(self.zeroed)}, elim {len(self.elim)}; "
                f"terms min/med/max {terms[0]}/{terms[len(terms)//2]}/{terms[-1]}")

    write_msolve = None  # emitted via reduce2-style writer below

from reduce2 import Cascade2 as _C2
Cascade3.write_msolve = _C2.write_msolve
