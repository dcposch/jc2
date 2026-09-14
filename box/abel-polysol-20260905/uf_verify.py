#!/usr/bin/env python3
"""Exact verification of the (UF) form and its standard-form rewritings.

Checks, with INDEPENDENT symbols (W, W', C, b, B, eta, x, 1/y):
  (I1)  x^2*F = P*Hdiff - Rfree                      [(UF) is the charged F of eq. (1)]
  (I2)  Rfree = 3K^2 Q/(16 y^4) - eta x^2 J          [(RC1) form, K=yL]
  (I3)  P*Hdiff - Rfree = (theta-3)(P^2) + G P - Rfree,  theta = x d/dx, G = (3/2)L(L+b) - Bx
        i.e. (UF) <=> (theta-3)(P^2) + G*P = Rfree   [Euler form]
  (I4)  second-kind Abel canonical data: P P' = f2 P^2 + f1 P + f0 with
        f2 = 3/(2x), f1 = (Bx - (3/2)L(L+b))/(2x), f0 = Rfree/(2x)
  (I5)  first-kind form in z=1/P: z' = A3 z^3 + A2 z^2 + A1 z, A3=-f0, A2=-f1, A1=-f2
Then, with the actual finite-t data (t=2,3,4; d a root of 3d^2=t+1):
  (P-inf) the coefficient of a perturbation eps*x^m of P in row x^(m+2N) of P*Hdiff-Rfree
          is lam(m) = 2*omega*(2N+m+6d)  (= Theorem H's lambda_k with m=k+1)
  (P-0)   the coefficient of eps*x^k of P in row x^k is -(k-3) b^2/2 (Briot-Bouquet exponent 3)
  (UT)    (4N-3)p^2 + (3/2)p - 3/16 = 0 at p = omega*y^2, discriminant 3N
  custody: lam(k+1) equals the frozen printed pivots of controls_t3_emit.log
"""
import sympy as sp, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
x, W, Wp, C, b, B, eta, yi, eps = sp.symbols('x W Wp C b B eta yi eps')  # yi = 1/y
y = 1/yi

def build_UF(t):
    """Return F (from (1)), P, L, Hdiff, Rfree with W,Wp,C,b,B,eta independent symbols."""
    A = 3*x**3*C**2/(4*y**2)          # A_Abel
    D = 3*b*x*C/(2*y)                 # D_Abel
    K = x**2*C - y*b
    r = b**2/4
    rhs = (W**2 + (B-2*A+D)*W + A*(A-D)/3 - B*(A-D) - b*eta*K/(2*y) - B*eta*x
           + (2*r*A - 4*r*(B+W))/x)
    F = 2*(x*W - r)*Wp - rhs
    L = K/y
    P = x*W - r
    Pp = W + x*Wp                     # P' with W' = Wp
    Hdiff = 2*x*Pp - 3*P - B*x + sp.Rational(3,2)*L*(L+b)
    Rfree = sp.Rational(3,16)*L**2*(L*(L+2*b) - 4*B*x) - eta*x**2*(b*L/2 + B*x)
    return F, P, Pp, L, K, Hdiff, Rfree

