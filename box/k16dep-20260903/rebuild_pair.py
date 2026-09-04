#!/usr/bin/env python3
"""Rebuild the actual ansatz pair (Q,P) in K[gamma,pi] of the normalized K=16 chart at a
numeric residual point (b3,b4,q_2..q_{t-1}) on a fixed fibre y of H_t, by replaying the proved
Laurent/Euler spine (Sol 17(qqq) sec.5-6 / Fable k16-terminal-proof sec.2, driver laurent_spine.py)
in exact field arithmetic (Fraction for a rational fibre, GF(p) for a modular root), and compute
J(Q,P) = Q_gamma P_pi - Q_pi P_gamma DIRECTLY by differentiation of the bivariate polynomials.

Chart (frozen t_order_system.py): z = pi - gamma, B = pi z + b1 pi + b2, A = pi B + b3,
h = pi A + b4;  Q = U(h) + A R(h) + y B,  P = V(h) + A S(h) + B T(h) + g z  (Sol 17(qqq) (2.1)).
Sign convention: T_{t,k} = -[X^k] R_s (rows), E(h) = sum_k T_{t,k} h^k.
Prediction re-derived in this lane:  J(Q,P) = c*gamma + pi*E(h)  with c = -y g.
"""
import argparse, json, random, sys
from fractions import Fraction

# ---------------- field ----------------
class Fld:
    def __init__(self, p=None):
        self.p = p
    def el(self, a):
        if self.p is None:
            return Fraction(a)
        return int(a) % self.p
    def add(self, a, b): return (a + b) if self.p is None else (a + b) % self.p
    def sub(self, a, b): return (a - b) if self.p is None else (a - b) % self.p
    def mul(self, a, b): return (a * b) if self.p is None else (a * b) % self.p
    def inv(self, a):
        if self.p is None:
            if a == 0: raise ZeroDivisionError("inverse of 0 in Q")
            return Fraction(1) / a
        a %= self.p
        if a == 0: raise ZeroDivisionError("inverse of 0 mod p")
        return pow(a, -1, self.p)
    def div(self, a, b): return self.mul(a, self.inv(b))
    def iszero(self, a): return (a == 0) if self.p is None else (a % self.p == 0)
    def frac(self, n, d): return self.div(self.el(n), self.el(d))

# ---------------- univariate dense polys over F (variable s) ----------------
def ptrim(F, f):
    while f and F.iszero(f[-1]): f.pop()
    return f
def padd(F, f, g):
    n = max(len(f), len(g)); r = [F.el(0)] * n
    for i, a in enumerate(f): r[i] = F.add(r[i], a)
    for i, a in enumerate(g): r[i] = F.add(r[i], a)
    return ptrim(F, r)
def psub(F, f, g): return padd(F, f, pscale(F, g, F.el(-1)))
def pscale(F, f, a): return ptrim(F, [F.mul(a, x) for x in f])
def pmul(F, f, g):
    if not f or not g: return []
    r = [F.el(0)] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        if F.iszero(a): continue
        for j, b in enumerate(g):
            r[i + j] = F.add(r[i + j], F.mul(a, b))
    return ptrim(F, r)
def pderiv(F, f): return ptrim(F, [F.mul(F.el(i), f[i]) for i in range(1, len(f))])
def pint(F, f, const):  # antiderivative with given constant
    r = [const] + [F.div(f[i], F.el(i + 1)) for i in range(len(f))]
    return ptrim(F, r)
def pcoef(F, f, k): return f[k] if k < len(f) else F.el(0)
def pshift(F, f, a):  # f(s + a)
    r = []
    for cf in reversed(f):
        r = padd(F, pmul(F, r, [a, F.el(1)]), [cf])
    return r
def pmono(F, k, cf=None): return ptrim(F, [F.el(0)] * k + [F.el(1) if cf is None else cf])
def pdivs(F, f):  # f / s, asserting f(0)=0
    assert not f or F.iszero(f[0]), "not divisible by s"
    return ptrim(F, f[1:])
def peval_dict(F, f, Ldict):  # f(L) with L a bivariate dict, Horner
    r = {}
    for cf in reversed(f):
        r = dadd(F, dmul(F, r, Ldict), dconst(F, cf))
    return r

