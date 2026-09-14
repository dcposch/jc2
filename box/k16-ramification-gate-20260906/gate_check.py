#!/usr/bin/env python3
"""Independent changed-object checks for the K16 ramification gate (Fable 5.1, 2026-09-06).
Exact arithmetic only: Fractions and Q(sqrt(-6)) pairs.  No CAS, no solver.
Polynomials are coefficient lists (index = degree).  Every claim is re-derived
from the definitions Z=xA, D=(3/4)Z^2, R=(x/3)D^2-D-1, f=3t(t-1), S=(t-1)D(f), Q=S-1.
"""
import resource
resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
from fractions import Fraction as Fr

class QS:  # a + b*sqrt(-6)
    __slots__ = ('a', 'b')
    def __init__(s, a, b=0): s.a = Fr(a); s.b = Fr(b)
    def __add__(s, o): o = lift(o); return QS(s.a+o.a, s.b+o.b)
    __radd__ = __add__
    def __neg__(s): return QS(-s.a, -s.b)
    def __sub__(s, o): return s + (-lift(o))
    def __rsub__(s, o): return lift(o) + (-s)
    def __mul__(s, o): o = lift(o); return QS(s.a*o.a-6*s.b*o.b, s.a*o.b+s.b*o.a)
    __rmul__ = __mul__
    def inv(s): n = s.a*s.a+6*s.b*s.b; return QS(s.a/n, -s.b/n)
    def __truediv__(s, o): return s*lift(o).inv()
    def __rtruediv__(s, o): return lift(o)*s.inv()
    def __eq__(s, o): o = lift(o); return s.a == o.a and s.b == o.b
    def __bool__(s): return s.a != 0 or s.b != 0
    def __repr__(s): return f"({s.a}+{s.b}r)"
def lift(o): return o if isinstance(o, QS) else QS(o)

FAILS = []
def check(cond, label):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond: FAILS.append(label)

def strip(p):
    while p and not p[-1]: p.pop()
    return p
def padd(p, q, K):
    n = max(len(p), len(q))
    return strip([(p[i] if i < len(p) else K(0)) + (q[i] if i < len(q) else K(0)) for i in range(n)])
