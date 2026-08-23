#!/usr/bin/env python3
"""Coefficient-level check of Prop 8.1(iv) (reduced pattern ODE) at two-pole
merge vertices and at the exhibit's suffix shapes (SHEET6-L1.md).

Reduced ODE (refs/sigray_full.pdf p. 39-41, Prop 8.1(iv)):
    delta * p * q' - (1-u) * p' * q = c * p,   c != 0.
Divide by (1-u), set rho := delta/(1-u); by top-cancellation (Cor 6.1 / case
(16)) rho = deg p / deg q. nu-equivariance: p = pt(t), q = eta^{e0} * w(t),
t = eta^nu (e0 = 1 iff nu >= 2, forced; e0 = 0 for nu = 1 root-free q...
nu=1 merged family has q = p*s, no eta factor forced).

Root law (derived, and used to correct the printed (II)(a)/(II)(b) patterns):
  - every root of p divides q with multiplicity EXACTLY 1;
  - roots of q not in p are simple;
  - at a root of p of p-mult m: rho != m (coefficient nonvanishing).

Families checked (exact arithmetic):
  A. merged mu=(1,1), k=0, nu>=2, l extra q-orbits:
       p = pt(t) = (t-a1)(t-a2),  q = eta * pt(t) * s(t), deg s = l,
       in t: E(t) := rho*pt*s + nu*rho*t*pt*s' + (rho-1)*nu*t*pt'*s = ctilde.
  B. merged nu=1, l extra simple q-roots: p = (e-a1)(e-a2), q = p*s:
       E := rho*p*s' + (rho-1)*p'*s = ctilde.
  C. single-pole suffix shape St 9.6(iii)(A) (mu=2, k=1, nu=7):
       p = pt = (t-A)^2 (t-B), q = eta * w(t), w = (t-A)(t-B) (rad form),
       E := rho*pt*w + nu*rho*t*pt*w' - nu*t*pt'*w = ctilde * pt.
     Also shows the PRINTED form q = eta*(t-A)^2-type is impossible (root law).
All solving is small linear algebra over Fraction after fixing the scaling.
"""
from fractions import Fraction as Fr

def pmul(a, b):
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return r

def padd(*ps):
    n = max(len(p) for p in ps)
    r = [Fr(0)] * n
    for p in ps:
        for i, x in enumerate(p):
            r[i] += x
    return r

def pscale(a, c): return [x * c for x in a]
def pderiv(a):    return [a[i] * i for i in range(1, len(a))]
def pshift(a):    return [Fr(0)] + list(a)          # multiply by t
def ptrim(a):
    while len(a) > 1 and a[-1] == 0: a = a[:-1]
    return a

def peval(a, x):
    r = Fr(0)
    for c in reversed(a): r = r * x + c
    return r

def merged_E(pt, s, nu, rho):
    """E = rho*pt*s + nu*rho*t*pt*s' + (rho-1)*nu*t*pt'*s (family A)."""
    t1 = pscale(pmul(pt, s), rho)
    t2 = pscale(pshift(pmul(pt, pderiv(s))), nu * rho) if len(s) > 1 else [Fr(0)]
    t3 = pscale(pshift(pmul(pderiv(pt), s)), (rho - 1) * nu)
    return ptrim(padd(t1, t2, t3))

