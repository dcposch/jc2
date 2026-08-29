#!/usr/bin/env python3
"""M>=2 equal-arrival merge families: exact semilinear quotient + T1 reduction.

Scope (read-only mathematics over the promoted record):
  * BOOK-OFFAXIS.md R1.0 / R2.1 / R2.2 / §10 P0-P2 (merge shape, handshakes,
    searrow (S), northeast (NE), root-mult (R), lambda price);
  * SHEET6-DEPTH.md §1 (i-normalized w), §5c (case-III 0-edge handshake);
  * SHEET6-MULTIPOLE.md MP1/MP2 and D9 (the td=6 negative control);
  * the generalized zero-chain law's normal form (xmodel/sol-td7-law.md eq (3)),
    which this module *derives as a special case* of a general merge identity.

Everything is exact (int / Fraction / symbolic Poly).  No floats, no search
caps, no engine import.  Nothing here asserts realizability, landing, a
ceiling, Keller or JC2.

Conventions (i-normalized, `SHEET6-DEPTH.md` §1):
    rho  = D/deg(p),  kbar = kappa*(1-pi),  w = (kbar - rho)/nu.
At a merge G with reduced pattern

    p = (-) eta^eps * prod_e (eta^nu - c_e^nu)^{mu_e}
                    * prod_j (eta^nu - d_j^nu)^{m_j}
    q = (-) eta * (each distinct nonzero p-orbit once) * (lex extra orbits)

    dp = eps + nu*P,  P = sum mu_e + sum m_j
    dq = 1 + nu*s,    s  = r0 + k + lex
    M  = gcd(dp, dq)

Every arriving edge carries an *effective invariant*

    what_e = w_e                    (case I/II, nonzero direction)
    what_0 = nu_H * w_H             (case III, 0-direction; DEPTH 5c / R2.1)

and a uniform transport law  kbar * E_e = mu_e * what_e * dq,
E_e = mu_e*dq - dp > 0.
"""
from fractions import Fraction as Fr
from math import gcd
import hashlib
import json

from polyexact import Poly

MODULE_TAG = "M2_EQUAL_JOIN_SEMILINEAR_OPUS5_20260829"


# --------------------------------------------------------------------------
# 0. small exact helpers
# --------------------------------------------------------------------------

def lcm(a, b):
    return a // gcd(a, b) * b


def prime_factors(n):
    """Sorted distinct primes of n >= 1 (trial division; exact, no cap:
    the loop bound is sqrt(n), which is a proof-complete bound, not a cap)."""
    n = abs(int(n))
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        out.append(n)
    return out


def radical(n):
    r = 1
    for p in prime_factors(n):
        r *= p
    return r


def vp(n, p):
    n = abs(int(n))
    if n == 0:
        raise ValueError("vp(0)")
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k


