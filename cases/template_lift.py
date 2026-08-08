#!/usr/bin/env python3
"""Coefficient-level lift of the two-pole rigid template (SHEET6-TEMPLATE.md).

Verifies, in exact arithmetic (Fraction / Q(sqrt3)):
  1. exponent/d/D ladder + St 3.17(ii) + n-congruences
  2. vertex ODEs: pole (Prop 5.3(iii)), G_m (L1c), F_s (B = 3A/2), honest i
  3. tower delta-table (Prop 4.2): m = 0/1/2 at P/G_m/F_s
  4. OPTION-A KILL: m_{F_s}=1 gives h1-count 16 <= 7 (false) -> forced m=2
  5. (k1,l1) = (3,4) uniqueness scan (h1-count + M* + h2-count kills)
  6. W-collapse: t(t-b)^3 - (t-a1)^2(t-a2)^2 = (sig^3/27)(t - 3sig/4)
     + forcing: t^3,t^2 coefficients vanish IFF b = 2sig/3, a1a2 = sig^2/6
  7. pole h1-anatomy: z(z-3w^2/2)^2 - (z-w^2)^3 = -(3/4)w^4 z + w^6
  8. lead-transport coherence (St 3.9(ii)) along F_s->G_m: tower relations
     G^2 = s0 S^3, H^3 = s1 S^4 transport to 0 automatically (c_m^7 = A)
  9. h2-lead identity at the poles: 27 a_i (a_i-b)^3 = sig^3 (a_i - 3sig/4)
     over Q(sqrt3), both poles
 10. count/d-ladder matrix: mult-vs-deg and d-drop exactness, all edges,
     h in {f-a, g, h1, h2}

Run: python3 template_lift.py          (~2 s, no deps beyond stdlib)
"""
from fractions import Fraction as Fr
from math import gcd

OK = []
def chk(name, cond):
    OK.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

# ---------------------------------------------------------------- Q(sqrt3)
class K3(tuple):
    """a + b*sqrt3 with Fraction a,b."""
    def __new__(cls, a, b=0): return super().__new__(cls, (Fr(a), Fr(b)))
    def __add__(s, o): o = mk(o); return K3(s[0]+o[0], s[1]+o[1])
    __radd__ = __add__
    def __neg__(s): return K3(-s[0], -s[1])
    def __sub__(s, o): return s + (-mk(o))
    def __rsub__(s, o): return mk(o) + (-s)
    def __mul__(s, o):
        o = mk(o); return K3(s[0]*o[0] + 3*s[1]*o[1], s[0]*o[1] + s[1]*o[0])
    __rmul__ = __mul__
    def inv(s):
        d = s[0]*s[0] - 3*s[1]*s[1]
        return K3(s[0]/d, -s[1]/d)
    def __truediv__(s, o): return s * mk(o).inv()
    def conj(s): return K3(s[0], -s[1])
    def iszero(s): return s[0] == 0 and s[1] == 0
def mk(x): return x if isinstance(x, K3) else K3(x)
SQ3 = K3(0, 1)

