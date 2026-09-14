#!/usr/bin/env python3
"""Reviewer controls for xmodel/k16-boundary-product-astra-20260906.md (gate: Fable).

Independent of box/k16-boundary-product-20260906/check.py: actual polynomials
(not free value symbols) wherever the producer used value symbols, plus the
controls the producer did not run. Every check raises an explicit exception
(no bare assert), so -O cannot erase a comparison.
Run: python3 box/k16-boundary-product-gate-fable5-20260906/gate_controls.py
"""
import sympy as S

class GateFail(Exception):
    pass

N_PASS = 0
def chk(cond, label):
    global N_PASS
    if not cond:
        raise GateFail(label)
    N_PASS += 1
    print("PASS", label)

x, t, X, B, eta, c, a0, a1, w1, w2 = S.symbols("x t X B eta c a0 a1 w1 w2")
cA, cW, alpha = S.symbols("cA cW alpha", nonzero=True)
u = S.symbols("u")

def E(Xv, W, Wp, A, b, e):
    U = Xv**3*A**2
    return (2*Xv*W*Wp - W**2 + (S.Rational(3, 2)*U-b)*W
            - S.Rational(3, 16)*U**2 + S.Rational(3, 4)*b*U + b*e*Xv)

def lowest(expr, var, Nsh=80):
    P = S.Poly(S.expand(expr*var**Nsh), var)
    d = min(m[0] for m in P.monoms())
    return d-Nsh, S.factor(P.coeff_monomial(var**d))

# ---------- Claim 1: pole/defect lemma, full valuation table ----------
for a in [2, 3, 4]:
    A = c/x**a + a0/x**(a-1); W = -B + w1*x + w2*x**2
    lo, lc = lowest(E(x, W, S.diff(W, x), A, B, eta), x)
    chk(lo == -(4*a-6) and S.simplify(lc + S.Rational(3, 16)*c**4) == 0,
        "C1 origin pole a=%d: unique leader x^%d, coeff -(3/16)c^4" % (a, lo))
for a in range(0, 4):
    for w in range(0, 8):
        if a == 0 and w == 0:
            continue
        A = (cA/u**a + a0/u**(a-1)) if a > 0 else cA + a0*u
        W = (cW/u**w + w1/u**(w-1)) if w > 0 else cW + w1*u
        lo, lc = lowest(E(alpha+u, W, S.diff(W, u), A, B, eta), u)
        if a == 0:
            pred, predc = -(2*w+1), -2*w*alpha*cW**2
        elif w <= 2*a-1:
            pred, predc = -4*a, -S.Rational(3, 16)*alpha**6*cA**4
        else:
            pred, predc = -(2*w+1), -2*w*alpha*cW**2
        chk(lo == pred and S.simplify(lc-predc) == 0,
            "C1 alpha!=0 a=%d w=%d: unique leader order %d" % (a, w, lo))
A = c/x + a0 + a1*x; W = -B + w1*x + w2*x**2
lo, lc = lowest(S.expand(E(x, W, S.diff(W, x), A, B, eta)), x)
chk(lo == 1 and S.simplify(lc - B*(eta-w1-S.Rational(3, 4)*c**2)) == 0,
    "C1 origin simple pole: E regular, [x^1]E = B(eta-W'(0)-3c^2/4), a0,a1-free")
p0 = (-3+2*S.sqrt(3))/4
chk(S.simplify(p0**2+S.Rational(3, 2)*p0-S.Rational(3, 16)) == 0, "C1 p0 root")
A = c/x; W = p0*c**2*x - B; e0 = (p0+S.Rational(3, 4))*c**2
chk(S.simplify(E(x, W, S.diff(W, x), A, B, e0)) == 0 and S.simplify(e0 - S.sqrt(3)*c**2/2) == 0
    and S.simplify(S.diff(W, x).subs(x, 0) - (e0 - S.Rational(3, 4)*c**2)) == 0,
    "C1 jet-omitted control: E==0, B eta!=0, W(0)=-B, W'(0)=eta-3c^2/4, A=c/x")
W0 = p0*c**2*x; e1 = p0*c**2
chk(S.simplify(E(x, W0, S.diff(W0, x), A, 0, e1)) == 0 and W0.subs(x, 0) == 0
    and S.simplify(S.diff(W0, x).subs(x, 0) - e1) == 0,
    "C1 B=0 control: E==0, both markings hold, A=c/x still has a pole")