def ceil_div(a, b):
    """ceil(a/b) for exact rationals/ints, b > 0."""
    q = Fr(a, 1) / Fr(b, 1) if not isinstance(a, Fr) else Fr(a) / b
    n, d = q.numerator, q.denominator
    return -((-n) // d)


def ceil_fr(x):
    x = Fr(x)
    return -((-x.numerator) // x.denominator)


# --------------------------------------------------------------------------
# 1. merge-local exact arithmetic  (any multiplicities, any 0-regime)
# --------------------------------------------------------------------------

class MergeLocalError(ValueError):
    pass


def merge_local(r0, mus, ms, lex, eps, whats, nu, zero_arrival=False):
    """Exact merge-local record.

    r0            number of NONZERO arriving orbits
    mus           list of r0 arrival multiplicities (positive ints)
    ms            list of k non-chain ("extra present") multiplicities
    lex           number of q-only extra orbits (>= 0)
    eps           0-root multiplicity; 0 = no 0-root
    whats         list of r0 effective invariants of the nonzero edges
                  (Fractions > 0); if zero_arrival, `what0` is appended last
    nu            merge pattern index nu_G (>= 1)
    zero_arrival  True  <=> a chain arrives at the 0-direction (case III),
                  which forces eps = mu_0 = the 0-arrival multiplicity.

    Returns a dict of exact values, or raises MergeLocalError on an illegal
    configuration (the recorded laws (S)/(NE)/(R) are enforced, never guessed).
    """
    mus = [int(x) for x in mus]
    ms = [int(x) for x in ms]
    k = len(ms)
    s = r0 + k + lex
    P = sum(mus) + sum(ms)
    dp = eps + nu * P
    dq = 1 + nu * s
    M = gcd(dp, dq)
    T = P - s * eps

    if r0 + (1 if zero_arrival else 0) < 1:
        raise MergeLocalError("no arriving edge")
    if any(x <= 0 for x in mus) or any(x <= 0 for x in ms):
        raise MergeLocalError("nonpositive multiplicity")
    if eps < 0:
        raise MergeLocalError("negative eps")
    if nu < 1:
        raise MergeLocalError("nu < 1")

    # law (R): dp != mu_star * dq for every multiplicity occurring in p
    occurring = set(mus) | set(ms) | ({eps} if eps >= 1 else set())
    for mstar in occurring:
        if dp == mstar * dq:
            raise MergeLocalError("root-mult law (R) violated at mult %d" % mstar)
    if T == 0:
        raise MergeLocalError("T = P - s*eps = 0 (equivalent to (R) at eps)")

    # law (S): searrow for every arriving edge; law (NE) for every other orbit
    edges = []  # (label, mu_e, what_e)
    for i, (mu_e, wh) in enumerate(zip(mus, whats[:r0])):
        edges.append(("nz%d" % i, mu_e, Fr(wh)))
    if zero_arrival:
        if eps <= 0:
            raise MergeLocalError("case III needs eps = mu_0 >= 1")
        edges.append(("zero", eps, Fr(whats[r0])))
    for lab, mu_e, wh in edges:
        if mu_e * dq <= dp:
            raise MergeLocalError("searrow (S) fails on edge %s" % lab)
        if wh <= 0:
            raise MergeLocalError("nonpositive effective invariant on %s" % lab)
    for m_j in ms:
        if m_j * dq >= dp:
            raise MergeLocalError("northeast (NE) fails on a non-chain orbit")
    if eps >= 1 and not zero_arrival:
        if eps * dq >= dp:
            raise MergeLocalError("northeast (NE) fails on the free 0-root")

    # uniform transport, per edge; consistency is R2.1
    kbars = []
    for lab, mu_e, wh in edges:
        E_e = mu_e * dq - dp
        kbars.append((lab, Fr(mu_e) * wh * dq / E_e, E_e, mu_e, wh))
    kbar = kbars[0][1]
    for lab, kb, _, _, _ in kbars[1:]:
        if kb != kbar:
            raise MergeLocalError("R2.1 inconsistency between edges (%s)" % lab)

    rho = kbar / dq
    X = kbar * Fr(dp, dq)
    w_child = (kbar - rho) / nu

    # lambda price (BOOK-OFFAXIS P0/P2 rule); arriving edges + q-extras cost 0
    lam = 0
    for m_j in ms:
        lam += max(1, ceil_fr(X / m_j - kbar))
    if eps >= 1 and not zero_arrival:
        lam += max(1, ceil_fr((X / eps - kbar) / nu))

    Cs = {lab: mu_e * s - P for lab, _, _, mu_e, _ in kbars}
    return {
        "r0": r0, "mus": mus, "ms": ms, "k": k, "lex": lex, "eps": eps,
        "nu": nu, "zero_arrival": zero_arrival,
        "P": P, "s": s, "dp": dp, "dq": dq, "M": M, "T": T,
        "kbar": kbar, "rho": rho, "X": X, "w_child": w_child, "lambda": lam,
        "E": {lab: E for lab, _, E, _, _ in kbars},
        "C": Cs,
        "whats": {lab: wh for lab, _, _, _, wh in kbars},
    }


# --------------------------------------------------------------------------
# 2. the unbounded-family classification  (Theorem A of the report)
# --------------------------------------------------------------------------

def pairwise_consistency_affine(mu_e, what_e, C_e, mu_f, what_f, C_f, eps):
    """Coefficients (const, nu) of the R2.1 two-edge consistency residual

        kappa_e * E_f - kappa_f * E_e,  kappa_x = mu_x*what_x,
        E_x = (mu_x - eps) + nu*C_x.

    The residual vanishes for infinitely many nu iff both returned entries
    vanish.  This is the exact quantifier the C_e=0 dichotomy needs."""
    ke = Fr(mu_e) * Fr(what_e)
    kf = Fr(mu_f) * Fr(what_f)
    const = ke * (mu_f - eps) - kf * (mu_e - eps)
    slope = ke * C_f - kf * C_e
    return const, slope


def classify_unbounded(r0, mus, ms, lex, eps, whats, zero_arrival=False):
    """Decide whether the merge-local nu_G can be unbounded with these fixed
    discrete data.  Returns (verdict, reason).  Verdicts:
        'UNBOUNDED_EQJOIN'  - the C=0 equal-arrival family
        'BOUNDED'           - nu_G admits only finitely many values
    No cap is used anywhere: the decision is by the exact affine algebra."""
    k = len(ms)
    s = r0 + k + lex
    P = sum(mus) + sum(ms)
    T = P - s * eps
    if T == 0:
        return "BOUNDED", "T = 0 is forbidden by the root-mult law (R)"
    edge_mu = list(mus) + ([eps] if zero_arrival else [])
    edge_wh = [Fr(x) for x in whats[:r0]] + ([Fr(whats[r0])] if zero_arrival else [])
    Cs = [mu_e * s - P for mu_e in edge_mu]
    for i in range(len(edge_mu)):
        for j in range(i + 1, len(edge_mu)):
            const, slope = pairwise_consistency_affine(
                edge_mu[i], edge_wh[i], Cs[i], edge_mu[j], edge_wh[j], Cs[j], eps)
            if const != 0 or slope != 0:
                return "BOUNDED", (
                    "edges %d,%d give an affine consistency equation with a "
                    "nonzero coefficient (const=%s, slope=%s): nu_G is pinned"
                    % (i, j, const, slope))
    # all mu equal and all what equal at this point (proved in the report)
    if len(set(edge_mu)) != 1 or len(set(edge_wh)) != 1:
        return "BOUNDED", "degenerate consistency without equal (mu,what)"
    mu = edge_mu[0]
    if zero_arrival:
        return "BOUNDED", (
            "case III: eps = mu_0 = mu forces E = nu*C with C >= 1, so "
            "kbar = mu*what*(1+nu*s)/(nu*C) is strictly decreasing and "
            "nu_G is determined by kbar")
    C = mu * s - P
    if C != 0:
        return "BOUNDED", "C = %d != 0: E_e = (mu-eps) + nu*C is unbounded" % C
    if k != 0 or lex != 0:
        return "BOUNDED", "C = 0 requires k = lex = 0"
    return "UNBOUNDED_EQJOIN", "equal (mu,w), k = lex = 0, no 0-arrival, C = 0"


# --------------------------------------------------------------------------
# 3. the normalized equal-arrival family record
# --------------------------------------------------------------------------

class EqJoinFamily:
    """The exact C = 0 equal-arrival merge family.

        p = (-) eta^eps * prod_{e=1..r} (eta^nu - c_e^nu)^mu
        q = (-) eta     * prod_{e=1..r} (eta^nu - c_e^nu)

    with r >= 2 arrivals of common multiplicity mu and common invariant w,
    0 <= eps <= mu-1 a FREE 0-root (eps = 0 means absent).  Closed forms:

        dp      = eps + nu*r*mu          dq   = 1 + nu*r
        E       = mu - eps               (independent of nu)
        kbar    = mu*w*dq/E              (affine and unbounded in nu)
        X       = mu*(kbar - w)          rho  = kbar/dq = mu*w/E
        M       = gcd(mu - eps, nu*r + 1)
        w_child = mu*w*r/E               (CONSTANT in nu)
        lambda  = 0 if eps == 0 else max(1, ceil(mu*w*r/eps))   (constant)
        T       = r*(mu - eps)
    """

    KIND = "EQJOIN"
    VERSION = 1

    def __init__(self, r, mu, eps, w, interior=True, apply_n1=True):
        if r < 2:
            raise ValueError("a merge needs r >= 2")
        if mu < 1:
            raise ValueError("mu >= 1")
        if not (0 <= eps <= mu - 1):
            raise ValueError("free 0-root needs 0 <= eps <= mu-1 (searrow/NE)")
        self.r, self.mu, self.eps = int(r), int(mu), int(eps)
        self.w = Fr(w)
        if self.w <= 0:
            raise ValueError("w > 0")
        self.E = self.mu - self.eps
        self.interior = bool(interior)     # MP2: interior merges emit M >= 2
        self.apply_n1 = bool(apply_n1)     # N1: gcd(kbar, nu) = 1 at nu >= 2
        a, b = self.w.numerator, self.w.denominator
        self.a, self.b = a, b
        # kbar in Z  <=>  B' | dq
        Bfull = b * self.E
        self.Bp = Bfull // gcd(Bfull, self.mu * a)
        # N1 obstruction radical: gcd(kbar,nu) > 1 iff some P | nu with
        # v_P(mu*a) > v_P(b*E)  (independent of nu, since P | nu => P ∤ dq)
        Rn1 = 1
        for p in prime_factors(self.mu * a):
            if vp(self.mu * a, p) > (vp(Bfull, p) if Bfull % p == 0 else 0):
                Rn1 *= p
        self.R_n1 = Rn1
        self.w_child = Fr(self.mu * self.r) * self.w / self.E
        self.T = self.r * self.E
        self.lam = 0 if self.eps == 0 else max(1, ceil_fr(Fr(self.mu * self.r) * self.w / self.eps))
        self.period = lcm(lcm(self.Bp, self.E), max(self.R_n1, 1))
        self.residues = self._residues()
        self.min_period = self._minimal_period()

    # ---- exact per-member data -------------------------------------------
    def dp(self, nu):
        return self.eps + nu * self.r * self.mu

    def dq(self, nu):
        return 1 + nu * self.r

    def M(self, nu):
        return gcd(self.E, self.dq(nu))

    def kbar(self, nu):
        return Fr(self.mu) * self.w * self.dq(nu) / self.E

    def X(self, nu):
        return Fr(self.mu) * (self.kbar(nu) - self.w)

    def rho(self, nu):
        return Fr(self.mu) * self.w / self.E

    def admissible(self, nu):
        """Exact membership test.  nu = 1 is EXCEPTIONAL (case I) and is
        excluded here by design; see `exceptional_nu1`."""
        if nu < 2:
            return False
        dq = self.dq(nu)
        if dq % self.Bp != 0:                       # kbar in Z  (DS1(c))
            return False
        if self.interior and gcd(self.E, dq) < 2:   # MP2
            return False
        if self.apply_n1 and gcd(nu, self.R_n1) != 1:   # N1 primitivity
            return False
        return True

    def _residues(self):
        L = self.period
        return tuple(sorted(c for c in range(L)
                            if self.admissible(c if c >= 2 else c + L)))

    def _minimal_period(self):
        L = self.period
        for d in sorted(set([x for x in range(1, L + 1) if L % x == 0])):
            if all(((c % d) in set(x % d for x in self.residues))
                   == (c in self.residues) for c in range(L)):
                # d is a period iff membership only depends on nu mod d
                ok = True
                for c in range(L):
                    for c2 in range(L):
                        if c % d == c2 % d and (c in self.residues) != (c2 in self.residues):
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    return d
        return L

    def members(self, nu_lo, nu_hi):
        """All admissible nu in [nu_lo, nu_hi].  A window, never a cap: the
        family is certified infinite by `is_infinite()`."""
        return [nu for nu in range(max(2, nu_lo), nu_hi + 1) if self.admissible(nu)]

    def is_infinite(self):
        """The admissible set is a union of residue classes mod `period`
        intersected with [2, oo); it is infinite iff some class is admissible."""
        return len(self.residues) > 0

    def exceptional_nu1(self):
        """nu_G = 1 is a Prop 9.3 case-I lattice meet: kbar is only required
        to be rational there, so it is an EXCEPTIONAL value outside the AP."""
        nu = 1
        return {
            "nu": 1, "dp": self.dp(1), "dq": self.dq(1),
            "kbar": self.kbar(1), "M": self.M(1),
            "note": "case I (V_{2,a}\\V_{1,a}); kbar in Q legal, N1 not applicable",
        }

    # ---- canonical record -------------------------------------------------
    def record(self):
        return {
            "schema": "EQJOIN-FAMILY/v%d" % self.VERSION,
            "kind": self.KIND,
            "r": self.r,
            "mu": self.mu,
            "eps": self.eps,
            "w": "%d/%d" % (self.a, self.b),
            "E_gap": self.E,
            "T": self.T,
            "lambda": self.lam,
            "w_child": "%d/%d" % (self.w_child.numerator, self.w_child.denominator),
            "kbar_affine": {"slope": "%d/%d" % ((Fr(self.mu * self.r) * self.w / self.E).numerator,
                                                (Fr(self.mu * self.r) * self.w / self.E).denominator),
                            "intercept": "%d/%d" % ((Fr(self.mu) * self.w / self.E).numerator,
                                                    (Fr(self.mu) * self.w / self.E).denominator)},
            "M_law": "gcd(%d, %d*nu + 1)" % (self.E, self.r),
            "kbar_integrality_modulus": self.Bp,
            "n1_radical": self.R_n1,
            "interior_mp2": self.interior,
            "apply_n1": self.apply_n1,
            "period": self.min_period,
            "residues_mod_period": sorted(set(x % self.min_period for x in self.residues)),
            "infinite": self.is_infinite(),
            "t1": "RIGID: prod_e (t - c_e^nu) = t^r - A, A != 0; C != 0 automatic",
            "consumes_full_nu": ["case-III-zero-edge-when-this-merge-is-the-leaving-vertex"],
        }

    def canonical_json(self):
        return json.dumps(self.record(), sort_keys=True, separators=(",", ":"))

    def family_hash(self):
        return hashlib.sha256(self.canonical_json().encode("utf-8")).hexdigest()

    def __eq__(self, other):
        return isinstance(other, EqJoinFamily) and self.record() == other.record()

    def __repr__(self):
        return ("EqJoinFamily(r=%d, mu=%d, eps=%d, w=%s) period=%d residues=%s"
                % (self.r, self.mu, self.eps, self.w, self.min_period,
                   sorted(set(x % self.min_period for x in self.residues))))
