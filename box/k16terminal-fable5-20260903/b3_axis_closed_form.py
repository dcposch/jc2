#!/usr/bin/env python3
"""Closed forms of the terminal rows on the b3-axis (b4=0, q_{<t}=0), symbolic in t.

Weight forcing (wt X=1, wt p=-t, wt b3=t+1) leaves on the axis:
  U = X^q + rho*b3*X^t,  C = X^(t-1),  T = g2 X^t,  S = g1 X^(2t) + sigma*b3*X^(t-1),
  V = X^e + nu1*b3*X^(2t) + nu2*b3^2*X^(t-1),  b1=b2=B0=0.
Then D3 holds by (5.7a); D2 fixes sigma; D1 fixes nu1, nu2; the band-3t row of D0
fixes rho (the q_{t+1} pivot); band 2t-1 gives alpha_t*b3^2; band t-2 gives beta_t*b3^3.
Everything is computed in Q(t)[d]/(3d^2-(t+1)), y=(d+t+1)/(2q).
"""
import sympy as sp
t, d, n = sp.symbols("t d n")
q, e = 2*t+1, 3*t+1
y = (d+t+1)/(2*q)
g1 = sp.Rational(1)*e/q
g2 = e*(d+q)/(2*q**2)
g = e*t*(3*d+2*(t+1))/(6*q**3)
field = sp.QQ.frac_field(t, sp.Symbol("rho"))
mod = sp.Poly(3*d*d-(t+1), d, domain=field)
def red(expr):
    num, den = sp.cancel(sp.together(expr)).as_numer_denom()
    num = sp.Poly(sp.expand(num), d, domain=field).rem(mod)
    den = sp.Poly(sp.expand(den), d, domain=field).rem(mod)
    return sp.factor((num*sp.invert(den, mod)).rem(mod).as_expr())
# unknown axis coefficients
rho, sigma, nu1, nu2 = sp.symbols("rho sigma nu1 nu2")
# D2 (5.7): y(S+2LS') = 3gU' + RT - LRT' + 2LR'T + g b3 (R/L + 5R'/2), coefficient of b3 X^(t-1)
# LHS coefficient: y(2(t-1)+1) sigma = y(2t-1) sigma; RHS: 3 g t rho + g (5t+2)/2
sigma_sol = red((3*g*t*rho + g*(5*t+2)/2)/(y*(2*t-1)))
# D1: 2yX V' = -Q1P1' + Q1'P1 + 2U'P2 (b1=0); coefficients derived in the lane notes
nu1_sol = red(((sigma_sol-g2) + y*q*g1 - 2*q*g + 2*t*rho*g2)/(4*y*t))
nu2_sol = red(t*(y*(sigma_sol-g2) - 2*rho*g)/(2*y*(t-1)))
# D0 band 3t: 2t nu1 - y e - q (sigma-g2) - t rho g1 = 0 -> linear in rho
band3t = red(2*t*nu1_sol - y*e - q*(sigma_sol-g2) - t*rho*g1)
band3t_poly = sp.Poly(sp.expand(sp.together(band3t).as_numer_denom()[0]), rho)
assert band3t_poly.degree() == 1
rho_sol = red(-band3t_poly.coeff_monomial(1)/band3t_poly.coeff_monomial(rho))
pivot_coef = red(band3t_poly.coeff_monomial(rho)/sp.together(band3t).as_numer_denom()[1])
sigma_v = red(sigma_sol.subs(rho, rho_sol)); nu1_v = red(nu1_sol.subs(rho, rho_sol)); nu2_v = red(nu2_sol.subs(rho, rho_sol))
# T_{t,k} = -[X^k] D0 (Sol sign: T = [X^k]E_t, E_t = -(D0 - yg))
alpha = red(-((t-1)*nu2_v - 2*y*t*nu1_v - t*rho_sol*(sigma_v-g2)))
beta = red(y*(t-1)*nu2_v)
def norm_lin(expr):
    """For a + b d in Q(t)[d], return the norm a^2 - b^2 (t+1)/3, factored."""
    p = sp.Poly(sp.expand(sp.together(expr).as_numer_denom()[0]), d)
    den = sp.together(expr).as_numer_denom()[1]
    a0 = p.coeff_monomial(1); a1 = p.coeff_monomial(d)
    return sp.factor(a0**2 - a1**2*(t+1)/3), sp.factor(den)
print("rho (q_{t+1} on axis) =", rho_sol)
print("q_{t+1} pivot coefficient on axis (must match p_Q(t,t+1)) =", pivot_coef)
print("sigma =", sigma_v); print("nu1 =", nu1_v); print("nu2 =", nu2_v)
print("ALPHA_t (b3^2 coefficient of T_{t,2t-1}) =", alpha)
print("  norm numerator, denominator =", norm_lin(alpha))
print("BETA_t (b3^3 coefficient of T_{t,t-2}) =", beta)
print("  norm numerator, denominator =", norm_lin(beta))
# compare with Sol's p_Q closed form at j=t+1
j = sp.Symbol("j")
A_q = 12*t*t+16*t+4-j*(3*t+4); B_q = 2*(t+1)*(j-t)
p_q = -3*t*e*(q-j)*(A_q*d+B_q)/((t+1)*q*(3*t+2)**2*(4*t-2*j+1))
print("p_Q(t,t+1) =", red(p_q.subs(j, t+1)))
print("ratio pivot/p_Q =", red(pivot_coef/p_q.subs(j, t+1)))
# fixed-t checks
for tv in (2,3,4,5,6):
    print("t=%d alpha=%s beta=%s" % (tv, sp.factor(alpha.subs(t,tv)), sp.factor(beta.subs(t,tv))))