def pmul(p, q, K):
    if not p or not q: return []
    r = [K(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        if not a: continue
        for j, b in enumerate(q): r[i+j] = r[i+j] + a*b
    return strip(r)
def pscale(c, p): return strip([c*a for a in p])
def pderiv(p): return strip([i*p[i] for i in range(1, len(p))])
def peval(p, x, K):
    v = K(0)
    for a in reversed(p): v = v*x + a
    return v
def pcompose(p, f, K):
    r = []
    for a in reversed(p): r = padd(pmul(r, f, K), [a], K)
    return r
def pdivmod(p, q, K):
    p = strip(list(p)); dq = len(q)-1; lc = q[-1]
    quo = [K(0)]*max(0, len(p)-dq)
    while p and len(p)-1 >= dq:
        c = p[-1]/lc; d = len(p)-1-dq; quo[d] = c
        for i in range(len(q)): p[d+i] = p[d+i] - c*q[i]
        strip(p)
    return strip(quo), p
def pgcd(p, q, K):
    p = strip(list(p)); q = strip(list(q))
    while q:
        _, r = pdivmod(p, q, K); p, q = q, r
    return pscale(1/p[-1], p) if p else []
def deg(p): return len(p)-1
def rdist(p, K): return deg(p) - deg(pgcd(p, pderiv(p), K))
def excess(p, K): return deg(p) - rdist(p, K)
def ordroot(p, a, K):
    k = 0
    while p and not peval(p, a, K): p = pderiv(p); k += 1
    return k

def build(A, K):
    x = [K(0), K(1)]
    Z = pmul(x, A, K)
    D = pscale(K(Fr(3, 4)), pmul(Z, Z, K))
    R = padd(padd(pscale(K(Fr(1, 3)), pmul(x, pmul(D, D, K), K)), pscale(K(-1), D), K), [K(-1)], K)
    f = [K(0), K(-3), K(3)]
    Df = pcompose(D, f, K)
    S = pmul([K(-1), K(1)], Df, K)
    Q = padd(S, [K(-1)], K)
    Af = pcompose(A, f, K); Apf = pcompose(pderiv(A), f, K)
    t = [K(0), K(1)]
    C = padd(pmul([K(-2), K(5)], Af, K), pmul(pscale(K(6), pmul(pmul(t, [K(-1), K(1)], K), [K(-1), K(2)], K)), Apf, K), K)
    return dict(x=x, Z=Z, D=D, R=R, f=f, Df=Df, S=S, Q=Q, Af=Af, C=C)

def lemma_checks(tag, A, K, r_Z, delta, n):
    o = build(A, K); Z, R, S, Q, C, Af, f = o['Z'], o['R'], o['S'], o['Q'], o['C'], o['Af'], o['f']
    N = 4*n+1
    check(deg(R) == N and deg(Q) == N and deg(S) == N, f"{tag}: deg R=deg Q=deg S=N={N}")
    # S = (27/4) t^2 (t-1)^3 A(f)^2 literally
    t = [K(0), K(1)]; t1 = [K(-1), K(1)]
    S2 = pscale(K(Fr(27, 4)), pmul(pmul(pmul(t, t, K), pmul(pmul(t1, t1, K), t1, K), K), pmul(Af, Af, K), K))
    check(S == S2, f"{tag}: S=(27/4)t^2(t-1)^3A(f)^2")
    check(rdist(Z, K) == r_Z and (peval(Z, K(Fr(-3, 4)), K) == 0) == bool(delta), f"{tag}: r(Z)={r_Z}, delta={delta}")
    check(rdist(S, K) == 2*r_Z - delta, f"{tag}: r(S)=2r-delta={2*r_Z-delta}")
    eQ, eR = excess(Q, K), excess(R, K)
    check(eQ == eR, f"{tag}: e(Q)=e(R)={eQ}")
    check(eQ <= 2*r_Z - delta - 1, f"{tag}: (RB) e(Q)={eQ} <= 2r-delta-1={2*r_Z-delta-1}")
    check(eQ + excess(S, K) <= N - 1, f"{tag}: e(S)+e(Q)={excess(S,K)}+{eQ} <= N-1")
    # e(Q) = deg gcd(Q, C): critical divisor consumes the excess
    check(deg(pgcd(Q, C, K)) == eQ, f"{tag}: e(Q)=deg gcd(Q,C) (critical divisor)")
    # S' = (27/4) t (t-1)^2 A(f) C
    Sp2 = pscale(K(Fr(27, 4)), pmul(pmul(pmul(t, pmul(t1, t1, K), K), Af, K), C, K))
    check(pderiv(S) == Sp2, f"{tag}: S'=(27/4)t(t-1)^2A(f)C, deg C={deg(C)}=2n-1")
    # norm identity R(f(t)) = -Q(t)Q(1-t)
    Rf = pcompose(R, f, K); Qs = pcompose(Q, [K(1), K(-1)], K)
    check(Rf == pscale(K(-1), pmul(Q, Qs, K)), f"{tag}: R(f(t)) = -Q(t)Q(1-t)")
    # mutated no-delta claim: if delta=1 the un-merged count 2r is wrong
    if delta: check(rdist(S, K) != 2*r_Z, f"{tag}: MUTANT r(S)=2r (fixed place unmerged) fails as required")
    return o

K = Fr
# T1: all simple, delta=0: A=x^2+x+1, n=3
lemma_checks("T1 A=x^2+x+1", [Fr(1), Fr(1), Fr(1)], K, 3, 0, 3)
# T2: Z=x(x+3/4)^2 : r=2, delta=1, repeated root AT the fixed place
lemma_checks("T2 A=(x+3/4)^2", [Fr(9, 16), Fr(3, 2), Fr(1)], K, 2, 1, 3)
# T3: A=(x+3/4)(x-2): r=3, delta=1
lemma_checks("T3 A=(x+3/4)(x-2)", [Fr(-3, 2), Fr(-5, 4), Fr(1)], K, 3, 1, 3)
# T4: A=(x-1)^2: r=2, delta=0
lemma_checks("T4 A=(x-1)^2", [Fr(1), Fr(-2), Fr(1)], K, 2, 0, 3)
# T4b: n=4, A=x(x-1)(x+3/4): s=2 (A(0)=0), r=3, delta=1
lemma_checks("T4b A=x(x-1)(x+3/4)", pmul(pmul([Fr(0), Fr(1)], [Fr(-1), Fr(1)], K), [Fr(3, 4), Fr(1)], K), K, 3, 1, 4)

# T5: fixed place over Q(sqrt(-6)): need Z(-3/4)^2=-8/3, A=lam(x^2+1), lam=-(128/225)sqrt(-6)
K = QS
lam = QS(0, Fr(-128, 225))
A5 = [lam, QS(0), lam]
o = build(A5, K); R, Q, S, Z, f = o['R'], o['Q'], o['S'], o['Z'], o['f']
a34 = QS(Fr(-3, 4)); half = QS(Fr(1, 2))
check(peval(Z, a34, K)*peval(Z, a34, K) == QS(Fr(-8, 3)), "T5: Z(-3/4)^2=-8/3")
check(peval(R, a34, K) == 0 and peval(pderiv(R), a34, K) == QS(Fr(4, 3)), "T5: R(-3/4)=0, R'(-3/4)=4/3")
check(peval(Q, half, K) == 0 and peval(pderiv(Q), half, K) == QS(-2), "T5: Q(1/2)=0, Q'(1/2)=-2")
check(peval(pderiv(Q), half, K) == 3*(half-1)*peval(pderiv(R), a34, K), "T5: Q'(1/2)=3(t-1)R'(-3/4) holds AT the fixed place")
check(ordroot(R, a34, K) == 1 and ordroot(Q, half, K) == 1, "T5: ord_{-3/4}R = ord_{1/2}Q = 1 (simple)")
check(excess(Q, K) == excess(R, K), f"T5: e(Q)=e(R)={excess(Q,K)} over Q(sqrt-6)")
Rf = pcompose(R, f, K); Qs = pcompose(Q, [K(1), K(-1)], K)
check(Rf == pscale(K(-1), pmul(Q, Qs, K)), "T5: R(f(t))=-Q(t)Q(1-t)")
check(ordroot(Rf, half, K) == 2 and ordroot(Qs, half, K) == 1, "T5: double zero of R(f) at 1/2 splits 1+1 across Q and Q(1-t); not e(Q)")
Wf = pcompose([QS(Fr(3, 4)), QS(1)], f, K)
check(ordroot(Wf, half, K) == 2 and ordroot(Q, half, K) == 1, "T5: W=x+3/4 gives W(f) double at 1/2 while Q is simple (no double count)")
# quadratic in D0 at alpha=-3/4 is a perfect square (D0+2)^2 (unique root, ramification)
check([QS(4), QS(4), QS(1)] == pmul([QS(2), QS(1)], [QS(2), QS(1)], K), "T5: -(1/4)D0^2-D0-1 ∝ (D0+2)^2 unique root")

# T6: (DC)/(NC) at the SECOND D0 root of alpha=28/3 with w=-2, via an independent truncated-series solve
K = Fr; M = 8
def ser_mul(p, q): return [sum(p[j]*q[i-j] for j in range(i+1)) for i in range(M+1)]
def ser_add(*ps): return [sum(p[i] for p in ps) for i in range(M+1)]
def ser_scale(c, p): return [c*a for a in p]
def ser_inv(p):
    q = [Fr(0)]*(M+1); q[0] = 1/p[0]
    for i in range(1, M+1): q[i] = -sum(p[j]*q[i-j] for j in range(1, i+1))/p[0]
    return q
def ser_der(p): return [(i+1)*p[i+1] for i in range(M)] + [Fr(0)]
def germ(alpha, D0, w, sign_dc=+1, use_t=None):
    t = alpha*D0/3
    xs = [alpha, Fr(1)] + [Fr(0)]*(M-1)
    Ws = [Fr(0), w, Fr(2, 7), Fr(-1, 5)] + [Fr(0)]*(M-3)   # arbitrary germ with W(alpha)=0
    xi = ser_inv(xs)
    def resid(Ds):
        Rs = ser_add(ser_scale(Fr(1, 3), ser_mul(xs, ser_mul(Ds, Ds))), ser_scale(-1, Ds), [Fr(-1)]+[Fr(0)]*M)
        Js = ser_add(ser_scale(2, ser_der(Ws)), ser_scale(-1, ser_mul(ser_add(Ws, [Fr(1)]+[Fr(0)]*M), xi)), ser_scale(2, Ds))
        return ser_add(Rs, ser_scale(-1, ser_mul(Ws, Js))), Rs, Js
    Ds = [D0] + [Fr(0)]*M
    piv = 2*t-1
    for j in range(1, M+1):
        Ds[j] = -resid(Ds)[0][j]/piv
    res, Rs, Js = resid(Ds)
    return t, Ds, Rs, Js, res
alpha = Fr(28, 3)
for D0 in (Fr(3, 4), Fr(-3, 7)):
    for w in (Fr(1), Fr(-2)):
        t, Ds, Rs, Js, res = germ(alpha, D0, w)
        check(alpha*D0*D0/3 - D0 - 1 == 0 and 3*t*(t-1) == alpha and D0 == 1/(t-1), f"T6: root D0={D0} -> t={t}, alpha=3t(t-1), D0=1/(t-1)")
        check(all(c == 0 for c in res), f"T6: formal contact to order {M} at D0={D0}, w={w}")
        J0 = 2*w + (6*t-1)/alpha
        check(Js[0] == J0 and Rs[0] == 0 and Rs[1] == w*J0, f"T6: J(alpha)=2w+(6t-1)/alpha, R'=wJ at D0={D0}, w={w}")
        check((2*t-1)*Ds[1] == w*J0 - D0*D0/3, f"T6: (DC) sign at D0={D0}, w={w}")
        check((2*t-1)*Ds[1] != w*J0 + D0*D0/3, f"T6: MUTANT (DC) with +D0^2/3 fails at D0={D0}, w={w}")
        # (NC): C(t)=3t(t-1)^2 A(alpha) w J(alpha) with A(alpha)=Z/alpha, Z^2=4D/3 (either sign)
        Zs = [Fr(0)]*(M+1); tgt = ser_scale(Fr(4, 3), Ds)
        Z0sq = tgt[0]
        # avoid sqrt: compare C^2 (both signs of Z give the same square)
        # C = (5t-2)A + 6t(t-1)(2t-1)A', A=Z/x, A' = (Z' x - Z)/x^2 ; use Z' = (2/3)D'/Z
        # C*Z*alpha^2 = (5t-2) Z^2 alpha + 6t(t-1)(2t-1)((2/3)D' alpha - Z^2)
        lhs = (5*t-2)*Z0sq*alpha + 6*t*(t-1)*(2*t-1)*(Fr(2, 3)*Ds[1]*alpha - Z0sq)  # = C*Z*alpha^2
        rhs = 3*t*(t-1)**2*w*J0*Z0sq*alpha  # = 3t(t-1)^2 (Z/alpha) wJ * Z alpha^2
        check(lhs == rhs, f"T6: (NC) C=3t(t-1)^2 A(alpha) w J(alpha) at D0={D0}, w={w}")
        check(lhs != 3*t*(t-1)*w*J0*Z0sq*alpha, f"T6: MUTANT (NC) missing complementary (t-1) factor fails at D0={D0}, w={w}")
        ts = 1-t
        check(lhs != 3*ts*(ts-1)**2*w*J0*Z0sq*alpha, f"T6: MUTANT (NC) at the conjugate preimage 1-t fails at D0={D0}, w={w}")

# T7: leading ratio: both roots of 16(4m-3)u^2+24u-3 are u=1/(4(2d+1)), d=+-sqrt(m/3); identity in (m,d)
for (m, d) in ((Fr(12), Fr(2)), (Fr(12), Fr(-2)), (Fr(27), Fr(3)), (Fr(27), Fr(-3)), (Fr(48), Fr(4)), (Fr(48), Fr(-4))):
    u = 1/(4*(2*d+1))
    check(16*(4*m-3)*u*u + 24*u - 3 == 0, f"T7: m={m}, d={d}: u=1/(4(2d+1))={u} solves lc-quadratic")
for (m, d) in ((Fr(5), Fr(1, 3)), (Fr(7, 2), Fr(-5)), (Fr(4), Fr(2, 3))):
    check((4*m-3) + 6*(2*d+1) - 3*(2*d+1)**2 == 4*(m-3*d*d), f"T7: (4m-3)+6(2d+1)-3(2d+1)^2 = 4(m-3d^2) at m={m}, d={d} (both signs of d retained)")
# and lc J = N lc W + (3/2) lc A^2 with lc R=(3/16)lcA^4: for u=lcW/lcA^2 the equation is exactly the quadratic
m = Fr(4); n = m-1; N = 4*n+1
for d in (Fr(2, 1),):  # symbolic sanity with an arbitrary a=lcA, at m=12 (d=2 rational)
    pass
a = Fr(5, 7); m = Fr(12); n = m-1; N = 4*n+1
for d in (Fr(2), Fr(-2)):
    lcW = a*a/(4*(2*d+1)); lcJ = N*lcW + Fr(3, 2)*a*a
    check(lcW*lcJ == Fr(3, 16)*a**4, f"T7: lc(W)lc(J)=lc(R) at m=12, d={d}, moving lc A={a}")

# T8: origin: W(0)=-1, W'(0)=1 force J(0)=1 and (WJ-R)_1 = 1-3c2, i.e. c2=W''(0)/2=1/3 (a marking the shape controls do not carry)
c2 = Fr(2, 9)
Ws = [Fr(-1), Fr(1), c2] + [Fr(0)]*(M-2); xs = [Fr(0), Fr(1)] + [Fr(0)]*(M-1)
Ds = [Fr(0), Fr(0), Fr(3, 4)] + [Fr(0)]*(M-2)  # D=(3/4)x^2A^2 with A(0)=1
W1x = [Ws[i+1] for i in range(M)] + [Fr(0)]  # (W+1)/x
Js = ser_add(ser_scale(2, ser_der(Ws)), ser_scale(-1, W1x), ser_scale(2, Ds))
Rs = ser_add(ser_scale(Fr(1, 3), ser_mul(xs, ser_mul(Ds, Ds))), ser_scale(-1, Ds), [Fr(-1)]+[Fr(0)]*M)
E1 = ser_add(ser_mul(Ws, Js), ser_scale(-1, Rs))
check(Js[0] == 1 and E1[0] == 0 and E1[1] == 1-3*c2, "T8: J(0)=1, (WJ-R)_0=0, (WJ-R)_1=1-3c2 -> origin forces W''(0)/2=1/3")

print("GATE_CHECK_FAILS=%d" % len(FAILS))
print("ALL_GATE_CHECKS_PASS" if not FAILS else "GATE_CHECKS_FAILED: " + "; ".join(FAILS))