# ---------- Claim 2: scaling with actual polynomials ----------
r, s, h, y, p = S.symbols("r s h y p")
for m in [4, 5]:
    q = 2*m-1
    acs = S.symbols("a0:%d" % (m-1)); wcs = S.symbols("w0:%d" % (q+1))
    A = sum(acs[i]*X**i for i in range(m-1)); W = sum(wcs[i]*X**i for i in range(q+1))
    Wt = s*W.subs(X, r*x); At = h*A.subs(X, r*x)
    lhs = E(x, Wt, S.diff(Wt, x), At, s*B, s*r*eta)
    rhs = s**2*E(X, W, S.diff(W, X), A, B, eta).subs(X, r*x)
    red = S.rem(S.Poly(S.expand(lhs-rhs), h), S.Poly(h**2-s*r**3, h)).as_expr()
    chk(S.expand(red) == 0, "C2 m=%d Etilde(x)=s^2 E(rx) mod h^2=s r^3, generic coefficients" % m)
    lam = h*r**(m-2)*acs[-1]; lcWt = s*r**q*wcs[-1]
    chk(S.simplify((lcWt/lam**2).subs(h**2, s*r**3) - wcs[-1]/acs[-1]**2) == 0,
        "C2 m=%d ratio lcW/lcA^2 preserved" % m)
    chk(S.simplify((s*r**3*r**(2*m-4)).subs({s: 1/B, r: B/eta}) - B**(2*m-2)/eta**(2*m-1)) == 0,
        "C2 m=%d lambda^2 y^2 = B^(2m-2)/eta^(2m-1)" % m)
mS = S.symbols("m", positive=True, integer=True); lamS, eta0 = S.symbols("lambda eta0", nonzero=True)
hval = lamS*y*eta0**(mS-2)
chk(S.simplify((hval**2 - eta0**(-3)).subs(lamS**2, 1/(y**2*eta0**(2*mS-1)))) == 0
    and S.simplify((p*lamS**2*eta0**(2*mS-1)).subs(lamS**2, 1/(y**2*eta0**(2*mS-1))) - p/y**2) == 0,
    "C2 converse: s=1, r=1/eta0, h=lambda y eta0^(m-2) valid iff eta0^q lambda^2 y^2=1; lc W=p/y^2")

# ---------- Claim 3: quadratic model with an ACTUAL A (m=4), not a free Z ----------
f = 3*t*(t-1)
def model(A):
    Z = S.expand(x*A)
    R = S.expand(S.Rational(3, 16)*x*Z**4 - S.Rational(3, 4)*Z**2 - 1)
    Zf = Z.subs(x, f)
    D = S.expand(S.Rational(3, 4)*Zf**2)
    Q = S.expand((t-1)*D - 1)
    tau = S.expand(x*Z**2/4)
    return Z, R, D, Q, tau
b0, b1 = S.symbols("b0 b1")
A = x**2 + b1*x + b0                       # m=4, lambda=1, generic lower coefficients
Z, R, D, Q, tau = model(A)
m = 4; q = 2*m-1
chk(S.degree(R, x) == 2*q-1 and S.degree(Q, t) == 2*q-1 and Q.subs(t, 0) == -1 and Q.subs(t, 1) == -1,
    "C3 deg R = deg Q = 4m-3 = 13, Q(0)=Q(1)=-1")
chk(S.expand(Q - Q.subs(t, 1-t) - (2*t-1)*D) == 0, "C3 Q - sigma Q = (2t-1) D")
chk(S.expand(Q*Q.subs(t, 1-t) + R.subs(x, f)) == 0, "C3 norm identity Q(t)Q(1-t) = -R(f(t)), actual A")
chk(S.rem(S.Poly(Q.subs(t, tau), x), S.Poly(R, x)).is_zero, "C3 phi well defined: Q(tau) = 0 in k[x]/(R)")
chk(S.rem(S.Poly(R.subs(x, f), t), S.Poly(Q, t)).is_zero, "C3 psi well defined: R(f) = 0 in k[t]/(Q)")
chk(S.rem(S.Poly(S.expand(f.subs(t, tau) - x), x), S.Poly(R, x)).is_zero, "C3 phi.psi = id: f(tau) = x mod R")
chk(S.rem(S.Poly(S.expand(tau.subs(x, f) - t), t), S.Poly(Q, t)).is_zero, "C3 psi.phi = id: tau(f(t)) = t mod Q")
# ramification: both directions, and Q'(1/2), and the W-slope quadratic
Zs = S.symbols("Zs")
Rz = S.Rational(3, 16)*x*Zs**4 - S.Rational(3, 4)*Zs**2 - 1
chk(S.expand(Rz.subs(x, -S.Rational(3, 4)) + S.Rational(9, 64)*(Zs**2 + S.Rational(8, 3))**2) == 0,
    "C3 R(-3/4) = -(9/64)(Z(-3/4)^2+8/3)^2: vanishes iff Z(-3/4)^2 = -8/3 (both directions)")
