# K=8,9 lower-band reduction from LEVEL 4 and the K+6 theorem

This note is a derivation aid for the compute lane.  It does not give either
row a verdict.

## 1. Charged facts and scope

Write `L=y-x`.  In the charged tower notation

```text
H = y^(K-1)L,                 h = H + lower total-degree bands,
beta^2 = alpha*h + rho,       f = h^2 + 2 beta,
g = h^3 + 3 beta*h + (3/2) alpha,
E = g^2-f^3.
```

The notation, degree bounds, and ID6 are stated at
`k4ray-degree-tower-opus5-20260903.md:49-68`.  The polynomial identity used
below is

```text
E = beta^3 - 3 rho h^2 - 9 beta rho + (9/4) alpha^2,
```

at `k4ray-degree-tower-opus5-20260903.md:115-137`.  For `K>=7`, MASTER gives a
unique scalar `lambda` such that

```text
deg(E-lambda*f)=K+6,    deg(E)<=2K,
```

with proof at `k4ray-degree-tower-opus5-20260903.md:141-186`.  LEVEL 4 gives

```text
H^2 | beta_b^3,
rho_(3b-2K) = beta_b^3/(3H^2),
deg rho = 3b-2K,
```

at `k4ray-degree-tower-opus5-20260903.md:223-259`.  At the two bottom rows this
already forces `beta_b=mu*y^(K-3)L`; see the explicit K=8,9 list at
`k4ray-degree-tower-opus5-20260903.md:367-385`.

This note applies only to `(K,b)=(8,6),(9,7)`, so put

```text
b=K-2,        r=3b-2K=K-6,       P=beta_b=mu*y^(K-3)L.
```

It is a reduction of those two fixed-`b` charts, not a proof about the other
allowed beta degrees.  The charged source explicitly warns that LEVEL 4 is a
necessary condition, not a kill (`k4ray-degree-tower-opus5-20260903.md:418-424`)
and that free subleading forms obstruct a naive LEVEL-5 inference
(`k4ray-degree-tower-opus5-20260903.md:488-496`).

## 2. Exact formal-quotient recurrence

Use total-degree bands

```text
h_i := [h]_(K-i),       0<=i<=K,        h_0=H,
p_i := [beta]_(b-i),    0<=i<=b,        p_0=P,
```

and set nonexistent `p_i` to zero.  The degree-`K-1` form `h_1` has zero pure
`y^(K-1)` coefficient, matching `h_mons(...,drop_top=True)` in
`pinned_chart.py:83-91,145-171`; the lower `h_i` are full binary forms.
Define

```text
S_n = sum_(a+b=n) h_a h_b,
T_n = sum_(a+b+c=n) p_a p_b p_c.
```

In the homogeneous fraction field let `q=beta^3/h^2` and let `q_n` be its band
of degree `r-n`.  It is safer in the driver not to invert `H`: recursively form

```text
q_0 = P^3/H^2,
N_n = T_n - sum_(i=1..n) S_i q_(n-i),
N_n = H^2 q_n.                                      (REC_n)
```

Every emitted equation is the last equality after denominators from earlier
bands have been cleared.  Neither `y` nor `L` is localized.

Why this is a necessary subsystem: `deg alpha <= 2b-K=K-4` and `deg rho=r`, so

```text
deg(beta*rho) <= b+r = 2K-8,
deg(alpha^2)  <= 2K-8,
deg(lambda*beta) = b = K-2.
```

For K=8,9, `2K-8 < K+6`.  Thus through and including the terminal degree
`K+6`,

```text
E-lambda*f = beta^3 - (3rho+lambda)h^2 + terms of lower degree.
```

Consequently the exact required bands are

```text
q_i = 3 rho_(r-i)       for 0<=i<r,
q_r = 3 rho_0 + lambda  (a scalar),
q_i = 0                 for r<i<2r,
q_(2r) = Theta/H^2,     equivalently N_(2r)=+Theta.
```

The terminal sign is positive and there is no factor 3, 8, or 64 when `p_i`
are beta bands.  The leading form `Theta=[E-lambda*f]_(K+6)` satisfies
`J(H,Theta)=c*x^4*H^2`; its exact solution and scale are at
`k4ray-degree-tower-opus5-20260903.md:188-219`.

Only bands through `2r` are touched: K=8 uses `p_1..p_4,h_1..h_4` and leaves
`p_5,p_6,h_5..h_8` free; K=9 uses `p_1..p_6,h_1..h_6` and leaves
`p_7,h_7..h_9` free.

## 3. Common closed parametrization through q_2

Put `Q=p_1`, `S=p_2`, `U=h_1`, `V=h_2`.  First

```text
q_0 = P^3/H^2 = mu^3*y^(K-7)L = 3 rho_r.
```

The condition that `q_1` be polynomial is exactly

```text
3*y^2*Q - 2*mu*U = 3*y^6*tau,       deg tau=K-7,
q_1 = 3*mu^2*tau.
```

