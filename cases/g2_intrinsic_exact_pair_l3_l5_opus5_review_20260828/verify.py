#!/usr/bin/env python3
"""
Independent standard-library checker for the intrinsic exact-pair L3/L4/L5 claims.

Opus 5 hostile review, 2026-08-28.  Pure stdlib, exact arithmetic, no CAS.

What is checked, and how independence is arranged
-------------------------------------------------
Every curve test carries TWO independently-produced objects:

  (A) a certified complete root set: an explicit factorization
          h(t^-kappa, y)  ==  A(t) * prod_i ( y - r_i(t) )
      with r_i in F_p[t,1/t], verified as an exact identity of Laurent
      polynomials.  This pins the FULL root multiset with no reference to
      any Newton-Puiseux recursion.

  (B) a certified place list: for each normalized place S of the curve in the
      x-chart, an explicit rational parametrization s |-> (x(s), y(s)) with
        - h(x(s), y(s)) == 0 exactly, and
        - a birationality certificate s == Num(x,y)/Den(x,y) verified by
          composing back,
      from which  e_S := -ord_s(x(s))  is read off geometrically.

The Sigray all-root recursion is then run as a THIRD, separate engine and its
residual-polynomial degrees / multiplicities are compared against (A), and the
deck-orbit data against (B).

Mutations (deliberately wrong variants) are asserted to FAIL, so that a
vacuous "everything passes" outcome is impossible.
"""

import sys
from math import gcd

P = 2521                       # prime; P-1 = 2520 = lcm(1..10)
assert all(pow(a, P - 1, P) == 1 for a in (2, 3, 5, 7, 11)), "P not prime-ish"

FAILURES = []
CHECKS = [0]


VERBOSE = [False]


def check(name, cond, detail=""):
    CHECKS[0] += 1
    if cond and VERBOSE[0]:
        print("  ok    %-58s %s" % (name, detail))
    if not cond:
        FAILURES.append((name, detail))
        print("  FAIL  %-58s %s" % (name, detail))
    return cond


# ----------------------------------------------------------------- Laurent(t)
# dict {exponent:int -> coeff:int mod P}, zero entries pruned.

def L(*pairs):
    return lclean({e: c for e, c in pairs})


def lclean(d):
    return {e: c % P for e, c in d.items() if c % P}


def ladd(a, b):
    r = dict(a)
    for e, c in b.items():
        r[e] = (r.get(e, 0) + c) % P
    return lclean(r)


def lneg(a):
    return {e: (-c) % P for e, c in a.items()}


def lmul(a, b):
    r = {}
    for e1, c1 in a.items():
        for e2, c2 in b.items():
            r[e1 + e2] = (r.get(e1 + e2, 0) + c1 * c2) % P
    return lclean(r)


def lpow(a, n):
    r = L((0, 1))
    for _ in range(n):
        r = lmul(r, a)
    return r


def lord(a):
    return min(a) if a else None            # ord_t; None for the zero series


def ltrunc(a, n):
    return lclean({e: c for e, c in a.items() if e < n})


# --------------------------------------------- bivariate (t-exponent, eta-deg)

def badd(a, b):
    r = dict(a)
    for k, c in b.items():
        r[k] = (r.get(k, 0) + c) % P
    return {k: c for k, c in r.items() if c}


def bmul(a, b):
    r = {}
    for (e1, d1), c1 in a.items():
        for (e2, d2), c2 in b.items():
            k = (e1 + e2, d1 + d2)
            r[k] = (r.get(k, 0) + c1 * c2) % P
    return {k: c for k, c in r.items() if c}


def bpow(a, n):
    r = {(0, 0): 1}
    for _ in range(n):
        r = bmul(r, a)
    return r


# ------------------------------------------------------- univariate over F_p
# poly in eta: dict {deg -> coeff}

def pdeg(p):
    return max(p) if p else -1


def peval(p, c):
    return sum(co * pow(c, d, P) for d, co in p.items()) % P


def proots(p):
    if not p:
        raise ValueError("zero residual polynomial")
    return [c for c in range(P) if peval(p, c) == 0]