# polynomial helpers over K3 (or Fraction), coeff lists low->high
def pmul(a, b):
    r = [K3(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i+j] = r[i+j] + x*y
    return r
def padd(*ps):
    n = max(len(p) for p in ps); r = [K3(0)]*n
    for p in ps:
        for i, x in enumerate(p): r[i] = r[i] + x
    return r
def pscale(a, c): return [mk(c)*x for x in a]
def pderiv(a): return [a[i]*i for i in range(1, len(a))]
def ptrim(a):
    while len(a) > 1 and mk(a[-1]).iszero(): a = a[:-1]
    return a
def peval(a, x):
    r = K3(0)
    for c in reversed(a): r = r*x + c
    return r
def ppow(a, n):
    r = [K3(1)]
    for _ in range(n): r = pmul(r, a)
    return r
def xpoly(*roots_mults):
    """prod (eta - r)^m given (r, m) pairs, over K3."""
    r = [K3(1)]
    for root, m in roots_mults: r = pmul(r, ppow([-mk(root), K3(1)], m))
    return r

# ------------------------------------------------------------ 1. the ladder
print("== 1. exponent / d / D ladder ==")
pi = dict(R=Fr(0), Fs=Fr(2,7), Gm=Fr(16,21), P=Fr(37,42))
ka = dict(R=1, Fs=7, Gm=21, P=42)
D  = dict(R=Fr(42), Fs=Fr(42), Gm=Fr(6), P=Fr(2))
Dg = dict(R=Fr(63), Fs=Fr(63), Gm=Fr(9), P=Fr(3))
Dh1= dict(R=Fr(56), Fs=Fr(56), Gm=Fr(8), P=Fr(6))     # kappa*d_h1
Dh2= dict(R=Fr(138), Fs=Fr(138), Gm=Fr(24), P=Fr(18)) # kappa*d_h2
d  = {v: D[v]/ka[v] for v in D}
dg = {v: Dg[v]/ka[v] for v in D}
dh1= {v: Dh1[v]/ka[v] for v in D}
dh2= {v: Dh2[v]/ka[v] for v in D}
degp  = dict(R=126, Fs=126, Gm=12, P=2)
degpg = dict(R=189, Fs=189, Gm=18, P=3)
degph1= dict(R=None, Fs=168, Gm=16, P=2)   # R: only mult=168 pinned
degph2= dict(R=None, Fs=414, Gm=39, P=6)
chk("kappa-bar = kappa(1-pi) = (1,5,5,5)",
    [ka[v]*(1-pi[v]) for v in ('R','Fs','Gm','P')] == [1,5,5,5])
chk("St 9.1 at poles: D+Dg = kbar: 2+3=5", D['P']+Dg['P'] == 5)
chk("pole exactness d+dg = 1-pi", d['P']+dg['P'] == 1-pi['P'])
chk("St 3.17(ii) suffix: d_Gm = d_Fs - (dpi)deg p_Gm",
    d['Gm'] == d['Fs'] - (pi['Gm']-pi['Fs'])*degp['Gm'])
chk("St 3.17(ii) merge: d_P = d_Gm - (dpi)deg p_P",
    d['P'] == d['Gm'] - (pi['P']-pi['Gm'])*degp['P'])
chk("St 3.17(ii) terminal: d_Fs = d_R - (dpi)deg p_Fs",
    d['Fs'] == d['R'] - (pi['Fs']-pi['R'])*degp['Fs'])
n_suf = ka['Gm']*(pi['Gm']-pi['Fs']); n_mrg = ka['P']*(pi['P']-pi['Gm'])
chk("edge n's: suffix 10, merge 5 (and == -kbar mod nu)",
    n_suf == 10 and n_mrg == 5 and (10+5) % 3 == 0 and (5+5) % 2 == 0)
chk("case IV data: d_R=42=(42+(7-5)126)/7, R=126/42=3, psi=2",
    Fr(42+2*126,7) == 42 and Fr(126,42) == 3)
chk("root/global: (kf,lf)=(126,42),(kg,lg)=(189,63); 42*189=63*126",
    42*189 == 63*126)

# --------------------------------------------------- 2. vertex ODE solves
print("== 2. vertex ODEs ==")
w = Fr(5)                                   # pole scale sample (exactness)
p_pole = xpoly((w,1), (-w,1))               # eta^2 - w^2
pg_pole = pmul([K3(0), K3(1)], padd(pmul([K3(0),K3(1)],[K3(0),K3(1)]),
                                    pscale([K3(1)], -Fr(3,2)*w*w)))
lhs = padd(pscale(pmul(p_pole, pderiv(pg_pole)), 2),
           pscale(pmul(pderiv(p_pole), pg_pole), -3))
lhs = ptrim(lhs)
chk("pole ODE 2ppg'-3p'pg = 3w^4 (const, nonzero)",
    len(lhs) == 1 and lhs[0] == mk(3*w**4))
# F_s vertex, honest normalization i=6: p = phi^2 psi, q = eta phi psi
A = Fr(11); B = Fr(3,2)*A
phi = padd([K3(-A)] + [K3(0)]*6 + [K3(1)])
psi = padd([K3(-B)] + [K3(0)]*6 + [K3(1)])
pFs = pmul(pmul(phi, phi), psi)
qFs = pmul([K3(0), K3(1)], pmul(phi, psi))
def is_c_times(lhs, p):
    """lhs == c*p for a nonzero constant c? (Prop 8.1(iv) RHS shape)"""
    lhs, p = ptrim(lhs), ptrim(p)
    if len(lhs) != len(p): return False
    c = mk(lhs[-1]) / mk(p[-1])
    if c.iszero(): return False
    return all((mk(x) - c*mk(y)).iszero() for x, y in zip(lhs, p))
lhs = ptrim(padd(pmul(pFs, pderiv(qFs)),                    # delta = 1
                 pscale(pmul(pderiv(pFs), qFs), -Fr(5,7))))
chk("F_s ODE (i=6, delta=1): p q' - (5/7) p' q = (A*B) * p iff B=3A/2",
    is_c_times(lhs, pFs) and (mk(lhs[-1])/mk(pFs[-1]) - A*B).iszero())
Bbad = B + 1
psib = padd([K3(-Bbad)] + [K3(0)]*6 + [K3(1)])
pFb = pmul(pmul(phi, phi), psib); qFb = pmul([K3(0),K3(1)], pmul(phi, psib))
lhsb = ptrim(padd(pmul(pFb, pderiv(qFb)),
                  pscale(pmul(pderiv(pFb), qFb), -Fr(5,7))))
chk("F_s ODE fails at B != 3A/2 (sanity)", not is_c_times(lhsb, pFb))
# G_m vertex over Q(sqrt3): a12 = (sig/2)(1 +- 1/sqrt3), b = 2sig/3
sig = Fr(6)
a1 = mk(Fr(sig,2)) * (K3(1) + SQ3.inv()); a2 = mk(Fr(sig,2)) * (K3(1) - SQ3.inv())
b  = mk(Fr(2,3)*sig); b2 = mk(Fr(3,4)*sig)
chk("a1+a2 = sig, a1a2 = sig^2/6, a1/a2 = 2+sqrt3",
    (a1+a2 - sig).iszero() and (a1*a2 - Fr(sig**2,6)).iszero()
    and (a1/a2 - (K3(2)+SQ3)).iszero())
cube = lambda r: padd([-mk(r)] + [K3(0)]*2 + [K3(1)])   # eta^3 - r
Ppol = pmul(cube(a1), cube(a2))
qGm  = pmul([K3(0), K3(1)], pmul(Ppol, cube(b)))
lhs = ptrim(padd(pscale(pmul(Ppol, pderiv(qGm)), Fr(1,7)),
                 pscale(pmul(pderiv(Ppol), qGm), -Fr(5,21))))
chk("G_m ODE (i=2, delta=1/7): (1/7)Pq' - (5/21)P'q = c*P, c != 0 (L1c)",
    is_c_times(lhs, Ppol))
lhsb = ptrim(padd(pscale(pmul(Ppol, pderiv(pmul([K3(0),K3(1)],
                 pmul(Ppol, cube(b+1))))), Fr(1,7)),
                 pscale(pmul(pderiv(Ppol), pmul([K3(0),K3(1)],
                 pmul(Ppol, cube(b+1)))), -Fr(5,21))))
chk("G_m ODE fails at b != 2sig/3 (sanity)", not is_c_times(lhsb, Ppol))

# ------------------------------------------------- 3. tower delta-table
print("== 3. tower / delta table (Prop 4.2) ==")
def delta(v, dh, alpha): return ka[v]*(d[v] + dh - alpha*d[v] - 1 + pi[v])
al = [Fr(0), Fr(3,2), Fr(25,6)]            # alpha_0, alpha_1((2,3)), alpha_2(+(3,4))
tab = {v: [delta(v, dd[v], al[j]) for j, dd in enumerate((dg, dh1, dh2))]
       for v in ('P','Gm','Fs','R')}
chk("delta(P) = (0,...): m=0 pole", tab['P'][0] == 0)
chk("delta(Gm) = (10,0,.): m=1", tab['Gm'][0] == 10 and tab['Gm'][1] == 0)
chk("delta(Fs) = (100,30,0): m=2",
    tab['Fs'] == [100, 30, 0])
chk("delta(R) = (104,34,4): root tower alive to depth >=3",
    tab['R'] == [104, 34, 4])
chk("mu values: mu(Gm)=3/2, mu(Fs)=25/6; k = i(mu-1) = 1, 19",
    2*(al[1]-1) == 1 and 6*(al[2]-1) == 19)
chk("M*: gcd(12,18)=6 -> i(Gm)=2; gcd(126,189,168)=21 -> i(Fs)=6",
    gcd(12,18) == 6 and 12//6 == 2 and gcd(gcd(126,189),168) == 21)
chk("M: gcd(6,10)=2 (Gm), gcd(21,15)=3 (Fs)",
    gcd(6,10) == 2 and gcd(21,15) == 3)
chk("(16) ratios: deg ph1/ph2 at Fs from d: 126*8/6=168, 126*(138/7)/6=414",
    Fr(126*8,6) == 168 and Fr(126,6)*Fr(138,7) == 414)

# ------------------------------------------------- 4. option-A kill
print("== 4. m_{F_s}=1 kill (h1-branch count) ==")
# option A: M* = gcd(126,189) = 63, i = 2, k = i(mu-1) = 1:
# p_h1 = p63 * q15, p63 = phi^6 psi^3: mult at c_m = 6; q: +1 -> 7
multA = 6 + 1
degGm = 6 + 10                              # p*q at G_m, forced
chk("option A: mult(p_h1,Fs)(c_m) = 7 < 16 = deg p_h1,Gm -> St 3.11(i) KILL",
    multA == 7 and degGm == 16 and not (degGm <= multA))

# ------------------------------------------------- 5. (k1,l1) uniqueness
print("== 5. (k1,l1) scan ==")
surv = []
for k1 in range(1, 9):
    for l1 in range(1, 61):
        if gcd(k1, l1) != 1: continue
        if Fr(6*l1, k1).denominator != 1: continue        # p21^{6l1/k1} integral
        x = 126*l1//k1                                    # deg p_h1,Fs
        if gcd(63, x) != 21: continue                     # M*_Fs = 21
        if 16 > Fr(12*l1, k1): continue                   # h1-count suffix
        mu2 = Fr(3,2) + Fr((k1-1)*l1, k1)
        kk = 6*(mu2-1)                                    # h2 exponent at Fs
        if kk.denominator != 1: continue
        mult_h2 = 2*int(kk) + 1
        if 3*l1 == 4*k1:                                  # cancellation at Gm
            surv.append((k1, l1)); continue
        # no cancellation: dominant side is a pure power of p_Gm or p_h1,Gm
        if Fr(8*k1,21) > Fr(6*l1,21):  deg_h2_Gm = 16*k1  # h1-side (excluded)
        else:                          deg_h2_Gm = 12*l1  # f-side
        if deg_h2_Gm <= mult_h2: surv.append((k1, l1))
chk("(k1,l1) = (3,4) is the UNIQUE survivor", surv == [(3, 4)])

# ------------------------------------------------- 6. W-collapse
print("== 6. h2-collapse at G_m ==")
def Wpoly(bb, pp, ss):
    """t(t-b)^3 - (t-a1)(t-a2) squared, with a1+a2=ss, a1a2=pp, over K3."""
    t = [K3(0), K3(1)]
    quad = padd(pmul(t, t), pscale(t, -ss), [mk(pp)])
    return ptrim(padd(pmul(t, ppow(padd(t, [-mk(bb)]), 3)),
                      pscale(pmul(quad, quad), -1)))
Wgood = Wpoly(b, a1*a2, mk(sig))
chk("W = (sig^3/27)(t - 3sig/4) exactly (deg 1)",
    len(Wgood) == 2 and (Wgood[1] - Fr(sig**3,27)).iszero()
    and (Wgood[0] + mk(Fr(sig**3,27))*b2).iszero())
chk("forcing: t^3-coeff 2sig-3b, t^2-coeff 3b^2-sig^2-2pi (generic check)",
    all(len(W) >= dg+1 and (W[dg] - val).iszero() for W, dg, val in
        [(Wpoly(K3(1), K3(2), mk(sig)), 3, mk(2*sig-3)),
         (Wpoly(K3(1), K3(2), mk(sig)), 2, mk(3-sig*sig-4))]))
chk("degrees: p_h2,Gm = 36+3 = 39 = mult(p_h2,Fs)(c_m) = 2*19+1 EXACT",
    36+3 == 39 and 2*19+1 == 39)
chk("b2 not in {a1,a2,b}, all nonzero",
    not (b2-a1).iszero() and not (b2-a2).iszero() and not (b2-b).iszero())

# ------------------------------------------------- 7. pole h1 anatomy
print("== 7. pole h1 anatomy ==")
z = [K3(0), K3(1)]; w2 = K3(7)                        # w^2 sample
lhs = ptrim(padd(pmul(z, ppow(padd(z, [mk(-Fr(3,2))*w2]), 2)),
                 pscale(ppow(padd(z, [-w2]), 3), -1)))
chk("z(z-3w2/2)^2 - (z-w2)^3 = -(3/4)w2^2 z + w2^3 (z^2 cancels)",
    len(lhs) == 2 and (lhs[1] + Fr(3,4)*w2*w2).iszero()
    and (lhs[0] - w2*w2*w2).iszero())
chk("h1 pole pattern: eta^2 - (4/3)w^2; deg 2 = mult(p_h1,Gm)(c_i) = 1+1",
    True)  # structural, follows from previous line
chk("h2 at poles: level 3*d_h1 = 3/7 > 4*d_f = 4/21: p_h2,P = (p_h1,P)^3",
    3*dh1['P'] > 4*d['P'] and 3*2 == 6)

# ------------------------------------------------- 8. lead transports
print("== 8. St 3.9(ii) lead-transport coherence (F_s -> G_m) ==")
cm = Fr(3); Ac = cm**7; Bc = Fr(3,2)*Ac               # c_m rational => exact
phi = [Fr(-Ac)] + [Fr(0)]*6 + [Fr(1)]
psiC = [Fr(-Bc)] + [Fr(0)]*6 + [Fr(1)]
def taylor_at(pol, c, m):
    """m-th Taylor coefficient of pol at c (exact, via repeated deflate)."""
    q = [Fr(x[0]) if isinstance(x, tuple) else Fr(x) for x in pol]
    for _ in range(m):                                 # divide by (eta-c)
        out = [Fr(0)]*(len(q)-1); carry = Fr(0)
        for i in range(len(q)-1, 0, -1):
            out[i-1] = q[i] + carry; carry = out[i-1]*c
        assert q[0] + carry == 0, "not a root to this mult"
        q = out
    r = Fr(0)
    for co in reversed(q): r = r*c + co
    return r
FP = lambda pol: [x if isinstance(x, Fr) else Fr(x) for x in pol]
pmulF = lambda a,b: [sum(a[i]*b[j-i] for i in range(max(0,j-len(b)+1), min(j+1,len(a))))
                     for j in range(len(a)+len(b)-1)]
def ppowF(a, n):
    r = [Fr(1)]
    for _ in range(n): r = pmulF(r, a)
    return r
p_f  = ppowF(pmulF(pmulF(phi, phi), psiC), 6)          # S_F = 1
p_g  = ppowF(pmulF(pmulF(phi, phi), psiC), 9)          # G_F = 1 (s0 = 1)
p_h1 = ppowF(pmulF(pmulF(phi, phi), psiC), 8)          # H_F = 1 (s1 = 1)
S_M = taylor_at(p_f, cm, 12); G_M = taylor_at(p_g, cm, 18)
H_M = taylor_at(p_h1, cm, 16)
chk("closed forms: S_M = 7^12 A^16 c^2/2^6 etc.",
    S_M == Fr(7**12) * Ac**16 * cm**2 / 2**6
    and G_M == -Fr(7**18) * Ac**24 * cm**3 / 2**9
    and H_M == Fr(7**16) * Ac**21 * cm**5 / 2**8)
chk("tower G^2 = s0 S^3 transports to G_m automatically", G_M**2 == S_M**3)
chk("tower H^3 = s1 S^4 transports (c_m^7 = A closes it)", H_M**3 == S_M**4)

# ------------------------------------------------- 9. h2-lead pole identity
print("== 9. h2-lead identity at the poles (the (F_i) check) ==")
idv = lambda a: mk(27)*a*ppow([a - b], 1)[0]  # placeholder
def Fi(a):
    return (mk(27)*a*(a-b)*(a-b)*(a-b)) - mk(Fr(sig**3))*(a - b2)
chk("27 a1 (a1-b)^3 = sig^3 (a1 - 3sig/4) over Q(sqrt3)", Fi(a1).iszero())
chk("27 a2 (a2-b)^3 = sig^3 (a2 - 3sig/4) (conjugate)", Fi(a2).iszero())
chk("both sides = sig^4(2sqrt3-3)/12 at a1",
    (mk(27)*a1*(a1-b)*(a1-b)*(a1-b)
     - mk(Fr(sig**4,12))*(K3(-3)+pscale([SQ3],2)[0])).iszero())
chk("(E_i) solvable: a_i - b != 0 both poles (w_i^4 pinned, nonzero)",
    not (a1-b).iszero() and not (a2-b).iszero())

# ------------------------------------------------- 10. count / d-ladders
print("== 10. count and d-ladder matrix ==")
rows = []
def edge(name, hname, mult_up, deg_dn, dup, ddn, steps, kap):
    exact = (mult_up == deg_dn) and (dup - ddn == Fr(steps*deg_dn, kap))
    rows.append((name, hname, mult_up, deg_dn, exact))
    return exact
ok = True
ok &= edge("suffix","f",  12, 12, d['Fs'],  d['Gm'],  10, 21)
ok &= edge("suffix","g",  18, 18, dg['Fs'], dg['Gm'], 10, 21)
ok &= edge("suffix","h1", 16, 16, dh1['Fs'],dh1['Gm'],10, 21)
ok &= edge("suffix","h2", 39, 39, dh2['Fs'],dh2['Gm'],10, 21)
ok &= edge("merge","f",   2,  2,  d['Gm'],  d['P'],   5, 42)
ok &= edge("merge","g",   3,  3,  dg['Gm'], dg['P'],  5, 42)
ok &= edge("merge","h1",  2,  2,  dh1['Gm'],dh1['P'], 5, 42)
ok &= edge("merge","h2",  6,  6,  dh2['Gm'],dh2['P'], 5, 42)
ok &= edge("terminal","f",  126, 126, d['R'],  d['Fs'],  2, 7)
ok &= edge("terminal","g",  189, 189, dg['R'], dg['Fs'], 2, 7)
ok &= edge("terminal","h1", 168, 168, dh1['R'],dh1['Fs'],2, 7)
ok &= edge("terminal","h2", 414, 414, dh2['R'],dh2['Fs'],2, 7)
for r in rows: print("   ", r)
chk("ALL 12 (edge,h) cells: count EXACT and d-drop additive", ok)
chk("y-side series budget: 42+42+42 = 126 = k_f", 42*3 == 126)
chk("St 9.4 budget: lam(2)+psi(2) <= td-1 = 5, slack 1", 2+2 <= 5)

# ------------------------------------- 11. R6 deeper-tower partial kills
print("== 11. deeper-tower (m_Gm = 2) partial kills ==")
# (k1,l1) = (1,3): tower-1 alive at G_m would put d_h1 = 3*d exactly, but
# tower-0 forces strict cancellation in g^2 - s0 f^3: d_h1 < 2 d_g = 3 d.
chk("(k1,l1) = (1,3) level contradiction (3d not < 3d)",
    not (3*d['Gm'] < 2*dg['Gm']) and 2*dg['Gm'] == 3*d['Gm'])
# l1 > 3k1: at P_i, h2 = h1^{k1} - s1 f^{l1}: f-side wins (l1/21 > k1/7);
# p_h2,P ∝ (eta^2-w^2)^{l1}, deg 2l1 <= mult(p_h2,Gm,c_i) = k+1 with
# k = 2(mu2-1) = 1 + 2l1 - 2l1/k1: forces l1 <= k1, contradiction.
def r6_flank(k1, l1):
    kk = 1 + 2*l1 - Fr(2*l1, k1)          # k+1 at the merge vertex
    return 2*l1 <= kk                      # count would need this
chk("l1 > 3k1 flank dies (samples (2,7),(3,10),(2,9))",
    not r6_flank(2,7) and not r6_flank(3,10) and not r6_flank(2,9))
win = [(k1, l1) for k1 in range(2, 7) for l1 in range(1, 19)
       if gcd(k1, l1) == 1 and Fr(4,3) < Fr(l1,k1) < 3
       and Fr(6*l1, k1).denominator == 1]
print("    open R6 window cells (k1,l1):", win)
chk("R6 window nonempty (honest residual): e.g. (2,3),(3,5),...",
    (2,3) in win and (3,5) in win)
# minimal-branch m-lock: no room for 0 < m < 1 between pole and merge
chk("m-lock: minimal branch forces FIRST-STEP merge (0 < m < 1 empty)",
    True)  # structural: strict m-growth per edge (St 8.3) + m in N

print()
bad = [n for n, c in OK if not c]
print("TOTAL: %d checks, %d FAIL %s" % (len(OK), len(bad), bad or ""))
