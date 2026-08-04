"""Symbolic pre-reduction of Generator-A systems: the corner/edge cascade.

All moves preserve the *saturated* variety — solutions with every listed
(non-fixed) corner coefficient nonzero — over any field where the cleared
integer coefficients are nonzero (checked against the target prime).

  M1 contradiction : equation = nonzero constant            -> EMPTY
  M2 monomial      : equation = k * m, one monomial, k != 0
                     - all vars of m are units (corners)    -> EMPTY
                     - exactly one distinct non-unit v in m -> v := 0
  M3 linear elim   : v occurs in the equation only as the single
                     monomial (v,) with coefficient q != 0, v not a unit
                     -> v := -rest/q, eliminate v and the equation
                     (guarded by MAXTERMS to limit swell)

Coefficient arithmetic is exact over Q (Fractions); emission clears
denominators and verifies nothing vanishes mod the target prime.
"""
from fractions import Fraction
from jc import cadd, cneg, cmul, cscale

MAXTERMS = 80          # cap on substitute size for M3
MAXPASSES = 400

def _cpow(c, e):
    r = {(): Fraction(1)}
    for _ in range(e):
        r = cmul(r, c)
    return r

def _subst(c, v, g):
    """substitute variable index v := g (coef dict) into coef dict c"""
    out = {}
    for m, k in c.items():
        e = sum(1 for i in m if i == v)
        if e == 0:
            out = cadd(out, {m: k})
        else:
            m2 = tuple(i for i in m if i != v)
            out = cadd(out, cmul({m2: k}, _cpow(g, e)))
    return out

def _kill_var(c, v):
    """substitute v := 0"""
    return {m: k for m, k in c.items() if v not in m}

class Cascade:
    def __init__(self, system):
        """system: a jc.SystemA (already torus-normalized, nonvanish mode).
        The final saturation product equation is REPLACED here by per-corner
        inverse equations at emission time."""
        self.S = system
        # drop the t-product saturation equation (last one) — corners get
        # individual inverses at emission instead
        self.eqs = [dict((m, Fraction(k)) for m, k in c.items())
                    for c in system.equations[:-1]]
        self.units = set(system.corner_vars)
        self.tvar = system.tvar
        assert all(self.tvar not in m for c in self.eqs for m in c), "t leaked"
        self.zeroed = []
        self.elim = []           # list of (v, coefdict g) with v := g
        self.alive = set(i for i in range(len(system.varnames)) if i != self.tvar)
        self.status = "reduced"

    def _pass(self):
        changed = False
        # --- M1 / M2
        neweqs = []
        force_zero = set()
        for c in self.eqs:
            if not c:
                changed = True
                continue
            if len(c) == 1:
                (m, k), = c.items()
                if m == ():
                    self.status = "EMPTY"      # nonzero constant
                    return False
                nonunits = [v for v in set(m) if v not in self.units]
                if not nonunits:
                    self.status = "EMPTY"      # product of units = 0
                    return False
                if len(nonunits) == 1:
                    force_zero.add(nonunits[0])
                    changed = True
                    continue                    # equation consumed
            neweqs.append(c)
        self.eqs = neweqs
        if force_zero:
            for v in sorted(force_zero):
                self.eqs = [_kill_var(c, v) for c in self.eqs]
                self.zeroed.append(v)
                self.alive.discard(v)
            self.eqs = [c for c in self.eqs if c]
            return True
        # --- M3: pick the cheapest linear elimination
        best = None
        for ei, c in enumerate(self.eqs):
            for m, k in c.items():
                if len(m) == 1 and m[0] not in self.units:
                    v = m[0]
                    if any(v in m2 for m2 in c if m2 != m):
                        continue
                    if len(c) - 1 > MAXTERMS:
                        continue
                    cost = len(c)
                    if best is None or cost < best[0]:
                        best = (cost, ei, v, k)
        if best is not None:
            _, ei, v, k = best
            c = self.eqs.pop(ei)
            rest = {m: kk for m, kk in c.items() if m != (v,)}
            g = cscale(rest, Fraction(-1) / k)
            self.eqs = [_subst(cc, v, g) for cc in self.eqs]
            self.eqs = [cc for cc in self.eqs if cc]
            self.elim.append((v, g))
            self.alive.discard(v)
            return True
        return changed

    def run(self):
        for _ in range(MAXPASSES):
            if not self._pass():
                break
        return self.status

    def stats(self):
        nv = len(self.alive)
        terms = sorted(len(c) for c in self.eqs)
        return (f"core: {nv} vars, {len(self.eqs)} eqs "
                f"(zeroed {len(self.zeroed)}, eliminated {len(self.elim)}); "
                f"eq term counts: min {terms[0] if terms else 0}, "
                f"median {terms[len(terms)//2] if terms else 0}, max {terms[-1] if terms else 0}")

    # -------------- emission

    def write_msolve(self, path, char):
        S = self.S
        alive_sorted = sorted(self.alive)
        names = {v: S.varnames[v] for v in alive_sorted}
        inv = {}
        for cvar in sorted(self.units & self.alive):
            inv[cvar] = f"i{S.varnames[cvar]}"
        allnames = [names[v] for v in alive_sorted] + list(inv.values())
        polys = []
        for c in self.eqs:
            den = 1
            for k in c.values():
                den = den * k.denominator // __import__("math").gcd(den, k.denominator)
            cc = {m: int(k * den) for m, k in c.items()}
            if char:
                assert all(v % char for v in cc.values()), "coefficient vanished mod p"
            polys.append(cc)
        strs = []
        for cc in polys:
            terms = []
            for m in sorted(cc):
                k = cc[m]
                ms = "*".join(self._mon_part(m, names))
                if ms == "":
                    terms.append(f"{'+' if k>0 else '-'}{abs(k)}")
                elif abs(k) == 1:
                    terms.append(f"{'+' if k>0 else '-'}{ms}")
                else:
                    terms.append(f"{'+' if k>0 else '-'}{abs(k)}*{ms}")
            s = "".join(terms)
            strs.append(s[1:] if s.startswith("+") else s)
        for cvar, iname in inv.items():
            strs.append(f"{iname}*{S.varnames[cvar]}-1")
        with open(path, "w") as f:
            f.write(",".join(allnames) + "\n")
            f.write(f"{char}\n")
            f.write(",\n".join(strs) + "\n")
        return len(allnames), len(strs)

    @staticmethod
    def _mon_part(m, names):
        parts = []
        k = 0
        while k < len(m):
            e = 1
            while k + e < len(m) and m[k + e] == m[k]:
                e += 1
            v = names[m[k]]
            parts.append(v if e == 1 else f"{v}^{e}")
            k += e
        return parts