# ---------------- bivariate dict polys over F: key (i,j) = gamma^i pi^j ----------------
def dtrim(F, d): return {k: v for k, v in d.items() if not F.iszero(v)}
def dconst(F, a): return dtrim(F, {(0, 0): F.el(a)})
def dadd(F, d1, d2):
    r = dict(d1)
    for k, v in d2.items(): r[k] = F.add(r.get(k, F.el(0)), v)
    return dtrim(F, r)
def dscale(F, d, a): return dtrim(F, {k: F.mul(a, v) for k, v in d.items()})
def dmul(F, d1, d2):
    r = {}
    for (i1, j1), v1 in d1.items():
        for (i2, j2), v2 in d2.items():
            k = (i1 + i2, j1 + j2); r[k] = F.add(r.get(k, F.el(0)), F.mul(v1, v2))
    return dtrim(F, r)
def dgamma(F, d): return dtrim(F, {(i - 1, j): F.mul(F.el(i), v) for (i, j), v in d.items() if i > 0})
def dpi(F, d): return dtrim(F, {(i, j - 1): F.mul(F.el(j), v) for (i, j), v in d.items() if j > 0})
def dstr(F, d, maxterms=12):
    items = sorted(d.items(), key=lambda kv: (-(kv[0][0] + kv[0][1]), -kv[0][0]))
    out = []
    for (i, j), v in items[:maxterms]:
        out.append("(%s)*gamma^%d*pi^%d" % (v, i, j))
    return " + ".join(out) + (" + ...[%d terms]" % len(d) if len(d) > maxterms else "")

# ---------------- the spine at a point ----------------
def spine_eval(F, t, y, pt, vals, B0):
    """Replay of laurent_spine.py at numeric data. Returns dict of all pieces (polys in s=L=X-b4)."""
    q, e = 2 * t + 1, 3 * t + 1
    b3, b4 = pt["b3"], pt["b4"]
    one = F.el(1)
    g1 = F.frac(e, q)
    g2 = F.add(F.mul(F.frac(e, q), y), F.frac(e * t, 2 * q * q))
    g = F.sub(F.mul(F.frac(e * t, q * q), y), F.frac(e * t * (t + 1), 6 * q ** 3))
    c = F.mul(F.el(-1), F.mul(y, g))
    sb4 = [b4, one]  # s + b4
    def spow(n):
        r = [one]
        for _ in range(n): r = pmul(F, r, sb4)
        return r
    U = spow(q)
    for i in range(2, 2 * t + 1):
        ui = pt["q%d" % i] if i < t else vals["u%d" % i]
        U = padd(F, U, pscale(F, spow(q - i), ui))
    Cp = spow(t - 1)
    for j in range(1, t):
        Cp = padd(F, Cp, pscale(F, spow(t - 1 - j), vals["c%d" % j]))
    A = pmul(F, [F.el(0), one], Cp)  # s*Cp  (= R = L C)
    s = [F.el(0), one]
    Bp = pscale(F, padd(F, pscale(F, Cp, F.el(5)), pscale(F, pmul(F, s, pderiv(F, Cp)), F.el(3))), F.div(g, F.mul(F.el(2), y)))
    B = pint(F, Bp, B0)
    assert F.iszero(F.sub(pcoef(F, B, t), g2)), "B leading coefficient != g2"
    Up = pderiv(F, U)
    rhsD = pscale(F, Up, F.mul(F.el(3), g))
    rhsD = padd(F, rhsD, pmul(F, A, B))
    rhsD = psub(F, rhsD, pmul(F, pmul(F, s, A), pderiv(F, B)))
    rhsD = padd(F, rhsD, pscale(F, pmul(F, pmul(F, s, pderiv(F, A)), B), F.el(2)))
    rhsD = padd(F, rhsD, pscale(F, padd(F, Cp, pscale(F, pderiv(F, A), F.frac(5, 2))), F.mul(g, b3)))
    D = ptrim(F, [F.div(rhsD[m], F.mul(y, F.el(2 * m + 1))) for m in range(len(rhsD))])
    assert F.iszero(F.sub(pcoef(F, D, 2 * t), g1)), "D leading coefficient != g1"
    b2 = vals["b2"]
    Q1 = psub(F, pmul(F, s, A), [F.mul(y, b3)])           # s A - y b3
    Y = psub(F, psub(F, pmul(F, s, D), pscale(F, B, b3)), [F.mul(g, b2)])  # s D - b3 B - g b2
    Z = psub(F, pmul(F, s, B), [F.mul(g, b3)])            # s B - g b3
    N = padd(F, psub(F, pmul(F, pderiv(F, Q1), Y), pmul(F, Q1, pderiv(F, Y))), pscale(F, pmul(F, Up, Z), F.el(2)))
    N0 = pcoef(F, N, 0)
    b1 = F.div(F.mul(F.el(-1), N0), F.mul(y, g))          # y g b1 + N(0) = 0
    num = padd(F, N, [F.mul(F.mul(y, g), b1)])
    Xp = pscale(F, pdivs(F, num), F.div(one, F.mul(F.el(2), y)))   # P0'
    assert F.iszero(F.sub(pcoef(F, Xp, 3 * t), F.el(e))), "Xp leading != e"
    Rs = psub(F, psub(F, pmul(F, Q1, Xp), pmul(F, Up, Y)), [F.mul(y, g)])
    RX = pshift(F, Rs, F.mul(F.el(-1), b4))               # R as polynomial in X = s + b4
    return dict(U=U, Cp=Cp, A=A, B=B, D=D, Q1=Q1, Y=Y, Z=Z, Xp=Xp, Rs=Rs, RX=RX, b1=b1, b2=b2,
                g=g, g1=g1, g2=g2, c=c, Up=Up)