def check_A_l1(nu):
    """Family A, l=1: pt = t^2 - sig*t + pi, s = t - b, rho = 2nu/(3nu+1).
    Coefficient equations (t^2, t^1 of E vanish) solved in closed form."""
    rho = Fr(2 * nu, 3 * nu + 1)
    sig = Fr(3)                                     # scaling gauge
    # t^2:  -rho(sig+b) - nu rho sig + nu(rho-1)(2b+sig)... solve linearly:
    # E2 = rho*(-(sig+b)) + nu*rho*(-sig) ... derive numerically instead:
    # unknowns (pi, b): solve the 2x2 linear system by elimination on a grid
    # of symbolic seeds -> here direct: E is linear in (pi, b) jointly? E2 is
    # linear in b (pi absent), E1 linear in (pi, sig*b). Do it exactly:
    # E2 coeff: rho*(coef) ... build with symbols via two-point interpolation.
    def E_coeffs(pi, b):
        pt = [pi, -sig, Fr(1)]
        s = [-b, Fr(1)]
        E = merged_E(pt, s, nu, rho)
        E += [Fr(0)] * (4 - len(E))
        return E
    # E2, E1 are affine in (pi, b): sample basis
    E00 = E_coeffs(Fr(0), Fr(0)); Ep = E_coeffs(Fr(1), Fr(0)); Eb = E_coeffs(Fr(0), Fr(1))
    # rows: [dE/dpi, dE/db, const] for degrees 2 and 1
    import itertools
    a11, a12, c1 = Ep[2] - E00[2], Eb[2] - E00[2], E00[2]
    a21, a22, c2 = Ep[1] - E00[1], Eb[1] - E00[1], E00[1]
    det = a11 * a22 - a12 * a21
    if det == 0: return None
    pi = (-c1 * a22 + c2 * a12) / det
    b  = (-a11 * c2 + a21 * c1) / det
    E = E_coeffs(pi, b)
    ok = (len(ptrim(E)) == 1)
    ct = E[0]
    # distinctness / nonvanishing
    disc = sig * sig - 4 * pi
    pt = [pi, -sig, Fr(1)]
    conds = dict(top_cancel=ok, ct_nonzero=(ct != 0), roots_distinct=(disc != 0),
                 roots_nonzero=(pi != 0), b_nonzero=(b != 0),
                 b_not_root=(peval(pt, b) != 0))
    return dict(nu=nu, rho=rho, sig=sig, pi=pi, b=b, ct=ct, **conds)

