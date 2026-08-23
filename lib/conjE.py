"""Conjecture E ("remainder vanishing", arXiv:2205.12792, Jac_conj5) -- exact
laptop-scale test rig for the smallest nontrivial instances.

Design: conjectureE-plan.md.  Layer 1 (formal) works in
Q[G~_j, x~_j, e_s, c~_b][tau^{+-1}, t] / (t^{mfr+1})  encoded as jc.py dicts
{(tau_exp, t_exp): Coef}.  Layer 2 substitutes the chart images
  u=0:  tau -> z*eta^n     (z = x+1 = L, eta = y^{1/m})
  u=1:  tau -> xi^m*zeta   (zeta = x+y = L, xi = x^{1/n})
into {(L_exp, frac_monomial_exp): Coef} and harvests one scalar equation per
slot.  P_k = "drop L-exponent >= k".  All arithmetic exact (int/Fraction).

OUTPUT DISCIPLINE: no polynomial data is ever printed or logged -- only
aggregate counts, statuses and timings.
"""

import os, sys, time, subprocess
from fractions import Fraction
from math import gcd, comb
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jc import cadd, cmul, cscale, padd, pmul, bracket  # exact dict arithmetic

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- poly helpers

def pscale(p, k):
    if k == 0:
        return {}
    return {kk: cscale(c, k) for kk, c in p.items()}

def pshift(p, dz, dh):
    return {(z + dz, h + dh): c for (z, h), c in p.items()}

def ptrunc(p, tmax):
    return {k: c for k, c in p.items() if k[1] <= tmax}

def ppow(p, s):
    r = {(0, 0): {(): 1}}
    for _ in range(s):
        r = pmul(r, p)
    return r

def binom_frac(A, k):
    """generalized binomial coefficient C(A,k), A rational."""
    r = Fraction(1)
    for i in range(k):
        r = r * (A - i) / (i + 1)
    return r

def eval_coef(c, vals):
    s = Fraction(0)
    for mon, v in c.items():
        t = Fraction(v)
        for idx in mon:
            t *= vals[idx]
        s += t
    return s

