#!/usr/bin/env python3
"""Independent implementation of the closed coefficient-array recurrence for the
terminal rows T_{t,k} (charged: k16-terminal-proof-sol56-20260903.md Sec.2,
equations (2.1)-(2.13)), used ONLY to audit the structural claims about the
terminal tail T_{t,t..2t-1}:

   (S1) weighted homogeneity, deg_wp T_{t,k} = 4t+1-k;
   (S2) deg_b3 T_{t,2t-1-r} <= 2 for r=0..t-1  (top tail);
   (S3) [b3^2] T_{t,2t-1} = -alpha_t, a scalar (weight 0) in A_t;
   (S4) [b3^2] T_{t,2t-1-r} =: a_r is a weight-r form in b4,q_2..q_{r,0} only;
   (S5) the linearised tail  G_r = a_0 T_{t,2t-1-r} - a_r T_{t,2t-1}  is
        b3-LINEAR of weight 2t+2+r;
   (S6) at t=2, y=1/5: a_0=0 and b4 divides every tail row -> the b3-axis is in
        V(tail) -> dim 1.

Ring: A_t = Q[y]/(H_t), H_t = 12q^2 y^2 - 12q(t+1) y + (t+1)(3t+2), q=2t+1.
Every coefficient is reduced modulo H_t (degree <= 1 in y).
"""
import sys, json
import sympy as sp
from sympy import binomial as C

def build(t, verbose=True):
    q = 2 * t + 1
    e = 3 * t + 1
    y = sp.Symbol('y')
    H = 12 * q**2 * y**2 - 12 * q * (t + 1) * y + (t + 1) * (3 * t + 2)
    d = 2 * q * y - (t + 1)
    g = sp.Rational(1, 6) * e * t * (3 * d + 2 * (t + 1)) / q**3

    b4, b3, b2 = sp.symbols('b4 b3 b2')
    u = {i: sp.Symbol('u%d' % i) for i in range(2, 2 * t + 1)}      # u_2..u_2t
    c = {j: sp.Symbol('c%d' % j) for j in range(1, t)}              # c_1..c_{t-1}
    resid = [b4] + [u[i] for i in range(2, t)] + [b3]               # b4,q_2..q_{t-1},b3
    wt = {b4: 1, b3: t + 1, b2: 2 * t + 1}
    for i in u: wt[u[i]] = i
    for j in c: wt[c[j]] = j

    yinv = sp.Rational(6, 1) * q * ((t + 1) - d) / ((t + 1) * (3 * t + 2))   # 1/y in A_t

    def red(expr):
        """reduce coefficients mod H_t (deg_y <= 1) and expand"""
        expr = sp.expand(expr)
        p = sp.Poly(expr, y)
        r = sp.rem(p, sp.Poly(H, y))
        return sp.expand(r.as_expr())

    def inv_y_mul(expr, k=1):
        out = expr
        for _ in range(k):
            out = red(sp.expand(out * yinv))
        return out

    # ---- (2.2) arrays U_m, C_m -------------------------------------------
    U = {}
    for m in range(0, q + 1):
        s = C(q, m) * b4**(q - m)
        for i in range(2, 2 * t + 1):
            if q - i >= m: s += u[i] * C(q - i, m) * b4**(q - i - m)
        U[m] = sp.expand(s)
    Cc = {}
    for m in range(0, t):
        s = C(t - 1, m) * b4**(t - 1 - m)
        for j in range(1, t):
            if t - 1 - j >= m: s += c[j] * C(t - 1 - j, m) * b4**(t - 1 - j - m)
        Cc[m] = sp.expand(s)
    get = lambda D, i: D.get(i, sp.Integer(0))

    # ---- (2.3) B ----------------------------------------------------------
    B = {0: sp.Integer(0)}
    for m in range(0, t):
        B[m + 1] = red(inv_y_mul(g * (3 * m + 5) * get(Cc, m) / (2 * (m + 1))))

    # ---- (2.4) S ----------------------------------------------------------
    S = {}
    for m in range(0, 2 * t + 1):
        acc = 3 * g * (m + 1) * get(U, m + 1)
        for a in range(0, m):
            b = m - 1 - a
            acc += (3 + 2 * a - b) * get(Cc, a) * get(B, b)
        acc += (g * b3 / 2) * (5 * m + 7) * get(Cc, m)
        S[m] = red(inv_y_mul(acc / (2 * m + 1)))

    # ---- (2.7) V, Y, Z ----------------------------------------------------
    V, Y, Z = {}, {}, {}
    for m in range(0, t + 2): V[m] = red(get(Cc, m - 2) - (y * b3 if m == 0 else 0))
    for m in range(0, 2 * t + 2): Y[m] = red(get(S, m - 1) - b3 * get(B, m) - (g * b2 if m == 0 else 0))
    for m in range(0, t + 2): Z[m] = red(get(B, m - 1) - (g * b3 if m == 0 else 0))

    # ---- (2.7) N, P0', R --------------------------------------------------
    N = {}
    for m in range(0, 3 * t + 2):
        acc = 0
        for a in range(0, m + 1):
            b = m - a
            acc += -get(V, a) * (b + 1) * get(Y, b + 1)
            acc += (a + 1) * get(V, a + 1) * get(Y, b)
            acc += 2 * (a + 1) * get(U, a + 1) * get(Z, b)
        N[m] = red(acc)
    P0 = {}
    for r in range(0, 3 * t + 1): P0[r] = red(inv_y_mul(get(N, r + 1) / 2))
    R = {}
    for m in range(0, 4 * t + 2):
        acc = 0
        for a in range(0, m + 1):
            b = m - a
            acc += get(V, a) * get(P0, b) - (a + 1) * get(U, a + 1) * get(Y, b)
        if m == 0: acc -= y * g
        R[m] = red(acc)

    # ---- X-coefficients:  [X^k]R = sum_{m>=k} binom(m,k)(-b4)^{m-k} R_m ----
    def Xcoef(k, Rd):
        acc = 0
        for m in range(k, 4 * t + 2):
            acc += C(m, k) * (-b4)**(m - k) * Rd.get(m, 0)
        return red(acc)

    # ---- (2.9) triangular high solve, weights j=1..2t+1 -------------------
    zvar = {}
    for j in range(1, t): zvar[j] = c[j]
    for j in range(t, 2 * t + 1): zvar[j] = u[j]
    zvar[2 * t + 1] = b2
    sol = {}
    Rcur = dict(R)
    for j in range(1, 2 * t + 2):
        band = Xcoef(4 * t + 1 - j, Rcur)
        band = red(band.subs(sol)) if sol else band
        z = zvar[j]
        pol = sp.Poly(sp.expand(band), z)
        deg = pol.degree()
        assert deg <= 1, ("band not affine in z", j, deg)
        a1 = red(pol.nth(1)); a0 = red(pol.nth(0))
        val = red(sp.expand(-a0 * sp.simplify(1 / a1))) if a1.free_symbols - {y} else None
        if val is None:
            # a1 is a scalar in A_t: invert it in A_t = Q[y]/(H_t)
            inv = sp.invert(sp.Poly(a1, y), sp.Poly(H, y)) if sp.Poly(a1, y).degree() >= 1 else sp.Integer(1) / a1
            inv = inv.as_expr() if hasattr(inv, 'as_expr') else inv
            val = red(sp.expand(-a0 * inv))
        sol[z] = val
        if verbose: print(f"   solved z_{j} = {z}   (pivot deg_y {sp.Poly(a1,y).degree()})", flush=True)
    # substitute
    Rsub = {m: red(sp.expand(R[m].subs(sol))) for m in R}
    T = {}
    for k in range(0, 2 * t):
        T[k] = red(-Xcoef(k, Rsub))
    return dict(t=t, y=y, H=H, d=d, g=g, q=q, T=T, wt=wt, resid=resid, b3=b3, b4=b4, red=red, u=u)