def check_A_general(nu, l):
    """Family A, general l: solve the linear system for (pi, b_1..b_l) with
    sig fixed (gauge). Unknown vector x = (pi, e_1..e_l) where s(t) =
    t^l + e_{l-1} t^{l-1} + ... (monic; e = elementary-symmetric signs).
    E has degrees l+2 .. 0; top auto-cancels; require t^{l+1}..t^1 = 0:
    l+1 equations, l+1 unknowns. Linear in (pi, s-coeffs) jointly? E is
    bilinear (pt has pi linearly; s linear in its coeffs) -> product terms
    pi*e_j appear: NOT linear. Solve by iterating: treat as linear in
    s-coeffs for fixed pi, then 1-d root-hunt in pi over Q via the last
    equation's numerator (rational function of pi -> polynomial)."""
    rho = Fr(2 * nu, (l + 2) * nu + 1)
    sig = Fr(3)
    def sys_for_pi(pi):
        # unknowns: s coeffs e_0..e_{l-1} (monic s). Equations: E_{l+1}..E_1.
        # Build E for basis vectors.
        def E_of(svec):
            pt = [pi, -sig, Fr(1)]
            s = list(svec) + [Fr(1)]
            E = merged_E(pt, s, nu, rho)
            E += [Fr(0)] * (l + 3 - len(E))
            return E
        base = E_of([Fr(0)] * l)
        cols = []
        for j in range(l):
            v = [Fr(0)] * l; v[j] = Fr(1)
            cols.append([a - b for a, b in zip(E_of(v), base)])
        # rows for degrees l+1 .. 1  (l+1 rows), unknowns l -> overdetermined
        # by 1 for fixed pi; solve top l rows, return residual of last row.
        rows = list(range(l + 1, 0, -1))
        A = [[cols[j][d] for j in range(l)] for d in rows]
        bvec = [-base[d] for d in rows]
        # Gaussian elimination on first l rows
        M = [row[:] + [bv] for row, bv in zip(A[:l], bvec[:l])]
        n = l
        for i in range(n):
            piv = next((r for r in range(i, n) if M[r][i] != 0), None)
            if piv is None: return None
            M[i], M[piv] = M[piv], M[i]
            for r in range(n):
                if r != i and M[r][i] != 0:
                    f = M[r][i] / M[i][i]
                    M[r] = [a - f * b for a, b in zip(M[r], M[i])]
        sol = [M[i][n] / M[i][i] for i in range(n)]
        res = sum(A[l][j] * sol[j] for j in range(l)) - bvec[l]
        return sol, res
    # residual as function of pi: rational; find rational roots by scanning a
    # polynomial fit: sample l+3 points, interpolate numerator via differences.
    # Simpler: scan a modest rational grid and also solve res(pi)=0 by
    # bisection-free exact interpolation (res is a rational function; its
    # numerator is a polynomial of low degree in pi). Sample and interpolate:
    pts = []
    for num in range(-40, 41):
        pi = Fr(num, 6)
        if pi == 0: continue
        out = sys_for_pi(pi)
        if out is None: continue
        sol, res = out
        pts.append((pi, res, sol))
        if res == 0:
            s = sol + [Fr(1)]
            pt = [pi, -sig, Fr(1)]
            return dict(nu=nu, l=l, rho=rho, pi=pi, s=s,
                        disc=sig * sig - 4 * pi,
                        note="exact-solution-on-grid")
    # Lagrange-interpolate numerator of res * common denominator: assume res
    # is polynomial of degree <= l+2 in pi (empirically true: pt linear in pi)
    n = min(len(pts), l + 4)
    xs = [p[0] for p in pts[:n]]; ys = [p[1] for p in pts[:n]]
    # Newton divided differences -> coefficients
    coef = ys[:]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (xs[i] - xs[i - j])
    # expand Newton form
    poly = [Fr(0)] * n
    acc = [Fr(1)]
    for j in range(n):
        for i, a in enumerate(acc):
            poly[i] += coef[j] * a
        acc = ptrim(padd(pshift(acc), pscale(acc, -xs[j])))
    poly = ptrim(poly)
    # rational root scan of poly (root = admissible pi)
    roots = []
    den = 1
    for c in poly: den = den * c.denominator // __import__('math').gcd(den, c.denominator) if c.denominator else den
    ipoly = [c * den for c in poly]
    lead = ipoly[-1]; const = ipoly[0]
    if const == 0: roots.append(Fr(0))
    def divs(n):
        n = abs(int(n)); return [d for d in range(1, n + 1) if n % d == 0] or [1]
    if const != 0 and lead != 0:
        for pn in divs(const.numerator if isinstance(const, Fr) else const):
            for qn in divs(lead.numerator if isinstance(lead, Fr) else lead):
                for sgn in (1, -1):
                    r = Fr(sgn * pn, qn)
                    if peval(poly, r) == 0: roots.append(r)
    roots = sorted(set(r for r in roots if r != 0))
    sols = []
    for pi in roots:
        out = sys_for_pi(pi)
        if out is None: continue
        sol, res = out
        if res != 0: continue
        s = sol + [Fr(1)]
        sols.append(dict(nu=nu, l=l, rho=rho, pi=pi, s=s, disc=sig * sig - 4 * pi))
    return dict(nu=nu, l=l, rho=rho, poly_deg=len(poly) - 1,
                rational_pi_solutions=sols)