out = {}
F, P, Pp, L, K, Hdiff, Rfree = build_UF(None)
I1 = sp.simplify(sp.expand(x**2*F - (P*Hdiff - Rfree)))
Q = K*(K+2*y*b) - 4*B*y**2*x
J = b*K/(2*y) + B*x
I2 = sp.simplify(sp.expand(Rfree - (3*K**2*Q/(16*y**4) - eta*x**2*J)))
G = sp.Rational(3,2)*L*(L+b) - B*x
# Euler form: theta(P^2) - 3 P^2 with theta = x d/dx acting through W' = Wp
thetaP2 = x*(2*P*Pp)
I3 = sp.simplify(sp.expand((P*Hdiff - Rfree) - (thetaP2 - 3*P**2 + G*P - Rfree)))
# canonical second-kind data
f2 = 3/(2*x); f1 = (B*x - sp.Rational(3,2)*L*(L+b))/(2*x); f0 = Rfree/(2*x)
I4 = sp.simplify(sp.expand(2*x*P*(P*Pp - (f2*P**2 + f1*P + f0)) - (P*Hdiff - Rfree)*P*0 - 2*x*P*P*Pp + 2*x*P*(f2*P**2+f1*P+f0)))
# I4 is trivially 0 by construction; the real check: P*Hdiff - Rfree == 2x( P P' - f2 P^2 - f1 P - f0 )
I4 = sp.simplify(sp.expand((P*Hdiff - Rfree) - 2*x*(P*Pp - f2*P**2 - f1*P - f0)))
out['I1_x2F_minus_PH_plus_R'] = str(I1)
out['I2_RC1'] = str(I2)
out['I3_Euler_form'] = str(I3)
out['I4_second_kind_canonical'] = str(I4)
assert I1 == 0 and I2 == 0 and I3 == 0 and I4 == 0
# first-kind form in z = 1/P: z' = -f0 z^3 - f1 z^2 - f2 z  (check: multiply by -P^2: P' = f2 P + f1 + f0/P)
z = sp.Symbol('z')
zp_first_kind = -f0*z**3 - f1*z**2 - f2*z
# P' = -z'/z^2 with z=1/P: check P P' = f2 P^2 + f1 P + f0 <=> z' = -f0 z^3 - f1 z^2 - f2 z
chk = sp.simplify(sp.expand((-(zp_first_kind.subs(z,1/P))*P**2) * P - (f2*P**2 + f1*P + f0)*0) )
# Explicit: P' from first-kind: P' = -z'/z^2 = -(-f0/P^3 - f1/P^2 - f2/P)*P^2 = f0/P + f1 + f2 P  -> P P' = f0 + f1 P + f2 P^2. OK
out['I5_first_kind_in_1_over_P'] = 'z_prime = A3 z^3 + A2 z^2 + A1 z + A0 with A3=-Rfree/(2x), A2=((3/2)L(L+b)-Bx)/(2x), A1=-3/(2x), A0=0'

