"""Canonical exact arithmetic for the D43 coefficient algebra K0.  Stdlib only.

Nothing here knows what is being proved.  It provides:

  * integer polynomial arithmetic and cyclotomic polynomials by exact division;
  * the cyclotomic quotient ring  Q[x]/(Phi_168)  with Fraction coefficients;
  * the canonical 432-monomial normal form of

        K0 = Q[z,r,A1,A2,h] / (Phi42(z), r^2-3, A1^3-(3+r), A2^3-(3-r), 2h^2-3)

    obtained by the confluent rewriting  z^12 -> ..., r^2 -> 3, A1^3 -> 3+r,
    A2^3 -> 3-r, h^2 -> 3/2  (Lemma L1 leading terms);
  * explicit finite-field helpers with no scanning over F_p.

No PARI, no third-party module, no network, no file access.
"""

from __future__ import annotations

from fractions import Fraction as Fr

# --------------------------------------------------------------------------
# integer polynomials, low-to-high coefficient lists
# --------------------------------------------------------------------------


def ptrim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                  for i in range(n)])


def psub(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
                  for i in range(n)])


def pmul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    return ptrim(out)


def pderiv(a):
    return ptrim([i * a[i] for i in range(1, len(a))])


def pdivexact(a, b):
    """Exact quotient a/b for integer polynomials; raises if inexact."""
    a = list(a)
    b = ptrim(b)
    if not b:
        raise ZeroDivisionError("divide by zero polynomial")
    if len(a) < len(b):
        if ptrim(a):
            raise ValueError("inexact division")
        return []
    q = [0] * (len(a) - len(b) + 1)
    for i in range(len(a) - len(b), -1, -1):
        c = a[i + len(b) - 1]
        if c % b[-1]:
            raise ValueError("inexact division")
        c //= b[-1]
        q[i] = c
        if c:
            for j, y in enumerate(b):
                a[i + j] -= c * y
    if ptrim(a):
        raise ValueError("nonzero remainder")
    return ptrim(q)


def cyclotomic(n):
    """Phi_n over Z, by exact division of x^n - 1 by the lower Phi_d."""
    num = [-1] + [0] * (n - 1) + [1]
    den = [1]
    for d in range(1, n):
        if n % d == 0:
            den = pmul(den, cyclotomic(d))
    return pdivexact(num, den)


def resultant(a, b):
    """Res(a,b) for integer polynomials, exact over Q by Euclid with tracking."""
    A = [Fr(c) for c in a]
    B = [Fr(c) for c in b]
    res = Fr(1)
    while True:
        B = [c for c in B]
        while B and B[-1] == 0:
            B.pop()
        if not B:
            return Fr(0)
        db = len(B) - 1
        if db == 0:
            return res * B[0] ** (len(A) - 1)
        R = list(A)
        while True:
            while R and R[-1] == 0:
                R.pop()
            if not R or len(R) - 1 < db:
                break
            c = R[-1] / B[-1]
            sh = len(R) - len(B)
            for j, y in enumerate(B):
                R[sh + j] -= c * y
        da = len(A) - 1
        dr = (len(R) - 1) if R else -1
        res *= (Fr(-1) ** (da * db)) * B[-1] ** ((da - dr) if R else da)
        A, B = B, R


def poly_eval_mod(coeffs, x, m):
    v = 0
    for c in reversed(coeffs):
        v = (v * x + c) % m
    return v


# --------------------------------------------------------------------------
# Q[x]/(Phi_168), Fraction coefficients
# --------------------------------------------------------------------------