def check_B(l):
    """Family B (nu=1): p = e^2 - sig e + pi, q = p*s, s monic deg l.
    E := rho*p*s' + (rho-1)*p'*s = ctilde, rho = 2/(2+l).
    Underdetermined (l unknowns-ish vs l constraints with 2 gauge dims);
    exhibit one exact solution with distinct nonzero roots."""
    rho = Fr(2, 2 + l)
    sig = Fr(3)
    # unknowns: pi and s-coeffs e_0..e_{l-1}; equations: deg l..1 of E vanish
    # (top auto-cancels), i.e. l equations, l+1 unknowns -> pick e_0 free.
    # Solve linearly in (pi, e_1..e_{l-1}) for sampled e_0 until distinctness.
    def E_of(pi, svec):
        p = [pi, -sig, Fr(1)]
        s = list(svec) + [Fr(1)]
        t1 = pscale(pmul(p, pderiv(s)), rho) if l >= 1 else [Fr(0)]
        t2 = pscale(pmul(pderiv(p), s), rho - 1)
        E = ptrim(padd(t1, t2))
        E += [Fr(0)] * (l + 2 - len(E))
        return E
    for e0num in range(1, 60):
        e0 = Fr(e0num, 4)
        # linear in x = (pi, e_1..e_{l-1}): sample basis
        m = l  # unknowns count
        def build(x):
            pi = x[0]; sv = [e0] + list(x[1:]) + []
            return E_of(pi, sv)
        base = build([Fr(0)] * m)
        cols = []
        for j in range(m):
            v = [Fr(0)] * m; v[j] = Fr(1)
            cols.append([a - b for a, b in zip(build(v), base)])
        rows = list(range(l, 0, -1))
        A = [[cols[j][d] for j in range(m)] for d in rows]
        bv = [-base[d] for d in rows]
        M = [row[:] + [c] for row, c in zip(A, bv)]
        sing = False
        for i in range(m):
            piv = next((r for r in range(i, m) if M[r][i] != 0), None)
            if piv is None: sing = True; break
            M[i], M[piv] = M[piv], M[i]
            for r in range(m):
                if r != i and M[r][i] != 0:
                    f = M[r][i] / M[i][i]
                    M[r] = [a - f * b for a, b in zip(M[r], M[i])]
        if sing: continue
        x = [M[i][m] / M[i][i] for i in range(m)]
        pi = x[0]; s = [e0] + list(x[1:]) + [Fr(1)]
        E = E_of(pi, [e0] + list(x[1:]))
        if len(ptrim(E)) != 1 or E[0] == 0: continue
        p = [pi, -sig, Fr(1)]
        disc = sig * sig - 4 * pi
        if disc == 0 or pi == 0: continue
        # s roots distinct from p's and nonzero: check resultant-ish via gcd
        # crude check: s(a_i) != 0 via evaluating s at p's roots symbolically:
        # res(p, s) != 0  <=>  s shares no root with p.
        def presultant(pp, ss):
            # Sylvester determinant, tiny sizes
            n1, n2 = len(pp) - 1, len(ss) - 1
            N = n1 + n2
            rowsS = []
            for i in range(n2):
                rowsS.append([Fr(0)] * i + list(reversed(pp)) + [Fr(0)] * (n2 - 1 - i))
            for i in range(n1):
                rowsS.append([Fr(0)] * i + list(reversed(ss)) + [Fr(0)] * (n1 - 1 - i))
            # determinant
            Mm = [r[:] for r in rowsS]
            det = Fr(1)
            for i in range(N):
                piv = next((r for r in range(i, N) if Mm[r][i] != 0), None)
                if piv is None: return Fr(0)
                if piv != i:
                    Mm[i], Mm[piv] = Mm[piv], Mm[i]; det = -det
                det *= Mm[i][i]
                for r in range(i + 1, N):
                    if Mm[r][i] != 0:
                        f = Mm[r][i] / Mm[i][i]
                        Mm[r] = [a - f * b for a, b in zip(Mm[r], Mm[i])]
            return det
        if presultant(p, s) == 0: continue
        if s[0] == 0: continue          # 0 a root of s -> q vanishes doubly at 0? (b_j != 0)
        # s squarefree?
        if presultant(s, pderiv(s)) == 0: continue
        return dict(l=l, rho=rho, sig=sig, pi=pi, s=s, ct=E[0], disc=disc)
    return dict(l=l, rho=rho, note="no solution found on scan grid")

def interp_poly(xs, ys):
    """Exact Newton interpolation -> coefficient list (low->high)."""
    coef = ys[:]
    n = len(xs)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (xs[i] - xs[i - j])
    poly = [Fr(0)]
    acc = [Fr(1)]
    for j in range(n):
        poly = ptrim(padd(poly, pscale(acc, coef[j])))
        acc = ptrim(padd(pshift(acc), pscale(acc, -xs[j])))
    return ptrim(poly)