For `q_2`, substituting this equation into `REC_2` first forces

```text
Q = 3*y^4*tau - L*psi.
```

The remaining condition is

```text
y^(K+1) |
  mu*y^(K-3)*S -(2/3)*mu^2*y^(K-5)*V +(1/4)*L*psi^2.       (D2)
```

For K=8 or 9, the first two terms in (D2) are divisible by `y^(K-5)`.
Since `gcd(y,L)=1`, (D2) forces `y^(K-5)|psi^2`, hence `y^2|psi` in both
cases.  Write `psi=y^2*phi` and write the quotient in (D2) as `chi`.  This gives
the pointwise-equivalent parametrization, over characteristic zero and on
`mu!=0`,

```text
deg tau=K-7,       deg phi=K-6,       deg chi=K-8,

p_1 = y^2*(3*y^2*tau-L*phi),
h_1 = (3/mu)*y^6*tau -(3/(2mu))*y^4*L*phi,

h_2 = (3/(2mu^2)) *
      (mu*y^2*p_2 +(1/4)*y^(9-K)*L*phi^2-y^6*chi),

q_1=3mu^2*tau,             q_2=3mu*chi.                 (PIN12)
```

The monic normalization of `h` contributes the one coefficient equation

```text
[y^(K-6)]phi = 2*[y^(K-7)]tau.
```

In a polynomial driver, replace `1/mu` by the existing `mu_inv` and retain
`mu*mu_inv-1`; do not divide by `y` or `L`.  The implication
`y^(K-5)|psi^2 => y^2|psi` is a complete pointwise parametrization, including
`psi=0`.  It is not an ideal-membership claim before radicalization.

The actual remainder still has to be matched.  With `Rh=4rho`, add

```text
K=8: Rh_2=(4/3)mu^3*y*L,      Rh_1=4mu^2*tau,  deg Rh<=2;
K=9: Rh_3=(4/3)mu^3*y^2*L,    Rh_2=4mu^2*tau,
     Rh_1=4mu*chi,             deg Rh<=3.
```

The frozen driver enforces only the top remainder band and the degree bound
(`pinned_chart.py:180-196`); omitting these new lower matches would make the
quotient parametrization a strictly weaker screener.

`PIN12` removes 15 geometric coefficients in either row: K=8 goes from 57 to
42, and K=9 from 73 to 58, before the next band.  The frozen starting counts
are at `k4ray-pinned-chart-gpt55-20260903.md:116-130`.

## 4. K=8 through the terminal band

Here `r=2`, `tau` is linear, `phi` is quadratic, and `chi` is scalar.  The band
requirements are

```text
q_0,q_1 polynomial; q_2 scalar; q_3=0; q_4=Theta_8/H^2.
```

Writing `T=p_3`, `W=h_3`, `REC_3` reduces exactly to

```text
L*phi^3 +36*chi*phi*y^5 -16*mu^3*W*y^2 +24*mu^2*T*y^4
 -12*mu*p_2*phi*y -18*phi^2*tau*y^2 = 0.              (K8-3)
```

The `y^0` coefficient forces `y|phi`.  Put `phi=y*v`, `deg v=1`; then

```text
h_3 = ( L*y*v^3 +36*chi*v*y^4 +24*mu^2*p_3*y^2
        -12*mu*p_2*v -18*v^2*tau*y^2 )/(16mu^3).       (K8-H3)
```

This is polynomial and is equivalent to (K8-3) on `mu!=0`.  It removes one
more coefficient and all six coefficients of `h_3`, taking 57 geometric
parameters to 35 before the terminal band.

For the terminal band use

```text
T_4 = 3P^2*p_4 +6P*p_1*p_3 +3P*p_2^2 +3p_1^2*p_2,
S_2 = 2H*h_2+h_1^2,
S_3 = 2H*h_3+2h_1*h_2,
S_4 = 2H*h_4+2h_1*h_3+h_2^2,
N_4 = T_4-S_2*q_2-S_3*q_1-S_4*q_0 = Theta_8.          (K8-4)
```

With `c=CST=1`,

```text
Theta_8 = y^8*L^2/6630 *
 (195x^4+240x^3y+320x^2y^2+512xy^3+2048y^4).
```

Coefficient RREF of (K8-4) is linear in the five `h_4` coefficients and should
eliminate them while retaining every residual divisibility equation.

## 5. K=9 through the terminal band

Here `r=3`, `tau` is quadratic, `phi` is cubic, and `chi` is linear.  The bands
are

```text
q_0,q_1,q_2 polynomial; q_3=kappa scalar;
q_4=q_5=0; q_6=Theta_9/H^2.
```

`REC_3` is

```text
L*phi^3 +36*chi*phi*y^6 -16*mu^3*h_3*y^4 +24*mu^2*p_3*y^6
 -12*mu*p_2*phi*y^2 -18*phi^2*tau*y^2 = 8*kappa*y^10. (K9-3)
```