class Cyclo168:
    """Arithmetic in Q[x]/(Phi_168).  Elements are Fraction coefficient lists."""

    def __init__(self, modulus):
        self.mod = ptrim(modulus)
        self.n = len(self.mod) - 1
        if self.mod[-1] != 1:
            raise ValueError("modulus must be monic")

    def red(self, a):
        a = [Fr(c) for c in a]
        n = self.n
        for i in range(len(a) - 1, n - 1, -1):
            c = a[i]
            if c:
                a[i] = Fr(0)
                for j in range(n):
                    a[i - n + j] -= c * self.mod[j]
        a = a[:n]
        while a and a[-1] == 0:
            a.pop()
        return a

    def mul(self, a, b):
        if not a or not b:
            return []
        out = [Fr(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b):
                    out[i + j] += Fr(x) * Fr(y)
        return self.red(out)

    def add(self, *xs):
        n = max((len(x) for x in xs), default=0)
        r = [sum((Fr(x[i]) for x in xs if i < len(x)), Fr(0)) for i in range(n)]
        while r and r[-1] == 0:
            r.pop()
        return r

    def scal(self, a, c):
        c = Fr(c)
        if c == 0:
            return []
        r = [Fr(x) * c for x in a]
        while r and r[-1] == 0:
            r.pop()
        return r

    def sub(self, a, b):
        return self.add(a, self.scal(b, -1))

    def pw(self, a, e):
        r = [Fr(1)]
        b = list(a)
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def xpow(self, k):
        return self.pw([Fr(0), Fr(1)], k % 168)

    def const(self, c):
        c = Fr(c)
        return [] if c == 0 else [c]

    def eval_int_poly(self, coeffs, val):
        acc = []
        for c in reversed(coeffs):
            acc = self.add(self.mul(acc, val), self.const(c))
        return acc


# --------------------------------------------------------------------------
# canonical K0 normal form on the 432 monomials
# --------------------------------------------------------------------------

BASIS_SHAPE = (12, 2, 3, 3, 2)


class K0Algebra:
    """K0 with a canonical normal form; ``phi42`` is the reduction datum."""

    def __init__(self, phi42):
        self.phi42 = tuple(phi42)
        if len(self.phi42) != 13 or self.phi42[-1] != 1:
            raise ValueError("Phi42 datum must be monic of degree 12")

    # -- core rewriting ----------------------------------------------------
    def norm(self, terms):
        work = dict(terms)
        out = {}
        while work:
            key, v = work.popitem()
            if v == 0:
                continue
            a, b, c, d, e = key
            if e >= 2:
                k = (a, b, c, d, e - 2)
                work[k] = work.get(k, Fr(0)) + v * Fr(3, 2)
                continue
            if d >= 3:
                k0 = (a, b, c, d - 3, e)
                k1 = (a, b + 1, c, d - 3, e)
                work[k0] = work.get(k0, Fr(0)) + v * 3
                work[k1] = work.get(k1, Fr(0)) - v
                continue
            if c >= 3:
                k0 = (a, b, c - 3, d, e)
                k1 = (a, b + 1, c - 3, d, e)
                work[k0] = work.get(k0, Fr(0)) + v * 3
                work[k1] = work.get(k1, Fr(0)) + v
                continue
            if b >= 2:
                k = (a, b - 2, c, d, e)
                work[k] = work.get(k, Fr(0)) + v * 3
                continue
            if a >= 12:
                for j in range(12):
                    if self.phi42[j]:
                        k = (a - 12 + j, b, c, d, e)
                        work[k] = work.get(k, Fr(0)) - v * self.phi42[j]
                continue
            out[key] = out.get(key, Fr(0)) + v
        return {k: v for k, v in out.items() if v != 0}

    # -- ring operations ---------------------------------------------------
    def mul(self, x, y):
        t = {}
        for kx, vx in x.items():
            for ky, vy in y.items():
                k = (kx[0] + ky[0], kx[1] + ky[1], kx[2] + ky[2],
                     kx[3] + ky[3], kx[4] + ky[4])
                t[k] = t.get(k, Fr(0)) + vx * vy
        return self.norm(t)

    def add(self, *xs):
        t = {}
        for x in xs:
            for k, v in x.items():
                t[k] = t.get(k, Fr(0)) + v
        return {k: v for k, v in t.items() if v != 0}

    def scal(self, x, c):
        c = Fr(c)
        return {} if c == 0 else {k: v * c for k, v in x.items()}

    def sub(self, x, y):
        return self.add(x, self.scal(y, -1))

    def pw(self, x, n):
        r = self.one()
        for _ in range(n):
            r = self.mul(r, x)
        return r

    def const(self, c):
        c = Fr(c)
        return {} if c == 0 else {(0, 0, 0, 0, 0): c}

    def one(self):
        return {(0, 0, 0, 0, 0): Fr(1)}

    def gen(self, idx):
        e = [0, 0, 0, 0, 0]
        e[idx] = 1
        return {tuple(e): Fr(1)}

    # -- the sigma involution  r -> -r, A1 <-> A2 --------------------------
    def sigma(self, x):
        t = {}
        for (a, b, c, d, e), v in x.items():
            k = (a, b, d, c, e)
            t[k] = t.get(k, Fr(0)) + (-v if b % 2 else v)
        return self.norm(t)

    # -- specialisation at a modular root frame ----------------------------
    def specialize(self, x, p, frame):
        z, r, a1, a2, h = frame
        s = 0
        for (a, b, c, d, e), v in x.items():
            t = pow(z, a, p) * pow(r, b, p) % p
            t = t * pow(a1, c, p) % p
            t = t * pow(a2, d, p) % p
            t = t * pow(h, e, p) % p
            den = v.denominator % p
            if den == 0:
                raise ZeroDivisionError("denominator vanishes at frame")
            s = (s + t * (v.numerator % p) * pow(den, -1, p)) % p
        return s

    def basis(self):
        return [(a, b, c, d, e)
                for a in range(BASIS_SHAPE[0])
                for b in range(BASIS_SHAPE[1])
                for c in range(BASIS_SHAPE[2])
                for d in range(BASIS_SHAPE[3])
                for e in range(BASIS_SHAPE[4])]


# --------------------------------------------------------------------------
# finite-field helpers: no scanning over F_p
# --------------------------------------------------------------------------


def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def factor_small(n):
    fs = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            fs.add(d)
            n //= d
        d += 1
    if n > 1:
        fs.add(n)
    return fs


def primitive_root(p):
    fs = factor_small(p - 1)
    g = 2
    while True:
        if all(pow(g, (p - 1) // q, p) != 1 for q in fs):
            return g
        g += 1


def primitive_nth_roots(p, n):
    """All primitive n-th roots of unity in F_p, requires n | p-1.

    Returns exactly phi(n) distinct values; each is verified to have exact
    order n, so no root-counting scan over F_p is performed anywhere.
    """
    if (p - 1) % n:
        raise ValueError("n does not divide p-1")
    w = pow(primitive_root(p), (p - 1) // n, p)
    out = []
    for k in range(1, n):
        if _gcd(k, n) == 1:
            out.append(pow(w, k, p))
    if len(set(out)) != len(out):
        raise AssertionError("repeated root")
    for v in out:
        if pow(v, n, p) != 1:
            raise AssertionError("not an n-th root")
        for q in factor_small(n):
            if pow(v, n // q, p) == 1:
                raise AssertionError("order too small")
    return sorted(out)


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def sqrt_mod(a, p):
    """Both square roots of a mod p, or [] if a is a non-residue."""
    a %= p
    if a == 0:
        return [0]
    if pow(a, (p - 1) // 2, p) != 1:
        return []
    if p % 4 == 3:
        x = pow(a, (p + 1) // 4, p)
        return sorted({x, (-x) % p})
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, x = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c = i, b * b % p
        t = t * c % p
        x = x * b % p
    return sorted({x, (-x) % p})


def cube_count_mod(a, p):
    """Number of cube roots of a in F_p for p = 1 mod 3.

    x -> x^3 is a homomorphism of F_p^* with kernel mu_3 of order 3, so every
    element of its image (the index-3 subgroup cut out by a^((p-1)/3) == 1)
    has exactly 3 preimages and every other nonzero element has none.  No
    discrete logarithm and no scan over F_p is used.
    """
    a %= p
    if (p - 1) % 3:
        raise ValueError("p is not 1 mod 3")
    if a == 0:
        return 1
    return 3 if pow(a, (p - 1) // 3, p) == 1 else 0


def cubic_character(a, p):
    """The value a^((p-1)/3) in mu_3(F_p) as a literal field element."""
    a %= p
    if a == 0:
        raise ZeroDivisionError("cubic character of zero")
    return pow(a, (p - 1) // 3, p)


def mu3(p):
    """The three cube roots of unity in F_p, sorted, for p = 1 mod 3."""
    w = pow(primitive_root(p), (p - 1) // 3, p)
    return sorted({1, w, w * w % p})