def pgcd(a, b):
    """Polynomial gcd over Q (monic)."""
    a, b = ptrim(a[:]), ptrim(b[:])
    while len(b) > 1 or (len(b) == 1 and b[0] != 0):
        if len(b) == 1: return [Fr(1)]
        # a mod b
        r = a[:]
        while len(r) >= len(b) and any(x != 0 for x in r):
            r = ptrim(r)
            if len(r) < len(b): break
            f = r[-1] / b[-1]
            sh = len(r) - len(b)
            r = ptrim([rc - f * (b[i - sh] if 0 <= i - sh < len(b) else Fr(0))
                       for i, rc in enumerate(r)])
            if len(r) == 1 and r[0] == 0: break
        a, b = b, r
        if len(b) == 1 and b[0] == 0: break
    a = ptrim(a)
    return [c / a[-1] for c in a] if a[-1] != 0 else a

def check_C_suffix(nu=7, rho=Fr(7, 5)):
    """St 9.6(iii)(A) single-pole shape (the exhibit suffix / St 9.7 parent):
    nu=7, p = pt = (t-A)^2(t-B), q = eta*w, w = (t-A)(t-B) (forced by the
    root law + deg q = 2nu+1).  CORRECT unreduced-in-pt equation:
        E := rho*pt*w + nu*rho*t*pt*w' - nu*t*pt'*w = ctilde * pt.
    Gauge A = 1; unknown B; E deg 5, pt deg 3: conditions: E5(auto?), E4 = 0,
    and E - ct*pt = 0 for deg 2,1,0 with ct := E3 - ... (careful: E=ct*pt
    componentwise).  We interpolate each residual as a polynomial in B and
    take the gcd -> common roots over C."""
    A = Fr(1)
    def E_of(B):
        pt = pmul(pmul([-A, Fr(1)], [-A, Fr(1)]), [-B, Fr(1)])
        w = pmul([-A, Fr(1)], [-B, Fr(1)])
        t1 = pscale(pmul(pt, w), rho)
        t2 = pscale(pshift(pmul(pt, pderiv(w))), nu * rho)
        t3 = pscale(pshift(pmul(pderiv(pt), w)), -nu)
        E = padd(t1, t2, t3)
        E += [Fr(0)] * (6 - len(E))
        return E, pt
    # residuals: r5 = E5, r4 = E4, and with ct := E3/pt3 (pt3=1): rj = Ej - ct*ptj
    samples = [Fr(k, 1) for k in range(-9, 10)] + [Fr(k, 2) for k in range(-9, 10, 2)]
    samples = [B for B in samples if B not in (A,)]
    data = {j: ([], []) for j in (5, 4, 2, 1, 0)}
    for B in samples[:14]:
        E, pt = E_of(B)
        ct = E[3]                       # pt monic deg 3
        res = {5: E[5], 4: E[4], 2: E[2] - ct * pt[2],
               1: E[1] - ct * pt[1], 0: E[0] - ct * pt[0]}
        for j in data:
            data[j][0].append(B); data[j][1].append(res[j])
    polys = {j: interp_poly(xs, ys) for j, (xs, ys) in data.items()}
    live = [p for p in polys.values() if not (len(p) == 1 and p[0] == 0)]
    if not live:
        return dict(nu=nu, rho=rho, verdict="ALL residuals identically 0: "
                    "B free (1-parameter family)")
    g = live[0]
    for p in live[1:]:
        g = pgcd(g, p)
    return dict(nu=nu, rho=rho,
                residual_polys={j: [str(c) for c in p] for j, p in polys.items()},
                common_gcd=[str(c) for c in g],
                verdict=("SOLVABLE over C: common roots exist (deg gcd = %d)"
                         % (len(g) - 1)) if len(g) > 1 else
                        "NO common root: pattern coefficient-IMPOSSIBLE")