def pmult(p, c):
    """multiplicity of c as a root of p (Sigray Notation 3.12; 0 if not a root)"""
    if not p:
        raise ValueError("zero polynomial")
    m = 0
    desc = [p.get(i, 0) for i in range(pdeg(p), -1, -1)]    # descending

    while len(desc) > 1:
        out, carry = [], 0
        for a in desc:
            carry = (a + carry * c) % P
            out.append(carry)
        rem = out[-1]
        if rem % P != 0:
            break
        desc = out[:-1]
        m += 1
    return m


# ------------------------------------------------------ curve substitution
# h given as dict {(i,j) -> coeff} for coeff * x^i * y^j

def h_deg_y(h):
    return max(j for (_, j) in h)


def h_lc_y(h, kappa):
    """A(t) = leading y-coefficient of h(t^-kappa, y)"""
    D = h_deg_y(h)
    return lclean({-kappa * i: c for (i, j), c in h.items() if j == D})


def h_as_ypoly(h, kappa):
    """h(t^-kappa, y) as {y-degree -> Laurent(t)}"""
    out = {}
    for (i, j), c in h.items():
        out.setdefault(j, {})
        out[j] = ladd(out[j], L((-kappa * i, c)))
    return {j: v for j, v in out.items() if v}


def h_shifted(h, kappa, prefix, n):
    """h_n(t, eta) with y = sum_{m<n} prefix[m] t^m + t^n eta  (Sigray Prop 3.1)."""
    Y = {}
    for m, c in enumerate(prefix[:n]):
        if c % P:
            Y[(m, 0)] = c % P
    Y[(n, 1)] = 1
    out = {}
    for (i, j), c in h.items():
        term = bmul({(-kappa * i, 0): c % P}, bpow(Y, j))
        out = badd(out, term)
    return out


def residual(hn):
    """Sigray Notation 3.10: p_{h,F} = eta-polynomial at the minimal t-exponent."""
    amin = min(e for (e, _) in hn)
    return amin, {d: c for (e, d), c in hn.items() if e == amin}


# =========================================================================
# PART A -- exhaustive Kummer orbit / stabilizer arithmetic  (pure Z/kappa)
# =========================================================================
# mu_kappa acts by phi(t) -> phi(zeta t), i.e. c_m -> zeta^m c_m.  With a
# primitive kappa-th root of unity, a and a' act identically on a series whose
# support is exactly S iff (a-a')*m == 0 mod kappa for all m in S.  So orbit
# and stabiliser sizes are exact integer data, computed here by brute force
# over the group and compared with the closed forms
#     |Stab| = gcd(kappa, gcd(S))     (gcd(kappa, empty) = kappa)
#     |Orb|  = kappa / |Stab|  =: reduced Puiseux denominator.

