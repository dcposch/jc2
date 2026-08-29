#!/usr/bin/env python3
"""U2 (nu=1, unbounded lex) exact core: LL-1/MP6 absorbed pattern, T1 identity,
degree class, M / w_tr / P1.

Stdlib only, Fraction arithmetic, no floats, no caps, no engine import.
Cap tokens (NUCAP, MAXNU, --cap) are refused by the emitter.
"""
from fractions import Fraction as Fr
from math import comb, gcd

from polyexact import Poly


# ---------------------------------------------------------------------------
# Univariate polynomials over Q, low-to-high coefficients.
# ---------------------------------------------------------------------------

def umul(a, b):
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r


def uadd(*ps):
    n = max((len(p) for p in ps), default=0)
    r = [Fr(0)] * n
    for p in ps:
        for i, x in enumerate(p):
            r[i] += x
    return r


def uscale(a, c):
    return [Fr(c) * x for x in a]


def uderiv(a):
    return [a[i] * i for i in range(1, len(a))]


def utrim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def ugcd(a, b):
    a, b = utrim(list(a)), utrim(list(b))
    while b and any(x != 0 for x in b):
        while a and a[-1] == 0:
            a.pop()
        while b and b[-1] == 0:
            b.pop()
        if not b:
            break
        while len(a) >= len(b) and a:
            lead = a[-1] / b[-1]
            d = len(a) - len(b)
            for i in range(len(b)):
                a[i + d] -= lead * b[i]
            while a and a[-1] == 0:
                a.pop()
        a, b = b, a
    while a and a[-1] == 0:
        a.pop()
    return a


def squarefree(p):
    g = ugcd(p, uderiv(p))
    return len(g) <= 1


def coprime(p, q):
    g = ugcd(p, q)
    return len(g) <= 1


# ---------------------------------------------------------------------------
# Closed forms after LL-1 / MP6 nu=1 absorption.
# ---------------------------------------------------------------------------

def u2_degrees(r, mu, L):
    """Absorbed nu=1 equal-mu shape, eps=k=0, e0=0.
    p = Rad^mu, q = Rad * S, deg Rad = r, deg S = L >= 1.
    dp = r*mu, dq = r+L  (the eta slot is not extra).
    """
    dp = r * mu
    dq = r + L
    E = mu * L                         # mu*dq - dp
    M = gcd(dp, dq)
    return dp, dq, E, M


def w_tr(w, r, L):
    """Successor invariant: w_tr = w * (r + L - 1) / L  (nu=1, E = mu L)."""
    return w * Fr(r + L - 1, L)


def kbar_of(w, r, mu, L):
    """kbar = mu * w * dq / E = w * (r + L) / L."""
    return w * Fr(r + L, L)


def M_law(r, mu, L):
    """M = gcd(r mu, r+L).  On r=2, L odd: gcd(mu, L+2).
    On L = 1 + r k: gcd(mu, r(k+1)+1).
    """
    return gcd(r * mu, r + L)


def mp2_alive_r2(mu, L):
    """r=2: even L is T1-dead; odd L has M = gcd(mu, L+2)."""
    if L % 2 == 0:
        return False
    return gcd(mu, L + 2) >= 2


# ---------------------------------------------------------------------------
# U2-ODE: r Rad S' - L Rad' S.
# ---------------------------------------------------------------------------

def ode_poly(Rad, S, r, L):
    return utrim(uadd(uscale(umul(Rad, uderiv(S)), r),
                      uscale(umul(uderiv(Rad), S), -L)))


def ode_is_nonzero_constant(Rad, S, r, L):
    lhs = ode_poly(Rad, S, r, L)
    if not lhs:
        return False, Fr(0)
    if any(lhs[i] != 0 for i in range(1, len(lhs))):
        return False, lhs[0] if lhs else Fr(0)
    return lhs[0] != 0, lhs[0]


# ---------------------------------------------------------------------------
# Symbolic T1 identity at absorbed nu=1 (eta = t).
# ---------------------------------------------------------------------------