def check_ZCH(nu, l):
    """Zero-chain merge family: p = eta*pt, pt = t - a (gauge a=1),
    q = eta*pt*s, deg s = l; dividing 8.1(iv) by eta*pt:
        E := (rho-1)*pt*s + (rho-1)*nu*t*pt'*s + rho*nu*t*pt*s' = ctilde,
    rho = (nu+1)/((l+1)nu+1); M = gcd(nu+1, l).  Balanced linear system in
    the monic s-coefficients; solve exactly."""
    rho = Fr(nu + 1, (l + 1) * nu + 1)
    a = Fr(1)
    pt = [-a, Fr(1)]
    def E_of(svec):
        s = list(svec) + [Fr(1)]
        t1 = pscale(pmul(pt, s), rho - 1)
        t2 = pscale(pshift(pmul(pderiv(pt), s)), (rho - 1) * nu)
        t3 = pscale(pshift(pmul(pt, pderiv(s))), rho * nu) if l >= 1 else [Fr(0)]
        E = padd(t1, t2, t3)
        E += [Fr(0)] * (l + 2 - len(E))
        return E
    base = E_of([Fr(0)] * l)
    cols = []
    for j in range(l):
        v = [Fr(0)] * l; v[j] = Fr(1)
        cols.append([x - y for x, y in zip(E_of(v), base)])
    rows = list(range(l + 1, 0, -1))          # t^{l+1} (auto 0) .. t^1
    A = [[cols[j][d] for j in range(l)] for d in rows[1:]]
    bv = [-base[d] for d in rows[1:]]
    M = [r[:] + [c] for r, c in zip(A, bv)]
    for i in range(l):
        piv = next((r for r in range(i, l) if M[r][i] != 0), None)
        if piv is None: return dict(nu=nu, l=l, note="singular")
        M[i], M[piv] = M[piv], M[i]
        for r in range(l):
            if r != i and M[r][i] != 0:
                f = M[r][i] / M[i][i]
                M[r] = [x - f * y for x, y in zip(M[r], M[i])]
    sol = [M[i][l] / M[i][i] for i in range(l)]
    E = E_of(sol)
    s = sol + [Fr(1)]
    ok = len(ptrim(E)) == 1 and E[0] != 0
    sq = peval(s, a) != 0 and s[0] != 0
    from math import gcd as _g
    return dict(nu=nu, l=l, rho=rho, M=_g(nu + 1, (l + 1) * nu + 1), s=[str(c) for c in s],
                const_ok=ok, ct=str(E[0]), s_avoids_pt_and_0=sq,
                top_residual=str(base and E[l + 1]))

def check_B_eta(l):
    """nu=1 merged, e0=1 variant: q = eta*pt*st, deg st = l-1 (0 among the
    l extra simple roots).  Same form as family A with nu=1:
        rho*pt*st + rho*t*pt*st' + (rho-1)*t*pt'*st = ctilde, rho = 2/(2+l).
    l=2 (st deg 1): hand-solved -> b = sig and pi = 0 forced (both fatal).
    General: solve linearly as in check_A_l1/check_A_general."""
    rho = Fr(2, 2 + l)
    if l == 2:
        # closed form (hand-verified): E2 = (b-sig)/? ... redo numerically:
        sig = Fr(3)
        def E_of(pi, b):
            pt = [pi, -sig, Fr(1)]
            st = [-b, Fr(1)]
            return merged_E(pt, st, 1, rho)
        E00, Ep, Eb = E_of(Fr(0), Fr(0)), E_of(Fr(1), Fr(0)), E_of(Fr(0), Fr(1))
        E00 += [Fr(0)] * (4 - len(E00)); Ep += [Fr(0)] * (4 - len(Ep))
        Eb += [Fr(0)] * (4 - len(Eb))
        a11, a12, c1 = Ep[2] - E00[2], Eb[2] - E00[2], E00[2]
        a21, a22, c2 = Ep[1] - E00[1], Eb[1] - E00[1], E00[1]
        det = a11 * a22 - a12 * a21
        if det == 0:
            return dict(l=l, note="singular linear system")
        pi = (-c1 * a22 + c2 * a12) / det
        b = (-a11 * c2 + a21 * c1) / det
        fatal = []
        if pi == 0: fatal.append("pi=0 (a chain direction at 0 AND ...)")
        pt = [pi, -sig, Fr(1)]
        if peval(pt, b) == 0: fatal.append("b is a root of p (mult(q)=2, root law)")
        return dict(l=l, rho=rho, pi=pi, b=b, fatal=fatal or None)
    return dict(l=l, note="use check_A_general(nu=1, l-1) machinery manually")