Zp = S.symbols("Zp")
Rp = S.diff(Rz, x) + S.diff(Rz, Zs)*Zp
chk(S.rem(S.Poly(S.expand(Rp.subs(x, -S.Rational(3, 4)) - S.Rational(4, 3)), Zs), S.Poly(Zs**2 + S.Rational(8, 3), Zs)).is_zero,
    "C3 R'(-3/4) = 4/3 whenever R(-3/4)=0, independent of Z'")
Qz = (t-1)*S.Rational(3, 4)*Zs**2 - 1     # Zs stands for Z(f(t)); dZ(f)/dt = Z'(f) f'(t) = 3(2t-1)Zp vanishes at 1/2
Qp = S.diff(Qz, t) + S.diff(Qz, Zs)*3*(2*t-1)*Zp
chk(S.rem(S.Poly(S.expand(Qp.subs(t, S.Rational(1, 2)) + 2), Zs), S.Poly(Zs**2 + S.Rational(8, 3), Zs)).is_zero,
    "C3 Q'(1/2) = -2 whenever Q(1/2)=0")
Wp_ = S.symbols("Wp_")
# at a simple root rho=-3/4 of R lying in W: W'(rho) J(rho) = R'(rho) = 4/3 and J(rho) = 2W'(rho) - 1/rho + (3/2)Z(rho)^2
Jrho = 2*Wp_ - 1/S.Rational(-3, 4) + S.Rational(3, 2)*S.Rational(-8, 3)
chk(S.expand(S.Rational(3, 2)*(Wp_*Jrho - S.Rational(4, 3)) - (3*Wp_**2 - 4*Wp_ - 2)) == 0,
    "C3 W-slope at the ramified root: 3W'^2 - 4W' - 2 = 0")
# codimension-one: the ramified root occurs for actual A; exhibit one (A(-3/4)^2 = -128/27) and check R(-3/4)=0 for it
Aram = x**2 + b1*x + (S.sqrt(-S.Rational(128, 27)) - S.Rational(9, 16) + S.Rational(3, 4)*b1)
chk(S.simplify(model(Aram)[1].subs(x, -S.Rational(3, 4))) == 0, "C3 ramified root realised by an actual degree-2 A (cannot be dropped)")

# ---------- Claim 4: NF correspondence on a concrete factor, DF with actual M, anti-invariance ----------
# concrete instance: A = x^2 - 5/18 gives Z(4/3)=2, so x0=4/3 is a root of R and t0=4/3 a root of Q.
Ac = x**2 - S.Rational(5, 18)
Zc, Rc, Dc, Qc, tauc = model(Ac)
chk(Rc.subs(x, S.Rational(4, 3)) == 0 and Qc.subs(t, S.Rational(4, 3)) == 0 and tauc.subs(x, S.Rational(4, 3)) == S.Rational(4, 3),
    "C4 instance: x0=4/3 root of R, t0=4/3 root of Q, tau(x0)=t0")
W1 = x - S.Rational(4, 3)
M1 = S.gcd(S.Poly(W1.subs(x, f), t), S.Poly(Qc, t)).as_expr()
chk(S.expand(M1 - (t - S.Rational(4, 3))) == 0 and Qc.subs(t, -S.Rational(1, 3)) != 0,
    "C4 instance: divisor of Q selected by the factor W1 is t-4/3 only; 1-t0 is not a Q root")
a1c = M1.subs(t, 0)*M1.subs(t, 1)
chk(S.expand(W1.subs(x, f) - (W1.subs(x, 0)/a1c)*M1*M1.subs(t, 1-t)) == 0,
    "C4 instance: W1(f(t)) = [W1(0)/(M1(0)M1(1))] M1(t) M1(1-t)  (NF with the evaluation constant)")