def solve_point(F, t, y, pt, B0):
    q = 2 * t + 1
    order = [("c%d" % j) for j in range(1, t)] + [("u%d" % j) for j in range(t, 2 * t + 1)] + ["b2"]
    vals = {v: F.el(0) for v in order}
    pivots = []
    for j, var in enumerate(order, start=1):
        band = 4 * t + 1 - j
        v0 = dict(vals); v0[var] = F.el(0)
        v1 = dict(vals); v1[var] = F.el(1)
        v2 = dict(vals); v2[var] = F.el(2)
        r0 = pcoef(F, spine_eval(F, t, y, pt, v0, B0)["RX"], band)
        r1 = pcoef(F, spine_eval(F, t, y, pt, v1, B0)["RX"], band)
        r2 = pcoef(F, spine_eval(F, t, y, pt, v2, B0)["RX"], band)
        piv = F.sub(r1, r0)
        assert F.iszero(F.sub(F.sub(r2, r0), F.mul(F.el(2), piv))), "row not affine in %s" % var
        if F.iszero(piv): raise ZeroDivisionError("zero pivot at %s" % var)
        vals[var] = F.div(F.mul(F.el(-1), r0), piv)
        pivots.append((band, var, piv, vals[var]))
    S = spine_eval(F, t, y, pt, vals, B0)
    RX = S["RX"]
    for k in range(2 * t, 4 * t + 2):
        assert F.iszero(pcoef(F, RX, k)), "high band %d survives" % k
    T = [F.mul(F.el(-1), pcoef(F, RX, k)) for k in range(2 * t)]
    return S, vals, pivots, T

def build_pair(F, t, y, pt, S, vals):
    b3, b4 = pt["b3"], pt["b4"]; b1, b2, g = S["b1"], S["b2"], S["g"]
    one = F.el(1); m1 = F.el(-1)
    Ld = dtrim(F, {(0, 4): one, (1, 3): m1, (0, 3): b1, (0, 2): b2, (0, 1): b3})
    Ad = dtrim(F, {(0, 3): one, (1, 2): m1, (0, 2): b1, (0, 1): b2, (0, 0): b3})
    Bd = dtrim(F, {(0, 2): one, (1, 1): m1, (0, 1): b1, (0, 0): b2})
    zd = dtrim(F, {(0, 1): one, (1, 0): m1})
    hd = dadd(F, Ld, dconst(F, b4))
    # sanity: h = pi*A + b4, A = pi*B + b3, B = pi*z + b1*pi + b2
    pid = {(0, 1): one}
    assert dadd(F, dmul(F, pid, Ad), dconst(F, b4)) == hd
    assert dadd(F, dmul(F, pid, Bd), dconst(F, b3)) == Ad
    assert dadd(F, dadd(F, dmul(F, pid, zd), dscale(F, pid, b1)), dconst(F, b2)) == Bd
    Vs = pint(F, S["Xp"], F.mul(g, b1))   # V = P0 + g b1, P0 = int P0'
    Q = dadd(F, dadd(F, peval_dict(F, S["U"], Ld), dmul(F, Ad, peval_dict(F, S["A"], Ld))), dscale(F, Bd, y))
    P = dadd(F, dadd(F, dadd(F, peval_dict(F, Vs, Ld), dmul(F, Ad, peval_dict(F, S["D"], Ld))),
                     dmul(F, Bd, peval_dict(F, S["B"], Ld))), dscale(F, zd, g))
    return Q, P, hd, Ld