if __name__ == "__main__":
    print("== FAMILY A: merged mu=(1,1), k=0, l=1 (exhibit family) ==")
    for nu in (3, 5, 7, 9):
        r = check_A_l1(nu)
        print(f"  nu={nu}: {r}")
    print("\n== FAMILY A: merged, general l (rational-pi solutions) ==")
    for (nu, l) in ((3, 3), (5, 1), (5, 3), (7, 1), (3, 5)):
        r = check_A_general(nu, l)
        if 'rational_pi_solutions' in r:
            print(f"  nu={nu} l={l}: poly_deg={r['poly_deg']} "
                  f"sols={len(r['rational_pi_solutions'])}")
            for s in r['rational_pi_solutions'][:2]:
                print(f"     pi={s['pi']} s={[str(x) for x in s['s']]} disc={s['disc']}")
        else:
            print(f"  nu={nu} l={l}: {r.get('note')} pi={r.get('pi')} "
                  f"s={[str(x) for x in r.get('s', [])]}")
    print("\n== FAMILY B: merged nu=1 (I-like), l extra simple q-roots ==")
    print("  e0=0 (q = p*s): PROVED EMPTY by Wronskian/log argument:")
    print("   rho*p*s' + (rho-1)*p's = ct, rho=2/(2+l)  <=>  2ps' - l p's = ct'")
    print("   <=> (s/p^{l/2})' = (ct'/2) p^{-(l+2)/2}; partial fractions of the")
    print("   RHS have nonzero 1/(t-a_i) residues -> log terms -> ct'=0 forced,")
    print("   but ct != 0 (Prop 8.1(iv) RHS nonzero). l=2 direct: ps'-p's const")
    print("   => (ps'-p's)' = 2(p-s) = 0 => s=p, sharing roots: contradiction.")
    for l in (2, 4):
        r = check_B(l)
        print(f"  e0=0 numeric scan l={l}: {r.get('note', r)}")
    print("  e0=1 (q = eta*p*st):")
    for l in (2,):
        print(f"   l={l}: {check_B_eta(l)}")
    r = check_A_general(1, 3)   # e0=1, l=4 <=> family-A form nu=1, st deg 3
    print(f"   l=4 (st deg 3 <=> A-machinery nu=1,l=3): "
          f"{r if 'note' in r else dict(poly_deg=r['poly_deg'], sols=len(r['rational_pi_solutions']))}")
    print("\n== FAMILY Z: zero-chain merges p = eta(eta^nu - c^nu) ==")
    for (nu, l) in ((3, 2), (2, 3), (5, 2), (2, 1)):
        print(f"  nu={nu} l={l}: {check_ZCH(nu, l)}")
    print("\n== FAMILY C: single-pole suffix shape 9.6(iii)(A) nu=7 mu=2 k=1 ==")
    print("  ", check_C_suffix())
    print("\n(printed (II)(a)/(II)(b) q with chain orbit SQUARED fails the root")
    print(" law: every root of p divides q with mult exactly 1 -- else in")
    print(" delta*p*q' - (1-u)*p'*q = c*p the LHS order at the root exceeds the")
    print(" RHS order.  Cross-check: the thesis's own ratio deg p/deg q = 21/15")
    print(" for 9.6(iii)(A) forces q = eta*(t-A)(t-B), i.e. eta*rad(p): ERRATUM.)")
