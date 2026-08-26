# Preregistration: D1 double-root toric blow-up

Date: 2026-08-25  
Execution: registered Amazon EC2 only  
Status: source design; no exclusion or lift verdict

## Exact chart

Consume the frozen independent ordinary tails and impose all eight equations

```text
r_l(f,kbar)=Lambda^(12+l)*gamma_l,
gamma_3=mu, gamma_6=nu, gamma_8=1+tau,
gamma_l=0 otherwise.
```

The exact, untruncated substitution is

```text
K=z^3+p*z+c,
p=-3*a^2, c=2*a^3+h,
f=K^3+K*x*Qhat+x^2*Rhat,
Qhat=q2*z^2+q1*z+q0,
Rhat=r2*z^2+r1*z+r0,
x*y=Lambda^6,
Lambda=tau^3*rho,
kbar=x*y*k.
```

The chart is the sole nilpotent valuation survivor with
`0<beta=v(Q)<6`: both `x` and `y` tend to zero, so first saturate by
`x*y*tau*rho`, then take the boundary

```text
x=y=Lambda=tau=rho=0, a=1, h=0.
```

On that boundary impose the complete leading family

```text
Qhat(1)=Qhat(-2)=0,
Qhat'(1)!=0,
27*Rhat(1)=Qhat'(1)^2.
```

All three coefficients of `Rhat` remain variables.  No `Rhat` slice and no
fixed value of `k,mu,nu` is permitted.

## Independent encodings

- A: factored coefficient substitution, global degree order, four sequential
  calls to Singular `sat`, then principal saturation by `Qhat'(1)`.
- B: fully expanded rational rows, `(lp(2),dp(18))` block order, interior
  saturation by an inverse variable and elimination, then a different inverse
  variable and elimination for `Qhat'(1)`.

Each encoding has a pure-boundary negative control and a strict monomial-arc
positive control.  A proof-grade terminal requires rc zero, empty stderr,
exactly one encoding-specific PASS marker, no FAIL marker, frozen input hash,
and agreement of the unit/nonunit verdict between both hosts.

## Adjudication and firewall

- `H=1` in both exact encodings excludes this toric chart for every fixed load.
- `H!=1` is only a survivor in the total polynomial load space.  It does not
  prove a formal lift and may reflect a curve on which `k,mu,nu` vary.
- A nonunit result must be decomposed by its load projection.  A fixed-load
  theorem then requires specialization before saturation or a proof that the
  survivor is vertical over a load point.
- The finite `VDIM=125` exceptional-fibre algebra is navigation only and is
  not a finite-determinacy theorem.
- This chart does not itself prove the preceding Newton-fan classification;
  it consumes that classification as a separately charged mathematical lemma.