# DF with an actual polynomial M and actual differentiation; D taken as an actual sigma-invariant polynomial
m0, m1 = S.symbols("m0 m1"); aa = S.symbols("aa", nonzero=True)
n0, n1, d0, d1, d2 = S.symbols("n0 n1 d0 d1 d2")
M = t**2 + m1*t + m0
sM = M.subs(t, 1-t)
V_report = S.diff(M, t)*sM - M*S.diff(M, t).subs(t, 1-t)      # M'(t) sigma M(t) - M(t) M'(1-t), prime = differentiate then substitute
chk(S.expand(V_report - S.diff(M*sM, t)) == 0, "C4 V = d/dt[M sigma M] (prime means differentiate, then substitute)")
Nn = t**2 + n1*t + n0; sN = Nn.subs(t, 1-t)
Dp = d0 + d1*f + d2*f**2                                        # sigma-invariant
Wf = -M*sM/aa; Jf = aa*Nn*sN
Wpf = S.diff(Wf, t)/S.diff(f, t)                                 # chain rule W'(f(t)) = (d/dt W(f))/f'(t)
link = Jf - 2*Wpf + (Wf+1)/f - 2*Dp
rhs = -2*t*(t-1)*V_report + (2*t-1)*(M*sM-aa) + 6*aa*t*(t-1)*(2*t-1)*Dp
lhs = 3*aa**2*t*(t-1)*(2*t-1)*Nn*sN
chk(S.simplify(3*aa*t*(t-1)*(2*t-1)*link - lhs + rhs) == 0, "C4 (DF) == 3a t(t-1)(2t-1) * link, actual polynomials")
DF = S.expand(lhs - rhs)
chk(S.expand(DF + DF.subs(t, 1-t)) == 0, "C4 (DF) is sigma-anti-invariant: DF(1-t) = -DF(t)")
G = S.cancel(DF/(2*t-1))
chk(S.expand(G - G.subs(t, 1-t)) == 0 and S.rem(S.Poly(DF, t), S.Poly(2*t-1, t)).is_zero,
    "C4 (DF) = (2t-1) * G with G sigma-invariant, i.e. G = G0(f(t)): no equations beyond the x-line residual")
# converse bookkeeping: J(0)=1 and W(0)=-1 from Q(0)=Q(1)=-1 alone
Mg = S.symbols("Mg0 Mg1"); Ng = S.symbols("Ng0 Ng1")
# Q(0)=M(0)N(0)=-1, Q(1)=M(1)N(1)=-1 => a N(0)N(1) = M(0)M(1)N(0)N(1) = 1
chk(S.simplify((Mg[0]*Mg[1])*(Ng[0]*Ng[1]) - 1).subs({Ng[0]: -1/Mg[0], Ng[1]: -1/Mg[1]}) == 0 or
    S.simplify(((Mg[0]*Mg[1])*(Ng[0]*Ng[1]) - 1).subs({Ng[0]: -1/Mg[0], Ng[1]: -1/Mg[1]})) == 0,
    "C4 converse: J(0) = a N(0)N(1) = 1 and W(0) = -M(0)M(1)/a = -1 are forced by Q(0)=Q(1)=-1")
# root-swap control scope: A = x^(m-2), m=4,5: R squarefree with >=2 distinct nonzero roots, so W'(0)=sum 1/rho takes >=2 values
for m in [4, 5]:
    Rm = S.expand(S.Rational(3, 16)*x**(4*m-3) - S.Rational(3, 4)*x**(2*m-2) - 1)
    g = S.gcd(S.Poly(Rm, x), S.Poly(S.diff(Rm, x), x))
    chk(g.degree() == 0 and Rm.subs(x, 0) == -1 and S.Poly(Rm, x).coeff_monomial(x**(4*m-4)) == 0,
        "C4 swap control m=%d: R squarefree, R(0)=-1, next-to-leading coefficient 0" % m)
# leading ratio is a consequence, not an extra condition: top of W J = R forces (UT) for p = lcW/lcA^2
lw, la = S.symbols("lw la", nonzero=True); mm = S.symbols("mm")
lcJ = (4*mm-3)*lw + S.Rational(3, 2)*la**2
chk(S.expand((lw*lcJ - S.Rational(3, 16)*la**4) - la**4*((4*mm-3)*(lw/la**2)**2 + S.Rational(3, 2)*(lw/la**2) - S.Rational(3, 16))) == 0,
    "C4 top of WJ=R is (UT) in p=lcW/lcA^2: the leading ratio is forced up to the choice of d-sign")

# history: Xempty §7.3 b=0 quartic map is biquadratic in v and is the composite v -> t=-(4/3)v^2 -> x=3t(t-1)
v = S.symbols("v")
f_xempty_b0 = 4*v**2 + S.Rational(16, 3)*v**4          # Xempty (UR2) f(v) at b=0, B=eta=1
chk(S.expand(f_xempty_b0 - f.subs(t, -S.Rational(4, 3)*v**2)) == 0,
    "HIST Xempty b=0 f(v) = 3t(t-1) with t = -(4/3)v^2: the quadratic model is the even-part reduction of the quartic map")

print("GATE_CONTROLS_PASS count=%d" % N_PASS)