def verify_absorbed_identity(r, mu, L):
    """lhs = rho p q' - p' q  equals  p * (mu/(r+L)) * (r Rad S' - L Rad' S)
    identically in eta and in the symbolic pattern coefficients.
    """
    n = 1 + r + L
    eta = Poly.var(n, 0)
    Rad = eta.pow(r)
    Rad_t = Poly.const(n, r) * eta.pow(r - 1) if r >= 1 else Poly.const(n, 0)
    for j in range(r):
        pj = Poly.var(n, 1 + j)
        Rad = Rad + pj * eta.pow(j)
        if j >= 1:
            Rad_t = Rad_t + Poly.const(n, j) * pj * eta.pow(j - 1)
    S = eta.pow(L)
    S_t = Poly.const(n, L) * eta.pow(L - 1) if L >= 1 else Poly.const(n, 0)
    for j in range(L):
        sj = Poly.var(n, 1 + r + j)
        S = S + sj * eta.pow(j)
        if j >= 1:
            S_t = S_t + Poly.const(n, j) * sj * eta.pow(j - 1)
    p = Rad.pow(mu)
    q = Rad * S
    dp = r * mu
    dq = r + L
    rho = Fr(dp, dq)
    lhs = Poly.const(n, rho) * p * q.diff(0) - p.diff(0) * q
    ode = (Poly.const(n, r) * Rad * S_t
           - Poly.const(n, L) * Rad_t * S)
    rhs = p * Poly.const(n, Fr(mu, dq)) * ode
    resid = lhs - rhs
    return resid.is_zero(), len(resid.d)


def verify_naive_eta_fails(r, mu, L):
    """The nu>=2 formula q = eta * Rad * S at nu=1 is a DIFFERENT polynomial
    identity: dq would be r+L+1.  The absorbed identity with that q does
    not hold with rho = r mu / (r+L).  Used as a mutation that must fire.
    """
    n = 1 + r + L
    eta = Poly.var(n, 0)
    Rad = eta.pow(r)
    for j in range(r):
        Rad = Rad + Poly.var(n, 1 + j) * eta.pow(j)
    S = eta.pow(L)
    for j in range(L):
        S = S + Poly.var(n, 1 + r + j) * eta.pow(j)
    p = Rad.pow(mu)
    q_naive = eta * Rad * S
    rho_absorbed = Fr(r * mu, r + L)
    lhs = Poly.const(n, rho_absorbed) * p * q_naive.diff(0) - p.diff(0) * q_naive
    return (not lhs.is_zero())


# ---------------------------------------------------------------------------
# r = 2: unique monic S of degree L for any quadratic Rad.
# ---------------------------------------------------------------------------

def rref_solve(A, b):
    m = len(A)
    n = len(A[0]) if A else 0
    M = [A[i][:] + [b[i]] for i in range(m)]
    row = 0
    pivots = []
    for col in range(n):
        piv = None
        for r in range(row, m):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[row], M[piv] = M[piv], M[row]
        f = M[row][col]
        M[row] = [x / f for x in M[row]]
        for r in range(m):
            if r == row:
                continue
            if M[r][col] != 0:
                g = M[r][col]
                M[r] = [x - g * y for x, y in zip(M[r], M[row])]
        pivots.append(col)
        row += 1
        if row == m:
            break
    for r in range(row, m):
        if M[r][n] != 0:
            return None
    x = [Fr(0)] * n
    for i, col in enumerate(pivots):
        x[col] = M[i][n]
    return x


def solve_S(Rad, r, L):
    """Monic S of degree L with all positive-degree ODE coefficients zero."""
    cols = []
    for j in range(L):
        v = [Fr(0)] * (L + 1)
        v[j] = Fr(1)
        cols.append(ode_poly(Rad, v, r, L) + [Fr(0)] * (r + L - 1))
        cols[-1] = cols[-1][: r + L - 1]
    particular = ode_poly(Rad, [Fr(0)] * L + [Fr(1)], r, L) + [Fr(0)] * (r + L - 1)
    particular = particular[: r + L - 1]
    rows = list(range(1, r + L - 1))
    if not rows:
        S = [Fr(0)] * L + [Fr(1)]
        ok, C = ode_is_nonzero_constant(Rad, S, r, L)
        return S, C
    A = [[cols[j][d] if d < len(cols[j]) else Fr(0) for j in range(L)]
         for d in rows]
    b = [-(particular[d] if d < len(particular) else Fr(0)) for d in rows]
    sol = rref_solve(A, b)
    if sol is None:
        return None
    S = sol + [Fr(1)]
    got = ode_poly(Rad, S, r, L)
    if any(got[i] != 0 for i in range(1, len(got))):
        return None
    C = got[0] if got else Fr(0)
    return S, C