def canon(c):
    """Coef over Q -> content-normalized integer Coef (None if identically 0)."""
    c2 = {m: Fraction(v) for m, v in c.items() if v != 0}
    if not c2:
        return None
    den = 1
    for v in c2.values():
        den = den * v.denominator // gcd(den, v.denominator)
    ints = {m: int(v * den) for m, v in c2.items()}
    g = 0
    for v in ints.values():
        g = gcd(g, abs(v))
    ints = {m: v // g for m, v in ints.items()}
    if ints[min(ints)] < 0:
        ints = {m: -v for m, v in ints.items()}
    return ints

def xpoly_to_z(coeffs):
    """coefficient list of p(x)  ->  coefficient list of p(z-1)."""
    out = [Fraction(0)] * max(1, len(coeffs))
    for k, ck in enumerate(coeffs):
        for r in range(k + 1):
            out[r] += Fraction(ck) * comb(k, r) * (-1) ** (k - r)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out

# ---------------------------------------------------------------- instance

class Instance:
    """Discrete data (a,b,m,n,delta,i) per eqs (4.1)/(4.2) of the paper,
    cross-checked against the table in conjectureE-plan.md section 2."""

    def __init__(self, a, b, m, n, delta, i):
        assert 2 <= a < b and gcd(a, b) == 1 and 0 < m < n
        assert m % a == 0 and n % a == 0
        assert (m // a) % delta == 0 and (n // a) % delta == 0
        mn = m * (n - m)
        assert 0 <= i <= mn
        um, unm = (i % m == 0), ((i + 1) % (n - m) == 0)
        if not (um or unm):
            raise ValueError("i not in index set I")
        assert um != unm, "Lemma not_both violated"
        self.a, self.b, self.m, self.n, self.delta, self.i = a, b, m, n, delta, i
        self.u = u = 0 if um else 1
        da = delta * a
        if u == 0:
            assert (n - m) % da == 0
            self.uE = (n - m) // da
            self.uF = (i * (n - m)) // mn
        else:
            assert m % da == 0
            self.uE = m // da
            self.uF = ((i + 1) * m) // mn
        self.d = u * m + n
        assert (b * self.d) % a == 0
        self.e = b * self.d // a
        self.mfr = self.d + self.e - u - 2
        assert self.d % da == 0
        self.vE = self.d // da
        self.r = gcd(m, n)
        ai = ((i + 1) * m) // mn
        bi = ai + (i * (n - m)) // mn
        if i > Fraction(mn * (a - 1), a):
            top = (u * n - u * m + m) * (a - 1)
            assert top % a == 0
            self.vF = self.uF + top // a - 1
        else:
            q1 = Fraction(da * ((i * (n - m)) // mn), n - m)
            q2 = Fraction(da * ai, m)
            if q1 == q2 and q1.denominator == 1:
                self.vF = u * ai + bi - 1
            else:
                self.vF = u * ai + bi
        self.Bmax = tuple(bb for bb in range(1, self.mfr + 1)
                          if (self.r * (self.e - bb)) % self.d == 0)
        self.p0 = da * (self.vE - self.uE)          # leading tau-power of H
        self.N = n if u == 0 else m                 # S(tau) = Z * Hmon^N
        self.SmaxE = (m + n) // da                  # E-support cap (1/da)T_{m,n}
        self.KE = n // da
        self.ells = list(range(self.uF, self.vF + 1))
        # formal variable registry
        names = []
        self.fG, self.fX, self.fE, self.fC = {}, {}, {}, {}
        for j in range(self.vE):
            self.fG[j] = len(names); names.append(f"G{j}")
        for j in range(self.vF + 1):
            self.fX[j] = len(names); names.append(f"X{j}")
        for s in range(da - 1):
            self.fE[s] = len(names); names.append(f"E{s}")
        for bb in self.Bmax:
            self.fC[bb] = len(names); names.append(f"C{bb}")
        self.fnames = names
        self._H = None
        self._slc = None
        self._jm = None

    def sE(self, j): return max(0, j - self.uE)
    def sF(self, j): return max(0, j - self.uF)

    # ------------------------------------------------ layer 1: formal series

    def build_H(self):
        """H = h(alpha(E~) + F~) in R_1[tau, t], keys (tau_exp, t_exp)."""
        if self._H is not None:
            return self._H
        da = self.delta * self.a
        Eh = {(self.vE - self.uE, 0): {(): 1}}
        for j in range(self.vE):
            Eh[(self.sE(j), self.vE - j)] = {(self.fG[j],): 1}
        H = ppow(Eh, da)
        for s in range(da - 1):
            Es = ppow(Eh, s)
            term = {(tz, tt + self.d - s * self.vE): cmul(c, {(self.fE[s],): 1})
                    for (tz, tt), c in Es.items()}
            H = padd(H, term)
        for j in range(self.vF + 1):
            H = padd(H, {(self.sF(j), self.d - j): {(self.fX[j],): 1}})
        assert H.get((self.p0, 0)) == {(): 1}, "leading term of H is not tau^p0"
        assert all(tt > 0 for (tz, tt) in H if (tz, tt) != (self.p0, 0))
        self._H = H
        return H

    def hpow(self, A):
        """truncated generalized-binomial power H^A (A rational, p0*A integer)."""
        H = self.build_H()
        lead = A * self.p0
        assert lead.denominator == 1, "non-integer tau-exponents (beta not admissible)"
        U = {(tz - self.p0, tt): c for (tz, tt), c in H.items()
             if (tz, tt) != (self.p0, 0)}
        out = {(0, 0): {(): Fraction(1)}}
        term = {(0, 0): {(): 1}}
        for k in range(1, self.mfr + 1):
            term = ptrunc(pmul(term, U), self.mfr)
            if not term:
                break
            cf = binom_frac(A, k)
            if cf != 0:
                out = padd(out, pscale(term, cf))
        return pshift(out, int(lead), 0)

    def prepare_slices(self):
        """slc[key][mu] = {tau_exp: Coef} of [H^A]_{t^mu};
        key 0 <-> A=e/d, key beta <-> A=(e-beta)/d.  jm = formal tail depths."""
        if self._slc is not None:
            return
        slc, jm = {}, {}
        for key in (0,) + self.Bmax:
            A = Fraction(self.e - (0 if key == 0 else key), self.d)
            P = self.hpow(A)
            per = {}
            for (tz, tt), c in P.items():
                per.setdefault(tt, {})[tz] = c
            slc[key] = per
            jm[key] = {mu: max([0] + [-tz for tz in d if tz < 0])
                       for mu, d in per.items()}
        self._slc, self._jm = slc, jm

    def jmax_B(self, B, mu):
        """formal frak-j(mu) for G~_{B,e-mu} (no formal cancellation between
        the base slice and the distinct c~_beta multiples)."""
        self.prepare_slices()
        vals = [self._jm[0].get(mu, 0)]
        for bb in B:
            if bb <= mu:
                vals.append(self._jm[bb].get(mu - bb, 0))
        return max(vals)

# ---------------------------------------------------------------- layer 2

class Model:
    """Concrete chart side.  assign=None: every E/F/alpha coefficient is a
    fresh scalar unknown (sweep mode).  assign given (u=0 only): exact rational
    values; c~_beta stay symbolic (fixture mode).  Structural facts built in:
      * top piece of E is exactly S(tau^{vE-uE});
      * L^{[j-uE]+} | (E)_j^w and L^{[j-uF]+} | (F)_j^w  (w-divisibility);
      * support caps  N0(E) = (1/da)T_{m,n},  supp(F) in T_{m,n}."""

    def __init__(self, inst, assign=None):
        self.inst = inst
        self.names, self.kinds = [], []
        self.cvar = {}
        self.img = {}
        u = inst.u
        for j in range(inst.vE):
            s = inst.sE(j)
            self.img[inst.fG[j]] = self._piece('g', j, s, inst.SmaxE, inst.KE, assign)
        for j in range(inst.vF + 1):
            s = inst.sF(j)
            self.img[inst.fX[j]] = self._piece('f', j, s, inst.m + inst.n, inst.n, assign)
        for s in range(inst.delta * inst.a - 1):
            if assign is not None:
                self.img[inst.fE[s]] = {(0, 0): {(): Fraction(assign[('e', s)])}}
            else:
                v = self._newvar(f"e{s}", ('e', s))
                self.img[inst.fE[s]] = {(0, 0): {(v,): 1}}
        for bb in inst.Bmax:
            v = self._newvar(f"c{bb}", ('c', bb))
            self.cvar[bb] = v
            self.img[inst.fC[bb]] = {(0, 0): {(v,): 1}}
        self.tvar = self._newvar("t", ('t',))          # saturation variable
        self.memo = {(): {(0, 0): {(): 1}}}
        self.simg = {}
        self._supcache = {}

    def _newvar(self, name, kind):
        self.names.append(name)
        self.kinds.append(kind)
        return len(self.names) - 1

    def _piece(self, kind, j, s, Smax, K, assign):
        """chart image of the formal bundle variable (piece_j^w / S(tau)^s)."""
        inst = self.inst
        if inst.u == 0:
            cap = Smax - j - s               # z-degree cap of the quotient poly
            h0 = inst.m * j - inst.n * s     # single eta-exponent
            if assign is not None:
                zc = xpoly_to_z(assign[(kind, j)])
                for _ in range(s):           # structural divisibility by z^s
                    assert zc[0] == 0, "fixture violates w-divisibility"
                    zc = zc[1:] or [Fraction(0)]
                assert len(zc) - 1 <= cap, "fixture violates support cap"
                return {(k, h0): {(): v} for k, v in enumerate(zc) if v != 0}
            return {(k, h0): {(self._newvar(f"{kind}{j}n{k}", (kind, j, k)),): 1}
                    for k in range(cap + 1)}
        # u = 1: basis (x+y)^s x^i y^{j-s-i}, i in [max(0,j-K), j-s];
        # image of the quotient: xi^{n i - m s} (zeta - xi^n)^{j-s-i}
        out = {}
        for i in range(max(0, j - K), j - s + 1):
            if assign is not None:
                co = {(): Fraction(assign[(kind, j)].get(i, 0))}
                if not co[()]:
                    continue
            else:
                co = {(self._newvar(f"{kind}{j}n{i}", (kind, j, i)),): 1}
            pw = j - s - i
            for rr in range(pw + 1):
                key = (rr, inst.n * i - inst.m * s + inst.n * (pw - rr))
                val = cscale(co, comb(pw, rr) * (-1) ** (pw - rr))
                out[key] = cadd(out.get(key, {}), val)
        return {k: c for k, c in out.items() if c}

    # ------------------------------------------------ substitution S

    def mono_img(self, mon):
        r = self.memo.get(mon)
        if r is None:
            r = pmul(self.mono_img(mon[:-1]), self.img[mon[-1]])
            self.memo[mon] = r
        return r

    def s_coef(self, coef):
        out = {}
        for mon, v in coef.items():
            out = padd(out, pscale(self.mono_img(mon), v))
        return out

    def slice_img(self, key, mu, tz):
        """concrete image of [ [H^A]_{t^mu} ]_{tau^{tz}} (cached)."""
        k = (key, mu, tz)
        if k not in self.simg:
            c = self.inst._slc[key].get(mu, {}).get(tz)
            self.simg[k] = self.s_coef(c) if c else {}
        return self.simg[k]

    def wslot(self, B, mu, tz):
        """concrete image of [G~_{B,e-mu}]_{tau^{tz}} (c-scaled sum)."""
        out = dict(self.slice_img(0, mu, tz))
        for bb in B:
            if bb <= mu:
                s = self.slice_img(bb, mu - bb, tz)
                if s:
                    cv = {(0, 0): {(self.cvar[bb],): 1}}
                    out = padd(out, pmul(cv, s))
        return out

    def tau_support(self, B, mu):
        sup = set(self.inst._slc[0].get(mu, {}))
        for bb in B:
            if bb <= mu:
                sup |= set(self.inst._slc[bb].get(mu - bb, {}))
        return sorted(sup)

    # ------------------------------------------------ the "supported" system

    def supported_equations(self, B):
        """eq (4.6): P_k(S(G~_{B,e-mu,k})) = 0 for mu in [0,mfr], k in [1,j(mu)];
        S(G~_{B,e-mu}) = 0 for mu in [e+1,mfr].  Returns dict frozen->Coef."""
        B = tuple(sorted(B))
        if B in self._supcache:
            return self._supcache[B]
        inst = self.inst
        inst.prepare_slices()
        N = inst.N
        eqs = {}

        def emit(c):
            cc = canon(c)
            if cc is not None:
                eqs[tuple(sorted(cc.items()))] = cc

        for mu in range(inst.mfr + 1):
            jm = inst.jmax_B(B, mu)
            wimg = {j: self.wslot(B, mu, -j) for j in range(1, jm + 1)}
            for k in range(1, jm + 1):
                O = {}
                for j in range(jm + 1 - k, jm + 1):
                    w = wimg.get(j)
                    if w:
                        O = padd(O, pshift(w, jm - j, N * (jm - j)))
                for (zx, hx), c in O.items():
                    if 0 <= zx <= k - 1:
                        emit(c)
            if mu >= inst.e + 1:
                full = {}
                for tz in self.tau_support(B, mu):
                    w = self.wslot(B, mu, tz)
                    if w:
                        full = padd(full, pshift(w, tz, N * tz))
                for _, c in full.items():
                    emit(c)
        self._supcache[B] = eqs
        return eqs

    def p1_slots(self, j):
        """z^0-slots of x_j = S(x~_j)  (the object P_1 acts on)."""
        return {(zx, hx): c for (zx, hx), c in self.img[self.inst.fX[j]].items()
                if zx == 0}

    def hypothesis_system(self, B, ell):
        """Hypotheses of E only: B supported + P_1(x_j)=0 for j in [ell+1,vF].
        Nonemptiness = the instance of E has actual content."""
        inst = self.inst
        eqs = dict(self.supported_equations(B))

        def emit(c):
            cc = canon(c)
            if cc is not None:
                eqs[tuple(sorted(cc.items()))] = cc

        for j in range(ell + 1, inst.vF + 1):
            for _, c in self.p1_slots(j).items():
                emit(c)
        return [eqs[k] for k in sorted(eqs)]

    def instance_system(self, B, ell):
        """Full system: hypotheses + saturation t*P_1(x_ell) = 1.
        Returns (eqs list, note)."""
        eqs = {tuple(sorted(c.items())): c for c in self.hypothesis_system(B, ell)}

        def emit(c):
            cc = canon(c)
            if cc is not None:
                eqs[tuple(sorted(cc.items()))] = cc

        lam = {}
        hset = set()
        for (zx, hx), c in self.p1_slots(ell).items():
            hset.add(hx)
            lam = cadd(lam, c)
        assert len(hset) <= 1, "P_1(x_ell) not a single fractional-monomial slot"
        if not lam:
            return None, "P1(x_ell) identically 0 (structural)"
        emit(cadd(cmul({(self.tvar,): 1}, lam), {(): -1}))
        return [eqs[k] for k in sorted(eqs)], ""

# ---------------------------------------------------------------- emission

def mon_str(names, mon):
    if not mon:
        return ""
    parts = []
    k = 0
    while k < len(mon):
        e = 1
        while k + e < len(mon) and mon[k + e] == mon[k]:
            e += 1
        v = names[mon[k]]
        parts.append(v if e == 1 else f"{v}^{e}")
        k += e
    return "*".join(parts)

def poly_str(names, c):
    terms = []
    for m in sorted(c.keys()):
        v = c[m]
        ms = mon_str(names, m)
        if ms == "":
            terms.append(f"{'+' if v > 0 else '-'}{abs(v)}")
        elif abs(v) == 1:
            terms.append(f"{'+' if v > 0 else '-'}{ms}")
        else:
            terms.append(f"{'+' if v > 0 else '-'}{abs(v)}*{ms}")
    s = "".join(terms)
    return s[1:] if s.startswith("+") else s

def write_msolve(path, names, eqs, char):
    used = sorted({i for c in eqs for m in c for i in m})
    with open(path, "w") as f:
        f.write(",".join(names[i] for i in used) + "\n")
        f.write(f"{char}\n")
        f.write(",\n".join(poly_str(names, c) for c in eqs))
        f.write("\n")
    return len(used)

def run_msolve(mspath, outpath, timeout, threads=4):
    with open(mspath) as f:
        f.readline()
        char = int(f.readline().strip())
    t0 = time.time()
    try:
        r = subprocess.run(["msolve", "-g", "2", "-t", str(threads),
                            "-f", mspath, "-o", outpath],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           timeout=timeout)
        rc = r.returncode
    except subprocess.TimeoutExpired:
        return "timeout", time.time() - t0
    dt = time.time() - t0
    if rc != 0 or not os.path.exists(outpath):
        return "error", dt
    txt = open(outpath).read()
    if not txt.strip():
        return "error", dt
    for line in txt.splitlines():
        if line.strip() == "[1]:":
            # On characteristic-zero input, msolve 0.10.1 may return from its
            # unit-basis branch after the first machine prime and before
            # rational reconstruction.  Never promote that `[1]` to Q-emptiness.
            return ("first-prime-empty", dt) if char == 0 else ("empty", dt)
    if not any(line.strip().endswith("]:") for line in txt.splitlines()):
        return "error", dt
    # The early return is unit-specific.  A successful non-unit char-0 run
    # has continued through CRT/rational reconstruction and establishes a
    # proper Q-ideal within the ordinary trust placed in msolve.
    return "nonempty", dt

# ---------------------------------------------------------------- linear c-solve

def linsolve_c(eqs, cvars):
    """Solve the affine-linear system in the c-variables (fixture mode).
    Returns dict cvar->Fraction (free vars 0) or None if inconsistent."""
    rows = []
    for c in eqs:
        row, const = {}, Fraction(0)
        for m, v in c.items():
            if m == ():
                const += Fraction(v)
            else:
                assert len(m) == 1 and m[0] in cvars, "system not linear in c"
                row[m[0]] = row.get(m[0], Fraction(0)) + Fraction(v)
        rows.append((row, const))
    pivots = {}
    for row, const in rows:
        row = dict(row)
        for pv, (prow, pconst) in list(pivots.items()):
            if pv in row:
                f = row.pop(pv)
                for k, v in prow.items():
                    row[k] = row.get(k, Fraction(0)) - f * v
                    if row[k] == 0:
                        del row[k]
                const -= f * pconst
        if row:
            pv = min(row)
            f = row.pop(pv)
            prow = {k: v / f for k, v in row.items()}
            pivots[pv] = (prow, const / f)
        elif const != 0:
            return None
    sol = {v: Fraction(0) for v in cvars}
    for pv in sorted(pivots, reverse=True):
        prow, pconst = pivots[pv]
        sol[pv] = -pconst - sum(v * sol[k] for k, v in prow.items())
    return sol

# ---------------------------------------------------------------- gate (a)

def commutation_check(inst, fix):
    """Independent validation path: compute the fractional powers AFTER the
    chart substitution (concrete Laurent series in (z, hmon, t)) and compare
    slice-by-slice with S(formal slices).  Returns (n_checked, n_mismatch)."""
    inst.prepare_slices()
    def cpmul(p, q):
        r = {}
        for (a1, b1, c1), x in p.items():
            for (a2, b2, c2), y in q.items():
                k = (a1 + a2, b1 + b2, c1 + c2)
                v = r.get(k, Fraction(0)) + x * y
                if v:
                    r[k] = v
                elif k in r:
                    del r[k]
        return r
    SH = {}
    for (tz, tt), coef in inst.build_H().items():
        img = fix.s_coef(coef)
        for (zx, hx), c in img.items():
            assert set(c) <= {()}, "commutation_check needs a numeric fixture"
            v = Fraction(c.get((), 0))
            if v:
                k = (zx + tz, hx + inst.N * tz, tt)
                SH[k] = SH.get(k, Fraction(0)) + v
                if SH[k] == 0:
                    del SH[k]
    lead = (inst.p0, inst.N * inst.p0, 0)
    assert SH.get(lead) == 1
    U = {(a - inst.p0, b - inst.N * inst.p0, c): v
         for (a, b, c), v in SH.items() if (a, b, c) != lead}
    checked = mism = 0
    for key in (0,) + inst.Bmax:
        A = Fraction(inst.e - (0 if key == 0 else key), inst.d)
        out = {(0, 0, 0): Fraction(1)}
        term = {(0, 0, 0): Fraction(1)}
        for k in range(1, inst.mfr + 1):
            term = {kk: v for kk, v in cpmul(term, U).items() if kk[2] <= inst.mfr}
            if not term:
                break
            cf = binom_frac(A, k)
            for kk, v in term.items():
                w = out.get(kk, Fraction(0)) + cf * v
                if w:
                    out[kk] = w
                elif kk in out:
                    del out[kk]
        la = int(A * inst.p0)
        conc = {(a + la, b + inst.N * la, c): v for (a, b, c), v in out.items()}
        for mu in range(inst.mfr + 1):
            agg = {}
            for tz, coef in inst._slc[key].get(mu, {}).items():
                for (zx, hx), c in fix.s_coef(coef).items():
                    v = Fraction(c.get((), 0))
                    if v:
                        kk = (zx + tz, hx + inst.N * tz)
                        agg[kk] = agg.get(kk, Fraction(0)) + v
                        if agg[kk] == 0:
                            del agg[kk]
            conc_mu = {(a, b): v for (a, b, c), v in conc.items() if c == mu}
            checked += 1
            if agg != conc_mu:
                mism += 1
    return checked, mism

FIX_P1 = {  # E = (x+1)y^2 + x*y + x^3, alpha = z^2+1, F0 = E + 2  (x-coeff lists)
    ('g', 0): [0, 0, 0, 1], ('g', 1): [0, 1], ('e', 0): 1,
    ('f', 0): [2, 0, 0, 1], ('f', 1): [0, 1], ('f', 2): [1, 1],
}

def _honest_pair_check():
    """Verify the gate fixture is an honest commuting pair of the right shape:
    F = E^2 + E + 3, G = E^3 + E, [F,G] = 0, w-degs (4,6), tops ((x+1)y^2)^{2,3}."""
    E = {(0, 2): {(): 1}, (1, 2): {(): 1}, (1, 1): {(): 1}, (3, 0): {(): 1}}
    one = {(0, 0): {(): 1}}
    F = padd(padd(pmul(E, E), E), pscale(one, 3))
    G = padd(pmul(pmul(E, E), E), E)
    ok = bracket(F, G) == {}
    dF = max(j for (_, j) in F); dG = max(j for (_, j) in G)
    topF = sorted(k for k in F if k[1] == dF) == [(0, 4), (1, 4), (2, 4)]
    topG = sorted(k for k in G if k[1] == dG) == [(0, 6), (1, 6), (2, 6), (3, 6)]
    return ok and dF == 4 and dG == 6 and topF and topG

def run_gate(log=lambda s: None):
    """Sanity gate: on the honest commuting pair (plan section 3.6; an
    automorphism pair with [F,G]=1 cannot realize this polygon shape --
    total degrees (6,9) violate Abhyankar divisibility -- so the plan's
    commuting-pair fixture is used), verify:
      (1) B_max IS supported (the affine-linear system for the c_beta is
          consistent, as Magnus' formula guarantees), and every supported
          equation vanishes identically at the solution;
      (2) the E-conclusion HOLDS at the fixture: P_1(x_ell) = 0;
      (3) a perturbed non-pair fixture is NOT supported (negative control);
      (4) cross-path: the symbolic sweep system evaluates to 0 at the fixture.
    Returns a summary dict (aggregates only)."""
    inst = Instance(2, 3, 2, 4, 1, 4)     # primary instance P1, ell = uF = vF = 2
    ell = 2
    assert _honest_pair_check(), "gate fixture is not an honest commuting pair"
    inst.prepare_slices()
    fix = Model(inst, assign=FIX_P1)
    n_chk, n_mism = commutation_check(inst, fix)
    eqs = list(fix.supported_equations(tuple(inst.Bmax)).values())
    cvars = set(fix.cvar.values())
    sol = linsolve_c(eqs, cvars)
    supported = sol is not None
    resid = 0
    if supported:
        vals = {v: sol[v] for v in cvars}
        resid = sum(1 for c in eqs if eval_coef(c, vals) != 0)
    # E-conclusion at the fixture
    lam = {}
    for _, c in fix.p1_slots(ell).items():
        lam = cadd(lam, c)
    concl = not lam or all(v == 0 for v in lam.values())
    # negative control: F0 = E + 2 + x*y  (not a polynomial in E any more)
    pert = dict(FIX_P1); pert[('f', 1)] = [0, 2]
    fixN = Model(inst, assign=pert)
    eqsN = list(fixN.supported_equations(tuple(inst.Bmax)).values())
    solN = linsolve_c(eqsN, set(fixN.cvar.values()))
    # cross-path: symbolic system evaluated at fixture + solved c
    cross_ok = None
    if supported:
        sym = Model(inst)
        symeqs = list(sym.supported_equations(tuple(inst.Bmax)).values())
        vals = {}
        for idx, kind in enumerate(sym.kinds):
            if kind[0] in ('g', 'f') and len(kind) == 3:
                _, j, k = kind
                zc = xpoly_to_z(FIX_P1[(kind[0], j)])
                vals[idx] = zc[k] if k < len(zc) else Fraction(0)
            elif kind[0] == 'e':
                vals[idx] = Fraction(FIX_P1[('e', kind[1])])
            elif kind[0] == 'c':
                vals[idx] = sol[fix.cvar[kind[1]]]
            else:
                vals[idx] = Fraction(0)   # saturation var, unused here
        cross_ok = all(eval_coef(c, vals) == 0 for c in symeqs)
    out = {
        "n_supported_eqs": len(eqs),
        "commutation": (n_chk, n_mism),
        "Bmax_supported": supported,
        "residual_nonzero": resid,
        "conclusion_P1_zero": concl,
        "negative_control_unsupported": solN is None,
        "cross_path_ok": cross_ok,
        "gate_pass": supported and resid == 0 and concl and (solN is None)
                     and (cross_ok is True) and n_mism == 0 and n_chk > 0,
    }
    log(f"gate: eqs={out['n_supported_eqs']} commutation={n_chk}chk/{n_mism}bad "
        f"supported={supported} resid={resid} conclusion_holds={concl} "
        f"negctrl_unsupported={out['negative_control_unsupported']} "
        f"cross={cross_ok} PASS={out['gate_pass']}")
    return out

# ---------------------------------------------------------------- sweep

MODP = 65521

def all_subsets(lst):
    for sz in range(len(lst) + 1):
        yield from combinations(lst, sz)

def run_sweep(outfile=None, sysdir=None, t_modp=120, t_char0=600,
              log=lambda s: None):
    """The smallest-instance sweep: (a,b,m,n)=(2,3,2,4), delta=1, i in I,
    all ell in [uF,vF], all B subseteq B_max, two msolve lanes
    (mod 65521 plus a char-0 run).  A printed char-0-header `[1]` can be the
    unit short circuit at the first prime and is not a rational certificate;
    a successful non-unit result has completed reconstruction.  Writes
    per-instance rows."""
    outfile = outfile or os.path.join(ROOT, "runs", "conjE_results.txt")
    sysdir = sysdir or os.path.join(ROOT, "systems", "conjE")
    os.makedirs(sysdir, exist_ok=True)
    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    t_all = time.time()
    gate = run_gate(log=log)
    rows, details, records = [], [], []
    for i in range(5):
        try:
            inst = Instance(2, 3, 2, 4, 1, i)
        except ValueError:
            continue
        base = dict(a=2, b=3, m=2, n=4, delta=1, i=i, u=inst.u)
        if not inst.ells:
            records.append(dict(base, ell=None, verdict="degenerate",
                                detail="ell-range [uF,vF] empty (vF<uF): "
                                       "hypotheses of E vacuous", t=0.0))
            log(f"i={i}: degenerate (no valid ell)")
            continue
        t_inst0 = time.time()
        inst.prepare_slices()
        model = Model(inst)
        for ell in inst.ells:
            t0 = time.time()
            n_empty = n_nonempty = n_other = n_const = n_trace = 0
            n_hyp_sat = n_hyp_other = 0
            nonempty_Bs = []
            for B in all_subsets(inst.Bmax):
                btag = "x".join(map(str, B)) or "none"
                tag = f"i{i}l{ell}B{btag}"
                # ---- hypothesis lane: E's hypotheses are non-vacuous iff the
                # hypothesis system has a point.  The all-zero configuration
                # (E = top piece only, F = 0, alpha = z^{da}, c = 0) is an
                # explicit exact witness iff no equation has a constant term.
                hyp = model.hypothesis_system(B, ell)
                if all(c.get((), 0) == 0 for c in hyp):
                    hs = "nonempty(zero-config point)"
                    n_hyp_sat += 1
                else:
                    hs = "zero-config-fails"         # would need a real search
                    n_hyp_other += 1
                # ---- saturated lane: hypotheses + P_1(x_ell) != 0
                eqs, note = model.instance_system(B, ell)
                if eqs is None:
                    n_empty += 1
                    details.append(f"# {tag} hyp={hs} structural: {note} -> empty")
                    continue
                if any(set(c) == {()} for c in eqs):
                    n_empty += 1
                    n_const += 1
                    details.append(f"# {tag} hyp={hs} eqs={len(eqs)} "
                                   f"const-contradiction -> empty (exact)")
                    continue
                fp = os.path.join(sysdir, tag + f".p{MODP}.ms")
                f0 = os.path.join(sysdir, tag + ".q.ms")
                nv = write_msolve(fp, model.names, eqs, MODP)
                write_msolve(f0, model.names, eqs, 0)
                s1, dt1 = run_msolve(fp, fp[:-3] + ".out", t_modp)
                s2, dt2 = run_msolve(f0, f0[:-3] + ".out", t_char0)
                details.append(f"# {tag} vars={nv} eqs={len(eqs)} hyp={hs} "
                               f"modp={s1}({dt1:.1f}s) char0={s2}({dt2:.1f}s)")
                if s2 == "empty":
                    n_empty += 1
                elif s2 == "first-prime-empty":
                    n_trace += 1
                elif s2 == "nonempty":
                    n_nonempty += 1
                    nonempty_Bs.append(B)
                else:
                    n_other += 1
                if s1 == "nonempty" and s2 == "first-prime-empty":
                    details.append(f"# {tag} WARNING modular-lane disagreement "
                                   f"(fixed prime nonempty, first prime empty)")
            nB = 2 ** len(inst.Bmax)
            if n_nonempty > 0:
                verdict = "NONEMPTY-NEEDS-WITNESS-ANALYSIS"
            elif n_other > 0 or n_hyp_other > 0:
                verdict = "undecided"
            elif n_hyp_sat == 0:
                verdict = "degenerate"      # hypotheses of E empty for every B
            elif n_empty == nB:
                verdict = "holds"           # exact structural contradictions only
            elif n_empty + n_trace == nB:
                verdict = "modular-trace-support"
            else:
                verdict = "undecided"
            dt = time.time() - t0
            records.append(dict(base, ell=ell, verdict=verdict,
                                detail=f"B-subsets {nB}: exact-empty={n_empty} "
                                       f"(const={n_const}) first-prime-empty={n_trace} "
                                       f"nonempty={n_nonempty} "
                                       f"other={n_other}; hyp-lane satisfiable={n_hyp_sat}"
                                       + (f" nonempty_B={nonempty_Bs}" if nonempty_Bs else ""),
                                t=dt))
            log(f"i={i} ell={ell}: {verdict} (exact {n_empty}/{nB}, "
                f"first-prime trace {n_trace}/{nB}, "
                f"hyp {n_hyp_sat}/{nB} satisfiable, {dt:.1f}s)")
        log(f"i={i}: done in {time.time()-t_inst0:.1f}s")
    # ------------- write results file
    with open(outfile, "w") as f:
        f.write("# Conjecture E (arXiv:2205.12792 Jac_conj5) smallest-instance sweep\n")
        f.write(f"# quadruple (a,b,m,n)=(2,3,2,4) delta=1; ts={int(time.time())}\n")
        f.write("# gate(a): honest commuting pair F=E^2+E+3, G=E^3+E, "
                "E=(x+1)y^2+xy+x^3 (plan sec 3.6; automorphism pairs with [F,G]=1 "
                "cannot realize this polygon shape: total degrees (6,9) violate "
                "Abhyankar divisibility)\n")
        f.write(f"# gate result: {gate}\n")
        f.write("# semantics: an instance row 'holds' = (i) for EVERY B subseteq "
                "B_max, {B supported} & {P_1(x_j)=0, j>ell} & {P_1(x_ell)!=0} is "
                "EMPTY by an exact characteristic-zero certificate, i.e. E holds in the "
                "strong form (proper-subset escape never needed) on the capped "
                "stratum N0(E)=(1/da)T_{m,n}, supp(F) in T_{m,n} (exactly what "
                "the E=>D induction instantiates; see plan honesty note); AND "
                "(ii) the hypotheses are non-vacuous: the hypothesis system "
                "{B supported}&{P_1(x_j)=0, j>ell} has an explicit exact point "
                "(the zero configuration E=top, F=0, alpha=z^da, c=0; for i=4 "
                "also the nontrivial honest-pair gate fixture), so E's "
                "implication has content and the verified conclusion is that "
                "P_1(x_ell)=0 on the WHOLE hypothesis variety.\n")
        f.write("# 'modular-trace-support' means the fixed-prime and char-0-header "
                "msolve -g lanes printed modular [1] bases; it is evidence only, "
                "not a Q certificate or a HOLD verdict.\n")
        f.write("# 'degenerate' = hypotheses of E vacuous (no valid (F,G,w)/ell "
                "configuration, or hypothesis system empty for every B), NOT a "
                "verification.\n")
        f.write("# columns: a b m n delta i u ell verdict time_s detail\n")
        for r in records:
            f.write(f"{r['a']} {r['b']} {r['m']} {r['n']} {r['delta']} {r['i']} "
                    f"{r['u']} {r['ell'] if r['ell'] is not None else '-'} "
                    f"{r['verdict']} {r['t']:.1f} :: {r['detail']}\n")
        f.write("# --- per-system detail ---\n")
        for d in details:
            f.write(d + "\n")
        f.write(f"# total wall time {time.time()-t_all:.1f}s\n")
    return gate, records

if __name__ == "__main__":
    def _log(s):
        print(s, flush=True)
    gate, records = run_sweep(log=_log)
    n_h = sum(1 for r in records if r["verdict"] == "holds")
    n_d = sum(1 for r in records if r["verdict"] == "degenerate")
    n_bad = len(records) - n_h - n_d
    _log(f"SWEEP DONE: {len(records)} instances: holds={n_h} degenerate={n_d} "
         f"other={n_bad}; gate_pass={gate['gate_pass']}")