def wdeg_check(expr, wt, b3, b4, resid):
    """return set of weighted degrees of monomials"""
    expr = sp.expand(expr)
    if expr == 0: return set()
    y = sp.Symbol('y')
    p = sp.Poly(expr, *resid)
    degs = set()
    for mono, co in zip(p.monoms(), p.coeffs()):
        w = sum(m * wt[v] for m, v in zip(mono, resid))
        degs.add(w)
    return degs

if __name__ == '__main__':
    t = int(sys.argv[1])
    print(f"=== t = {t} ===", flush=True)
    D = build(t)
    y, T, wt, resid, b3, b4, red = D['y'], D['T'], D['wt'], D['resid'], D['b3'], D['b4'], D['red']
    print("\nrow weighted-degree check (expect 4t+1-k):")
    for k in range(0, 2 * t):
        nonconst = sp.expand(T[k] - T[k].subs({v: 0 for v in resid}))
        degs = wdeg_check(nonconst, wt, b3, b4, resid)
        print(f"   T[{k}]  wdeg set = {sorted(degs)}   expected {4*t+1-k}   const={sp.simplify(T[k].subs({v:0 for v in resid}))}", flush=True)
    print("\ntop tail rows T_{t,2t-1-r}, r=0..t-1:")
    for r in range(0, t):
        k = 2 * t - 1 - r
        p = sp.Poly(sp.expand(T[k]), b3)
        print(f"   r={r} k={k}: deg_b3 = {p.degree()}   wdeg(expected)={2*t+2+r}", flush=True)
        a_r = red(p.nth(2)) if p.degree() >= 2 else sp.Integer(0)
        print(f"        a_{r} = [b3^2]T = {sp.factor(sp.simplify(a_r))}", flush=True)
    json.dump({'t': t}, open(f'/home/ubuntu/jc2/box/k16hsop-20260903/tail_t{t}_meta.json', 'w'))