Again the constant coefficient forces `phi=y*v`, now with `deg v=2`.  The
remaining low band is precisely

```text
y | v*(L*v^2-12mu*p_2).                                (K9-SPLIT)
```

Since `(y)` is prime, (K9-SPLIT) is covered exactly by the two charts

```text
A: v=y*w, deg w=1;
B: L*v^2-12mu*p_2=y*zeta, deg zeta=4.
```

No localization of `v` is needed; the intersection is harmlessly present in
both charts.  Define

```text
omega = v*(L*v^2-12mu*p_2)/y
      = w*(L*y^2*w^2-12mu*p_2)       on A,
      = v*zeta                        on B.
```

Then all of `h_3` is expressed by

```text
h_3 = (omega+36chi*v*y^3+24mu^2*p_3*y^2
       -18v^2*tau-8kappa*y^6)/(16mu^3).                (K9-H3)
```

For the next two zero bands set

```text
T_4 = 3P^2*p_4+6P*p_1*p_3+3P*p_2^2+3p_1^2*p_2,
S_3 = 2H*h_3+2h_1*h_2,
S_4 = 2H*h_4+2h_1*h_3+h_2^2,
N_4 = T_4-S_1*kappa-S_2*q_2-S_3*q_1-S_4*q_0 = 0;

T_5 = 3P^2*p_5+6P*p_1*p_4+6P*p_2*p_3
      +3p_1^2*p_3+3p_1*p_2^2,
S_5 = 2H*h_5+2h_1*h_4+2h_2*h_3,
N_5 = T_5-S_2*kappa-S_3*q_2-S_4*q_1-S_5*q_0 = 0.      (K9-45)
```

These equations are linear in `h_4` and `h_5`, respectively.  Eliminate their
coefficients by staged coefficient RREF, without dividing by coordinate
monomials.

The terminal band is

```text
T_6 = 3P^2*p_6+6P*p_1*p_5+6P*p_2*p_4+3P*p_3^2
      +3p_1^2*p_4+6p_1*p_2*p_3+p_2^3,
S_6 = 2H*h_6+2h_1*h_5+2h_2*h_4+h_3^2,
N_6 = T_6-S_3*kappa-S_4*q_2-S_5*q_1-S_6*q_0 = Theta_9,

Theta_9 = y^9*L^2/1365 *
 (35x^4+42x^3y+54x^2y^2+81xy^3+243y^4).              (K9-6)
```

The scalar relation is `lambda=kappa-3rho_0`.  In the frozen driver's scaled
variable, `lam=64lambda`, hence `lam=64kappa-48Rh_0`.  For K=8 it is
`lam=192mu*chi-48Rh_0`.

## 6. Map to the frozen driver and proof-scope cautions

The frozen code uses

```text
B=2beta, Al=4alpha, Rh=4rho,
64E = 8B^3-48Rh*h^2-72B*Rh+9Al^2
```

(`k4ray-pinned-chart-gpt55-20260903.md:44-55,90-100`).  Thus substitute
`p_i=B_(b-i)/2`.  Equivalently, a recurrence built from `8B^3/h^2` is 64 times
the beta recurrence: its positive bands equal `48Rh`, its scalar band equals
`48Rh_0+lam`, and its terminal is `64Theta/H^2`.

The present chart imposes `CSTP-1` and only localizes `mu` by
`mu*mu_inv-1` (`k4ray-pinned-chart-gpt55-20260903.md:102-114`).  Therefore the
Theta constants above assume `CST=1` while `mu` remains a variable.  Do not also
set `mu=1`: the displayed grading has only one scaling parameter, with
`w(mu)=K+2` from `pinned_chart.py:148-154`, while `CST` has its own nonzero
weight.  An alternative `mu=1` slice is safe over the algebraic closure only if
`CST` is kept nonzero via a separate Rabinowitsch localizer, in which case every
Theta above must be multiplied by `CST`.

The main ideals are inhomogeneous localizations, so a modular unit remains only
an F_p statement until an exact-Q computation confirms it; the charged report
states this at `k4ray-pinned-chart-gpt55-20260903.md:292-310`.  A POSDIM result
for the quotient screener is not a point of the full Jacobian chart.  Even a
full-chart point is not a counterexample until its reconstructed Jacobian is
checked exactly, per `FALLACY-v2.md:14-21,29-30`.

Finally, the tower shape itself has a charged residual proof obligation:
`a_2=0,a_1=3beta,a_0=(3/2)alpha` is described as normalized but its full
band-by-band induction is not proved at
`k4ray-unsplit-lemma-opus5-20260903.md:125-146`, and the open is restated at
`k4ray-unsplit-lemma-opus5-20260903.md:467-475`.  A conditional chart kill is
not an unconditional census promotion unless that obligation is discharged or
the campaign already has an independent accepted source for the tower form.