def laurent_identities(F, t, S):
    """D0..D4 of Sol (2.3) as polys in s, from the rebuilt pieces."""
    s = [F.el(0), F.el(1)]; g = S["g"]; y_ = None
    Q1, Up, Y, Z, Xp = S["Q1"], S["Up"], S["Y"], S["Z"], S["Xp"]
    return Q1, Up, Y, Z, Xp

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("t", type=int)
    ap.add_argument("--fibre", default=None, help="rational root of H_t (e.g. 1/5) or integer root mod p with --modp")
    ap.add_argument("--modp", type=int, default=None)
    ap.add_argument("--point", default=None, help="comma list b3,b4,q2,..,q_{t-1}")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--B0", default="0")
    ap.add_argument("--json", default=None, help="banked terminal_laurent_t2.json for row control (t=2)")
    ap.add_argument("--label", default="")
    a = ap.parse_args()
    t = a.t; q = 2 * t + 1; e = 3 * t + 1
    F = Fld(a.modp)
    if a.modp is None:
        y = Fraction(a.fibre)
    else:
        y = int(a.fibre) % a.modp
    H = F.add(F.add(F.mul(F.el(12 * q * q), F.mul(y, y)), F.mul(F.el(-12 * q * (t + 1)), y)), F.el((t + 1) * (3 * t + 2)))
    assert F.iszero(H), "fibre is not a root of H_t"
    if a.point:
        vals_pt = [F.el(Fraction(x)) if a.modp is None else F.el(int(x)) for x in a.point.split(",")]
    else:
        rnd = random.Random(a.seed)
        vals_pt = [F.el(rnd.randint(1, 50)) for _ in range(t)]
    names = ["b3", "b4"] + ["q%d" % j for j in range(2, t)]
    pt = dict(zip(names, vals_pt))
    B0 = F.el(Fraction(a.B0)) if a.modp is None else F.el(int(a.B0))
    print("=== rebuild t=%d fibre y=%s%s point %s B0=%s %s" % (t, a.fibre, (" mod %d" % a.modp) if a.modp else "", pt, B0, a.label))
    S, vals, pivots, T = solve_point(F, t, y, pt, B0)
    c, g = S["c"], S["g"]
    print("normalizer: g1=%s g2=%s g=%s c=-y*g=%s" % (S["g1"], S["g2"], g, c))
    for band, var, piv, val in pivots:
        print("PIVOT band=%d var=%s coef=%s value=%s" % (band, var, piv, val))
    print("b1=%s b2=%s" % (S["b1"], S["b2"]))
    print("TERMINAL rows T_{t,k} (k=0..%d): %s" % (2 * t - 1, T))
    print("T0 + c = tau_t(point) = %s   (tau=0 <=> T0 = -c)" % F.add(T[0], c))
    if a.json:
        import sympy as sp
        rec = json.load(open(a.json))
        b3s, b4s, ys = sp.symbols("b3 b4 q5_1")
        ok = True
        for row in rec["terminal"]:
            k = row["band"]
            val = sp.sympify(row["expr"]).subs({b3s: sp.Rational(pt["b3"]), b4s: sp.Rational(pt["b4"]), ys: sp.Rational(y)})
            val = Fraction(int(val.p), int(val.q))
            mine = F.mul(F.el(-1), T[k])  # JSON stores R = -E, band k = [X^k]R = -T_k
            flag = (val == mine)
            ok = ok and flag
            print("JSON_CONTROL band=%d json=%s mine=-T_k=%s %s" % (k, val, mine, "OK" if flag else "MISMATCH"))
        print("JSON_ROWS_MATCH=%s" % ok)
    # Laurent identities D0..D4 (Sol (2.3)) from the pieces
    s = [F.el(0), F.el(1)]
    Q1, Up, Y, Z, Xp = S["Q1"], S["Up"], S["Y"], S["Z"], S["Xp"]
    Q2 = pscale(F, s, y); P3 = pscale(F, s, g)
    D0 = psub(F, pmul(F, Q1, Xp), pmul(F, Up, Y))
    D1 = padd(F, psub(F, padd(F, pscale(F, pmul(F, Q2, Xp), F.el(2)), pmul(F, Q1, pderiv(F, Y))), pmul(F, pderiv(F, Q1), Y)), pscale(F, pmul(F, Up, Z), F.el(-2)))
    D2 = padd(F, padd(F, padd(F, pscale(F, pmul(F, Up, P3), F.el(-3)), pmul(F, Q1, pderiv(F, Z))), pscale(F, pmul(F, pderiv(F, Q1), Z), F.el(-2))),
              psub(F, pscale(F, pmul(F, Q2, pderiv(F, Y)), F.el(2)), pmul(F, pderiv(F, Q2), Y)))
    D3 = padd(F, psub(F, pmul(F, Q1, pderiv(F, P3)), pscale(F, pmul(F, pderiv(F, Q1), P3), F.el(3))),
              pscale(F, psub(F, pmul(F, Q2, pderiv(F, Z)), pmul(F, pderiv(F, Q2), Z)), F.el(2)))
    D4 = psub(F, pscale(F, pmul(F, Q2, pderiv(F, P3)), F.el(2)), pscale(F, pmul(F, pderiv(F, Q2), P3), F.el(3)))
    # E(h) as poly in s: E(X) = sum T_k X^k, X = s + b4
    EX = ptrim(F, list(T)); Es = pshift(F, EX, pt["b4"])
    chk = {
        "D0 == -c - E(h)": psub(F, D0, psub(F, [F.mul(F.el(-1), c)], Es)) == [],
        "D1 == -c*b1": psub(F, D1, [F.mul(F.el(-1), F.mul(c, S["b1"]))]) == [],
        "D2 == -c*b2": psub(F, D2, [F.mul(F.el(-1), F.mul(c, S["b2"]))]) == [],
        "D3 == -c*b3": psub(F, D3, [F.mul(F.el(-1), F.mul(c, pt["b3"]))]) == [],
        "D4 == c*L": psub(F, D4, pscale(F, s, c)) == [],
    }
    for k_, v_ in chk.items(): print("LAURENT_IDENTITY %s : %s" % (k_, "OK" if v_ else "FAIL"))
    print("D0 as poly in s (low->high): %s" % D0)
    # direct bivariate Jacobian
    Q, P, hd, Ld = build_pair(F, t, y, pt, S, vals)
    degQ = max(i + j for (i, j) in Q); degP = max(i + j for (i, j) in P)
    print("pair built: deg Q=%d (expect %d) terms=%d ; deg P=%d (expect %d) terms=%d" % (degQ, 4 * q, len(Q), degP, 4 * e, len(P)))
    J = dadd(F, dmul(F, dgamma(F, Q), dpi(F, P)), dscale(F, dmul(F, dpi(F, Q), dgamma(F, P)), F.el(-1)))
    print("J(Q,P) direct = %s" % dstr(F, J, 8))
    Ed = peval_dict(F, EX, hd)
    pred = dadd(F, dconst_scale(F, c, (1, 0)), dmul(F, {(0, 1): F.el(1)}, Ed))
    diff = dadd(F, J, dscale(F, pred, F.el(-1)))
    print("J - (c*gamma + pi*E(h)) = %s  -> %s" % (dstr(F, diff, 4) if diff else "0", "FORMULA_OK" if not diff else "FORMULA_FAIL"))
    ztype = dadd(F, dconst_scale(F, c, (1, 0)), dconst_scale(F, F.mul(F.el(-1), c), (0, 1)))
    print("J == c*(gamma - pi) = -c*z ? %s" % ("YES (z-type pair)" if dadd(F, J, dscale(F, ztype, F.el(-1))) == {} else "NO"))
    print("J == c*gamma ? %s" % ("YES" if dadd(F, J, dscale(F, dconst_scale(F, c, (1, 0)), F.el(-1))) == {} else "NO"))
    print("J == 0 ? %s" % ("YES" if J == {} else "NO"))
    print("J term count = %d ; J degree = %s" % (len(J), max((i + j for (i, j) in J), default=-1)))

def dconst_scale(F, a, key): return dtrim(F, {key: F.el(a)})

if __name__ == "__main__":
    main()