def r2_recurrence_S(L, A=Fr(2)):
    """Unique monic S for Rad = t^2 - A, from the exact recurrence.
    C = -2 L A s_1 / something: empirically C = -2 A * (coeff of t^{L-1} wait).
    For A=2, C = -4 s_1.
    """
    s = [Fr(0)] * (L + 1)
    s[L] = Fr(1)
    # (t^2 - A) S' - L t S = C/2   (because r=2)
    # recurrence on t^m, m = L .. 1:
    # (m-1-L) s_{m-1} - A (m+1) s_{m+1}  wait A=2 in t^2-2 uses -2 k s_k
    # General Rad=t^2-A: (t^2-A) S' - L t S = C/2
    # sum (k-L) s_k t^{k+1} - A sum k s_k t^{k-1} = C/2
    for m in range(L, 0, -1):
        rhs = A * (m + 1) * s[m + 1] if m + 1 <= L else Fr(0)
        den = m - 1 - L
        if m - 1 >= 0:
            if den == 0:
                if rhs != 0:
                    return None
            else:
                s[m - 1] = rhs / den
    C = -2 * A * s[1]   # C/2 = -A s_1  from t^0
    return s, C


def d9_residue_r2(n):
    """D9 / L1b: even L = 2n-2, residue of Rad^{-n} at a simple root of a
    squarefree quadratic, up to a nonzero (a1-a2) power, is
    (-1)^{n-1} binom(2n-2, n-1) != 0 for n >= 2.
    """
    return ((-1) ** (n - 1)) * comb(2 * n - 2, n - 1)


# ---------------------------------------------------------------------------
# Power family Rad = t^r - A, L = 1 + r k.
# ---------------------------------------------------------------------------

def power_S(r, k, A=Fr(1)):
    """S for Rad = t^r - A, L = 1 + r k.  Recurrence from
    (t^r - A) S' - L t^{r-1} S = C/r.
    Sparse: only degrees 1, 1+r, 1+2r, ..., 1+k r.
    """
    L = 1 + r * k
    s = [Fr(0)] * (L + 1)
    s[L] = Fr(1)
    # (t^r - A) sum m s_m t^{m-1} - L t^{r-1} sum s_m t^m = C/r
    # sum m s_m t^{m+r-1} - A sum m s_m t^{m-1} - L sum s_m t^{m+r-1} = C/r
    # sum (m - L) s_m t^{m+r-1} - A sum m s_m t^{m-1} = C/r
    # For degree d >= 1: (d-r+1 - L) s_{d-r+1}  - A (d+1) s_{d+1} = 0
    # i.e. if the first index is valid.
    for d in range(L + r - 2, 0, -1):
        i = d - r + 1
        j = d + 1
        coeff_i = (i - L) if 0 <= i <= L else None
        rhs = A * j * s[j] if j <= L else Fr(0)
        if coeff_i is None or coeff_i == 0:
            if i is not None and 0 <= i <= L and coeff_i == 0 and rhs != 0:
                return None
            continue
        if 0 <= i <= L:
            s[i] = rhs / coeff_i
    # C/r = -A * 1 * s_1   (t^0 from -A sum m s_m t^{m-1} at m=1)
    C = -A * r * s[1] if L >= 1 else Fr(0)
    return s, C, L


def dickson(n, alpha=Fr(1)):
    """Dickson D_n(x, alpha), low-to-high."""
    coef = [Fr(0)] * (n + 1)
    for i in range(n // 2 + 1):
        if n - i == 0:
            continue
        term = Fr(n, n - i) * comb(n - i, i) * ((-alpha) ** i)
        coef[n - 2 * i] += term
    return coef


# ---------------------------------------------------------------------------
# P1 terminal test.
# ---------------------------------------------------------------------------

def ceil_fr(x):
    x = Fr(x)
    return -((-x.numerator) // x.denominator)


def terminal_psi(w, M):
    if w >= 1 or w <= 0 or M < 2:
        return None
    j = M * (1 - w)
    if j.denominator != 1 or j < 1:
        return None
    return ceil_fr(Fr(M, int(j))) - 1


def fdiv(n):
    n = int(n)
    if n <= 0:
        return []
    out, d = [], 1
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            if d != n // d:
                out.append(n // d)
        d += 1
    return sorted(out)