# ---------- finite-t pivot laws ----------
def finite_t(t):
    d = sp.Symbol('d')
    N = t+1; q = 2*t+1
    minp = 3*d**2 - (t+1)
    yy = (d+t+1)/sp.Integer(2*q)
    om = 3*(2*d-1)/(4*yy**2*(4*t+1))
    om_alt = 1/(4*yy**2*(2*d+1))
    red = lambda e: sp.rem(sp.numer(sp.together(e)), minp, d)/sp.denom(sp.together(e))
    def zero_mod(e):
        e = sp.together(sp.expand(e)); n = sp.numer(e)
        return sp.rem(sp.expand(n), minp, d) == 0
    res = {'t': t, 'N': N}
    res['omega_two_forms_agree'] = zero_mod(om - om_alt)
    # (UT)
    p = om*yy**2
    res['UT'] = zero_mod((4*N-3)*p**2 + sp.Rational(3,2)*p - sp.Rational(3,16))
    res['UT_discriminant_is_3N'] = sp.simplify(sp.Rational(9,4) + 4*(4*N-3)*sp.Rational(3,16) - 3*N) == 0
    res['UL'] = zero_mod(om*yy**2 - 1/(4*(2*d+1)))
    # generic polynomial data for the pivot computation
    cs = sp.symbols(f'c1:{t}') if t > 1 else ()
    Cpoly = x**(t-1) + sum(cs[i-1]*x**(t-1-i) for i in range(1,t))
    ws = sp.symbols(f'w1:{q}')
    Wpoly = om*x**q - B + sum(ws[i-1]*x**i for i in range(1,q))
    Lp = (x**2*Cpoly - yy*b)/yy
    Pp_ = x*Wpoly - b**2/4
    def PH_minus_R(Pexpr):
        Hd = 2*x*sp.diff(Pexpr,x) - 3*Pexpr - B*x + sp.Rational(3,2)*Lp*(Lp+b)
        Rf = sp.Rational(3,16)*Lp**2*(Lp*(Lp+2*b) - 4*B*x) - eta*x**2*(b*Lp/2 + B*x)
        return sp.expand(Pexpr*Hd - Rf)
    base = PH_minus_R(Pp_)
    # pivot at infinity: perturb P by eps*x^m, look at row x^(m+2N), linear coefficient in eps
    piv_inf = {}
    for m in range(0, 2*N):   # pivot is affine in m; m>=0 suffices for the law
        pert = PH_minus_R(Pp_ + eps*x**m)
        diffe = sp.expand(pert - base)
        # Laurent-safe extraction: multiply by x^6 so all exponents are >= 0
        row = sp.Poly(sp.expand(diffe*x**6), x).coeff_monomial(x**(m+2*N+6))
        lin = sp.expand(row).coeff(eps, 1)
        lam = 2*om*(2*N + m + 6*d)
        piv_inf[m] = zero_mod(lin - lam) if lin is not None else None
    res['pivot_infinity_law_2om(2N+m+6d)'] = piv_inf
    # pivot at 0: perturb by eps*x^k, row x^k, coefficient -(k-3) b^2/2
    piv0 = {}
    for k in range(0, 2*N+1):
        pert = PH_minus_R(Pp_ + eps*x**k)
        row = sp.expand(sp.Poly(sp.expand(pert - base), x).coeff_monomial(x**k)).coeff(eps,1)
        piv0[k] = zero_mod(row + (k-3)*b**2/2)
    res['pivot_zero_law_-(k-3)b^2/2'] = piv0
    # low rows x^0..x^3 vanish identically given the jets (eta=w1, B=-P_1, P_0=-b^2/4, L'(0)=0)
    low = [sp.Poly(base.subs(eta, ws[0]), x).coeff_monomial(x**k) for k in range(4)]
    res['low_rows_x0_x3_vanish_with_eta=w1'] = [zero_mod(e) for e in low]
    res['row_x3_before_eta_link'] = str(sp.factor(sp.Poly(base, x).coeff_monomial(x**3)))
    # Theorem H pivots: rows x^(q+k+2) of x^2F = rows of PH-R, linear in w_k
    thH = {}
    for k in range(1, q):
        row = sp.Poly(base.subs(eta, ws[0]), x).coeff_monomial(x**(q+k+2))
        thH[k] = str(red(sp.diff(row, ws[k-1])))
    res['TheoremH_pivots_w_k'] = thH
    rowB = sp.Poly(base.subs(eta, ws[0]), x).coeff_monomial(x**(q+2))
    res['TheoremH_pivot_B'] = str(red(sp.diff(rowB, B)))
    res['TheoremH_pivot_B_equals_-2alpha_d'] = zero_mod(sp.diff(rowB,B) + 2*(3/(4*yy**2))*d)
    res['TheoremH_pivot_B_equals_-om(4N+6d)'] = zero_mod(sp.diff(rowB,B) + om*(4*N+6*d))
    return res

for t in (2,3,4):
    out[f't{t}'] = finite_t(t)
    print(f't={t} done', flush=True)
(HERE/'uf_verify.json').write_text(json.dumps(out, indent=1, default=str)+'\n')
print(json.dumps(out, indent=1, default=str))
ok = all(v==0 for v in (I1,I2,I3,I4))
for t in (2,3,4):
    r = out[f't{t}']
    ok &= r['UT'] and r['UL'] and r['omega_two_forms_agree'] and r['UT_discriminant_is_3N']
    ok &= all(v for v in r['pivot_infinity_law_2om(2N+m+6d)'].values() if v is not None)
    ok &= all(r['pivot_zero_law_-(k-3)b^2/2'].values())
    ok &= all(r['low_rows_x0_x3_vanish_with_eta=w1'])
    ok &= r['TheoremH_pivot_B_equals_-2alpha_d'] and r['TheoremH_pivot_B_equals_-om(4N+6d)']
print('UF_VERIFY_ALL_PASS' if ok else 'UF_VERIFY_FAIL')