def part_A():
    print("PART A  exhaustive Kummer orbit/stabiliser arithmetic")
    bad_ambient = 0
    total = 0
    for kappa in range(1, 13):
        for mask in range(1 << 12):
            S = [m for m in range(12) if mask >> m & 1]
            stab = [a for a in range(kappa)
                    if all((a * m) % kappa == 0 for m in S)]
            orb = kappa // len(stab)
            g = 0
            for m in S:
                g = gcd(g, m)
            closed = gcd(kappa, g) if g else kappa        # gcd(kappa,0)=kappa
            total += 1
            if len(stab) != closed or orb != kappa // closed:
                check("A/orbit-stabiliser", False,
                      "kappa=%d S=%s" % (kappa, S))
                return
            if orb != kappa:
                bad_ambient += 1
    check("A/orbit-stabiliser closed form on %d (kappa,support) pairs" % total, True)
    # MUTATION M2: "reduced denominator == ambient index kappa" must be false often
    check("A/M2 mutation 'reduced denom == ambient kappa' is refuted",
          bad_ambient > 0, "%d counterexamples" % bad_ambient)
    # zero / constant support convention
    for kappa in (1, 2, 4, 6, 12):
        for S in ([], [0]):
            stab = [a for a in range(kappa)
                    if all((a * m) % kappa == 0 for m in S)]
            check("A/constant-support kappa=%d S=%s gives e=1" % (kappa, S),
                  kappa // len(stab) == 1)
    print("  (%d checks so far)" % CHECKS[0])


# =========================================================================
# PART B -- curve tests
# =========================================================================

def root_of_unity(n):
    """primitive n-th root of unity in F_p (n | P-1)"""
    assert (P - 1) % n == 0, n
    for g in range(2, P):
        w = pow(g, (P - 1) // n, P)
        if all(pow(w, n // q, P) != 1 for q in set(prime_factors(n))):
            return w
    raise RuntimeError


def prime_factors(n):
    f, d = [], 2
    while d * d <= n:
        while n % d == 0:
            f.append(d)
            n //= d
        d += 1
    if n > 1:
        f.append(n)
    return f


class Curve:
    def __init__(self, name, h, kappa, A, roots, places, notes=""):
        self.name, self.h, self.kappa = name, h, kappa
        self.A, self.roots, self.places, self.notes = A, roots, places, notes


def certify_factorization(cv):
    """A(t) * prod (y - r_i) == h(t^-kappa, y), exact Laurent identity."""
    prod = {0: L((0, 1))}                       # y-poly with Laurent coeffs
    for r in cv.roots:
        new = {}
        for j, c in prod.items():               # multiply by (y - r)
            new[j + 1] = ladd(new.get(j + 1, {}), c)
            new[j] = ladd(new.get(j, {}), lmul(lneg(r), c))
        prod = {j: c for j, c in new.items() if c}
    prod = {j: lmul(cv.A, c) for j, c in prod.items()}
    prod = {j: c for j, c in prod.items() if c}
    target = h_as_ypoly(cv.h, cv.kappa)
    return prod == target


def certify_place(cv, pl):
    """h(x(s),y(s))==0 exactly, plus a birationality certificate for s."""
    xs, ys, num, den = pl["x"], pl["y"], pl["num"], pl["den"]
    val = {}
    for (i, j), c in cv.h.items():
        val = ladd(val, lmul(L((0, c)), lmul(lpow(xs, i), lpow(ys, j))))
    on_curve = (val == {})
    nn, dd = {}, {}
    for (i, j), c in num.items():
        nn = ladd(nn, lmul(L((0, c)), lmul(lpow(xs, i), lpow(ys, j))))
    for (i, j), c in den.items():
        dd = ladd(dd, lmul(L((0, c)), lmul(lpow(xs, i), lpow(ys, j))))
    birational = (dd != {}) and (nn == lmul(L((1, 1)), dd))
    e_geo = -lord(xs)
    return on_curve, birational, e_geo


def deck(r, kappa, w):
    """(zeta . r)(t) = r(zeta t) with zeta = w a primitive kappa-th root."""
    return lclean({e: c * pow(w, e, P) for e, c in r.items()})


def part_B(curves):
    print("\nPART B  curve-level checks (certified factorization + parametrization)")
    for cv in curves:
        print("  %s   kappa=%d   %s" % (cv.name, cv.kappa, cv.notes))
        k = cv.kappa
        check("%s: full-root factorization identity" % cv.name,
              certify_factorization(cv))

        # B_x roots = the certified roots lying in F_p[[t]] (ord >= 0);
        # the zero series {} has ord None and is included.
        finite = [r for r in cv.roots if (lord(r) is None or lord(r) >= 0)]
        distinct = []
        for r in finite:
            if r not in distinct:
                distinct.append(r)

        # ---- place certificates -> geometric e_S
        e_geo = []
        for pl in cv.places:
            oc, bi, e = certify_place(cv, pl)
            check("%s: place '%s' lies on the curve" % (cv.name, pl["tag"]), oc)
            check("%s: place '%s' birationality certificate" % (cv.name, pl["tag"]), bi)
            check("%s: place '%s' is in B_x (y regular)" % (cv.name, pl["tag"]),
                  lord(pl["y"]) is None or lord(pl["y"]) >= 0)
            e_geo.append(e)

        # ---- deck orbits of the finite roots
        w = root_of_unity(k) if k > 1 else 1
        orbits = []
        seen = set()
        for r in distinct:
            key = tuple(sorted(r.items()))
            if key in seen:
                continue
            orb, cur = [], r
            for _ in range(k):
                if cur not in orb:
                    orb.append(cur)
                seen.add(tuple(sorted(cur.items())))
                cur = deck(cur, k, w)
            orbits.append(orb)
        check("%s: #deck orbits == #certified places" % cv.name,
              len(orbits) == len(cv.places),
              "orbits=%d places=%d" % (len(orbits), len(cv.places)))
        check("%s: orbit sizes == geometric ramification e_S" % cv.name,
              sorted(len(o) for o in orbits) == sorted(e_geo),
              "orbits=%s e_geo=%s" % (sorted(len(o) for o in orbits), sorted(e_geo)))
        for o in orbits:
            r = o[0]
            g = 0
            for m in r:
                g = gcd(g, m)
            closed = gcd(k, g) if g else k
            check("%s: kappa/gcd(kappa,supp) == orbit size (orbit of ord %d)"
                  % (cv.name, lord(r) if r else -1),
                  k // closed == len(o), "supp=%s k=%d" % (sorted(r), k))
            check("%s: stabiliser size == kappa/e_S" % cv.name,
                  closed == k // len(o))

        # ---- no cross-place / cross-component collision
        allpairs_ok = True
        for i in range(len(orbits)):
            for j in range(i + 1, len(orbits)):
                if set(map(lambda z: tuple(sorted(z.items())), orbits[i])) & \
                   set(map(lambda z: tuple(sorted(z.items())), orbits[j])):
                    allpairs_ok = False
        check("%s: distinct orbits are disjoint (no place collision)" % cv.name,
              allpairs_ok)

        # ---- Sigray Proposition 3.1 (*) and (**), and Statement 3.9(i),(iii)
        prop_ok, stmt_i_ok, stmt_iii_ok = run_recursion(cv, distinct)
        check("%s: Prop 3.1 (*) deg p_d == #roots with the prefix" % cv.name, prop_ok[0])
        check("%s: Prop 3.1 (**) mult(p_d,c) == #roots with extended prefix" % cv.name,
              prop_ok[1])
        check("%s: Statement 3.9(i)  mult(p_F,c) == deg(p_{F*c})" % cv.name, stmt_i_ok)
        check("%s: Statement 3.9(iii) d_{F*c} = d_F - mult/kappa" % cv.name, stmt_iii_ok)

        # ---- terminal certificate: deg p == 1  <=>  separation
        terminal_audit(cv, distinct)


def run_recursion(cv, distinct, drop_zero_root=False, collected=None):
    """Sigray all-root recursion; returns ((*)ok,(**)ok), 3.9(i)ok, 3.9(iii)ok."""
    k, h = cv.kappa, cv.h
    ok_star = ok_starstar = ok_i = ok_iii = True
    MAXN = 14

    def walk(prefix, parent_deg):
        nonlocal ok_star, ok_starstar, ok_i, ok_iii
        n = len(prefix)
        amin, pd = residual(h_shifted(h, k, prefix, n))
        matching = [r for r in distinct
                    if all(r.get(m, 0) == prefix[m] % P for m in range(n))]
        if pdeg(pd) != len(matching):
            ok_star = False
        # a leaf record is born exactly where the residual degree first hits 1
        if collected is not None and pdeg(pd) == 1 and parent_deg != 1:
            collected.append(list(prefix))
        if pdeg(pd) <= 0 or n >= MAXN:
            return
        rts = proots(pd)
        if drop_zero_root:
            rts = [c for c in rts if c != 0]
        for c in rts:
            m = pmult(pd, c)
            ext = [r for r in matching if r.get(n, 0) == c % P]
            if m != len(ext):
                ok_starstar = False
            amin2, pd2 = residual(h_shifted(h, k, prefix + [c], n + 1))
            if m != pdeg(pd2):
                ok_i = False
            if amin2 != amin + m:
                ok_iii = False
            if n + 1 < MAXN and pdeg(pd2) >= 1:
                walk(prefix + [c], pdeg(pd))

    walk([], 0)
    return (ok_star, ok_starstar), ok_i, ok_iii


def terminal_audit(cv, distinct):
    """deg p_{h,F} == 1 as the finite terminal certificate; support-gcd validity."""
    k, h = cv.kappa, cv.h
    for r in distinct:
        # minimal N with deg p == 1 at the length-N prefix of r
        Nterm = None
        for N in range(0, 16):
            pref = [r.get(m, 0) for m in range(N)]
            _, pd = residual(h_shifted(h, k, pref, N))
            if pdeg(pd) == 1:
                Nterm = N
                break
        if Nterm is None:
            check("%s: terminal deg-1 certificate reached" % cv.name, False,
                  "root ord %s" % lord(r))
            continue
        others = [q for q in distinct if q != r]
        contacts = [lord(ladd(r, lneg(q))) for q in others]
        maxc = max(contacts) if contacts else -1
        check("%s: terminal N=%d exceeds every contact (max %d)"
              % (cv.name, Nterm, maxc), Nterm > maxc,
              "N=%d maxcontact=%d" % (Nterm, maxc))
        # support gcd read from the truncation equals the true support gcd
        gt = 0
        for m in r:
            gt = gcd(gt, m)
        gt = gcd(k, gt) if gt else k
        gp = 0
        for m in range(Nterm):
            if r.get(m, 0):
                gp = gcd(gp, m)
        gp = gcd(k, gp) if gp else k
        check("%s: truncated support gcd == full support gcd at terminal N"
              % cv.name, gp == gt, "gp=%d gt=%d N=%d" % (gp, gt, Nterm))
        # MUTATION M7: at N-1 the support gcd may be wrong -- record it
        if Nterm >= 1:
            gm = 0
            for m in range(Nterm - 1):
                if r.get(m, 0):
                    gm = gcd(gm, m)
            gm = gcd(k, gm) if gm else k
            if gm != gt:
                MUT7[0] += 1


MUT7 = [0]


# =========================================================================

def mk(*terms):
    d = {}
    for i, j, c in terms:
        d[(i, j)] = (d.get((i, j), 0) + c) % P
    return {kk: v for kk, v in d.items() if v}


def build_curves():
    C = []

    # ---- C1  x y^2 - 1 : one place, e=2.  kappa = 2 (tight), 4 and 6 oversized.
    h1 = mk((1, 2, 1), (0, 0, -1))
    pl1 = [dict(tag="S(e=2)", x=L((-2, 1)), y=L((1, 1)),
                num={(0, 1): 1}, den={(0, 0): 1})]          # s = y
    for kap in (2, 4, 6):
        hk = kap // 2
        C.append(Curve("C1 x*y^2-1", h1, kap, L((-kap, 1)),
                       [L((hk, 1)), L((hk, -1))], pl1,
                       "one place e=2; %s" %
                       ("tight cover" if kap == 2 else
                        "OVERSIZED cover (Sol report 2 control 6.1)")))

    # ---- C2  x y^3 - 1 : one place, e=3.
    h2 = mk((1, 3, 1), (0, 0, -1))
    pl2 = [dict(tag="S(e=3)", x=L((-3, 1)), y=L((1, 1)),
                num={(0, 1): 1}, den={(0, 0): 1})]
    for kap in (3, 6):
        w3 = root_of_unity(3)
        C.append(Curve("C2 x*y^3-1", h2, kap, L((-kap, 1)),
                       [L((kap // 3, pow(w3, e, P))) for e in range(3)], pl2,
                       "one place e=3; %s" % ("tight" if kap == 3 else "OVERSIZED")))

    # ---- C5  (xy-1)(x^3 y - x^2 - 1) : two places e=1, contact 3 (Sol control 6.2, N=3)
    h5 = poly_mul(mk((1, 1, 1), (0, 0, -1)), mk((3, 1, 1), (2, 0, -1), (0, 0, -1)))
    pl5 = [dict(tag="S1 (xy=1)", x=L((-1, 1)), y=L((1, 1)),
                num={(0, 0): 1}, den={(1, 0): 1}),                    # s = 1/x
           dict(tag="S2 (x^3y=x^2+1)", x=L((-1, 1)), y=L((1, 1), (3, 1)),
                num={(0, 0): 1}, den={(1, 0): 1})]
    C.append(Curve("C5 (xy-1)(x^3y-x^2-1)", h5, 1, L((-4, 1)),
                   [L((1, 1)), L((1, 1), (3, 1))], pl5,
                   "premature common prefix, contact 3 (Sol control 6.2)"))

    # ---- C6  y - 3 : horizontal line, constant series, oversized kappa
    h6 = mk((0, 1, 1), (0, 0, -3))
    pl6 = [dict(tag="S(horizontal)", x=L((-1, 1)), y=L((0, 3)),
                num={(0, 0): 1}, den={(1, 0): 1})]
    for kap in (1, 6):
        C.append(Curve("C6 y-3 (horizontal line)", h6, kap, L((0, 1)),
                       [L((0, 3))], pl6,
                       "constant series, kappa=%d" % kap))

    # ---- C7  y : zero series
    h7 = mk((0, 1, 1))
    pl7 = [dict(tag="S(y=0)", x=L((-1, 1)), y={},
                num={(0, 0): 1}, den={(1, 0): 1})]
    C.append(Curve("C7 y (zero series)", h7, 4, L((0, 1)), [{}], pl7,
                   "zero-support convention, OVERSIZED kappa=4"))

    # ---- C8  x^5 y^2 - (x^2+1)^2 : one place e=2, long expansion y = s + s^5
    h8 = mk((5, 2, 1), (4, 0, -1), (2, 0, -2), (0, 0, -1))
    pl8 = [dict(tag="S(e=2, y=s+s^5)", x=L((-2, 1)), y=L((1, 1), (5, 1)),
                num={(2, 1): 1}, den={(2, 0): 1, (0, 0): 1})]   # s = y x^2/(x^2+1)
    C.append(Curve("C8 x^5y^2-(x^2+1)^2", h8, 2, L((-10, 1)),
                   [L((1, 1), (5, 1)), L((1, -1), (5, -1))], pl8,
                   "e=2, tight cover, nontrivial support {1,5}"))
    C.append(Curve("C8 x^5y^2-(x^2+1)^2", h8, 4, L((-20, 1)),
                   [L((2, 1), (10, 1)), L((2, -1), (10, -1))], pl8,
                   "OVERSIZED kappa=4, support {2,10}, gcd 2, e=2"))

    # ---- C10 (y^2-x)(xy-1) : escaping branch (x,y both infinite) + one B_x place
    h10 = poly_mul(mk((0, 2, 1), (1, 0, -1)), mk((1, 1, 1), (0, 0, -1)))
    pl10 = [dict(tag="S(xy=1)", x=L((-1, 1)), y=L((1, 1)),
                 num={(0, 0): 1}, den={(1, 0): 1})]   # e=1: s = 1/x
    C.append(Curve("C10 (y^2-x)(xy-1)", h10, 2, L((-2, 1)),
                   [L((-1, 1)), L((-1, -1)), L((2, 1))], pl10,
                   "two escaping branches x=y=infinity are excluded from B_x"))

    # ---- C11 (x-5)(xy-1) : vertical component present
    h11 = poly_mul(mk((1, 0, 1), (0, 0, -5)), mk((1, 1, 1), (0, 0, -1)))
    pl11 = [dict(tag="S(xy=1)", x=L((-1, 1)), y=L((1, 1)),
                 num={(0, 0): 1}, den={(1, 0): 1})]
    C.append(Curve("C11 (x-5)(xy-1)", h11, 1,
                   lmul(L((-1, 1)), L((-1, 1), (0, -5))),
                   [L((1, 1))], pl11,
                   "vertical component contributes nothing in the x-chart"))

    # ---- C12 (y-3)(xy^2-1) : horizontal + e=2 place, zero residual root present
    h12 = poly_mul(mk((0, 1, 1), (0, 0, -3)), h1)
    pl12 = [dict(tag="S(horizontal)", x=L((-1, 1)), y=L((0, 3)),
                 num={(0, 0): 1}, den={(1, 0): 1}),
            dict(tag="S(e=2)", x=L((-2, 1)), y=L((1, 1)),
                 num={(0, 1): 1}, den={(0, 0): 1})]
    C.append(Curve("C12 (y-3)(x*y^2-1)", h12, 2, L((-2, 1)),
                   [L((0, 3)), L((1, 1)), L((1, -1))], pl12,
                   "reducible: two components, e=1 and e=2, zero root at level 0"))
    return C


def poly_mul(a, b):
    r = {}
    for (i1, j1), c1 in a.items():
        for (i2, j2), c2 in b.items():
            k = (i1 + i2, j1 + j2)
            r[k] = (r.get(k, 0) + c1 * c2) % P
    return {k: v for k, v in r.items() if v}


# =========================================================================
# PART C -- mutations that must FAIL
# =========================================================================

def part_C(curves):
    print("\nPART C  mutations (each must be detected)")
    VERBOSE[0] = True

    by = {}
    for cv in curves:
        by.setdefault(cv.name, []).append(cv)

    # M3: dropping the zero residual root loses branches
    cv = [c for c in curves if c.name.startswith("C12")][0]
    distinct = [r for r in cv.roots if lord(r) is None or lord(r) >= 0]
    got = []
    run_recursion(cv, distinct, drop_zero_root=True, collected=got)
    full = []
    run_recursion(cv, distinct, drop_zero_root=False, collected=full)
    check("C/M3 dropping the zero residual root loses leaves",
          len(got) < len(full), "kept %d of %d" % (len(got), len(full)))

    # M4: non-squarefree h -- deg p_d over-counts distinct Puiseux series
    h1 = mk((1, 2, 1), (0, 0, -1))
    h13 = poly_mul(h1, h1)
    _, pd = residual(h_shifted(h13, 2, [], 0))
    check("C/M4 non-squarefree (x y^2-1)^2: deg p_d = 4 but 2 distinct series",
          pdeg(pd) == 4, "deg p_d = %d" % pdeg(pd))
    _, pd1 = residual(h_shifted(h1, 2, [], 0))
    check("C/M4 control: squarefree x y^2-1 gives deg p_d = 2", pdeg(pd1) == 2)

    # M5: escaping (pole) roots must NOT be counted
    cv = [c for c in curves if c.name.startswith("C10")][0]
    _, pd = residual(h_shifted(cv.h, cv.kappa, [], 0))
    check("C/M5 deg p_d counts only ord>=0 roots (1, not deg_y h = 3)",
          pdeg(pd) == 1, "deg p_d = %d, deg_y h = %d" % (pdeg(pd), h_deg_y(cv.h)))

    # M6: premature terminal on the Sol 6.2 control merges two places
    cv = [c for c in curves if c.name.startswith("C5")][0]
    _, pd = residual(h_shifted(cv.h, 1, [0, 1, 0], 3))
    check("C/M6 prefix of length 3 on (xy-1)(x^3y-x^2-1) is NOT terminal",
          pdeg(pd) == 2, "deg p at N=3 is %d" % pdeg(pd))
    _, pd4 = residual(h_shifted(cv.h, 1, [0, 1, 0, 0], 4))
    check("C/M6 prefix of length 4 IS terminal", pdeg(pd4) == 1,
          "deg p at N=4 is %d" % pdeg(pd4))

    # M7: support gcd read one step before the terminal N can be wrong
    check("C/M7 premature support gcd gives a wrong ramification somewhere",
          MUT7[0] > 0, "%d occurrences" % MUT7[0])

    # M2 already exercised exhaustively in Part A.

    # M8: reading a place-level order off the raw cover t-order without
    #     dividing by q = kappa/e_S is wrong on an oversized cover.
    cv2 = [c for c in curves if c.name.startswith("C1 ") and c.kappa == 6][0]
    r = cv2.roots[0]
    check("C/M8 raw t-order 3 on kappa=6 cover != place order 1 (q=3)",
          lord(r) == 3 and lord(r) // (cv2.kappa // 2) == 1)


def main():
    print("=" * 74)
    print("Opus 5 independent checker: intrinsic exact-pair L3/L4/L5")
    print("F_p with p = %d  (p-1 = %d)" % (P, P - 1))
    print("=" * 74)
    part_A()
    curves = build_curves()
    part_B(curves)
    part_C(curves)
    print("\n" + "=" * 74)
    if FAILURES:
        print("RESULT: FAIL   (%d of %d checks failed)" % (len(FAILURES), CHECKS[0]))
        for n, d in FAILURES:
            print("   -", n, d)
        return 1
    print("RESULT: PASS   (all %d checks passed)" % CHECKS[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())
